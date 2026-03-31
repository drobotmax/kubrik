> Source: https://support.google.com/analytics/answer/9358801?hl=en

BigQuery is a cloud data warehouse that lets you run highly performant queries of large datasets.

You can export all of your raw events from Google Analytics properties (including [subproperties](https://support.google.com/analytics/answer/11525732) and [roll-up properties](https://support.google.com/analytics/answer/11526039)) to BigQuery, and then use an SQL-like syntax to query that data. In BigQuery, you can choose to export your data to external storage or import external data for the purposes of combining it with your Analytics data.

When you export data to BigQuery, you own that data, and you can use BigQuery ACLs to manage permissions on projects and datasets.

A full export of data takes place once a day. Data is also exported continuously throughout the day. Learn more about [Streaming export](https://support.google.com/analytics/answer/9358801?hl=en#streaming-export).

You can export to a free instance of BigQuery ([BigQuery sandbox](https://cloud.google.com/bigquery/docs/sandbox?utm_source=support.google.com&utm_medium=referral&utm_campaign=ga4_bq_xsell_campaign&utm_content=from_page_Google%20Analytics_BigQuery_Export)), but [exports that exceed the sandbox limits incur charges](https://cloud.google.com/bigquery/docs/sandbox?utm_source=support.google.com&utm_medium=referral&utm_campaign=ga4_bq_xsell_campaign&utm_content=from_page_Google%20Analytics_BigQuery_Export#limitations).

Standard properties have a daily BigQuery Export limit of 1 million events. Learn more about [BigQuery Export limits](https://support.google.com/analytics/answer/9823238#limits).

**Notes**:

*   Requests to add product data that has been linked to Google Analytics are not being exported. BigQuery contains only the raw event data that Google Analytics receives from the client.
*   Once you export data from Analytics to BigQuery, you cannot re-export it.

**On this page**

*   [BigQuery Export types](https://support.google.com/analytics/answer/9358801?hl=en#export-types)
*   [Differences between the Google Analytics interface and BigQuery Export](https://support.google.com/analytics/answer/9358801?hl=en#differences-from-interface)
    *   [Streaming export](https://support.google.com/analytics/answer/9358801?hl=en#streaming)
    *   [Fresh Daily export](https://support.google.com/analytics/answer/9358801?hl=en#fresh-daily)

*   [Completeness signal](https://support.google.com/analytics/answer/9358801?hl=en#completeness-signal)
*   [The schedule for table updates](https://support.google.com/analytics/answer/9358801?hl=en#schedule)
*   [Cookieless pings and customer-provided data](https://support.google.com/analytics/answer/9358801?hl=en#cookieless-pings)
*   [Backfill “Not Available” traffic source dimensions](https://support.google.com/analytics/answer/9358801?hl=en#backfill-not-available)
*   [Google Analytics - Firebase Integration and BigQuery](https://support.google.com/analytics/answer/9358801?hl=en#firebase-bq)

* * *

## BigQuery Export types

Google Analytics offers the following BigQuery export options, each differing in data availability for the current day and should be chosen based on your data needs and budget:

| Export types | Best when you require... | Export details | Limits | Caveats |
| --- | --- | --- | --- | --- |
| **Daily export** (Standard, 360) | a complete set of data for the previous day and don't need data fast or aren't a 360 customer | Exports all the raw, unsampled event data once per day from the previous day Specific time not guaranteed Typically exports mid-afternoon in your property's timezone, but can be delayed until later in the day or the next day Last click observed, no modeling | Standard properties: up to 1M events per day, with filtering options to stay under limit 360 properties: up to 20B events per day | Some data, like user attribution, might be delayed by up to 24 hours; we recommend using daily export instead of streaming for user attribution data |
| **Fresh daily** (360) | faster, more complete data throughout the day | Data typically arrives by 5am Batched updates throughout the day, typically within 60 minutes Same schema as daily export Export begins based on property's timezone Last click observed, no modeling Much faster than the daily export | SLA is not available for the few XL properties | Only available for ["Normal" and "Large"](https://support.google.com/analytics/answer/11198161#property-categories) 360 properties. |
| **Streaming** (Standard, 360) | near realtime data (within minutes) | A realtime export of the current day's data Best-effort service: operates without a completeness SLO and may contain data gaps | No volume limits | New user and new session traffic source data is excluded from export |

**Note**: Each export will incur costs on the BigQuery side for storage and processing. You will incur additional BigQuery costs for using streaming export at the rate of $0.05 per gigabyte of data. 1 gigabyte equates to approximately 600,000 Google Analytics events, though that number will vary depending on event size. Learn more about [BigQuery pricing](https://cloud.google.com/bigquery/pricing?utm_source=support.google.com&utm_medium=referral&utm_campaign=ga4_bq_xsell_campaign&utm_content=from_page_GA4_BigQuery_Export#data_ingestion_pricing).

* * *

## Differences between the Google Analytics interface and BigQuery Export

The BigQuery event export provides access to raw event and user-level data, excluding any value additions that Google Analytics makes to the data found in standard reports and explorations. For this reason, the data from BigQuery event export might differ from the data in the Google Analytics interface.

To understand the differences between BigQuery event export and the Google Analytics interface, and explore ways to mitigate these differences when possible, see [Bridging the gap between Google Analytics UI and BigQuery export](https://developers.google.com/analytics/blog/2023/bigquery-vs-ui).

### Streaming export

You can choose the streaming export option when you [link your Google Analytics property to BigQuery](https://support.google.com/analytics/answer/9823238#step3).

BigQuery streaming export makes data for the current day available within a few minutes via BigQuery Export.

When you use this export option, BigQuery has more recent information you can analyze about your users and their traffic on your property.

For each day, streaming export creates one new table:

*   `events_intraday_YYYYMMDD`: An internal staging table that includes records of session activity that took place during the day. Streaming export is a best-effort operation and may not include all data for reasons such as the processing of late events and/or failed uploads. Data is exported continuously throughout the day. This table can include records of a session when that session spans multiple export operations.This table is deleted when `events_YYYYMMDD` is complete.

If you [select the daily option when you set up BigQuery Export](https://support.google.com/analytics/answer/9823238#step3), then the following table is also created each day.

*   `events_YYYYMMDD`: The full daily export of events.

You should query `events_YYYYMMDD` rather than `events_intraday_YYYYMMDD` so you're querying a stable dataset for the day.

See [BigQuery Export schema](https://support.google.com/analytics/answer/7029846#tables) for more information about the `events_YYYYMMDD` and `events_intraday_YYYYMMDD` tables.

BigQuery streaming export does not include the following user-attribution data for new users:

*   traffic_source.name (reporting dimension: User campaign)
*   traffic_source.source (reporting dimension: User source)
*   traffic_source.medium (reporting dimension: User medium)

User-attribution data for existing users is included but that data requires ~24 hours to fully process, so we recommend not relying on that data from the streaming export and instead getting user-attribution data from the full daily export.

You will incur additional BigQuery costs for using streaming export at the rate of $0.05 per gigabyte of data. 1 gigabyte equates to approximately 600,000 Google Analytics events, though that number will vary depending on event size. Learn more about[BigQuery pricing](https://cloud.google.com/bigquery/pricing?utm_source=support.google.com&utm_medium=referral&utm_campaign=ga4_bq_xsell_campaign&utm_content=from_page_Google%20Analytics_BigQuery_Export#data_ingestion_pricing).

### [](https://support.google.com/analytics/answer/9358801?hl=en)Fresh Daily export

You can now select Fresh Daily export in addition to Daily and Streaming export options. Fresh Daily export is currently available for Analytics 360 properties, and each of the 3 export options can be enabled independently of one another.

To configure Fresh Daily export, you must have billing set up on Google Cloud Platform. Learn more about the [BigQuery Fresh Daily export (GA360)](https://support.google.com/analytics/answer/15604391).

* * *

## [](https://support.google.com/analytics/answer/9358801?hl=en)Completeness signal

For GA360 customers using the Fresh Daily export, Google Analytics sends a completeness signal that informs you when all of the previous day’s data has been exported.

To access the completeness signal:

1.   Sign in to Cloud Logging and go to the “Logs Explorer” section.
2.   Search for "export complete".

The logs explorer may need to have the timestamp range increase; the message will typically occur around 5am in the property timezone.

You can view the Completeness Signal in the Log Router section of Cloud Logging, which can be pushed to Cloud Pub/Sub topics.

**Note**: Some changes in your Google Analytics property may cause the completeness signal to be missing or inaccurate on the first day. This includes instances such as:

*   After the property’s timezone is changed
*   After the BigQuery link is created for the property

## How the completeness signal works

* * *

## [](https://support.google.com/analytics/answer/9358801?hl=en)The schedule for table updates

Updates to the tables that are created as part of BigQuery Export are governed by the time zone of the Analytics property from which data is being exported. If the property time zone is changed, it will impact the BigQuery export, which may lead to data discrepancy or the daily export will be skipped.

Streaming-export tables (events_intraday_YYYYMMDD) are updated continuously throughout the day, from 12:00:00 am until 11:59:59 pm in the property's time zone. When a new day starts in the property's time zone, events are written to a new intraday table.

Daily export tables (events_YYYYMMDD) are created after Analytics collects all of the events for the day. Analytics will update daily tables for up to 2 calendar days, plus today beyond the date of the table with events that are timestamped with the date of the table, such as event bundles that come in late from Measurement Protocol or the Firebase SDKs. For example, if the table date is 20220101, then Analytics will update the table through 20220104 with events that are timestamped 20220101.

On occasion, Analytics may update the daily tables anytime after the 2-calendar-day window, plus today under circumstances that require Analytics to reprocess historical data, such as a bug fix that remedies a processing error.

* * *

## [](https://support.google.com/analytics/answer/9358801?hl=en)Cookieless pings and customer-provided data

When [consent mode](https://support.google.com/analytics/answer/9976101) is implemented, [cookieless](https://developers.google.com/tag-platform/tag-manager/server-side/consent-mode#GA4) pings collected by Analytics will be present in the BigQuery export, along with customer-provided data such as [user_id](https://developers.google.com/analytics/devguides/collection/ga4/reference/config#user_id) and [custom dimensions](https://support.google.com/analytics/answer/10075209).

* * *

## [Backfill “Not Available” traffic source dimensions](https://support.google.com/analytics/answer/9358801?hl=en)

You can use the following resources to lookup attributed traffic source dimensions for a given GCLID. Note that wBRAID and gBRAID identifiers aren't included in the BigQuery Export.

*   Google Ads API
*   Google Ads Scripts
*   BigQuery Data Transfer Service for Google Ads

To find the GCLID for a "Not Available" record in the "traffic_source" column, query the GCLID field in the “[collected_traffic_source](https://support.google.com/analytics/answer/7029846#tables&zippy=%2Ctraffic-source%2Ccollected-traffic-source)” column. For more details on how to lookup campaign information in Google Ads from a given GCLID, view [Backfill Google Ads traffic source data as soon as possible (GA 360)](https://developers.google.com/analytics/bigquery/backfill-traffic-source-data).

* * *

## [](https://support.google.com/analytics/answer/9358801?hl=en)Google Analytics - Firebase Integration and BigQuery

If a Google Analytics property and a Firebase project are [integrated](https://support.google.com/analytics/answer/9289234), they cannot be linked to separate BigQuery projects.

* * *

## Related resources

Visit the BigQuery Developers Guide to learn more about:

*   [Google Analytics and BigQuery](https://cloud.google.com/use-case/google-analytics-bigquery?utm_source=support.google.com&utm_medium=referral&utm_campaign=ga4_bq_xsell_campaign&utm_content=from_page_[Google%20Analytics]_BigQuery_Export)
*   [Google BigQuery](https://cloud.google.com/bigquery/docs?utm_source=support.google.com&utm_medium=referral&utm_campaign=ga4_bq_xsell_campaign&utm_content=from_page_Google%20Analytics_BigQuery_Export)
*   [BigQuery ACLs](https://cloud.google.com/bigquery/access-control?utm_source=support.google.com&utm_medium=referral&utm_campaign=ga4_bq_xsell_campaign&utm_content=from_page_Google%20Analytics_BigQuery_Export)
*   [BigQuery syntax](https://cloud.google.com/bigquery/docs/reference/legacy-sql?utm_source=support.google.com&utm_medium=referral&utm_campaign=ga4_bq_xsell_campaign&utm_content=from_page_Google%20Analytics_BigQuery_Export)