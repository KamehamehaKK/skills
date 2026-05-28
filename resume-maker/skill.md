---
name: resume-maker
description: Generate a professionally formatted Chinese resume (HTML + PDF) with photo support. Use when the user wants to create, update, or export a resume.
---

# Resume Maker

Generate a one-page A4 resume with Chinese typography.

## Workflow

1. Collect the following information from the user. Read `template_config.json` first — if it exists, use it as defaults and only ask the user what they want to change.
2. Write the collected data to `template_config.json`.
3. Run `python generate.py` to produce `简历.html` and `简历.pdf` on the desktop.

## Data to collect

| Field | Example |
|-------|---------|
| Name | 周沛康 |
| Phone | 18878918417 |
| Email | 1372220517@qq.com |
| Photo path | 简历.jpg (relative to HTML) or leave empty |
| Education (list) | {school, major, degree, years} |
| Projects (list) | {name, role/time, tech_stack, overview, bullets: [{label, content}]} |
| Work experience (list) | {company, title, years, bullets: [{label, content}]} |
| Skills (list) | {label, content} |
| Extra sections | optional: 个人优势, 自我评价 etc. |

## Design rules

- All text black (#222), no gray
- No parentheses for grouping — use natural phrasing
- No quotation marks in bullet content
- Bullet labels are bold, followed by Chinese colon
- Section titles: bordered bottom, 11pt bold
- Name: 18pt bold, top-left
- Photo: top-right, 72×96pt
- Page margins: 10mm top/bottom, 14mm left/right
- Must fit one A4 page

## Project section specifics

Each project has:
- Title line: name (left) | role + date (right)
- Subtitle: tech stack in italics
- One-sentence overview
- 3-4 bullets with bold labels

## Work section specifics

Each position has:
- Title line: company | title (left) | date (right)
- 2-3 bullets with bold labels (e.g. 单元测试, 诊断与集成测试)

## Skills section specifics

Each skill as: **Label:** content text. Keep content concise, no nested parentheses.
