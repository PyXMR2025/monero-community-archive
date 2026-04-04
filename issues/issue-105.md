---
title: Consider Switch commitments for future supply security
source_url: https://github.com/monero-project/research-lab/issues/105
author: tevador
assignees: []
labels: []
created_at: '2022-08-25T22:27:08+00:00'
updated_at: '2022-09-06T03:01:51+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Monero currently uses Pedersen commitments to hide real transaction amounts. The commitments have the form of `C = r*G + v*H`, where `r` is the blinding factor, `v` the amount and `H` is a random generator with an unknown discrete logarithm with respect to `G`.

Pedersen commitments are perfectly hiding, but only computationally binding. That means that even an adversary with an infinite computational power cannot reveal the amount `v` that was hidden in the commitment.

On the other hand, if the discrete logarithm of `H` is ever found, the commitment scheme is no longer binding and an adversary can open the commitment to any monetary value, effectively creating undetectable inflation.

We should consider adopting the idea od Switch commitments<sup>[1]</sup>, which instead use perfectly *binding* ElGamal commitments with two verification modes:

1. In the "partial" verification mode, they behave exactly like current Pedersen commitments and can use Bulletproofs(+) to prove the amount range.
2. They can be switched to "full" verification in the future, ensuring that old commitments cannot be open to arbitrary monetary value even if the discrete log of `H` is broken.

Thanks to the "partial" verification mode, there would be absolutely no performance cost of using switch commitments for now. The size cost is one additional curve point `D = r*J` per commitment. This curve point can be completely ignored until we switch to the full verification mode in the future (which will also require a different range proof algorithm).

A side-effect of the perfect bindingness of the ElGamal commitment is that a future computationally unbound adversary can unmask transaction amounts, which is arguably a better outcome than undetectable inflation. People who would prefer unconditional privacy can set `D` to a random curve point. This will keep their commitments perfectly hiding, but will make their outputs unspendable with full verification.

A good time to adopt switch commitments would be with Seraphis. The reason is that when the full verification is activated in the future, old RingCT outputs (with just the Pedersen commitment) would become unspendable. This could be done just by disabling the v2 -> v4 output migration path.

[1] https://eprint.iacr.org/2017/237.pdf

# Discussion History
## UkoeHB | 2022-08-25T22:45:27+00:00
This may not be compatible with the Seraphis squashed enote model.

## tevador | 2022-08-26T07:05:38+00:00
> A side-effect of the perfect bindingness of the ElGamal commitment is that a future computationally unbound adversary can unmask transaction amounts

I realized that this is a bigger issue for Monero because unmasked amounts also break ring signatures (unless some of the decoys happen to have the same amount).

This can be prevented by hiding the ElGamal commitment `(C', D')` behind a hash and using the hash to derive the Pedersen blinding factor:

`C' = r'*G + v*H`
`D' = r'*J`
`r = r' + H(C', D')`
`C = r*G + v*H`

V3 outputs would use the derived Pedersen commitment `C`. When the full veification is activated, the output migration v3 -> v4 would have to leak the output being spent by revealing `(C', D')` with the new range proof (verifiers can check that `C' = C - H(C', D')*G` to make sure the ElGamal commitment is correct).

**Advantages**
* No verification overhead.
* No size overhead.
* Historical amounts stay hidden even if the DLP is broken.
* Unspent v3 outputs can be migrated without the risk of supply inflation.

**Drawbacks**
* Some extra calculations when creating a v3 output (one extra commitment, one hash and one scalar addition).

I think the tiny drawback is more than worth it.

> This may not be compatible with the Seraphis squashed enote model..

It has no effect on the proof construction. You use the switch commitment the same way you would use a normal Pedersen commitment until the full verification is needed in the future (then you would need a modified range proof and membership proof).

## tevador | 2022-08-31T18:15:48+00:00
Here is an even more efficient scheme:

1. Select a random mask `r'`
2. Calculate `D' = r'*J`
3. Calculate `r = r' + H(D')`
4. Return the Pedersen commitment `C = r*G + v*H`

This saves one commitment calculation compared to the previous scheme.

When the "switch" happens, spent outputs will have to reveal `D'` and an unconditional range proof. Verifiers can calculate `C'= C - H(D')*G` and check the range proof against the ElGamal commitment `(C', D')`.
~~Forging the commitment requires breaking the preimage security of the hash function, which is infeasible even for a quantum computer if the hash function is at least 256-bit.~~ See a security estimate below.

