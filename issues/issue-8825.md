---
title: How to run multiple nodes on one ip?
source_url: https://github.com/monero-project/monero/issues/8825
author: Dinamitrii
assignees: []
labels:
- question
created_at: '2023-04-18T18:39:19+00:00'
updated_at: '2023-12-07T21:19:14+00:00'
type: issue
status: closed
closed_at: '2023-12-07T21:19:14+00:00'
---

# Original Description
How to run multiple nodes on one ip?
Sorry if this question is stupid but i want to run multiple nodes on different machines but i have only one real ip and i'm behind router.Port forwarding works only with one local machine.Which setting have to be changed or what could be the settings of the router?
Thank you in advance.

# Discussion History
## moneromooo-monero | 2023-04-19T16:15:46+00:00
Listen on different ports for p2p, rpc, and zmq (or just disable the latter). You probably also want a different --data-dir (though it's supposed to be able to use two nodes a single chain).

## Dinamitrii | 2023-04-19T18:37:07+00:00
So until now i used the router capabilities for 
pc1 used the original ports 18080~18083 outer to the same inner forwarding
pc2 18084~18087 outer to the 18080~18083 inner and
pc3 18088~18091 outer to the 18080~18083 inner.

Until now pc2 and pc3 importing the blockchain(exported by me) and after that i'll see if getting this msg for no incoming connections.

How it seems to you this setup?
Thank you in advance :)

# Action History
- Created by: Dinamitrii | 2023-04-18T18:39:19+00:00
- Closed at: 2023-12-07T21:19:14+00:00
