---
title: Dynamic pools reload
source_url: https://github.com/xmrig/xmrig/issues/939
author: xmrig
assignees:
- xmrig
labels:
- enhancement
- META
created_at: '2019-02-21T09:43:13+00:00'
updated_at: '2019-08-02T12:02:31+00:00'
type: issue
status: closed
closed_at: '2019-08-02T12:02:31+00:00'
---

# Original Description
In version 2.13 added support for dynamic pools reload (without miner restart), similar feature was already available in xmrig-proxy.

#### 2 ways to achieve this feature:
* Set option `""watch": true"` in your config, edit config and save it, miner will reload configuration and immediately apply new pool list.
* Use HTTP API with endpoint `PUT /1/config`.

For each pool added new option `enabled` with boolean value to allow disable pool without deleting from config, this feature currently available for all miners except proxy.

# Discussion History
# Action History
- Created by: xmrig | 2019-02-21T09:43:13+00:00
- Closed at: 2019-08-02T12:02:31+00:00
