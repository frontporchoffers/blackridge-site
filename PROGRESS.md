# Black Ridge Contracting — Project Progress

**Site:** https://blackridgecontractor.com
**Local path:** `/Users/Drew/Desktop/Claude/claude-skills-main/Projects/local-seo-agency/brc-site/`
**Host:** Netlify (drag-and-drop deploy from this folder)
**Last updated:** 2026-05-06

---

## Current phase

**Phase 4 — Visibility & Rankings.**
Indexing throttle is broken (Discovered — not indexed went from 28 → 0). Now the problem is rankings: site appears in 1,600+ impressions across 150+ commercial queries but ranks position 47 on average. Pushing positions from 50 → 10 with authority signals + on-page tightening.

---

## Stage log

### Phase 1 — Technical build (done)
- Static HTML site deployed to Netlify, `www → non-www` 301
- Page tree: /, /about, /contact, /portfolio, 9 service pages, 15 area pages, 7 blog posts (after 2026-05-06 publish)
- Netlify config: HSTS, CSP, cache headers, 404 page
- Internal linking: homepage links to all services + all areas; indexed pages link to unindexed via nav/footer/service-area-tag blocks
- Canonical tags on every page
- Contact: (515) 219-4654, drew@blackridgecontractor.com

### Phase 2 — Schema (done 2026-04-20)
- about.html and portfolio.html upgraded to full LocalBusiness + AboutPage/CollectionPage + FAQPage
- All schema uses `@id: "https://blackridgecontractor.com/#business"` so Google sees one entity
- ImageObjects in portfolio have copyrightNotice, license, acquireLicensePage
- `sameAs` array unified across pages: Facebook, 2× Google Maps, Yelp, full Houzz URL, DT Chamber

