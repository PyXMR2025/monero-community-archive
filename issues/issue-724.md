---
title: Mining 2 pools same time?
source_url: https://github.com/xmrig/xmrig/issues/724
author: LearnMiner
assignees: []
labels: []
created_at: '2018-07-25T10:31:47+00:00'
updated_at: '2018-11-05T13:54:22+00:00'
type: issue
status: closed
closed_at: '2018-11-05T13:54:22+00:00'
---

# Original Description
Its possible mining 2 pools at same time inside code? and how can i do?

Or change pool every 1 accept share for example

# Discussion History
## 0xhesch | 2018-08-04T13:13:45+00:00
The principle you ask for is somewhat similar to how the donation fee works - which has been tested thoroughly. You can increase the fee to 50% while changing the donation target to your (own) second pool.

If you do it this way you should consider making manual donations to support the dev.

## snipeTR | 2018-08-04T13:22:59+00:00
Two process run and json max cpu useg %50

# Action History
- Created by: LearnMiner | 2018-07-25T10:31:47+00:00
- Closed at: 2018-11-05T13:54:22+00:00
