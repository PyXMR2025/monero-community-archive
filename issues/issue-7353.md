---
title: Is the ability of InProofV2 in the Zero to Monero document overstated?
source_url: https://github.com/monero-project/monero/issues/7353
author: ghost
assignees: []
labels: []
created_at: '2021-01-27T16:37:27+00:00'
updated_at: '2022-09-11T21:50:49+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Here is the document. See the bottom of page 79 onwards for InProofV2.
[https://web.getmonero.org/library/Zero-to-Monero-2-0-0.pdf](url)

The document correctly outlines how Outproofs can be 'faked' at the bottom of page 78. To bring others up to speed, one can take a stealth address:

`P = H(rA) + B`

and rearrange like:

`P - H(rA)G = B`
[H is a scalar derivation, G is the ec-basepoint, r is the tx private key, `A(,a)` and `B(,b) `are the public (private) view and spend keys (of the owner) respectively]

and plug some arbitrary A' into the left hand side and derive a corresponding B', such that A' and B' still satisfy the original stealth address P. One then presents `(A', B', r)` to the verifier who then naively 'confirms' that the Monero address `(A',B')` matches the output. For completeness it's worth saying that despite procuring such an `(A', B')` the 'faker' does not have access to the private counterpart of B' (=b'), and therefore cannot spend the output. 

The document then goes on to specify another proof called 'InProof V2' which is meant to be a proof of the other side of the sender-receiver shared secret `rA =aR`; that is, the prover is supposed to 'prove knowledge' of the private view key for the Monero address that owns a particular output. However, again we are permitted to choose some arbitrary A' (and B') to satisfy the stealth address in question. 

The Z2M document makes the following claim however:

> Prove ‘full’ ownership with the one-time address key:
...an InProof shows a one-time address was constructed with a specific address (except with
negligible probability)

and then later details the actual way of fully proving ownership, which has it's own issues:
> Proving ownership, once an InProof is complete, is as simple as signing a message with the spend
key.

My contention is that the statement 

> an InProof shows a one-time address was constructed with a specific address (except with
negligible probability)

is incorrect, as any A',B' that satisfy P are equal candidates at the InProof stage; an InProof without a corresponding signature means nothing. It might be worth migrating the signature step into the actual proof step-by-step guide (and perhaps the code), beings as it's so critical.

All the best,

Chris


# Discussion History
## UkoeHB | 2021-01-27T17:41:47+00:00
Chris,

I see what you're saying... without a proof on `K^s`, it could be any random curve point. In other words you could misrepresent ownership of a single output with a fake InProofV2 (although the address couldn't own any other outputs except with negligible probability).

Even with a proof/signature on `K^s`, it is possible for the sets of outputs 'owned' by two addresses to overlap in one output (as provable using InProofV2s, which at least lock down the addressing scheme), if the second address is derived from `k^o` in that output. In other words, randomly generate `k'^v`, and derive `k'^s` from `k'^s = k^o - H(k'^v*rG, t)`. This key pair `k'^v, k'^s` can be used to receive new outputs. I don't think there is a way to detect this overlap trick.

Anyway, it seems InProofs are due for an upgrade to include signatures on the spend key.

## UkoeHB | 2021-01-28T13:38:43+00:00
@ChrisCharrison the overlap trick only works for outputs you actually own, because then you know the private keys in `p - H(rA) = b` and can compute `p - H(rA') = b'` then use `a', b'` as a new view/spend pair.

## ghost | 2021-01-28T18:04:43+00:00
That's absolutely right @UkoeHB . For those reading the full proof of why this works is:

`P - H(rA)G = pG + H(rA)G`   writing both terms as scalar multiplication
`pG - H(rA)G = (p -H(rA))G`  because point addition is additive 
`(p-H(rA))G = bG`                  as before
`=> p-H(rA) = b`

You can trivially find multiple pairs of `(a', b')` that satisfy P if you own the output (and therefore know what the output private key `p` is). We actually sign outputs with the _output_ private key and not the spend key when we sign a transaction. You can do an valid inproof an then sign afterwards with any spendkey that fits the equation for P, but that only proves that you able to spend the output because you have by proxy proven that you know the output private key. By no means are you proving that your output belongs to a certain XMR address `(A,B)` just by signing a message with a spendkey. @UkoeHB surely this means that we simply never know who an output truly belongs to? Because once you can compute multiple `(a',b')` and that allow you to reach the same output private key, you could claim plausible deniability over which original `(a,b)` you used to achieve that output private key the very first time you computed it?



## UkoeHB | 2021-01-28T18:22:20+00:00
@ChrisCharrison it is not quite that severe. If your address `(A', B')` owns more than one output (as shown with InProofs), then any outputs after the first must have been intentionally sent to that address by the sender.

The importance of InProofs is, given _some specific publicly known address_, you can demonstrate the full set of outputs owned by that address. After all, you can have any number of private addresses which own any number of outputs. I'm not sure what advantage you would get in terms of plausible deniability... whether it's one address or another shown to own the output (or multiple), in the end it is _you, the address holder_ who really owns the funds.

This overlap trick is only useful in niche cases where you want to demonstrate ownership of a single output without revealing which address the sender used to construct it with (but you don't want the verifier to realize they are being tricked).

## ghost | 2021-01-28T19:06:56+00:00
Yes agreed. That is what I meant to get across - there is no unique private spendkey that solely owns the right to spend a given output, and one person can hold many of those keys. It's a subtle but interesting feature of the Monero cryptography. Many people just think of multiple addresses being able to spend the same output because they have different view keys but share the same spend key. Well maybe most people out there don't even know about that possibility lol. To comment on your final sentence (and why I asked about all this in the first place) - we run a less private fork of Monero and for accounting/regulatory purposes it's much desirable to know exact addresses to know the exact flow of tokens, and not have any scope for that kind of trickery. Thanks for the discussion @UkoeHB. 

## UkoeHB | 2022-09-11T21:18:04+00:00
I looked at this again. `InProofV2`s are checking amount commitments the same way `OutProofV2`s are. If an amount commitment is successfully checked, then its output must be spendable by the `Kv, Ks` pair used to make the `InProofV2` (if it is spendable at all under the standard address rules). Therefore, it shouldn't be necessary to sign on `Ks` in the `InProofV2`. If you want to prove that you can spend all the outputs mentioned in inproofs, then you need to sign on all your `Ks`s.

To clarify: `InProofV2` and `OutProofV2` are currently only 'indirectly' checking amount commitments and nominal spendkeys. They return an amount equal to the total amount owned by the target address, which is nonzero if that address owns any of the outputs in the transaction that is the subject of a proof.

# Action History
- Created by: ghost | 2021-01-27T16:37:27+00:00
