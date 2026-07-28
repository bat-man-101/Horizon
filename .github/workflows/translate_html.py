"""Machine translate generated Horizon HTML files to Chinese using Google Translate."""
import os, re
from deep_translator import GoogleTranslator

translator = GoogleTranslator(source='en', target='zh-CN')

def translate_title(title):
    if not title or re.search(r'[\u4e00-\u9fff]', title):
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

            def trans_bold(m):
                t = translate_title(m.group(1))
                return f'**{t}**' if t != m.group(1) else m.group(0)
            content = re.sub(r'\*\*(.*?)\*\*', trans_bold, content)

            with open(path, 'w', encoding='utf-8') as fh:
                fh.write(content)
            print(f'  Translated: {path}')
print('Done: all HTML files translated')
