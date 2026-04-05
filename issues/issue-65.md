---
title: '[Feature] FCMP++ key image proofs without spend knowledge'
source_url: https://github.com/seraphis-migration/monero/issues/65
author: jeffro256
assignees: []
labels: []
created_at: '2025-07-08T22:31:14+00:00'
updated_at: '2025-07-08T22:31:23+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
# FCMP++ key image proofs without spend knowledge

## Problem

The [Carrot key hierarchy](https://github.com/jeffro256/carrot/blob/master/carrot.md#52-new-key-hierarchy) introduces [outgoing view keys](https://github.com/jeffro256/carrot/blob/master/carrot.md#224-full-view-only-tier) (OVKs): a wallet tier which allows for calculating of key images and thus locating of outgoing transactions without the ability to spend. However, there is not yet a way to prove that a key image is associated to a one-time address without full knowledge of $x, y$ s.t. $O = x G + y T$. Anyone who can calculate key images by themselves necessarily knows $x$, however, it should be possible to partially hide knowledge of $y$, but still convince someone that a key image is associated to a one-time address.

## Requirements

We want a key image proving system which:

* Allows the Carrot *generate-image* wallet tier to prove key image association without interaction/knowledge of $k_{ps}$
* Does not allow "account-based" correlation if adversary is provided with 2 key image proofs
* Does not leak $k_{gi}$ to a quantum adversary
* Is reasonably performant

## Solution

Note: See [this section](https://github.com/jeffro256/carrot/blob/master/carrot.md#52-new-key-hierarchy) of the Carrot spec for more information on how account secrets and addresses are derived in the Carrot key hierarchy.

Entity `S` with knowledge of $k_{ps}$ can generate "re-randomized account spend pubkeys" by sampling $k_r \in [0, ℓ)$ and calculating $K^r_s = (k_{ps} + k_r) T$. Then, they can generate a classic univariate Schnorr proof-of-knowledge $\Omega_{rs}$ over $T$. They can do this as many times as they like, then send the proof $\Omega_{rs}$ and keys $k_r, K^r_s$ to entity `P`.

Then, given one-time address $O$, and key image $L$, entity `P` can then form a [*Generalized* Schnorr proof](https://eprint.iacr.org/2009/050.pdf) (GSP) which proves the following relations for some $k_j, x, y$:

* $O = k_j * K^r_s  + x * G + y * T$
* $L = x * H^2_p(O)$

We can write this as the matrix:

```
[K_rs, G, T]
[   0, I, 0]
```

Which has input; `[k_j, x, y]`, and output: `[O, L]`. Here, $I = H^2_p(O)$.

Let's say that entity `P` has knowledge of $k_{gi}$ and $s_{ga}$, and that some one-time address $O$ was addressed to index $j$ with sender extensions $k^g_o$ and $k^t_o$. `P` can calculate $k^j_{subscal}$ (derivation left as homework for reader). Then they can calculate $k_j = k^j_{subscal} / k_r$, $x = k_{gi} * k^j_{subscal} + k^g_o$, and $y = k^t_o$. They then then plug in $k_j, x, y$ to construct a GSP $\Omega_{gsp}$.

Now, if entity `P` wants to prove key image association to entity `V`, they can do so by sending $O, L, K^r_s, \Omega_{rs}, \Omega_{gsp}$. `V` would then verify both $\Omega_{rs}, \Omega_{gsp}$ with the corresponding inputs.

## Soundness

**TODO**: flesh out more

Since `V` can verify that $K^r_s$ is univariate over $T$, and that the only opening over $G$ is in $x$, and that that $x$ is the discrete log between $I$ and $L$, this should be sound.

## Quantum forward secrecy

**TODO**

## Drawbacks

This can only be done a finite number of times before `P` runs out of unique $(K^r_s, k_r, \Omega_{rs})$ tuples and either A) interaction with `S` is needed, B) account association over multiple proofs is possible, or C) `P` refuses to make more key-image proofs.

# Discussion History
# Action History
- Created by: jeffro256 | 2025-07-08T22:31:14+00:00
