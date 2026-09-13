"""Free machine translation with multi-provider fallback (no API key required).

Why this module exists
----------------------
The project used to translate titles/digests by calling Google's free ``gtx``
endpoint (``translate.googleapis.com/translate_a/single``).  That works from a
home network but is **completely unusable from GitHub Actions**: runners sit on
Azure IP ranges (probe run 2026-09-13 had egress IP ``20.168.103.50``) which
Google has rate-limited.  Measured behaviour from the runner:

================  ==========================================================
endpoint          result
================  ==========================================================
google gtx        ``HTTP 429`` — ``<title>Sorry...</title>`` abuse page (0.31 s)
google web        ``HTTP 302`` → ``google.com/sorry``
deep_translator   ``TooManyRequests`` (single *and* batch)
MyMemory          ``HTTP 200`` → ``你好世界`` (0.82 s)   ← works
Youdao free       ``HTTP 302``
================  ==========================================================

Because the 429 arrives in ~0.3 s and the caller silently swallowed the error,
every title fell back to the original English text — which is exactly why the
WeCom push looked half-Chinese / half-English.

Provider chain (first success wins): MyMemory → Google gtx → Google web.
"""

from __future__ import annotations

import logging
import re
from typing import Callable, Dict, List, Optional

import httpx

logger = logging.getLogger(__name__)

_GOOGLE_GTX = "https://translate.googleapis.com/translate_a/single"
_GOOGLE_WEB = "https://translate.google.com/m"
_MYMEMORY = "https://api.mymemory.translated.net/get"

_CJK = re.compile(r"[\u4e00-\u9fff]")
_KANA = re.compile(r"[\u3040-\u309f\u30a0-\u30ff]")

#: Provider order.  MyMemory first because it is the only one that answers
#: from GitHub Actions / Azure egress IPs.
_PROVIDERS = ("mymemory", "google_gtx", "google_web")

DEFAULT_TIMEOUT = 15.0
_MAX_CHARS = 500  # MyMemory rejects very long `q` values

#: One debug line per provider/reason pair, for the whole process run.
_SEEN_FAILURES: List[str] = []


def has_cjk(text: str) -> bool:
    """Return True when *text* contains Chinese (Han) characters."""
    return bool(_CJK.search(text or ""))


def has_kana(text: str) -> bool:
    """Return True when *text* contains Japanese kana."""
    return bool(_KANA.search(text or ""))


def guess_source(text: str) -> str:
    """Best-effort ISO source language for providers that need it explicit."""
    return "ja" if has_kana(text) else "en"


def needs_translation(text: str, *, min_len: int = 3) -> bool:
    """Return True when *text* is not already Chinese and long enough to bother.

    Text that is already Chinese (Han without kana) is skipped; Japanese text
    is *not* skipped — it is translated to Chinese like everything else.
    """
    if not text or len(text.strip()) < min_len:
        return False
    if has_cjk(text) and not has_kana(text):
        return False
    return True


def _normalize(text: str) -> str:
    return re.sub(r"\s+", " ", text or "").strip()


def _via_mymemory(client: httpx.Client, text: str) -> Optional[str]:
    resp = client.get(
        _MYMEMORY,
        params={"q": text[:_MAX_CHARS], "langpair": f"{guess_source(text)}|zh-CN"},
    )
    if resp.status_code != 200:
        raise RuntimeError(f"HTTP {resp.status_code}")
    data = resp.json()
    out = (data.get("responseData") or {}).get("translatedText") or ""
    # MyMemory echoes the query back when it has no translation for the pair.
    if out.strip().upper() == text.strip().upper():
        return None
    return out or None


def _via_google_gtx(client: httpx.Client, text: str) -> Optional[str]:
    resp = client.get(
        _GOOGLE_GTX,
        params={
            "client": "gtx",
            "sl": "auto",
            "tl": "zh-CN",
            "dt": "t",
            "q": text[:1500],
        },
    )
    if resp.status_code != 200:
        raise RuntimeError(f"HTTP {resp.status_code}")
    data = resp.json()
    return "".join(seg[0] for seg in data[0] if seg and seg[0])


