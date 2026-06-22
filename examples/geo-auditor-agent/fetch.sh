#!/usr/bin/env bash
# List the session's output files and download the audit report.
set -euo pipefail
cd "$(dirname "$0")"
set -a; source .env; source IDS.env; set +a
BASE=https://api.anthropic.com/v1
AUTH=(-H "x-api-key: $ANTHROPIC_API_KEY" -H "anthropic-version: 2023-06-01" \
      -H "anthropic-beta: managed-agents-2026-04-01" -H "content-type: application/json")
mkdir -p outputs
curl -sS "${AUTH[@]}" "$BASE/files?scope_id=$SESSION_ID" -o /tmp/geo_files.json
echo 'files in this session:'
python3 -c "import json;d=json.JSONDecoder(strict=False).decode(open('/tmp/geo_files.json').read());[print('  ',f['id'],f.get('filename')) for f in d.get('data',[])] or print('  (none yet)')"
FID=$(python3 -c "import json;d=json.JSONDecoder(strict=False).decode(open('/tmp/geo_files.json').read());c=[f for f in d.get('data',[]) if 'geo-audit' in (f.get('filename') or '')] or [f for f in d.get('data',[]) if (f.get('filename') or '').endswith('.md')];print(c[0]['id'] if c else '')")
if [ -n "$FID" ]; then
  curl -sS "${AUTH[@]}" "$BASE/files/$FID/content" -o outputs/geo-audit-report.md
  echo "saved → outputs/geo-audit-report.md"
else
  echo "no report yet — is the run finished? (bash poll.sh)"
fi
