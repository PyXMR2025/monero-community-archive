---
title: Monero Research Lab Meeting - Wed 25 March 2026, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/1359
author: Rucknium
assignees: []
labels: []
created_at: '2026-03-25T10:21:41+00:00'
updated_at: '2026-04-08T15:04:16+00:00'
type: issue
status: closed
closed_at: '2026-04-08T15:04:16+00:00'
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

6. [Bulletproofs*: Verifier-Efficient Arithmetic Circuit Proofs via Folding](https://eprint.iacr.org/2026/586). [CCS update](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/626#note_35351).

7. [CCS proposal: I2P SAMv3 support](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/650).

8. Any other business

Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: Rucknium

Previous meeting agenda/logs:

#1355  

# Discussion History
## plowsof | 2026-03-25T12:26:05+00:00
Can emsczkp research Bulletproofs* update be added to the agenda, if not discussed then shared for visibility ? https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/626#note_35351

## Rucknium | 2026-03-25T15:06:17+00:00
@plowsof : Yes

## Rucknium | 2026-04-01T15:07:39+00:00
Log:

> __< rucknium >__ Meeting time! https://github.com/monero-project/meta/issues/1359     

> __< rucknium >__ 1. Greetings     

> __< UkoeHB >__ Hi     

> __< jberman >__ waves     

> __< rbrunner >__ Hello     

> __< vtnerd >__ hi     

> __< rucknium >__ 2. Updates. What is everyone working on?     

> __< vtnerd >__ me: working on some monerod bug fixes, and a bunch of docker stuff for monero-lws (primarily for use in the docs/tutorials website)     

> __< iamnew117:matrix.org >__ hello     

> __< jberman >__ me: progressing FCMP++ integration audit, continuing on a fix for a hanging shutdown in monerod (PR should be ready today)     

> __< UkoeHB >__ me: to start reviewing carrot_core today.     

> __< rucknium >__ 3. FCMP code integration audit overview (https://github.com/seraphis-migration/monero/issues/294).     

> __< jberman >__ Received a quote from Cypher Stack, and with the help of sgp_:monero.social planning to reach out to some more firms to get additional quotes. Would prefer to keep the CS quote private until we have all quotes & estimates     

> __< rucknium >__ I need to start bringing out some auction theory for these audit bidding processes 😉     

> __< jberman >__ Heh     

> __< rucknium >__ Anything else on this agenda item?     

> __< rucknium >__ 4. FCMP beta stressnet (https://github.com/seraphis-migration/monero/issues/166).     

> __< jberman >__ Have gotten word from kayaba, progress on the major blocking item for beta (GBP changes in response to audit) is expected     

> __< rucknium >__ Great!     

> __< rbrunner >__ "progess is expected" sounds cautious, but certainly going into the right direction :)     

> __< rucknium >__ 5. Grease Payment Channels (https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/651).     

> __< rucknium >__ This is a CCS proposal for the first operational payment channel implementation for Monero.     

> __< rucknium >__ Total requested budget is 516.9 XMR.     

> __< rucknium >__ The Bitcoin Lightning Network is a network of many payment channels linked together. IIRC, the Grease team wants to focus on one-to-one or small networks instead of trying to implement a Monero Lightning Network.     

> __< plowsof >__ CJS77 can not make it today, kayaba responded to a comment on gitlab earlier here https://libera.monerologs.net/monero-research-lab/20260325#c663230     

> __< rbrunner >__ Quite some stuff to read, that CCS text is very detailed     

> __< jberman >__ Seems like kayabanerve:matrix.org raised a good point. In line with that point, it doesn't seem like it should be marketed as a trustless solution when it relies on a solution not yet fleshed out / explained     

> __< rucknium >__ After the meeting, CjS77 can answer any quested posted during the meeting.     

> __< rucknium >__ I'm a skeptic on Payment Channel Networks as a 2nd layer payment system, but not a skeptic on small-scale payment channels, FWIW.     

> __< jberman >__ and also the core innovation of payment channels was/is the trustless factor, so I think it's extremely critical that that is fleshed out     

> __< rbrunner >__ It seems it's altogether easy to underestimate what is needeed for "just connect two people" ...     

> __< articmine >__ This is a very exciting proposal. I find the focus on one to one or small networks particularly appealing. My comment is that this is not a substitute for scaling.     

> __< rucknium >__ IMHO, Payment Channel Networks (PCNs) have problems with user adoption, reliability, and privacy.     

> __< articmine >__ rucknium: I agree for large scale network attempts     

> __< rucknium >__ Lightning has improved its privacy characteristics in recent years AFAIK, but I don't think privacy issues in PCNs can be eliminated completely.     

> __< rucknium >__ Tang, Wang, Fanti, & Oh (2020) "Privacy-Utility Tradeoffs in Routing Cryptocurrency over Payment Channel Networks" https://arxiv.org/abs/1909.02717     

> __< articmine >__ One to one or very small is a different matter .     

> __< rucknium >__ > However, in deployed PCNs [payment channel networks], channel balances (i.e., edge weights are not revealed to users for privacy reasons; users know only the initial weights at time 0. Hence, when routing transactions, users first guess a path, then check if it supports the transaction. This guess-and-check process dramatica [... too long, see https://mrelay.p2pool.observer/e/zpee_PIKLW1fbFNV ]     

> __< rucknium >__ One of that paper's authors, Fanti, is the lead author of the Dandelion++ paper.     

> __< articmine >__ I am especially interested in one to one.     

> __< rbrunner >__ So this probably also shows nicely how complexity can explode if you from connecting two parties to networks?     

> __< rbrunner >__ *if you go     

> __< rucknium >__ I think payment channels could be useful for xmrchat.com , for example. Instant payments for the lie super chat messages and you would never have the 10 block lock problem if you wanted to send a lot of messages in a short time. Of course, having a service-side "wallet" that you deposit XMR credits to would have similar characteristics, but would not be trustless.     

> __< rbrunner >__ Using XMR like a micropayment system     

> __< rucknium >__ rbrunner: IIRC, a paper showed that Lightning routing was NP-hard. But there are heuristics that can get you routing with acceptable reliability. I will try to find the paper.     

> __< rbrunner >__ Might not take long only people start to bet over such channels ...     

> __< articmine >__ Micro payments is a possible application; however I see XMR funded centralized ledgers as very viable for micro payments. The funding of such a ledger could in itself be a use case for payment channels      

> __< rucknium >__ I think this is the paper: Pickhardt & Richter (2021) "Optimally Reliable & Cheap Payment Flows on the Lightning Network" https://arxiv.org/abs/2107.05322     

> __< rucknium >__ > We observe that finding the cheapest multi-part payments is an NP-hard problem considering the current fee structure and propose dropping the base fee to make it a linear min-cost flow problem. Finally, we discuss possibilities for maximizing the probability while at the same time minimizing the fees of a flow. While this tu [... too long, see https://mrelay.p2pool.observer/e/gfW9_PIKTlNqNHZ3 ]     

> __< rucknium >__ Pickhardt has done a lot of work on Lightning routing.     

> __< rbrunner >__ As far as I know it's quite some time since the last time LN really made waves. Maybe struggles to grow?     

> __< rucknium >__ Back to the Key Escrow Service (KES). That does seem like a significant problem with Grease at the moment.     

> __< rbrunner >__ But I don't think that this really means something for our XMR based proposal now.     

> __< rucknium >__ rbrunner: Merchant data suggests that Lightning adoption is low. And Lightning has an additional big incentive for users that Grease would not have. On-chain BTC fees are much higher than XMR fees are or will be.     

> __< rbrunner >__ I see     

> __< jberman >__ As I understand it, the existence of the KES implies a reduction in security of the protocol compared to payment channels as implemented on Bitcoin     

> __< jeffro256 >__ rucknium: True, though on the flip side, as was previously mentioned, the 10 block lock is a "push" force      

> __< rucknium >__ KES serves a purpose similar to the Hash Time Locked Contract (HTLC) + watchtower system in Lightning, right? Except Lightning users can go without a third-party watchtower if their own Lightning node has reliable uptime. With Grease, the KES is mandatory for trustlessness, right?     

> __< jberman >__ That's how I understand it rucknium:monero.social     

> __< jeffro256 >__ rucknium: That's how I understand it      

> __< jeffro256 >__ Jinx      

> __< rucknium >__ It's how we understand it :P     

> __< rucknium >__ FWIW, Grease isn't the only proposed Monero payment channel systems. I think there are at least 4 papers total. But Grease, based on Monet, is the only one that has much, if any, code written.     

> __< rucknium >__ ■ (https://eprint.iacr.org/2022/117); ■ (https://eprint.iacr.org/2021/1445); ■ (https://eprint.iacr.org/2020/1441); ■ (https://eprint.iacr.org/2022/744); ■ (https://ieeexplore.ieee.org/abstract/document/10371398)     

> __< rucknium >__ ^ Each of the squares is a Monero Payment Channel paper. From https://github.com/monero-project/research-lab/issues/94     

> __< rucknium >__ More discussion on Grease for now? It will probably appear on next week's agenda too.     

> __< rucknium >__ emsczkp:matrix.org: Is emsczkp:matrix.org  here?     

> __< emsczkp:matrix.org >__ here i am     

> __< jberman >__ congrats emsczkp:matrix.org :)     

> __< emsczkp:matrix.org >__ just to say thank you and i hope you appreciate little BP*. it's already an amazing experience. Looking foreward to see your comments     

> __< rucknium >__ One more thing on PCNs for Monero: IMHO, you have a privacy issue with PCNs even with FCMP because a single Monero tx output start to accumulate "history" if you use it for PCNs. The info is transmitted through the network. But Grease, at present, would mostly avoid that since it's use case is one-to-one and/or small network.     

> __< rucknium >__ 6. Bulletproofs*: Verifier-Efficient Arithmetic Circuit Proofs via Folding (https://eprint.iacr.org/2026/586). CCS update (https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/626#note_35351).     

> __< rucknium >__ emsczkp:matrix.org: Could you summarize what your paper has accomplished?     

> __< rucknium >__ Typo: * its use case     

> __< emsczkp:matrix.org >__ In a very summary. This is the first folding scheme, in my knowledge, for BP. Following the ProtoStar compiler, here the name BP*. This toward enabling a best verification across many (folded) proofs and folding scheme are a promising approach     

> __< emsczkp:matrix.org >__ as this result shows     

> __< rucknium >__ Could you explain section 6 of the paper, especially equation 10?     

> __< rucknium >__ And when does the asymptote kick in? :)     

> __< rucknium >__ I know usually you cannot really say when an asymptote kicks in, but I want to check how practical the performance improvement is.     

> __< rucknium >__ Or if the "small/negligible terms" would actually dominate in practical applications.     

> __< rucknium >__ Or if you don't know yet, that is ok.     

> __< emsczkp:matrix.org >__ yes this is an estimate of the resulting IVC verifier execution time, after the folding-to-IVC compilation (as pointed by ProtoStar), and exactily follows a TH of Protostar to show up these estimates     

> __< rucknium >__ I don't know how to interpret expression (10). Maybe in the future you could create a table with example numbers.     

> __< rucknium >__ With comparison to previous implementations.     

> __< emsczkp:matrix.org >__ certainly, concrete implemetation and evaluations are left as future work. but, is in the nature of folding to appreciate such improvements, and we can do such a theoretical enstimation, or otherwise the scheme will be trivial     

> __< jberman >__ IIUC the scheme requires knowledge of the witness to construct the folded proof, right? I.e. not anyone can take 100 random proofs constructed by others and fold them with this scheme     

> __< jberman >__ Requiring knowledge of the witness is what was orginally postulated / expected from BP* (e.g. to make it more efficient to verify huge input proofs), so that would be expected     

> __< jberman >__ to verify huge input txs*     

> __< emsczkp:matrix.org >__ jberman: what is folded are NARK proofs     

> __< emsczkp:matrix.org >__ jberman: do you mean a monolithic BP ?     

> __< emsczkp:matrix.org >__ ah no, you said BP*     

> __< jberman >__ so the idea behind BP* is to take n NARK proofs and fold them. Is my understanding incorrect in that the BP* scheme requires the original prover of the NARK proofs to construct the BP*, since the original prover has knowledge of the witness used to construct each NARK proof?     

> __< emsczkp:matrix.org >__ oh yes, the folding prover folds on the witness     

> __< emsczkp:matrix.org >__ oh my god no, sorry i'm bit tired     

> __< jberman >__ no worries :)     

> __< emsczkp:matrix.org >__ i mean, the secret witnesses of the arithmetic circuit preserve zero-knowledge     

> __< rucknium >__ emsczkp:matrix.org: The conversation can continue once you've had rest, if you want.     

> __< emsczkp:matrix.org >__ sure, thanks!     

> __< rucknium >__ 7. CCS proposal: I2P SAMv3 support (https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/650).     

> __< rucknium >__ This has been discussed at a few MRL meetings. More comments or questions for jpk68:matrix.org  ?     

> __< jpk68:matrix.org >__ Apologies for being late, I am here :)     

> __< ofrnxmr >__ imo SAMv3 is a perfectly sane endeavor, but i don't support adding more money via ccs, as there is much more xmr available at this bounty https://bounties.monero.social/posts/32/140-204m-i2p-baked-into-the-monero-gui     

> __< rucknium >__ jpk68:matrix.org: I think you're on time :)     

> __< jpk68:matrix.org >__ ofrnxmr: Not sure if you've seen it yet, but I responded directly to this, in a comment under the CCS     

> __< ofrnxmr >__ ofrnxmr: jpk responded to this concern on the ccs, but my stance remains the same: just claim the bounty     

> __< ofrnxmr >__ jpk68:matrix.org: I did :)     

> __< jpk68:matrix.org >__ As I said, this can hardly be considered a 'bounty' sort of job, considering it includes research, testing, several different milestones (which have to do with different tasks), etc.     

> __< jpk68:matrix.org >__ In my opinion, at least     

> __< ofrnxmr >__ Other attempts were incomplete or not reviewed favorably. If you're confident that youll complete the ccs, then the bounty should more than (3x) cover your troubles     

> __< jpk68:matrix.org >__ Dedicating several months' worth of effort to this without any sort of structured plan with milestones wouldn't be very ideal     

> __< jpk68:matrix.org >__ I could do this without the CCS, but it would take far longer as I can't really just commit to a bounty like that     

> __< jpk68:matrix.org >__ Also, I am not the only one that is confident about the proposal, it is endorsed by I2P devs as I stated before     

> __< rucknium >__ And bounties aren't "reserved" for anyone. It's first-complete, first-paid, within reason. CCS has a informal exclusivity period before the CCS can be completed by anyone.     

> __< ofrnxmr >__ they are, like me, in favor of the endeavor. I am not in favor of adding more money to this. Everodd or the other persons who have attempted thr bounty could have opened ccs's and we'd have just beem throwing money away     

> __< rucknium >__ "completed by anyone" = "completed by someone who is not the original proposer"     

> __< jpk68:matrix.org >__ Yes, as explained in my comment, I really want to make sure the proper approach is taken with this task     

> __< jpk68:matrix.org >__ ofrnxmr: I don't think anyone has attempted this with the actual plan to do this with SAM support in the daemon     

> __< jpk68:matrix.org >__ Besides the I2P devs' original CCS, of course     

> __< jpk68:matrix.org >__ Luigi suggested it could be taken up by someone else; I have taken up this offer     

> __< ofrnxmr >__ Essentially, what im saying is since this bounty is essentially dead, we should just earmark it for the ccs     

> __< jpk68:matrix.org >__ https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/454#note_25233     

> __< rucknium >__ AFAIK, there is no precedent for "transferring" XMR from bounties to the CCS. But it could be done in theory.     

> __< ofrnxmr >__ Not raise more money and still leave the bounty open     

> __< jpk68:matrix.org >__ Just to add, StormyCloud has already offered to fund the proposal (in full)     

> __< jpk68:matrix.org >__ It's a registered US nonprofit which sponsors the I2P project     

> __< ofrnxmr >__ jpk68:matrix.org: So why need the ccs? Just accept the funding directly     

> __< jpk68:matrix.org >__ Because it's a joint effort between both communities, and was directly suggested by Luigi     

> __< jpk68:matrix.org >__ Also, from a legal standpoint, a nonprofit sending a large amount of cryptocurrency directly to an anonymous developer would likely be extremely problematic     

> __< rucknium >__ You could also consider https://donate.magicgrants.org/monero/apply     

> __< rucknium >__ It would be nonprofit to nonprofit.     

> __< jpk68:matrix.org >__ That's possible, I suppose     

> __< rucknium >__ But MAGIC would require some KYC from you.     

> __< jpk68:matrix.org >__ Yes, my point exactly :)     

> __< jpk68:matrix.org >__ I don't really see why the CCS is a bad option here. Again, it was suggested by Luigi - has he gone back on his statement about this, or do others disagree with him?     

> __< ofrnxmr >__ The ccs is not a legal org or corp. Sending money to ccs is no diff than sending it to an anonymous stranger > <jpk68:matrix.org> Also, from a legal standpoint, a nonprofit sending a large amount of cryptocurrency directly to an anonymous developer would likely be extremely problematic     

> __< jpk68:matrix.org >__ I'm simply just curious     

> __< rucknium >__ We are thirty minutes past the hour. I will end the meeting here. Discussion can continue of course.     

> __< ofrnxmr >__ Thanks ruck     

> __< jpk68:matrix.org >__ ofrnxmr: I would have to disagree with this. StormyCloud sending money to the CCS or general fund can easily be seen as a donation to an open-source project, similar to how they themselves receive anonymous donations     

> __< plowsof >__ well the bounty will be changed to meet the the approved scope/method from the CCS as the alternatives are seemingly privacy foot guns e.g. temporary anonymity network usage . to secure funding jpk could be promised 33% as a reviewer whilst keeping within the bounties site ideals       

> __< jpk68:matrix.org >__ As the CCS/project is not a legal entity, as you have said, they do not need to do any KYC or complicated tax-related stuff     

> __< plowsof >__ promising of funding is not used to put things on the CCS, not a good precedent and promotes schemers and grifters      

> __< plowsof >__ the CCS has a 100% funding rate currently      

> __< jpk68:matrix.org >__ plowsof: What do you mean, as a reviewer? Reviewing others' submissions?     

> __< jpk68:matrix.org >__ I don't really understand your first sentence, sorry     

> __< plowsof >__ yes ' this submission is ai slop, im continuing with my own, when im finished ill claim the entire bounty or 50~ what i had asked for from the ccs to review/improve a genuine submission'     

> __< plowsof >__ people can send monero anon btw , also, i dont like the "luigi, has he gone back on his statement" what     

> __< jpk68:matrix.org >__ I'm simply asking why there's a disagreement. It's not supposed to be finger-pointing/innuendo     

> __< jpk68:matrix.org >__ It seems Luigi said he is in favour of a CCS being done for this, and others seem to disagree     

> __< jpk68:matrix.org >__ plowsof: Apologies again, I really don't understand what this means. Do you mean the CCS should be asked to review bounty submissions in this situation or something?     

> __< sgp_ >__ rucknium: Just echoing this. MAGIC Grants needs to know who we send money to. If that's all workable, then the proposal seems within our mission based on my skimming     

> __< CjS77 >__ Hey all, I've read through the convo on Grease -- thanks for the feedback; I think the sentiment on the value prop aligns with mine -- I'm not interested in creating a payment channel network; I 100% believe that there's enough utility in "simple" biparty channels. And as we went into the weeds on Monet, we found that even this is far from simple,     

> __< CjS77 >__ hence the quotes. On the topic of trustlessness on the KES; I have some ideas brewing, & I like working collaboratively. Is this group open to me posting (half-baked) ideas here to try  and iterate and throw out the doomed ideas? I'd still like to keep the KES *implementation* out of scope for this proposal, but if we know that trustlessness is     

> __< CjS77 >__ achievable on the KES, I would suggest that's good enough.     

> __< jeffro256 >__ CjS77: I have posted many a half-baked idea in #monero-research-lounge:monero.social ;)     

> __< jpk68:matrix.org >__ sgp_: I really appreciate your offer, thank you. I'll have to do some thinking about this, but my first thought is that it wouldn't be super feasible for me to do KYC right now     

> __< emsczkp:matrix.org >__ jberman: Just to not leave this unclear, the orginal NARK prover has knowledge of the (secret) witness. this should not be confused with the accumulator witness     

> __< jpk68:matrix.org >__ Okay, how about this: the bounty money can go wherever, it doesn't matter to me. I will just submit the CCS and that's all.     

> __< jpk68:matrix.org >__ If plowsof decides I should receive the bounty, that's fine, but if not, I don't care     

> __< CjS77 >__ jeffro256: Cool. erm, is that this room? (I'm going to have to get a proper IRC client methinks)     

> __< jpk68:matrix.org >__ What would be useful to me here is assurance I will be compensated, not the amount of money. The 50 XMR from the CCS is more than enough for me.     

> __< jpk68:matrix.org >__ Sorry for burying you messages, jeffro/CJ :)     

> __< jeffro256 >__ CjS77: Yes, it is a room. You can join over IRC on Libera, or over Matrix on monero.social      

> __< jberman >__ emsczkp:matrix.org: Does the accumulator (AFAIU this is the one "folding" the many proofs into one folded proof) need to have knowledge of the original NARK prover's secret witness?     

> __< CjS77 >__ jeffro256: #monero-research-lounge:monero.social is empty, so just checking that it's the right place     

> __< emsczkp:matrix.org >__ jberman: it depends on your design :)     

