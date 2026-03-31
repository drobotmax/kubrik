> Source: https://support.google.com/merchants/answer/14166401?hl=en

Key event tracking, when enabled in Merchant Center, allows you to monitor your sales using specific key event metrics related to purchases. Key event tracking helps you identify which products and keywords are most successful for your business.

This article explains how key event tracking works and provides instructions on how to set it up in Merchant Center.

* * *

**On this page**

*   [Benefits of key event tracking](https://support.google.com/merchants/answer/14166401?hl=en#benefits)
*   [How key event tracking works](https://support.google.com/merchants/answer/14166401?hl=en#how_it_works)
*   [Set up key event tracking](https://support.google.com/merchants/answer/14166401?hl=en#set_up_conversion_tracking)
*   [Remove key event tracking](https://support.google.com/merchants/answer/14166401?hl=en#Remove_conversion_tracking)
*   [Frequently asked questions](https://support.google.com/merchants/answer/14166401?hl=en#faqs)

* * *

## [](https://support.google.com/merchants/answer/14166401?hl=en)Benefits of key event tracking

*   **Performance measurement**: Key event tracking enables you to measure the success of your product sales. When used with a web analytics tool, key event tracking allows you to track how effectively your products are showing for free on Google. Key event tracking helps you get performance reports with insights about your free product listings – like whether they’ve led to purchases and how they compare to your overall Google traffic.
*   **Continuous Improvement**: Key event tracking provides a feedback loop for ongoing optimization of your products. You can continually refine and enhance your product offerings, and website based on product traffic and data-driven insights, leading to better results over time.
*   **Improved metrics**: Key event tracking plays an important role in understanding and improving metrics such as clicks, impressions, and click-through rate (CTR) to improve your online advertising and marketing.

* * *

## [](https://support.google.com/merchants/answer/14166401?hl=en)[How key event tracking works](https://support.google.com/merchants/answer/14763078)

After a customer clicks on your free product listings, key event tracking adds a bit of additional information—a parameter called a result id—to the URLs customers click through.

#### **Example**

If someone clicks on your free listings from www.example.com, the final URL will look like www.example.com/?srsltid=123xyz.

The result id is created at the time of an impression. If a customer clicks the same free listings again, the same result id will be used.

**Note**: When you create a new key event action, auto-tagging will be turned on automatically.

* * *

## [](https://support.google.com/merchants/answer/14166401?hl=en)Set up key event tracking

The 3 steps involved in setting up key event tracking include:

1.   Enabling auto-tagging
2.   Linking a key event source with 2 options: 
    1.   Link to Google Analytics property - This option requires linking an existing Google Analytics account.
    2.   Apply tags on your website - This option requires you to change your website’s code.

3.   Setting up a tag on your website

Key event tracking can either be automatically enabled by default for some Merchant Center accounts or enabled at the account level by an admin, depending on the account setup. To enable key event tracking, follow the steps below.

### Step 1 of 3: Enabling auto-tagging

1.   In your [Merchant Center account](https://merchants.google.com/), click the **Settings**![Image 1: Tools and setting menu icon [Gear]](https://storage.googleapis.com/support-kms-prod/vyDyoYvlunmkVyVjH9CZTw60xwyZpzKoWuPC) in the left navigation menu.
2.   Select **General**.
3.   Select **Key event setup** tab.
4.   Toggle on **Auto-tagging**. A banner will appear confirming that the auto-tagging feature is turned on. Now you can start adding key event sources.

### Step 2 of 3: Linking a key event source with 2 options

1.   Select **Add key event source**. You can either select to go through Google Analytics or through applying tags to your website.
2.   In “Select how to track product purchases”, you can select either “Link Google Analytics” or “Link your website”.
3.   If you have a Google Analytics 4 account, you can select “Link Google Analytics” and you can link your accounts to send key event details on purchases from Google Analytics to Merchant Center.
4.   If you don't have a Google Analytics 4 account, you can use a Google tag that sends purchase details directly from your website to Merchant Center. Select “Link your website” and select **Next**.

### Step 3 of 3: Setting up a tag on your website

1.   On the “Receive Tracking” page under “Configure key event tracking data” 
    1.   Add “Tracking name”.
    2.   Select “Attribution model”.
    3.   Select a “[Lookback window](https://support.google.com/merchants/answer/14281382)” of 7, 30, 40 days. 30 days is the recommended lookback window.
    4.   Select **Next**.

2.   On the “Send tracking” page under “Link your website tag to Merchant Center to track purchases” 
    1.   Select **Set up** button.
    2.   In the “Set up a Google tag” dialog, use “Install manually” to install the Google tag with gtag.js in your website code. 
        *   If you use a website builder or CMS like Wordpress, Shopify, or Wix, use the “Install with a CMS or website builder” option under “Show more options”.
        *   You can also reuse an existing Google tag by choosing the “Use a Google tag you already have” option under “Show more options”.

    3.   Next to the code snippet,select ![Image 2](https://lh3.googleusercontent.com/aVy1SLrN9LqA509b6pnY_WPapE6rif_AL1v2o4hAwzRlCyXdmbhgFZax0xX6LD6L9g=w28) to copy the code to your clipboard.
    4.   Paste the entire tag snippet in the code of every page of your website, immediately after the `<head>`element.
    5.   You can test that the tag is properly installed by clicking **Test installation**.
    6.   Close the dialog and select **Next.**

3.   On the “Define purchase event” page under “Define how to track a purchase event”, choose one of the 3 options below: 
    1.   Option 1: Add the key event URL. This is the URL of the page that a customer lands on after completing a purchase.
    2.   Option 2 & 3: Select **Advanced settings** for instructions on how to add a purchase event directly to your website when a page opens (Option 2) or when a button is clicked (Option 3).

4.   Select **Done**.

After you’ve configured the connection with the key event source, you’ll need to refresh the page to view the key event source added to the table in Merchant Center.

After you’re all set up, you’ll start viewing key event metrics in your [performance dashboard](https://support.google.com/merchants/answer/14152817).

As a reminder, you must ensure you're providing users with clear and comprehensive information about the data you collect on your apps, and getting [consent](https://www.google.com/about/company/user-consent-policy.html) for that collection where legally required.

* * *

## [](https://support.google.com/merchants/answer/14166401?hl=en)Remove key event tracking

To remove key event tracking, follow these steps:

1.   In your [Merchant Center account](https://merchants.google.com/), click the **Settings**![Image 3: Tools and setting menu icon [Gear]](https://storage.googleapis.com/support-kms-prod/vyDyoYvlunmkVyVjH9CZTw60xwyZpzKoWuPC) in the left navigation menu and select **General**.
2.   Select **Key event setup** tab.
3.   For a Google Analytics key event source, select **Remove access** in the table's "Actions" column next to the key event source that you wish to delete. In the pop-up window, select **Remove access**.
4.   For an Online store key event source, select **Delete** next to the key event source that you wish to delete. In the confirmation dialog box, select **Delete**.

* * *

## [](https://support.google.com/merchants/answer/14166401?hl=en)Frequently asked questions

## How do I view traffic from free listings in Google Analytics?

## What if my website doesn't allow URL parameters?

* * *

### Related links

*   [About traffic source dimensions](https://support.google.com/analytics/answer/1033173)

##