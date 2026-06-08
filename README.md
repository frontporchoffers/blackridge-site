# Black Ridge Contracting — Site

Static HTML site for [blackridgecontractor.com](https://blackridgecontractor.com), deployed via Netlify.

## How deploys work

This repo is connected to Netlify. **Every push to `main` auto-deploys the live site in ~90 seconds.** No more drag-and-drop.

## How scheduled blog posts work

Write blog posts ahead of time. Drop them in `blog/scheduled/` using this naming convention:

```
blog/scheduled/YYYY-MM-DD-slug.html
```

For example: `blog/scheduled/2026-07-15-roof-maintenance-tips.html`

Every day at ~6am Central, a GitHub Action runs and:

1. Looks at every file in `blog/scheduled/`
2. For any file whose date prefix is ≤ today's date:
   - Rewrites internal URLs from `/blog/scheduled/...` to `/blog/slug`
   - Fixes relative paths (`../../` → `../`) so styles and links work at the new depth
   - Updates `datePublished` and `dateModified` in the JSON-LD schema to today
   - Updates the visible "Published Month DD, YYYY" line
   - Moves the file to `blog/slug.html`
   - Adds a new URL entry to `sitemap.xml` with today's lastmod
   - Inserts a new card at the top of `blog/index.html`
   - Deletes the source file from `blog/scheduled/`
3. Commits and pushes the changes
4. Netlify auto-deploys

**Manual trigger:** Actions tab → "Publish Scheduled Blog Posts" → Run workflow.

## Folder structure

```
brc-site/
├── .github/
│   ├── workflows/
│   │   └── publish-scheduled-posts.yml   # Daily cron job
│   └── scripts/
│       └── publish_scheduled.py          # Publish logic
├── about.html
├── blog/
│   ├── index.html                        # Blog landing page
│   ├── scheduled/                        # Drafts queued by publish date
│   └── *.html                            # Published posts
├── areas/                                # City landing pages
├── services/                             # Service landing pages
├── pictures/                             # Images
├── sitemap.xml
├── robots.txt
├── netlify.toml                          # Netlify config (headers, redirects)
└── index.html

```

## Local development

Edit files, push, done. There's no build step. To preview locally, open `index.html` in a browser or run a quick static server:

```bash
python3 -m http.server 8000
# Open http://localhost:8000
```

## After publishing

If a scheduled post just went live, Drew should manually:

1. Run a quick rich-results check: [Google Rich Results Test](https://search.google.com/test/rich-results) on the new URL
2. Resubmit `sitemap.xml` in GSC → Sitemaps to nudge Google to recrawl
3. Share the post on GBP, Nextdoor, and Facebook for the first social signal
