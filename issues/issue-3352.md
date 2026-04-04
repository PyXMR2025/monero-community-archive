---
title: Monero Wallet RPC
source_url: https://github.com/monero-project/monero/issues/3352
author: jinglics
assignees: []
labels:
- invalid
created_at: '2018-03-05T15:31:09+00:00'
updated_at: '2018-03-05T17:00:58+00:00'
type: issue
status: closed
closed_at: '2018-03-05T17:00:58+00:00'
---

# Original Description
The latest version monero-wallet-rpc doesn't support argument --prompt-for-password?
Is there anyway in which I can protect the password?
Thanks

# Discussion History
## moneromooo-monero | 2018-03-05T15:42:21+00:00
Please give details of what you've tried, and what/how did not work, and any errors.

## jinglics | 2018-03-05T15:53:54+00:00
monero-wallet-rpc --config-file /root/.bitmonero/bitmonero_wallet.conf --prompt-for-password
Error: Failed to parse arguments: unrecognised option 'prompt-for-password'


## moneromooo-monero | 2018-03-05T15:58:52+00:00
Are you sure you're using a recent version ? It's in the --help here, and works when used. Recent version possibly means more recent than the current binaries.

## jinglics | 2018-03-05T16:03:45+00:00
I used this version: v0.11.1.0
Helium Hydra, Point Release 1

## moneromooo-monero | 2018-03-05T16:57:29+00:00
OK, then you just need to use a newer version. If you want to use binaries, there will be new ones within the next two weeks

+invalid


# Action History
- Created by: jinglics | 2018-03-05T15:31:09+00:00
- Closed at: 2018-03-05T17:00:58+00:00
