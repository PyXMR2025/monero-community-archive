---
title: Monero Research Lab Meeting - Wed 01 November 2023, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/915
author: Rucknium
assignees: []
labels: []
created_at: '2023-11-01T15:42:54+00:00'
updated_at: '2023-11-10T16:54:35+00:00'
type: issue
status: closed
closed_at: '2023-11-05T18:47:38+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

[Join the Monero Matrix server if you don't already have a Matrix account.](https://forum.monero.space/d/79-how-to-join-the-monero-core-team-matrix-server-web)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/converter.html?iso=20211027T170000&p1=1440)

Main discussion topics:

1. Greetings

2. Discuss: Reducing 10 block lock: https://github.com/monero-project/research-lab/issues/102#issuecomment-1577827259

3. Discuss: [Exploring Trustless zk-SNARKs for Monero's payment protocol](https://github.com/monero-project/research-lab/issues/100). What are the bottlenecks for potential implementation?

4. Improvements to the decoy selection algorithm ( [Decoy Selection Algorithm - Areas to Improve](https://github.com/monero-project/research-lab/issues/86), [Binning PoC](https://github.com/monero-project/research-lab/issues/88), [OSPEAD](https://ccs.getmonero.org/proposals/Rucknium-OSPEAD-Fortifying-Monero-Against-Statistical-Attack.html) ) @j-berman @Rucknium

5. Seraphis. ( [UkoeHB's Seraphis Proof of Concept work](https://ccs.getmonero.org/proposals/seraphis-wallet-poc-2.html), [Seraphis repo](https://github.com/UkoeHB/Seraphis) ).

6. MRL Meta: "Cat herding", i.e. prioritization of research areas and features. Active recruitment of technical talent, MRL structure, funding (@Rucknium & others) [MoneroResearch.info repository of Monero-related research papers](https://moneroresearch.info/), [Reddit discussion](https://www.reddit.com/r/Monero/comments/pkg3d6/the_monero_project_should_actively_recruit/)

7. Any other business

8. Confirm next meeting agenda


Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: Rucknium

Previous meeting agenda/logs:

#913 

# Discussion History
## plowsof | 2023-11-10T16:54:35+00:00
Logs 
> __< r​ucknium:monero.social >__ Meeting time! https://github.com/monero-project/meta/issues/915     

> __< r​ucknium:monero.social >__ 1) Greetings     

> __< v​tnerd:monero.social >__ Hi     

> __< r​ucknium:monero.social >__ 2) Updates. What is everyone working on?     

> __< rbrunner >__ Hello     

> __< v​tnerd:monero.social >__ Still on subaddresss (unit tests). It's basically done, minus at least one outstanding bug     

> __< r​ucknium:monero.social >__ me: I counted the non-RingCT rings and transactions since the August 2023 hard fork. About 0.005% of txs had at least one non-RingCT ring: https://github.com/monero-project/research-lab/issues/59#issuecomment-1783237506     

> __< r​ucknium:monero.social >__ ^ This matters because we want to decide whether to allow non-RinCT outputs to be put in rings with RingCT outputs in the Seraphis upgrade proposal.     

> __< j​effro256:monero.social >__ That’s way less than I would’ve guessed     

> __< j​effro256:monero.social >__ Interesting     

> __< r​ucknium:monero.social >__ Except in the unmixable edge case, users haven't been able to produce non-RingCT outputs for about 4 years IIRC. It makes sense to me that there are few users spending very old outputs     

> __< r​ucknium:monero.social >__ Some of the txs had some RingCt and non-RingCT rings. You can have both in a single tx     

> __< j​effro256:monero.social >__ Do you have a count of total non-RingCT outputs and total number of non-RingCT inputs ?     

> __< r​ucknium:monero.social >__ Total non-RingCT outputs that have every been produced? No, I don't have that right now.     

> __< r​ucknium:monero.social >__ What do you mean by the second one?     

> __< r​ucknium:monero.social >__ You mean total number of non-RCT rings that have ever existed?     

> __< j​effro256:monero.social >__ If we knew 1) the total number of non-RingCT outputs ever produced and 2) the total number of non-RingCT input rings ever used, then we could get a rough estimate of what percentage of non-RingCT outputs are unspent     

> __< r​ucknium:monero.social >__ Yes. You could probably break it down further by non-RCT amount. It's an interesting question, but it would take some time to code it up. How important is it to the GitHub issue discussion?     

> __< r​ucknium:monero.social >__ Many of those outputs probably will never be spent. Lost keys, dust, etc.     

> __< r​ucknium:monero.social >__ We are well into (3) Discussion. What do we want to discuss?     

> __< j​effro256:monero.social >__ I posted a Jamtis proposal breakdown     

> __< j​effro256:monero.social >__ https://gist.github.com/tevador/50160d160d24cfc6c52ae02eb3d17024?permalink_comment_id=4744307#gistcomment-4744307     

> __< j​effro256:monero.social >__ Does anyone have questions or want to discuss pros/cons ?     

> __< rbrunner >__ If I just take the column with the least "x", the winner is in the last one ...     

> __< j​effro256:monero.social >__ It’s not that important but would add an extra layer of depth to the discussion of if its worth it to change. Honestly I could code this up myself tho     

> __< v​tnerd:monero.social >__ as long as the address fits within a dns txt record for openalias, its not too bad     

> __< rbrunner >__ I am a bit surprised about the minimal speed reductions. I vaguely remember some comments where you talked about much bigger (potential?) speed problems.     

> __< rbrunner >__ Did I misunderstand?     

> __< rbrunner >__ Or misremember?     

> __< j​effro256:monero.social >__ No you remember correctly, but that’s a bandwidth thing for light wallets     

> __< j​effro256:monero.social >__ The 0.4% difference is for full wallets     

> __< rbrunner >__ I see. And how is that last column solution in this regard?     

> __< j​effro256:monero.social >__ Light wallet *computation* is slowed down 100x     

> __< j​effro256:monero.social >__ I should add that, even though I don’t think it’s a bottleneck     

> __< rbrunner >__ Compute what?     

> __< j​effro256:monero.social >__ So the last column “flexible” VTs allows the community to adjust the “match rate” for LW scanning as light wallet users require     

> __< j​effro256:monero.social >__ So it doesn’t make anything *faster* but allows us to manually control the bandwidth and computation requirements for light wallets if it gets out of hand     

> __< j​effro256:monero.social >__ We can do this by enforcing a different value for npbits     

> __< j​effro256:monero.social >__ Basically CPU time needed for scanning     

> __< r​ucknium:monero.social >__ Something I can contribute is the potential privacy impact of flexible vs dynamic view tags. AFAIK, flexible view tag length allows the wallet to choose length, which can produce transaction non-uniformity on chain. My discussion note on fungibility defects can tell you how big the privacy impact could be: https://github.com/Rucknium/misc-research/tree/main/Monero-Fungibility-Defect-Classifier/pd     

> __< j​effro256:monero.social >__ No flexible view tags do NOT allow the wallet to choose view tag length unless they can skirt relay rules     

> __< r​ucknium:monero.social >__ Then why does "Doesn't Need Recent Chaindata for VT constr.?" have a checkmark for flexible view tags?     

> __< rbrunner >__ But we have to count on the community of Monero daemon runners to mostly update, for the scheme to work, right?     

> __< rbrunner >__ Something similar like the tx_extra size restriction that was introduced that way     

> __< j​effro256:monero.social >__ Because it would ostensibly be a constant value for a given set of rules     

> __< j​effro256:monero.social >__ Yup, same with fees     

> __< rbrunner >__ The slow, slow introduction of soft forks :)     

> __< r​ucknium:monero.social >__ Zcash raised the fee for tx relay without a hard fork and it was a big UX problem, FWIW.     

> __< rbrunner >__ Well, if things get really hard, I guess we could hardfork after all within a reasonable timeframe     

> __< rbrunner >__ in that unlikely case     

> __< j​effro256:monero.social >__ Well technically there is no soft forking involved since it’s only relay rules     

> __< r​ucknium:monero.social >__ With flexible few tags, "Doesn't Need Recent Chaindata for VT constr.?" is "does not", but the wallets have to know what the nodes are requiring, still.     

> __< j​effro256:monero.social >__ What was the UX problem? I assume there were wallets which didn’t update to the new rules and their transactions got dropped     

> __< r​ucknium:monero.social >__ Yes, that was it.     

> __< j​effro256:monero.social >__ Yes     

> __< j​effro256:monero.social >__ FWIW I don’t foresee the length getting changed ls very often, only in cases where it becomes unweildy for a large section of LW users     

> __< rbrunner >__ Well, aren't we talking about a coin that needs months to address even very serious problems, quite in general? I hope we could do better.     

> __< j​effro256:monero.social >__ Wdym ?     

> __< r​ucknium:monero.social >__ "We"....well, there are many nonstandard Monero wallet implementations     

> __< rbrunner >__ Those Zcash problems in particular. I am not very surprised that many wallets and/or wallet users did not update intime     

> __< rbrunner >__ Maybe we can mitigate by allowing the wallets to query the required length     

> __< j​effro256:monero.social >__ Ohhhh yeah     

> __< r​ucknium:monero.social >__ The Zcash problem was foreseeable. They should have implemented the fee changes at a hard fork. But once they decided to have it as a node relay rule, it's hard to fix the problem.     

> __< rbrunner >__ Indeed     

> __< rbrunner >__ That "fee problem" should not have existed in the first place, for a sane cryptocurrency, if you ask me     

> __< j​effro256:monero.social >__ That’s not a bad idea… as long as it’s cached and almost never changes then it shouldnt usually affect UX     

> __< r​ucknium:monero.social >__ Zcash even has a small advantage: Their node software has an auto-shutoff period. Node runners have to update their nodes once every...3 months I think. So they could assume that nodes would update their relay rules. Many wallets didn't of course.     

> __< rbrunner >__ But anyway, do we speculate that we may quickly establish new fee levels under some circumstances? If yes, which ones?     

> __< rbrunner >__ (if we are already a bit off topic, talking about non-hardfork changes)     

> __< r​ucknium:monero.social >__ I mentioned the Zcash fee problem since raising fees is similar to requiring a specific view tag length.     

> __< rbrunner >__ Ok     

> __< r​ucknium:monero.social >__ rbrunner: did you mean quickly establish new view tag lengths?     

> __< rbrunner >__ No, I was just wondering whether it may be worth it to think a bit more about such relay rules updates     

> __< rbrunner >__ because maybe beside view tag length fee changes could be already a second one     

> __< rbrunner >__ and wondered whether I am correct there     

> __< rbrunner >__ And "quick" comes in because, well, "cannot wait for a hardfork" maybe     

> __< r​ucknium:monero.social >__ For example, if there were a spam incident that higher fees could defeat?     

> __< rbrunner >__ Yeah, but I think we may be on the safe side here, because if I remember correctly the daemons tells the fee that is needed     

> __< rbrunner >__ The wallet may give the user an estimate that is way off, however     

> __< r​ucknium:monero.social >__ Yes, but about 10% of transactions are produced by wallets that don't listen to the nodes. Or mis-hear the nodes....I dont know.     

> __< r​ucknium:monero.social >__ You don't have to design around those 10%, but don't forget about it, either.     

> __< rbrunner >__ Yes. I think we talk about problems with many aspects here.     

> __< rbrunner >__ But anyway, if things are pretty quiet, as they are now for quite some time already, no view tag length changes, right?     

> __< rbrunner >__ Or, we are talking not about the normal case, but about special situations.     

> __< j​effro256:monero.social >__ Yeah fixed-length view tags are great in that their privacy scales up with volume, and you compare your LW specs as a linear fraction of what the node requirements are. They only real downside is that they can’t adjust in special circumstances. That is what I aim with “flexible” view tags: they normally don’t change, but if there is a large outcry from LW users that they c<clipped messag     

> __< j​effro256:monero.social >__ an’t keep up with their fraction of node requirements, then it could be adjusted through relay rule     

> __< j​effro256:monero.social >__ But the idea is that most of the time they would be fixed size until the community manually changes it     

> __< rbrunner >__ I guess the code is not much more complex, the code needed to implement that flexible length?     

> __< j​effro256:monero.social >__ Dynamic view tags, on the other hand, adjust dynamically to match a certain number of enotes per time period based on transaction volume. Which means that LW requirements will never have to increase ever     

> __< j​effro256:monero.social >__ But that also means that their anon set, according to one’s LWS, doesn’t increase with volume     

> __< r​ucknium:monero.social >__ I don't like the idea of an "outcry" triggering a change in tx relay rules, if the issue can be anticipated.     

> __< j​effro256:monero.social >__ That’s definitely one of the upsides of flexible view tags: implementation is much easier than dynamic     

> __< j​effro256:monero.social >__ Well just because the outcry doesn’t exists doesn’t mean you have to respond to it , but now you have the option.     

> __< rbrunner >__ I think dynamic has a lot of edge cases to consider, especially around the time of the dynamic change     

> __< j​effro256:monero.social >__ The problem is that these performance / processing requirement are REALLY HARD to anticipate. @tevador and I spent weeks talking about this but at the end of the day it’s just speculation     

> __< rbrunner >__ There will probably be an outcry because something happened, and that "something" may well be unexpected. We would not care about the outcry, but about what happened     

> __< j​effro256:monero.social >__ Yeah, the flexible step is probably smaller. The decision between flexible and dynamic honestly isn’t too important because we can switch back and forth between the two by changing relay rules, just like we would change flexible view tag size. The really important decision is whether we want to add the extra exchange key or not     

> __< rbrunner >__ I think you will be able to win people over for that if it can be shown that the thing "flies", that the necessary changes are reasonable all around     

> __< rbrunner >__ in complexity, time needed to implement, and resource requirements in general     

> __< rbrunner >__ which I think is almost achieved     

> __< rbrunner >__ IMHO     

> __< r​ucknium:monero.social >__ Do a grep search for "why does syncing take so long" on all Monero support forums. :P     

> __< rbrunner >__ Yeah, those people will get shiny new LWs :)     

> __< rbrunner >__ Without any strong drawbacks     

> __< r​ucknium:monero.social >__ We are past the hour. This conversation will continue :)     


Automated by [this](https://github.com/plowsof/post-libera-meeting-logs)

# Action History
- Created by: Rucknium | 2023-11-01T15:42:54+00:00
- Closed at: 2023-11-05T18:47:38+00:00
