#!/usr/bin/env bash
# Run the scraper and get the jobs back in a single HTTP call (no library needed).
# Usage: APIFY_TOKEN=... bash examples/http/run_sync.sh > jobs.json
set -euo pipefail

curl -sS -X POST \
  "https://api.apify.com/v2/acts/angelrxdriguez~xing-jobs-scraper/run-sync-get-dataset-items?format=json" \
  -H "Authorization: Bearer ${APIFY_TOKEN}" \
  -H "Content-Type: application/json" \
  -d '{
        "mode": "search",
        "keywords": ["python"],
        "locations": ["Berlin"],
        "maxItems": 20
      }'

# Other formats: replace format=json with format=csv or format=xlsx
