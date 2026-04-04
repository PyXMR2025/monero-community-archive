---
title: Confusing daemon messages at startup, particularly first sync
source_url: https://github.com/monero-project/monero-gui/issues/645
author: BoscoMurray
assignees: []
labels: []
created_at: '2017-03-30T15:03:52+00:00'
updated_at: '2017-04-18T18:58:42+00:00'
type: issue
status: closed
closed_at: '2017-04-18T18:58:42+00:00'
---

# Original Description
I believe this may be the same on all OS, but I'm running Ubuntu 16.04.

When the wallet starts and I open an old wallet file, I see a prompt that the daemon will start automatically. That's fine, but in the background is another window which states "Wallet is not connected to daemon (Start daemon)". This is a little counterintuitive, especially as this background message does not dissappear after the deamon has started. It does finally, after the sync is complete.

When that initial prompt about the deamon being started automatically dissappears, the next window which opens states "Waiting for daemon to start...", and stays like that for a long time, despite the daemon running in the background.

Even being technical, these messages give the impression that something might not be working correctly. Looking closer, this is just how it works. For the non-technical, it's a major turn-off. It would be nice to work on cleaning up how the wallet handles communicating the daemons status with the end user.

# Discussion History
## medusadigital | 2017-04-18T10:06:24+00:00
how does GUI beta 2 work for you ? 

this was with beta 1 i assume ? 

## BoscoMurray | 2017-04-18T10:13:45+00:00
This was beta 2. Beta 1 was similar - I think it stated that it was waiting for the deamon to start while the deamon had actually started in the background. These new messages in beta 2 appear to be trying to improve the situation by communicating more to the user, but from my perspective it seems to have confused it further. I'll run through a fresh install and sync again today, to see if it does the same again.

## BoscoMurray | 2017-04-18T18:58:42+00:00
I've not been able to replicate the issue. Perhaps the VM I was using previously did not have enough ram. This time I gave the VM 2 CPU and 8GM memory, and the GUI messages are reflecting what is actually happening . I'll just close the issue.

# Action History
- Created by: BoscoMurray | 2017-03-30T15:03:52+00:00
- Closed at: 2017-04-18T18:58:42+00:00
