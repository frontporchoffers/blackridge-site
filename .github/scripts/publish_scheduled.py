"""
Publish scheduled blog posts.

Walks blog/scheduled/, finds posts whose YYYY-MM-DD filename prefix is <= today,
moves them to blog/, fixes internal paths and dates, updates sitemap.xml and
blog/index.html. Designed to run from the repo root inside a GitHub Action.

File naming convention: blog/scheduled/YYYY-MM-DD-slug.html
After publish:           blog/slug.html
"""

import re
import sys
from datetime import datetime, date
from pathlib import Path

try:
    from bs4 import BeautifulSoup
except ImportError:
    print("ERROR: beautifulsoup4 not installed. Run: pip install beautifulsoup4 lxml")
    sys.exit(1)

# Repo root is two parents up from this script (.github/scripts/file.py -> repo root)
ROOT = Path(__file__).resolve().parent.parent.parent
BLOG_DIR = ROOT / "blog"
SCHED_DIR = BLOG_DIR / "scheduled"
SITEMAP = ROOT / "sitemap.xml"
BLOG_INDEX = BLOG_DIR / "index.html"

DATE_PREFIX_RE = re.compile(r"^(\d{4}-\d{2}-\d{2})-(.+)\.html$")
TODAY = date.today()
TODAY_ISO = TODAY.isoformat()
TODAY_LONG = TODAY.strftime("%B %-d, %Y")  # e.g. "June 8, 2026"


def find_due_posts():
    """Return [(file, pub_date, slug), ...] for posts ready to publish."""
    if not SCHED_DIR.exists():
        return []
    posts = []
    for f in SCHED_DIR.glob("*.html"):
        m = DATE_PREFIX_RE.match(f.name)
        if not m:
            print(f"  Skipping {f.name}: does not match YYYY-MM-DD-slug.html")
            continue
        pub_date = datetime.strptime(m.group(1), "%Y-%m-%d").date()
        slug = m.group(2)
        if pub_date <= TODAY:
            posts.append((f, pub_date, slug))
    return sorted(posts, key=lambda p: p[1])


def fix_paths_and_dates(html: str, slug: str, original_prefix: str) -> str:
    """Rewrite scheduled-folder URLs to live-folder URLs, fix relative path depth,
    update datePublished/dateModified, and update visible 'Published ...' text."""
    # Canonical, og:url, mainEntityOfPage @id, etc.
    scheduled_url = f"https://blackridgecontractor.com/blog/scheduled/{original_prefix}-{slug}"
    live_url = f"https://blackridgecontractor.com/blog/{slug}"
    html = html.replace(scheduled_url, live_url)

    # Path depth: file moves from /blog/scheduled/ to /blog/, so ../../ becomes ../
    html = html.replace('../../', '../')

    # Update Article schema dates
    html = re.sub(r'"datePublished":\s*"\d{4}-\d{2}-\d{2}"',
                  f'"datePublished": "{TODAY_ISO}"', html)
    html = re.sub(r'"dateModified":\s*"\d{4}-\d{2}-\d{2}"',
                  f'"dateModified": "{TODAY_ISO}"', html)

    # Update human-readable "Published Month DD, YYYY" text
    html = re.sub(r'Published [A-Z][a-z]+ \d{1,2}, \d{4}',
                  f'Published {TODAY_LONG}', html)

    return html


def extract_card_meta(html: str, slug: str):
    """Pull image, title, description for the blog index card."""
    soup = BeautifulSoup(html, 'lxml')

    title = soup.title.get_text() if soup.title else slug
    # Strip site name suffix
    title = re.sub(r'\s*\|\s*Black Ridge.*$', '', title).strip()

    desc_tag = soup.find('meta', attrs={'name': 'description'})
    description = desc_tag.get('content', '') if desc_tag else ''

    og_image = soup.find('meta', attrs={'property': 'og:image'})
    image_path = '../pictures/Black Ridge Contracting Full Size Photo.png'
    if og_image:
        m = re.search(r'blackridgecontractor\.com(/pictures/[^"]+)',
                      og_image.get('content', ''))
        if m:
            image_path = '..' + m.group(1)

    return title, description, image_path


def update_sitemap(slug: str):
    """Add a new URL or refresh lastmod on an existing one."""
    text = SITEMAP.read_text()
    url = f"https://blackridgecontractor.com/blog/{slug}"

    if url in text:
        # Existing entry: refresh lastmod
        text = re.sub(
            r'(<loc>' + re.escape(url) + r'</loc>\s*<lastmod>)\d{4}-\d{2}-\d{2}',
            r'\g<1>' + TODAY_ISO,
            text
        )
    else:
        # New entry: insert before </urlset>
        entry = (
            '  <url>\n'
            f'    <loc>{url}</loc>\n'
            f'    <lastmod>{TODAY_ISO}</lastmod>\n'
            '    <changefreq>monthly</changefreq>\n'
            '    <priority>0.7</priority>\n'
            '  </url>\n'
        )
        text = text.replace('</urlset>', entry + '</urlset>')

    SITEMAP.write_text(text)


def insert_blog_card(title: str, description: str, image_path: str, slug: str):
    """Insert a new card at the top of the card-grid in blog/index.html."""
    html = BLOG_INDEX.read_text()

    new_card = (
        '\n          <div class="card reveal">\n'
        f'            <img src="{image_path}" alt="{title}" width="600" height="400" loading="lazy" style="width:100%;height:auto;border-radius:8px;margin-bottom:1rem">\n'
        f'            <h3>{title}</h3>\n'
        f'            <p style="font-size:0.85rem;opacity:0.7;margin-bottom:0.5rem">{TODAY_LONG}</p>\n'
        f'            <p>{description}</p>\n'
        f'            <a href="{slug}.html" class="btn btn-primary" style="margin-top:1rem">Read More &#8594;</a>\n'
        '          </div>\n'
    )

    # Insert right after the opening card-grid div
    pattern = r'(<div class="card-grid card-grid-3">\s*\n)'
    new_html, count = re.subn(pattern, r'\1' + new_card, html, count=1)
    if count == 0:
        print(f"  WARNING: could not locate card-grid in blog/index.html, skipping card insert for {slug}")
        return
    BLOG_INDEX.write_text(new_html)


def main():
    print(f"Scanning for scheduled posts due on or before {TODAY_ISO}...")
    posts = find_due_posts()
    if not posts:
        print(f"No posts due today.")
        return

    for source_file, pub_date, slug in posts:
        original_prefix = pub_date.strftime("%Y-%m-%d")
        print(f"Publishing {source_file.name} -> blog/{slug}.html")
        try:
            html = source_file.read_text()
            html = fix_paths_and_dates(html, slug, original_prefix)

            dest = BLOG_DIR / f"{slug}.html"
            dest.write_text(html)

            title, description, image_path = extract_card_meta(html, slug)
            update_sitemap(slug)
            insert_blog_card(title, description, image_path, slug)

            source_file.unlink()
            print(f"  Done. Title: {title!r}")
        except Exception as e:
            print(f"  FAILED: {e}")
            # Continue with other posts

    print(f"Finished. Processed {len(posts)} post(s).")


if __name__ == "__main__":
    main()
