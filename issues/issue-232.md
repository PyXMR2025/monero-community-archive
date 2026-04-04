---
title: Meta Meeting Solutions
source_url: https://github.com/monero-project/meta/issues/232
author: anonimal
assignees: []
labels: []
created_at: '2018-06-02T17:50:00+00:00'
updated_at: '2023-12-20T19:40:49+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
What started as [this](https://github.com/monero-project/kovri/issues/134) grew into [this](https://github.com/monero-project/meta/issues/13) and has now become the copy/pasted/mutated standard of how we organize meetings. Now that we have multiple groups with multiple meetings, and a whole lot more people, our current solution is becoming cumbersome, error prone, and also clutters the meta issue tracker.

I like the github collaboration aspect, but there must be a better solution than what we have now. Perhaps something with Taiga? Whatever the solution, I hope it includes calendar and calendar/app support so we can create a unified calendar which has the ability to interop with other calendars and can track all meetings at all times.

# Discussion History
## SamsungGalaxyPlayer | 2018-06-03T19:03:19+00:00
I know @rehrar is looking into using the NextCloud calendar tool.

I proposed a similar idea in #206.

## anonimal | 2018-06-04T23:33:50+00:00
Oops, I didn't even see that, thanks @SamsungGalaxyPlayer.

## anonimal | 2018-06-07T22:30:23+00:00
I can't find any good IRC meeting bots that also include calendar functionality.

## SamsungGalaxyPlayer | 2018-06-08T01:58:21+00:00
@anonimal in the absence of a better solution, it may be easier to get a Slack integration, which could then be relayed to IRC and the other platforms.

## rehrar | 2018-06-08T02:27:20+00:00
If what we want does not exist, one of the ideas I had had was to see if someone can make something for us. There are plenty of people who code, but maybe in another language (i.e. not C++), so they don't feel like they can contribute to Monero proper.

These people can be wrangled up and we can see if they can't code something specific to our needs. Something that might include community calendar functionality, a bot that pops in to appropriate IRC channels and records conversations at specified meeting times and subsequently PRs them wherever appropriate, and, of course, open source, self-hosted.

## rehrar | 2018-06-08T02:30:18+00:00
As well, there does currently exist different plugins for CMS's like WordPress (ew, I know) that have community calendar functionality wherein events can be submitted by anyone, and moderated by the owners of the site. This can probably be tweaked to fit our needs (minus the bot) if need be as an alternative to the meta issues. I agree with @anonimal. The current list of Issues is just a plethora of Meetings.

This is a good problem to have as it means Monero is growing, but it's definitely time to look for alternative solutions.

## anonimal | 2018-06-08T06:16:46+00:00
>Slack integration,

Does mattermost have anything similar?

## nahuhh | 2023-12-18T13:42:15+00:00
> 
> Does mattermost have anything similar?

I believe so

## dan-is-not-the-man | 2023-12-20T19:40:48+00:00
Something like this:

https://meetings.monerokon.org

redirects too

https://mattermost.monerokon.org/plugins/focalboard/team/89jtbrysdj86xyxre15e9zba7o/shared/bjr4hgznpupn178h58g4xsd4zio/vcg69qmx4qtgambntadywej5owy?r=k9sryfcathag7x83dhz17afqc1r


Or Monerokon use it this way

https://mattermost.monerokon.org/plugins/focalboard/team/7jxzshir6j895kwgu71mdx5xrc/shared/buntcef156pgp7fy6x5oyn33rny/vchn7j3cnkpnmiyczoqcbyizkcy?r=k7drhyrbfygt844ejqb7h58o6dw

# Action History
- Created by: anonimal | 2018-06-02T17:50:00+00:00
