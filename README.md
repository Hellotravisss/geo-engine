# geo-engine

**Get your brand cited and recommended by AI answer engines** — ChatGPT, Perplexity, Google AI Overviews, Gemini, Claude, Copilot. A complete, opinionated [Claude Code](https://claude.com/claude-code) skill for **Generative Engine Optimization (GEO / AEO)**.

When someone asks an AI *"best Canadian take-home pay calculator"* or *"architectural photographer in Vancouver,"* GEO is the work that makes the AI name **your** brand. This repo packages a full engagement — **scope → audit → on-site → off-site → measure & report** — distilled from real builds, into a skill you can run on your own sites or use for client work.

## The one idea most "GEO checklists" miss

> **Off-site citations are the dominant lever — by far.** On-site work (schema, `llms.txt`, answer-first content) only makes you *eligible*. What actually moves AI recommendations is how many trusted places across the web cite or mention you — Reddit, "best-of" listicles, Wikidata, journalist/data mentions. This skill leads with that, and grades every recommendation by **evidence strength** — no hype, and no "guaranteed AI placement" (AI answers are non-deterministic and personalized).

## The leverage hierarchy (lead with the top, not the bottom)

1. 🔑 **Being cited / mentioned in third-party corpora** — the dominant lever by far (Reddit, Wikipedia/Wikidata, listicles, news).
2. 💎 **Original data, statistics & citations in your content** — markedly more likely to be cited by LLMs; doubles as outreach bait.
3. **Extractable answer structure** — answer-first, question-shaped headings, tables/FAQs.
4. **Structured data** (schema.org), 5. **Entity & authority** (Wikidata, E-E-A-T), 6. **Freshness**, 7. **AI-crawler access**.
8. `llms.txt` — cheap, harmless, *weak/speculative*. Ship it; never sell it as the thing that works.

## What's inside

- **`.claude/skills/geo-engine/`** — the skill: `SKILL.md` + 6 references:
  - `archetypes.md` · `audit-rubric.md` · `onsite-sop.md` · `schema-library.md` · `offsite-sop.md` · `measurement.md`
- **`examples/geo-auditor-agent/`** — a build kit that turns the method into a **running [Claude Managed Agent](https://platform.claude.com/docs/en/managed-agents/overview)**: hand it a URL, it audits the live site and writes a scored report + roadmap. Includes a real sample output in `evals/case-01/expected.md`.

## The engagement (5 phases)

| Phase | What it does |
|---|---|
| **0 · Scope & baseline** | Pick the archetype, define the target prompts, record where AI ranks you today. |
| **1 · Audit** | Score the site against the leverage hierarchy → a prioritized roadmap (quick wins vs strategic). |
| **2 · On-site** | AI-crawler access, `llms.txt`, structured data, answer-first content, original-data assets. |
| **3 · Off-site** | The real lever: Reddit, original-data outreach (HARO/Featured/Qwoted), listicles, Wikidata. |
| **4 · Measure & report** | Re-run the target prompts monthly across engines; track mention rate & share-of-voice. |

## Archetypes it covers

Service/local business · data/tool product · SaaS/B2B · ecommerce · publisher/content · directory/aggregator · personal brand / entity (a person or brand with no real website — optimize the entity, not a site) — each with its own priority order and copy-paste schema.

## Case studies (the method, applied to real sites)

- **CanPay Insights** ([canpayinsights.ca](https://canpayinsights.ca)) — *data/tool* archetype. A free Canadian payroll / take-home-pay calculator. The off-site & original-data playbook came from here.
- **Travis Zhang Photography** ([traviszhang.com](https://traviszhang.com)) — *service/local* archetype. A Vancouver architectural photographer. The on-site & entity playbook came from here.

> **Honest note:** GEO compounds over weeks–months. These show the method *applied*; AI-visibility is tracked over time and never guaranteed.

## Install

This is a Claude Code skill — copy it into your skills directory:

```bash
# Global (available in every project):
cp -R .claude/skills/geo-engine ~/.claude/skills/

# …or per-project: copy .claude/skills/geo-engine into your project's .claude/skills/
```

Then in Claude Code, run **`/geo-engine`**, or just ask it to *"do GEO on example.com."* It will scope, audit, and implement against the method above.

## Run it as an autonomous auditor (optional)

`examples/geo-auditor-agent/` builds a hosted agent that audits any URL on demand. You need an Anthropic API key. See `examples/geo-auditor-agent/LAUNCH.md`:

```bash
cd examples/geo-auditor-agent
cp .env.example .env          # add your ANTHROPIC_API_KEY
bash launch.sh                # env → agent → session → audit kickoff
bash poll.sh && bash fetch.sh # watch, then download the report
```

## Built by

**Travis Zhang (Qi Zhang)** — [traviszhang.com](https://traviszhang.com) · [canpayinsights.ca](https://canpayinsights.ca)

Available for GEO audits, implementation, and monthly retainers (individuals & companies): **info@traviszhang.com**

## License

[MIT](LICENSE) — use it, fork it, sell services with it.
