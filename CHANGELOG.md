# Changelog

All notable changes to **geo-engine**. Format loosely follows [Keep a Changelog](https://keepachangelog.com/).

## [1.3.1] — 2026-06-23
Tier-3 polish: GEO acronym disambiguated in the trigger description (fewer geography false-positives) + colloquial trigger verbs; `sr-only` hidden-H1 cloaking guardrail; honesty hedges (retrieval path dominant in 2026; structured data is "mostly hygiene", limited direct citation evidence).

## [1.3.0] — 2026-06-23
Second wave of self-review (Tier-2) fixes + changelog.
### Added
- `references/i18n.md` — **domestic / Chinese-market GEO**: domestic engines (豆包/Kimi/DeepSeek/文心/Baidu), the platform-first leverage shift (小红书/知乎/B站/公众号), domestic entity anchors (百度百科/高德/百度地图), and the two-program model for bilingual brands. Pointers added in `SKILL.md`.
- **Data-correctness audit check** — score whether the brand's *own* published figures/calculator outputs are correct and internally consistent (the CanPay stale-tax-constant failure mode); plus a schema "re-check values after any data change" pitfall.
- **Canonicalization + multi-locale** on-site guidance — one host/scheme/trailing-slash with a verify snippet; reciprocal `hreflang` + `x-default` + per-locale self-canonical.
- **Executable Wikidata steps** (`P31`/`P856`/external-IDs + referencing + the notability-deletion warning) and **GBP/review red lines** (no fake/incentivized reviews, no name-stuffing) + entity-consistency re-verify.
- **Off-site executable playbooks** — subreddit find-and-vet checklist (rules/karma/age gates); journalist response template + anti-fabrication / no-pay-to-pitch rules.
- **Measurement spine** — KPI operational definitions + AI-referral referrer allowlist + fixed competitor set; a multi-month **Trend** section; audit baseline reduced to report KPIs as **"month 0"**.
- Phase signposts on reference files.
### Changed
- Demoted Ahrefs Brand Radar from "enterprise backbone" to **optional paid instrumentation** (named alternatives: Profound, Peec AI, Otterly.AI, Semrush AI); manual method reaffirmed as the default.
- Reframed the case studies as proving the **method**, not archetype breadth (other types unvalidated).

## [1.2.0] — 2026-06-23
First wave of Tier-2 (folded into 1.3.0 notes above): China GEO file, measurement KPI/trend, off-site playbooks.

## [1.1.0] — 2026-06-23
Tier-1 self-review fixes from a multi-agent review.
### Added
- A real **scoring scheme** for the audit (status × evidence weight → group scores → overall **/100**) wired into the report Scorecard.
- **Live edge-robots verification** — fetch robots.txt *as an AI user-agent* to catch CDN/host overrides (e.g. Cloudflare AI Crawl Control silently blocking AI bots).
- **Directory / aggregator archetype** across SKILL, archetypes, schema (`CollectionPage`/`ItemList`), and off-site channels.
- Measurement **sampling control** (~3 runs/engine/month) + noise guidance.
- Colloquial trigger verbs ("rank in / show up in / get found by ChatGPT").
### Fixed
- Broken `robots.txt` template (`CCBot` missing `Allow:`); added `Claude-User`; made `onsite-sop.md §1` the single canonical bot list.
- Demoted the unsourced "~80%" claim to a labeled directional heuristic for internal consistency.

## [1.0.0] — 2026-06-21
Initial open-source release: the `geo-engine` skill (`SKILL.md` + 6 references), the `geo-auditor` Claude Managed Agent example, and two real case studies (CanPay = data/tool, traviszhang = service/local).
