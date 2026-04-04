---
title: multisig fails for offline signing
source_url: https://github.com/monero-project/monero/issues/6324
author: burnside
assignees: []
labels: []
created_at: '2020-02-07T22:15:59+00:00'
updated_at: '2020-06-17T02:04:29+00:00'
type: issue
status: closed
closed_at: '2020-06-17T02:04:29+00:00'
---

# Original Description
Version 0.15.0.1 (and some previous)

I have been trying to build a system to sign multisig monero transactions from a 100% offline wallet.  Unfortunately even after multiple rounds of export/import multisig info, I have not been able to successfully execute an offline transaction.

Even in 2 of 2, what should be a simple flow:

Online wallet refresh
Online wallet export
Offline wallet import
Offline wallet refresh
Offline wallet export
Online wallet import
Online wallet refresh
Online wallet create transaction

Fails reliably with "LR not found for enough participants" in the create transaction process.

The size of the export coming out of the offline wallet being approximately 2/3 the size of the export coming out of the online wallet.

Then if instead the offline wallet is connected to an up to date monerod and allowed to sync, suddenly it's export size grows to match that of the online wallet, and the same process functions as expected.

There seems to be some metadata that is required that is not flowing from the online wallet to the offline wallet and back again for the online wallet to be able to reliably create a transaction after importing the data from an offline wallet.

I have tried many other permutations of the flow, refreshing before and after imports, creating the transaction before and after imports or before and after exports.  The only thing that seems to get it going is allowing the offline wallet to sync the blockchain, then doing the export.

Am I missing something?  Or do I really need to copy the entire blockchain to my offline wallet with each transaction?

# Discussion History
## moneromooo-monero | 2020-02-07T22:51:24+00:00
Importing multisig transactions causes a wallet to rescan the chain with the new knowledge it got from the files it gets from other signers. It might be theoretically possible to do this without having to rescan, by keeping "partial" output data, not sure offhand. But you can stop trying now, it will not work with the current code.


## burnside | 2020-02-08T01:02:54+00:00
@moneromooo-monero Thank you, I'm glad I'm not just doing it wrong.

In summary, a completely offline wallet is not currently feasible without a sneakernet of the entire chain?

## moneromooo-monero | 2020-02-08T13:10:49+00:00
Correct for multisig.

# Action History
- Created by: burnside | 2020-02-07T22:15:59+00:00
- Closed at: 2020-06-17T02:04:29+00:00
