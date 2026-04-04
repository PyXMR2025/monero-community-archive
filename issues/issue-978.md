---
title: Monero Research Lab Meeting - Wed 13 March 2024, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/978
author: Rucknium
assignees: []
labels: []
created_at: '2024-03-13T14:19:06+00:00'
updated_at: '2024-03-19T20:53:32+00:00'
type: issue
status: closed
closed_at: '2024-03-19T20:53:32+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

[Join the Monero Matrix server if you don't already have a Matrix account.](https://web.archive.org/web/20230128130949/https://forum.monero.space/d/79-how-to-join-the-monero-core-team-matrix-server-web)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/converter.html?iso=20211027T170000&p1=1440)

Main discussion topics:

1. Greetings

2. Updates. What is everyone working on?

3. [Possible spam incident](https://bitinfocharts.com/comparison/monero-transactions.html#3m)

4. @jeffro256 [ I think we can improve how the nodes handle alternative blocks in a way that might naturally reduce the number of reorgs on the network.](https://github.com/monero-project/meta/issues/966#issuecomment-1936243293)

5. Any other business

6. Confirm next meeting agenda


Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: Rucknium

Previous meeting agenda/logs:

#976 

# Discussion History
## Rucknium | 2024-03-14T12:45:12+00:00
> __< r​ucknium:monero.social >__ There was unusual fee behavior yesterday and today. There are four standard fee tiers: 20, 80, 320, and 4000 nanoneros per byte. On March 11, the share of "non-spam" txs paying 320 nanoneros/byte was 4.5%. It had been steady for a few days until then, too. Then on March 12 and today the share of those 320 fee txs increased to about 35%.     

> __< r​ucknium:monero.social >__ In the block tabulation, it looks like this set of 320 fee txs started at block 3103476 (2024-03-12 14:04:08 UTC) and ended after block 3104042 (2024-03-13 08:42:57 UTC). These 320 fee txs are almost all 1in/2out.     

> __< r​ucknium:monero.social >__ It could be a big centralized service turning on and off its fee priority. Or the suspected spammer could be changing its behavior.     

> __< r​ucknium:monero.social >__ The auto fee fix to the GUI/CLI wallet only increases fee from 20 to 80 nanoneros per byte when the mempool is congested.     

> __< r​ucknium:monero.social >__ Fee tabulation by block: https://paste.debian.net/hidden/fb7ec136/     

> __< r​ucknium:monero.social >__ Ah, wait that tabulation was just for today. Here is yesterday and today: https://paste.debian.net/hidden/8d45e207/     

> __< r​ucknium:monero.social >__ MRL meeting in this channel in about two hours     

> __< r​ucknium:monero.social >__ By the way, the numbers for the lowest fee tier (80) don't add match the blockchain data since I remove a portion of the low-fee 1in/2out txs as "spam".     

> __< r​ucknium:monero.social >__ I mean lowest fee tier (20)     

> __< r​ucknium:monero.social >__ Meeting time! https://github.com/monero-project/meta/issues/978     

> __< r​ucknium:monero.social >__ 1) Greetings     

> __< rbrunner >__ Hello     

> __< vtnerd >__ hi     

> __< d​angerousfreedom:matrix.org >__ Hi     

> __< 0​xfffc:matrix.org >__ Hi everyone     

> __< c​haserene:matrix.org >__ hi     

> __< r​ucknium:monero.social >__ 2) Updates. What is everyone working on?     

> __< r​ucknium:monero.social >__ me: Analyzing the blockchain and mempool data from the last week and a half of the suspected spam incident.     

> __< vtnerd >__ I was working on finding a segfault lws (still not found), unit testing the lws rest api, and a little bit on figuring out how to enable multi-machine scanning in lws     

> __< vtnerd >__ I may punt on the last one, as its looking pretty complicated     

> __< vtnerd >__ until someone explictly needs it (its probably unlikely)     

> __< rbrunner >__ Like some sort of load balancing?     

> __< 0​xfffc:matrix.org >__ Me: I updated RW lock (9181) last week, the lock is final at this point. Worked here and there on few GitHub issues. But main thing I am working on is performance benchmarks suite for XMR. I finished a prototype yesterday. ( https://github.com/0xFFFC0000/monero-perf/tree/main/private-testnet ). The prototype does have 3 wallet limitation. Now I am implementing it in C++ ( https://<clipped message>     

> __< 0​xfffc:matrix.org >__ github.com/0xFFFC0000/benchmark-project ). Numbers from these performance benchmarks can help us a lot in evaluating different PRs (including the 9181).     

> __< vtnerd >__ rbrunner: yes, send account scanning over socket to other machines for scanning     

> __< r​ucknium:monero.social >__ 3) Discussion. We have the possible spam incident: https://bitinfocharts.com/comparison/monero-transactions.html#3m     

