---
title: invalid payment id
source_url: https://github.com/monero-project/monero/issues/5517
author: randy86
assignees: []
labels:
- invalid
created_at: '2019-05-03T04:39:32+00:00'
updated_at: '2019-05-03T09:33:46+00:00'
type: issue
status: closed
closed_at: '2019-05-03T09:33:46+00:00'
---

# Original Description
how to generate 64 char payment id, i've already using 
**openssl rand -hex 32**
and generate this
curl -X POST http://127.0.0.1:18082/json_rpc -d '{"jsonrpc":"2.0","id":"0","method":"make_integrated_address","params":{"payment_id":"a2ad26b5fa357de021b05a01309004575e2c4da9dfee97f08b267aa8cf391c2d"}}' -H 'Content-Type: application/json'

but result still Invalid Payment ID

# Discussion History
## pallas1 | 2019-05-03T06:40:19+00:00
64 bits, not 32 bytes.

## moneromooo-monero | 2019-05-03T09:29:07+00:00
Needs to be 8 bytes (16 hex chars).

+invalid


# Action History
- Created by: randy86 | 2019-05-03T04:39:32+00:00
- Closed at: 2019-05-03T09:33:46+00:00
