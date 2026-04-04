---
title: '{newline} symbol missed in daemon after block counter'
source_url: https://github.com/monero-project/monero/issues/4741
author: Seriy-A
assignees: []
labels: []
created_at: '2018-10-27T17:23:09+00:00'
updated_at: '2018-11-07T14:25:14+00:00'
type: issue
status: closed
closed_at: '2018-11-07T14:25:14+00:00'
---

# Original Description
every message after block counter appears like NumberDateStamp
examples:
`block 174070 / 16878202018-10-27 15:41:51.975   16284   INFO    global  src/blockchain_db/lmdb/db_lmdb.cpp:600  [batch] DB resize needed`
`block 225270 / 16878202018-10-27 16:45:05.761   16284   WARN    net.dns src/common/dns_utils.cpp:519    WARNING: no two valid MoneroPulse DNS checkpoint records were received`

logfile looks nice (all \n correct, new record==new line), so it seems thats counter bug

# Discussion History
## moneromooo-monero | 2018-10-27T17:33:31+00:00
This is one of the export/import tools, right ?

## moneromooo-monero | 2018-10-27T17:41:50+00:00
https://github.com/monero-project/monero/pull/4742 should fix it.

## Seriy-A | 2018-10-27T17:54:38+00:00
> 
> 
> This is one of the export/import tools, right ?

v.13 only import tool tested yet, v.12 was in monerod too

## moneromooo-monero | 2018-11-07T14:15:56+00:00
+resolved

# Action History
- Created by: Seriy-A | 2018-10-27T17:23:09+00:00
- Closed at: 2018-11-07T14:25:14+00:00
