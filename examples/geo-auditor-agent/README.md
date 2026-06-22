# geo-auditor — GEO audit as a hosted agent

Turns the `geo-engine` method into a **[Claude Managed Agent](https://platform.claude.com/docs/en/managed-agents/overview)** that audits any URL on demand and writes a scored GEO report + prioritized roadmap to `/mnt/session/outputs/geo-audit-report.md`.

The agent's "brain" is `agent-system.md` (the audit method); the task + definition of done are `first_prompt.txt` + `outcome.md`.

## Use it

```bash
cp .env.example .env        # add your ANTHROPIC_API_KEY (platform.claude.com → API keys)
bash launch.sh              # creates environment → agent → session → sends the audit kickoff
bash poll.sh                # status + the grader's verdict (a run takes a few minutes)
bash fetch.sh               # downloads outputs/geo-audit-report.md
```

`launch.sh` is resumable (it reads `IDS.env` and skips anything already created). To audit a different site, edit `first_prompt.txt` (URL + target questions) and start a fresh session.

## Files
- `agent-system.md` — the audit method (the system prompt).
- `agent.meta.json` — agent config (name, model, tools); `launch.sh` merges it with `agent-system.md` into the create payload.
- `environment.json` — the cloud sandbox.
- `first_prompt.txt` + `outcome.md` — the task + the rubric the run is graded against.
- `evals/` — example inputs across archetypes; `case-01/expected.md` is a **real sample audit output**.

## A real sample output
See `evals/case-01/expected.md` — a full scored GEO audit of canpayinsights.ca produced by this agent.

> Costs cents per run; `max_iterations: 3` caps each run. Never commit your `.env`.
