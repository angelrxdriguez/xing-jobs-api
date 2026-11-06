// Search data engineer jobs in Munich on Xing and print them as a table.
//
// Usage:
//   npm install
//   APIFY_TOKEN=... node examples/node/quickstart.mjs
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });

const run = await client.actor('angelrxdriguez/xing-jobs-scraper').call({
    mode: 'search',
    keywords: ['data engineer'],
    locations: ['München'],
    maxItems: 50,
});

const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.table(items.map((job) => ({
    title: job.title,
    company: job.company,
    city: job.city,
    workplace: job.workplace,
    salary: job.salaryMin ? `${job.salaryMin}-${job.salaryMax} ${job.salaryCurrency}${job.salaryIsEstimate ? ' (est.)' : ''}` : '',
})));
