> Source: https://support.google.com/analytics/answer/7667196?hl=en

The Google Analytics Data Retention controls give you the ability to set the amount of time before user-level and event-level data stored by Google Analytics is automatically deleted from Analytics servers.

## User and event data retention

The retention period applies to user-level and event-level data associated with cookies, user-identifiers, such as User-ID, and advertising identifiers, such as DoubleClick cookies, Android’s Advertising ID [AAID or AdID], Apple’s Identifier for Advertisers [IDFA].

You can choose how long Analytics retains data before automatically deleting it.

The maximum amount of time that Analytics will retain Google-signals data is 26 months, regardless of your settings. By default, Google signed-in data expires after 26 months. However, if the Analytics Data Retention setting is set to anything shorter than 26 months, the Google signed-in data will respect this shorter time frame.

## Google Analytics properties

For Google Analytics properties, you can set the retention period of user-level data to:

*   2 months
*   14 months

This retention period also applies to [key events](https://support.google.com/analytics/answer/9355848) data.

For all other event data, you can set retention to:

*   2 months
*   14 months
*   26 months (360 only)
*   38 months (360 only)
*   50 months (360 only)

The two-month retention period is always applied to age, gender, and interest data regardless of your settings.

When you increase the retention period it is applied to data that you have already collected. [Large and XL properties](https://support.google.com/analytics/answer/14207402) are limited to 2 months.

Learn more about data retention in [Google Analytics 360 (Google Analytics Properties)](https://support.google.com/analytics/answer/11202874).

Keep in mind that the data retention setting does not affect standard aggregated reports (including primary and secondary dimensions) in your Google Analytics property, even if you create comparisons in the reports. The data retention setting only affects explorations and funnel reports.

## Reduce or increase the retention period

When data reaches the end of the retention period, it is deleted automatically on a monthly basis.

If you reduce the retention period, then any affected data is deleted during the next monthly process. For example, if you change from _26 months_ to _14 months_, then any data older than 14 months is deleted during the next monthly process.

If you increase the retention period for a Google Analytics property, the change is applied to data that you have already collected and that you have not already deleted.

Whenever you modify the retention period, Analytics waits 24 hours before implementing the change. During this 24-hour period, you can revert your change and your data will be unaffected.

If you use a date range for non-aggregated reports, such as Explorations in Google Analytics, that is longer than your retention period, then data for that additional time is not visible in reports. For example, if you set retention to 14 months and you use a date range of 14 months + 1 day, then data for the additional 1 day is not available in your reports.

## [When large properties exceed event collection limits](https://support.google.com/analytics/answer/7667196?hl=en)

When a [standard property becomes Large or a 360 property becomes XL](https://support.google.com/analytics/answer/14207402), the event-level data retention setting is automatically reduced to 2 months and event-level data older than 2 months becomes inaccessible and is permanently deleted.

If the property is on pace to reach these limits based on weekly event volume, Analytics will send a warning email to all property administrators. When the limit is reached, Analytics will send another email to all property administrators notifying them that the data retention setting has been reduced.

Between these two notifications, you can reduce the number of billable events sent to the Google Analytics property to remain within the current limits for your property size and keep the longer event-level retention. If you received the warning for a free property, you can also [upgrade to 360](https://support.google.com/analytics/answer/11202874#upgrade-downgrade)to get access to higher limits.

## [](https://support.google.com/analytics/answer/7667196?hl=en)Reset on new activity

Turn this option **ON** to reset the retention period of the user identifier with each new event from that user (thus setting the expiration date to current time plus retention period). For example, if data retention is set to 14 months but a user initiates a new session every month, then that user's identifier is refreshed every month and never reaches the 14-month expiry. If the user doesn't initiate a new session before the retention period expires, then that user's data is deleted.

If you do not want the retention period for a user identifier reset when that user has new activity, turn this option **OFF**. Data associated with the user identifier will be deleted automatically after the retention period.

The reset feature applies to only user-level data.

## Set the options

You need the [Editor role](https://support.google.com/analytics/answer/2884495) to set this option for a Google Analytics property.

1.   In [Google Analytics](https://www.google.com/analytics/web), click [**Admin**](https://analytics.google.com/analytics/web/#/?pagename=admin&utm_source=gahc&utm_medium=dlinks).
2.   [Make sure you are in the correct account and property](https://support.google.com/analytics/answer/12813202).

1.   In the _PROPERTY_ column, click **Data Settings > Data Retention**.
2.   _Event data retention_: select the retention period you want.
3.   _Reset user data on new activity_: turn the switch on or off.
4.   Click **Save**.

## Data retention and the Users metric

As of February of 2018, we added the Users metric to many additional reports. Because this metric is new in these reports, we do not have aggregated data for this metric for all of these reports for all time. This may impact your historical reporting: there may be zeros for Active user counts prior to the time for which we have aggregated data for that metric.

We began aggregating data for 360 properties on May 1, 2016, and for standard properties on Sept 1, 2016.

This does not affect the Audience Overview report, however, which has aggregated Active user data for a much longer period of time.