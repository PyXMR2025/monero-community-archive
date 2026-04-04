---
title: daemon.cpp line 144 uncaught exception
source_url: https://github.com/monero-project/monero/issues/2040
author: fresheneesz
assignees: []
labels: []
created_at: '2017-05-23T00:37:46+00:00'
updated_at: '2017-05-24T07:54:58+00:00'
type: issue
status: closed
closed_at: '2017-05-24T07:54:58+00:00'
---

# Original Description
I noticed my gui wallet got stuck on block 1288639, so I tried shutting it down and starting up the daemon from the command line. I got this:

```
2017-May-22 17:27:08.390923 ERROR C:/msys64/DISTRIBUTION-BUILD/src/cryptonote_core/checkpoints.cpp:1
06 CHECKPOINT FAILED FOR HEIGHT 1288616. EXPECTED HASH: <875ac1bc7aa6c5eedc5410abb9c694034f9e7f79dce
4c60698baf37009cb6365>, FETCHED HASH: <1e6b1019968d4a33b281ab70d83947bc051ac952f26dd2693c427b04d8215
1fe>
2017-May-22 17:27:08.391423 ERROR C:/msys64/DISTRIBUTION-BUILD/src/cryptonote_core/blockchain.cpp:34
02 WARNING: local blockchain failed to pass a MoneroPulse checkpoint, and you could be on a fork. Yo
u should either sync up from scratch, OR download a fresh blockchain bootstrap, OR enable checkpoint
 enforcing with the --enforce-dns-checkpointing command-line option
```

So I started it with that recommended flag and got this:

```
2017-May-22 17:27:46.733410 ERROR C:/msys64/DISTRIBUTION-BUILD/src/cryptonote_core/checkpoints.cpp:1
06 CHECKPOINT FAILED FOR HEIGHT 1288616. EXPECTED HASH: <875ac1bc7aa6c5eedc5410abb9c694034f9e7f79dce
4c60698baf37009cb6365>, FETCHED HASH: <1e6b1019968d4a33b281ab70d83947bc051ac952f26dd2693c427b04d8215
1fe>
2017-May-22 17:27:46.734412 ERROR C:/msys64/DISTRIBUTION-BUILD/src/cryptonote_core/blockchain.cpp:33
96 Local blockchain failed to pass a checkpoint, rolling back!
2017-May-22 17:27:51.084107 WARNING: batch transaction mode already enabled, but asked to enable bat
ch mode
2017-May-22 17:27:51.085085 batch transaction already in progress
2017-May-22 17:27:51.114414 ERROR C:/msys64/DISTRIBUTION-BUILD/src/daemon/daemon.cpp:144 Uncaught exception! batch transaction already in progress
```

This kinda sucks. I don't want to have to redownload the entire blockchain. Also by the way, where is the gui wallet's repository? Is it open source? I'd love to be able to create issues for it when they come up.

# Discussion History
## nfd9001 | 2017-05-24T06:52:46+00:00
Are you running v0.10.3.1-release? Your wallet may be out of date; there was a hard fork around the time that block went live. Try getting the new version and let the daemon sync your chain from there.

## fresheneesz | 2017-05-24T07:54:58+00:00
My wallet was out of date. I tried resyncing so not sure if the update would have rolled back correctly - I updated and re DLed the blockchain. Works now!

# Action History
- Created by: fresheneesz | 2017-05-23T00:37:46+00:00
- Closed at: 2017-05-24T07:54:58+00:00
