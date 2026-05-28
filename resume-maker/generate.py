import json
import os
import sys

DESKTOP = os.path.join(os.path.expanduser("~"), "OneDrive", "Desktop")

CSS = '''
@page { size: A4; margin: 10mm 14mm; }
* { margin: 0; padding: 0; box-sizing: border-box; }
body {
  font-family: "Microsoft YaHei", "PingFang SC", "Hiragino Sans GB", sans-serif;
  font-size: 10pt; line-height: 1.7; color: #222;
  max-width: 210mm; margin: 0 auto; padding: 0; background: #fff;
}
.header {
  display: flex; justify-content: space-between; align-items: center;
  margin-bottom: 0; position: relative; z-index: 1;
}
.header-left .name { font-size: 18pt; font-weight: 700; letter-spacing: 2pt; margin-bottom: 2pt; }
.header-left .contact { font-size: 9pt; color: #222; }
.header-right img { width: 72pt; height: 96pt; object-fit: cover; border-radius: 3pt; }
.section { margin-top: 6pt; }
.section-title {
  font-size: 11pt; font-weight: 700; border-bottom: 1pt solid #000;
  padding-bottom: 2pt; margin-bottom: 5pt; letter-spacing: 1pt;
}
.entry { margin-bottom: 6pt; }
.entry-header { display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 2pt; }
.entry-title { font-size: 10.5pt; font-weight: 700; }
.entry-meta { font-size: 8.5pt; color: #222; white-space: nowrap; }
.entry-subtitle { font-size: 9pt; color: #222; font-style: italic; margin-bottom: 3pt; }
ul { padding-left: 1.4em; margin: 2pt 0; }
li { margin-bottom: 1.5pt; }
.reflection {
  background: #f9f9f9; border-left: 3pt solid #bbb;
  padding: 6pt 10pt; margin-top: 6pt; font-size: 9.5pt; color: #222;
}
.skill-group { margin-bottom: 4pt; }
.skill-label { font-weight: 700; display: inline; }
.skill-text { color: #222; }
.highlight-card {
  background: #f6f6f6; border-radius: 4pt; padding: 10pt 12pt; margin-top: 6pt;
}
.highlight-card p { margin-bottom: 3pt; }
.highlight-card .label { font-weight: 700; }
@media print { body { padding: 0; margin: 0; } }
'''


