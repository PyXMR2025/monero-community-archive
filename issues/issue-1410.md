---
title: Monero Research Lab Meeting - Wed 24 Jun 2026, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/1410
author: Rucknium
assignees: []
labels: []
created_at: '2026-06-24T14:44:48+00:00'
updated_at: '2026-07-01T14:52:29+00:00'
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

3. [emsczkp research Bulletproofs* Milestone 2 completed](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/626#note_36734).

4. [Post-quantum encryption](https://github.com/monero-project/research-lab/issues/151#issuecomment-4412416686). [Jamtis](https://gist.github.com/tevador/639d083c994c1ef9401832c08e2b7832#appendix-c-instant-sync-protocol).

5. [FCMP beta stressnet](https://github.com/seraphis-migration/monero/releases/).

6. [`monerosim`](https://github.com/Fountain5405/monerosim).

7. Any other business

8. Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: Rucknium

Previous meeting agenda/logs: #1407 

# Discussion History
## Rucknium | 2026-07-01T14:52:29+00:00
Logs

> __< gingeropolous >__ unfortunately I won't be able to attend live during the meeting. But I'm continuing to push monerosim towards mainnet fidelity. Current results here: https://github.com/Fountain5405/monerosim/blob/main/docs/20260620_network_topology_study.md . TL;DR, it seems the hypothesis was right, that a 100% reachable network behaves differently than main net.      

> __< gingeropolous >__ the sim currently running is the "churning" - nodes turning on and off throughout the sim, as opposed to always on.     

> __< rucknium >__ Meeting time! https://github.com/monero-project/meta/issues/1410     

> __< rucknium >__ 1. Greetings     

> __< emsczkp:matrix.org >__ Hello     

> __< rbrunner >__ Hello     

> __< jberman >__ waves     

> __< DataHoarder >__ 👋     

> __< jpk68:matrix.org >__ Hello     

> __< syntheticbird >__ Hello     

> __< jeffro256 >__ Howdy     

> __< articmine >__ Hi     

> __< rucknium >__ 2. Updates. What is everyone working on?     

> __< syntheticbird >__ me: warning people to STAY HYDRATED 🚰     

> __< jeffro256 >__ me: reviewing upstream PRs, implementing feedback for FCMP++/CARROT PRs, writing documentation for existing code      

> __< rucknium >__ me: Keeping stressnet stressed with transaction spam. Helping identify stressnet bugs.     

> __< DataHoarder >__ updated my tooling and go-p2pool test to support beta stressnet (which works vastly better than alpha for the purposes of mining, so far, even with the current tx spam levels)     

> __< jpk68:matrix.org >__ Making some patches, and have also ostensibly finished the daemon integration for I2P SAM. Waiting on sone feedback :)     

> __< jberman >__ me: continuing reviewing jeffro's Carrot/FCMP++ hot-cold wallet PR, continuing investigating the observed stressnet wallet double spend error with rucknium:monero.social's help     

> __< rucknium >__ 3. emsczkp research Bulletproofs* Milestone 2 completed (https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/626#note_36734).     

> __< emsczkp:matrix.org >__ Hi everyone! this updated version of the paper provides the proofs of the main theorems establishing the security of the BP* folding scheme. In particular, Theorem 1 proves that the modified AC proof for Bulletproofs is complete, HVZK, and special sound. Before introducing the BP* folding scheme, the paper presents an intermed [... too long, see https://mrelay.p2pool.observer/e/-6bkoJALcmlnOWtT ]     

> __< emsczkp:matrix.org >__ The revised version also includes some changes with respect to the previous draft. In particular, it introduces a new algebraic verifier map V^comm and its relaxed version. This required the introduction of additional error terms in both the accumulator and the accumulation proof.     

> __< emsczkp:matrix.org >__ Overall, the main purpose of this step is the security proof      

> __< emsczkp:matrix.org >__ I've added more details in the GitLab update comment     

> __< jberman >__ sounding like great progress!     

> __< rucknium >__ emsczkp:matrix.org: Thank you! After completing Milestone 2, did you uncover anything that makes Milestone 3 (extend Bulletproofs* to Generalized Bulletproofs) more difficult or easier?     

> __< emsczkp:matrix.org >__ thanks, for the step 3 i think it will be appropriate to go into detail about GBP's relation and security proofs, but the folding scheme now appears to me extendable to GBP     

> __< emsczkp:matrix.org >__ i can't say for sure, but i see good foundations     

> __< rucknium >__ Do you have more discussion of this item or questions for emsczkp:matrix.org  at this time?     

> __< rucknium >__ Thank you, emsczkp:matrix.org .     

> __< rucknium >__ 4. Post-quantum encryption (https://github.com/monero-project/research-lab/issues/151#issuecomment-4412416686). Jamtis (https://gist.github.com/tevador/639d083c994c1ef9401832c08e2b7832#appendix-c-instant-sync-protocol).     

> __< emsczkp:matrix.org >__ rucknium: Thank you!     

> __< tevador >__ I have no significant updates for today.     

> __< rucknium >__ Anyone else have comments or questions on this item?     

> __< tevador >__ I think that with the implementation of Polyseed in the official wallet (big thanks to rbrunner), it makes sense to directly implement Jamtis and skip the Carrot hierarchy to save 1 Polyseed bit.     

> __< rbrunner >__ You mean no "Carrot key hierarchy" feature bit, but a "Jamtis" feature bit?     

> __< tevador >__ Yes, exactly     

> __< jeffro256 >__ tevador: I disagree, I still think that there's value in having a hierarchy with enchanced features and some quantum privacy which is backwards compatible and indistinguishable from existing addresses     

> __< articmine >__ What would be the impact on the timing of the HF  here?     

> __< jberman >__ I don't think we need to make a decision on that until FCMP++ / Carrot (without the Carrot key hierarchy) is 100% merged upstream in the first place. It'll be a question of what to work on/prioritize next at that point/what the timeline to Jamtis versus Carrot hierarchy would be expected to be     

> __< tevador >__ Jamtis is strictly superior to the Carrot key hierarchy     

> __< rbrunner >__ Well, skipping the Carrot key hierarchy and go directly to Jamtis is of course a much bigger question than any feature bits alone :)     

> __< jberman >__ articmine: 0 impact     

> __< tevador >__ The only reason to introduce an intermediate wallet type would be if Jamtis was severely delayed for some reason (I don't forsee that at the moment).     

> __< rbrunner >__ Looks like a hard decision to me. Both pathes have advantages and disadvantages     

> __< jpk68:matrix.org >__ FWIW, having multiple intermediate addressing protocols (which will each presumably be used for just a few years) in the codebase would seemingly create quite a large attack surface, and that code will have to be maintained forever if we are to keep restore functionality     

> __< rbrunner >__ Just wondering, couldn't a switch to Jamtis get complicated if it should turn out that it brings a significant performance hit?     

> __< jeffro256 >__ tevador: Except in metrics that I previously mentioned: backwards compatability, and by extension, ease of implementation, and indistinguishability      

> __< rbrunner >__ Do we have already any idea how Jamtis might perform     

> __< jeffro256 >__ "Details table" section in https://github.com/monero-project/research-lab/issues/151#issuecomment-4281932714     

> __< rbrunner >__ "Just a few years" is quite a lot in the life of a cryptocurrency, as they develop today, if you ask me     

> __< tevador >__ jeffro256: no protocol with the features of Jamtis can compete on those metrics. But you are technically correct. However, Carrot is also beaten by CryptoNote on the 'ease of implementation' metric.     

> __< DataHoarder >__ 19:25:56 <tevador> Jamtis is strictly superior to the Carrot key hierarchy     

> __< DataHoarder >__ the reason for Carrot though is being still backwards compat with address format as mentioned     

> __< rbrunner >__ Ah, yes, sorry I forgot this table. Where we ruled out schemes that would run for freaking hours!     

> __< tevador >__ Jamtis scanning performance should be roughly on par with Carrot, except for wallets with a lot of received external payments that need CSIDH decryption.     

> __< articmine >__ What about TX sizes?     

> __< jeffro256 >__ Unpruned parts of the tx (the part that wallets download) would be 31% larger      

> __< jeffro256 >__ For BC512      

> __< tevador >__ Jamtis aims for on-chain indistinguishability, which implies identical tx sizes. But there will be ~132 bytes in tx extra for all transactions (even legacy ones).     

> __< rbrunner >__ IMHO it could well be that we can go into a focussed decision process only with the FCMP++ and Carrot hardfork successfully behind us, not yet now     

> __< tevador >__ Yes, it's definitely too early to decide. I was just stating my opinion.     

> __< jeffro256 >__ Yes, TBC, the bit that decides whether unpruned tx sections rises by 31% is whether or not we collectively decide to support Jamtis in some wallets AND plan for on-chain distinguishability. If we stuck with only the Carrot hierarchy, then tx sizes would stay down. But if some wallets support Jamtis-PQ and we decide that all  [... too long, see https://mrelay.p2pool.observer/e/oZvloZALcUFpZnRF ]     

> __< articmine >__ A 31% increase in sizes is less than 1 year of Neilsen's law     

> __< tevador >__ It's the price to pay for PQ privacy with static address support.     

> __< rbrunner >__ Well, right now only storage prices rise trememdously. Thanks, AI     

> __< rbrunner >__ Will give quite a dent in that law     

> __< articmine >__ This is very short term. I prefer to focus on the long term      

> __< articmine >__ Yes I am very much aware of the SSD pricing issue      

> __< rbrunner >__ Understood. And still, we want to offer a cryptocurrency that works today, for various values of "today" for the next years     

> __< rbrunner >__ Well, should probably have written "works well"     

> __< rucknium >__ More discussion of this for now?     

> __< rucknium >__ 5. FCMP beta stressnet (https://github.com/seraphis-migration/monero/releases/).     

> __< rucknium >__ We are pushing up the long term median block size now. https://stressnetnode1.redteam.cash/     

> __< rucknium >__ We produced a 17MB block recently: https://stressnet.p2pool.observer/block/cdae2957c5c0034d7b40a79ba636b31e01635456ab6398e3a3e2e68caebd6958     

> __< DataHoarder >__ have been seeing an increase on block sizes (recent ones have quite a list of txs) https://stressnet.p2pool.observer/block/cdae2957c5c0034d7b40a79ba636b31e01635456ab6398e3a3e2e68caebd6958 thanks to the spam     

> __< DataHoarder >__ heh. yep that block. there is a second one as well https://stressnet.p2pool.observer/block/d36b9d9f057c972d54293bb7d2c57e475a97a9d34ddebe9e8973b3bf641adcf8     

> __< rucknium >__ Thanks to DataHoarder[m]  for getting his FCMP block explorer working :)     

> __< jeffro256 >__ Not a whole lot of updates from me. Still bugging hardware wallet people. Working on hot/cold PR, thanks j-berman. I'm about to push a couple business PRs to upstream      

> __< DataHoarder >__ my p2pool miner will stop packing txs past 128K block blob byte sizes, but I can deal with that. it's 70 KiB / 128 KiB so far and approaching quick :)     

> __< rucknium >__ I decided to turn some of my spam wallets to high fees to push block sizes up and exhaust the wallets' funds.     

> __< DataHoarder >__ anything else to do to help push sizes further? I have p2pool mining code which is quite efficient at packing these sudden high fee txs     

> __< jberman >__ Stressnet generally seems to continue to run smooth. Unfortunately, the issue I brought up last week of wallets sporadically erroring on tx construction with double spend errors is actually not solved yet (seems I mistakenly mis-identified the root cause of the issue, realized thanks to rbrunner7:monero.social's pushback on t [... too long, see https://mrelay.p2pool.observer/e/jM6KopALSlNURmpR ]     

> __< DataHoarder >__ I can send funds or mine to other addresses if that'd help Rucknium :)     

> __< rucknium >__ DataHoarder: DataHoarder: We hit another long-term median ceiling again. I don't know how long we will be scraping that ceiling until it gives way. I'd guess 1-4 days.     

> __< DataHoarder >__ additionally could make many miner outputs on coinbases, that send each to a different wallet (and with some changes, maybe multiple per wallet)     

> __< rucknium >__ DataHoarder: I may need more funds in a week to two. You can pay me back for those high-fee mined blocks :D     

> __< DataHoarder >__ so far I have been sending to the faucet, give an address and I can send via the wallet :)     

> __< DataHoarder >__ also, for anyone mining or spamming, if you'd like to get listed on the blocks list with attribution or https://stressnet.p2pool.observer/pools, or display payment details, you can give an address+viewkey     

> __< rucknium >__ I chose to exhaust funds on a few wallets because eventually big wallets get slower. Big = lots of historical txs.     

> __< jeffro256 >__ Same here, I've built up some miner funds , let me know where to send em      

> __< rucknium >__ My main stressnet wallet: 9uk5eY8waibQp7MMwpo3JrcMFatbiGtHKcTHMEzxWE39An8R3VTbztTPcJ7MDYEVVrAC4ueSV5KzP4GMTTwGoGBjAtKFp7i     

> __< rucknium >__ Thanks.     

> __< DataHoarder >__ sent ~640 tXMR your way.     

> __< rucknium >__ More discussion about stressnet?     

> __< rucknium >__ DataHoarder: Thank you.     

> __< DataHoarder >__ how long is v2 beta stressnet expected to continue for?     

> __< articmine >__ I would suggest that it run until the hard limit 100 MB code issues are addressed      

> __< articmine >__ So we'll afy the HF     

> __< articmine >__ after      

> __< DataHoarder >__ 100MB blob byte size or weight size?     

> __< articmine >__ DataHoarder: Enough to trigger the code issues     

> __< DataHoarder >__ privacy wise, would it be proper in these sweep cases https://stressnet.p2pool.observer/tx/b5ec0584c6da18cc13ecc71a95609bd801cd1ee2379b6bc6bb12f18cc5ccd339 to not send 0.000000000000 XMR back as change?     

> __< jberman >__ It would be nice to solve the following big issues observed: sporadic double spend errors, higher ban frequency, possibly node's pool not catching up to another. And get p2p SSL and hot/cold wallet support running / tested. It would also be very nice to get the major RPC getblocks.bin speedup implemented too because I expect t [... too long, see https://mrelay.p2pool.observer/e/3JywopALUjNmcFh6 ]     

> __< articmine >__ Yes      

> __< jberman >__ the former "nice-to-solves" would be nice to solve to be certain if the cause is tx relay v2, pre-existing, or anything FCMP++/Carrot related (though that is not my current suspicion)     

> __< jberman >__ tx relay v2 though I guess is a big +1 especially for FCMP++ once tx sizes are much larger, so it's indirectly related in that way     

> __< rucknium >__ Would the RPC getblocks.bin speedup affect wallets' txpool requests at all?     

> __< jberman >__ rucknium: ya that's what I'm referring to there (the pool fetching part of getblocks.bin, not the blocks fetching part)     

> __< jeffro256 >__ DataHoarder: You need 1 scannable output per tx as per CARROT rules. Also, if you share your viewkey and the public can see amounts of UTXOs , they can calculate that the output has 0 XMR anyways     

> __< rucknium >__ Ah good.     

> __< DataHoarder >__ jeffro256: yeah, this case is due to viewkey sharing specifically that it decrypts the 0 XMR. I guess it'll be better with full Carrot where those outputs end up internal instead of the special external change case.     

> __< jberman >__ The main reason the sweep case has 0 amount change back to sender is so that seeds remain compatible for background syncing and light wallet support as currently implemented (without needing to reveal your key images to a daemon/server)     

> __< rucknium >__ I think my max spam pace is being limited by slow wallet-node interaction. I think I can only get 25-30 wallets connected per node before adding more wallets decreases total spam volume. And I don't have infinite nodes.     

> __< DataHoarder >__ right! the tx needs to be picked up by a spend / view balance wallet     

> __< rucknium >__ If we want to go a lot higher with tx volume, faster RPC would be very helpful I think.     

> __< DataHoarder >__ Rucknium: I see a lot of txs coming as discretized units instead of batches which is spamming some of my logs, so somewhere it's hitting a bottleneck     

> __< DataHoarder >__ example recent ones https://privatebin.net/?80e0dae714f31b58#6LpSPFNkyXywMyMBsrPmBPHDK7NBip7buEa7yaGB6HWP     

> __< jberman >__ ya it's known when there's a lot of txs in the pool, the /getblocks.bin request can be extremely slow and prevent the daemon from doing anything: https://github.com/seraphis-migration/monero/issues/293     

> __< rucknium >__ Discretized units instead of batches means what?     

> __< DataHoarder >__ afaik the verification is faster (1.5s for the recent big blocks)     

> __< DataHoarder >__ Rucknium: on ZMQ interface new txs can be notified as one event instead of individual ones. Usually the node is fast enough that it aggregates them a bit, but recently it has started sending many individual events (which adds some overhead)     

> __< rucknium >__ jberman:monero.social: Will the new getblock.bin code make txpool requests become a non-blocking operation?     

> __< rucknium >__ DataHoarder: Do you think that is related to clumping in p2p tx messages?     

> __< jeffro256 >__ It will still be blocking      

> __< jberman >__ rucknium: no, it can make the request take ~0.1s as opposed to 3-15s+ per wallet. Making it a non-blocking operation is another potential improvement mentioned in that issue     

> __< DataHoarder >__ yeah, maybe they are less clumped, so they don't come at once, or the monero code takes time verifying them. they also come very quick one after each other     

> __< jeffro256 >__ Unfortunately that's just how the blockchain DB and higher level code work      

> __< rucknium >__ e.g. https://github.com/Fountain5405/monerosim/issues/3 "Clumping in transaction broadcast messages"     

> __< DataHoarder >__ I am talking about post-verification, where it notifies listeners via ZMQ. I can't remember if that's done per clump on the wire message, or on the go as txs get verified     

> __< rucknium >__ I think we had some attrition with the total number of nodes on the network. IMHO a smaller network causes less tx message clumping. I don't know if that could be causing what you're seeing.     

> __< rucknium >__ 6. monerosim (https://github.com/Fountain5405/monerosim).     

> __< DataHoarder >__ code on my side is performant, so doesn't make much of a difference except sending ~400 new jobs to xmrig instead of 2-10 per block     

> __< rucknium >__ gingeropolous:monero.social gave an update before the meeting:     

> __< rucknium >__ > unfortunately I won't be able to attend live during the meeting. But I'm continuing to push monerosim towards mainnet fidelity. Current results here: https://github.com/Fountain5405/monerosim/blob/main/docs/20260620_network_topology_study.md . TL;DR, it seems the hypothesis was right, that a 100% reachable network behaves differently than main net.     

> __< rucknium >__ > the sim currently running is the "churning" - nodes turning on and off throughout the sim, as opposed to always on.     

> __< rucknium >__ I think someone has one last question for the meeting.     

> __< emsczkp:matrix.org >__ Can I quickly ask about the Milestone ? Do people think another review slot is needed next week, or can we consider the current state sufficient for approval? Thanks     

> __< rucknium >__ IMHO this depends on if anyone plans to spent time reading the revised paper at this point.     

> __< rbrunner >__ Yeah, feedback from one of our cryptographers would be interesting     

> __< rbrunner >__ Even as they are surely quite busy already ...     

> __< ofrnxmr >__ > <jberman> It would be nice to solve the following big issues observed: sporadic double spend errors, higher ban frequency, possibly node's pool not catching up to another. And get p2p SSL and hot/cold wallet support running / tested. It would also be very nice to get the major RPC getblocks.bin speedup implemented too b [... too long, see https://mrelay.p2pool.observer/e/i6mSo5ALV0N2THow ]     

> __< ofrnxmr >__ I'm running p2p ssl     

> __< rucknium >__ We will see if anyone comments here and then decide about approval timeline.     

> __< ofrnxmr >__ On stressnet, on 2 nodes, and seems to be a third node on sttessnet also running it     

> __< rucknium >__ We can end the meeting here. Thanks everyone.     

> __< ofrnxmr >__ (sorry for the interruption)     

> __< articmine >__ Thanks      

> __< jberman >__ rucknium: I will try to make time over the next week, but FWIW the summary does sound like solid progress to me     

> __< rucknium >__ Thanks, jberman:monero.social     

> __< emsczkp:matrix.org >__ jberman: Thank you     

> __< vtnerd >__ Crap missed reminders about meeting. I was focused on the fido2 encryption lib, initial but not yet complete code is at github.com/vtnerd/fhse     

> __< vtnerd >__ There's already the base structure with tests and ci     

> __< DataHoarder >__ tevador: is there any implementation of current jamtis progress/research other than the gist?     

> __< tevador >__ There is only the specification in the gist, no code yet.     



# Action History
- Created by: Rucknium | 2026-06-24T14:44:48+00:00
