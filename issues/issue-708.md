---
title: Enhancement - Miner take "algo" and "variant" settings from proxy or http link
source_url: https://github.com/xmrig/xmrig/issues/708
author: borodamd
assignees: []
labels:
- enhancement
created_at: '2018-06-29T08:00:25+00:00'
updated_at: '2018-11-05T13:53:52+00:00'
type: issue
status: closed
closed_at: '2018-11-05T13:53:52+00:00'
---

# Original Description
If i want to switch mining from Cryptonight-lite to Cryptonight, i need to reconfigure proxy and all miners one by one.

If will be an great option to take this options direct from proxy or use whole config from http link - will be easier to change coin to mine.

# Discussion History
## xmrig | 2018-07-01T08:33:04+00:00
cn/cn-lite/cn-heavy require different memory amount, so different settings, threads, etc, it require new config format and ability to restart threads. On protocol level proxy can tell miner what algorithm and variant used.
Thank you.

## xmrig | 2018-11-05T13:53:52+00:00
Merge with #618

# Action History
- Created by: borodamd | 2018-06-29T08:00:25+00:00
- Closed at: 2018-11-05T13:53:52+00:00
