---
title: '"XXX days behind" sync status message is incorrect'
source_url: https://github.com/monero-project/monero/issues/591
author: iamsmooth
assignees: []
labels: []
created_at: '2016-01-02T01:10:24+00:00'
updated_at: '2017-08-08T11:18:14+00:00'
type: issue
status: closed
closed_at: '2017-08-08T11:18:14+00:00'
---

# Original Description
Cosmetic issue reported by 'boolberry' on bitcointalk.org. 

The future change to two-minute blocks caused the displayed number of days for historical one-minute blocks to be incorrect while syncing.


# Discussion History
## ghost | 2016-09-15T15:00:18+00:00
Hi @iamsmooth, this should have been fixed by #1012 - is it still an issue for you or can this be closed?


## fresheneesz | 2017-05-23T08:06:32+00:00
I'm seeing this issue too. The count of maximum blocks seems to be continuously changing up and down. This means I have no idea how behind I am or when its likely to complete.

```
2017-May-23 00:57:07.166407 [P2P9][2.91.165.235:53113 INC]Sync data returned a new top block candidate: 1234709 -> 1275233 [Your node is 40524 blocks (56 days) behind] 

SYNCHRONIZATION started

2017-May-23 00:57:28.693060 [P2P0][45.32.227.208:55036 INC]Synced 1234809/1288639
2017-May-23 00:58:22.921540 [P2P8][45.32.227.208:55036 INC]Synced 1235009/1288639
2017-May-23 00:58:52.889483 [P2P0][2.91.165.235:53192 INC]Sync data returned a new top block candidate: 1235095 -> 1275233 [Your node is 40138 blocks (55 days) behind] 

SYNCHRONIZATION started
2017-May-23 00:59:14.577848 [P2P3][45.32.227.208:55036 INC]Synced 1235209/1288639
2017-May-23 01:00:14.278749 [P2P1][54.77.194.160:60796 INC]Synced 1235409/1288639
2017-May-23 01:00:14.280704 [P2P4][45.32.227.208:55036 INC]Synced 1235409/1288639
2017-May-23 01:00:32.895010 [P2P3][99.43.35.63:50853 INC]Sync data returned a new top block candidate: 1235460 -> 1316280 [Your node is 80820 blocks (112 days) behind] 

SYNCHRONIZATION started

2017-May-23 01:00:41.112836 [P2P6][2.91.165.235:53281 INC]Sync data returned a new top block candidate: 1235522 -> 1275233 [Your node is 39712 blocks (55 days) behind] 

SYNCHRONIZATION started

2017-May-23 01:00:55.985285 [P2P1][45.32.227.208:55036 INC]Synced 1235609/1316280
2017-May-23 01:01:37.922672 [P2P3][45.32.227.208:55036 INC]Synced 1235809/1288639
2017-May-23 01:02:25.486658 [P2P5][45.32.227.208:55036 INC]Synced 1236009/1288639
2017-May-23 01:02:45.772910 [P2P6][46.228.6.34:44763 INC]Sync data returned a new top block candidate: 1236030 -> 1288639 [Your node is 52609 blocks (73 days) behind] 

SYNCHRONIZATION started

2017-May-23 01:03:39.288503 [P2P7][45.32.227.208:55036 INC]Synced 1236209/1285192
2017-May-23 01:04:07.260009 [P2P6][176.15.173.233:35806 INC]Sync data returned a new top block candidate: 1236285 -> 1306701 [Your node is 70416 blocks (97 days) behind] 

SYNCHRONIZATION started

2017-May-23 01:04:18.388194 [P2P2][2.91.165.235:53455 INC]Sync data returned a new top block candidate: 1236345 -> 1275233 [Your node is 38888 blocks (54 days) behind] 

SYNCHRONIZATION started

2017-May-23 01:04:30.075575 [P2P9][45.32.227.208:55036 INC]Synced 1236409/1288639
```

Note that this is the Daemon log from monero-wallet-gui, I assume that output comes straight from the core daemon.

## hyc | 2017-05-23T11:28:06+00:00
Seems like your daemon is old. In v0.10.3.1 the "new top block" message block number never decreases.

Anyway, what you're talking about is not the same as this issue, which was that the number of days didn't match the number of blocks being logged. That has definitely been fixed, and this issue should be closed.

## fresheneesz | 2017-05-23T17:42:41+00:00
@hyc Looks like you're right. The latest version of monero-wallet-gui seems to contain v0.10.1.0 . I swapped out those binaries with v0.10.3.1 and it seems to be working fine so far. Where is the repository for monero-wallet-gui? I'd like to write an issue there

## moneromooo-monero | 2017-08-08T11:06:41+00:00
+resolved

# Action History
- Created by: iamsmooth | 2016-01-02T01:10:24+00:00
- Closed at: 2017-08-08T11:18:14+00:00
