---
title: Donate server for xhv is broken
source_url: https://github.com/xmrig/xmrig/issues/2487
author: Lonnegan
assignees: []
labels:
- bug
created_at: '2021-07-21T15:41:25+00:00'
updated_at: '2021-12-19T15:43:33+00:00'
type: issue
status: closed
closed_at: '2021-12-19T15:43:33+00:00'
---

# Original Description
xmrig tries to mine the dev fee for 1 minute every 100 minutes. When mining Haven (xhv), that seems to be broken atm.

![donate-xhv](https://user-images.githubusercontent.com/60088495/126517744-b6f71ffc-48fe-437a-8714-7452feb187e9.png)

So you don't get dev fee atm when people mine Haven. Please fix your donate pool in order to get your well deserved dev fee! :)

# Discussion History
## xmrig | 2021-07-22T01:20:23+00:00
Fixed, thank you. This bug was caused by too much aggressive user agent filtering.

# Action History
- Created by: Lonnegan | 2021-07-21T15:41:25+00:00
- Closed at: 2021-12-19T15:43:33+00:00
