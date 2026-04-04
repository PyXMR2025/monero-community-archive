---
title: '[discussion] timelock_coins and get_timelock_proof'
source_url: https://github.com/monero-project/monero/issues/8010
author: ghost
assignees: []
labels: []
created_at: '2021-10-16T23:00:41+00:00'
updated_at: '2021-10-17T14:09:09+00:00'
type: issue
status: closed
closed_at: '2021-10-17T14:09:09+00:00'
---

# Original Description
Implement method `timelock_coins <amount> <unlock_time>`. Same as `locked_transfer` but it is a self transfer. It also returns a `timelock_proof` : a receipt with the amount and lock time similar to `get_spend_proof`. The method `get_timelock_proof txid` will provide user with proof of amount locked and duration. 

Reason: I think this will make it easier for users to lock coins and interact with monero dApps which require locked coins as a form of authentication. 

# Discussion History
## ghost | 2021-10-16T23:03:46+00:00
Also, `check_timelock_proof` to pair with `get_timelock_proof`.

# Action History
- Created by: ghost | 2021-10-16T23:00:41+00:00
- Closed at: 2021-10-17T14:09:09+00:00
