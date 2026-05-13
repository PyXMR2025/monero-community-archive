---
title: Monero Research Lab Meeting - Wed 29 April 2026, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/1380
author: Rucknium
assignees: []
labels: []
created_at: '2026-04-29T14:48:18+00:00'
updated_at: '2026-05-13T14:28:02+00:00'
type: issue
status: closed
closed_at: '2026-05-13T14:28:02+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

Live log: https://libera.monerologs.net/monero-research-lab

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/meeting.html?p1=1440)

Main discussion topics:

1. Greetings

2. Updates. What is everyone working on?

3. [FCMP code integration audit overview](https://github.com/seraphis-migration/monero/issues/294). [CCS proposal](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/663). [Auditor quotes](https://github.com/seraphis-migration/monero/issues/294#issuecomment-4291345141).

4. [Post-quantum encryption](https://github.com/monero-project/research-lab/issues/151#issuecomment-4281932714).

5. [FCMP beta stressnet](https://github.com/seraphis-migration/monero/releases/).

6. [CCS proposal: ProbeLab P2P Network Metrics Proposal](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/667).

7. [CCS proposal: Grease Payment Channels](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/651).

8. Any other business

Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: Rucknium

Previous meeting agenda/logs:

#1377 

# Discussion History
## Rucknium | 2026-05-06T14:38:22+00:00
Log:

> __< sgp_ >__ I have a conflict during the meeting, but:     

> __< sgp_ >__ The FCMP++ 1a/1b audit process has kicked off.     

> __< sgp_ >__ I have a call to discuss GBPs with zksec tomorrow. I hope to move forward with that quickly, with a goal of final approval during next week's meeting.[... more lines follow, see https://mrelay.p2pool.observer/e/2_X5nP4KSnVpWU1u ]     

> __< sgp_ >__ For FCMP++ 1a/1b, we ended up going with vendor 1 instead of 4 due to scheduling. Both are good choices, but vendor 1 will deliver 2 months sooner     

> __< rucknium >__ Meeting time! https://github.com/monero-project/meta/issues/1380     

> __< rucknium >__ 1. Greetings     

> __< vtnerd >__ Hi     

> __< jberman >__ waves     

> __< tevador >__ Hi     

> __< koe000:matrix.org >__ Hi     

> __< jpk68:matrix.org >__ Hello     

> __< rbrunner >__ Hello     

> __< gingeropolous >__ hi     

> __< syntheticbird >__ Hi     

> __< rucknium >__ 2. Updates. What is everyone working on?     

> __< tevador >__ me: PQ encryption for Jamtis     

> __< gingeropolous >__ monerosim. trying to optimize, see how quickly i can do a 48 hr sim. making sure its nice and shiny     

> __< articmine >__ Hi     

> __< yiannisbot:matrix.org >__ Hi everyone!      

> __< vtnerd >__ me: doing monerod reviews and in the process of taking over swansontec’s  mempool scanning PR for LWS. Hoping to get that in before branching on a 1.0 release     

> __< jpk68:matrix.org >__ Working on the I2P SAM CCS proposal     

> __< articmine >__ I updated the scaling definitions for the new 12500 bytes reference transaction weight      

> __< jeffro256 >__ howdy      

> __< jberman >__ me: beta stressnet launched (now helping debug there)! Moving forwards with Phase 1 of Integration audit. Various PR's in prep for monerod release v0.18     

> __< rucknium >__ 3. FCMP code integration audit overview (https://github.com/seraphis-migration/monero/issues/294). CCS proposal (https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/663). Auditor quotes (https://github.com/seraphis-migration/monero/issues/294#issuecomment-4291345141).     

> __< rucknium >__ sgp_:monero.social gave an update before the meeting     

> __< tevador >__ Who is Vendor 1?     

> __< jberman >__ Vendor 1 is Trail of Bits     

> __< rucknium >__ > The FCMP++ 1a/1b audit process has kicked off.     

> __< rucknium >__ > I have a call to discuss GBPs with zksec tomorrow. I hope to move forward with that quickly, with a goal of final approval during next week's meeting.     

> __< rucknium >__ > The divisors paper from zksec suggested small fixes and we're looking at those, but we don't expect these to require actual changes in the code.     

> __< rucknium >__ > A helioseleine secondary audit will be prudent. I need to write up what makes the most sense for that. Some stuff was formally proven, but other stuff wasn't and needs manual review     

> __< jeffro256 >__ me: fixing stuff on master and attempting to fix stuff on beta stressnet. Reworking old FCMP++ PRs. Trying to have hot/cold wallets and wallet knowledge proofs done by next beta release      

> __< rucknium >__ > For FCMP++ 1a/1b, we ended up going with vendor 1 instead of 4 due to scheduling. Both are good choices, but vendor 1 will deliver 2 months sooner     

> __< jberman >__ The specific candidates Trail of Bits (ToB) shared who would work on the integration audit had direct relevant experience on cryptography theory and impl review, as well as with Rust FFI's     

> __< jeffro256 >__ ToB can allegedly start working May th      

> __< jeffro256 >__ 4th     

> __< jberman >__ May 11th*     

> __< articmine >__ ..and expected completion      

> __< jberman >__ With expected completion date of May 22nd     

> __< jeffro256 >__ Did they change it?     

> __< jberman >__ They want to use next week to prepare and plan with us, and then actually begin the 11th      

> __< jeffro256 >__ Understood      

> __< tevador >__ I have a comment about the future audit of mx25519: Since Carrot doesn't use the scalar inversion code, it could be removed from the library to simplify the audit. Pinging jeffro256 to confirm.     

> __< jeffro256 >__ Yes, Carrot doesn't ever use the scalar inversion code      

> __< jeffro256 >__ Although, wouldn't Jamtis still use it for the Janus check?      

> __< tevador >__ Yes, Jamtis will use it, but I'll have to check if your changes in the library are compatible.     

> __< tevador >__ It might be better to leave it for a future Jamtis audit.     

> __< jeffro256 >__ That's totally fair. It could definitely be excluded from an audit scope      

> __< rucknium >__ More on this topic?     

> __< rucknium >__ 4. Post-quantum encryption (https://github.com/monero-project/research-lab/issues/151#issuecomment-4281932714).     

> __< tevador >__ I decided to cap Jamtis address length at 420 characters for usability reasons (the maximum that can fit in one IRC message). For the PQ encryption options A/B/C, I'm now listing the largest CSIDH size that can fit in this limit (AC1152, BC704 and CC832). I personally think AC1152 (or AC1024) is the best choice, but I'm ready to hear arguments.     

> __< tevador >__ I also added LWS privacy to the details table     

> __< koe000:matrix.org >__ It may be more efficient to review the inversion now instead of later, since the auditor will already be in the mindset. Separating means paying for an auditor to set up that mindset twice.     

> __< tevador >__ koe000: the inversion code is completely separate from the ladder code, it should have been two libraries instead of one     

> __< tevador >__ On topic: I'm now running a search for CSIDH-832 parameters for option C. Option B doesn't seem very appealing to me.     

> __< tevador >__ Does anyone have any comments? Option A/C preference?     

> __< jberman >__ I haven't had time to focus on it     

> __< vtnerd >__ Yeah I've read it, but haven't thought about all the ramifications. My fault for not prepping for the meeting     

> __< vtnerd >__ C seems like the most logical from end users perspective, but I'm not sure of the rough perf numbers     

> __< tevador >__ Rough perf numbers for C are in the table.     

> __< tevador >__ For CC832 specifically, it's about 3h to scan 100k enotes using 1 CPU core.     

> __< jeffro256 >__ Option A is unacceptable me still. If we are going to seriously discuss PQ privacy, we can't change the bar to what we currently have with RingCT (assuming QA has addresses now, and QA didn't have addresses then)     

> __< jeffro256 >__ *to me     

> __< jeffro256 >__ Option C is obviously preferable, but that 2x slowdown is rough with some of these algorithms      

> __< tevador >__ It's more like 1000x slowdown.     

> __< tevador >__ But may still be acceptable and people who can't accept it can use LWS.     

> __< jeffro256 >__ Sorry, 2x bandwidth burden, 1000x CPU-side slowdown      

> __< rbrunner >__ Could that force *all* smartphone wallet apps into using LWS?     

> __< tevador >__ With option C, scanning on a smartphone would be almost impossible.     

> __< jeffro256 >__ Maybe. I wonder if one of these algorithms become popular and/or standardized, whether hardware will include acceleration for those ops like with AES      

> __< tevador >__ jeffro256: Option A is meant as an emergency back stop for the PQ scenario, while focusing on classical usability. Option C is the PQ pessimistic choice.     

> __< rucknium >__ Depending on who hosts the LWS, using LWS could be a greater privacy risk than using the status quo quantum-vulnerable addresses.     

> __< jeffro256 >__ The PQ security column is not very confidence inspiring for any of the algorithms whose address fit into an IRC message. In my mind, 2^60 is very achievable for a well funded adversary today, especially one who is willing to invest in ASICs. And unlike our PoW algo, we can't rug pull the ASIC maker once the key material is out in the wild      

> __< vtnerd >__ Yeah damn, I did see these rough numbers elsewhere, C is brutal     

> __< jeffro256 >__ Could be wrong about the feasabiity though      

> __< tevador >__ 2^60 quantum work is unachievable even if Curve25519 is broken, 2^60 classical work is achievable today     

> __< articmine >__ tevador: So we move to a home server phone client model     

> __< jeffro256 >__ I'm going to have to take your word on that one ;) Good to hear though. I have no ballpark in my head for how hard 2^60 quantum work is     

> __< jeffro256 >__ Is there a NIST recommendation for quantum work security thresholds?     

> __< rucknium >__ But wouldn't a multi-user LWS instance get overwhelmed too?     

> __< tevador >__ I listed some papers in the github issue, so you don't need to take my word for it. Beaking Curve25519 is around 2^26 quantum work.     

> __< rucknium >__ Can they do many of the operations in batches to reduce the load?     

> __< jeffro256 >__ Okay, thanks I'll look into those      

> __< vtnerd >__ rucknium: the number of accounts is certainly lowered bigtime     

> __< articmine >__ rucknium: They may which is why I am suggesting a home server model     

> __< jeffro256 >__ vtnerd could you expand on that plz?     

> __< tevador >__ For CC832, an AVX512 52-bit limb batched implementation would work.     

> __< jberman >__ If we were to push for the home server model as the expected core use case, then aiming to eliminate the key exchange protocol from the chain would be the more compelling route     

> __< jberman >__ I think we should very strongly aim to avoid that, and apologies I don't have a more helpful take on deciding among the options     

> __< vtnerd >__ I just meant that you need more CPU for the same number of accounts. So like edge wallet may need more servers for the processing, etc      

> __< tevador >__ Should we explore the route of interactive payments? But I think payments to offline addresses can't be completely removed.     

> __< jeffro256 >__ To piggyback off what jberman said, if we assume liveness of the receiver, we can get PQ security today with 0 PQ-specific cryptography, just symmetric encryption      

> __< articmine >__ tevador: Yes     

> __< jberman >__ this is also the route that Zcash's Tachyon is taking AFAIU     

> __< jeffro256 >__ I also am a fan of interactive payments, but the discussion is mostly orthogonal in my opinion. We can, and probably should, support both.      

> __< vtnerd >__ Yikes. The non-interactive part is a killer feature      

> __< jberman >__ I agree with vtnerd     

> __< tevador >__ vtnerd: you mean interactive?     

> __< rbrunner >__ But well, it looks like we may have to take on a killer burden to make that feature possible ...     

> __< jeffro256 >__ jberman: One can still have interactive payments, but use the L1 as a data availability layer for seed restoring. IIRC, Tachyon is more or less removing support for restoring from seed      

> __< jeffro256 >__ At least from the L1     

> __< jeffro256 >__ Could be wrong, there's a lot of developments happening over there      

> __< vtnerd >__ No I meant the offline addresses are huge feature, as the online approach complicates UX     

> __< tevador >__ Also Zcash is tackling the address length issue by having some sort of address registration service.     

> __< rbrunner >__ Worst-case scenario we go for 1000 times slower scanning, 400 byte addresses, big-sized transactions, and then it turns out quantum computers are not really feasible ..     

> __< vtnerd >__ And if the home server is down, nothing gets processed. I think this hurt all the mimblewimble chains, although it's tough to know why certain tech never took hold     

> __< quadriocellata:matrix.org >__ vtnerd: Offline addresses and ability to sync to remote nodes either on device, or worst case external lws. Not just a phone home approach bc UX would be a lot worse imo      

> __< articmine >__ I must disclose that I have a 50% interest in the Monero Nodo project, now Polymathy,and home servers is something we may move into      

> __< rbrunner >__ Good luck with home servers pretty much over the whole so-called "third world" ...     

> __< rucknium >__ More on this topic for now?     

> __< tevador >__ I'll have a look at online transactions, but Jamtis has other improvements over legacy addresses. It would be a loss not to release it.     

> __< jeffro256 >__ Absolutely. I'm not advocating for dropping support for offline addresses (for the moment) , but IMO it would be a loss to not look into online addressing protocols for the sake of PQ security     

> __< diego:cypherstack.com >__ hi can I speak on the audit thing?     

> __< diego:cypherstack.com >__ I can do so after the meeting     

> __< rucknium >__ diego:cypherstack.com: Yes     

> __< jberman >__ I am somewhat warming up to Option A in that it's a step towards stronger quantum protection without a major loss in UX, while the quantum field continues to advance (and hopefully develops more optimal provably secure algos)     

> __< tevador >__ jberman: Yes, considering that legacy addresses offer ZERO post-quantum protection, Option A is an improvement.     

> __< jberman >__ specifically AC1024 & AC1152     

> __< jeffro256 >__ Well not zero, it's 2^26 ;)     

> __< diego:cypherstack.com >__ Cypher Stack is doing a code review too. We weren't chosen for the money, but it doesn't matter. We started weeks ago. You should still go with the other group too btw.     

> __< rucknium >__ Thank you, diego:cypherstack.com     

> __< diego:cypherstack.com >__ Welcome. Should be done in a few weeks. Big progress on it already.     

> __< diego:cypherstack.com >__ also going to lol lmao at the divisors zk-security thing but I'll do that in Lounge     

> __< diego:cypherstack.com >__ anyways, sorry to interrupt     

> __< rucknium >__ Anything more about post-quantum addresses for now?     

> __< rucknium >__ 5. FCMP beta stressnet (https://github.com/seraphis-migration/monero/releases/).     

> __< jberman >__ We have lift off! v1.0 is released: https://github.com/seraphis-migration/monero/releases     

> __< jeffro256 >__ Already found some issues with the wallet ;) debugging them as we speak      

> __< jeffro256 >__ Specifically, users in the stressnet channel found them     

> __< rucknium >__ Daily discussion of stressnet is in the room #monero-stressnet:monero.social  ( ##monero-stressnet on IRC, IIRC).     

> __< jberman >__ We're squashing a restore bug at the moment for older wallets. Some hiccups are expected. We're definitely hoping that it'll be a smoother experience overall than alpha, considering the very wide slate of bugs squashed during alpha     

> __< jberman >__ The FCMP++ & Carrot fork is targeted for next week (May 6th)     

> __< rucknium >__ AFAIK, most bugs in my xmrspammer were squashed in testing on alpha stressnet: https://github.com/Rucknium/xmrspammer . Don't spam before beta stressnet actually forks off. One last thing is the excessive RAM consumption when the spammer has been running for a long time. I will try some fixes, starting with gc()  :D     

> __< rucknium >__ More on beta stressnet?     

> __< rucknium >__ 6. CCS proposal: ProbeLab P2P Network Metrics Proposal (https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/667).     

> __< rucknium >__ Is yiannisbot:matrix.org  here?     

> __< yiannisbot:matrix.org >__ Yup, hi!     

> __< rucknium >__ The CCS proposal website is temporarily down. I don't know when it may return.     

> __< yiannisbot:matrix.org >__ Hmm.. bummer     

> __< rucknium >__ yiannisbot:matrix.org gave comments last week after the meeting: https://libera.monerologs.net/monero-research-lab/20260423#c669972-c669974     

> __< yiannisbot:matrix.org >__ Just as a reminder, we have proposed last week that we use an alternative license, which keeps things open source. Let me give a couple of links      

> __< yiannisbot:matrix.org >__ We've seen the comments, yes, thanks for the feedback.     

> __< yiannisbot:matrix.org >__ This is the license that we've proposed: https://polyformproject.org/licenses/noncommercial/1.0.0/ - but of course, we're happy discuss, hear any concerns and negotiate.      

> __< rucknium >__ Technically, Polyform is not open source. It is a type of source-available license I think: https://polyformproject.org/about     

> __< yiannisbot:matrix.org >__ Here's the message from further up with some more thoughts: https://matrix.to/#/!toFcRZtpaiwiyapgVO:matrix.org/$aRrAibkCmihlY0aI1R6PmtWHPcFrrXc15YYAYSU3UkI?via=matrix.org&via=monero.social&via=unredacted.org     

> __< rucknium >__ > PolyForm is not…Open source or free software. There are plenty of existing open source licenses. PolyForm is not a substitute for them, but an alternative for those who want to license source code under limited rights.     

> __< jeffro256 >__ yiannisbot:matrix.org: 404 link      

> __< yiannisbot:matrix.org >__ I see. So, IIUC, this is not acceptable, or seen favourably by the community?      

> __< rucknium >__ Did you see kayabanerve:matrix.org 's comment on it? https://libera.monerologs.net/monero-research-lab/20260423#c670008     

> __< vtnerd >__ jeffro256:monero.social: remove last slash     

> __< rucknium >__ > Note: The proposed license above is not FOSS. That isn't to say I'm against its usage or reasoning for it, but I want to clarify that if there's a requirement for FOSS (e.g. by the CCS), that is insufficient unless an exception is granted (however that would happen).     

> __< rucknium >__ > It wasn't claimed to be FOSS, I just want to be clear it doesn't check the "FOSS" box in case that matters as some people may not immediately understand that.     

> __< articmine >__ yiannisbot:matrix.org: This may well depend on the intended use case by members of the Monero community     

> __< yiannisbot:matrix.org >__ What would be the preferred license?      

> __< plowsof:matrix.org >__ not a good fit for the CCS no, you could try to debate the rule "All work must be licensed permissively at all stages of the proposal. There is no time where your work can be licensed under a restrictive license (even as you're working on it). Your proposal will be terminated if this is not remedied." but i doubt it would swing opinions enough to have your proposal merged      

> __< rucknium >__ You said the reason you didn't like AGPL is because "On AGPL specifically: AGPL covers the code itself but leaves a gap for commercial use of the data that’s collected. PolyForm Noncommercial is a cleaner boundary for our situation, which we believe covers both sides."     

> __< rucknium >__ AFAIK, usually CCS-funded code is MIT or GPL.     

> __< articmine >__ The best model I see to allow the developer to sell proprietary software while maintaining FLOSS compatibility is the AGPL.v3.0 with  customized permissions      

> __< rucknium >__ I suggested AGPL because it specifically would require anyone running the code even if behind a server, like your competitors, to contribute back to the code.     

> __< yiannisbot:matrix.org >__ Yeah, I understand the concerns. Would AGPL v3.0 be fine by the community? We would be ok to go with this in fact.      

> __< articmine >__ For example one can restrict an AGPL permission to Non Commercial      

> __< rucknium >__ yiannisbot:matrix.org: yiannisbot:matrix.org: I think AGPL v3.0 would be OK with the community for the license. (There are other parts of your proposal that the community may disagree with, but the license should be ok.)     

> __< rucknium >__ plowsof:matrix.org: Could you comment on using an AGPL license?     

> __< yiannisbot:matrix.org >__ Should we decide that we go with AGPL v3.0 and discuss other parts?      

> __< rucknium >__ Yes we can discuss other parts now. I don't see more discussion about license for now     

> __< rucknium >__ IIRC, sgp_:monero.social  said on the CCS website that he preferred ProbeLab working on the part network privacy issues instead of a dashboard. It's unfortunate that the CCS website is down. We cannot see the proposal and comments now,     

> __< rucknium >__ And dennis_tra:matrix.org  from ProbeLab added some comments in the CCS website.     

> __< yiannisbot:matrix.org >__ I think Dennis's comments were mostly on the license part. But I can't remember exactly.      

> __< rucknium >__ Sorry, it's hard to discuss the proposal with the website being down. I don't see more discussion on it during this meeting. We will come back to it once we can see the proposal again.     

> __< yiannisbot:matrix.org >__ Yes, fair enough. So should the discussion continue in the repo, or in the next meeting? What's the suggestion?      

> __< plowsof >__ originally, cuprate was AGPL (syntheticbird / boog900 can confirm the details) but the community was pushing for MIT - the compromise for CCS funded work was MIT licensing on binaries?     

> __< jpk68:matrix.org >__ Pretty sure Cuprate is AGPL binaries and MIT libraries     

> __< rucknium >__ plowsof: That wasn't a hard rule, was it? Just a community preference IIRC.     

> __< sgp_ >__ my main comment is that I don't think we really need a dashboard, I think we need research on how dandelion++ works in an adversarial environment, with the presence of a community ban list that X% of honest nodes use and is Y% effective at fingerprinting adversarial nodes     

> __< plowsof >__ no not a hard rule     

> __< moneromooo >__ rucknium: gitlab (and thus the ccs) is down due to lak of disk space, and will stay down until more disk is added. I've mentioned this in the core chat, no idea who reads it when though.     

> __< rucknium >__ moneromooo: Thank you!     

> __< boog900 >__ plowsof: kinda: https://github.com/Cuprate/cuprate/issues/26#issuecomment-1924894292      

> __< boog900 >__ the final binary is AGPL with the libs that can be used by others MIT     

> __< boog900 >__ most of our code is MIT      

> __< rucknium >__ sgp_:monero.social: Maybe this in "my doing". I suggested that ProbeLab start with monitoring to get trust and then after that to research the bigger questions.     

> __< yiannisbot:matrix.org >__ sgp_: Agreed. We've been diving into Dandelion++ and want to do a study on this. But IMO, these are two separate things. The current CCS proposal is for a dashboard and a study on Spy nodes, which will ultimately pave the way for a Dandelion++ study     

> __< sgp_ >__ I personally see the dashboard as more of an ongoing cost than a benefit tbh     

> __< sgp_ >__ like, what would we use it for any why do we need it     

> __< jpk68:matrix.org >__ Rucknium has already made a similar dashboard, right?     

> __< rucknium >__ https://xmrnetscan.redteam.cash/     

> __< rucknium >__ The code I have runs much slower than what ProbeLab claims to have. My code (written with boog900:monero.social  ) may start to hit the 24-hour daily scan limit.     

> __< rucknium >__ My code is less robust and was missing data for a while.     

> __< rucknium >__ And the ProbeLab monitoring includes monitoring on unreachable nodes, which mine does not.     

> __< yiannisbot:matrix.org >__ The dashboard can be valuable for several things. Most importantly I would say if alerts are integrated. For instance, rapid change/shift of node geolocation could be a sign of an attack.      

> __< articmine >__ It seems to me that this kind of dashboard would be useful for members of the community to spy and analyze the spy nodes.     

> __< articmine >__ This will also help bring attention to this issue      

> __< rucknium >__ We need to move to the final agenda item soon. It's the Grease proposal.     

> __< rucknium >__ 7. CCS proposal: Grease Payment Channels (https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/651).     

> __< rucknium >__ CjS77 and kayabanerve:matrix.org  discussed Grease in #monero-research-lounge:monero.social  recently: https://libera.monerologs.net/monero-research-lounge/20260427 https://libera.monerologs.net/monero-research-lounge/20260428     

> __< rucknium >__ I think the summary is that CjS77 suggested a trustless Key Escrow Service (KES) method, but kayabaNerve thought it was not feasible in the near-term.     

> __< yiannisbot:matrix.org >__ Fair enough, should we continue the discussion in the lounge, or the repo? Or next meeting?  > <rucknium> We need to move to the final agenda item soon. It's the Grease proposal.     

> __< ixr3:matrix.org >__ rucknium: Cancel that proposal     

> __< rucknium >__ yiannisbot:matrix.org: I think all three is good. Getting input from more people would be good. For example, I don't think boog900:monero.social  has put in an opinion, but I could have missed it.     

> __< rucknium >__ More comments on Grease?     

> __< rucknium >__ We can end the meeting here. Thanks everyone.     

> __< articmine >__ Thanks      

> __< quadriocellata:matrix.org >__ thanks     

> __< jpk68:matrix.org >__ Thanks :)     

> __< quadriocellata:matrix.org >__ articmine:monero.social: I sent you a dm if you have a couple minutes     

> __< jberman >__ tevador: is there possibly an advantage of CSIDH-1024 versus CSIDH-1152 beyond the obvious figures in the table? e.g. potentially wider support / optimized impls out in the wild?     



# Action History
- Created by: Rucknium | 2026-04-29T14:48:18+00:00
- Closed at: 2026-05-13T14:28:02+00:00
