import json
import os

DESKTOP = os.path.join(os.path.expanduser("~"), "OneDrive", "Desktop")

CSS = '''
@page { size: A4 portrait; margin: 0; }
* { margin: 0; padding: 0; box-sizing: border-box; }
body {
  font-family: "Microsoft YaHei", "PingFang SC", "Hiragino Sans GB", sans-serif;
  font-size: 11pt; line-height: 1.7; color: #333; font-weight: 600;
  background: #f0e6d8; overflow: hidden;
}
.page {
  display: flex; width: 210mm; height: 297mm; margin: 0 auto;
  position: relative;
}

/* Decorative elements */
.dec-dot {
  position: absolute;
  width: 8mm; height: 8mm;
  border-radius: 50%;
  background: #e8967a; opacity: 0.08;
  z-index: 0; pointer-events: none;
}
.dec-dot-1 { top: 8mm; right: 15mm; width: 18mm; height: 18mm; opacity: 0.1; }
.dec-dot-2 { top: 30mm; right: 5mm; width: 10mm; height: 10mm; opacity: 0.12; }
.dec-dot-3 { bottom: 22mm; right: 20mm; width: 12mm; height: 12mm; opacity: 0.08; }
.dec-dot-4 { bottom: 5mm; right: 5mm; width: 6mm; height: 6mm; opacity: 0.12; }

/* ===== LEFT SIDEBAR ===== */
.sidebar {
  width: 60mm; height: 297mm; background: #f5ede0;
  padding: 9mm 6mm 3mm 6mm;
  display: flex; flex-direction: column;
  border-right: 1.5px solid #e8967a;
  flex-shrink: 0; z-index: 1;
}

/* Photo */
.sidebar .photo-wrap {
  text-align: center; margin-bottom: 5mm;
}
.sidebar .photo-circle {
  width: 36mm; height: 36mm; border-radius: 50%;
  border: 3px solid #e8967a; overflow: hidden;
  margin: 0 auto; display: inline-block;
  background: #fff;
}
.sidebar .photo-circle img {
  width: 100%; height: 100%; object-fit: cover;
  object-position: center top;
}

/* Sidebar sections */
.sidebar .sb-section { margin-bottom: 4mm; }
.sidebar .sb-title {
  font-size: 11pt; font-weight: 700; color: #333;
  border-bottom: 2px solid #e8967a;
  padding-bottom: 2pt; margin-bottom: 3pt;
  display: flex; align-items: center; gap: 3pt;
}
.sidebar .sb-title .icon {
  width: 14pt; height: 14pt; flex-shrink: 0;
  display: inline-flex; align-items: center; justify-content: center;
}
.sidebar .sb-item {
  font-size: 10pt; font-weight: 600; color: #444;
  margin-bottom: 1.5pt; line-height: 1.55;
}
.sidebar .sb-item .label { color: #666; margin-right: 2pt; font-weight: 700; }

/* Self evaluation paragraph in sidebar */
.sidebar .eval-text {
  font-size: 10pt; font-weight: 600; color: #444;
  line-height: 1.65; text-indent: 2em; margin-top: 2pt;
}

/* Certificates */
.cert-list { list-style: none; padding: 0; }
.cert-list li {
  font-size: 10pt; font-weight: 600; color: #444; margin-bottom: 2pt;
  padding-left: 10pt; position: relative; line-height: 1.55;
}
.cert-list li::before {
  content: ""; position: absolute; left: 0; top: 7pt;
  width: 5pt; height: 5pt; border-radius: 50%;
  background: #e8967a;
}

/* ===== RIGHT MAIN ===== */
.main {
  flex: 1; height: 297mm; padding: 9mm 10mm 3mm 8mm;
  display: flex; flex-direction: column;
  position: relative; z-index: 1;
  background: #f0e6d8;
}

/* Header */
.main-header { margin-bottom: 3.5mm; }
.main-header .name {
  font-size: 24pt; font-weight: 700; color: #222;
  letter-spacing: 4pt; margin-bottom: 2pt;
}
.main-header .job-obj {
  font-size: 12pt; color: #555; font-weight: 700; margin-bottom: 1pt;
}
.main-header .salary {
  font-size: 11pt; color: #e8967a; font-weight: 700;
}

/* Section header bar */
.section-header {
  background: #e8967a; color: #fff;
  font-size: 12pt; font-weight: 700;
  padding: 3pt 12pt 3pt 8pt;
  margin-bottom: 5pt; margin-left: -2pt;
  display: flex; align-items: center; gap: 4pt;
  border-radius: 0 3pt 3pt 0;
  line-height: 1.4;
}
.section-header .sh-icon {
  width: 14pt; height: 14pt; flex-shrink: 0;
  display: inline-flex; align-items: center; justify-content: center;
}

/* Content sections */
.section-content { margin-bottom: 4mm; }

/* Work experience items */
.work-entry { margin-bottom: 5pt; }
.work-entry-header {
  display: flex; justify-content: space-between; align-items: baseline;
  margin-bottom: 2pt;
}
.work-entry-period {
  font-size: 11pt; font-weight: 700; color: #e8967a;
  white-space: nowrap;
}
.work-entry-title {
  font-size: 11pt; font-weight: 700; color: #333;
  flex: 1; text-align: center;
}
.work-entry-desc {
  font-size: 10.5pt; font-weight: 600; color: #444;
  line-height: 1.65; text-indent: 2em;
}

/* Skills section */
.skill-category {
  font-size: 11pt; font-weight: 700; color: #e8967a;
  margin-top: 4pt; margin-bottom: 2pt;
  display: flex; align-items: center; gap: 3pt;
}
.skill-category .sc-dot {
  width: 6pt; height: 6pt; border-radius: 50%;
  background: #e8967a; flex-shrink: 0;
}
.skill-desc {
  font-size: 10.5pt; font-weight: 600; color: #444;
  line-height: 1.7; margin-bottom: 2pt;
  padding-left: 2em;
}

/* Work photos grid */
.photos-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  grid-template-rows: repeat(3, 1fr);
  gap: 3pt;
  margin-top: 3mm;
}
.photos-grid img {
  width: 100%; height: 100%;
  object-fit: cover;
  border-radius: 2pt;
  aspect-ratio: 4/3;
}

@media print {
  body { padding: 0; margin: 0; }
  .page { box-shadow: none; }
}
'''