> __< r​ucknium:monero.social >__ I've been estimating the mean/median/percentile effective ring size of this is actually the prophesied black marble flooding.     

> __< r​ucknium:monero.social >__ The mean has been about 5.5 for the last few days. If the "spam" volume stays the same, it will decrease slowly now as more of the probability mass of the decoy selection algorithm moves into the spam time interval.     

> __< r​ucknium:monero.social >__ isthmus might try to re-run the scripts that we wrote to analyze the 2021 spam incident. The database workflow that we were using us broken, so it has to be repaired or a new workflow written. The 2021 analysis was mostly to provide evidence for or against the txs being produced by a single entity.     

> __< r​ucknium:monero.social >__ Is there a critical threshold for effective ring size that should not be crossed, assuming this is a black marble flood? What do we think?     

> __< rbrunner >__ Hard to say. Rings are only 1 of 3 privacy mechanisms, amounts stay invisible, stealth addresses hold, even if the effective rings size continues to go lower.     

> __< rbrunner >__ We lived for quite some time with a ringsize of 5, I think. Because that just was the ringsize back then, period.     

> __< c​haserene:matrix.org >__ I think we're already in the red zone. but going below 3 (historical ring size) would be critically bad     

> __< r​ucknium:monero.social >__ If the spam stays at its current level indefinitely (about 400kB blocks), the median effective ring size will decrease to 3 eventually. That may be low enough to allow chain reaction analysis. And we shouldn't forget about the extremes. 3 or 5.5 may be average, but some rings will pick up more spam tx outputs by chance.     

> __< rbrunner >__ Well, I think we are mostly aware that if we are not careful any "cure" we come up might turn out to be worse than the "disease"     

> __< r​ucknium:monero.social >__ Some of the countermeasure that I have seen: 1) Raise fees, 2) Raise ring size, 3) Change dynamic block size algorithm, 4) See if miners will voluntarily limit block size, 5) Launch decentralized counterspam to reduce the share of outputs owned by the spammer. 1-3 would require a hard fork AFAIK.     

> __< rbrunner >__ Blocksize growth seems pretty limited so far. You could speak of a "spam wave", but not, or not yet anyway, a "flood"     

> __< r​ucknium:monero.social >__ Do we want to try to figure out if a single node (or a small number) is broadcasting the txs?     

> __< c​haserene:matrix.org >__ I don't think that would be conclusive, the spammer could use many nodes     

> __< r​ucknium:monero.social >__ The suspected spammer is letting the block size algorithm's 100 block median fall down. Not sure if it's deliberate or accidental. That's limiting the block growth rate.     

> __< rbrunner >__ Yeah, so far it has been a pretty nice spammer ...     

> __< r​ucknium:monero.social >__ Do you think it would be conclusive if one node were found? You could confirm the hypothesis, but lack of evidence for a single node origin would not confirm that it is not spam.     

> __< c​haserene:matrix.org >__ that will work against them once eniugh nodes update to the fee patch, but I don't know if we see that yet in fee usage     

> __< r​ucknium:monero.social >__ Work against them? The auto fee adjustment is wallet-level, not node-level AFAIK. Users have to update.     

> __< rbrunner >__ Yes, the wallet decides the fee factor to apply     

> __< c​haserene:matrix.org >__ yes, I would conseder that conclusive. so it may be worthy to investigate     

> __< d​angerousfreedom:matrix.org >__ How do we know that the 20k average txs/day that we had previously were not poisoned by 10k or 15k txs from a spammer?     

> __< rbrunner >__ How would we go on to defeat Dandelion++? Some sort of coordinated listening?     

> __< r​ucknium:monero.social >__ dangerousfreedom: We do not know that. A slow rise in spam has been theorized before.     

