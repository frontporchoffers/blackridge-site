# Blackridge Roofing Organic #1 Plan (90-day) — v2 (post-fable)

Target: hyperlocal roofing dominance first (Ankeny / Johnston / WDM / Beaverdale), let authority spread to "roofing Des Moines." Plan built via claude-seo-main sub-skills (seo-plan, seo-local, seo-geo/AISEO, seo-schema, seo-audit), then independently hardened by fable-checker. All 5 fable findings integrated below.

**Execution order revised: sub-service pages → hyperlocal consolidation → blog + authority workstreams in parallel → pillar rebuild last.** (Original 3→2→1 order burned the Aug–Sep Iowa storm season with informational blog content while transactional queries went uncovered.)

---

## Immediate surgical fixes (do this week — 30 min work)

Not strategy. Bugs found by the audit that hurt conversion and quality signals every day they wait.

**`/services/roofing.html` copy — em-dash strip left 4 broken sentences:**
- Line 270: "attention to detail. no shortcuts, no surprises." — restore comma
- Line 281: "premium shingles or metal. installed the right way." — restore comma
- Line 323: "Nofees, no change orders" — missing space, restore " No fees,"
- Line 396: "Roofing FAQs. Answered by Our Team" — restore " — " → but no em-dashes per voice rule, so " · " or comma
- Line 463 testimonial: `"...claim too.". Chris B.` mangled — restore quote flow

**Schema fixes on `/services/roofing.html`:**
- Add `streetAddress: "1615 SW Main St"` to PostalAddress (currently missing though footer shows it)
- Change `@type` from `LocalBusiness` → `RoofingContractor`
- Add `geo` with 5-decimal lat/lng (Ankeny: 41.72917, -93.60591)
- Add `priceRange: "$$"`
- Add `dateModified` to schema

**`robots.txt`:** already open (`User-agent: * / Allow: /`) — nothing to add. AI crawlers not blocked.

**Broken favicon path:** line 20 references `pictures/...` but should be `../pictures/...` (service page depth).

---

## Move 1 — Sub-service transactional pages (weeks 1–3) — MOVED UP

Storm season is Aug–Sep. Transactional queries ("roof repair Ankeny," "storm damage roof Des Moines," "roof inspection Iowa") spike now. These pages go first.

Create under `/services/roofing/`:
- `/services/roofing/repair` — 800–1,200 words
- `/services/roofing/replacement` — 800–1,200 words
- `/services/roofing/storm-damage` — 800–1,200 words (front-load hail + wind)
- `/services/roofing/inspection` — 800–1,200 words

Each:
- Dedicated Service schema per page
- 134–167 word answer block front-loaded (AI citation optimal length)
- CTA + click-to-call above fold
- 2–3 real Drew photos each (from the roofing-jpg folder just delivered)
- Internal link back to `/services/roofing` (pillar) + 2 relevant `/areas/{city}` pages

## Move 2 — Consolidate into existing `/areas/` city pages (weeks 3–6)

**Original mistake:** creating new `/roofing-johnston`, `/roofing-ankeny`, etc. would cannibalize the 15 existing script-generated `/areas/{city}.html` pages and stack a second doorway-page layer on top of the one PROGRESS.md line 60 already diagnoses (~20 sitemap URLs uncrawled by Google).

**Corrected approach:** deep-enhance the 4 highest-priority existing `/areas/` pages with roofing-specific content:
- `/areas/ankeny.html` — home base
- `/areas/johnston.html` — already ranking #1.78 for "general contractor Johnston," pivot to roofing
- `/areas/west-des-moines.html` — highest income
- `/areas/beaverdale.html` — wait, need to check if this exists (not in listed 15) — if not, add it or use `/areas/des-moines.html`

Each enhanced page:
- Push to 1,500+ words with >60% unique content (RicketyRoo swap test — if you can swap city name and it still reads, Google penalizes as doorway)
- Neighborhood-specific: housing stock era (Beaverdale = 1920s–40s bungalows, WDM = 90s–2020s mixed), storm history, local permit process
- 3–4 real local photos each
- Roofing-specific FAQ per city
- `LocalBusiness` → `RoofingContractor` schema with `areaServed` = just that city

**Prune or 301-redirect the weakest of the other 11 `/areas/` pages** — the thin ones are burning crawl budget and reinforcing the doorway signal. Keep only those with a real client story or unique local content.

## Move 3 — Blog calendar (weeks 1–20, runs in parallel from day one)

