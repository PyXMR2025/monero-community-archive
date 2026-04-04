---
title: Transfer tab background color
source_url: https://github.com/monero-project/monero-gui/issues/165
author: peronero
assignees: []
labels: []
created_at: '2016-11-15T00:07:55+00:00'
updated_at: '2017-06-30T17:28:26+00:00'
type: issue
status: closed
closed_at: '2017-06-30T17:28:26+00:00'
---

# Original Description
The grey background color of the Transfer tab/page is visibly darker than the grey background in any other tab - the lighter version seems to be correct and is more pleasant to the eye.

Using Tumbleweed with GNOME.

# Discussion History
## M5M400 | 2016-11-15T12:06:40+00:00
Can't verify that on current master and never noticed that before. Can you make screenshots and post the commit you're on? Might speed up things.


## moneromooo-monero | 2016-11-15T14:46:53+00:00
This happens when you can't transfer (eg, daemon disconnected, etc)


## taushet | 2016-11-21T17:33:03+00:00
@moneromooo-monero is that clear enough to the user though?

## peronero | 2016-11-26T04:14:22+00:00
This isn't very clear to the user as @taushet points out - a shade of red would be more indicative of something 'not being right', but a different shade of grey just takes away from a consistent user experience and might even further obscure that there's something wrong since it diminishes the contrast with the greyed out fields.

A user in this case - where he/she is blocked from doing something by a dependency on another functionality - is ideally expecting text fields and buttons to be inaccessible and their inaccessibility to be visually communicated (greyed out fields, buttons of a lighter shade, unclickable, etc.), along with an explanation of what is wrong and perhaps even a visual indicator where he can fix this and/or monitor progress (blinking sync status perhaps). 



## Jaqueeee | 2016-11-26T14:53:49+00:00
This change is implemented in the Daemon integration branch i'm working on.
https://github.com/monero-project/monero-core/commit/a78b8f5e3a54a71fa06a1490af541bce5aec861c

## peronero | 2016-12-15T18:37:29+00:00
Doesn't look fixed on a fresh build from master - background color on only this tab is still darker than on any other tabs.

Update: Not addressed as of Beta 2.

# Action History
- Created by: peronero | 2016-11-15T00:07:55+00:00
- Closed at: 2017-06-30T17:28:26+00:00
