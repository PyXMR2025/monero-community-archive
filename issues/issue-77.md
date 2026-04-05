---
title: Integration tests for patches
source_url: https://github.com/MrCyjaneK/monero_c/issues/77
author: MrCyjaneK
assignees: []
labels: []
created_at: '2024-10-17T09:43:16+00:00'
updated_at: '2024-12-01T14:02:22+00:00'
type: issue
status: closed
closed_at: '2024-12-01T14:02:22+00:00'
---

# Original Description
- `0001-polyseed.patch`
  - Create a wallet in all languages supported by polyseed with and without seed offset, compare it to what cake wallet produces (store keys and seeds in test file)
  - This one is expected to fail in normalized languages, let's not worry too much about it for now
- `0002-wallet-background-sync-with-just-the-view-key.patch`
  - Create a new wallet
  - Setup background sync
  - close the wallet
  - open background-synced wallet in view only mode via password
  - close it
  - open original wallet
  - check for any errors
- `0004-coin-control.patch`
  - Check freezing/unfreezing, selecting preferred inputs, and transaction creation
- `0009-Add-recoverDeterministicWalletFromSpendKey.patch`
  - Check if created wallet has seed (and if it's correct)
- `0012-WIP-UR-functions.patch`
  - Test transaction creation via two wallets view only and offline


~~Some of these steps will require a synced wallet with balance, which is not ideal, as time to complete the tasks would take more and more time because of rising block height, so a solution that I propose is to create a wallet in advance, and use a server to automatically sync all the wallets in advance, then CI will only have to sync a few blocks.
Wallet files will be stored on a static web host, with a HTTP basic auth enabled, in addition to that wallets will be encrypted. This should be enough - considering the fact that no more than 0.01 will be in there.~~

Or more ideally - run them in docker in stagenet?

# Discussion History
# Action History
- Created by: MrCyjaneK | 2024-10-17T09:43:16+00:00
- Closed at: 2024-12-01T14:02:22+00:00
