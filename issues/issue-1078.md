---
title: Monero Research Lab Meeting - Wed 18 September 2024, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/1078
author: Rucknium
assignees: []
labels: []
created_at: '2024-09-18T16:56:31+00:00'
updated_at: '2024-10-01T21:06:54+00:00'
type: issue
status: closed
closed_at: '2024-10-01T21:06:54+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

[Join the Monero Matrix server if you don't already have a Matrix account.](https://web.archive.org/web/20230128130949/https://forum.monero.space/d/79-how-to-join-the-monero-core-team-matrix-server-web)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/converter.html?iso=20211027T170000&p1=1440)

Main discussion topics:

1. Greetings

2. Updates. What is everyone working on?

3. [Stress testing `monerod`](https://github.com/monero-project/monero/issues/9348)

4. Research [Pre-Seraphis Full-Chain Membership Proofs](https://www.getmonero.org/2024/04/27/fcmps.html). Reviews for [Carrot](https://github.com/jeffro256/carrot/blob/master/carrot.md).

5. 10 block lock discussion: https://github.com/monero-project/research-lab/issues/102#issuecomment-1577827259 , [Monero output lock analysis](https://github.com/AaronFeickert/pup-monero-lock/releases/tag/final)

6. Chainalysis capabilities video.

7. Any other business

8. Confirm next meeting agenda


Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: Rucknium

Previous meeting agenda/logs:

#1070 

# Discussion History
## Rucknium | 2024-09-24T14:28:33+00:00
> __< Rucknium >__ Meeting time! https://github.com/monero-project/meta/issues/1078     

> __< Rucknium >__ Welcome to an IRC-only edition of MRL meeting     

> __< Rucknium >__ The monero.social Matrix server is down     

> __< rbrunner >__ Hello. Hehe, last week I was the last holdout on IRC, not on Matrix ...     

> __< Rucknium >__ 1) Greetings     

> __< chaserene >__ hello     

> __< xFFFC0000 >__ Hi everyone.     

> __< jeffro256 >__ howdy from IRC     

> __< Rucknium >__ 2) Updates. What is everyone working on?     

> __< Rucknium >__ me: Mostly working on N block lock analysis     

> __< jeffro256 >__ me: working on an enote store for Carrot      

> __< jberman >__ *waves*, me: continuing on fcmp's, about to start on tx construction     

> __< Rucknium >__ 3) Stress testing monerod https://github.com/monero-project/monero/issues/9348     

> __< xFFFC0000 >__ me: finished the fast pop_blocks and flush_txpool. Will submit for review. Finishing the issues jeffro mentioned for rpc limit fix right now.     

> __< Rucknium >__ There has been discussion here about how to put wallet-monerod RPC calls in "chunks", which is important when the txpool is large: https://github.com/spackle-xmr/monero/pull/32     

> __< Rucknium >__ Thanks to patches from plowsof and tobtoht, the stressnet repo's builds and tests are all passing with green checkmarks     

> __< plowsof >__ (i changed a few chars of a regex to make a version string pass ^^)     

> __< Rucknium >__ 4) Research Pre-Seraphis Full-Chain Membership Proofs. Reviews for Carrot. https://github.com/jeffro256/carrot/blob/master/carrot.md     

> __< jeffro256 >__ 0xFFFC0000: for the record, were there actual instances of hitting the LEVIN_DEFAULT_MAX_PACKET_SIZE limit during the get_blocks call or was this precautionary?     

> __< jberman >__ I haven't fully read that PR code, but to avoid that issue of gaps in the request, the restricted endpoint serves all of the pool's tx hashes in the first response respecting the time of the request, then the client will then fetch all the blobs in chunks     

> __< xFFFC0000 >__ jeffro256: there was. When I was debugging I was getting failure if I don’t introduce that limitation     

> __< xFFFC0000 >__ jberman: that totally makes sense. Strange I didn’t notice it. If we serve hashes in first request, then technically we will be consistent in response.     

> __< xFFFC0000 >__ s/request/response/     

> __< jeffro256 >__ jberman: are you saying that that is what it *should* do, or what the wallet *currently* does? AFAIK the wallet just repeatedly calls /get_blocks with incremental pool updates      

> __< jberman >__ when pointing to a restricted rpc that's what it does. the restricted daemon will serve tx hashes in a field remaining_added_pool_txids on the first request, then the client requests those in chunks     

> __< jberman >__ just piggy-backing off that logic i think may be simpler     

> __< jberman >__ https://github.com/monero-project/monero/blob/a1dc85c5373a30f14aaf7dcfdd95f5a7375d3623/src/wallet/wallet2.cpp#L3105-L3117     

