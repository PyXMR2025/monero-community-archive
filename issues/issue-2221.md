---
title: 'Deleted '
source_url: https://github.com/xmrig/xmrig/issues/2221
author: dodois
assignees: []
labels: []
created_at: '2021-03-31T13:54:38+00:00'
updated_at: '2021-09-09T06:41:45+00:00'
type: issue
status: closed
closed_at: '2021-04-04T17:03:17+00:00'
---

# Original Description
No description

# Discussion History
## snipeTR | 2021-03-31T16:09:30+00:00
Please check json with this tool
https://jsonformatter.curiousconcept.com

## SChernykh | 2021-03-31T16:23:14+00:00
You get an incorrect answer from the pool, it's not the problem with config.json

## SChernykh | 2021-03-31T16:34:20+00:00
It's useless to check with curl. You need to see what pool sends to xmrig. But I'll take a wild guess and say that you configured the pool to use TLS and didn't enable it in config.json, or vice versa.

## SChernykh | 2021-04-04T13:51:29+00:00
You need to add `-DWITH_DEBUG_LOG=ON` to cmake command line.

# Action History
- Created by: dodois | 2021-03-31T13:54:38+00:00
- Closed at: 2021-04-04T17:03:17+00:00
