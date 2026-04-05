---
title: 'NiceHash rejected '
source_url: https://github.com/xmrig/xmrig/issues/549
author: welj
assignees: []
labels: []
created_at: '2018-04-12T20:19:20+00:00'
updated_at: '2018-11-05T13:29:40+00:00'
type: issue
status: closed
closed_at: '2018-11-05T13:29:40+00:00'
---

# Original Description
Hi, sometime have errors in NiceHash:
rejected (139/9) diff 100001 "Invalid nonce; is miner not compatible with NiceHash?" (69 ms)

xmrig 2.5.2


# Discussion History
## xmrig | 2018-04-12T22:09:36+00:00
Please provide all possible details. What exactly url used on nicehash, information about miner, etc.
Thank you.

## welj | 2018-04-13T06:56:45+00:00
starting with>> xmrig -o 159.8.13.236:3363 -u MY_WALLET.MY_WORKER -p x -t 12 --av=2 --variant 1
linux ubuntu 16.04

## adem4ik | 2018-04-15T12:28:05+00:00
@welj I think you should use "cryptonightv7.LOCATION.nicehash.com:3363" instead of IP.

# Action History
- Created by: welj | 2018-04-12T20:19:20+00:00
- Closed at: 2018-11-05T13:29:40+00:00
