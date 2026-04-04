---
title: Recognize spent outputs with view key only
source_url: https://github.com/monero-project/research-lab/issues/58
author: UkoeHB
assignees: []
labels: []
created_at: '2020-01-29T19:55:17+00:00'
updated_at: '2021-04-09T19:29:11+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
(OUTDATED, see [this comment](https://github.com/monero-project/research-lab/issues/58#issuecomment-581090684) down below)

Monero addresses are (`K_v`,`K_s`), with private keys (`k_v`,`k_s`) corresponding to 'view' and 'spend'. One time addresses are constructed based on the 'transaction public key' `rG` (for the simple non-subaddress case). A one-time address (aka stealth) is `K^o = H_n(r*K_v,t)*G + K_s`, where `H_n()` is a hash to scalar function, and `t` is the index of the output to which the address-holder is being given spend-rights.

An address holder can use his view key to search for owned outputs. He finds `rG` and `K^o` in a transaction's data, then calculates `k_v*rG`, and `K'_s = K^o - H_n(k_v*rG)*G`, and checks `K'_s ?= K_s`. If they match, then he owns the output and may spend it by signing an MLSAG with the private key `k^o = H_n(k_v*rG,t) + k_s`.

Currently the only way to know if an output has been *spent* is to calculate the key images of all owned outputs, then check if any of those images have appeared in the blockchain before. Calculating a key image `KI` requires the private spend key `k_s`, since `KI = k^o*H_p(K^o)` (where `H_p` is Monero's unique hash-to-point algorithm), and since `k^o` is partly composed of `k_s`.

This reality is somewhat confusing, since a 'view' key can't actually be used to *view* an address' balance (sum of unspent owned outputs)!

My proposal is a new 'viewspent' public key for every input to a transaction. This public key will be stored in the transaction extra field, and not verified as part of the protocol. It will exist merely as a convenience that transaction authors create for themselves, so their view-only wallets may easily and safely recognize an address' balance. It may not be rigorous enough for an audit environment, where all key images of known owned outputs are required (even though this will leak future spends of those outputs), since transaction authors are free to create fake viewspent keys. Since one-time addresses themselves, and view keys by extension, are not part of the protocol (someone may do like Bitcoin, and assign output ownership by including an address directly in transaction data, though all other wallets would not be able to interact with those outputs), I do not view this audit-related drawback as a real detriment to the proposal. View keys and one-time addresses are essentially conveniences to begin with, so viewspent keys are on a similar level to the transaction public key.

Viewspent key: `K_vs = (k_s/k_v)*H_p(K^o)`
Check for spent: `KI - k_v*K_vs ?= H_n(k_v*rG,t)*H_p(K^o)`

Users only need to check for spent when one of their owned outputs is referenced in the input ring of a transaction (and only when not already identified as spent), which should only require per-owned-output checks on the order of the ring sizes themselves (11 currently), an insignificant amount of scanning compared to finding owned outputs in the first place.

The view key's inverse `(1/k_v)` is included to prevent the person who originally created an output from using the sender-receiver shared secret `rKv` to realize the recipient spent that output.

Bonus: I recommend deprecating the extra field's 0x01 tag, and using 0x04 exclusively (extra pub keys) since the keys from this proposition can be randomly shuffled amongst the transaction public keys. Randomly shuffled pub keys is beneficial to tx join protocols that want to use a promising in-consideration mitigation for the Janus attack.

UPDATE1: within the extra field, separate viewspent keys into its own type sub-field, to reduce unnecessary scanning for owned outputs.

# Discussion History
## SarangNoether | 2020-01-30T23:39:14+00:00
With Triptych, it is possible to hide up to 64 bytes of data in the proof by knowledge of a PRNG seed; however, any entity that does this can brute-force the signing index. Since such a key is only intended to be used by the author of a transaction, it could be stored in this way and not incur any additional space cost. The recovery process is done during signature verification and is computationally cheap. However, the nonlinearity of Triptych key images would be problematic for this construction.

## SamsungGalaxyPlayer | 2020-01-31T04:25:51+00:00
Is this optional? Mandatory? Can it be spoofed if mandatory?

## UkoeHB | 2020-01-31T07:24:56+00:00
EDIT: moving this proof to Issue #68, so this thread can focus on the viewspent proposal.

Just like transaction public keys are technically optional, viewspent is also optional. There may be a way to leverage this concept to prove a given key image does NOT correspond with a one-time address from its corresponding ring, assuming verifier's knowledge of the view private key and prover's knowledge of the spend private key. This side note is suitable for audit environments, and doesn't expose the key images of unspent outputs. It can be implemented right now without changing how transactions are constructed.

1. For every time an owned output `K^o` is referenced in the ring of a transaction, take the key image to be tested `KI_?` of that ring signature.
2. Create three 2-base signatures on base keys: 
a) generator `G` and `K^s`: signing key k^s
b) generator `G` and `KI_? - H_n(k_v*rG,t)*H_p(K^o)`: signing key k^s
c) generator `G` and `H_p(K^o)`: signing key k^s*k^s
3. The verifier checks that
a) first key of (a) and first key of (b) == `K^s` (the spend key)
b) second key of (a) == first key of (c)
c) second key of (b) != second key of (c), or in other words,
`k^s[KI_? - H_n(k_v*rG,t)*H_p(K^o)] != k^s*k^s*H_p(K^o)`

