> Source: https://support.google.com/webmasters/answer/12660034?hl=en

If your website has been identified by Google as an online merchant, you may see the following tools and reports on Search Console about shopping experiences available on Google:

*   A report titled **Merchant opportunities**under**Shopping**.
*   A setting titled **Shipping and returns** under **Settings**>**Shopping**(if you’ve associated a Merchant Center account with your Search Console property)

Site status is determined programmatically by Google. You can read more about[Product snippets and Merchant listings here](https://developers.google.com/search/docs/advanced/structured-data/product). Eligible sites are those that primarily exist to sell physical goods or have Product structured data on your site.

**[](https://support.google.com/webmasters/answer/12660034?hl=en)What is an online merchant?**

An online merchant is a site that sells physical goods or services directly to consumers (not to other businesses) on that site. Websites that redirect users to other sites (affiliate sites), or don't allow purchase completion on the site, are not considered online merchants for Search Console's reporting purposes.

The Shopping section in Search Console could include the following reports, depending on what kind of structured data Google found on your site:

## Product snippet rich report

This is a [rich result report](https://support.google.com/webmasters/answer/7552505) for [Product snippet structured data](https://developers.google.com/search/docs/advanced/structured-data/product-snippet) found on your site. Product snippet items can be shown as typical web search results with visual enhancements—for example, product ratings and prices. This report will be present if Google found Product snippet structured data on your site.

## Merchant listing rich report

This is a [rich result report](https://support.google.com/webmasters/answer/7552505) for [Merchant listing structured data](https://developers.google.com/search/docs/advanced/structured-data/merchant-listing) found on your site. Merchant listings are an extension of the Product snippet items that enable more full-featured search results and always include a price. For example, they might appear in a carousel of similar products from different sellers, or in a knowledge panel in search results.

## Merchant opportunities

The Merchant opportunities report shows recommendations for improving how your online shop appears on Google. You'll see this report if you have an eligible site that sells physical goods.

If you see the Merchant opportunities report but not the [Product snippet](https://support.google.com/webmasters/answer/7552505)[rich result](https://support.google.com/webmasters/answer/7506797) report or the Merchant listing rich result report, this means that either:

*   Google hasn’t found structured data on your site, or
*   Google found structured data, but the sample data used by Search Console to generate reports doesn't contain any entity data.

If you see the Product snippet or Merchant listings rich result reports and not the Merchant opportunities report, Google found structured data on your site, but doesn’t recognize your site as an online shop that sells physical goods.

## Shipping and returns

This setting can be found under **Settings**>**Shopping** for online merchants to use Search Console to add, view and manage [shipping and return settings](https://support.google.com/webmasters/answer/14907594).

Only available to owners or full users of a Search Console property. If you have a Merchant Center account, you’ll need to [associate it with your Search Console property](https://support.google.com/webmasters/answer/9419894?hl=en&sjid=6935562983160265888-NC#zippy=%2Crequest-an-association).

**If you're a merchant but you're not seeing the shopping section in Search Console**

Make sure that you have valid [Merchant listing structured data](https://developers.google.com/search/docs/advanced/structured-data/merchant-listing) on your website. You can check whether Google has found and indexed any valid Merchant listing items on your site by opening your [Merchant listings structured data report](https://search.google.com/search-console/r/merchant-listings). If the report is not present, then Google hasn't found any structured data on your site. If the report is present, make sure that your Merchant listings are valid.

##