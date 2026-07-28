"""Machine translate generated Horizon HTML files to Chinese using Google Translate.
Translates English, Japanese and other languages to Chinese.
Phase 1: Translate markdown headings/links/bold (for intermediate .md files)
Phase 2: Translate all visible text in final HTML files"""
import os, re
from html.parser import HTMLParser
from deep_translator import GoogleTranslator

translator = GoogleTranslator(source='auto', target='zh-CN')

HAS_CJK = re.compile(r'[\u4e00-\u9fff]')       # Chinese characters
HAS_KANA = re.compile(r'[\u3040-\u309f\u30a0-\u30ff]')  # Japanese hiragana/katakana

def needs_translate(text):
    """Return True if text needs translation."""
    if not text or len(text) < 3:
        return False
    has_cjk = bool(HAS_CJK.search(text))
    has_kana = bool(HAS_KANA.search(text))
    if has_cjk and not has_kana:
        return False
    if has_kana:
        return True
    return True

def translate_text(text):
    if not needs_translate(text):
        return text
    try:
        result = translator.translate(text)
        if result and result != text:
            return result
    except:
        pass
    return text

# ─── Phase 1: Markdown translation (headings, links, bold) ───
summary_dir = 'docs'
for root, dirs, files in os.walk(summary_dir):
    for f in files:
        if f.endswith('.md'):
            path = os.path.join(root, f)
            with open(path, 'r', encoding='utf-8', errors='replace') as fh:
                content = fh.read()

            # Translate markdown headings
            def trans_heading(m):
                prefix = m.group(1)
                orig = m.group(2)
                t = translate_text(orig)
                return f'{prefix}{t}' if t != orig else m.group(0)
            content = re.sub(r'^(#{1,4}\s+)(.+)$', trans_heading, content, flags=re.MULTILINE)

            # Translate markdown links [title](url)
            def trans_link(m):
                orig = m.group(1)
                url = m.group(2)
                t = translate_text(orig)
                return f'[{t}]({url})' if t != orig else m.group(0)
            content = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', trans_link, content)

            # Translate bold text **text**
            def trans_bold(m):
                t = translate_text(m.group(1))
                return f'**{t}**' if t != m.group(1) else m.group(0)
            content = re.sub(r'\*\*(.*?)\*\*', trans_bold, content)

            with open(path, 'w', encoding='utf-8') as fh:
                fh.write(content)
            print(f'  MD translated: {path}')

# ─── Phase 2: Full HTML text translation ───
# Strategy: use html.parser to identify text nodes, translate, rebuild.

class HTMLTranslatorParser(HTMLParser):
    """HTML Parser that collects text nodes with their translated versions."""
    def __init__(self):
        super().__init__()
        self.result = []
        self._skip_tags = {'script', 'style', 'code', 'pre'}
        self._skip_depth = 0

    def handle_starttag(self, tag, attrs):
        if tag in self._skip_tags:
            self._skip_depth += 1
        # Rebuild the tag as-is
        attr_str = ''
        for k, v in attrs:
            if v is None:
                attr_str += f' {k}'
            else:
                v_esc = v.replace('"', '&quot;')
                attr_str += f' {k}="{v_esc}"'
        self.result.append(f'<{tag}{attr_str}>')

    def handle_endtag(self, tag):
        if tag in self._skip_tags:
            self._skip_depth -= 1
        self.result.append(f'</{tag}>')

    def handle_startendtag(self, tag, attrs):
        attr_str = ''
        for k, v in attrs:
            if v is None:
                attr_str += f' {k}'
            else:
                v_esc = v.replace('"', '&quot;')
                attr_str += f' {k}="{v_esc}"'
        self.result.append(f'<{tag}{attr_str}/>')

    def handle_data(self, data):
        if self._skip_depth > 0:
            self.result.append(data)
            return
        text = data.strip()
        if text and len(text) >= 5 and re.search(r'[a-zA-Z]', text) and needs_translate(text):
            translated = translate_text(text)
            if translated and translated != text:
                # Preserve original whitespace wrapping
                leading = len(data) - len(data.lstrip())
                trailing = len(data) - len(data.rstrip())
                ws = data[:leading] if leading else ''
                we = data[-trailing:] if trailing else ''
                self.result.append(f'{ws}{translated}{we}')
                return
        self.result.append(data)

    def handle_entityref(self, name):
        self.result.append(f'&{name};')

    def handle_charref(self, name):
        self.result.append(f'&#{name};')

    def handle_comment(self, data):
        self.result.append(f'<!--{data}-->')

    def handle_decl(self, decl):
        self.result.append(f'<!{decl}>')

def translate_html_file(path):
    with open(path, 'r', encoding='utf-8', errors='replace') as fh:
        html_content = fh.read()

    parser = HTMLTranslatorParser()
    try:
        parser.feed(html_content)
    except Exception as e:
        print(f'  WARN: parse error in {path}: {e}')
        return

    new_html = ''.join(parser.result)
    if new_html != html_content:
        with open(path, 'w', encoding='utf-8') as fh:
            fh.write(new_html)
        print(f'  HTML translated: {path}')

for root, dirs, files in os.walk(summary_dir):
    for f in files:
        if f.endswith('.html') and not f.endswith('index.html'):
            translate_html_file(os.path.join(root, f))

print('Done: all files translated')
