---
title: monerod crashed
source_url: https://github.com/monero-project/monero/issues/4303
author: kenken64
assignees: []
labels: []
created_at: '2018-08-26T00:24:14+00:00'
updated_at: '2018-08-30T16:18:54+00:00'
type: issue
status: closed
closed_at: '2018-08-30T16:18:54+00:00'
---

# Original Description
Uncaught exception! Error adding hard fork version to db transaction: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid

./monerod --log-level 3 --testnet --data-dir /mnt/d/bdata/monero --hide-my-port --no-igd

# Discussion History
## kenken64 | 2018-08-26T01:01:15+00:00
Running on master branch windows 10 ubuntu 16.04 with admin rights


## moneromooo-monero | 2018-08-26T08:52:23+00:00
32 bit or 64 bit OS ?

Did your machine/OS crash before, or did the power go out and you don't have a battery/UPS ?

## kenken64 | 2018-08-30T16:18:54+00:00
somehow i restart my windows 10 it works now !

# Action History
- Created by: kenken64 | 2018-08-26T00:24:14+00:00
- Closed at: 2018-08-30T16:18:54+00:00
