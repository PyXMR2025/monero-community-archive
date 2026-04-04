---
title: Monero Research Lab Meeting - Wed 30 July 2025, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/1247
author: Rucknium
assignees: []
labels: []
created_at: '2025-07-29T22:07:49+00:00'
updated_at: '2025-08-08T21:17:01+00:00'
type: issue
status: closed
closed_at: '2025-08-08T21:17:01+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/meeting.html?p1=1440)

Main discussion topics:

1. Greetings

2. Updates. What is everyone working on?

3. [Transaction volume scaling parameters after FCMP hard fork](https://github.com/ArticMine/Monero-Documents/blob/master/MoneroScaling2025-07.pdf).

4. [FCMP++ optimization coding competition](https://www.getmonero.org/2025/04/05/fcmp++-contest.html).

5. [FCMP alpha stressnet planning](https://github.com/seraphis-migration/monero/issues/53#issuecomment-3053493262).

6. [Spy nodes](https://github.com/monero-project/research-lab/issues/126).

7. [Proposal and spec for Proof-of-Work Enabled Relay ("PoWER")](https://github.com/monero-project/research-lab/issues/133).

8. PoW mining pool centralization. [Qubic Monero Hashpower Share](https://gist.github.com/Rucknium/0873b10b6d36ff6c9d6f8f54107d16f7). [TEE-assisted Censorship-Resistant Block Template Production](https://github.com/monero-project/research-lab/issues/134). 

9. Any other business

Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: Rucknium

Previous meeting agenda/logs:

#1244 

# Discussion History
## Rucknium | 2025-07-31T20:08:06+00:00
Logs:

> __< r​ucknium:monero.social >__ Meeting time! https://github.com/monero-project/meta/issues/1247     

> __< r​ucknium:monero.social >__ 1) Greetings     

> __< a​rticmine:monero.social >__ Hi     

> __< rbrunner >__ Hello     

> __< v​tnerd:monero.social >__ Hi     

> __< s​yntheticbird:monero.social >__ Hi     

> __< j​berman:monero.social >__ *waves*     

> __< c​haser:monero.social >__ hello     

> __< j​effro256:monero.social >__ Howdy     

> __< g​ingeropolous:monero.social >__ hi     

> __< r​ucknium:monero.social >__ 2) Updates. What is everyone working on?     

> __< v​tnerd:monero.social >__ Me: currently fighting the monero_c build process     

> __< r​ucknium:monero.social >__ me: Setting up "honeypots" to discover more about spy node infrastructure. Monitoring Qubic hashpower share: https://gist.github.com/Rucknium/0873b10b6d36ff6c9d6f8f54107d16f7 I submitted a new research CCS proposal:  https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/599     

> __< j​effro256:monero.social >__ Me: finished firs draft of hot-cold FCMP++/Carrot wallets, reviewing rbrunner7's subnet dedup PR     

> __< j​berman:monero.social >__ me: squashing bugs reported by ofrnxmr  in the fcmp++ integration, refactoring refresh() to *not* download all hashes in the chain from before the wallet's restore height (since this has no tangible benefit as is)     

> __< g​ingeropolous:monero.social >__ me: still driving the bots to build monerosim.     

> __< a​rticmine:monero.social >__ I have been working on the scaling. Expect to have a revised document for the next meeting.     

> __< a​rticmine:monero.social >__ A long term sanity median is very much feasible and the wallets can be insulated from constant fee calculations     

> __< a​rticmine:monero.social >__ The value will also be in using MA for node relay bandwidth caps to effectively manage the blocksize     

> __< r​ucknium:monero.social >__ 3) [Transaction volume scaling parameters after FCMP hard fork](https://github.com/ArticMine/Monero-Documents/blob/master/MoneroScaling2025-07.pdf).     

> __< a​rticmine:monero.social >__ As I mentioned a sanity median is in the works.      

> __< a​rticmine:monero.social >__ One thing I am looking for is the latest stress net TPS for FCM++     

> __< a​rticmine:monero.social >__ FCMP++     

> __< j​effro256:monero.social >__ Did the tx byte sizes from last week affect your analysis at all?     

> __< a​rticmine:monero.social >__ Not materially     

> __< a​rticmine:monero.social >__ The more critical issues in my mind iss going to be verification times     

> __< a​rticmine:monero.social >__ Since 1) they are serious and 2) can be mitigated substantially outside the consensus     

> __< a​rticmine:monero.social >__ Multi thread and GPU / graphics verification will be critical here     

> __< j​effro256:monero.social >__ I am going to disagree that GPU verification is critical. It's a nice-to-have, but far from critical IMO     

> __< a​rticmine:monero.social >__ Byte sizes alone point to verify large block sizes because of current bandwidth availability. In my analysis the impact of sizes is for the most part factored in  with the change to ZM     

> __< a​rticmine:monero.social >__ It means we have to restrict blocksize in non consensus     

> __< a​rticmine:monero.social >__ But it is not required right now     

> __< a​rticmine:monero.social >__ GPU verification     

> __< s​yntheticbird:monero.social >__ I wonder how many years left before we're going to ask ourselves about NPU verification     

> __< a​rticmine:monero.social >__ It depends on transaction demand     

> __< r​ottenwheel:unredacted.org >__ draft of a gist on it, or code-related? any links? 😁     

> __< j​effro256:monero.social >__ rottenwheel: working code: https://github.com/seraphis-migration/monero/pull/52     

> __< o​frnxmr:monero.social >__ https://github.com/monero-project/monero/pull/9856 this sped up initial sync by 40% for me     

> __< r​ottenwheel:unredacted.org >__ ah, yes; saw that before around here. thank you.     

> __< o​frnxmr:monero.social >__ Not sure about w/ fcmp or w/o checkpoints     

> __< r​ottenwheel:unredacted.org >__ rucknium good luck with the new proposal. thanks for the continued research and reports.     

> __< j​effro256:monero.social >__ ofrnxmr:  FCMP++ uses curves (Helios-Selene) where that scalar-point multiplication wouldn't be applicable, so the speedup will almost certainly be less pronounced syncing FCMP++, but that's very interesting     

> __< j​berman:monero.social >__ Wondering if there are any changing thoughts on tx weights clamping to powers of 2? Just reiterating from last week, this would incentivize the creation of multiple tx of lower input combinations instead of single larger txs (e.g. 1-in + 2-in > 3-in)     

> __< a​rticmine:monero.social >__ My take is that there will be significant improvement in verification after the FCMP++ fork.     

> __< a​rticmine:monero.social >__ 1 in + 2 in > 4 in becomes the test     

> __< a​rticmine:monero.social >__ With power s of 2     

> __< j​berman:monero.social >__ By ">" I meant, a user is incentivized to spend 3 inputs across 2 txs (a 1-input and a 2-input), instead of in a single 3-input tx     

> __< a​rticmine:monero.social >__ I understand     

> __< j​effro256:monero.social >__ We also would prefer people do a 4-in over a 3-in & 1-in, so it has to be bounded in both directions     

> __< a​rticmine:monero.social >__ If the cost of 3 in and 4 in are the same. Then we end up comparing 1 in + 2 in to 4 in     

> __< j​berman:monero.social >__ What if a user only has 3 inputs?     

> __< a​rticmine:monero.social >__ They have to pay for 4     

> __< a​rticmine:monero.social >__ 3 in is still valid     

> __< j​berman:monero.social >__ They would be better off spending as a 1-in and 2-in instead of 3 though     

> __< a​rticmine:monero.social >__ Then this is the case against powers of 2     

> __< j​berman:monero.social >__ right I was wondering if there are any thoughts on changing the currently proposed powers of 2 approach, taking that case into account     

> __< a​rticmine:monero.social >__ Yes. This really comes down to the t numbers     

> __< a​rticmine:monero.social >__ Both size and verification time.     

> __< a​rticmine:monero.social >__ It is not just proof sizes. There is also the base part of the tx to consider     

> __< a​rticmine:monero.social >__ and the greater number of outputs     

> __< j​effro256:monero.social >__ jberman: depending on the specific weight function, your issue of making a 2-in + 1-in instead of a 3-in because of the powers of 2 weight might not be so bad if we model the sender as also taking into account the *future* weight of having to spend 2-in versus a 1-in     

> __< a​rticmine:monero.social >__ There is another advantage to powers of 2. It encourages the consolidation of dust     

> __< j​berman:monero.social >__ In that case it's even worse no? because the future 2-in weight will be > future 1-in     

> __< j​effro256:monero.social >__ Now if in the future, they only needed a small input from one of the two, then they pay no additional cost, however, if they needed to consolidate, they would pay that cost. So its strange b/c it's conditional on how they schedule their future payments     

> __< j​berman:monero.social >__ Oh you're saying it's more expensive to them in the future to consolidate those 2 future outputs, gotcha     

> __< j​effro256:monero.social >__ Right, which would naturally disincentive the sneder from doing that     

> __< j​effro256:monero.social >__ Methinks we need a fee market simulation     

> __< j​berman:monero.social >__ I can work on a table of all FCMP++/Carrot byte sizes and current verification times of default txs of 1 - 128 inputs and 2 - 16 outputs     

> __< g​ingeropolous:monero.social >__ did someone say simulation     

> __< j​effro256:monero.social >__ It contains rational actors trying to pay the least amount of fees while fulfilling payments in a certain timeframe     

> __< r​ucknium:monero.social >__ Did someone say market     

> __< j​effro256:monero.social >__ While node actors adjust the fee market policy to minimize verification time and storage costs     

> __< a​rticmine:monero.social >__ This would be very helpful     

> __< a​rticmine:monero.social >__ ... and answer this question     

> __< j​berman:monero.social >__ Will do that and comment it here: https://github.com/seraphis-migration/monero/issues/44     

> __< r​ucknium:monero.social >__ 4) [FCMP++ optimization coding competition](https://www.getmonero.org/2025/04/05/fcmp++-contest.html).     

> __< r​ucknium:monero.social >__ Last meeting we planned to have a post-mortem discussion about this.     

> __< j​effro256:monero.social >__ jberman do you want to dump the post here now, or publish it in a bit ? I'm fine w/ now     

> __< r​ucknium:monero.social >__ IMHO, the big win was `ec-divisors`, which attracted one (IIRC) submission, but got a 30x speedup.     

> __< r​ucknium:monero.social >__ Oh, there is a post     

> __< j​berman:monero.social >__ I'll dump it here, one sec     

> __< j​effro256:monero.social >__ Is xmrack here today?     

> __< r​ucknium:monero.social >__ And the `ec-divisors` win makes me wonder if the speedup could have been achieved by doing a review of the relevant literature and finding the fast algorithm that way, instead of a competition. I mean, as a lesson for the future.     

> __< a​ck-j:matrix.org >__ Hello     

> __< j​berman:monero.social >__ https://paste.debian.net/1388773/     

> __< j​effro256:monero.social >__ The one thing I wanted to talk to xmrack about is how they went about scouting for contestants, and if there is anything to be taken away from that process. (you don't have to answer now lol I kinda put you on the spot). That was something I wasn't involved in, but the outreach that they did produced good results. IIRC they contacted Fabrizio directly. Is that correct?     

> __< j​berman:monero.social >__ Fabrizio ack'd kayabanerve 's idea to use an FFT as "likely better" here:  https://github.com/fabrizio-m/fcmp-competition/pull/1#issuecomment-3033736170. It was also a matter of finding someone to do the work     

> __< a​ck-j:matrix.org >__ Correct. I looked at the ZPrize contest (recommended by kayaba at some point) which was the most similar contest to what we planned on running. https://github.com/z-prize/2023-entries     

> __< a​ck-j:matrix.org >__ I went through each of the submissions for 2022 and 2023 and dug out contestants email addresses from their submissions and reached out to them directly. I only received a few replies with Fabrizio being one of them.      

> __< a​ck-j:matrix.org >__ I also reached out to people who have published monero-related cryptography related research papers but had no luck there.     

> __< a​ck-j:matrix.org >__ I’m not sure I have any lessons learned besides that we got really lucky with Fabrizio being a wizard and a perfect fit for our rust-based competition     

> __< a​ck-j:matrix.org >__ I think posting to reddit was good for general awareness but I’m not positive that was successful at attracting competitors.     

> __< r​ucknium:monero.social >__ Ready to move to the next agenda item?     

> __< r​ucknium:monero.social >__ 5) [FCMP alpha stressnet planning](https://github.com/seraphis-migration/monero/issues/53#issuecomment-3053493262).     

> __< o​frnxmr:monero.social >__ - Unable to connect a wallet to an unrestricted rpc if txpool > 100mb: https://github.com/monero-project/monero/pull/9473     

> __< o​frnxmr:monero.social >__ - dynamic block sync size: https://github.com/monero-project/monero/pull/9494 also here https://github.com/seraphis-migration/monero/pull/78     

> __< j​effro256:monero.social >__ jberman mentioned that the >8-in PR is ready for review now, I will take a look at it very soon     

> __< j​berman:monero.social >__ I'd also like to knock out this wallet refresh refactor too to address ofrnxmr 's bugs     

> __< o​frnxmr:monero.social >__ Ive tested the bss numerous times, but am unsure about 9473's correctness     

> __< o​frnxmr:monero.social >__ Ive tested the dbss (9494) numerous times, but am unsure about 9473's correctness     

> __< j​berman:monero.social >__ what was the reasoning on 9473 for not just requesting max 100 txs at a time on unrestricted too? that seemed like a simple solution to the issue there     

> __< o​frnxmr:monero.social >__ I dont know. Batching into 100 (or even 500) seems like the most simple solution     

> __< j​berman:monero.social >__ can discuss it further later     

> __< j​berman:monero.social >__ w.r.t. stressnet, I'd say let's get 1 more week to address above (refresh refactor, 9473, 8 input PR, and dynamic block sync size)     

> __< o​frnxmr:monero.social >__ What will it take before we can use the optimized libs?     

> __< o​frnxmr:monero.social >__ (currently takes me abt 20 seconds to build an 8in 8out tx, iirc)     

> __< j​berman:monero.social >__ Lederstrumpf's helioselene optimizations + kayaba's optimizations on top are already merged upstream. Open PR over here for fabrizio's: https://github.com/kayabaNerve/fcmp-plus-plus/pull/33     

> __< j​berman:monero.social >__ If fabrizio's not in by next week, I'll just push to my fork and we can use it from there in fcmp++-stage     

> __< r​ucknium:monero.social >__ 6) [Spy nodes](https://github.com/monero-project/research-lab/issues/126).     

> __< r​ucknium:monero.social >__ I've set up some "honeypots" to try to learn more about the spy node infrastructure. No results to report yet.     

> __< r​ucknium:monero.social >__ My proposal to make a few changes to the DNS ban list contents is available for comments & questions: https://github.com/monero-project/meta/issues/1242     

> __< r​ucknium:monero.social >__ Like jeffro256 say, he is working on reviewing rbrunner's PR: p2p: Improved peer selection with /24 subnet deduplication to disadvantage 'spy nodes' https://github.com/monero-project/monero/pull/9939     

> __< rbrunner >__ Thankful for that :)     

> __< r​ucknium:monero.social >__ Anything more on spy nodes?     

> __< r​ucknium:monero.social >__ 7) [Proposal and spec for Proof-of-Work Enabled Relay ("PoWER")](https://github.com/monero-project/research-lab/issues/133).     

> __< o​frnxmr:monero.social >__ Not spy node related, per say, but there are miners that seem to check ports and possibly mine on them     

> __< o​frnxmr:monero.social >__ my xmrig-proxy has 20 unknown monero addresses that have connected to it over the past month or so     

> __< r​ucknium:monero.social >__ ofrnxmr: You mean trying to start the miner through an unrestricted RPC? Or just a nodeless miner looking for block templates?     

> __< j​berman:monero.social >__ I think boog900 raised some valid points that bump favorability of Equi-X over RandomX in discussion starting here: https://github.com/monero-project/research-lab/issues/133#issuecomment-3130110655     

> __< b​asses:matrix.org >__ Thanks a lot for your hard work!     

> __< o​frnxmr:monero.social >__ No, i mean a miner (probably xmrig) is connecting to my xmrig-proxy     

> __< j​berman:monero.social >__ I'm still curious how long RandomX PoW construction on light mode would take, assuming it takes some reference machine 1-2s on fast mode     

> __< j​berman:monero.social >__ Haven't gotten around to testing that out     

> __< o​frnxmr:monero.social >__ They have their user section of xmrig set to a primary monero address, so it doesnt seem to be just knocking kookijg for unrestricted rpc, but an actual miner looking for a stratum or rpc     

> __< r​ucknium:monero.social >__ 8) PoW mining pool centralization. [Qubic Monero Hashpower Share](https://gist.github.com/Rucknium/0873b10b6d36ff6c9d6f8f54107d16f7). [TEE-assisted Censorship-Resistant Block Template Production](https://github.com/monero-project/research-lab/issues/134).     

> __< r​ucknium:monero.social >__ Qubic changed their mining wallet at around 9:30 UTC today, so their mined blocks cannot be deduced from the method I used in the gist ^ anymore. And their pool API has stopped working AFAIK.     

> __< r​ucknium:monero.social >__ But you can get a good approximation of the number of blocks they have mined by getting all the blocks that other mining pools claim, then seeing what's left.     

> __< a​rticmine:monero.social >__ Is there anything in tx extra?     

> __< r​ucknium:monero.social >__ I see 15 - 25% of blocks unclaimed by other pools, in the last 24 hours     

> __< a​rticmine:monero.social >__ That is unique to Qubic?     

> __< r​ucknium:monero.social >__ I am not sure about the tx_extra contents     

> __< a​rticmine:monero.social >__ So the unclaimed blocks may have a signature     

> __< o​frnxmr:monero.social >__ The unclaimed blocks were like 5% before? I dont remembwr     

> __< a​rticmine:monero.social >__ Tx extra for the coinbase is used by Tari     

> __< sech1 >__ Unknown blocks were 1.5% of all blocks before, so just subtract 1.5% from what https://miningpoolstats.stream/monero pie chart shows     

> __< r​ucknium:monero.social >__ Years ago, DataHoarder made this Go program that pulls the blocks claimed by most major pools' APIs: https://git.gammaspectra.live/WeebDataHoarder/monero-blocks     

> __< DataHoarder >__ could update it to re-fetch data     

> __< o​frnxmr:monero.social >__ miningpoolstats.stream shows 5% unknown, 12% qubic over the last 1000 blocks. And 11% now (unknown)     

> __< a​rticmine:monero.social >__ Also the PoUWin Qubic is highly centralized with like 90% control     

> __< r​ucknium:monero.social >__ And then https://p2pool.observer/api gives you p2pool-mined blocks     

> __< r​ucknium:monero.social >__ Qubic claims that many miners are switching to their pool. I don't yet believe that claim without evidence.     

> __< rbrunner >__ DataHoarder: Please do if you can spare the time     

> __< a​rticmine:monero.social >__ I will be on MoneroTalk regarding Qubic later today     

> __< o​frnxmr:monero.social >__ I dont believe that claim at all     

> __< sech1 >__ 4.71 GH/s are not on their pool at the moment. So they need 4.71 GH/s to overtake them     

> __< sech1 >__ So far they haven't shown more than 2.2 GH/s even at peak moments.     

> __< r​ucknium:monero.social >__ I wonder how much info the makers of xmrig have about miners possibly switching pools, from the 1% hashrate donation behavior.     

> __< sech1 >__ The only evidence about switching miners was from supportxmr     

> __< DataHoarder >__ https://p2pool.observer/api https://mini.p2pool.observer/api (and nano, old, old-mini) etc. but they can be coalesced     

> __< sech1 >__ they had ~300 MH/s miner profit switching between Monero and Qubic     

> __< a​rticmine:monero.social >__ They need to incentivize by paying Qubic to get the hash rate to move     

> __< DataHoarder >__ in general if the mining coinbase has quite some outputs it tends to be p2pool, specially with the merge mining tag     

> __< r​ucknium:monero.social >__ If subsidizing attacking hashpower is their strategy, two (or more) can play that game. XMRvsBeast already does some subsidization of p2pool miners with the hashrate raffle, AFAIK.     

> __< a​rticmine:monero.social >__ So about 6%     

> __< sech1 >__ Current Qubic price is $0.000002281 per coin, and give 1T/week emission, it's $325k/day going to miners     

> __< sech1 >__ double that of Monero's miner subsidy     

> __< sech1 >__ So they in theory can overtake Monero in raw hashrate, they do have the money (daily subsidy)     

> __< sech1 >__ The question is, how do they manage to keep the price from falling, they're a small cap coin     

> __< a​rticmine:monero.social >__ This depends on the price difference and the effective emission of Qubic vs Monero     

> __< o​frnxmr:monero.social >__ Do they have the buy liquidity to support that 325k/day 🙃     

> __< sech1 >__ Their effective emission (in $) is two times bigger right now     

> __< o​frnxmr:monero.social >__ You can claim 325k by looking at spot,but its not real if you cant exit your position without crashing the price to 0     

> __< a​rticmine:monero.social >__ No they are getting Qubic to cover this     

> __< a​rticmine:monero.social >__ It. Is an effective merged mining     

> __< sech1 >__ So someone is dumping big money to keep the price afloat and subsidy the miners     

> __< a​rticmine:monero.social >__ They have to keep the Qubic price afloat     

> __< o​frnxmr:monero.social >__ right. They sell xmr for 30k/day, buy qubic with 30k (or put up buy walls)     

> __< o​frnxmr:monero.social >__ hoping nobody actually mines qubic,sells 100% of it and buys 2x as much xmr     

> __< a​rticmine:monero.social >__ Then they have to pay for power     

> __< sech1 >__ Also, TradeOgre is currently down (this exchange had a huge amount of Qubic on the sell side).     

> __< a​rticmine:monero.social >__ Bingo     

> __< sech1 >__ That makes it easier to keep the price afloat, because there is a lot of coins locked there now and for an indefinite time     

> __< a​rticmine:monero.social >__ Feed the Qubic to the bears     

> __< a​rticmine:monero.social >__ ... but they can manipulate Qubic to mitigate this bear raid approach     

> __< a​rticmine:monero.social >__ By locking the Qubic up     

> __< sech1 >__ Also Qubic plan the halving in 3 weeks time, that will reduce the subsidy proprotionally (unless they manipulate the price again)     

> __< a​rticmine:monero.social >__ Awareness can be a real problem for them     

> __< r​ucknium:monero.social >__ If you want to fight fire with fire, the Core General Fund could temporarily subsidize honest hashpower. (Of course, I love volunteering other people's money 😁.)     

> __< sech1 >__ The best way to subsidize XMR hashrate would be to pay P2Pool miners (proportionally to their hashrate) - it's easy to put together a list of miners every day for a manual payout, DataHoarder's observer can do it     

> __< r​ucknium:monero.social >__ I don't know what other realistic active countermeasures there may be.     

> __< kanzure >__ how would honest miners be picked     

> __< r​ucknium:monero.social >__ If countermeasures are considered necessary.     

> __< sech1 >__ I just wrote how     

> __< DataHoarder >__ weight of their shares in difficulty units is tracked as part of consensus     

> __< r​ucknium:monero.social >__ Right. The p2pool sidechain is a secure, honest way to get the addresses of miners.     

> __< sech1 >__ Currently, all P2Pool miners earn 20-22 XMR/day. If 50 XMR/day are paid to them, that's double the profit and a good enough incentive for other miners to switch     

> __< sech1 >__ No, not the double. More than triple, because it adds up     

> __< kanzure >__ ah okay, and qubic block structure is incompatible with p2pool requirements?     

> __< sech1 >__ Yes, they are incompatible     

> __< DataHoarder >__ p2pool can merge mine, are they "merge mining" or doing something else?     

> __< r​ucknium:monero.social >__ What if Qubic points its own hashpower at p2pool? Wouldn't the forced orphaning tatic fail, because other p2pool miners would be mining on other miners' honest blocks?     

> __< sech1 >__ Qubic is merge mining Tari     

> __< o​frnxmr:monero.social >__ Qubic was using p2pool before     

> __< sech1 >__ No, they used nanopool     

> __< o​frnxmr:monero.social >__ They used p2pool for a while too     

> __< sech1 >__ I'm not aware of that, and I watch p2pool daily     

> __< r​ucknium:monero.social >__ The `--enforce-dns-checkpointing` optional flag also exists, but IMHO its use should not be encouraged. Just a reminder that it exists: https://docs.getmonero.org/interacting/monerod-reference/#server     

> __< a​rticmine:monero.social >__ I see as the better strategy " merge" mining Qubic by honest Monero miners     

> __< sech1 >__ "Mining" Qubic leaves you no choice but to also participate in their attack     

> __< sech1 >__ they use some centralized approach for mining     

> __< rbrunner >__ They just let you run xmrig pointed to their pool. Did nobody here actually try?     

> __< o​frnxmr:monero.social >__ Moneroocean wrote about adding qubic to their pool, but wasnt as simple as a regular chain     

> __< a​rticmine:monero.social >__ No if one can decentralize Qubic     

> __< o​frnxmr:monero.social >__ https://matrix.monero.social/_matrix/media/v1/download/monero.social/QozzcjCsmwKnwuYBsREzxdyy     

> __< a​rticmine:monero.social >__ Take the fight to their chain     

> __< rbrunner >__ They don't have one :)     

> __< o​frnxmr:monero.social >__ https://matrix.monero.social/_matrix/media/v1/download/monero.social/vGPKThqFvmAAnCBOZVQjpBJg     

> __< r​ucknium:monero.social >__ rbrunner: And xmrig doesn't let you pick the block template, right?     

> __< rbrunner >__ It runs fully under control of their "miner"     

> __< rbrunner >__ And you know what is really hilarious? So far on each day except Saturday they run xmrig only 50% of the time     

> __< a​rticmine:monero.social >__ Is there the possibility of a Qubic chain split     

> __< rbrunner >__ Again, there is no chain.     

> __< r​ucknium:monero.social >__ They have  block explorer IIRC     

> __< rbrunner >__ Please, you all. Have a closer look. It's a very interesting beast. Very different.     

> __< r​ucknium:monero.social >__ a block explorer*     

> __< a​rticmine:monero.social >__ It is     

> __< rbrunner >__ No, they have a tick explorer     

> __< rbrunner >__ Those are not blocks in some blockchain     

> __< r​ucknium:monero.social >__ Yes, what are those ticks?!     

> __< DataHoarder >__ git has a commit explorer too     

> __< r​ucknium:monero.social >__ I looked at the explorer a while, trying to understand.     

> __< rbrunner >__ I don't spill the secret, because people should have a look themselves.     

> __< rbrunner >__ Just for the record: Please take them serious as a credible threat.     

> __< a​rticmine:monero.social >__ I agree     

> __< rbrunner >__ The first for years. Maybe that makes it all so difficult. To mentally switch.     

> __< a​rticmine:monero.social >__ The degree of centralization in Qubic is key to the threat     

> __< sech1 >__ Well, if ofrnxmr is right about Qubic using p2pool before (I don't remember that), then mining subsidy should be sent to centralized pools, preferably smaller ones. Because P2Pool lets you use your own node and therefore run an attack (orphan blocks).     

> __< d​uggavo:matrix.org >__ I think the Qubic owner is a serial shitcoin creator. He does this just to gain attention and investors in his otherwise useless coin. Stop giving them spotlight and the solution will be already half way there.     

> __< rbrunner >__ Yeah, what a shitcoin IOTA was ... no innovation, no ideas, no nothing.     

> __< a​rticmine:monero.social >__ My take is that the greater the awareness of this in the Monero community the lease the threat     

> __< rbrunner >__ Everybody here could have invented that, right? :)     

> __< r​ucknium:monero.social >__ I could work on a couple of data tasks in this area: Set up a webapp for real-time charts of Qubic's probably hashpower share. I could also work on displaying any alt chains that appear and any transaction double-spends.     

> __< o​frnxmr:monero.social >__ The problem is that monero community panics instead of doing anything     

> __< rbrunner >__ Even the Qubic fans themselves long for the realtime info they lost today, so do go ahead     

> __< r​ucknium:monero.social >__ Alt chains are easy to get from the node. Double spends could be detected from the txpool data collection infrastructure I've helped run for years.     

> __< a​rticmine:monero.social >__ I went through the 2018 Bitmain attack. The Monero community did a lot     

> __< rbrunner >__ ofnrxmr, please write down somewhere what "could be done".     

> __< d​uggavo:matrix.org >__ I think the only way to really stop the risk of a 51% attack from the QUBIC - forever - would be changing the consensus system. Possibly to something similar to Zano's private 50% PoW 50% PoS. I know this would be very controversial here, but I think it could raise the security. Especially if the PoS blocks have a reduced block reward compared to PoW blocks.     

> __< o​frnxmr:monero.social >__ People could spin up their miners instead of writr twitter threads about how we should switch to scrypt     

> __< r​ucknium:monero.social >__ I have been thinking of ofrnxmr 's idea of a "delayed payout" for PoW miners. Seems interesting. But that's long-term. What are available plans in the short term?     

> __< a​rticmine:monero.social >__ We need to avoid an overreaction     

> __< rbrunner >__ ... as well as underreactions ...     

> __< sech1 >__ The real way to stop it is to own all of the available CPU power, which Monero is far away from. They are only able to do this because their mining subsidy is higher at the moment.     

> __< DataHoarder >__ if they are fully centralized and they can just point miners to new solution - no merge mining per se, but they can merge mining if they desire, they are like a big single centralized pool effectively     

> __< o​frnxmr:monero.social >__ I said in lounge that i'm against POS, but also said that if we DID add hybrid POS that it should only allow staking of virgin, pow mined coins     

> __< a​rticmine:monero.social >__ Monero is way stronger after 2018     

> __< DataHoarder >__ pow mined coins are public, and then also there's the coalescing issue somewhere on github     

> __< a​rticmine:monero.social >__ Selling manure can be very profitable     

> __< DataHoarder >__ #108 and #109     

> __< DataHoarder >__ would do well :D     

> __< o​frnxmr:monero.social >__ And i'd also add that hybrid pos should be a 90:10 split, with 4 minutes per pow block and 4minutes per pos block     

> __< r​ucknium:monero.social >__ I like the delayed PoW payout idea because it reduces the threat of malicious short-term CPU rental.     

> __< sech1 >__ In terms of hashrate, Monero is way stronger than even a year ago. It was 2.2 GH/s a year ago, not it's 4.5-4.7 GH/s (not counting Qubic)     

> __< sech1 >__ If Qubic happened last year, they would already be able to 51%     

> __< d​uggavo:matrix.org >__ I'd agree with 9:1 reward split and 4 min PoW / 4 min PoS.     

> __< a​rticmine:monero.social >__ POS has a host of issues     

> __< d​uggavo:matrix.org >__ A low PoS reward mitigates many of the downsides of that approach.     

> __< o​frnxmr:monero.social >__ my idea would only allow staking virgin POW coins. No buy-ins.     

> __< DataHoarder >__ organically sourced moneros     

> __< a​rticmine:monero.social >__ There is also another angle. Copyleft for mining code     

> __< r​ucknium:monero.social >__ Those are "Coinbase Consolidation Tx Type" https://github.com/monero-project/research-lab/issues/108 and     

> __< r​ucknium:monero.social >__ "Avoid selecting coinbase outputs as decoys" https://github.com/monero-project/research-lab/issues/109     

> __< o​frnxmr:monero.social >__ Xmrig is copyleft     

> __< a​rticmine:monero.social >__ The issue with POS is borrowing coins     

> __< rbrunner >__ They have a repository for their slightly modified xmrig. Again, nobody actually checked, right?     

> __< DataHoarder >__ they'd have to borrow the private keys of a miner     

> __< c​haser:monero.social >__ if there is a good overlay PoS design, this^ is it. I've been toying with a design for a while that has the same property.     

> __< a​rticmine:monero.social >__ With a strong copyleft one can take down the repository     

> __< DataHoarder >__ besides setting donation to 0 rbrunner this is the only relevant commit there yep rbrunner https://github.com/xmrig/xmrig/commit/b41fcf5b0d874fc0e17655dc77f32f32912cff5a     

> __< r​ucknium:monero.social >__ ofrnxmr's idea mostly prevents borrowing coins because they cannot be transferred in an on-chain tx. And if you "sell" a private key to someone, then the seller can just use it, too. ANd nothing prevents you from "selling" the key to multiple buyers.     

> __< c​haser:monero.social >__ and there need not be a staking reward per se. changing the monetary policy is off the table.     

> __< d​uggavo:matrix.org >__ That would prevent "mine-and-dump", but I am not sure it could actually be secure. The stakers would be only a subset of the miners. I think it could actually reduce the security.     

> __< a​tomfried:matrix.org >__ Wouldnt that mean a 51% pow attack acquires more and more power over the network?     

> __< a​ntilt:we2.ee >__ after dedoubling eigentrust would be worth checking out (in the long run)     

> __< r​ucknium:monero.social >__ It is better to spread the power over the network across a lot of time instead of concentrate in a few minutes, especially with an ASIC-resistant mining algorithm.     

> __< o​frnxmr:monero.social >__ it would be a 25.5% attack if they have 51% of the pow     

> __< DataHoarder >__ there was the wow change to require private keys to generate PoW solutions     

> __< DataHoarder >__ that'd kill pools, generally     

> __< DataHoarder >__ is that still working fine?     

> __< d​uggavo:matrix.org >__ This assumes all the miners stake the coins indefinitely.     

> __< r​ucknium:monero.social >__ For example: Today, a miner mines a coinase of about 0.6 XMR. They can spend 0.3 XMR of that now. In a randomly-selected time in the future, within the next year or something, they have to validate a block with their private key to make the other 0.3 XMR spendable.     

> __< d​uggavo:matrix.org >__ Yes, Wownero requires the mining blob to be signed with the miner's private spend key. It works, but killing pools and killing P2Pool is not viable. Monero's blocks are too infrequent to allow that. It would centralize the network.     

> __< r​ucknium:monero.social >__ I read that some pools implemented closed-source mining software to avoid wownero's strategy.     

> __< r​ucknium:monero.social >__ I'm not sure how true what I read is.     

> __< d​uggavo:matrix.org >__ Those pools must remain private and with trusted users. A pool with open registration would be leeched by miners who steal block rewards.     

> __< r​ucknium:monero.social >__ like...Qubic (effectively)?     

> __< DataHoarder >__ if you can run the miner locally, you have the keys     

> __< sech1 >__ No, not exactly     

> __< sech1 >__ Wownero solution only leaks you the tx spend key for a block you're currently mining     

> __< sech1 >__ I remember because I helped them implement it     

> __< d​uggavo:matrix.org >__ That makes sense. It's a sort of delayed Proof-of-Work. But how would that work with miners on pools or solo/p2pool miners who aren't always online?     

> __< sech1 >__ Still, you can steal a block if you find it     

> __< DataHoarder >__ either it's delayed or you can actively act in consensus PoS to accelerate that     

> __< DataHoarder >__ so you can take very delayed coins, or PoS? but then the delay on part effectively does the same     

> __< DataHoarder >__ doesn't change 51% attacks     

> __< DataHoarder >__ that's done on hashrate alone, and if PoS would be a very minor part of the slice, that'd not affect as much     

> __< r​ucknium:monero.social >__ duggavo: Pool operators get the coinbase reward, not the miners. So pools stay online. p2pool miners must stay online. If they block that you have to validate is at a specified time in the future, just make sure you are online when it's your time to validate.     

> __< DataHoarder >__ p2pool miners don't have their wallets unlocked or have to     

> __< sech1 >__ They don't need private keys to mine, no     

> __< DataHoarder >__ in my case I mined to a cold wallet somewhere backed by a hw wallet     

> __< r​ucknium:monero.social >__ It would change how much time you would have to possess 51% of hashrate.     

> __< d​uggavo:matrix.org >__ I don't understand why not with 10:1 PoW:PoS block reward with 240s:240s PoW:PoS target block time. What's wrong with that?     

> __< r​ucknium:monero.social >__ Then get online and get with the program :D     

> __< r​ucknium:monero.social >__ HW wallet makers say don't mine to a HW wallet.     

> __< DataHoarder >__ 51% of hashrate or 51% of reward?     

> __< r​ucknium:monero.social >__ That's up for discussion.     

> __< r​ucknium:monero.social >__ It's a new idea worth exploring IMHO.     

> __< r​ucknium:monero.social >__ Anyway, back to short term. Short term things that can be discussed?     

> __< DataHoarder >__ like, if it's rations like 10:1 or anything like that it'd be at most 20% harder?     

> __< DataHoarder >__ as mentioned before if they are effectively just a big centralized pool they can point hashrate anywhere, p2pool, other pools (?)     

> __< DataHoarder >__ so funding these miners might not do the right thing     

> __< r​ucknium:monero.social >__ You can have the share of blocks validated by the two mechanisms be different from the share of rewards. e.g. half of blocks validated by the delay mechanism, but 25% of rewards to the delayed payout.     

> __< d​uggavo:matrix.org >__ Ratio of 10:1 would be for the reward, the difficulty ratio would be 1:1.     

> __< d​uggavo:matrix.org >__ So in practice: 50% of the blocks are found with PoS, and they contribute to 50% of the overall cumulative difficulty. But they receive only 10% of the rewards.     

> __< r​ucknium:monero.social >__ Alternatively, hashpower could be directly rented through miningpoolrentals.com     

> __< r​ucknium:monero.social >__ The money would not "go as far" when directly renting, vs. subsidizing, I think.     

> __< DataHoarder >__ Time for monero to make its own centralized pool funded by monero funds to mine monero?     

> __< r​ucknium:monero.social >__ The meeting's length is about two and a half hours.     

> __< DataHoarder >__ they could just point miners to this :(     

> __< o​frnxmr:monero.social >__ thanks ruck. Ttyl     

> __< r​ucknium:monero.social >__ People should feel free to continue discussing, but we can end the meeting here.     

> __< r​ucknium:monero.social >__ Thanks everyone.     

> __< DataHoarder >__ I thought this was the meeting after-hours talk!     

> __< DataHoarder >__ I'll update my scripts to fetch block data from current pools that are available at least     

> __< r​ucknium:monero.social >__ Thanks, DataHoarder. I ran the script today and everything seemed to work fine, but I did not check everything carefully.     

> __< d​uggavo:matrix.org >__ I've had a couple of ideas about the eventual hybrid PoW / PoS consensus for Monero. Please let me know what you think. https://gist.github.com/duggavo/7b5f1f8cad5bd56c9f27648ccc1728ba     



# Action History
- Created by: Rucknium | 2025-07-29T22:07:49+00:00
- Closed at: 2025-08-08T21:17:01+00:00
