---
title: Linkable Ring Signature based on 1-Out-of-Many, no sender-detection
source_url: https://github.com/monero-project/research-lab/issues/56
author: RandomRun
assignees: []
labels: []
created_at: '2019-09-06T07:21:51+00:00'
updated_at: '2019-10-07T19:31:42+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Hi all.

I was reading the Lelantus paper to try to figure out a way to mitigate the sender detection problem with its key image format while retaining the good scaling properties, and ended up reading the One-Out-of-Many Proofs paper, which is one of its main components. I think that maybe the 1ofMnay construction could be used to yield another linkable ring signature using linking tags similar to current Monero key images, and that, due to their use of `Hp(.)`, cannot be detected by the sender.

Here is my summarized understanding of what the One-Out-of-Many Proofs do, based on [this version of the paper](https://link.springer.com/content/pdf/10.1007%2F978-3-662-46803-6_9.pdf) (mostly pages 11 through 14):

The proof takes in a collection of `2^n` points, such that, at a position `l`, is of the form `c_l = g^r` (for some secret `r` known only to the prover), and allows the prover to convince the verifier of his knowledge of `r` by producing a point whose discrete log wrt the base point `g` is:

`z_d := r*x^n + sum(\rho_k*x^k for k in [0,n-1])`.

Notice that the value of the other commitments `c_i` do not affect the value of `z_d`. It only depends on `r` and the `\rho_k`'s which were chosen randomly by the prover. Any contribution from the other `c_i`'s only seem to affect only the `c_dk` values, and those contributions are removed during the proof.

As the paper mentions, producing such `z_d` in this manner can already be viewed as a (non-linkable) ring signature.

**Modified linkable scheme:**

Now consider what would happen if we formed the auxiliary ring `(Hp(c_i))`, for `i` in `[0,2^n]`. At position `l` we have `Hp(c_l)`, and if we could prove that the discrete log of that point with respect to some other point is also `r` using the same parameters as the first proof, then they both would output the same `z_d`! And indeed, the point `J` that satisfies `DL(Hp(c_l), J) = DL(c_l, g) = r` is `J := Hp(c_l)^(1/r)`, which is unlinkable to `c_l`.  `J` will be the linking tag which, in the context of transactions, will be used to prevent double spend.

At the beginning of the proof the prover provides `J` to the verifier, so they know to run the first part of the protocol wrt to `g` (and stop right before the verifier would select `x`) and then repeat the procedure, replacing `g` by `J` everywhere it occurs, but keeping the same parameters `r_j, a_j, s_j, t_j` and `\rho_k`. (In fact, the values `r_j, a_j, s_j` and `t_j` are only used to show that the index `l` committed is indeed a sequence of zeros and ones of size `n` and therefore this may be run only once to compute the `f_j`'s, which are just numbers. Indeed, it looks like the only thing that will incur an extra cost is computing the new `c_dk`'s.)

Once once that is done, the random oracle picks a single random challenge value `x` that should be used in the two proofs. And if the prover has acted honestly, then the two values of `z_d` will match. (Correctness)

If the prover messes with the `\rho_k`'s or `r` (when defining J) then, since the `z_d`'s will be different polynomials in `x`, the chance of the `z_d` values coinciding will be negligible. Also the index `l` will be the same, provided that the same `f_i`'s are used in both proofs (otherwise the same signer could produce multiple linking tags), so making sure that this happens is an important part of the verification. (So it seems plausible to me that this scheme will be unforgeable too, but it still requires proving, of course)

Please let me know what you think.

# Discussion History
## SarangNoether | 2019-09-06T18:21:19+00:00
It's not clear to me if this could be directly adapted to Lelantus, since it uses double-blinded commitments (one term for the value and the other for the standard blinder). In particular, the Lelantus modification to the Groth 1-of-N proof no longer shows that the prover knows a single value `r` such that `C = rG`, but instead that the prover knows two values `v` and `r` such that `C = rG + vH` (the generator notation is different in the paper). Therefore it wouldn't be possible to select a single point for which the same discrete log is known to the prover.

Was there another application you were considering that does a more "traditional" approach to linkable ring signatures and would also permit proving transaction balance, as Lelantus does?

## RandomRun | 2019-09-06T21:13:06+00:00
Indeed, what I am describing is not a proposed modification for Lelantus, just something that occurred to me while examining one of its components, the One-Out-of-Many Proof protocol. The way I stated it may have suggested that it was a modification to Lelantus, but I meant to say it is a modification of the RS scheme found in the 1ofMany paper.

Indeed, all I did was try to map out the components of an LSAG into the ring signature proposed in the 1ofMany paper so as to make it linkable and with a similar key image format currently used in Monero (i.e. involving `Hp(.)`) so that the sender can't do any algebraic tricks to figure out that a certain output he created is being used.

**A possible approach for transaction balancing:**

The way I am thinking about incorporating amounts into a transaction model that incorporates this scheme is just create coins that are pairs `(P, C)`, where the first point `P = p*G` is the one time address used to sign off the amount `a` contained in the Pedersen commitment `P = a*H + m*G`, where `m`is the mask. 

In order to spend this money, form a list of `N=2^n` coins from the blockchain, `((P_i, C_i))` for `i` in `[0, N]`, such that `(P, C) = (P_l, C_l)`, for some `l` in `[0, N]`.

Next, decide on new outputs to be created, `(Q_k, D_k)`, where `D_k = a_k*H + m_k*G` and `Q_k`'s are one-time-addresses, say for `k = 1, 2'. Range proofs as usual.

**The signature:**

First let `D = D_1 + D_2`, and set the ring `(P_i, Hp(P_i) , C_i - D)`. Now we can apply the LRS to the first two components, and a regular 1ofMany proof of knowledge of a commitment to zero. 

(For what it comes next, it may be worth looking at the protocol illustrated in figure 2, page 14 of the paper linked above. Also we are going from additive to multiplicative notation.)

As mentioned before, to ensure that all the relevant computation happens with the corresponding points at the same index `l`, it should suffice to pick the parameters `r_j, a_j, s_j, and t_j` once, derive the values `p_ik`'s and `f_j`'s and stick to them for all computations, that is for the LRS and the commitment to zero proof.

The values of `rho_k`'s need to remain the same for computing the `c_dk`'s for the signing key and its linkability tag components, but new `rho_k`'s can be (probably should be) picked for the proof that one of the amount commitments is a commitment to zero.

After all those have been picked, the random oracle picks a challenge `x` that should work for all the proofs in order to validate. 

**Analogous behavior:**

These are just some parallels that I found interesting.

In LSAGs, the verifier is convinced that the commitment is to zero by verifying a signature from it.
In the LRS from 1ofMany, it does the regular 1ofMany protocol.

In LSAGs, we ensure that the signing key, is processed along with its corresponding linkability tag and Pedersen commitment buy aligning them in the verification steps. 
In the LRS from 1ofMany and its corresponding amount, we ensure that they are processed together by using the same `f_j`, which are the masking of their index `l`.

In LSAGs, the verifier is convinced that the key image is correct by looking at two equations, on different base points, that have the same coefficient relations. This is achieved by using the same coefficients `s_0, ..., s_N-1` for both equations, and picking values `h_0, ..., h_N-1` that work for both of them.
In the LRS from 1ofMany, the verifier is convinced if the two proofs output the same `z_d` values.This is achieved by using the same `rho_k` values.

In LSAGs, in the linking component, the prover provides a linking tag `I` and uses it as a "public key" to complete a signature on a certain base point. Those range points will range over `Hp(P_i)`'s, and wherever `DL(I, Hp(P_i)) = DL(P_i, G)`, that is where the signer closes the ring.
In the LRS from 1ofMany, the linking computation uses a linking tag `J` as a "base point", letting all the possible signing keys range over `Hp(P_i)`'s. The signer is able to sign if `DL(Hp(P_i), J) = DL(P_i, G)`. Those equations are teh reason why we define `I := r*Hp(P_l)`, but `J := (1/r)*Hp(P_l)`.











## SarangNoether | 2019-09-09T14:59:00+00:00
This idea could be extended to the multi-input case as well, of course. If I'm doing my counting correctly, a 2-input set of proofs (not including the necessary intermediate commitments used to show balance) would occupy 4.1 kB for N=128, and 5.3 kB for N=512. Verification is linear in the size of the anonymity set as usual, but commitments could be reused across inputs, and non-commitment generators can be reused and cached for faster batching operations.

## SarangNoether | 2019-09-10T18:45:51+00:00
Here is some basic [proof-of-concept code](https://github.com/SarangNoether/skunkworks/tree/lrs/lrs) for this idea. It's only for research, so don't use it for any production purposes.

## RandomRun | 2019-09-12T18:19:44+00:00
Intuitively, this protocol should perform no worse than running 1ofMany three times: one for the signing keys, another for their linking components, and a third for the amounts. Of course, it already does less than that, since some of the computation is done only once already. So I was considering whether we can make the proof even more compact by adapting the CLSAG idea to this construction, that is: signing with a linear combination of the controlled keys, along with their corresponding keys w.r.t. the linking component. If this works here, then there would be one less set of `c_dk`'s to be communicated, which would reduce the proof size.

Indeed, we are proving that for some index `l`, `P_l = r*G`, and `Hp(P_l) = r*J`, for `J := (1/r)*Hp(P_l)`. Note that, in this construction, `Hp(P_l)` is viewed as a public key w.r.t. the base point `J`, whereas in regular MLSAGs it is `I` that is a public key w.r.t. the base point `Hp(P_l)`. With that in mind, the analogous thing to do here is to use `Hp(P_l)` in the linear combination (and not the linking tag as in the original CLSAG).

Using the above notation for the amount commitment to zero, i.e., if `D_1` and `D_2` are new amount commitments being created and `D := D_1 + D_2 + fee*H`, then `D_l := C_l - D` is a commitment to zero. Say `D_l = y*G`, for some `y`. That means that if the prover defines the point `D' := y*J`, and pass `D'` along with `J` to the verifier, he will be able to prove, using 1ofMany, that:

`DL(Hp(P_l) + D', J) = DL(P_l + D_l, G) [= r+y] `, for some index `l`.

As before, this is insecure, so we require instead that the above relation be satisfied for any random linear combination for those keys. That is, for any scalars `a, b`:

`DL(a*Hp(P_l) + b*D', J) = DL(a*P_l + b*D_l, G) [= a*r+b*y] `, for some index `l`.

In practice, of course, `a` and `b` will be given by a random oracle query including all involved points: `P_i`'s, `Hp(P_i)`'s, `J` and `D'`.

What do you think?

## SarangNoether | 2019-09-13T17:51:56+00:00
The algebra seems to check out.

## RandomRun | 2019-09-29T23:42:24+00:00
I believe we may be able to sign with several outputs at once, using a single ring! Please let me know what you think. (The starting point for what is suggested below is before the CLSAG-like ideas from my previous comment, so I suggest ignoring my previous comment on first reading this one. I haven't checked how the two might go together yet.)

**Recall:**

Let `l = (l_1,..., l_n)` be the fixed index of the signer's public key. In the 1ofMany Proofs and the scheme proposed above, we use the fact that the polynomial 

`p_i(x) =  Prod(f_{j, i_j} for j in [1,n+1])` 

is monic of degree `n`, if `i = l`, but has degree strictly smaller than `n`, otherwise. This allows the signer to subtract away anything coming from the points it doesn't control, but crucially not the one it claims to know the discrete logarithm. (The dividing away done in the 1ofMany paper becomes subtracting away in additive notation which I am using.)

**Example: signing with two keys from the same ring:**

Suppose that the signer happens to also own another public key in that ring, of index `m = (m_1,..., m_n)`. (It follows the same procedure to commit to the digits of `m`, as done with `l`, and forms the corresponding `f_j`'s. In order to distinguish the `f_j`'s for `l` from those from `m`, I will use the more explicit notation below, I hope it is clear.) Following the same reasoning as above, it could set the polynomial:

`p_i(x) =  Prod(f_{i_j, l_j} for j in [1,n+1]) + Prod(f_{i_j, m_j} for j in [1,n+1])` 

which is monic of degree `n`, if `i = l` **OR** if `i = m`, but has degree strictly smaller than `n`, otherwise. 

So after subtracting away all contributions from the keys not controlled by the signer, it can use its knowledge of the discrete logarithm of those two points to produce a `zd` that will be the discrete logarithm of the final sum w.r.t. the base point.

Indeed, if  `P_l = rl*G` and `P_m = rm*G`, and if we don't modify anything other than the steps to commit to the new index and for its `f_j`'s, then 

`zd = (rl + rm)*x^n - Sum(\rho_k*x^k for k in [0, n])`.

This by itself seems like a plausible way to prove ownership of two of the keys in the ring. 

**Involving the linking tags:**

As before, consider the corresponding ring of "public keys" `[Hp(P_i) for i in [0, N]]`. They are viewed as "public keys" in the sense that, for instance `Hp(P_l) = rl*Jl`, where `Jl := (rl)^{-1}*Hp(P_l)`, and `Hp(P_m) = rm*Jm`, where `Jm := (rm)^{-1}*Hp(P_m)`.

Here we have to take the single `zd` above and split into two values, `zl` and `zm`. In order to do that, let the signer sample `\rho_l,k`'s and `\rho_m,k`'s and define `\rho_k := \rho_l,k + \rho_l,k`, so that:

`zd = zl + zm `
` =  rl*x^n - Sum(\rho_l,k*x^k for k in [0, n]) `
` + rm*x^n - Sum(\rho_m,k*x^k for k in [0, n])`.

This break down of the discrete logarithm in two will be important for the linking component below, after we properly define their `C_dk`'s. Indeed, whereas for the signing component we had: 

`C_dk = Sum(p_ik*P_i for i in [0, N]) + \rho_k*G`,

for the linking component need to we use:

`C_dk := Sum(p_ik*Hp(P_i) for i in [0, N]) + \rho_l,k*Jl + \rho_m,k*Jm`.

The final summation becomes:

`Sum(Hp(P_i)^pi(x) for i in [0,N]) - Sum(x^k*C_dk for k in [1,n])` 
`=  (rl*x^n - Sum(\rho_l,k*x^k for k in [0, n]))*Jl`
` + (rm*x^n - Sum(\rho_m,k*x^k for k in [0, n]))*Jm` 
`= zl*Jl + zm*Jm`.

The verifier, initially receiving `Jl, Jm` from the prover and later (after the challenge `x`) receiving `zl, zm`, can check that the signing component sum comes down to `zl*G + zm*G` and that the linking sum is also `zl*Jl + zm*Jm`.

**Getting amounts involved:**

Suppose we have amount commitments associated with every key in the ring, so that in fact the ring looks like this: `(P_i, C_i) for i in [0,N]`, such that `C_l = yl*G + al*H` and `C_m = ym*G + am*H`, for amounts `al, am` and masks `yl, ym` known to the signer.  

If we reuse the `pi(x)`'s for the ring of amount commitments (and new `\rho_k`'s), so that the proper commitments get picked up, and we subtract the contributions of the other points, then the final sum will be a new commitment:

`C_f := x^n*C_l + x^n*C_m - Sum(\rho_k*x^k for k in [0,n])`
` = (x^n(yl + ym) - Sum(\rho_k*x^k for k in [0,n])*G`
` + x^n*(al + am)*H`.

In other words, passing a ring of amount commitments through this algorithm will produce a new commitment to the sum of the amounts of the selected commitments, multiplied by `x^n`.

But this is good, because if the signer commits to the amount commitments it wants to create, say `D = D1 + D2 + fee*H = w*G + (al + am)*H`, before starting the proof, then, at the end all it has to do is to prove that `C_f - x^n*D` is a commitment to zero, which it is!











## RandomRun | 2019-10-02T04:37:54+00:00
Another thing is that we may not have to communicate separately all the different `C_dk`'s for the signature, linking and amount components. Instead, it may be possible to just add all the three up in one single sum and add all the `C_dk`'s together as well, reducing communications costs. In this approach, the verifier would just compute the sum (which is the sum of all three components above):

`S := Sum(pi(x)*( P_i + Hp(P_i) + C_i) for i in [0,N]) - Sum(x^k*C_dk for k in [0,n])`,

where:

`C_dk := Sum(p_ik*(P_i + Hp(P_i) + C_i) for i in [0, N])`
`+ \rho_k*G + (\rho_l,k*Jl + \rho_m,k*Jm) + \rho_a,k*G`.

The final sum `S` will then be of the form 

`S = (zl+zm)*G + (zl*Jl + zm*Jm) + C_f`.

So, defining `C_f := S - (zl+zm)*G + (zl*Jl + zm*Jm)`, as before, all the prover has to do is to show that `C_f - x^n*D` is a commitment to zero.



## SarangNoether | 2019-10-07T19:31:42+00:00
This commit contains some initial (and probably not secure) code to prove knowledge of openings to multiple commitments, along with the correct construction of the corresponding linking tags: https://github.com/SarangNoether/skunkworks/commit/f0a1e1aaf3e39e0d83a4e0a247e05e1f5d537455

# Action History
- Created by: RandomRun | 2019-09-06T07:21:51+00:00
