---
title: Change countdown to start connecting local daemon from 5 sec to 10 sec
source_url: https://github.com/monero-project/monero-gui/issues/1004
author: erciccione
assignees: []
labels: []
created_at: '2017-12-08T14:11:06+00:00'
updated_at: '2017-12-10T21:51:09+00:00'
type: issue
status: closed
closed_at: '2017-12-10T21:51:09+00:00'
---

# Original Description
After reading many posts like [this one on reddit](https://www.reddit.com/r/Monero/comments/7idaet/did_i_do_something_wrong_when_connecting_to/), I think many people don't see in time the popup window who warn "Starting Monero daemon in 5 seconds" after creating the wallet . This cause the GUI to often start syncing a local daemon without the user noticing. This can cause issues to first time or not expert users.

My proposal is to change the countdown from 5 to 10 seconds. This should give time enough to see the popup

# Discussion History
## aekrylov | 2017-12-10T21:25:54+00:00
Why not disable the countdown completely,leaving only a prompt to start a local daemon? IMO that's rather annoying, and changing number of seconds won't do if the user is AFK (otherwise, the popup most likely will be senn immediately)

# Action History
- Created by: erciccione | 2017-12-08T14:11:06+00:00
- Closed at: 2017-12-10T21:51:09+00:00
