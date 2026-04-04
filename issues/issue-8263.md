---
title: Trezor and Ledger interoperability
source_url: https://github.com/monero-project/monero/issues/8263
author: ghost
assignees: []
labels: []
created_at: '2022-04-17T14:58:46+00:00'
updated_at: '2022-05-29T15:32:12+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Currently the Trezor and Ledger hardware wallets are not interoperable with the 'monero-wallet-gui', even though they both have the same mnemonic seed and derivation path. This is explained in this issue: https://github.com/monero-project/monero/issues/5744

This is very unfortunate and since I currently have some free bandwidth, I would like to try to implement a solution. I was wondering how you think would be the best way to approach that? I was thinking of adding an option to Ledger to use the SLIP-0010 scheme as described in the above issue, instead how its currently done. It could be hidden as an advance option.

# Discussion History
## selsta | 2022-04-18T23:10:52+00:00
I assume adding support for SLIP-0010 would solely be a patch here? https://github.com/LedgerHQ/app-monero

One thing to consider is getting changes merged to Ledger's repo might be difficult, especially changes to how the private key gets computed.

# Action History
- Created by: ghost | 2022-04-17T14:58:46+00:00
