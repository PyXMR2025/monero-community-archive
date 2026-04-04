---
title: Unknown command 'mining_status'
source_url: https://github.com/monero-project/monero/issues/8485
author: vincent7128
assignees: []
labels: []
created_at: '2022-08-06T00:16:15+00:00'
updated_at: '2022-08-06T04:48:16+00:00'
type: issue
status: closed
closed_at: '2022-08-06T04:42:39+00:00'
---

# Original Description
How to check mining status?

[wallet xx]: version
Monero 'Fluorine Fermi' (v0.18.0.0-release)

[wallet xx]: mining_status
Error: Unknown command 'mining_status', try 'help'


# Discussion History
## vincent7128 | 2022-08-06T04:48:16+00:00
I use this now:
curl -v -X POST http://127.0.0.1:18081/mining_status -d '{}' -H 'Content-Type: application/json'


# Action History
- Created by: vincent7128 | 2022-08-06T00:16:15+00:00
- Closed at: 2022-08-06T04:42:39+00:00
