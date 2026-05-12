"""
Substrate · Essay Builder
Converts the three markdown essays into styled HTML pages.
Run this whenever you edit an essay's markdown file.
"""

import os
import re

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


def format_paragraph(text):
    """Convert one paragraph's markdown to inline HTML."""
    # Bold: **text** -> <strong>text</strong>
    text = re.sub(r"\*\*([^\*]+)\*\*", r"<strong>\1</strong>", text)
    # Italic: *text* -> <em>text</em>  (avoid matching ** which is already gone)
    text = re.sub(r"(?<!\*)\*([^\*\n]+)\*(?!\*)", r"<em>\1</em>", text)
    # Collapse internal whitespace/newlines to single space
    text = re.sub(r"\s+", " ", text).strip()
    return f"<p>{text}</p>"


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


def build_all():
    """Build all essays."""
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Read the shared stylesheet so we can inline it
    css_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "styles.css")
    with open(css_path, "r") as f:
        css_content = f.read()

    for essay in ESSAYS:
        md_path = os.path.join(SOURCE_DIR, f"{essay['slug']}.md")
        html_path = os.path.join(OUTPUT_DIR, f"{essay['slug']}.html")

        with open(md_path, "r") as f:
            md_text = f.read()

        body_html = markdown_to_html_paragraphs(md_text)
        more_reading_html = build_more_reading_html(essay["slug"])
        full_html = build_essay_html(essay, body_html, more_reading_html, css_content)

        with open(html_path, "w") as f:
            f.write(full_html)

        print(f"Built: {html_path}")


if __name__ == "__main__":
    build_all()
    print("\nAll essays built. Open them in /home/claude/site/essays/")