This seemingly roundabout approach prevents the verifier from learning `k^s*H_p(K^o)`, which he could use in combination with the view key to compute the real key image for that output, while leaving him confident that the tested key image doesn't correspond to that output.

In fact, the prover only needs to do proof (b) for each key image to be tested. There should only be on the order of 11 (current ring size) tests per owned output, since that's around how many times an output is likely to be included in rings as decoys.

EDIT: moving this proof to Issue #68, so this thread can focus on the viewspent proposal.

## SarangNoether | 2020-01-31T13:53:11+00:00
Since 2a and 2b share the same discrete logarithm across all points, they can be combined into a single proof.

## vtnerd | 2020-01-31T18:15:36+00:00
In 99.9% of cases, a spent output results in change coming back to the same viewkey. So it is already possible to infer a balance. If a wallet always sends a 0XMR change - even when sweeping (which has privacy benefits too) - then the balance can be inferred with just the viewkey. AFAIK, there's no way to make this mandatory in the protocol, so a non-standard wallet could move funds with sending this notification to the original wallet.

EDIT: This does "break" in certain situations, so 99.9% is probably too aggressive of a claim. Its some reasonably high percent though. The case that "breaks" this inference is when someone used your output in their ring to send you money. This is statistical unlikely, and can be filtered once you actually spend the output. I'm pointing this all of this out because anyone doing viewkey management can give a fairly good estimate of true account balance without an additional behavior _today_.

EDIT2: Multisig would probably break this behavior too, but I haven't thought about it more.

## vtnerd | 2020-01-31T18:16:44+00:00
BTW, I noticed this while writing the light-wallet-server. When get the JSON back from the server, it was easy to spot which was the "real spend" without doing any key-image calculation.

## UkoeHB | 2020-01-31T22:27:14+00:00
@vtnerd Currently the 0XMR change output is directed to a random address, and only gets created when a dummy output is required (e.g. 2-output minimum; see `transfer_selected_rct()`).

