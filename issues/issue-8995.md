---
title: 'suddenly E duplicate key: support_flags'
source_url: https://github.com/monero-project/monero/issues/8995
author: MXS2514
assignees: []
labels: []
created_at: '2023-09-18T12:39:10+00:00'
updated_at: '2023-09-18T12:40:49+00:00'
type: issue
status: closed
closed_at: '2023-09-18T12:40:49+00:00'
---

# Original Description
E duplicate key: support_flags
Exception at [portable_storage::load_from_binary], what=duplicate key: support_flags
![image](https://github.com/monero-project/monero/assets/14242157/8eaa74e8-b8ab-443d-8cb1-4e2cbc8a8ce5)

got many those with last 24 hours , same issue #8062, already delete related file, but not work

my cli:
`monerod.exe --data-dir=.\ --db-sync-mode safe:sync --rpc-bind-port xxx --enable-dns-blocklist --hide-my-port --prune-blockchain --sync-pruned-blocks --log-level 0`

# Discussion History
## selsta | 2023-09-18T12:40:49+00:00
You can ignore it, someone is sending you invalid p2p packets. Happens on a lot of nodes but doesn't cause any issues.

# Action History
- Created by: MXS2514 | 2023-09-18T12:39:10+00:00
- Closed at: 2023-09-18T12:40:49+00:00
