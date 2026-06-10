"""
Substrate · Essay Builder
Converts the three markdown essays into styled HTML pages.
Run this whenever you edit an essay's markdown file.
"""

import os
import re
from datetime import date

# Essay metadata - edit here to add/reorder essays
ESSAYS = [
    {
        "slug": "01-the-ontology-of-a-business",
        "edition": "01",
        "title": "The Ontology of a Business",
        "subtitle": "On what your company actually is, underneath what you have been telling yourself it is.",
        "date": "2026",
    },
    {
        "slug": "02-why-folder-structure-is-architecture",
        "edition": "02",
        "title": "Why Folder Structure is Architecture",
        "subtitle": "On Interpretable Context Methodology, and why the cleanest AI system is one that does not look like an AI system.",
        "date": "2026",
    },
    {
        "slug": "03-strategy-is-downstream",
        "edition": "03",
        "title": "Strategy is Downstream",
        "subtitle": "On why most strategy fails, what it is downstream of, and the layer that has to be settled first.",
        "date": "2026",
    },
    {
        "slug": "04-field-notes-on-duty",
        "edition": "04",
        "title": "Field Notes — Installing the Architecture in a Co-Founded Company",
        "subtitle": "Build log from On Duty, the fleet safety platform I am building with my stepdad as co-founder.",
        "date": "2026",
    },
    {
        "slug": "05-the-three-layers-of-a-business",
        "edition": "05",
        "title": "The Three Layers of a Business",
        "subtitle": "On why most strategy frameworks are missing the middle layer, and what changes when you name it.",
        "date": "2026",
    },
]

SOURCE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "writing")
OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "essays")


def markdown_to_html_paragraphs(md_text):
    """Convert essay body markdown into HTML, handling our specific patterns."""
    # Strip the header/metadata block (everything up to first ---)
    parts = md_text.split("\n---\n", 1)
    body = parts[1] if len(parts) > 1 else md_text

    # Strip trailing signature (--- *Substrate...*)
    body = re.split(r"\n---\n\s*\*Substrate", body)[0]
    body = body.strip()

    # Process line by line, building paragraphs and headers
    html_parts = []
    current_para = []
    in_para = False

    lines = body.split("\n")
    i = 0
    while i < len(lines):
        line = lines[i].rstrip()

        # Horizontal rule
        if line.strip() == "---":
            if current_para:
                html_parts.append(format_paragraph("\n".join(current_para)))
                current_para = []
            html_parts.append("<hr>")
            i += 1
            continue

        # Header (## )
        if line.startswith("## "):
            if current_para:
                html_parts.append(format_paragraph("\n".join(current_para)))
                current_para = []
            heading = line[3:].strip()
            html_parts.append(f"<h2>{heading}</h2>")
            i += 1
            continue

        # Sub-header (### )
        if line.startswith("### "):
            if current_para:
                html_parts.append(format_paragraph("\n".join(current_para)))
                current_para = []
            heading = line[4:].strip()
            html_parts.append(f"<h3>{heading}</h3>")
            i += 1
            continue

        # Bullet list (consume contiguous "- " lines)
        if line.startswith("- "):
            if current_para:
                html_parts.append(format_paragraph("\n".join(current_para)))
                current_para = []
            items = []
            while i < len(lines) and lines[i].rstrip().startswith("- "):
                item_text = lines[i].rstrip()[2:]
                items.append(f"      <li>{format_inline(item_text)}</li>")
                i += 1
            html_parts.append("<ul>\n" + "\n".join(items) + "\n    </ul>")
            continue

        # Empty line = paragraph break
        if line.strip() == "":
            if current_para:
                html_parts.append(format_paragraph("\n".join(current_para)))
                current_para = []
            i += 1
            continue

        # Regular content line
        current_para.append(line)
        i += 1

    # Flush remaining paragraph
    if current_para:
        html_parts.append(format_paragraph("\n".join(current_para)))

    return "\n\n    ".join(html_parts)