## UkoeHB | 2020-01-31T23:43:21+00:00
Multisig might benefit a lot from viewspent keys or even @vtnerd 's probabalistic method, since currently the only way to know if an output has been spent ex-post is by collaborating with all other signers to compute the full key images. As rbrunner's MMS project revealed, dealing with partial key images is quite a pain. He says in his [documentation](https://web.getmonero.org/resources/user-guides/multisig-messaging-system.html) "That 'import_multisig_info needed' thing is perhaps the single most tiresome aspect of CryptoNote multisig transactions and quite some work e.g. in the case of 3/3 or 2/3 multisig where already a total of six pieces of information must be passed around each time, only to finalize reception of some coins and/or being able to transfer again after a transfer."

## UkoeHB | 2020-02-02T00:59:01+00:00
Update based on conversations over the past few days

_Introduction_

At the consensus protocol level, each address given spend-rights to an amount of money is simply a public key, and signing with the private key activates that spend-right. Each address may activate that sign right once, so functionally they are one-time addresses. Spend keys, view keys, and transaction public keys, are all wallet standard conveniences that enable many one-time addresses to be derived from a single `parent’ address, which can then be used to activate the many spend-rights. In fact, view keys themselves are one step further removed from the protocol since the same effect could be had with a single spend key.

A view key can be used, in combination with a transaction public key, to identify a parent address’ owned outputs (and their amounts). Users must have both view and spend keys to actually spend those outputs (although often the view key is derived from the spend key).

To know if an owned output has already been spent, it is currently necessary to calculate their key images and check against the blockchain. In the ubiquitous scheme of parent addresses a key image depends on the one-time address private key, which in turn depends on the spend private key. Therefore an accurate parent address’ (wallet’s) balance (sum of unspent outputs’ amounts) needs the spend key.


_Probabilistic balance_

[vtnerd] Someone with just the view key may infer a wallet balance based on outputs received from transactions that reference an owned output. Such outputs are probably `change’, directed back to the same wallet, and hence the input amount - change = amount spent. There are two main cases where this can fail.
1. An entire input is transferred without change. This has two subtypes. In 2-output transactions (there is a minimum of two outputs per tx) with only one recipient, the change amount will be ‘0’ and sent to a randomly generated recipient address; this could be changed to the sender’s address for use in estimating account balance. In 3+-output transactions there is no change output, which would be invisible to this method. Around 95% of modern transaction volume is 2-output transactions (https://usercontent.irccloud-cdn.com/file/oSealHXL/image.png & 1.8% of tx volume is 16-outputs from Isthmus’ data). A coin thief may use this to ‘hide the steal’ from view-only wallets.
2. An owned output was created by someone else, who happened to include in one of their input’s rings a reference to another owned output. This method erroneously treats the new output like a change output. This means high volume wallets using this method are more likely to falsely estimate the balance, and it therefore likely won’t be used by big players.

Feedback: moneromooo is resistant to this since “I think the uncertainty kills it. People will rely on it and complain when it's wrong. And if it's uncertain, it's pointless, isn't it. The main use people want is to ensure they can see when their money is stolen. Which relying on change does not help.” vtnerd likes it because “You should be able to do a view-key only frontend that does a "good enough" job for an individual to monitor the wallet from phone” 


_viewspent key balance_

[koe] With a `viewspent’ key included when spending an owned output, the view key can be used to identify that it has been spent. Scanning time is insignificant since only transactions where an owned (and thought-to-be unspent) output is referenced need to be considered. There are currently two ways to include this key in transaction data (one such key per input).
1. A tx_extra field type (segregated from tx pub keys to reduce scanning time).
2. Offsets in the first 2 indexed scalars of MLSAG signatures. Even if one of those is the real response, the other won’t be.

And there are two main drawbacks.
1. If someone steals coins from a wallet, this method may not identify those stolen coins if the thief ‘hides the steal’ by faking the viewspent key.
2. On a per-input basis it either costs 1 32 byte curve point in the tx extra field (an absolute increase in chain size), or 2 32 byte MLSAG scalars (increase in node storage of 56 bytes per input since each node retains 1/8th of prunable data). Or, if pruned nodes don’t save those scalars, view-wallet syncing would require concurrent access to 8 pruned nodes or a full node. I predict that viewspent-enabled nodes would become popular.

Note: viewspent may not be possible for Triptych which uses a different key image format, this is an area of open investigation.

Feedback: 
1. sarang against anything that is gameable and increases tx size, “I don't see why keeping it in sig scalars (and then pulling from a full node) isn't a reasonable compromise on this”
2. sgp “in the [case of giving view key to another party for convenience], I want as many barriers to preventing someone from figuring out which outputs are actually spent as possible” and “[in the case of handing out view key for audit functionality], I would want to be 100% sure it can't be gamed”

_Considerations_

1. Utility of view-only wallets (generally)
	a) Common user: convenient balance checking without exposure to the spend key. As users become more confident that they won’t make a mistake with spend-enabled software, this will become less important.
	b) View-only wallets are much safer to use in risky environments; trusted organizations (e.g. MyMonero) may be given custody of view keys for online balance checking without risk of losing funds. In particular, such view-enabled services remove the inconvenience of waiting for a blockchain scan before balance is available. They can be combined with spend-rights wallets for a more user-friendly experience (the service is responsible for scanning, and the wallet is responsible for making transactions).
	c) May be given to others who are allowed view-access to a wallet but not spend-rights. The classic example is financial analysts in companies who need to keep track of expenditures.
2. Disutility of current view-only wallets
	a) View-only wallets must currently sync key images with a spend-enabled wallet in order to know the full balance.
	b) Multisig wallets, both spend-enabled and view-only, must collaborate with at least the threshold amount of other signers in order to compute key images (for any threshold above 2 it would be very tedious). This is a huge problem for future adoption of Monero, since multisig is very important for corporate environments, and essential to low-trust escrowed marketplaces. Moreover, non-signing members of a tx have no way to know the other members spent funds without directly communicating with them!
3. Disutility of viewspent-enabled wallets
	a) Cannot be relied on to find evidence of thievery, since viewspent keys can be faked or the probabilistic method hidden from. View-only wallets should periodically sync with spend-enabled wallets to make sure no funny business has occurred. This should usually happen before creating transactions, in terms of efficient architecture design. Secondary to this, wallets not viewspent-enabled won’t know what to do with viewspent keys.
	b) Cannot be used directly for rigorous audits, since like mentioned the viewspent keys can be faked. A new kind of unspent proof will make this problem obsolete.
4. [sarang] Elegance of hiding viewspent keys in signature data.
	a) does not fingerprint compliant/non-compliant wallets
	b) does not increase blockchain size directly (although may lead to nodes storing more data, since they might prune less), it’s essentially invisible to the blockchain
	c) may plug-and-play easily with other signing methods (CLSAG, Triptych, RCT3.0)

_Q&A_

Q: [gingeropolous] what is the currency parallel here?
A: A spend key gives access to a locked vault containing gold. A view key (currently) shows how much gold was ever added to that vault (it’s dropped through a hole, and in the hole is a counter that can’t be tampered with). A viewspent key is a nanny cam pointed at a record inside the vault, which details withdrawals (additions - withdrawals = balance). A thief who gets through the door might not write down his withdrawal, so the spend key must be used to check the vault manually to verify the contents.

## SarangNoether | 2020-02-02T02:23:23+00:00
The construction listed here does not guarantee that the key image appearing in the signature corresponds to the expected ring member. An adversary holding the user's view key can simply include a view/spent key that passes the verification equation, but actually corresponds to another ring member spent by the adversary (perhaps to itself). This would fool the user into seeing an artificially-low balance. You could achieve the same level of functionality by hiding/encrypting a flag indicating a spend instead, with less complexity.

## UkoeHB | 2020-02-02T02:31:08+00:00
As @SarangNoether said, anyone with the view key can fake a viewspent key into signaling something when in fact the key image was the attacker's.

Suppose instead of `K_vs = (k_s/k_v)*H_p(K^o)` it was `K_vs = (1/k_v)*[KI - Z]` where `Z = H_n(k_v*rG,t)*H_p(K^o)`. The attacker can put in any `KI` and it will cancel out, making the check `KI - k_v*K_vs ?= H_n(k_v*rG,t)*H_p(K^o)` succeed for any `KI`.

Solution 1: (following the 2-base proof mentioned in Issue #68) embed a proof in MLSAG scalars that the spend key component of the key image corresponds to our public spend key.
1. Base points `G` and `H_p(K^o)`; signing key `k^s`; record `k^s*H_p(K^o)` and `(c,r)` proof elements in the scalars
2. Verify `KI - H_n(k_v*rG,t)*H_p(K^o)` ?= `k^s*H_p(K^o)`

Solution 2: reveal the signing index
1. Add a message (EDIT: that depends in part on the private view key) to all the MLSAG scalars and verify they are all there. Only the signing index's scalar (e.g. the signature response) won't contain that message, so if the signer isn't our owned output it will be revealed.

Note: both of these solutions mean that using the tx extra field is infeasible. The former uses 3x 32 bytes per proof which is simply too expensive, and the second obviously uses all the MLSAG scalars.



## SarangNoether | 2020-02-02T02:35:29+00:00
The "message" you're hiding in scalars for the second idea would be a hash of the view key, the scalar index, and public data unique to the signature. Reuse of any scalar's hash input would allow linking between signatures.

## UkoeHB | 2020-02-02T22:10:54+00:00
Another point in favor: with paper wallets it can be a hassle to check the full balance without reliable view-only capability. See [this](https://monero.stackexchange.com/questions/11959/view-balance-without-a-transaction-hash) recent merchant's comment.

## SarangNoether | 2020-02-02T22:14:39+00:00
It depends on your definition of "reliable" here. Balance is only correct if every spend follows the standard, which cannot be enforced. It's a convenience feature that assumes/requires all your wallet software complies.

## UkoeHB | 2020-02-02T22:45:16+00:00
That's a good point. If a user wants fully enabled view-only capabilities, they must only spend their outputs with full-view compatible wallets.

## UkoeHB | 2021-04-09T19:29:10+00:00
[another proposal](https://github.com/monero-project/monero/issues/1070) issue #1070 in `monero-project`

# Action History
- Created by: UkoeHB | 2020-01-29T19:55:17+00:00
