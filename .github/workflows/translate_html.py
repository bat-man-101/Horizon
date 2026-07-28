"""Machine translate generated Horizon HTML files to Chinese using Google Translate.
Translates English, Japanese and other languages to Chinese."""
import os, re
from deep_translator import GoogleTranslator

translator = GoogleTranslator(source='auto', target='zh-CN')

HAS_CJK = re.compile(r'[\u4e00-\u9fff]')       # Chinese characters
HAS_KANA = re.compile(r'[\u3040-\u309f\u30a0-\u30ff]')  # Japanese hiragana/katakana

def needs_translate(text):
    """Return True if text needs translation (English, Japanese, or mixed)."""
    if not text or len(text) < 3:
        return False
    has_cjk = bool(HAS_CJK.search(text))
    has_kana = bool(HAS_KANA.search(text))
    if has_cjk and not has_kana:
        return False  # Already Chinese (or mixed CJK like "AI 新闻")
    if has_kana:
        return True   # Japanese text needs translation
    return True       # No CJK at all = English/others

def translate_title(title):
    if not needs_translate(title):
        return title
    try:
        result = translator.translate(title)
        if result and result != title:
            return result
    except:
        pass
    return title

summary_dir = 'docs'
for root, dirs, files in os.walk(summary_dir):
    for f in files:
        if f.endswith('.md') or f.endswith('.html'):
            path = os.path.join(root, f)
            with open(path, 'r', encoding='utf-8', errors='replace') as fh:
                content = fh.read()

            # Translate markdown headings
            def trans_heading(m):
                prefix = m.group(1)  # ## 
                orig = m.group(2)
                t = translate_title(orig)
                return f'{prefix}{t}' if t != orig else m.group(0)
            content = re.sub(r'^(#{1,4}\s+)(.+)$', trans_heading, content, flags=re.MULTILINE)

            # Translate markdown links [title](url) - the title part
            def trans_link(m):
                orig = m.group(1)
                url = m.group(2)
                t = translate_title(orig)
                return f'[{t}]({url})' if t != orig else m.group(0)
            content = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', trans_link, content)

            # Translate bold text **title**
            def trans_bold(m):
                t = translate_title(m.group(1))
                return f'**{t}**' if t != m.group(1) else m.group(0)
            content = re.sub(r'\*\*(.*?)\*\*', trans_bold, content)

            with open(path, 'w', encoding='utf-8') as fh:
                fh.write(content)
            print(f'  Translated: {path}')
print('Done: all HTML files translated')
