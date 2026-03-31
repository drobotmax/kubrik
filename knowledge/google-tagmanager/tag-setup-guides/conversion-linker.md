> Source: https://support.google.com/tagmanager/answer/7549390?hl=en

If a container loads a Google tag on every page, it does not also need a conversion linker tag. Containers with Google Ads and Floodlight tags will automatically load a Google tag first, before sending events.

Conversion linker tags are used to help tags measure click data so that conversions are measured effectively. Deploy a conversion linker tag on any page where visitors may land after they click an ad or promotion.

When people click on your ads, the URL of the [landing page](https://support.google.com/google-ads/answer/14086) of your website typically includes information about the click. When a site visitor takes an action that you’ve tagged as a conversion (e.g. when a Google Ads conversion tag is fired), the click information is used to associate that conversion with the click that brought the visitors to your site.

The conversion linker tag automatically detects the ad click information in your landing page URLs, and stores this information in first-party cookies and browser local storage on your domain for web pages, and passes the data in URLs for AMP pages. If you use a conversion linker tag with Google Marketing Platform products, the conversion linker tag may also store unique identifiers in those cookies.

## Basic setup

![Image 1: An animation showing how to set up Conversion Linker in Tag Manager.](https://storage.googleapis.com/support-kms-prod/DbmH9hMNr4jZtlxeCixvVHnf3DYfwmcA7b38)

To set up a conversion linker tag:

1.   In Google Tag Manager, navigate to your container and click **Tags**, then **New**.
2.   Click **Tag Configuration** and select **Conversion Linker** from the list of tag types.
3.   Click **Triggering** and choose a trigger. 
    *   **Note**: In most cases, you should use the **All Pages** trigger to ensure that the linker tag is active on any potential landing page. Alternatively, you can create a trigger for specific page views where site visitors will land after an ad is clicked.

4.   Click **Save**.
5.   Preview and debug your setup using Google Tag Manager’s Preview mode and Google Tag Assistant to ensure the Conversion Linker tag is firing correctly on relevant pages.
6.   After confirming, publish your container.

Instances of conversion linker tags for web and AMP containers will have the additional option to [link across domains](https://support.google.com/tagmanager/answer/7549390#linker) and web containers will also include the ability to [override cookie settings](https://support.google.com/tagmanager/answer/7549390#override).

## Link across domains

Conversion linker tags in web and AMP containers can be configured to link across domains for cases where you have the landing pages and conversion pages on multiple domains. When you select this option, hyperlinks that point to a linked domain will have a linker parameter appended to the URL. A destination domain with a compatible linker tag will check inbound URLs for linker parameters. If a valid linker parameter is found, a 1st party measurement cookie is extracted and stored. [Learn more](https://developers.google.com/gtagjs/devguide/linker).

To configure the conversion linker tag to work with multiple domains:

1.   Select **Enable linking across domains**. This setting will enable this tag to handle incoming links that have a linker parameter.
2.   Optional, but recommended for web and AMP containers: In **Auto Link Domains**, enter a list of domains that should be linked with this tag. Any links that point to a domain listed in this field will have a linker parameter appended to the URL.
3.   _Optional for web containers:_ To link forms, set **Decorate Forms** to _**true**_.
4.   _Optional for web containers:_ If you need to tell Tag Manager to read the unique parameter from a fragment (`#`) instead of a standard query (`?`), set **URL Position** to _**Fragment**_. Otherwise, leave this option set to the default _**Query Parameter**_ option.

Note: Decorate Forms will only work in conjunction with the **URL Position** option set to **Query Parameter**. This is because some browsers strip off the URL fragment from form submissions.

## Override cookie settings (advanced)

For most cases, the basic configuration of this tag will be sufficient. **Only adjust the settings if you have a specific need that requires it.**

You may need to override some cookie settings in cases where you already have cookies with the same names, you need to have multiple sets of cookies, or when you don’t want ad click info from one subdomain of your website to be available for conversions on another subdomain. For these cases, use the override cookie settings feature.

The conversion linker tag sets ad click information in cookies named _\_gcl\_*, such as \_gcl\_aw, and \_gcl\_gs_ _._ These cookies use the top-most [domain](https://support.google.com/tagmanager/answer/7549390#domain) and root level [path](https://support.google.com/tagmanager/answer/7549390#path). If you need to override any of these settings, you can do so in **Linker Options**.In addition, conversion linker tags store ad click information in Browser Local Storage (key: _\_gcl\_ls_).

When you select the **Override cookie settings** checkbox, text fields for **Name prefix**, **Domain**, and **Path** will appear:

*   **Name:** This is the prefix used as part of the cookie names.The default prefix name is _\_gcl_. For example, if you change the Name field to _\_gcl2_, the Conversion Linker tag will set cookies named _\_gcl2\_aw_ and _\_gcl2\_dc_. If you change the prefix of the cookie names, any tags that read ad click info from these cookies (e.g. Google Ads conversion tags) must also be configured to use the same prefix.
*   **Domain:** This is the domain of your website on which the first-party cookies should be set. By default, a conversion linker tag will use the highest level domain on which it can set cookies. For example, if your website address is _blog.example.com_, a conversion linker tag will set the cookie domain to _example.com_. Only set this field if you need to limit the cookies to a lower-level domain.
*   **Path:** This is the path used to set the cookies. By default, the cookie path will be the root level of the domain. Only set this field if you need to limit the cookies to a subdirectory of a domain.

You can also edit how tags work with first-party cookies set by conversion linker tags: These tags will offer two additional configuration options in the **Conversion Linking** section:

*   **Enable Conversion Linking:** By default, all tags that read data set by the conversion linker tag have "Enable Conversion Linking" set to _true_. Set this value to false if you need to disable the tag's ability to work with Conversion Linker tags.
*   **Cookie Prefix:** If you have changed the cookie name prefix in a conversion linker tag, add that same prefix in this field so that the tag can read data from the correct cookie.

*   [Google Ads conversions](https://support.google.com/tagmanager/answer/6105160)
*   [Standard Google Ads remarketing](https://support.google.com/tagmanager/answer/6106960)
*   [Google Ads dynamic remarketing](https://support.google.com/tagmanager/answer/6106009)
*   [Measure users across domains](https://support.google.com/tagmanager/answer/6164469)
*   [gtag.js Developers: Measure users across domains](https://developers.google.com/analytics/devguides/collection/gtagjs/cross-domain)

##