def escape(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def render_header(data):
    has_photo = bool(data.get("photo"))
    header_style = 'margin-bottom: -20pt;' if has_photo else ''
    lines = [f'<div class="header" style="{header_style}">', '<div class="header-left">']
    lines.append(f'<div class="name">{escape(data["name"])}</div>')
    lines.append('<div class="contact">')
    lines.append(f'电话：{escape(data["phone"])} &nbsp;|&nbsp; 邮箱：{escape(data["email"])}')
    lines.append('</div></div>')
    if data.get("photo"):
        lines.append('<div class="header-right">')
        lines.append(f'<img src="{escape(data["photo"])}" alt="照片">')
        lines.append('</div>')
    lines.append('</div>')
    return '\n'.join(lines)


def render_education(entries):
    lines = ['<div class="section">', '<div class="section-title">教育背景</div>', '<div class="entry">']
    for e in entries:
        lines.append('<div class="entry-header">')
        lines.append(f'<span class="entry-title">{escape(e["school"])} · {escape(e["major"])} · {escape(e["degree"])}</span>')
        lines.append(f'<span class="entry-meta">{escape(e["years"])}</span>')
        lines.append('</div>')
    lines.append('</div></div>')
    return '\n'.join(lines)


def render_projects(projects):
    lines = ['<div class="section">', '<div class="section-title">项目经历</div>']
    for p in projects:
        lines.append('<div class="entry">')
        lines.append('<div class="entry-header">')
        lines.append(f'<span class="entry-title">{escape(p["name"])}</span>')
        lines.append(f'<span class="entry-meta">{escape(p["role_time"])}</span>')
        lines.append('</div>')
        if p.get("tech_stack"):
            lines.append(f'<div class="entry-subtitle">{escape(p["tech_stack"])}</div>')
        if p.get("overview"):
            lines.append(f'<p style="margin-bottom:3pt;">{escape(p["overview"])}</p>')
        if p.get("bullets"):
            lines.append('<ul>')
            for b in p["bullets"]:
                lines.append(f'<li><strong>{escape(b["label"])}：</strong>{escape(b["content"])}</li>')
            lines.append('</ul>')
        lines.append('</div>')
    lines.append('</div>')
    return '\n'.join(lines)


def render_work(work_entries):
    lines = ['<div class="section">', '<div class="section-title">工作经历</div>']
    for w in work_entries:
        lines.append('<div class="entry">')
        lines.append('<div class="entry-header">')
        lines.append(f'<span class="entry-title">{escape(w["company"])} | {escape(w["title"])}</span>')
        lines.append(f'<span class="entry-meta">{escape(w["years"])}</span>')
        lines.append('</div>')
        if w.get("bullets"):
            lines.append('<ul>')
            for b in w["bullets"]:
                lines.append(f'<li><strong>{escape(b["label"])}：</strong>{escape(b["content"])}</li>')
            lines.append('</ul>')
        if w.get("reflection"):
            lines.append(f'<div class="reflection"><strong>个人思考：</strong>{escape(w["reflection"])}</div>')
        lines.append('</div>')
    lines.append('</div>')
    return '\n'.join(lines)


def render_skills(skills):
    lines = ['<div class="section">', '<div class="section-title">技能</div>']
    for s in skills:
        lines.append('<div class="skill-group">')
        lines.append(f'<span class="skill-label">{escape(s["label"])}：</span>')
        lines.append(f'<span class="skill-text">{escape(s["content"])}</span>')
        lines.append('</div>')
    lines.append('</div>')
    return '\n'.join(lines)


def render_extra(sections):
    if not sections:
        return ''
    lines = []
    for sec in sections:
        lines.append('<div class="section">')
        lines.append(f'<div class="section-title">{escape(sec["title"])}</div>')
        if sec.get("content"):
            lines.append(f'<p>{escape(sec["content"])}</p>')
        if sec.get("card_items"):
            lines.append('<div class="highlight-card">')
            for item in sec["card_items"]:
                lines.append(f'<p><span class="label">{escape(item["label"])}</span>——{escape(item["text"])}</p>')
            lines.append('</div>')
        lines.append('</div>')
    return '\n'.join(lines)


def generate():
    config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "template_config.json")
    with open(config_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    sections = [
        render_header(data),
        render_education(data.get("education", [])),
        render_projects(data.get("projects", [])),
        render_work(data.get("work", [])),
        render_skills(data.get("skills", [])),
        render_extra(data.get("extra_sections", [])),
    ]

    body = '\n'.join(sections)
    html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<title>简历 - {escape(data["name"])}</title>
<style>{CSS}</style>
</head>
<body>
{body}
</body>
</html>'''

    # Write HTML to desktop
    html_path = os.path.join(DESKTOP, "简历.html")
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html)

    # Generate PDF
    try:
        from playwright.sync_api import sync_playwright
        pdf_path = os.path.join(DESKTOP, "简历.pdf")
        file_url = "file:///" + html_path.replace("\\", "/")
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            page.goto(file_url, wait_until="networkidle")
            page.pdf(path=pdf_path, format="A4", print_background=True)
            browser.close()
        print(f"PDF saved: {pdf_path}")
    except ImportError:
        print("Warning: playwright not installed. Run: pip install playwright && playwright install chromium")
    except Exception as e:
        print(f"PDF generation failed: {e} (HTML saved OK)")

    print(f"HTML saved: {html_path}")


if __name__ == "__main__":
    generate()
