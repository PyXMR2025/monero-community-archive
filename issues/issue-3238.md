---
title: '(testnet) "WARNING: batch transaction mode already enabled, but asked to enable
  batch mode"'
source_url: https://github.com/monero-project/monero/issues/3238
author: ghost
assignees: []
labels: []
created_at: '2018-02-07T01:57:57+00:00'
updated_at: '2018-02-08T23:05:39+00:00'
type: issue
status: closed
closed_at: '2018-02-08T23:05:39+00:00'
---

# Original Description
Looking at my testnet daemon output, I see a bunch of normal messages about reorgs and synchronized ok stuff, but in the middle I see a strange warning that says: "WARNING: batch transaction mode already enabled, but asked to enable batch mode"

Is this an issue I should report on? Or is it nothing?

Log (pertinent section is in bold):

2018-02-04 10:58:00.690 [P2P0]  INFO    global  src/cryptonote_core/blockchain.cpp:1465 ----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT 1091856
id:     <a43c49c5eaf13a311f012a5e111ad382cce5b803e10f3ff76eed8e817306ec66>
PoW:    <06f3d48530a938dc9568d76c9d64a70113ec30c16f05ae4614ca569810980000>
difficulty:     25465
2018-02-04 10:58:54.384 [P2P6]  INFO    global  src/cryptonote_core/blockchain.cpp:1454 ###### REORGANIZE on height: 1091856 of 1091856 with cum_difficulty 41088097723
 alternative blockchain size: 2 with cum_difficulty 41088123203
2018-02-04 10:58:54.481 [P2P6]  INFO    global  src/cryptonote_core/blockchain.cpp:1465 ----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT 1091856
id:     <75c3ff0eb36a4987f955f1b7ea50b7662af18ea35fc2bd4e596022c2f23895e1>
PoW:    <be7ab019fde8b988c0fdbec5e3e9b24b7c6389ea5a18972f1e28a0208a730100>
difficulty:     25465
**2018-02-04 10:58:54.481 [P2P6]  WARN    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:2733 WARNING: batch transaction mode already enabled, but asked to enable batch mode**
2018-02-04 10:58:54.606 [P2P6]  INFO    global  src/cryptonote_core/blockchain.cpp:924  REORGANIZE SUCCESS! on height: 1091856, new blockchain size: 1091858
2018-02-04 18:10:09.671 [P2P8]  INFO    global  src/cryptonote_core/blockchain.cpp:1465 ----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT 1092039
id:     <a30e219c1a04212f7fdcd9713682b3f60e55d75c8561e06181a594dc54b212ce>
PoW:    <de7f971103c29e43a38054b8d26fa52eee3d5388dbf5d90413f0d03e0caa0000>
difficulty:     25312
2018-02-04 20:36:05.959 [P2P8]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1548    SYNCHRONIZED OK
2018-02-05 06:41:40.108 [P2P4]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1548    SYNCHRONIZED OK
2018-02-06 03:46:06.774 [P2P5]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1167    [88.99.252.250:43536 INC]  Synced 1092952/1092952
2018-02-06 03:46:06.774 [P2P5]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1548    SYNCHRONIZED OK
2018-02-06 05:59:57.732 [P2P1]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1548    SYNCHRONIZED OK
2018-02-06 20:38:41.998 [P2P4]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1548    SYNCHRONIZED OK


# Discussion History
## hyc | 2018-02-07T11:46:58+00:00
It's nothing, ignore it.

# Action History
- Created by: ghost | 2018-02-07T01:57:57+00:00
- Closed at: 2018-02-08T23:05:39+00:00