> __< c​haserene:matrix.org >__ you're right, that's the wallet. if.tney keep stepping back, the block size can't grow and *if* they keep their tx's on the cheap fee level, more honest tx's will be included     

> __< r​ucknium:monero.social >__ Basically D++ is a statistical obfuscation technique. If the signal is huge, like with spam, then it can be heard above the noise.     

> __< r​ucknium:monero.social >__ The spammer can keep pushing up block size even if all users update to the auto fee fix.     

> __< rbrunner >__ But that would probably need some daemon instrumentation, to get some statistics, I guess. Or some third program that speaks the protocol.     

> __< r​ucknium:monero.social >__ Sharma, P. K., Gosain, D., & Diaz, C. 2022. "On the anonymity of peer-to-peer network anonymity schemes used by cryptocurrencies."  https://moneroresearch.info/index.php?action=resource_RESOURCEVIEW_CORE&id=130     

> __< r​ucknium:monero.social >__ ^ This paper analyzed D++'s resistance to a specific form of statistical analysis. I thought this paper was unrealistic since they needed huge tx volumes to determine the node origin of txs. But now we have a huge tx volume, so it could work. I tried the paper's python code a while ago and it seemed to work ok.     

> __< r​ucknium:monero.social >__ Yes the main data you need is tx arrival times at many nodes in the network. Not quick or easy to set up. You would have to get volunteer nodes or nodes that try to place themselves strategically in the network.     

> __< c​haserene:matrix.org >__ they can, but at at a slower rate compared to a scenario where they increase their fees too, no? there's a chance the increased budget requirement could keep them back     

> __< rbrunner >__ Basically a lot of the analysis here just shows how good Monero is at privacy :)     

> __< j​effro256:monero.social >__ One problem I have with D++ right mow is that node connections are unencrypted which means that ISPs have an advantage in being able to tell where transactions originated from if they decided to collude     

> __< r​ucknium:monero.social >__ Did you see my comments before the meeting? Recently there was a big increase in high fee txs. Then that stopped.     

> __< j​effro256:monero.social >__ Dummy stems don't mean much against DPI     

> __< r​ucknium:monero.social >__ Yes, IRC the D++ paper says that it doesn't protect against ISP surveillance.     

> __< r​ucknium:monero.social >__ IIRC*     

> __< rbrunner >__ If we go up with the ringsize and stay in "reasonable" territory, say 20, will that help? And if yes how much? Just needs a bit more spam to overcome?     

> __< selsta >__ it's possible that the spammer is using Tor/I2P     

> __< r​ucknium:monero.social >__ rbrunner: I can run some scenarios     

> __< c​haserene:matrix.org >__ I didn't, will read the backlog. that's not good     

> __< rbrunner >__ That would be splendid, rucknium     

> __< rbrunner >__ "Not good" as in "making matters worse"?     

> __< j​oiboi.crypto:matrix.org >__ #FreeOfrnxmr     

> __< r​ucknium:monero.social >__ Basically, when spam txs increase, effective ring size decays exponentially. So the largest drop happens when the spam volume is "small".     

> __< r​ucknium:monero.social >__ I have a few plots I can post soon     

> __< c​haserene:matrix.org >__ rbrunner: I think so, yes     

> __< r​ucknium:monero.social >__ If the spammer is willing to make high fee (320 nanoneros/byte) txs, then they have a large budget.     

> __< rbrunner >__ Maybe a dumb idea, but we could make the ringsize user-selectable again, with a minimum of 16. So people basically could choose their level of privacy ... or so, maybe that fails somewhere     

> __< r​ucknium:monero.social >__ I will do rbrunner's suggested analysis of simulating ring size increases. Other suggestions for analysis I could do?     

> __< c​haserene:matrix.org >__ re: changing minimum fee or dynamic block size algo, I would appreaciate input from ArticMine:     

> __< j​effro256:monero.social >__ Selectable ring sizes leads to fingerprinting     

> __< rbrunner >__ Yup. It would be a question of the "lesser evil".     

> __< rbrunner >__ And it seems there are no really easy options on the table, sadly     

> __< j​effro256:monero.social >__ Yeah. If we allow different ring sizes we should probably change the tx weight mechanism since a 2x increase in CLSAG verification time wouldn't lead to a 2x increase in weight     

