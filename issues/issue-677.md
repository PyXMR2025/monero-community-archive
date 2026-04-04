---
title: Wrong date in transaction history
source_url: https://github.com/monero-project/monero-gui/issues/677
author: MaxXor
assignees: []
labels: []
created_at: '2017-04-14T09:16:45+00:00'
updated_at: '2017-04-17T15:12:17+00:00'
type: issue
status: closed
closed_at: '2017-04-17T15:12:17+00:00'
---

# Original Description
There seems to be that all dates in the transaction history before 2016-09-21 (hardfork v3) are wrong. My other transactions after that date are shown correctly.

![transaction_history](https://cloud.githubusercontent.com/assets/7271470/25039497/1dfc799a-2104-11e7-87c3-974185b4496a.png)

# Discussion History
## jonathancross | 2017-04-16T12:44:46+00:00
Interesting that they are all the exact same date, yet very different block heights.

Can you please add details about your platform, Monero GUI version number, is this a binary release or built from source, etc.

Note: I am not seeing this behavior in the latest binary release v0.10.3.1 (GUI Beta 2) for Mac OSX.

## MaxXor | 2017-04-16T13:04:43+00:00
Yes, indeed very strange. I'm using the binary release v0.10.3.1 (GUI Beta 2) on Windows 7 64bit.

## medusadigital | 2017-04-17T05:43:44+00:00
i have seen this bug, but it was months ago before beta 1 release and never happened again.

is this wallet cache completely created with GUI beta 2 ? 

 

## MaxXor | 2017-04-17T08:18:24+00:00
The wallet was created with monero-cli 0.9 if I remember correctly and I've never used the GUI until now. Could I possibly fix it when I delete the cache and do a full re-scan of the wallet?

## medusadigital | 2017-04-17T14:56:22+00:00
ah, so its such an old cache? yes please, regenerate the cache from scratch.

you can either:

- delete cache and rebuild the cache
- restore wallet from seed and give a new name

## MaxXor | 2017-04-17T15:12:17+00:00
Restored the wallet from seed and did a full re-scan. Now it shows the correct dates for all my transactions, thanks @medusadigital.

# Action History
- Created by: MaxXor | 2017-04-14T09:16:45+00:00
- Closed at: 2017-04-17T15:12:17+00:00
