---
title: Monero Research Lab Meeting - Wed 13 May 2026, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/1388
author: Rucknium
assignees: []
labels: []
created_at: '2026-05-13T14:41:35+00:00'
updated_at: '2026-05-20T14:43:23+00:00'
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

3. Audit of Helios/Selene Rust library.

4. [Post-quantum encryption](https://github.com/monero-project/research-lab/issues/151#issuecomment-4412416686).

5. [FCMP beta stressnet](https://github.com/seraphis-migration/monero/releases/).

6. [CCS proposal: ProbeLab P2P Network Metrics Proposal](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/667).

7. Any other business

Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: Rucknium

Previous meeting agenda/logs:

#1384 

# Discussion History
## Rucknium | 2026-05-20T14:43:23+00:00
Log:

> __< tevador >__ The recommended reading in preparation for today's meeting is this comment, the following comment and the comment linked in it. https://github.com/monero-project/research-lab/issues/151#issuecomment-4412416686     

> __< kayabanerve:matrix.org >__ I'm happy with AC1024 when it's clarified that while an adversary may see your address received an output, they can't see for how much _or_ where it was spent. Despite not achieving address unlinkability, I believe that's most of the actual benefit we want. cc tevador to explicitly confirm that as while it's a straightforward [... too long, see https://mrelay.p2pool.observer/e/0O-h1IILbE1IRDRL ]     

> __< kayabanerve:matrix.org >__ (and thank you, tevador, for all your hard work on this in general)     

> __< hbs:matrix.org >__ For whatever it matters, my personal view is that a "might" is always better than certainty.     

> __< sgp_ >__ I think either AC1024 or BC512 are sensible choices based on those tables. Thus I think AC1024 wins for practicality     

> __< sgp_ >__ I know that somewhat contradicts my advocacy for BC512 earlier, so apologies for dragging that out     

> __< camphor:matrix.org >__ Now that the mining attack is over, might this be reconsidered? https://github.com/monero-project/research-lab/issues/98     

> __< rucknium >__ camphor:matrix.org: I don't know if anyone has the available time at the moment to reopen the selfish mining mitigation discussion, but I hope we will in a few months. But if someone wants to push for it, they can lead analysis and discussion.     

> __< rucknium >__ MRL meeting in this room in two hours.     

> __< sgp_ >__ I want to briefly add that an RFQ was sent out for Helios/Selene review. No action needed here (yet)     

> __< rucknium >__ Meeting time! https://github.com/monero-project/meta/issues/1388     

> __< rucknium >__ 1. Greetings     

> __< vtnerd >__ hi     

> __< tevador >__ Hi     

> __< jberman >__ waves     

> __< gingeropolous >__ hi     

> __< rbrunner >__ Hello     

> __< articmine >__ Hi     

> __< rucknium >__ 2. Updates. What is everyone working on?     

> __< jberman >__ beta stressnet     

> __< gingeropolous >__ monerosim v0.1.0 is out: https://github.com/Fountain5405/monerosim     

> __< rucknium >__ me: Keeping stressnet stressed and reporting issues.     

> __< iamnew117:matrix.org >__ Hello     

> __< tevador >__ Jamtis-PQ     

> __< koe000:matrix.org >__ Hi. Me: multisig wip     

> __< rbrunner >__ Polyseed, still     

> __< vtnerd >__ me: updating/rebasing serialization PR and looking at how to alleviate serialization limitations wrt to blocksize     

> __< vtnerd >__ it might be possible to alleviate issues without adopting a new serialization framework, but it’ll be gross and probably rejected     

> __< jpk68:matrix.org >__ Hello     

> __< rucknium >__ 3. Audit of Helios/Selene Rust library.     

> __< rucknium >__ sgp_: sgp_:monero.social said "I want to briefly add that an RFQ was sent out for Helios/Selene review. No action needed here (yet)"     

> __< rucknium >__ AFAIK no further discussion of this item is needed, but please speak up if it is needed.     

> __< sgp_ >__ Action will be required around May 30 :)     

> __< rucknium >__ 4. Post-quantum encryption (https://github.com/monero-project/research-lab/issues/151#issuecomment-4412416686).     

> __< jeffro256 >__ Howdy      

> __< tevador >__ The goal for today is to hopefully make a final decision on the PQ encryption variant for Jamtis. See the table in the linked comment for details.     

> __< jeffro256 >__ me: beta stressnet issues and features      

> __< tevador >__ Any objections to going forward with Jamtis-AC1024?     

> __< rucknium >__ "Monero adopts a PQ protocol" = Resistance to PQ counterfeiting and theft, right?     

> __< sgp_ >__ None from me. Just to clarify, AC512 isn't considered because it doesn't offer meaningful efficiency compared to AC1024 right? The extra margin is cheap in this case?     

> __< gingeropolous >__ is the argument against BC512 mainly the 5x scan time?     

> __< tevador >__ rucknium: Yes, that has to be adopted before Q-Day.     

> __< jberman >__ I think it's worth noting that clients would have to download the pruned tx data, so mobile scan time (which is presently usually bottlenecked by download speeds via remote daemons) would increase from pruned tx sizes as well     

> __< rucknium >__ tevador, how confident are you that CSIDH-1024 won't be broken for 60 years?     

> __< jberman >__ I note this because Jamtis-AN509 looks pretty attractive in that table as well, but when considering the 4.35x pruned tx size impact on mobile wallets, it's harder to swallow     

> __< tevador >__ I'm fairly confident about CSIDH-1024.     

> __< gingeropolous >__ because "Alice received an enote in tran. X." vs. "Alice might have received an enote in tran. X." seems like quite the difference      

> __< tevador >__ There are 2 arguments against BC512: 1. Scan time 2. (in-)security     

> __< jberman >__ All things considered, I +1 that Jamtis-AC1024 is the strongest option on this table here as a positive incremental step forward toward improved PQ privacy     

> __< tevador >__ Although even BC512 is likely good for ~20 years longer than Curve25519     

> __< sgp_ >__ gingeropolous: the key distinction is that you can't continue using that information to discover transactions where those outputs might be spent. That significantly mitigates the privacy downside     

> __< articmine >__ 2 security is a concern for me      

> __< jpk68:matrix.org >__ Would AN509 allow for a non-interactive protocol like CSIDH would?     

> __< gingeropolous >__ 2^60 vs 2^72 ?      

> __< tevador >__ Yes, AC1024 and AN509 are functionally *almost* equivalent, except AN509 loses privacy if the address generator tier is compromised, AC1024 does not.     

> __< tevador >__ Yes, 2^72 is 4096 times harder to break (actually more due to practical reasons) than 2^60.     

> __< gingeropolous >__ yeah 20 vs 50 yrs as in your scenario. though part of me is attracted to the 20 b/c it keeps the fire lit. 50 years ppl can handwaive "its fine......"     

> __< tevador >__ The choice is either high privacy for 20 years and then none vs medium privacy for 50 years and then none.     

> __< jberman >__ We have to deal with PQ to prevent hidden inflation, so the timeline is sooner than 20 years regardless     

> __< jeffro256 >__ Besides the fact that it still doesn't hide the social graph with timing information? I have a feeling that with all these variations, our addressing protocol suite might end up like TLS: many different modular cryptographic components with one overarching generalized architecture  > <tevador> Any objections to going forward with Jamtis-AC1024?     

> __< jberman >__ and can't really be handwaved     

> __< rbrunner >__ I guess there are no variants of NTRU-509 that are bit less heavy, but still quite attractive? NT-300 or whatever ...     

> __< rbrunner >__ *NTRU-300     

> __< tevador >__ No, the security of lattices drops very fast, NTRU-300 would be completely insecure.     

> __< tevador >__ jeffro256: Depends on what you mean by social graph. AC1024 is enough to hide spends.     

> __< sgp_ >__ I was initially drawn to the "flashy" privacy of BC over AC, but in practice it's a high extra cost (and in practice, a lower security margin) to provide better privacy only in a specific edge case, at least that's how I currently view it     

> __< jeffro256 >__ So are we disabling LWS for AC1024?     

> __< jeffro256 >__ Or we send s_vv to the LWS ?     

> __< jeffro256 >__ s_vb     

> __< tevador >__ No, LWS will work independently of the PQ encryption layer.     

> __< jeffro256 >__ Okay so primary vt is still PQ insecure right ?     

> __< tevador >__ The expensive CSIDH-1024 calculation kicks in after a 24-bit view tag match, which is a relatively managable amount of CPU time.     

> __< tevador >__ For AC1024, the whole view tag is classical. For BC512, the secondary view tag is PQ.     

> __< gingeropolous >__ yeah i can get behind AC1024     

> __< tevador >__ gingeropolous: Can you elaborate?     

> __< gingeropolous >__ i mean the arguments for it vs. the bc512 make sense.      

> __< jeffro256 >__ So if both secondary and primary view tags are not hidden from a QA, then the social graph is revealed with extremely high probability , getting exponentially higher the more interactions b/t 2 entities      

> __< gingeropolous >__ i think either are probably fine, if we're going to bolt on a PQ preventative thing, based on whats been presented to my feeble brain     

> __< tevador >__ jeffro256: How so? The QA can find received enotes, but cannot locate outgoing payments.     

> __< sgp_ >__ jeffro256:monero.social this is minimized because they need to know what address to check to see if it received funds, right?     

> __< tevador >__ Yes, the all this assumes that your Jamtis address is known to the attacker and the attacker is not the sender.     

> __< jeffro256 >__ tevador: They can locate view tags for change enotes , and all outgoing txs must have a change enote even if change amount is 0     

> __< tevador >__ No, view tags for change enotes are calculates with symmetric crypto, which is PQ-proof.     

> __< sgp_ >__ Even if they weren't, you could use a different change address     

> __< jeffro256 >__ Then LWS cannot find change enotes for AC1024 . Thats fine if that's the tradeoff we want to take , but that should be noted      

> __< tevador >__ LWS can locate the enotes, because users will give the LWS server their symmetric secret for internal view tags.     

> __< tevador >__ If they choose that option to reduce the download bandwidth.     

> __< jeffro256 >__ Oh , but a different symmetric secret from s_vb?     

> __< tevador >__ Yes, a single purpose secret, s_fa     

> __< tevador >__ https://gist.github.com/tevador/639d083c994c1ef9401832c08e2b7832#43-additional-keys     

> __< rbrunner >__ Can't ever have too many keys and secrets :)     

> __< jeffro256 >__ Ah interesting , I didn't see that in the updated spec, sorry. Interesting . so now there's 3 scan paths      

> __< jeffro256 >__ Yeah that could work      

> __< koe000:matrix.org >__ jeffro255: we discussed it a few weeks ago in here, maybe you forgot     

> __< jeffro256 >__ In that case, I think AC1024 is a decent choice      

> __< neptunian:unredacted.org >__ Good evening, all.     

> __< jeffro256 >__ Given the performance of better privacy options      

> __< neptunian:unredacted.org >__ jeffro256: Yeah. Given it's sufficiently strong and still PQ with reasonable overhead, I'd choose AC1024.     

> __< jeffro256 >__ koe000:matrix.org: Yes I do remember discussing , but I guess I didn't quite get that we were talking about slightly different things     

> __< rucknium >__ I see some Matrix people typing, but no message yet     

> __< rucknium >__ We should probably move to the next item. I will leave it to tevador to decide whether the discussion today is enough to go forward with AC1024 R&D or if even more discussion is needed.     

> __< jpk68:matrix.org >__ You can ignore my typing, I have nothing really worth sharing about this :)     

> __< neptunian:unredacted.org >__ I do have a question about BC1024 and related.     

> __< neptunian:unredacted.org >__ We already sort of concluded that performance overhead for it is entirely undesirable (see https://github.com/monero-project/research-lab/issues/151#issuecomment-4412416686), however, I would like to know if PEGASIS or CSURF would make this at all feasible.     

> __< neptunian:unredacted.org >__ I'm just curious as to whether or not this would be viable after both variants receive more scrutiny.      

> __< neptunian:unredacted.org >__ I don't have much else to add here since most topics seem to have been covered. I'm just throwing out a curiosity I have.     

> __< tevador >__ CSUDH-1024 performs the same as CSIDH-1024 and PEGASIS is not much faster and only has a proof of concept, far from practically usability.     

> __< tevador >__ CSURF-1024*     

> __< rucknium >__ 5. FCMP beta stressnet (https://github.com/seraphis-migration/monero/releases/).     

> __< neptunian:unredacted.org >__ rucknium: I saw some crazy stuff go down on the stressnet, haha.     

> __< rucknium >__ jberman:monero.social: Do you want to share the GH issues that have appeared on stressnet?     

> __< tevador >__ From the PEGASIS paper: Our implementation in SageMath takes 1.5s to compute a group action at the CSIDH-512 security level, 21s at CSIDH-2048 level and around 2 minutes at the CSIDH-4096 level     

> __< jberman >__ Sure     

> __< rucknium >__ We got to 5MB blocks and 1.4GB txpool. There was an accidental deep reorg. And a rare confession by the reorg-er :)     

> __< jberman >__ Red Failed to verify spam after deep reorg, node unresponsive, investigation still ongoing (we attempted another deep reorg that didn't trigger the issue): https://github.com/seraphis-migration/monero/issues/372     

> __< jberman >__ Double spend errors / rescan_spent apparently not resolving (this may be a regression from alpha, investigating further today): https://github.com/seraphis-migration/monero/issues/365     

> __< jeffro256 >__ I think that j-berman has identified an issue which causes ridiculous slowdowns after a large reorg when the node is set to mine and/or provide block templates over RPC. It could happen on mainnet as well too      

> __< neptunian:unredacted.org >__ tevador: Yikes.     

> __< rucknium >__ I am surprised that we seem to be hitting a ceiling at 5MB blocks, despite txs with fee level 2. Maybe I shouldn't be surprised.     

> __< jberman >__ Higher ban frequency (some theories on why, definitive cause not identified yet): https://github.com/seraphis-migration/monero/issues/373     

> __< rucknium >__ I assume the new scaling rules have something to do with it.     

> __< jberman >__ Failed to switch to alternative blockchain in the logs (narrowed in on the cause, looks like a not-too-serious / not-too-difficult to rectify issue): https://github.com/seraphis-migration/monero/issues/374     

> __< jberman >__ One node's pool not catching up to another (not yet deeply investigated, nahuhh shared a theory on the issue): https://github.com/seraphis-migration/monero/issues/375     

> __< articmine >__ rucknium: It makes sense since there is an 8x cap on the median     

> __< jberman >__ Windows GUI binary crashing, but not self-compiled windows version (possibly caused by another solved issue with redsh4de:matrix.org's help): https://github.com/seraphis-migration/monero/issues/376     

> __< rucknium >__ People are using my spammer, but the reorgs are making it difficult sometimes! https://github.com/Rucknium/xmrspammer     

> __< jberman >__ And we've solved an RPC issue causing problems for cross-platfrom wallet -> daemon (thanks to redsh4de's help) : https://github.com/seraphis-migration/monero/issues/367     

> __< rucknium >__ "One node's pool not catching up to another" is disappointing to me because we have had this symptom since the very first stressnet, which was non-FCMP.     

> __< rucknium >__ Different nodes having different txpool contents would usually make accepting 0-conf txs unsafe.     

> __< jberman >__ On alpha we used ad hoc code for refilling the pool to reduce bandwidth usage of the stressnet. Now we have tx relay v2, and we reintroduced the current node's logic for pool refilling. So that one will take some investigation to see why it's not working as expected     

> __< rucknium >__ So are we stuck at 5MB blocks until the long-term median starts rising?     

> __< neptunian:unredacted.org >__ rucknium: Is the divergence worse under FCMP or just more noticeable here with the spammer?     

> __< articmine >__ rucknium: Yea     

> __< rucknium >__ neptunian:unredacted.org: No. The txpool divergence has occurred with about the same severity for the last 3 stressnets. Maybe not so bad in the 2nd stressnet (FCMP alpha).     

> __< ofrnxmr >__ rucknium: the long term median was decreased for stressnet fwiw     

> __< articmine >__ One can go to 10 MB by paying the max fee with no scaling      

> __< articmine >__ I am assuming that the ML is starting at ZM     

> __< rucknium >__ ofrnxmr:monero.social: Do you remember what it's set to? I guess I could try to look for the config constant.     

> __< jberman >__ 2 weeks     

> __< jberman >__ https://github.com/seraphis-migration/monero/pull/301/changes     

> __< rucknium >__ Thanks, jberman:monero.social     

> __< jeffro256 >__ So blocksize can increase with ~1 week of spam      

> __< articmine >__ jberman: Then one can go to 6MB     

> __< rucknium >__ I'm going to stop trying to spam with level 2 fees. Just level 1 and wait for the long term median to kick in.     

> __< articmine >__ rucknium: It wull not with no spam     

> __< articmine >__ This is by design      

> __< rucknium >__ Then I will go for level 2 fees     

> __< jberman >__ I think would be good if we have another try at repro'ing that deep reorg red verified spam     

> __< rucknium >__ What can be done different this time?     

> __< jberman >__ We discussed in the stressnet channel invalidating lots of txs, we can move discussion back in there     

> __< rucknium >__ I think DataHoarder[m]  may possibly have a node in the bad state from the first reorg. Last hope.     

> __< articmine >__ One should be able to maintain the short term median with level 1 fees     

> __< articmine >__ From what I can see this is working as designed      

> __< rucknium >__ More about stressnet?     

> __< jberman >__ Hoping we'll have made good progress on those issues by next week :)     

> __< jberman >__ and v1.2 coming soon that also solves a number of issues: https://github.com/seraphis-migration/monero/pull/380      

> __< rucknium >__ yiannisbot:matrix.org     

> __< yiannisbot:matrix.org >__ Hi 👋     

> __< rucknium >__ 6. CCS proposal: ProbeLab P2P Network Metrics Proposal (https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/667).     

> __< rucknium >__ The CCS system is back up. Thanks for everyone who helped get it working again: https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/667     

> __< rucknium >__ In the last discussion, a few people were not happy with the part of the CCS that was a monitor dashboard, similar to https://xmrnetscan.redteam.cash/     

> __< yiannisbot:matrix.org >__ Yup, correct.      

> __< boog900 >__ oh wow look at the new nodes in the last few days      

> __< rucknium >__ :(     

> __< boog900 >__ so much adoption 🚀     

> __< rucknium >__ plowsof:matrix.org is working on a better DNS-based blocklist that could contain more addresses: https://github.com/monero-project/monero/pull/10572     

> __< yiannisbot:matrix.org >__ The dashboard would give more insights regarding the new nodes, but indeed there was some disagreement from the community to proceed with this.      

> __< yiannisbot:matrix.org >__ By "this", I mean Milestone 1 of the proposal.     

> __< plowsof >__ thanks for sharing, after review comments from iamamyth im moving to obtaining a url:hash for the ban list and applying it directly. same effect none the less     

> __< boog900 >__ I don't think it would give us much more insight, we pretty much know that 1000 real nodes did not come online overnight     

> __< yiannisbot:matrix.org >__ Agreed. So AFAIU, the community is in favour of dropping M1 from the proposal and moving on with M2 - is that correct rucknium:monero.social ?     

> __< rucknium >__ I think M1 has received negative feedback. M2 needs more feedback.     

> __< jpk68:matrix.org >__ The XMR/EUR exchange rate is a bit off     

> __< rucknium >__ For M2, you would probably want to get an estimate of how frequently nodes rotate peers. I had some rough results here: https://github.com/Rucknium/misc-research/blob/main/Monero-Black-Marble-Flood/pdf/monero-black-marble-flood.pdf     

> __< rucknium >__ Line 329 - 349, pages 20 - 21. And Figure 14     

> __< rucknium >__ If you were to do M2, I would want to have a confidence interval on your estimator for the number of unreachable nodes. I don't really want you to solve the estimation problem by setting up hundreds of nodes (or proxies) and get a good estimate by brute force.     

> __< rucknium >__ So you could derive the confidence intervals mathematically (ideal, but difficult) or do Monte Carlo and/or bootstrapping to get the confidence intervals.     

> __< yiannisbot:matrix.org >__ Sure, but out of curiosity, why would this not be desired?     

> __< yiannisbot:matrix.org >__ > I don't really want you to solve the estimation problem by setting up hundreds of nodes (or proxies) and get a good estimate by brute force     

> __< rucknium >__ Bloats your costs. Bloats MRL's costs if it wants to take samples over time. And deploying that many nodes and collecting all the data together is like spying on users.     

> __< rucknium >__ The task is to use mathematics to get the estimate. Throwing more infrastructure is...not difficult enough!     

> __< rucknium >__ We want to use your expertise. Not just have SaaS (software as a service)     

> __< rucknium >__ I should say I want that. I shouldn't speak for others.     

> __< yiannisbot:matrix.org >__ I see, yes. I think a combination of both would be ideal. If costs are unbearable, it could be that deploying nodes could be done once a week/month/whatever.      

> __< rucknium >__ I shouldn't speak for others on that statement.     

> __< rucknium >__ You should be able to express the confidence interval as a function of the number of nodes you need to deploy. Then make a decision about how many nodes would give you an acceptable confidence interval.     

> __< yiannisbot:matrix.org >__ Is it recommended then to add the following statement in M2 of the proposal?     

> __< yiannisbot:matrix.org >__ > So you could derive the confidence intervals mathematically (ideal, but difficult) or do Monte Carlo and/or bootstrapping to get the confidence intervals.     

> __< rucknium >__ yiannisbot:matrix.org: yiannisbot:matrix.org: Yes. I think so.     

> __< yiannisbot:matrix.org >__ rucknium: Yes, exactly. That's what I also had in mind. But needs some more thinking.      

> __< rucknium >__ Or, I could try to figure out that part of the project, but it would reduce your budget accordingly.     

> __< yiannisbot:matrix.org >__ rucknium: And then bring the topic back here next week? Or what's the process going forward?      

> __< rucknium >__ I try to get more people involved in Monero research instead of being greedy with tasks that are in my area.     

> __< yiannisbot:matrix.org >__ rucknium: Not sure I'm getting this :)      

> __< rucknium >__ yiannisbot:matrix.org: You need more feedback on Milestone 2.     

> __< yiannisbot:matrix.org >__ WDYM?     

> __< yiannisbot:matrix.org >__ rucknium: Sure, how can we make that happen? Are there people here that we can bring into the discussion?      

> __< rucknium >__ yiannisbot:matrix.org: I am a statistician (actually, economist with empirical focus) and therefore proposing and exploring the properties of a statistical estimator is in my area. But I don't want to lay claim to a task just because it's in my area. Anyway, there is much more research on Monero stats than I can do alone.     

> __< rucknium >__ https://ccs.getmonero.org/how-to-ccs/     

> __< rucknium >__ > 7. You're done. Now go drum up some support. Good job on getting all the way here. When you finish, the community will be discussing your proposal on the merge request itself. If you want to weigh in on the discussion, feel free. It will be up to you to get people to support your proposal, both for it to be moved to the Funding Required stage, and also while its awaiting donations.     

> __< rucknium >__ I think you should ask for feedback on M2 from the people who have already given feedback on M1. That includes people who have given negative feedback. A lot of people don't have a specific interest enough to give feedback. You can go to the broader community like #monero-community:monero.social  , Monero Reddit, Twitter, or o [... too long, see https://mrelay.p2pool.observer/e/v7aW4YILdUxjVi1v ]     

> __< boog900 >__ I think 113 XMR is quite a bit for this task ngl.      

> __< boog900 >__ Is that the amount it'll be?     

> __< rucknium >__ We're 1:45 into the meeting. I will end the meeting here and discussion on topics can continue. Thanks everyone.     

> __< yiannisbot:matrix.org >__ The amount is estimated to be about that, yes. We'll revisit though once we have the full feedback of what is desired here.     

> __< yiannisbot:matrix.org >__ Rucknium gave some constructive feedback on the direction.     

> __< yiannisbot:matrix.org >__ rucknium: Yes, I suspect that this is the most likely feedback we're going to get. So in order for this to go forward, it will need feedback from a few technical people. That's what we've seen generally. So if you know people that would care/appreciate this kind of work it would be great to talk to them (during this meeting or elsewhere).      

> __< rucknium >__ Those people would probably be boog900:monero.social , vtnerd:monero.social , syntheticbird:monero.social , ofrnxmr:monero.social , sgp_:monero.social , plowsof:matrix.org     

> __< rucknium >__ And articmine:monero.social     

> __< rucknium >__ (If I didn't mention you and you think I should have, now is your time to speak up and comment!)     

> __< rucknium >__ rbrunner could comment, too, since he wrote the anti-spy subnet deduplication code.     

> __< ofrnxmr >__ Doing that right now btw > <jberman> I think would be good if we have another try at repro'ing that deep reorg red verified spam     

> __< yiannisbot:matrix.org >__ Thank you! Message to those folks: please contribute ideas to the discussion, either here, or in the Lounge or in the proposal repo itself. I think this would speed things up quite a bit. > <rucknium> Those people would probably be boog900:monero.social , vtnerd:monero.social , syntheticbird:monero.social , ofrnxmr:monero.social , sgp_:monero.social , plowsof:matrix.org     

> __< ofrnxmr >__ Is the current plan to gpl / foss any work? I need to re-look at m2     

> __< yiannisbot:matrix.org >__ ofrnxmr: Yes. We agreed in the previous meeting to go with AGPL. Let us know thoughts.     

> __< DataHoarder >__ What bad state Rucknium?     

> __< rucknium >__ DataHoarder: https://github.com/seraphis-migration/monero/issues/372     

> __< DataHoarder >__ unless I shut it off at the right time I don't think I have one     



# Action History
- Created by: Rucknium | 2026-05-13T14:41:35+00:00
