---
title: Multi-index Triptych
source_url: https://github.com/monero-project/research-lab/issues/66
author: SarangNoether
assignees: []
labels: []
created_at: '2020-01-31T13:24:31+00:00'
updated_at: '2020-02-12T02:11:03+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
The [Triptych](https://eprint.iacr.org/2020/018) proving system is a `d`-LRS-type construction with functionality similar to that of MLSAG or CLSAG, permitting proofs on multiple components of key vectors in a set while hiding the signing index. The version specified in the preprint can be integrated into the Monero transaction protocol, requiring a separate proof for each spent input and using commitment offsets to assert transaction balance.

However, we've investigated an alternate Triptych construction (in [math](https://github.com/SarangNoether/skunkworks/blob/triptych/paper/multi.tex) and [code](https://github.com/SarangNoether/skunkworks/tree/triptych/triptych-multi)) that permits signing for multiple indices in the same list simultaneously within the same proof, while also taking care of balance assertion.

However, the soundness of this extension to Triptych is unknown. If shown to reduce to a known cryptographic hardness assumption, it would be useful due to its scaling benefits.

# Discussion History
## UkoeHB | 2020-02-12T01:51:36+00:00
Would this imply all inputs are at the same index? IIRC RCTTypeFull was never really used much due to that problem.

## SarangNoether | 2020-02-12T02:11:03+00:00
No, the opposite. There is a single list of commitments, and a single proof is used for all indices in the list corresponding to all signers at once.

# Action History
- Created by: SarangNoether | 2020-01-31T13:24:31+00:00
