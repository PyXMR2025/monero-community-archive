---
title: Support checking if wallet rpc is connected to daemon
source_url: https://github.com/monero-project/monero/issues/8314
author: woodser
assignees: []
labels: []
created_at: '2022-05-05T21:36:59+00:00'
updated_at: '2022-05-31T13:12:00+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
This issue requests the ability to check if monero-wallet-rpc is connected to a daemon using an rpc call.

One workaround is to call `check_reserve_proof` and check for the error message "Failed to connect to daemon", but this is roundabout and [causes an error](https://github.com/monero-ecosystem/monero-javascript/issues/56) in monero-wallet-rpc's console unless a real message signature is used.

# Discussion History
# Action History
- Created by: woodser | 2022-05-05T21:36:59+00:00
