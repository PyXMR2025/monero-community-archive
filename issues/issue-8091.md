---
title: 'bug: ''destinations'' field is empty when showing details of a multisig transaction
  with show_transfer'
source_url: https://github.com/monero-project/monero/issues/8091
author: erciccione
assignees: []
labels: []
created_at: '2021-11-28T14:01:44+00:00'
updated_at: '2024-03-24T08:22:20+00:00'
type: issue
status: closed
closed_at: '2024-03-24T08:22:20+00:00'
---

# Original Description
I made 2 transfers X and Y from a multisignature wallet.

The transactions have been relayed, but when using `show_transfer TXID_OF_X` and `show_transfer TXID_OF_Y`, the `destinations` field results empty in the CLI.

The weird thing is that if i check the transfers in the GUI, the destination address is shown for transaction Y, but not for transaction X, where i only see `Unknown recipient`.

# Discussion History
## rbrunner7 | 2022-01-07T14:14:59+00:00
I would guess that the destination gets only recorded in the wallet that finally submits the tx to the network, and that the destination is not part of the multisig info that gets exchanged later between the wallets to get them "synced" again. If correct result would be that only submitters of transactions have destination info, but transaction "starters" and "in-between-signers" (starting with 3/3 multisig) not.

I don't have no guess however about possible reasons for the difference between CLI wallet display and GUI wallet display.

## rbrunner7 | 2022-01-07T14:58:19+00:00
I did an actual experiment: The destination is set and visible in the wallet that submits the fully signed transaction to the network, but only until `import_multisig_info` is done: That command somehow destroys the info, so starting from then no wallet knows the destination anymore.

This is a bit unfortunate.

## rbrunner7 | 2022-01-07T16:57:22+00:00
I analyzed the problem.

The issue is that the wallet core code implements a quite drastic method to take in multisig info: It throws away blocks and everything it knows about transactions in those blocks in preparation and then resyncs. Because the destinations of transactions are a wallet-only info - they are not recorded in the blockchain - they got lost in this process.

It would not be trivial to improve this. I ask myself if the effort would be worth it, as in any case only the submitting wallet will have destinations anyway. (Distributing destinations as part of multisig sync info would be an even greater effort, probably too expensive / complicated.)

# Action History
- Created by: erciccione | 2021-11-28T14:01:44+00:00
- Closed at: 2024-03-24T08:22:20+00:00
