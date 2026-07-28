"""Convert Horizon markdown posts to standalone HTML pages.
No Jekyll dependency needed - serves directly as static HTML."""
import os, re, markdown
from datetime import datetime

POSTS_DIR = "docs/_posts"
OUT_DIR = "docs"

def convert_md_to_html(md_text, title=""):
    """Convert markdown to standalone HTML with basic styling."""
    body = markdown.markdown(md_text, extensions=['fenced_code', 'tables'])
    
    html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>{title}</title>
<style>
  * {{ box-sizing: border-box; }}
  body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "PingFang SC", "Microsoft YaHei", sans-serif; background: #f5f6f8; color: #1f2937; margin: 0; padding: 20px; line-height: 1.7; }}
  .container {{ max-width: 800px; margin: 0 auto; background: #fff; padding: 24px 32px; border-radius: 12px; box-shadow: 0 1px 3px rgba(0,0,0,.1); }}
  h1 {{ font-size: 22px; border-bottom: 2px solid #2563eb; padding-bottom: 8px; }}
  h2 {{ font-size: 18px; margin-top: 28px; color: #2563eb; }}
  a {{ color: #2563eb; text-decoration: none; }}
  a:hover {{ text-decoration: underline; }}
  blockquote {{ border-left: 4px solid #2563eb; margin: 12px 0; padding: 8px 16px; background: #f0f4ff; }}
  details {{ border: 1px solid #e2e5ea; border-radius: 8px; padding: 8px 12px; margin: 12px 0; background: #fafafa; }}
  summary {{ cursor: pointer; font-weight: 600; }}
  hr {{ border: none; border-top: 1px solid #e2e5ea; margin: 20px 0; }}
  .star {{ color: #f59e0b; }}
</style>
</head>
<body>
<div class="container">
{body}
</div>
</body>
</html>"""
    return html

for root, dirs, files in os.walk(POSTS_DIR):
    for f in files:
        if f.endswith(".md"):
            path = os.path.join(root, f)
            with open(path, "r", encoding="utf-8") as fh:
                content = fh.read()
            
            # Extract title from front matter
            title_match = re.search(r'title:\s*"([^"]+)"', content)
            title = title_match.group(1) if title_match else f.replace(".md", "")
            
            # Remove front matter
            body = re.sub(r'^---[\s\S]*?---\n*', "", content)
            
            html = convert_md_to_html(body, title)
            
            # Generate output path: YYYY/MM/DD/summary-zh.html
            date_match = re.search(r'(\d{4})-(\d{2})-(\d{2})', f)
            if date_match:
                y, m, d = date_match.groups()
                out_dir = os.path.join(OUT_DIR, y, m, d)
                os.makedirs(out_dir, exist_ok=True)
                lang = "zh" if "zh" in f else "en"
                out_path = os.path.join(out_dir, f"summary-{lang}.html")
            else:
                out_path = path.replace(".md", ".html")
            
            with open(out_path, "w", encoding="utf-8") as fh:
                fh.write(html)
            print(f"  Generated: {out_path}")

print("Done: all posts converted to standalone HTML")
