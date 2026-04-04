---
title: Dummy transaction inputs
source_url: https://github.com/monero-project/research-lab/issues/96
author: tevador
assignees: []
labels: []
created_at: '2022-01-06T18:15:46+00:00'
updated_at: '2024-05-15T19:40:19+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
This is not a fully thought out proposal, just an idea I had today.

It's an extension of the [idea](https://github.com/monero-project/research-lab/issues/95#issuecomment-1004985047) by @paulshapiro to mandate all transactions to have 16 outputs.

The holy grail of fungibility would be for all transactions to look the same. We can thus extend the idea and mandate all transactions to have the same number of outputs *and* the same number of inputs. For practical reasons, the number of tx inputs would have to be greater than 1 to allow for consolidation of inputs.

However, this would mean that wallets that only own 1 UTXO would be unable to construct a transaction because the consensus protocol requires that each input spends a previous output in the blockchain (by publishing a unique key image).

Turns out that the RingCT protocol can support dummy inputs if we make the following consensus change:

* All transaction input rings implicitly include the pseudo-amount commitment `C` as one of the ring keys.

Normally, the amount commitment has the form of `C = r G + v H`, where `r` is a blinding factor and `v` is the amount being spent. Since nobody knows the discrete logarithm of `H`, it is impossible to sign with this commitment **unless** `v == 0`. In that case, an input can be constructed which references only decoys from the blockchain and in fact "spends" a zero amount dummy input. Such dummy inputs would be indistinguishable from real spends.

Besides the obvious fungibility benefits of having all transactions of exactly the same size, this would also allow transactions to easily hide cross-ring correlations, e.g. all transactions could always reference some decoys from the same block or the same transaction in multiple rings etc.

