---
title: Unclear error message when trying to send more than my balance.
source_url: https://github.com/monero-project/monero/issues/1147
author: oyvkva
assignees: []
labels: []
created_at: '2016-09-28T10:47:26+00:00'
updated_at: '2016-12-15T17:09:40+00:00'
type: issue
status: closed
closed_at: '2016-12-15T17:09:40+00:00'
---

# Original Description
`transfer somewhere 5000`

> Failed to find a way to create transactions. This is usually due to dust which is so small it cannot pay for itself in fees.

I get this message in wallet if I try to send more than my balance.

Log:

> not enough money to transfer, available only 0.300000000000, transaction amount 5000.000000000000 = 5000.000000000000 + 0.000000000000 (fee)

Wouldn't it be good if it said "Not enough money to transfer" in wallet as well?


# Discussion History
## ghost | 2016-10-07T22:48:07+00:00
The fault is likely due to the message not matching the log output in `simplewallet.cpp`

That said, there doesn't seem to be any check for unspendable dust which might make this difficult to fix properly without a new function and error message.

Also, there's a lot of error message reduplication both within the functions of `simplewallet.cpp` and in `/wallet/wallet_errors.h`. 

I think this is a deeper problem than it first appears, and is tangentially related to the logging system itself which needs overhauling. I'll see if I can ask the main devs for some pointers before I even try tackling this.


## moneromooo-monero | 2016-10-15T15:38:26+00:00
https://github.com/monero-project/monero/pull/1220


# Action History
- Created by: oyvkva | 2016-09-28T10:47:26+00:00
- Closed at: 2016-12-15T17:09:40+00:00
