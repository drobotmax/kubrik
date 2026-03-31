> Source: https://support.google.com/analytics/answer/9303323?hl=en

Discover more about the Google Analytics hierarchy and learn about organization, account, and property configurations.

*   [Overview](https://support.google.com/analytics/answer/9303323?hl=en#overview)
*   [Organization](https://support.google.com/analytics/answer/9303323?hl=en#organizations)
*   [Analytics account](https://support.google.com/analytics/answer/9303323?hl=en#accounts)
*   [Analytics property](https://support.google.com/analytics/answer/9303323?hl=en#properties)
*   [Data streams](https://support.google.com/analytics/answer/9303323?hl=en#streams)
*   [Switching between accounts and properties](https://support.google.com/analytics/answer/9303323?hl=en#switching)
*   [Compare Analytics and Firebase hierarchies](https://support.google.com/analytics/answer/9303323?hl=en#compare)

## Google Analytics hierarchy overview

Google Analytics is organized in a hierarchy:

*   Organization (optional) 
    *   Analytics account 
        *   Analytics property

You can assign users to the organization, account, and property levels, and you can give them [permissions](https://support.google.com/analytics/answer/9305587) at each level.

Learn more about managing users at the [organization level](https://support.google.com/marketingplatform/topic/9014057) and at the [account/property level](https://support.google.com/analytics/answer/9305788).

## Organization configuration

Products and users are collected together in organizations. An organization represents a company, and lets you access your company’s product accounts (e.g., Analytics, Tag Manager), and manage cross-product integrations and users' product-specific permissions. You access your organizations at [marketingplatform.google.com/home](https://marketingplatform.google.com/home).

For example, an organization could have the following configuration:

*   Organization 
    *   Analytics account 
        *   Analytics property

    *   Google Tag Manager account

Organizations are optional, though recommended for the benefits they provide. [Learn more](https://support.google.com/marketingplatform/answer/9013752) about organizations.

## Analytics account

The account is the gateway to Analytics, and provides the container for your Analytics properties. You can have one or more Analytics accounts (up to a maximum of 100). Each account can contain up to 2,000 properties.

How you manage the relationship between accounts and properties is up to you. You can use a one-to-one relationship of one account/one property, or you can use a one-to-many relationship of one account/many properties.

[Learn more about how to structure your account](https://support.google.com/analytics/answer/9679158).

When you create an account, you have the option to add it to an existing organization.

Analytics users are identified by Google email addresses. Those addresses could be for Google accounts like Gmail, or they could be for Google Workspace accounts associated with individual businesses.

You sign in to Analytics at [google.com/analytics](https://marketingplatform.google.com/about/analytics/), using your Google email address and password. When you sign in, you have access to all of the accounts and properties that your email address is associated with.

If you have permissions at the account level, then you can see all of the properties in that account. If you have permissions for only a subset of properties, then you can see only those properties and their data streams.

## Analytics property

Properties are the containers for your reports based on the data you collect from your apps and sites. You can create up to 2,000 properties in an account.

### Google Analytics

A Google Analytics property represents an app and/or website. For example, you might have a game app that you sell via Google Play and App Store, and you might have a marketing website for that app. You can create a property that represents just the app or the app and website.

When you use a property to represent an app, it should represent a single logical application, like a single game. That single logical application can be the same game on different platforms (e.g., Android and iOS).

Google Analytics properties use the concept of separate data streams (see below) for the customer touchpoints that send data to the property.

#### 360 properties

If you're an Analytics 360 customer, you can create two additional types of properties:

*   Subproperties: A subproperty gets its data from one other property. The data in a subproperty is typically (but not necessarily) a subset of the data in its [source property](https://support.google.com/analytics/answer/11546303). [Learn more about subproperties](https://support.google.com/analytics/answer/11525732)
*   Roll-up properties: A roll-up property gets its data from multiple other properties. Roll-up properties provide a broad view of your business across products, brands, or regions by combining data from multiple [source properties](https://support.google.com/analytics/answer/11546303) into a single roll-up property. [Learn more about roll-up properties](https://support.google.com/analytics/answer/11526039)

## Data streams (Google Analytics properties)

Each Google Analytics property can have up to 50 data streams (any combination of app and web data streams, including a limit of 30 app data streams).

A data stream is a flow of data from a customer touchpoint (e.g., app, website) to Analytics.

When you create a data stream, Analytics generates a snippet of code that you add to your app or site to collect that data. Data is collected from the time you add the code, and that data forms the basis of your reports.

If you're collecting data for a single logical application on multiple platforms like Android and iOS, then you create a data stream for each platform (e.g., one data stream for your game app on Google Play and another data stream for your game app on App Store).

If you delete a data stream, Analytics preserves the historical data, but there is no further processing of that data, nor can you use that data in report filters.

[Learn more about how to add streams to your Analytics properties](https://support.google.com/analytics/answer/9304153#stream).

## Switching between accounts and properties

Analytics provides and easy way to switch between the different accounts and properties you have access to via a simple menu in the user interface. [Learn more](https://support.google.com/analytics/answer/10253796).

## Compare Analytics and Firebase hierarchies

| Analytics | Firebase |
| --- | --- |
| Account | (no comparable level) |
| Property | Project |
| Data stream | App |