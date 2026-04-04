---
title: Lovely Day Dev meeting summary
source_url: https://github.com/monero-project/monero-site/issues/104
author: Gingeropolous
assignees: []
labels: []
created_at: '2016-02-17T11:40:44+00:00'
updated_at: '2016-02-17T16:34:02+00:00'
type: issue
status: closed
closed_at: '2016-02-17T16:34:02+00:00'
---

# Original Description
Lots of stuff done in the past 2 weeks:

v2 block tests
flattened CMake issues (DNSSEC will work again)

the possibilities of inconstent database state and the mempool transactions ""have been clobbered""

amongst other stuff not mentioned, but copying here from moneromoos milestone work:
fixes for the wallet creating txes over max size the daemon will accept
more work on tests (including tests for the MRL-0004 changes)
going through all the V1/V2 stuff to catch what I saw was wrong
fix for txes not expiring from pool due to other nodes coming online regularly
better handling of pending/failed txes in simplewallet
new command/RPC to flush txes from the txpool
preventing two daemons from using the same data dir concurrently
more intelligent handling against duplicate outs
## RingCT

Shen is almost done with reference code, volunteers needed to actually implement. warptangent takes on the db stuff. 

https://github.com/ShenNoether/MiniNero/tree/master/brief

When RingCT gets merged, will be a good time to merge other database formats. 
DB format changes - build a converter that "upgrades" format changes. It's left open, but hyc agrees to tackle it later. 
## Dev Branch

This has become the bastard child of Monero development apparently. Lines 82 - 167 encompass discussion on this topic. The goal is "to merge back to the dev branch" Ultimately the decision is to hack at it for a bit and reevalauate in next meeting. 

> <moneromooo> What I'll do it hack at it to make it work better, really. All that's needed is time without the problem of a release coming too quick.

Godspeed moneromooo. 
## Hardforks

The next fork (RingCT) will be the last time any modifications of the hardfork schedule are permitted. 


# Discussion History
## fluffypony | 2016-02-17T16:34:02+00:00
Added in https://github.com/monero-project/monero-site/commit/5935fc89e8d28cc4fb5aa7a697f1bb6fecf85437 - thank you!


# Action History
- Created by: Gingeropolous | 2016-02-17T11:40:44+00:00
- Closed at: 2016-02-17T16:34:02+00:00
