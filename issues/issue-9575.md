---
title: No longer possible to create multisig wallets purely through RPC
source_url: https://github.com/monero-project/monero/issues/9575
author: ghost
assignees: []
labels:
- question
- request
created_at: '2024-11-16T00:02:02+00:00'
updated_at: '2024-11-28T15:04:13+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Now that multisig is considered unsafe/experimental, you cannot create and use multisig wallets via RPC, there is no command to enable it for the wallet, so it will always fail unless you create a hacky shell script.

# Discussion History
## moneromooo-monero | 2024-11-23T14:28:37+00:00
This is unlikely, given this is tested in functional tests.
Please give more details.


## ghost | 2024-11-28T15:04:12+00:00
Youve stumbled onto one of the biggest problems with monero, _documentation_
In the tests you can see they are passing a multisig enable command to prepare_multisig, although the official doc show that RPC call take no params. Use that.
Best of luck


# Action History
- Created by: ghost | 2024-11-16T00:02:02+00:00