> __< m​onerobull:matrix.org >__ Custom ringsize is dumb     

> __< m​onerobull:matrix.org >__ Isn't that partially at fault for wanacry payments getting traced or was that something else?     

> __< c​haserene:matrix.org >__ doing this would be a tradeoff. I'm more against than for (horrible optics and UX), but if for, you could prescribe a few ring sizes, not the way it worked in the old days where any amount could go.     

> __< m​onerobull:matrix.org >__ It's silly, if the attacker owns 90% of decoys they still do that whether you have 15 or 500 decoys but with the later it's way more fingerprintable     

> __< rbrunner >__ Ok :)     

> __< m​onerobull:matrix.org >__ All of this is solved with fcmps     

> __< m​onerobull:matrix.org >__ 2 million decoys let's go     

> __< rbrunner >__ rucknium: Maybe try to find out what the effects of "counterspam" would be? How much does the community have to spam to keep "effective ringsize up"?     

> __< r​ucknium:monero.social >__ I can do that     

> __< rbrunner >__ Counterspam is of course also bad, but well ...     

> __< c​haserene:matrix.org >__ sounds impossible, but could a FCMP upgrade be feasibly done separately from Seraphis?     

> __< s​emisimple:monero.social >__ Actually, why not try to counterspam and see if that causes a reaction of the "real" spammer     

> __< c​haserene:matrix.org >__ because that would be a trump card     

> __< rbrunner >__ Even if possible, that would probably take a year to go into effect. If we don't rush with inacceptable risks     

> __< j​effro256:monero.social >__ Technically yes, but then you would basically have to remake seraphis lol     

> __< m​onerobull:matrix.org >__ Biggest issue with counter spam is not knowing when to stop if there are multiple counter spammers     

> __< rbrunner >__ We have to consider that the *whole* reason for the exercise may be to drive us to do something unwise.     

> __< m​onerobull:matrix.org >__ At this point it's most likely about chainalysis raising money     

> __< r​ucknium:monero.social >__ IMHO, probably the best short term countermeasure, if it is really a black marble flood, is to see if miners would set a limit on the block size that they will not go above. Only a majority of hashpower would be enough to reduce the 100 block median     

> __< rbrunner >__ That's also my "pet theory", as recently explained on Reddit     

> __< r​ucknium:monero.social >__ https://matrix.monero.social/_matrix/media/v1/download/monero.social/bGgVqJzYAtzSQXUdTKOcWunA     

> __< m​onerobull:matrix.org >__ The worst part is, when chainalysis inevitably releases their "tracing monero" report the fud will be immense even though monero still protects amounts and receiver     

> __< m​onerobull:matrix.org >__ So they can only get down to a 50/50?     

> __< r​ucknium:monero.social >__ ^ That long term projection is if all decoys are selected from the spam time interval. Since some decoys are being selected from before the spam start point, we are not there yet.     

> __< rbrunner >__ Not immediately clear to me why limiting blocksize is beneficial?     

> __< rbrunner >__ Not as a flood protection, but keeping the effective ringsize up     

> __< c​haserene:matrix.org >__ that's somithing to keep in mind, yes     

> __< r​ucknium:monero.social >__ I stopped it at effective ring size 2. I can extend the visualization.     

> __< m​onerobull:matrix.org >__ I don't think it's needed     

> __< r​ucknium:monero.social >__ But that's just average. Some txs would have effective ring size 1 since they would select all spammer-controlled outputs by chance.     

> __< m​onerobull:matrix.org >__ How many TX per day would that even be at effective ringsize 2m     

> __< m​onerobull:matrix.org >__ How many TX per day would that even be at effective ringsize 2?     

> __< r​ucknium:monero.social >__ rbrunner: Since limiting block size limits the amount of spam that can be packed in. And keeps the number of real txs constant. I guess that last  part assumes that users update to the auto fee fix.     

> __< r​ucknium:monero.social >__ monerobull: Looks like about 200,000 tx/day would be needed for that.     

> __< rbrunner >__ Yes, and that the spammer does not go higher with fees themselves?     

> __< m​onerobull:matrix.org >__ 👍     

> __< r​ucknium:monero.social >__ Yes, also assuming that.     

