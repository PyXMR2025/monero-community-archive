---
title: Does v2.12.0 support the new algorithm of March 9?
source_url: https://github.com/xmrig/xmrig/issues/937
author: ttsite
assignees: []
labels:
- question
created_at: '2019-02-18T13:13:09+00:00'
updated_at: '2019-02-22T10:24:50+00:00'
type: issue
status: closed
closed_at: '2019-02-22T10:24:49+00:00'
---

# Original Description
Will v2.12.0 support the new algorithm of March 9, and if so, will the replacement be automatically replaced by the new algorithm? The software does not need to be restarted (CPU mining software). Thank you!!?

# Discussion History
## xmrig | 2019-02-19T00:38:54+00:00
v2.13 will support March hardfork.

Same as before miner will switch algorithm on fly, both for CPU/GPU in 2 cases:

* `variant` option set to `-1` (automatic)
* Pool supports algorithm negotiation, in this case `variant` option doesn't mater.

## ttsite | 2019-02-19T00:52:38+00:00
> v2.13
When will this edition be issued, thank you!!


## xmrig | 2019-02-19T04:30:36+00:00
Exact date not decided yet, but in dev branch support for new algorithm already added.
Thank you.

## minhng99 | 2019-02-20T07:32:22+00:00
any test pool for the new algorithm?

## xmrig | 2019-02-20T08:21:22+00:00
Traditional http://killallasics.moneroworld.com/ already updated.
Thank you.

## minhng99 | 2019-02-20T08:24:33+00:00
it looks like that pool is broken, the " Mining Pool Address:" is empty, do you know what it is?

edit: anyway, it looks like killallasics.moneroworld.com:3333

## xmrig | 2019-02-22T10:24:49+00:00
v2.13.0 released.

# Action History
- Created by: ttsite | 2019-02-18T13:13:09+00:00
- Closed at: 2019-02-22T10:24:49+00:00
