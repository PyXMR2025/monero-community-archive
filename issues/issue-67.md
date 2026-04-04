---
title: Multisignature implementation
source_url: https://github.com/monero-project/research-lab/issues/67
author: SarangNoether
assignees: []
labels: []
created_at: '2020-01-31T13:33:34+00:00'
updated_at: '2020-02-23T08:21:14+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
The [threshold ring signature](https://eprint.iacr.org/2018/774) paper by @b-g-goodell and I describes a provably-secure construction requiring a commit-and-reveal phase. The current multisignature implementation should be updated to reflect this construction properly.

# Discussion History
## UkoeHB | 2020-01-31T20:06:14+00:00
The implementation would also benefit from (based on the paper): robust key aggregation, and domain separated hashing with prefixes depending on application. It would also benefit from: aggregation signing instead of round-robin to reduce message rounds, and randomly sorting the output indices (currently disabled in code to ensure each participant uses the same indices [EDIT: this should be done by the transaction initiator, randomly shuffling the destinations before sending them out in a tx file to be signed, or maybe the shuffle_outs flag should be activated when it's the initiator] [EDIT2: based on my research, the destination list actually is randomly sorted by the original tx initiator, and then all other signers use that same randomly sorted list]).

## UkoeHB | 2020-02-14T05:02:43+00:00
From what I can tell in the current version partial key images are unsigned (see export_multisig() in wallet2.cpp), which means a cosigner could send a fake partial key image to another cosigner, then (e.g. in a 2-of-3) cooperate with a third signer to spend funds in the multisig wallet. The cosigner with doctored key image would not be aware those funds were spent, while believing he has the power to see when it happens.

UPDATE: There appears to be precedent for signing key images, namely in ReserveProofV1 where key images are signed with a 1-member ring signature. Applying this for partial key images would, I imagine, not be an extreme burden. See [this line of code](https://github.com/monero-project/monero/blob/39e18902763a5fd6f355294d8b135c8f5bc2ec99/src/wallet/wallet2.cpp#L11535).

# Action History
- Created by: SarangNoether | 2020-01-31T13:33:34+00:00
