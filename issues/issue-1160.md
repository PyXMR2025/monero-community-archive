---
title: How does V3.1.1 operate with commands?
source_url: https://github.com/xmrig/xmrig/issues/1160
author: ttsite
assignees: []
labels:
- question
created_at: '2019-09-04T00:17:21+00:00'
updated_at: '2019-12-22T19:23:13+00:00'
type: issue
status: closed
closed_at: '2019-12-22T19:23:13+00:00'
---

# Original Description
What is the command line format of v3.1.1?
xmrig.exe -a cryptonight -o stratum+tcp://127.0.0.1:7777 -u Wallet address -p x
Why can't you use this format in the past? Who knows where to change it? Thank you!

# Discussion History
## xmrig | 2019-09-04T00:48:54+00:00
This format should work well, if on other end xmrig-proxy or pool with algorithm negotiation support you don't need specify `-a` at all, it will ignored anyway, otherwise you must specify exact algorithm https://github.com/xmrig/xmrig/blob/master/doc/ALGORITHMS.md#algorithm-names
Thank you.

## ttsite | 2019-09-04T01:16:07+00:00
[2019-09-04 09:15:36.217] [stratum+tcp://pool.minexmr.com:7777] Incompatible/dis
abled algorithm "cn/0" detected, reconnect
[2019-09-04 09:15:36.220] [stratum+tcp://pool.minexmr.com:7777] login error code
: 6
[2019-09-04 09:15:42.130] [stratum+tcp://pool.minexmr.com:7777] Incompatible/dis
abled algorithm "cn/0" detected, reconnect
[2019-09-04 09:15:42.133] [stratum+tcp://pool.minexmr.com:7777] login error code
: 6


# Action History
- Created by: ttsite | 2019-09-04T00:17:21+00:00
- Closed at: 2019-12-22T19:23:13+00:00
