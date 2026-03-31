> Source: https://support.google.com/webmasters/answer/13144973?hl=en

If your page is blocked to Google by a [robots.txt](https://support.google.com/webmasters/answer/12818275) rule, it probably won't appear in Google Search results, and in the unlikely chance it does, the result [won't include a description](https://support.google.com/webmasters/answer/7489871).

## [](https://support.google.com/webmasters/answer/13144973?hl=en)1. Confirm that a page is blocked by robots.txt

**If you have [verified your site ownership](https://support.google.com/webmasters/answer/9008080)in Search Console:**

1.   [Open the URL Inspection tool](https://search.google.com/search-console?action=inspect).
2.   Inspect the URL shown for the page in the Google search result.Make sure that you've selected the Search Console property that contains this URL.
3.   In the inspection results, check the status of the**Page indexing**section. If it says**Blocked by robots.txt**, then you've confirmed the problem. Move to the next section to fix it.

**If you have not verified your site in Search Console:**

1.   [Search for a robots.txt validator](https://www.google.com/search?q=robots.txt+validator).
2.   In the validator, enter the URL of the page that is missing the description. Use the URL shown for the page in Google search results.
3.   If the validator say that the page is blocked to Google, you've confirmed the problem. Move to the next section to fix it.

## [](https://support.google.com/webmasters/answer/13144973?hl=en)2. Fix the rule

1.   Use a[robots.txt validator](https://www.google.com/search?q=robots.txt+validator)to find out which rule is blocking your page, and where your robots.txt file is.
2.   Fix or remove the rule: 
    *   **If you are using a website hosting service**—for example, if your site is on Wix, Joomla, or Drupal—we can't provide exact guidance how to update your robots.txt file because every hosting service has its own way to do this. Search your hosting provider's documentation to learn how to unblock your page or site to Google. Suggested terms to search for: "robots.txt _provider\_name_" or"unblock page to Google _provider\_name_". **Example search:**[robots.txt Wix](https://www.google.com/search?q=robots.txt+wix)
    *   **If you're able to modify your robots.txt file directly**, remove the rule, or else update it according to [robots.txt syntax](https://support.google.com/webmasters/answer/6062596).

##