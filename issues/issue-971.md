---
title: Can't get Monero GUI wallet to start synchronizing...
source_url: https://github.com/monero-project/monero-gui/issues/971
author: sabiam3
assignees: []
labels:
- resolved
created_at: '2017-11-24T08:23:23+00:00'
updated_at: '2018-10-13T21:09:20+00:00'
type: issue
status: closed
closed_at: '2018-10-13T21:09:20+00:00'
---

# Original Description
Hi all,

I'm new to Monero, and generally not all that computer-savvy, so I'm at a total loss as to how to solve this issue with getting the GUI wallet to begin synchronizing. I'm working on Mac OS Sierra, and this is version 0.11.1.0 of the wallet.

The wallet's network status says that it is synchronizing, but the status bar is stuck on "establishing connection". The Daemon log reads out a series of messages like this, which indicates that the blockchain height isn't being identified:

Height: 1/1 (100.0%) on mainnet, not mining, net hash 0 H/s, v1, up to date, 0(out)+0(in) connections

I've tried running with monerod and changing the log level as others have suggested to remedy similar problems. I can't even begin to make heads or tails of all of the different errors and warnings that are part of the GUI log, all of which seem to have different sources based on the research I've been able to do myself. Link to the GUI log here: https://paste.fedoraproject.org/paste/IG97qkiCiFZp0UH3r3-7RQ

Thanks for the help.

# Discussion History
## dEBRUYNE-1 | 2017-11-24T15:24:21+00:00
Are you using an university network or your work network to sync?

## sabiam3 | 2017-11-24T17:59:18+00:00
No, but I haven't considered any network solutions to the problem. I couldn't rule that out.

## dEBRUYNE-1 | 2017-11-25T15:25:56+00:00
Can you try the following steps:

1. Reboot to ensure no Monero related processes are running anymore. 

2. Delete `~/.bitmonero`.

3. Start `monerod` from the terminal as follows -> `./monerod --log-level 1`

4. Paste the content of `~/.bitmonero/bitmonero.log` to https://paste.fedoraproject.org 

Let me know if you need any assistance. 

----------------------

>No, but I haven't considered any network solutions to the problem. I couldn't rule that out.

Monero uses P2P, so if your network is blocking these kind of connections, `monerod` won't be able to sync. 

## sanderfoobar | 2018-10-13T21:04:47+00:00
Inactive issue - am closing. Re-open if problems persist.

+resolved

# Action History
- Created by: sabiam3 | 2017-11-24T08:23:23+00:00
- Closed at: 2018-10-13T21:09:20+00:00
