---
title: Hidden timelocks
source_url: https://github.com/monero-project/research-lab/issues/65
author: SarangNoether
assignees: []
labels: []
created_at: '2020-01-31T13:19:58+00:00'
updated_at: '2020-06-07T16:29:40+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
The [DLSAG](https://eprint.iacr.org/2019/595) preprint specifies a method for applying hidden timelocks to its dual-key output construction.

Even without DLSAG or its intended non-interactive refund mechanism, it's possible to integrate hidden timelocks into the Monero protocol. Outputs come equipped with a separate Pedersen commitment to a lock time (using a standardized time format, either blocks or timestamps). Ring signatures are extended to include another key vector dimension. Signers produce an auxiliary commitment to the same time, but with a random mask, and include this offset as part of each ring member in signatures. Then, the signer chooses a random (not necessarily uniform) auxiliary time value between the lock time and the current time, and includes this in the clear; it generates a particular range proof demonstrating that the difference between the auxiliary time value and the (hidden) time value in the auxiliary commitment is positive and range-limited.

It's not feasible to include this functionality using MLSAG signatures, since this would require the addition of a separate set of scalars that scales with the ring size. However, including it with CLSAG signatures adds only a single group element. Adding them to Triptych would also add a single group element. There is an added computational complexity for the verifier (and prover) that, at first estimate, would negate the time savings from an MLSAG-CLSAG migration.

This functionality could be mandatory or optional, depending on the risk assessment.

# Discussion History
## UkoeHB | 2020-01-31T19:59:19+00:00
Time locks are especially cool since they rely on concepts already present in Monero's transaction protocol.

1. Given a commitment to lock time `t` (the tx outputs can be spent once `real_time >= t`) with random mask `x`, present in it's original transaction: `C(x, t) = xG + tH`
2. Create a new commitment to the same thing (a 'pseudo timelock commitment') with new random mask `y`, in the new transaction trying to spend an old output locked to time `t`: `C(y, t) = yG + tH`
3. Sign in a ring the commitment to zero, using the decoy inputs' timelock commitments `C(x, t)'` for other ring members: `C(x, t) - C(y, t) = (x - y)G`
4. Pick a time `t'` where the transaction will be spent (or later), and calculate (`t'` is communicated in cleartext for verifiers):  `P = t’H - C(y,t)`
5. Do a range proof on `P`, since if `t' - t` is negative it will roll over and not fit in the legitimate range.

# Action History
- Created by: SarangNoether | 2020-01-31T13:19:58+00:00
