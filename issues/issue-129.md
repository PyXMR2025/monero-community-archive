---
title: Add explicit support for a worthwhile PCN design
source_url: https://github.com/monero-project/research-lab/issues/129
author: kayabaNerve
assignees: []
labels: []
created_at: '2024-11-29T22:54:05+00:00'
updated_at: '2025-05-24T10:48:46+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
FCMPs++ enable transaction chaining, and with it, certain atomic swap/payment channel designs. This ends the tradition of a new paper claiming to support Monero, only because it assumed we support signing child transactions before parents (when we don't currently), and not actually supporting Monero.

I don't believe the posited PC designs which only require transaction chaining are actually good and would end up used? I believe they simply exist as a conquering of cryptography and problem solving?

I believe Monero should evaluate PCN (payment channel network) designs and their requirements. Then, the ones with non-viable requirements should be eliminated. Then, the remaining ones should be evaluated on their practicality to use and practicality to implement.

I'd like to open the discussion by providing the construction of timelocks.

We can, with transparent timelocks, add an extra element to the output tuple. That increases the cost of growing the tree non-trivially as we do 33% more hashing on the initial layer.

Within the FCMP, currently passed the tree root from the reference block, we'd also pass the reference block number. We'd require a 32-bit range proof for the reference block number minus the output tuple's timelock, proving it to be a positive number.

Please note the existing tree can be ported as-is. It'd simply have the output tuple's timelock generator set with a zero coefficient for all existing leaves. We'd just have the annoyance of using generators 0..=2, 3..=5 for OIC and generators 6,7 for their timelocks (the generators ae currently allocated off a straight tape, shifting to using 0..=3, 4..=7 would break the layout for existing leaves). Then the growth cost is paid as prior described.

This is actually simple and cheap except for the additional tree growth cost, and if we adopt Curve Forests in the future (n trees instead of one tree), all trees would suffer this additional 33% cost on the leaf layer.

This restores the existing (deprecated) timelock behavior. This has many issues (lack of privacy, accidental misuse, doesn't enable atomic swaps/PCNs) and was deprecated for a reason.

I first tackle the issue of privacy. We embed the timelock into the output key itself, committed to with the new generator `W` (`T` is already a label in-use). This modifies `O` to `x G + y T + z W`, where `z` is the timelock block. This does not require any modifications to the tree layout. All existing outputs without a timelock are modifed as-is. All existing outputs with a timelock have their output key modified with the necessary `z W` component using a variable-time 32-bit double and add (quite cheap and will be infrequent)

The $\tilde{O}$ component of the input tuple is not allowed to have a non-`G`/`T` component. The spend-auth and linkability proof will fail to open such a $\tilde{O}$. This ensures the $\tilde{O}$ in the input tuple does not have one.

Before passing it to the FCMP, the $\tilde{O}$ is increased by the reference block number scaling `W`. Then, inside the FCMP, we no longer check that $O$ plus the re-randomization equals $\tilde{O}$. We check $O$ plus the re-randomization plus a positive 32-bit number equals $\tilde{O}$. This is done via a 32-bit range proof, an application of the divisor gadget (7 multiplicative constraints), and one more addition (3 multiplicative constraints if incomplete point addition, which I believe we can get away with). That would be 42 constraints in total (11% of the existing amount, likely possible with a reduction of the target set size to some other acceptable number).

This achieves a private instantiation of the existing timelock structure, has minimal migration costs (and doesn't require a queue like the current plan, which is so painful we have #125), and doesn't incur any additional costs with building the tree.

Instead of requiring the lock be satisfied, we can introduce an additional bit (one multiplicative constraint) for if the lock isn't satisfied. If the lock isn't satisfied, we'd negate the y-coordinate of the timelock difference proved for in-circuit and continue (which still verifies the timelock was correctly defined).

Now that we have a bit for if the timelock has been satisfied, we can define conditional logic for it. In each FCMP, we can verify proofs `X = x G`, `A = a T`, `B = b T`, and then check the output is defined as $O = X + A + B + z W$. We then check if the input tuple is $\tilde{O} = X + A$ (ignoring the tweak by the reference block scaling `W` and the re-randomization) if the timelock has yet to be satisfied or $\tilde{O} = X + B$ if the timelock has been satisfied (again ignoring the aforementioned tweak and re-randomization).

The cost of verifying the three proofs of knowledge is the expensive part. With Selene, the curve used for the first layer, we can efficiently perform the Schnorr Proof of Knowledge verification equation for Ed25519 (17 or 19 multiplicative constraints). We can't efficiently perform a SHA2/Keccak/Blake2 hash for the challenge. We can do a Pedersen hash of R, A (the PoK's nonce, key), but we'd have a Selene point as the output. Converting that to an Ed25519 scalar nicely would require a Bulletproof on a curve which towers Selene yet is defined over Ed25519's scalar field's prime (presumed infeasible). We could use an arithmetic hash, which would be a security concern and ~70 arithmetic constraints, but would produce a Selene scalar. We'd have to argue a Selene scalar is sufficiently uniform for a Schnorr PoK (likely true, Schnorr signatures work with half-width challenges) or sample multiple Selene scalars to achieve a wide reduction. Alternatively to an arithmetic hash, we can cycle the Selene PVC with Helios such that it becomes a Selene scalar. This introduces no new cryptographic assumptions, and minimizes multiplicative constraints, but requires committing to all the variables for the divisors.

Please note the costs wouldn't double if we verified three Schnorr signatures. There's optimizations we can make here. I'd guess the entire conditional key selection to be possible with as few as ~84 multiplicative constraints, and take as many as 210 in the worst case.

Please also note that if we raise the 'compute factor' to minimize bandwidth, we're growing the amount of multiplicative constraints we pay for (to reduce the amount of commitments necessary) but we aren't actually using those constraints under current proposals. The space opened by even a factor of 2 would almost certainly be sufficient to cover this scheme entirely (ignoring the additional variables it needs committed to, which will require a few more commitments).

Normal transfers can define `O` as they do now. The spender would define `a`/`b` however they want at time of spend, so long as they sum to `y` (including `a = 1, b = y - 1`). Timelocks to only allow funds be spendable after a certain point in time aren't possible under this extended proposal as a proof of knowledge is required for the key to-be-used prior to timelock expiry. Someone wishing to timelock their coins would have to erase that secret from memory themselves yet could never offer cryptographic proof of its unspendability (a TEE could be used here though). Since I don't care for that use-case, I don't offer further commentary on it.

Apologies for any typos/ill-formatting. I typed this up on my phone while out of office.

# Discussion History
## kayabaNerve | 2024-11-30T00:14:22+00:00
This design also prevents scanning timelocked outputs (preventing griefing merchants who forget to check). You'd need to explicitly note such outputs or attempt to factor the W component if you find a potentially yours output (cc @jeffro256, CARROT, how you confirm an output is targeted at you via the amount commitment even if you don't know how to spend it yet and may never learn how to spend it).

Alternatively, we can spend 4 bytes encrypting the timelock used.

## kayabaNerve | 2024-11-30T04:11:58+00:00
We may not need the range proof at all for the private timelock proposal. https://gist.github.com/kayabaNerve/acdcd641fd930546ecd87743b06b37d8 posits a range proof premised on how exactly our scalar multiplication gadget (premised on divisors) works. Interpolating points (the 256 powers of 2 for a 256-bit scalar multiplication, the 32 powers of 2 for a 32-bit scalar multiplication) produces a divisor of length respective to the amount of points interpolated.

By performing the scalar multiplication for `z W` in-circuit, if we limit the divisor to length 32 and allow interpolating the 32 powers of 2, the highest scalar which can be proven for (in effect) is 32 * 2**32. This is outside the 32-bit range but is still valid as a positive number for the necessary use here.

Unfortunately, this idea requires formally proving that one can not create a shorter divisor which interpolates more points (mapping out any special cases which may exist in the underlying algebra). That's a pain, but this idea can be done in as few as 10 multiplicative constraints if that clears. We can forgo that academia if we pay the multiplicative constraints for the explicit range proof.

---

If we have the challenge for the Schnorr signature as a Selene scalar, we need to scale an Ed25519 point with it. We can't have the user provide the bit decomposition and simply check that the two are equivalent. Without explicit bits (1 multiplicative constraint each, +256 multiplicative constraints in total, which at least doubles the estimate and makes the optimal case roughly four times larger), for the Selene scalar `c`, the prover can find `d` such that `c' = c + d * l` where `c' % p = c`, `l` is the order of Ed25519, and `p` is the order of Selene. Despite the proof over Selene verifying a congruent challenge was used (per Selene), the prover actually used an arbitrary challenge `c'` over Ed25519.

We can avoid these extra bit commitments with the same premise as we can avoid the range proof. With our current scalar multiplication gadget, while the prover can malleate via `c + d * l`, they then have to build a divisor interpolating the 256 powers of 2 to achieve that discrete logarithm. That limits the choice of `d` to less than 256 (`c + 256 * l` requires interpolating the point for 2**255 more than 256 times, and since the divisor is only allowed to interpolate 256 points...). Then we solely have to argue that even with 256 choices of the challenge, that doesn't offer enough of an advantage to break the security of the proof of knowledge.

---

All of this issue is rough notes on a few different topics. In order to move forward with the original premise of this issue (a worthwhile PCN), a survey of PCN designs, features, and requirements would have to be conducted. The building blocks here are interesting but there must be something they build to for they themselves to be worthwhile. I also apologize for my notes being a bit rough. I'm sure some work/refinement is needed for proper understanding (without prior knowledge of all the things already worked on and discussed for FCMPs++) and for notational accuracy.

## kayabaNerve | 2024-12-04T22:34:52+00:00
I proposed squashing the two keys which would be conditionally selected. That loses the information on which would be eligible prior to timelock and which after. We can require the key before the timelock have a square root provided. After the timelock, we require the key + 1 have a square root provided. Then, the two participants in the protocol can require the keys for before/after have/don't have the necessary square roots.

## josephSummerhays17 | 2025-02-20T05:08:40+00:00
What makes you think transaction chaining based protocols wouldn't be used? Where can I read more about these protocols?

## adapt-L | 2025-05-24T10:48:45+00:00
Is this discussion still open? I'm not very experienced (I can't speak to the cryptography), but i've been reading about payment channels on bitcoin. 

One thing they discuss in the bitcoin network is having a separate "uncongested block height"/timestop feature (https://lightning.network/lightning-network-paper.pdf#subsubsection.3.3.1) that delays timelocks when blocks are full to improve security of payment channels in the context of flooding attacks. You basically keep track of a separate block height that you stop incrementing when the blocks are full, and evaluate the "sequence number" in terms of this other block height. In bitcoin, it's not practical because it relies on miners acting in good faith to report the status of the mempool.

Monero, however, could take advantage of this idea due to the dynamic block size. You can just assume that blocks are congested when the block size is growing. So if you include block height as an input to transactions, then you may want to use this "uncongested block height" mechanism instead, or something like it instead of the actual block height.

I agree with your stance on TEEs. In general, TEEs are only practical for securing a small amount of funds, and in the case of payment channels you want to have a lot of liquidity in each channel.

# Action History
- Created by: kayabaNerve | 2024-11-29T22:54:05+00:00
