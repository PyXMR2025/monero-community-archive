---
title: Monero Research Lab Meeting - Wed 12 November 2025, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/1296
author: Rucknium
assignees: []
labels: []
created_at: '2025-11-11T23:41:50+00:00'
updated_at: '2025-11-25T23:25:27+00:00'
type: issue
status: closed
closed_at: '2025-11-25T23:25:27+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/meeting.html?p1=1440)

Main discussion topics:

1. Greetings

2. Updates. What is everyone working on?

3. [Coinbase Consolidation Tx Type](https://github.com/monero-project/research-lab/issues/108).

4. [Transaction volume scaling parameters after FCMP hard fork](https://github.com/ArticMine/Monero-Documents/blob/master/MoneroScaling2025-11.pdf). [Revisit FCMP++ transaction weight function](https://github.com/seraphis-migration/monero/issues/44).

5. [Simple Market-Based Monero Fee Proposal](https://github.com/monero-project/research-lab/issues/152).

6. [FCMP alpha stressnet](https://monero.town/post/6763165).

7. Mining pool centralization: [Temporary rolling DNS checkpoints](https://github.com/monero-project/monero/issues/10064), [Share or Perish](https://github.com/monero-project/research-lab/issues/146), and [Lucky transactions](https://github.com/monero-project/research-lab/issues/145).

8. Any other business

Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: Rucknium

Previous meeting agenda/logs:

#1292 

# Discussion History
## ArticMine | 2025-11-12T06:01:56+00:00
I am requesting:
1) That the latest version https://github.com/ArticMine/Monero-Documents/blob/master/MoneroScaling2025-11.pdf be included instead of the July version. 
2) That the "Simple Market Based Monero  Fee Proposal" be discussed as a separate item on the agenda from my work. 

## Rucknium | 2025-11-18T22:30:57+00:00
Log

> __< DataHoarder >__ Don't have much more time to gather more data (can adjust / tune up this and make charts later) but some interim sweep data from mini. The rest is being generated at the moment https://git.gammaspectra.live/WeebDataHoarder/p2pool-sweep-analysis/src/branch/master/mini.md     

> __< DataHoarder >__ We know the total value swept, and fee, data is available as CSV on https://git.gammaspectra.live/WeebDataHoarder/p2pool-sweep-analysis/src/branch/master/data (for main/mini)     

> __< DataHoarder >__ picked only sweeps of 8 >= inputs and at least 80% of owned decoys by same miner across all input rings     

> __< DataHoarder >__ FCMP++ Estimate is currently fee * 4, without taking into account what fee level the miner picked (assuming they keep the same behavior). If input count > 128, I add an extra fudge, but should get better numbers for the constant cost of splitting a sweep later on     

> __< DataHoarder >__ for people sweeping even 10-20 inputs their fees go from 2-3% to 10-15% of the mined value     

> __< DataHoarder >__ I'll post the full output of the program later today, my RPC full node is quite slow :)     

> __< articmine >__ Yes fees are in my latest proposal > <DataHoarder> Have we gotten final values for fees for given byte size for FCMP++? Otherwise I'll assume ~4x byte size and just list that, no "new fee" just old one     

> __< articmine >__ The increase in the minimum penalty free zone is from 300000 to 1000000. bytes      

> __< articmine >__ This deals with most of the transaction weight increase      

> __< DataHoarder >__ That's for block sizing mainly, right? I guess it affects the default priority transactions are sent at      

> __< DataHoarder >__ I'll update the code after, it's still running :)     

> __< rucknium >__ MRL meeting in this room in one hour.     

> __< rucknium >__ In two hours I mean     

> __< rucknium >__ Meeting time! https://github.com/monero-project/meta/issues/1296     

> __< rucknium >__ 1. Greetings     

> __< DataHoarder >__ hello     

> __< jberman >__ waves     

> __< rucknium >__ 2. Updates. What is everyone working on?     

> __< DataHoarder >__ P2Pool Sweep scan just finished (see mini https://git.gammaspectra.live/WeebDataHoarder/p2pool-sweep-analysis/src/branch/master/mini.md and main on that repo     

> __< DataHoarder >__ ^ working on getting relevant numbers out of that     

> __< ofrnxmr >__ testing fixes for fcmp++ ooms w/ berman and mayhem     

> __< jberman >__ Submitted PR's to mitigate OOM's caused by FCMP++ verification on the stressnet, submitted a PR to fix locking behavior in monerod + a couple other daemon fix PR's upstream from stressnet, reviewed 0xfffc:monero.social  's tx relay v2 + dynamic span + runaway span fix, continuing with some OOM testing and getting GUI binaries prepared hopefully for alpha stressnet v1.5     

> __< rucknium >__ me: Packet analysis using Kopyciok, Y., Schmid, S., & Victor, F. 2025. "Friend or Foe? Identifying Anomalous Peers in Moneros P2P Network"  as an alternative to the peer ID spoofing. So far, the ban list nodes are highly correlated with some of the anomalous packet categories, but none of them have zero percent false positive  [... too long, see https://mrelay.p2pool.observer/e/wIqdlMgKbFowdGFy ]     

> __< vtnerd >__ Hi - forgot about time change - working on subaddr lookahead client side. Ran into a db issue (again) so investigating that first     

> __< rucknium >__ I think I pinged everyone on GitHub when I forgot to scrub the "" in front of usernames in the logs 😅 . I'll remember to do that in the future or scrub it with the formatting script.     

> __< rucknium >__ And I will now deliberately ping jeffro256:monero.social     

> __< rucknium >__ 3. Coinbase Consolidation Tx Type (https://github.com/monero-project/research-lab/issues/108).     

> __< DataHoarder >__ Fun topic. It may affect other miners too, but a fee increase for P2Pool under FCMP++ might make it unprofitable compared to centralized options, even when P2Pool main for example reduces outputs with smaller PPLNS window size     

> __< rucknium >__ The main reasons to do this are to have reasonable consolidation fees for p2pool miners and to reduce blockchain bloat from p2pool consolidations.     

> __< ofrnxmr >__ How would this reduce bloat post-fcmp?     

> __< DataHoarder >__ From recent crunched data using identified sweeps on-chain (see https://git.gammaspectra.live/WeebDataHoarder/p2pool-sweep-analysis/src/branch/master/mini.md towards the end) it's not as bad for recent outputs on Mini     

> __< ofrnxmr >__ how     

> __< DataHoarder >__ it's still increasing 1-2.5% fee relative to swept value to 4-10%     

> __< rucknium >__ Not to attack p2pool, but I will try to take stock of p2pool: The p2pool share of hashpower has stayed at 5-10 percent for years. p2pool also did little to prevent the Qubic episode.     

> __< jberman >__ p2pool has an alternative option which is to maintain long term state in its sidechain of who has contributed what hashrate across epochs, and increase min payout     

> __< DataHoarder >__ These sweeps had a different reason to allow consolidation, which is that they were easily identifiable regardless. Under FCMP++ that is no longer the case, so the topic is mainly an efficiency issue     

> __< DataHoarder >__ as jberman said the alternative is to keep long term state in p2pool (no longer ephemeral sidechain)     

> __< DataHoarder >__ p2pool share has stayed lower, either due to complex setup to mine, even when good programs and integration in GUI exist     

> __< DataHoarder >__ effectively losing 5-10% of mined value when sweeping as is at the moment would kill p2pool     

> __< DataHoarder >__ long term state would be needed, as people already abandon p2pool when awaiting for a share (increasing payout minimum = increasing work to get a share at the moment)     

> __< rucknium >__ So you would set a minimum payout for p2pool if the sidechain had long-term state? Or payout for long time windows, regardless of how much a miner earned in the period?     

> __< DataHoarder >__ I'd be keen for the second option, as to make it handle payouts without wallets the only way it has to pay is ... finding blocks     

> __< DataHoarder >__ Allowing a balance to accumulate past PPLNS windows can open for specific griefing attacks as well     

> __< DataHoarder >__ The other option considered that doesn't require much except from miners is they might optionally decide to mine their own sweep transactions in their own block founds     

> __< DataHoarder >__ And do so for other miners, when block space allows for it (empty-ish blocks)     

> __< rucknium >__ DataHoarder: DataHoarder: Such as pool switching to get an advantage?     

> __< rucknium >__ Such as below the min relay fee?     

> __< DataHoarder >__ rucknium: depending how and when miners can choose to get paid out, specially as there's not much other than the pubkeys as way to identify as miner, they can cause early payouts, or orphan out someone else's share more efficiently     

> __< DataHoarder >__ yeah. an example given is zero-fee txs, but these would be kept local/shared out of band     

> __< rucknium >__ Then other nodes would not have the slow-to-verify txs and block propagation would be slower. That could increase the p2pool orphan rate     

> __< DataHoarder >__ It would, yes     

> __< DataHoarder >__ Miner outputs are already special (exposed amounts, generally agreed to only able to have main addresses mine on it, specially under carrot)     

> __< DataHoarder >__ Allowing an optional single-time one way sweep for miners to efficiently aggregate these might be relevant. Or not. That's why I asked the topic brought     

> __< DataHoarder >__ Even 9 inputs totaling 0.01 XMR end up with 1.2% fee on current system, end up with 5% assuming 4x at same picked fee level      

> __< rucknium >__ I wasn't aware of these other ideas to reduce consolidation costs, especially the long-term sidechain state idea.     

> __< jberman >__ can you expand on that? I imagine current p2pool also has a similar griefing vector > <DataHoarder> Rucknium: depending how and when miners can choose to get paid out, specially as there's not much other than the pubkeys as way to identify as miner, they can cause early payouts, or orphan out someone else's share more efficiently     

> __< DataHoarder >__ jberman: currently p2pool you get paid, even if the share ends up orphaned     

> __< jberman >__ why not keep track of orphans long term as well?     

> __< DataHoarder >__ block found is a block found. state tracking systems further than that that are account-less (aka, don't ask user to have additional keys to sign requests) end up with those problems     

> __< DataHoarder >__ Long term state tracking would need to get explored, regardless. I don't think we have a good level of detail on it currently, or sech1 pondered on it     

> __< jberman >__ it generally seems like a solvable problem to me     

> __< jberman >__ (not easily solvable, but solvable)     

> __< ofrnxmr >__ "effectively losing 5-10% of mined value when sweeping as is at the moment would kill p2pool" this is purely an issue with the size of the payouts.     

> __< ofrnxmr >__ Its 10% because payouts are only 10x the size of the fee     

> __< DataHoarder >__ it is definitely an issue on size of payouts, but only way that p2pool can payout without intermediary is via wallets, yes     

> __< DataHoarder >__ P2Pool Main has dynamic PPLNS window and as such it mainly stays at around 3-5% under FCMP++ increase     

> __< rucknium >__ Smart contracts on the side chain? :D     

> __< ofrnxmr >__ centralized pool payouts are like 100x the size of p2pool. I dont see why p2pool needs payouts that are miniscule     

> __< DataHoarder >__ though small miners don't mine there     

> __< DataHoarder >__ centralized pool payouts can already do the zero fee tx (or even normal txs) and include them in their own blocks only, anyhow     

> __< ofrnxmr >__ they dont need to though     

> __< ofrnxmr >__ They just have high payouts     

> __< DataHoarder >__ they also have an account-based database that can just keep track of the state     

> __< ofrnxmr >__ the pool takes a % of the %, its in their own economic interests to charge tx fees even on their own withdrawals     

> __< DataHoarder >__ knowledge of addr = you can click and payout.     

> __< DataHoarder >__ except on p2pool they are all public, and the only way it can payout is by making blocks     

> __< sech1 >__ long term state tracking and fixed min payouts can be gamed by large hashrate miners. It was what I wanted initially for p2pool, but I couldn't figure out how to make it fair for small miners     

> __< sech1 >__ the problem is p2pool can only payout in 0.6 XMR chunks - it can't pay more or less per block     

> __< DataHoarder >__ it could be larger, depending on txs fees at the moment     

> __< DataHoarder >__ it also can't choose not to pay out     

> __< DataHoarder >__ it will keep finding blocks     

> __< sech1 >__ no matter which logic is used, big hashrate miners can game it and switch their mining wallets as soon as they get paid out more than they would get under fair distribution     

> __< sech1 >__ because if a small hashrate miner doesn't get paid in a block (despite having shares in PPLNS window), that small piece of the block reward will go to someone else     

> __< sech1 >__ and someone else can "run away with the money" (change the mining wallet address)     

> __< jberman >__ you give a larger proportion of the reward to the smaller miners once they reach min payout. large hashrate miners aren't necessarily incentivized to switch because then p2pool breaks down and isn't usable. it's similar as to why a larger hash rate miner doesn't immediately switch to a centralized pool once they receive a shar [... too long, see https://mrelay.p2pool.observer/e/2faElcgKb09NYmcy ]     

> __< sech1 >__ I tried to simulate "p2pool with memory and min payout". Even when all miners mine fairly, small hashrate miners got underpaid. I did it in 2021 before releasing p2pool (the idea was to have the normal min payout and long term tracking).     

> __< sech1 >__ min payout logic works and works well when there is a pool wallet. But when there is a strict 0.6 XMR that needs to be paid out with each block - it leads to problems and some miners get overpaid while some others get underpaid     

> __< DataHoarder >__ on a "trusted" setup (you expect participants to not disappear and sign when needed) mining to multisig, then allowing multisig payouts when intended can work, but not for trustless p2pool     

> __< jberman >__ you have to give a larger proportion of future payouts to the smaller miners who miss prior blocks     

> __< sech1 >__ Of course my simulations were not very rigorous and "scientific". Maybe something for MRL researchers to look at     

> __< jberman >__ p2pool can find multiple blocks within a single window, ya?     

> __< sech1 >__ yes     

> __< DataHoarder >__ p2pool would also need to handle deep reorgs as part of payouts if we need to track "paid out" state across time     

> __< sech1 >__ jberman I tried several different variants of how to fix the disproportion in payouts. I couldn't find the working logic     

> __< DataHoarder >__ Then this looks like the path to take a closer look sech1 to get it workable?     

> __< jberman >__ I do think it may be worth a revisit     

> __< DataHoarder >__ It's definitely better to produce only as few outputs as needed, alternatively if found unworkable a combination of both + maybe making our own out-of-band tx inclusion system might be relevant for P2Pool to allow cheaper sweeps under existing setup     

> __< sech1 >__ There was one "working" variant. It's to have a hard cutoff. For example, 0.001 XMR min payout - so no more than 600 payouts per block. PPLNS window can be 6000 shares, and only miners with 10+ shares get paid with each block     

> __< sech1 >__ It cuts off small hashrate miners completely, but everyone else gets paid fairly     

> __< DataHoarder >__ Yeah, the closer to solo mining you are the better it is :)     

> __< sech1 >__ So if your hashrate is < 1/600 of pool hashrate, you don't get paid at all and have to switch to a smaller pool     

> __< DataHoarder >__ ^ which ends with streaks of several weeks without blocks found and people making "day XX of no payouts on nano" on reddit and people hopping around away from p2pool     

> __< DataHoarder >__ they can get shares there, but no found blocks to pay out with :)     

> __< rucknium >__ There are actually a few papers about p2pool with smart contracts.     

> __< sech1 >__ 1/600 = 420 kh/s for p2pool-main at the moment, and 31 kh/s for p2pool-mini     

> __< sech1 >__ and 4 kh/s for p2pool-nano     

> __< sech1 >__ so it doesn't really work for 1 kh/s miners     

> __< sech1 >__ even if they get lucky, luck averages out when you need to have 10+ shares in PPLNS window to get paid     

> __< DataHoarder >__ the issue sech1 raised as well, say a pool gets mined by many small miners and a couple big miners. Big miners get payouts, are done with it, leave. Now small ones opt to get paid out. But effectively they can only get still dust but need to find full blocks (where does the rest of XMR go to? :D)     

> __< DataHoarder >__ tbh sech1 if we can have long term windows, mini/nano would not be relevant     

> __< sech1 >__ long term windows means p2pool needs to sync much more and use much more memory     

> __< DataHoarder >__ at that level shares could come faster     

> __< DataHoarder >__ indeed, that'd requite also syncing this data when miners come in     

> __< DataHoarder >__ my long-term mini block db (with compact compressed blocks, one full block every 32) is ~28 GiB for its lifetime     

> __< DataHoarder >__ 18 GiB for main     

> __< DataHoarder >__ nano is 1.1 GiB for just a couple of months.     

> __< DataHoarder >__ if "balance" is considered as long term state, I don't know if stuff similar utreexo would be applicable here, by moving the needs to the miner side     

> __< DataHoarder >__ that'd make p2pool mining more complex, though.     

> __< rucknium >__ Any more about this topic for now? Some things to consider and investigate.     

> __< DataHoarder >__ I think looking into long-term state sech1 would be relevant before concluding this topic ^ but can be kept for another meeting later on (or closed here if the consensus is no coinbase sweeps, nothing for p2pool)     

> __< jberman >__ > long term windows means p2pool needs to sync much more and use much more memory     

> __< jberman >__ more sync yes, more memory not necessarily but storage yes. I think the main goal here is offloading work from the Monero chain onto p2pool for this     

> __< DataHoarder >__ I wrote the message before yours rucknium, I mean "concluding" as closing the issue. I don't think we need to discuss further today     

> __< rucknium >__ 4. Transaction volume scaling parameters after FCMP hard fork (https://github.com/ArticMine/Monero-Documents/blob/master/MoneroScaling2025-11.pdf). Revisit FCMP++ transaction weight function (https://github.com/seraphis-migration/monero/issues/44).     

> __< jberman >__ I opened a PR to set weight approximately equal to byte size here: https://github.com/seraphis-migration/monero/pull/232     

> __< articmine >__ I uploaded the proposed weights spreadsheet      

> __< jberman >__ haven't had the chance to dig into articmine:monero.social 's latest scaling proposal     

> __< articmine >__ With respect to the scaling side the change is to cap the block rather than the short term median to 16x ML     

> __< articmine >__ As for the weights. The x in 2 out size follow a good linear regression with the number of inputs      

> __< articmine >__ One can actually calculate the weight with a 2 parameter linear equation      

> __< articmine >__ Then have an add on for additional outputs      

> __< articmine >__ The one question I see is do we want to adjust at all for powers of 2 and verification time jumps?     

> __< articmine >__ I am free either way      

> __< articmine >__ The adjusted weights do that for up to 8 in     

> __< articmine >__ The raw weights do not      

> __< articmine >__ Both sets of weights follow the principle of roughly equal to size in the PR     

> __< articmine >__ As for fees. There proposal is flat like now with a 2 In 2 out low fee of about 47 micro XMR     

> __< articmine >__ Very close to the current fees     

> __< articmine >__ Any questions at this time      

> __< rucknium >__ 5. Simple Market-Based Monero Fee Proposal (https://github.com/monero-project/research-lab/issues/152).     

> __< rucknium >__ articmine:monero.social suggested that this agenda item be split from the previous one.     

> __< articmine >__ Thank you      

> __< rucknium >__ Any discussion of this?     

> __< rucknium >__ 6. FCMP alpha stressnet (https://monero.town/post/6763165).     

> __< jberman >__ repeating my update from before: Submitted PR's to mitigate OOM's caused by FCMP++ verification on the stressnet, submitted a PR to fix locking behavior in monerod + a couple other daemon fix PR's upstream from stressnet, reviewed  0xfffc 's tx relay v2 + dynamic span + runaway span fix, continuing with some OOM testing and getting GUI binaries prepared hopefully for alpha stressnet v1.5     

> __< jberman >__ I'm hoping v1.5 will be the last release of alpha stressnet, and we can move to beta stressnet next. I'd say the biggest TODO for beta is settling on scaling      

> __< articmine >__ Does the 16x cap work?     

> __< rucknium >__ When a tx has a high number of inputs, FCMPs need to consume more RAM than rings because each ring is a separate proof, but a FCMP is one single proof for all inputs. Right?     

> __< jberman >__ articmine: need to review the 16x cap in totality with the proposal     

> __< kayabanerve:matrix.org >__ Sorry for missing the meeting thus far. My update is just what I've done due to being pinged by jberman re: memory use.     

> __< kayabanerve:matrix.org >__ I am against adding transparent TXs for reduced fees for any usecase.     

> __< kayabanerve:matrix.org >__ FCMPs do need to simultaneously represent the state of all inputs within an FCMP when verifying, causing higher RAM use. I identified an oversight which brought us down 33%. jberman identified a problem area that I did the math on and identified could be hundreds of MB. I then wrote a patch to attempt fixing it, which was bad  [... too long, see https://mrelay.p2pool.observer/e/m6e1lsgKM19GZGs2 ]     

> __< jberman >__ tbc, the latter change is an additional 66% reduction in RAM usage in exchange for ~3x slower verification      

> __< kayabanerve:matrix.org >__ It is not being suggested or merged at this time. It was solely an experiment for one specific area jberman identified, and I estimated was likely a problem.     

> __< rucknium >__ Is that because the CPU is working on raw computations or is the higher time because of RAM allocations?     

> __< articmine >__ Why amounts of RAM are we talking about?     

> __< ofrnxmr >__ 800mb vs 1.2gb     

> __< kayabanerve:matrix.org >__ But with a nontrivial amount of work (4-20 hours), could possibly implement the reduced memory without such computational overhead.     

> __< jberman >__ initial RAM 1.2GB, after first change to oversight 800mb, after this last change that isn't usable because it 3x's verification time 266mb     

> __< kayabanerve:matrix.org >__ Well, for the experiment, 266 MB vs 800 MB     

> __< kayabanerve:matrix.org >__ And that's just one specific spot which jberman identified as a top contender. As I've said prior, we could spend weeks going through the entire codebase for such improvements     

> __< articmine >__ It needs to be an ongoing project      

> __< rucknium >__ Judging by the ASNs of a lot of reachable nodes, a high share of reachable nodes are probably on VPSes, which usually have low RAM.     

> __< kayabanerve:matrix.org >__ rucknium:monero.social: The experiment was to transform a vector of sparse vectors into a single sparse vector. The issue is, you can no longer index into the outer vector for the elements for a specific vector. You have to iterate the entire sparse vector and filter as it's no longer organized.     

> __< ofrnxmr >__ rucknium: Im syncing on 2gb ram system rn     

> __< rucknium >__ ofrnxmr:monero.social: Stressnet?     

> __< ofrnxmr >__ Yss     

> __< jberman >__ mayhem69:matrix.org still no OOM?     

> __< ofrnxmr >__ 800mb change + runawayspans + dynamic span + malloc env variable. Single core     

> __< kayabanerve:matrix.org >__ We could use a HashMap, instead of a non-sparse vector, so we don't pay the cost of empty vectors (16 bytes for a nullptr and a length of 0, but we have thousands of them), but then we have the overhead of the HashMap. That's why it'd be some amount of hours to go through and decide the best way to represent this vector.     

> __< kayabanerve:matrix.org >__ The best way is probably as done in the experiment, but a single-pass filter, instead of the current linear filter, but that'd require rewriting how it's called and the actual verifier code.     

> __< ofrnxmr >__ jberman: Mayhem had an OOM w/o malloc env var, but added it. Not sure if OK now     

> __< kayabanerve:matrix.org >__ Hence why it'd be some time to resolve     

> __< mayhem69:matrix.org >__ jberman: I got an OOM on what seems like FMCP verification but I was running without MALLOC_ARENA_MAX=1 on that run and didn't have log-level 2 set, I've restarted and it seems to be fine so far for the last 8-10 hours. Still syncing and watching and will provide updates on if it OOM's again      

> __< jberman >__ Nice, thank you :)     

> __< rucknium >__ Thanks everyone for your work on this.     

> __< kayabanerve:matrix.org >__ I'll note that this not having runaway memory doesn't mean it won't require more memory, and that this may be fine albeit with a new min mem requirement     

> __< rucknium >__ Are you using a specific linear algebra crate for FCMP?     

> __< kayabanerve:matrix.org >__ what's linear algebra     

> __< kayabanerve:matrix.org >__  /s :p     

> __< kayabanerve:matrix.org >__ The Generalized Bulletproof crate has its own representation for linear combinations to its needs for use in cryptography. I don't believe there's any off-the-shelf library which would be usable.      

> __< kayabanerve:matrix.org >__ The provided impl is sane, using sparse representations to keep memory usage low. The non-sparse vector of sparse vectors was for a parameter which should've been small.     

> __< kayabanerve:matrix.org >__ It just isn't small here, it's ~1000, and then every input creates ~400 expressions, and most of them reference something with a _large_ index due to the layout of the circuit.     

> __< kayabanerve:matrix.org >__ So we had 128*1000*4000 * 16 bytes to denote an empty vector at the first 1000 positions before the final sparse vector at the end for terms for the 1000th entry.     

> __< rucknium >__ Anything more about stressnet?     

> __< jberman >__ nothing on my end     

> __< kayabanerve:matrix.org >__ Noting a starting index, instead of padding with empty vectors, doesn't solve the case where the first commitment and the 1000th commitment are referenced, but it'd reasonably solve the case where solely the 1000th commitment is referenced, which should be _most_ instances of the problem optimized by the experiment.     

> __< kayabanerve:matrix.org >__ inb4 the 4-20 hours of work I mentioned     

> __< rucknium >__ 7. Mining pool centralization: Temporary rolling DNS checkpoints (https://github.com/monero-project/monero/issues/10064), Share or Perish (https://github.com/monero-project/research-lab/issues/146), and Lucky transactions (https://github.com/monero-project/research-lab/issues/145).     

> __< rucknium >__ Nothing on this for now.     

> __< DataHoarder >__ No updates since last time on the topic of Monero patches     

> __< rucknium >__ We can end the meeting here. Thanks everyone.     

> __< DataHoarder >__ Qubic is having issues, broken centralized XMR task server , and some spamming     

> __< DataHoarder >__ Though still alive.     

> __< DataHoarder >__ Thanks for having the coinbase topic in! If any of you have relevant papers/suggestions you can bring these up in #monero-research-lounge or #p2pool-log (they should both be bridged)     

> __< articmine >__ Well Qubic has breached 0.000001 USD. We will see if they breach their all time low on coinmarketcap     




# Action History
- Created by: Rucknium | 2025-11-11T23:41:50+00:00
- Closed at: 2025-11-25T23:25:27+00:00