> __< rbrunner >__ Ah, that's some of the stuff you built on top my own PR     

> __< xFFFC0000 >__ The restricted and unrestricted are same algorithm fundamentally?     

> __< jberman >__ then `m_node_rpc_proxy.get_transactions` requests in 100 tx chunks     

> __< jberman >__ yes so current wallet2 wallets using this endpoint should automatically know to get chunked requests even if a non-restricted daemon updates to use this logic     

> __< jeffro256 >__ Hmmm that's weird that I didn't notice that before. Technically, this is not guaranteed to be consistent if I understand that code correctly; txs may leave the pool between calls to /get_blocks and /get_transactions     

> __< xFFFC0000 >__ Exactly what I was thinking. Thanks a lot.     

> __< xFFFC0000 >__ jeffro but you get the hashes of all txis at the time of first request.     

> __< rbrunner >__ Well, if you get anything in chunks it's impossible to avoid that, no?     

> __< jeffro256 >__ rbrunner: not necessarily, if you obtain the transaction data in a way that respects pool update times      

> __< jberman >__ if it's not in the pool then read_pool_txs won't add it     

> __< rbrunner >__ Right.     

> __< jberman >__ and the request shouldn't fail since it's using /get_transactions which includes both pool and non-pool txs     

> __< jeffro256 >__ It could in the pool, then served in remaining_added_pool_txids, and then pushed out of the pool before the  follow-up call to /get_transactions, right?     

> __< jberman >__ right, in which case read_pool_txs won't add it to the struct the pool logic uses to process pool txs     

> __< jeffro256 >__ If it's served in added_pool_txs, that should be fine as long as the packet size isn't too big      

> __< jberman >__ fwiw I still don't think there's a perfect way to do this, since prior txs you already read may also exit the pool by the time all chunks are complete     

> __< jeffro256 >__ Okay so we just need to adjust the balancing between added_pool_txs and remaining_added_pool_txids on the daemon side then?     

> __< jberman >__ I think this is a reasonable approach (and it also mirrors what wallets did before the incremental time logging change)     

> __< jeffro256 >__ ... Assuming the the TXIDs don't take up up the max packet size     

> __< jberman >__ ya it won't work if txids take up max packet size     

> __< jeffro256 >__ That's like, what 3 million txs added in the pool since the last fetch?     

> __< jberman >__ haha what's the size again?     

> __< xFFFC0000 >__ 100mb for max levin package size.     

> __< jberman >__ yep ~3mn txs     

> __< Rucknium >__ Do we need more time for discussion on this?     

> __< jeffro256 >__ I think that should be fine     

> __< Rucknium >__ 4) Research Pre-Seraphis Full-Chain Membership Proofs. Reviews for Carrot. https://github.com/jeffro256/carrot/blob/master/carrot.md     

> __< jeffro256 >__ I followed up with some more firms since the last meeting, one has responded back and said that they will have a proposal soon     

> __< jeffro256 >__ A couple of minors changes to the spec also     

> __< jeffro256 >__ Not much other than that at the moment, though     

> __< Rucknium >__ Different FCMP topic: From what I understand, monerod will still provide an RPC endpoint that would allow wallets to construct the FCMP input proofs, as a backup to wallet-side merkle tree cacheing. Therefore, a decoy distribution is still needed.     

> __< Rucknium >__ Is that correct, as of current plans?     

> __< jeffro256 >__ Yes     

> __< jberman >__ It has been then plan, but the more I'm thinking on it, the less I think it needs to be there. Even light wallet servers would be able to keep track of owned paths today using just the view key     

> __< jberman >__ It's only when we have that "filter-assist" light wallet tier when light wallets would definitely need that endpoint     

> __< Rucknium >__ My short-term plan is to finish up some of the black marble research items, finish the OSPEAD estimation with current data, then possibly work on fee uniformity and/or evaluation of Clover.     

> __< Rucknium >__ Which the OSPEAD estimate would provide the decoy distribution if it is needed in the final FCMP codebase.     

> __< Rucknium >__ It would be good to get fee uniformity and Clover investigated before the FCMP hard fork, too     

> __< jeffro256 >__ I worry about pushing some mobile wallets (or wallets with lazy devs) into becoming de-facto light wallets if they are either forced to implement wallet-side tree building in a short time or become a light wallet      

> __< rbrunner >__ Hmmm, I was thinking most of them use wallet2 at their core     

> __< jberman >__ ya and wallet2 will do it     

> __< jeffro256 >__ Yes, the ones that use wallet2 would be fine      

> __< rbrunner >__ And the rest MyMonero or MyMonero tech     