## kayabaNerve | 2022-08-31T20:08:00+00:00
So the more efficient scheme has the benefit of preserving the perfectly blinding property, yet can be converted to a perfectly binding scheme for the cost of a scalar add, a scalar mul, and a hash (solely on the wallet side), without bandwidth nor integration difficulties. I appreciate that.

The part I don't appreciate is this doesn't solve the underlying problem IMO. Given a quantum adversary, or the likelihood of a near quantum adversary, Monero will have to ban all RCT outputs. This proposal allows Seraphis outputs to be migrated after the fact without Monero's integrity being compromised.

The reason for this would be to allow Monero to be a secure, long-term store of value without a liveliness requirement which I appreciate. While this already isn't possible for RCT outputs due to the inflation possible, it is possible for pre-RCT outputs and Seraphis outputs, without risking inflation. The issue is that it's still not possible for pre-RCT outputs and Seraphis outputs as while it'd be secure for the Monero protocol, it'd be insecure from the perspective of the users. Their keys could still be compromised enabling theft of their funds. Monero, as a protocol, would be enabling this despite knowing it's a risk AND would be giving users a false belief they can migrate whenever when the clock is ticking.

I'd rather Monero NOT enable a quantum adversary to commit theft, and NOT communicate to users they can migrate whenever in a race condition setting. When we have PQ cryptography, and the likelihood if a quantum adversary is high enough, I'd rather ban all outputs, clearly establishing the requirement to spend them for safety and not enabling theft. While aggressive, it's the only actually secure method.

Alternatively, spend authorization keys may be augmentable with a PQ-secure scheme, just like we're discussing augmenting commitments here.

Side note: Why H(D')? Why nor H(r')? If D' is factored, v can be brute forced. We can save a scalarmul by removing the privacy of this scheme, which is only intended to be used in scenarios where privacy can already be broken. I guess its private to the majority for longer, and the scalarmul is cheap enough?

## tevador | 2022-08-31T21:01:46+00:00
> Their keys could still be compromised enabling theft of their funds.

Actually, this scheme also protects from theft to a certain degree. See the security proof below.
Of course, a quantum adversary will be able to break the Diffie-Hellman key exchange if they learn the original address the output was sent to.

> I'd rather ban all outputs, clearly establishing the requirement to spend them for safety and not enabling theft

I'm sure that Monero will quite strongly recommend users to migrate to a new scheme as soon as there is evidence that the DLP might be broken in the future. Switch commitments just give users *the chance* to migrate later instead of burning all unspent outputs.

Also there is some chance that the discrete log of the generator `H` might be broken by classical means before quantum computers are available. If I had a supercomputer that can break one discrete log in 10 years, I would most certainly choose to break `H` instead of some random user's private key.

> Why H(D')? Why nor H(r')?

The quantum adversary will be able to learn the amount hidden in the commitment, but it doesn't mean we need to tell everyone what the original amount was. What if an adversary *only* knows the discrete log of `H`, but is unable to crack arbitrary keys? The ElGamal commitment scheme still offers computational privacy and it's intended to be activated well before quatum computers can break DLP.

### Security proof sketch

Let's assume a quantum adversary who can easily break DLP.

Given an amount commitment `C` in the blockchain, the adversary must produce a group element `D'` and a valid range proof for the ElGamal commitment.

The following relations are known to the adversary:

`C = c*G`
`H = h*G`
`J = j*G`

To pass consensus, the adversary must produce:

`C' = (r + v*h)*G`
`D' = r*J`

such that:

1. `v < 2^64`
2. `C' = C - H(D')*G`

Equation 2. can be rewritten as:

`(r + v*h) = c - H(r*j*G)`
 
Here `h`, `j` and `c` are constants and `r` and `v` are variables.

The adversary can select a random `r` can calculate `v` as:

`v = (c - r - H(r*j*G)) / h`

Assuming the output of the hash function is uniform on the interval `[0, q)`, where `q` is the group order, `v` will also be uniformly distributed on the interval `[0, q)`. Since `q ~ 2^252`, the probability of success after one attempt is `~2^-188`.

Using the Grover's algorithm [1], the adversary can find a value of `r` that produces a valid amount `v` after `sqrt(2^188) = ~2^94` attempts. So that gives us about 94 bits of post-quantum security. Interestingly, this also prevents the adversary from stealing any outputs unless they know the hidden blinding factor **even if they can break the output key**.

