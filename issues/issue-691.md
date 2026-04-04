---
title: Monero Research Lab Meeting - Wed 20 April 2022 @ 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/691
author: Rucknium
assignees: []
labels: []
created_at: '2022-04-19T03:02:05+00:00'
updated_at: '2022-04-26T22:23:23+00:00'
type: issue
status: closed
closed_at: '2022-04-26T22:23:23+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

[Join the Monero Matrix server if you don't already have a Matrix account.](https://forum.monero.space/d/79-how-to-join-the-monero-core-team-matrix-server-web)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/converter.html?iso=20211027T170000&p1=1440)

Main discussion topics:

1. Greetings

2. Fee discretization ( https://github.com/monero-project/research-lab/issues/94#issuecomment-1101555982 ).

3. Revisit @tevador 's idea to record account indices in the tx, to improve robustness of output recovery: https://libera.monerologs.net/monero-research-lab/20211230 . Additional reading: https://gist.github.com/tevador/50160d160d24cfc6c52ae02eb3d17024#gistcomment-4025357

4. Focus on Seraphis address schemes and hopefully reach some kind of decision (or get closer, maybe narrow down the choices to 2 or 3). [Schemes](https://github.com/monero-project/research-lab/issues/92) [@tevador proposal](https://gist.github.com/tevador/50160d160d24cfc6c52ae02eb3d17024)

5. Adaptive CPU regulation for improved mining performance ( maxwellsdemon )

6. Further analysis of July-Aug 2021 tx volume anomaly ( Isthmus / Mitchellpkt - see [these meeting logs](https://github.com/monero-project/meta/issues/621#issuecomment-948953655)) [Previous analysis](https://mitchellpkt.medium.com/fingerprinting-a-flood-forensic-statistical-analysis-of-the-mid-2021-monero-transaction-volume-a19cbf41ce60) with [Reddit discussion](https://www.reddit.com/r/Monero/comments/pvm634/fingerprinting_a_flood_forensic_statistical/)

7. Improvements to the mixin selection algorithm ( [Decoy Selection Algorithm - Areas to Improve](https://github.com/monero-project/research-lab/issues/86), [JBerman's weekly updates](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/249#note_11480), [Binning PoC](https://github.com/monero-project/research-lab/issues/88), [OSPEAD](https://ccs.getmonero.org/proposals/Rucknium-OSPEAD-Fortifying-Monero-Against-Statistical-Attack.html) ) @j-berman @Rucknium

8. Seraphis/Triptych/Lelantus Spark ( [UkoeHB's Seraphis Proof of Concept work](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/256), [Seraphis repo](https://github.com/UkoeHB/Seraphis), [Lelantus Spark](https://eprint.iacr.org/2021/1173) & [Tripych Multisig](https://github.com/cypherstack/triptych-multisig/blob/main/main.pdf) )

9. MRL META: "Cat herding", i.e. prioritization of research areas and features. Active recruitment of technical talent, MRL structure, funding (@Rucknium & others) [Reddit discussion](https://www.reddit.com/r/Monero/comments/pkg3d6/the_monero_project_should_actively_recruit/)

10. Examine sample size and random seed matters in Monero's unit tests. IRC discussion: [monero-dev](https://libera.monerologs.net/monero-dev/20211018#c39593) , [monero-research-lab](https://libera.monerologs.net/monero-research-lab/20211018)

11. Multisig Drijvers attack mitigation [Technical note](https://github.com/UkoeHB/drijvers-multisig-tech-note) , [Haveno bounty](https://github.com/haveno-dex/haveno/issues/103)

12. Any other business

13. Confirm next meeting agenda


Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: UkoeHB

Previous meeting agenda/logs:

#688

# Discussion History
## UkoeHB | 2022-04-25T13:30:16+00:00
```
[04-25-22 16:59:55] <UkoeHB> meeting time https://github.com/monero-project/meta/issues/691
[04-25-22 16:59:55] <UkoeHB> 1. greetings
[04-25-22 16:59:55] <UkoeHB> hello
[04-25-22 17:00:48] <xmr-ack[m]> hi
[04-25-22 17:01:07] <jberman[m]> howdy
[04-25-22 17:01:10] <rbrunner> Hello
[04-25-22 17:02:27] <Rucknium[m]> Hi
[04-25-22 17:02:29] <mj-xmr[m]> o/
[04-25-22 17:02:43] <cryptogrampy[m]> hi
[04-25-22 17:03:11] <UkoeHB> 2. updates, what is everyone working on?
[04-25-22 17:04:44] <mj-xmr[m]> As per @Rucknium's request, together with @jberman I'm documenting the Decoy Algorithm, and the Gamma Picker. My approach is to create isolated unit tests, where each one of them goes a step further in the decision tree, testing corner cases, as well as going through the "happy" (typical) path. Each such test... (full message at https://libera.ems.host/_matrix/media/r0/download/libera.chat/4c43742938f528ae8feb99fcb2baa41fd560b3ee)
[04-25-22 17:04:51] <mj-xmr[m]> `/wall o'text`
[04-25-22 17:05:32] <UkoeHB> me: Continuous development on Seraphis. Today or tomorrow I should have unit tests for binned reference sets (bins are deterministic, bin locations are manually defined). I think overall it is better to let the bin location selection be wallet-defined, both due to complexity and for flexibility/continuous improvement outside of the hardfork schedule.
[04-25-22 17:06:13] <Rucknium[m]> Gathering info about fee discretization. Set up reeemuru 's `analitiko` Shiny app on a VPS at https://analitiko.app/ . OSPEAD tasks.
[04-25-22 17:08:19] <UkoeHB> Btw the view tag PR was merged, hurray :)! I will be rebasing multisig pr 8149 today.
[04-25-22 17:09:24] <UkoeHB> 3. ok, let's talk about discretizing fees
[04-25-22 17:09:35] <jberman[m]> update from me: mainly PR review/updating my own PR's. I also dug into Dandelion++ tx broadcast a bit and found that there was not a leak where I suspected there might be one on tx re-submission to a node, so that was good
[04-25-22 17:13:07] <UkoeHB> The basic idea with discretizing fees is to enforce a limited number of fee values at consensus. The advantage would be mitigating fee-based analysis of txs (wallet implementation fingerprinting, user behavior analysis, tx construction timing which is very impactful for multisig), and also saving a few bytes on tx size by using a compact representation. There are a few ideas to implement it: 1) mandate 1 significant 
[04-25-22 17:13:08] <UkoeHB> figure in the fee value, 2) use powers of some multiplier (e.g. 1.2, 1.5, 2), 3) use powers of some multiplier rounded to 1 significant figure.
[04-25-22 17:13:43] <Rucknium[m]> My current view on discretizing fees: As has been discussed, high-precision fees can present a privacy risk due to fingerprinting. There are two issues I can think of right now that may be a drawback of discretizing fees:
[04-25-22 17:15:29] <Rucknium[m]> 1) Around discrete jumps that are high in percent terms, a poorly-constructed fee estimator may interpret the move from a 1 unit to 2 unit fee (i.e. a doubling of fees) as a signal to aggressively outbid competitors. Then there is a snowballing effect and a fee bubble, which would be irritating to users.
[04-25-22 17:17:39] <Rucknium[m]> 2) Discretizing fees may complicate other attempts to increase transaction uniformity by implementing some fee-smoothing ideas from, for example Ethereum's EIP-1559 fee mechnism
[04-25-22 17:18:06] <UkoeHB> can you summarize fee smoothing?
[04-25-22 17:18:27] <Rucknium[m]> But I think that the privacy benefits overrule both those issues, so I think we should move ahead with discretizing fees
[04-25-22 17:18:36] <kayabanerve[m]> Not to mention if you can artificially trigger raised fees and wait to see how long TXs take to use higher fees, right? Less accuracy increasing the severity of bad implementations which therefore makes them easier to detect?
[04-25-22 17:20:32] <kayabanerve[m]> Not really/not to a increased degree notable enough?
[04-25-22 17:21:05] <Rucknium[m]> I am not an expert in EIP-1559, but from my understanding, the fee mechanism makes ETH gas fees more predictable. That reduces distinct fee levels. We also have to think about not just the fees themselves but also think about what fee estimation algorithm produced the fee -- if the fee estimation method can be reverse-engineered based on blockchain data or the mempool status, then that can create the anonymity "puddles".
[04-25-22 17:22:00] <Rucknium[m]> So if there is less of a need to estimate fees -- i.e. the consensus rules gives an optimal fee -- then there is less scope for fingerprintability of fee estimation algorithms.
[04-25-22 17:22:39] <UkoeHB> Even with discretized fees, some analysis will be possible. Hopefully rather than puddles, we will have more of a venn diagram where it isn't clear which puddle you're looking at.
[04-25-22 17:23:06] <rbrunner> I am a bit confused about talking about "estimates". Was always thinking that Monero fees are simply calculated?
[04-25-22 17:23:38] <rbrunner> Whether with high precision or maybe in more discrete steps in the future, but product of a formula?
[04-25-22 17:23:40] <UkoeHB> fee estimator = estimating what fee you need to get your tx into the chain within '2mins, 10mins, 1hr, etc'
[04-25-22 17:24:36] <rbrunner> So this still quite theoretical for Monero, at least at the moment?
[04-25-22 17:24:46] <UkoeHB> kayabanerve[m]: I think it would depend on the implementation... hard to know in advance
[04-25-22 17:24:53] <UkoeHB> rbrunner: right
[04-25-22 17:25:38] <gingeropolous> but the fee is based on the size (weight) of the tx. so does the fingerprintability concern center on when a tx was made? 
[04-25-22 17:25:48] <kayabanerve[m]> We could theoretically provide a fee estimator in wallet2 and reduce differences that way
[04-25-22 17:26:04] <UkoeHB> gingeropolous: that's only for the minimum fee, you can pick any fee value above that (and people do)
[04-25-22 17:26:53] <gingeropolous> roight roight
[04-25-22 17:27:01] <Rucknium[m]> rbrunner: In my mind this is the tricky part: You can have a free-for-all, as we have now. Transactions are included in a transaction basically as a first-price auction (assuming miners are rational). People can bid anything, which leads to privacy problems. Or we could bake a specific fee formula into consensus, but that leads to side deals between miners and users, which is harmful to privacy, as ArticMine alluded to a week or
[04-25-22 17:27:01] <Rucknium[m]> two ago.
[04-25-22 17:27:22] <UkoeHB> kayabanerve[m]: yeah wallet2 already has a fee estimator, so most txs already fall into one big pool
[04-25-22 17:28:02] <kayabanerve[m]> UkoeHB: ^ . The puddle attack would be something like the fee is 1, as it should be, and someone sends a few at 2. Half the wallets start using 3 saying it increased by 100%! We're at load! Use an even higher fee! Then the other half of sane wallets say 1 is fine, this is momentary. For the next few minutes you can fingerprint into puddles.
[04-25-22 17:28:03] <UkoeHB> the fee estimator just chooses your tx priority, that's all (a more advanced estimator could bid arbitrary amounts)
[04-25-22 17:28:22] <Rucknium[m]> Maintaining the first-price auction implicitly assumes that at some point Monero will have a fee market, either intermittently or permanently. If we didn't think Monero would ever have a fee market, then we would be better off baking a fee formula into consensus.
[04-25-22 17:28:23] <kayabanerve[m]> UkoeHB: Great to hear
[04-25-22 17:29:51] <rbrunner> So the basic idea with discretization is to leave freedom to choose fees to people, just not down to an arbitrary precision?
[04-25-22 17:29:59] <Rucknium[m]> Note that sech1 said earlier, "No, wallet bumps the fee automatically when mempool is full"
[04-25-22 17:30:35] <rbrunner> Yeah, I think the wallet uses the next-higher standard multiplier then
[04-25-22 17:30:37] <UkoeHB> kayabanerve[m]: I see, yeah it would be one vector for puddling. In practice, any implementation that isn't a copy paste of wallet2 right now, is going to be fingerprintable since the granularity is so high. With lower granularity, there would be a lot more overlap between different estimators.
[04-25-22 17:31:23] <kayabanerve[m]> UkoeHB: Considering wallet2 has one, I'd even be willing to discuss ruckniums original comment at this time
[04-25-22 17:32:01] <kayabanerve[m]> Not that it wasn't valuable or a fair theoretical point. Solely that most wallets will be successfully covered without issue and edge cases already are edges like you say.
[04-25-22 17:32:05] <UkoeHB> about snowballing?
[04-25-22 17:32:45] <kayabanerve[m]> Snowballing and the privacy implications further discussed
[04-25-22 17:33:05] <UkoeHB> Are you suggesting there would be _worse_ privacy with discretized fees?
[04-25-22 17:33:13] <kayabanerve[m]> I'm not saying we don't we have to review the code before deployment. I'm saying if we get that impl right... The ecosystem should be fine 
[04-25-22 17:33:57] <kayabanerve[m]> UkoeHB: With puddling attacks which isn't applicable when an identical algorithm is applied, so no, I'm dropping that suggestion, but yes, I did suggest it had drawbacks originally 
[04-25-22 17:34:23] <UkoeHB> What exactly are you suggesting?
[04-25-22 17:34:56] <Rucknium[m]> I think to avoid the fee "snowballing" or "bubble", it may be sufficiently to have a decent fee estimator in `wallet2`. The snowballing or bubble would probably only occur if the vast majority of wallets are misinterpreting the fee rise. If only a few fringe wallet implementations misinterpret it, then we would not have the cascading effect, probably.
[04-25-22 17:35:40] <kayabanerve[m]> I was pointing out non uniform, low quality algorithms, could be identified with on purposely triggered algorithms since increments would be more notable since they're no longer granular
[04-25-22 17:35:54] <kayabanerve[m]> Rucknium[m]: This is what I'm currently stating my belief is
[04-25-22 17:36:12] <kayabanerve[m]> *on purposely triggered snowballs
[04-25-22 17:36:20] <Rucknium[m]> By the way, if anyone is interested in an extensive and rigorous analysis of Ethereum's EIP-1559, see: https://arxiv.org/abs/2012.00854
[04-25-22 17:36:34] <UkoeHB> Rucknium[m]: there is also a recursive prisoner's dilemma with fee estimators. If fee estimators consistently overestimate fees, then users will just select lower fees manually (or switch to a wallet that performs better).
[04-25-22 17:37:05] <mj-xmr[m]> kayabanerve[m]: This can be "regularized"
[04-25-22 17:38:12] <mj-xmr[m]> I mean, the fee estimator can have a logarithmic-like ceiling protection.
[04-25-22 17:38:41] <Rucknium[m]> UkoeHB: In theory, yes. With bounded rationality and satisficing behavior, users may tolerate poor fee estimation algorithms. `bitcoind` apparently has an algorithm that systematically overestimates necessary fees, and a huge number of people still use it.
[04-25-22 17:39:01] <kayabanerve[m]> Yep. So as long we get a good algorithm into wallet2 which the ecosystem then naturally adopts... All good :)
[04-25-22 17:39:12] <UkoeHB> kayabanerve[m]: I'm not sure that discretized fees would have a bigger problem from triggered algorithm increments than non-discretized fees. Your trigger-er just needs to know what conditions are required to get a statistically significant response from the algorithm under scrutiny.
[04-25-22 17:41:26] <kayabanerve[m]> UkoeHB: Yeah, potentially not. I think my interest was in the fact that as a small integer it'll be rounded and because of the significant change at each step, normal network latency effects on fees which may cause a few % of variation, offering natural deviation, may be dropped. Because there's no longer a perpetual cycle of such sightly different tx fees... It cleans up the data a bit
[04-25-22 17:42:09] <kayabanerve[m]> That was my theoretical thought process I 100% haven't implemented nor extensively reviewed current fee policies before wanting to bring up current discussion. I do know there's already a mask on fees which handles this to some degree
[04-25-22 17:45:23] <UkoeHB> In conclusion... anyone who think 'please dont do this' or 'eh dont bother'?
[04-25-22 17:45:39] <rbrunner> Seems to me that progressing in steps could be a good idea. Start small, e.g. with making tx construction time estimates much harder by discretization
[04-25-22 17:45:54] <rbrunner> and leave the complicated fee estimator wars and snowballs for later
[04-25-22 17:46:19] <UkoeHB> rbrunner: the fee pr rounds fees to 2 sig figs in wallet2 https://github.com/monero-project/monero/pull/7819
[04-25-22 17:46:57] <UkoeHB> rbrunner: also, I am mostly looking at discretizing fees for seraphis (although we could expedite it to an earlier fork too)
[04-25-22 17:47:25] <rbrunner> Hmmm .. somehow missed that.
[04-25-22 17:47:25] <Rucknium[m]> I said this before the meeting, but I'll put it on the record here in the meeting log: I'm willing and able to research a fee estimation algorithm that handles discrete fees, minimizes privacy risks, and reduces the likelihood of a fee bubble. Not now, but down the road as we get closer to Seraphis implementation on mainnet.
[04-25-22 17:47:38] <merope> I think that the dynamic blocksize might also soften the blow in regards to any positive feedback loops in the fee levels
[04-25-22 17:48:39] <merope> Since the blocksize is not fixed, keeping a steady fee pressure would push the blocksize up, which in turn would reduce the fee pressure for new transactions and increase the total cost of keeping the pressure up
[04-25-22 17:49:09] <UkoeHB> Rucknium[m]: I think that would a really valuable long-term project, so I am looking forward to it :)
[04-25-22 17:49:24] <Rucknium[m]> I think the dynamic bloc size is good for long-term fee stability, but it would still be subject to temporary short-term spikes in tx demand and feees
[04-25-22 17:49:45] <jberman[m]> <kayabanerve[m]> "Yeah, potentially not. I think..." <- If one wallet is using a different algorithm than another or you're trying to pinpoint a tx to a particular point in time, more granular fees imo are definitely more likely to leak this and therefore the puddles form easier when that is the case. I can't imagine a circumstance where this wouldn't hold
[04-25-22 17:50:00] <gingeropolous> ^
[04-25-22 17:52:53] <UkoeHB> Anyone have opinions on what a good scaling factor would be? I really like powers of 1.5 rounded to 1 sig fig (conveniently, this distribution includes every power of 10 from 1 to 1e19).
[04-25-22 17:53:35] <Rucknium[m]> UkoeHB: If you implement this is the code now, and then somehow we figure out that it's a really bad idea before it hits mainnet, how difficult would it be to reverse it in the code implementation?
[04-25-22 17:54:32] <UkoeHB> Rucknium[m]: probably not that hard
[04-25-22 17:55:16] <merope> I think the scaling factor should be evaluated against the pressure it puts towards pushing the blocksize up. ie.: "If we bump to the next fee level, how many more transactions can we fit in a block? How much faster are blocks going to grow?"
[04-25-22 17:56:45] <merope> If the granularity is too small, then a user/wallet might have to skip a few levels at a time to justify their inclusion in the next block
[04-25-22 17:57:19] <merope> But if the granularity is too coarse, then the blocksize growth might become unstable
[04-25-22 17:57:58] <mj-xmr[m]> Just shillin' here, but this calls for a proper simulation...
[04-25-22 17:58:08] <gingeropolous[m]> :)
[04-25-22 17:58:30] <UkoeHB> merope: sound's like you have some homework :)
[04-25-22 17:58:59] <merope> One CCS proposal at a time 😅
[04-25-22 17:59:32] <merope> I wouldn't know how to model it, but intuition tells me this is a control theory problem
[04-25-22 17:59:55] <mj-xmr[m]> It sounds like it, alright (I'm a control engineer)
[04-25-22 18:00:06] <merope> (but maybe this already obvious to you)
[04-25-22 18:00:06] <UkoeHB> maybe some homework for mj-xmr[m] ?
[04-25-22 18:00:10] <merope> *this was
[04-25-22 18:01:02] <Rucknium[m]> It's not just a control theory problem. People are not atoms ;)
[04-25-22 18:01:09] <mj-xmr[m]> UkoeHB: If anybody has time to give me a 1-2 hours tutorial, I can take it up.
[04-25-22 18:01:25] <mj-xmr[m]> Rucknium[m]: Discrete control theory. Happy now?
[04-25-22 18:01:30] <Rucknium[m]> It has control theory elements
[04-25-22 18:01:47] <UkoeHB> Ok, we are at the hour mark so I'll call it. Thanks for attending everyone
[04-25-22 18:01:47] <UkoeHB> I will implement round(pows(1.5)) as an interim solution so I can make further progress on my PoC.
```

# Action History
- Created by: Rucknium | 2022-04-19T03:02:05+00:00
- Closed at: 2022-04-26T22:23:23+00:00
