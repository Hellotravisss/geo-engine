#!/usr/bin/env bash
# Quick status + verdict + usage for the launched session.
set -euo pipefail
cd "$(dirname "$0")"
set -a; source .env; source IDS.env; set +a
BASE=https://api.anthropic.com/v1
AUTH=(-H "x-api-key: $ANTHROPIC_API_KEY" -H "anthropic-version: 2023-06-01" \
      -H "anthropic-beta: managed-agents-2026-04-01" -H "content-type: application/json")
curl -sS "${AUTH[@]}" "$BASE/sessions/$SESSION_ID" -o /tmp/geo_poll.json
python3 -c "import json;d=json.JSONDecoder(strict=False).decode(open('/tmp/geo_poll.json').read());print('status :',d.get('status'));print('verdict:',[e.get('result') for e in d.get('outcome_evaluations',[])]);print('usage  :',d.get('usage') or {})"
