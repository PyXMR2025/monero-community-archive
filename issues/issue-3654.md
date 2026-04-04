---
title: After create new address, pools not accept this address
source_url: https://github.com/monero-project/monero/issues/3654
author: Ales999
assignees: []
labels: []
created_at: '2018-04-17T15:47:21+00:00'
updated_at: '2018-04-17T17:58:25+00:00'
type: issue
status: closed
closed_at: '2018-04-17T17:58:25+00:00'
---

# Original Description
Hello!
My primary address started with 42... and good using all pools.
After upgrade wallet to 'Lithium Luna', create new address.
New address started with 84... and this address not valid, example for pool supportxmr.com:
"error: Invalid payment address provided"
Why ? 
Today add new address, this started with 86...
It's normal ?

PS Using MAC OS 10.12.6, GUI version, and remote daemon.

# Discussion History
## moneromooo-monero | 2018-04-17T17:00:23+00:00
The pools aren't maintained here. If you want them to support subaddresses, file a bug in their own repos. I'm not sure which are the best maintained versions, but https://github.com/zone117x/node-cryptonote-pool is the original repo for the main pool software.

## Ales999 | 2018-04-17T17:58:25+00:00
Ah, these are subaddresses. Understood thanks. Then close this.

# Action History
- Created by: Ales999 | 2018-04-17T15:47:21+00:00
- Closed at: 2018-04-17T17:58:25+00:00
