---
title: invalid block template from daemon when mining salvium to local node
source_url: https://github.com/xmrig/xmrig/issues/3511
author: sfhdfshdfh
assignees: []
labels: []
created_at: '2024-07-11T16:32:09+00:00'
updated_at: '2024-07-13T07:54:03+00:00'
type: issue
status: closed
closed_at: '2024-07-13T07:43:56+00:00'
---

# Original Description
**Describe the bug**
it throws an error when trying to mine salvium rx/0 with --daemon flag
error is job error "invalid block template received from daemon"
daemon was run by --add-priority-node seed03.salvium.io flag. xmrig dev claimed it would work fine already for this randomx coin. but it doesnt. 

**To Reproduce**
win 10
xmrig.exe -t 24 -a rx/0 --daemon -o 127.0.0.1:19081 -u SaLxxxx

**Expected behavior**


**Required data**
 - XMRig version 6.21.0

# Discussion History
## SChernykh | 2024-07-12T06:26:45+00:00
Salvium is not supported. Use #3508 if you want to mine it.

> xmrig dev claimed it would work fine already for this randomx coin. but it doesnt.

That was claimed for pool mining, not solo mining.

## sfhdfshdfh | 2024-07-13T07:43:56+00:00
pool does seem to accept the shares from original xmrig with -a rx/0 but neither pool nor the miner ever hit any blocks. that pool went down after it failed finding blocks. i think it should be named rx/sal instead. xmrig will get obsolete if it doesnt get flexible enough with adding more cpu algos and coins. your fee system, mines monero for you afterall anyway not the same 5hitcoin your user does.

## SChernykh | 2024-07-13T07:54:02+00:00
Salvium uses exactly the same algorithm, it's rx/0. Pool issues are not xmrig issues - as soon as some pool gets working, xmrig will work when mining to it.

# Action History
- Created by: sfhdfshdfh | 2024-07-11T16:32:09+00:00
- Closed at: 2024-07-13T07:43:56+00:00