> __< Rucknium >__ AFAIK, Exodus has custom code that works with remote nodes.     

> __< jberman >__ isn't Exodus a light wallet too?     

> __< jeffro256 >__ Rucknium: we might add an additional daemon output distribution that covers all the outputs that FCMP would be able to spend from (which is everything not malformed), as opposed to the RingCT distribution. I don't know if that would affect your research     

> __< Rucknium >__ No. You can choose your own remote node with Exodus Desktop at least. And I think Mobile, too (check with tobtoht)     

> __< jberman >__ I think switching a full wallet to a light wallet is way more work than using the new client-side tree building algo when syncing      

> __< jeffro256 >__ You might be right      

> __< rbrunner >__ Well, Exodus is multi-coin, and not open source, last time I checked.     

> __< Rucknium >__ Basically, it wouldn't because non-RingCT outputs are spent verry rarely. Just ned to make sure that the support of the distribution has positive probability to the beginning of the chain. Basically every distribution I am working with has unbounded support, so they satisfy that     

> __< Rucknium >__ IIRC Exodus produces about 5 percent of Monero txs     

> __< rbrunner >__ Yeah, and I was the one coining the motto "No wallet left behind" :)     

> __< jberman >__ if Exodus isn't using wallet2 and implemented their own syncing logic, they should be more than capable of porting the tree building sync algo     

> __< rbrunner >__ That RPC call would not be very expensive to implement, I guess?     

> __< jeffro256 >__ Probably not      

> __< jberman >__ no it's a very simple endpoint     

> __< Rucknium >__ There were a bunch of wallets that missed the Aug 2022 hard fork deadline, including Exodus. AFAIK the main change was view tags.     

> __< jeffro256 >__ We also need an RPC endpoint that compresses the tree before a certain client-specified height anyways unless we want to force every user to resync their wallet from height 0     

> __< jberman >__ yep     

> __< Rucknium >__ I have a table of which wallets missed the deadline here: https://github.com/Rucknium/misc-research/tree/main/Monero-Nonstandard-Fees#determining-which-wallets-are-creating-transactions-with-nonstandard-fees     

> __< Rucknium >__ I think a lot of those wallets in the table used LWS/MyMonero code     

> __< Rucknium >__ 5) 10 block lock discussion https://github.com/monero-project/research-lab/issues/102     

> __< Rucknium >__ I have been working on kayabaNerve's query from last meeting, which I thought would be "easy". I am still not completely satisfied with my probability model, so I don't have computations to share yet.     

> __< c​haserene:matrix.org >__ FYI, the availability of the monero.social Matrix is very spotty on my end. I still haven't received Rucknium's 15:08 UTC reminder either on my monero.social or my matrix.org account, I only see it on https://libera.monerologs.net/monero-research-lab/20240918     

> __< c​haserene:matrix.org >__ whoever can read this: try from IRC (e.g. HexChat: https://hexchat.github.io/downloads.html). that at least seems to work.     

> __< b​asses:matrix.org >__ there are issues with monero.social currently     

> __< Rucknium >__ Does anyone have access to this paper? Jiang & Zhang (2024) "Profitability Analysis of Time-Restricted Double-Spending Attack on PoW-Based Large Scale Blockchain With the Aid of Multiple Types of Attacks" https://ieeexplore.ieee.org/document/10644062     

> __< Rucknium >__ Published just last month     

> __< r​ottenwheel:kernal.eu >__ PSA. monero.social Matrix homeserver is down. If you still want to participate in today's MRL meeting, use a different homeserver or join through IRC.     

> __< chaserene >__ (^I guess monero.social is back.)     

> __< chaserene >__ (old messages incoming)     

> __< r​ottenwheel:kernal.eu >__ Or perhaps it'll be postponed till homeserver is back up. We'll find out soon.     

> __< rbrunner >__ If you think it can't get any worse ... then you are bombarded with hours' old messages     

> __< Rucknium >__ 6) Chainalysis capabilities video.     

> __< Rucknium >__ Any more thoughts on the video?     

> __< chaserene >__ back on topic: IMHO if we were to use Kayaba's requirement from the last meeting, 10 blocks seem to be...too low     

> __< Rucknium >__ There is a huge difference between an adversary having 10 percent and an adversary having 30 percent of hashpower     

> __< rbrunner >__ I don't think that anything more than 10 is viable for "political" reasons - I don't think will swallow that.     

> __< rbrunner >__ *people will swallow that     

> __< rbrunner >__ Not that this should disturb any research, of course     

> __< Rucknium >__ Endor made some nice tables of historical deep re-orgs on other chains: https://gist.github.com/endorxmr/a13dce62ae1ba4676a1ed0311d96bf07     

