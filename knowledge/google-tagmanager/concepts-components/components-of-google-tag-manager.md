> Source: https://support.google.com/tagmanager/answer/6103657?hl=en

Understand how tags, triggers, variables, and the data layer work together.

Google Tag Manager uses these concepts to handle how tags are configured and fired:

*   **Tag:** A tag is code that send data to a system such as Google Analytics.
*   **Trigger:** A trigger listens for certain events, such as clicks, form submissions, or page loads. When an event is detected that matches the trigger definition, any tags that reference that trigger will fire.
*   **Variable:** A variable is a named placeholder for a value that will change, such as a product name, a price value, or a date.
*   **Data layer:** Tag manager implements a data layer to temporarily hold values in the client so that they can be used by tags, triggers, and variables.

In this article we will explore how these concepts work together.

A [_**tag**_](https://support.google.com/tagmanager/topic/3281056) is a snippet of code that executes on a page or mobile app. Tags can serve a variety of uses, but most of the tags used in tag management systems are designed to send measurement information from your site to a third party. Examples include the [Google Analytics tag](https://support.google.com/tagmanager/answer/6107124) and the [Google Ads conversion tag](https://support.google.com/tagmanager/answer/6105160).

If you don't use a tag management solution, the code for each tag is added directly to the source code. With Tag Manager, you instead control all of your tags from a web user interface.

Tags execute, or _fire_, in response to events. Events could be page loads, button clicks, page scrolls, etc. In Tag Manager, you define [_**triggers**_](https://support.google.com/tagmanager/topic/7679384) to listen for those events and specify when tags should fire.

## Triggers and variables

Tag Manager has many [built-in variables](https://support.google.com/tagmanager/topic/7182737) to choose from, and you may configure additional [custom variables](https://support.google.com/tagmanager/answer/7683362). For example: the predefined variable "_url_" contains the address of the currently loaded page. If you want a tag to fire only on the page _example.com/purchase/receipt.html_, define a trigger with these settings:

*   **Event:** Page View
*   **Trigger Type:** Page View
*   **Fire On:** Some Page Views 
    *   **Fire the tag when these conditions are true:**

_URL contains example.com/purchase/receipt.html_

Configure built-in variables or custom variables to make information available to your application when you need it. Use these variables in trigger conditions or to pass information to tags.

## Variables and the data layer

The [data layer](https://developers.google.com/tag-manager/devguide#datalayer) is used to temporarily hold data. It is a structured format that is understood by Tag Manager to make it easy for you to move that data from your web page or mobile app to tags, triggers, and other variables in Tag Manager.

You don't necessarily need to set up a data layer in order for variables to retrieve information. Tag Manager Variables can also be configured to retrieve values directly from JavaScript variables, first-party cookies, from the DOM. However, the best practice is to have your variables retrieve information directly from a well-organized data layer object. A data layer implementation can minimize the likelihood of data loss from inadvertent code changes, encourage a well organized and accessible data model, and simplify troubleshooting.

**Note:** For web applications, every page must have code that adds the needed information onto the data layer. The data layer does not automatically persist across pages.

## Data layer implementation scenarios

Consider these points help you decide if a data layer implementation is right for your needs:

*   **If your tags only need to fire when pages load** (i.e. they don't need to fire in response to user interactions on the page) and the tags don't need any information beyond URL and referrer, you only need to add the container snippet to each page of your site. A data layer implementation is probably not necessary.
*   **If your tags only need to fire when pages load, but need information beyond URL and referrer** (such as the page type or user ID), you may need to add code that creates a data layer and pushes information to it.
*   **If the data you wish to use isn't available until after the user has interacted with the page**, you will need to add code that [pushes data to the data layer](https://developers.google.com/tag-manager/reference#datalayerpush), and then you will have to configure Tag Manager to leverage the data layer when the desired events occur.

## Related resources

*   [About tags](https://support.google.com/tagmanager/answer/3281060)
*   [How triggers work](https://support.google.com/tagmanager/answer/7679316)
*   [Variables](https://support.google.com/tagmanager/topic/7683268)
*   [Developer Guide](https://developers.google.com/tag-manager/devguide)

##