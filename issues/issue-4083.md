---
title: Ledger/BIP-39 24 Word Phrase Support
source_url: https://github.com/monero-project/monero-gui/issues/4083
author: ghost
assignees: []
labels: []
created_at: '2022-12-07T18:34:28+00:00'
updated_at: '2022-12-07T18:34:28+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Currently on the GUI wallet you can only restore a wallet with a 25 word Electrum recovery seed. Many people use hardware wallets such as the Ledgers or metal backups, most of which use 24 word BIP-39 seed phrases. Unfortunately, there is currently no direct way to input the 24 word BIP-39 seed phrase into the Monero GUI wallet (eg if you lost your Ledger or if you simply use a metal/paper wallet which are more commonly available in 24 word formats).

Ledger has a standard and reproducible process for deriving 25 word Electrum recovery seeds from a 24 word BIP-39 seed phrase. If you wish to migrate to/use the Monero GUI wallet, you currently need to use the Ledger python script to convert the 24 word BIP-39 seed phrase to a 25 word Electrum recovery seed. This is an additional step and somewhat more technical than the GUI wallet or using the Ledger since it relies on a python script.

Ideally, one would instead be able to enter the 24 word BIP-39 seed phrase directly into the Monero GUI wallet. This would be a second option in addition to the 25 word Electrum phrase (and a third option once Polyseed gives 16 word phrases). The 24 to 25 word conversion code is already publicly available so this should be relatively simple to implement. This would help to improve security/simplicity for those using 24 word BIP-39 seed phrases.

Reference: https://github.com/LedgerHQ/app-monero/tree/master/tools/python

# Discussion History
# Action History
- Created by: ghost | 2022-12-07T18:34:28+00:00
