---
title: Miner automatically getting disconnected.
source_url: https://github.com/xmrig/xmrig/issues/273
author: sathish09
assignees: []
labels: []
created_at: '2017-12-18T18:25:47+00:00'
updated_at: '2018-03-14T23:41:36+00:00'
type: issue
status: closed
closed_at: '2018-03-14T23:41:36+00:00'
---

# Original Description
Miner automatically getting disconnected from the proxy server. but the local API interface is reporting the hashrate. I even tried to restart every 20 minutes. but still, the issue is not resolved. I tried all the pools and proxies. Also tried without using proxy same thing happens. Help me resolve the issue.

# Discussion History
## QwertyJack | 2017-12-19T02:43:05+00:00
Try a static diff.

## sathish09 | 2017-12-19T04:18:16+00:00
in the miner or in the proxy? I tried setting up a static difficulty in proxy but the same thing happened miners got disconnected after some time period.

## QwertyJack | 2017-12-19T14:48:18+00:00
How much is your static diff?

## sathish09 | 2017-12-20T07:26:06+00:00
5000

## QwertyJack | 2017-12-20T11:33:25+00:00
The diff is fine. Check your network.

# Action History
- Created by: sathish09 | 2017-12-18T18:25:47+00:00
- Closed at: 2018-03-14T23:41:36+00:00
