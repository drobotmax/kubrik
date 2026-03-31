> Source: https://support.google.com/analytics/answer/9826983?hl=en

For downgrading Google Analytics properties, and other 360 products generally, to standard, refer to [Downgrading from 360 to standard](https://support.google.com/marketingplatform/answer/9013959).

For downgrading Google Analytics properties to standard, refer to the [Upgrading/downgrading to/from 360 section of this article](https://support.google.com/analytics/answer/9826983?hl=en#upgrade-downgrade).

Given the recent suspension of Google advertising systems in Russia, we’ll be pausing the creation of new Russian 360 accounts on Analytics and Tag Manager. Additionally, we will pause ads on Google properties and networks globally for advertisers based in Russia.

## 360 feature limits

Google Analytics 360 provides higher limits for Google Analytics property data collection, reporting, retention, and export to BigQuery.

| Feature | Google Analytics properties (standard) | Google Analytics properties under Analytics 360 |
| --- | --- | --- |
| Event parameters | 25 per event 50 event-scoped custom dimensions per property 50 event-scoped custom metrics per property | 100 per event 125 event-scoped custom dimensions per property 125 event-scoped custom metrics per property |
| User properties | 25 per event | 25 per event |
| User-scoped custom dimensions | 25 per property | 100 per property |
| Conversions | 30 | 50 |
| Audiences | 100 | 400 |
| Explorations | 200 created per user per property 500 shared per property | 200 created per user per property 1000 shared per property |
| Explore sampling limits | 10M events per query | 1B events per query |
| Unsampled explorations | Not available | Unsampled results up to 50B events per day per property |
| API quotas Most requests consume fewer than 10 tokens. | 25,000 tokens per day | 250,000 tokens per day |
| Data retention | Up to 14 months Options: 2, 14 months | Up to 50 months Options: 2, 14, 26, 38, and 50 months [XL properties](https://marketingplatform.google.com/about/analytics_products/sla/): 2 months |
| BigQuery Export | Daily export: 1 M events Streaming export: unlimited | Daily export: Billions of events Streaming export: unlimited |
| Events per User per day (for app data streams) | 500 | 2000 |
| Distinctly named events There is no limit on the number of distinctly named events for _web_ data streams. | 500 per app instance (for app data streams) | 2000 per app instance (for app data streams) |
| Calculated metrics | 5 calculated metrics per standard property | 50 calculated metrics per 360 property |

## Upgrading/downgrading to/from 360

The self-service upgrade/downgrade option is only available to Analytics properties that are linked to a Google Marketing Platform organization that has an active 360 order ([learn more about orders](https://support.google.com/marketingplatform/answer/9013858#orders)). If you purchased Analytics through a Google Sales Partner, then the partner has to perform the service-level upgrade/downgrade.

Users who are either Org admins or Billing admins for the organization to which the Analytics account is linked can upgrade Google Analytics properties to or downgrade them from the 360 service level.

Sales Partners can set the service levels of properties for their clients. Sales Partner clients and Direct clients can set the service levels of their own properties. To set the service level of a property:

1.   [Sign in to Google Marketing Platform.](https://marketingplatform.google.com/home)
2.   Click **Administration > Organizations**.
3.   Click the relevant organization.
4.   Sales Partner: Click **Clients**, then click a client name. Under Linked accounts, select **Analytics**, then the specific account. Client: Under _Linked accounts_, select **Analytics**, then the specific account.
5.   Select the check box for the Google Analytics property you want to upgrade/downgrade.
6.   Click ![Image 1: More](https://lh3.googleusercontent.com/oLoRPrHJd7m46sWijX6zBWnEnfslP62AxJSwt5Nj0bNbpaYHz2pyscExleiofsH2kQ=h36), then click **Upgrade selected properties** or **Downgrade selected properties**.

When you upgrade a property the service level changes to 360; when you downgrade a property, the service level changes to standard. If you have the necessary permissions to change the service level for a property but the interface controls to upgrade/downgrade are not available, then there is no order for the account, the order end date has passed, or the order start date is set to a future date.

### Effects of upgrading

When you upgrade a Google Analytics property to 360, the property immediately benefits from the increased limits [described above](https://support.google.com/analytics/answer/9826983?hl=en#limits). In certain cases, the upgrade may take up to four hours to apply.

Upgrading a Google Analytics property to 360 will not impact billing for your Analytics account until the account has moved onto an Analytics 360 contract for Google Analytics properties. In addition, SLAs will not be available to upgraded properties until the account has moved onto an Analytics 360 contract for Google Analytics properties.

### Effects of downgrading

When you downgrade a Google Analytics property from 360 to standard, that property is immediately subject to the standard limits [described above](https://support.google.com/analytics/answer/9826983?hl=en#limits).

If the property currently exceeds those limits because of the previous upgrade to 360, then you have to bring the property within the standard limits before you can create objects or change settings that would cause the property to exceed the standard limits. For example, if you marked more than 30 events as conversions while the property was 360 and want to mark a new event as a conversion, you have to unmark events until you're below the limit of 30.

##