---
title: Monero Research Lab Meeting - Wed 21 January 2026, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/1330
author: Rucknium
assignees: []
labels: []
created_at: '2026-01-20T23:10:22+00:00'
updated_at: '2026-01-31T21:21:26+00:00'
type: issue
status: closed
closed_at: '2026-01-31T21:21:26+00:00'
---

# Original Description

Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/meeting.html?p1=1440)

Main discussion topics:

1. Greetings

2. Updates. What is everyone working on?

3. [RandomX Version 2](https://github.com/SChernykh/RandomX/blob/v2/doc/design_v2.md).

4. [FCMP and CARROT reviews and audits status](https://cryptpad.fr/sheet/#/2/sheet/view/yPVIUywwA9-deE9VF6GYm9bXbPdCerdST3UDEEfBxcM/embed/).

5. [FCMP alpha stressnet](https://monero.town/post/6763165).

6. Bulletproof prover and verifier optimization research.

7. Any other business

Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: Rucknium

Previous meeting agenda/logs:

#1324 

# Discussion History
## plowsof | 2026-01-24T13:27:53+00:00
Logs 
    
    
    
    
    
    
    
    
    
> **\<rucknium\>** <rucknium> Meeting time! https://github.com/monero-project/meta/issues/1330     
    
> **\<rucknium\>** <rucknium> 1. Greetings     
    
> **\<ack-j:matrix.org\>** <ack-j:matrix.org> Hi     
    
> **\<DataHoarder\>** hello world     
    
> **\<boog900\>** <boog900> Hi     
    
> **\<sech1\>** Hello     
    
> **\<jeffro256\>** <jeffro256> Howdy     
    
> **\<sgp_\>** <sgp_> Hello     
    
> **\<w0venhand:matrix.org\>** <w0venhand:matrix.org> Hi     
    
> **\<jberman\>** <jberman> waves     
    
> **\<vtnerd\>** <vtnerd> Hi     
    
> **\<articmine\>** <articmine> Hi     
    
> **\<rucknium\>** <rucknium> 2. Updates. What is everyone working on?     
    
> **\<DataHoarder\>** Have been doing RandomX benchmarks for V2 and looking into low-level CPU performance counters on current generations, specifically now investigatin how increasing prefetch distance across RandomX vm loops reduces the waits and increase instruction throughput.     
    
> **\<rucknium\>** <rucknium> me: Back on using Markov Decision Process to analyze selfish mining countermeasures.     
    
> **\<DataHoarder\>** (note there seems to be a 2-5s delay on IRC bridging since last night outage, I'll investigate later)     
    
> **\<sech1\>** I finished RandomX v2 in its current state (including the documentation) and have been testing it     
    
> **\<jeffro256\>** <jeffro256> Me: reviewing ArticMine's scaling updates and digging into OSSFuzz issues      
    
> **\<vtnerd\>** <vtnerd> Me: working on lwsf/monero_c builds for windows and macos. No decent progress on that asan issue unfortunately      
    
> **\<articmine\>** <articmine> I updated the scaling documents to address changes with respect to the calculation for the maximum fee and also a series of fixes     
    
> **\<jberman\>** <jberman> me: followed up on @jeffro256 's unbiased hash to point impl (a blocker for beta stressnet) and did a bit of refactoring of my own code for that impl and for the FCMP++/Carrot integration. Unrelated to the unbiased hash to point, I have some more refactoring ideas to implement in line with my changes there before opening up th [... too long, see https://mrelay.p2pool.observer/e/78aQ2N4KX01nQzFa ]     
    
> **\<rucknium\>** <rucknium> The Monerotopia Conference is happening February 12 to 15 in Mexico City: https://monerotopia.com/ . Some MRL regulars and semi-regulars like  @jeffro256:monero.social , @articmine:monero.social , @freeman:cypherstack.com ,  @diego:cypherstack.com , and myself will be presenting.     
    
> **\<articmine\>** <articmine> Yes I will be speaking at MoneroTopia and also afterwards at the Crypto Vigilante     
    
> **\<rucknium\>** <rucknium> 3. RandomX Version 2 (https://github.com/SChernykh/RandomX/blob/v2/doc/design_v2.md).     
    
> **\<rucknium\>** <rucknium> sech1, could you describe the purpose of the RandomX update, what tasks remain, any way others can assist, and maybe an expected timeline for completion?     
    
> **\<sech1\>** The purpose is to fix the bottlenecks in RandomX on modern CPUs. The main things we found are CFROUND instruction and memory access, so this is what we changed in v2     
    
> **\<sech1\>** I think the only task that remains is PowerPC big-endian intrinsics (two small functions). Need a ppc64be systems to test it     
    
> **\<jeffro256\>** <jeffro256> Can you explain a bit further what about the "memory access" was a bottleneck?     
    
> **\<articmine\>** <articmine> Is this going to be ready for the upcoming hard fork?     
    
> **\<sech1\>** The CPU is waiting for data from the memory (dataset) instead of executing instructions, so it wastes energy     
    
> **\<sech1\>** There's a smaller bottleneck with L3 cache access where CPU waited too, but we filled it with AES tweak     
    
> **\<sech1\>** acricmine it's already 99% ready, just needs ppc64be test     
    
> **\<DataHoarder\>** we are doing live benchmarks with it, PR/code is ready as well     
    
> **\<DataHoarder\>** I have been doing similar tests in my go-randomx project (where it's also already implemented)     
    
> **\<rucknium\>** <rucknium> Any expected effect on the Bitmain X9?     
    
> **\<DataHoarder[m]\>** quoting from elsewhere as well:     
    
> **\<sech1\>** 18:22:02 <sech1> If they have RISC-V CPU with hardware AES instructions, it should drop from 1 MH/s to ~650 KH/s on v2     
    
> **\<sech1\>** 18:22:32 <sech1> If they have the CPU without hardware AES instructions, but with an AES crypto accelerator to generate the scratchpad, they're screwed[... more lines follow, see https://mrelay.p2pool.observer/e/2oG72N4KRUtVQm9U ]     
    
> **\<sech1\>** It depends on how X9 implemented AES support. If it's a separate circuit not in the CPU, X9 will be effectively bricked     
    
> **\<sech1\>** Yes, that above ^     
    
> **\<sech1\>** Worst case (for us) it will drop hashrate from 1 MH/s to 650 KH/s     
    
> **\<rucknium\>** <rucknium> I assume you don't know anyone with an actual X9 unit yet.     
    
> **\<sech1\>** It's on preorder now, delivery in July     
    
> **\<sech1\>** So no one but Bitmain has it     
    
> **\<DataHoarder\>** They also would need to bother and update the firmware which they didn't even for minor changes on other coins they supported     
    
> **\<articmine\>** <articmine> Why do I see deja vu here eight years later?     
    
> **\<syntheticbird\>** <syntheticbird> and be sure you'll see it again in eight years     
    
> **\<rucknium\>** <rucknium> sech1: Before you have said that miners would need a 6 month period of time between released of the "final" monerod for the hard fork and activation of the hard fork with RandomX V2. Is that timeline still accurate?     
    
> **\<sech1\>** 6 months after XMRig release, not monerod     
    
> **\<sech1\>** If v2 is finalized and released soon, miners will start updating     
    
> **\<rucknium\>** <rucknium> That makes it easier if it's not a monerod requirement.     
    
> **\<DataHoarder\>** ^ even if no hardfork is set for monero at that point, just xmrig finalized support     
    
> **\<sech1\>** We plan to finalize v2 in January, make a pull request, then I can start updating XMRig and it will be also released in February     
    
> **\<DataHoarder\>** I guess it'd be rx/0 to rx/1 or whatever version shift     
    
> **\<sech1\>** So miners will be (for the most part) hardfork-ready in August     
    
> **\<sech1\>** no, rx/v2 :)     
    
> **\<sech1\>** I don't want to have confusion with number again as it happened with Cryptonight     
    
> **\<rucknium\>** <rucknium> Would Version 2 need any kind of external audit like Version 1 did, or are the changes small enough not to need it?     
    
> **\<sech1\>** Changes are small and evolutionary     
    
> **\<rucknium\>** <rucknium> Seems like everything is going smoothly :)     
    
> **\<DataHoarder\>** note a v2 hardfork also would include commitments, for anyone tracking that work     
    
> **\<DataHoarder\>** commitments already exist in randomx codebase merged     
    
> **\<rucknium\>** <rucknium> commitments of?     
    
> **\<sech1\>** https://github.com/monero-project/monero/issues/8827     
    
> **\<sech1\>** Those commitments ^     
    
> **\<jeffro256\>** <jeffro256> Commitments to PoW verifiable by Blake2b     
    
> **\<rucknium\>** <rucknium> Good to hear.     
    
> **\<jeffro256\>** <jeffro256> It's DoS-resistant pre-verification for our RandomX PoW     
    
> **\<jeffro256\>** <jeffro256> Integration PR is here: https://github.com/monero-project/monero/pull/10038     
    
> **\<rucknium\>** <rucknium> Anything else on RandomX Version 2?     
    
> **\<rucknium\>** <rucknium> Thanks so much, sech1 and DataHoarder, for working on it!     
    
> **\<rucknium\>** <rucknium> 4. FCMP and CARROT reviews and audits status (https://cryptpad.fr/sheet/#/2/sheet/view/yPVIUywwA9-deE9VF6GYm9bXbPdCerdST3UDEEfBxcM/embed/).     
    
> **\<rucknium\>** <rucknium> I kept this agenda item to follow up on the followups from last meeting.     
    
> **\<sgp_\>** <sgp_> Divisors is waiting on me. I'll reach out and CC jberman     
    
> **\<jberman\>** <jberman> Veridise confirmed to sgp their helioselene review/audit is progressing     
    
> **\<rucknium\>** <rucknium> @sgp_:monero.social: You mean soliciting firms for a third review of divisors?     
    
> **\<sgp_\>** <sgp_> Specifically zkSec, yeah. We already got a quote but that was months ago before the CS work on it wrapped up. So we need to update it and accept it     
    
> **\<rucknium\>** <rucknium> Thanks.     
    
> **\<jberman\>** <jberman> CS submitted their latest round of work on GBP, it's currently on us to review that work. That review will take some time to complete     
    
> **\<rucknium\>** <rucknium> @jberman:monero.social: Building on this? https://github.com/cypherstack/divisor_deep_dive     
    
> **\<sgp_\>** <sgp_> @jberman: Then after that review, back to zkSec for a second opinion. We got a quote for that already as well     
    
> **\<rucknium\>** <rucknium> Is there a reason it's not been posted publicly?     
    
> **\<sgp_\>** <sgp_> The CS GBP stuff?     
    
> **\<rucknium\>** <rucknium> Yes     
    
> **\<jberman\>** <jberman> @rucknium: Building on this: https://repo.getmonero.org/-/project/54/uploads/b2d5c8198f55d72b588f1ef138126850/GBP_Security_Review.pdf     
    
> **\<rucknium\>** <rucknium> Ok. Also posted here: https://moneroresearch.info/243     
    
> **\<sgp_\>** <sgp_> I believe the intent was to publish after kayaba did their review of it, but I'm double checking     
    
> **\<sgp_\>** <sgp_> To make sure the suggested changes were feasible in practice (in the implementation)     
    
> **\<rucknium\>** <rucknium> They suggested changes in their latest review? Would that affect timeline at all?     
    
> **\<sgp_\>** <sgp_> There definitely has been a delay because of it (CS found issues with GBPs as originally written). Assuming the suggested fix is feasible (which kayaba sadly can't confirm asap since they're heads down for a Serai audit for another month), then the further delays should be minimal. If it's infeasible, then that'll be another delay     
    
> **\<sgp_\>** <sgp_> If CS is suggesting these fixes, there is a good chance that they will work as intended given their Monero experience     
    
> **\<rucknium\>** <rucknium> Isn't there a transparency reason to post it?     
    
> **\<rucknium\>** <rucknium> If it will take kayabaNerve a while to review it, then it could be best to let others see it now.     
    
> **\<sgp_\>** <sgp_> Fwiw I haven't seen it either, I'm just aware of the context around the delays. I wouldn't be opposed to posting it in draft form here     
    
> **\<jberman\>** <jberman> Same position here^     
    
> **\<rucknium\>** <rucknium> Would be great if you could make that happen :)     
    
> **\<sgp_\>** <sgp_> Ok, I asked kayaba. If I don't hear back (unlikely) I'll ask CS     
    
> **\<rucknium\>** <rucknium> Thanks.     
    
> **\<rucknium\>** <rucknium> Anything else on this agenda item?     
    
> **\<rucknium\>** <rucknium> 5. FCMP alpha stressnet (https://monero.town/post/6763165).     
    
> **\<jberman\>** <jberman> My position is more or less the same as last week. From my perspective, we're looking good for beta since v1.5 solved the core reliability issues. Perhaps ofrnxmr has an opinion on v1.5's current status as well     
    
> **\<jeffro256\>** <jeffro256> Gotta fix the core tests in https://github.com/seraphis-migration/monero/pull/282 and update to match https://github.com/seraphis-migration/monero/issues/44#issuecomment-3776204112     
    
> **\<jeffro256\>** <jeffro256> After that, scaling changes will be ready for review      
    
> **\<rucknium\>** <rucknium> Would the suggested changes to Generalized Bulletproofs affect performance enough that it would be a good idea to include the changes in beta stressnet? Probably the answer to this question is unknown, without the Cypher Stack document and/or kayaba's review.     
    
> **\<jberman\>** <jberman> A significant perf impact would definitely surprise me, but ya it's an unknown as of now     
    
> **\<jberman\>** <jberman> I do think it would be a good idea to have that task item settled before releasing beta     
    
> **\<jberman\>** <jberman> We have outstanding tasks we're in the finishing stages for beta now (jeffro is working on scaling, I'm continuing on unbiased hash to point / some refactorings as needed, tx relay v2 is in review). It's all finishing stages though     
    
> **\<diego:cypherstack.com\>** <diego:cypherstack.com> Hey. Guys.      
    
> **\<diego:cypherstack.com\>** <diego:cypherstack.com> I want FCMPs out Q2 2026     
    
> **\<diego:cypherstack.com\>** <diego:cypherstack.com> I'll get everyone a $10 gift card to cold stone or an equivalent ice cream shop.      
    
> **\<diego:cypherstack.com\>** <diego:cypherstack.com> Plz and thx     
    
> **\<rucknium\>** <rucknium> @diego:cypherstack.com: There was a desire to publicly post Cypher Stack's latest Generalized Bulletproofs work.     
    
> **\<rucknium\>** <rucknium> Is that possible to do soon?     
    
> **\<diego:cypherstack.com\>** <diego:cypherstack.com> Lemme ask.      
    
> **\<rucknium\>** <rucknium> Thank you.     
    
> **\<rucknium\>** <rucknium> Anything else about stressnet?     
    
> **\<jberman\>** <jberman> nothing from me     
    
> **\<jeffro256\>** <jeffro256> nothing from me      
    
> **\<rucknium\>** <rucknium> 6. Bulletproof prover and verifier optimization research.     
    
> **\<rucknium\>** <rucknium> More Bulletproofs!     
    
> **\<rucknium\>** <rucknium> @ack-j:matrix.org:     
    
> **\<ack-j:matrix.org\>** <ack-j:matrix.org> MAGIC recieved a project proposal with the following research goals that we'd like community feedback on:     
    
> **\<ack-j:matrix.org\>** <ack-j:matrix.org> This project aims to deliver significant 2X speedup for both prover and verifier efficiency for Bulletproofs-style range proofs, while preserving their compact communication complexity of 2 log N. More precisely, it seeks to halve the number of computationally expensive group exponentiations required by existing Bulletproofs-b [... too long, see https://mrelay.p2pool.observer/e/n9aL2t4KbThCbm1x ]     
    
> **\<ack-j:matrix.org\>** <ack-j:matrix.org> The lead researcher, Dr Nan Wang, is well published in topics such as range proofs and ring signatures.[... more lines follow, see https://mrelay.p2pool.observer/e/n9aL2t4KbThCbm1x ]     
    
> **\<rucknium\>** <rucknium> Has anyone here closely read any of the papers linked above? It looks like at least one of them (BulletCT) could help with Bulletproofs efficiency. Anyone know anything about it?     
    
> **\<jberman\>** <jberman> I have not, but on the surface, seems like a great proposal     
    
> **\<rucknium\>** <rucknium> The proposed protocol would not be quantum resistant, or would it?     
    
> **\<jberman\>** <jberman> I would assume not     
    
> **\<cyrix126:gupax.io\>** <cyrix126:gupax.io> @rucknium: not with Ed25519     
    
> **\<jeffro256\>** <jeffro256> If the work to speeding up bulletproofs is applicable to either FCMP++'s GBPs and/or Bulletproof+ range proofs, then I am in support of it, especially at that price.     
    
> **\<cyrix126:gupax.io\>** <cyrix126:gupax.io> sry if it's a dumb question but would the proposal be compatible with https://ccs.getmonero.org/proposals/emsczkp-research-folding-gbp.html ?     
    
> **\<rucknium\>** <rucknium> The new protocol would require a hard fork probably, right?     
    
> **\<jeffro256\>** <jeffro256> Practically, I think that it's probably too late in the game to make it into the FCMP++ hard fork, but assuming that research and development go well for BulletCT, it would make a good candidate for a follow-up improvement HF     
    
> **\<jeffro256\>** <jeffro256> @rucknium: Almost certainly      
    
> **\<rucknium\>** <rucknium> @ack-j:matrix.org: MAGIC didn't adopt my suggestion to change the title of the Fuzzing project to something easier to understand :P     
    
> **\<articmine\>** <articmine> It is a worthwhile proposal for the first post FCMP++ hard fork.     
    
> **\<ack-j:matrix.org\>** <ack-j:matrix.org> We generally agree and see it as a solid proposal to push forward bulletproof research with little risk.     
    
> **\<ack-j:matrix.org\>** <ack-j:matrix.org> @cyrix126:gupax.io  that is a good question that I’m not sure of the answer     
    
> **\<ack-j:matrix.org\>** <ack-j:matrix.org> @rucknium:monero.social: sorry. Will update     
    
> **\<jberman\>** <jberman> @cyrix126:gupax.io: a good question. I'd guess maybe and probably not, but perhaps could yield potential improvements to BP* as well. Perhaps @emsczkp:matrix.org could give better insight (but may need further details)     
    
> **\<emsczkp:matrix.org\>** <emsczkp:matrix.org> it might be interesting to see how their poly evaluation proofs are working     
    
> **\<emsczkp:matrix.org\>** <emsczkp:matrix.org> within BP range proofs of course, i'm looking into that     
    
> **\<rucknium\>** <rucknium> @emsczkp:matrix.org: Could you read https://moneroresearch.info/285  Wang, N., Wang, Q., Liu, D., Esgin, M. F., & Abuadbba, A. (2025). BulletCT: Towards More Scalable Ring Confidential Transactions With Transparent Setup. BulletCT: Towards More Scalable Ring Confidential Transactions With Transparent Setup.     
    
> **\<rucknium\>** <rucknium> and tell us what you think?     
    
> **\<ack-j:matrix.org\>** <ack-j:matrix.org> @emsczkp:matrix.org: assuming we fund this proposal within the next month. Would their 13 week timeline overlap with your work and have the opportunity to benefit from it?     
    
> **\<rucknium\>** <rucknium> It's not part of your CCS proposal, so don't feel obligated to do it.     
    
> **\<emsczkp:matrix.org\>** <emsczkp:matrix.org> I'll take a look yes     
    
> **\<emsczkp:matrix.org\>** <emsczkp:matrix.org> also if the authors of the paper want discuss with me, it's ok     
    
> **\<rucknium\>** <rucknium> @emsczkp:matrix.org: Thank you!     
    
> **\<jberman\>** <jberman> thank you @emsczkp:matrix.org !     
    
> **\<emsczkp:matrix.org\>** <emsczkp:matrix.org> welcome     
    
> **\<rucknium\>** <rucknium> @ack-j:matrix.org: You could put them it touch with @emsczkp:matrix.org     
    
> **\<ack-j:matrix.org\>** <ack-j:matrix.org> Will do     
    
> **\<rucknium\>** <rucknium> Anything else on this item?     
    
> **\<rucknium\>** <rucknium> We can end the meeting here. Thanks everyone.     
    
> **\<@rucknium\>** 👋 > <@rucknium> We can end the meeting here. Thanks everyone.     
    
> **\<syntheticbird\>** <syntheticbird> Delicious meeting     
    
> **\<jeffro256\>** <jeffro256> Thanks everyone!     
    
> **\<@rucknium\>** <brandon:cypherstack.com> no good reasons, only several poor reasons. i wanted matthias from curve trees to take a look at it, and haven't gotten around to communicating about that. i wanted sarang to take a look at it. etc. but it's important and i agree it should be posted publicly sooner rather than later > <@rucknium> Is there a reason it's not been posted publicly?     
    
> **\<rucknium\>** <rucknium> Just put the DRAFT LaTeX watermark :)     
    
> **\<@sgp_\>** <brandon:cypherstack.com> > <@sgp_> There definitely has been a delay because of it (CS found issues with GBPs as originally written). Assuming the suggested fix is feasible (which kayaba sadly can't confirm asap since they're heads down for a Serai audit for another month), then the further delays should be minimal. If it's infeasible, then that'll be another delay     
    
> **\<brandon:cypherstack.com\>** <brandon:cypherstack.com> yes, the proposal i reviewed (i believe written by sarang, which was a modification of a previous version based on matthias' comments) had a problem with the extractor which sarang did not catch, and the only fix we could identify required a modification to the protocol which worsened efficiency slightly. @kayabanerve:matrix.org has more comments about that.     
    
> **\<brandon:cypherstack.com\>** <brandon:cypherstack.com> @rucknium: yeah, i plan on posting it soon(tm)     
    
> **\<rucknium\>** <rucknium> If you can estimate the inefficiency increase and it's not very high, e.g. 20% or less total increase in FCMP verification time, it would seem OK to me.     
    
> **\<brandon:cypherstack.com\>** <brandon:cypherstack.com> @brandon:cypherstack.com: despite the delay, i count this as a win because the version which would have been posted would have possibly allowed malicious parties to falsely convince verifiers of arithmetic circuit satisfaction. however, we do suspect that someone who could pull that off would be reducible to a discrete log [... too long, see https://mrelay.p2pool.observer/e/9Zvo294Kb1JUSTd1 ]     
    
> **\<brandon:cypherstack.com\>** <brandon:cypherstack.com> @rucknium: @kayabanerve:matrix.org should have a better view of that; i believe we had a few back-and-forth conversations on the specific complexity costs of my proposed fix     
    
> **\<brandon:cypherstack.com\>** <brandon:cypherstack.com> afaik, kayaba has not concretely implemented my changes, so does not yet have concrete efficiency analysis done, and my back of the envelope asymptotics were slightly incorrect the last i spoke with kayaba about it     
    
> **\<rucknium\>** <rucknium> Thanks for your work on that, @brandon:cypherstack.com     

Automated by [this](https://github.com/plowsof/post-libera-meeting-logs)

# Action History
- Created by: Rucknium | 2026-01-20T23:10:22+00:00
- Closed at: 2026-01-31T21:21:26+00:00
