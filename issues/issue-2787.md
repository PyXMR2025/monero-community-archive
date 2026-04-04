---
title: Get integrated address from transaction by payment id
source_url: https://github.com/monero-project/monero/issues/2787
author: Arti3DPlayer
assignees: []
labels: []
created_at: '2017-11-10T17:21:17+00:00'
updated_at: '2017-11-12T10:26:47+00:00'
type: issue
status: closed
closed_at: '2017-11-12T10:26:47+00:00'
---

# Original Description
My actions:

1) `monero-wallet-cli  make_integrated_address`
Receive: 
```
"result": {
    "integrated_address": "my_address"
    "payment_id": "my_payment_id"
  }
```

2)  Then from another wallet I send money with transfer method: https://getmonero.org/resources/developer-guides/wallet-rpc.html#transfer


3) `monero-wallet-cli  get_transefrs`
Receive
`{'payment_id': 'some_unique_payment_id', 'amount': 100}`

4) `monero-wallet-cli make_integrated_address(some_unique_payment_id)
`
5) Received new address, instead of existing one

# Discussion History
## moneromooo-monero | 2017-11-11T11:03:54+00:00
I had to do a few assumptions on what you left unsaid:

- you used monero-wallet-rpc instead of monero-wallet-cli (since make_integrated_address is a RPC)
- my_payment_id and some_unique_payment_id are the same (otherwise it doesn't make sense)
- the transfer was made to the integrated address

Given that, it works for me. I get the same address from the first make_integrated_address RPC (without a payment id) and the second one (with a payment id).

Make sure you didn't make a mistake, and if you didn't, give more precise repro steps.


## Arti3DPlayer | 2017-11-12T10:26:47+00:00
@moneromooo-monero thanks for answer. Yes it was my mistake. Works well

# Action History
- Created by: Arti3DPlayer | 2017-11-10T17:21:17+00:00
- Closed at: 2017-11-12T10:26:47+00:00
