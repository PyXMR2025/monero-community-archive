---
title: Janus mitigation
source_url: https://github.com/monero-project/research-lab/issues/62
author: SarangNoether
assignees: []
labels: []
created_at: '2020-01-31T12:55:18+00:00'
updated_at: '2021-06-29T04:02:19+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
# Janus mitigation

The [Janus attack](https://web.getmonero.org/2019/10/18/subaddress-janus.html) can be used in an attempt to link known subaddresses, in order to determine if they are derived from the same master wallet address.


## Attack description

A user with wallet view and spend keys `(a,b)` generates a master wallet address `(A,B) := (aG,bG)`. She generates subaddresses `i` and `j` as follows, where `H` is a hash-to-scalar function.

For index `i`:
`B_i := H(a,i)*G + B` and `A_i := a*B_i`

For index `j`:
`B_j := H(a,j)*G + B` and `A_j := a*B_j`

To attempt to link these subaddresses, an adversary generates a Janus output `P`, using transaction private key `r`:
`R := r*B_i`
`P := H(r*A_i)*G + B_j`
Note the mismatched indices in the output public key.

When recovering the output, the recipient computes `P - H(a*R)*G == B_j` and assumes the output is directed to subaddress `j`. If the recipient acknowledges receipt of the transaction, the adversary knows that subaddresses `i` and `j` are linked.

Note that the attack can also attempt to link a subaddress to its corresponding master address.


## Mitigation

To allow the recipient to detect Janus outputs, the sender is required to include a second transaction public key `R' := r*G` using the fixed basepoint `G`.

On detection of the output public key `P`, the recipient computes the detected subaddress spend private key:
`b_j = H(a,j) + b`

Finally, the recipient checks that the following equation holds:
`R - b_j*R' == 0`
If the equation holds, the output is not a Janus output. If it fails, the output is malformed and may be a Janus output; the recipient should not acknowledge receipt, but may spend the funds if the output is spendable.


### Correctness

To see why the mitigation detects a Janus output:
`R - b_j*R' == r*B_i - b_j*(r*G) == r*(B_i - B_j) != 0` (for `i != j`)

In order for the adversary to fool the mitigation check, it must provide `R'` such that `b_jR' == b_i*G`, which it cannot do since subaddress private keys are uniformly and independently distributed and unknown to the adversary.


## Considerations

This mitigation requires the addition of a single group element `R' = r*G` for each transaction private key `r` used in a transaction. This point is redundant in the case where no subaddresses appear as recipients, since it has the same construction as a standard-address transaction public key. The presence or absence of additional transaction public keys is already a signal of the presence of subaddress recipients, which is a separate concern.

No additional computational complexity is present when scanning transactions for controlled outputs. For each identified output requiring the mitigation, the complexity of the check is minimal. This check can also be batched across multiple transactions if desired, in order to increase efficiency when computing many checks at once.


# Discussion History
## SarangNoether | 2020-01-31T12:59:46+00:00
The previous mitigation example requires a separate additional base-`G` point for each transaction private key, which can scale poorly.

Here is an alternate idea from @UkoeHB on a way to permit Janus mitigation in a way that plays nicely with unique transaction keys.

These are the steps a transaction creator would perform to produce a multi-output transaction with standard-address and subaddress destinations:
1. Choose a *master transaction private key* `r` uniformly at random.
2. Compute and publish the *Janus key* `R := r*G`.
3. For each output index `i` directed to standard address `(A,B)`:
   - Choose a random *indexed private key* `r_i`.
   - Compute and publish the *indexed public key* `R_i := r_i*G`.
   - Compute and publish the *output public key* `P_i := H(r_i*A)*G + B`.
4. For each output index `i` directed to subaddress `(A,B)`:
   - Compute the *indexed private key* `r_i := r + H(R,i)`.
   - Compute and publish the *indexed public key* `R_i := r_i*B`.
   - Compute and publish the *output public key* `P_i := H(r_i*A)*G + B`.

Recipients recover their output private keys as usual.

To test for a Janus attack, the recipient of the output at index `i` (with subaddress private spend key `b_i`) checks that the equality `b_i*(R + H(R,i)*G) - R_i == 0` holds. If it does, then the output is not a Janus output; if it does not, the output is invalid and may be a Janus output.

## UkoeHB | 2020-02-01T16:17:48+00:00
There is currently no mitigation to the Janus attack (it's 100% undetectable), and the method proposed here is the cheapest possible mitigation in terms of blockchain bloat (it requires 1 additional 32-byte public key for each mitigated transaction, although current 2-output tx where the non-change output is to a subaddress currently uses 1 tx pub key, which would become 3 tx pub keys post-mitigation). It DOES require the user's spend key, so view-only wallets are still vulnerable to this attack, and (assuming this is implemented) high-stakes users should use spend-rights enabled wallets (i.e. wallets with both view and spend keys) to receive funds.

I feel that it's important for this proposal (or a counter-proposal) to be implemented. It would surely be disconcerting for users who may be vulnerable, to want to use Monero and yet hear that efforts to mitigate this problem were rejected. It undermines the utility of subaddresses.

## UkoeHB | 2020-02-01T16:52:48+00:00
Since this mitigation involves adding public keys to the tx extra field, @SarangNoether says it would be best to consider it in the larger context of updating how the tx extra field is treated. In particular Issue #61 should be resolved first, and due to the nature of Monero join protocols a la CoinJoin (work in progress) it would be beneficial to those protocols for the Janus base key to be randomly shuffled amongst other transaction public keys.

Issue #58 recommends adding more pub keys to the tx extra field, although it would be best to segregate those from transaction public keys to prevent increasing scan times.

## UkoeHB | 2020-02-16T19:50:59+00:00
The indexed tx private key method, as stated, has a flaw. If two outputs are sent to the same subaddress `(A_i, B_i)`, and their tx pub keys are `R_1` and `R_2`, then someone who knows `(A_i, B_i)` could test those tx pub keys by calculating `R_1 - H(R,1)*B_i ?= R_2 - H(R,2)*B_i`.

We get around this by making another shared secret with the Janus base key `R = r*G `and the recipient's view key: `r*A_i`. Now, `R_1 = [r + H(r*A_i,1)]*B_i` and `R_2 = [r + H(r*A_i,2)]*B_i`. Only by recreating the shared secret can the Janus test be performed. 

`b_i*(R + H(a_i*R,1)*G) ?= R_1`

## UkoeHB | 2020-03-24T07:43:28+00:00
There are some slight problems related to normal addresses here.
1. If a normal address transaction public key is just a random one e.g. `r_t G`, then it could also be `r_t B_i` for some subaddress `A_i, B_i` supposedly also owned by the recipient (now using `t` to indicate the output index, and `i` to indicate the subaddress index; the sender-reciever shared secret would be `r_t A_i`). The recipient wouldn't be able to identify he was subject to a Janus attack. Instead we make even the normal address tx pub keys like the subaddress tx pub keys, in other words `r_i = r + H(r*A_i,t)`. The normal address recipient just needs to check that the actual tx pub key in tx data is correct, `R_t ?= R + H(a*R,t)*G`, and observers wouldn't be able to make that check since they don't know `a*R`.
2. But wait, it turns out if the index shared secret is based on the view key, an attacker could make `R = r*B_i` (and use `R_t = r*B_i + H(r*A_i,t)*G`), pushing the Janus attack even deeper (and the sender-receiver shared secret would be `r*A_i + H(r*A_i,t)*A = a*R_t`, using the normal address view key `A` and subaddress key `A_i`)! The solution is to make it a shared secret with the spend key directly, `r_t = r + H(r*B_i,t)`. Now the normal address recipient computes `R_t ?= R + H(b_i*R,t)*G` (and subaddress recipient computes `R_t ?= b_i*[R + H(b_i*R,t)*G]`). This guarantees `R = r*G` (i.e. its base key is `G`), as the tx author would be unable to make the shared secret `r*B_i` on any other base.

Unfortunately this means even if all recipients are normal addresses, they would still require individual transaction public keys and a Janus base key.

## UkoeHB | 2020-04-01T17:43:39+00:00
Note: Adding the final form of Janus mitigation would add an average 64 bytes per transaction (average output count is ~2.2, most of which have 1 tx pub key currently, so +1 janus base key +1 tx pub key = 64 bytes average).

## SarangNoether | 2020-04-01T17:45:06+00:00
> Note: Adding the final form of Janus mitigation would add an average 64 bytes per transaction (average output count is ~2.2, most of which have 1 tx pub key currently, so +1 janus base key +1 tx pub key = 64 bytes average).

For context, the migration from MLSAG to CLSAG signatures already reduces the typical transaction size by about 600 bytes.

## UkoeHB | 2020-04-08T05:27:14+00:00
Note that the necessity of implementing Janus for _all_ transactions, not just the potentially small minority which use subaddresses, means scanning times could double (although as @jtgrassie has pointed out, we don't have an actual estimate of the effect on scanning time, which would be valuable) on a per-tx basis following the update. By scanning, I mean the process of searching for owned outputs.

UPDATE: I actually counted the EC operations involved, and Janus might not increase scan times more than around 15-30% on average. See Issue #73 for more details.

## UkoeHB | 2020-04-16T13:01:40+00:00
After talking with @knaccc, there are two new ideas to add here.

1. An alternate Janus mitigation would be for provers to make a 48-byte Schnorr signature on key `K^v` with `r_t` as signing key to prove the shared secret was constructed legitimately. The basic method would be to truncate the hash output, so with signature `(c,r)` the challenge `c` component is 16 bytes, and response `r` is 32 bytes like normal. This would imply one such signature per tx pub key, would not entail additional scanning time since extra transaction public keys wouldn't be necessary, and would not require the private spend key so view-only wallets would be compatible.

2. Most 2-output transactions include a change output. Change outputs are easy to identify for recipients, since they can recompute the key images of owned outputs and recognize the appearance of one (or more) in the tx where they received the change output (implying they made that tx in the first place). Another way to do this (courtesy of @knaccc) is to send change outputs to a secret subaddress with index -1. Since it's only known to you then outputs received to that address must be change and you don't have to worry about Janus. Not having to worry about Janus means no need for an extra tx pub key, or, for the 48-byte Schnorr method, no need for an extra Schnorr proof. This offers a big optimization, since we once again only need 1 tx pub key for 2-out tx (most tx are 2-out). It also has substantial bearing on Issue #73, by reducing EC operations for scanning 2-outs from 2 to 1.

EDIT: The result of point 2 is recommendation to enforce 1 tx pub key for 2-out transactions (the vast majority only need 1 tx pub key already anyway), and enforce 1 tx pub key per output for 3+-output transactions. This improves transaction uniformity will also promoting optimized tx size and scan times.

## UkoeHB | 2020-05-25T01:20:10+00:00
For posterity I am pasting the complete updated 'Janus base key method' here, since I'm removing it from my proposal (Monero repo issue #6456) in the name of less ambiguity.

This changes how tx authors make transaction public keys, does *not* change how recipients scan for owned inputs, *does* add a step for recipients after they identify an owned output (it requires the private spend key).

Assume we want to make a tx with `p` outputs, to be indexed `t = 0,...,p-1`. Some of the recipients are subaddresses `(K^v_i, K^s_i)` where `v` means 'view' and `s` means 'spend' (`i` is the subaddress index, note that `K^v_i = k^v*K^s_i` using private view key `k^v`), and some are normal addresses `(K^v, K^s)`. For more of this terminology/notation, see [Zero to Monero Second Edition](https://web.getmonero.org/library/Zero-to-Monero-2-0-0.pdf) especially Chapter 4.

1. Generate a random base transaction private key `r` and compute `R = r*G`. This is the 'Janus base key'.
2. For each recipient `t` compute their transaction private key: 
	a. If a normal address: `r_t = r + H(r*K^s,t)`
	b. If a subaddress:     `r_t = r + H(r*K^s_i,t)`
3. For each recipient `t` compute their transaction public key.
	a. If a normal address: `R_t = r_t*G`
	b. If a subaddress:     `R_t = r_t*K^s_i`
4. For each recipient `t` compute the sender-receiver shared secret to be used with one-time addresses and output commitments (and view tags).
	a. If a normal address: `r_t*K^v`
	b. If a subaddress:     `r_t*K^v_i`

Note that transaction public keys depend on the output index, so should be ordered the same way as outputs (so there is a 1:1 correspondence). The Janus base key is not used to scan for outputs, and is basically inert except to perform the Janus test.

Now suppose we are looking for outputs and encounter a specific one-time address/tx pub key pair `(K^o_t, R_t)`.

1. Compute the nominal sender-receiver shared secret: `k^v*R_t`.
2. Check for ownership (we will change this step a bit in Proposal Part 3: View Tags, but this is how things are currently done) by computing the nominal spend key: `K^s_nom = K^o_t - H(k^v*R_t,t)*G`. Then see if `K^s_nom` equals one of our address's/subaddresses' spend keys relevant to the private view key `k^v`. If it does, horray we own the output and can spend it!
3. Perform a Janus test to make sure the sender isn't messing around trying to associate some of our subaddresses together. Basically we will recompute the transaction public key to make sure it was made honestly. Note that `k^s_i` is the _full_ subaddress spend key, i.e. `k^s_i*G = K^s_i`, where `k^s_i = k^s + H(k^v,i)`.
	a. If the output is owned by a normal address: `R_t ?= R + H(k^s*R,t)*G`
	b. If the output is owned by a subaddress:     `R_t ?= k^s_i*(R + H(k^s_i*R,t)*G)`

Janus mitigation also entails feeding information back to the user if an output gets flagged. In my opinion flagged outputs should still be spendable, but the user should receive a big warning. Janus is most likely to be abused if users are likely to not get or heed a warning.

Cost: Every output to be tested for Janus needs its own transaction public key. This can increase scanning times and transaction sizes if it means transactions have more tx pub keys. Actually testing owned outputs for Janus is trivial with respect to scanning time. All transactions must have a Janus base key, for 32 bytes per transaction (note there is a bug in core code where transactions with >1 tx pub key have an extra tx pub key that isn't used for anything, which means adding Janus and fixing the bug would have a neutral effect for those tx).

Drawbacks: requires private spend key and at best weakly compatible with view-only wallets, not compatible with TxTangle, multisig users must collaborate to perform a Janus test

Note: If transaction public keys are constrained (2-out tx limited to 1 tx pub key, so there must be one change output), wallets performing Janus tests would also have to identify change outputs. That means knowing key images for owned outputs, and checking the tx where they received an output that failed the Janus test to see if its key images are theirs (or encoding the amount with a change tag instead of normal blinding factor, and trying to recompute the output commitment to see how it was encoded).

## UkoeHB | 2020-05-27T01:23:00+00:00
Also deprecating the 48-byte Schnorr proof method, and pasting here for posterity.

Originally ideated by @knaccc. Transaction authors make, for each sender-receiver shared secret to be Janus tested, a basic Schnorr proof that the secret was made out of the recipient's view key. For more of this terminology/notation, see [Zero to Monero Second Edition](https://web.getmonero.org/library/Zero-to-Monero-2-0-0.pdf) especially Chapter 4.

Given a recipient view key `K^v`, and transaction private key `r_t` (with output index `t`).
1. Generate random signature value `alpha`, and compute `alpha*K^v`.
2. Compute the 16-byte challenge: `c = H_16("janus_schnorr", K^v, r_t*K^v, [alpha*K^v], t)`
3. Define the response: `resp = alpha - c*r_t`
4. Publish the proof pair `(c, resp)` in the transaction alongside the tx pub key `R_t = r_t*G` or (for a subaddress recipient) `R_t = r_t*K^s_i`.

Recipient encounters a one-time address/tx pub key pair `(K^o_t, R_t)` and identifies it as an owned output.
1. With the sender-reciever shared secret: `k^v*R_t`
2. Compute the nominal 16-byte challenge: `c_nom = H_16("janus_schnorr", K^v, r_t*K^v, [resp*K^v + c*R_t], t)`
3. If `c_nom ?= c` then `R_t` was constructed from the view key corresponding to the spend key that can spend this output.

Cost: Every output to be tested for Janus needs a 48-byte Schnorr proof. Actually testing owned outputs for Janus is trivial with respect to scanning time.

_Change outputs_

In a 2-out tx it won't be clear which output corresponds to the 48-byte Janus proof in the tx (recall we are enforcing 1 tx pub key for 2-out tx). Both recipients will try to verify the proof, and only one will succeed (the non-change recipient). If the proof fails, it means the owned output might be a change out, so the recipient should check before concluding they are susceptible to a Janus attack.

For the solution proposed here, the tx author makes a special change tag from their private view key, key prefixing with the transaction's one-time keys and the tx pub key to ensure uniqueness and to ensure the change tag can only be used in this transaction. He uses this value to encrypt the amount to be stored in the `ecdhInfo:amount` field in transactions.
1. `change_tag = H("change_tag", k^v, K^o_0, K^o_1, R)`
2. Normal case vs change output case (for output amount `b_t`),
a) normal: `amount_t = b_t XOR_8 H("amount", H(r_t*K^v,t))`
b) change: `amount_t = b_t XOR_8 change_tag`

Upon receipt of an output from a 2-out tx:
1. Check if the output amount commitment `C^b_t` can be reconstructed in the normal way (by decoding `amount_t`, computing `C^b_t_nom`, and comparing `C^b_t_nom ?= C^b_t`), and if it can't then if the transaction is a 2-out tx try decrypting `amount_t` with `change_tag` and reconstructing the amount commitment. If that works, then set `Janus_passes = true`. If neither works, then the amount may be malformed or output commitment has a problem.
2. Check the 48-byte Schnorr signature. If it succeeds, then set a flag `Janus_passes = true`.
3. At the end of checking a received output, if the flag `Janus_passes == false` then issue a warning to the user.

Is 8 bytes for the change tag enough (amount blinding factors are 8 bytes, since amounts are 8 bytes)? The risk with change tags is a malicious person performing a Janus attack then creating an encrypted amount that successfully passes `C^b_t_nom ?= C^b_t` based on a change tag, even though the malicious person doesn't know the appropriate view key. In other words, they have to successfully guess a good change tag. At 8 bytes the probability is 1 in 1.8e19, while total on-chain outputs are on the order of 1e7 currently (after 6 years of transactions). Even at 0.5 cents per transaction (0.005 USD), it would cost 50000 USD to get a 1e-12 chance of successfully faking a change output. I consider that cost prohibitive. A 1.8e19 probability also means it's very unlikely for the change_tag to accidentally equal the normal blinding factor, a collision that might set off an erroneous Janus warning (depending how the change output identifying logic gets set up).

## UkoeHB | 2021-06-29T00:59:51+00:00
New idea
- zero bytes in blockchain
- mitigates Janus with just private view key
- **cost**: larger addresses, modified output handling (for construction, identification, spending)

### New address format

New addresses would have three keys instead of two. Both normal address and subaddress variants are shown.

- **Spend key** (unchanged): `K^s = k^s G  OR  K^{s,i} = k^{s,i} G`
- **Ancillary key** (new): `K^a = H("ancillary_key", k^v) G  OR  K^{a,i} = H("ancillary_key", k^v, i) G`
- **View key** (modified): `K^v = k^v K^a  OR  K^{v,i} = k^v K^{a,i}` (instead of `K^v = k^v G  OR  K^{v,i} = k^v K^{s,i}`)


### Modifications to output construction

- **Sender-receiver shared secret**: `r K^v` (unchanged)
- **One-time address construction**: `K^o = H(r K^v) G + K^s` (unchanged)
- **Transaction public key**: `R = r K^a` (modified; each output must have a unique txout pub key [change outputs may be able to get by without their own txout pub keys, e.g. so [this proposal](https://github.com/monero-project/monero/issues/6456) still works with 1 txout pub key for 2-out tx; use `R = r K^a_nonchange` as single txout pub key, then `(1/k^a_change) R` for the change output's commitment mask])
- **Commitment mask**: `y = H(r K^v, r G)` (modified; to reconstruct commitment, must know `r G`, which is not recorded in the chain)


### Janus mitigation

Janus mitigation hinges on the new commitment mask construction.

1. Identify an owned output.
2. See which address/subaddress owns it.
3. Use the corresponding ancillary private key `k^a` to compute `r G = (1/k^a) R`.
4. Recompute the commitment from the decoded amount `b` and `y = H(r K^v, r G)`, `C = y G + b H`.
5. If recomputing the commitment fails, then you can't spend the output, so it can be ignored (no need to notify the user of an attempted Janus attack or anything; it can be logged in case there is a bug).

This works because the sender can only know the value `(1/k^a) R` if it equals `r G`, and `k^a` is associated with the address revealed by view-key scanning so the sender cannot make `r K^a` based on a different address.

# Action History
- Created by: SarangNoether | 2020-01-31T12:55:18+00:00
