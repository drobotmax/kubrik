# KUBRIK News Pipeline Run | 2026-03-31

Articles: 0 | KB Updates: 0 | Skipped: 0

## Status: ERROR - No articles fetched

The digest script ran successfully but returned an empty digest.
All RSS feed fetches failed with HTTP 403 (network access blocked in sandbox environment).

**Feeds attempted:**
- Google Ads Blog: https://blog.google/products/ads-commerce/rss/ -> 403
- Yandex Ads News: https://yandex.ru/adv/news/rss -> 403
- Meta Business News: https://www.facebook.com/business/news -> 403

**WebFetch fallback also failed (all sources returned 403):**
- https://developers.facebook.com/blog/ -> 403
- https://searchengineland.com/feed -> 403
- https://www.seroundtable.com/category/google-ads -> 403
- https://developers.google.com/google-ads/api/docs/release-notes -> 403

## KB Updates

None.

## Notify Only

None.

## Breaking

None.

## Action Required

Configure network access or a proxy in the pipeline environment to allow outbound HTTP requests to external RSS feeds.

Commit: no changes
