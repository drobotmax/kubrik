> Source: https://support.google.com/webmasters/answer/10351509?hl=en

**Topics**

*   [Managing properties and settings](https://support.google.com/webmasters/answer/10351509?hl=en#managing)
    *   Manage site settings
    *   Add a property
    *   Remove a property
    *   Add/remove associations
    *   Move your site to another host

*   [Monitoring](https://support.google.com/webmasters/answer/10351509?hl=en#monitoring)
    *   Basic Search Console usage
    *   Check your index coverage (how much of my site is on Google?)
    *   Monitor your AMP coverage on Google
    *   Monitor your [rich result](https://support.google.com/webmasters/answer/7506797) coverage
    *   Monitor your sitemap coverage
    *   Monitor your site traffic from Google
    *   Monitor your page usability
    *   Monitor your Core Web Vitals statistics (LCP/FID/CLS)

*   [Troubleshooting](https://support.google.com/webmasters/answer/10351509?hl=en#troubleshooting)
    *   Why is a page or site missing from Google?
    *   Why is a rich result not visible on Google?
    *   Debugging traffic drops
    *   Debugging ranking drops
    *   Problems with a search snippet

*   [Testing](https://support.google.com/webmasters/answer/10351509?hl=en#testing)
*   [Crawling/Indexing](https://support.google.com/webmasters/answer/10351509?hl=en#crawling-indexing)
    *   Ask Google to crawl (or recrawl) your page
    *   Temporarily block pages or images from Google
    *   Request a crawl or recrawl
    *   Submit/monitor sitemap coverage

## [](https://support.google.com/webmasters/answer/10351509?hl=en)Managing properties and settings

### Manage site settings

Site settings are accessible by clicking the Setting gear ![Image 1: Settings](https://lh3.googleusercontent.com/oyYmLH7WiMYp3MZfUMAXaTyojw4lv4t9lNMat9eUz3wxsQTJ7hSD91gBKW10q-VaROs=h36) at the bottom of the [navigation pane](https://support.google.com/webmasters/answer/10352053). [See your site settings.](https://search.google.com/search-console/settings)

User settings are available by clicking the icon at the top of the page. User settings affect your Search Console behavior regardless of property, such as which messages you should receive emails for. [See your user settings.](https://search.google.com/search-console/user-settings)

### Add a property

[See how to add a website property.](https://support.google.com/webmasters/answer/34592) If you can perform verification for a [Domain-level property](https://support.google.com/webmasters/answer/10432272), we generally recommend a Domain-level property over a [URL-prefix property](https://support.google.com/webmasters/answer/10432366), when appropriate, because it combines http and https traffic as well as traffic to all subdomains of your property's domain.

### Remove a property

[Learn how to remove yourself or someone else from your property.](https://support.google.com/webmasters/answer/9357768)

### Add/remove associations

Associations are managed using the [Associations page](https://search.google.com/search-console/settings/associations). ([Documentation here](https://support.google.com/webmasters/answer/9419894))

### Move your site to another host

When moving your site to another URL host (say from example.com to example.org or example2.com) you might want to [follow these migration instructions](https://developers.google.com/search/docs/advanced/crawling/site-move-with-url-changes) to prevent losing too much Google traffic during the move.

## [](https://support.google.com/webmasters/answer/10351509?hl=en)Monitoring

### Basic Search Console usage

Read this guide to [basic day-to-day Search Console usage](https://support.google.com/webmasters/answer/6258314), if you're not a full-time SEO.

### Check your index coverage (how much of my site is on Google?)

Ideally, Google should have all the important [canonical pages](https://developers.google.com/search/docs/advanced/crawling/consolidate-duplicate-urls#expandable-1) (that is, non-duplicate pages) for your site indexed. It can take some time for new pages to appear, and you can help Google find new or updated pages by [publishing a sitemap or asking for a crawl](https://developers.google.com/search/docs/advanced/crawling/ask-google-to-recrawl).

**For smaller sites** (a few hundred pages or fewer), or if you**just want to check a page or two**, simply search for a given URL on Google.

Another useful trick is to use the site: search operator to limit results to a given host or path, and optionally provide search terms within that path to see which pages Google has indexed. For example:

*   The search term `site:example.com` returns (almost) all results indexed on example.com
*   The search term `site:example.com/pets` returns only indexed pages under the path example.com/pets
*   The search term `site:example.com/pets food` returns only indexed pages under the path example.com/pets that match the term "food"

To see general coverage **for larger sites**, use the [Coverage report](https://support.google.com/webmasters/answer/7440203). Ideally, the number of URLs in the report should be roughly the same as the number of URLs on your site, and the important URLs should be marked Valid, few (if any) URLs should be marked Error, and the duplicate or possibly unimportant pages can be marked Excluded. Read the documentation for the report to understand all the details.

If important pages are missing, see the [troubleshooting section](https://support.google.com/webmasters/answer/10351509?hl=en#missing_page_or_site).

**Don't expect 100% coverage of your site**

For various reasons, Google almost certainly won't have every single page of your site in the index. The important thing is that Google has indexed the canonical (non-duplicate) versions of your important pages.

### Monitor your AMP coverage on Google

Use the [AMP Status report](https://support.google.com/webmasters/answer/7450883) to see how many of your AMP pages have been found and indexed, and any indexing problems encountered. Read the documentation for that report to understand what to look for, and how to interpret the report's results.

If a page has issues, click into the report and click the **Inspect**![Image 2](https://storage.googleapis.com/support-kms-prod/4AWTCFaeOPxIbo9Hb8M7sIXXu4gFvA3MhQTN) icon next to a URL in the examples table to troubleshoot that URL in the [URL Inspection tool](https://support.google.com/webmasters/answer/9012289). Confirm that the AMP version is accessible by Google, indexable, and properly linked, and that Google has no parsing issues.

If many pages seem to be missing, inspect a few of the pages to see what is preventing it from being indexed. When many pages are missing, they often share a common indexing issue.

To monitor your AMP traffic on Google use the [Performance reports](https://support.google.com/webmasters/topic/9384513), and filter by search appearance of the appropriate AMP type (or view the **Search Appearance**or**Discover Appearance**tab).

### Monitor your rich result coverage

Search Console will provide a [Rich Result report](https://support.google.com/webmasters/answer/7552505) for every [rich result type](https://developers.google.com/search/docs/advanced/appearance/search-result-features)that Google creates for your site. You can find these reports in the **Enhancements** section of the navigation bar. If Google found structured data that couldn't be parsed, it will create an [Unparseable Structured Data report](https://support.google.com/webmasters/answer/9166415).

### Monitor your sitemap coverage

Use the [Sitemaps report](https://support.google.com/webmasters/answer/7451001) to monitor parsing issues for any sitemaps submitted using that report.

Additionally, you can filter the Coverage report to show only URLs covered by a specific sitemap (limited to sitemaps submitted using the Sitemaps report).

### Monitor your site traffic from Google

The [Performance reports](https://support.google.com/webmasters/topic/9384513) show your traffic on various Google platforms, including Search, Discover, and News. You will only have Discover or News versions of this report if you have sufficient data for the report.

These reports allow you to filter by URL, date, type of Search result, and more. Read the documentation to fully understand the report.

### Monitor your page usability

Make sure you're providing an overall[good page experience](https://developers.google.com/search/docs/guides/page-experience).To test page experience of a specific URL, [test the URL](https://support.google.com/webmasters/answer/10351509?hl=en#testing) Core Web Vitals and whether it uses HTTPS.

### Monitor your Core Web Vitals statistics (LCP/FID/CLS)

See site-wide statistics on the speed and responsiveness for your site, based on actual user data, for the key metrics of [largest contentful paint](https://web.dev/articles/lcp), [first input delay](https://web.dev/articles/fid) and [Cumulative Layout Shift](https://web.dev/articles/cls/)

## [](https://support.google.com/webmasters/answer/10351509?hl=en)Troubleshooting

### [](https://support.google.com/webmasters/answer/10351509?hl=en)Why is a page or site missing from Google?

*   For missing pages, [read the missing page guide](https://support.google.com/webmasters/answer/7474347).
*   If your site is blocked in the browser, [read here](https://support.google.com/webmasters/answer/6347750).

### Why is a rich result not visible on Google?

If you have implemented structured data but it isn't appearing in Google, [follow these troubleshooting steps](https://support.google.com/webmasters/answer/9079920?ref_topic=9163961#rich_result).

### Debugging traffic drops

See [this help page](https://support.google.com/webmasters/answer/9079473) and this blog post to troubleshoot drops in traffic from Google to your site.

### Debugging ranking drops

See [this help page for troubleshooting ranking drops in Google Search](https://support.google.com/webmasters/answer/9079473).

### Problems with a search snippet

If a search snippet for your site is too short, too long, or doesn't seem to describe your page accurately, [see here](https://support.google.com/webmasters/answer/9079920).

## [](https://support.google.com/webmasters/answer/10351509?hl=en)Testing

The following site testing tools are available in Search Console:

*   [**URL Inspection tool**](https://support.google.com/webmasters/answer/9012289): A comprehensive testing tool that provides indexing, crawling, AMP, and structured data information about a page. For complex debugging for all types of issues on both the live or indexed version of this page, use this tool. You must own the property to be able to use this tool.
*   [**AMP test**](https://support.google.com/webmasters/answer/7320015): Test whether the page fulfills Google AMP requirements. Works on the live page only; no information about the indexed version of the page. You need not own the property or be logged in to use this tool.
*   [**Rich results test**](https://support.google.com/webmasters/answer/7445569): Test whether Google is able to process rich results structured data on a page. Works on the live page only; no information about the indexed version of the page. You need not own the property or be logged in to use this tool.

**Note** that the default view in the URL Inspection tool is the _indexed_ version of the URL. All other tools only test the _live_ version of the page. If the page has changed since the last crawl, the indexed (URL Inspection) result will be different than the live tester's result. However, if you click **Test live URL** in the URL Inspection tool, you should see the same results as in the other live testing tool.

## [](https://support.google.com/webmasters/answer/10351509?hl=en)[Crawling](https://support.google.com/webmasters/answer/7646114)/[Indexing](https://support.google.com/webmasters/answer/7645831)

### Ask Google to crawl (or recrawl) your page

If you've recently added or made changes to a page on your site, you can request that Google re-index your page using [any of the methods listed here](https://developers.google.com/search/docs/advanced/crawling/ask-google-to-recrawl).

### Temporarily block pages or images from Google

To temporarily (6 months) remove pages or images _**on sites that your own**_ from Google, use the [Removals tool](https://support.google.com/webmasters/answer/9689846).

### Request a crawl or recrawl

The simplest way to request a crawl **for a single page** is using the [URL Inspection tool](https://support.google.com/webmasters/answer/9012289):

1.   [Open the tool](https://search.google.com/search-console?action=inspect).
2.   Enter the full URL of the page and click **Enter**.
3.   Click **Request indexing**. The request will fail immediately if there is an access problem with the page. The request will fail silently if you have exceeded your quota of indexing requests.

**To request a crawl for multiple pages,**[use a sitemap](https://support.google.com/webmasters/answer/6065812#sitemap).

### Submit a sitemap, monitor submitted sitemaps, monitor index coverage of URLs in a sitemap

To submit a sitemap, or monitor whether Google could read your submitted sitemap, use the [Sitemaps report](https://support.google.com/webmasters/answer/7451001).

Note that the Sitemaps report shows information only about sitemaps submitted using that report. Sitemaps found independently by Google won't be shown there. However, you can submit a sitemap through the report even if Google already knows about it, in order to be able to monitor Google's crawl attempts.

The only ways to block a sitemap from being read are to delete the sitemap or block it using [robots.txt](https://support.google.com/webmasters/answer/12818275).

To monitor indexed URLs by sitemap, choose a sitemap in the dropdown selector on the [Page Indexing report](https://search.google.com/search-console/index).