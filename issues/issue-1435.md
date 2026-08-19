---
title: Monero Research Lab Meeting - Wed 05 August 2026, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/1435
author: Rucknium
assignees: []
labels: []
created_at: '2026-08-03T15:00:05+00:00'
updated_at: '2026-08-17T21:39:12+00:00'
type: issue
status: closed
closed_at: '2026-08-17T21:39:12+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

Live log: https://libera.monerologs.net/monero-research-lab

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/meeting.html?p1=1440)

Main discussion topics:

1. Greetings

2. Updates. What is everyone working on?

3. [PQ turnstile spend enables a Carrot/Jamtis distinguisher (privacy leak)](https://github.com/jeffro256/carrot/issues/10).

4. FCMP++ to-do list status. [Programming tasks](https://github.com/seraphis-migration/monero/issues/53). [Reviews and audits](https://cryptpad.fr/sheet/#/2/sheet/view/yPVIUywwA9-deE9VF6GYm9bXbPdCerdST3UDEEfBxcM/embed/). [FCMP++ Integration Audit Overview](https://github.com/seraphis-migration/monero/issues/294). [Network upgrade schedule Gantt chart](https://html-preview.github.io/?url=https://github.com/jeffro256/fcmp-carrot-plan/blob/master/fcmp%2B%2B-carrot.html).

5. [Relative locks with FCMP++](https://github.com/monero-project/research-lab/issues/161).

6. [Shi, Zhang, Ge, Lan, Zhang, & Wang (2026) "Deanonymizing Monero Transactions in Tor Network."](https://arxiv.org/abs/2607.07062)

7. [FCMP beta stressnet](https://github.com/seraphis-migration/monero/releases/).

8. Any other business

8. Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: Rucknium

Previous meeting agenda/logs: #1431   

# Discussion History
## Rucknium | 2026-08-11T17:12:55+00:00
Logs

> __< tevador >__ Can we add this to the meeting agenda? https://github.com/jeffro256/carrot/issues/10     

> __< tevador >__ The second fix is relatively easy to implement, but would need to be fast-tracked to meet the code freeze deadline and possibly be audited.     

> __< rucknium >__ Yes     

> __< rucknium >__ Meeting time! https://github.com/monero-project/meta/issues/1435     

> __< rucknium >__ 1. Greetings     

> __< ack-j:matrix.org >__ Hi     

> __< rucknium >__ jeffro256:monero.social: ping     

> __< rbrunner >__ Hello     

> __< vtnerd >__ Hi     

> __< tevador >__ Hi     

> __< DataHoarder >__ hello     

> __< jberman >__ waves     

> __< rucknium >__ 2. Updates. What is everyone working on?     

> __< rucknium >__ me: Keeping stressnet stressed. We hit 20MB blocks this week. Stressnet bugs.     

> __< syntheticbird >__ Hi     

> __< jpk68:matrix.org >__ Hello     

> __< redsh4de:matrix.org >__ hi     

> __< jberman >__ me: after combing through rucknium:monero.social 's stressnet logs, implemented a series of fixes addressing the most significant apparent issues surrounding tx relay (some upstream, some pertaining to tx relay v2 that we'd want in for the first release of the protocol)     

> __< vtnerd >__ Me: looked at lws DB locking issue, updated weak ptr pr which finally appears mergable, worked a little on strand blocking issue, and have looked at another serialization issue     

> __< articmine >__ Hi     

> __< rucknium >__ 3. PQ turnstile spend enables a Carrot/Jamtis distinguisher (privacy leak) (https://github.com/jeffro256/carrot/issues/10).     

> __< tevador >__ Is jeffro256 present?     

> __< rucknium >__ We can put this item later if you want, tevador     

> __< tevador >__ Basically - when the PQ turnstile protocol is activated (in the future when we want to migrate), it will leak more info than expected. A fix is proposed.     

> __< tevador >__ The fix needs to ne applied to Carrot before the HF.     

> __< tevador >__ OK, we can continue with the next item.     

> __< rucknium >__ I will bundle the FCMP++ schedule with this one since they are related. I will go to relative locks next     

> __< rucknium >__ 5. Relative locks with FCMP++ (https://github.com/monero-project/research-lab/issues/161).     

> __< rucknium >__ There was discussion in this room on Monday: https://libera.monerologs.net/monero-research-lab/20260803     

> __< rucknium >__ Seems like there is good support for the boolean relative lock.     

> __< tevador >__ The last meeting agreed to reserve unlock_time = 1 without actually implementing the lock. I think implementing the lock is feasible for the HF.     

> __< jberman >__ I'd prefer to focus entirely on what's critical for the hf personally, I think stopping at reserving unlock_time = 1 is ok       

> __< rbrunner >__ Pessimists might argue that something will force us into a relatively early hardfork one or the other way, and there we could implement this lock ..     

> __< rbrunner >__ *early follow-up hardfork     

> __< rucknium >__ I've forgotten: For actual implementation of the lock, is a soft fork needed?     

> __< tevador >__ It could be a soft fork if unlock_time = 1 is reserved.     

> __< tevador >__ reserved meaning not rejected by consensus     

> __< tevador >__ Here is a rough amount of code needed to implement the consensus code: https://github.com/seraphis-migration/monero/pull/445     

> __< rucknium >__ Would it be a good idea to audit the implementation code?     

> __< rucknium >__ If it were to be deployed with the HF     

> __< jberman >__ This doesn't need an audit. The payment channel architecture and design perhaps ?     

> __< rucknium >__ It's very short     

> __< rbrunner >__ But that can definitely come later?     

> __< jpk68:matrix.org >__ Considering the double-spend issue that was fixed recently, the prospect of more complexity with this HF is a bit unsettling (especially if the code isn't audited)     

> __< rbrunner >__ And even multiple payment channel approaches implemented I guess     

> __< rbrunner >__ jpk68: Did you have a look at that 445 code?     

> __< UkoeHB >__ I'll put tevador's #10 issue on my todo for today     

> __< jpk68:matrix.org >__ I did, but FWIW the double-spend fix was even less lines of code     

> __< jpk68:matrix.org >__ s/less/fewer/     

> __< rucknium >__ I just think of the number of critical vulnerabilities patched in the BTC Lightning network code. Is it possible to bring payment channels to an audit standard? Or would it be checking if an implementation matches a paper? Anyway, that would be later on.     

> __< tevador >__ To minimize scope, the reservation of unlock_time = 1 only needs 3 lines (1 of which is a comment and 1 is a constant definition)     

> __< rbrunner >__ I am also often weary at more complexity, but if that code really is all on the consensus side, where would a problem hide there?     

> __< rucknium >__ Thanks, UkoeHB     

> __< UkoeHB >__ On monday I posted my revised ACK for the simple relative_lock as a 'prove it or lose it' opportunity for PC proponents.     

> __< rbrunner >__ I am sure there are myriads ways of messing up a payment channel implementation, but that's something else     

> __< rucknium >__ I like the phrase :)     

> __< tevador >__ I think it's well known that payment channels can be implemented with just relative locks and adaptor signatures. The specific protocol is not important for the lock implementation.     

> __< tevador >__ Relative locks can also simplify some atomic swaps protocols.     

> __< DataHoarder >__ the change would allow such designs (or if just the reservation is done, allow a soft fork later to allow the designs) but what tevador is asking for does not include any payment channel design/PoC in code directly to be included into codebase, only specific consensus changes to make them viable     

> __< jberman >__ the code in that PR is incorrect. itwould allow a reference_block higher than chain height, because get_tree_root_at_blk_idx can return a tree root higher than chain height     

> __< DataHoarder >__ (then there is the other suggestion that has extra fields on the tx, but afaik that's not in scope for this HF reservation)     

> __< jberman >__ augh, nvm, spoken too soon     

> __< jberman >__ the changes look ok on first pass     

> __< DataHoarder >__ the question is whether to bring just reservation or that PR to implement relative blocks using the reservation for the HF      

> __< rbrunner >__ Maybe it's more complicated to find out whether somebody can do some nonsense, using those locks in malicious ways.     

> __< rbrunner >__ And if yes, how to mitigate if necessary     

> __< rucknium >__ Could we view the choice this way?: Is it possible to implement actual relative locks without piling more on the plate of people who are chest-deep in the FCMP HF launch work?     

> __< DataHoarder >__ this lock prevents including txs entirely, which is different from them being included and having weird stuff happening     

> __< rbrunner >__ That sounds hopeful     

> __< DataHoarder >__ (so they'd wouldn't be "mineable" until the lock passes)     

> __< tevador >__ Has the code being touched by PR 445 already been audited?     

> __< jberman >__ I think it's not a big deal to get this code in in terms of manpower. Maybe would be nice to have more time to think on the failure modes / concrete payment channel design, but it's such a small change that it's not an issue of manpower      

> __< jberman >__ tevador: no     

> __< tevador >__ I think the audit scope expansion should be pretty minimal.     

> __< rbrunner >__ Seems to me it should be no problem to wait a little with this     

> __< rucknium >__ jberman:monero.social: Are you changing your mind about this, or you just don't feel very strongly about it? > <jberman> I'd prefer to focus entirely on what's critical for the hf personally, I think stopping at reserving unlock_time = 1 is ok       

> __< jberman >__ if people want it in, then manpower isn't the issue / this won't meaningfully delay FCMP++     

> __< rucknium >__ Did tevador once enumerate all of Monero's soft forks?     

> __< rbrunner >__ Hmm, did we have any?     

> __< rucknium >__ I am just thinking of how difficult it would be to soft fork later     

> __< rucknium >__ IIRC, tevador had a broad definition of soft fork     

> __< tevador >__ I don't think Monero has ever had a soft fork     

> __< DataHoarder >__ I tend to come back to https://www.reddit.com/r/Monero/comments/1mvmg44/a_list_of_all_of_moneros_consensus_changes/ which might not be correct     

> __< jberman >__ I have some mild discomfort with a change that may lead to a sub-optimal design (payment channel txs have this fingerprint, fixed 720 days)     

> __< DataHoarder >__ they call a few "soft forks"     

> __< rucknium >__ Wasn't the counterfeiting bug at least a soft fork?     

> __< DataHoarder >__ but these are more like, secret updates to miners to prevent specific attacks     

> __< DataHoarder >__ yeah, #9 on that list     

> __< tevador >__ OK, technically the double spend fix was a soft fork     

> __< jberman >__ 720 blocks*     

> __< tevador >__ jberman: Not all payment channel txs would actually use the time lock on-chain. It only appears when the channel is force closed (meaning there is a dispute).     

> __< jberman >__ right, *the force close txs     

> __< tevador >__ What's the worst thing that can happen if we implement the lock? Nobody using it?     

> __< rucknium >__ Maybe BTC Lightning forced closed txs on-chain could be measured. Or did the Taproot update obscure them?     

> __< articmine >__ This does beg the question. The percentage of force closed TXs vs the increase in the annonimity set due to increased adoption as a result of payment channels.      

> __< DataHoarder >__ There was a larger suggestion that did not use this unlock time field, and would remove that signal, but adds a new field to txs     

> __< rucknium >__ I don't think the force-close txs would create much of a privacy problem. I am willing to listen to other views on that. IMHO, tx fungibility defects matter most when a user's wallet always or usually creates the defect. Then you can follow that wallet's behavior through time. In the extreme, you could even follow it with FCMP txs.     

> __< rucknium >__ But you would not have a user always using force-close txs.     

> __< jpk68:matrix.org >__ Why add part of it now, if the other half has to be added in a later fork anyways? Why not just add it all later?     

> __< UkoeHB >__ jpk68: the point is to give PC advocates the chance to prove it's worth the extra effort/tx cost     

> __< UkoeHB >__ or that's the point from my point of view ^.^     

> __< rucknium >__ Should we move on for now or continue discussing this issue at this meeting?     

> __< DataHoarder >__ 19:46:33 <jpk68:matrix.org> Why add part of it now, if the other half has to be added in a later fork anyways? Why not just add it all later?     

> __< DataHoarder >__ to allow a soft fork (rule tightening) instead of hard fork     

> __< UkoeHB >__ I think we should get a prod-oriented PR for the change and aim further discussion at that.     

> __< DataHoarder >__ though the full set also looks very minimal, as shown in #445     

> __< jpk68:matrix.org >__ If it goes unused, it's just going to create more technical debt for the future with no benefit     

> __< tevador >__ It's a chicken-egg problem. Nobody is going to design a payment channel for Monero using non-existent relative locks.     

> __< rbrunner >__ Well, somebody even tried to implement, but then ran into serious problems ...     

> __< UkoeHB >__ It's a small price for a large opportunity, and the field can be eliminated if it proves useless.     

> __< rbrunner >__ This some small beside the complexity monsters that are FCMP++ and Carrot you can hardly see it :)     

> __< rbrunner >__ *This is so small     

> __< jberman >__ tevador: Grease is seeking funding for their payment channel impl. Their request has seen resistance because they rely on trust in a key escrow service. I think there would be more interest in their request if it was to remove trust using this relative lock feature     

> __< tevador >__ Yes, I think Grease might be interested in using the relative lock in their protocol if it's implemented.     

> __< rucknium >__ > Historical note: We based Grease on Monet/Auxchannel on the predicate that timelocks were unlikely to be added into Monero due to the heterogeneity they would introduce.     

> __< rucknium >__ > But if they were to be implemented in FCMP in a ZK manner, then I agree, this approach is not only much better, it's basically a no-brainer.     

> __< rucknium >__ https://github.com/monero-project/research-lab/issues/161#issuecomment-5107532847     

> __< jberman >__ It doesn't need to be implemented to spur that interest     

> __< rucknium >__ That's what one of the Grease developers said.     

> __< tevador >__ "We based Grease on Monet/Auxchannel on the predicate that timelocks were unlikely to be added into Monero"     

> __< rucknium >__ UkoeHB: What does everyone think about koe's suggestion? "I think we should get a prod-oriented PR for the change and aim further discussion at that."     

> __< rbrunner >__ Certainly allows a focussed long-time disucssion     

> __< tevador >__ AFAICS the PR only needs a test to be added?     

> __< tevador >__ Comment on the PR if anything else is missing.     

> __< jberman >__ tevador: ya I think that calculus changes with this brand new development     

> __< jberman >__ is there interest in funding Grease to develop their design with this new feature? if not, then why would we want it in?     

> __< jberman >__ I don't think this is a chicken-and-egg problem. If there's interest today in Grease developing a design using this feature, then it lends support for the feature     

> __< tevador >__ IIRC their CCS was rejected mostly due to the key escrow requirement. With time-locks, I don't think anyone would oppose it.     

> __< jpk68:matrix.org >__ Maybe this concern is unfounded, but making consensus changes for payment channels could potentially offload some of the onus to keep the base layer inherently scalable     

> __< rucknium >__ This item will reappear next meeting. Let's move to the next item     

> __< rucknium >__ 6. Shi, Zhang, Ge, Lan, Zhang, & Wang (2026) "Deanonymizing Monero Transactions in Tor Network." (https://arxiv.org/abs/2607.07062)     

> __< rucknium >__ Does anyone now want to suggest specific code changes to mitigate the issues raised in the paper and/or volunteer to implement them? Or, especially, review them?     

> __< boog900 >__ This PR should fix one of the issues: https://github.com/monero-project/monero/pull/11048     

> __< rucknium >__ I was thinking more about putting Dandeion++ inside the Tor part of the relay. Besides the implementation complexity, it would probably suffer from easy black hole attacks because Tor Monero nodes are easily Sybil attacked.     

> __< rucknium >__ And then if all the honest nodes get black hole attacked, you are almost back to square one. Or, you are back to BTC network privacy with the diffusion tx broadcast behavior.     

> __< rucknium >__ Any thoughts on black hole attacks?     

> __< vtnerd >__ That was my thought on d++ over tor, theres already an issue with quality relays     

> __< vtnerd >__ I'm going to implement the address relay issue so it doesn't include it every response      

> __< boog900 >__ I do think we should do multiple hops over Tor tho      

> __< boog900 >__ even if not full D++     

> __< vtnerd >__ And I'm going to look into hardening the timed sync requests to limit the timing analysis      

> __< rucknium >__ By the way, a black hole attack on D++ occurs when a malicious peer decides not to relay a stem-phase D++ tx to another peer. It "swallows" the tx to prevent propagation. D++ has an embargo timer that will make the original tx originator ( and any honest nodes that got the tx during the stem phase) to initiate a fluff-phase tx broadcast behavior.     

> __< vtnerd >__ multiple hops over tor would be similar to d++ as we don't send to every outbound tor connection iirc     

> __< rucknium >__ vtnerd: Thanks, vtnerd:monero.social     

> __< boog900 >__ The goal would be to make it so someone getting a tx from an incoming Tor connection does not know they created the tx     

> __< vtnerd >__ The way the code is written, implementing d++ over tor should be somewhat easy, but the results as you mentioned may be less desirable      

> __< boog900 >__ also I want to bring up this PR: https://github.com/monero-project/monero/pull/9295     

> __< boog900 >__ Cuprate has those changes and this is making our tx-relay faster according to gingeropolous:monero.social's monero-sim     

> __< boog900 >__ so faster and more private (more stem hops)     

> __< rucknium >__ The change could be a good use case for monerosim. Try both versions.     

> __< rucknium >__ More discussion of this item for now?     

> __< rucknium >__ 7. FCMP beta stressnet (https://github.com/seraphis-migration/monero/releases/).     

> __< rucknium >__ (We will go back to potential Carrot fix and FCMP schedule after this)     

> __< rucknium >__ We thought we had squashed all of the tx relay bugs, but one more appeared     

> __< jberman >__ Last week I had hoped to put out the next v2.1 release by this week. Ended up identifying a whole series of issues with rucknium:monero.social 's logs, and made PR's for those. The most significant one includes some solid changes to tx relay v2: https://github.com/seraphis-migration/monero/pull/450     

> __< jberman >__ "but one more appeared" -> it turned out that this was apparently caused by an issue that this already-existing PR would fix https://github.com/seraphis-migration/monero/pull/419 , but while digging found a whole bunch of other things worth fixing, including issues from tx relay v2 leading to nodes banning peers     

> __< rucknium >__ So we finally reduced peer ban frequency? Nice.     

> __< jberman >__ The changes to tx relay v2 are especially important imo because it includes a change to the messaging protocol, which we'd want in for the first release of tx relay v2     

> __< rucknium >__ IMHO, peer bans weren't too bad, but it's nice that they will be reduced further.     

> __< jberman >__ I think they also didn't appear as bad because stressnet unbans peers after 2m     

> __< jberman >__ rucknium: the changes would definitely reduce ban frequency (for one, because it stops banning peers and just drops connections lol), but the bulk of changes benefit most from all nodes on the network running them      

> __< rucknium >__ https://mrelay.p2pool.observer/m/monero.social/jQXkPhEHVyFzDJjcBMKvxuZy.png (stressnet_blocksize_week_2026-08-05.png)     

> __< rucknium >__ ^ We hit 20MB blocks this week. IIRC, 20MB blocks was hit on last year's stressnet, but this is the first time on this stressnet.     

> __< rucknium >__ https://mrelay.p2pool.observer/m/monero.social/kZeJRfKupSfsQziIfLKiFeiN.png (stressnet_cpu_week_2026-08-05.png)     

> __< rucknium >__ https://mrelay.p2pool.observer/m/monero.social/KClGPhaHOWkHDrlYfOcWmxja.png (stressnet_RAM_week_2026-08-05.png)     

> __< rucknium >__ ^ That's CPU usage and RAM     

> __< rucknium >__ Anything more on stressnet?     

> __< rucknium >__ Those plots are from https://stressnetnode1.redteam.cash/ . The web app is blank right now because my nodes are catching up. Full storage with logs and everything. Needed to delete things.     

> __< jberman >__ Reiterating a comment I made over in the nwlb channel: assuming the tx relay v2 changes go through, I lean toward wanting a v3 beta stressnet where everyone on the current beta stressnet would have to update to v3, so that we can test that these changes to tx relay v2 are working smoothly. Discussed briefly with boog900:monero.social as well     

> __< jberman >__ Not something that needs to be settled on right now, but just putting the thought out there     

> __< rucknium >__ And it would reduce storage requirements :D     

> __< jberman >__ well it would continue the current stressnet chain     

> __< jberman >__ but I guess we could start over again if people wanted to do that too?     

> __< boog900 >__ You would want to keep the current scaling progress right?     

> __< boog900 >__ how hard is it to build up?     

> __< rucknium >__ You mean a hard fork with the current chain? Or how do you get everyone to upgrade?     

> __< rucknium >__ Takes a couple of weeks to get where we are. Now I have too much of a good thing and my storage is filling 🥲     

> __< jberman >__ We could include something that just prevents new nodes from connecting to the v2 nodes, but continues with the current chain     

> __< rucknium >__ I am OK to try to go a few more weeks with the current chain. I will have to cut the fat to the bone, on storage.     

> __< rucknium >__ I think kico  stopped mining because of too much storage required     

> __< boog900 >__ how big is it?     

> __< boog900 >__ the DB     

> __< rucknium >__ 115GB pruned     

> __< jberman >__ if stressnet participants would prefer a fresh chain to re-spam again, then I think that would be ok     

> __< kico >__ I can add space :D     

> __< kico >__ sorry forgot about the node xD     

> __< jberman >__ thanks kico :)     

> __< kico >__ np     

> __< kico >__ on it :)     

> __< jberman >__ in any case, I think we can cross that bridge of deciding next stressnet steps once/if the tx relay v2 changes go through fine     

> __< rucknium >__ Sounds good. Anything else on stressnet?     

> __< jberman >__ nothing from me     

> __< rucknium >__ 3. PQ turnstile spend enables a Carrot/Jamtis distinguisher (privacy leak) (https://github.com/jeffro256/carrot/issues/10).     

> __< rucknium >__ tevador and jeffro256:monero.social     

> __< tevador >__ Anyone is welcome to comment on the issue     

> __< jberman >__ initial proposal seems reasonable to me     

> __< rucknium >__ What are the downsides to these fix options? A cheap hash calculation and more review of this part of Carrot?     

> __< tevador >__ The fix using k_v would involve one extra elliptic curve operation when constructing a tx     

> __< jberman >__ Does the alternative fix proposed remove the downside risk jeffro256:monero.social  mentioned of making K_v public leaking incoming history?     

> __< tevador >__ Correction: one extra elliptic curve operation when accepting an enote (unless we cache K_v^j)     

> __< tevador >__ K_v^j is not published in the PQ protocol. This might have been a misunderstanding by jeffro256.     

> __< tevador >__ jeffro256 complained that the fix involving k_v makes scanning clunky, hence the alternative proposal     

> __< jberman >__ ack, I think will be best to give jeffro a chance to assess     

> __< rucknium >__ 4. FCMP++ to-do list status. Programming tasks (https://github.com/seraphis-migration/monero/issues/53). Reviews and audits (https://cryptpad.fr/sheet/#/2/sheet/view/yPVIUywwA9-deE9VF6GYm9bXbPdCerdST3UDEEfBxcM/embed/). FCMP++ Integration Audit Overview (https://github.com/seraphis-migration/monero/issues/294). Network upgrade  [... too long, see https://mrelay.p2pool.observer/e/oMqR5p0LREEzZjYw ]     

> __< jberman >__ tobtoht prepared master for Rust build changes, which sets the stage for the Rust FFI getting to master here https://github.com/monero-project/monero/pull/10359 , which is the 2nd to last PR from the Phase 1 audit     

> __< jberman >__ The last PR from Phase 1 is relatively small compared to the priors     

> __< jberman >__ Then it's on to Phase 2 PR's. I don't think an audit needs to hold up the Phase 2 PR's from merge, but arguably still worth auditing alongside Phase 3 especially taking into account the recently identified double spend vuln that would have been in Phase 3 scope     

> __< UkoeHB >__ Link to vuln?     

> __< jberman >__ We're also working on getting quotes for a secondary audit of the Rust FCMP++ lib circuit and gadgets impl (in addition to the fcmp-plus-plus Rust lib), as part of the Research audit task. This covers the section of code analogous to Zcash's recent hidden inflation vuln     

> __< jberman >__ UkoeHB: https://github.com/seraphis-migration/monero/pull/446     

> __< rucknium >__ We can end the meeting here. Thanks everyone.     

> __< tevador >__ foreshadowing comment: https://github.com/monero-project/research-lab/issues/142#issuecomment-3215321512     

> __< DataHoarder >__ 20:38:26 <jberman> if stressnet participants would prefer a fresh chain to re-spam again, then I think that would be ok     

> __< DataHoarder >__ I'd prefer some space cleanup, another heavy session and might run of (fast) storage I have for stressnet. but if that sets back the size scaling, maybe not     


# Action History
- Created by: Rucknium | 2026-08-03T15:00:05+00:00
- Closed at: 2026-08-17T21:39:12+00:00
