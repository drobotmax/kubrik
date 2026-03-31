> Source: https://support.google.com/tagmanager/topic/9002003?hl=en

## Get started with Tag Manager

Make sure your tag configurations function as expected.

[](https://support.google.com/tagmanager/answer/14842769?hl=en&ref_topic=15191151)[Next: Publishing, versions, and approvals](https://support.google.com/tagmanager/answer/6107163?hl=en&ref_topic=15191151)

For subtitles in your language, turn on YouTube captions. Select the **Settings** icon ![Image 1: Image of YouTube settings icon](https://storage.googleapis.com/support-kms-prod/UrHzzlx74G5ig5vYXo9Nk43r7NM5fj72Tbu1) at the bottom of the video player, then select **Subtitles/CC** and choose your language.

* * *

Google Tag Manager’s preview and debug mode allows you to browse a site on which your [container code](https://support.google.com/tagmanager/answer/14842164) is implemented as if the current container draft was deployed, so that you can test a container configuration before it is published. Your previewed site is connected to [Tag Assistant](https://support.google.com/tagassistant/answer/10039345) so that you can inspect which tags fired and in which order.

## Enable preview and debug mode

To enable preview and debug mode for the current workspace:

1.   Go to [https://tagmanager.google.com](https://tagmanager.google.com/).
2.   Sign in to your Google Account. Learn how to [create a new Google Account](https://support.google.com/accounts/answer/27441).
3.   Open the Tag Manager container you want to edit.
4.   In the **Workspace** tab, click **Preview** (top right) to launch Google Tag Assistant in a new tab.
5.   Enter your site's URL.
6.   Some sites or pages might be broken by an additional debug parameter added to the URL. If so, you can uncheck the box **Include debug signal in the URL**.
7.   Click **Connect**. Your site opens in a new window and displays as **Connected** in the bottom right. 
8.   Click back on the Tag Assistant tab and click **Continue**to access the debug interface. 

To preview an older version of a container:

1.   In the top navigation of your workspace, click **Versions**.
2.   Find the version you would like to work with, click **More Actions**![Image 2: More](https://lh3.googleusercontent.com/oLoRPrHJd7m46sWijX6zBWnEnfslP62AxJSwt5Nj0bNbpaYHz2pyscExleiofsH2kQ=h36)and select **Preview**.

## Use preview and debug mode

Once preview and debug mode is enabled, a new window will launch for the page you entered. The debug interface shows detailed information about your tags, including how tags fired and what data is being processed. The debug interface will only appear on the same browser that was used to enable preview mode, or for [shared users](https://support.google.com/tagmanager/topic/9002003?hl=en#share), and is not visible to your regular website visitors.

Use the information in the debug interface to find out if tags and triggers fire properly and what data they pass to their respective services. As you click through your previewed website, the debug interface will update information about how your tags are fired. You can use this information to check if a tag fired successfully, and what triggered (or did not trigger) its firing status.

The debug interface is not available for the following container types:

*   Mobile app containers (To learn more about how to preview and debug mobile app containers, read the[iOS](https://developer.google.com/tag-manager/ios/v5/#preview-debug-pubish-container) and[Android](https://developer.google.com/tag-manager/android/v5/#preview-debug-pubish-container) developer documentation.)
*   AMP containers (It is still possible to preview your site.)

When preview and debug mode is enabled, the previewed container configuration and Tag Assistant debug interface are only visible from the same browser from where you activated preview and debug mode. You can share this preview with others with a custom-generated URL.

To share a preview of your workspace configuration with a colleague:

![Image 3: Screenshot of the Share and Preview mode container.](https://storage.googleapis.com/support-kms-prod/zup77ourQcLJ5KSnRZyuKRL85HaCwJJMoUCL)

1.   In Tag Assistant, click **More Actions**![Image 4: More](https://lh3.googleusercontent.com/oLoRPrHJd7m46sWijX6zBWnEnfslP62AxJSwt5Nj0bNbpaYHz2pyscExleiofsH2kQ=h36), then select **Share**.
2.   In the **Share debug session** dialog, enter your target website domain and the tags to debug.
3.   Copy the resulting preview URL from the indicated box.
4.   Paste the copied preview URL into an electronic message and send it to a colleague. The preview URL lets the user connect to your site in preview mode and to view the Tag Assistant debug interface.

You can also share the current or older versions of a container from your workspace:

1.   In the top navigation of your workspace, click **Versions**.
2.   Find the version you would like to share, click **More Actions**![Image 5: More](https://lh3.googleusercontent.com/oLoRPrHJd7m46sWijX6zBWnEnfslP62AxJSwt5Nj0bNbpaYHz2pyscExleiofsH2kQ=h36) and select **Share Preview**.
3.   In the Share Preview dialog, enter your target website domain (e.g. https://example.com/).
4.   Copy the resulting preview URL from the indicated box.
5.   Paste the copied preview URL into an electronic message and send it to a colleague. The preview URL lets the user connect to your site in preview mode and to view the Tag Assistant debug interface.

## Exit preview and debug mode

To exit preview mode and stop debugging:

1.   Click the X in the upper left corner of the Tag Assistant debug interface.
2.   Click **Stop debugging** on the Tag Assistant activation page.

[](https://support.google.com/tagmanager/answer/14842769?hl=en&ref_topic=15191151)[Next: Publishing, versions, and approvals](https://support.google.com/tagmanager/answer/6107163?hl=en&ref_topic=15191151)

##