# SVG icons
ICON_PERSON = "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='%23e8967a' width='14' height='14'%3E%3Cpath d='M12 12c2.7 0 4.8-2.1 4.8-4.8S14.7 2.4 12 2.4 7.2 4.5 7.2 7.2 9.3 12 12 12zm0 2.4c-3.2 0-9.6 1.6-9.6 4.8v1.2c0 .7.5 1.2 1.2 1.2h16.8c.7 0 1.2-.5 1.2-1.2v-1.2c0-3.2-6.4-4.8-9.6-4.8z'/%3E%3C/svg%3E"
ICON_WORK = "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='white' width='14' height='14'%3E%3Cpath d='M20 6h-4V4c0-1.1-.9-2-2-2h-4c-1.1 0-2 .9-2 2v2H4c-1.1 0-2 .9-2 2v11c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V8c0-1.1-.9-2-2-2zm-6 0h-4V4h4v2z'/%3E%3C/svg%3E"
ICON_SKILL = "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='white' width='14' height='14'%3E%3Cpath d='M20.57 14.86L22 13.43 20.57 12 17 15.57 8.43 7 12 3.43 10.57 2 9.14 3.43 7.71 2 5.57 4.14 4.14 2.71 2.71 4.14l1.43 1.43L2 7.71l1.43 1.43L2 10.57 3.43 12 7 8.43 15.57 17 12 20.57 13.43 22l1.43-1.43L16.29 22l2.14-2.14 1.43 1.43 1.43-1.43-1.43-1.43L22 16.29z'/%3E%3C/svg%3E"
ICON_STAR = "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='%23e8967a' width='14' height='14'%3E%3Cpath d='M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z'/%3E%3C/svg%3E"
ICON_CERT = "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='%23e8967a' width='14' height='14'%3E%3Cpath d='M12 1L3 5v6c0 5.55 3.84 10.74 9 12 5.16-1.26 9-6.45 9-12V5l-9-4zm-2 16l-4-4 1.41-1.41L10 14.17l6.59-6.59L18 9l-8 8z'/%3E%3C/svg%3E"


