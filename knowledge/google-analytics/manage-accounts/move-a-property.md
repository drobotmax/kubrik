> Source: https://support.google.com/analytics/answer/9305872?hl=en

*   [About moving properties](https://support.google.com/analytics/answer/9305872?hl=en#about)
*   [Things to keep in mind](https://support.google.com/analytics/answer/9305872?hl=en#things)
*   [How to move a property](https://support.google.com/analytics/answer/9305872?hl=en#how)

## About moving properties

If you need to reorganize your properties in Analytics, you can move them (and their data streams) from one account to another.

Moving properties lets you keep your Analytics implementation current with your business. You might be reorganizing after a merger, after an internal restructuring, or after hiring a new agency.

You move a property from a _source_ account to a _destination_ account.

When you move a property, there are some aspects of the property that are moved with the property such as tag ID, property settings, data streams, reporting data, and property-level integrations. There are also some aspects of the property that remain in the source account such as change history. These are covered in more detail in the next section of this article.

## Things to keep in mind

### Source account

If the source account no longer contains properties after the move, you can [delete the source account](https://support.google.com/analytics/answer/9304776). An empty source account still counts against the maximum number of Analytics accounts you can have.

### Tagging

The Tracking ID (for example, G-123ABC) does not change, so there’s no need to retag anything.

The source account does not reuse the ID, so the ID remains unique throughout your Analytics environment.

### Property permissions

When you move a property, you have two options for how to handle permissions:

*   _Replace existing property permissions with permissions of the destination account_. The property will inherit permissions from the destination account.
*   _Keep existing property permissions_. The current property permissions are copied along with the property. Users who have account-level access in the source account will have property-level access in the destination account.

### Reporting data

All reporting data associated with a property is moved (not copied) to the destination account.

### Property settings, and associated configurations and objects

Property settings remain intact when you move a property, as do other settings and associated objects like tracking customizations such as User-ID, Remarketing Audiences and Dynamic Attributes, Custom Definitions, Data Import, and Custom Tables.

### Data streams

All data streams associated with a property are moved, and all the data-stream settings remain intact.

### Linked accounts and integrations

Any accounts you have linked to a property such as Google Ads or AdSense, and any integrations you have with other platforms like Firebase, BigQuery, Campaign Manager 360, Display & Video 360, or Search Ads 360 remain intact when you move a property.

If you have linked your Analytics property to an account with Google Ad Manager, you may not move this property; if you want to move such a property, contact your Google Marketing Platform support representative to unlink Ad Manager first. Then relink after the move.

If you need to unlink your Analytics 360-Ad Manager integration in order to move a property, be aware that unlinking will close all audiences published to those linked destinations, and you cannot currently reopen those audiences from Analytics.

### Change history

When you move a property, any [change history](https://support.google.com/analytics/answer/9305465) associated with that property prior to the move remains with the source account. Changes after the move are recorded in the destination account.

### Billing

Billing applies only to Analytics 360 properties. Billing is uninterrupted as long as the property retains its 360 status.

### Subproperties

If you want to move a [source property](https://support.google.com/analytics/answer/11546303), you need to first remove all of its [subproperties](https://support.google.com/analytics/answer/11524031).

You can't move a subproperty since the subproperty relies on its source property for all its data.

[Learn more about removing subproperties](https://support.google.com/analytics/answer/11525657)

[Learn more about subproperties](https://support.google.com/analytics/answer/11525732)

### Roll-up properties

If you want to move a [roll-up property](https://support.google.com/analytics/answer/11526144), you need to first remove all of its [source properties](https://support.google.com/analytics/answer/11546303).

If you want to move a source property, you need to first remove it from the roll-up property

[Learn more about removing source properties](https://support.google.com/analytics/answer/11538056#add-remove)

[Learn more about roll-up properties](https://support.google.com/analytics/answer/11526039)

### When you can't move a property

There are some circumstances in which you **cannot** move a property:

*   The source account and the destination account belong to different Google Marketing Platform organizations.
*   The source account does not belong to a Google Marketing Platform organization, and the destination account does belong to a Google Marketing Platform organization.

 Contact an [organization admin](https://support.google.com/marketingplatform/answer/9013956) to link the source account to the same organization as the destination account.
*   The service level for the property is set to 360, and the account link to the organization has not been verified. Contact an [organization admin](https://support.google.com/marketingplatform/answer/9013956) to either: 
    *   [Link the source account and the destination account to the same organization](https://support.google.com/marketingplatform/answer/9014054)
    *   [Downgrade the property from 360 to Standard](https://support.google.com/marketingplatform/answer/9013959), which lets you move the property

*   You do not have the [Administrator and Editor roles](https://support.google.com/analytics/answer/2884495) for the destination account.
*   The property is linked to Google Ad Manager.

 Contact your Google Marketing Platform support representative to unlink the property. You can relink after the move.

 If you are moving the property to a destination account that is owned by a different legal entity than the source account, you have to sign a new linking contract.
*   One or more unsampled reports are being processed for the property.

 Wait for the unsampled reports to finish processing, and then retry the move.
*   The destination account already has the maximum number of properties (50 by default).

## How to move a property

1.   In **[Admin](https://analytics.google.com/analytics/web/#/?pagename=admin&utm_source=gahc&utm_medium=dlinks)**, under _Property_, click [**Property details**](https://analytics.google.com/analytics/web/#/?pagename=admin-property&utm_source=gahc&utm_medium=dlinks). **Note**: The previous link opens to the last Analytics property you accessed. You must be signed in to a Google Account to open the property. You can [change the property](https://support.google.com/analytics/answer/12813202) using the property selector. You must be an [Editor or above](https://support.google.com/analytics/answer/9305587)at the property level to move a property. 
2.   Select the **Move property** button.
3.   Select the destination account.
4.   Choose your permissions settings: 
    *   _Keep existing property permissions_. The current set of user permissions is copied along with the property, and the property will not inherit permissions from the destination account.
    *   _Replace existing property permissions with permissions of the destination account_. The property will inherit permissions from the destination account.

5.   Click **Move**.
6.   Confirm data processing, then click **Save**.