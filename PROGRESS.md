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
