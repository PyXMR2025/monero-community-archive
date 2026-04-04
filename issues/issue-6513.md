---
title: According to documentation, payment_id can be ignored in transfer RPC call,
  but it returns an error if empty
source_url: https://github.com/monero-project/monero/issues/6513
author: thestick613
assignees: []
labels: []
created_at: '2020-05-07T23:18:56+00:00'
updated_at: '2020-05-07T23:27:10+00:00'
type: issue
status: closed
closed_at: '2020-05-07T23:27:10+00:00'
---

# Original Description
According to [docs])https://github.com/monero-project/monero/wiki/Wallet-RPC-Documentation#transfer), payment_id is optional, but this is what you get if you don't put a payment_id:

`{'error': {'code': -5, 'message': 'Payment ID has invalid size: '}, 'id': '0', 'jsonrpc': '2.0'}`

What's the catch?

# Discussion History
## thestick613 | 2020-05-07T23:27:10+00:00
I was calling the wrong RPC function.

# Action History
- Created by: thestick613 | 2020-05-07T23:18:56+00:00
- Closed at: 2020-05-07T23:27:10+00:00
