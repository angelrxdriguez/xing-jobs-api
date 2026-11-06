"""Daily feed: append the Xing jobs published since the last run to a CSV file.

Run it once a day (cron, Windows Task Scheduler, or GitHub Actions). Thanks to "onlyNewJobs",
each run only returns, and only charges for, jobs you have not received before.

Usage:
    APIFY_TOKEN=... python examples/python/daily_feed_to_csv.py
"""
import csv
import os
from decimal import Decimal
from pathlib import Path

from apify_client import ApifyClient

ACTOR = "angelrxdriguez/xing-jobs-scraper"
CSV_FILE = Path("xing_jobs.csv")
COLUMNS = ["datePosted", "title", "company", "city", "postalCode", "workplace", "employmentType",
           "careerLevel", "salaryMin", "salaryMax", "salaryCurrency", "salaryIsEstimate", "url", "applyUrl"]


def dataset_id(run):
    return run["defaultDatasetId"] if isinstance(run, dict) else run.default_dataset_id


def main():
    client = ApifyClient(os.environ["APIFY_TOKEN"])
    run = client.actor(ACTOR).call(
        run_input={
            "mode": "feed",
            "feedCities": ["Berlin", "Hamburg", "München"],
            "feedKeywords": ["entwickler", "developer", "engineer"],
            "onlyNewJobs": True,
            "stateKey": "daily-feed-example",  # use one key per feed you schedule
            "maxItems": 1000,
        },
        max_total_charge_usd=Decimal("1.00"),
    )
    new_file = not CSV_FILE.exists()
    count = 0
    with CSV_FILE.open("a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=COLUMNS, extrasaction="ignore")
        if new_file:
            writer.writeheader()
        for job in client.dataset(dataset_id(run)).iterate_items():
            writer.writerow(job)
            count += 1
    print(f"{count} new jobs appended to {CSV_FILE}")


if __name__ == "__main__":
    main()
