---
title: Daemon failed to start - Linux Mint
source_url: https://github.com/monero-project/monero-gui/issues/3854
author: harrwester
assignees: []
labels: []
created_at: '2022-03-09T14:37:52+00:00'
updated_at: '2022-03-09T16:46:54+00:00'
type: issue
status: closed
closed_at: '2022-03-09T16:46:54+00:00'
---

# Original Description
I ran a local node (advanced mode) monero wallet (gui 0.17.3.1-release qt 5.15.2) on linux mint 20.3 cinnamon without issues for several weeks. Today, it suddenly decided not to connect to daemon and showed me "Daemon failed to start" after 120s of trying. I'm very new to crypto stuff in general and have no idea where to begin with this issue, let alone how to fix this. Any suggestions for the rookie?

# Discussion History
## selsta | 2022-03-09T14:39:03+00:00
Is the blockchain stored on an external hard drive?

## harrwester | 2022-03-09T14:45:02+00:00
Well, it is on a 1TB EXTERNAL HD since I downloaded the blockchain, but waiting for SSD already. 

## selsta | 2022-03-09T16:27:34+00:00
It sounds like your blockchain is corrupted, that can happen when you unplug the external hard drive during sync. You will have to delete the blockchain and resync.

Maybe it's best if you wait for the SSD and use a remote node in the meantime.

## harrwester | 2022-03-09T16:42:41+00:00
Yes, probably. I'll wait for SSD and will give a feedback afterwards. Thanks!

## selsta | 2022-03-09T16:46:54+00:00
So basically, once you delete the corrupted database the daemon should start again. I'm closing this, if you continue to have issues in the future please comment and I can reopen.

# Action History
- Created by: harrwester | 2022-03-09T14:37:52+00:00
- Closed at: 2022-03-09T16:46:54+00:00
