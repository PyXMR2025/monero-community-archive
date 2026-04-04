---
title: Rpc 'Transfer' method with 16 character payment_id from an integrated address
source_url: https://github.com/monero-project/monero/issues/1528
author: Pwnmanship
assignees: []
labels: []
created_at: '2017-01-05T13:17:41+00:00'
updated_at: '2017-08-07T17:18:13+00:00'
type: issue
status: closed
closed_at: '2017-08-07T17:18:13+00:00'
---

# Original Description
First I get the payment_id and address from an intregrated address which gives:
Address: 46w8MJYhrSca5gZug7PrwZNKjvHFmKeV11L6pNJPgj5QNEHsN6eeX3DaAQFwZ1ufD4LYCZKArktt113W7QjWvQ7CLjUXpwk
Payment_id: 635e56cc6fbe2b3e


Then I use that to call a transfer:
`{"jsonrpc":"2.0","id":1,"method":"transfer","params":{"destinations":[{"address":"46w8MJYhrSca5gZug7PrwZNKjvHFmKeV11L6pNJPgj5QNEHsN6eeX3DaAQFwZ1ufD4LYCZKArktt113W7QjWvQ7CLjUXpwk","amount":386174160000}],"payment_id":"635e56cc6fbe2b3e","get_tx_key":true,"mixin":3,"unlock_time":0}}`

And the error I get:
`{
  "error": {
    "code": -5,
    "message": "Payment id has invalid format: \"635e56cc6fbe2b3e\", expected 16 or 64 character string"
  },
  "id": 1,
  "jsonrpc": "2.0"
}`

This is with the newest monerod and monero-wallet-rpc.

# Discussion History
## ghost | 2017-01-06T12:12:28+00:00
If this has been addressed, please close the issue.

## luigi1111 | 2017-01-10T22:59:55+00:00
The payment ID is in the integrated address; you shouldn't be supplying it in addition to that.

## moneromooo-monero | 2017-08-07T17:11:24+00:00
+resolved

# Action History
- Created by: Pwnmanship | 2017-01-05T13:17:41+00:00
- Closed at: 2017-08-07T17:18:13+00:00
