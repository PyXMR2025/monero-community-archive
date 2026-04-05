---
title: light mode or randomx
source_url: https://github.com/xmrig/xmrig/issues/1308
author: axsoftshi
assignees: []
labels:
- question
created_at: '2019-11-21T04:46:48+00:00'
updated_at: '2019-12-04T10:46:18+00:00'
type: issue
status: closed
closed_at: '2019-12-04T10:46:18+00:00'
---

# Original Description
How to make the compiled program use light mode without randomx, enough memory in time and without randomx

# Discussion History
## xmrig | 2019-11-21T08:56:05+00:00
If you like complete disable RandomX support use option cmake option `-DWITH_RANDOMX=OFF` full list of options: https://xmrig.com/docs/miner/cmake-options

Light mode useless for mining, there is no direct option to enable this mode, miner will switch to light mode if fails to allocate dataset.
Thank you.

## 2010phenix | 2019-11-22T21:43:41+00:00
> Light mode useless for mining, there is no direct option to enable this mode, miner will switch to light mode if fails to allocate dataset.

confirm about speed but is some.... one off.., have few server with CPU 24 core and 8GB but 6-7GB used by Oracle base+system, CPU load only with full backup DB(1 hrs), other time CPU load 2-5%, maybe copy code part with **fails allocate dataset**(light mode) and do with cmake option compile miner only with light mode?



## xmrig | 2019-11-22T21:55:07+00:00
https://github.com/xmrig/xmrig/blob/master/src/crypto/rx/RxDataset.cpp#L43 after removing this line `allocate(hugePages);` miner will always use light mode.
Thank you.

## xmrig | 2019-11-29T06:36:24+00:00
In next version it will be available via config or command line https://github.com/xmrig/xmrig/issues/1318#issuecomment-559676080

## 2010phenix | 2019-11-29T23:43:34+00:00
@xmrig, man you are code master!
Thx.

# Action History
- Created by: axsoftshi | 2019-11-21T04:46:48+00:00
- Closed at: 2019-12-04T10:46:18+00:00
