---
title: monero-wallet-cli help description suggestions
source_url: https://github.com/monero-project/monero/issues/6791
author: garlicgambit
assignees: []
labels: []
created_at: '2020-08-30T17:59:17+00:00'
updated_at: '2022-05-25T10:06:18+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Change "wihch" to "which" in the `--extra-entropy` description.  
  
Add a description to `--command`. For example: "Run builtin command and exit" or "Run builtin wallet command and exit".  
  
Mention that `--create-address-file` will save the main address. Example: "Create a main address file for new wallets" or "Create file with main address for new wallet"  
  
Mention 'RPC' in all SSL RPC related options. Only `--daemon-ssl-allowed-fingerprints` and `--daemon-ssl` mention RPC.

# Discussion History
## jonathancross | 2020-11-11T17:24:58+00:00
Apparently the "wihch" typo was fixed here: https://github.com/monero-project/monero/commit/a3844e257eb6e032a5ad4d9595f7df15af64d7ac

# Action History
- Created by: garlicgambit | 2020-08-30T17:59:17+00:00
