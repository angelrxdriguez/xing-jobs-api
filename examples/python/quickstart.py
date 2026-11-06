"""Search Python jobs in Berlin on Xing and print them.

Usage:
    pip install -r requirements.txt
    APIFY_TOKEN=... python examples/python/quickstart.py
"""
import os
from decimal import Decimal

from apify_client import ApifyClient

ACTOR = "angelrxdriguez/xing-jobs-scraper"


def dataset_id(run):
    # apify-client >= 3 returns a model object, older versions return a dict
    return run["defaultDatasetId"] if isinstance(run, dict) else run.default_dataset_id


def main():
    client = ApifyClient(os.environ["APIFY_TOKEN"])
    run = client.actor(ACTOR).call(
        run_input={
            "mode": "search",
            "keywords": ["python"],
            "locations": ["Berlin"],
            "maxItems": 50,
        },
        max_total_charge_usd=Decimal("0.10"),  # never spend more than $0.10 on this run
    )
    for job in client.dataset(dataset_id(run)).iterate_items():
        if job.get("salaryMin"):
            salary = f"{job['salaryMin']:,}-{job['salaryMax']:,} {job['salaryCurrency']}"
            if job.get("salaryIsEstimate"):
                salary += " (estimate)"
        else:
            salary = "no salary"
        print(f"{job['title']} | {job['company']} | {job.get('city')} | {job.get('workplace') or '-'} | {salary}")
        print(f"    {job['url']}")


if __name__ == "__main__":
    main()
