---
title: Ask about transactions that see remote nodes
source_url: https://github.com/monero-project/monero/issues/9471
author: wipedlifepotato
assignees: []
labels:
- question
- low priority
created_at: '2024-09-05T14:02:20+00:00'
updated_at: '2024-10-23T11:10:31+00:00'
type: issue
status: closed
closed_at: '2024-10-23T11:10:31+00:00'
---

# Original Description
Hello. I get information that if enable set_log +daemon.rpc:DEBUG on monerod node, then node can see transaction. Them transactions that see node. Do see node Amount/Who send/Who receive? Or is see only IP + TXs encrypted broadcasting string, that only can be decrypted by Who send/Who receive?

 I tried to found something in source code, but there I found only encrypt for payment_id, and leave this and want to just ask in issue. If someone can show that part in source code I will be happy
 
 If I use local node, then network not see who send transaction? 

# Discussion History
## selsta | 2024-09-06T22:13:36+00:00
The node you are connected to does not see "Amount/Who send/Who receive", but it does see your IP address.

> If I use local node, then network not see who send transaction?

Since monero is a P2P network, other nodes will see your IP address if your node broadcasts a transaction. To mitigate that, monero uses Dandelion++ https://dl.acm.org/doi/pdf/10.1145/3292040.3219620

# Action History
- Created by: wipedlifepotato | 2024-09-05T14:02:20+00:00
- Closed at: 2024-10-23T11:10:31+00:00
