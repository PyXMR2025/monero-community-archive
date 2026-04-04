---
title: Proof data storage
source_url: https://github.com/monero-project/research-lab/issues/64
author: SarangNoether
assignees: []
labels: []
created_at: '2020-01-31T13:09:41+00:00'
updated_at: '2022-12-13T00:51:05+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
It's possible to storage data in a Bulletproof range proof, under particular trust assumptions. In particular, knowledge of a PRNG seed used for random element generation can be used to store 32 bytes of arbitrary data; however, this allows for the brute-force recovery of all Pedersen values used in the proof by any entity that knows the seed. For a proof consisting of exactly one Pedersen commitment, the inclusion of another 32 bytes of data is possible, but this leaks the Pedersen mask. Storage of data should therefore be intended only for use by the prover.

Similarly, it's possible in Triptych to store 64 bytes of arbitrary data per proof in a way that leaks the signing index to a PRNG seed holder.

# Discussion History
## boogerlad | 2021-07-13T19:47:52+00:00
Is storing 64 bytes of arbitrary data still possible with Triptych? If so, couldn't this be used to replace `tx_extra`?

## SarangNoether | 2021-07-13T21:15:18+00:00
Yes, a Triptych proof can store 64 bytes of arbitrary data using a seeded PRNG.

## boogerlad | 2021-07-14T00:23:03+00:00
Is this a "bug" or a "feature"? That is, will the ability to store arbitrary data eventually be removed? I can think of some pretty nifty use cases.

## SarangNoether | 2021-07-14T00:27:38+00:00
The network can't detect it, so it's not possible to "remove" this feature. It's entirely up to client software to embed and/or recover this data.

## UkoeHB | 2022-12-13T00:50:58+00:00
Here is a paper about inserting a communication channel via steganography: https://ieeexplore.ieee.org/abstract/document/9356584

# Action History
- Created by: SarangNoether | 2020-01-31T13:09:41+00:00