(Unfortunately, the dummy input idea doesn't work with Seraphis AFAICS.)





# Discussion History
## tevador | 2022-01-07T10:38:09+00:00
There is a modification that might also work with Seraphis.

In seraphis, the output keys `K` and amount commitments `C` have the forms:
<code>K = a X + b U</code>
<code>C = r G + v H</code>
where `X, U, G, H` are  4 different generators. The reference set consists of tuples `(K,C)` referring to previous outputs in the blockchain.

The sender publishes an e-note image `(K', C')` and a linking tag <code>K<sup>\~</sup></code>:
<code>K' = t<sub>1</sub> G + a X + b U</code>
<code>C' = (t<sub>2</sub> + r) G + v H</code>
<code>K<sup>\~</sup> = (b / a) U</code>
where <code>t<sub>1</sub></code> and <code>t<sub>2</sub></code> are random masks to hide which output is being spent.

To support dummy inputs, three changes are needed:

* redefine output keys as <code>K = a G + b U</code> (using the generator `G` instead of `X`)
* redefine the masked key as <code>K' = K + t<sub>1</sub> X</code> (using the generator `X` for masking)
* implicitly include the tuple `(C' + U, E)` in the reference set, where `E` is the identity element

To construct a dummy input, the sender would generate two random masks <code>t<sub>1</sub></code> and <code>t<sub>2</sub></code> and publish:
<code>K' = t<sub>1</sub> X + t<sub>2</sub> G + U</code>
<code>C' = t<sub>2</sub> G</code>
<code>K<sup>\~</sup> = (1 / t<sub>2</sub>) U</code>

The sender can construct a valid membership proof that will validate with any set of blockchain decoys. The input amount is zero as the spent e-note is using the commitment `E = 0 G + 0 H`.

With a fixed number of inputs, it would be best to use Seraphis-Merge, which combines all input proofs into one and is more space efficient.

Edit: Redefining amount commitments is not possible for backwards compatibility.

## UkoeHB | 2022-01-07T16:42:34+00:00
Surprisingly, I think that would work. However it would be incompatible with Seraphis-Squashed (I don't think there is any way to have dummy inputs that work with Seraphis-Squashed).

## LocalMonero | 2022-01-09T19:59:36+00:00
Would dummy inputs that are indistinguishable from real inputs be able to solve the 10-block-lock problem? After all, it's the invalidation of transactions through real double-spent inputs within the 3-5 block danger zone that's the primary issue, isn't it? With dummy inputs we can be sure that they won't be double spent.

## MajesticBank | 2022-03-26T11:11:50+00:00
> Surprisingly, I think that would work. However it would be incompatible with Seraphis-Squashed (I don't there is any way to have dummy inputs that work with Seraphis-Squashed).

Would dummy inputs make spending of many recent inputs have less impact on privacy?

## UkoeHB | 2022-12-13T00:04:00+00:00
Update on the dummy outputs mentioned here: dummy tx outputs would reduce the number of times the average enote is referenced as a ring member, because the number of tx inputs would become much lower on average than the number of outputs + dummies. Adding in dummy inputs would change that equation.


## kayabaNerve | 2023-06-24T07:30:40+00:00
I don't believe the above described scheme is secure. Prover-selected t2 allows the prover to burn any linking tag they're aware of, breaking any scheme which reveals the relevant view key.

With an arithmetic circuit based membership, it'd be possible to use a properly selected arithmetic hash function to generate an uncontrollable 0-amount enote, then let the prover select that or a legitimate member *with no modifications to Seraphis*. Unfortunately, it'd decently increase the proof time for all proofs.

## tevador | 2023-06-24T14:37:08+00:00
> I don't believe the above described scheme is secure. Prover-selected t2 allows the prover to burn any linking tag they're aware of, breaking any scheme which reveals the relevant view key.

CMIIW, but the Seraphis linking tag is `(b/a) U`, where `b` is the secret spend key and `a` is the secret view key (it's actually the sum of several keys linked to the view key). In order to hijack a linking tag, you'd need to know both `a` and `b`,  otherwise finding `t2` such that `(1/t2) U = (b/a) U` involves solving the DLP. Someone who knows `b` can just spend the output directly, so I don't think this allows for any new attacks.

## kayabaNerve | 2023-06-26T19:03:57+00:00
That would be if the view key allows calculation via `bU * a.invert()`, not `(b * a.invert()) * U` as I assumed from my brief reading of the above. That would prevent normalization as described here, voiding my concerns. Thanks for clarifying. I am definitely not up to date on Seraphis.

If so, then it should be much more feasible to support this with an arithmetic circuit membership proof. At worst, for a 4-component enote (one being the amount), it'd be 3 DLog PoKs (if `amount == 0` doesn't break anything). By fixing the U component to 1, it'd be just 2 DLog PoKs. Ideally, one other could also just be fixed, getting this down to one other DLog PoK.

A DLog PoK isn't horribly cheap. It's < 256 arithmetic circuit gates though. The bigger concern would be around the power of two padding and overall circuit alignment. It's definitely an option on the table, without any modifications to Seraphis (if prior stated condition is acceptable).

## tevador | 2024-05-10T07:37:36+00:00
Here is how dummy inputs might work with the current FCMP proposal:

Each transaction would have `d = f(n)` dummy inputs where `f(n)` is some function of the total number of inputs `n`. One option is `f(n) = n - 1`, which completely obscures the number of real inputs.

The transaction would contain a list of `d` dummy keys `K* = x* G + y* T`, where `x*` and `y*` are random scalars drawn by the person constructing the transaction.

When verifying a transaction, we would take the tree at the reference block and for each dummy key, append the tuple <code>(K*, I<sub>dummy</sub>, G)</code> to the tree. Here <code>I<sub>dummy</sub></code> would be a fixed base for dummy key images (this is safe because there are no related dummy keys). The membership proofs of the transaction would be verified with the modifed root. Note that the dummy keys only modify the root for one transaction, not the whole network.

When spending a dummy input, the input amount would always be zero because `G = 1 G + 0 H`. Spending a dummy input would be indistinguishable from spending a real input, even to an adversary who can solve the discrete logarithm problem (perfect forward secrecy).

Costs:

* `32*d` extra bytes in each transaction (for the dummy keys)
* Verifiers need to perform one `tree.grow` operation for each transaction.

Edit: common base for dummy key images as proposed by @kayabaNerve. Amount commitment changed from `O` to `G` because the point at infinity is invalid for the tree proof.

## chaserene | 2024-05-11T20:19:48+00:00
> mandate all transactions to have the same number of outputs and the **same number of inputs**.

(emphasis mine)

@tevador is my understanding correct that in such a regime, unless you have a mandated number of enotes whose total value covers the amount you want to transact + fee, you have to create "join" transactions and, as long as transactions can't refer to information in the same block they're confirmed in, each "join" round will impose an n-block delay on your originally intended transaction?

## kayabaNerve | 2024-05-13T05:15:10+00:00
Aggregating TX inputs is already necessary (and already has such side effects) under the current Monero. It just has a rather high aggregation limit (200 something inputs in practice) where this would presumably set a more reasonable limit (4-8).

## tevador | 2024-05-13T13:02:54+00:00
With the current FCMP proposal, the aggregation limit would be around 64 inputs (limited by max tx size). If we wanted to adopt dummy inputs, we could at least quantize the input counts to 2, 4, 8, 16, 32 and 64. If we similarly restricted the number tx outputs to 2 or 16, we would effectively limit the possible number of transaction shapes from several thousand to just 12.

## chaserene | 2024-05-13T20:04:58+00:00
based on tevador's comments elsewhere, I presumed the plan with this issue is to have 2/2 only (which is a stark UX difference from 200-in max).

discretizing the input count as 2^n and making the output count binary sounds quite reasonable. if it weren't for anti-n-block lock solutions (which create enotes in advance like PocketChange), I wouldn't even hold 16-out as necessary.

## kayabaNerve | 2024-05-13T21:00:47+00:00
If 2/2 only, the same aggregation commentary applies.

@tevador We can save a hash to point if we have all dummy keys using a single generator. That enables related key attacks yet there aren't related key attacks for the dummy input which is presumed uniformly sampled by the TX creator.

## tevador | 2024-05-15T19:39:03+00:00
> We can save a hash to point if we have all dummy keys using a single generator. That enables related key attacks yet there aren't related key attacks for the dummy input which is presumed uniformly sampled by the TX creator.

Good idea. We could save not only a hash-to-point, but also a scalar multiplication in the Pedersen hash. Because both `I.x` and `C.x` are constants, we could precompute `I.x H_i + C.x H_j` for all possible sibling positions.

# Action History
- Created by: tevador | 2022-01-06T18:15:46+00:00
