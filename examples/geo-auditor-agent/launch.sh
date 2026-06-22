#!/usr/bin/env bash
# geo-auditor — resumable launch. Safe to re-run: reads IDS.env and skips what already exists.
set -euo pipefail
cd "$(dirname "$0")"

if [ ! -f .env ]; then echo "Missing .env (ANTHROPIC_API_KEY). See LAUNCH.md."; exit 1; fi
set -a; source .env; set +a
[ -f IDS.env ] && { set -a; source IDS.env; set +a; }
: "${ANTHROPIC_API_KEY:?ANTHROPIC_API_KEY not set in .env}"

BASE=https://api.anthropic.com/v1
AUTH=(-H "x-api-key: $ANTHROPIC_API_KEY" -H "anthropic-version: 2023-06-01" \
      -H "anthropic-beta: managed-agents-2026-04-01" -H "content-type: application/json")
MODEL=${MODEL:-claude-opus-4-8}

pyget(){ python3 -c "import json,sys;print(json.JSONDecoder(strict=False).decode(open(sys.argv[1]).read())[sys.argv[2]])" "$1" "$2"; }
check(){ python3 -c "import json,sys;d=json.JSONDecoder(strict=False).decode(open(sys.argv[1]).read());sys.exit(1 if d.get('type')=='error' else 0)" "$1" || { echo 'API error:'; cat "$1"; echo; exit 1; }; }

echo '==> available models (newest Opus-class is the default):'
curl -sS "${AUTH[@]}" "$BASE/models" -o /tmp/geo_models.json -w '  http %{http_code}\n' || true
python3 -c "import json;d=json.load(open('/tmp/geo_models.json'));print('   '+', '.join(m['id'] for m in d.get('data',[])[:8]))" 2>/dev/null || true

# 1) environment
if [ -z "${ENV_ID:-}" ]; then
  echo '==> creating environment...'
  curl -sS "${AUTH[@]}" "$BASE/environments" -d @environment.json -o /tmp/geo_env.json -w '  http %{http_code}\n'
  check /tmp/geo_env.json
  ENV_ID=$(pyget /tmp/geo_env.json id); echo "ENV_ID=$ENV_ID" >> IDS.env
  echo "✅ 📦 environment $ENV_ID"
else echo "↺ environment exists: $ENV_ID"; fi

# 2) agent (assemble agent.json = meta + system file, then create)
if [ -z "${AGENT_ID:-}" ]; then
  echo '==> assembling agent.json + creating agent...'
  MODEL="$MODEL" python3 -c "import json,os;m=json.load(open('agent.meta.json'));m['model']=os.environ['MODEL'];m['system']=open('agent-system.md').read();json.dump(m,open('agent.json','w'),indent=2,ensure_ascii=False)"
  curl -sS "${AUTH[@]}" "$BASE/agents" -d @agent.json -o /tmp/geo_agent.json -w '  http %{http_code}\n'
  check /tmp/geo_agent.json
  AGENT_ID=$(pyget /tmp/geo_agent.json id); AGENT_VERSION=$(pyget /tmp/geo_agent.json version)
  { echo "AGENT_ID=$AGENT_ID"; echo "AGENT_VERSION=$AGENT_VERSION"; } >> IDS.env
  echo "✅ 🤖 agent $AGENT_ID (v$AGENT_VERSION, $MODEL)"
else echo "↺ agent exists: $AGENT_ID (v${AGENT_VERSION:-?})"; fi

# 3) session
if [ -z "${SESSION_ID:-}" ]; then
  echo '==> creating session...'
  AGENT_ID="$AGENT_ID" ENV_ID="$ENV_ID" python3 -c "import json,os;json.dump({'agent':os.environ['AGENT_ID'],'environment_id':os.environ['ENV_ID'],'title':'canpayinsights.ca — GEO audit'},open('/tmp/geo_sreq.json','w'))"
  curl -sS "${AUTH[@]}" "$BASE/sessions" -d @/tmp/geo_sreq.json -o /tmp/geo_sess.json -w '  http %{http_code}\n'
  check /tmp/geo_sess.json
  SESSION_ID=$(pyget /tmp/geo_sess.json id); echo "SESSION_ID=$SESSION_ID" >> IDS.env
  echo "✅ ▶️ session $SESSION_ID"
else echo "↺ session exists: $SESSION_ID"; fi

# 4) kickoff (build the outcome event from first_prompt.txt + outcome.md)
echo '==> sending outcome kickoff...'
python3 -c "import json;task=open('first_prompt.txt').read();rub=open('outcome.md').read();json.dump({'events':[{'type':'user.define_outcome','description':task,'rubric':{'type':'text','content':rub},'max_iterations':3}]},open('kickoff.json','w'),ensure_ascii=False,indent=2)"
curl -sS "${AUTH[@]}" "$BASE/sessions/$SESSION_ID/events" -d @kickoff.json -o /tmp/geo_evt.json -w '  http %{http_code}\n'
check /tmp/geo_evt.json
echo "✅ 🎯 outcome kickoff sent → session $SESSION_ID"
echo
echo "Watch it:   bash poll.sh     (run a few times; or watch in the Console)"
echo "Get report: bash fetch.sh    (once status = idle/terminated and the verdict has landed)"
