> Source: https://support.google.com/tagmanager/answer/10718549?hl=en

Google Tag Manager includes several features that work together to help you manage how tags behave in response to [consent](https://support.google.com/analytics/answer/9976101) settings. Tag Manager features a [consent initialization trigger](https://support.google.com/tagmanager/answer/10718549?hl=en#consent-initialization-trigger), [tag settings for consent management](https://support.google.com/tagmanager/answer/10718549?hl=en#tag-settings), and a [Consent Overview](https://support.google.com/tagmanager/answer/10718549?hl=en#consent-overview) page. Several third-party consent management providers have built [integrations with consent mode](https://support.google.com/tagmanager/answer/10718549?hl=en#cmp-integrations) into their products. This article describes how to set up the consent management features in Tag Manager.

[Set up consent mode in Google Analytics](https://www.youtube.com/watch?v=MqAEbshMv84)

For subtitles in your language, turn on YouTube captions. Select the **Settings** icon ![Image 1: Image of YouTube settings icon](https://storage.googleapis.com/support-kms-prod/UrHzzlx74G5ig5vYXo9Nk43r7NM5fj72Tbu1) at the bottom of the video player, then select **Subtitles/CC** and choose your language.

* * *

## [](https://support.google.com/tagmanager/answer/10718549?hl=en)Consent Initialization trigger

The **Consent Initialization** trigger is designed to help you ensure that all consent settings are honored before any other triggers fire. The Consent Initialization trigger is used for tags that set or update the user consent state for your site, such as a consent management platform tag or tags that set consent defaults.

Each web container includes a **Consent Initialization - All Pages** trigger by default. Select this trigger to fire any tags that require it.

The Consent Initialization trigger is not used for tags that should fire early on a site. For tags that aren't specifically used to manage consent settings, use an [**Initialization** trigger](https://support.google.com/tagmanager/answer/7679319) instead. The Consent Initialization trigger will always fire before all other tags, including any Initialization triggers.

**Note:** When writing your own templates or Custom HTML tags, any commands executed in callbacks or commands that use `gtag()` are not guaranteed to be available before the next trigger fires. To ensure that consent information is available as quickly as possible, use the [Tag Manager Consent APIs](https://developers.google.com/tag-manager/templates/consent-apis). Read the [developer guides](https://developers.google.com/tag-manager/consent) for more information.

## Tag consent settings

Tags with built-in consent checks typically modify their behavior based on the consent granted. Each tag can have customized consent settings. To edit consent settings for a tag:

1.   In any web tag, click **Advanced Settings > Consent Settings**.
2.   Review settings listed in **Built-In Consent Checks**. Tags with built-in consent checks include logic that changes the tag's execution behavior based on the user's consent state. Read how consent mode operates for [Google Ads](https://support.google.com/google-ads/answer/10000067), [Google Analytics](https://support.google.com/analytics/answer/9976101) and [Floodlight](https://support.google.com/campaignmanager/topic/6228828). _**Note:** Third-party consent management platforms may feature different default built-in behaviors._
3.   Select **Additional Consent Checks**. 
    *   **Not set:** Default. No additional consent checks are performed by this tag.
    *   **No additional consent required:** Select this option to indicate that your tag does not need to check for additional consent in order to fire. You may choose to use this option to distinguish tags that need no additional consent outside of their built-in consent checks for any tags that you have not yet reviewed.
    *   **Require additional consent for tag to fire:** This tag will only fire if the status of all specified consent types are 'granted' when the tag is triggered. If you select this option, the **+ Add required consent** button will appear. Use this button to add additional consent types. Tag Manager supports the consent types listed in the table below, and you can add your own custom consent types based on what is supported by your consent management platform.

## Tag Manager consent types

The following consent types can be used to control tag firing in Google Tag Manager. Google tags that support [consent mode](https://support.google.com/analytics/answer/9976101) already adjust their behavior based on these consent types.

_The visual representation below is for illustrative purposes only and should not be considered legal guidance._

![Image 2: An illustration of a cookie consent banner.](https://storage.googleapis.com/support-kms-prod/VzBj1qltGLJIdiM0ClnlZOfBOXlagVJ8CjPR)

**Consent Type****Description**
ad_storage Enables storage (such as cookies) related to advertising.
ad_user_data Sets consent for sending user data related to advertising to Google. The ad_user_data consent type is required for measurement use cases, such as enhanced conversions and tag-based conversion tracking.
ad_personalization Sets consent for personalized advertising.
analytics_storage Enables storage (such as cookies) related to analytics e.g. visit duration.

_The visual representation below is for illustrative purposes only and should not be considered legal guidance._

![Image 3: An animation showing a cookie consent banner and what happens if you accept or deny cookies.](https://storage.googleapis.com/support-kms-prod/fHtvLIdImKzy8Ozkvb9fGaXMdKOjyjbwI87k)

In addition to the consent mode parameters, there are the following privacy parameters:

**Storage Type****Description**
functionality_storage Enables storage that supports the functionality of the website or app e.g. language settings.
personalization_storage Enables storage related to personalization e.g. video recommendations
security_storage Enables storage related to security such as authentication functionality, fraud prevention, and other user protection.

## Consent Overview

The Consent Overview page provides a high level view of all the consent settings across the tags in your container. To enable this feature in your container:

1.   In Tag Manager, click **Admin > Container Settings**.
2.   Under **Additional Settings**, select **Enable consent overview**.

To access the Consent Overview page:

1.   Click **Tags** in the left navigation.
2.   Click the **Consent Overview**![Image 4](https://lh3.googleusercontent.com/rCgH25zRXx76T0i9re_uG27lUuB0KzdFaQuzQad1LL9QKCawGI3z4N7y33JrFzJGpyQjjQwmqvwcyTv4YAB4yfstxgX0Oj_ax5zzIF10EV12m3yL6O9QvcDj4ko2k_jjinXsvStRTw) icon.

The Consent Overview page groups tags into two categories:

*   **Consent Not Configured:** Lists tags where no action has been taken. These tags are in the 'not set' state.
*   **Consent Configured:** List of tags where Additional Consent Checks has been set to either "No additional consent required" or "Require additional consent for tag to fire"

### Bulk consent edits

From the Consent Overview screen, you can edit consent settings for multiple tags at the same time:

1.   Click **Tags** in the left navigation.
2.   Click the **Consent Overview**![Image 5](https://lh3.googleusercontent.com/rCgH25zRXx76T0i9re_uG27lUuB0KzdFaQuzQad1LL9QKCawGI3z4N7y33JrFzJGpyQjjQwmqvwcyTv4YAB4yfstxgX0Oj_ax5zzIF10EV12m3yL6O9QvcDj4ko2k_jjinXsvStRTw) icon.
3.   In a list of tags, use the checkboxes to the left of each entry to select which items you would like to update. When one or more tags are selected, the **Edit Consent Settings**![Image 6](https://lh5.googleusercontent.com/Q85QWwDm8z319IpWldT6NiSKvxeslQ_WIiG8YjSBc9NoGLkmLrOrlyeEMrBSXgm0xE8RvvRRpFI9Wc03jB0pPqH9N_XEOla9xM03mucYYpnXzdzj414RWgmQcWG9Lhp_kI_O5fso7w) icon will appear.
4.   Modify settings for **Additional Consent Checks**.
5.   Click **Save**.
6.   [Publish your container](https://support.google.com/tagmanager/answer/6107163) for the changes to take effect.

## Consent configuration settings behavior with the Transparency & Consent Framework v2.0

Google Ads and Google Analytics tags integrate with the IAB Transparency & Consent Framework (TCF) v2.0 framework. If customers have TCF support enabled, Google product tags will respect TCF user consent settings. Interpretation of TCF behaviors may differ between products. Read the documentation for each product to learn how they integrate with TCF: [Google Ads](https://support.google.com/google-ads/answer/10021549), [Google Analytics](https://support.google.com/analytics/answer/10022331), [Campaign Manager](https://support.google.com/campaignmanager/answer/10031693), and [Display and Video 360](https://support.google.com/displayvideo/answer/9798183).

Currently, Tag Manager consent configuration settings support **TCF Purpose 1: Store and/or access information in a device**, and users can configure their tags for the five consent types [listed in the table above](https://support.google.com/tagmanager/answer/10718549?hl=en#consent-types) if they are also supported by your consent management platform.