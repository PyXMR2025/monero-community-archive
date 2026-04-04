---
title: Monero Release Checklist for v0.17.0.0 (hard-fork) - 10/17/2020
source_url: https://github.com/monero-project/meta/issues/500
author: sethforprivacy
assignees: []
labels: []
created_at: '2020-08-17T18:11:18+00:00'
updated_at: '2020-10-21T17:07:21+00:00'
type: issue
status: closed
closed_at: '2020-10-21T17:07:20+00:00'
---

# Original Description
- [x] Security audit
- [x] Code audit 
- [ ] Ledger integration
  - [x] Implemented in Monero codebase (if needed)
  - [x] Ledger app integration coded by Ledger
  - [ ] Ledger Monero app update available
- [ ] Trezor integration
  - [x] Implemented in Monero codebase (if needed)
  - [x] Trezor app integration coded by Trezor
  - [ ] Trezor firmware update available (if needed)
- [x] Fork height set
  - [ ] Monero-announce mailer notice 
  - [ ] Twitter announcement 
  - [ ] Reddit announcement 
  - [ ] Getmonero.org announcement 
- [ ] Notify wallets
  - [ ] MyMonero
  - [ ] Coinomi
  - [ ] Exa Wallet
  - [ ] Wookey Wallet
  - [ ] X Wallet
  - [ ] Guarda
  - [ ] ZelCore
  - [ ] Cake Wallet
  - [ ] Monerujo
  - [ ] Edge Wallet
  - [ ] Exodus
  - [ ] XMRWallet
- [ ] Notify exchanges
  - [ ] https://web.getmonero.org/community/merchants/#exchanges
- [ ] Notify 3rd party payment processors
  - [ ] https://web.getmonero.org/community/merchants/#payment-gateways
- [ ] Notify mining pools
  - [ ] https://miningpoolstats.stream/monero
- [ ] New release name found using Monero naming convention
- [ ] Release tagged
  - [ ] Update src/version.cpp.in with new version AND new name (if necessary)
  - [ ] Update Gitian YML files in contrib/gitian/ to the new version number
  - [ ] Update README.md with new fork table entry (or at least update the Recommended Monero version)
  - [ ] Update contrib/gitian/README.md so that the instructions reflect the current version
  - [ ] Update src/checkpoints/checkpoints.cpp with a recent hardcoded checkpoint
  - [ ] Update src/blocks/checkpoints.dat with ./monero-blockchain-export --output-file checkpoints.dat --block-stop <recent block height> --blocksdat
  - [ ] Update expected_block_hashes_hash in src/cryptonote_core/blockchain.cpp with checkpoints.dat sha256 hash
- [x] Testnet forked
- [ ] Testnet testing/verification
  - [ ] Ledger
  - [ ] Trezor
  - [ ] Release-specific testing
  - [ ] RPC testing/update RPC documentation
- [ ] CLI reproducible builds validated
- [ ] CLI released
  - [ ] https://web.getmonero.org/downloads/ updated
  - [ ] Update hashes.txt on website
  - [ ] Update downloads.yml on website
  - [ ] Update auto-update DNS records
  - [ ] Update redirects on downloads box
  - [ ] Update seed nodes
- [ ] GUI released
  - [ ] https://web.getmonero.org/downloads/ updated
  - [ ] Update hashes.txt on website
  - [ ] Update hashes.txt.sig on website
  - [ ] Update downloads.yml on website
  - [ ] Update auto-update DNS records
  - [ ] Update redirects on downloads box
- [ ] Release announcements made
  - [ ] Monero-announce mailer notice 
  - [ ] Twitter announcement 
  - [ ] Reddit announcement 
  - [ ] Getmonero.org announcement

# Discussion History
## selsta | 2020-09-09T00:16:09+00:00
Ledger integration
- [X]  Implemented in Monero codebase (if needed)
- [X]  Ledger app integration coded by Ledger
- [ ] Ledger Monero app update available

Trezor integration
- [X]  Implemented in Monero codebase (if needed)
- [X]  Trezor app integration coded by Trezor
- [ ] Trezor firmware update available (if needed)

---------

- [X] Testnet forked

----------

- [ ] New release name found using Monero naming convention

## sethforprivacy | 2020-09-09T00:44:26+00:00
Thanks, @selsta!

Added the missing items to the checklist, and updated status as you said.

## scottAnselmo | 2020-10-21T17:07:20+00:00
Closing as both v0.17.0 and v0.17.1 have been released

# Action History
- Created by: sethforprivacy | 2020-08-17T18:11:18+00:00
- Closed at: 2020-10-21T17:07:20+00:00
