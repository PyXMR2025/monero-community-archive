---
title: 'MinerGate errors: -  error: "Timeout", code: -42 | read error: "end of file"
  | no active pools, stop mining'
source_url: https://github.com/xmrig/xmrig/issues/874
author: PiotrMP006
assignees: []
labels: []
created_at: '2018-11-12T12:24:37+00:00'
updated_at: '2019-03-17T16:33:42+00:00'
type: issue
status: closed
closed_at: '2019-03-17T16:33:42+00:00'
---

# Original Description
Hi

MinerGate errors:

[2018-11-12 13:09:49] [0;31m [stratum+tcp://xmr.pool.minergate.com:45700] **error: "Timeout", code: -42** [0m
[2018-11-12 13:09:49] [0;31m [stratum+tcp://xmr.pool.minergate.com:45700] **read error: "end of file"** [0m
[2018-11-12 13:09:49] [0;31m **no active pools, stop mining** [0m

# Discussion History
## 2010phenix | 2018-11-12T17:50:13+00:00
what version miner you used?

## xmrig | 2018-11-13T15:22:27+00:00
Disable `keepalive` or change pool.

## PiotrMP006 | 2018-11-14T05:34:04+00:00
Hi

I use version 2.8.3 Win32 with disabled keepalive 

## cignevulmo | 2018-11-18T23:02:27+00:00
Bendede aynı sorun var arada bu hatayı alıyorum !

read error : "end of file" no active pools,stop mining

## DeadManWalkingTO | 2019-03-17T14:55:30+00:00
I think this issue can be closed.
Thank you!

# Action History
- Created by: PiotrMP006 | 2018-11-12T12:24:37+00:00
- Closed at: 2019-03-17T16:33:42+00:00
