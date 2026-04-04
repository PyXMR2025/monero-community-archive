---
title: monero-wallet-rpc export_key_images returns unexpected result
source_url: https://github.com/monero-project/monero/issues/4992
author: woodser
assignees: []
labels: []
created_at: '2018-12-18T13:23:50+00:00'
updated_at: '2019-01-30T17:16:07+00:00'
type: issue
status: closed
closed_at: '2019-01-30T17:16:07+00:00'
---

# Original Description
monero-wallet-rpc `export_key_images` returns a response like `{id=0, jsonrpc=2.0, result={offset=311}}` which does not include `signed_key_images` as [documented](https://www.getmonero.org/resources/developer-guides/wallet-rpc.html#export_key_images).

Environment: latest master, Mac OSX

# Discussion History
## moneromooo-monero | 2018-12-24T12:41:46+00:00
Did you import outputs beforehand ? export_key_images will export those *new* ones which were imported.

## moneromooo-monero | 2018-12-24T13:01:30+00:00
https://github.com/monero-project/monero/pull/5012 allows you to get all key images.

## woodser | 2018-12-24T14:30:54+00:00
No I didn't import outputs beforehand.  The need to import outputs then call export_key_images to return new images was unknown to me as it's not documented for wallet RPC.  +1 on the ability to get all key images (#5012)

## woodser | 2019-01-30T17:16:07+00:00
Resolved by #5012 

# Action History
- Created by: woodser | 2018-12-18T13:23:50+00:00
- Closed at: 2019-01-30T17:16:07+00:00
