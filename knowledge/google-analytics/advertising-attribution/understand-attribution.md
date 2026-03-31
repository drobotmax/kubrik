> Source: https://support.google.com/analytics/topic/10597959?hl=en

## Advertising and attribution

Analyze how your ads drive users to perform meaningful actions on your website or app

[](https://support.google.com/analytics/answer/13684192?hl=en&ref_topic=10595744)[Next: All channels performance report](https://support.google.com/analytics/answer/12198930?hl=en&ref_topic=10595744)

## Overview

Customers may do several searches and click several of your ads before making a purchase or completing another important action on your website or app. Typically, all credit for the important action, called a [key event](https://support.google.com/analytics/answer/9355848?), is given to the last ad customers clicked. But was it solely that ad that made them decide to interact with a key event on the path to a key event? What about the other ads they clicked on before it?

Attribution is the act of assigning credit for important user actions to different ads, clicks, and factors along the user's path to completing the action.

An attribution model can be a rule, a set of rules, or a data-driven algorithm that determines how credit is assigned to [touchpoints](https://support.google.com/analytics/answer/14709948) along a user's path to completing important actions.

There are 3 attribution models available in the Attribution reports in Google Analytics properties:

*   Data-driven attribution
*   Paid and organic last click
*   Google paid channels last click

**Note**: All attribution models exclude direct visits from receiving attribution credit, unless the path to key event consists entirely of direct visits.

## ![Image 1: Google Ads logo](https://storage.googleapis.com/support-kms-prod/424967d8-7264-4bc3-b296-d1cb5929a8e6) Reach your marketing goals

Put your insights from Google Analytics to work with Google Ads to help get your business in front of the right customers across Search, YouTube, and more.

## Access the Attribution reports

To access the Attribution reports:

1.   In Google Analytics, click **Advertising** on the left.
2.   Under _Attribution_, click **Attribution models** or **Attribution paths**.

## Data-driven attribution

**Data-driven**: Data-driven attribution distributes credit for the key event based on data for each key event. It's different from the other models because it uses your account's data to calculate the actual contribution of each click interaction.

![Image 2: Data-driven model icon](https://lh3.googleusercontent.com/XB0uIdySmY1njJdD5Fq7reMBbkme4oMujx-VXcntFwdCC2bACtrGiY6dBuiN91RLg4o=w48) Each **Data-driven** model is specific to each advertiser and each key event.

### How data-driven attribution works

Attribution uses machine learning algorithms to evaluate both converting and non-converting paths. The resulting _Data-driven_ model learns how different touchpoints impact key event outcomes. The model incorporates factors such as time from key event, device type, number of ad interactions, the order of ad exposure, and the type of creative assets. Using a counterfactual approach, the model contrasts what happened with what _could have occurred_ to determine which touchpoints are most likely to drive key events. The model attributes credit to these touchpoints based on this likelihood.

**Notes**:

*   Depending on data availability, data-driven attribution models may leverage aggregate data from [Data sharing settings](https://support.google.com/analytics/answer/1011397).
*   Conversions can be reattributed for up to 7 days after the conversion.

### The methodology behind data-driven attribution (advanced)

## Paid and organic last click

**Note**: The first click, linear, time decay, and position-based attribution models are no longer available as of November 2023. Learn more [About the deprecated models](https://support.google.com/google-ads/answer/13427716).

![Image 3: Last interaction model icon](https://lh3.googleusercontent.com/-USKjk6oD8OY7P3UowRQsY7umTlhvOose1fsecdnedDri9Lsd7cLUry1HB3GqrGp64M=w48)**Paid and organic last click**: Ignores direct traffic and attributes 100% of the key event value to the last channel that the customer clicked through (or engaged view through for YouTube) before converting. See examples below of how key event value is allocated:

**Examples**

1.   Display > Social > Paid Search > Organic Search → 100% to Organic Search
2.   Display > Social > Paid Search > Email → 100% to Email
3.   Display > Social > Paid Search > Direct → 100% to Paid Search
4.   Direct → 100% Direct traffic

**Note**:

*   **Paid and organic last click** and **Last non-direct click** are two names for the same attribution model.

An engaged view is counted in data-driven attribution when a user:

*   Watches an ad for 30 seconds (or until the end if it is less than 30 seconds)
*   Clicks on a teaser card
*   Clicks a companion banner or video wall
*   Clicks on a phrase that is a call to action
*   Clicks on the end screen
*   Clicks to visit the advertiser’s website

## Google paid channels last click

![Image 4: Last interaction model icon](https://lh3.googleusercontent.com/-USKjk6oD8OY7P3UowRQsY7umTlhvOose1fsecdnedDri9Lsd7cLUry1HB3GqrGp64M=w48)**Google paid channels last click**: Attributes 100% of the key event value to the last Google Ads channel that the customer clicked through before converting. If there is no Google Ads click in the path, as in Example 6, the attribution model falls back to Paid and organic last click.

**Examples**

1.   Display > Social > Paid Search > Organic Search → 100% to Paid Search
2.   Display > Social > YouTube EVC > Email → 100% to YouTube
3.   Display > Social > Email > Direct → 100% to Email (fallback to last non-direct click)
4.   Direct → 100% Direct traffic

## Select attribution settings

The Attribution settings page lets you choose how key event reports in Google Analytics assign credit to different ads, clicks, and other factors before users trigger key events.Google Analytics provides a streamlined process for managing cross-channel conversions. Key events in Google Analytics are the primary source for creating conversions that can be shared with Google Ads.

To select key event attribution settings:

1.   Sign in to [Google Analytics](http://analytics.google.com/).
2.   In **[Admin](https://analytics.google.com/analytics/web/#/?pagename=admin&utm_source=gahc&utm_medium=dlinks)**, under _Data display_, click **Events**. **Note**: The previous link opens to the last Analytics property you accessed. You must be signed in to a Google Account to open the property. You can [change the property](https://support.google.com/analytics/answer/12813202) using the property selector.

You must be a[Marketer or above](https://support.google.com/analytics/answer/9305587)at the property level to select the attribution settings. 
3.   Click **Attribution settings**.
4.   Review these attribution settings: 
    *   [Reporting attribution model](https://support.google.com/analytics/answer/10597962#reporting-attribution-model)
    *   [Channels that can receive credit](https://support.google.com/analytics/answer/10597962#channels-receive-credit)
    *   [Key event lookback window](https://support.google.com/analytics/answer/10597962#window)

5.   Click **Save**.

[](https://support.google.com/analytics/answer/13684192?hl=en&ref_topic=10595744)[Next: All channels performance report](https://support.google.com/analytics/answer/12198930?hl=en&ref_topic=10595744)

##