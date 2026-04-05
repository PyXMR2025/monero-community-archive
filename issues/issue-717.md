---
title: 'Can''t mine to subaddresses, code: -1'
source_url: https://github.com/xmrig/xmrig/issues/717
author: ghost
assignees: []
labels:
- question
created_at: '2018-07-13T03:56:28+00:00'
updated_at: '2018-07-14T09:25:29+00:00'
type: issue
status: closed
closed_at: '2018-07-14T09:25:29+00:00'
---

# Original Description
Release v0.12.0.0, Lithium Luna, added support for subaddresses but, whenever you set your config.json setting to a subaddress (an 8-prefix address) you get an error

`[mine.pool.com:port] error: "Invalid payment address provided", code: -1`

# Discussion History
## xmrig | 2018-07-14T09:25:29+00:00
* Subaddresses support depends of pool, miner know nothing about addresses, this error sent by pool, you should ask it your pool operator.
* Miner not require to run any daemon or wallet.

Thank you.

# Action History
- Created by: ghost | 2018-07-13T03:56:28+00:00
- Closed at: 2018-07-14T09:25:29+00:00
