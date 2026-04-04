---
title: ' A single payment id is allowed per transaction'
source_url: https://github.com/monero-project/monero/issues/3805
author: zeshanvirk
assignees: []
labels: []
created_at: '2018-05-15T05:54:38+00:00'
updated_at: '2018-05-15T19:56:57+00:00'
type: issue
status: closed
closed_at: '2018-05-15T19:56:57+00:00'
---

# Original Description
I'm trying to send some tokens to an integrated address with a payment id but getting this error 

`  "code": -5,
    "message": "A single payment id is allowed per transaction"`

if i remove the id, transaction done successfully, i'm using transfer method

# Discussion History
## stoffu | 2018-05-15T07:13:41+00:00
Do you get this error even when you're sending to just one integrated address?

## zeshanvirk | 2018-05-15T07:20:25+00:00
yes, as i'm sending to just one integrated address.

## el00ruobuob | 2018-05-15T07:29:10+00:00
The integrated address includes a payment id. If you only use the integrated address and try not to add a second id is it working? From the OP I'll say yes.

## stoffu | 2018-05-15T07:30:06+00:00
@el00ruobuob Ah that explains it.

## zeshanvirk | 2018-05-15T07:40:42+00:00
yes if i not include the id it works, did the wallet itself adds the paymentID that is generated along with integrated address?

## iDunk5400 | 2018-05-15T07:59:56+00:00
Integrated addresses are addresses that integrate a (short) payment id.

From monero-wallet-cli:
```
[wallet 4BFQiD]: help integrated_address
Command usage:
  integrated_address [<payment_id> | <address>]

Command description:
  Encode a payment ID into an integrated address for the current wallet public address (no argument uses a random payment ID), or decode an integrated address to standard address and payment ID
```

## stoffu | 2018-05-15T08:50:34+00:00
You can use this tool https://xmr.llcoins.net/addresstests.html (Check Address) to see the short payment ID integrated in an integrated address.

## dEBRUYNE-1 | 2018-05-15T19:48:46+00:00
+resolved

# Action History
- Created by: zeshanvirk | 2018-05-15T05:54:38+00:00
- Closed at: 2018-05-15T19:56:57+00:00