> __< chaserene >__ Rucknium: yes. I guess this is about trying to guess what capabilities the adversary has, which we can't know for certain.     

> __< chaserene >__ rbrunner: I would agree     

> __< 0​xfffc:monero.social >__ ( I can’t vouch for this service. But some people are using it successfully to access scientific papers :     

> __< 0​xfffc:monero.social >__ https://www.smartquantai.com     

> __< 0​xfffc:monero.social >__ )     

> __< chaserene >__ Endor's table is interesting, would be even more useful w/ reorg depths (in hour terms)     

> __< Rucknium >__ At least with this research we can say for some N lock time, chosen by heuristics, politics, or otherwise, _this_ is the risk profile.     

> __< rbrunner >__ Fully agree, that's very useful in any case     

> __< Rucknium >__ I think we can end the meeting here. Thanks everyone.     

> __< jeffro256 >__ Thanks everyone!     

> __< chaserene >__ Rucknium: no doubt about that. I'm curious though to understand, what parameters would such a risk profile include?     

> __< chaserene >__ BTW, thank you all     

> __< Rucknium >__ Adversary's hashpower share and how long they possess it. Any ideas on any other ones to include?     

> __< chaserene >__ got it, so this is similar to the table you presented last week. Endor's table made me think that the security budget [dollars/sec] is a factor. I'm unsure how to incorporate it though.     

