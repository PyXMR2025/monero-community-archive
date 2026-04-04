---
title: Unable to do transactions Cannot deserialize mg[i] (Trezor T)
source_url: https://github.com/monero-project/monero/issues/6955
author: ossii79
assignees: []
labels: []
created_at: '2020-10-31T23:43:23+00:00'
updated_at: '2020-11-01T00:38:11+00:00'
type: issue
status: closed
closed_at: '2020-11-01T00:38:11+00:00'
---

# Original Description
Using latest code, tried both on windows 10 and linux, wallet-cli and gui wallet with a Trezor T.
Wallet syncs fine with remote daemon, however when trying to do transactions I get
`Can't create transaction: unexpected error: Cannot deserialize mg[i]`

Tried to do this with log_lvl 2. It creates the transaction, everything looks normal (recieving address, change amount etc) all the way to the end (transaction created) until it throws the error message.
Nothing it shown in transactions and no amount has been sent.


# Discussion History
## selsta | 2020-10-31T23:44:32+00:00
Did you try updating your Trezor firmware?

## ossii79 | 2020-11-01T00:38:11+00:00
Well that was embarrasing... Your absolutly right, upgrading the trezor firmware from 2.3.3 to 2.3.4 resolved it.

# Action History
- Created by: ossii79 | 2020-10-31T23:43:23+00:00
- Closed at: 2020-11-01T00:38:11+00:00
