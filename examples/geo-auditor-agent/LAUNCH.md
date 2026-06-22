# geo-auditor — launch runbook

A read-only, on-demand **GEO audit agent**: hand it a URL + target questions → it writes a scored 6-dimension GEO audit + roadmap. v0 target: `canpayinsights.ca`.

## Prerequisite — your API key (one time)
Create an API key at **platform.claude.com → API keys** (note which **workspace** it's in — the Console only shows that workspace's agents). Put it in `my-agent/.env`:

```
ANTHROPIC_API_KEY=sk-ant-...
```
`.env` is chmod 600 and git-ignored. The key never goes anywhere else. Runs cost cents; `max_iterations: 3` caps each run.

## Launch (resumable)
```bash
cd my-agent
bash launch.sh        # env → agent → session → outcome kickoff. Re-run safe (skips what exists).
bash poll.sh          # status + verdict + usage. Run a few times; an audit run takes a few minutes.
bash fetch.sh         # downloads the report → outputs/geo-audit-report.md
```
`launch.sh` reads `IDS.env` first and skips any object already created, so if a step fails you can just run it again.

## What each file is
| File | Role |
|---|---|
| `agent-system.md` | The agent's brain — the GEO audit method (edit this to change how it audits). |
| `agent.meta.json` | Agent config minus the system prompt (name, model, tools). `launch.sh` merges the two into `agent.json`. |
| `environment.json` | The 📦 environment (cloud, unrestricted networking). |
| `first_prompt.txt` + `outcome.md` | The task + the rubric. `launch.sh` builds `kickoff.json` from them. |
| `evals/` | case-01 = canpayinsights (v0 input) · case-02 = traviszhang (held) · case-03 = a competitor (held). |
| `launch.sh` / `poll.sh` / `fetch.sh` | Create+kickoff · watch · download. |
| `IDS.env` | Live IDs, appended as objects are created. |

## After the first run
- Read `outputs/geo-audit-report.md` against `outcome.md`. If it's genuinely good, save it as `evals/case-01/expected.md` (the regression baseline).
- Re-point at another site: edit `first_prompt.txt` (URL + target questions) and re-run `launch.sh` (clear `SESSION_ID` from `IDS.env` first for a fresh run), or just create a new session.
- Run the held-back cases: `bash evals/run-evals.sh`.

## Iterate (change ONE thing)
- Sharper rubric → edit `outcome.md`, new session, re-kickoff (no version bump — the rubric lives in the kickoff, not the agent).
- Better method / add the `pdf` skill → edit `agent-system.md` / `agent.meta.json`, then **update** the agent (new version): `curl -sS "$BASE/agents/$AGENT_ID" "${AUTH[@]}" -d '{"version":'$AGENT_VERSION',"system":"..."}'`, then bump `AGENT_VERSION` in `IDS.env`.

## Console
Sessions / traces: `https://platform.claude.com/workspaces/<workspace>/sessions/<SESSION_ID>` (use `default` for `<workspace>` unless your key lives elsewhere — Settings → API Keys shows which).
