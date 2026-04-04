---
title: 'p2pool mining excessive ram usage never reclaims reboots required '
source_url: https://github.com/monero-project/monero-gui/issues/3935
author: tehoblivious
assignees: []
labels: []
created_at: '2022-05-31T20:30:46+00:00'
updated_at: '2023-02-15T15:51:20+00:00'
type: issue
status: closed
closed_at: '2023-02-15T15:51:20+00:00'
---

# Original Description
So, I've noticed and seem to have confirmed, if I need to ever restart the MONERO GUI WALLET p2pool miner due to changing thread intensity that means restarting the whole miner setup which also seems to mean restarting the monerod daemon in the node section which ultimately combines to wasted RAM usage I can't even find in the task manager to kill off. So there seems to be a memory process problem for sure. I'm going to need to reboot my computer now lol 55 GB/64 GB ram, like, this isn't going to work.

tl;dr; it appears monerod or p2pool process in monero gui wallet never gets closed completely so end up having wasted memory usage on the computer and end up requiring a reboot since these processes don't show up/kill easily enough especially on something like windows

EDIT : PS: it's probably also clear to most users that trying to restart the MONERO GUI WALLET p2pool miner that almost always it never starts up properly again that you need to restart the daemon in the node settings tab again, that'd be the other ease of use thing, like upon start mining button : KILL ALL p2pool/monerod instances (FREE UP RAM) and start monerod afterwards


so yeah mining via the gui wallet seems good for 24/7 rigs
but kinda bad for main multi-tasking workstations considering you may start/stop multiple times a day 
and eventually the RAM seems to get out of hand 

# Discussion History
## selsta | 2022-05-31T22:57:12+00:00
Note p2pool mining integration was marked beta as it was known that the first release was still having issues. The integration isn't trivial so we have to go through bug reports one by one.

@devhyper can you reproduce this?

## devhyper | 2022-06-01T07:12:04+00:00
I wasn't able to reproduce this on my machine with a remote node, which might mean your issue is with the local daemon restarts.
I'll open a PR to only restart the daemon if the zmq parameter is not present.
@tehoblivious Can you try `taskkill /F /T /IM p2pool.exe` and see if the RAM usage drops?

## tehoblivious | 2022-06-01T21:38:57+00:00
 @tehoblivious Can you try `taskkill /F /T /IM p2pool.exe` and see if the RAM usage drops?

TL;DR: I tried, still very high RAM ): reboot still required- swear there might be hidden processes somehow(???) 

know what's strange? I killed off both p2pool.exe and monerod.exe and yet I swear these must be hidden processes because I still see elevated RAM usage and via the task manager there's literally nothing indicating such usage 

I have no idea why it's acting like this

BUT I do know this problem eventually happens when ya start/stop monero gui wallet p2pool mining multiple times a day 
eventually the average RAM usage is way higher than you'd expect 
I can reproduce, just start stopping mining throughout the day as i'd normally use a multi-purpose high end PC, mining and other things, and sometimes mining's gotta "pause" 

Yeah even via a admin command prompt doing those kill commands I'm still seeing much higher ram than normal
**are they like hidden processes?** again back to the lost and restart entire computer solution ): 
RAM usage is like 42 GB/64 without even mining, no games open, no video editing, nothing outta the usual, strange. (should be closer to 24-30'something, but 40 GB is heavy usage, memory leakage somewhere/somehow) 



# Action History
- Created by: tehoblivious | 2022-05-31T20:30:46+00:00
- Closed at: 2023-02-15T15:51:20+00:00
