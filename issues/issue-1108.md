---
title: Sync status reporting 100% incorrectly
source_url: https://github.com/monero-project/monero/issues/1108
author: voidzero
assignees: []
labels: []
created_at: '2016-09-20T15:30:15+00:00'
updated_at: '2016-10-04T22:12:27+00:00'
type: issue
status: closed
closed_at: '2016-10-04T22:12:27+00:00'
---

# Original Description
The status command currently reports:

Height: 1139870/1140106 (100.0%) on mainnet, not mining, net hash 31.18 MH/s, v2 (next fork in 2.0 days), up to date, 8+0 connections

This is monero compiled statically, on Gentoo, amd64, commit hash 53e18cafdfb2bf..


# Discussion History
## ghost | 2016-09-20T18:57:43+00:00
1139870/1140106 is 99.98%

What degree of precision would you like?


## voidzero | 2016-09-20T19:16:52+00:00
Floor it - 99.9%. Because 100% will be understood as "fully synchronised."


## ghost | 2016-09-20T20:53:15+00:00
Now that I think about it, maybe 2 significant digits would be nice, and 100% if its within 1 block.

Just thinking out loud.


## moneromooo-monero | 2016-09-24T10:40:35+00:00
https://github.com/monero-project/monero/pull/1124


## luigi1111 | 2016-10-04T22:12:27+00:00
Fixed as above.


# Action History
- Created by: voidzero | 2016-09-20T15:30:15+00:00
- Closed at: 2016-10-04T22:12:27+00:00
