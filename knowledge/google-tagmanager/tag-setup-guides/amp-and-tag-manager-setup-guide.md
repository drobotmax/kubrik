> Source: https://support.google.com/tagmanager/answer/9205783?hl=en

The [Accelerated Mobile Pages Project](https://www.ampproject.org/) (AMP) is an open-source web platform that helps to improve the performance of your web content. AMP includes built-in support for Google Tag Manager. This document describes the recommended way to set up Google Tag Manager on AMP pages.

To install Tag Manager for AMP:

1.   [Create](https://support.google.com/tagmanager/answer/9205783?hl=en#create) an AMP container in Tag Manager.
2.   [Add](https://support.google.com/tagmanager/answer/9205783?hl=en#install) the Tag Manager snippet to your AMP pages.
3.   [Configure](https://support.google.com/tagmanager/answer/9205783?hl=en#configure)tags in your Tag Manager container and publish.

## Create an AMP container

Tag Manager features an AMP container type. Create a new AMP container for your project:

1.   On the **[Accounts](https://tagmanager.google.com/#/home)** screen, click **More Actions** (![Image 1: More](https://lh3.googleusercontent.com/oLoRPrHJd7m46sWijX6zBWnEnfslP62AxJSwt5Nj0bNbpaYHz2pyscExleiofsH2kQ=h36)) for the account you'd like to use. Select **Create Container**.
2.   Name the container. Use a descriptive name, e.g. "_example.com - news - AMP_".
3.   Under **Where to Use Container**, select **AMP**.
4.   Click **Create**.

Your container is now ready. The next step is to install the Tag Manager code on your AMP pages.

Tag Manager will provide information on how to best install the code snippet, and you can refer to the [next section](https://support.google.com/tagmanager/answer/9205783?hl=en#install) for further guidance.

## Add the Tag Manager snippet

After you create your new AMP container, the **Install Google Tag Manager** screen will appear. Tag Manager provides two code snippets. Copy these code snippets so that they appear on your AMP pages.

**Note:**To access the code snippets later, click the container ID number at the top of your workspace overview page, or click **Admin** and then**Install Google Tag Manager**.

The first snippet adds the amp-analytics component to your AMP page. This code is placed at the end of your page's `<head>` section, and should only appear once on the page.

<!-- AMP Analytics --><script async custom-element="amp-analytics" src="https://cdn.ampproject.org/v0/amp-analytics-0.1.js"></script>

**Important:** Only add this code to your page if it does not already exist, and ensure it only appears once per page.

The second snippet configures amp-analytics to use Tag Manager. Place this code immediately after the opening <body> element. Replace _`GTM-CONTAINER\_ID`_ with your Tag Manager's container ID, or copy and paste the entire snippet from the Tag Manager user interface.

<!-- Google Tag Manager -->

<amp-analytics config="https://www.googletagmanager.com/amp.json?id=GTM-CONTAINER_ID" data-credentials="include"></amp-analytics>

## Configure your container and publish

When your pages have the container snippet correctly installed, they will be able to fire tags deployed from Tag Manager. The next step is to create tag configurations and publish the container.

To create a new tag:

1.   Click **Tags**![Image 2: and then](https://lh3.googleusercontent.com/QbWcYKta5vh_4-OgUeFmK-JOB0YgLLoGh69P478nE6mKdfpWQniiBabjF7FVoCVXI0g=h36)**New**.
2.   Click **Tag Configuration** and select the tag type from the list of [supported AMP tags](https://support.google.com/tagmanager/answer/9205783?hl=en#supported_tags).
3.   Configure the tag with information provided by your tag vendor.
4.   Click **Triggering** and add one or more event conditions that will cause the tag to fire.
5.   Name the trigger and click **Save**.

Repeat these steps for any additional tag configurations. When your container configuration is ready, [publish your container](https://support.google.com/tagmanager/answer/6107163) for the changes to take effect.

## Page variables

Tag Manager can capture AMP variables and use them in tag and trigger configurations. For instance, a page that sells shoes might have variables that describe the properties of a particular shoe. These values can be used to create Tag Manager variables:

<amp-analytics config="https://www.googletagmanager.com/amp.json?id=Tag Manager-XXXXXX;Tag Manager.url=SOURCE_URL" data-credentials="include">

<script type="application/json ">

{

"vars" : {

"type": "shoes",

"color": "red"

}

}

</script>

</amp-analytics>

To create a user-defined variable in Tag Manager that captures the color variable from the above code:

1.   Click **Variables**.
2.   Under **User-Defined Variables**, click **New**.
3.   Click **Variable Configuration** and select **AMP Variable**.
4.   In the **Amp Variable Name** field, enter the field name (e.g. "_color_".)
5.   Give the variable a descriptive name (e.g. "_AMP Variable - color_".)
6.   Click **Save**.

*   [Adobe Analytics](http://www.adobe.com/marketing-cloud/web-analytics.html)
*   [AT Internet](http://www.atinternet.com/)
*   [Burt](http://burtcorp.com/)
*   [Chartbeat](https://chartbeat.com/)
*   [Clicky](https://clicky.com/)
*   [comScore](http://www.comscore.com/)
*   [Custom image](https://support.google.com/tagmanager/answer/6107167)
*   [Cxense](https://www.cxense.com/)
*   [Floodlight](https://support.google.com/tagmanager/topic/6334112)
*   [Google Ads](https://support.google.com/tagmanager/topic/6334091)
*   [Google Analytics](https://support.google.com/tagmanager/answer/6107124)
*   [Salesforce DMP (Krux)](https://www.salesforce.com/products/marketing-cloud/data-management/?d=DMP)
*   [LinkedIn](https://business.linkedin.com/marketing-solutions)
*   [LinkPulse](http://www.linkpulse.com/)
*   [Médiamétrie](http://www.mediametrie.com/)
*   [mParticle](https://www.mparticle.com/)
*   [ÖWA](http://www.oewa.at/)
*   [Parse.ly](http://parse.ly/)
*   [Piano](http://piano.io/)
*   [Quantcast](https://www.quantcast.com/)
*   [Segment](https://segment.com/)
*   [SimpleReach](https://www.simplereach.com/)
*   [Snowplow](http://snowplowanalytics.com/)
*   [Webtrekk](https://www.webtrekk.com/)

##