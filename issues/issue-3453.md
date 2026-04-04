---
title: wallet-cli stuck on Starting refresh under Ledger
source_url: https://github.com/monero-project/monero-gui/issues/3453
author: tbfvrs
assignees: []
labels: []
created_at: '2021-05-03T12:29:37+00:00'
updated_at: '2021-05-03T12:48:36+00:00'
type: issue
status: closed
closed_at: '2021-05-03T12:48:36+00:00'
---

# Original Description
Hello

I bought Ledger Nano X recently and moved all my coins from Trezor to it;
I've generated a new wallet using this [tut](https://monero.stackexchange.com/questions/8503/how-do-i-generate-a-ledger-monero-wallet-with-the-cli-monero-wallet-cli);
Everything went smoothly and was working (refreshing went well...);
Today I've synchronized the net, plugged Ledger and started Monero app;
Next started monero-wallet-cli, input wallet name, password, choose not to export viewkey (same when creating the wallet) but it is stuck on Starting refresh and cannot be interrupted (can't write, Esc, Ctrl+C does not work);
Tried to exit the deamon but it didn't close but stuck on Deinitializing core RPC server...

Anyone have a clue what went wrong and what to do...?

Greetz


# Discussion History
## selsta | 2021-05-03T12:31:26+00:00
You have to export the view key, the Ledger is not strong enough to do scanning on device.

## tbfvrs | 2021-05-03T12:48:36+00:00
> 
> 
> You have to export the view key, the Ledger is not strong enough to do scanning on device.

Ohhh OK and I thought (judging by the formentioned tut) it will be slower but still refreshing...
Thanks

# Action History
- Created by: tbfvrs | 2021-05-03T12:29:37+00:00
- Closed at: 2021-05-03T12:48:36+00:00
