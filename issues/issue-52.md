---
title: Shorter MLSAGs with Hidden Amounts
source_url: https://github.com/monero-project/research-lab/issues/52
author: RandomRun
assignees: []
labels: []
created_at: '2019-03-16T19:05:55+00:00'
updated_at: '2019-05-02T10:59:13+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
It is my understanding that right now the Monero MLSAG signature contains two sequences of scalars. Their use is to separately and respectively ensure linkability and that the commitments for the amounts add up to zero. (I am basing my understanding from posts about ringCT (e.g. [here](https://monero.stackexchange.com/questions/7802/understanding-mlsag-in-monero-transaction)), and although I am aware that Monero now uses Bulletproofs, I believe that the MLSAG part should still be the same, since, to my knowledge, bulletproofs integration only affected the range proofs.) 

So, to recap and make sure that I got the right picture, this is what I think goes on now:

**Signing:**

Signer picks a ring of outputs that includes his own output, plus decoys. The simplified ring information needed for signing looks like this:

`Ring = (P_i, C_i)` for `i` in `[1,n+1]`, 

where `C_i` is already denoting the committed amounts for each `P_i`, subtracted the commitments for the new output amounts being created in the transaction being signed.  

(WLOG and to simplify the exposition, we assume that his output is at position `n`. I.e., the signer knows scalars `p_n, c_n` such that `(P_n, C_n) = (p_n*G, c_n*G)`. Also, in what follows I will omit the transaction message from the hashes `Hs` just to simplify notation but in reality they should be there, of course.)

Next, he picks two sequences of random scalars: `s'_0, s_1, ..., s_{n-1}` and `r'_0, r_1, ..., r_{n-1}`. He computes:

`L_0 := s'_0*G`
`R_0 := s'_0*Hp(P_n)`
`S_0 := r'_0*G`
`h_0 := Hs(L_0||R_0||S_0)`,

and, for `i` in `[1,n]`, computes:

`L_i := s_i*G + h_{i-1}*P_i`
`R_i := s_i*Hp(P_i) + h_{i-1}*I`
`S_i := r_i*G + h_{i-1}*C_i`
`h_i := Hs(L_i||R_i||S_i)`.

Finally, he sets: 

`s_0 := s'_0 - h_{n-1}*p_n`, `r_0 := r'_0 - h_{n-1}*c_n`, and 
`sig := (h_0, s_0,..., s_{n-1}, r_0,..., r_{n-1}, I)`.

**Verification:**

Verifier parses the signature information and computes, for `i` in `[1,n+1]`:

`L_i := s_i*G + h_{i-1}*P_i`
`R_i := s_i*Hp(P_i) + h_{i-1}*I`
`S_i := r_i*G + h_{i-1}*C_i`
`h_i := Hs(L_i||R_i||S_i)`.

If `h_0 = h_n`, then it passes verification.

If that understanding is correct, I am wondering if that signature cannot be made shorter by completely eliminating the `S_i` component and the `r_i`'s from the signature.
That would entail redefining `L_i` and `R_i` to aggregate, respectively, `C_i` and `C' := c_n*Hp(P_n)`.

**The Naive Approach and the problem with it:**

The naive approach would be to just add `C_i` and `C'` to `P_i` and `I`, respectively, and redefine:

`L_0 := s'_0*G`
`R_0 := s'_0*Hp(P_n)`
`h_0 := Hs(L_0||R_0)`,

for `i` in `[1,n]`:

`L_i := s_i*G + h_{i-1}*(P_i + C_i)`
`R_i := s_i*Hp(P_i) + h_{i-1}*(I + C')`
`h_i := Hs(L_i||R_i)`

Finally, redefine:

`s_0 := s'_0 - h_{n-1}*(p_n + c_n)`
`sig := (h_0, s_0,..., s_{n-1}, I, C')`.

This naive approach already has the advantage of passing the corresponding verification for an honest signer and having a shorter signature. However, it also has a big problem: since the verifier has no way to check that `I` and `C'` were produced honestly, a malicious signer could easily provide random points `I'` and `C''` such that `I + C' = I' + C''`, thus allowing him to create new coins undetected.

**Solution: Use a Linear Combination with Hashed Coefficients:**

To fix that, before redefining `L_i` and `R_i`, the signer computes:

`mu_P = Hs("points", Ring, I, C')`
`mu_C = Hs("amounts",Ring, I, C')`.

Then he proceeds to define:

`L_0 := s'_0*G`
`R_0 := s'_0*Hp(P_n)`
`h_0 := Hs(L_0||R_0)`,

and, for each `i` in `[1,n]`:

`L_i := s_i*G + h_{i-1}*(mu_P*P_i + mu_C*C_i) = s_i*G + (h_{i-1}*mu_P)*P_i + (h_{i-1}*mu_C)*C_i`
`R_i := s_i*Hp(P_i) + h_{i-1}*(mu_P*I + mu_C*C') = s_i*Hp(P_i) + (h_{i-1}*mu_P)*I + (h_{i-1}*mu_C)*C'`.
`h_i := Hs(L_i||R_i)`

Finally, he sets:

`s_0 := s'_0 - h_{n-1}*(mu_P*p_n + mu_C*c_n)`
`sig := (h_0, s_0,..., s_{n-1}, I, C')`.

This way, the honest signing still passes the corresponding verification, but any attempt to find `I'` and `C''` such that the linear combination `mu_P*I + mu_C*C' = mu'_P*I' + mu'_C*C''` holds would fail, except with negligible probability, since the values of `mu'_P` and `mu'_C` would change unpredictably.

This signature format change would incur only the additional computational cost of two `Hs` operations, and two extra scalar multiplications per ring member, and the space cost of containing the extra point `C'`.

[Edit: I had forgotten to add `C'` to the definition of the hashed coefficients, but all points involved in the linear combination should be included, of course.]

# Discussion History
## b-g-goodell | 2019-03-16T20:21:30+00:00
 1. With a simple ringct transaction, the amount commitments C_i in forming your key (P_i, C_i) as you describe are Pedersen commitments to amounts, not public keys. The way we can show we know how to open the commitments C_i is to not use these commitments in the MLSAG, but the difference between the input and output commitments. That is to say, each C_i in your exposition has a known discrete log with respect to G (except with negligible probability) only if we write C_i =  D_in - Sum(D_out) where each D_in and D_out are Pedersen commitments. Assuming this is what you meant when you break C_i down into c_i*G and c_i*Hp(stuff), we can move along...
 2. You are correct that merely adding C_i and C' to P_i and I, respectively, leads to a key cancellation problem, which could cause bad transactions.
 3. You are correct that using the linear combinations as you describe would eliminate the key cancellation problem, assuming the hash function is not a badly chosen one. This is how musig aggregates keys together. 
 4. Viewing an MLSAG signature as a multi-signature with both keys P_i and D_in - Sum(D_out), except signed only by one signer (and hence eliminating the rounds of interaction in multisignatures)  your approach is essentially to apply the Musig key aggregation approach and construct a usual LSAG ring signature from that aggregated key.

This is actually a neat way to map a many-rowed MLSAG ring signature scheme to a single-rowed LSAG signature scheme. I like it. I would want a tight security proof before moving on implementation, but I don't think that proof would be too difficult... What I find interesting about this is that this introduces a sublinearity in signature sizes... if we want to sign with a length-n vector of keys in a ring signature with R members, we can do so for the same space as a length-1 vector of keys, although verification time increases requisitely.

## RandomRun | 2019-03-17T12:24:59+00:00
1.  That is indeed what I meant. I see now that the way I wrote didn't make that very clear. Thank you for pointing that out and writing that clarification.

3. I actually first learned about this trick reading Zero to Monero, and thought it was their idea. Only later did I learn it was presented in the Musig paper. 

4. That is a good way to think about it. I wasn't seeing it as a multisig of sorts until you mentioned it.

I hadn't thought about how to aggregate different rings from an MLSAG together, just their hidden amounts component. It is an interesting idea. Aggregating public keys that don't need to be linked, like commitments to zero in this context, seems less complex than adding ones that do need to be linked, like other one-time addresses.


## RandomRun | 2019-03-18T02:23:46+00:00
I have been trying to aggregate two rings of signing keys together the same way the amount commitment component was aggregated, but so far I haven't been able to. I suspect we may not be able to do that as seamless as the amount case, or at all. The reason is this: for the amount case, `C_n` is a signing key w.r.t. the point `G`, and later we define `C' := c_n*Hp(P_n)`, so we have two pairs of points `(P_n, I)` and `(C_n, C')` have the same discrete logarithm to w.r.t. `G` and `Hp(P_n)`, respectively.

If we take two points and their respective key images `(P_n, Ip)`, `(Q_n, Iq)`, they will have same discrete logarithms w.r.t. different pairs of points, namely `G, Hp(P_n)` and `G, Hp(Q_n)`, and I think it will be hard to come up with a definition of `R_i` that is defined over a common point, since `Hp(P_n)` and `Hp(Q_n)` are independent.

Consider, however, that the reason that the key image is not linkable to the signing keys is not because of the use of `Hp(.)`, but rather because `G` and `Hp(P)` are independent points. In general if one sees two points `x*G` and `x*H`, with `H` independent from `G`, then there is no way to extract `x` or link the two. So that all we need is independence.

With that in mind, if we fix an independent point `H`, redefining the key image of `P = p*G` as `I := p*H` should work just as well for all the guarantees that Monero already offers, plus it would allow for seamless aggregation of points just like we did with a point and the amount key.  [**Edit: as pointed out by @apoelstra below, and in the Cryptonote 2.0 paper, the idea of using a fixed base point leads to a problem with the sender being able to link two payments made the same receiver. So it is not true that all guarantees are preserved with a fixed base point.**]

So, for instance, a regular linkable ring signature would look like this:

`L_0 := s'_0*G`
`R_0 := s'_0*H`
`h_0 := Hs(L_0||R_0)`,

and, for i in [1,n]:

`L_i := s_i*G + h_{i-1}*P_i`
`R_i := s_i*H + h_{i-1}*I`
`h_i := Hs(L_i||R_i)`.

And:

`s_0 := s'_0 - h_{n-1}*p_n`, and
`sig := (h_0, s_0,..., s_{n-1}, I)`, as usual.

With this change, we could get a ring signature whose size depends only on the ring size, but not the number of rings.

## SarangNoether | 2019-03-19T19:10:51+00:00
Here is some simple [example code](https://github.com/SarangNoether/skunkworks/tree/clsag/clsag) that shows how this might work with both full and simple transaction types.

## b-g-goodell | 2019-03-21T00:34:22+00:00
Reminding myself: problems with indices being exposed

## stoffu | 2019-03-22T02:55:52+00:00
@RandomRun 

I also find the scheme sound.

> With that in mind, if we fix an independent point H, redefining the key image of P = p*G as I := p*H should work just as well for all the guarantees that Monero already offers, plus it would allow for seamless aggregation of points just like we did with a point and the amount key.

For your second proposal, I find the idea of fixing the basepoint for key images workable as well, but I think it means that the signer's index has to be the same for all the rings, which I think is undesirable (AFAIK this is why RCTSimple type with pseudo outputs was introduced).


## RandomRun | 2019-03-22T04:45:58+00:00
@stoffu I share your concern. Probably the trade-off between compressing all signing keys at the expense of linking the indices is not a good one, and just aggregating the amounts may be good enough for now.

Fixing the base point `H` however has other advantages besides opening the door for aggregation. For instance, taking `Hp(.)` by itself incurs some computational costs but, more importantly, fixing the base point `H` allows for faster computations of double scalar multiplications, as pointed out by @SarangNoether. He is working on simulations for that, so I will let him elaborate more on that as I don't fully understand that part.

So right now I believe that changing the key image but not aggregating signing keys would allow for faster verification times and smaller signatures (compared to present ones, although not quite as the aggregated ones, of course) without compromising untraceability.

## RandomRun | 2019-03-22T05:07:41+00:00
Update: in transitioning to the new key image format, new signing and verification algorithms are needed that involve outputs that could have been spent with the previous key image format as well as the new ones. In the following I will outline how such a transition can work.

First a block height `M` for the change must be fixed, and that would of course entail a hard fork, so that could be any of the scheduled ones.

**Hybrid verification:**

The verifier receives a signature `sig = (h0, s0, s1,..., sn-1, I)`, it will construct the verification steps as follows:

for `i` in `[1,n]`, computes:
  
`Li := si*G + h_{i-1}*I`
`Ri := si*H + h_{i-1}*I`, if the global index of the `i`th output shows that it was created after height `M`, or
`Ri := si*Hp(Pi) + h_{i-1}*I`, otherwise.
`hi := Hs(Li || Ri)`.

If `h0 = hn`, it passes verification; otherwise it fails.

Therefore, in order to pass verification, the signer will need to produce the signature constructed in the same way. 

**Hybrid signature:**

Signer picks random scalars `s'0, s1,..., sn-1`, and computes:

`I = pn*H`, if `Pn`'s output was created after height `M`, or
`I = pn*Hp(Pn)`, otherwise.

`L0 := s'0*G`
`R0 := s'0*H`, if his own coins are from an output created after height `M`, or
`R0 := s'0*Hp(Pn)`, otherwise,
`h0 := Hs(L0 || R0)`.

For `i` in `[1,n-1]`, computes:

`Ri := si*H + h_{i-1}*I`, if the global index of the `i`th output shows that it was created after height `M`, and
`Ri := si*Hp(Pi) + h_{i-1}*I`, otherwise.
`hi := Hs(Li || Ri)`.

Sets `s0 := s'0 - h_{n-1}*pn`, as before, and publishes `sig = (h0, s0, s1,..., sn-1, I)`.

Some observations:

Notice that this doesn't require any changes to the output format itself, but only to the signing and verifying algorithms.

Since the points `H` and `Hp(P)`'s are independent, there is no risk of key image collisions, so that new used key images can be safely added to the collection of old used key images, and there is no way to distinguish the two types. Also, the verification algorithm above prevents outputs from double spending, since they can only use one key image, as enforced by the components `Ri`. If the signer tries to use the wrong key image format, they will either not be able to solve for `s0`, or the signature will be incorrectly formed and rejected by the verifier.

## stoffu | 2019-03-22T06:05:53+00:00
@RandomRun 

> Fixing the base point H however has other advantages besides opening the door for aggregation. For instance, taking Hp(.) by itself incurs some computational costs but, more importantly, fixing the base point H allows for faster computations of double scalar multiplications, as pointed out by @SarangNoether. He is working on simulations for that, so I will let him elaborate more on that as I don't fully understand that part.

It's also important to consider the balance between the added implementation complexity and the provided performance benefit. I don't really feel like bringing external data such as the fork height and the output keys creation heights into the basic RingCT functions unless the advantage is very significant (which doesn't seem to be the case to me here).


## apoelstra | 2019-04-04T21:30:27+00:00
@SarangNoether asked me to take a look at this issue.

Here are some notes:
1. The scheme seems sound to me. Certainly, if it's not, I'll have learned some new and humbling lesson about how to think about these sorts of proofs. But I agree with everyone asking for a formal writeup before trying to deploy this!
2. As always, be careful with commitments - be sure that everything the verifier has access to goes into the µ_P and µ_C hashes, and that these are hashed in some way such that the hashed data is parseable in principle. (This is a heuristic my colleagues at Blockstream keep hammering into my head, to eliminate the risk that different things might result in the same hash. The worst offenders are variable-length lists of variable-length objects, though it looks like you have none of them here.)
3. As has been noticed, if you try to extend this trick to combining multiple inputs' ring signatures into one, you are forced to use the same index for all of them. I don't think there's any way around this, and I think the idea is DOA from a privacy standpoint.
4. Be careful using a fixed generator instead of H_p. The van Saberhagen paper says not to do this because it interacts badly with stealth addresses. (But the reasoning for this was super sketchy; I think Pedro or Tim Ruffing had a paper that formalized this and it was a giant pain in the ass.)

## SarangNoether | 2019-04-04T21:52:01+00:00
Thanks @apoelstra for looking this over. Comments regarding the notes:

1. We're working on a writeup with security proofs!
2. The commitments are currently the source of a few questions on security. To be "real" aggregated MuSig-style keys, it looks like each ring member needs a separate hash that includes the specific key at that index, as well as the entire set. The version listed right now uses the same hashes for each ring member. We can probably work up proofs for both, but I suspect the former will be much easier (though computationally a tiny bit more costly). Comments welcome on this.
3. We don't intend to use this for multiple inputs because of the common-index problem that has been noted. Multiple spends will use separate signatures, as we do now.
4. The current iteration of this scheme that's in testing uses the same key image generators as we do now (hashing the public keys). It would be nice to migrate to a fixed generator for efficiency, but the back-of-the-envelope estimates show very little benefit in verification time from doing so.

## RandomRun | 2019-04-05T03:09:06+00:00
@apoelstra Indeed it seems that using the fixed point for the key image may lead to the problem referred to in the Cryptonote 2.0 paper. Thank you for pointing that out!

I will leave it here for others reading the thread. I am paraphrasing from the section 'Notes on the Hash Function Hp', from the Cryptonote 2.0 paper:

If Alice sends two payments to Bob, whose stealth address is `(A,B)`, by picking two different random values `r1` and `r2` and forming the two one-time addresses `P1 := Hs(r1*A)*G + B` and `P2 := Hs(r2*A)*G + B`, then she might be able to connect the two corresponding key images as Bob publishes them. Indeed, if we use the fixed base point `H`, their key images are:

`I1 = (Hs(r1*A) + b)*H` and `I2 = (Hs(r2*A) + b)*H`.

Now, subtracting the two, Alice could check that:

`I1 - I2 =  (Hs(r1*A) - Hs(r2*A))*H`.

This would give Alice the ability see when those outputs were spent by Bob.

# Action History
- Created by: RandomRun | 2019-03-16T19:05:55+00:00
