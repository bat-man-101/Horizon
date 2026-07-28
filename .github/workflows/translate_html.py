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
        if f.endswith('.html'):
            path = os.path.join(root, f)
            with open(path, 'r', encoding='utf-8') as fh:
                content = fh.read()

            def trans_title_tag(m):
                return '<title>' + translate_title(m.group(1)) + '</title>'
            content = re.sub(r'<title>(.*?)</title>', trans_title_tag, content)

            for tag in ['h1', 'h2', 'h3', 'h4']:
                def make_trans(t=tag):
                    def trans_h(m):
                        orig = m.group(1)
                        t2 = translate_title(orig)
                        return f'<{t}>{t2}</{t}>' if t2 != orig else m.group(0)
                    return trans_h
                content = re.sub(f'<{tag}>(.*?)</{tag}>', make_trans(), content)

            # Translate <a> anchor text (item titles)
            def trans_a(m):
                t = translate_title(m.group(1))
                return f'>{t}<' if t != m.group(1) else m.group(0)
            content = re.sub(r'>([^<]{4,})</a>', trans_a, content)

            # Translate <li> text that looks like item titles (数字. text)
            def trans_li(m):
                t = translate_title(m.group(1))
                return f'{t}</li>' if t != m.group(1) else m.group(0)
            content = re.sub(r'<li>([^<]{4,}?)</li>', trans_li, content)

            def trans_bold(m):
                t = translate_title(m.group(1))
                return f'**{t}**' if t != m.group(1) else m.group(0)
            content = re.sub(r'\*\*(.*?)\*\*', trans_bold, content)

            with open(path, 'w', encoding='utf-8') as fh:
                fh.write(content)
            print(f'  Translated: {path}')
print('Done: all HTML files translated')
