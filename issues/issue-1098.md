---
title: Unknown/unsupported algorithm "(null)" detected - minexmr.com
source_url: https://github.com/xmrig/xmrig/issues/1098
author: derWahnsinn
assignees: []
labels:
- question
created_at: '2019-08-04T10:11:06+00:00'
updated_at: '2020-04-04T19:28:29+00:00'
type: issue
status: closed
closed_at: '2019-08-04T11:31:27+00:00'
---

# Original Description
hi, having the problem that I can't connect to minexmr pool anymore. 

I'm running the current beta version **xmrig-2.99.4-beta-xenial-x64** without any special options and with hugepages activated

> [pool.minexmr.com:4444] Unknown/unsupported algorithm "(null)" detected, reconnect
> [pool.minexmr.com:4444] login error code: 6

the last working version for me is **xmrig-2.16.0-beta**

did I miss something?

thanks in advance

# Discussion History
## xmrig | 2019-08-04T10:44:29+00:00
#1066 This pool not support algorithm negotiation, so now you must specify algo option with value `cn/r`.
Thank you.

## derWahnsinn | 2019-08-04T11:31:27+00:00
thanks very much!

# Action History
- Created by: derWahnsinn | 2019-08-04T10:11:06+00:00
- Closed at: 2019-08-04T11:31:27+00:00
