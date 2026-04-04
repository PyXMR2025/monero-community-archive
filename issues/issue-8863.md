---
title: get_spend_proof not working for offline wallet rpc
source_url: https://github.com/monero-project/monero/issues/8863
author: mmbbee
assignees: []
labels:
- proposal
created_at: '2023-05-18T10:24:24+00:00'
updated_at: '2023-12-09T06:16:45+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
At the moment, a `monero-wallet-rpc` setup with `offline=true` is unable to generate a SpendProof (`get_spend_proof`), because the code tries to reach out to a daemon node, which is not preset for offline signers

@moneromooo-monero has suggested we should be able to remove the [code calling out to the deamon](https://github.com/monero-project/monero/blob/master/src/wallet/wallet2.cpp#L10855-L10856), and then spend proofs could work in a segregated watch-only / offline signing setup 

# Discussion History
## moneromooo-monero | 2023-05-18T10:41:30+00:00
To expand, the wallet requests pruned tx data (which a wallet already has, though I'm not sure this is passed to the cold wallet), and uses just the vin (which the cold wallet almost certainly has). So the call seems superfluous.

## DangerousFreedom1984 | 2023-07-02T13:54:46+00:00
Is there another method to get the spend_proof other [this](https://github.com/monero-project/monero/blob/master/src/wallet/wallet2.cpp#L11119) one that I'm not aware of? Otherwise it seems impossible to have an offline (not connected to the node) wallet (rpc-wallet, cli-wallet or any wallet) to get the spend_proofs. The node can be offline though (not syncing the new blocks).
Basically we need to use the node to get the public keys of the ring members. This information could be stored offline though I dont believe it is by default.

# Action History
- Created by: mmbbee | 2023-05-18T10:24:24+00:00
