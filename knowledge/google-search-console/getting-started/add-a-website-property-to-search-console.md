> Source: https://support.google.com/webmasters/answer/34592?hl=en

A _property_ is Search Console's term for a discrete thing that you can examine or manage in Search Console. A _website property_ represents a website: that is, all pages that share the common domain or URL prefix that you specify. You can manage multiple properties, and choose which one to see or manage using the [property selector](https://support.google.com/webmasters/answer/10352053) in Search Console.

Here is how to add a website property to your Search Console account. Note that you must be able to[prove that you own the site (or appropriate section of that site](https://support.google.com/webmasters/answer/9008080)) in order to add it to your Search Console account. You can create a property that includes an entire domain (example.com) or a property that is limited to a single branch (example.com/clothing/).

If you are unable to prove ownership, you can ask another property owner to [grant you access to the property](https://support.google.com/webmasters/answer/7687615#manage-users).

You can have up to 1,000 properties in your Search Console account.

## [](https://support.google.com/webmasters/answer/34592?hl=en)Types of website properties

Search Console supports the following website property types:

|  | [URL-prefix property](https://support.google.com/webmasters/answer/10432366) | [Domain property](https://support.google.com/webmasters/answer/10431861) |
| --- | --- | --- |
| Description | Includes only URLs with the specified prefix, including the protocol (http/https). If you want your property to match any protocol or subdomain (http/https/www./m. and so on), then consider creating a Domain property instead. [See more details.](https://support.google.com/webmasters/answer/34592?hl=en#url_prefix_prop_tips) | A domain-level property that Includes all subdomains (m, www, and so on) and multiple protocols (http, https, ftp). If you need to limit your data by URL path segments (example.com/es/, example.com/en/, and so on) or by protocol (http/https), then create a URL-prefix property instead. [See more details.](https://support.google.com/webmasters/answer/34592?hl=en#domain_property) |
| Verification | [Many possible methods](https://support.google.com/webmasters/answer/9008080) | [DNS record verification](https://support.google.com/webmasters/answer/9008080#domain_name_verification) only |
| Examples | Property `http://example.com/` ✔ http://example.com/dresses/1234 🅧 http s://example.com/dresses/1234 - **https does not match** 🅧 http://www**.**example.com/dresses/1234 - **www. does not match** | Property `example.com` ✔ http://example.com/dresses/1234 ✔https://example.com/dresses/1234 ✔http://www.example.com/dresses/1234 ✔http://support.m.example.com/dresses/1234 |

## [](https://support.google.com/webmasters/answer/34592?hl=en)Add a new property

If someone else has granted you permission to a property, just open Search Console and select the property using the [property selector](https://support.google.com/webmasters/answer/10352053). Otherwise, you'll need to add a new property to your Search Console account as described next.

Adding a property does not affect your website on Google Search, it only enables you to track your site's performance on Google. If you don't get it done all in one sitting, or have setup problems, it won't hurt your website.

**To add a new property:**

1.   Open the property selector dropdown in any Search Console page, or [click here](https://search.google.com/search-console/welcome).
2.   Select **+ Add property** on the dropdown.
3.   Choose the type of property to add: ## Google-hosted property (Sites, Blogger, Workspace) 
4.   You will be asked to choose a [verification method](https://support.google.com/webmasters/answer/9008080). After choosing, you will be shown the required verification steps for the chosen method. You can verify immediately or save your settings and resume the process later: 
    *   **To verify immediately,** follow the verification steps described without closing the popup window, then click **Verify** in the popup window. If it will take you some time to perform these steps, you can always save your settings and resume the process later (described next).
    *   **To pause and resume the process later**, click **Verify later** to save your current state, close the popup, and verify your site at your convenience. After you have performed the required verification steps, finish verification by selecting the saved (but unverified) property in the property selector in the navigation bar, and selecting **Verify**.

5.   Data should begin to appear in your property in a few days. Data collection for a property starts as soon anyone adds the property to their Search Console account, even before verification. Data collection continues as long as any user has that property in their account, whether or not it has a verified owner. If your property has no data several days after verification, it is possibly because the site hasn't been seen in Google Search, or that you have specified the wrong URL (for example, you specified http instead of https for your URL-prefix property).

**Support for non-latin characters in property URLs**

Search Console supports [Internationalizing Domain Names in Applications (IDNA)](http://www.faqs.org/rfcs/rfc3490.html) as site URLs. Just type your domain name as usual, and it will appear correctly in Search Console. For example, if you type **http://bücher.example.com/** in the **Add property** box, it will appear correctly.

## [](https://support.google.com/webmasters/answer/34592?hl=en)Re-add a removed property

You can re-add a property that you have removed without verification, as long as the property still has one verified owner.

To re-add the property, simply add the property as described above in steps 1-3, and you should automatically be re-verified.

##