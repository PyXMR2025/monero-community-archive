---
title: Can't create transaction.
source_url: https://github.com/monero-project/monero-gui/issues/91
author: AwfulCrawler
assignees: []
labels: []
created_at: '2016-10-29T21:12:38+00:00'
updated_at: '2016-11-05T08:11:35+00:00'
type: issue
status: closed
closed_at: '2016-11-05T08:11:35+00:00'
---

# Original Description
The following error occurred when trying to send a transaction. (OS = Ubuntu 16.04)

> Can't create transaction: internal error: histogram reports no outputs for 2000000000000, not even ours

Steps leading up to it:

1) Running GUI and daemon on one computer and CLI + daemon on another
2) Sent 2XMR from CLI wallet to GUI wallet
3) XMR was received.
4) After balance was unlocked, try to send 1 XMR to another wallet.
5) Error message as shown above.

Screenshot shown below:

![screenshot from 2016-10-30 09-51-27](https://cloud.githubusercontent.com/assets/18298280/19832766/440c0e0a-9e89-11e6-93a2-a14c45efa779.png)


# Discussion History
## Jaqueeee | 2016-10-30T09:29:29+00:00
Is this on main or testnet?


## AwfulCrawler | 2016-10-30T20:11:42+00:00
It was on mainnet.  Ran both monerod and monero-core without any command line options.

I see the following in the terminal:

> Progress text: Synchronizing blocks 1168282 / 1168252

This seems a bit odd (the left number is greater than the right).  Could this be related to the error, or is this normal behaviour?


## Jaqueeee | 2016-10-30T20:28:44+00:00
about the sync: It's "normal" behavior. The daemon block height is cached for some time in the wallet. So this could happen if wallet caches block height from daemon that isn't fully synced.


## Jaqueeee | 2016-11-01T16:50:57+00:00
EDIT: removed. Commented wrong issue


## fluffypony | 2016-11-01T17:09:56+00:00
@Jaqueeee I'm being dumb, I can't see the config folder in the screenshot...plz help:)


## Jaqueeee | 2016-11-01T17:25:22+00:00
Lol. I'm the dumb one here @fluffypony. Posted this comment on wrong issue. See https://github.com/monero-project/monero-core/pull/96 :)


## Jaqueeee | 2016-11-04T12:53:22+00:00
I have experienced this issue on two scenarios. 
1. When daemon isn't fully synced (fixed by https://github.com/monero-project/monero-core/issues/99)
2. When using 0.10 daemon. Will be fixed when new daemon is released. Until then you need to build own daemon from master branch. 


# Action History
- Created by: AwfulCrawler | 2016-10-29T21:12:38+00:00
- Closed at: 2016-11-05T08:11:35+00:00
