> Source: https://support.google.com/analytics/topic/14710097?hl=en

## Events and key events

Discover more about Google Analytics events including the different types of events, how they are grouped together, and implementation steps.

[](https://support.google.com/analytics/topic/14710097?hl=en)[Next: Automatically collected events](https://support.google.com/analytics/answer/9234069?hl=en&ref_topic=14710097)

An event allows you to measure a specific interaction or occurrence on your website or app. For example, you can use an event to measure when someone loads a page, clicks a link, or completes a purchase, or to measure system behavior, such as when an app crashes or an impression is served.

**Example**: A news website might include events like "article_read" when a visitor finishes an article, "video_play" when they start a video, or "newsletter_signup" when they sign up for email updates. Measuring these events helps the website owner understand which content is most popular and how users engage with the site.

## Types of events

The following types of events are collected automatically:

*   [**Automatically collected events**](https://support.google.com/analytics/answer/9234069) are events that are collected by default when you set up Google Analytics on your website or app.
*   [**Enhanced measurement events**](https://support.google.com/analytics/answer/9216061) are events that are collected when you set up Google Analytics on your website or app and enhanced measurement is enabled.

You must implement the following types of events in order to see them in Analytics:

*   [**Recommended events**](https://support.google.com/analytics/answer/9267735) are events that you implement, but that have predefined names and parameters. These events unlock existing and future reporting capabilities.
*   [**Custom events**](https://support.google.com/analytics/answer/12229021) are events that you define. Make sure you only create custom events when no other events work for your use case. Custom events don't show up in most standard reports so you need to set up custom reports or explorations for meaningful analysis.

## How it works

Let's say someone clicks a link on your tagged website that takes them to an external website. The following illustrates what happens when the user clicks the link:

## See events in realtime

When an event is sent from your website or app, you can use the following to verify that Analytics has collected the event successfully:

## Realtime report

The _Event count by Event name_ card in [the Realtime report](https://support.google.com/analytics/answer/9271392) shows you each triggered event and the number of times each event was triggered in the last 30 minutes by the users on your website or app. You can click an event to see the event parameters that were sent with the event.

## DebugView report

[The DebugView report](https://support.google.com/analytics/answer/7201382) shows you all the events that one user triggered. It's useful when you want to verify that you have set up an event and event parameters correctly. Before you can use the report, you must enable debug mode.

## Understand key events

A key event is an event that measures an action that's particularly important to the success of your business. When someone triggers the event by performing the action, the key event is recorded in Google Analytics and surfaced in your Google Analytics reports.

Any event you collect can become a key event. To measure a key event, create or identify an event that measures the action and then mark the event as a key event. After you mark the event as a key event, you can see how many users perform the action and evaluate marketing performance across all channels that lead users to perform the action.

The following flow shows how to mark an event as a key event. In short, if an event is important to your business's success, you can mark the event as a key event in Analytics.

Event → Key Event

Learn more [About key events](https://support.google.com/analytics/answer/9267568).

## Understand event grouping

Most of the events that your users trigger on your website or app are not sent one at a time. Instead, most events are grouped together (or batched), where each batch has up to 20 events.

**Note**: Event grouping applies to automatically collected events like “session_start” and “page_view”. If you notice these events being dropped, review your account for potential implementation issues.

Events are not batched, however, in some circumstances:

*   Key events are transmitted immediately, although they may be part of a batch 
    *   **Note**: Marking events like “page_view” as key events doesn’t guarantee that they won’t be part of a batch. This approach only ensures that events are transmitted immediately.

*   Containers loaded in debug mode never batch events to facilitate the realtime experience
*   Events that are held by your device are sent when a user leaves a page
*   In browser environments that don't support the `fetch` API, all events are sent immediately

When a user's device goes offline (for example, a user loses internet access while browsing your app), Analytics stores event data on their device and then sends the data once their device is back online. Analytics ignores events that arrive more than 2 calendar days, plus today after the events were triggered.

Google Analytics has a 16 KB size limit on event data each time data is sent. The size limit applies to both individual and grouped events. When the limit is exceeded for grouped events, the batch will still be sent to the server, however, the entire batch won’t be processed.

**Tip**: You can use the Chrome developer tool to confirm the payload size of grouped events before they’re sent to the server.

### Related links

*   [Engagement overview report](https://support.google.com/analytics/answer/13391283)
*   [Reporting: event performance](https://support.google.com/analytics/answer/9353726)

[](https://support.google.com/analytics/topic/14710097?hl=en)[Next: Automatically collected events](https://support.google.com/analytics/answer/9234069?hl=en&ref_topic=14710097)

##