### Phase 3 — Authority & first indexing batch (done 2026-04-20 to 2026-04-22)
- ✅ GBP claimed/verified, posting weekly
- ✅ Yelp, Houzz, DT Chamber, Realtor.com, Zillow agent profile backlinks live
- ✅ Bing Webmaster Tools set up (IndexNow plugin deprecated, doesn't exist)
- ✅ All 25 priority URLs submitted via GSC Request Indexing across 3 days
- ✅ Indexing went from 8 → 12 indexed; "Discovered — not indexed" went from 28 → 0

### Phase 4 — Visibility & rankings (in progress, started 2026-05-06)
- ✅ **Sitemap lastmod refreshed** to 2026-05-06 across all 37 URLs (was stale at 2026-04-03)
- ✅ **New blog post published:** `/blog/concrete-driveway-replacement-iowa` (added to sitemap + blog index)
- ✅ **Title tags rewritten** on three top-impression pages:
  - /areas/des-moines: "Des Moines General Contractor | Roofing, Siding & Remodeling" (was at position 8, 82 impressions)
  - /areas/west-des-moines: "West Des Moines Contractor | Roofing, Siding & Remodel" (was at position 12, 51 impressions)
  - /blog/best-siding-materials-iowa: "Best Siding for Iowa Weather: Vinyl vs. Fiber Cement vs. Wood" (was at position 7.8, 132 impressions, 0 clicks)
- ⏳ Iowa Home Builders Association backlink (Drew action)
- ⏳ Better Business Bureau application (Drew waiting on approval)
- ⏳ Resubmit sitemap in GSC after Netlify redeploy

---

## GSC status (as of 2026-05-06)

**Indexed:** 12
**Page with redirect:** 4 (likely www variants)
**Discovered — not indexed:** 0 ✅
**Crawled — not indexed:** 0 ✅
**Server error (5xx):** 0
**Sitemap URLs Google hasn't crawled yet:** ~20 of 37 (crawl budget rationing — fixes are sitemap freshness + authority)

### Performance (last 90 days)
- 1,637 impressions, 17 clicks, avg position 47, avg CTR ~1%
- Top performer: homepage (12 clicks, 315 impressions, position 8.97, 3.81% CTR)
- Pattern: appearing in many relevant queries, ranked positions 50-90 — relevance OK, authority weak

### Top opportunity pages (page-1-adjacent)
| Page | Impressions | Position | After 5/6 title tag rewrite |
|---|---|---|---|
| /areas/des-moines | 82 | 8 | retitled — monitor |
| /blog/best-siding-materials-iowa | 132 | 7.8 | retitled — monitor |
| /areas/west-des-moines | 51 | 12 | retitled — monitor |

### Brand confusion
"Black Ridge Exteriors" and "Blackridge Construction" are competitor brands generating impressions on this site. Treat that traffic as parasitic; doesn't convert.

---

## Next actions (prioritized)

1. **Redeploy `brc-site/` to Netlify** — drag-and-drop
2. **Resubmit sitemap.xml in GSC** (Search Console → Sitemaps → submit https://blackridgecontractor.com/sitemap.xml again) — fresh lastmod dates trigger recrawl
3. **Verify in Rich Results Test** that the new blog post + retitled pages parse cleanly
4. **Iowa HBA membership** — biggest single backlink lever for unlocking the ~20 unindexed sitemap URLs
5. **Publish next blog post 2026-05-15** from `blog/scheduled/2026-05-01-iowa-storm-damage-roof-repair.html` (already past due date — repurpose or update)
6. **Pull next GSC snapshot ~2026-05-13** (one week from sitemap refresh) to measure crawl/index movement

---

## Known gaps / future work

- Portfolio images are mostly placeholders — only Interior Painting + Street View are real
- Blog has 5 more scheduled drafts in `blog/scheduled/` (siding 6/1, basement 6/15, kitchen mistakes 7/1, gutter cleaning 7/15)
- AggregateRating.reviewCount hardcoded at 47 across pages — refresh when GBP count changes
- Drew has additional profiles he doesn't remember — needs audit (Nextdoor, Thumbtack, Porch, BuildZoom)

---

## Reference

- GSC reports snapshots: `brc-site/gsc-reports/` (4/17 + 5/06)
- Lighthouse audits: `lighthouse-desmoines.json`, `lighthouse-homepage.json`, `lighthouse-roofing.json`
- Vault mirror: `Drew's Brain/Projects/Blackridge Contractor/STATUS.md`
- Active checklist (when work is in flight): `brc-site/GSC-INDEXING-CHECKLIST.md`

---

## Status check 2026-09-24

- **Lead channel = phone calls (Drew, 9/24); form is secondary.** Gmail shows no real Formspree leads since March: submissions since March = Drew tests (4/5, 4/6, 4/22, 7/31) + two vendor pitches (6/15 DraftRise, 8/1 AI-SEO spam). Calls are untracked, so we cannot tie leads to pages or sources.
- Latest GSC export on disk is 2026-06-08 (3.5 months stale): homepage pos ~10; siding/areas/concrete pages pos 35-55; 26 clicks total, 4 of them "black ridge exteriors" brand confusion.
- Content engine healthy: roofing hub + 4 sub-pages (7/28), 14 areas pages enhanced, blog auto-publish cron running daily (9/7 + 9/21 posts shipped, 7 queued through 12/28). Hosting on Vercel since 7/29.
- Diagnosis: site has no lead problem it can solve with more blog posts. Organic pages sit on page 4-5; contractor leads come from the map pack + reviews + paid local.
- Still open from May: Iowa HBA membership, BBB. AggregateRating reviewCount hardcoded at 47. Verify vs real GBP count.

- **Lead volume (Drew, 9/24):** ~1 real call/month, lots of spam calls. ~4 serious calls total, 1 closed job (Janet). Close rate ~25% on serious calls; volume is the constraint.

## Visibility audit 2026-09-25 (corrected with Drew same day)

- **GBP: verified, posting works** (Drew 9/25). The 6/8 "post removed / posting turned off" email and the 7/28 re-verify email are resolved; the 6/8 post is still live.
- **Reviews: 2 Google reviews, both 5 stars** (Drew 9/25). Site said 4.9 / 47 everywhere. **Fixed 9/25:** schema reviewCount/ratingCount → 2, ratingValue → 5.0, all visible "4.9/5 Google Rating" badges and "47 customers" copy corrected across 62 pages.
- **Confirmed true by Drew:** Licensed & Insured, 200+ projects, family-owned since 2020.
- **Open questions for Drew:** "BBB Accredited" badge (May notes said application pending) and named testimonials (Mike R., Sarah T., David L., Nancy J., Lisa P., Jennifer M., etc.) marked up as Review schema on the homepage. Keep only if real.
- GSC data on disk is from 6/8. Need a fresh export.
- FB: Black Ridge Page https://www.facebook.com/p/Black-Ridge-Contracting-61574268338602/ (a Page, not a group). Auto-poster proposed, cloned from /Users/Drew/fbpost.