Some research suggests that SHA-3/Keccak is one of the most susceptible hash functions to quantum attacks [2], so we should probably prefer Blake2 or SHA256 for the `H(D')` calculation.

[1] https://en.wikipedia.org/wiki/Grover%27s_algorithm
[2] https://arxiv.org/pdf/2202.10982.pdf

## tevador | 2022-08-31T21:18:01+00:00
The security estimate above also shows that the scheme where both `C'` and `D'` are hashed is more secure.

If we set `r = r' + H(C', D')`

then the adversary must solve

`(r + v*h) = c - H(C', D')`

Since both `v` and `r` are inside the hash function, the adversary must select `v` and solve for `r` using Grover's search, requiring `2^126` attempts instead of `2^94`.

## kayabaNerve | 2022-08-31T22:44:33+00:00
ACK re: theft protection which is great.

NACK towards any suggestion it's unlikely for addresses to be known. It was phrased as "if" here, not unlikely, yet I do believe it's largely likely and should be considered as such.

Regardless, this is now a system extending the time in which outputs can be migrated due to the protocol security offered AND the theft-resistance offered. It also has no impact on the protocol itself as we know it.

Since this is now constructed as a perfectly hiding solution extending security in a PQ scenario via a conversion to a binding solution, I'm interested* to include it. When the discussion comes to activating it/relying on it, this will be yet another discussion, yet right now it's solely a minor computational burden on the wallet protocol. I don't believe this changes how it will be inevitable to ban ECC solutions entirely one day, and we are forced to accept RCT will need to banned when the time comes. This does provide a longer migration period for Seraphis though :)

*it seems functional. I'm sure there can be some comment on how much it increases the time it takes to receive an output. I also can't comment on the security analysis.

## tevador | 2022-09-01T19:25:33+00:00
> we are forced to accept RCT will need to banned when the time comes

I'm expecting at least a couple decades until the switch, which would make RCT outputs only a negligible fraction of all historical outputs.

> wallet protocol

Good observation. This proposal is actually just a wallet-side change and thus does not require a hard fork. But the problem is that both the sender and the receiver need to be aware of the new protocol, so it's best to couple it to Seraphis, which will force everyone to update anyways.

> theft-resistance

This protocol could be paired with a similar change of the spend keys, which could allow for some future migration path. It was first proposed here: https://github.com/monero-project/monero/issues/8418

For example, let `P` be a public key of a quantum-secure signature scheme. We can calculate the Monero spend key as `b = H(P)`. Later when the DLP is broken, `P` can be revealed to migrate the coins to a secure output.

I think CRYSTALS-Dilithium would be a good candidate for the signature scheme. It has very fast keygen (~microseconds) and the public key size is about 1.5 KB. It's also patent-free and likely to be standardized by NIST., which means it has had a fair amount of peer review.

[1] https://eprint.iacr.org/2017/633.pdf

## UkoeHB | 2022-09-01T20:23:15+00:00
I am having a hard time understanding exactly how this scheme is supposed to work.

1. What is stored in the chain, and when?
2. What proofs are required, and when?

## tevador | 2022-09-01T21:07:50+00:00
`T_0` is when Seraphis is rolled out. `T_1` is the time when we trigger "the switch". `T_2` is the time when the discrete log of `H` is broken.

To prevent inflation, the requirement is `T_1 < T_2`.

