> Source: https://support.google.com/analytics/topic/10595462?hl=en

## Advertising and attribution

Create conversions based on key events so you can view the same conversion data across Google Ads and Analytics

[](https://support.google.com/analytics/answer/13823256?hl=en&ref_topic=10595744)[Next: Cross-channel budgeting plans (Beta)](https://support.google.com/analytics/answer/14896117?hl=en&ref_topic=10595744)

A conversion is created from a Google Analytics event and provides a consistent way of measuring important actions in both Google Analytics and Google Ads. A conversion helps you improve your marketing strategy by providing consistent conversion counts across platforms so you can understand and optimize your ad campaigns. Conversions based on Google Analytics events allow you to measure important actions that originate from organic channels like search, email, and social for cross-channel campaign measurement use cases.

The following flow shows how to create a conversion from a Google Analytics key event. In short, if an event is important to your business's success, you can mark the event as a key event in Analytics. Then, if the key event is important for optimizing ad campaigns and measuring their performance, create a conversion in Google Ads from the Analytics key event.

Event → Key Event → Conversion

## Google Analytics and Google Ads conversions

This feature may not be available to your Google Analytics property. The Google Analytics team is actively working to expand this feature to more properties. Please reach out to your support team if you have questions about the eligibility of your property.

Conversion management is streamlined across Google Ads and Google Analytics for a unified cross-channel experience. This enables you to:

*   Create conversions directly from your Google Analytics events and seamlessly share them with Google Ads. Some settings, like conversion window and counting method, might not be editable in Google Ads.
*   Manage conversion settings for both Google Analytics and Google Ads from a centralized interface.
*   Use categorized lists, improved search and filtering, and detailed settings review to manage your conversions effectively. Tools will also be available to identify and address diverging conversion settings between Google Analytics and Google Ads.
*   Track all conversion changes within Google Analytics change history, including detailed "before and after" views and shareable deep links.

Learn more about [creating conversions](https://support.google.com/analytics/answer/14710559#how-to-create-conversions).

**Notes**:

*   A linked Google Ads account is required to create a new Google Analytics conversion from a key event.
*   You can create a conversion in Google Analytics which makes the conversion available in Google Ads.

## Benefits of creating conversions

By creating Google Ads conversions based on the Google Analyics events, you can:

*   Report on the same conversion counts between Google Ads and Analytics
*   Report on non-Google and organic channels, including channels that are part of the same cross-channel campaign
*   Bid against the conversions in your ad campaigns
*   Build audiences for re-marketing purposes

## [](https://support.google.com/analytics/topic/10595462?hl=en)Create a conversion

### Step 1 of 2: Identify or mark an event as a key event

1.   In **[Admin](https://analytics.google.com/analytics/web/#/?pagename=admin&utm_source=gahc&utm_medium=dlinks)**, under _Data display_, click [**Events**](https://analytics.google.com/analytics/web/#/?pagename=admin-events&utm_source=gahc&utm_medium=dlinks). **Note**: The previous link opens to the last Analytics property you accessed. You must be signed in to a Google Account to open the property. You can [change the property](https://support.google.com/analytics/answer/12813202) using the property selector. You must have at least [Marketer](https://support.google.com/analytics/answer/9305587) access at the property level to mark an event as a key event. 
2.   In the "Key events" tab, choose an event that measures an important interaction by clicking the star icon next to the event name.

### Step 2 of 2: Create a new conversion from the key event

#### Create conversions through Google Ads

1.   In your [Google Ads account](https://ads.google.com/), click the**Goals** icon.
2.   Select**Summary**under "Conversions".
3.   Click**Create conversion action**
4.   Select the Google Analytics property you'd like to use.
5.   On the next page, select the Google Analytics event that you’d like to use to measure your conversions, then click **Select events**.
6.   Click **Save and continue**.

#### Create conversions through Google Analytics

We recommend you create conversions based on Google Analytics events to:

*   Access rich behavioral reporting in Analytics
*   Share and reuse conversions across linked Google products, such as Google Ads.
*   Measure credit for the conversion across different channels.

1.   In [**Advertising**](https://analytics.google.com/analytics/web/#/?pagename=reporting-advertising-snapshot&utm_source=gahc&utm_medium=dlinks), under "Tools", select **Conversion management**. **Note**: The previous link opens to the last Analytics property you accessed. You must be signed in to a Google Account to open the property. You can [change the property](https://support.google.com/analytics/answer/12813202) using the property selector. You must have at least [Marketer](https://support.google.com/analytics/answer/9305587) access to import key events as conversions into Google Ads. 
2.   Select the Google Ads account in the **Showing conversions for** dropdown where you want to create conversions.
3.   Click **New conversion**, then **Next**.
4.   Select the events or key events you want to create as conversions in Google Ads. 
    *   **Note**: Events selected from the "Events" section will be marked as key events in Google Analytics.

5.   If prompted, select the Conversion category for your selected events and key events.
6.   Click **Next** to review your selected conversions, then **Save**.

## Managing conversion settings

Google Analytics provides a centralized control interface that serves as the primary location for handling conversion settings across Google Analytics and Google Ads. This includes **categorized lists**, **enhanced search** and **filtering**, and a **detailed settings review** feature to help locate and examine your conversion configurations. Google Analytics will also play a crucial role in identifying and helping to **reconcile any discrepancies** between your Google Analytics and Google Ads conversion settings. You also have access to a **comprehensive change history** in Google Analytics with a detailed log of all modifications made to conversions.

Learn more about [editing your conversion settings through the Google Ads and Google Analytics interface](https://support.google.com/google-ads/answer/2375435#edit-conv-settings).

### Select channels that can receive credit for web conversions

In the [Attribution settings](https://support.google.com/analytics/answer/10597962?) in Google Analytics, you can choose from the following options under _Channels that can receive credit_, enabling you to determine which channels can receive credit for web conversions shared between Google Analytics and Google Ads:

*   **Google paid channels**
*   **Paid and organic channels**

Choosing the **Google paid channels** attribution setting lets you see conversions from Google Ads in your Google Analytics conversion reports. If you choose **Paid and organic channels**, you can report on conversions from both paid and organic sources in Google Analytics, providing a broader, cross-channel view of your conversions beyond Google Ads paid channels.

Changing this setting applies going forward and to all linked Google Ads accounts. It may impact the conversions you create bidding and reporting in Google Ads. These changes may take a few days before they're reflected in your Google Ads campaigns and reports.

**Notes**:

*   **Paid and organic channels** only applies to web conversions; app conversions always use **Google paid channels**.
*   When you select **Paid and organic channels**, "Conversion window" and "Counting method" settings must be managed by Google Analytics by navigating to Advertising > Conversion management > "3 dot icon" > Google Analytics.

## Default conversion settings

By default, most settings for conversions based on Google Analytics events will match across Google Ads and Google Analytics.

*   **Counting method:** Settings match by default.
*   **Conversion windows:** Settings match by default.
*   **Channels eligible for conversion credit:** These channels are also known as attribution channels: 
    *   **For****Google Ads reports:**_Google Paid_ attribution is the default setting, and can be updated to Paid and Organic.
    *   **For Google Analytics reports:**_Paid and Organic_ attribution is the default setting.

*   **Attribution model:** This setting is controlled at the report level in Google Analytics.
*   **Account time zone:** Google Analytics reporting uses the Google Analytics property time zone. Google Ads reporting uses the Google Ads account time zone. If accounts and properties are set in different time zones, you might see discrepancies in reporting.

Make sure you’ve set the columns “All conv.” or “All conv. (by conv. time)” for viewing in Google Ads to match what’s in Google Analytics. The default setting is “All conv.” for the columns.

## Report on conversions

The _Conversion performance_ report in the Advertising section lets you select conversions shared with your Google Ads account and evaluate the performance of those conversions in Google Analytics. [Learn more about the Conversion performance report](https://support.google.com/analytics/answer/14715749)

[](https://support.google.com/analytics/answer/13823256?hl=en&ref_topic=10595744)[Next: Cross-channel budgeting plans (Beta)](https://support.google.com/analytics/answer/14896117?hl=en&ref_topic=10595744)

##