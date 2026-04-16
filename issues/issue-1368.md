---
title: Monero Research Lab Meeting - Wed 08 April 2026, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/1368
author: Rucknium
assignees: []
labels: []
created_at: '2026-04-08T15:08:33+00:00'
updated_at: '2026-04-14T21:12:25+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

Live log: https://libera.monerologs.net/monero-research-lab

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/meeting.html?p1=1440)

Main discussion topics:

1. Greetings

2. Updates. What is everyone working on?

3. [FCMP code integration audit overview](https://github.com/seraphis-migration/monero/issues/294).

4. [FCMP beta stressnet](https://github.com/seraphis-migration/monero/issues/166).

5. [Grease Payment Channels](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/651).

6. [Discussion: Post-quantum security and ethical considerations over elliptic curve cryptography](https://github.com/monero-project/research-lab/issues/131). [Safeguarding cryptocurrency by disclosing quantum vulnerabilities responsibly](https://research.google/blog/safeguarding-cryptocurrency-by-disclosing-quantum-vulnerabilities-responsibly/ ).

7. [More Jamtis features in Carrot](https://github.com/seraphis-migration/monero/issues/310).

8. Any other business

Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: Rucknium

Previous meeting agenda/logs:

#1365 

# Discussion History
## Rucknium | 2026-04-14T21:12:25+00:00
Log

> __< kayabanerve:matrix.org >__ I may or may not be present but my update is https://github.com/monero-oxide/monero-oxide/commit/cba7117d2cb4a45444c54005604b2a943a8517f1     

> __< kayabanerve:matrix.org >__ I did the initial changes to indexing instructed by CS's latest commentary, and merged the performance fixes jberman wanted. I have to do a complete side-by-side review to confirm there's no other discrepancies/deviations, but that should model the performance hit and be usable for that evaluation.     

> __< kayabanerve:matrix.org >__ I'm sure sgp_:monero.social: can provide commentary on the being-discussed audits to follow up.     

> __< gingeropolous >__ i won't be present, my update is the final 5% of monerosim. some issue where the particular launch order of activity causes some wallets to not send, while others send tons of txs.      

> __< rucknium >__ Meeting time! https://github.com/monero-project/meta/issues/1368     

> __< tevador >__ Hi     

> __< jpk68:matrix.org >__ Hello     

> __< rucknium >__ 1. Greetings     

> __< vtnerd >__ Hi     

> __< iamnew117:matrix.org >__ Hello     

> __< rucknium >__ 2. Updates. What is everyone working on?     

> __< UkoeHB >__ Hi     

> __< jberman >__ waves     

> __< UkoeHB >__ Me: finished carrot_core review, wrote https://github.com/seraphis-migration/monero/issues/310, likely to look at multisig next (blocking hf afaik)     

> __< jberman >__ Reviewing upstream PR's, rebased https://github.com/seraphis-migration/monero/pull/89 , FCMP++ audit tasks     

> __< jpk68:matrix.org >__ I've been doing a bit of preliminary research on SAM protocol parameters, namely signature and encryption types for destinations     

> __< jpk68:matrix.org >__ Can elaborate if anyone is interested     

> __< kayabanerve:matrix.org >__ I posted my update prior re: the Generalized Bulletproofs.     

> __< vtnerd >__ me: lws+lwsf are up-to-date with fcmp++/carrot and working on testing /feed protocol this week     

> __< rucknium >__ 3. FCMP code integration audit overview (https://github.com/seraphis-migration/monero/issues/294).     

> __< jberman >__ We're engaged in discussions with a number of candidates for Phase 1. From the quotes we've received and candidates we've spoken to, we feel $50k is a sound budget for this phase. I've also opened a CCS requesting ~$150k budgeted for all 3 phases here: https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/663     

> __< jberman >__ AFAIK, we should have all quotes by next week's meeting     

> __< rucknium >__ Anything more on this item?     

> __< jberman >__ Nothing from me     

> __< rucknium >__ 4. FCMP beta stressnet (https://github.com/seraphis-migration/monero/issues/166).     

> __< rucknium >__ AFAIK, this update from kayabanerve:matrix.org  is about beta stressnet readiness progress: https://github.com/monero-oxide/monero-oxide/commit/cba7117d2cb4a45444c54005604b2a943a8517f1     

> __< articmine >__ Sorry I am late      

> __< rucknium >__ "I did the initial changes to indexing instructed by CS's latest commentary, and merged the performance fixes jberman wanted. I have to do a complete side-by-side review to confirm there's no other discrepancies/deviations, but that should model the performance hit and be usable for that evaluation."     

> __< rucknium >__ CS = Cypher Stack.     

> __< jberman >__ kayaba notes those 2 issues highlighted in that commit description are also now immediate blockers, and I pinged Diego on that as well     

> __< jberman >__ So the main blocking items there are now 1) a response to those raised issues, and 2) kayaba's complete review     

> __< jberman >__ I can also check the perf hit today/tomorrow     

> __< jberman >__ W.r.t. beta stressnet, yep this is the final blocking task     

> __< jberman >__ Would like this item settled before launching     

> __< rucknium >__ 5. Grease Payment Channels (https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/651).     

> __< rucknium >__ More discussion on Grease?     

> __< syntheticbird >__ Greasus christ when are we going to have a payment channel 🥁     

> __< rucknium >__ 6. Discussion: Post-quantum security and ethical considerations over elliptic curve cryptography (https://github.com/monero-project/research-lab/issues/131). Safeguarding cryptocurrency by disclosing quantum vulnerabilities responsibly (https://research.google/blog/safeguarding-cryptocurrency-by-disclosing-quantum-vulnerabilities-responsibly/).     

> __< code2 >__ lol -- I've still writing up the distributed KEs ideas. Been a bit tied up with easter holidays and things the last few days     

> __< code2 >__ still confident I'll get it out this week     

> __< rucknium >__ code2: Thanks     

> __< syntheticbird >__ Ever since the last comment of this issue and the discussion about economical safety during the MRL meeting there has been discussion about jamtis and carrot.      

> __< syntheticbird >__ ngl a recap about what where we are on PQ discussion would be greatly appreciated     

> __< syntheticbird >__ from what i remember, adding turnstile support was on the table for carrot     

> __< UkoeHB >__ tevador is working on a Jamtis-PQ spec. The PQ aspect would be aimed at forward secrecy in case of a future quantum adversary. PQ tx protocol sounds infeasible with current quantum crypto.     

> __< tevador >__ Carrot PQ forward secrecy: https://github.com/jeffro256/carrot/blob/master/carrot.md#211-address-conditional-forward-secrecy     

> __< semisimple >__ After looking a bit into the quantum topic, it seems to me it is a really tough nut to crack. Almost all PQC schemes have extremely large address and signature sizes that it becomes really tough to implement into a blockchain that is targeting a high number of transactions. Even full quantum blockchains like QRL without much privacy are not really efficient     

> __< tevador >__ Jamtis-PQ aims to close this last privacy gap (forward secrecy if an address is known)     

> __< tevador >__ Jamtis-PQ will feature CSIDH-1024 for quantum-resistant public key encryption     

> __< semisimple >__ UkoeHB: I would be interested how that would look like. Is there a draft or do you want to wait until it is finished?     

> __< syntheticbird >__ I thought isogeny based public cryptosystem were broken during the NIST competition ?     

> __< tevador >__ It's work in progress     

> __< tevador >__ syntheticbird: the break of SIKE/SIDH has no effect on CSIDH, which is a different cryptosystem     

> __< jpk68:matrix.org >__ Is CSURF still being considered?     

> __< syntheticbird >__ tevador: ack.     

> __< UkoeHB >__ semisimple: I am not working on it, tevador is.     

> __< tevador >__ Yes, the selected parameters are sort of a CSURF variant     

> __< tevador >__ Details here (this will be part of the Jamtis-PQ specs): https://github.com/monero-project/research-lab/issues/151#issuecomment-3640488509     

> __< syntheticbird >__ If I understand correctly the last tech meeting. Their is advocacy for skipping the new carrot key hierarchy for the upcoming HF and push towards deploying Jamtis-PQ after that? is that correct?     

> __< tevador >__ A limitation of Jamtis-PQ is that the view tag is still calculated using traditional ECDH, so a quantum attacker will be able to locate e-notes, but not decrypt them.     

> __< UkoeHB >__ syntheticbird: that's what I have advocated. No one else has commented yay or nay.     

> __< jberman >__ tevador: what are your thoughts on contracting a research firm to explore a maximally efficient complete PQ protocol?     

> __< tevador >__ jeffro256 should comment on that     

> __< tevador >__ jberman: I think kayabanerve made some estimates around ~500 KB per transaction for a full PQ protocol     

> __< semisimple >__ I have no credibility, but in my opinion the quantum threat is indeed not to be underestimated even though it is probably still a bit in the future. I consider any effort and funds to be well spent.     

> __< tevador >__ Probably some work should start on this front, but I'm skeptical anything practical will come up. There was a RingCT-like PQ protocol published a while ago that had ~100 KB transactions.     

> __< jberman >__ tevador: "and being a couple years old, is lacking my current knowledge and more modern developments" presumably there may be further developments on that front     

> __< UkoeHB >__ Can RingCT or FCMP++ not be translated 1:1 to a PQ scheme?     

> __< kayabanerve:matrix.org >__ I don't think there's a clear path to decentralizing Grease and I'm unclear about the benefit of middle-man-premised payment channel technology     

> __< kayabanerve:matrix.org >__ I'm interested to see JAMTIS-PQ (or any other such scheme) following the FCMP++ upgrade.     

> __< syntheticbird >__ ukoehb what do you mean     

> __< tevador >__ UkoeHB: probably something based on STARKS, which are hash based, so PQ proof.     

> __< syntheticbird >__ oh wait nvm i just understand     

> __< kayabanerve:matrix.org >__ FCMP++ is premised as a composition of membership, spend-auth + linkability, balance, and range. I did chicken scratch on a PQ composition a couple year ago, suggesting something approximate to Bitcoin's P2PKH.     

> __< kayabanerve:matrix.org >__ Specifically, I noted on a specific additively-homomorphic commitment scheme (Ajtai?) be used for all computational purposes, yet the current output key be replaced with a 32-byte Blake2 hash or similar, in order to achieve succinct outputs and likely addresses as well. All unpacking would be deferred to the inputs.     

> __< UkoeHB >__ tevador: if hashes are required, why would CSIDH key exchange work? Perhaps I should just read up on it.     

> __< kayabanerve:matrix.org >__ The clearest way to achieve the ~5 goals of a private payment protocol is yes, to take the rock-solid FRI with conservative parameters and call it a day. Ideally, the choice of hashes and commitments used are sufficiently forward-thinking to enable more efficient proofs in the future.     

> __< tevador >__ There is no hash-based post-quantum key exchange protocol. Hash-based protocols are only for proofs and signatures.     

> __< kayabanerve:matrix.org >__ There are more specific proofs we could discuss the application ol for each and every component. That discussion would be poor due to how involved it'd be and the fact we aren't currently investing that involvement (even if we should be).     

> __< jbabb:cypherstack.com >__ I have seen these recently tho haven't had time to digest them     

> __< jbabb:cypherstack.com >__ SHRIMPS: 2.5 KB post-quantum signatures across multiple stateful devices https://delvingbitcoin.org/t/shrimps-2-5-kb-post-quantum-signatures-across-multiple-stateful-devices/2355     

> __< jbabb:cypherstack.com >__ see also the similar SHRINCS: 324-byte stateful post-quantum signatures with static backups324-byte stateful post-quantum signatures with static backups https://delvingbitcoin.org/t/shrincs-324-byte-stateful-post-quantum-signatures-with-static-backups/2158     

> __< jbabb:cypherstack.com >__ ofc not applicable to us but interesting comparison points     

> __< kayabanerve:matrix.org >__ Hash-based signatures, such as SHRINCS presumable is by the name, almost certainly cannot be used by Monero.     

> __< UkoeHB >__ tevador: I guess I'm confused how you can do a key exchange but can't do a signature.     

> __< kayabanerve:matrix.org >__ Monero needs a non-interactive re-randomizable signature scheme, and I'd say one which reasonably supports arbitrary threshold schemes while remaining indistinguishable.     

> __< UkoeHB >__ With EC-like operations.     

> __< kayabanerve:matrix.org >__ A hash-based scheme wouldn't achieve re-randomization.     

> __< tevador >__ It's the opposite. With hashes, you can do a signature, but can't do key exchange. You need CSIDH or lattices for key exchange.     

> __< kayabanerve:matrix.org >__ ... wouldn't offer?     

> __< kayabanerve:matrix.org >__ ... wouldn't enable?     

> __< kayabanerve:matrix.org >__ Ugh. Or you use a non-rerandomizable signature scheme, but you do the signature transparently, then publish a ZK proof that a valid signature exists (without revealing which public key was associated) D: Such a mess to consider.     

> __< tevador >__ Yes, if we want to keep stealth addresses, then it has so be something lattice-based.     

> __< UkoeHB >__ Can you use CSIDH or lattices for signatures? Or is it just prohibitively expensive?     

> __< kayabanerve:matrix.org >__ Here's my extremely-limited chicken scratch from a couple years ago. I started the notes right as I hit my burn out: https://github.com/kayabaNerve/monero-pq     

> __< tevador >__ CSIDH can do plain signatures, but not the kind Monero needs.     

> __< kayabanerve:matrix.org >__ Note it can be criticized to all hell for its addressing proposal and it was never meant to be an address proposal like JAMTIS. It was meant to be a very basic draft of modularity and composition to enable discussing and scoping individual sections, while any actual development would be on a dead-simple, slow af, giant, FRI-ba [... too long, see https://mrelay.p2pool.observer/e/j53ivfcKTDZMQ1Q0 ]     

> __< UkoeHB >__ I will look into that. It would be odd to me for plain signatures to work, but not e.g. RingCT.     

> __< kayabanerve:matrix.org >__ I wouldn't be surprised about how one couldn't re-randomize an isogeny map     

> __< kayabanerve:matrix.org >__ tevador: Maybe a code-based signature?     

> __< kayabanerve:matrix.org >__ Not to say we should move to code-based cryptography, to say I don't believe we are explicitly limited to lattices. I'd assume, at this time, we'd be limited to lattices or codes.     

> __< kayabanerve:matrix.org >__ Lattices are the most likely candidate for good performance across all proofs, but any LWE-premised proofs are going to be hell to put into a multisignature protocol unless the signature scheme was explicitly designed with that in mind (such as Raccoon)     

> __< rucknium >__ 7. More Jamtis features in Carrot (https://github.com/seraphis-migration/monero/issues/310).     

> __< tevador >__ Anyways... The roadmap is: 1) FCMP++/Carrot 2) Jamtis-PQ (for full PQ privacy, but not soundness. 3) Some full PQ protocol.     

> __< kayabanerve:matrix.org >__ 👍     

> __< tevador >__ The proposal is not to ship the Carrot key hierarchy with FCMP++     

> __< kayabanerve:matrix.org >__ I don't believe that was planned at this time     

> __< tevador >__ I'm quoting #310     

> __< kayabanerve:matrix.org >__ And I'm noting I think that specific comment is already the plan, in case someone wants to correct me or further explain any distinction     

> __< syntheticbird >__ a counter argument to this proposal, carrot self-enote are symmetrically encrypted and do provide some level of QC protection. This is minimal but can be used by people right now to mitigate damage from future decryption. If we remove the new hierarchy for jamtis PQ we're removing this capability and we do not have any guarantee on when Jamtis-PQ will be shipped      

> __< syntheticbird >__ hell, some would fcmp++ would be on mainnet by now     

> __< jberman >__ there have been some discussions about bringing the Carrot key hierarchy in with the fork. I'm personally in favor of shipping after so as to not delay the fork     

> __< tevador >__ Any delay to FCMP++ means more transactions that WILL be fully deanonymized in the future.     

> __< tevador >__ I think the wallet-side work will be significantly reduced if we stick to the legacy hierarchy for the fork.     

> __< rucknium >__ UkoeHB: Do you have more comments now about "More Jamtis features in Carrot"?     

> __< tevador >__ I think it became "Fewer Jamtis features in Carrot"     

> __< rucknium >__ Any more discussion on this item?     

> __< jberman >__ (btw I have another agenda item to raise, apologies for the late addition)     

> __< tevador >__ What is planned for the fork (AFAIK): Janus attack mitigation, forward secret key images and full chain membership set.     

> __< rucknium >__ jberman:monero.social: You can raise it.     

> __< UkoeHB >__ The proposal is to never ship the Carrot key hierarchy, not to do it after.     

> __< jberman >__ Back in June 2024, Aaron (Sarang) completed a security review of the FCMP++ composition at Cypher Stack. UkoeHB recently raised that that report didn't have a follow-up formal review, and I figured it would make sense to have Cypher Stack conduct such a review because they have a new team that has also identified issues in th [... too long, see https://mrelay.p2pool.observer/e/vqGmvvcKakJZMjZa ]     

> __< jberman >__ If at all possible, would love to get MRL sign-off on this. I apologize for not raising this further in advance (health complications got in the way).     

> __< syntheticbird >__ (may the good health be with you)     

> __< jberman >__ The report: https://github.com/cypherstack/fcmp-review/releases     

> __< tevador >__ More reviews can't hurt if it's done in parallel with other work.     

> __< UkoeHB >__ Sounds good to me     

> __< articmine >__ I support this review      

> __< UkoeHB >__ I also proposed an audit for tevador's mx25519 crate.     

> __< rucknium >__ We had a "rule" to post proposals for spending from the FCMP research fund at least 24-48 hours before the MRL meeting for final approval. This review seems very reasonable, but is it possible to follow the rule? Will a lot of time be lost if we wait a week?     

> __< jberman >__ UkoeHB: Ya I think that one is worth a distinct CCS, just need to follow through on it     

> __< jberman >__ rucknium: At worst we lose a week + possibly availability with CS for other work at a later time, so it could compound a bit     

> __< jberman >__ Imo this would be a low risk, relatively low cost, solid value item to bang out     

> __< rucknium >__ What do others think? Follow the rule in this case or no?     

> __< syntheticbird >__ rules are meant to be broken     

> __< syntheticbird >__ idk something inspirational like that yk what i mean     

> __< rucknium >__ syntheticbird:monero.social: That phrase came up in my head too 🙂     

> __< articmine >__ Given the lack of opposition there is a case for making an exception      

> __< rucknium >__ We'll make an exception. More discussion of this proposal? Any objections or reservations?     

> __< jberman >__ I'll highlight a comment shared by kayaba that it's CS conducting a review of CS, rather than an independent party     

> __< syntheticbird >__ nope     

> __< jberman >__ My contention is that since this is essentially a new team that has demonstrably identified issues in existing work (their GPB follow-up), that they are close to de facto independent / worthy of the task     

> __< kayabanerve:matrix.org >__ I'm not opposed to the follow-up composition review     

> __< rucknium >__ jberman:monero.social: I agree. What would be an alternative? Another firm doing a review?     

> __< sgp_ >__ I'm not opposed for the price     

> __< kayabanerve:matrix.org >__ In an ideal sense, though I don't think CS actually represents a conflict     

> __< jberman >__ rucknium: yep     

> __< rucknium >__ What delicate parts of the protocol would this review hit?     

> __< rucknium >__ In other words, what could go wrong if a review misses something?     

> __< kayabanerve:matrix.org >__ This will primarily cover the interoperability between the membership and SA+L proof, and the SA+L proof itself     

> __< rucknium >__ kayabanerve:matrix.org  and sgp_:monero.social  : Neither of you are in favor, just "not opposed"? Is that correct?     

> __< kayabanerve:matrix.org >__ I honestly don't care and effectively see it as a "why not" at an acceptable price, to be blunt     

> __< kayabanerve:matrix.org >__ Can't hurt, cheap enough it's probably worth it for peace of mind, but I already have peace of mind and don't care accordingly     

> __< kayabanerve:matrix.org >__ That's why I said I'm not opposed and am effectively kicking the advocacy to jberman, though others hear also seemed to think it worthwhile     

> __< rucknium >__ The price is good. Makes it easier to approve.     

> __< kayabanerve:matrix.org >__ *others here     

> __< sgp_ >__ rucknium: Ideally multiple firms would be solicited but for the price I'm not concerned, basically     

> __< sgp_ >__ More solicitations for this is likely to be a waste of everyone's time     

> __< rucknium >__ I'm seeing some in favor and some "not opposed". No one opposed. I think that's reaches the threshold to proceed with it.     

> __< genoce:matrix.org >__ > <syntheticbird> a counter argument to this proposal, carrot self-enote are symmetrically encrypted and do provide some level of QC protection. This is minimal but can be used by people right now to mitigate damage from future decryption. If we remove the new hierarchy for jamtis PQ we're removing this capability and we do not have any guarantee on when Jamtis-PQ will be shipped      

> __< genoce:matrix.org >__ I thought that the symmetrically encrypted carrot self-enote would work without the new carrot key hierachy too? UkoeHB     

> __< jberman >__ Thank you rucknium:monero.social. I'll respect the rule going forward, appreciate the exception     

> __< rucknium >__ We can end the meeting here. Feel free to continue discussing topics. Thanks everyone.     

> __< UkoeHB >__ genoce: yes, the carrot hierarchy should only be useful for adding wallet functionality. But the main beneficiaries are cold/hardware wallets, so most users wouldn't have a reason to adopt it. Much simpler to just wait a little longer for Jamtis-PQ so most or all users can benefit and wallet complexity is minimized.     

> __< genoce:matrix.org >__ UkoeHB: I agree with this take     

> __< genoce:matrix.org >__ Thank you for your work     

> __< jeffro256 >__ SyntheticBird Cryptographic support for the PQ turnstile for Carrot is already in the updated version of the spec and implemented in the code > <syntheticbird> from what i remember, adding turnstile support was on the table for carrot     

> __< tevador >__ Is this the latest version? https://github.com/jeffro256/carrot/blob/master/carrot.md     

> __< jeffro256 >__ > A limitation of Jamtis-PQ is that the view tag is still calculated using traditional ECDH, so a quantum attacker will be able to locate e-notes, but not decrypt them.     

> __< jeffro256 >__ This can have some pretty bad long-term privacy consequences when the account is used multiple times, and the adversary has multiple public addresses of people. They can effectively make a probabilistic social graph of interactions, with its certainty increasing the more "links" between accounts. I have a post on the Jamtis gi [... too long, see https://mrelay.p2pool.observer/e/vMaPwfcKcTc2Zmpt ]     

> __< jeffro256 >__ If we're going the PQ exchange route, I cannot support having the view tag key exchange happen over an elliptic curve, because that somewhat defeats the point of the regular key exchange      

> __< jeffro256 >__ tevador yes      

> __< jeffro256 >__ PQ changes are in https://github.com/jeffro256/carrot/pull/6     

> __< syntheticbird >__ ukoehb ack on the encrypted self-enote. I'm happy to be wrong. In this case I would tend to support your proposal, but as seen with Seraphis and FCMP++ timeline, waiting a "little longer" is really not something I would be betting on     

> __< jeffro256 >__ For more info on the risk: read the "LW2LW relationship" section at https://gist.github.com/tevador/d3656a217c0177c160b9b6219d9ebb96?permalink_comment_id=5044400#gistcomment-5044400. Assume that the PQ adversary with possession of public Jamtis-PQ addresses is same as a filter-asset LWS     

> __< UkoeHB >__ syntheticbird: skipping carrot key hierarchies would bring Jamtis-PQ closer since there's less wallet work needed. But yes, a little longer may mean over a year.     

> __< UkoeHB >__ jeffro256: what would be the perf multiplier for doing view tags on CSIDH?     

> __< tevador >__ jeffro256: Sadly, using CSIDH for the view tag is not feasible for performance reasons. Scan times would increase 1000x.     

> __< UkoeHB >__ tevador: will Jamtis-PQ be able to prevent Janus attacks that use the CSIDH key? Since `d_e` won't be recomputed.     

> __< UkoeHB >__ Since the janus anchor isn't included *     

> __< tevador >__ The CSIDH key is not subject to the Janus attack because all addresses use the same base curve, e.g. all addresses have Z_5 = z5^j * E where E is the base curve.     

> __< UkoeHB >__ tevador: I don't follow. What prevents someone from copy pasting `z5^j * E` to an address with `z5^z * E`?     

> __< tevador >__ Can you be more specific? Which value would the attacker put in the transaction?     

> __< tevador >__ Specifically, what Z_e and j would be used to mount a Janus attack.     

> __< tevador >__ I don't see how to execute the attack in a way that matches all 4 shared secrets. At least X     

> __< tevador >__ X3 will differ     

> __< UkoeHB >__ Reading #151 now     

> __< tevador >__ jeffro256: Let's define key exchange properties: 1) Fast enough for view keys. 2) Supports unlinkable subaddresses. 3) Address size < 1 KB.     

> __< tevador >__ CSIDH has 2) and 3). NTRU/Kyber have 1) and 3). AFAIK there is no PQ key exchange that has all 3 properties.     

> __< jpk68:matrix.org >__ Would McEliece have 1 and 2? Apologies if this is a dumb question     

> __< tevador >__ AFAIK McEliece has none.     

> __< jpk68:matrix.org >__ Alright, thanks. Just asked because it was mentioned in the Jamtis-PQ spec (and disqualified for addresses that are too large).     

> __< UkoeHB >__ tevador: 151 mentions CSIDH keys need to be validated, implying a hf would be required. Did this change? You mentioned soft-forking.     

> __< UkoeHB >__ tevador: Ok I am even more confused. Is there only one CSIDH key in addresses? Is the shared secret supposed to be recovered after decrypting the index? Wouldn't that allow a PQ observer who knows an address to uncover indices? 24 bits of view tags + however many bits an index could heuristically imply means we'd have to assume PQ observers have strong confidence in the set of non-auxiliary-selfsend enotes owned by each      

> __< UkoeHB >__ user (whose addresses are known). Only amounts, key images, and change-identification would be hidden.     

> __< UkoeHB >__ Amendment: all selfsends would be protected from all but primary view tag checks (and auxiliary selfsends would be immune to this as well).     

> __< syntheticbird >__ Doesn't McEliece have the longest key in the entire PQ algorithm kingdom     

> __< syntheticbird >__ lmfao 128 bit security is a 1MB public key     

> __< UkoeHB >__ Mitigation for exclusive selfsend primary view tag analysis: only use 1 byte of the view tag, the rest gibberish. A filter-assist layer will send all 1-byte matches along with 3-byte matches (assuming 3 bytes for the primary view tag - a 2000x cost for CSIDH-1024 would be 11-bit slowdown, so 3 bytes seems reasonable) to the view-balance layer. The vb layer checks exclusive selfsends for both 1-byte and 3-byte matches,      

> __< UkoeHB >__ and the normal path (with CSIDH) for 3-byte matches. Auxiliary selfsends would be checked for all txs with exclusive selfsend successes.     

> __< UkoeHB >__ Instead of 1b + 2b gibberish, can do complementary view tag with `k_vb` for a small optimization. So normal: 3b primary view tag, exclusive selfsend: 1b primary + 2b complementary, auxiliary selfsend: 3b auxiliary view tag.     

> __< UkoeHB >__ Filter-assist layer only needs to care about npbits/ncbits. The vb layer can branch on how large the match is.     

> __< UkoeHB >__ Ah the exact index `j` would be hidden by `s_ct` (unless the generate-address tier is compromised). So only known address matching would be possible.     

> __< UkoeHB >__ Which isn't a problem because all known addresses can be linked via `k_fa` from solving DLPs.     

> __< UkoeHB >__ Only a small problem* since matching enotes to specific addresses is a bit useful for fund flow analysis.     



# Action History
- Created by: Rucknium | 2026-04-08T15:08:33+00:00
