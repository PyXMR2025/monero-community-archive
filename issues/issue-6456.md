---
title: 'Proposal/Request: Update Supplementary Transaction Content'
source_url: https://github.com/monero-project/monero/issues/6456
author: UkoeHB
assignees: []
labels: []
created_at: '2020-04-16T21:38:22+00:00'
updated_at: '2021-07-26T23:04:28+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
# Proposal/Request: Update Supplementary Transaction Content

Monero is constantly being improved, which is fun and frankly amazing. Discussion and research has been ongoing over the past months (see MRL Issues [#61](https://github.com/monero-project/research-lab/issues/61), [#62](https://github.com/monero-project/research-lab/issues/62), [#71](https://github.com/monero-project/research-lab/issues/71), and [#73](https://github.com/monero-project/research-lab/issues/73)) on some relatively minor transaction details, and at last there seems to be a clean path forward. Ideally all the changes proposed here would be rolled out in the same hard fork.

UPDATE 1 (April 17, 2020): Added 48-byte Schnorr proof as an alternate Janus mitigation.
UPDATE 2 (April 17, 2020): Added change_tag option for 48-byte Schnorr method.
UPDATE 3 (April 18, 2020): Added key points from my discussion with @knaccc about which 48-byte Schnorr Janus mitigation approach is better (change address designation vs 6-byte change_tag). Reduced change tag from 8 bytes to 6 bytes.
UPDATE 4 (April 23, 2020): Converted change tag into blinding factor for encrypted amount, reducing additional bytes required to 0. Deprecated change address based on this improvement (go to edit log to view previous iterations of this proposal).
UPDATE 5 (May 21, 2020): Added 'implementation guideline' at the end, since there is a lot going on in this proposal.
UPDATE 6 (May 24, 2020): Reworked proposal to improve readability, and removed all 'options'/ambiguity (e.g. removed Janus base key method).
UPDATE 7 (May 26, 2020): Improved Janus proof so transactions with >2-outputs only need 32 bytes per output instead of 48 (still need a 48-byte proof for 2-out tx).
UPDATE 8 (May 26, 2020): Replaced Janus proofs with encoded transaction private keys, so 2-out tx only need 32 bytes, and >2-out tx need 32 bytes per output (simplified version of UPDATE 7). Moved 2-out tx change output discovery mechanism to a hidden tx private key, returning amount encoding to its normal form. Reordered proposal so view tags (part 2) are introduced before the Janus mitigation (part 3), since the latter now relies on the former.
UPDATE 8 (June 4, 2020): Noted an alternative to 'hidden tx private keys' for identifying change outputs in 2-out tx. Namely, we could use a change-out-specific derivation-to-scalar.
UPDATE 9 (January 22, 2021): Noted that Janus mitigation can be reduced to 16 bytes if transaction private keys are derived from a 16-byte nonce.



## Introduction

tl;dr

1. Improve transaction indistinguishability: enforce one format for the extra field (sorted TLV), enforce one tx pub key for 2-out tx and one tx pub key per output for >2-out tx.
2. Reduce scanning time (how long it takes to check each output on-chain to see if we own it): add a 1-byte view tag for each output in a tx.
3. Mitigate the Janus attack (a way to associate subaddresses made from the same private keys): encode the transaction private key and record it in transactions.
	a. There must be a change output in each 2-out tx. A special 'hidden' transaction public key is used to differentiate change and non-change outputs in 2-out transactions. For efficiency, this relies on a unique construction for view tags in 2-out tx.
4. Reorganize transaction structure: all non-optional features should be outside the extra field, so add a `tx_supplement` section to transactions (should contain: tx pub keys, Janus proofs, view tags)


### Introduction Part 1: Extra Field

A thorny issue for Monero is the extra field, which is a completely unregulated part of the transaction structure. Anyone can put anything they want in the extra field. There are two important arguments about this field.

1. An arbitrary data field in transactions appears to defy Monero's core design goal of private fungible transactions. If transactions can be differentiated based on what's in their extra fields, then they are less interchangeable and less anonymous.
2. The Monero core team cannot see the future nor evaluate all possible usecases of Monero. To a large extent, it is up to users how Monero actually gets used. If there is a feature which only a subset of Monero users find valuable, it requires adding data to transactions, and the core team either isn't interested or does not have the resources to implement it, then the only way that feature can exist without a fork is with something like the extra field. Moreover, if for some reason periodic hard forks become no longer feasible, then without an extra field the Monero transaction structure will be frozen for eternity. Just as Monero is changing today, who knows how it will change in the future. An extra field permits changes that don't depend on hard forks.

From my point of view, both arguments are too strong to abandon either of them. We must do our best within those constraints.

Now, we can create a simple, useful abstraction. Any 'legitimate' use of the extra field can be considered a 'feature' (e.g. random bytes with no purpose are not a legitimate feature). Multiple 'features' can coexist within the extra field. Indeed, right now we have the 'transaction public key', 'additional transaction public keys', 'encrypted payment ID', and 'extra nonce' all living together in the extra field.

A transaction is composed of a 'base configuration', the bare minimum to make a valid transaction that the vast majority of wallets can understand, and beyond that a 'set of features', which are non-essential but we can assume must be implemented in a compatible way with other wallets/services using those features (otherwise what's the point?).

How do we harmonize with argument 1? Every single possible implementation of 'base' + 'a given set of features' should be indistinguishable. As protocol designers, we must assume that if variation is permitted by the protocol, then all those variations will appear in the wild. In other words, our job here is to constrain transaction content so the most an observer can know is whether or not a given feature exists in a transaction. We should also avoid giving special treatment to different features, i.e. enforce a consistent and straightforward ruleset for all potential features. NOTE: Let's assume (to head off complaints) that variations in how a feature is implemented are considered different features (we certainly can't take responsibility for those variations). See **Proposal Part 1: Sorted TLV In Extra Field** below for my solution to this design goal.


### Introduction Part 2: View Tags

Scanning the blockchain for owned outputs is constrained by how long it takes to check each individual output. Checking an output means performing several elliptic curve computations, which are relatively slow. There is a cheap, simple way to reduce scan times for new outputs by reducing the number of EC ops required (on average). It would add one byte per output to the tx structure, and should be deployed with a hard fork to streamline adoption. See **Proposal Part 2: View Tags** and **Part 4: Expand/Reorganize TX Structure**.


### Introduction Part 3: Transaction Public Keys

We want Monero transactions to be as similar to each other as possible. Currently the number of tx public keys in a transaction leaks information about its recipients. If there are multiple tx pub keys it means at least one recipient is a subaddress. Due to intricacy around how tx pub keys are made, not _all_ transactions with subaddresses have more than 1 tx pub key, which thankfully makes the exact anonymity set for subaddress recipients very ambiguous (only when a transaction has 2 non-change outputs, where at least one of them is to a subaddress, will there be more than 1 tx pub key). Nevertheless, it would be better if no information was leaked (see also [MRL Issue #71](https://github.com/monero-project/research-lab/issues/71)).

The vast majority of transactions have two outputs, where one of them is a change output sending leftover Moneroj back to the tx author (or a dummy output with 0 amount). Luckily, 2-out tx with a change (or dummy) output only require one tx pub key, so we can easily enforce one tx pub key for all 2-out tx. Among the remaining tx with >2-out, some only require one tx pub key while some require one per output. However, in the name of indistinguishability, I propose to enforce one tx pub key per output for all >2-out tx. See **Proposal Part 4: Expand/Reorganize TX Structure**. Note: A small minority of 2-out tx with no change output would become 3-out tx. [credit: @knaccc]

_Janus mitigation_

As many people know, the Janus attack is an obscure yet potentially real attack on the idea subaddresses can't be associated with the normal address they were derived from. I won't belabor it here, [see @SarangNoether's writeup](https://github.com/monero-project/research-lab/issues/62#issue-558115837).

The mitigation I chose for this proposal is (after many iterations and different ideas) to encode the transaction private key for each tx pub key and record it in transactions. It requires one 16-byte (or 32-byte) encoded value per tx pub key, and adds steps after owned outputs are identified. Multiplying the tx pub key by the inverse of its private key will reveal the base key used, which is enough to identify Janus attacks. See **Proposal Part 3: Janus Mitigation**.

But wait, if the tx private key is given to recipients, how can we allow non-change recipients in 2-out tx to know the tx private key for _both_ outputs (since there is only 1 tx pub key)? The workaround is to make a hidden transaction public key for change outputs that can be derived deterministically from the tx author's private view key and the 'visible' tx pub key's encoded private key. Normally this method would significantly slow down scanning for owned outputs, but thanks to the efficiency gains from view tags the effect is hardly noticeable.


### Introduction Part 4: Organization

Ubiquitous and non-optional parts of a transaction should be part of the transaction structure (not the 'extra' field). This means tx pub keys should move from the tx extra to a new 'tx_supplement' in the tx structure. Subaddress support is also non-optional, so I believe the encoded tx private keys should also go there. Likewise with view tags. Usually we would leave the tx pub keys in the tx extra since moving them invites technical debt, but this large proposal which touches several different parts of the transaction structure is a good opportunity to clean things up. See **Proposal Part 4: Expand/Reorganize TX Structure**.

Note: Technically a wallet could make transactions without tx pub keys, but I guarantee all other wallets wouldn't be able to identify outputs received from that oddball wallet. Using tx pub keys is a wallet consensus sufficiently non-optional to canonize (from my point of view).



## Proposal

### Proposal Part 1: Sorted TLV In Extra Field

Originally proposed in [MRL Issue #61](https://github.com/monero-project/research-lab/issues/61), which includes pseudo-code demonstrating how to implement it. Functionally the extra field would behave the same as it does now, since we already default to TLV format (it's just not enforced). The original proposal recommends adding restricted tags only useable via hardfork, but I am no longer in favor of that idea.

An example 'feature' could be @moneromooo's [encrypted memo field](https://github.com/monero-project/monero/pull/6410).

Cost: No effect on transaction sizes, minimal increase in transaction verification time (especially since I'm also proposing to remove things from the extra field), and a small-to-moderate size development project. The biggest challenge would likely be organizing backward compatibility for wallets reading older tx. The cost to non-core wallet implementations is tiny, since they just have to add sorting (TLV is ubiquitous).

Note: [this github Issue](https://github.com/monero-project/monero/issues/6668) proposes deprecating the extra field completely.


### Proposal Part 2: View Tags

Originally proposed in [MRL Issue #73](https://github.com/monero-project/research-lab/issues/73). This slightly changes how transaction authors build transactions, and how recipients search for owned outputs. For more of this terminology/notation, see [Zero to Monero Second Edition](https://web.getmonero.org/library/Zero-to-Monero-2-0-0.pdf) especially Chapter 4.

Transaction author:

1. With sender-receiver shared secret `k^v*R_t` for output `t`, compute the so-called 'derivation to scalar': `dv_to_s_t = H(k^v*R_t,t)`. Note: they have to compute `dv_to_s_t` to make the one-time address `K^o_t`, so there is no real need to compute it more than once.
2. Compute the view tag for output `t`: `view_tag_t = first_byte_of(H("view_tag",dv_to_s_t))`
3. Store the view tag in the transaction.

Potential recipient of output `t`:

1. Given transaction public key `R_t`, compute the nominal derivation to scalar: `dv_to_s_t_nom = H(k^v*R_t,t)`
2. Compute the nominal view tag: `view_tag_t_nom = first_byte_of(H("view_tag",dv_to_s_t_nom))`
3. Check if `view_tag_t_nom ?= view_tag_t` i.e. if it's the same as the view tag stored for output `t` in the tx.
4. If they match, then compute the nominal spend key `K^s_nom = K^o_t - dv_to_s_t_nom*G`
5. See if `K^s_nom` corresponds to their normal spend key, or one of their subaddresses' spend keys. If it does, yay they own the output and can spend it (after doing the Janus test)!

For all non-owned outputs, the recipient will only get to step 4 about once out of every 256 outputs, and therefore only performs the EC computations in 4 for 1/256 unowned outputs.

Justify 1 byte design choice for the view tag: bytes are the basic unit of memory, and the difference in scan times between 1 byte and even 32 byte view tags is insignificant (implying no amount of increase in view tag size will have a meaningful impact; a view tag scan is 1 EC operation per tx pub key, while a full scan is ~3 EC ops, so with 1 byte tags there are 255 + 3 EC ops for every 256 unowned outputs on average, and going to 32 byte tags only reduces it to 256 EC ops for 256 unowned outputs).

Cost: There would be 1 byte more per output. A small development project.

Note: It would be nice to have a timing profile of output scanning for evalutating the impact of adding view tags, and more generally understanding what contributes to scan times.

Note2: What about wallets that fail to implement view tags correctly? Clearly wallets can still use the current method of scanning for outputs, and ignore view tags altogether. However, if the core wallet and other large wallets rely on view tags, then any other wallet that doesn't comply will incur a _lot_ of complaints from users who send outputs to other wallets that don't recognize them (this means other wallets should retain the ability to slow-scan just in case). Wallet implementers will be naturally incentivized to build tx with functional view tags. Keep in mind a similar objection could be raised about transaction public keys, which aren't validated or validate-able or even strictly necessary to make useable transactions, yet are ubiquitous and do not cause problems.


### Proposal Part 3: Janus Mitigation

_Method 1: Janus base key ([deprecated option](https://github.com/monero-project/research-lab/issues/62#issuecomment-633332476))_

Layed out and developed in [MRL Issue #62](https://github.com/monero-project/research-lab/issues/62).

_Method 2: 48-byte Schnorr proof ([deprecated option](https://github.com/monero-project/research-lab/issues/62#issuecomment-634367975))_

Originally ideated by @knaccc.

_Method 3a: 16-byte (or 32-byte) encoded tx private key_

Since we will be enforcing a unique tx pub key for each output (except change outputs in 2-out tx), it is now conceivable to inform recipients about the transaction private key for their owned outputs. Previously (e.g. currently), knowing the tx private key for transactions with just one tx pub key (most tx) would allow someone to figure out all the corresponding recipients and amounts.

Given a sender-receiver shared secret `r_t*K^v`, where `r_t` is the transaction private key for the output at index `t`, define `r_t` as a hash of a 16-byte nonce `n_r_t`, `r_t = H("tx_private_key", n_r_t)`, then encode `n_r_t` for the recipient as follows {thanks to @tevador for his idea to use a 16 byte nonce to seed the tx private key, so Janus mitigation is more efficient - if 16 bytes is deemed too little randomness, then a 32 byte tx private key can be generated as normal and added to transactions in encrypted form instead of the 16-byte nonce}
1. Compute `n_r_t_encoded = n_r_t XOR_16 H("encoded_tx_private_key", r_t*K^v, t)`

If a recipient encounters a one-time address/tx pub key pair `(K^o_t, R_t)` and identifies it as output owned by address (`K^v_i`, `K^s_i`).
1. Compute `n_r_t_nom = n_r_t_encoded XOR_16 H("encoded_tx_private_key", k^v*R_t, t)
2. Compute `r_t_nom = H("tx_private_key", n_r_t_nom)`
3. Compute `R_t_nom = r_t_nom * K^s_i`
4. If `R_t_nom == R_t` then `R_t` was constructed correctly, otherwise a Janus attack was executed.

_Method 3b: change outputs in a 2-out tx_

As stated, 2-out tx will have only one tx pub key, with one encoded tx nonce Rather than use the same tx nonce for both the change and non-change outputs, we will derive a hidden tx nonce from the encoded tx nonce and compute a hidden tx pub key for making the change output.

1. Given an encoded tx nonce `n_r_encoded` (there is only one so the index isn't relevant here), compute it using the change address's normal view key `k^v` (i.e. if the change address is a subaddress, use its normal address's view key): `n_r_hidden = H_16("change_tx_private_key", k^v, n_r_encoded)`
2. Compute the hidden tx pub key: `R_hidden = H("tx_private_key", n_r_hidden)*G`
3. Use, but don't include in the transaction, `R_hidden` for constructing the change output.
4. Compute the change output's view tag: `view_tag_change_t = first_byte_of(H("change_view_tag", k^v, dv_to_s_t))`

In the original process tx pub keys were aligned 1:1 with view tags, but now there is only one tx pub key `R` so we will reuse the shared secret. We also add a logic branch for identifying change outputs.
1. Compute the sender-receiver shared secret `k^v*R`.
2. For each of the two outputs `t \in {0,1}`
	a. Compute the nominal derivation to scalar: `dv_to_s_t_nom = H(k^v*R,t)`
	b1. Compute the nominal view tag: `view_tag_t_nom = first_byte_of(H("view_tag",dv_to_s_t_nom))`
	b2. Compute the nominal change view tag: `view_tag_change_t_nom = first_byte_of(H("change_view_tag",k^v,dv_to_s_t_nom))`
	c. Check if either matches `view_tag_t` (view tag corresponding to output `t`)
	d1. If the normal tag matches, then compute the nominal spend key: `K^s_nom = K^o_t - dv_to_s_t_nom*G`
	d2. If the change tag matches, move down to step 3.
	e. If `K^s_nom` matches a stored spend key, congrats we own the (non-change) output and can spend it! Now we should perform the Janus test by decoding the transaction nonce `n_r_encoded`, etc.
3. Now to identify change outputs (logic branch triggered by `view_tag_change_t_nom == view_tag_t`, should happen every ~1/256 unowned outputs).
	a. Compute the nominal hidden tx nonce: `n_r_hidden_nom = H_16("change_tx_private_key", k^v, n_r_encoded)`
	b. Compute the nominal hidden tx public key: `R_hidden_nom = H("tx_private_key", n_r_hidden_nom)*G`
	c. Use the hidden tx pub key to check if output `t` is owned. If it is then there is no need to perform a Janus test.

Note: By prefixing the change view tag with the private view key, even the non-change recipient who knows `r` won't be able to compute the change view tag. Meanwhile, we continue to use `dv_to_s_t_nom` so we don't have to compute `k^v*R_hidden` (expensive) until after the change view tag is flagged (rare).

Note2: An alternative to 'hidden tx private keys for change outputs' would be modifying how one-time addresses are constructed. For example, using a 'change-out derivation to scalar' prefixed with the private view key: `dv_to_s_change = H(k^v, k^v*R,t)`. Whether to use this or the hidden key depends on which is simpler and cleaner to implement.

Note3: If encoded tx nonces are implemented then OutProofs would be insufficient to prove creation of a transaction output, since they rely on knowledge of the transaction private key (which tx recipients would now know as well). This means OutProofs would require corresponding SpendProofs that prove we created the transaction itself. OutProofs would still be useful for showing a specific recipient received a certain amount of money. Also, OutProofs would not work for change outputs in 2-out tx, although aiui they don't work for change outputs currently anyway. Instead, make an InProof proving ownership of a change output and a SpendProof proving we created the tx it originated in.

_Total cost_

Apparently about 95% of modern transactions are 2-out tx, and there are on average 2.2 outputs per transaction. Therefore the average cost per transaction from adding encoded tx private keys is approximately:
`.95*16 + 0.05*(2*16) + 0.2*16 = 20 bytes`


### Proposal Part 4: Expand/Reorganize TX Structure

This part's ideas originated in IRC discussions which I don't have links for. It's pretty straightforward.

1. Make a new section in the transaction structure called `tx_supplement`.
	a. Encoded tx private keys (corresponding 1:1 with outputs, except 2-out tx which have just one)
	b. Transaction public keys (corresponding 1:1 with outputs, except 2-out tx which have just one)
	c. View tags (corresponding 1:1 with outputs)

Cost: By constraining tx pub keys, some small minority of 2-out tx that don't have change outputs will become 3-out tx, and all >2-out tx that currently have just one tx pub key will now have tx pub keys for all outputs. A medium size development project.

Note: Enforcing 1 tx pub key per output for >2 out tx would likely increase average tx size by around 6-10 bytes, since about 5% of tx have >2 outs, which leads to an overall average of 2.2 outputs, and (0.05*32 + 0.2*32) = 8.



## Implementation Guideline

One possible path for implementing all the changes:

1. Add tx_supplement to the transaction structure. [HF_ADD_TX_SUPPLEMENT]
2. Move transaction public keys to the tx_supplement. [HF_TX_PUB_KEYS_IN_TX_SUPPLEMENT]
a. Enforce 1 tx pub key for 2-out tx, and 1 tx pub key per output for >2-out tx. This would add a check to block verification (HF version dependent), and rework how tx pub keys are constructed for new transactions (no need for backward compatibility). It also adds a scenario for making a dummy output (when there are only two outputs and both are non-change). [HF_ENFORCE_TX_PUB_KEY_QUANTITY]
3. Add view_tag to the tx_supplement (one per output). Change how transactions are constructed, and add logic to transaction scanning. [HF_INCLUDE_VIEW_TAGS]
4. Add encoded tx nonces for Janus mitigation. These go in the tx_supplement. [HF_INCLUDE_JANUS_PROOFS]
a. For 2-out tx, use the hidden tx pub key for change outputs, implement 'change view tags', and add logic to 'scanning for owned outputs' for identifying change outputs.
b. Enforce one encoded tx nonce for 2-out tx, and one encoded tx nonce per output for >2-out tx (and one encoded tx nonce per output for miner transactions since there is never a change output).
a. Optional: Perform a timing analysis on transaction scanning to better understand the costs of scanning, and to quantify the benefit of view tags.
5. Enforce sorted TLV in the tx_extra. The core code already constructs transactions with sorted TLV, so implementing it mostly entails adding a check in block verification. Note that implementations in the wild just need to add sorting to their tx_extras, since AFAIK they all use TLV by default. [HF_ENFORCE_SORTED_TLV_IN_TX_EXTRA]
a. Optional: Move extra_nonce to tx_supplement to enforce uniformity (I recommend 32 bytes for miner transactions only, and 0 bytes for non-miner tx). Out of scope for this proposal, I would like to make a guideline for coinbase uniformity that doesn't impose a large burden on pool and solo-miner implementations. Might make a separate proposal that includes moving the extra nonce.
b. Optional: Move encrypted payment ID to tx_supplement. As @knaccc pointed out it would be preferable if people used subaddresses instead of integrated addresses, but putting encrypted IDs in the tx_supplement would 'canonize' them and ultimately make them harder to deprecate. I agree this should remain in the tx_extra.


*DISCLAIMER*

While I present these changes as a package, they don't have to all be implemented. In particular sorted TLV is contentious. Hopefully my argument in favor is clear enough.




















# Discussion History
## ghost | 2020-04-16T23:21:14+00:00
When you say "Sorted TLV", do you mean _recursively_ "Sorted TLV", whatever TLV means?

## UkoeHB | 2020-04-16T23:27:42+00:00
Does it matter how it gets sorted? Not sure I understand the question.

## ghost | 2020-04-16T23:41:44+00:00
If I attach a list of tiktok videos as an item in tx-extra, do I have to sort these videos by TLV? If the answer is no, then your "Sorted TLV" is non recursive. If yes, then it would be recursive.

## UkoeHB | 2020-04-17T00:13:06+00:00
Sorted TLV says nothing about the contents of values, so I suppose non-recursive is correct.

## knaccc | 2020-04-17T10:21:03+00:00
Great work, love the view tags.

The Janus mitigation described above requires a full-spend wallet rather than a view-only wallet. I think the design goal for Janus mitigation should be for it to work with view-only wallets.

If a 48-byte schnorr signature was used instead of a Janus key, then for 2-out txs the extra storage required for Janus mitigation would increase from 32 bytes to 48 bytes per tx.

For n-out transactions where n>=3, the extra storage required for Janus mitigation would increase from 32 bytes per tx to 48 bytes per output.

Since the vast majority of txs are 2-out, I think the extra 16 bytes in that situation is justified. I also think that the extra storage is justified for n>=3-out txs, since they are relatively rare.

## iamamyth | 2020-04-17T10:21:30+00:00
> Justify 1 byte design choice for the view tag: bytes are the basic unit of memory, and the difference in scan times between 1 byte and 2 byte view tags is insignificant (1/256 vs 1/65536 = 0.4% change in amount of outputs to fully scan).

This seems a questionable justification. First off, I don't understand why 2 bytes would be the proper comparison, as the logical choice would be 4 or 8 bytes, as that's the amount of data likely to yield the optimal execution on most architectures (1 byte addressing, while technically possible, only makes sense in architectures without out of order execution; otherwise, you end up with false dependencies). Second, I find your phrasing odd: 2\*\*8 vs 2\*\*16 is a *huge* difference, 256x, to be precise. A 256x optimization is not to be taken lightly, and, at 4 or 8 bytes, the optimization would be even more massive. So, the justification here, to me, reads less like a justification, and more like a rather abridged, and somewhat dubious, statement of known information. A proper justification would address the time-space tradeoff: Why is the extra space so valuable that it shouldn't be used to dramatically speed up the computation? Even at 8 bytes, would the bloat be so bad? Isn't the entire blockchain doomed if an extra 8 bytes per transaction hobble it? After all, there's this [active PR](https://github.com/monero-project/monero/pull/6410), which seems to considerably increase space usage, as compared to the proposal here.

## knaccc | 2020-04-17T10:31:05+00:00
@iamamyth 

>  that's the amount of data likely to yield the optimal execution on most architectures

The EC variable base scalarmult operation required for each output is so computationally expensive (a modern CPU can only do in the order of thousands per second) that any 1 vs 4/8 byte scanning optimizations would not make any significant difference.

I agree with @UkoeHB 's choice of 1 byte per view tag.

## ghost | 2020-04-17T11:21:20+00:00
> The EC variable base scalarmult operation required for each output is so computationally expensive

Which scalarmult is used differently in the case of a 8 bytes or 1 byte viewtag?

## UkoeHB | 2020-04-17T11:25:34+00:00
@iamamyth
> This seems a questionable justification. First off, I don't understand why 2 bytes would be the proper comparison, as the logical choice would be 4 or 8 bytes, as that's the amount of data likely to yield the optimal execution on most architectures (1 byte addressing, while technically possible, only makes sense in architectures without out of order execution; otherwise, you end up with false dependencies). Second, I find your phrasing odd: 2**8 vs 2**16 is a _huge_ difference, 256x, to be precise. A 256x optimization is not to be taken lightly, and, at 4 or 8 bytes, the optimization would be even more massive. So, the justification here, to me, reads less like a justification, and more like a rather abridged, and somewhat dubious, statement of known information. A proper justification would address the time-space tradeoff: Why is the extra space so valuable that it shouldn't be used to dramatically speed up the computation?

2 bytes is just an example. The bottleneck for scanning is EC operations, and going from 1 byte to 2 bytes only reduces EC ops by around 0.4%. i.e. given 256 outputs, with 1 byte you do 255 scalar-mult-key ops, and then 1 normal scan; with 65536 outputs, with 2 bytes you do 65535 scalar-mult-key ops, and 1 normal scan. But the fraction of 1scan/65535smk is only ~0.004x smaller than 1scan/255smk. So, you don't gain much on average. As @knaccc said, optimal execution isn't really a concern since EC ops are so much more expensive than data-handling optimization. EDIT: I agree with you more bytes would be justified if the 255/256 cases were super fast, so scan times were dominated by the remaining 1/256th case. However, view tags must be based on a shared secret for privacy (i.e. so no one else can compute the view tag and narrow down which outputs we might own), and shared secrets require an EC operation (unless we get into RSA territory, which seems like a dead end) EDIT2: while a normal scan requires around 3 EC operations.

@fuwa0529 

> Which scalarmult is used differently in the case of a 8 bytes or 1 byte viewtag?

There is no difference. It's just a question of how many bytes you truncate off the hash. The hash output is 32 bytes, but with view tag you only save some of those bytes.

## iamamyth | 2020-04-17T23:00:07+00:00
@UkoeHB I see. The original MRL proposal does a fine job of explaining the savings, I just found the 1 vs 2 byte justification here lacking, as it elides the dominant factor: Adding a view tag reduces EC ops by 2/3 per negative. This cost savings ratio is the crucial component of the calculation, as it ultimately determines the appropriate scale of the false positive ratio (e.g. no savings makes the whole thing worthless; 10x savings would make for a ~3.4% reduction by adding an extra byte; etc). So, discussing the false positive ratio without explicit mention of the savings ratio seemed to miss the core issue.

My point in mentioning 4 or even 8 bytes was simply that considering extremes helps best illustrate the function's behavior: Even scaling the tag to 8 bytes saves < 1% at a 2/3 savings factor, so of course 2 bytes is a non-starter. Put differently, when you can reject the maximum gain from expanding the tag as inconsequential, you have proven expansion is unwarranted; rejecting the minimum gain is less compelling. That said, I probably shouldn't have mentioned the pipelining issue, it just distracted from my aim.

## UkoeHB | 2020-04-17T23:12:54+00:00
@iamamyth I updated the justification based on what you said. Thanks

Note that the comment '1 byte is a standard unit of memory' lets us select 1 byte rather than say 7 bits or 9 bits, without any hassle.

## Mitchellpkt | 2020-05-25T18:04:48+00:00
I'm very strongly in favor of this proposal, since the current transaction format is [super leaky](https://github.com/monero-project/research-lab/issues/61#issuecomment-607377450) and long overdue for an overhaul. This proposal eliminates a variety of fungibility defects in one fell swoop, and will permanently shut down several transaction linkability heuristics.

Misc thoughts and questions:
- I just want to confirm - the protocol will reject any transactions whose `tx_supplement` contains anything besides the whitelisted tags, right? 
- What would be a reasonable upper limit on `tx_extra` length? I think (?? not sure) that right now the only limit is effectively the block size, which is sloppy security, and imho especially dangerous since we have a dynamic block size. (edit: relevant Easter egg: txn with [35 kB of "deadbeef"](https://xmrchain.net/tx/fba62a80ff85021671227b25035fa809973bae29b2b93479c433d4d3ab99ec48) in `tx_extra`, discovered by @NeptuneResearch)
- The view tag is a clever idea, good thinking.
- I'm glad that we're mitigating Janus, *phew!
- What's the current thinking on encrypted PIDs? Do we want them to be included on all transactions or only those from a subset of users? 
- Side note - I would support an encrypted memo field if it was enforced on all transactions with a fixed ciphertext length. 

## UkoeHB | 2020-05-25T19:03:47+00:00
@Mitchellpkt 
1. Yes the `tx_supplement` content would be mandatory. The `tx_extra` should be the only optional part of transactions.
2. The `tx_extra` is constrained by the transaction size limit (149.4kB iirc). Since it's inherently open-ended I don't think we have much choice except to leave the size also open-ended. If the concern is bloat then we should just reduce the tx size limit.
3. View tag: thanks! It remains to be analyzed how much impact it will have on scanning times.
4. Janus: yeah it will be good to have in there. Sadly +48 bytes is pretty expensive (and even many more bytes for >2-out tx), but there don't seem to be any alternatives.
5. Encrypted PIDs: afaik the core team still wants to deprecate these at some point, so they are in a state of 'tentative support'. The core code always adds an ePID to 2-out tx, even if it's a dummy, but there is no enforcement. Canonizing subaddresses with the Janus mitigation acts as a sort of chess move in the direction of ePID deprecation.
6. Encrypted memo field: the `tx_extra` seems like a good place for something discretionary like a memo field.

## SarangNoether | 2020-05-27T20:16:45+00:00
See [this issue](https://github.com/monero-project/research-lab/issues/73#issuecomment-634915828) for timing data relating to view tags.

## Gingeropolous | 2020-09-11T03:00:10+00:00
> The Monero core team cannot see the future nor evaluate all possible usecases of Monero. To a large extent, it is up to users how Monero actually gets used. 

I dunno. I would put forth that monero is digital money. There is really only one usecase of money - the storage and transfer of value. And the thing doing this storage and transfer must be fungible, thus, private. 

If monero isn't private (due to tx_extra letting people introduce oracle bamboo shoots that program your money to make it farm some yams), then its not money. 

Basically, let monero be money. If people want to program their money, they can make something else that can interface with monero, right? There's no need for the programming of the money to be on the same chain as the money. 

## UkoeHB | 2020-09-11T03:40:52+00:00
"If people want to program their money, they can make something else that can interface with monero, right?"

Technically the transaction public key, Janus mitigation, and view tag are all 'extra programming' for Monero. An alternate wallet could choose to implement their own completely different addressing scheme. However, tx pub keys are ubiquitous and useful. We don't know the future... what if something just as useful as tx pub keys gets invented? Without the tx extra, and assuming a hard fork is not possible or doesn't have enough support, that new feature may be infeasible.

## UkoeHB | 2020-09-23T18:09:10+00:00
Additional context on the fungibility implications of leaving the `tx_extra` as it is: https://github.com/neptuneresearch/monero-tx-extra-statistics-report

Thanks a lot to [the Noncesense Research Lab](https://noncesense-research-lab.github.io/) for the excellent work!

## Gingeropolous | 2021-05-12T03:42:58+00:00
@UkoeHB , where do view tags stand? 

## UkoeHB | 2021-06-01T13:40:36+00:00
@Gingeropolous afaik no one is working on them, or this proposal, right now.

## UkoeHB | 2021-07-26T23:04:28+00:00
I was asked recently:

> Which changes are low-hanging fruit? That is to say: changes that are the easiest to implement on mainnet, have rough consensus, have a relatively low negative impact and relatively high positive impact on Monero.

Easiest to implement:
1) sorted TLV in extra field
2) enforcing 1 tx pub key for 2-out tx, 1/output for >2-out tx
3) view tags
4) Janus mitigation

Highest impact (imo):
1) view tags
2) Janus mitigation
3) TLV and tx pub key stuff

Consensus:
1) view tags
2) ? not really clear

# Action History
- Created by: UkoeHB | 2020-04-16T21:38:22+00:00