Roofing-first calendar locked from prior message. First post = *Iowa Hail Damage: How to Spot It on Your Roof* (Aug 10 slot, storm season live). Every post:
- First 60 words = self-contained definition + direct answer
- One 134–167 word answer block per H2
- `Article` schema with `dateModified`, author = "Drew Heberer"
- Internal link to pillar + relevant sub-service page + relevant `/areas/{city}` page
- Real photos from Drew's roll (27 JPGs available, minus the 1 Italy shot)

## Move 4 — Pillar rebuild (weeks 8–10) — LAST

`/services/roofing` grows to 2,500–3,000 words. Structure:
1. Hero opens with 134–167 word AI-citable definition block (materials cost, timeline, when-to-replace)
2. Materials comparison table (asphalt / metal / cedar / EPDM: cost, lifespan, Iowa fit, warranty)
3. Iowa storm playbook (hail damage, first-72-hour homeowner checklist)
4. Insurance claim walkthrough (5-step process, adjuster expectations)
5. Neighborhood callouts → link to enhanced `/areas/{city}` pages
6. Sub-service anchor links → link to `/services/roofing/{sub}` pages
7. Expanded FAQ (add "What roofing materials handle Iowa hail best?" + "Do I need a permit to replace my roof in Des Moines?")

---

## Authority workstream (weeks 1–12) — added, was missing entirely

**This is the treatment for the diagnosed disease.** PROGRESS.md line 65: "relevance OK, authority weak. avg position 47." Content and technical work won't lift positions past the teens without this.

Week 1 (start now):
- **BBB accreditation** — finish application (already pending per memory)
- **Iowa HBA membership** — on hold per memory (cost). Revisit when cash flow allows; still the single biggest local roofing backlink
- **GAF certified contractor directory** — apply. High-DA manufacturer directory, standard roofer play, free listing on GAF's find-a-contractor tool
- **Owens Corning Preferred Contractor** — same play, second manufacturer
- **CertainTeed SELECT ShingleMaster** — third manufacturer if bandwidth
- **Angi / HomeAdvisor** — free tier listing (real backlinks, not just leads)
- **Nextdoor business page** — hyperlocal signal + reviews

Ongoing:
- Local news pitch: send Drew's storm-response story to Des Moines Register + WHO-TV storm coverage desk (spring/summer storms are recurring news; roofers who show up in coverage get high-DA links)
- Realtor partner one-pager: keep following up on the 5 realtor recipients; each realtor referral is worth more than any content post

---

## Off-site (weeks 1–4) — trimmed

**Kept:**
- GBP primary category → Roofing Contractor (single biggest ranking lever — Drew confirm)
- Bing Places claim (ChatGPT, Copilot, Alexa source)
- Apple Business Connect claim (Apple Maps + Siri)
- Data aggregator submissions: Data Axle, Foursquare, Neustar/TransUnion (one-time push)
- Review velocity: 1–2 new Google reviews per 18-day window, mention "roof" or "roofing" in body
- `/llms.txt` publish (5-min task, low weight but low cost)

**Cut per fable (overweight for a 1–2 person op):**
- ~~Monthly YouTube channel~~ — opportunistic only, phone footage OK, embed when a job produces obvious content
- ~~8 Reddit mentions/quarter~~ — no forced cadence, show up if you see a relevant thread but zero recurring labor
- ~~robots.txt AI allowlist~~ — no-op, already allowed

---

## KPI targets (90 day) — leads row added

| Metric | Baseline (7/28) | 30 day | 60 day | 90 day |
|---|---|---|---|---|
| **Calls + form fills / month** | (need baseline) | +25% | +50% | +100% |
| Clicks / month | 40 | 55 | 80 | 120 |
| Impressions / month | 6,195 | 8,000 | 12,000 | 18,000 |
| Indexed pages | 13 | 18 | 24 | 30+ |
| Avg position across roofing queries | 47 | 32 | 22 | 12 |
| Position "roofing Ankeny" | TBD | top 10 | top 5 | top 3 |
| Position "roofing Johnston" | ~15 | top 8 | top 5 | top 3 |
| Position "roofing Des Moines" | mid-30s | top 25 | top 15 | top 10 |
| Google reviews | 2 | 4 | 6 | 8+ |
| High-DA backlinks (BBB, HBA, manufacturer directories, news) | ~5 | 8 | 12 | 15+ |

---

## What could break this plan

- **GBP category is wrong** — nothing else compensates. Verify week 1.
- **Reviews don't grow** — 18-day rule, rankings cliff at 3 weeks.
- **`/areas/` cleanup gets skipped** — thin doorway pages actively pull down Google's quality assessment of the whole domain.
- **Authority workstream stalls** — content will land, positions stall in the teens. This is the true bottleneck, not content volume.
- **Sub-service pages miss storm season** — August–September window is when transactional queries spike; miss it and next real chance is spring 2027.