def escape(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def generate():
    config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "template_config_hk.json")
    with open(config_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    name = escape(data["name"])
    age = escape(str(data["age"]))
    origin = escape(data.get("origin", ""))
    education = escape(data.get("education", ""))
    phone = escape(data.get("phone", ""))
    job_obj = escape(data.get("job_objective", ""))
    salary = escape(data.get("expected_salary", ""))
    photo = data.get("photo_path", "")
    skills = data.get("skills", {})
    intro = escape(data.get("intro", ""))
    certs = data.get("certificates", [])
    work_exp = data.get("work_experience", [])
    work_photos = data.get("work_photos", [])

    # Sidebar basic info
    sb_items = []
    for key, val in [("姓名", name), ("年龄", age), ("籍贯", origin), ("学历", education), ("电话", phone)]:
        if val:
            sb_items.append(f'<div class="sb-item"><span class="label">{key}：</span>{val}</div>')

    # Self evaluation as paragraph
    eval_html = f'<p class="eval-text">{intro}</p>'

    # Certificates
    cert_html = ""
    if certs:
        cert_list_items = "".join(f'<li>{escape(c)}</li>' for c in certs)
        cert_html = f'''
  <div class="sb-section">
    <div class="sb-title"><span class="icon"><img src="{ICON_CERT}"/></span>持有证书</div>
    <ul class="cert-list">{cert_list_items}</ul>
  </div>'''

    # Work experience items (beautified)
    work_items = []
    for w in work_exp:
        period = escape(w.get("period", ""))
        title = escape(w.get("title", ""))
        desc = escape(w.get("description", ""))
        title_html = f'<span class="work-entry-title">{title}</span>' if title else ""
        work_items.append(f'''
    <div class="work-entry">
      <div class="work-entry-header">
        <span class="work-entry-period">{period}</span>
        {title_html}
      </div>
      <div class="work-entry-desc">{desc}</div>
    </div>''')

    # Skills section (cooking + cleaning bullet points)
    cooking = escape(skills.get("cooking", ""))
    cleaning = escape(skills.get("cleaning", ""))
    skills_html = f'''
    <div class="skill-category"><span class="sc-dot"></span>烹饪技能</div>
    <div class="skill-desc">{cooking.replace(chr(10), '<br>')}</div>
    <div class="skill-category"><span class="sc-dot"></span>保洁技能</div>
    <div class="skill-desc">{cleaning.replace(chr(10), '<br>')}</div>'''

    # Work photos
    photos_html = ""
    if work_photos:
        img_tags = ""
        for p in work_photos[:9]:
            img_tags += f'<img src="{escape(p)}" alt="作品">'
        photos_html = f'<div class="photos-grid">{img_tags}</div>'

    # Build sidebar
    sidebar = f'''
<div class="sidebar">
  <div class="photo-wrap">
    <div class="photo-circle"><img src="{escape(photo)}" alt="照片"></div>
  </div>

  <div class="sb-section">
    <div class="sb-title"><span class="icon"><img src="{ICON_PERSON}"/></span>基本信息</div>
    {''.join(sb_items)}
  </div>
{cert_html}

  <div class="sb-section">
    <div class="sb-title"><span class="icon"><img src="{ICON_STAR}"/></span>自我评价</div>
    {eval_html}
  </div>
</div>
'''

    # Build main
    main = f'''
<div class="main">
  <div class="dec-dot dec-dot-1"></div>
  <div class="dec-dot dec-dot-2"></div>
  <div class="dec-dot dec-dot-3"></div>
  <div class="dec-dot dec-dot-4"></div>

  <div class="main-header">
    <div class="name">{name}</div>
    <div class="job-obj">求职目标：{job_obj}</div>
    <div class="salary">期望薪资：{salary}</div>
  </div>

  <div class="section-content">
    <div class="section-header">
      <span class="sh-icon"><img src="{ICON_WORK}"/></span>工作经历
    </div>
    {''.join(work_items)}
  </div>

  <div class="section-content">
    <div class="section-header">
      <span class="sh-icon"><img src="{ICON_SKILL}"/></span>技能特长
    </div>
    {skills_html}
  </div>

  {photos_html}
</div>
'''

    html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<title>家政简历 - {name}</title>
<style>{CSS}</style>
</head>
<body>
<div class="page">
{sidebar}
{main}
</div>
</body>
</html>'''

    html_path = os.path.join(DESKTOP, "家政简历.html")
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"HTML saved: {html_path}")

    # Generate PDF
    try:
        from playwright.sync_api import sync_playwright
        pdf_path = os.path.join(DESKTOP, "家政简历.pdf")
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


if __name__ == "__main__":
    generate()
