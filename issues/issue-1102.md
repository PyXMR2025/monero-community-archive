---
title: Monero Research Lab Meeting - Wed 30 October 2024, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/1102
author: Rucknium
assignees: []
labels: []
created_at: '2024-10-29T21:05:26+00:00'
updated_at: '2024-11-07T18:55:16+00:00'
type: issue
status: closed
closed_at: '2024-11-07T18:55:16+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

[Join the Monero Matrix server if you don't already have a Matrix account.](https://web.archive.org/web/20230128130949/https://forum.monero.space/d/79-how-to-join-the-monero-core-team-matrix-server-web)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/converter.html?iso=20211027T170000&p1=1440)

Main discussion topics:

1. Greetings

2. Updates. What is everyone working on?

3. Monero Research Computing Server hardware needs.

4. [FCMP++ tx size and compute cost](https://gist.github.com/kayabaNerve/c42aeae1ae9434f2678943c3b8da7898) and [MAX_INPUTS/MAX_OUTPUTS](https://github.com/monero-project/research-lab/issues/100#issuecomment-2433524326)

5. [FCMP++ Optimization Competition](https://github.com/kayabaNerve/fcmp-plus-plus-optimization-competition)

6. Reviews for [Carrot](https://github.com/jeffro256/carrot/blob/master/carrot.md).

7. [Proposal for FCMP++ HF Activation Rule to Retroactively Ignore Future `unlock_time`](https://github.com/monero-project/research-lab/issues/125)

8. Any other business

9. Confirm next meeting agenda

Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: Rucknium

Previous meeting agenda/logs:

#1098 

# Discussion History
## Rucknium | 2024-10-31T16:03:51+00:00
Logs:


> __< r​ucknium:monero.social >__ Meeting time! https://github.com/monero-project/meta/issues/1102     

> __< r​ucknium:monero.social >__ 1) Greetings     

> __< j​berman:monero.social >__ *waves*     

> __< rbrunner >__ Hello     

> __< c​haser:monero.social >__ hello     

> __< v​tnerd:monero.social >__ Hi     

> __< k​ayabanerve:matrix.org >__ 👋     

> __< s​yntheticbird:monero.social >__ Hello     

> __< r​ucknium:monero.social >__ 2) Updates. What is everyone working on?     

> __< r​ucknium:monero.social >__ me: Wrote a review of "Uniformly Most Powerful Tests for Ad Hoc Transactions in Monero": https://github.com/cypherstack/churn/issues/2 . A comment and a gist about `MAX_INPUTS`/`MAX_OUTPUTS` for FCMP: https://github.com/monero-project/research-lab/issues/100#issuecomment-2447705805 and https://gist.github.com/Rucknium/784b243d75184333144a92b3258788f6 . OSPEAD, too.     

> __< k​ayabanerve:matrix.org >__ I wrapped up the multi-input prover/verifier, worked on the const time contest I'll discuss later, and provided a few write-ups on a few topics.     

> __< v​tnerd:monero.social >__ Finished http client code and testing in LWS. Various asio related cleanups in lws. Some ci changes in Lws     

> __< s​yntheticbird:monero.social >__ Working on expanding fcmp++ crate FFI on jberman's monero branch     

> __< s​yntheticbird:monero.social >__ and getting up to speed on FCMP++     

> __< b​oog900:monero.social >__ I spent some time looking into why my node scanner found less than half the amount of IPs vs monero.fail's "Recent Peer" count: https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/469#note_26940     

> __< b​oog900:monero.social >__ > TL/DR: From the data I have it looks like 40% of the IPs running Monero nodes are not real nodes and ~75% of the "Recent Peers" from my scan using monero.fails tool were from an IP in the 6 main subnets + some 23.92.36.* that the proxy nodes were using.     

> __< j​berman:monero.social >__ Continuing tree building, mostly been trying to think through optimal async design     

> __< k​ayabanerve:matrix.org >__ inb4 the optimal async design is to download the monero blockchain via drone delivery of a preloaded SSD     

> __< s​yntheticbird:monero.social >__ lmfao     

> __< j​berman:monero.social >__ that's basically where I was headed     

> __< r​ucknium:monero.social >__ 3) Monero Research Computing Server hardware needs.     

> __< k​ayabanerve:matrix.org >__ Aussies demonstrated how homing pigeons exceeded local ISP transfer rates years ago, why are we ignoring proven     

> __< k​ayabanerve:matrix.org >__ *proven science?     

> __< r​ucknium:monero.social >__ IMHO, 1TB of RAM for about 15 XMR is a good investment for MRL     

> __< k​ayabanerve:matrix.org >__ What's the new update re: hardware? I remember some discussion on it and general vibes of it being worthwhile.     

> __< s​yntheticbird:monero.social >__ fwiw IP over Avian carrier imply huge consequences in case of packet loss (death of pigeons)     

> __< plowsof >__ multiple pigeons will be sent of course      

> __< r​ucknium:monero.social >__ Update is: It would even be useful now, since I have to stop a loop to do these MAX_INPUTS/MAX_OUTPUT analyses.     

> __< r​ucknium:monero.social >__ Because I have room for only one database, and that database is being used in RAM     

> __< k​ayabanerve:matrix.org >__ I maintain my vibe it's worthwhile     

> __< r​ucknium:monero.social >__ Ok. I will suggest that gingeropolous  puts in a CCS proposal.     

> __< r​ucknium:monero.social >__ 4) FCMP++ tx size and compute cost and MAX_INPUTS/MAX_OUTPUTS https://gist.github.com/kayabaNerve/c42aeae1ae9434f2678943c3b8da7898  https://github.com/monero-project/research-lab/issues/100#issuecomment-2433524326     

> __< rbrunner >__ Sounds good to me. Will "pay" itself in no time     

> __< rbrunner >__ Somehow surprising that over half of all existing txs are 1-input     

> __< k​ayabanerve:matrix.org >__ I posted a gist estimating TX sizes, which I've prior mentally down yet never wrote out the formulas for.     

> __< k​ayabanerve:matrix.org >__ *proof sizes     

> __< k​ayabanerve:matrix.org >__ My mental estimations have been wrong by a factor of ~2.4 which I am now deeply ashamed over.     

> __< k​ayabanerve:matrix.org >__ We can recover the results to just 1.4 by increasing the computational complexity as detailed in the provided table.     

> __< rbrunner >__ "5472 exceeds the originally estimated ~2.5kB by a notable margin" That sentence? :)     