> __< emsczkp:matrix.org >__ application *     

> __< emsczkp:matrix.org >__ that said, i'm going to rest, we can continue offline     

> __< jpk68:matrix.org >__ I have updated my proposal with a statement regarding the bounty funds. If anyone is willing to provide feedback on this, that would be great. Thanks :)     

> __< rucknium >__ CjS77: #monero-research-lounge on Libera IRC network shouldn't be empty.     

> __< rucknium >__ Did you add the :monero.social suffix? Don't add it for IRC.     

> __< jeffro256 >__ rucknium: ^^^     

> __< jeffro256 >__ oops he left      

> __< plowsof >__ Rucknium ofrnxmr jpk68 do note this bounty: https://bounties.monero.social/posts/76/4-214m-research-overseer-attack-countermeasures     

> __< plowsof >__ also note distribution of bounty funds to reviewers/testers: https://github.com/monero-project/monero/pull/8619#issuecomment-3283393492     

> __< jpk68:matrix.org >__ Thanks. And again, the CCS can be funded by StormyCloud without any taken from the bounty     

> __< stormycloud:i2p.net >__ We would like to involve the community with a CCS. Since its a community effort.     



# Action History
- Created by: Rucknium | 2026-03-25T10:21:41+00:00
- Closed at: 2026-04-08T15:04:16+00:00
