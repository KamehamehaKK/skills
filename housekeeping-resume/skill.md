---
name: housekeeping-resume
description: Generate a housekeeping/domestic worker resume (HTML + PDF) with peach-themed two-column layout, photo, and 9 work photo grid. Use when the user wants to create a domestic service resume.
---

# Housekeeping Resume Generator

Generate a two-column A4 housekeeping resume with peach/peach-orange theme, matching the template design.

## Workflow

1. Collect the following information from the user. If `template_config_hk.json` exists, use as defaults.
2. Write data to `template_config_hk.json`.
3. Run `python housekeeping_generate.py` to produce HTML and PDF on the desktop.

## Data to collect

| Field | Notes |
|-------|-------|
| name | Full name |
| age | Age |
| origin | Hometown / province |
| education | Education level |
| job_objective | e.g. "住家保姆 / 钟点家政 / 育婴师" |
| expected_salary | e.g. "6000-8000元/月" |
| phone | Phone number |
| photo_path | Path to the portrait photo |
| skills | Skills and specialties text |
| work_experience | List of {period, description} |
| intro | Self-introduction paragraph |
| work_photos | Array of paths to 9 work photos |

## Design rules

- Two-column layout: left sidebar (~32% width, cream #f5ede0 background), right main (~68%, white)
- Left sidebar: circular photo with peach (#e8967a) border, then "基本信息", "个人优势" sections
- Right area: name (18pt bold), job objective, salary at top
- Section headers: peach background bar (#e8967a), white text, with small icon prefix, left-aligned
- Section header bar spans full width of right column
- Thin peach vertical line separates sidebar from main content
- 9 work photos in a 3x3 grid with small gaps, below the skills section
- Page margins: 0 (content fills page), inner padding 8mm
- All text dark gray (#333)
- Font: "Microsoft YaHei", sans-serif
- Must fit one A4 page
