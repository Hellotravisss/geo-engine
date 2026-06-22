#!/usr/bin/env bash
# Launch one session per eval case, pinned to the CURRENT agent version (regression check).
# Run after v0 passes. Sessions run server-side; poll them after (Console or poll loop printed below).
set -euo pipefail
cd "$(dirname "$0")/.."
set -a; source .env; source IDS.env; set +a
BASE=https://api.anthropic.com/v1
AUTH=(-H "x-api-key: $ANTHROPIC_API_KEY" -H "anthropic-version: 2023-06-01" \
      -H "anthropic-beta: managed-agents-2026-04-01" -H "content-type: application/json")
: "${AGENT_ID:?run launch.sh first}"; : "${AGENT_VERSION:?}"; : "${ENV_ID:?}"
RES="evals/results-v${AGENT_VERSION}.json"; echo "[]" > "$RES"

for d in evals/case-*/; do
  name=$(basename "$d"); [ -f "$d/input.txt" ] || continue
  AID="$AGENT_ID" VER="$AGENT_VERSION" ENV="$ENV_ID" NAME="$name" \
    python3 -c "import json,os;json.dump({'agent':{'type':'agent','id':os.environ['AID'],'version':int(os.environ['VER'])},'environment_id':os.environ['ENV'],'title':'eval '+os.environ['NAME']},open('/tmp/geo_ev_s.json','w'))"
  sid=$(curl -sS "${AUTH[@]}" "$BASE/sessions" -d @/tmp/geo_ev_s.json | python3 -c "import json,sys;print(json.JSONDecoder(strict=False).decode(sys.stdin.read())['id'])")
  IN="$d/input.txt" python3 -c "import json,os;task=open(os.environ['IN']).read();rub=open('outcome.md').read();json.dump({'events':[{'type':'user.define_outcome','description':task,'rubric':{'type':'text','content':rub},'max_iterations':3}]},open('/tmp/geo_ev_k.json','w'),ensure_ascii=False)"
  curl -sS "${AUTH[@]}" "$BASE/sessions/$sid/events" -d @/tmp/geo_ev_k.json >/dev/null
  echo "▶️ $name → session $sid"
  RES="$RES" NAME="$name" SID="$sid" python3 -c "import json,os;p=os.environ['RES'];a=json.load(open(p));a.append({'case':os.environ['NAME'],'session':os.environ['SID'],'verdict':None});json.dump(a,open(p,'w'),indent=2)"
done
echo
echo "Eval sessions launched (running server-side). Recorded in $RES."
echo "Poll each, then fill in its verdict. Quick poll loop:"
echo "  for s in \$(python3 -c \"import json,os;print(' '.join(x['session'] for x in json.load(open('$RES'))))\"); do bash -c 'SESSION_ID='\$s' bash poll.sh' 2>/dev/null; done"
