> Source: https://support.google.com/tagmanager/answer/12962079?hl=en

Learn how to unblock your Google tags to get the full benefits of consent mode. Troubleshoot Tag Manager and CMP consent settings.

_This article is for website or app owners who have implemented consent mode._

[Consent mode](https://support.google.com/analytics/answer/9976101) allows you to adjust how your Google tags behave based on the consent status of your users and enables Google to model conversions and behavioral data. If your Google tags may be delayed or blocked until a consent interaction occurs, your modeled conversions are less accurate, and [behavioral modeling](https://support.google.com/analytics/answer/11161109) in Google Analytics is unavailable.

For more comprehensive measurement to make sense of disparate data and make the most of first-party data, we recommend you adjust your tag settings so Google tags load in all cases. If consent is denied, tags that fire communicate non-identifying signals like consent state and country. These signals improve conversion modeling and enable behavioral modeling. However, blocking tags prevents them from firing so they can't send any information at all.

To get behavioral modeling in Google Analytics and improve conversion modeling in Google Ads while respecting your users' consent status, follow the troubleshooting steps in this article to unblock your Google tags.

## How to check if you have blocked tags

You may have blocked tags if you have set up consent mode but you see a message that [behavioral modeling](https://support.google.com/analytics/answer/11161109#show) is unavailable in your Google Analytics property.

![Image 1: GA4 Admin > Reporting identity > Blended](https://storage.googleapis.com/support-kms-prod/VDEM0VF9SbYonDN1MObul9de5T96moHUyCnD)

If you use Tag Manager, you can use Tag Assistant to check if you have blocked tags:

1.   [Start a new debug session](https://support.google.com/tagassistant/answer/10039345#start) in Tag Assistant.
2.   Go to **Summary****> Tags**.
3.   Look at the **Tags Fired** section. Check if all the tags you expect to fire are listed.
4.   If any tag you expect to fire did not, find it in the **Tags Not Fired** section and click it. The tag is blocked if either 
    *   A trigger or variable based on the user’s consent is one of the trigger conditions, or
    *   You see a section called "Required Additional Consent" with one or more rows in the table beneath it.

For more information on using Tag Assistant to debug consent settings, read [Tag Assistant Consent Mode debugging](https://developers.google.com/tag-platform/devguides/consent-debugging).

## How to unblock tags

How you unblock tags depends on how you tagged your website or app and what mechanisms you've implemented to prevent tags from firing. Google tags may be blocked in multiple places. Check each tagging method that you've used. If you use a Consent Management Platform (CMP), check its settings as well.

This document provides troubleshooting steps for the most common causes of blocked tags.

## Unblock tags with Tag Manager

The two most common causes of blocked tags in Tag Manager are exception triggers and additional consent checks. Follow the troubleshooting instructions in this section to remove exception triggers and additional consent checks from Google tags. Google tags are Google Analytics, Google Ads, Floodlight, and Conversion Linker tags.

### Remove exception triggers

Exceptions triggers for Google tags were likely set up before consent mode existed and should be removed. Consent mode adjusts Google tag behavior based on consent state, so the exception isn't necessary anymore.

Remove exceptions from Google tags so they work properly:

1. In [Tag Manager](https://tagmanager.google.com/), click **Workspace**.

2. Click **Tags**in the left navigation.

3. In the _Firing triggers_ column, find Google tags with exceptions.

![Image 2: Workspace > Tags > Firing Triggers](https://lh3.googleusercontent.com/0oWzwH93NGaUC7Qg1cs9yiFu6PKYbva2LHqR0BM5SpyHOrMtf5VhRaiRjmp1L6iuzWKW=w895)

4. In the _Name_ column, click the name of the tag.

5. Click **Triggering**.

6. Under Triggering, find the exception. You may have more than one exception trigger.

To quickly identify which tags use a particular exception trigger, click the trigger. At the bottom of that trigger, _References to this Trigger_ lists all the tags that use the trigger.

![Image 3](https://storage.googleapis.com/support-kms-prod/ICuvUGh3hvOrsd76Q824bWRVe4ElPYKLPora)

7. Click **Remove**![Image 4: Remove](https://storage.googleapis.com/support-kms-prod/AZTcS8zmRRrwsFrrIc7z92L7dMhcDSqoenB1) next to each of the exception triggers you’d like to remove.

Only remove exception triggers for Google tags: Google Analytics, Google Ads, Floodlight, and Conversion Linker. Non-Google tags will not change their behavior based on consent mode.

8. Click **Save** in the upper right corner.

9. [Preview your changes](https://support.google.com/tagmanager/answer/6107056).

10. [Publish your container](https://support.google.com/tagmanager/answer/6107163) for the changes to take effect.

### Remove additional consent checks for tags with built-in consent checks

Tag Manager lets you block non consent-aware tags from firing when the required consent has not been granted. In other words, if tags don't have built-in consent checks, you can use the Tag Manager additional consent checks to respond to consent status. Google tags have built-in consent checks and modify their behavior based on consent status, so they don't require additional consent checks. If you have implemented consent mode and use additional consent checks at the same time, they won't work properly. If your CMP loads asynchronously, it might not always run before your Google tags. The tags may be triggered before users interact with your consent banner, or before consent state updates arrive. Even if consent is later granted, the tags don't fire unless consent is granted when they were first triggered.

Remove additional consent checks from Google tags so they work properly:

1.   In Tag Manager, click **Workspace**.
2.   Click **Tags** in the left navigation.
3.   Click the name of your Google tag.
4.   Click **Tag configuration > Advanced settings > Consent settings**
5.   Review settings listed in **Built-In Consent Checks**. You should see `ad_storage` and `analytics_storage` listed.
6.   Select **Additional Consent Checks** and choose either: 
    *   **Not set**: Default. No additional consent checks are performed by this tag or
    *   **No additional consent required**: Select this option to indicate that your tag does not need to check for additional consent in order to fire.

7.   [Preview your changes](https://support.google.com/tagmanager/answer/6107056).
8.   [Publish your container](https://support.google.com/tagmanager/answer/6107163) for the changes to take effect.

## [](https://support.google.com/tagmanager/answer/12962079?hl=en)Unblock tags with a Consent Management Platform

Consent Management Platforms (CMPs) block Google tags in three main ways:

*   Automatic blocking
*   Manual blocking
*   Tag Management System (TMS) based blocking
*   Consent mode override

The approach to unblocking the tags varies depending on which of these methods your CMP implementation is using. General instructions for each approach are provided below, followed by links to blocking documentation for select CMPs. If you are unsure which blocking approach your site uses, contact your CMP representative or support team.

If you have a consent banner using consent mode that sends "update" commands when consent changes, enable this setting for Google Ads and/or Google Analytics to treat data as not having consent granted until Google receives a consent signal from your website. After a consent signal is received, this will be updated to mark consent according to end-user choices. [Learn more about consent mode override](https://support.google.com/tagmanager/answer/12962079#ovverride).

To simplify the deployment of consent banners and consent mode, you can use an integrated CMP partner for setup. This allows you to deploy a banner and implement consent mode within the Google tag user interface with just a few clicks. Learn how to [Use an integrated CMP partner to set up your consent banner and consent mode](https://support.google.com/tagmanager/answer/15239830).

**Only unblock tags that support consent mode.** If you use any [legacy tags](https://developers.google.com/tag-platform/devguides/consent#legacy_tag_controls) which don't support consent mode, you must replace them with newer tags which do.

**Ensure that the consent mode default command is being set before any Google tags fire.** Failure to do this will cause Google tags to fire as if consent mode is not in use.

### Automatic blocking

Automatic blocking is set in your CMP's user interface. If you have implemented your CMP’s automatic blocking functionality, the general approach to unblocking Google tags is one of the following:

*   Modify the Google tag as specified by your CMP to indicate that autoblocking should ignore it. This is usually done by adding an attribute to the Google script tags.
*   Exempt Google tags from blocking in your CMP’s user interface. This is usually done by mapping the Google vendor to a purpose which is always allowed (sometimes called Essential) or by setting the automatic blocking feature to ignore Google tags entirely.

The first approach allows for you to choose exactly which Google tags are exempted from blocking. It can be useful if you have a mix of tags that support consent mode and ones that do not. If you choose the second approach, be sure that you have not implemented tags that lack support for consent mode.

### Manual blocking

Manual blocking modifies the Google tag so it cannot load until the CMP has loaded. Your CMP may instruct you to make changes to the `type` or `src` attributes of the Google tag, such as to change the type to `“text/plain”` or the `src` attribute to `<cmp_name>-src`. To undo this blocking technique, replace the Google tags modified with these CMP-specific modifications with the original tag as downloaded from the source Google platform.

### Tag management system blocking

This approach uses a tag management system such as Google Tag Manager to fire Google tags. The CMP fires an event which indicates when consent has been granted, and that event is used as a trigger for Google and other types of tags that require user consent. If you are using this approach, modify the triggers for your Google tags to remove any consent-based criteria, firing only based on the criteria your business requires. For example, for a page view analytics event, fire only on the page load trigger and not on the consent granted event provided by your CMP.

### CMP-specific documentation

The following list links to documentation about tag blocking for specific CMPs. Some of these articles describe how to implement rather than how to remove blocking. If this is the case for your CMP, reverse the documented process following the general guidance provided above.

If your instructions for your CMP are not listed, contact your CMP representative or support team for help.

**Cookiebot** ([automatic](https://support.cookiebot.com/hc/en-us/articles/360009063660), [manual](https://support.cookiebot.com/hc/en-us/articles/4405978132242-Manual-Markup-Guide), [Google Tag Manager](https://support.cookiebot.com/hc/en-us/articles/360003793854-Google-Tag-Manager-deployment))

**Cookie Information** ([automatic](https://support.cookieinformation.com/en/articles/5412170-managing-cookies#h_e8fb332b90), [manual](https://support.cookieinformation.com/en/articles/5444629-third-party-cookie-blocking), [Google Tag Manager](https://support.cookieinformation.com/en/articles/5451615-google-tag-manager-implementation))

*   To unblock Google tags with automatic blocking, reclassify them in such a way that they are not blocked. If you have questions, contact Cookie Information.

**Commander’s Act**([Tag Commander](https://community.commandersact.com/trustcommander/user-guides/categories-and-tags/assign-categories), [Google Tag Manager](https://community.commandersact.com/trustcommander/setup-guides/tag-manager/google-tag-manager#manage-gtm-tags-with-trustcommander))

*   For Tag Commander, uncheck “Include in Privacy Scope”
*   For Tag Manager, remove CMP triggers as described above

**Consent Manager** ([automatic](https://help.consentmanager.net/books/cmp/page/automatic-blocking-of-codes-and-cookies), [manual](https://help.consentmanager.net/books/cmp/page/how-to-block-third-party-codes-cookies-if-no-consent-is-given), [Google Tag Manager](https://help.consentmanager.net/books/cmp/page/google-tag-manager-%28gtm%29#bkmrk-example%3A-blocking-go))

**Didomi**([automatic](https://support.didomi.io/create-a-required-purpose-for-necessary-cookies-1), [manual](https://developers.didomi.io/cmp/web-sdk/third-parties/custom-integrations/no-tag-manager), [Google Tag Manager](https://support.didomi.io/block-your-tags-with-our-google-tag-manager-integration))

*   If unblocking manually blocked tags with Didomi, remove only the data-purposes or data-vendor attributes. Do not revert the “didomi/javascript” modification as this change ensures that Didomi loads and sets consent mode default consent before Google Tag Manager or other Google tags are allowed to load.

**iubenda** ([manual](https://www.iubenda.com/en/help/1229-manual-tagging-blocking-cookies), [Google Tag Manager](https://www.iubenda.com/en/help/1235-google-tag-manager-blocking-cookies))

**OneTrust** ([automatic](https://community.cookiepro.com/s/article/UUID-71e7d0a8-03d8-e272-e683-72cadded2ecf), [manual](https://community.cookiepro.com/s/article/UUID-730ad441-6c4d-7877-7f85-36f1e801e8ca), [Google Tag Manager](https://community.cookiepro.com/s/article/UUID-301b21c8-a73a-05e8-175a-36c9036728dc))

**Osano**([automatic](https://docs.osano.com/3rd-party-1st-party-blocking), [Google Tag Manager](https://docs.osano.com/osano-and-google-tag-manager))

**Usercentrics** ([manual](https://docs.usercentrics.com/#/direct-implementation-guide), [Google Tag Manager](https://docs.usercentrics.com/#/browser-sdk-google-tag-manager-configuration?id=adding-data-processing-technologies))