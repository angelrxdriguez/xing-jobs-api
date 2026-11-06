# Xing Jobs API — examples

Code examples for getting job postings from **[Xing](https://www.xing.com/jobs)**, the leading
professional network in Germany, Austria and Switzerland (DACH), as structured data. They use the
**[Xing Jobs Scraper](https://apify.com/angelrxdriguez/xing-jobs-scraper)** on Apify.

Each job includes:

- title, company, city, region and postal code
- **salary range**: real, or Xing's estimate, flagged with `salaryIsEstimate`
- **remote / hybrid / on-site**, employment type, career level, discipline and industry
- **language of the ad**, so you can find English-speaking jobs in Germany
- keywords, a summary of responsibilities, company size and company page
- full description, posting and expiry dates, and the apply link

```
title              Python Developer Financial Services (all genders)
company            Exxeta
city               Berlin
workplace          hybrid
employmentType     FULL_TIME
careerLevel        Mit Berufserfahrung
salaryMin–Max      59,000–86,000 EUR (estimate)
```

See [`sample_output.json`](sample_output.json) for complete records.

📖 Step-by-step tutorial: [Get every new Xing job, with salaries, into a spreadsheet every morning](https://dev.to/angelrxdriguez/get-every-new-xing-job-with-salaries-into-a-spreadsheet-every-morning-3cjc)

## Quick start

1. Create a free account on [Apify](https://console.apify.com/sign-up) and copy your API token from
   **Settings → API & Integrations**.
2. Set it as an environment variable:

   ```bash
   export APIFY_TOKEN="your-token"        # macOS / Linux
   setx APIFY_TOKEN "your-token"          # Windows (open a new terminal afterwards)
   ```
3. Run an example:

   ```bash
   pip install -r requirements.txt
   python examples/python/quickstart.py
   ```

No code at all? Open the [Actor page](https://apify.com/angelrxdriguez/xing-jobs-scraper), fill in
the form and download the results as Excel, CSV or JSON.

## Examples

| File | What it does |
|---|---|
| [`examples/python/quickstart.py`](examples/python/quickstart.py) | Search Python jobs in Berlin and print them |
| [`examples/python/english_remote_jobs.py`](examples/python/english_remote_jobs.py) | English-language, remote or hybrid jobs paying at least €60k |
| [`examples/python/daily_feed_to_csv.py`](examples/python/daily_feed_to_csv.py) | **Daily feed:** append only the jobs that are new since the last run to a CSV |
| [`examples/node/quickstart.mjs`](examples/node/quickstart.mjs) | The quick start in Node.js |
| [`examples/http/run_sync.sh`](examples/http/run_sync.sh) | Plain HTTP with `curl`, no library needed |

## Two ways to collect jobs

**Search** by keywords and cities. Every keyword is searched in every city, within a 20 km radius.

```json
{ "mode": "search", "keywords": ["data engineer"], "locations": ["München", "Wien"] }
```

**Feed** of every new job on Xing, built from Xing's public sitemaps (~500,000 active jobs). Combine
it with `onlyNewJobs` and a schedule to get a daily feed:

```json
{ "mode": "feed", "feedCities": ["Berlin", "Hamburg"], "onlyNewJobs": true, "stateKey": "berlin-hamburg" }
```

## Filters

Jobs that don't match a filter are skipped, and **you are not charged** for them.

| Input | Example |
|---|---|
| `employmentTypes` | `["FULL_TIME", "PART_TIME", "CONTRACTOR", "INTERN"]` |
| `workplace` | `["remote", "hybrid"]` |
| `languages` | `["en"]`, ads written in English |
| `minSalary` | `60000`, yearly in EUR (`includeEstimatedSalaries: false` to ignore Xing's estimates) |
| `postedWithinDays` | `7` |

## Pricing

$1 per 1,000 jobs, plus $0.00005 per run. Apify's free plan includes monthly credits you can use to
try it. To cap the cost of a run, pass `max_total_charge_usd` as in the Python examples.

## Data and compliance

The scraper only uses pages that Xing's `robots.txt` allows for all crawlers and collects **job
postings only**, never people's profiles. By default it removes e-mail addresses and phone numbers
from descriptions. You are responsible for using the data in line with Xing's terms and applicable
law, such as GDPR.

## License

The examples in this repository are MIT-licensed. The scraper itself runs on Apify and is a paid
service.
