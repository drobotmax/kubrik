> Source: https://support.google.com/analytics/topic/12270146?hl=en

## Measure ecommerce

[](https://support.google.com/analytics/topic/12270146?hl=en)[Next: [GA4] Set up ecommerce events](https://support.google.com/analytics/answer/12200568?hl=en&ref_topic=12270146)

This article is for anyone who owns an ecommerce website or app and is thinking about setting up Google Analytics ecommerce measurement.

## Overview

An ecommerce website or app is a store that sells products or services to customers digitally. It typically displays and describes products or services, lets customers purchase products or services, and accepts payments and returns.

Ecommerce measurement in Google Analytics lets you collect and analyze data about how customers interact with your ecommerce store. A developer needs to set up the [ecommerce events](https://support.google.com/analytics/answer/14434488) on your site or app to get started. No additional configuration is required.

Once set up, you'll begin to see data about what products people view, what they buy, and how they shop, typically within 24 to 48 hours of when users begin to use your tagged site or app.

## Benefits

Ecommerce measurement helps you understand what your customers like, how well your marketing works, and how to make your online store better to increase sales and engagement. For example, by implementing ecommerce events, you can figure out which colors are most popular, how large the average order value is, and whether certain promotions increase purchases.

Once you're collecting ecommerce event data, in addition to using the data in your reports, you can use the data in audiences for analyzing different groups of users and for exporting the data to advertising platforms like Google Ads so you can run more data-driven advertisements.

## [Ecommerce setup](https://support.google.com/analytics/topic/12270146?hl=en)

Setting up ecommerce measurement can be straightforward, depending on how you've set up your website or app:

*   **Website builders (like Shopify or WooCommerce):** Website builders are web-based applications used to create and design websites with prebuilt templates and customization options. Website builders often have ecommerce events built into the website code. This means you can start analyzing data and using it for customer insights right away. For help, check the documentation for your website builder to see what's built into your website code; for example:

    *   [Learn about ecommerce measurement on Shopify](https://help.shopify.com/en/manual/reports-and-analytics/google-analytics/tracking-ecommerce-events-using-analytics)

    *   [Learn about ecommerce measurement on Woocommerce](https://woo.com/document/google-analytics-integration/)

*   **Custom websites or mobile apps, or enhanced website builder functionality:** If your site or app is custom-made or you want more ecommerce features than your website builder offers, you'll need to set up ecommerce events manually. This involves defining each product or service you sell and ensuring these events are correctly placed and triggered on your site or app for accurate data. For help, we've created resources with examples of the ecommerce events that a developer will need to set up, with instructions on setting them up in your website or app.

    *   [Set up ecommerce events on a website with gtag.js](https://developers.google.com/analytics/devguides/collection/ga4/ecommerce?client_type=gtag)

    *   [Set up ecommerce events on a website with Google Tag Manager](https://developers.google.com/analytics/devguides/collection/ga4/ecommerce?client_type=gtm)

    *   [Set up ecommerce events on an app with the Google Analytics for Firebase SDK](https://firebase.google.com/docs/analytics/measure-ecommerce)

## Ecommerce dimension support

You can gather ecommerce data directly within Google Analytics reporting:

*   **Dimension availability**: Default and custom ecommerce dimensions can be selected in the ecommerce category within dimension pickers for secondary dimensions, filters, comparisons, and customization, giving you flexibility in analyzing ecommerce data.
*   **Compatibility**: 
    *   For filters, comparisons, and customization pickers, incompatible ecommerce dimensions are displayed.
    *   For secondary dimensions, incompatible ecommerce dimensions are greyed out.
    *   Existing comparisons using item-scoped dimensions are disabled when users switch to reports with incompatible concepts.

*   **Match type support**: You can use any available match type when filtering or making comparisons and customizations using ecommerce dimensions, as long as the report is entirely item-scoped.

**Note**: You can only filter or make comparisons and customizations within reports for ecommerce dimensions using “exactly match” if event-scoped data is present in a report.

[](https://support.google.com/analytics/topic/12270146?hl=en)[Next: [GA4] Set up ecommerce events](https://support.google.com/analytics/answer/12200568?hl=en&ref_topic=12270146)

##