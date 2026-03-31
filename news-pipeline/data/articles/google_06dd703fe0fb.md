# Google’s Commerce Media Suite: Where retailer insights meet the power of YouTube

Source: https://blog.google/products/marketingplatform/360/googles-commerce-media-suite-where-retailer-insights-meet-the-power-of-youtube/
Platform: google
Date: 2026-03-24
Fetched: 2026-03-31

---


        Kroger joins Google’s Commerce Media Suite

    {
        "@context": "https://schema.org",
        "@type": "NewsArticle",
        "mainEntityOfPage": "https://blog.google/products/marketingplatform/360/googles-commerce-media-suite-where-retailer-insights-meet-the-power-of-youtube/",
        "headline": "Google’s Commerce Media Suite: Where retailer insights meet the power of YouTube",
        "datePublished": "2026-03-24T13:00:00+00:00",
        "dateModified": "2026-03-24T15:49:38.909792+00:00",
        "description": "Supercharge performance across the full customer journey by connecting Kroger’s shopper insights with Google’s AI and scale.",
        "author": {
            "@type": "Person",
            "name": "Marta Martinez"
        },
        "publisher": {
            "@type": "Organization",
            "name": "Google",
            "logo": {
                "@type": "ImageObject",
                "url": "https://blog.google/static/blogv2/images/google-1000x1000.png?version=pr20260319-1641",
                "width": "200",
                "height": "200"
            }
        },
        "image": {
            "@type": "ImageObject",
            "url": "https://storage.googleapis.com/gweb-uniblog-publish-prod/images/Google_CMN_Banner_static.width-1300.png",
            "width": "1440",
            "height": "810"
        },
        "speakable": {
            "@type": "SpeakableSpecification"
        }
    }

          document.querySelectorAll('.deferred-stylesheet').forEach(function(link) {
            function enableStylesheet() {
              if (link.rel !== 'stylesheet') {
                link.rel = 'stylesheet';
              }
            }

            // Attach the normal load-listener
            link.addEventListener('load', enableStylesheet);

            // Safely check if Performance API is supported
            if (window.performance && typeof performance.getEntriesByType === 'function') {
              // Check the Performance entries buffer for a matching URL
              const url = link.href;
              const alreadyFetched = performance
                .getEntriesByType('resource')
                .some(entry => entry.name === url);

              if (alreadyFetched) {
                // Preload was fulfilled (from cache or just fast), so activate now
                enableStylesheet();
              }
            }
          });

  let trustedTypePolicy = {
      createHTML: (str) => str,
      createScript: (str) => str,
      createScriptURL: (url) => url
  };
  if (window.trustedTypes && window.trustedTypes.createPolicy) {
      const safeScriptDomains = [
          'blob:',
          '/static/blogv2/',
          '/static/keyword/',
          '/static/youtube/',
          '/static/blog_youtube/',
          '//cdn.ampproject.org/',
          '//googleads.g.doubleclick.net',
          '//survey.g.doubleclick.net',
          '//www.google-analytics.com/',
          '//www.google.com',
          '//www.googletagmanager.com',
          '//www.gstatic.com',
          '//www.youtube.com',
          '//youtube.googleapis.com',
          '//ssl.gstatic.com/trends_nrtr/'
      ];
      const safeScripts = [
          'google_tag_manager[""]',
          '(function anonymous('
      ];
      trustedTypePolicy = window.trustedTypes.createPolicy('default', {
          /* Enable create HTML */
          createHTML: (str) => {
              return str
          },
          /* Enable script creation */
          createScript: (str) => {
              const safeScriptString = safeScripts.find(
                  (safeScript) => str.includes(safeScript)
              );
              if (!safeScriptString) {
                  console.warn(
                      `unsafe createScript: "${str}"`
                  );
              }

              return str;
          },
          /* Allow for safe domains only */
          createScriptURL: (url) => {
              const safeDomainsUrl = safeScriptDomains.find(
                  (safeDomain) => url.includes(safeDomain)
              );
              if (!safeDomainsUrl && !url.startsWith(window.location.origin)) {
                  console.warn(
                      `Unsafe createScriptURL: "${url}"`
                  );
              }

              return url;
          },
      });
  }

  window.trustedTypePolicy = trustedTypePolicy;

