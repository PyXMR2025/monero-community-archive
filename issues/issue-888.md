---
title: cryptonote_format_utils.cpp:148 max_out exceeded
source_url: https://github.com/monero-project/monero/issues/888
author: got3nks
assignees: []
labels: []
created_at: '2016-07-06T15:43:25+00:00'
updated_at: '2016-08-10T14:53:57+00:00'
type: issue
status: closed
closed_at: '2016-08-10T14:53:57+00:00'
---

# Original Description
Running latest version 0.9.4, I have removed the blockchain and rebuilding it with blockchain_import tool:

```
monero@crypto:~/monero$ ./blockchain_import --input-file=blockchain.raw
2016-Jul-06 15:39:59.941849 Starting...
2016-Jul-06 15:39:59.941883 Setting log level = 0
2016-Jul-06 15:39:59.941908 database: lmdb
2016-Jul-06 15:39:59.941917 database flags: 0
2016-Jul-06 15:39:59.941925 verify:  true
2016-Jul-06 15:39:59.941933 batch:   true  batch size: 5000
2016-Jul-06 15:39:59.941941 resume:  true
2016-Jul-06 15:39:59.941948 testnet: false
2016-Jul-06 15:39:59.941955 bootstrap file path: blockchain.raw
2016-Jul-06 15:39:59.941963 database path:       /home/cryptos/monero
2016-Jul-06 15:39:59.960434 Loading blockchain from folder /home/monero/lmdb ...
2016-Jul-06 15:40:00.152084 The DB has no hard fork info, reparsing from start
2016-Jul-06 15:40:00.452865 Blockchain not loaded, generating genesis block.
2016-Jul-06 15:40:00.503638 ERROR /DISTRIBUTION-BUILD/src/cryptonote_core/cryptonote_format_utils.cpp:148 max_out exceeded
2016-Jul-06 15:40:00.753990 Blockchain initialized. last block: 0, d1463.h10.m40.s0 time ago, current difficulty: 1
2016-Jul-06 15:40:00.763581 bootstrap file recognized
2016-Jul-06 15:40:00.763615 bootstrap file v0.1
2016-Jul-06 15:40:00.763630 bootstrap magic size: 4
2016-Jul-06 15:40:00.763642 bootstrap header size: 1024
2016-Jul-06 15:40:00.763658 Scanning blockchain from bootstrap file...
```

**ERROR /DISTRIBUTION-BUILD/src/cryptonote_core/cryptonote_format_utils.cpp:148 max_out exceeded**

What is the cause of the error and how to fix?


# Discussion History
## luigi1111 | 2016-07-07T19:43:37+00:00
Fixed in #782.

Also referenced in #790.


# Action History
- Created by: got3nks | 2016-07-06T15:43:25+00:00
- Closed at: 2016-08-10T14:53:57+00:00
