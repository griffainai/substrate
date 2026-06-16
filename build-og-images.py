"""
Substrate · OG image builder
Generates 1200x630 social preview cards (Open Graph / Twitter) — one per essay,
plus a default site card. Brand-matched to styles.css: paper background, accent
rule, serif-italic title, mono eyebrow.

Run after editing the ESSAYS list in build-essays.py:
    python build-og-images.py

Output: og/<slug>.png for each essay, og/substrate-default.png for the site.
Pure PIL, no external converters. Fonts fall back gracefully if a face is missing.
"""

import os
import importlib.util
from PIL import Image, ImageDraw, ImageFont

SITE_DIR = os.path.dirname(os.path.abspath(__file__))
OG_DIR = os.path.join(SITE_DIR, "og")

# Single source of truth: pull the essay list straight from build-essays.py
# (filename has a hyphen, so load it by path rather than importing by name)
_spec = importlib.util.spec_from_file_location(
    "build_essays", os.path.join(SITE_DIR, "build-essays.py")
)
_be = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_be)
ESSAYS = _be.ESSAYS

# Brand palette (from styles.css)
PAPER = (250, 248, 244)
INK = (26, 24, 21)
INK_MUTED = (110, 104, 94)
ACCENT = (44, 85, 69)
RULE = (212, 207, 195)

W, H = 1200, 630
MARGIN = 90

# Windows system fonts — close matches to the site's Cormorant Garamond / JetBrains Mono.
# First existing path wins; falls back to PIL default if none are present.
FONT_CANDIDATES = {
    "serif_italic": ["C:/Windows/Fonts/georgiai.ttf", "C:/Windows/Fonts/cambriai.ttf", "C:/Windows/Fonts/timesi.ttf"],
    "serif": ["C:/Windows/Fonts/georgia.ttf", "C:/Windows/Fonts/cambria.ttc", "C:/Windows/Fonts/times.ttf"],
    "mono": ["C:/Windows/Fonts/consola.ttf", "C:/Windows/Fonts/cour.ttf"],
}


def load_font(kind, size):
    for path in FONT_CANDIDATES[kind]:
        if os.path.exists(path):
            return ImageFont.truetype(path, size)
    return ImageFont.load_default()


def wrap(draw, text, font, max_w):
    words = text.split()
    lines, cur = [], ""
    for word in words:
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=font) <= max_w or not cur:
            cur = trial
        else:
            lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def tracked(draw, pos, text, font, fill, spacing):
    """Draw text with extra letter-spacing (for the mono eyebrow/wordmark)."""
    x, y = pos
    for ch in text:
        draw.text((x, y), ch, font=font, fill=fill)
        x += draw.textlength(ch, font=font) + spacing


def make_card(out_path, eyebrow, title, subtitle=None):
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # top accent bar
    d.rectangle([0, 0, W, 10], fill=ACCENT)

    # wordmark + eyebrow (mono, letter-spaced)
    tracked(d, (MARGIN, 74), "SUBSTRATE", load_font("mono", 25), ACCENT, 3)
    tracked(d, (MARGIN, 122), eyebrow.upper(), load_font("mono", 21), INK_MUTED, 2)

    # Lay out title + subtitle inside the band between the eyebrow and the
    # bottom rule, vertically centered, never overflowing.
    max_w = W - 2 * MARGIN
    y_top = 200
    y_limit = H - 78 - 30  # keep clear of the bottom rule

    # subtitle measured first (it claims fixed space at the bottom of the band)
    sub_size = 29
    sub_line_h = int(sub_size * 1.34)
    sub_lines = []
    if subtitle:
        sf = load_font("serif_italic", sub_size)
        sub_lines = wrap(d, subtitle, sf, max_w)[:2]
    sub_block = (len(sub_lines) * sub_line_h + 22) if sub_lines else 0

    # pick the largest title size that wraps to <= 3 lines AND fits the remaining budget
    title_budget = (y_limit - y_top) - sub_block
    chosen, title_lines, tf = 40, None, None
    for size in (80, 72, 64, 58, 52, 46, 40):
        tf = load_font("serif_italic", size)
        title_lines = wrap(d, title, tf, max_w)
        if len(title_lines) <= 3 and len(title_lines) * int(size * 1.16) <= title_budget:
            chosen = size
            break
    if title_lines is None or len(title_lines) > 3:
        tf = load_font("serif_italic", 40)
        title_lines = wrap(d, title, tf, max_w)[:3]
        chosen = 40
    title_line_h = int(chosen * 1.16)
    title_block = len(title_lines) * title_line_h

    # vertically center the whole block within the band
    y = y_top + max(0, ((y_limit - y_top) - (title_block + sub_block)) // 2)
    for ln in title_lines:
        d.text((MARGIN, y), ln, font=tf, fill=INK)
        y += title_line_h
    if sub_lines:
        y += 22
        for ln in sub_lines:
            d.text((MARGIN, y), ln, font=sf, fill=INK_MUTED)
            y += sub_line_h

    # bottom rule + url
    d.line([MARGIN, H - 78, W - MARGIN, H - 78], fill=RULE, width=1)
    tracked(d, (MARGIN, H - 56), "jaydenforshee.com", load_font("mono", 21), INK_MUTED, 2)

    img.save(out_path, "PNG")
    print("Built:", out_path)


def build_all():
    os.makedirs(OG_DIR, exist_ok=True)
    for e in ESSAYS:
        make_card(
            os.path.join(OG_DIR, f"{e['slug']}.png"),
            f"Reading Room · Edition {e['edition']}",
            e["title"],
            e["subtitle"],
        )
    # default card for index / practice / audit
    make_card(
        os.path.join(OG_DIR, "substrate-default.png"),
        "The Practice of Jayden Forshee",
        "Substrate",
        "Reading businesses at their structural layer, and installing the AI architecture that runs from what they actually are.",
    )
    print("\nAll OG cards built in", OG_DIR)


if __name__ == "__main__":
    build_all()
