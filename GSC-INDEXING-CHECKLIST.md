# GSC Request Indexing Checklist

**Started:** 2026-04-20
**25 URLs total, paced across 3 days to stay under GSC's daily quota**

How to use: open Google Search Console → paste URL into top search bar → click "Request Indexing" → check the box below. If GSC says "Quota exceeded," stop for the day and resume tomorrow.

---

## Day 1 — Mon 2026-04-20: Revenue services + top 2 suburbs (9 URLs)

- [x] https://blackridgecontractor.com/services/roofing
- [x] https://blackridgecontractor.com/services/kitchen-remodeling
- [x] https://blackridgecontractor.com/services/bathroom-remodeling
- [x] https://blackridgecontractor.com/services/basement-finishing
- [x] https://blackridgecontractor.com/services/remodeling
- [x] https://blackridgecontractor.com/services/gutters
- [x] https://blackridgecontractor.com/services/interior-painting
- [x] https://blackridgecontractor.com/areas/waukee
- [x] https://blackridgecontractor.com/areas/clive

## Day 2 — Tue 2026-04-21: Remaining affluent areas + trust pages (8 URLs)

- [ ] https://blackridgecontractor.com/areas/altoona
- [ ] https://blackridgecontractor.com/areas/grimes
- [ ] https://blackridgecontractor.com/areas/windsor-heights
- [ ] https://blackridgecontractor.com/areas/pleasant-hill
- [ ] https://blackridgecontractor.com/areas/norwalk
- [ ] https://blackridgecontractor.com/about
- [ ] https://blackridgecontractor.com/portfolio
- [ ] https://blackridgecontractor.com/blog/

## Day 3 — Wed 2026-04-22: Smaller areas + blog content (8 URLs)

- [ ] https://blackridgecontractor.com/areas/bondurant
- [ ] https://blackridgecontractor.com/areas/polk-city
- [ ] https://blackridgecontractor.com/areas/carlisle
- [ ] https://blackridgecontractor.com/blog/roof-replacement-guide-central-iowa
- [ ] https://blackridgecontractor.com/blog/kitchen-remodel-cost-des-moines
- [ ] https://blackridgecontractor.com/blog/bathroom-remodel-ideas-iowa
- [ ] https://blackridgecontractor.com/blog/basement-finishing-ankeny-guide
- [ ] https://blackridgecontractor.com/blog/siding-gutter-maintenance-iowa

---

## Checkpoint — Mon 2026-04-27

- [ ] Open GSC Coverage report → filter "Discovered — currently not indexed"
- [ ] For any URL from Day 1 still listed: resubmit Request Indexing
- [ ] Do NOT resubmit any URL more than once per 7-day cycle (Google ignores spam resubmits)
- [ ] Log indexing movement in `Drew's Brain/Projects/Blackridge Contractor/GSC Indexing Log.md`

## Before you start Day 1

- [ ] Confirm Netlify redeploy is live: `curl -I https://blackridgecontractor.com/about` should return `200`
- [ ] Confirm new schema is live: view source on `/about`, search for `@id` — should find `https://blackridgecontractor.com/#business`
