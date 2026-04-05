---
title: difference between versions?
source_url: https://github.com/xmrig/xmrig/issues/1740
author: snipeTR
assignees: []
labels:
- question
created_at: '2020-06-23T08:22:46+00:00'
updated_at: '2020-08-19T01:11:15+00:00'
type: issue
status: closed
closed_at: '2020-08-19T01:11:15+00:00'
---

# Original Description
Will there be a revolutionary difference between version 6.2.X and version 5.11.X? According to what do you name the version? what will be the biggest difference.

# Discussion History
## xmrig | 2020-06-23T09:41:13+00:00
v6 includes GPU only KawPow algorithm, it is completely different from other algorithms including network protocol, so it major change, but config format is compatible.

* v6 can use v5 config.
* v5 can use v6 config but kawpow profiles will be silently ignored and not saved.

https://github.com/xmrig/xmrig/pull/1694#issuecomment-638310915


# Action History
- Created by: snipeTR | 2020-06-23T08:22:46+00:00
- Closed at: 2020-08-19T01:11:15+00:00