> __< rbrunner >__ All a bit unfortunate     

> __< selsta >__ a company like Chainanalysis would try to keep things under the radar. they wouldn't start spamming 7x the tx amount from one day to another, creating a 20mb txpool, harming UX and making everyone aware that something is going on     

> __< rbrunner >__ Well, who would then?     

> __< rbrunner >__ It's not that all their employees are competent for sure. Who knows who got the job :)     

> __< m​onerobull:matrix.org >__ Selsta: they might have not expected the auto fee to be broken lol     

> __< hyc >__ yeah - someone incompetent     

> __< rbrunner >__ hey, yes, Chainanalysis alright, but they outsorced the job     

> __< c​haserene:matrix.org >__ if a sensible ring size increase (=doesn't disadvantage many potential users) could get us a significant advantage, that's one intervention that won't have catastrophic downsides and isn't a regression     

> __< m​onerobull:matrix.org >__ How about a temporary rushed implementation of triptych/s     

> __< rbrunner >__ monermooo must still have a branch around somewhere with that     

> __< a​rticmine:monero.social >__ A ring size increase combined with parallel verification can work here     

> __< a​rticmine:monero.social >__ Also we can target the estimated tx size for full membership proofs     

> __< hyc >__ there's already a high degree of parallelism on incoming verify     

> __< rbrunner >__ That's an interesting argument: To "adjust" already today to the FCMP tx size     

> __< a​rticmine:monero.social >__ This would create a seamless transition to full membership proofs from a scaling perspective     

> __< m​onerobull:matrix.org >__ How big of an increase would that be Artic?     

> __< a​rticmine:monero.social >__ We could also consider a 4x increase in the minimum node relay fee     

> __< selsta >__ +1 for higher fees     

> __< j​effro256:monero.social >__ I wouldn't be opposed to a fee increase     

> __< rbrunner >__ Even without any idea how deep "their" pockets are?     

> __< a​rticmine:monero.social >__ How big is the current estimates for a 2 in 2 out full membership proofs Tx in bytes?     

> __< rbrunner >__ That's one of the dangers that I personally see: to rush into some unwise fee increase     

> __< selsta >__ i would be in favor of higher fees even if there isn't an attack, sub one cent is too low     

> __< hyc >__ is it too low? low tx fee was a seling point     

> __< c​haserene:matrix.org >__ I don't think we'll ever know how deep their pockets are until they stop     

> __< a​rticmine:monero.social >__ The consideration is that fees are node relay not consensus     

> __< r​ucknium:monero.social >__ kayabanerve, jberman : Do you have an estimate for 2in/2out FCMP tx size?     

> __< m​onerobull:matrix.org >__ I'd be fine with the current "normal" tier fees of about 1.6 euro cents per standard tx. Going above 5 cents kills the "digital cash" aspect imo     

> __< a​rticmine:monero.social >__ I asked the above question in the last MoneroKon     

> __< m​onerobull:matrix.org >__ My bank charges 10 cents per tx and I absolutely despise them for it     

> __< a​rticmine:monero.social >__ That is my idea     

> __< m​onerobull:matrix.org >__ Besides, it's only cheap in fiat terms at current fiat evaluation     

> __< a​rticmine:monero.social >__ By the way I can now speak freely after the end of the trial     

> __< r​ucknium:monero.social >__ If there were a way to have a purchasing power oracle for a unit of XMR, the exchange rate changes wouldn't be a big problem. Maybe it could be linked to network hashpower since hashpower is linked to XMR purchasing power. That makes assumptions about how RandomX hashpower will change in the future.     

> __< a​rticmine:monero.social >__ There is a justification for a 4x increase in the minimum node relay fee while keeping the current quadratic fee scaling     

> __< a​rticmine:monero.social >__ There is tx per day and block size     

> __< a​rticmine:monero.social >__ In the absence of spam     

> __< c​haserene:matrix.org >__ tying anything to oracles is a huge can of worms and very large attack surface, even just to hash rate     

> __< a​rticmine:monero.social >__ By the way I am not convinced this is a spam attacj     

> __< sech1 >__ Fee level is _okay_, panic raising fees is stupid. When price pumps eventually will we panic drop fees? Hardfork every time?     

> __< a​rticmine:monero.social >__ Attack     

> __< s​emisimple:monero.social >__ Also fee increase does not fix the underlying security problem, assuming there is one. Just makes it more expensive, which would still be ridiculously cheap for large scale actors     

> __< sech1 >__ And to be fair 140k tx/day is nothing. Increasing ring size is most sensible thing to do, if do anything     

> __< a​rticmine:monero.social >__ We need to take a very close look at the impact of the Binance delisting on DEXs, instant exchanges, peer to peer trading and even CEX customer behavior     

> __< c​haserene:matrix.org >__ note that this works only against DoS, not black marbles. I know you don't think at all this is a black marble scenario, and I think you're wrong on that     

> __< r​ucknium:monero.social >__ IIRC this paper says basically you can use congestion pricing to form a fee oracle just from user bids for block space: Huberman, G., Leshno, J. D., & Moallemi, C. (2021). "Monopoly without a Monopolist: An Economic Analysis of the Bitcoin Payment System." https://moneroresearch.info/index.php?action=resource_RESOURCEVIEW_CORE&id=78     

> __< a​rticmine:monero.social >__ It does increase the cost     

> __< r​ucknium:monero.social >__ But that would require accepting a lot of congestion I think.     

> __< a​rticmine:monero.social >__ ... I am suggesting this combine with a ring size increase     

> __< a​rticmine:monero.social >__ So a multi faceted approach     

> __< r​ucknium:monero.social >__ After the Mordinal incident, analysis of P2Pool outputs, and the 2021 spam incident, I have thought for a while that current ring size provides a safety margin that is too low.     

> __< r​ucknium:monero.social >__ We are 25 minutes past the hour. Should we continue to monitor the suspected spam and continue discussing next Wednesday?     

> __< a​rticmine:monero.social >__ I have my doubts. That being said there are solutions that can deter a black marble attack until we move to full membership proofs     

> __< c​haserene:matrix.org >__ thanks. if this paper implies congestion in the sense of tx volume, there are live working examples for that     

> __< a​rticmine:monero.social >__ Yes but Monero has an adaptive block size     

> __< sech1 >__ We can revive Mordinals so people will start spamming their NFT transactions     

> __< sech1 >__ Problem solved      

> __< a​rticmine:monero.social >__ So Bitcoin solutions will not work     

> __< r​ucknium:monero.social >__ Black marble flooding was one of the first theorized attacks against Monero privacy. It was analyzed in the first MRL research bulletin. So...plenty of time to develop a solution. almost 10 years     

> __< j​effro256:monero.social >__ Lol when tx_extra weight clawback?     

> __< r​ucknium:monero.social >__ ArticMine: IIRC the paper suggested modifying bitcoin's block size limit to adjust to congestion. It was supposed to provide a constant miner revenue from txs in purchasing power terms.     

> __< a​rticmine:monero.social >__ The best solution is to increase the ring size. Ideally to infinity with full membership proofs     

> __< sech1 >__ Limit tx extra to 256 bytes so each Mordinal will create a dozen tx     

> __< r​ucknium:monero.social >__ If the ring size were to increase, what would be a reasonable hard fork schedule?     

> __< sech1 >__ Hard fork is +6 months after binary release     

> __< sech1 >__ Not earlier      

> __< a​rticmine:monero.social >__ Which is not relevant to Monero with its adaptive block size and tail emission     

> __< r​ucknium:monero.social >__ This is in the paper: "To summarize, this analysis suggests the following simple adaptations to the current protocol. First, a smaller block size K is preferable. Second, an adjustment of the block rate to μ = λ/(Kρ∗) in response to demand λ. This keeps congestion constant at ρ∗, yielding a stable, desired level of revenue."     

> __< r​ucknium:monero.social >__ Yes, it is probably not feasible because there are a lot of economic assumptions.     

> __< a​rticmine:monero.social >__ The trouble with Bitcoin like coins is the need to replace falling block rewards with Tx fee     

> __< a​rticmine:monero.social >__ This premise has never been shown to work     

> __< a​rticmine:monero.social >__ We only need to be concerned with  pricing out spam while keeping the ham affordable     

> __< c​haserene:matrix.org >__ "~5.5kb" (https://github.com/monero-project/research-lab/issues/100#issuecomment-1609536076)     

> __< j​effro256:monero.social >__ Tangentially related (and not proposing we do anything now): but does anyone feel that the emissions is currently too low compared to other chains which makes XMR comparably less profitable to mine ? IMO security budget could be higher     

> __< a​rticmine:monero.social >__ Once I have an estimate on the full membership proofs Tx size I can get to work on the modifications to the scaling algorithm and fees     

> __< a​rticmine:monero.social >__ So 6000 bytes     

> __< r​ucknium:monero.social >__ IMHO changing anything about the emission would reduce the purchasing power of the block reward more than keeping it the same. It would reduce confidence     

> __< a​rticmine:monero.social >__ I will review the GitHub  link     

> __< c​haserene:matrix.org >__ I have thought about it, but I'm vastly deterred from touching a monetary policy we have good consensus on     

> __< j​effro256:monero.social >__ Yes I'm of the same opinion. Wish it was higher from the get go     

> __< a​rticmine:monero.social >__ This is very workable with the additional flexibility on increasing the minimum node relay fee     

> __< j​effro256:monero.social >__ Doing it now is a bad look     

> __< d​angerousfreedom:matrix.org >__ If we consider the spammer with unlimited resources then increasing the ring size wont stop him, neither limiting the block size nor letting the fees go up (like btc). I also cant see what could be done. Maybe a solution that encopasses all of that (increased ring size, smaller blocks, higher fees). The question would be then, what users want the most? Privacy, low fees, constant <clipped me     

> __< d​angerousfreedom:matrix.org >__ blocksizes... I personally think that Monero has a pretty damn good privacy already. I wouldnt care about smaller blocks and higher fees. I actually think it is a greater selling point to know what will be the maximum blockchain size in 5 years from now then saying that the fees will remain this low (in XMR terms) in five years. I think money should be scarce (not only in the supp<clipped me     

> __< d​angerousfreedom:matrix.org >__ ly but also in the resources required to operate it) as well as acceptable. So it is a personal trade-off. But anyway, at this point, I dont think any changes are necessary, if things get bad in the future, I'm of the opinion that we should reduce the block size so txs with higher fees have higher priorities and the spammer would need to pay more and therefore benefit the miners.     

> __< a​rticmine:monero.social >__ No company has an unlimited budget. Also a flood XMR could likely be illegal and at best a public nightmare     

> __< j​effro256:monero.social >__ Increasing ring size makes it exponentially harder to get a deterministic hit FWIW     

> __< c​haserene:matrix.org >__ an attacker doesn't care about legality, it actually may be approved by a government     

> __< d​angerousfreedom:matrix.org >__ In the current money printing system everything is legal and unlimited     

> __< r​ucknium:monero.social >__ I think we can end the meeting. We'll keep monitoring. Read you next week.     

> __< selsta >__ hopefully next week we will have more information how the spam evolved     

> __< c​haserene:matrix.org >__ this reminds me of Artic bringing up Nielsen's Law (https://en.wikipedia.org/wiki/Jakob_Nielsen_(usability_consultant)#Nielsen's_law) in his recent interview. would it make sense to define constraints in the (dynamic) block size according to it, or something like it? this could be one way to gain predictability without sticking to static parameters.     

> __< a​js_:matrix.org >__ MoneroKon CFP deadline is this Friday… if you would like to do a talk or host a workshop, submit proposal here: https://apply.monerokon.org     

> __< a​rticmine:monero.social >__ My take is a reference tx size of 6000 bytes. This will allow for a 2.5x increase in ring size. When combined with a 4x increase in the minimum node relay fee we are looking at a 10x increase in the cost of a potential spam attack while only having a 4x increase in the cost of ham     

> __< a​rticmine:monero.social >__ We can also implement the ideas of capping the growth to Nielsen's Law l proposed in the last MoneroKon     

> __< a​rticmine:monero.social >__ This can be implemented as an interim solution until full membership proofs are available.     

> __< a​rticmine:monero.social >__ The beauty here is that when full membership proofs are available it will be seamless from a scaling point of vie     

> __< a​rticmine:monero.social >__ View     

> __< c​haserene:matrix.org >__ as an aside, even without FCMP, we're looking at 2500-3000 byte Seraphis transactions (depending on variant), assuming ring size = 128     

> __< a​rticmine:monero.social >__ The use of graphics processors for parallel processing of verification is required here particularly for devices such as the Monero Nodo that has a powerful and idle graphics processor     

> __< a​rticmine:monero.social >__ This can be accommodated with the current reference tx size of 3000 bytes.     

> __< a​rticmine:monero.social >__ So if it is available it is an option     

> __< a​rticmine:monero.social >__ I am proposing doubling the reference tx size to 6000 bytes     

> __< a​rticmine:monero.social >__ So ring 40 under the current proofs, ring 512 under Seraphis without FCMP     

> __< c​haserene:matrix.org >__ if an attacker establishes a communication channel with a miner/miners who use modified node software, can't they lower the cost imposed on them by the minimum relay fee?     

> __< a​rticmine:monero.social >__ Yes     

> __< c​haserene:matrix.org >__ I prefer to treat miners as rationally selfish actors who instasell every spendable reward they earned     

> __< a​rticmine:monero.social >__ This is the danger with going too high on the minimum node relay fee     

> __< selsta >__ without Seraphis we also don't have privacy perserving light wallets for mobile. that means too large ring sizes can make monero unusably slow on mobile phones.     

> __< c​haserene:matrix.org >__ are you suggesting that with a "moderate" minimum relay fee bump, like 4x, it's less likely that such channels are established?     

> __< a​rticmine:monero.social >__ Which is why graphics processor verification is important. Mobile phones have powerful graphics processors     

> __< j​effro256:monero.social >__ IIRC wallets don't download or validate proofs so ring size doesnt affect them     

> __< selsta >__ we also don't have GPU verification code, most of the nodes run on systems that don't have a GPU, writing portable GPU code between different vendors is difficult, so I don't think that is anything we should take into account in the short term     

> __< a​rticmine:monero.social >__ Yes. If it is just over the threshold     

> __< selsta >__ also isn't there a risk of a network split when using GPU verification due to implementation differences between different GPU vendors? that was one of the reasons why we never implemented ASM optimizations on the node side for block verification     

> __< a​rticmine:monero.social >__ The exception is servers. One can write for multi core / thread CPUs at the same time. All consumer and small business devices have GPUs     

> __< a​rticmine:monero.social >__ Also if one sets up a server at home or in a small business it is trivial to add aGPU     

> __< a​rticmine:monero.social >__ There are cross device platforms for coding this     

> __< a​rticmine:monero.social >__ GPU verification is inevitable     

> __< a​rticmine:monero.social >__ Your mobile phone has a very powerful GPU. It just does not have whirling fans     

> __< sech1 >__ GPU verification on the wallet side doesn't cause chain splits     

> __< m​onerobull:matrix.org >__ does this have anything to do with matrix calculations?     

> __< selsta >__ sech1: I think he means on the node side     

> __< m​onerobull:matrix.org >__ (matrix calculations are used for machine learning and will presumably get asics with insane performance gains in the near future)     

> __< a​rticmine:monero.social >__ It is basically massive parallel processing     

> __< sech1 >__ On the node side, CPU can double check all rejected tx, although it still leaves space for false positives     

> __< a​rticmine:monero.social >__ That is what GOU are very good at     

> __< a​rticmine:monero.social >__ GPYs     

> __< a​rticmine:monero.social >__ GPUs     

> __< c​haserene:matrix.org >__ I'm sure we'll continue monitoring it and discuss developments as they happen     

> __< a​rticmine:monero.social >__ Yes we need to monitor the suspected spam. We also should reach out to the community to determine what if any impact has the Binance delisting had on transaction rates on chain via DECs instant exchanges peer to peer trading etc     

> __< c​haserene:matrix.org >__ I agree that's an interesting data point. however, saying that CEX trading transactions (where parties didn't withdraw to a wallet after each trade) are now happening on DEXs and instant exchanges in a meaningful scale sounds unrealistic. the inherent fees and the settlement times are so high in comparison that they price a lot of that action out, and these people weren't interest<clipped message>     

> __< c​haserene:matrix.org >__ ed in self-custody to begin with.     


# Action History
- Created by: Rucknium | 2024-03-13T14:19:06+00:00
- Closed at: 2024-03-19T20:53:32+00:00