> __< k​ayabanerve:matrix.org >__ I'll also note we can be variable here. We can have one-input TX uses a compute factor of 4 and two-input TX use a compute factor of 2. This causes them to share a base cost, which means the block will still efficiently verify.     

> __< k​ayabanerve:matrix.org >__ This would slow down the time to accept a one-input TX into the mempool however (as the one-input TX is now paying a higher base cost and mempool acceptance presumably isn't verifying TXs in batches).     

> __< k​ayabanerve:matrix.org >__ rbrunner: Yes, that's *2.2x larger.     

> __< k​ayabanerve:matrix.org >__ The other discussion is how this impacts MAX_INPUTS. Please note how a large input quantity spikes the base cost.     

> __< k​ayabanerve:matrix.org >__ If the block only has a single 16-input transaction, that single proof will cost us thousands of scalar multiplications alone. If we had 5 4-input transactions (which is how they'd be aggregated under MAX_INPUTS=4), the computational complexity would be a fraction.     

> __< r​ucknium:monero.social >__ FWIW, the current tx propagation protocol tends to clump txs together in single gopssip messages. About 75 percent of tx gossip messages have more than one tx. See Table 2 of my https://github.com/Rucknium/misc-research/blob/main/Monero-Black-Marble-Flood/pdf/monero-black-marble-flood.pdf     

> __< k​ayabanerve:matrix.org >__ (as the 4-input TXs would reasonably share their base cost with other TXs, making their cost an amortized percentage of the base cost and only the per-proof costs)     

> __< k​ayabanerve:matrix.org >__ Then for MAX_OUTPUTS, my advocacy to reduce it was so that one cannot be sent outputs faster than one can accumulate them. Since there's a logarithmic time bound, it isn't the end of the world to have exceed MAX_INPUTS. We can discuss reducing MAX_OUTPUTS however if we want to more conservative (while this discussion is on the table) or as we plan for input/output quantity uniformity.     

> __< k​ayabanerve:matrix.org >__ Rucknium: That is great to know, thank you.     

> __< r​ucknium:monero.social >__ The current tx propagation protocol isn't a true classical gossip protocol because the relay timers are per-connection, not per-tx `*` per-connection. Having timers only be per-connection makes txs clump more.     

> __< rbrunner >__ "one cannot be sent outputs faster than one can accumulate them" What means "accumulate" here?     

> __< k​ayabanerve:matrix.org >__ If I can send you 8 outputs in one TX, yet you can only use 4 outputs as inputs in a TX, you must make 2 transactions to get 2 outputs (which can be used in a single transaction).     

> __< r​ucknium:monero.social >__ IMHO, it may make sense to have a deep empirical analysis of the best parameters, given the composition of current tx ins/outs.     

> __< k​ayabanerve:matrix.org >__ Those 2 transactions would be to consolidate (accumulate) the received outputs.     

> __< rbrunner >__ Ah, I see. You could flood my wallet with enotes faster than I could consolidate them.     

> __< k​ayabanerve:matrix.org >__ My recommendation at this time is likely MAX_INPUTS = 4, or MAX_INPUTS = 8, with a sliding compute factor. The sliding compute factor would have lower-input transactions target the base-cost of higher-input transactions.     

> __< rbrunner >__ Will be interesting to see how all these new rules and restrictions and interrelationsships will play out. A whole new world, in a way.     

> __< k​ayabanerve:matrix.org >__ If we assume a batch verification, that's optimal for bandwidth and efficiency purposes, so long as whatever the MAX_INPUTS value is actually appears in most batches.     

> __< r​ucknium:monero.social >__ I have a very preliminary (i.e. have not double-checked for correctness) analysis of how output consolidation would affect input proof size and computational cost for a few different values of `MAX_INPUTS`: https://gist.github.com/Rucknium/784b243d75184333144a92b3258788f6     

> __< r​ucknium:monero.social >__ Preliminary summary: "The units are not yet interpretable, but the relative values can be compared between different MAX_INPUTS rules....The size cost metric is 9221, 9355, and 10205 for `MAX_INPUTS` = 4, 8, and 16, respectively. The computational cost metric is 7992, 10353, and 13727 for `MAX_INPUTS` = 4, 8, and 16, respectively."     

> __< k​ayabanerve:matrix.org >__ rbrunner: We can make it more interesting and have the compute factor be smaller over the weekend, give our computers and a couple days off /s     

> __< r​ucknium:monero.social >__ ^ This is an analysis of what happens when users would be forced to change their `inputs > MAX_INPUTS` txs into multi-stage consolidations     

> __< s​yntheticbird:monero.social >__ just so for the uneducated ones at the other side of the room. When you're discussing MAX_INPUTS parameters, you're talking about the limit of inputs a transaction under FCMP++ can contain? If so, are we limited by size or computational power?     

> __< k​ayabanerve:matrix.org >__ I don't expect more progress to be made on this today other than awareness and potential a minor amount of discussion on 4/8 for MAX_INPUTS.     

> __< k​ayabanerve:matrix.org >__ *potentially     

> __< k​ayabanerve:matrix.org >__ SynetheticBird: Both. A 210-input TX (which is currently allowed) would cause ~100k scalar multiplications in a DoSsy af spike to CPU use.     

> __< r​ucknium:monero.social >__ And my analysis assumes that there is no change in how coinbase txs are handled. Consolidation of P2Pool coinbase outputs create a lot of the high-input txs. This is a proposal to change that: https://github.com/monero-project/research-lab/issues/108     

> __< k​ayabanerve:matrix.org >__ Bandwidth isn't an issue at high-input counts, it amortizes quite well. Bandwidth is an issue at low-input counts due to the base cost.     

> __< s​yntheticbird:monero.social >__ nice try at writing my name + Is the scalar multiplication a work for the wallet (receiver? sender?) or the node?     

> __< k​ayabanerve:matrix.org >__ I'll also note this prioritizes the Curve Forests design which means eventually, Monero won't build one tree (cc jberman to comment on tree building) yet n trees where n == MAX_INPUTS.     

> __< k​ayabanerve:matrix.org >__ Curve Forests wouldn't benefit 1-input TX. It'd make TXs with more inputs even smaller though? I think I'm doing my math there right?     

> __< k​ayabanerve:matrix.org >__ It's a really weird scaling formula.     

> __< k​ayabanerve:matrix.org >__ The proof verification scalar multiplications DoS the node.     

> __< r​ucknium:monero.social >__ On curve forests: does it matter what the MAX_INPUTS are before a hypothetical curve forest activation, or is it good to have limited MAX_INPUTs because it prepares the ecosystem for a low MAX_INPUTS (setting aside the fact that we get better CPU load with MAX_INPUTS with curve _trees_ in the next hard fork)?     

> __< k​ayabanerve:matrix.org >__ All of these proof timing/size discussions really are about nodes (eh, wallet upload bandwidth requirements can also be argued).     

> __< k​ayabanerve:matrix.org >__ Rucknium: If we set MAX_INPUTS to 8 now, I'd go around saying it'll probably eventually become 4. I wouldn't say it's 8 and will likely remain 8.     

> __< s​yntheticbird:monero.social >__ ok thx for the explanations on the dos vector     

> __< r​ucknium:monero.social >__ My question is basically about backward/forward compatibility     

> __< k​ayabanerve:matrix.org >__ The eventual line of progress I see is with a low MAX_INPUTS *unless* we resolve proof folding (which almost certainly doesn't make sense at this scale).     

> __< k​ayabanerve:matrix.org >__ We don't have to set the end-goal low MAX_INPUTS now. We do need to set a reasonable MAX_INPUTS and I'd personally call it an interim MAX_INPUTS for people to adjust to it going even lower.     

> __< k​ayabanerve:matrix.org >__ (though setting a MAX_INPUTS now doesn't lock-in some future MAX_INPUTS, obviously we'd have further discussions when the time comes depending on what makes sense at the time)     

> __< r​ucknium:monero.social >__ 5) FCMP++ Optimization Competition https://github.com/kayabaNerve/fcmp-plus-plus-optimization-competition     

> __< k​ayabanerve:matrix.org >__ I drafted a competition for anyone to write more efficient implementations of Helios/Selene (affects everything) / divisor calculation (solely affects the prover and is IMO acceptable at this point in time).     

> __< k​ayabanerve:matrix.org >__ tevador prior said they'd do an optimized Helios/Selene. tevador has been incommunicado for some months now.     

> __< r​ucknium:monero.social >__ Would this efficient implementation need to be audited for mainnet deployment?     

> __< k​ayabanerve:matrix.org >__ We can either find an explicit entity to do the work or post an open contest. Then we can aggregate pieces of the submissions for some super lib (or just accept the best one as-is).     

> __< k​ayabanerve:matrix.org >__ I did my best to create a clear set of rules to that end.     

> __< k​ayabanerve:matrix.org >__ `  - name: Audit the implementation of the Towering Curve Cycle`     

> __< k​ayabanerve:matrix.org >__ Yes     

> __< k​ayabanerve:matrix.org >__ Also, no, I'm not outsourcing my own work.     

> __< k​ayabanerve:matrix.org >__ > This will also include an implementation of the towering curve cycle, Helios and Selene, though not one expected to be performant enough for deployment.     

> __< k​ayabanerve:matrix.org >__ I was clear in my CCS I don't expect my impl to be production grade. The fact we did achieve ~13ms when batch verifying FCMPs was a surprise I was quite happy with.     

> __< k​ayabanerve:matrix.org >__ As we now discuss increase the compute factor (decreasing bandwidth, increasing computational time), it's worth prioritizing reducing the cost of each operation of Helios/Selene to balance that out.     

> __< j​berman:monero.social >__ why pay so much more for ec-divisors versus helioselene, especially considering ec-divisors is acceptable and helioselene isn't right now?     

> __< k​ayabanerve:matrix.org >__ (also, jberman has been bothering me about the time to build the tree which this also helps with)     

> __< k​ayabanerve:matrix.org >__ I said I think ec-divisors is acceptable.     

> __< k​ayabanerve:matrix.org >__ I also am not Monero Customer Support and don't have to deal with anyone complaining proving FCMPs takes longer than ring signatures did.     

> __< s​yntheticbird:monero.social >__ Would a bounty rewards be appropriate for the competition.     

> __< k​ayabanerve:matrix.org >__ ec-divisors is non-trivial *and will be cause user complaints if wallets don't do their jobs properly*.     

> __< j​berman:monero.social >__ helioselene will cause complaints even if wallets do their jobs properly at this point     

> __< k​ayabanerve:matrix.org >__ ec-divisors, with EC FFT, would presumably be anywhere from 50-80% faster. It just requires someone implement EC FFT which is probably a few weeks of work.     

> __< k​ayabanerve:matrix.org >__ Helioselene will or tree building will which you're now blaming helioselene for?     

> __< k​ayabanerve:matrix.org >__ (not to say that's unfair blame, to clarify what aspect we're complaining about)     

> __< j​berman:monero.social >__ referring to tree building, which uses helioselene     

> __< rbrunner >__ Do we have any known examples of somewhat similar competitions, and how they turned out? Right now I am a bit sceptic of the approach, I confess, i.e. will this attract talent?     

> __< k​ayabanerve:matrix.org >__ Anyways. The work to optimize Helioselene is much less than the work to optimize ec-divisors. The rewards are representative of that.     

> __< r​ucknium:monero.social >__ Maybe make stricter rules about first/second best so that someone cannot submit their first-best implementation with `sleep(0.0001)` to get both prizes.     

> __< k​ayabanerve:matrix.org >__ We can find people to do these tasks, we can host one competition (not both), or I can do the work necessary to action this.     

> __< k​ayabanerve:matrix.org >__ Rucknium: I am planning a rule which does say the judges can just disqualify anything not usable/not in good faith. I'm just wondering how to phrase it in a way which isn't too hostile :(     

> __< k​ayabanerve:matrix.org >__ I'm trying to provide clear rules to minimize drama and to set clear expectations, but it's already such a list of rules because people can find all sorts of loop-holes.     

> __< k​ayabanerve:matrix.org >__ rbrunner: There was one, I can pull it up.     

> __< k​ayabanerve:matrix.org >__ I'm also unsure this will work out in practice. I'm not here to die on the hill of doing this content.     

> __< k​ayabanerve:matrix.org >__ https://zprize.io     

> __< rbrunner >__ Interesting     

> __< s​yntheticbird:monero.social >__ The competition aims at collecting an implementation that is production ready for a security-critical project. We expect researchers and talents to respect this goal by not providing PoC, prototypes that only fulfill the algorithm characteristics without giving any importance to the level of quality we could expect for a production-ready software.     

> __< j​berman:monero.social >__ "Prize winners will be determined in good faith and in the sole discretion of prize sponsors" seems solid     

> __< s​yntheticbird:monero.social >__ forgot the quotes     

> __< rbrunner >__ USD 500'000 price pools sound impressive     

> __< r​ucknium:monero.social >__ I think this competition is a good idea, FWIW     

> __< j​berman:monero.social >__ (at the bottom of zprize.io)     

> __< k​ayabanerve:matrix.org >__ Yes I am not proposing 500,000 yet ~50,000, which may be one of the reasons we fail to attract talent :(     

> __< rbrunner >__ They take their toys and play elsewhere :)     

> __< k​ayabanerve:matrix.org >__ I'd be a lot more confident at 100k yet it's hard to argue spending 100k on this.     

> __< s​yntheticbird:monero.social >__ make a CCS for real. there is already 0xfffc in the race     

> __< s​gp_:monero.social >__ At least Monero is cool, it's not some silly goal. It's practical. That'll help attract interest     

> __< k​ayabanerve:matrix.org >__ SyntheticBird: A GPU impl would be disqualified :/     

> __< rbrunner >__ Is optimizing the current solution for a few percents of speed gain admissible, according to the rules right now?     

> __< k​ayabanerve:matrix.org >__ We need this to work on VPSs.     

> __< s​yntheticbird:monero.social >__ kayabnerve: 0xfffc is a *"performance engineer"* from what he said. he should be able to make CPU optimization as well     

> __< k​ayabanerve:matrix.org >__ I'd independently 100% support a CCS for GPU-accelerated Android/iOS tree building/scanning..     

> __< k​ayabanerve:matrix.org >__ rbrunner: Floor improvement of 20%.     

> __< rbrunner >__ Good.     

> __< k​ayabanerve:matrix.org >__ SyntheticBird: Yeah, I'd love to see them participate. I just want to be clear GPU unfortunately isn't a valid submission *for this proposal*     

> __< s​yntheticbird:monero.social >__ ack     

> __< j​berman:monero.social >__ what if we reach out to the winners of zprize.io and see if they have thoughts on the contest/if they'd be interested if we did a contest?     

> __< k​ayabanerve:matrix.org >__ Neither is SIMD which I'm more pissier about. SIMD is effectively universal and would be great to build Helioselene around.     

> __< k​ayabanerve:matrix.org >__ The issue is we'd have to write SIMD for each platform or use a third-party SIMD abstraction.     

> __< k​ayabanerve:matrix.org >__ jberman: I wouldn't expect sponsorship yet can email them with the topic :)     

> __< r​ucknium:monero.social >__ IIRC, MoneroNodo wanted some monerod code for GPU since the machine has a GPU.     

> __< s​yntheticbird:monero.social >__ kayabanerve: I feel like that with FCMP++ all the web wallet project relying on web assembly compilation are going to sink deep into the cold abyss. no gpu no simd, no anything in the web realm     

> __< k​ayabanerve:matrix.org >__ It isn't that I don't support GPU backends. I completely do. I just can't advocate GPU backends in this discussion over increasing the baseline. I feel that has to be a separate discussion.     

> __< r​ucknium:monero.social >__ We have two more agenda items.     

> __< k​ayabanerve:matrix.org >__ WebGPU?     

> __< k​ayabanerve:matrix.org >__ WASM has a GPU API     

> __< r​ucknium:monero.social >__ 6) Reviews for Carrot. https://github.com/jeffro256/carrot/blob/master/carrot.md     

> __< r​ucknium:monero.social >__ jeffro256:  Anything to discuss about Carrot at this meeting?     

> __< k​ayabanerve:matrix.org >__ There's also WASM SIMD proposals AFAIK, they're just limited to 128-bit. I think some are usable in real life?     

> __< s​yntheticbird:monero.social >__ kayabaNerve: afaik webGPU compute shaders are still experimental and SIMD is considered in the WASM community to be unlikely to merge anytime soon.     

> __< r​ucknium:monero.social >__ jeffro wasn't in the greetings     

> __< k​ayabanerve:matrix.org >__ we're missing jefrro :(     

> __< j​berman:monero.social >__ zprize 2023 winners: https://www.zprize.io/blog/announcing-the-2023-zprize-winners , 2022 winners: https://www.zprize.io/blog/announcing-zprize-results     

> __< r​ucknium:monero.social >__ 7) Proposal for FCMP++ HF Activation Rule to Retroactively Ignore Future `unlock_time` https://github.com/monero-project/research-lab/issues/125     

> __< k​ayabanerve:matrix.org >__ SyntheticBird: SIMD is supported by v8 and SpiderMonkey. There's existing teams doing EC on WebGPU (it was one of the zprize discussions).     

> __< r​ucknium:monero.social >__ IIRC, there was a not yet a consensus view on the timing of the retroactive disabling of `unlock_time`     

> __< s​yntheticbird:monero.social >__ re: 7.     

> __< s​yntheticbird:monero.social >__ as long as we alert users through every channels that we reserve the right to do so its okay really.     

> __< s​yntheticbird:monero.social >__ kayabanerve: TIL     

> __< k​ayabanerve:matrix.org >__ I thought we agreed on May 1st with the threat  of moving it up.     

> __< r​ucknium:monero.social >__ The Monero Twitter could be excited about disabling `unlock_time`     

> __< m​onerobull:monero.social >__ >What this proposal does NOT do     

> __< m​onerobull:monero.social >__     Invalidate currently existing unlock_time values     

> __< m​onerobull:monero.social >__ rip to infinity exchanger, 2 years remaining     

> __< rbrunner >__ I don't remember either substantial opposition against May 1 from last meeting, but well the protocol has the details of course     

> __< k​ayabanerve:matrix.org >__ something something monero-wallet's scanner api doesn't expose received outputs until you explicitly handle their timelock conditions     

> __< s​yntheticbird:monero.social >__ I propose we move the limit to May 21st because its the international tea day and we could sip tea regarding locked tx being unlocked     

> __< r​ucknium:monero.social >__ I think rbrunner, kayabaNerve, and myself were OK with May 1, with threat to make the date earlier if an adversary starts spamming. Do we have more opinions?     

> __< k​ayabanerve:matrix.org >__ something something safer ux which would save real users real money     

> __< r​ucknium:monero.social >__ logs from last meeting: https://libera.monerologs.net/monero-research-lab/20241023#c450652     

> __< rbrunner >__ I see, not only the Twitter, kayabynerve is "excited" as well     

> __< s​yntheticbird:monero.social >__ last meeting was allergic to easter eggs     

> __< r​ucknium:monero.social >__ Looks like jeffro was OK with May 1st, too.     

> __< j​berman:monero.social >__ +1 to an announcement saying May 1 is a soft target, is also contingent on fcmp++, and moving it earlier is also still a possibilty. A blog post + Monero twitter account linking to blog post would be solid     

> __< s​yntheticbird:monero.social >__ I'll make the reddit post I need more karma     

> __< r​ucknium:monero.social >__ The rules for missing a meeting is that you have to do any chores proposed at a meeting, jeffro256 . :P     

> __< j​effro256:monero.social >__ So sorry I missed the meeting! Yes I am okay with May 1st. And no, nothing to comment on regarding Carrot at the moment     

> __< r​ucknium:monero.social >__ One comment to get out of chores 😱     

> __< j​effro256:monero.social >__ Who needs their floors mopped?     

> __< r​ucknium:monero.social >__ I think we have loose consensus on making an announcement about the May 1st deadline, with the condition about FCMP++ activation and the caveat of possibly moving the date earlier if there is an attempted malicious DoS.     

> __< r​ucknium:monero.social >__ Well, I was going to suggest that jeffro write the post, but he showed up     

> __< r​ucknium:monero.social >__ We can end the meeting here. Thanks everyone.     

> __< j​effro256:monero.social >__ We should include a proposed block index value in the announcement as well IMO     

> __< j​effro256:monero.social >__ Will calculate that now     

> __< j​effro256:monero.social >__ I will note that using the CLSAG activation height and timestamp as a way to predict block heights of future timestamps is already off by by 44 days for predicting the *current* block     

> __< j​effro256:monero.social >__ The expected timestamp for block 3270595 using the CLSAG activation height is `1726433957 = (3270595 - 2688888) * 120 + 1656629117`. The actual is 1730312167, which is `(1730312167 - 1726433957) / 60 / 60 / 24 = 44 days` ahead of schedule     

> __< j​effro256:monero.social >__ It's still ~94% accurate, but the error will build up to be >1.5 months by May 1st     

> __< j​effro256:monero.social >__ Can we use `block_index = 3270000`, `timestamp = 1730243700` as our anchor ?     

> __< 0​xfffc:monero.social >__ Yes, and I am willing to implement ( at least a prototype version of them ) on my own dev work CCS and without submitting extra CCS.      

> __< 0​xfffc:monero.social >__ Having a prototype parallel implementation will help me understand the parallelization opportunities. Might help us better judge the competitors too.      

> __< 0​xfffc:monero.social >__ The only blocker, as I admitted in the other room is my lack of knowledge about the algorithms (helioselene and eventually ec-divisors).     

> __< k​ayabanerve:monero.social >__ The Rust lib is only about a thousand lines IIRC. Point doubling, addition, and then double-and-add mul shouldn't be horrific.     

> __< b​lurt4949:matrix.org >__ Another stupid question regarding input counts in FCMP++: How difficult would it be to split large input transactions (say, 100-in) into several smaller "proof groups" (in this case, if MAX_INPUTS = 4, then 25)? Meaning, each group would function as if they were inputs to separate transactions, but their amount commitments, signed message, etc still contributing to the actual tran<clipped message>     

> __< b​lurt4949:matrix.org >__ saction. Seems to avoid the issue of inconvenient consolidation transactions, and is also more efficient since it doesn't require making several new outputs, privacy concerns about input/output count fingerprinting aside.     

> __< b​lurt4949:matrix.org >__ (Forgive me if I'm butchering terminology here, and am unclear)     

> __< 0​xfffc:monero.social >__ I see what you saying and you are correct. But I have a habit of doing r&d and understanding the picture before jumping into the code. Questions like how FCMP works, where these algorithms are used, etc etc etc (maybe bad habit from doing r&d in grad school )     

> __< k​ayabanerve:monero.social >__ blurt4949: Then the cost is bandwidth. A 210-input TX would consume an entire block of space. Doing a series of proofs was part of the original proposal however.     

> __< k​ayabanerve:monero.social >__ But yes, we can set MAX_PROOF_INPUTs = 4 and go from there.     

> __< k​ayabanerve:monero.social >__ 0xfffc: I respect your eagerness and your knowledge on this field. I apologize I'm unable to match your eagerness and contribute my knowledge on this field.     

> __< k​ayabanerve:monero.social >__ I don't give short answers to he unhelpful. It's the extent I'm willing to help *at this moment*. You will have to figure it out from there or we will have to mutually convene when I have more time.     

> __< j​effro256:monero.social >__ I propose tentatively setting ignore-unlock-time block index `J` to 3401782, with threat of setting earlier. https://github.com/monero-project/research-lab/issues/125#issuecomment-2448077632. We can discuss this in the next meeting, though     

> __< 0​xfffc:monero.social >__ No need to apologies. We all trying to learn. And totally understandable about being short on time. Though I hope when we both had spare time, we can collaborate on this :)     

> __< k​ayabanerve:monero.social >__ jeffro256: Why not declare a Unix timestamp and in 6 months, we find the first block to exceed it?     

> __< k​ayabanerve:monero.social >__ Why hardcode a block now?     

> __< k​ayabanerve:monero.social >__ It's worse for human understanding and isn't portable to the testnets.     

> __< k​ayabanerve:monero.social >__ Dynamically saying first block whose on-chain time exceeds May 1st, 2025 is portable, easy to understand, and valid     

> __< 0​xfffc:monero.social >__ I agree ☝. Unix timestamp would be simple solution. And I always like simple solutions.     

> __< k​ayabanerve:monero.social >__ 0xffc: helioselene defines two prime fields and additionally uses (but does not itself define) the 2**255-19 prime field seen in Ed25519. If you have implementations of those three fields and arithmetic over them (add, sub, mul, multiplicative inverse), you can define points in Projective coordinates and the universal point addition formulas present within the helioselene library.     

> __< j​effro256:monero.social >__ kayabanerve: this might not be a huge issue, but using a "first past the post" rule for activating the rule might cause small griefing incentive for the miners to set their block timestamp past the activation timestamp, even if it's not that time yet. IIRC, this can only cause a jump 2(?) hours in the future     

> __< k​ayabanerve:monero.social >__ With point addition, you can build scalar multiplication.     

> __< k​ayabanerve:monero.social >__ The tree hash is just a bunch of scalarmuls.     

> __< k​ayabanerve:monero.social >__ jeffro256: on-chain time, not header time.     

> __< 0​xfffc:monero.social >__ Thanks. Will do my research and that is a good starting point.     

> __< k​ayabanerve:monero.social >__ We already have an in-consensus sufficiently-hard-to-manipulate clock.     

> __< j​effro256:monero.social >__ the rule could be that for the first block where `Blockchain::get_adjusted_time()` exceeds the target timestamp, we activate, but I want to deprecate that method since it isn't a reliable (AKA monotonic) clock, even if deterministic     

> __< k​ayabanerve:monero.social >__ It is monotonic     

> __< k​ayabanerve:monero.social >__ It doesn't guarantee increment yet it is monotonic as soon as it's populated     

> __< k​ayabanerve:monero.social >__ (monotonic just requires it doesn't decrement, not that it can't return the same value multiple times)     

> __< k​ayabanerve:monero.social >__ I had to do this review while working on Serai, I'll link it     

> __< k​ayabanerve:monero.social >__ https://github.com/serai-dex/serai/blob/next/processor%2Fmonero%2Fsrc%2Frpc.rs#L53     

> __< k​ayabanerve:monero.social >__ Basically, checking you're greater than the median always ensures the value pushed is on the right-hand side of the median.     

> __< k​ayabanerve:monero.social >__ You either have a removal on the left hand side or a removal on the right hand side. A removal on the right hand side causes a NOP to the median value. A removal on the left hand side makes one of the more-right values (higher-valued) the new median.     

> __< k​ayabanerve:monero.social >__ The median itself being removed is equivalent to a value from the left-hand side being removed. A more right value will take its place.     

> __< k​ayabanerve:monero.social >__ I should've linked the relevant rule there. Apologies for not doing so.     

> __< k​ayabanerve:monero.social >__ You also can achieve an always incrementing clock by adding the block height to the time. That causes excessive drift however.     

> __< j​effro256:monero.social >__ It would be monotonic if `get_adjusted_time` *only* returned the median of N timestamps where consensus rules verified each new timestamp is greater than or equal to the median of the last N, but the verrry last line of `get_adjusted_time` blows this up by returning the min of the median of the last N timestamps and the "adjusted_current_block_ts", which is a function purely of the last timestam     

> __< k​ayabanerve:monero.social >__ ... Oh, so the issue isn't the protocol, it's this one stupid fn around the protocol's defined object     

> __< j​effro256:monero.social >__ Well it's used in consensus for transaction unlock times, but not for block timestamps     

> __< j​effro256:monero.social >__ Why? Beats the hell out of me....     

> __< k​ayabanerve:monero.social >__ Just copy/paste it without the min?     

> __< k​ayabanerve:monero.social >__ Also, wait, are block timestamps compared to the median or the result of this adjusted time fn? Did I mess up?     

> __< k​ayabanerve:monero.social >__ And does this collapse 🤔     

> __< k​ayabanerve:monero.social >__ The median must always be <= the last timestamp so it'll be the branch always taken by this min as soon as the timestamp is populated, right?     

> __< j​effro256:monero.social >__ Block timestamps are just compared to the median of the last `BLOCKCHAIN_TIMESTAMP_CHECK_WINDOW=60`  blocks     

> __< k​ayabanerve:monero.social >__ When would the most recent timestamp ever be the smaller value? When the median isn't populated yet?     

> __< k​ayabanerve:monero.social >__ Except then the median returns 0 AFAIK, it won't use a partial window.     

> __< k​ayabanerve:monero.social >__ And why not just hook our ignore unlock time after code into this same logic? Why explicitly use get_adjusted_time?     

> __< j​effro256:monero.social >__ I'd very much rather use a raw median over `get_adjusted_time`. The downside over a hardcoded fork height is that it requires additional RPC logic to implement     

> __< j​effro256:monero.social >__ or when the miner is naughty     

> __< k​ayabanerve:monero.social >__ That isn't an answer     

> __< k​ayabanerve:monero.social >__ How can they be naughty when they must exceed the median     

> __< j​effro256:monero.social >__ Lemme think if that is possible. It's a median against different  set of blocks (off by one)     

> __< j​effro256:monero.social >__ But it would be a newer set of blocks     

> __< j​effro256:monero.social >__ So it might not be possible     

> __< b​oog900:monero.social >__ `get_adjusted_time` returns the minimum of the adjusted median and the adjusted top timestamp.     

> __< b​oog900:monero.social >__ adjusted median = median + 3660     

> __< b​oog900:monero.social >__ adjusted top timestamp = top timestamp + 120     

> __< b​oog900:monero.social >__ so the top timestamp could still be above the median but below the adjusted median     

> __< k​ayabanerve:monero.social >__ Ah. Thanks boog900     

> __< k​ayabanerve:matrix.org >__ jeffro256: So why not use the raw median? Why would this require any RPC logic?     

> __< k​ayabanerve:matrix.org >__ Whenever we do the check the block time is over the median, if we haven't prior saved the block over the pole to the disk, we save that block     

> __< k​ayabanerve:matrix.org >__ When processing TXs, if in a block over the pole, we ignore the timelock     

> __< k​ayabanerve:matrix.org >__ ez    


# Action History
- Created by: Rucknium | 2024-10-29T21:05:26+00:00
- Closed at: 2024-11-07T18:55:16+00:00
