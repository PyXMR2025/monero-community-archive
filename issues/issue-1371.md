---
title: Monero Research Lab Meeting - Wed 15 April 2026, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/1371
author: Rucknium
assignees: []
labels: []
created_at: '2026-04-14T21:22:11+00:00'
updated_at: '2026-04-29T14:45:02+00:00'
type: issue
status: closed
closed_at: '2026-04-29T14:45:02+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

Live log: https://libera.monerologs.net/monero-research-lab

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/meeting.html?p1=1440)

Main discussion topics:

1. Greetings

2. Updates. What is everyone working on?

3. [FCMP code integration audit overview](https://github.com/seraphis-migration/monero/issues/294). [CCS proposal](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/663).

4. [Increased FCMP++ membership proof size, marginally slower 1-input verification time](https://github.com/seraphis-migration/monero/issues/317).

5. [Proposal for FCMP++ HF Activation Rule to Retroactively Ignore Future `unlock_time`](https://github.com/monero-project/research-lab/issues/125).

6. [CCS proposal: ProbeLab P2P Network Metrics Proposal](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/667).

7. [CCS proposal: Grease Payment Channels](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/651).

8. [Discussion: Post-quantum security and ethical considerations over elliptic curve cryptography](https://github.com/monero-project/research-lab/issues/131). [Safeguarding cryptocurrency by disclosing quantum vulnerabilities responsibly](https://research.google/blog/safeguarding-cryptocurrency-by-disclosing-quantum-vulnerabilities-responsibly/ ).

9. [More Jamtis features in Carrot](https://github.com/seraphis-migration/monero/issues/310).

10. Any other business

Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: Rucknium

Previous meeting agenda/logs:

#1368 

# Discussion History
## Rucknium | 2026-04-21T21:21:40+00:00
Log

> __< rucknium >__ Meeting time! https://github.com/monero-project/meta/issues/1371     

> __< rucknium >__ 1. Greetings     

> __< plowsof >__ 👋     

> __< syntheticbird >__ Hi     

> __< articmine >__ Hi     

> __< tevador >__ Hi     

> __< vtnerd >__ Hi     

> __< jberman >__ waves     

> __< iamnew117:matrix.org >__ hello     

> __< rbrunner >__ Hello     

> __< jpk68:matrix.org >__ Hello     

> __< rucknium >__ 2. Updates. What is everyone working on?     

> __< tevador >__ Jamtis-PQ     

> __< jberman >__ me: using the latest FCMP++ lib changes, preparing for beta     

> __< rbrunner >__ Implementing Polyseed in the Monero core software     

> __< vtnerd >__ Me: testing lwsf /feed implementation via unit tests     

> __< jeffro256 >__ Howdy     

> __< rucknium >__ 3. FCMP code integration audit overview (https://github.com/seraphis-migration/monero/issues/294). CCS proposal (https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/663).     

> __< jberman >__ We're waiting on a quote from likely just 1 more firm, and have a good slate of candidates we're discussing. I think we should have a proposed candidate for discussion by next week's meeting, and will respect the rule aiming to post the candidate at least 24 hours in advance of the meeting     

> __< jberman >__ The CCS proposal itself is sitting at 2 likes, which makes me slightly uneasy about support for it, perhaps others have thoughts on that here     

> __< jberman >__ I presume people may have the thought this is "yet another round of FCMP++ audits" on top of the FCMP++ Research audit. Perhaps I can make it clear this is auditing the code I've been writing for the past 2 years     

> __< rucknium >__ Did previous hard forks have integration audits? I'm just curious. I think it's good if this is new with this hard fork, i.e. security precautions are ratcheting upward.     

> __< jberman >__ while the FCMP++ Research Audit was focused on the more math-focused side of the FCMP++ protocol and lib by kayabanerve:matrix.org     

> __< jeffro256 >__ rucknium: IIRC QuarksLab reviewed the BP code, but I could be wrong      

> __< sneedlewoods_xmr:matrix.org >__ jberman: I think it received more positive feedback last community meeting     

> __< jberman >__ rucknium: not that I'm aware of. IIRC I believe the BP+ protocol was audited, but I'm not sure if moneromoo's actual PR integrating it into consensus was audited     

> __< jberman >__ perhaps moneromooo / selsta have a better answer     

> __< jeffro256 >__ TBF, the FCMP++ integration contains a significantly higher amount of business logic touching crypto, that if done incorrectly, can lead to inflation bugs      

> __< rucknium >__ I thumbed-up the proposal now :)     

> __< tevador >__ FWIW, I have no objections to that CCS proposal.     

> __< rucknium >__ jeffro256: jeffro256:monero.social: Maybe this info could be added to the proposal so the stakes are known.     

> __< selsta >__ I don't think we had an audit of mooo's integration PR     

> __< rucknium >__ Thanks, selsta     

> __< rucknium >__ More discussion on this item?     

> __< jeffro256 >__ To be extraordinarily reductive, the integration code for RingCT was A) changing the tx format, B) adding new data to the DB to store amount commitments, and C) adding a table for RingCT-specific outputs, D) switching which crypto functions were used for verification. The FCMP++ integration does all of that plus includes Rust  [... too long, see https://mrelay.p2pool.observer/e/zIGZ3fkKSFNGNG90 ]     

> __< jeffro256 >__ I can add a more accessible blurb to that CCS today      

> __< rbrunner >__ Yes, please do that, will be very valuable     

> __< ofrnxmr >__ rucknium: #monero-community:monero.social workgroup is deferring to MRL as to when and whether it is merged     

> __< jberman >__ would be welcome, thank you jeffro256:monero.social 🙏     

> __< rucknium >__ 4. Increased FCMP++ membership proof size, marginally slower 1-input verification time (https://github.com/seraphis-migration/monero/issues/317).     

> __< jberman >__ Re-sharing: the GBP fix identified and proposed by Cypher Stack has increased FCMP++ tx sizes ~33% and 1-in verification times ~10%. Results and further thoughts are here: https://github.com/seraphis-migration/monero/issues/317     

> __< jberman >__ I'm in favor of moving forward with these new figures, and penciling in continued follow-up research into the 2nd alternative route shared there     

> __< rucknium >__ Can we consider the mathematics of the new protocol (+33% tx size) to be fully reviewed?     

> __< syntheticbird >__ 3 more months before FCMP++ HF     

> __< syntheticbird >__ unless this can be done in parallel     

> __< rucknium >__ I agree that it would be better to tolerate the larger tx size instead of opening the n'th can of worms by researching the 2nd alternative route, reviewing it, etc.     

> __< articmine >__ rucknium: It has a small impact on scaling     

> __< tevador >__ I also support going ahead with the new sizes, perhaps adjusting the reference tx size if needed.     

> __< jpk68:matrix.org >__ syntheticbird: Until the fork, or until its date is announced?     

> __< jberman >__ rucknium: No, kayabanerve:matrix.org has 2 follow-up questions posted here: https://github.com/cypherstack/generalized-bulletproofs-fix/issues , and has explicitly mentioned intent to do a round of deeper review     

> __< syntheticbird >__ jpk68:matrix.org: im just saying if we ask for another review on the result of a review, we're gonna have to wait on it too.     

> __< articmine >__ ... and likely on fees     

> __< tevador >__ Do we have a checklist of items that need to be completed before tagging the HF version?     

> __< jberman >__ Commit description here indicates kayabanerve:matrix.org 's blockers on it: https://github.com/monero-oxide/monero-oxide/commit/cba7117d2cb4a45444c54005604b2a943a8517f1     

> __< jberman >__ But kayabanerve:matrix.org also stated that such blockers are not worth blocking beta on, which I can discuss in the FCMP++ beta discussion     

> __< jberman >__ tevador: I'll update this checklist with tasks like "Complete all outstanding Research items", "Audit integration", "beta stressnet", etc.: https://github.com/seraphis-migration/monero/issues/53     

> __< jeffro256 >__ I feel like a 33% increase in tx size will affect beta scaling ...      

> __< tevador >__ jberman: thanks, I missed that issue     

> __< jberman >__ This was my initial take on scaling impact fwiw     

> __< jberman >__ The reference tx size was 10k, which still seems reasonably applicable, and the minimum penalty zone of 625kb was chosen with the size of large blocks in mind, rather than as a function of tx size IIRC. So I don't immediately see a reason to modify the fee structure     

> __< jberman >__ And faster increasing membership proof size as n inputs increases fits within the rationale for choosing weight to roughly follow byte size: https://github.com/seraphis-migration/monero/issues/44#issuecomment-3423391977     

> __< rucknium >__ jberman:monero.social: I replaced the beta streetnet agenda item with the item we are currently discussing. You can discuss beta stressnet now. > <jberman> But kayabanerve:matrix.org also stated that such blockers are not worth blocking beta on, which I can discuss in the FCMP++ beta discussion     

> __< articmine >__ We need to increase the transaction weights accordingly and also increase fees     

> __< jberman >__ Tx weights roughly follow byte size, they are increased as a result of this change     

> __< articmine >__ Which means a small fee increase      

> __< articmine >__ The reference tx weight would need to increase which in turn means an initial fee increase      

> __< jberman >__ is that the only change in mind?     

> __< jberman >__ it's currently 10k bytes     

> __< jberman >__ which is still larger than the new 2-in/2-out     

> __< jberman >__ or sorry, new 2-in/2-out is 10,425 bytes     

> __< tevador >__ yes, the reference size might need to be increased slightly     

> __< articmine >__ Vs ~8000 before      

> __< articmine >__ Bytes      

> __< jberman >__ Shall we make it 10.5k bytes to roughly match 2-in/2-out?     

> __< articmine >__ I am thinking ~ 12500 bytes      

> __< jberman >__ I'm ok with that     

> __< tevador >__ that's approx a +56% fee increase     

> __< articmine >__ Correct      

> __< tevador >__ sounds reasonable     

> __< rucknium >__ 5. Proposal for FCMP++ HF Activation Rule to Retroactively Ignore Future unlock_time (https://github.com/monero-project/research-lab/issues/125).     

> __< ofrnxmr >__ articmine: In whole numbers, i assume thats like ~0.00012 xmr for a 2in/2out tx?     

> __< jberman >__ hang on, before moving to this item, I think we should finish discussion on scaling / beta     

> __< rucknium >__ jberman:monero.social: Ok     

> __< tevador >__ I think the only constant in the code that needs to be changed is the reference tx size     

> __< jberman >__ sounds good to you ArticMine ?     

> __< articmine >__ Yes      

> __< jeffro256 >__ Okay then I will open the PR     

> __< jberman >__ on beta: I don't think kayabanerve:matrix.org will have availability to continue on the GBP item until EOM. in discussions, my take is kayaba seems to hold a view any further changes are not expected to fundamentally alter tx size or verification/prove time, and feels we should move forward with beta     

> __< rucknium >__ That sounds good to me     

> __< jeffro256 >__ Should we simply add 33% as an empty byte buffer to the beta txs to mimic bandwidth loads?     

> __< jeffro256 >__ Or whatever the actual change would be      

> __< jberman >__ I'm somewhat uneasy about it, in an ideal world I'd personally prefer to have this item completely settled before beta launch, but I think we're more likely to delay FCMP++ if we wait. The beta will be very useful no matter what, like the alpha was     

> __< rucknium >__ I misunderstood. The code for the new changes hasn't been written yet?     

> __< jberman >__ kayabanerve:matrix.org implemented the change already, it's just final task items remaining to sign off on it for production use essentially / slate it for auditing I believe     

> __< jberman >__ the benchmarks I posted are using the changes kayaba implemented     

> __< jberman >__ i.e. you understood correctly rucknium:monero.social     

> __< rucknium >__ Then the 33% empty byte buffer would be unnecessary?     

> __< jberman >__ yes, that would be unnecessary     

> __< jeffro256 >__ Ah okay, so we can use the actual code (or something ostensibly similar to final production version) in the beta stressnet branch?     

> __< jberman >__ yep     

> __< jeffro256 >__ If so, then I misunderstood, as I thought that the code wasn't done yet. Kayaba is just waiting for CS to sign off?     

> __< jberman >__ no kayaba is just busy with other work at the moment     

> __< jberman >__ I'm ok with moving forward with using the latest changes and launching beta     

> __< jeffro256 >__ Okay yeah, if it is complete (not necessarily sound) and will have similar performance characteristics, then I agree     

> __< jberman >__ ok, then I say let's have all beta code ready for next week's meeting, so we're prepared to announce beta then with release binaries etc.     

> __< jeffro256 >__ SGTM     

> __< rucknium >__ That would be great. Thank you.     

> __< rucknium >__ More discussion on this item?     

> __< jberman >__ nothing from me     

> __< rucknium >__ 5. Proposal for FCMP++ HF Activation Rule to Retroactively Ignore Future unlock_time (https://github.com/monero-project/research-lab/issues/125).     

> __< jberman >__ Firstly, we should have been on top of the May 1, 2025 date and announced it more formally, I apologize for that     

> __< jeffro256 >__ Me too, I thought that it had gotten more highly disseminated, but I guess not. I vaguely remember some people debating it on Reddit, but I can't find any actual evidence of that discussion happening      

> __< tevador >__ Is a getmonero.org blog post planned?     

> __< jberman >__ Going forward, I think we should double check volume of unlock times since we last checked, and if all looks good, I think we should set a new date relatively soonish (e.g. 6/1/26)      

> __< jeffro256 >__ tevador:  It should be     

> __< jberman >__ And then yes, make a blog post and announce     

> __< tevador >__ There shouldn't be many nonzero unlock_times due to the relay rule     

> __< jeffro256 >__ jberman: If the long-term unlocked outputs is still in the double digits, or even below say 200, then I would be fine resetting the date      

> __< rucknium >__ I can check the volume of those txs.     

> __< rbrunner >__ I also tried to find any discussion of this decision on Reddit, and failed. Found only discussions predating the decision.     

> __< jeffro256 >__ But because of the relay rule introduction, it also might not make much sense to reset the date      

> __< jberman >__ ya the relay rule is an implied rule to an extent such that I don't think it would be a major violation of the social contract to keep the 5/1/25 date     

> __< rucknium >__ https://gist.github.com/Rucknium/48dd80d52c26ab461035e4da5b1e5230     

> __< rucknium >__ > Below are all non-coinbase transactions with nonzero unlock time confirmed on the Monero blockchain between September 1, 2024 (height 3227566) and October 13, 2024 (height 3258526).     

> __< rucknium >__ > Version 0.18.3.4 of the Monero deamon, which prevents these transactions from entering the node's txpool, was released on August 22, 2024: https://github.com/monero-project/monero/releases/tag/v0.18.3.4     

> __< jbabb:cypherstack.com >__ is the intention to sunset unlock_times across the board entirely?     

> __< rucknium >__ That's the older data     

> __< rucknium >__ jbabb:cypherstack.com: Yes. Having custom unlock time would make FCMP code a lot more complicated.     

> __< jberman >__ jbabb:cypherstack.com: The plan already in place is to not allow custom unlock_time at consensus at the fork     

> __< tevador >__ most of the unlock times in rucknium's gist are invalid anyways     

> __< jeffro256 >__ rucknium: We have had multiple vulnerability fix releases since then, so hopefully those pools have updated in the last 1.5 years      

> __< jberman >__ The plan we're discussing now is to retroactively not respect any custom unlock_time created after x date once the fork happens      

> __< jberman >__ and x date would be a date before the fork     

> __< tevador >__ I think it's quite likely there have not been any unlock_time values with a future time at all since May 2025.     

> __< jberman >__ I agree, and in which case, I think we'd be ok with setting a soon-ish future date to avoid nagging complaints about "officially" announcing a date in the past     

> __< jbabb:cypherstack.com >__ my small comment is not in opposition but rather that I and a couple of others have been playing with atomic swap protocols which would benefit from unlock_time support but aren't blocked by its absence, just left to work with weaker refund path delay methods like VTSs     

> __< jbabb:cypherstack.com >__ better to solidify it at consensus imo rather than left to relay rules     

> __< rucknium >__ jbabb:cypherstack.com: Which protocols?     

> __< jbabb:cypherstack.com >__ toys at this point, nothing production ready anyways     

> __< jberman >__ if there is a complete protocol defined that would definitely benefit from the unlock_time that monero currently supports, it would be new/relevant info     

> __< tevador >__ AFAIK no production atomic swaps have used it. It's quite useless actually.     

> __< tevador >__ Who can prepare a getmonero.org blog post?     

> __< jberman >__ I or jeffro256:monero.social can handle it     

> __< jeffro256 >__ AFAIK the most useful time locks are ones which are specified in a signed input and conditional on some other condition like revealing a hash preimage. Monero's time locks are not that      

> __< rucknium >__ Maybe prep the blog post, extract the mainnet chain data (me), then finalize decision on the date next meeting?     

> __< jberman >__ jeffro256: right, so that one output can be spent before time x, and another after time x. DLSAG introduced that concept. no one has shown how to use monero's unlock_time to achieve that     

> __< tevador >__ rucknium: sounds good     

> __< rucknium >__ 6. CCS proposal: ProbeLab P2P Network Metrics Proposal (https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/667).     

> __< rucknium >__ ProbeLab has discussed their preliminary network scan results here previously.     

> __< rucknium >__ dennis_tra:matrix.org  and yiannisbot:matrix.org  aren't able to attend the meeting today, but they can respond to comments and questions later.     

> __< rucknium >__ The mainnet spy node situation has gotten worse. On March 31, about 900 new spy nodes appeared. That raised the percentage of nodes that are spy nodes from 47% to 55%. It looks like they appeared in a few Amazon-owned ASNs.     

> __< rucknium >__ This new deployment is more dangerous than previous ones because more of the nodes are scattered into their own subnets. The subnet deduplication countermeasure (https://github.com/monero-project/monero/pull/9939) is less effective against the new deployment. Maybe the adversary chose the deployment configuration to defeat the countermeasure or it may have been happenstance.     

> __< rucknium >__ That data is here: https://xmrnetscan.redteam.cash/ . Creating the ASN static treemap plot is triggering an error condition, so it's missing. The IP subnet treemap is available. You can click the interactive ASN treemap, but (warning) it may cause an error condition in your browser.     

> __< rucknium >__ Two issues I see with ProbeLab's proposal are 1) Mixing open source with a closed source backend and 2) Cost.     

> __< rucknium >__ The first part of their proposal is to publish an open source extension that hooks into their closed-source "generic" network analyzer that they have used with a lot of other chains. There is some precedent for funding data dashboards with closed-source backends, e.g. TxStreet (https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/217).     

> __< jeffro256 >__ > <rucknium> Maybe prep the blog post, extract the mainnet chain data (me), then finalize decision on the date next meeting?     

> __< jeffro256 >__ Rucknium: can you extract the running total of custom-locktime, currently unlocked at each block over time, please? That would be the most useful graph as it pertains to the wallet DoS vector. I made one here: https://github.com/monero-project/monero/pull/9522#issuecomment-2420662734     

> __< rucknium >__ Maybe ProbeLab could make sure that their open source implementation dumps all useful data to a minimally-structured file, so the open source portion is still useable even if not hooked into their closed source product.     

> __< rucknium >__ jeffro256:monero.social: Yes     

> __< jeffro256 >__ Sorry, this is the real graph: https://github.com/monero-project/monero/pull/9522#issuecomment-2420299652. The previous was FCMP++-tree-specific      

> __< syntheticbird >__ Regarding new deployment, I don't think even Cake Wallet is hosting a monero node on AWS. Recommending on banning Azure, Google and Amazon cloud ASN wouldn't be inappropriate     

> __< rucknium >__ I think the first milestone labor time and costs are reasonable. The second milestone is to collect data on unreachable nodes. I think the labor needed for that may be overestimated in the proposal. Perhaps ProbeLab can further break down the expected process for that milestone.     

> __< rucknium >__ syntheticbird:monero.social: Doing that would cut off any honest nodes using those services from the network     

> __< rucknium >__ I also want an estimate of infrastructure costs alone so it is known what the continued cost of running the monitor would be. The current proposal includes 6 months of monitoring.     

> __< rucknium >__ This proposal will be discussed next MRL meeting, too. ProbeLab people may be able to join the meeting then.     

> __< rucknium >__ 7. CCS proposal: Grease Payment Channels (https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/651).     

> __< rucknium >__ The proposers added info about possible KES (Key Exchange Service) options: https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/651#note_35871     

> __< jberman >__ The protocol still seems to rely on trust and doesn't have a particularly viable path to removing that trust AFAICT     

> __< rucknium >__ Step 2 says "Deploy the first production KES on the Secret network. We don't particularly like Intel SGX, but it's a relatively cheap deployment, is better than a purely centralized KES, and bridges the gap until..."     

> __< rucknium >__ I am not surprised they don't particularly like Intel SGX. It had a vulnerability that affected Secret: https://tee.fail/     

> __< jbabb:cypherstack.com >__ sorry to speak on something again without linking code again, but I'll report similarly re: unlock_times that I and a small group have been playing with grease (not in the context of swaps yet, tho) and it was remarkably easy to set up and use on stagenet.  I don't have any useful input re: a KES but I can report that the grea [... too long, see https://mrelay.p2pool.observer/e/oJ6v3_kKM09SNVct ]     

> __< rucknium >__ jbabb:cypherstack.com: Can you give info on where you see practical use cases for it?     

> __< jberman >__ I'd personally rather see a return to the drawing board here and a fleshed out protocol that does not rely on trust at any step     

> __< jbabb:cypherstack.com >__ rucknium:monero.social: not really, just in reducing tx fees for parties that already trust eachother and do regular business afaict atp     

> __< jberman >__ XMR would probably be better spent on ideating protocols that don't rely on trust than implementing trusted solutions imo     

> __< rbrunner >__ I tend to agree regarding trust, although it must of course be quite brutal for the authors of Grease if we ask them to "go back to the drawing board"     

> __< jberman >__ Yea, I don't know exactly how to sugarcoat my thoughts here     

> __< rucknium >__ Depositing credits to services is an old trust-based solution. It's used by a lot of service providers that accept cryptocurrency.     

> __< jberman >__ Ya, ecash     

> __< rbrunner >__ Yes, unfortunately you don't need complicated payment channels if regarding trust we could just ask somebody we trust to run a simple online database with balances ...     

> __< rbrunner >__ (Wildly simplified, of course.)     

> __< rucknium >__ The issue with depositing credits is that most (or all) of those services don't offer refunds from the deposit wallets. If they did, it would be like a cryptocurrency options contract. But payment channels would avoid that AFAIK.     

> __< jbabb:cypherstack.com >__ I hedge my statements as in "for parties that already trust eachother" due to not having had enough time to look into the conditions around closing a channel uncooperatively.  I report we used it and it worked, nothing more     

> __< rucknium >__ More discussion on this? I want to hit post-quantum and possible Jamtis/Carrot modifications. Sorry the meeting is long.     

> __< rbrunner >__ Wouldn't a centralized KES also be an easy point for any law enforcement agency to bring down?     

> __< jbabb:cypherstack.com >__ rbrunner: see samourai->ashigaru and paynym.is->paynym.rs; yes     

> __< rucknium >__ Would an adversary that takes control of the KES have to cooperate with at least one of the parties to steal or lock funds?     

> __< rucknium >__ One of the two parties in a channel     

> __< rucknium >__ 8.  Discussion: Post-quantum security and ethical considerations over elliptic curve cryptography (https://github.com/monero-project/research-lab/issues/131). Safeguarding cryptocurrency by disclosing quantum vulnerabilities responsibly (https://research.google/blog/safeguarding-cryptocurrency-by-disclosing-quantum-vulnerabilities-responsibly/).     

> __< jberman >__ rucknium: According to this that is the case: https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/651#note_34850     

> __< rucknium >__ Any discussion about post-quantum cryptography in this meeting? (Especially from tevador ?)     

> __< tevador >__ Here is the current draft of Jamtis-PQ: https://gist.github.com/tevador/639d083c994c1ef9401832c08e2b7832     

> __< tevador >__ The first comment lists 3 questions that need to be discussed before moving on.     

> __< tevador >__ I think the most important is the first question, which offers a trade off between privacy and post-quantum security.     

> __< rucknium >__ > Jamtis is backward compatible with the Carrot transaction protocol, requiring only 132 additional bytes per transaction in tx-extra. Jamtis addresses can coexist with CryptoNote addresses and the resulting transactions are indistinguishable in the blockchain.     

> __< rucknium >__ Does that mean that Carrot txs would have 132 bytes of random data in tx_extra?     

> __< tevador >__ Yes, that's the idea. When sending to a legacy address, the sender will insert a dummy PQ key.     

> __< tevador >__ I want to avoid the problem we had with subaddresses when inspecting tx_extra would leak information about recipients.     

> __< tevador >__ Regarding the unresolved issues, I'm currently leaning towards 1B and 3C.     

> __< rucknium >__ Thank you for the write-up, tevador.     

> __< rucknium >__ More discussion on this for now?     

> __< rucknium >__ 9.  More Jamtis features in Carrot (https://github.com/seraphis-migration/monero/issues/310).     

> __< jeffro256 >__ Unless there's been an update since last time, I don't have anything else to add      

> __< rucknium >__ We can end the meeting here. Thanks everyone.     

> __< tevador >__ Thanks.     

> __< jeffro256 >__ Thanks everyone      

> __< ofrnxmr >__ Thanx     

> __< jberman >__ tevador: I think it would be helpful to rationalize what impact a change from 2^73 to 2^61 T-gates actually means in practice and/or compare to recommendations / standards out there     

> __< jberman >__ 1B does seem more desirable though     

> __< tevador >__ Assuming a fast quantum computer (superconducting qubits), 2^61 is about 5000 years, 2^73 is millions of years.     

> __< tevador >__ Some details are in Appendix B including references to papers.     

> __< jberman >__ According to ref paper 25, CSIDH-512 is in NIST's PQ security category 1, which is  "Any attack that breaks the relevant security definition must require computational resources comparable to or greater than those required for key search on a block cipher with a 128-bit key (e.g. AES128)"     

> __< jberman >__ And then security category 2 is: "Any attack that breaks the relevant security definition must require computational resources comparable to or greater than those required for collision search on a 256-bit hash function (e.g. SHA256/ SHA3-256)"     

> __< jberman >__ https://csrc.nist.gov/projects/post-quantum-cryptography/post-quantum-cryptography-standardization/evaluation-criteria/security-(evaluation-criteria)     

> __< jberman >__ so based on that rec, "level 1" security sounds ok for encryption, but not collision resistance to have something comparable to 128 bit security? I'm not entirely sure how to interpret that     

> __< jberman >__ seems it would be used for encryption only in this proposal, which seems to line up with expected comparable to 128 bit security     

> __< tevador >__ CSIDH-512 was initially thought to be in NIST category 1, but it was later shown to fall short of that category.     

> __< tevador >__ NIST category 1 is from 2^80 T-gates, so both CSIDH-512 and CSIDH-1024 fall short. But that doesn't mean they are insecure.     

> __< tevador >__ For comparison, Curve25519 is about 2^26 T-gates, so the difference is at least a factor of 2^35 if we ignore the much higher memory cost of CSIDH (~1 million qubits compared to ~1200 for Curve25519).     

> __< jberman >__ ack     

> __< nioc >__ FCMP++ Integration Audit CCS has been moved to funding require   https://ccs.getmonero.org/proposals/fcmp++-integration-audit.html     

> __< moneromooo >__ I agree with selsta that I do not think my integration PR was audited. It was certainly well reviewed though.     




# Action History
- Created by: Rucknium | 2026-04-14T21:22:11+00:00
- Closed at: 2026-04-29T14:45:02+00:00