> __< k​ayabanerve:matrix.org >__ I've realized and am willing to concede I don't have a clear view of what powers should be conceded to an adversary and what probability we want to reduce to at this time. I appreciate Rucknium doing the work I asked for on the feasibility of DoSs with limited hash power over time, and look forward to that number in order to influence our decision making process (though off-hand I<clipped message     

> __< k​ayabanerve:matrix.org >__ 'd guess they'll be so unlikely they won't matter). I apologize if my request for those calculations are too burdensome.     

> __< Rucknium >__ IMHO, the problem with saying that the adversary has X budget to spend it any way they want is that it's always better to rent a lot of hashpower for a very short period of time than to rent a little hashpower for a long period of time.     

> __< Rucknium >__ No, it's fine. That's what I'm here for.     

> __< chaserene >__ ok, I *think* I get it. then, as I see it, the adversary hash power share value (the column headers in https://gist.github.com/Rucknium/da1e57b1864aca477dfa3b4e02e86e26) is about what we assume to be the upper bound on what share an adversary can get access to, regardless of their budget.     

> __< chaserene >__ it's more about "how much of the current hash power is controlled by rogue entities who can urn malicious at any time" + "how much potentially rentable/buyable hash power is out there that's currently not used for mining Monero". is that correct?     

> __< chaserene >__ *turn     

> __< r​ucknium:monero.social >__ IMHO, that's a valid interpretation. The probability calculations don't tell you how the adversary acquired the hashpower.     

> __< r​ucknium:monero.social >__ I like this passage from Rosenfeld (2014): "There is nothing special about the default, often-cited figure of 6 confirmations [for bitcoin]. It was chosen based on the assumption that an attacker is unlikely to amass more than 10% of the hashrate, and that a negligible risk of less than 0.1% is acceptable. Both these figures are arbitrary, however; 6 confirmations are overkill for<clipped message     

> __< r​ucknium:monero.social >__  casual attackers, and at the same time powerless against more dedicated attackers with much more than 10% hashrate.     

> __< c​haser:monero.social >__ yeah. Satoshi was really good at coming up with arbitrary values that stick with people.     

> __< c​haser:monero.social >__ do I sense it correctly though that that's not the interpretation underlying your table?     

> __< r​ucknium:monero.social >__ daybreak: Big changes to the decoy selection algorithm at a time that is not a hard fork means that some users will be using the old version and some would be using the new version. The new Chainalysis video confirms that adversaries are using these types of transaction uniformity defects to reduce user privacy. See my discussion note here for some risk tables: https://github.com/<clipped message     

> __< r​ucknium:monero.social >__ Rucknium/misc-research/blob/main/Monero-Fungibility-Defect-Classifier/pdf/classify-real-spend-with-fungibility-defects.pdf     

> __< r​ucknium:monero.social >__ If there are no major problems with FCMP (which it looks that way right now), then an OSPEAD-derived decoy distribution would likely be used for wallet-daemon RPC calls as a backup to the in-wallet merkle tree cache as discussed in today's MRL meeting. If for some reason major problems with FCMP are discovered, then a hard fork to increase ring size with current RingCT tech could <clipped message     

> __< r​ucknium:monero.social >__ occur. An OSPEAD-derived distribution would likely be implemented at that hard fork.     

> __< r​ucknium:monero.social >__ chaser: The table is agnostic about that. These calculations start to get anchored when merchant and services use them. For example, I as a merchant weight how much my goods/services cost me, how much an adversary woud have to spend, etc. The calculations are made more complicated by the fact that an adversary can double-spend against more than one target. IIRC one paper suggested<clipped message     

> __< r​ucknium:monero.social >__  that merchants look at the total value being exchanged on the honest, visible blockchain to determine total risk (i.e. as if all txs were going to be double-spent). Of course, you cannot do that with Monero since amounts are confidential.     

> __< r​ucknium:monero.social >__ But most merchants and services won't and don't make such complicated calculations. They just set a single confirmation number for everything, maybe arbitrarily chosen, and let it be.     

> __< r​ucknium:monero.social >__ AFAIK, today the biggest value that is being exchanged is just other cryptocurrencies against each other, not real goods and services. Peer-to-peer electronic cash....?     

> __< e​ndor00:matrix.org >__ Perhaps looking at this script might help? https://gist.github.com/endorxmr/07364dc54f277abf487574d455d67341     

> __< e​ndor00:matrix.org >__ The security budget is the amount of money "generated" by the network over time. If we assume miners are rational (i.e. they never mine at a loss, i.e. they pay for electricity no more than they earn from mining), then that is also the maximum amount of money spent on electricity     

> __< c​haser:monero.social >__ Rucknium I see. the shitcoin casino averted the double-spend threat :)     

> __< r​ucknium:monero.social >__ chaser: I think it enabled the double-spend threat, just not with real goods/services, but with cryptocurrency exchanges. AFAIK most of the incidents in endor00 's table involved transferring other cryptocurrency coins out of the exchange as part of the double spends.     

> __< e​ndor00:matrix.org >__ By playing around with the security budget, the electricity cost, and the efficiency of the mining devices, we can calculate an approximate size of the mining network (number of devices of a given model, total power consumption, profitability, ROI time, etc.) - which allows us to estimate on how much it would cost to acquire a given amount of hashrate (and thus, own a given % of the nethash)     

> __< c​haser:monero.social >__ Rucknium yes, that's correct. however, I'm almost sure that the trading on on-chain DEXes (think Ethereum, Solana) outweighs CEX deposit/withdrawal volumes.     

> __< c​haser:monero.social >__ to be honest (this is an answer to endor00 too), I may have misunderstood this discussion. my unconscious assumption was that the threat model includes adversaries with extra-protocol incentives, who mine alternative chains even if only for disrupting Monero (for which, admittedly, "double spend risk" is not the right term). a budget-based analysis makes a lot more sense there.     

> __< r​ucknium:monero.social >__ It's potentially both types of adversary motivations IMHO. A targeted double-spend beyond the N block lock would cause collateral damage to other users who have their txs invalidated under FCMP. And for an adversary that just wants to cause disruption, the collateral damage _is_ the motivation.     

> __< e​ndor00:matrix.org >__ Any incentive is a good incentive - the problem is quantifying it.     

> __< e​ndor00:matrix.org >__ With a simple double-spend attack, it should be fairly straightforward (some % probability of success within a fixed timeframe, vs. a given "reward").     

> __< e​ndor00:matrix.org >__ If the goal is pure disruption, you can frame it in terms of cost vs. effect (spend X $ to cause some amount of reorgs with some % success, and disrupt some number of txes worth some $ amount).     

> __< e​ndor00:matrix.org >__ With other types of attacks, it's a bit more complicated, and requires some/a lot of assumptions about the attacker's costs and access to resources, or a more detailed model of what they're doing exactly     

> __< c​haser:monero.social >__ yes, if we want to account for adversaries with extra-protocol incentives, cost and resource access are key.     

> __< c​haser:monero.social >__ we could/should assume the attacker's priority will be to control as much hash power simultaneously as possible. these's a lot of compute in existence that's currently not mining Monero, could profitably mine it, and is accessible, so the share will be (100-ε)%.     

> __< c​haser:monero.social >__ then, even if we pick a double spend attack success probability that we're comfortable with, for a good answer, we need to:     

> __< c​haser:monero.social >__ 1) define a curve that estimates how much non-Monero-mining hash power can be simultaneously acquired at what cost, and     

> __< c​haser:monero.social >__ 2) pick a budget for the adversary.     

> __< c​haser:monero.social >__ (s/profitably/practically, we're beyond profitability here)   

# Action History
- Created by: Rucknium | 2024-09-18T16:56:31+00:00
- Closed at: 2024-10-01T21:06:54+00:00