1. For `T_0 < t < T_1`, the chain stores Pedersen commitments and Bulletproofs. The blinding factors of the Pedersen commitments hide an ElGamal commitment, but this is transparent to verifiers, who only verify the Pedersen commitment and the Bulletproof. So no change from the current situation, only wallets need an update.
2. For `t > T_1`, the chain stores ElGamal commitments and a new kind of range proof (BulletProofs don't work, but AFAIK there is a Borromean-based scheme that works).

An output created at time `t < T_1` can be spent at time `t > T_1` if the owner publishes the hidden ElGamal commitment `(C', D')`. Chain verifiers can check that `C = C' - H(C', D')*G`, where `C` is the Pedersen commitment in the blockchain (this proves that both `C` and `C'` have the same value).

Since the ElGamal commitment is perfectly binding, no inflation is possible when `t > T_1`. The purpose of the range proof is to show with zero knowledge that the commitment has the form of `C'= r'*G + v*H`, `D' = r'*J` and `v < 2^64`.

## UkoeHB | 2022-09-01T21:47:37+00:00
This still leaves a lot of questions.

1. After `T_1` are you spending enotes in membership proofs with decoys or just with a single reference? If there are decoys then you must have a masked commitment of some kind - how is that handled?
1. Are you doing something different for the balance proof? Or still sum-to-zero?
1. What changes at `T_2`? Still using ElGamal commitments?

## tevador | 2022-09-01T22:35:44+00:00
1. I was thinking of a single reference when migrating. Once the output has been migrated from the Pedesen to ElGamal scheme, masking should be possible (needs the same mask on `C` and `D`).
2. Balance proof involves opening the commitment. E.g. input has `(C_1, D_1)`, output `(C_2, D_2)`. A scalar `p` must be published such that `p*G = C_2 - C_1` and `p*J = D_2 - D_1`. I guess sum to zero is also possible, but then you can't have a pseudo-random blinding factor on all outputs. If masking is used, then you can do sum to zero easily by adjusting the last mask.
3. Nothing changes a t `T_2`. We probably won't even know when `T_2` occured.

## kayabaNerve | 2022-09-02T02:08:00+00:00
This absolutely should be done with Seraphis if done. My note on it being a wallet protocol only change was solely to endorse the privacy implications, not to suggest it shouldn't be done with a hard fork.

ACK on the possibility of using Dilithium, yet preferably with IETF-standardization or at least a draft close to it. NACK to usage of any PQ scheme in a wallet protocol at this time. H(P) = private spend key has the benefit of not requiring wallet software to implement a full PQ scheme on top of everything else since its single sided. So if the proposal is kept to that, ACK.

## tevador | 2022-09-02T19:16:46+00:00
Since we ideally need to activate the PQ mitigation long before you can go to the store and buy your personal QC to crack keys, it's not a good idea to leak the spend key. Since the view keys are derived from the spend key, publishing a large number of spend keys would essentially transform the currently opaque blockchain into a transparent one, leaking the whole history of transactions to everyone.

Here is a better method.

The Seraphis output key has the following format:

`K_o = (a_1 + a_2 + a_3)*X + b*U`

where `a_1` is a fixed private key (the view balance key), `a_2` is a key extension provided by the address generation wallet component and `a_3` is a key extension provided by the sender. `b` is the private spend key.

The following wallet-side changes would be needed:

1. Generate the key `a_1` directly from the master seed `m`, e.g. `a_1 = H("view-balance-key" || m)`. It cannot be derived from the spend key. `A = a_1*X` is the associated public key.
2. The spend key is generated from two temporary keys `(x, y) = H("spend keys" || m)`. Calculate `B' = x*U`. Use `y` to derive a Dilithium key pair `(k_dl, P_dl)`. The private spend key is finally calculated as `b = x + H(A || B' || P_dl)`.
3. Generate the private keys `a_2` and `a_3` using double hashing instead of single hashing, i.e. `a_2 = H(H(generator key || j))` and `a_3 = H(H(shared secret))`.


After "the switch", you would spend an output protected by the public key `K_o`, by revealing `A`, `B'`, `P_dl` and the hash preimages `p_2` and `p_3` of `a_2` and `a_3` (the original cryptographic material is safe due to double hashing). Additionally, you'd need to provide the Seraphis key image + proof of correctness. The transaction would be signed with Dilithium.

Verifiers can check that `B' ?= K_o - A - H(p_2)*X - H(p_3)*X - H(A || B' || P_dl)*U`

All of the partial keys are strongly bound by hashes, so they are secure against a DLP break.

#### Advantages

1. Enables a future quantum-secure output migration.
1. No consensus changes are needed until "the switch", i.e. no change in transaction size or verification costs.
1. Past transactions stay private even after "the switch" (at least until someone breaks the keys).

#### Disadvantages

1. Cannot be applied to legacy wallets (because their private spend key is already bound to existing public keys, which will be broken).
1. Dilithium code is needed to generate and restore a wallet and the wallet generation is slightly more complex.
1. One additional hash calculation when generating addresses, sending and receiving outputs.
1. All migrated outputs from the same wallet share the same tuple `(A, B', P_dl)`, so they will become linkable after "the switch".

I think the disadvantages are quite minor.

## baro77 | 2022-09-02T19:31:35+00:00
I confess I haven't read carefully the whole thread (sorry) because I've just discover it trying to chase after MRL matrix room.. however I would like to underline something seeming subtle to me about the starting point.... Monero uses Pedersen commitments, however I'm not sure it's theoretically hiding amounts. That's because of how RingCT are built. I have written something about it on stackexchange: https://monero.stackexchange.com/questions/11238/should-monero-use-elgamal-commitments-instead-of-pedersen-commitments/12982#12982
The point is that output UTXO doesn't contain only Pedersen commitment (by which every node can check tx balance) but also amount "encrypted/committed" via transaction keys (to let payer and payee to agree on the actual value) - you all are super expert, but in case here there's a recap: https://www.getmonero.org/library/RctCheatsheet20210604.pdf
And my educated guess is that encrypted amount is something very similar to blinding factor constraint used in ElGamal commitments.... Hope this make sense and can be of any help!

## UkoeHB | 2022-09-02T21:38:32+00:00
> Since the view keys are derived from the spend key, publishing a large number of spend keys would essentially transform the currently opaque blockchain into a transparent one, leaking the whole history of transactions to everyone.

This is true for legacy Monero key recovery. I always pictured that (for normal wallets) the Seraphis `k_s` and `k_vb` keys would each be derived from a root entropy that is produced by hashing a secret of some kind (e.g. mnemonic seed). So: implementation-defined secret -> canonical root entropy -> {`k_s`, `k_vb`}.

> The spend key is generated from two temporary keys (x, y) = H("spend keys" || m). Calculate B' = x*U. Use y to derive a Dilithium key pair (k_dl, P_dl)

You don't need the intermediate keys `x, y`. Just derive `k_dl` directly from `m`.

> Additionally, you'd need to provide the Seraphis key image + proof of correctness.

If the DLP between `U` and `X` is known, then the key image uniqueness guarantee is lost, making all of this of questionable utility.

> Past transactions stay private even after "the switch" (at least until someone breaks the keys).

This will reveal that past transactions have shared enote destinations (`k_s U` and `k_vb X` are constants). With direct-reference membership proofs, many decoys will be exposed as decoys when they get spent 'post-switch'.

## tevador | 2022-09-02T22:29:25+00:00
> Seraphis `k_s` and `k_vb` keys would each be derived from a root entropy that is produced by hashing a secret of some kind (e.g. mnemonic seed)

Perfect. That means point 1. of my proposal is already taken care of.

> You don't need the intermediate keys `x`, `y`. Just derive `k_dl` directly from `m`.

The intermediate key `x` is needed in any case.

The reason for the intermediate key `y` is a better encapsulation of the Dilithium library, which doesn't need to know how Seraphis keys are derived.

But these are just implementation details. `P_dl` could be derived directly from `m` using a unique domain separation string.

> If the DLP between U and X is known, then the key image uniqueness guarantee is lost, making all of this of questionable utility.

The hashes bind the `X` and `U` components, which in turn binds the resulting key image, preventing double spending.

Knowing `u` such that `X = u*U` does not help the adversary satisfy the validation equation:

`B' ?= K_o - A - H(p_2)*X - H(p_3)*X - H(A || B' || P_dl)*U`

which can be rewritten in terms of `log_U` as

`x ?= k_o - a_1*u - H(p_2)*u - H(p_3)*u - H(a_1*X || x*U || P_dl)`

The adversary can choose `x`, `a_1`, `p_2`, `p_3` and `P_dl`, but satisfying the equation still involves computing a hash preimage, which is infeasible even with a quantum computer.

One attack strategy would be to select some values of `x`, `a_1` and `P_dl` and rearrange the equation as:

`H(p_2) + H(p_3) ?= (k_o - a_1*u - x - H(a_1*X || x*U || P_dl)) / u`

Now the expression on the right side is a constant, so satisfying the equation requires finding 2 hash preimages that sum to a specific value. One could use the Wagner's algorithm to remove a few bits of security, but nowhere near enough to make the attack feasible AFAIK.

> This will reveal that past transactions have shared enote destinations (k_s U and k_vb X are constants)

I don't think `k_s U` and `k_vb X` ever appear on chain in Seraphis. They are always masked. So past transactions should be secure.

Of course, the migrated output will be provably spent, but that's the price to pay for the secure migration. This should only affect relatively recent rings.

## UkoeHB | 2022-09-02T22:42:36+00:00
> The hashes bind the X and U components, which in turn binds the resulting key image, preventing double spending.

If the DLP between `X` and `U` is known, then you can make `K_t1` in the composition proof anything you want. If you are banking on using `B'` and `A` being produced as you specify, well any malicious tx author can define them as composites of `X` and `U` before the 'switch'.

> I don't think k_s U and k_vb X ever appear on chain in Seraphis. They are always masked. So past transactions should be secure.

Any enote you are spending is the output of a past transaction. What you mean is "... past transactions with no unspent outputs should be secure."

## tevador | 2022-09-02T22:53:56+00:00
> any malicious tx author can define them as composites of X and U before the 'switch'

Good point. The spend key should then be defined as `x + H(A || B' || P_dl || SigA || SigB)`, where `SigA` is a Schnorr signature with respect to `X` and `SigB` is a Schnorr signature with respect to `U`.

## UkoeHB | 2022-09-02T23:14:07+00:00
Here is my general take on this proposal.

Seraphis is a transaction protocol loaded to the brim with complex changes compared to RingCT. All of those changes are concise and directly usable after launch. This proposal recommends adding changes that are not useful now, and may _never_ become useful. It looks like scope creep that increases the material and cognitive costs to actually implement and validate Seraphis (who is going to write the security proofs justifying these changes? are we willing to wait an extra 3-12 months to get the implementation, proofs, and reviews?).

If Monero needs to transition to a quantum-secure protocol, then it should do so in a separate update that is complete in itself, instead of tacked-on to Seraphis. A complete solution that evolves Monero to the next level, without privacy or utility losses, using state-of-the-art cryptography, when it is needed and not before.

## kayabaNerve | 2022-09-03T02:41:53+00:00
I actually believe the modified switch commitment scheme, which would be a wallet protocol change with minimal performance costs and trivial implementation, should be done with Seraphis. While any Dilithium discussion does fall under Ukoe's commentary, its ability to be adopted arbitrarily to protect all future outputs let us delay such a large and complicated change. The switch commitment scheme has to be effectively done with a hard fork and is trivial however, as its just an additional addition to the mask.

## UkoeHB | 2022-09-03T05:17:30+00:00
> I actually believe the modified switch commitment scheme, which would be a wallet protocol change with minimal performance costs and trivial implementation, should be done with Seraphis. While any Dilithium discussion does fall under Ukoe's commentary, its ability to be adopted arbitrarily to protect all future outputs let us delay such a large and complicated change. The switch commitment scheme has to be effectively done with a hard fork and is trivial however, as its just an additional addition to the mask.

The switch commitment is pointless without a defense against double spends. It isn't just a 'trivial implementation' - you need a comprehensive security proof showing that the solution embedded in Seraphis will prevent inflation if triggered before the DLP is broken.

## tevador | 2022-09-03T08:11:26+00:00
> This proposal recommends adding changes that are not useful now, and may never become useful.

It's a relatively cheap contigency plan. Wearing a seatbelt when driving may also never be useful, but it's a relatively cheap mitigation.

> scope creep that increases the material and cognitive costs to actually implement and validate Seraphis

It has no effect on the validation of Seraphis. You could think of it as having 4 black-box key derivation functions:

1. `DeriveKeys`, accepts a seed `m`, returns the pair `(k_s, k_vb)`.
2. `MakeCommit`, accepts `r', v`, returns `(C, r)`, where `r` is the new blinding factor.
3. `ExtendAddress`, accepts `k_ga, j`, returns `k_addr`.
4. `ExtendSend`, accepts `K_1, q`, returns `k_send`. 

I understand that you feel overwhelmed with Seraphis. I can code the derivation functions as a separate wallet component if needed.

> A complete solution that evolves Monero to the next level, without privacy or utility losses, using state-of-the-art cryptography, when it is needed and not before

1. If there is a sudden breakthrough, there may be enough time for an emergency hardfork activating the switch, but it will be certainly impossible to roll out an entirely new implementation of Monero.
2. Without a forward-compatible solution now, you will have to disable spending of Seraphis outputs at some point, effectively burning money.

## UkoeHB | 2022-09-03T19:12:43+00:00
> It has no effect on the validation of Seraphis.

The changes in this proposal would only be needed at consensus - you are effectively embedding a transaction protocol under the surface of Seraphis. That makes it absolutely part of validating Seraphis. It also means this 'secondary transaction protocol' needs the same implementation, proof, and review rigor as Seraphis itself. We can't shoehorn major protocol changes.

> I understand that you feel overwhelmed with Seraphis.

Seraphis is not overwhelming, but its complexity is at capacity. Additional changes like this proposal would definitely push it over the brim. If Seraphis becomes too complex, it may have long-term impacts on the health of Monero R&D by discouraging and exhausting existing and new contributors.

> If there is a sudden breakthrough, there may be enough time for an emergency hardfork activating the switch, but it will be certainly impossible to roll out an entirely new implementation of Monero.

If this is the case then we shouldn't be relying on the DLP at all right now. The point of cryptographic assumptions is they will be unbroken within any meaningful timeframe.

## tevador | 2022-09-03T19:37:54+00:00
> the same implementation, proof, and review rigor as Seraphis itself

Major parts of the "secondary protocol" don't even need to be implemented in code yet, perhaps beyond some PoC. The only code that would need review are the 4 derivation functions I mentioned earlier. The protocol itself would need a review, but it's a relatively simple protocol compared to Seraphis, since it lacks a privacy layer and consists of cryptographic primitives that are not new (ElGamal commitments, hash commitments and a quantum-secure signature scheme).

Nobody is asking you personally to review or implement the protocol. I'm quite sure that the Monero community can raise enough funds to have it done in time. Seraphis is most likely *the only time* that a change like this can be rolled out.

## UkoeHB | 2022-09-03T20:03:22+00:00
> Nobody is asking you personally to review or implement the protocol.

Well... multisig would require quite a bit of work to make it compatible with the changes to `Ko`, so that's presumably something I would need to handle.

## kayabaNerve | 2022-09-04T23:24:05+00:00
I present a PoC.

https://github.com/kayabaNerve/serai/commit/5fa593fe061ee078b4bd480f0eeb6d9c4e2210f2

This embeds an ElGamal commitment into the Pedersen commitments at a wallet-protocol level. If we realize this scheme is ineffective at creating a PQ-viable migration plan, we can never use it for a minor performance cost. If it is effective, and we can prove it as such, we have this benefit available. This also is more resistant against theft as described (which is why I originally dismissed the idea as partial, yet now am advocating for it). While I believe we would still also want to augment private keys in another, much longer, much more annoying discussion, that isn't effectively required to be a hard fork therefore letting us delay such a discussion.

I'll also note this passes all tests on my end, including ones for multisig, though sure, the Monero codebase is not laid out as mine is and there would be more leg work when moving it into Monero. The important distinction is the proof that this is purely on the wallet level, since they ran against an unmodified Monero daemon. Due to the location of the modification, no changes to scanning (including rebuilding the commitment) nor the higher level TX creation process were necessary (though the CLSAG code did need to not use this modified function, of course).

@tevador Would you mind confirming that this is a correct implementation of the currently proposed idea?

As a side note, we would need to discuss the sender being able to clawback funds under such a scheme. We can simply comment that it's infeasible to break all one-time keys, and unknown which are valuable due to the perfectly blinding properties, so those are still sufficiently viable. But yes, this scheme only truly makes sense with a PQ augmentation for private spend keys. This is a halfway point usable for a limited amount of time that may preserve an extra year or two of outputs however.

## tevador | 2022-09-05T13:26:42+00:00
> I present a PoC.
> 
> [kayabaNerve/serai@5fa593f](https://github.com/kayabaNerve/serai/commit/5fa593fe061ee078b4bd480f0eeb6d9c4e2210f2)
> 

LGTM

> This embeds an ElGamal commitment into the Pedersen commitments at a wallet-protocol level. If we realize this scheme is ineffective at creating a PQ-viable migration plan, we can never use it for a minor performance cost. If it is effective, and we can prove it as such, we have this benefit available. This also is more resistant against theft as described (which is why I originally dismissed the idea as partial, yet now am advocating for it). While I believe we would still also want to augment private keys in another, much longer, much more annoying discussion, that isn't effectively required to be a hard fork therefore letting us delay such a discussion.
> 

The switch commitment scheme is not enough to prevent undetectable inflation. The reason for this is that a quantum adversary can easily double spend due to the Seraphis key image format.

See my post-quantum proposal, which offers a comprehensive solution: https://gist.github.com/tevador/23a84444df2419dd658cba804bf57f1a


## kayabaNerve | 2022-09-06T03:01:51+00:00
Right, sorry. I have reviewed that do believe we should move forward there :)

# Action History
- Created by: tevador | 2022-08-25T22:27:08+00:00
