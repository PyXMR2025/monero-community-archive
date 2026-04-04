---
title: Replace Monero's hash-to-point function with the FCMP++ Upgrade
source_url: https://github.com/monero-project/research-lab/issues/142
author: kayabaNerve
assignees: []
labels: []
created_at: '2025-08-21T14:07:37+00:00'
updated_at: '2026-03-05T23:28:44+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Over a year ago, we discussed in a [MRL meeting](https://github.com/monero-project/meta/issues/1037) the uniformity of Monero's hash-to-point function. I raised the concern due to the complete lack of documentation and understanding, wanting to ensure the implementation was proper. In the worst case, the algorithm would presumably be biased by a few bits, reducing our security by ~2 bits.

I've spent the last ~13 hours [working on this](https://github.com/monero-oxide/monero-oxide/pull/33) and come to the conclusion our implemented hash to point is in fact Elligator. Specifically, it's the Elligator 2 map applied to Curve25519 _as detailed in Section 5.5 of the [Elligator paper](https://eprint.iacr.org/2013/325)_. This is distinct from Elligator 2 _as specified in Section 5.2 and as seen in standards_ due to a slightly different choice in the second candidate `x` coordinate.

While the oddity of a slightly different specification isn't worth pushing the issue over, now that the answer has been found, what is worth pushing the issue over is how Elligator 2 is _biased_.

> Fix r ∈ R, and write (x, y) = ψ(r). ... −ux(x+A) = −uv(v+A) = −uv(−vur2) = u2v2r2, which is a square.

The points output from Elligator 2 will only be the points whose `x` coordinates satisfy `−ux(x+A)` being square, which is only half of the points on the elliptic curve.

The solution is simply to invoke Elligator 2 twice, summing the result. This will make the bias negligible. With the FCMP++ upgrade, we'll no longer invoke a hash-to-point on historical outputs (requiring context on hold they are to determine which output to use), solely hashing them once upon accumulation (and never again). This, along with the fact it's already a hard fork, makes it a prime position to perform the upgrade during.

Additionally, we can discuss not just invoking Elligator 2 twice, yet moving to the standardized version as it'll have implementations _already available_, simplifying ecosystem development.

# Discussion History
## tevador | 2025-08-21T19:23:47+00:00
> the issue over is how Elligator 2 is biased

Is this actually something that needs to be fixed?

It seems that halving the number of points would reduce collision security by about 0.5 bits. The CryptoNote whitepaper states (p. 17):

> None of the proofs demands H_p to be an ideal cryptographic hash function.

The only reason why H_p is needed is to break the linear relationship between the key images of related keys.

Overall, I don't see much benefit in upgrading. We'll have to keep the original version in the codebase anyways, so the "upgrade" would just add needless complexity to the protocol.

## kayabaNerve | 2025-08-21T19:40:43+00:00
That isn't quite true AFAIK. In the historic proofs, it was also used as a challenge function in a way relevant to their security. That doesn't matter now as those proofs are deprecated and will be disabled with the FCMP++ upgrade, but it should be noted this function seeded the BP+ CRS which _is_ still in use.

It doesn't make sense to accept this reduction for no reason. The complexity of having a v2 should be acceptable. I can agree not to tweak it to follow standards so the v2 is trivial to implement (two calls and a point addition), but I'll note following standards would make the cryptography _more accessible_ as it'd now be compatible with existing implementations.

## tevador | 2025-08-21T21:08:51+00:00
> it should be noted this function seeded the BP+ CRS which is still in use

Are you proposing to also replace this use case, or just its usage in the key image calculation?

What are the requirements for H_p in the security proofs of FCMP++?

> It doesn't make sense to accept this reduction for no reason.

A security reduction of half a bit doesn't make any infeasible attack feasible. For comparison, our elliptic curve (Curve25519) is about 1.2 bits less secure than Secp256k1 used by Bitcoin. That doesn't mean we need to replace it.

## kayabaNerve | 2025-08-21T22:33:37+00:00
I'm proposing we replace the hash to point moving forward, and that would include for constants. The BP+ will be the only currently active constants needing to be updated that I'm aware of.

Beyond the usage for CRSs, the hash to point function primarily is used as a CRH. If someone's outgoing view key is known, the discrete logarithms of their key images can be learned but their key images can't be burnt _by a different output_ due to having a distinct generator of unknown relation.

*1.7 bits, if we only use half of our preferred curve /s

I care less about a half bit in the grand scheme of things and more about the principle, as these small issues add up. I'd prefer to draw a line in the sand here. We know this isn't a proper hash function. We can say it's acceptable, but we also can fix it. With the FCMP++ upgrades, nodes only hash the output keys for their key image generators once when accumulating into the tree. We can likely easily set all TXs with CARROT outputs to use the unbiased hash to point function and new BP+ generators. Yes, having a v2 here is technically more complex, but it's proper practice and shouldn't be a practical issue. If we go one small step further (updating the second candidate to follow the paper's specification), we'd also immediately inherit all successive analysis of Elligator (the implemented variant is presumably a remnant of an earlier draft of Elligator with similar properties and effectively the same arguments in the long run, though this would have to be confirmed) AND support from all libraries implementing the standard. This would _reduce_ the burden of external implementations working with Monero in the furture.

Sorry for repeating my already stated points a bit here. I am just strongly opinionated on fixing this (though I can be swayed either way on updating the implementation to the standard).

## tevador | 2025-08-22T14:52:58+00:00
There are two separate use cases for "map to curve":