<div class="data-layer-init-data" data-ga4-analytics='
  {
    "event": "dataLayer_initialized",

      "page_name": "Kroger joins Google’s Commerce Media Suite",

    "experiments": "undefined",
    "locale": "en-us",
    "page_type": "blogv2 | article page",
    "primary_tag": "products - google marketing platform",
    "secondary_tags": "Google Ads",

      "landing_page_tags": "products - google ads",

      "article_name": "Google’s Commerce Media Suite: Where retailer insights meet the power of YouTube",
      "author_name": "Marta Martinez",

    "publish_date": "2026-03-24|13:00",
    "hero_media": "mp4",

      "special_hero": "undefined",

    "days_since_published": "7",

      "content_category": "Products - Google Marketing Platform",

    "word_count": "medium 300-599",
    "has_audio": "no",
    "has_video": "yes"
  }'>

  (function() {
    var dataLayerInitElement = document.querySelector('.data-layer-init-data');
    var dataLayerObject = JSON.parse(
      dataLayerInitElement.getAttribute('data-ga4-analytics')
    );

    // Change undefined strings to primitive value undefined.
    Object.entries(dataLayerObject).forEach(([key, value]) => {
      dataLayerObject[key] = value === 'undefined' ? undefined : value;
    });

    if (!window['dataLayer']) {
      window['dataLayer'] = [];
    }
    window['dataLayer'].push(dataLayerObject);
  }());

    <script
      id="feedback-surveys-json"
      type="application/json"

      >
      [{"model": "blogsurvey.survey", "pk": 17, "fields": {"name": "Article survey - level of detail - Jan 2026", "survey_id": "article-survey-level-of-detail-jan-2026_260127", "scroll_depth_trigger": 75, "previous_survey": null, "display_rate": 75, "participation_prompt": "Help us improve The Keyword with a one-question survey", "participation_prompt_disclaimer": "This survey is anonymous. All responses will be aggregated and used only for analysis to improve our services.", "thank_message": "Thank you!", "thank_emoji": "✅", "questions": "[{\"id\": \"28b29c1a-755e-4789-888f-12d0491a3e0a\", \"type\": \"simple_question\", \"value\": {\"question\": \"Did this article provide the level of detail you were looking for?\", \"responses\": [{\"id\": \"66f88e6a-4fa6-418f-ba13-31f3c1dda823\", \"type\": \"item\", \"value\": \"Yes, I got what I needed\"}, {\"id\": \"78927bfc-17be-4e0f-aacf-8a2f2a3d333d\", \"type\": \"item\", \"value\": \"No, I wanted more technical depth\"}, {\"id\": \"b685a5ac-bb2e-42eb-a1cb-ce64341b9c06\", \"type\": \"item\", \"value\": \"No, I wanted a simpler overview\"}, {\"id\": \"06e8f828-5dcf-4736-81fb-43c23e932d1b\", \"type\": \"item\", \"value\": \"I was looking for something else entirely\"}]}}]", "target_article_pages": true, "target_short_post_pages": false, "target_primary_only_tag": true}}]

    <a href="#jump-content" class="h-c-header__jump-to-content"
        data-glue-jump-link>
      Skip to Main Content

      <svg

  class="h-c-header__hamburger-img h-c-header__hamburger-img--standard events-off"

  role="presentation"

>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20260319-1641#h-burger">

        <svg
  aria-label="The Google logo"

  role="img"

>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20260319-1641#h-color-google-logo">

            Marketing Platform

  Google’s Commerce Media Suite: Where retailer insights meet the power of YouTube
  <div class="uni-article-progress-bar__social"
    data-analytics-module='{
      "module_name": "Progress Bar",
      "section_header": "Google’s Commerce Media Suite: Where retailer insights meet the power of YouTube"
    }'
  >

    <svg

  class="h-c-icon h-c-icon--color-text"

  aria-hidden="true"
  title="Share"

>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20260319-1641#social-share">

    Share

<a aria-label="Share on X"
    class="article-share__link-text uni-click-tracker"
    href="https://twitter.com/intent/tweet?text=Google%E2%80%99s%20Commerce%20Media%20Suite%3A%20Where%20retailer%20insights%20meet%20the%20power%20of%20YouTube%20%40google&url=https://blog.google/products/marketingplatform/360/googles-commerce-media-suite-where-retailer-insights-meet-the-power-of-youtube/"
    target="_blank"
    data-ga4-method="twitter">
  <svg

  class="h-c-icon h-c-icon--social h-c-icon--30px"

  aria-hidden="true"

  viewBox="0 0 30 30"

