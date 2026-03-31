> Source: https://support.google.com/analytics/answer/9940393?hl=en

To **delete data** associated with user IDs or pseudonymous IDs, see [User explorer](https://support.google.com/analytics/answer/9283607).

You need the [Editor role](https://support.google.com/analytics/answer/2884495) to make data-deletion requests for a Google Analytics property.

If you need to delete data from the Analytics servers for any reason, then you can use a data-deletion request to issue a request for its removal.

A data-deletion request is used to delete text collected by event parameters. The specific text data will be erased and replaced with “(data deleted)”, but the event will still be counted in the overall metrics in your reports.

**Note**: When you delete all parameters, the event name will also be deleted, as the event name is also a parameter.

*   [Create a data-deletion request](https://support.google.com/analytics/answer/9940393?hl=en#create)
*   [After request is created](https://support.google.com/analytics/answer/9940393?hl=en#after)
*   [Parameters available for deletion](https://support.google.com/analytics/answer/9940393?hl=en#parameters)
*   [How data deletion impacts other Google Analytics features](https://support.google.com/analytics/answer/9940393?hl=en#deletions)

* * *

## [](https://support.google.com/analytics/answer/9940393?hl=en)Create a data-deletion request

1.   In **[Admin](https://analytics.google.com/analytics/web/#/?pagename=admin&utm_source=gahc&utm_medium=dlinks)**, under _Data collection and modification_, click [**Data deletion request**](https://analytics.google.com/analytics/web/#/?pagename=admin-data-deletion&utm_source=gahc&utm_medium=dlinks). **Note**: The previous link opens to the last Analytics property you accessed. You must be signed in to a Google Account to open the property. You can [change the property](https://support.google.com/analytics/answer/12813202) using the property selector. You must be an [Editor or above](https://support.google.com/analytics/answer/9305587)at the property level to create a data-deletion request. 
2.   The table lists your most-recent requests. To make a new request, click **Schedule data deletion request**.
3.   Select your deletion type: 
**Delete all parameters on all events**This option deletes all registered and automatically collected parameters across all collected events.
**Delete all registered parameters on selected events**This option deletes all registered parameters collected across a list of events you select in the next step.
**Delete selected parameters on all events**This option deletes registered parameters that you select in the next step across all collected events.
**Delete selected parameters on selected events**This option deletes registered parameters that you select in the next step across a list of events that you also select in the next step.
**Delete selected user properties**This option deletes user properties that you select in the next step
4.   Select the _Start_ and _End_ dates. Keep in mind that the deletion process uses your property's time zone when deleting data.
5.   Select the specific data field(s) you want to delete: 
    *   **Events:** When applicable, select up to 100 events from the events list. The list shows the most recent events you’ve collected and may not be a complete history. You may also enter any event name and press enter to add any custom event name to the list. You may add up to 100 events to any single request.
    *   **Parameters:** When applicable, select up to 100 parameters from the parameters list. The list shows a complete set of all historically registered parameters you’ve collected.
    *   **User Properties:** When applicable, select up to 100 user properties from the user property list. The list shows a complete set of all historically registered user properties you’ve collected.

6.   Enter a value to identify which data you want to delete. Optionally, select "Only delete parameter values that contain the following text". Enter a value in the text box. Analytics will only delete dimension values for the specified events/parameters/user dimensions that contain the value you enter here. Analytics treats this as a _contains_ operator, and uses a case-insensitive match when it applies values for deletion. You cannot specify a reserved value like “(not set)”: Analytics does not delete reserved values.
7.   Click **Schedule Request**.

* * *

## [](https://support.google.com/analytics/answer/9940393?hl=en)After request is created

**Editor role** users are notified of the request via email. There is a preview period that begins shortly after you submit the request.

The **first 7 days**of the preview period are also a grace period during which **Editor role** users can cancel the request from the request-details page. From **day 8** of the preview period until the deletion request completes, your request status is **_Preview active / Deletion in progress_**.

### Cancellation/Deletion

You can cancel any request within 7 days from the time it was created. Use the request-details page. During the first 7 days, you can also see a preview of the effects of the deletion in your reports and in [Explorations](https://support.google.com/analytics/answer/7579450).

You can have a maximum of 12 (**grace period**/**pending deletion**) active requests per property at any one time.

During the grace period and while the deletion is pending or in progress, your reports and analyses **omit** the data that is identified in the request as though it were already deleted. This omission of data gives you the opportunity to preview the effect of the deletion and confirm that it is what you expect.

A data-deletion request can take between **7 and 63** days to be processed, (depending on the amount of data to be deleted), and data must be more than **12 days** old before it can be deleted.

A list of the most-recent requests is visible for each property under _Property column > Data Deletion Requests._ Once the request is completed, **the deletion of the data is not reversible**.

**Editor role** users are notified again when data deletion begins and again when it finishes.

* * *

## [](https://support.google.com/analytics/answer/9940393?hl=en)Parameters available for deletion

Analytics supports the deletion of **auto-collected** parameters and **custom**parameters **registered as custom dimensions.**

Analytics does not delete numeric parameters, text parameters derived from internal trusted identifiers, nor the reserved values "", "(not set)", and "(data deleted)".

### Auto-collected parameters

Auto-collected parameters can only be deleted when selecting Delete all parameters on all events.

##### List of auto-collected parameters that Analytics does not delete

### Custom parameters

Analytics deletes custom parameters that were registered as custom dimensions. If you do not see the parameter you want to delete in the list, it's possible that the parameter was never registered. You must confirm the name and registration of the parameter you are trying to delete.

If you created a custom dimension that gets its value from an auto-collected parameter, the deletion of the custom parameter **will not** delete the auto-collected parameter.

Before July 2022, Analytics did not support the deletion of archived parameters. If you archived a custom dimension before July 2022 and need to perform a deletion of that event parameter, you can do one of the following:

*   delete all parameters across all events, or
*   delete all parameters for a set of events.

* * *

## [](https://support.google.com/analytics/answer/9940393?hl=en)How data deletion impacts other Google Analytics features

### Campaign attribution

When a deletion is completed, from that point forward all historical campaign information is no longer available for attribution - that information will have been deleted. Attribution credit going forward could go to other campaigns (if any are available from 1st-party ad clicks, or new campaign information collected after the deletion) or it will be considered "Direct".

### Conversion reporting

All [Conversion reporting](https://support.google.com/analytics/answer/14715749) data for the specified date range within a data deletion request will be deleted if the request references one or more fields used in Conversion reporting. Conversion reports will show no data for the specified date range.

**Note**: Data deletion requests will remove the data based on the date range specified in the request, not the date when the data was collected. Conversion reporting propagates values based on lookback windows and creates reports based on interaction dates. It’s your responsibility to identify the date range for your request based on the specific data that you want to remove. If you notice that there’s additional data that should be deleted, you’ll need to create an additional data deletion request with the date range for that data.

### Consent Mode

If you're using [Consent mode](https://support.google.com/analytics/answer/9976101) for your property, you may need to add seven calendar days to the end date of your data-deletion request to ensure that any value you are specifically targeting for deletion is deleted from behavioral models. This is because Analytics trains machine-learning models on data from consented users (i.e., the data you may be trying to delete) and approximates future user behavior based on that training data.

Consented data may be used to model data for up to seven days beyond when the consented data was present in reporting, and therefore you may need to add seven additional days to your deletion request. For example, if the original end date for your data-deletion request is January 1, change that to January 8 instead.

### Subproperties

Any data that you delete from a source property is also deleted from its subproperties. However, any data that you delete from a subproperty is only deleted from that subproperty. Learn more [about subproperties](https://support.google.com/analytics/answer/11525732)

### Roll-up properties

Roll-up properties are distinct datasets that combine data from one or more source properties. Unlike subproperties, roll-ups do not have a hierarchical relationship with their sources.

When you make a data-deletion request for a source property, that request does not automatically apply to linked roll-up properties. If you need to remove the same data from a roll-up, you must submit a separate deletion request directly in the roll-up property. Conversely, when you make a deletion request for a roll-up property, the deletion only affects the roll-up and not its source properties. Learn more [about roll up properties](https://support.google.com/analytics/answer/11526039).