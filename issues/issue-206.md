---
title: '[Infrastructure] Add hosted open-source calendar solution for meetings and
  events'
source_url: https://github.com/monero-project/meta/issues/206
author: SamsungGalaxyPlayer
assignees: []
labels: []
created_at: '2018-04-10T18:20:41+00:00'
updated_at: '2020-07-24T20:19:09+00:00'
type: issue
status: closed
closed_at: '2020-07-24T20:19:09+00:00'
---

# Original Description
The Monero project hosts a number of excellent tools to help workgroups, including Mattermost and Taiga. I recommend adding an open-source calendar tool to this list. We can use this ticket to deliberate and select the preferred tool if desired.

A calendar is highly needed for planning workgroup meetings and events. Although this meta Github is excellent for documentation purposes, it is relatively unknown by many members of the community. Furthermore, it would be great if we could update calendar event information automatically, and for these updates to be pushed to all the subscribers instantly. People can be informed about upcoming meetings and events without manually keeping track of everything. They would only need to subscribe to the calendar.

I recommend the following:

1. Hosting a web-accessible calendar service.
2. Giving access to different workgroup leaders. If desired, create a different calendar for each workgroup, so that the leaders have permissions to edit only their own calendars. Create a process for requesting a new workgroup calendar.
3. Including a link to the calendar on the getmonero.org website.
4. Including a link to the calendar in various IRC channels descriptions.
5. Including a link to the calendar in various subreddits (r/MoneroCommunity, perhaps r/Monero also?). Include a visual representation if possible showing the next 5 or so events.

After a bit of searching, I found [AgenDAV](https://github.com/agendav/agendav/), which may work for this purpose.

If there is no desire for a hosted open-source calendar service, I will make one with Google Calendar.

# Discussion History
## bitlamas | 2018-04-10T18:28:58+00:00
This is an excellent idea and would definitely make more people participate in the meetings. Whenever considering the tool for the calendar management, please consider one that can export [iCalendar](https://en.wikipedia.org/wiki/ICalendar) (.ics) files, so anyone will be able to subscribe / import the calendar in their own favorite calendar platform (like Thunderbird, Outlook, Google Calendar, etc).

## SamsungGalaxyPlayer | 2018-04-10T18:38:29+00:00
Yes @curumimxara that is an extremely important requirement. Users should be able to subscribe and see the events seamlessly in their own calendars.

## rehrar | 2018-04-10T18:38:50+00:00
The events page on getmonero.org was taken down because it wasn't updated often enough. A calendar solution is indeed a great idea since it doesn't have to wait on the core team to merge and get them up there. It can hopefully be updated on the fly very quickly. I'll do some research and see what I can't get up.

Although we can attach it to events.getmonero.org or something similar, another option is to move away from the Core Team entirely for this one. This means hosting that is not part of the core team's infrastructure, and a purchased VPS box to run it. I'm more than happy to maintain it. If we don't decide to go this route, it may take some time as pigeons and I get this up and going on one of the servers managed by the core team.

## erciccione | 2018-04-11T13:13:40+00:00
This is something very needed, some community members already tried to create a calendar in past, but without maintaining they all became obsolete quite soon. The creation of a workgroup dedicated to this should solve the issue.
I agree only if we go for open source solutions (self hosted or not)

## b-g-goodell | 2018-06-12T15:06:28+00:00
Idea: use github API and amazon AWS to track github issues on the meta repo with the word "meeting" in their title, pushes an RSS feed that we can publish on getmonero.org ... if spam becomes an issue, the word "meeting" will be insufficient to warrant getting pushed into the feed and we might need a whitelist of meeting-issue creators but...

Rather than try to maintain a calendar, this would sort of be a passive watch-and-publish sort of thing.

## SamsungGalaxyPlayer | 2019-05-29T23:26:18+00:00
For a few glorious months, I used the NextCloud instance hosted by Monero Outreach for this. They are ending hosting of this hosted platform. They have stated that they are working on something else, but at the moment we do not have a calendar solution.

# Action History
- Created by: SamsungGalaxyPlayer | 2018-04-10T18:20:41+00:00
- Closed at: 2020-07-24T20:19:09+00:00
