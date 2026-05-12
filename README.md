# Substrate Site

This folder is your entire website. Everything is plain HTML and markdown — no build system, no framework, no server required. You can host this on Vercel, Netlify, Cloudflare Pages, or any static host for free.

## Folder structure

```
site/
├── index.html              ← main page (the practice)
├── ICM-paper.pdf           ← the Jake Van Clief paper
├── styles.css              ← shared styles for essay pages
├── build-essays.py         ← run this after editing essays
├── writing/                ← your essay source files (markdown)
│   ├── 01-the-ontology-of-a-business.md
│   ├── 02-why-folder-structure-is-architecture.md
│   └── 03-strategy-is-downstream.md
└── essays/                 ← generated essay HTML pages
    ├── 01-the-ontology-of-a-business.html
    ├── 02-why-folder-structure-is-architecture.html
    └── 03-strategy-is-downstream.html
```

## Three ways to update — easiest first

### To update an existing essay (5 minutes)

1. Open the markdown file in `writing/` (any text editor — VS Code, Sublime, even Notepad)
2. Edit the text
3. Run: `python3 build-essays.py`
4. Push to your host

The build script reads the markdown and rebuilds the HTML automatically. Your site stays in sync.

### To add a new essay (15 minutes)

1. Create a new markdown file in `writing/` — copy an existing one as a template
2. Open `build-essays.py` and add an entry to the `ESSAYS` list at the top:
   ```python
   {
       "slug": "04-your-new-essay",
       "edition": "04",
       "title": "Your New Essay",
       "subtitle": "What the essay is about, in one sentence.",
       "date": "2026",
   },
   ```
3. Run: `python3 build-essays.py`
4. Open `index.html` in the Reading Room section (§ VIII) and add a new `<li class="more-reading-item">` block linking to the new essay
5. Push to your host

### To edit the main page (the practice page itself)

Open `index.html` directly. The sections are clearly labeled (`§ I — The Premise`, `§ II — The Substrate`, etc.). Edit any section's text. Save. Push.

## Daily updates — the easy workflow

For real "update daily" workflow, here is the simplest setup:

1. **Put the whole `site/` folder in a GitHub repository.**
2. **Connect the repo to Vercel** (or Netlify or Cloudflare Pages — all free, all do the same thing). They watch your repo. Every time you push a change, the site updates automatically within 30 seconds.
3. **For text edits:** open GitHub.com → navigate to the file → click the pencil icon → edit in the browser → commit. The site updates automatically. No local setup, no terminal, no anything.
4. **For new essays:** edit a markdown file in the browser the same way, then run `build-essays.py` to regenerate the HTML, then commit. Or if you want to skip the build step entirely, just write the essay directly as an HTML file in `essays/` using one of the existing essays as a template.

Time to update an essay from your phone, from anywhere: about 90 seconds.

## What to do this week

1. **Replace `hello@example.com`** in three places: `index.html` (footer + ending section + meta tag) and the essay HTML files' footers. Search-and-replace works.
2. **Register `jaydenforshee.com`** at Cloudflare or Namecheap (~$12/year).
3. **Push the site/ folder to GitHub**, connect to Vercel, point the domain at it.
4. **Set up email forwarding** at Cloudflare so `hello@jaydenforshee.com` or `jayden@jaydenforshee.com` forwards to your real inbox. Free, takes 5 minutes.

After this week, your name is your URL, your email comes from your domain, and updating the site takes 90 seconds from anywhere.

## Adding case studies later

When you finish your first paid engagement and want to add it as a case study:

1. Create `case-studies/` folder
2. Write each case study as a markdown file there
3. Add a `§ IX — Case Studies` section to `index.html` modeled on the Reading Room section
4. Optionally extend `build-essays.py` to also build case studies (or just write them directly as HTML)

The site is designed to grow. Adding sections does not require rebuilding anything that already works.

---

*Substrate · Practice of Jayden Forshee · 2026*
