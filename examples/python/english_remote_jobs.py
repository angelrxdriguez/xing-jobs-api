"""English-language, remote or hybrid jobs in Germany paying at least EUR 60,000 a year.

Filters run inside the scraper: jobs that don't match are skipped and not charged.

Usage:
    APIFY_TOKEN=... python examples/python/english_remote_jobs.py
"""
import json
import os
from decimal import Decimal

from apify_client import ApifyClient

ACTOR = "angelrxdriguez/xing-jobs-scraper"


def dataset_id(run):
    return run["defaultDatasetId"] if isinstance(run, dict) else run.default_dataset_id


def main():
    client = ApifyClient(os.environ["APIFY_TOKEN"])
    run = client.actor(ACTOR).call(
        run_input={
            "mode": "search",
            "keywords": ["software engineer", "data engineer", "devops"],
            "locations": ["Berlin", "München", "Hamburg", "Frankfurt am Main"],
            "languages": ["en"],
            "workplace": ["remote", "hybrid"],
            "minSalary": 60000,
            "maxPagesPerSearch": 10,
            "maxItems": 300,
        },
        max_total_charge_usd=Decimal("0.50"),
    )
    jobs = list(client.dataset(dataset_id(run)).iterate_items())
    with open("english_remote_jobs.json", "w", encoding="utf-8") as f:
        json.dump(jobs, f, ensure_ascii=False, indent=2)
    print(f"Saved {len(jobs)} jobs to english_remote_jobs.json")
    for job in sorted(jobs, key=lambda j: -(j.get("salaryMax") or 0))[:10]:
        print(f"{job.get('salaryMax') or '?':>7} EUR  {job['workplace']:<7} {job['title']} — {job['company']} ({job.get('city')})")


if __name__ == "__main__":
    main()