def _via_google_web(client: httpx.Client, text: str) -> Optional[str]:
    resp = client.get(
        _GOOGLE_WEB,
        params={"sl": "auto", "tl": "zh-CN", "q": text[:1500]},
    )
    if resp.status_code != 200:
        raise RuntimeError(f"HTTP {resp.status_code}")
    match = re.search(r'class="result-container">(.*?)</div>', resp.text, re.S)
    return match.group(1).strip() if match else None


_PROVIDER_FUNCS: Dict[str, Callable[[httpx.Client, str], Optional[str]]] = {
    "mymemory": _via_mymemory,
    "google_gtx": _via_google_gtx,
    "google_web": _via_google_web,
}


def _is_good(source: str, candidate: Optional[str]) -> bool:
    """A usable translation is non-empty, changed, and actually Chinese."""
    if not candidate:
        return False
    out = _normalize(candidate)
    return bool(out) and out != _normalize(source) and has_cjk(out)


def _note_failure(provider: str, exc: BaseException) -> None:
    note = f"{provider}/{type(exc).__name__}"
    if note not in _SEEN_FAILURES:
        _SEEN_FAILURES.append(note)
        logger.warning("translation provider unavailable — %s: %s", provider, exc)


def translate(
    text: str,
    client: Optional[httpx.Client] = None,
    *,
    timeout: float = DEFAULT_TIMEOUT,
) -> Optional[str]:
    """Translate *text* into Chinese, or return ``None`` if all providers fail.

    Returning ``None`` (rather than the original text) lets callers keep the
    original title untouched instead of writing an English string into a
    Chinese-only field.
    """
    text = _normalize(text)
    if not needs_translation(text):
        return None

    owns_client = client is None
    if owns_client:
        client = httpx.Client(timeout=timeout)
    try:
        for provider in _PROVIDERS:
            try:
                result = _PROVIDER_FUNCS[provider](client, text)
            except Exception as exc:  # noqa: BLE001 - provider chain, keep going
                _note_failure(provider, exc)
                continue
            if _is_good(text, result):
                return _normalize(result)
        logger.debug("all translation providers failed for: %.60s", text)
        return None
    finally:
        if owns_client:
            client.close()


async def atranslate(
    text: str,
    client: Optional[httpx.AsyncClient] = None,
    *,
    timeout: float = DEFAULT_TIMEOUT,
) -> Optional[str]:
    """Async twin of :func:`translate` for use inside the orchestrator loop."""
    text = _normalize(text)
    if not needs_translation(text):
        return None

    owns_client = client is None
    if owns_client:
        client = httpx.AsyncClient(timeout=timeout)
    try:
        for provider in _PROVIDERS:
            try:
                if provider == "mymemory":
                    resp = await client.get(
                        _MYMEMORY,
                        params={
                            "q": text[:_MAX_CHARS],
                            "langpair": f"{guess_source(text)}|zh-CN",
                        },
                    )
                    if resp.status_code != 200:
                        raise RuntimeError(f"HTTP {resp.status_code}")
                    data = resp.json()
                    out = (data.get("responseData") or {}).get("translatedText") or ""
                    if out.strip().upper() == text.strip().upper():
                        out = ""
                elif provider == "google_gtx":
                    resp = await client.get(
                        _GOOGLE_GTX,
                        params={
                            "client": "gtx",
                            "sl": "auto",
                            "tl": "zh-CN",
                            "dt": "t",
                            "q": text[:1500],
                        },
                    )
                    if resp.status_code != 200:
                        raise RuntimeError(f"HTTP {resp.status_code}")
                    data = resp.json()
                    out = "".join(seg[0] for seg in data[0] if seg and seg[0])
                else:
                    resp = await client.get(
                        _GOOGLE_WEB,
                        params={"sl": "auto", "tl": "zh-CN", "q": text[:1500]},
                    )
                    if resp.status_code != 200:
                        raise RuntimeError(f"HTTP {resp.status_code}")
                    match = re.search(
                        r'class="result-container">(.*?)</div>', resp.text, re.S
                    )
                    out = match.group(1).strip() if match else ""
            except Exception as exc:  # noqa: BLE001 - provider chain, keep going
                _note_failure(provider, exc)
                continue
            if _is_good(text, out):
                return _normalize(out)
        return None
    finally:
        if owns_client:
            await client.aclose()


def translation_health() -> str:
    """Human-readable summary of which providers failed this run."""
    return ", ".join(_SEEN_FAILURES) if _SEEN_FAILURES else "all providers OK"
