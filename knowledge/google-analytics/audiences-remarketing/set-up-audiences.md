> Source: https://support.google.com/analytics/topic/14272803?hl=en

Audiences are groups of your users who share the same attributes. You can share audiences with the advertising products you use, like Google Ads, so you can market to specific groups of users.

## What is an audience?

In Google Analytics, an audience is a group of users from your site and/or app who have generated similar behavioral data or who share demographic or other descriptive data (e.g., same age group, same gender, were acquired by the same campaign).

For example, you might want to create an audience of all users who have made a purchase of any kind (`purchase` event_count > 0).

You might find this audience too large for the practical purposes of your ad campaigns. In this case, you can identify smaller groups of users who have more specific behavior and demographics in common, like:

*   Users from California who have purchased 1-5 items
*   Users from San Francisco, California who have purchased 1-5 items in the last 7 days
*   Users from San Francisco who purchased 1-5 items in the last 7 days and who spent more than $100

You can build audiences around any of the data you collect and you can define your audiences as broadly or narrowly as necessary: _All users who purchased sunglasses_ or _All users who purchased the black wraparounds with the blue reflective lenses_.

Anytime a user visits your site or app and their behavior and/or descriptive data match your audience conditions, then that user is added to the audience. The rate at which an audience accumulates users depends on how often users who visit your site or app engage in behavior and/or match descriptive data that satisfy your audience definition. Audiences with broader definitions (fewer conditions) will accumulate users more quickly than audiences with more narrow definitions (more conditions).

Analytics backfills audiences with up to 30 days of data, if that data is available. If you've already had users who fit your audience definition during the last 30 days, then your audience will be populated with users within 24 to 48 hours, and an additional hour for prepopulation. Daily event processing takes 24 hours.

**Note**: You might notice different numbers of users for Audiences and Segments with the same conditions.

Despite seeming similar, Audiences and Segments are fundamentally different features:

*   An **Audience** is a group of users who meet a set of conditions. Users enter and exit the audience over time (e.g. if a user purchased two years ago and then never visited the site again, this user will not be part of the “purchasers” audience anymore) and is not calculated retroactively from the date it was created (e.g. if you create a “purchasers” audience today it won’t include users who purchased before today).
*   A **Segment** is a set of conditions used to filter the data in a report. It doesn’t include any membership logic and it’s fully retroactive (e.g. a “purchasers” segment will include all the users who purchased during the date range of the query where the segment is applied).

Learn more about [Segment builder](https://support.google.com/analytics/answer/9304353).

* * *

## What do you do with an audience?

You can use audiences in your reports and advertising campaigns.

### Reporting

If you do nothing but create the audience, you can open a report about it in Analytics and see how many users from that audience visit your site/app, how many [key events](https://support.google.com/analytics/answer/9355848) and engaged sessions they generate, and the technologies they use to engage with your content.

In your reports, you can use audiences as the basis for [comparisons](https://support.google.com/analytics/answer/9269518). (Select Audience name as the dimension and select a specific audience for the dimension value.) Then you can compare audiences in the context of the same data: did my audience of customers from Los Angeles buy more sunglasses than my audience of customers from San Francisco? Who bought more of the really expensive ones?

In the [Explore module](https://support.google.com/analytics/topic/9266525), you can use the Audience name and Last audience name dimensions to dig deeper into which methods of acquiring specific audiences were more effective, which audiences continued to engage once you did acquire them, how those users navigated through your content and through specific funnels you have in mind.

### Advertising

If you have your Analytics property linked to Google's advertising products like Google Ads, Display & Video 360, or Search Ads 360, you share your Analytics audiences with those products.

The Purchasers audience, which Analytics creates by default when your users trigger `in_app_purchase` or `purchase` events, is shared with any linked advertising products.

When you create the product links between Analytics and your advertising products and select the option to _enable personalized advertising,_ your audiences are available in those other products to use to show users ads based on their specific online behavior (e.g., remarketing ads about products they have viewed on your site but haven't yet purchased).

When your audiences are available in Google's advertising products, you can use them to specify who you want to show your ads to. For example, if your audience is _All users who purchased sunglasses_, then whenever one of the users in that audience opens a site or app on which you're advertising, your ad is automatically entered into the bidding to appear to that user. This lets you spend your ad dollars on users who are most likely to respond to your ads.

* * *

## Predictive audiences

A predictive audience has at least one condition based on a predictive metric. Analytics generates predictive metrics by modeling the data you collect (if you collect the required minimum amounts of the necessary data) and predicting which of your users will behave a certain way. The predictive models evaluate your data to figure out things like which users are likely to make a purchase, which users are likely to churn (stop using your site/app), and how much revenue users are likely to generate.

Predictive audiences are helpful when you're trying to figure out where to spend your marketing budget. You can spend it on users that made a purchase or users that are more likely to make a purchase in the next 7 days.

If Analytics is generating predictive metrics for your property, you can use them when you build your own audiences; for example, "include users from San Francisco AND users who are likely to make a purchase in the next 7 days".

An additional benefit of Analytics generating predictive metrics is that it uses them to generate predictive audiences like _Likely 7-day purchasers_ and _Predicted 28-day top spenders_ that you can use as-is or as the basis for your own custom audiences.

Learn more about [predictive metrics](https://support.google.com/analytics/answer/9846734) and [predictive audiences](https://support.google.com/analytics/answer/9805833)

* * *

## Additional reading

*   [Creating Analytics audiences](https://support.google.com/analytics/answer/12799863)
*   [Sharing Analytics audiences with your linked advertising products](https://support.google.com/analytics/answer/12800258)