def format_inline(text):
    """Apply inline markdown (bold/italic) and collapse whitespace."""
    text = re.sub(r"\*\*([^\*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<!\*)\*([^\*\n]+)\*(?!\*)", r"<em>\1</em>", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def format_paragraph(text):
    """Convert one paragraph's markdown to inline HTML."""
    return f"<p>{format_inline(text)}</p>"


def build_more_reading_html(current_slug):
    """Build the 'more reading' block linking to other essays."""
    others = [e for e in ESSAYS if e["slug"] != current_slug]
    if not others:
        return ""

    items = []
    for e in others:
        items.append(f'''      <li class="more-reading-item">
        <a href="{e["slug"]}.html">{e["title"]}</a>
        <span class="more-reading-item-meta">Edition {e["edition"]} · {e["subtitle"]}</span>
      </li>''')

    return f'''
    <div class="more-reading">
      <div class="more-reading-eyebrow">— More from the Reading Room</div>
      <ul class="more-reading-list">
{chr(10).join(items)}
      </ul>
    </div>'''


def build_essay_html(essay, body_html, more_reading_html, css_content):
    """Assemble the full essay page with inlined CSS so it renders standalone."""
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<meta name="color-scheme" content="light only" />
<meta name="supported-color-schemes" content="light" />
<meta name="theme-color" content="#faf8f4" />
<title>{essay["title"]} — Substrate</title>
<meta name="description" content="{essay["subtitle"]} Reading Room, Edition {essay["edition"]}." />
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;0,600;1,300;1,400;1,500&family=Inter:wght@300;400;500;600&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>
{css_content}
</style>
</head>
<body>

  <nav class="nav">
    <div class="nav-inner-narrow">
      <a href="../index.html" class="nav-mark">Substrate <span class="nav-mark-sub">Practice of Jayden Forshee</span></a>
      <a href="../index.html#reading-room" class="nav-back">← Reading Room</a>
    </div>
  </nav>

  <article>
    <div class="essay-meta">Reading Room · Edition {essay["edition"]} · {essay["date"]}</div>
    <h1 class="essay-title">{essay["title"]}</h1>
    <p class="essay-subtitle">{essay["subtitle"]}</p>
    <div class="essay-divider"></div>

    {body_html}
    {more_reading_html}
  </article>

  <footer>
    <div class="footer-inner footer-inner-narrow">
      <div>Substrate · Practice of Jayden Forshee · 2026</div>
      <div><a href="mailto:jaydiorforshee@gmail.com">jaydiorforshee@gmail.com</a></div>
    </div>
  </footer>

</body>
</html>
'''


SITE_ROOT = "https://jaydenforshee.com"


def build_sitemap():
    """Regenerate /sitemap.xml from current ESSAYS list + the static top-level pages."""
    site_dir = os.path.dirname(os.path.abspath(__file__))

    def lastmod_for(rel_path):
        full = os.path.join(site_dir, rel_path)
        if os.path.exists(full):
            return date.fromtimestamp(os.path.getmtime(full)).isoformat()
        return date.today().isoformat()

    entries = [
        (f"{SITE_ROOT}/", lastmod_for("index.html"), "weekly", "1.0"),
        (f"{SITE_ROOT}/practice.html", lastmod_for("practice.html"), "monthly", "0.9"),
        (f"{SITE_ROOT}/audit.html", lastmod_for("audit.html"), "monthly", "0.8"),
    ]
    for essay in ESSAYS:
        rel = f"essays/{essay['slug']}.html"
        entries.append((f"{SITE_ROOT}/{rel}", lastmod_for(rel), "yearly", "0.7"))

    lines = ['<?xml version="1.0" encoding="UTF-8"?>',
             '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for loc, lastmod, changefreq, priority in entries:
        lines.append("  <url>")
        lines.append(f"    <loc>{loc}</loc>")
        lines.append(f"    <lastmod>{lastmod}</lastmod>")
        lines.append(f"    <changefreq>{changefreq}</changefreq>")
        lines.append(f"    <priority>{priority}</priority>")
        lines.append("  </url>")
    lines.append("</urlset>")

    out = os.path.join(site_dir, "sitemap.xml")
    with open(out, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    print(f"Built: {out}")


def build_practice(css_content):
    """Build /practice.html from 00_root/website/practice.md (the canonical offer doc)."""
    site_dir = os.path.dirname(os.path.abspath(__file__))
    # practice.md lives in the workspace at 00_root/website/practice.md
    workspace_root = os.path.abspath(os.path.join(site_dir, "..", ".."))
    src = os.path.join(workspace_root, "00_root", "website", "practice.md")
    out = os.path.join(site_dir, "practice.html")

    if not os.path.exists(src):
        print(f"Skipped practice page — source not found at {src}")
        return

    with open(src, "r", encoding="utf-8") as f:
        md_text = f.read()

    body_html = markdown_to_html_paragraphs(md_text)

    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<meta name="color-scheme" content="light only" />
<meta name="supported-color-schemes" content="light" />
<meta name="theme-color" content="#faf8f4" />
<title>The Practice — Substrate</title>
<meta name="description" content="A working document on what I do, how I do it, and what an engagement looks like. The practice of Jayden Forshee." />
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;0,600;1,300;1,400;1,500&family=Inter:wght@300;400;500;600&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>
{css_content}
</style>
</head>
<body>

  <nav class="nav">
    <div class="nav-inner-narrow">
      <a href="index.html" class="nav-mark">Substrate <span class="nav-mark-sub">Practice of Jayden Forshee</span></a>
      <a href="index.html" class="nav-back">← Home</a>
    </div>
  </nav>

  <article>
    <div class="essay-meta">The Practice · A Working Document · 2026</div>
    <h1 class="essay-title">Substrate</h1>
    <p class="essay-subtitle">A working document on what I do, how I do it, and what an engagement looks like. A practice — and a teaching.</p>
    <div class="essay-divider"></div>

    {body_html}
  </article>

  <footer>
    <div class="footer-inner footer-inner-narrow">
      <div>Substrate · Practice of Jayden Forshee · 2026</div>
      <div><a href="mailto:jaydiorforshee@gmail.com">jaydiorforshee@gmail.com</a></div>
    </div>
  </footer>

</body>
</html>
'''

    with open(out, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Built: {out}")


def build_all():
    """Build all essays."""
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Read the shared stylesheet so we can inline it
    css_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "styles.css")
    with open(css_path, "r", encoding="utf-8") as f:
        css_content = f.read()

    for essay in ESSAYS:
        md_path = os.path.join(SOURCE_DIR, f"{essay['slug']}.md")
        html_path = os.path.join(OUTPUT_DIR, f"{essay['slug']}.html")

        with open(md_path, "r", encoding="utf-8") as f:
            md_text = f.read()

        body_html = markdown_to_html_paragraphs(md_text)
        more_reading_html = build_more_reading_html(essay["slug"])
        full_html = build_essay_html(essay, body_html, more_reading_html, css_content)

        with open(html_path, "w", encoding="utf-8") as f:
            f.write(full_html)

        print(f"Built: {html_path}")


if __name__ == "__main__":
    build_all()
    # Build the practice page using the same shared CSS as essays
    css_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "styles.css")
    with open(css_path, "r", encoding="utf-8") as f:
        css_content = f.read()
    build_practice(css_content)
    build_sitemap()
    print("\nAll essays built. Open them in /home/claude/site/essays/")
