---
title: Deprecate the Monero Mattermost
source_url: https://github.com/monero-project/meta/issues/534
author: SamsungGalaxyPlayer
assignees: []
labels: []
created_at: '2020-12-28T15:10:41+00:00'
updated_at: '2021-02-02T20:56:55+00:00'
type: issue
status: closed
closed_at: '2021-02-02T20:56:54+00:00'
---

# Original Description
Mattermost has not lived up to the user experience expectations people had for it.

Issues contributing to its disuse:

* IRC crowd didn't use it, so DMs aren't compatible
* Matrix/Element is a more commonly recommended alternative
* Relays were largely inconsistent, with occasional, long outages
* Everything is built around IRC with Mattermost acting as a relay only
* Mattermost has limited use in other orgs, so we weren't meeting people where they were (like Slack/Discord/Telegram)

Given the limited features of Mattermost and the user experience drawbacks of using it, I recommend that we stop recommending it and focus on building other platforms.

To-do:

1. Determine whether to kill or keep Mattermost (possibly email users informing them of this discussion); then if it will be removed:
2. Email signed-up users informing them
3. Add Mattermost warning banners informing them (if possible)
4. Remove Mattermost from all portions of the website
5. Delete the Mattermost after ~3 months of the announcement

We should encourage users to use Freenode, Matrix/Element, or Discord.

# Discussion History
## erciccione | 2020-12-28T17:57:06+00:00
I think best would be to replace mattermost with a matrix instance.

## rehrar | 2020-12-28T18:33:26+00:00
I support this. The choice of Mattermost was made two or three years ago when, at the time, Matrix was very buggy and inconsistent. It has, since then, grown tremendously, and is an awesome platform. Conversely, Mattermost has largely stagnated, or rather, developed features that pertain largely to enterprises rather than FOSS groups.

A few outstanding security issues still haven't been fixed, and so I think it's best that it be deprecated. I will look into this further.

## scottAnselmo | 2020-12-28T19:43:01+00:00
Thanks rehrar. Notice is now out in the 'Town Square' of Monero's Mattermost as well for this conversation to make sure any MM users chime in.

## Nurmagoz | 2020-12-31T02:35:34+00:00
Hi There, 

In whonix we as well expanded our communications channels, we had only IRC at the beginning but later we expanded to matrix and telegram. 

The nice thing you can have is to link all of them together instead of deprecating if there is controversy or to avoid it, In the case here mattermost can be bridged to matrix , and materix can be bridged to telegram or IRC as well. 

as bridges from mattermost <-> Matrix there are 2 bridges: 

https://github.com/dalcde/matrix-appservice-mattermost

https://github.com/42wim/matterbridge 

## erciccione | 2020-12-31T09:17:50+00:00
@TNTBOMBOM I wouldn't keep mattermost alive when very few people use it. Maintaining the instance and the bridge is an unnecessary effort IMO. Better directly migrate to matrix.

## SamsungGalaxyPlayer | 2021-02-02T20:56:54+00:00
The Mattermost will be deprecated. Closing.

# Action History
- Created by: SamsungGalaxyPlayer | 2020-12-28T15:10:41+00:00
- Closed at: 2021-02-02T20:56:54+00:00
