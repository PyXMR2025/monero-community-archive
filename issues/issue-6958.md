---
title: 'monerod crashes during resync: Exception in threadpool'
source_url: https://github.com/monero-project/monero/issues/6958
author: nullcopy
assignees: []
labels: []
created_at: '2020-11-01T17:29:40+00:00'
updated_at: '2020-11-02T03:19:09+00:00'
type: issue
status: closed
closed_at: '2020-11-01T20:13:00+00:00'
---

# Original Description
When running `monerod` on latest 0.17.1.1, the node repeatedly crashes during resync with the following output:
```
2020-10-31 15:18:25.197 [P2P3]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:368     [70.180.135.90:18080 OUT] Sync data returned a new top block candidate: 2210000 -> 2220390 [Your node is 10390 blocks (14.4 days) behind] 
2020-10-31 15:18:25.197 [P2P3]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:368     SYNCHRONIZATION started
2020-10-31 15:18:30.508 [P2P0]  ERROR   default src/common/threadpool.cpp:170   Exception in threadpool job: mprotect failed
```

I am running monerod v0.17.1.1 on Ubuntu 20.04.

# Discussion History
## dEBRUYNE-1 | 2020-11-01T19:31:57+00:00
Please close either #6957 or #6958. Currently, a duplicate exists. 

## moneromooo-monero | 2020-11-01T20:13:00+00:00
Duplicate.

## nullcopy | 2020-11-02T03:19:09+00:00
Sorry for the duplicate issues. Must've had a browser session issue :facepalm:

# Action History
- Created by: nullcopy | 2020-11-01T17:29:40+00:00
- Closed at: 2020-11-01T20:13:00+00:00
