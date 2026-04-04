---
title: Monero Research Lab Meeting - Wed 07 January 2026, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/1321
author: Rucknium
assignees: []
labels: []
created_at: '2026-01-06T22:34:02+00:00'
updated_at: '2026-01-20T23:11:27+00:00'
type: issue
status: closed
closed_at: '2026-01-20T23:11:27+00:00'
---

# Original Description

Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/meeting.html?p1=1440)

Main discussion topics:

1. Greetings

2. Updates. What is everyone working on?

3. [Spy nodes](https://github.com/monero-project/meta/issues/1124).

4. [FCMP alpha stressnet](https://monero.town/post/6763165).

5. Any other business

Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: Rucknium

Previous meeting agenda/logs:

#1318 

# Discussion History
## Rucknium | 2026-01-12T22:34:35+00:00
Log

> __< rucknium >__ Meeting time! https://github.com/monero-project/meta/issues/1321     

> __< rucknium >__ 1. Greetings     

> __< vtnerd >__ hi     

> __< rbrunner >__ Hello     

> __< gingeropolous >__ howdy     

> __< plowsof >__ 👋     

> __< rucknium >__ 2. Updates. What is everyone working on?     

> __< rucknium >__ me: Fixed the database lock issue for the Monero net scanner. Revising the webapp (Not linking to it now since it has a big error message :D )     

> __< vtnerd >__ me: re-worked the lwsf<->lws<->monerod protocols for fcmp++ tree building. still works! currently looking into a bug about 0-conf reporting and fcmp++     

> __< gingeropolous >__ me: working on monerosim. claude code is wow. might have just one-shotted the whole mining shim thing. although i got the generate blocks one working great as well, doesn't require any monero mods. waiting on MRC resources freeing up to test 1000 node scale up. can currently get 85 agents on 32GB ram. nodes sync, txs generate and relay, included in blocks.     

> __< articmine >__ Hi     

> __< jbabb:cypherstack.com >__ knee-deep in reviewing the carrot impl     

> __< DataHoarder >__ implemented carrot tx proofs (generate, verify) on my libraries, doing some benchmarks on RandomX V2     

> __< rucknium >__ 3. Spy nodes (https://github.com/monero-project/meta/issues/1124).     

> __< rucknium >__ I had planned to have the spy nodes webapp revised by now, but I'm getting an unexpected launch error on the server at the moment.     

> __< rucknium >__ The network scanner seems to be working well again after I switched to a different Rust crate for connected with SQLite databases. It allows specifying a longer connection timeout so the database doesn't appear fatally locked to the tokio threads.     

> __< rucknium >__ For finalizing the new ban list, we need to have the original signers, at least, sign it. IIRC, SethForPrivacy's Docker image requires that the signatures are valid.     

> __< rucknium >__ The signers would be boog900:monero.social , syntheticbird:monero.social , jeffro256:monero.social , and myself.     

> __< rucknium >__ I usually don't like to do announcements on Friday or Monday. So we could aim to announce tomorrow or next on Tuesday.     

> __< rucknium >__ We would want to hit Reddit, monero.town, Twitter at least with the announcement.     

> __< rucknium >__ And the GitHub issue     

> __< gingeropolous >__ +1     

> __< rucknium >__ Anything more on spy nodes?     

> __< rucknium >__ 4. FCMP alpha stressnet (https://monero.town/post/6763165).     

> __< rucknium >__ gingeropolous:monero.social suggested that tx spam volume be decreased so that he can have all the RAM available on the big-RAM Monero Research Computing machine. The one with 1TB of RAM.     

> __< rucknium >__ I think that would be fine     

> __< rucknium >__ So that gingeropolous:monero.social  can run the scaled-up monerosim     

> __< gingeropolous >__ it should be like 5-8 hrs is all i need     

> __< articmine >__ With the new scaling parameters we need to consider a significantly higher penalty free for stressnet instead of just relying on spam.      

> __< articmine >__ Otherwise it will take years to test for many of the identified issues with scaling      

> __< rucknium >__ Yes. I think initially we thought that the actual FCMP hard fork scaling parameters should be used for beta stressnet, but now I think differently.     

> __< articmine >__ The simplest is to increase the penalty free zone ZM     

> __< rucknium >__ By the way, I checked the current long term median block weight for this stressnet. It is 664 KB. The long term median before stressnet started was 176 KB.     

> __< articmine >__ Then keep the other parameters 8x on MN and 1.2x on ML the same      

> __< rucknium >__ AFAIK, get_info doesn't give you the long term median, which is what I thought before. You have to query a block header.     

> __< gingeropolous >__ articmine:monero.social: , im hopeful monerosim allows for faster testing. so far i can run 6 hours of monero network in about 20 minutes.... faster if the hardware is better     

> __< DataHoarder >__ I show that long term median on each block on my explorer like https://stressnet.p2pool.observer/block/d9399b53688d0bb8a2db9d4fe7f5168a9935b0b067430b8dbeb444a9f42e6dc7     

> __< DataHoarder >__ Indeed comes from block headers     

> __< articmine >__ gingeropolous: So a factor of 18. That will certainly help     

> __< gingeropolous >__ gonna need moar ram     

> __< boog900 >__ rucknium: I think that value would just be that blocks long term weight not the median long term weight     

> __< boog900 >__ https://monero-book.cuprate.org/consensus_rules/blocks/weights.html#calculating-a-blocks-long-term-weight     

> __< rucknium >__ boog900:monero.social: What's the difference?     

> __< articmine >__ The long term block weight can be significantly higher than the long term median, if growth lags behind the long term median.     

> __< articmine >__ It can also be lower      

> __< rucknium >__ Is there an RPC query that can get the median long term weight?     

> __< boog900 >__ A blocks long term weight is the value that is used in the long term blocks list to get the median long term weight      

> __< boog900 >__ In the same way a blocks weight is used in the short term list to get the short term median block weight      

> __< boog900 >__ You could get the long term median weight under some circumstances if the block is outside a certain range by multiplying or dividing by 1.7. For example before stressnet the median was almost certainly 176 * 1.7     

> __< rucknium >__ boog900:monero.social: Your answer is "no, not an easy way to get this info"     

> __< rucknium >__ unless Mercury is in retrograde     

> __< articmine >__ If the long term block weight is under the penalty free zone, then the long term median is the penalty free zone.     

> __< articmine >__ On it has been given enough time to reset      

> __< boog900 >__ rucknium: Well the blocks long term weight is bounded to the long term median divided by 1.7 and multiplied by 1.7 so you can get the value if you have a very small or very large block.     

> __< boog900 >__ But yeah I'm not sure if there is an API that just tells you the value      

> __< articmine >__ With the new proposed changes this bound is 1.2     

> __< rucknium >__ In the 26 November meeting jberman:monero.social  said     

> __< rucknium >__ > personally I'd like to complete the alpha stressnet (reach a point where alpha stressnet is running smooth under reasonable conditions), ideally within the next 4 weeks. and then reopen a conversation on target dates     

> __< rucknium >__ jberman:monero.social and/or jeffro256:monero.social , how close do you think is the end of alpha and beginning of beta stressnet?     

> __< jberman >__ apologies, I messed up timing on this meeting     

> __< jeffro256 >__ Me too, hi      

> __< jbabb:cypherstack.com >__ A "scalenet" with modifered parameters to make spamming much easier to spam in order to get better data on the scaling question makes sense to me, but as a subsequent testnet following this stressnet with its current params     

> __< jbabb:cypherstack.com >__ s/spam/do     

> __< articmine >__ boog900: No the block weight can still be up to 100x ML under the current scaling and up to 16x ML under the proposed scaling     

> __< jeffro256 >__ https://github.com/seraphis-migration/monero/issues/166     

> __< boog900 >__ articmine: The long term weight is a different value.     

> __< jberman >__ Re: end of alpha: We have 1 more open PR for v1.5 that prevents OOM's during initial block download. It is an upstream issue, but the stressnet is triggering it for some. That PR is: https://github.com/seraphis-migration/monero/pull/275     

> __< articmine >__ I've how many cycles of ML     

> __< boog900 >__ boog900: https://github.com/monero-project/monero/blob/eac1b86bb2818ac552457380c9dd421fb8935e5b/src/cryptonote_core/blockchain.cpp#L4569     

> __< articmine >__ Over how many cycles of ML is this long term weight calculated      

> __< articmine >__ MzL can lag     

> __< jeffro256 >__ We've got the weight func modified in the staging branch, Berman is currently working on some changes to tx relay v2 with 0xfffc, we're not going to wait for carrot-derived wallets, hot/cold wallets is ready on PR #52, Unbiased hash-to-point is implemented and ready to merged into the staging branch, the other points are mostly resolved on the staging branch AFAIK      

> __< jberman >__ I also PR'd changes to tx relay v2 that would be nice to have tested in alpha, since tx relay v2 is a fairly significant change affecting the daemon:  https://github.com/0xFFFC0000/monero/pull/62     

> __< jeffro256 >__ So we basically just need to integrate the updated scaling parameters and tx relay v2 and it should be ready to go I think     

> __< jeffro256 >__ Yeah true, we need to upstream the span changes      

> __< jeffro256 >__ But we don't have to wait for them to be upstreamed to start the beta, yeah?     

> __< jberman >__ Sorry I wasn't clear. We need that PR specfically for v1.5 of the alpha stressnet. I was just highlighting how that is an upstream issue (and a separate upstream PR is warranted as well)     

> __< jberman >__ I was thinking we verify that v1.5 solves all the major outstanding alpha stressnet issues people have reported during testing (like OOM's) before moving to beta     

> __< jberman >__ A few stressnet users have also reported new crashes even with a pre-release of v1.5, and I'm still working my way through those, starting with this segfault: https://github.com/seraphis-migration/monero/issues/258     

> __< jberman >__ I'm almost done with a fix for that issue, and then it's on to this issue: https://github.com/seraphis-migration/monero/issues/277     

> __< jeffro256 >__ What path should we take if people keep experiencing some of these same errors? Is it not still worth moving to the beta stressnet and continue debugging there?     

> __< jberman >__ It's hard to prioritize changes like scaling algo for beta when there are triggerable outstanding segfaults     

> __< articmine >__ jberman: I would suggest keeping the existing scaling algo until these issues are fixed     

> __< jeffro256 >__ I absolutely wouldn't push for production with outstanding segfault issues, but ostensibly the errors, if not fixed, will also occur on beta for similar reasons.     

> __< jeffro256 >__ If they occur for similar reasons, then debugging on these issues isn't impacted by moving to beta.      

> __< jberman >__ I also think we need a solution this PR is addressing first and foremost before we should move on to beta, because OOM's have plagued alpha and this should take care of the last major known cause: https://github.com/seraphis-migration/monero/pull/275     

> __< articmine >__ jeffro256: If we change the scaling algo not right away     

> __< jeffro256 >__ If anything, the scaling issues triggering segfaults more often would only make it easier to debug.     

> __< jberman >__ jeffro256: these aren't issues with the FCMP++ integration i.e. they are issues with current production code is also why I think they deserve priority     

> __< jeffro256 >__ jberman: Also, sorry I meant to review this yesterday, will do today.      

> __< jberman >__ np thank you 🙏     

> __< jeffro256 >__ jberman: That's fair, I understand why youbut also I think that we can do this largely in parallel since as you're saying FCMP++ scaling and these OOM errors      

> __< jeffro256 >__ oops     

> __< rucknium >__ Anything more on stressnet?     

> __< jeffro256 >__ I understand why prioritizing this issue over FCMP++ scaling, but I just think that they're mostly orthogonal . But optimistically, if #275 closes up the OOM issues, then we can go full speed ahead :)     

> __< jeffro256 >__ Let's hope that happens      

> __< jberman >__ I agree they're definitely orthogonal. It's just a matter of manpower really. I don't want to divert attention away from dealing with reliability issues like the OOM's / segfault. if we had someone else (like perfect daemon :) ) focusing on them, I would be content moving on to beta tasks like scaling     

> __< rucknium >__ Has anyone heard anything from perfect_daemon? I assume, given his M.O., that he's working on a huge PR in secret.     

> __< jeffro256 >__ Nope      

> __< jeffro256 >__ I've tried to DM unsuccessfully      

> __< jberman >__ I assume the same     

> __< jbabb:cypherstack.com >__ FCMP testing itself is definitedly a priority over scaling questions.  a separate "scalenet" that makes spamming much easier is a orthogonal/tangential to the goal of "just" getting FCMPs working, but it allows an avenue for those that're concerned about scaling issues to prove their point without so much effort invested into spambots.      

> __< vtnerd >__ ruckinum I was about to say if perfect-daemon can’t look at this, I probably could given that my fcmp++ changes are going well     

> __< vtnerd >__ the question is whether we should re-write the span code. probably needs it, otoh its semi-working in production so     

> __< articmine >__ jbabb:cypherstack.com: This is where a significantly higher penalty free zone can be used     

> __< boog900 >__ I think the syncing code is up there with the worst parts of the daemon.      

> __< jberman >__ fwiw, I was primarly referring to issues like https://github.com/seraphis-migration/monero/issues/258 and https://github.com/seraphis-migration/monero/issues/277 , but span code also ya     

> __< jbabb:cypherstack.com >__ I agree overall that they're separate questions.  And maybe it is too much effort just to investigate scaling, but if we want to lower the parameters that we've apparently achieved consensus on, a "scalenet" seems like a way to do that more easily than with the current spam approach     

> __< jberman >__ I'm pretty close to done on 258 though     

> __< rucknium >__ jbabb:cypherstack.com: What do you mean? Would there be no spam on scalenet?     

> __< jbabb:cypherstack.com >__ rucknium: I mean that the current spam efforts are doing well to increase blocksize, but if we really want to break things, opening up the scaling params would make that a lot easier to do.  I agree that it's basically tangential to FCMP work, tho     

> __< articmine >__ jbabb:cypherstack.com: I agree.     

> __< jbabb:cypherstack.com >__ since we already have loose consensus on params that can be paired with the FCMP HF, if we don't want to lower them anymore, a "scalenet" may be unnecessary.     

> __< jberman >__ one benefit to the current approach is that it's showing cracks in the system as they appear (and would appear in production conditions), and we tackle them in that priority order      

> __< rucknium >__ I think we just need to decide what's the target block size to hit in the next stressnet. Then make it easy to hit it.     

> __< jberman >__ e.g. issues 4mb blocks showed up fairly early, got tackled fairly early because of that     

> __< jbabb:cypherstack.com >__ it may be unnecessary or something that's safe to defer until after the FCMP HF / beta FCMP work     

> __< articmine >__ jbabb:cypherstack.com: The advantage of a scalenet is to accelerate the process.     

> __< articmine >__ Then we can see in say a few months an issue that may take several years      

> __< rucknium >__ Anything else on stressnet?     

> __< jberman >__ My take on status: release v1.5 (hopefully within the next days), see what if any major reliability issues remain, either work on those reliability issues or continue toward beta. Tx relay v2 at this point may be fine to kick to beta     

> __< rucknium >__ We can end the meeting here. Thanks everyone.     

> __< articmine >__ Thanks      

> __< DataHoarder >__ As a note to the long term weights I should be able to display these on the explorer for the current tip, given I'm getting the miner data and calculating the expected growth inline     

> __< DataHoarder >__ Scalenet sounds great plus a few tricks of ours, if the point is to specifically stress that part. Might be good to expect resetting it regularly (so we don't end with TiB of state) and can test new changes iteratively      

> __< rucknium >__ The new version of https://moneronet.info is working now 😁     

> __< monerobull:matrix.org >__ > 1 TB ram > <rucknium> gingeropolous:monero.social suggested that tx spam volume be decreased so that he can have all the RAM available on the big-RAM Monero Research Computing machine. The one with 1TB of RAM.     

> __< monerobull:matrix.org >__ > And I always thought we are a poor project!     

> __< rucknium >__ It was funded by a CCS proposal: https://ccs.getmonero.org/proposals/gingeropolous_1TB_MRC.html     

> __< rucknium >__ Thank you donors!     

> __< 321bob321 >__ Ram only node inbound     


# Action History
- Created by: Rucknium | 2026-01-06T22:34:02+00:00
- Closed at: 2026-01-20T23:11:27+00:00