>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20260319-1641#social-x">

  x.com

<a aria-label="Share on Facebook"
    class="article-share__link-text uni-click-tracker"
    href="https://www.facebook.com/sharer/sharer.php?caption=Google%E2%80%99s%20Commerce%20Media%20Suite%3A%20Where%20retailer%20insights%20meet%20the%20power%20of%20YouTube&u=https://blog.google/products/marketingplatform/360/googles-commerce-media-suite-where-retailer-insights-meet-the-power-of-youtube/"
    target="_blank"
    data-ga4-method="facebook">
  <svg

  class="h-c-icon h-c-icon--social h-c-icon--30px"

  aria-hidden="true"

  viewBox="0 0 30 30"

>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20260319-1641#social-facebook">

  Facebook

<a aria-label="Share on LinkedIn"
    class="article-share__link-text uni-click-tracker"
    href="https://www.linkedin.com/shareArticle?mini=true&url=https://blog.google/products/marketingplatform/360/googles-commerce-media-suite-where-retailer-insights-meet-the-power-of-youtube/&title=Google%E2%80%99s%20Commerce%20Media%20Suite%3A%20Where%20retailer%20insights%20meet%20the%20power%20of%20YouTube"
    target="_blank"
    data-ga4-method="linkedin">
  <svg

  class="h-c-icon h-c-icon--social h-c-icon--30px"

  aria-hidden="true"

  viewBox="0 0 30 30"

>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20260319-1641#social-linkedin">

  LinkedIn

<a aria-label="Share with Email"
    class="article-share__link-text uni-click-tracker article-share__email"

      href="mailto:?subject=Google%E2%80%99s%20Commerce%20Media%20Suite%3A%20Where%20retailer%20insights%20meet%20the%20power%20of%20YouTube&body=Check out this article on the Keyword:%0A%0AGoogle%E2%80%99s%20Commerce%20Media%20Suite%3A%20Where%20retailer%20insights%20meet%20the%20power%20of%20YouTube%0A%0ASupercharge performance across the full customer journey by connecting Kroger’s shopper insights with Google’s AI and scale.%0A%0Ahttps://blog.google/products/marketingplatform/360/googles-commerce-media-suite-where-retailer-insights-meet-the-power-of-youtube/"

    target="_blank"
    data-ga4-method="email">
  <svg

  class="h-c-icon h-c-icon--social h-c-icon--30px"

  aria-hidden="true"

  viewBox="0 0 30 30"

>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20260319-1641#social-mail">

  Mail

<div class="copy-link uni-copy-share uni-click-tracker"
  data-component="uni-copy-popup-component"
  data-ga4-analytics-share-copy-link
  data-ga4-method="Copy link">

  <button class="copy-link__trigger copy-link__trigger-text"
    data-ga4-method="Copy link"
    title="Copy link">
    <svg

  class="h-c-icon h-c-icon--color-text"

  role="presentation"

  title="Copy link"

>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20260319-1641#social-link">

    Copy link

  {
    "find_an_article": "Find an article...",
    "rss_link": "/rss/",
    "rss_feed": "RSS feed",
    "press_corner": "Press corner",
    "press_corner_slug": "press/",
    "secondary_menu": "Secondary menu",
    "search": "Search",
    "submit": "Submit",
    "close": "Close",
    "execute_search": "Execute search",
    "dismiss_search": "Dismiss search",
    "suggested_results_for": "[[number]] suggested results for [[query_term]]",
    "by_string": "By",
    "conjunction_symbol": "\u0026",
    "suggested_searches": "Suggested searches",
    "images": "Images",
    "image_library_slug": "image\u002Dlibrary/"
  }

<uni-search-bar
  class="uni-search-bar"
  search-placeholder="Ask a question or enter a keyword"
  page-locale="en-us"
  onboarding-text="Search freely using keywords, or by asking a question"
  site-id="2"

    hide-language-picker="true"
    rss-feed-url="/products/marketingplatform/rss/"

  >

    ["How is Gemini changing Maps?", "What is \"vibe design?\"", "How can I learn new AI skills?"]

        <div class="article-hero__primary-tag__col"
          data-analytics-module='{
            "module_name": "Article Hero",
            "section_header": "Google’s Commerce Media Suite: Where retailer insights meet the power of YouTube"
          }'>
          <a class="article-hero__primary-tag article-hero__primary-tag--link uni-spacer-2-bottom"
            href="https://blog.google/products/marketingplatform/"
            data-ga4-analytics-eyebrow-click='{
  "link_text": "Google Marketing Platform",
  "link_url": "https://blog.google/products/marketingplatform/",
  "link_type": "internal"
}'

