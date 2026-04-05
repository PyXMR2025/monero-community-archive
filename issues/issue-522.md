---
title: --donate-level=N does not work from command line
source_url: https://github.com/xmrig/xmrig/issues/522
author: angelbbs
assignees: []
labels:
- duplicate
created_at: '2018-04-08T20:40:10+00:00'
updated_at: '2018-04-08T20:42:56+00:00'
type: issue
status: closed
closed_at: '2018-04-08T20:42:56+00:00'
---

# Original Description
After version 2.5.0 --donate-level=N does not work from command line. Always set to 5%.
i.e.
xmrig --url=stratum+tcp://cryptonightv7.eu.nicehash.com:3363 --user=user.worker --pass=x --nicehash  --api-port=4002 --donate-level=1

* VERSIONS:     XMRig/2.6.0-beta1 libuv/1.19.2 MSVC/2017
* HUGE PAGES:   available, enabled
* CPU:          Intel(R) Core(TM) i7-4770S CPU @ 3.10GHz (1) x64 AES-NI
* CPU L2/L3:    1.0 MB/8.0 MB
* THREADS:      4, cryptonight, av=1, donate=5%
* POOL #1:      cryptonightv7.eu.nicehash.com:3363
* API BIND:     [::]:4002
* COMMANDS:     hashrate, pause, resume
2018-04-08 23:33:52] use pool cryptonightv7.eu.nicehash.com:3363 159.8.13.236
2018-04-08 23:33:52] new job from cryptonightv7.eu.nicehash.com:3363 diff 10000

# Discussion History
## xmrig | 2018-04-08T20:42:56+00:00
Only version 2.6.0-beta1 affected and it already fixed #494
Thank you.

# Action History
- Created by: angelbbs | 2018-04-08T20:40:10+00:00
- Closed at: 2018-04-08T20:42:56+00:00
