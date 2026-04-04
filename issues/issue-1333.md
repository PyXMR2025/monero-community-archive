---
title: Monero Research Lab Meeting - Wed 28 January 2026, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/1333
author: Rucknium
assignees: []
labels: []
created_at: '2026-01-27T23:14:13+00:00'
updated_at: '2026-02-11T01:48:27+00:00'
type: issue
status: closed
closed_at: '2026-02-11T01:48:27+00:00'
---

# Original Description

Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/meeting.html?p1=1440)

Main discussion topics:

1. Greetings

2. Updates. What is everyone working on?

4. [FCMP and CARROT reviews and audits status](https://cryptpad.fr/sheet/#/2/sheet/view/yPVIUywwA9-deE9VF6GYm9bXbPdCerdST3UDEEfBxcM/embed/).

5. [FCMP alpha stressnet](https://monero.town/post/6763165).

6. Bulletproof prover and verifier optimization research.

7. [CARROT Outgoing View Keys (OVKs)](https://github.com/jeffro256/carrot/blob/master/carrot.md#22-new-wallets-only).

8. Any other business

Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: Rucknium

Previous meeting agenda/logs:

#1330 

# Discussion History
## Rucknium | 2026-01-31T21:20:53+00:00
Log

> __< rucknium >__ Meeting time! https://github.com/monero-project/meta/issues/1333     

> __< rucknium >__ 1. Greetings     

> __< jeffro256 >__ Howdy     

> __< articmine >__ Hi     

> __< rbrunner >__ Hello     

> __< gingeropolous >__ howdy do     

> __< emsczkp:matrix.org >__ hi     

> __< DataHoarder >__ hullo     

> __< midipoet >__ hi     

> __< cyrix126:gupax.io >__ Hello     

> __< jberman >__ waves     

> __< rucknium >__ 2. Updates. What is everyone working on?     

> __< DataHoarder >__ RandomX V2 testing, specially around new prefetch parameter tweak now part of the main design https://github.com/SChernykh/RandomX/blob/v2/doc/design_v2.md (and is considered finalized for the PR)     

> __< gingeropolous >__  trying to put the final touches on the monerosim package.      

> __< rucknium >__ me: Selfish mining countermeasures analysis.     

> __< rucknium >__ gingeropolous:monero.social: How did your 1000-node test go?     

> __< jeffro256 >__ Me: finished reviewing j-berman's unbiased hash-to-point changes, fixiing beta scaling tests, working on my Monerotopia presentation      

> __< gingeropolous >__ its working well. I want to demonstrate something useful, so im getting a simulation that does a network upgrade (going from one version of monerod to another.... in this case, one that that has tx relay v2 pulled in). Currently the user agent code isn't handling the wallet correctly during the daemon restart. But otherwise it runs     

> __< jberman >__ me: preparing the FCMP++ integration code for auditing, finalizing tx relay v2     

> __< rucknium >__ gingeropolous:monero.social: Fantastic. Thanks.     

> __< rucknium >__ 3. FCMP and CARROT reviews and audits status (https://cryptpad.fr/sheet/#/2/sheet/view/yPVIUywwA9-deE9VF6GYm9bXbPdCerdST3UDEEfBxcM/embed/).     

> __< rucknium >__ Was the Cypher Stack Generalized Bulletproofs review & suggestions posted? I didn't see it.     

> __< jeffro256 >__ No updates from me      

> __< rucknium >__ diego:cypherstack.com: Has the Generalized Bulletproofs new review been posted?     

> __< jberman >__ sgp_:monero.social reached out to zkSec (specifically a curve trees author) to review divisors, don't believe there's been an update     

> __< jberman >__ re: integration audit, I'm aiming to have the code ready by EOW, and will start planning an audit approach then     

> __< rucknium >__ brandon:cypherstack.com: Any update on posting the Generalized Bulletproofs review draft? > <brandon:cypherstack.com> yeah, i plan on posting it soon(tm)     

> __< rucknium >__ "I'm still cleaning it up" is a valid response :)     

> __< rucknium >__ I'll go to the next agenda item. Maybe Cypher Stack staff will come in later.     

> __< rucknium >__ 5. FCMP alpha stressnet (https://monero.town/post/6763165).     

> __< diego:cypherstack.com >__ yes > <rucknium> diego:cypherstack.com: Has the Generalized Bulletproofs new review been posted?     

> __< jberman >__ I'm still thinking it would be nice to have tx relay v2 tested on alpha. I'm going to prepare all the changes that would be solid for a v1.6 release (nothing significant at this stage), and also port those changes to the staging branch in prep for beta     

> __< diego:cypherstack.com >__ it's on iacr     

> __< jberman >__ If we have capacity to get a v1.6 release out, then that would be solid, but if not, then we'll just have it ready for beta     

> __< vtnerd >__ sorry Im late, here now     

> __< jeffro256 >__ So tx relay v2 changes coming along well?     

> __< jberman >__ Generally, I remain confident that alpha achieved a level of stability that is ready to move to beta     

> __< diego:cypherstack.com >__ grabbing the link, moment     

> __< jberman >__ jeffro256: Yep, changes are pretty much done     

> __< jberman >__ Completed boog900:monero.social 's latest review round     

> __< brandon:cypherstack.com >__ I submitted the generalized bulletproof paper to iacr last week but the editors have not posted it yet. As soon as I get the link sent to me I will share it here.     

> __< rucknium >__ brandon:cypherstack.com: Thank you!     

> __< jeffro256 >__ jberman: agreed, thanks for all that work     

> __< rucknium >__ I agree that alpha should try tx relay v2 because we don't know yet if beta stressnet should have changes to Generalized Bulletproofs (GBP).     

> __< jberman >__ ack     

> __< rucknium >__ 6. Bulletproof prover and verifier optimization research.     

> __< rucknium >__ emsczkp:matrix.org: Did you find time to look at  https://moneroresearch.info/285 Wang, N., Wang, Q., Liu, D., Esgin, M. F., & Abuadbba, A. (2025). BulletCT: Towards More Scalable Ring Confidential Transactions With Transparent Setup. ?     

> __< emsczkp:matrix.org >__ > <rucknium> emsczkp:matrix.org: Could you read https://moneroresearch.info/285  Wang, N., Wang, Q., Liu, D., Esgin, M. F., & Abuadbba, A. (2025). BulletCT: Towards More Scalable Ring Confidential Transactions With Transparent Setup. BulletCT: Towards More Scalable Ring Confidential Transactions With Transparent Setup.     

> __< emsczkp:matrix.org >__ I don't want to dominate this agenda item, just share some thoughts on BulletCT     

> __< emsczkp:matrix.org >__ BulletCT contributes to RingCT signature schemes with a “K-weight” version of K-out-of-N proofs (K/N proofs), inspired by the Any-out-of-N proofs (Any/N proofs), and proposes a new Tag proof.     

> __< emsczkp:matrix.org >__ BulletCT doesn’t bring improvements to Bulletproofs proof system itself; rather, it compares mainly against the Any/N RingCT scheme, the Omniring and RingCT-3.0.      

> __< emsczkp:matrix.org >__ Overall, BulletCT constructs a RingCT signature by combining four proofs, K/N proof, Tag proof, Balance proof and Range proof. The authors only provide the K/N proof and Tag proof. Moreover, both K/N proof and Tag proof follow the Bulletproofs-style proof for two different objectives: K/N proof proves the “existence of a val [... too long, see https://mrelay.p2pool.observer/e/qLCO-eAKUDhwYVY3 ]     

> __< emsczkp:matrix.org >__ However, it is unclear to me why the authors use separate Bulletproofs-style proofs for the K/N proof and the Tag proof. While the K/N proof appears to be motivated by Bulletproofs’ bit-decomposition constraints, an analogous motivation is not evident for the Tag proof. Finally, neither construction presents an explicit redu [... too long, see https://mrelay.p2pool.observer/e/qLCO-eAKUDhwYVY3 ]     

> __< emsczkp:matrix.org >__ this is my brief review     

> __< emsczkp:matrix.org >__ i don't agree Bulletct will benefit for Bulletproofs neither FCMP      

> __< emsczkp:matrix.org >__ i didn't read the other paper, but i will do     

> __< jberman >__ Thank you emsczkp:matrix.org !     

> __< emsczkp:matrix.org >__ welcome     

> __< sgp_ >__ Fwiw I don't think anyone claimed that bulletct as written would benefit Monero directly     

> __< jberman >__ emsczkp:matrix.org: Do you draw this conclusion because you think there isn't enough support for their idea? In other words, do you think they could take your feedback specifically from the second paragraph and iterate? Or that it's fundamentally flawed     

> __< emsczkp:matrix.org >__ here maybe > <rucknium> Has anyone here closely read any of the papers linked above? It looks like at least one of them (BulletCT) could help with Bulletproofs efficiency. Anyone know anything about it?     

> __< rucknium >__ So my hypothesis was wrong :D     

> __< emsczkp:matrix.org >__ jberman: i don't see the prover/verifer optimizations in BulletCT. I would like more details on that particular optimizations, or at least which papers do     

> __< emsczkp:matrix.org >__ here the authors claim there are "it seeks to halve the number of computationally expensive group exponentiations required by existing Bulletproofs-based constructions, yielding an almost 2X practical speedup" ... i haven't find this yet > <ack-j:matrix.org> MAGIC recieved a project proposal with the following research goals that we'd like community feedback on:     

> __< sgp_ >__ BulletCT is related work, but it's not "using BulletCT as a direct starting point, we changed this and this to create a Monero compatible proposal". Ack-j can chime in if my understanding is wrong     

> __< rucknium >__ Right. I was trying to get an idea of the researcher's research agenda .     

> __< sgp_ >__ They aren't saying BulletCT accomplishes the scope/claims     

> __< ack-j:matrix.org >__ Yea bulletCT is different. The papers that are more relevant are SwiftRange and flashproofs. I will get you a link     

> __< rucknium >__ To fund this, you would want to know if the objective of the research is feasible and if the researcher is likely to succeed in his/her goal.     

> __< ack-j:matrix.org >__ https://moneroresearch.info/index.php?action=list_LISTSOMERESOURCES_CORE&method=creatorProcess&id=692     

> __< ack-j:matrix.org >__ Here is the authors publications. 3 papers on range proofs and then bulletct is an outlier     

> __< rucknium >__ I suggested the wrong one. Sorry.     

> __< ack-j:matrix.org >__ Update on the MAGIC side. Dr. Nan Wang identified a soundness flaw in their proposed bulletproof+ optimization that affects the verifier efficiency. Their proposal still should double the prover efficiency and benefit verifier efficiency, but the 2x verifier estimate has been reduced.     

> __< ack-j:matrix.org >__ We plan to make a reddit post soon and start the fundraising round     

> __< jberman >__ fwiw, I don't recall exactly how long it takes to construct the BP+, but I at least haven't noticed it to be a perf issue when constructing a tx     

> __< jeffro256 >__ Especially after FCMP++ ...     

> __< jberman >__ right     

> __< rucknium >__ Verifier efficiency is usually much more important than prover efficiency, for blockchains.     

> __< jberman >__ FCMP++ construction is still pretty slow especially for large input txs, to the point it would actually be a noticeable thing for users     

> __< sgp_ >__ rucknium: This was emphasized to them by ack-j:matrix.org  fwiw     

> __< ack-j:matrix.org >__ https://mrelay.p2pool.observer/m/matrix.org/tGRPFJzPclIFBXyRgcohWeCS.pdf (Monero_Proposal 3.pdf)     

> __< ack-j:matrix.org >__ The author agreed to let us share the proposal. Here is the latest revision     

> __< rucknium >__ emsczkp:matrix.org: Any thoughts on the "Project Feasibility" section?     

> __< emsczkp:matrix.org >__ yea, now I see swiftrange promises BP rangeproof speed-up     

> __< emsczkp:matrix.org >__ I'm not in swiftrange, I'll take a look     

> __< jeffro256 >__ It says communication cost up to 2x as the "range size" increases. I'm guessing that that's the 64-bit amount, and not the number of outputs ?     

> __< emsczkp:matrix.org >__ of course, don't want to block the fundraising     

> __< rucknium >__ I think the risks are 1) Cannot be implemented in Monero for unforeseen reasons, 2) Becomes obsolete before a hark fork (after FCMP hark fork) occurs that could use it, 3) Speedup is very little, 4) Soundness does not pass peer review.     

> __< rucknium >__ Of course, all research is risky, so that's not new     

> __< emsczkp:matrix.org >__ jeffro256: it should be the bit-range domain yes     

> __< rucknium >__ Communication = size in bytes, right?     

> __< emsczkp:matrix.org >__ rucknium: usually the proof size = communication is bytes     

> __< rucknium >__ Everyone should feel free to give more feedback on the proposal after the meeting or any time.     

> __< rucknium >__ 7. CARROT Outgoing View Keys (OVKs) (https://github.com/jeffro256/carrot/blob/master/carrot.md#22-new-wallets-only).     

> __< rucknium >__ I have at least two questions. Is there any other known way to get quantum forward secrecy and/or prepare outputs for a post-quantum turnstile to prevent a quantum computer from counterfeiting XMR?     

> __< rucknium >__ Other than OVKs, I mean     

> __< DataHoarder >__ Current PQ Turnstile design for new Carrot wallet with Carrot tx outputs: https://gist.github.com/jeffro256/146bfd5306ea3a8a2a0ea4d660cd2243     

> __< jeffro256 >__ Yes, you can still come up with a wallet format scheme that sends change to a symmetric secret without having an OVK.     

> __< jeffro256 >__ And it should be possible to be made compatible with that turnstile design DataHoarder linked     

> __< jeffro256 >__ jeffro256: it would be akin to having two view-incoming keys: one for actual incoming XMR from others, which is the discrete log relation of your Monero address points, and one used for change.     

> __< DataHoarder[m] >__ Doesn't Carrot generate-image key + Carrot view incoming key effectively means OVK (you can scan inputs, you can generate key images to detect the spends) then, except for internal change?     

> __< jeffro256 >__ Plus s_ga (to determine address-specific openings), yes.     

> __< DataHoarder[m] >__ right, s_ga is derived from s_vb, not k_v     

> __< jeffro256 >__ s_ga meaning the "generate-address secret"     

> __< rucknium >__ jeffro256: The actual UX would be having two view keys? Or usually people would use a concatenated key, combining the two?     

> __< DataHoarder[m] >__ (current key hierarchy https://github.com/jeffro256/carrot/blob/master/carrot.md#52-new-key-hierarchy )     

> __< rucknium >__ Is midipoet still here?     

> __< jeffro256 >__ rucknium: For most use cases I envision, if you want the all-inclusive view-balance secret, you can just transmit that 32 byte secret, since it derives the others.     

> __< midipoet >__ Yes     

> __< articmine >__ rucknium: and how does this address the concerns that have been raised regarding OVKs?     

> __< rucknium >__ There is a fear that users would be persuaded to give up their outgoing view keys to centralized exchanges or other surveillance-adjacent entities. Anyone want to write out thoughts on this hypothesis?     

> __< jeffro256 >__ jeffro256: But you can split it up however you like for different use cases      

> __< jberman >__ My opinion: the tangible benefits the OVK brings are still not very well understood, undervalued, and under-appreciated, especially in how the OVK would improve security (and usability) for hot/cold wallets, multisig, and hw wallets.     

> __< jberman >__ The arguments in favor of SMALL businesses (and businesses of ALL sizes) have been nicely expanded on in various places.     

> __< rucknium >__ I have read of Monero users needing to submit cryptographic payment proofs. I don't know to whom or in what circumstances they are required. Anyone familiar with this behavior? I have not read of anyone needing to submit current incoming view keys.     

> __< jberman >__ On the nayside: the boogeyman argument of "they'll collect the keys and shut out people who don't provide them" is a hypothetical that rests on sheep being sheep and giving up their private keys.     

> __< jberman >__ So in sum: individuals and small businesses who want greater security using Monero, who want to build a circular unfuckwithable economy, are essentially being held back by hypothetical sheep being sheep.     

> __< midipoet >__ OVKs would be a method towards compliance for any obliged entity, that's for certain. Whether there is appetite for CEXs to implement a system that maintains a database of OVKs for their customers is unknown. Though perhaps they could delegate the analysis to surveillance companies, who would certainly benefit from having access to an OVK database (one would assume).     

> __< DataHoarder[m] >__ rucknium: You can accomplish most of the detailed items directly with view incoming keys, specially in legacy wallets, but FCMP++ also removes the ability to do any sort of output/decoy statistical analysis     

> __< DataHoarder[m] >__ (and on an aside, new Carrot wallet is not explicitly a change that is being hardforked, the tx output format change is the one being hardforked and this also benefits legacy wallets)     

> __< jeffro256 >__ midipoet: Practically: they would benefit IMMENSELY from having many people's view-incoming keys. With enough keys in a strongly connected subgroup of users, it's similar privacy-wise to having OVKs. Why do you think that this hasn't been done? There must be some political reason, no?     

> __< jeffro256 >__ midipoet: This is not to the fact that you can prove your entire tx history of a standard wallet with 100%, without OVKs. Yet there has been no push for this either.      

> __< rucknium >__ AFAIK, if the CCS wallet had disclosed an OVK, the community would have known about the theft immediately instead of a month+ afterward. I think the same thing could have been accomplished by regular export and public posting of key images, but that creates its own type of security risks.     

> __< articmine >__ midipoet: Yes 1 hop compliance is a use case. It is what can be used for travel rule compliance.     

> __< DataHoarder[m] >__ rucknium: When looking at the incident txs you could correlate that all inputs had been swept and directly attribute it due to the working of wallet change, but it'd have been entirely clear with OVK     

> __< articmine >__ This is a. far cry from the harm caused by BS     

> __< articmine >__ rucknium: This is a classic very good use case for OVK     

> __< jeffro256 >__ DataHoarder[m]: Especially since they used something akin to Monerujo Pocketchange and it was traceable for like 3 hops IIRC      

> __< hbs:matrix.org >__ jeffro256: Convenience differs though, in one case there is a need for continous export of KIs, in the other the one time hand out of the OVK is suddicient     

> __< midipoet >__ sure, but IVKs aren't negotiable are they? OVKs seem to be (as I understand it). The reason that CEXs haven't pushed for access to more view keys, is basically because it's been too complex to implement. It's easier to just delist. With more user friendly view keys this might (?!) change.      

> __< DataHoarder[m] >__ jeffro256: https://blocks.p2pool.observer/tx/ffc82e64dde43d3939354ca1445d41278aef0b80a7d16d7ca12ab9a88f5bc56a and the 0-XMR change shows it's a sweep of n inputs!     

> __< jberman >__ midipoet: "So in sum: individuals and small businesses who want greater security using Monero, who want to build a circular unfuckwithable economy, are essentially being held back by hypothetical sheep being sheep."     

> __< DataHoarder[m] >__ on this jeffro256:monero.social would a PQ Turnstile be possible without a general Carrot generate-image key for external incoming transactions? > <rucknium> I have at least two questions. Is there any other known way to get quantum forward secrecy and/or prepare outputs for a post-quantum turnstile to prevent a quantum computer from counterfeiting XMR?     

> __< articmine >__ midipoet: It can also strengthens legal cases against Monero delisting     

> __< jeffro256 >__ midipoet: What do you mean by "negotiable"? They aren't technically required for Monero to function, they simply make the UX suck way less. You can technically come up with a wallet format where the view key derives the spend key, no there exists no non-custodial IVKs     

> __< midipoet >__ articmine: yes, that might be true. But ultimately any CEX can list or delist whatever coin they want.      

> __< jeffro256 >__ jeffro256: Or you can simply set them equal to each other, but that would be externally observable in the main address      

> __< articmine >__ Any legal challenge would likely target the regulators and regulations      

> __< midipoet >__ jberman: I don't get the sheep being sheep bit, to be honest. Personally, I am not overly against OVKs, if there are legitimate purposes for them, aside from compliance. It seems (from what I have read) there are.      

> __< rucknium >__ jeffro256: jeffro256:monero.social: I wondered about that. But that's a wallet-level change (like carrot), not blockchain-level, right? So it would always be possible to create a new wallet with an IVK.     

> __< DataHoarder[m] >__ rucknium: it would always be possible to make a wallet with the scheme, or even a wallet that just reports proofs as needed     

> __< jberman >__ Someone who gives up their OVK is a sheep being a sheep. A business that requires OVK's is a sheep being a sheep     

> __< articmine >__ I am in favor of keeping the OVKs as proposed in Carrot at least as an option for wallet creation      

> __< DataHoarder[m] >__ the other suggestion was around UX. Don't display these in the GUI, but CLI only, or warn users about them.     

> __< gingeropolous >__ i wonder if they can have a default expiration     

> __< DataHoarder[m] >__ That said, exchanges could always ask for your seed words :)     

> __< jeffro256 >__ rucknium: CARROT is primarily an addressing protocol. I want to separate that conceptually from its recommended wallet format. So many different wallet formats can, and will, communicate XMR to each other over CARROT. But yes, CARROT has no consensus level rules, except for the new output format, which is simply reserve b [... too long, see https://mrelay.p2pool.observer/e/jYXp-uAKV1JpQmdS ]     

> __< DataHoarder[m] >__ gingeropolous: it's baked in address generation     

> __< midipoet >__ jberman: ah ok. i.e submitting control of the information is the problem, as opposed to whether it's a view key, a transaction id, a private key, etc.      

> __< jeffro256 >__ > <DataHoarder[m]> it would always be possible to make a wallet with the scheme, or even a wallet that just reports proofs as needed     

> __< jeffro256 >__ Exactly. If user convenience is the limiting factor for regulators, regulators could require you to use an auto-reporting wallet software TODAY, which is cryptographically verifiable if you try to evade that software, for that specific wallet, once you have disclosed the view-incoming key.      

> __< articmine >__ gingeropolous: Sweep the wallet and claim the spend key was compromised . There are workarounds with very reasonable plausibility     

> __< DataHoarder[m] >__ ☝ > <jeffro256> Exactly. If user convenience is the limiting factor for regulators, regulators could require you to use an auto-reporting wallet software TODAY, which is cryptographically verifiable if you try to evade that software, for that specific wallet, once you have disclosed the view-incoming key.      

> __< midipoet >__ Having said all that, there is a level of technological determinism to the whole thing. If we make view keys really easy to use, the use of them might become normalised. That would be detrimental to the way we imagine Monero being used as a currency. The fact view keys/key image sharing hasn't become normalised is probably very strongly correlated to the current technical/usability barriers to the sharing/generating      

> __< midipoet >__ process.      

> __< DataHoarder[m] >__ Users use view keys already when they make a view-only wallet in GUI, or use a hardware wallet     

> __< DataHoarder[m] >__ (or multisig, but that is an advanced feature)     

> __< jeffro256 >__ gingeropolous: It's completely possible to export OVKs per-address. But in the boogeyman scenario, why would the boogeyman ask for the inferior per-address OVKs instead of the main one?     

> __< DataHoarder[m] >__ OVK in the case of these massively simplifies interacting with hardware wallets or making multisig txs. You also no longer need to bring the cold keys from storage or connect the hw wallet to check balances, as hw wallet setups atm can't export key images.     

> __< DataHoarder[m] >__ So you can't share these with a secondary wallet in a different computer.     

> __< jberman >__ midipoet: Collecting  JUST view keys of today is effectively 99% as useful as OVK's, since they can see change and therefore see the vast majority of outgoing transactions as well (the spends are extremely straightforward to pinpoint)     

> __< jberman >__ ESPECIALLY to a surveillance panopticon     

> __< DataHoarder[m] >__ jberman: Yeah. Today it would be quite harmful due to the ability to tag an output and trace it statistically in decoys. Akin to how https://p2pool.observer/sweeps works     

> __< jberman >__ "The fact view keys/key image sharing hasn't become normalised is probably very strongly correlated to the current technical/usability barriers to the sharing/generating process" -> there is no reason to think this     

> __< DataHoarder[m] >__ FCMP++ entirely removes the ability to do this, so a lot of the specific knowledge and behavior around view keys also changes     

> __< jberman >__ no evidence to support that claim     

> __< articmine >__ How practical is this at scale? > <jberman> Collecting  JUST view keys of today is effectively 99% as useful as OVK's, since they can see change and therefore see the vast majority of outgoing transactions as well (the spends are extremely straightforward to pinpoint)     

> __< just_another_day:matrix.org >__ One of the reasons can be to conceal their intentions until OVKs are adopted > <jeffro256> Practically: they would benefit IMMENSELY from having many people's view-incoming keys. With enough keys in a strongly connected subgroup of users, it's similar privacy-wise to having OVKs. Why do you think that this hasn't been done? There must be some political reason, no?     

> __< jberman >__ just_another_day:matrix.org: One can spin up boogeymen endlessly     

> __< jeffro256 >__ > <jberman> Collecting  JUST view keys of today is effectively 99% as useful as OVK's, since they can see change and therefore see the vast majority of outgoing transactions as well (the spends are extremely straightforward to pinpoint)     

> __< jeffro256 >__ Funnily enough, I have a link to a presentation video which covers this exact topic. I think you would be interested in it: https://www.youtube.com/watch?v=MYzZ1DzSWCY     

> __< midipoet >__ Sure. spinning up boogyman is basically what threat assesment is. Monero users love doing it.      

> __< midipoet >__ Doesn't invalidate it     

> __< intr:unredacted.org >__ the problem is that most of these boogeymen involve voluntary user actions, in the same vein you may be "compelled" to give up your private spend key     

> __< jberman >__ intr:unredacted.org: So in sum: individuals and small businesses who want greater security using Monero, who want to build a circular unfuckwithable economy, are essentially being held back by hypothetical sheep being sheep.     

> __< articmine >__ jberman: This is only part of the problem     

> __< midipoet >__ How do OVKs provide greater security for an individual that uses Monero. Like what is the use case there?     

> __< DataHoarder[m] >__ midipoet: There is no longer need to bring any spend key online until it's time to spend, even in-memory.     

> __< DataHoarder[m] >__ You could now implement a wallet that has a different extra password to spend/show seed words     

> __< jberman >__ midipoet: 1. Hot/cold wallet users frequently check their balance. That occurs in the real world, they're going to do it. Not needing to load the spend key to do so is reducing attack surface for said users.     

> __< articmine >__ midipoet: Auditing and monitoring without using the spend key     

> __< gingeropolous >__ light wallets work better too right     

> __< gingeropolous >__ try as I might i've never gotten my mobile monero wallet to be useful. its always out of sync     

> __< articmine >__ Hardware wallets for example are just a special case of auditing and monitoring      

> __< midipoet >__ So then most of here agree that the benefits outweigh the costs, and the potential (boogeyman) risks. What is the problem then?     

> __< midipoet >__ *most here     

> __< jberman >__ 2. Multisig users. Same for them. To see their balance requires communicating with other multisig users who all have to load their spend keys to generate key images. Eliminating that requirement is a +1 for multisig security and a MJAJOR +10 for multisig usability, which has been a MAJOR pain implementing for Monero     

> __< jeffro256 >__ midipoet: Software wallets: spend key can stay decrypted during sync. Hot/cold wallets: improved UX and security b/c cold wallet does not need to be consulted unless to sign transactions. Multisig: improved UX and security b/c participants do not have to consult with each other to calculate key images during refresh. Hardware  [... too long, see https://mrelay.p2pool.observer/e/hpac--AKYWlpV0o0 ]     

> __< DataHoarder[m] >__ jeffro256: *spend key can stay encrypted during sync.     

> __< jberman >__ Another overlooked benefit for hw wallets is how much simpler it is to design a hw wallet that does not have to ingest outputs and generate key images and export them back to the software wallet     

> __< rucknium >__ midipoet: midipoet: Informed consent. The information known here needs to be communicated better to the whole Monero user community.     

> __< midipoet >__ rucknium: seems fair.      

> __< jberman >__ Has anyone noticed the plethora of failed hw wallet projects in Monero? How long have we been waiting for a seed-signer like device? Does anyone recall why Passport didn't end up supporting Monero?     

> __< DataHoarder[m] >__ On this part FCMP++ allows signing and then the wallet can be the one filling the membership proofs right? which also eases hw wallet construction     

> __< jberman >__ Simplifying hw wallet design will make it easier for various people to design hw wallets for Monero, again improving security for Monero users     

> __< hbs:matrix.org >__ jberman: On a side note, with Ledger filing for its IPO in the US soon there is a non zero probability that Monero support be dropped in the future     

> __< gingeropolous >__ rucknium: perhaps we need a good long blog post on getmonero.org      

> __< gingeropolous >__ you can't trust me to write it tho cause im hooked on llms     

> __< rbrunner >__ Is it so ...     

> __< DataHoarder[m] >__ gingeropolous: The previous blogpost on the topic was https://www.getmonero.org/2024/04/27/fcmps.html (which mentions OVK) so this can be further expanded to Carrot tx output format and Carrot wallet     

> __< midipoet >__ gingeropolous: do you have an llm-based partner as well?     

> __< rbrunner >__ Yeah, sometimes I like to write such posts, but right now I would rather wait for the storm to subside before even thinking about it     

> __< midipoet >__ You could have a panel on risks v benefits at Monerotopia/MoneroKon     

> __< rbrunner >__ I see the discussions on Reddit over almost a week now as a more or less lost case     

> __< rucknium >__ Why not jeffro256:monero.social  write it, then check for ease of understanding by someone else?     

> __< jeffro256 >__ jberman: Hardware / cold wallets' implementation requirements right now are basically an entire wallet engine, including burning bug mitigations, enote scanning, key image communication, BP+ proving (range proofs are included in signature hash), CLSAG proving, etc. After FCMP++/Carrot/new wallet format, it changes to just [... too long, see https://mrelay.p2pool.observer/e/m_Gz--AKTXMzY192 ]     

> __< jeffro256 >__ Plus exporting the other keys.     

> __< jeffro256 >__ rucknium: I was planning on doing this for Monerotopia in just over 2 weeks ;)     

> __< rbrunner >__ I volunteer to review and comment anything in this direction, if that's of any use     

> __< rbrunner >__ If it has the form of a presentation, I mean     

> __< jberman >__ happy to review/comment as well!     

> __< DataHoarder[m] >__ I don't know if this message got lost in the discussion or was answered before (AFAIK we only answered what to do with internal change, not external incoming outputs) > <DataHoarder[m]> on this jeffro256:monero.social would a PQ Turnstile be possible without a general Carrot generate-image key for external incoming transactions?     

> __< jeffro256 >__ Good question. It may be possible, but not with the current design AFAICT > <DataHoarder[m]> on this jeffro256:monero.social would a PQ Turnstile be possible without a general Carrot generate-image key for external incoming transactions?     

> __< midipoet >__ oh, I see. A lot has been said on Reddit. Missed all of that.      

> __< rbrunner >__ About 1000 comments now in total, probably? Some people have been very busy, and very persistent.     

> __< midipoet >__ Yeah. At least it's people getting enthused though.      

> __< rbrunner >__ Yes, lol. I look at a certain other coin subreddit and see 2, 3 messages per day. Well :)     

> __< DataHoarder[m] >__ +Twitter, and it woke up several people to come to reddit to start disproving lies in comments or misunderstandings     

> __< intr:unredacted.org >__ including fluffypony     

> __< DataHoarder[m] >__ jeffro256: Might be curious how one would look as due diligence (with a wallet hierarchy to match) to see what such change it'd allow if each of the keys was shared except main spend keys (or whatever allows producing txs)     

> __< DataHoarder[m] >__ Changes in address format (cryptonote addresses) would allow much more IIRC but that's not in scope (JAMTIS is doing that)     

> __< rucknium >__ We have spent an hour on this agenda item, so I will end the meeting here. Thanks everyone.     

> __< articmine >__ Thanks      

> __< jeffro256 >__ Agreed. I'll into into it. I suspect an issue will be that if you make your opening over T depend on the opening over G, revealing the key image opening (to prove PQ soundness), will necessarily reveal your entire signing key, so authorization will be broken.     

> __< jeffro256 >__ Thanks everyone!     

> __< rbrunner >__ Hmm, the ease of support in hardware wallets for Carrot wallets may mean that if somebody wants to continue with a legacy wallet, hardware wallet support may not be there anymore?     

> __< DataHoarder[m] >__ rbrunner: Some of the FCMP++ benefits also map over to legacy ones, regarding tx construction     

> __< DataHoarder[m] >__ online spend keys would still be needed for decoding spends     

> __< rbrunner >__ Yes, I see, but our offer to people that we continue legacy wallets indefinitely, with 2 secret keys, would have a small "but": No hardware, only software. No drama though IMHO     

> __< DataHoarder[m] >__ jeffro256: Yeah, I think this was also partially discussed when someone suggested making two keys/secrets the same instead of being derived differently, that it broke certain aspects against a quantum capable adversary, but I do not remember the specifics     

> __< DataHoarder[m] >__ rbrunner: As in, the hardware does the same work as in new carrot wallet, besides different derivation and can only provide view incoming key. The signing still happens the same way on both with spend keys, then wallet software can fill the rest.     

> __< DataHoarder[m] >__ And ofc, you need to actively query the hw wallet (with the spend key) for legacy wallets to check spend status.     

> __< rbrunner >__ DataHoarder: Thanks. That's sounds better than I feared. It's not that much much for firmware writers to continue to support both, if I understand you correctly     

> __< rbrunner >__ *much work     

> __< rbrunner >__ Thanks to some "magic" that FCMP++ itself is providing     

> __< sgp_ >__ I don't think that any of the arguments against view keys is grounded in sound argument, personally     

> __< sgp_ >__ anyone at gunpoint can ask for your private spend key, if we're talking highly theoretical risks for the worst case     

> __< sgp_ >__ maybe this would be a concern if you had to pay for a new Monero wallet, or get one made by an regulated entity for you. But you don't. Wallets are free and permissionless     

> __< venture >__ "at gunpoint" quite hyperbole :) shotgun-kyc is a thing already, and I think it is sound to be concerned about shotgun-OVK.      

> __< venture >__ current viewkeys were to my knowledge quite useless with KIs. and KIs was not something that could reasonably be asked for given that most (mobile) wallets don't export them.     

> __< venture >__ highly theoretical/ hypothetical "sheep being sheep" is also a bit hand wavy to me. Sheep being sheep is a tautology. and regulations are shaped by the majority.      

> __< venture >__ ^^ not arguing here, I'm quite indifferent to it.      

> __< venture >__ *useless *without KIs.      

> __< sgp_ >__ the core issue with "shotgun kyc" is counterparty risk, not compliance     

> __< sgp_ >__ someone else who has your money can have it stolen, etc     

> __< jberman >__ venture: fine, hypothetical sheep following regulations for sheep     

> __< jberman >__ you are free to be scared of the behavior of hypothetical sheep. Such fear shouldn't inhibit security for people who don't care what sheep do     

> __< jberman >__ "current viewkeys were to my knowledge quite useless with KIs" -> this is incorrect. current view keys are 99% as useful as OVK's and can see outgoing transactions (because most outgoing transactions include change which the current view key can see)     

> __< intr:unredacted.org >__ it's been circular reasoning for a week straight now     

> __< venture >__ jberman: if I create 2 receiving enotes, a change note would not be created at all, no?     

> __< DataHoarder >__ the two receiving enotes would need to fully send the balance     

> __< sgp_ >__ the more common "exempt" case would be for a sweep_all     

> __< DataHoarder >__ in CURRENT network you could correlate decoys used with view key abilities     

> __< jberman >__ when you create a normal tx in Cake Wallet today (e.g. I send ".4 Monero"), the incoming view key will detect that tx     

> __< jberman >__ the current view key*     

> __< brandon:cypherstack.com >__ IACR thinks this is not sufficiently new and interesting, so we put it up on a github: https://github.com/cypherstack/generalized-bulletproofs-fix     

> __< hbs:matrix.org >__ > <jberman> you are free to be scared of the behavior of hypothetical sheep. Such fear shouldn't inhibit security for people who don't care what sheep do     

> __< hbs:matrix.org >__ Calling sheeps ppl who will simply comply with regulations which may be put in place because the technology has evolved to allow them may be a little manichaen, there may be more categories than just sheeps and security conscious individuals and businesses.     

> __< 321bob321 >__ If you give them the option they will take it. If the option isnt there they cant force anything.     

> __< jberman >__ I disagree. People who e.g. use custodial wallets because regulations would require it are de facto sheep. Same principle here     

> __< intr:unredacted.org >__ the option is already there     

> __< DataHoarder >__ the option to give seed words is always there     

> __< hbs:matrix.org >__ DataHoarder: goes against private property laws in most jurisdictions     

> __< intr:unredacted.org >__ private keys?     

> __< sgp_ >__ I don't love the "sheep" comparison. But the concern isn't about view keys at all. It's about trying to force what other people do. You can't force other people to not share their wallet info, and to not use a custodial wallet for that matter. Removing view keys doesn't prevent bad behavior, and it probably doesn't even discourage it since custodial wallets often win on convenience already anyway     

> __< DataHoarder >__ remember they can make the option be there anytime, too     

> __< DataHoarder[m] >__ ^ > <DataHoarder[m]> it would always be possible to make a wallet with the scheme, or even a wallet that just reports proofs as needed     

> __< DataHoarder[m] >__ also this one ^ > <jeffro256> Exactly. If user convenience is the limiting factor for regulators, regulators could require you to use an auto-reporting wallet software TODAY, which is cryptographically verifiable if you try to evade that software, for that specific wallet, once you have disclosed the view-incoming key.      

> __< sgp_ >__ On a more fun and productive note, zkSecurity just confirmed their quote for divisors remains $50,000. So I would like to add approval for that to the agenda for next week     

> __< sgp_ >__ cc rucknium:monero.social jberman:monero.social     

> __< basses:matrix.org >__ 321bob321: Dan, meant like with "true" no log VPN providers, they can't provide info that they don't log https://mullvad.net/en/blog/2023/4/20/mullvad-vpn-was-subject-to-a-search-warrant-customer-data-not-compromised     

> __< basses:matrix.org >__ DataHoarder: isn't that treated like similar to passwords/encryption keys?     

> __< intr:unredacted.org >__ full view keys are also private keys     

> __< basses:matrix.org >__ there are laws to protect you from that     

> __< intr:unredacted.org >__ (afaik)     

> __< basses:matrix.org >__ Recently, news broke out that M$ was giving FBI bitlocker encryption keys as they had an option when setting a Microsoft account to backup that key on their server for "recovery" purposes that is already checked.     

> __< basses:matrix.org >__ This account setup is forced on windows 11     

> __< intr:unredacted.org >__ lesson learned: don't use a monero wallet developed by microsoft     

> __< just_another_day:matrix.org >__ Is your position that the discussed risks aren't credible, that they are credible but irrelevant, or both? > <jberman> you are free to be scared of the behavior of hypothetical sheep. Such fear shouldn't inhibit security for people who don't care what sheep do     

> __< just_another_day:matrix.org >__ As MRL agreed to move forward with OVKs, it'd be interesting to make a prediction on whether the discussed risks will materalize.     

> __< jberman >__ My position is that the risk that hypothetical sheep give up their private keys (and hypothetical sheep businesses require them), does not outweigh the benefits of increased security for Monero users     

> __< jberman >__ The benefits are tangible, known, and more significant than the naysayers claim. The hypothetical boogeyman argument rests on sheep     

> __< DataHoarder[m] >__ just_another_day:matrix.org: Also agreed to make experiments to see how PQ would look without it     

> __< venture >__ isn't the PQ threat realistically valid by the very same boogeyman only? ;)     

> __< jberman >__ No     

> __< DataHoarder[m] >__ It can be used in a store and decode later manner     

> __< DataHoarder[m] >__ Or ofc, inability to migrate to a safe system     

> __< intr:unredacted.org >__ I meant to ask, jberman:monero.social, you mentioned fcmp++ transaction building takes a long time. How long roughly?     

> __< jberman >__ IIRC a few secouds per input, with optimizations still on the table (e.g. with parallelization and crypto optimizations)     

> __< intr:unredacted.org >__ Damn, I see. Thank you     



# Action History
- Created by: Rucknium | 2026-01-27T23:14:13+00:00
- Closed at: 2026-02-11T01:48:27+00:00
