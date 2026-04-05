---
title: wallet-cli complains about missing key images
source_url: https://github.com/seraphis-migration/monero/issues/29
author: ComputeryPony
assignees: []
labels: []
created_at: '2025-04-18T02:58:26+00:00'
updated_at: '2025-04-24T18:11:54+00:00'
type: issue
status: closed
closed_at: '2025-04-24T18:11:53+00:00'
---

# Original Description
While testing the fcmp++-staging branch (using commit 9737c75c17e9aae19241440d593482d6e853e1dd) and playing around on a private testnet I managed to get the wallet-cli to start printing `(Some owned outputs have missing key images - export_outputs, import_outputs, export_key_images, and import_key_images needed)` after doing a `refresh`.

This happened after I mined ~600 blocks to wallet01 and did a `sweep_all` to wallet02 (this took... a while). All the resulting vouts show the key image as ??? when doing `incoming_transfers verbose` in wallet02.

Despite this wallet02 was still able to spend these outputs, I was able to `sweep_all` them to wallet02 repeatedly until I consolidated it down to a single unspent vout.

I was testing this by changing `stagenet_hard_forks` in `hardforks.cpp` to just make all the hardforks 1 block apart and adding a 17 entry, hopefully this is the correct way to set this up.

# Discussion History
## ComputeryPony | 2025-04-24T18:11:53+00:00
Fixed in #32 

# Action History
- Created by: ComputeryPony | 2025-04-18T02:58:26+00:00
- Closed at: 2025-04-24T18:11:53+00:00