1) To deterministically generate a point on the curve which has an unknown discrete logarithm relationship to other points.
2) Random oracle.

The current H_p used by Monero meets 1) but does not meet 2).

If there is evidence that a random oracle like behavior is required for our security, I would be in favor of upgrading. Upgrading just for "the principle" is not something I would recommend.

## kayabaNerve | 2025-08-22T16:05:14+00:00
As I stated, we also require a collision-resistance functionality which is harmed by how this maps two distinct inputs to one singular output.

But I hear you and respect if we won't agree on how to move forward. I asked it to be discussed at the next MRL meeting if you'd like to attend there :)

## iamamyth | 2025-08-22T17:17:57+00:00
Would a new function introduce branch complexity, or can you make a clean break? In other words, do you propose introducing conditionals to determine which function to use, or does the choice of function depend solely on context, such as the FCMP++ libraries using the new function (even if those libraries, in turn, are of course gated by the hardfork)?

## tevador | 2025-08-22T17:59:00+00:00
> As I stated, we also require a collision-resistance functionality which is harmed by how this maps two distinct inputs to one singular output.

The imperfect map to curve still has 125.3 bits of collision resistance, as opposed to 125.8 for the map that covers the whole curve.

There are cases when half a bit bias would have a significant impact on security (such as when generating nonces for digital signatures), but I don't think that applies here.

## kayabaNerve | 2025-08-22T18:41:57+00:00
As a correction, the formula for the second candidate _is_ equivalent to the one in the specification in 5.2. That's why both are mentioned in the same location. Credit to @boog900 for noticing this.

We use the specified Elligator map already and there's no reason off-the-shelf implementations can't be used if they have matching behavior for the sign bit. The present code converts the choice of candidate into if the odd/even Edwards X coordinate is taken (approximate to the paper, though the paper technically uses it to determine if a normalized choice of sqrt for the Curve25519 Y coordinate should be negated). The IETF specification uses the sign of the input (dropped when squared) to determine the sign of the output. `curve25519_dalek` appears to use the 256th # bit of a hash's output to determine the sign of the output.

---

Any place we perform a call to hash-to-point function, it'd need the context of if FCMP++ or not. Within the FCMP++ code? Sure, we can simply call the new function and be done with it. We'll probably need conditionals (or to wrap the function into one which accepts an argument for which variant to use) elsewhere however.

## tevador | 2025-08-22T18:59:22+00:00
> Within the FCMP++ code? Sure, we can simply call the new function and be done with it.

I don't think that's true. When building the FCMP tree, old outputs will have to be hashed with the old hash function, otherwise double spends are trivially possible.

It gets even more complicated due to the fact that there will be a 720-block window when both RCT and FCMP transactions are allowed.

## kayabaNerve | 2025-08-22T20:18:42+00:00
> Within the FCMP++ code

By this, sorry, I meant within the FCMP++ libraries which solely and exclusively work to the effect of FCMP++. This would be regarding sampling the CRS for the FCMP and so on. After that, I don't actually believe we invoke the hash-to-point function as we largely rely on the value within the tree..

You're right the FCMP tree building code (which is implemented within Monero's C++, and why I didn't think of it) will have to be informed of if the output is a CARROT output or not to determine which to use for the key image generator.

## j-berman | 2026-02-25T02:13:30+00:00
Note, @kayabaNerve provided more context in this MRL meeting https://github.com/monero-project/meta/issues/1261 to which @tevador ack'd its stronger reasoning in support of this proposal:

> 

    < tevador > I think we should investigate and also model worst case attacks. I think even if you can find a collision in Hp, I don't think it implies you can burn an ouput.

    < k​ayabanerve:matrix.org > See jberman, jeffro256 noting we have the perfect spots to deal with this.

    < k​ayabanerve:matrix.org > It does because if you have the outgoing view key.

    < k​ayabanerve:matrix.org > You can create two outputs with the same discrete logarithm for their key image, and then you solely need a key image generator collision to perform a burn.

    < tevador > For RCT it does not imply burning an output. I'm not very familiar with Carrot.

    < k​ayabanerve:matrix.org > It's an FCMP++ comment, not a CARROT comment. You're right for RingCT.

    < tevador > If FCMP is more vulnerable than RCT, the update can make more sense.

    < k​ayabanerve:matrix.org > FCMP++ allows users to publish what were RingCT private spend keys and are now FCMP++ outgoing view keys for newly created wallets.

    < k​ayabanerve:matrix.org > The only reason that's safe is because the key image generator is a CRH binding to the outgoing view key and the private spend key.

    < k​ayabanerve:matrix.org > See the difficulties Seraphis had with the burning bug, leading Seraphis to define the outgoing view key as a point and a scalar whose ratio formed the linking tag.

    < tevador > ^ I don't think this was mentioned in your proposal on github. That's a pretty strong point.

    < k​ayabanerve:matrix.org > I did say we require it to be a CRH to stop the burning bug 😅

    < k​ayabanerve:matrix.org > But I'm sorry I didn't provide sufficient context/background on that


## vtnerd | 2026-03-05T16:57:15+00:00
I'm bumping a really old discussion, but I missed a subtle point previously. Doesn't this create two anonymity pools in fcmp++? This seems rather unfortunate.

## kayabaNerve | 2026-03-05T23:28:44+00:00
No. The items within the anonymity pool are triples of `(O, I, C)`. This changes the derivation of `I` _before_ insertion into the singular anonymity pool.

# Action History
- Created by: kayabaNerve | 2025-08-21T14:07:37+00:00
