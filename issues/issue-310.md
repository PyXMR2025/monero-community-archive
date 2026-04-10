---
title: More Jamtis features in Carrot
source_url: https://github.com/seraphis-migration/monero/issues/310
author: UkoeHB
assignees: []
labels: []
created_at: '2026-04-07T01:16:19+00:00'
updated_at: '2026-04-07T22:42:24+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
**EDIT:** Interpret this document as instead advocating the following: simplify Carrot to just 'Legacy-Carrot' (removing the new key hierarchy), and push for Jamtis-PQ after the FCMP++ hardfork (essentially Jamtis-Carrot with improved quantum forward-secrecy).

[Carrot](https://github.com/jeffro256/carrot/blob/pq_secure_ki/carrot.md) is a new addressing protocol with two pieces. First is an enote construction and scanning protocol, and second is a new key hierarchy. Both old CryptoNote-style addresses and new Carrot-key-hierarchy addresses would use the same enote construction/scanning protocol. Addresses for the new key hierarchy would look like old addresses.

The Carrot key hierarchy and enote construction details trace back to [Jamtis](https://gist.github.com/tevador/50160d160d24cfc6c52ae02eb3d17024) (also see [Seraphis impl](https://raw.githubusercontent.com/UkoeHB/Seraphis/master/implementing_seraphis/Impl-Seraphis-0-0-4.pdf) and the variation [Jamtis-RCT](https://gist.github.com/tevador/d3656a217c0177c160b9b6219d9ebb96)).

Jamtis includes three features not present in Carrot. I propose adjusting the Carrot key hierarchy and address format to include them. For clarity, the new format is called 'Jamtis-Carrot' here.

If Jamtis-Carrot is accepted, the FCMP++ hardfork code *only* needs to support constructing enotes for Jamtis-Carrot addresses. Jamtis-Carrot wallet gen, advanced key hierarchy features, and scanning do not need to be implemented immediately (outside of lower-level code that can be unit tested). Existing legacy addresses would still benefit from the Legacy-Carrot changes to enote construction (burning bug and Janus mitigations plus some [PQ improvements](https://gist.github.com/jeffro256/146bfd5306ea3a8a2a0ea4d660cd2243)) that are already being [PRd and reviewed](https://github.com/monero-project/monero/pull/9559) and have been audited.

## 1. Filter-assist keys

Filter-assist keys are elliptic curve points that would be included in user addresses (32 bytes). Using the filter-assist key is optional and privacy-optimized.

- Enables 'filter-assist services' that use the filter-assist key to filter enotes in the blockchain using view tags and store them for transmission to users (or store their blockchain indices, which can be translated to enotes + key images).
- Filter-assist scanning has far better privacy than light wallets. The sooner light wallets are fazed out, the better.
- Filter-assist scanning would be a major boon to the mobile ecosystem (i.e. the subset of users who are relatively less privacy-focused). It would also lessen the possibility of light wallet usage by mobile wallets.

#### Implementation note

Carrot [section 7.8.3](https://github.com/jeffro256/carrot/blob/pq_secure_ki/carrot.md#783-mandatory-self-send-enote-rule) has a rule about mandatory self-sends, but the design does not support it. `s_sr = s_vb` for internal enotes, and you aren't going to be sending `s_vb` to a light wallet. 7.8.3 only works if all txs have an exclusive selfsend (but Carrot only has something like that for the 'special' enote in 2-outs).

Filter-assist service use requires the exclusive/auxiliary selfsend distinction so all enotes you construct will have an exclusive selfsend (even if it's a dummy). This ensures a filter-assist service user can identify all their spent enotes via key images sent alongside view tag matches.

## 2. Embedded address indices

Address indices would be embedded in public addresses (either 10 or 18 bytes; similar to, and replacing, encrypted payment IDs).

- Eliminates subaddress lookahead and the associated lookup table.
- Eliminates the distinction between main addresses, subaddresses, and embedded addresses. All three 'types' (and others as yet unimagined) would have the same format.
- Enable more advanced address generation like random addresses, point-of-sale address gen, and hidden payment IDs (addresses with payment IDs would be indistinguishable from those without).
  - 16-byte indices would allow random address generation, which improves privacy for the most privacy-focused users. Subaddresses are not ideal because restored wallets have no way of knowing the full set of subaddresses that have been generated before, and it is difficult (e.g. with the current Carrot design) to have multiple address-generating point-of-sale locations that won't collide.

#### Design

The Jamtis address index is 8 or 16 bytes. It is ciphered by the `cipher-tag` secret using TwoFish, and a short 1 or 2 byte MAC is appended for filtering deciphered indices. The full address tag equals `ciphered index | MAC`.

Here I propose including a 1-byte 'index mode', which would communicate *how* the index bytes should be interpreted. This is important for wallets so they can provide multiple index strategies (e.g. subaddress vs random generation) and handle restores from arbitrary wallets (which may use unknown index modes). The full address tag will be 18 bytes: `ciphered index (16bytes) | encoded mode (1byte) | MAC (1byte)`.

Implementation:

- Default modes
  - 0 = legacy subaddress + payment id
  - 1 = 16-byte UUID
  - 2 = randomly generated
- Encoding index `j` with mode `m` and cipher secret `s_ct`
  - `s_ct_m = s_ct[..31] | m` (note that `s_ct` is 32 bytes but `j` is 16 bytes, so 1 byte less entropy should not be a problem here)
  - `j_enc = Cipher[s_ct_m](j)` (`m` embedded in the encoding)
  - `MAC = H_2[s_ct](j_enc)` (`m` embedded in the MAC)
  - `hint = (m | 0) XOR MAC` (2 bytes)
  - `addr_tag = j_enc | hint`
- Decoding `addr_tag` with cipher secret `s_ct`
  - `j_enc = addr_tag[..16]`
  - `MAC = H_2[s_ct](j_enc)`
  - `m = addr_tag[16..] XOR MAC`
  - Check `m < 2^8` (this validates the MAC; or can check the MAC byte directly)
  - `s_ct_m = s_ct[..31] | m`
  - `j = Decipher[s_ct_m](j_enc)`
- Include mode `m` in `k^j` extensions so they are fully bound to the source address.
- Carrot specifies one 8-byte encoded payment ID be included in txs. This would change to be 18 bytes per enote, and enotes constructed for legacy enotes would shove payment IDs in those bytes (this would allow legacy payment ids for each output instead of just one per tx).

#### Indices: 16 bytes vs 8 bytes

The main argument for 8 bytes is it gives smaller addresses and enotes.

Arguments for 16 bytes:
- [UUIDs](https://en.wikipedia.org/wiki/Universally_unique_identifier) are 16 bytes and a robust industry standard. In the long view, 16 bytes makes enterprise applications more feasible.
- 16 bytes can be randomly generated without concern for collisions. Collision-resistance for 8 bytes, while not impossible to accept at 32 bits, is too low for confidence especially for heavy users.
- 16 bytes can accommodate a legacy subaddress + legacy payment ID mode, which both absorbs legacy functionality and expands it without affecting privacy.
- More bytes guards against the wide range of potential future use-cases that might demand more from the address format.
  - To be clear, the purposes of the encoded address index are enote identification and indistinguishable subaddressing, so bytes *beyond* a large ID are much less justifiable (i.e. the goal is not to add an arbitrary memo field to addresses).

#### Counterarguments

- Carrot requires subaddress tables less than legacy wallets because of 'enote scan binding' which lets you cache potentially-owned enotes for later checking against a subaddress table.
  - While an improvement, it remains a clumsy workflow unlikely to see much use.

## 3. Robust self-send attribution

Carrot adds a selfsend distinction between 'payment' and 'change' enotes, however these can be specified by any tx author so enote attribution is not robust to adversarial tx authors. The Jamtis design embeds enote types using the view-balance key, ensuring robust enote attribution and expanding the enote types to include 'churn' and 'dummy' enotes.

Affects enote construction and scanning. Adds 0 bytes to addresses and enotes.

- Improves tx history clarity.

This would probably have to be implemented if filter-assist keys are included, since Jamtis filter-assist keys require exclusive selfsends (see discussion in the filter-assist section).

#### Counterarguments

- Self-send enote attribution reduces plausible deniability if the view-balance key is compromised (e.g. due to a quantum adversary), compared to Carrot where enotes marked as 'change' could have been created by an adversarial tx author.
  - View-balance key exposure means key images can be used to flag selfsend enotes anyway, making this argument dubious.
  - Jamtis-PQ would have robust attribution (since the filter-assist key almost certainly requires it), and consistent design is preferable.

## Misc. arguments for Jamtis-Carrot

Instead of waiting for Jamtis-PQ.

- Filter-assist and address index functionality can be built up now instead of after/with a [move to PQ](github.com/monero-project/research-lab/issues/151). The move to PQ would therefore not affect wallet APIs.
- The advent of quantum threats is controversial, so PQ updates *may* get stalled or killed by opposition (either to quantum itself or its efficiency implications) or because of complexity. Tying features to PQ is therefore risky. It also muddies the waters around whether PQ is actually desired for its own sake.
- Carrot-key-hierarchy addresses looking like CryptoNote addresses is likely to be a perpetual source of confusion and/or uncertainty for users. Ambiguity is the antithesis of UX.
- Most users would not benefit from the Carrot key hierarchy as it stands, so it may not get a lot of actual use. The main beneficiaries would be cold and hardware wallets, which would finally be able to scan without key image exports. Merchants *may* gain from address generating, but the current ecosystem likely can't support much use (e.g. a grocery store could use it, but are there XMR grocery stores? or XMR atms?). In contrast, J-C includes benefits to casual mobile users (if wallets provide filter-assist scanning as a service) and privacy-conscious users (random address generation, light wallets phased out).

## Misc. arguments against Jamtis-Carrot

- Jamtis-Carrot addresses all look the same, but they *will* look different from legacy addresses. This creates one additional anonymity puddle.
  - Moving to a PQ protocol may or may not create a new puddle. If old addresses stop working with a move to PQ, then the existing puddles would disappear.
  - One reason this might materially affect user privacy is if a user uses addresses in different places. If the pool of old address users grows small, then old addresses appearing in multiple places may be relatively more linkable (smaller anonymity pool). Related to this, if a set of use patterns of old addresses shifts to new addresses, this may be a signal the underlying user is the same. It would be useful to post a blog about privacy implications when J-C wallets are released.
- Increases code complexity and requires a Carrot-Jamtis audit (possibly from the same [team](https://github.com/cypherstack/carrot_core-audit/blob/main/carrot_core-audit.pdf) that audited Carrot @jbabb). In the worst-case scenario, the work to get a minimal implementation merged could delay the FCMP++ hardfork.
  - To avoid FCMP++ delays, my code focus would be on address parsing + enote construction and validation so post-hardfork legacy wallets can send funds to Jamtis-Carrot addresses once there is code for Jamtis-Carrot wallets.
  - Auditing Jamtis-Carrot would mean less audit work for Jamtis-PQ, although still more work total.
- Jamtis-Carrot would require users to learn to recognize a new address format.
  - User education would already be required for the Carrot key hierarchy, but Jamtis-Carrot *would* have more features to teach.
- Jamtis-Carrot addresses would be 50 bytes larger (32 + 18). Txs would be larger by 18 bytes per enote for the encrypted address tags.
  - Jamtis-PQ addresses would also be much larger and include these features anyway, so size isn't necessarily a principled downside here.
- New parsing logic for J-C addresses. Public endpoints for addresses throughout the ecosystem will need to adapt any custom code that parses/checks addresses.
  - Can be mitigated by ecosystem surveys before releasing J-C wallets. Separating J-C release from FCMP++ would facilitate this.
- Adding address features creates opportunity for coercive privacy loss (e.g. being forced to give someone your Carrot view-balance secret).
  - Monero is designed to have opt-out privacy. Mitigating coercion is not within that mandate (no matter how much I or anyone wishes it were meaningfully possible), and if it was then even the CryptoNote address scheme would be less permissive than it is.
- Legacy wallets could hypothetically become 'legacy-Carrot' hybrid wallets that produce both legacy and Carrot addresses. A 'legacy-JC' hybrid is much less likely to work or make sense.
  - There is currently [not much](https://github.com/seraphis-migration/monero/issues/306) appetite for legacy-Carrot hybrid wallets.

# Discussion History
## ComputeryPony | 2026-04-07T04:24:40+00:00
Of all the points here, personally I have always been irked by the subaddress index problem and would love to see it gone.
Both from a perspective of not having to have non-deterministic scanning times and essentially having to "pick the lock" to your own enote as well as the user experience of dealing with lookup tables, main address vs subaddress vs embedded address, and inability to randomly generate address.
I would love to see embedded indices and consider the 18 byte larger address + enote a small price to pay and just part of fixing the mistake in the original implementation of subaddresses, not counting the privacy benefits of having TXs more uniform as a result.

However, what would likely be the time delay for something like that feature alone?
The greatest benefit to monero users currently is the FCMPs and I wouldn't want to delay that any longer than necessary even if I would love to see changes like these.

Would this push back the hardfork by more than 3 months or so? If so I would personally vote for it being a separate hardfork simply to get FCMPs out the door as soon as possible.

## tevador | 2026-04-07T05:21:02+00:00
> The advent of quantum threats is controversial, so PQ updates may get stalled or killed by opposition (either to quantum itself or its efficiency implications) or because of complexity. Tying features to PQ is therefore risky. It also muddies the waters around whether PQ is actually desired for its own sake.

I think it's nearly universally accepted now that PQ encryption is required ASAP for any protocol that needs forward secrecy due to "harvest now, decrypt later" type of attacks.

> Instead of waiting for Jamtis-PQ.

The change from "Jamtis-Carrot" to "Jamtis-PQ" is smaller than you think.

I'm still working on the full specs, but here is how Jamtis-PQ is planned to work, assuming the Carrot on-chain e-note format is used:

1. Each Jamtis-PQ address encodes the tuple <code>(j', K<sub>1</sub><sup>j</sup>, D<sub>2</sub><sup>j</sup>, D<sub>3</sub><sup>j</sup>, D<sub>4</sub><sup>j</sup>, Z<sub>5</sub><sup>j</sup>)</code>, where `j'` is the encrypted value of `j` and the other five values are public keys: 1x Ed25519 public key, 3x Curve25519 public keys and 1x CSIDH-1024 public key.
2. The address index `j` is a 128-bit value, `j'` is `j` encrypted with Twofish.
3. The Jamtis-PQ address length is 464 base32 characters.
4. When Jamtis-PQ is shipped, a new field is added to tx_extra of **all transactions** (a total of 132 bytes). The presence of the field is validated with a soft forking rule. The new field contains: primary view tag size in bits and the sender's CSIDH-1024 public key. This makes the Jamtis-PQ upgrade a soft-fork, so it doesn't delay the FCMP++ hard fork.
5. The 24-bit Carrot view tag is split into the primary and secondary view tags according to the primary view tag size stored in tx_extra. The primary view tag size will probably be restricted to 8 bits via a relay rule.
6. The encrypted value of `j'` is stored in the Carrot Janus anchor field. This allows for deterministic scanning.
7. The scanning performance is nearly identical to Jamtis-Carrot because the CSIDH-1024 shared secret is only calculated upon a full view tag match.

This allows for e-notes to be sent to both legacy addresses and to Jamtis-PQ addresses without any detectable on-chain differences.

Jamtis-PQ e-notes have a total of 4 shared secrets between the sender and the recipient:

1. The first X25519 shared secret is used for the primary view tag (filter assist).
2. The second X25519 shared secret is used for the secondary view tag and for decrypting `j'`.
3. The third X25519 shared secret is used for Janus attack protection and for decrypting the e-note.
4. The CSIDH-1024 post-quantum shared secret is combined with the third shared secret (hybrid encryption), which makes the e-note amount and the pubkey extensions hidden from quantum enabled attackers.

Therefore I'm strongly in favor of implementing Jamtis-PQ instead of Jamtis-Carrot to limit the number of address formats used in the Monero ecosystem.


## rbrunner7 | 2026-04-07T05:23:57+00:00
I don't understand the *Implementation notes* in chapter 1 about filter-assist keys. Maybe you can elaborate?

Two points that especially confuse me:

> Carrot [section 7.8.3](https://github.com/jeffro256/carrot/blob/pq_secure_ki/carrot.md#783-mandatory-self-send-enote-rule) has a rule about mandatory self-sends, but the design does not support it.

Does that mean that the design of Carrot has a problem not yet addressed?

> so all enotes you construct will have an exclusive selfsend (even if it's a dummy).

Does that mean that every enote will become two, with a corresponding faster growth rate for the blockchain? And if yes, is that new, or already a part of Carrot that I am not aware?

## UkoeHB | 2026-04-07T15:19:27+00:00
## @ComputeryPony 

> Would this push back the hardfork by more than 3 months or so?

It should not interfere with the hardfork. If necessary it could be released at a later date and only Legacy-Carrot would accompany FCMP++.

## @tevador 

> I think it's nearly universally accepted now that PQ encryption is required ASAP for any protocol that needs forward secrecy due to "harvest now, decrypt later" type of attacks.

For some reason I thought Jamtis-PQ would go with a PQ tx protocol. Forward secrecy is much more plausible and less complex. I definitely look forward to seeing the full protocol, as forward secrecy is quite difficult.

We can look at the details once you have published, but I will be pushing to include an index mode byte as described in the OP (the MAC would be nice but is not that important).

> Therefore I'm strongly in favor of implementing Jamtis-PQ instead of Jamtis-Carrot to limit the number of address formats used in the Monero ecosystem.

@jeffro256 what do you think about simplifying Carrot to *just* Legacy-Carrot and removing the new key hierarchy? Then you and I pushing hard on Jamtis-PQ once there is a spec (or falling back to Jamtis-Carrot if the forward secrecy effort is deemed intractable). This would alleviate FCMP++ hardfork pressure, avoid excess wallet complexity, and accelerate Jamtis feature inclusion.

## @rbrunner7 

> Does that mean that the design of Carrot has a problem not yet addressed?

At least a claim that isn't supported (specifically that all txs contain a selfsend that light wallets can identify). This only affects light wallets and IMO is a minor concern.

> Does that mean that every enote will become two, with a corresponding faster growth rate for the blockchain? And if yes, is that new, or already a part of Carrot that I am not aware?

No, most txs have a change output, which is a selfsend. Only 0-change txs will include a dummy.

## kayabaNerve | 2026-04-07T16:23:43+00:00
Without commentary on the proposal as a whole, I'd like to be clear I'm against this being discussed in conjunction with the FCMP++ HF. Specifically, I am against notable changes to CARROT or the introduction of visibly different addresses being done now, before the HF.

For one proposed change here, changing the private key used to differentiate self-send outputs with no effect into the address/TX format, I do not mind it being discussed prior to the upcoming HF.

## tevador | 2026-04-07T16:44:49+00:00
> For some reason I thought Jamtis-PQ would go with a PQ tx protocol. Forward secrecy is much more plausible and less complex. I definitely look forward to seeing the full protocol, as forward secrecy is quite difficult.

Jamtis-PQ is essentially Jamtis-RCT with an extra PQ key exchange and minor tweaks, shoehorned into the Carrot enote format for indistinguishability

I don't think there is any practically usable PQ technology that could be used to replace FCMP++ as a whole, without balooning transaction sizes to hundreds of kilobytes and having file-sized addresses.

> I will be pushing to include an index mode byte

1. "Index mode" is a wallet implementation detail. The address index will be a 128-bit opaque value and it will be up to individual wallets how it is presented to the user.
2. There is no space for more than 128 bits because the index reuses the Carrot Janus anchor field, which is 16 bytes per e-note. Technically it could be added to tx_extra (one per output), but I think that's hard to justify and ugly.
3. The Jamtis-PQ address format is already optimized around a 128-bit index size. The CSIDH prime size (1021 bits) was selected specifically so that the total address payload size is a multiple of 5 bits for optimal base32 encoding.

> the MAC would be nice but is not that important

The old Jamtis MAC is obsolete now and not needed due to the 24-bit view tag size.

## UkoeHB | 2026-04-07T17:20:48+00:00
> There is no space for more than 128 bits because the index reuses the Carrot Janus anchor field, which is 16 bytes per e-note. Technically it could be added to tx_extra (one per output), but I think that's hard to justify and ugly.

The anchor field isn't released, it can be changed to 17 bytes trivially.

> The Jamtis-PQ address format is already optimized around a 128-bit index size. 

Two empty bits out of > 2000 is not practically meaningful. It's just aesthetically slightly irksome.

> "Index mode" is a wallet implementation detail.

Yes the mode is for wallets. Without communicating the mode, multi-mode wallets and wallet interoperability become either much more difficult, unreliable, or impossible.

## tevador | 2026-04-07T17:33:46+00:00
> The anchor field isn't released, it can be changed to 17 bytes trivially.

Jamtis-PQ is designed to fit into the Carrot e-note format described [here](https://github.com/jeffro256/carrot/blob/master/carrot.md) without hard forking changes. I don't think the transaction protocol should be changed at this point. I specifically wanted to avoid any such discussions that could delay the FCMP++ hard fork.

## UkoeHB | 2026-04-07T17:38:07+00:00
> Jamtis-PQ is designed to fit into the Carrot e-note format described [here](https://github.com/jeffro256/carrot/blob/master/carrot.md) without hard forking changes. I don't think the transaction protocol should be changed at this point. I specifically wanted to avoid any such discussions that could delay the FCMP++ hard fork.

This is a very frustrating response. It's not released, it's not merged, it doesn't need an audit, the diff to change it is trivial (1 line to change the `JANUS_ANCHOR_BYTES` constant), and the hardfork is months away.

## kayabaNerve | 2026-04-07T17:57:05+00:00
@tevador Off-topic, but I prior sketched a composition to discuss what one would look for a PQ transaction protocol, the goal being to modularize each component. In my work, I found that nesting commitments meant we could actually have minimal spend keys and so on, due to expanding within the spend proof: https://github.com/kayabaNerve/monero-pq This was chicken scratch I did before getting burnt out and stepping back though, and being a couple years old, is lacking my current knowledge and more modern developments...

RE: the future of Monero addresses, I'm not for any further changes before the FCMP++ HF except as I scoped above. Targeting deployment in a later upgrade isn't something I object to, so long as so clearly scoped.

One thing I'd like clarified is JAMTIS-CARROT vs JAMTIS. I'd assume, from an initial read, JAMTIS-CARROT would be easier to implement (with more consolidated code) due to closing the gap between CARROT and JAMTIS, not replacing it like JAMTIS would?

Personally, while we can discuss the UX of JAMTIS/JAMTIS-CARROT as establishing features which would carry to something like JAMTIS-PQ as well, I'm uncomfortable at the idea of having three active address formats. A key part of CARROT was the complete continuation of all existing addresses and the indistinguishability between them (except maybe an incredibly marginal amount of bias which could be detected by a QC? I remember some stray comment about that). In that sense, I would prefer to wait for a PQ address format, especially if it makes a selling point out of the new and unique features the post-quantum address format would bring.

One would have to argue that JAMTIS-CARROT fills a gap between CARROT and a PQ proposal which justifies maintaining yet another address format. The only way I see that happening if if the time-to-live for JAMTIS-CARROT is ~more than a year, year a half, sooner than a PQ format, when if we don't adjust the FCMP++ HF, both would presumably be kicked to a future upgrade anyways. Unfortunately, I think that likely makes this proposal untimely.

## tevador | 2026-04-07T19:26:18+00:00
@UkoeHB I consider the Carrot e-note format to be frozen. I think it's too late for any non-security related changes. I will refrain from discussing this further. I'd rather focus on completing Jamtis-PQ.

> The only way I see that happening if if the time-to-live for JAMTIS-CARROT is ~more than a year, year a half, sooner than a PQ format

I think the work should focus on deploying FCMP++ as soon as possible and then adding PQ encryption as the next step. The other Jamtis features are less important and it's better to end up with only 2 distinct address formats rather than 3.

If shipping FCMP++ only with the legacy key hierarchy makes it easier to deploy, then it might be worth considering.

## kayabaNerve | 2026-04-07T19:55:09+00:00
I can agree with that, tevador, even if a bit more strict than my own message. As for FCMP++ without CARROT, as we originally discussed, at least a minimal set of tweaks is needed in order to achieve forward secrecy (the additional derivation of the re-randomization over T). I've told jeffro I won't endorse CARROT if it threatens the FCMP timelines, but I believe at this point, the addressing protocol is specified, implemented, and reviewed, and therefore not a concern to the FCMP++ timeline _except for how ecosystems which re-implemented address derivation may be delayed_. At the same time, I don't see how Monero's HF would be blocked by such ecosystem considerations, as actual integrations use `wallet2` which will be ready and able.

# Action History
- Created by: UkoeHB | 2026-04-07T01:16:19+00:00
