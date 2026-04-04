---
title: p2pool mining excessive ram usage never reclaims reboots required
source_url: https://github.com/monero-project/monero/issues/8342
author: tehoblivious
assignees: []
labels: []
created_at: '2022-05-19T05:44:02+00:00'
updated_at: '2022-05-31T20:29:24+00:00'
type: issue
status: closed
closed_at: '2022-05-31T20:29:02+00:00'
---

# Original Description
So, I've noticed and seem to have confirmed, if I need to ever restart the MONERO GUI WALLET p2pool miner due to changing thread intensity that means restarting the whole miner setup which also seems to mean restarting the monerod daemon in the node section which ultimately combines to wasted RAM usage I can't even find in the task manager to kill off. So there seems to be a memory process problem for sure. I'm going to need to reboot my computer now lol 55 GB/64 GB ram, like, this isn't going to work.

tl;dr; it appears monerod or p2pool process in monero gui wallet never gets closed completely so end up having wasted memory usage on the computer and end up requiring a reboot since these processes don't show up/kill easily enough especially on something like windows 


EDIT : PS: it's probably also clear to most users that trying to restart the MONERO GUI WALLET p2pool miner that almost always it never starts up properly again that you need to restart the daemon in the node settings tab again, that'd be the other ease of use thing, like upon start mining button : KILL ALL p2pool/monerod instances (FREE UP RAM) and start monerod afterwards 

# Discussion History
## ghost | 2022-05-31T20:08:48+00:00
You might want to close this and repost it in the monero-gui repo https://github.com/monero-project/monero-gui

## tehoblivious | 2022-05-31T20:28:58+00:00
> You might want to close this and repost it in the monero-gui repo https://github.com/monero-project/monero-gui


ah true thanks 

# Action History
- Created by: tehoblivious | 2022-05-19T05:44:02+00:00
- Closed at: 2022-05-31T20:29:02+00:00
