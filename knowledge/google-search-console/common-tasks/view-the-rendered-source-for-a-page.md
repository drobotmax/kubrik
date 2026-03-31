> Source: https://support.google.com/webmasters/answer/11626894?hl=en

## Overview

When you visit a page, the website sends HTML code to your browser. Often this source code includes additional resources such as scripts, which must be loaded, and which may alter the page code.

Right-clicking "show source" typically shows only the original page code returned to the browser, before scripts and other resources have been loaded and run. But there are many instances, particularly when troubleshooting your page, when you need to see the code of the final, rendered page on the browser, after all resources have been loaded, and any scripts run. For example:

*   To search for Google Analytics or Google Tag Manager tags used in verification.
*   To debug page loading and display (that is, to check that all libraries and other resources that you want to be loaded are).
*   To look at structured data on the served page.

## How to view the rendered source

Here are a few methods to view the rendered source code for a web page:

*   **In the Chrome browser:**Right-click any part of the page and select**Inspect**to see all the HTML from the rendered page. Search for items in the rendered HTML with `Control + F`(Windows) or `Command + F` (Mac).
*   **For a page on your own site:**
    1.   [Inspect the URL](https://support.google.com/webmasters/answer/9012289), either by entering the URL directly in the URL Inspection tool, or by clicking an inspection link ![Image 1](https://storage.googleapis.com/support-kms-prod/4AWTCFaeOPxIbo9Hb8M7sIXXu4gFvA3MhQTN)next to a URL shown in most Search Console reports.
    2.   Click**Test live URL > View tested page**.
    3.   The**HTML**tab shows the rendered HTML for the page.

*   **For a page on any site,** not just a site that you own: 
    1.   Open the [Rich Results Test](https://search.google.com/test/rich-results).
    2.   Enter the URL of the page. The page must be available to Google without a login, and not blocked by [robots.txt](https://support.google.com/webmasters/answer/12818275).
    3.   Click**View tested page**.
    4.   The**HTML**tab shows the rendered HTML for the page.

##