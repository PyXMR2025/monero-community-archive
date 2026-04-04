---
title: Support restoring multisig wallets from seed in monero-wallet-rpc
source_url: https://github.com/monero-project/monero/issues/8877
author: woodser
assignees: []
labels:
- feature
- proposal
created_at: '2023-05-25T14:05:34+00:00'
updated_at: '2024-01-06T13:42:04+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
This issue requests restoring multisig wallets from seed in monero-wallet-rpc.

Currently `restore_deterministic_wallet` returns an error "invalid mnemonic" with a multisig seed.

monero-wallet-cli supports restoring from seed using the `--restore-from-seed` startup flag, but ideally support can be added to monero-wallet-rpc without using a startup flag.

# Discussion History
## JacksonZ03 | 2024-01-06T13:42:03+00:00
`--restore-multisig-wallet` flag works just fine for me for restoring multisig wallets from the seed. Not sure if there's any real benefit to this.

# Action History
- Created by: woodser | 2023-05-25T14:05:34+00:00