data-ga4-analytics-landing-lead='{
  "event": "landing_page_lead",
  "link_text": "Google Marketing Platform"
}'

          >
            Google Marketing Platform

    Google’s Commerce Media Suite: Where retailer insights meet the power of YouTube

  {
    "reading_time": "[[read\u002Dtime]] min read"
  }

<div class="article-meta__author-container"
  data-analytics-module='{
    "module_name": "Hero Menu",
    "section_header": "Google’s Commerce Media Suite: Where retailer insights meet the power of YouTube"
  }'>

            Mar 24, 2026

            ·

    <svg

  class="h-c-icon h-c-icon--color-text"

  aria-hidden="true"
  title="Share"

>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20260319-1641#social-share">

    Share

<a aria-label="Share on X"
    class="article-share__link-text uni-click-tracker"
    href="https://twitter.com/intent/tweet?text=Google%E2%80%99s%20Commerce%20Media%20Suite%3A%20Where%20retailer%20insights%20meet%20the%20power%20of%20YouTube%20%40google&url=https://blog.google/products/marketingplatform/360/googles-commerce-media-suite-where-retailer-insights-meet-the-power-of-youtube/"
    target="_blank"
    data-ga4-method="twitter">
  <svg

  class="h-c-icon h-c-icon--social h-c-icon--30px"

  aria-hidden="true"

  viewBox="0 0 30 30"

>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20260319-1641#social-x">

  x.com

<a aria-label="Share on Facebook"
    class="article-share__link-text uni-click-tracker"
    href="https://www.facebook.com/sharer/sharer.php?caption=Google%E2%80%99s%20Commerce%20Media%20Suite%3A%20Where%20retailer%20insights%20meet%20the%20power%20of%20YouTube&u=https://blog.google/products/marketingplatform/360/googles-commerce-media-suite-where-retailer-insights-meet-the-power-of-youtube/"
    target="_blank"
    data-ga4-method="facebook">
  <svg

  class="h-c-icon h-c-icon--social h-c-icon--30px"

  aria-hidden="true"

  viewBox="0 0 30 30"

>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20260319-1641#social-facebook">

  Facebook

<a aria-label="Share on LinkedIn"
    class="article-share__link-text uni-click-tracker"
    href="https://www.linkedin.com/shareArticle?mini=true&url=https://blog.google/products/marketingplatform/360/googles-commerce-media-suite-where-retailer-insights-meet-the-power-of-youtube/&title=Google%E2%80%99s%20Commerce%20Media%20Suite%3A%20Where%20retailer%20insights%20meet%20the%20power%20of%20YouTube"
    target="_blank"
    data-ga4-method="linkedin">
  <svg

  class="h-c-icon h-c-icon--social h-c-icon--30px"

  aria-hidden="true"

  viewBox="0 0 30 30"

>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20260319-1641#social-linkedin">

  LinkedIn

<a aria-label="Share with Email"
    class="article-share__link-text uni-click-tracker article-share__email"

      href="mailto:?subject=Google%E2%80%99s%20Commerce%20Media%20Suite%3A%20Where%20retailer%20insights%20meet%20the%20power%20of%20YouTube&body=Check out this article on the Keyword:%0A%0AGoogle%E2%80%99s%20Commerce%20Media%20Suite%3A%20Where%20retailer%20insights%20meet%20the%20power%20of%20YouTube%0A%0ASupercharge performance across the full customer journey by connecting Kroger’s shopper insights with Google’s AI and scale.%0A%0Ahttps://blog.google/products/marketingplatform/360/googles-commerce-media-suite-where-retailer-insights-meet-the-power-of-youtube/"

    target="_blank"
    data-ga4-method="email">
  <svg

  class="h-c-icon h-c-icon--social h-c-icon--30px"

  aria-hidden="true"

  viewBox="0 0 30 30"

>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20260319-1641#social-mail">

  Mail
