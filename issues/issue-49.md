---
title: Investigate HMAC solution to nonce distribution "problem"
source_url: https://github.com/monero-project/research-lab/issues/49
author: b-g-goodell
assignees: []
labels: []
created_at: '2019-02-18T18:18:29+00:00'
updated_at: '2019-05-15T04:03:19+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Previous studies on nonce distribution for our POW algorithm suggest that our algorithm is behaving badly as a random oracle.

Suggested change:  instead of mining looking for H(block || nonce)*diff < targ, modify this to H(block || hmac(nonce))*diff < targ where the hmac is computed with some public key agreed upon by consensus, and possibly the hmac should be repeated over several rounds. hmac outputs are uniform under very weak assumptions, they are easy to compute (require a few hashes and xors) and guarantees that the input nonce to the POW hash is uniformly selected. 

ASICs may be designed with greater energy efficiency when seeking nonces that solve H(block || nonce)*diff < targ within a certain range. This hmac removes the adversarial control over the nonce.

We need to investigate the relative impact this could have on CPU miners and investigate any and all impacts this could have on the incentive structure behind mining Monero.

# Discussion History
## b-g-goodell | 2019-02-18T18:20:36+00:00
One of the papers that come to mind when this came up: https://link.springer.com/content/pdf/10.1007/978-3-642-32009-5_21.pdf

## Silur | 2019-05-03T14:19:24+00:00
Instead of selecting a common HMAC key in a concensus step, I'd advise to use VRFs. They are basically HMACS with assymetric keys, and they behave well as a RO. This way every miner has their own extra trapdoor information that is publicly verifiable to be bound on the original hash, this eliminates adversarial control.

## b-g-goodell | 2019-05-06T16:51:01+00:00
This is an interesting thought. I'm not terribly familiar with VRFs. HMACs
are very easy to implement, have strong indistinguishability properties...
and if the key is generated from a primitive polynomial (i.e. round keys in
parazoa/sponge constructions), the adversarial control over the HMAC key
shouldn't be a problem. However, if there is an easy-and-safe-to-implement
VRF with similar indistinguishability properties as HMAC (any
suggestions?), I'd be happy to drop the concensus-decided key.

On Fri, May 3, 2019 at 8:19 AM Silur <notifications@github.com> wrote:

> Instead of selecting a common HMAC key in a concensus step, I'd advise to
> use VRFs. They are basically HMACS with assymetric keys, and they behave
> well as a RO. This way every miner has their own extra trapdoor information
> that is publicly verifiable to be bound on the original hash, this
> eliminates adversarial control.
>
> —
> You are receiving this because you authored the thread.
> Reply to this email directly, view it on GitHub
> <https://github.com/monero-project/research-lab/issues/49#issuecomment-489111491>,
> or mute the thread
> <https://github.com/notifications/unsubscribe-auth/AD2ZD7XPQMF3VYU5XVGO6FLPTRCW5ANCNFSM4GYFTDXQ>
> .
>


## b-g-goodell | 2019-05-06T17:26:41+00:00
Actually, my idea as stated is dumb, whether with HMAC or VRF... and here is why... but it's fixable...

Say you have two random oracles H and G and proof of work is played by finding an input x such that H(block || G(x))*diff < targ. Then a miner merely stores G(x) into a table for many inputs x, orders the values of x linearly by their value G(x), and proceeds through the nonces G(x) by proceeding through their inputs according to the linear order. Nothing is saved, gained, or prevented, and in fact the miner is incentivized to collate a big table for G over time.

On the other hand, if H is a random oracle and G(-,key) is a family of keyed random oracles, then playing the game by computing H(block || G(x, block))*diff < targ prevents the miner from generating the table ahead of seeing the block. Of course, the miner selects the block, so it's possibly they can maliciously select stuff to mess with G(x, block). However, they still won't really be able to pre-compute a big table for any old block they want to publish, and it'd be more fruitful for them to merely play the POW game faithfully, I think.

## b-g-goodell | 2019-05-06T17:31:30+00:00
Note this is not a way around parallel computing: if G and H are both highly parallelizable, then someone with a block could compute many choices of G(x, block) and then compute H(block || G(x,block))*diff for all those choices.

## Silur | 2019-05-11T09:14:00+00:00
Here is a short version of an elliptic curve VRF, I can present a jupyter notebook PoC to one of the usual research meetings:
We want to prove that `a||privkey` hashes to `b` without disclosing b. We output `b`, and a proof.
**Public information:** 
-`g` generator, 
-`a` the public part of the input
-`H1`  hashes bitstrings to the curve,
-`H2`  hashes points to its abscissa,
-`H3`  any safe hash like SHA3
- g^x the prover's public key

**Private information:**
- `x` the private part of the input i.e the asymmetric HMAC key

**Prover**:
- `h = H1(a)`
- select uniform random scalar `k`
- `c = H3(g||h||g*x||h*x||g*k||h*k)`
- `s = k - c*x`
- output `(h*x, H2(h*x) c, s)`

**Verifier**:
- `h = H1(a)`
- `u = g*x*c + g*s  = g^k`
- `v = h*x*c + h*s = h^x`
- check that the proof has `c = H3(g||h||g*x||h*x||g*k||h*k)` and `H2(h*x)`

This construction also prevents adversaries to go ahead of the block with precomputed proofs as you modelled above. I don't know how parallelizable EC operations are now :/

## Silur | 2019-05-12T10:47:55+00:00
I've implemented the above scheme in Rust hope it can help evaluating the idea: https://github.com/Silur/ECVRF

## b-g-goodell | 2019-05-13T02:16:36+00:00
Thanks, MCC has been nuts and I will review this when I get home.

On Sun, May 12, 2019, 6:47 AM Silur <notifications@github.com> wrote:

> I've implemented the above scheme in Rust hope it can help evaluating the
> idea: https://github.com/Silur/ECVRF
>
> —
> You are receiving this because you authored the thread.
> Reply to this email directly, view it on GitHub
> <https://github.com/monero-project/research-lab/issues/49#issuecomment-491584563>,
> or mute the thread
> <https://github.com/notifications/unsubscribe-auth/AD2ZD7WXMRRYJI7R76JF37LPU7YVZANCNFSM4GYFTDXQ>
> .
>


## stoffu | 2019-05-15T04:03:19+00:00
> Previous studies on nonce distribution for our POW algorithm suggest that our algorithm is behaving badly as a random oracle.

> ASICs may be designed with greater energy efficiency when seeking nonces that solve H(block || nonce)*diff < targ within a certain range. This hmac removes the adversarial control over the nonce.

Do we really know for sure if such an efficiency gain exists? The particular non-uniform nonce distribution may be simply because of the way some miners were implemented. Your proposal may end up introducing another complexity to the protocol by "solving" a nonexistent problem.

Also, if the PoW algorithm was behaving badly as a random oracle, the correct fix IMO should be to fix the PoW algorithm itself instead of tweaking the handling of nonces.


# Action History
- Created by: b-g-goodell | 2019-02-18T18:18:29+00:00
