---
title: Monero Research Lab Meeting - Wed 05 November 2025, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/1292
author: Rucknium
assignees: []
labels: []
created_at: '2025-11-04T23:01:55+00:00'
updated_at: '2025-11-18T22:31:01+00:00'
type: issue
status: closed
closed_at: '2025-11-18T22:31:01+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/meeting.html?p1=1440)

Main discussion topics:

1. Greetings

2. Updates. What is everyone working on?

3. [Transaction volume scaling parameters after FCMP hard fork](https://github.com/ArticMine/Monero-Documents/blob/master/MoneroScaling2025-07.pdf). [Revisit FCMP++ transaction weight function](https://github.com/seraphis-migration/monero/issues/44). [Simple Market-Based Monero Fee Proposal](https://github.com/monero-project/research-lab/issues/152).

4. [FCMP alpha stressnet](https://monero.town/post/6763165).

5. Mining pool centralization: [Temporary rolling DNS checkpoints](https://github.com/monero-project/monero/issues/10064), [Share or Perish](https://github.com/monero-project/research-lab/issues/146), and [Lucky transactions](https://github.com/monero-project/research-lab/issues/145).

6. Any other business

Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: Rucknium

Previous meeting agenda/logs:

#1289 

# Discussion History
## Rucknium | 2025-11-11T23:38:55+00:00
Log

> __< rucknium >__ I will add more structure to the scaling discussion agenda item. I will ask meeting participants to write what they think are the relevant facts about transaction volume scaling. These facts must be about the present or past. Nothing about the future. "It is difficult to make predictions, especially about the future." Exampl [... too long, see https://mrelay.p2pool.observer/e/w-eq8sUKZG1yUVda ]     

> __< rucknium >__ I think there is a path to rough consensus on post-hardfork scaling parameters. Finding the path will be easier if the discussion participants can get on the same page about the facts.     

> __< rucknium >__ The meeting starts in 45 minutes, at 17:00 UTC as usual.     

> __< articmine >__ We cannot ignore the future if we analyze the present and past. In particular the impact of blockchain surveillance  BS in suppressing Monero adoption for the last decade.      

> __< articmine >__ A simple reversal in the US courts of a criminal conviction could derail the entire BS law enforcement narrative, and unleash Monero adoption after suppression  for over a decade.     

> __< articmine >__ I will not support baking into the Monero protocol the harm that the BS companies have done to Monero by looking at only the past and present.     

> __< articmine >__ There is also the very real issue of conflict of interest here.     

> __< rucknium >__ The future will be discussed later in the meeting. It will be much easier to start by closing the gap between participants by agreeing on facts.     

> __< rucknium >__ Meeting time! https://github.com/monero-project/meta/issues/1292     

> __< rucknium >__ 1. Greetings     

> __< articmine >__ Hi     

> __< spackle >__ Hello     

> __< jberman >__ waves     

> __< sgp_ >__ Hello     

> __< vtnerd >__ Hi     

> __< boog900 >__ hi     

> __< rucknium >__ 2. Updates. What is everyone working on?     

> __< sgp_ >__ ping kayabaNerve. Working out a GBP issue (which they believe they found a resolution for)     

> __< ArticMine >__ I have updated the scaling proposal and commented on the changes and impacts https://github.com/seraphis-migration/monero/issues/44     

> __< rucknium >__ me: Starting my first adventures with using Wireshark to analyze Monero p2p packets for spy node analysis. Did you know that Monero has its own display filter in Wireshark? https://www.wireshark.org/docs/dfref/m/monero.html      

> __< rucknium >__ ping @jeffro256:monero.social     

> __< jeffro256 >__ Howdy     

> __< vtnerd >__ Me: subaddress lookahead in lws daemon     

> __< jeffro256 >__ Me: fleshing out device integration for Carrot and working thru some Stressnet bugs       

> __< rucknium >__ 3. Transaction volume scaling parameters after FCMP hard fork (https://github.com/ArticMine/Monero-Documents/blob/master/MoneroScaling2025-07.pdf). Revisit FCMP++ transaction weight function (https://github.com/seraphis-migration/monero/issues/44). Simple Market-Based Monero Fee Proposal (https://github.com/monero-project/research-lab/issues/152).     

> __< rucknium >__ I will add more structure to the scaling discussion agenda item. I will ask meeting participants to write what they think are the relevant facts about transaction volume scaling. These facts must be about the present or past. Nothing about the future. "It is difficult to make predictions, especially about the future." Example  [... too long, see https://mrelay.p2pool.observer/e/vPP488UKQWJUbzhv ]     

> __< jberman >__ Me: We released v1.4 of the stressnet which includes some monerod fixes and improvements. I identified a significant cause of high memory usage in the FCMP++ integration (batch verifying many large input proofs simultaneously), discussed with @kayabanerve:matrix.org  who brought down mem usage 33%, and I wrote an initial patch [... too long, see https://mrelay.p2pool.observer/e/4qv588UKanpVLUpy ]     

> __< rucknium >__ I think there is a path to rough consensus on post-hardfork scaling parameters. Finding the path will be easier if the discussion participants can get on the same page about the facts.     

> __< ArticMine >__ Here are the facts https://bitinfocharts.com/comparison/transactions-price-xmr.html#log&alltime     

> __< jberman >__ Again, first and foremost, I want to reiterate there appears to be rough consensus for tx weight roughly equal to byte size     

> __< ArticMine >__ A 30x growth in on chain transaction is nuder 2 years and strong evidence of the suppression of Monero adoption by the BS companies for close to a decade.      

> __< rucknium >__ @jberman:monero.social: I agree.     

> __< articmine >__ @jberman: That is correct     

> __< sgp_ >__ I only have one comment at this moment, which is how I don't understand how my simpler proposal is in conflict with "Monero's principles."     

> __< sgp_ >__ For the simple proposal, consider for comparison scaling parameters as follows: set the initial flex space to 16 MB-ish (as what ArticMine picked in their update) and the permitted growth rate to 50%/year.     

> __< sgp_ >__ Is this acceptable ArticMine? What's the risk to Monero's principles in your view if we do that?     

> __< kayabanerve:matrix.org >__ Hello, I've been handling bug fixes, improvements to oxide as it targets 1.0, managing merging GBPs into oxide's main branch _and_ its BBP program, and going back and forth with Berman a bit (they're doing the work) on higher than expected memory use. I did make a patch for one obvious oversight that brought it down 33%, but t [... too long, see https://mrelay.p2pool.observer/e/6JOI9MUKQ3NsQXd3 ]     

> __< kayabanerve:matrix.org >__ Sorry for the late hello     

> __< jeffro256 >__ @sgp_:monero.social: I will look more deeply at your proposal shortly .Could you link it here now for the record please ?     

> __< sgp_ >__ github.com/monero-project/research-lab/issues/152     

> __< spackle >__ @rucknium:monero.social: Quick note that the most recent proposal from ArticMine is https://github.com/ArticMine/Monero-Documents/blob/master/MoneroScaling2025-11.pdf     

> __< spackle >__ There is no penalty zone when the penalty median is equal to the maximum block size. Miners will receive the full block reward when creating a steady stream of 16 MB blocks.     

> __< spackle >__ If the surge factor is instead set to 8 (M_N=min(M_S, 8*M_L)), miners are penalized for creating 16 MB blocks and a fee market is required to support that level.      

> __< spackle >__ I prefer setting the surge factor to 8. That said, either approach gives the design a safety margin. If there is consensus behind either option I believe both are acceptable.     

> __< ArticMine >__ My change allows for nor low rate scaling between MS at 8x ML and MS at 16x ML,. There is not need to pay outrageous fees if the scaling rate is low     

> __< ArticMine >__ The fees become prohibitive with just changinng the scaling factor to 8     

> __< spackle >__ As I see it, the key requirement is that there is no short term gap between daemon performance and scaling limits. So long as there is developer/community consensus that the daemon can handle a steady stream of 16 MB blocks, either is acceptable.     

> __< ArticMine >__ It is the way for me to be able to support the safety margin at 16x     

> __< rucknium >__ What are the facts about daemon performance?     

> __< spackle >__ At the moment, I do not know that 16 MB is the correct level. I am waiting to hear the educated opinions of others.     

> __< ArticMine >__ I also provided an interim temporary proposal using the current RingCT     

> __< ArticMine >__ with a much lower cap     

> __< ArticMine >__ Effectively 4x     

> __< sgp_ >__ A fact is that 16 MB blocks full for a year (e.g. miner spam) is ~4 TB of growth per year. Assuming no further growth in the block size or additional spam     

> __< jberman >__ Once we have this OOM issue solved + tx relay v2 in, we will likely get a better picture of what the daemon is able to handle. Hopefully that will be within the next week or 2     

> __< ArticMine >__ Please. I will not agree to baking the harms of BS ito the protocol. there is no such spam     

> __< ArticMine >__ We are talking about ham     

> __< articmine >__ @jberman: This is wi I also provided the lower interim option     

> __< ArticMine >__ If addition time is neeeded to fix this     

> __< jberman >__ Bringing blockchain surveillance into this discussion is a non sequitur. FCMP++ is by 100 miles the most significant thing we can do to negatively impact blockchain surveillance at this stage     

> __< ArticMine >__ We have to consider post quantum attack for example when BC can play a role     

> __< ArticMine >__ it is far from a non sequitor     

> __< jberman >__ Great! Carrot brings post quantum forward secrecy for people who don't share their addresses / for change outputs     

> __< ArticMine >__ the issue here is the suppression of adoption     

> __< jberman >__ Delaying FCMP++ / Carrot is the most helpful thing you can do for blockchain surveillance     

> __< boog900 >__ I do think there should be some cost preventing people from creating 16 MB bocks forever     

> __< ArticMine >__ I really believe we can avoid this, but unfortunately we do have real issue with the code that need to be addressed     

> __< boog900 >__ Although I do think 16 MB is a much better target for performance than 32 MB      

> __< ArticMine >__ The is what I call the BS harm trap     

> __< ArticMine >__ if Monero adoption had not been suppressed by the BC companies 16 MB blocks could esily be the norem     

> __< ArticMine >__ norm     

> __< sgp_ >__ @boog900:monero.social the simple proposal could be set with a flex space of 16 MB. Then those blocks could still be made, but only at the cost of the block reward. And the size of the flex space could be permitted to grow (accounting for tech improvements)     

> __< sgp_ >__ *cost of the tail emission     

> __< rucknium >__ I think that the advocates for fast scaling are worried that history will repeat itself. Bitcoin's 1MB limit was supposed to be a temporary anti-spam measure. As the saying goes, there is nothing more permanent than a "temporary" solution.      

> __< rucknium >__ The advocates for slower scaling are worried that fast scaling could become a DDoS threat against the network because daemon performance is suboptimal.     

> __< rucknium >__ Am I seeing things correctly?     

> __< articmine >__ @sgp_: The fex in the simple proposal is extremely ext     

> __< articmine >__ Expensive      

> __< articmine >__ @rucknium: Yes the Bitcoin issue is real.     

> __< articmine >__ We need to address the deamon issues. Not allow this to be an excuse to cripple Monero over the long term      

> __< sgp_ >__ at 16 MB max block size, the approximate penalty from the tail emission is 0.000384615 XMR/tx, or ~$0.13 in today's prices     

> __< jberman >__ "because daemon performance is suboptimal" -> 16mb blocks = 4TB of chain data per year     

> __< sgp_ >__ https://mrelay.p2pool.observer/m/monero.social/feLUbEJBHwlueOxjWrvaHMIT.png (image.png)     

> __< boog900 >__ I do like the slow increase with the more complex proposal though, with yours you can wack a 16 MB block straight away right? > <@sgp_> @boog900:monero.social the simple proposal could be set with a flex space of 16 MB. Then those blocks could still be made, but only at the cost of the block reward. And the size of the flex space could be permitted to grow (accounting for tech improvements)     

> __< articmine >__ In 50 blocks      

> __< articmine >__ Spam is one of the real issues with this simple proposal      

> __< rucknium >__ @jberman:monero.social: You are saying that the issues you see with fast scaling include raw blockchain storage size?     

> __< sgp_ >__ @boog900: If that's what you set it to. You can of course pick a lower number if you want. Creating a block that consumes the entire flex space costs the tail emission     

> __< articmine >__ There is no pricing for the base scaling      

> __< jberman >__ @rucknium: yes, imo daemon performance isn't even the primary issue     

> __< elongated:matrix.org >__ @sgp_: For a attacker (rouge mining pool) it doesn’t matter     

> __< jberman >__ There is also verification time and wallet sync time that would end up painful even when implemented in the theoretically optimal way     

> __< tevador >__ I don't think we should allow anyone to choke the network with a random 16 MB block.     

> __< sgp_ >__ @elongated:matrix.org: A mining pool pays the opportunity cost by not receiving the tail emission, that's a major advantage of the simple proposal     

> __< elongated:matrix.org >__ @sgp_: We had qubic, they can be incentivised other ways     

> __< articmine >__ tevador: ThIs is the reason why a ZCash type attack did not work in Monero     

> __< sgp_ >__ The other proposal has no cost, so it's incrementally more. Whether it's a deterrent is another matter     

> __< sgp_ >__ *sufficient deterrent     

> __< elongated:matrix.org >__ @sgp_: Can current ecosystem handle 16mb blocks ?     

> __< boog900 >__ @jberman:monero.social: do you think growth should be slower or it should cost to maintain 16 MB blocks?     

> __< articmine >__ @sgp_: As I indicated I will respond to your proposal in GitHub. First I want to work on the weights for which we have consensus     

> __< spackle >__ There is the additional matter that miners may limit block sizes out of sheer practicality, and I expect that would be the case in reality. If the network is configured to sufficiently limit the network to daemon performance in the short term to what it can handle, all network participants are given some amount of time to respond to any condition that arises.     

> __< boog900 >__ Or something else      

> __< sgp_ >__ Fwiw I don't propose 16 MB blocks, I'm just saying that those are *compatible" with my proposal if that's what you want. I want smaller blocks     

> __< spackle >__ But they must be given some amount of time to respond thoughtfully, and not ambushed.     

> __< spackle >__ Put differently, when everyone goes to sleep at night they must know that the network will be in a stable condition when they wake up the next day. I believe that is the key requirement for the scaling algorithm in the short term.     

> __< jberman >__ I think it should cost to maintain 16 MB blocks and I agree I like that a miner / the network can't immediately create a 16 MB block in the more complex proposal     

> __< articmine >__ @jberman: There is a cost to maintain  16 MB blocks     

> __< articmine >__ If you stop the short term median resets      

> __< sgp_ >__ In mine, the max allowed block size will incur a fixed cost of 0.6 XMR per block     

> __< articmine >__ This has always been the case     

> __< articmine >__ Can we move on     

> __< rucknium >__ Move on to the next agenda item?     

> __< articmine >__ Yes      

> __< rucknium >__ Ok     

> __< rucknium >__ 4. FCMP alpha stressnet (https://monero.town/post/6763165).     

> __< monerobull:matrix.org >__ Why did that ping me     

> __< monerobull:matrix.org >__ Ah, town link      

> __< jberman >__ Repeating my prior update: We released v1.4 of the stressnet which includes some monerod fixes and improvements. I identified a significant cause of high memory usage in the FCMP++ integration (batch verifying many large input proofs simultaneously), discussed with kayabanerve who brought down mem usage 33%, and I wrote an ini [... too long, see https://mrelay.p2pool.observer/e/99Co9cUKaV9rUjM2 ]     

> __< jberman >__ v1.4 may have introduced a regression as well that we're looking into too     

> __< jberman >__ Repeating the 3 blocking issues: 1) OOM's, 2) daemon kicking all txs from the pool but one, 3) wallet running into double spends after some use     

> __< jberman >__ 1. we're making progress     

> __< jberman >__ 2. v1.4 included a bug fix that addressed this issue, monitoring to see if that repeats     

> __< jberman >__ 3. I'm waiting on a repeat occurrence with reflected daemon logs for this one     

> __< jberman >__ With OOM addressed + tx relay v2 (which may also help with OOM's), and observed stable perf under stress, I would advocate for moving to the beta     

> __< DataHoarder >__ how soon after alpha concludes would beta come online?     

> __< jberman >__ A week seems reasonable to me     

> __< rucknium >__ IMHO, a little more notice than a week would be good to get more people running nodes. But you can give more than one week of notice if the alpha stressnet shuts down after the beta announcement     

> __< rucknium >__ @boog900:monero.social: Could cuprate participate in stressnet, in the RingCT phase and/or FCMP phase, with that timeline?     

> __< jberman >__ Of note, we'll also want to reach consensus on scaling params and implement it before beta, so there is going to be some time     

> __< boog900 >__ Yes ringCT maybe FCMP      

> __< rucknium >__ @jberman: Yes, that would been needed, too.     

> __< DataHoarder >__ would remaining carrot changes be done before beta?     

> __< boog900 >__ We can always join late too      

> __< jberman >__ DataHoarder: yes     

> __< jberman >__ well I guess it depends which carrot changes you're referring to     

> __< kayabanerve:matrix.org >__ The issue with the FCMP phase is that someone has to update oxide, and then propagate to Cuprate, and I'll note a few misc rules have been added which'll need to found and indexed     

> __< jberman >__ We have a TODO list tracker for beta here: https://github.com/seraphis-migration/monero/issues/166     

> __< kayabanerve:matrix.org >__ Updating oxide isn't the worst, it's already in Rust, I'm just noting someone has to get it over the hump     

> __< jeffro256 >__ DataHoarder: Which changes ?     

> __< DataHoarder >__ personalization string for one      

> __< DataHoarder >__ for the transcript / blake2b in general     

> __< DataHoarder >__ any coinbase specific changes (for example same pubkey suggested by tevador, but I think that's relevant for future stuff)     

> __< rucknium >__ Anything else on stressnet?     

> __< jberman >__ Nothing from me     

> __< rucknium >__ Thank you, everyone working on stressnet fixes :)     

> __< rucknium >__ 5. Mining pool centralization: Temporary rolling DNS checkpoints (https://github.com/monero-project/monero/issues/10064), Share or Perish (https://github.com/monero-project/research-lab/issues/146), and Lucky transactions (https://github.com/monero-project/research-lab/issues/145).     

> __< DataHoarder >__ maybe spend some developer time between alpha and beta stressnet fixing the bug within that core function for DNS checkpoints to function ^ ?     

> __< DataHoarder >__ this is an example of technical debt and flawed implementation, if we are to be fixing those :)     

> __< boog900 >__ DataHoarder: Do we know where the bug is yet?     

> __< boog900 >__ Or what the exact bug is     

> __< DataHoarder >__ we know the symptom and affected function, unclear if that's where the bug is. I think links were posted last meeting, but I don't have that backlog available currently     

> __< DataHoarder >__ a checkpoint set on an altchain at a specific height causes monero to get stuck and not be able to switch to the altchain or add blocks after     

> __< rucknium >__ DataHoarder: https://libera.monerologs.net/monero-research-lab/20251029#c604484-c604495     

> __< DataHoarder >__ it'd help massively as mentioned if we can get a specific repro sequence, as otherwise it's hard to test against. or a unit test for it :)     

> __< rucknium >__ We can end the meeting here. Thanks everyone.     

> __< sgp_ >__ I accidentally closed my issue, can it be reopened please? https://github.com/monero-project/research-lab/issues/152     

> __< sgp_ >__ rip     

> __< rucknium >__ Done.     

> __< articmine >__ @rucknium: Thanks     

> __< sgp_ >__ @rucknium: thanks!     

> __< sgp_ >__ @jeffro256:monero.social: am I misunderstanding your comment about the fee market, and sender fee selections?     

> __< ofrnxmr >__ @boog900:monero.social  im testing now, but i think we have the runaway spans fixed. > <@jberman> Repeating the 3 blocking issues: 1) OOM's, 2) daemon kicking all txs from the pool but one, 3) wallet running into double spends after some use     

> __< ofrnxmr >__ for stripe_main_proceed, there were 2 contributing factors:     

> __< ofrnxmr >__ 1. I found an issue with next_needed_height, there it would incorrectly display blocks that we already have (fixed by 0xfffc)[... more lines follow, see https://mrelay.p2pool.observer/e/xrXE-MUKM1VlQTNW ]     




# Action History
- Created by: Rucknium | 2025-11-04T23:01:55+00:00
- Closed at: 2025-11-18T22:31:01+00:00
