"""Machine translate generated Horizon HTML/Markdown to Chinese.

Uses the shared multi-provider translator in ``src/ai/translate.py``.  When
``LIBRETRANSLATE_URL`` is configured the **self-hosted LibreTranslate instance
on the NAS** is tried first — it is unlimited, so full-text (body) translation
is affordable; otherwise the chain falls back to MyMemory → Google gtx → web.

Phase 1: translate markdown headings / link titles / bold (intermediate .md).
Phase 2: translate visible text nodes in the standalone HTML — now including
long article bodies (previously skipped above 120 chars).

A global cap (``TRANSLATE_MAX``, default 2000 strings) guards against runaway
costs when only quota-limited public providers are available.  Strings are
translated at most once per run.
"""

import os
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from src.ai.translate import (  # noqa: E402
    needs_translation,
    translate,
    translation_health,
)

MAX_TRANSLATIONS = int(os.environ.get("TRANSLATE_MAX", "2000"))
MAX_TEXT_LEN = int(os.environ.get("TRANSLATE_MAX_LEN", "2000"))
_SELF_HOSTED = bool((os.environ.get("LIBRETRANSLATE_URL") or "").strip())

_stats = {"done": 0, "cached": 0, "skipped": 0}
_cache: dict[str, str] = {}


def translate_text(text: str) -> str:
    """Return a Chinese translation of *text*, or *text* unchanged on failure."""
    if _stats["done"] + _stats["cached"] >= MAX_TRANSLATIONS:
        return text
    if text in _cache:
        _stats["cached"] += 1
        return _cache[text]
    if not needs_translation(text):
        return text
    result = translate(text)
    if result:
        _cache[text] = result
        _stats["done"] += 1
        return result
    return text


# ─── Phase 1: Markdown translation (headings, links, bold) ───
summary_dir = "docs"
for root, dirs, files in os.walk(summary_dir):
    for f in files:
        if not f.endswith(".md"):
            continue
        path = os.path.join(root, f)
        with open(path, "r", encoding="utf-8", errors="replace") as fh:
            content = fh.read()
        original = content

        def trans_heading(m):
            prefix = m.group(1)
            orig = m.group(2)
            t = translate_text(orig)
            return f"{prefix}{t}" if t != orig else m.group(0)

        content = re.sub(
            r"^(#{1,4}\s+)(.+)$", trans_heading, content, flags=re.MULTILINE
        )

        def trans_link(m):
            orig = m.group(1)
            url = m.group(2)
            t = translate_text(orig)
            return f"[{t}]({url})" if t != orig else m.group(0)

        content = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", trans_link, content)

        def trans_bold(m):
            t = translate_text(m.group(1))
            return f"**{t}**" if t != m.group(1) else m.group(0)

        content = re.sub(r"\*\*(.*?)\*\*", trans_bold, content)

        if content != original:
            with open(path, "w", encoding="utf-8") as fh:
                fh.write(content)
            print(f"  MD translated: {path}")


# ─── Phase 2: HTML visible-text translation ───
class HTMLTranslatorParser(HTMLParser):
    """Collect text nodes, translate them, rebuild the document."""

    def __init__(self):
        super().__init__()
        self.result = []
        self._skip_tags = {"script", "style", "code", "pre"}
        self._skip_depth = 0

    @staticmethod
    def _attrs(attrs):
        attr_str = ""
        for k, v in attrs:
            if v is None:
                attr_str += f" {k}"
            else:
                attr_str += f' {k}="{v.replace(chr(34), "&quot;")}"'
        return attr_str

    def handle_starttag(self, tag, attrs):
        if tag in self._skip_tags:
            self._skip_depth += 1
        self.result.append(f"<{tag}{self._attrs(attrs)}>")

    def handle_endtag(self, tag):
        if tag in self._skip_tags:
            self._skip_depth -= 1
        self.result.append(f"</{tag}>")

    def handle_startendtag(self, tag, attrs):
        self.result.append(f"<{tag}{self._attrs(attrs)}/>")

    def handle_data(self, data):
        if self._skip_depth > 0:
            self.result.append(data)
            return
        text = data.strip()
        if (
            text
            and 5 <= len(text) <= MAX_TEXT_LEN
            and re.search(r"[a-zA-Z]", text)
            and needs_translation(text)
        ):
            translated = translate_text(text)
            if translated and translated != text:
                leading = len(data) - len(data.lstrip())
                trailing = len(data) - len(data.rstrip())
                ws = data[:leading] if leading else ""
                we = data[-trailing:] if trailing else ""
                self.result.append(f"{ws}{translated}{we}")
                return
        self.result.append(data)

    def handle_entityref(self, name):
        self.result.append(f"&{name};")

    def handle_charref(self, name):
        self.result.append(f"&#{name};")

    def handle_comment(self, data):
        self.result.append(f"<!--{data}-->")

    def handle_decl(self, decl):
        self.result.append(f"<!{decl}>")


def translate_html_file(path):
    with open(path, "r", encoding="utf-8", errors="replace") as fh:
        html_content = fh.read()

    parser = HTMLTranslatorParser()
    try:
        parser.feed(html_content)
    except Exception as e:
        print(f"  WARN: parse error in {path}: {e}")
        return

    new_html = "".join(parser.result)
    if new_html != html_content:
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(new_html)
        print(f"  HTML translated: {path}")


for root, dirs, files in os.walk(summary_dir):
    for f in files:
        if f.endswith(".html") and not f.endswith("index.html"):
            translate_html_file(os.path.join(root, f))

print(
    f"Done: {_stats['done']} translated, {_stats['cached']} cached, "
    f"cap={MAX_TRANSLATIONS}, max_len={MAX_TEXT_LEN}, "
    f"self_hosted={_SELF_HOSTED} | providers: {translation_health()}"
)
