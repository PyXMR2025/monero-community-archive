---
title: Monero Research Lab Meeting - Wed 07 June 2023, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/846
author: Rucknium
assignees: []
labels: []
created_at: '2023-06-07T14:09:31+00:00'
updated_at: '2023-06-13T04:36:00+00:00'
type: issue
status: closed
closed_at: '2023-06-13T04:36:00+00:00'
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

Meeting chairperson: UkoeHB

Previous meeting agenda/logs:

#844 

# Discussion History
## UkoeHB | 2023-06-07T21:02:39+00:00
`[06-07-2023 17:00:05] <UkoeHB> Meeting time`
`[06-07-2023 17:00:11] <UkoeHB> 1. greetings`
`[06-07-2023 17:00:13] <UkoeHB> hello`
`[06-07-2023 17:00:17] <vtnerd> hi`
`[06-07-2023 17:00:18] <xmrack[m]> Hi`
`[06-07-2023 17:00:22] <rbrunner> Hello`
`[06-07-2023 17:00:24] <jeffro256[m]> Howdy`
`[06-07-2023 17:00:52] <chaserene> hello`
`[06-07-2023 17:01:08] <Rucknium[m]> Hi`
`[06-07-2023 17:03:12] <UkoeHB> 2. updates, what’s everyone working on?`
`[06-07-2023 17:04:02] <UkoeHB> Me: slowly putting together monerokon presentation. I’m considering taking a long break after monerokon to properly reset.`
`[06-07-2023 17:04:18] <Rucknium[m]> me: OSPEAD`
`[06-07-2023 17:05:23] <vtnerd> zeroconf webhoooks (LWS), otherwise and p2p-encryption / bp++. both are coming along slowly, but some progress is being made`
`[06-07-2023 17:05:28] <Rucknium[m]> There is a 90% probability that MAGIC will have something to announce about EAE attack research this week`
`[06-07-2023 17:05:31] <chaserene> I examined the long-term reorg data provided hyc`
`[06-07-2023 17:05:53] <jeffro256[m]> me: adding support for separation of coinbase/non-coinbase output distributions directly into BlockchainLMDB for issue #109`
`[06-07-2023 17:06:43] <jeffro256[m]> Rucknium[m]: Is it bad.... `
`[06-07-2023 17:06:58] <Rucknium[m]> No`
`[06-07-2023 17:07:29] <Rucknium[m]> The announcement will be "please, community, fund this research so we know how bad it is"`
`[06-07-2023 17:07:37] <Rucknium[m]> And how it could be defended against.`
`[06-07-2023 17:08:33] <UkoeHB> 3. discussion`
`[06-07-2023 17:08:36] <chaserene> I truly wonder how it can be defended against other than churning`
`[06-07-2023 17:09:35] <chaserene> yeah, it's an art for now`
`[06-07-2023 17:10:34] <UkoeHB> chaserene: it sounded like you have some things you want to discuss today`
`[06-07-2023 17:11:04] <xmrack[m]> Increasing the ring size could help`
`[06-07-2023 17:11:04] <chaserene> yes. I wondered where the bottlenecks are exactly on the path to global membership proofs`
`[06-07-2023 17:11:04] <xmrack[m]> But it would need to probably be in the thousands of decoys`
`[06-07-2023 17:11:20] <chaserene> and whether involving new people and expertise could accelerate progress on it`
`[06-07-2023 17:12:22] <Rucknium[m]> Maybe ask Bailey if he wants to do this for trustless global membership proofs: Bailey & Miller (2023) "Formalizing Soundness Proofs of SNARKs" https://eprint.iacr.org/2023/656`
`[06-07-2023 17:12:39] <xmrack[m]> <xmrack[m]> "https://moneroresearch.info/..." <- UkoeHB: did you have a chance to read this paper/ have any thoughts on the concept?`
`[06-07-2023 17:12:42] <chaserene> Rucknium implied it's mostly a math problem for now, to which I answered that even hiring mathematicians and academics could be an option`
`[06-07-2023 17:12:54] <rbrunner> Maybe me manage to summon kayabaNerve, because he was so far a main force behind this push`
`[06-07-2023 17:13:03] <Rucknium[m]> That would also help us figure out what the state of the security proofs are in these papers`
`[06-07-2023 17:13:42] <Rucknium[m]> kayabanerve: What are the bottlenecks to implementing trustless global membership proofs in Monero?`
`[06-07-2023 17:15:24] <rbrunner> tevador has also been pretty active in the issue: https://github.com/monero-project/research-lab/issues/100`
`[06-07-2023 17:15:43] <chaserene> Rucknium[m]: thanks, that's a point to start at. there are all these researchers on whose efforts Monero is built, but I sense some kind of divide between their world and ours `
`[06-07-2023 17:16:32] <Rucknium[m]> chaser: IMHO, if you want this to happen, you should contact Bailey`
`[06-07-2023 17:16:54] <rbrunner> Well, theory and implementing are by very nature quite different already, seems to me`
`[06-07-2023 17:17:02] <Rucknium[m]> I don't want to do it since I have a lot on my plate already. And cryptography isn't something I know`
`[06-07-2023 17:17:50] <UkoeHB> xmrack[m]: not yet`
`[06-07-2023 17:18:11] <Rucknium[m]> Sometimes there is a divide since what researchers come up with cannot be practically implemented in Monero (or any other usable system). I guess the idea is that research will eventually fix the problems that an unimplementable idea has.`
`[06-07-2023 17:18:44] <Rucknium[m]> For example, that paper that xmrack linked that wanted to have address sizes in the kilobytes`
`[06-07-2023 17:19:21] <Rucknium[m]> Or these papers that want a partitioning decoy selection algorithm. Those are a little closer to being practical, but with disadvantages.`
`[06-07-2023 17:19:25] <chaserene> Rucknium: I'm no cryptographer either. I'll take a look at the paper to have at least a basic understanding and see if I can formulate how Bailey can help in this`
`[06-07-2023 17:20:36] <plowsof11> i would just like to pop this invitation in from QuarksLab (if anyone was interested)- "We can schedule a new presentation of our activities and convictions in the next few days if that suits you, for example: June 8th between 14h and 16h / 13th afternoon /15th between 3pm and 5pm" if someone wants to "know how they could help the project", i am also going to poke the bp++ author again for an update on the final version of the pap`
`[06-07-2023 17:21:13] <Rucknium[m]> That's why MAGIC says that we would fund actionable research on Monero: https://monerofund.org/apply_research`
`[06-07-2023 17:21:23] <UkoeHB> plowsof11: that sounds valuable to me`
`[06-07-2023 17:21:24] <Rucknium[m]> (I wrote it)`
`[06-07-2023 17:21:40] <jeffro256[m]> Rucknium[m]: That's not necessarily completely infeasible, you already have to copy/paste XMR addresses, and a couple kilobytes can still fit on a QR code `
`[06-07-2023 17:21:50] <Rucknium[m]> And it needs "A plan to work with Monero's developers and/or researchers to integrate the results of the research into Monero's protocol or ecosystem."`
`[06-07-2023 17:22:35] <rbrunner> Hardware wallets will surely thank us for 2KB addresses or so ...`
`[06-07-2023 17:22:50] <chaserene> Rucknium: yes, this is a much more promising avenue for this  than CCS`
`[06-07-2023 17:23:06] <chaserene> I dunno, I'm already freaked out by the Jamtis address lengths`
`[06-07-2023 17:23:52] <Rucknium[m]> plowsof: Are those UTC times?`
`[06-07-2023 17:24:18] <xmrack[m]> rbrunner: 2kb….. thats cute. They propose 37kb addresses `
`[06-07-2023 17:24:28] <rbrunner> :)`
`[06-07-2023 17:24:33] <jeffro256[m]> oop`
`[06-07-2023 17:24:49] <plowsof11> I have no idea, i will get the times / tell them UkoeHB wants to attend (hopefully it is not just a sales rep reading a generic pdf) `
`[06-07-2023 17:25:23] <Rucknium[m]> A presentation from them seems interesting to me`
`[06-07-2023 17:26:23] <plowsof11> great, ill pass this on and get times / more info `
`[06-07-2023 17:27:39] <UkoeHB> Thanks plowsof11`
`[06-07-2023 17:28:16] <chaserene> while we're waiting for kayabanerve or tevador to pop in, I want to put this forward: visualization of hyc's long-term reorg data https://github.com/monero-project/research-lab/issues/102#issuecomment-1577827259`
`[06-07-2023 17:28:17] <chaserene> done by me, wholly non-quantitative, but has a few interesting insights`
`[06-07-2023 17:28:24] <jeffro256[m]> I wanted to bring this up so people can chew on it: is there any downsides to the #109 idea of when spending non-coinbase outputs, only selecting non-coinbase decoys? I have a couple in mind, but I don't want to bias ideas that people may have. `
`[06-07-2023 17:28:31] <xmrack[m]> Nice work chaser `
`[06-07-2023 17:29:20] <xmrack[m]> jeffro256[m]: Wouldnt an obvious downside be that when a coinbase output is spent it’s guaranteed to be the true spend? `
`[06-07-2023 17:29:45] <Rucknium[m]> chaser: Thanks for the parsing of the log files. I think we could probably reduce the 10 block lock to 5 blocks. Probably. We would want to do more analysis and thinking about it.`
`[06-07-2023 17:30:31] <chaserene> namely,`
`[06-07-2023 17:30:31] <chaserene> * reorgs correlate w/ hash power`
`[06-07-2023 17:30:31] <chaserene> * reorgs relative to hashpower decreased a lot after Carbon Chameleon, and even more after Fluorine Fermi, and I wonder if you guys have a guess why`
`[06-07-2023 17:30:42] <Rucknium[m]> You could say if the real spend is a coinbase, then all ring members are coinbase outputs`
`[06-07-2023 17:31:12] <Rucknium[m]> chaser: I think sech1 helped improve network connectivity and reduced the probability of re-orgs`
`[06-07-2023 17:31:38] <jeffro256[m]> @xmrack Yes that's biggest one, when miners want to spend outputs it reveals their true spend. This isn't such a big issue for me though, since 1) 90% of miners are either p2pool or trad pool miners so miner spends are already public information or 2) if it's a solo pool miner, they can churn once to a normal output (wallet code would do this default ideally)`
`[06-07-2023 17:32:10] <chaserene> Rucknium[m]: a-ha`
`[06-07-2023 17:33:16] <jeffro256[m]> There was also the changes that ooo implemented which allowed for more p2p connections to stay alive and healty `
`[06-07-2023 17:33:19] <chaserene> Rucknium: I would lean toward a more conservative reduction (8?), see how it performs in prod, and reassess whether to keep it, go higher or go lower. I agree with hyc's notion about unknown unknowns earlier in that thread. a reduction would invite more attackers who so far have been outpriced`
`[06-07-2023 17:33:48] <Rucknium[m]> chaser: I think this was the PR from sech1: https://github.com/monero-project/monero/pull/8675`
`[06-07-2023 17:34:19] <jeffro256[m]> ^^^^^`
`[06-07-2023 17:34:22] <chaserene> Rucknium: nice, thanks`
`[06-07-2023 17:35:06] <Rucknium[m]> If an attacker has enough hashpower to reorg 5 blocks, then Monero has bigger problems than the privacy issue with re-orgs`
`[06-07-2023 17:35:10] <Rucknium[m]> I agree that when the system changes, you could see the incentives change, so attackers could change behavior. But 5 blocks...?`
`[06-07-2023 17:35:26] <jeffro256[m]> https://github.com/monero-project/monero/pull/8426`
`[06-07-2023 17:35:59] <chaserene> jeffro256: thanks`
`[06-07-2023 17:36:17] <jeffro256[m]> Before PR #8426, a lot of connections were getting dropped and stagnating. Afterwards, alive connections went up on average by about 30% `
`[06-07-2023 17:36:28] <xmrack[m]> jeffro256: what do you think of Rucknium idea to have coinbase outputs create rings using only other coinbase outputs. This way we stick to our ethos of private by default `
`[06-07-2023 17:37:09] <Rucknium[m]> chaser: The 10 block lock can only be changed by a hard fork. Stepping it down gradually would take years`
`[06-07-2023 17:37:19] <UkoeHB> jeffro256[m]: from a meta point of view, a special rule for coinbase spends doesn’t solve the root problem which is inadequacy of ring signatures. Setting a precedent could have long term effects… which is an ambiguous complaint.`
`[06-07-2023 17:38:53] <jeffro256[m]> xmrack[m]: My PR actually does this currently, but it doesn't take into account amounts which reduces the effectiveness `
`[06-07-2023 17:39:26] <chaserene> Rucknium[m]: yeah, I know. I can imagine attackers who aren't willing to attempt the whole thing with 10 blocks, but will come out of the shadows with 5. but of course I can't prove it would play out that way`
`[06-07-2023 17:39:52] <jeffro256[m]> UkoeHB: Yes, but this is a clear cut rule which raises the effective ring size for free in terms of on-chain data, and just a tiny overhead for RPC servers `
`[06-07-2023 17:41:28] <jeffro256[m]> Obviously nothing is better theoretically than just increasing ring size, but look at the impact in practice, especially with p2pool`
`[06-07-2023 17:42:02] <Rucknium[m]> You could use the formula for 51% attack success probability to determine the hashpower for an occasionally successful 10 block reorg vs. 5 block reorg with minority hashpower`
`[06-07-2023 17:42:20] <UkoeHB> That path has a clear slippery slope. Say you make it a wallet rule, well now you have implementation variance. In response, we get pressure for a protocol rule. After that might come balance splitting (coinbase/non-coinbase), which is a wallet nightmare. What if some other use-case clearly divides the global money supply? The coinbase precedent will encourage going down the same route again.`
`[06-07-2023 17:42:26] <hyc> IMO the 10-block lock must stay unchanged. Tweak wallets to auto-create change like Monerujo did, if purchase convenience is an issue`
`[06-07-2023 17:44:13] <hyc> A more useful problem to tackle is speeding up IBD further. we've discussed methods a few times already but nothing's come of them.`
`[06-07-2023 17:45:00] <rbrunner> IBD = initial block distribution?`
`[06-07-2023 17:45:03] <hyc> allow nodes further than N blocks behind to use summary/checkpoint hashes, generated the same way as the hardcoded ones,`
`[06-07-2023 17:45:05] <hyc> yes`
`[06-07-2023 17:45:09] <chaserene> D = downuoad`
`[06-07-2023 17:45:18] <hyc> ^ yes`
`[06-07-2023 17:46:06] <UkoeHB> 10-block lock is a safety factor of at least 2.5, which is a good value. Idk if we can justify a lower safety factor.`
`[06-07-2023 17:46:29] <hyc> yeah, decreasing that is playing with fire`
`[06-07-2023 17:46:50] <Rucknium[m]> Here's that minority attack formula: https://www.worldscientific.com/doi/abs/10.1142/S021902491850053X`
`[06-07-2023 17:47:14] <jeffro256[m]> UkoeHB: I get the concern, but I don't think I buy this slippery slope argument since there is already a hard protocol difference between coinbase and non-coinbase outputs (coinbase outputs appear in special transactions in the block and have amounts encoded in tx prefix even when version > 1). `
`[06-07-2023 17:47:41] <Rucknium[m]> Safety factor of 2.5? Is that in the github issue somewhere?`
`[06-07-2023 17:47:44] <chaserene> hyc: I agree speeding up IBD is good, but not sure how it's related to the problem caused by the 10-block lock`
`[06-07-2023 17:47:46] <rbrunner> Well, 5 blocks are still 10 minutes, which won't make all people happy anyway.`
`[06-07-2023 17:48:20] <hyc> chaserene: not related. IMO the 10-block issue needs to be dropped and forgotten.`
`[06-07-2023 17:48:38] <hyc> let the wallets deal with the UX.`
`[06-07-2023 17:49:03] <UkoeHB> Rucknium[m]: with a typical reorg depth of 2-3, we get a safety factor of at least 2.5`
`[06-07-2023 17:49:04] <chaserene> Rucknium[m]: I think he means that all the reorgs we see are 2-4 blocks deep`
`[06-07-2023 17:49:30] <rbrunner> With years between 4 block reorgs, right?`
`[06-07-2023 17:49:35] <hyc> decreasing the 10-block lock is foolish, if not totally reckless.`
`[06-07-2023 17:49:40] <Rucknium[m]> PocketChange and similar solutions probably reduce privacy. Consolidating pocketchange can improve guessing probability of real spends.`
`[06-07-2023 17:50:03] <chaserene> I don't know, those reaorgs don't have a clear date to them in the logs`
`[06-07-2023 17:50:25] <hyc> you will just have to estimate based on the logfile names`
`[06-07-2023 17:50:32] <hyc> and perhaps the line numbers in each logfile`
`[06-07-2023 17:51:26] <hyc> Rucknium[m]: I suppose this is the same problem we have from churning`
`[06-07-2023 17:52:03] <Rucknium[m]> Maybe some similarities with churning`
`[06-07-2023 17:52:34] <UkoeHB> jeffro256[m]: I’m not convinced, you can use any distinction to make an anonymity puddle. Whether the cause is a protocol rule or a user behavior, the result is the same in terms of privacy.`
`[06-07-2023 17:53:14] <Rucknium[m]> PocketChange consolidation is basically this problem: Borggren, N., & Yao, L. (2020). "Correlations of multi-input Monero transactions." https://moneroresearch.info/index.php?action=resource_RESOURCEVIEW_CORE&id=57`
`[06-07-2023 17:53:36] <hyc> yeah, understood`
`[06-07-2023 17:54:02] <Rucknium[m]> There is a warning in wallet2 when you spend two real spends that are close to each other in age...and both old, IIRC`
`[06-07-2023 17:55:11] <chaserene> <Rucknium[m]> "PocketChange and similar..." <- yes, I really didn't like how the Monerujo dev didn't mention at all the privacy tradeoff`
`[06-07-2023 17:55:31] <chaserene> in their announcements`
`[06-07-2023 17:55:44] <UkoeHB> We are approaching the end of the meeting, are there any last-minute questions or comments on other topics?`
`[06-07-2023 17:55:54] <Rucknium[m]> If coinbase outputs are not excluded from rings, then ring size should be increased to compensate for the number of black marbles that coinbases create`
`[06-07-2023 17:56:18] <Rucknium[m]> Maybe "proportion" is a better term than "number". Since coinbase outputs are included in proportion to their prevalence in recent blocks`
`[06-07-2023 17:57:09] <hyc> since we want to increase ringsize to N=128 or more anyway, just do that`
`[06-07-2023 17:57:51] <Rucknium[m]> The formula would be...something...to nominal ring size be equivalent to effective ring size at a particular (lower) ring size.`
`[06-07-2023 17:59:09] <Rucknium[m]> This issue with coionbase outputs was brought up months ago and there were no strong objections. I asked what the next step were...and nothing`
`[06-07-2023 17:59:09] <jeffro256[m]> Doesn't matter if ring size is 128, there's still X% of ring members which are coinbase when spending non-coinbase. Why not remove those ring members for free?`
`[06-07-2023 17:59:11] <Rucknium[m]> So there is a problem with the decisionmaking process here`
`[06-07-2023 17:59:32] <Rucknium[m]> jeffro's work is a sunk cost, of course. We don't have to do it just because the sunk cost was expended`
`[06-07-2023 18:00:16] <rbrunner> Removing is not "free", you rise the complexity of the system overall, and the codebase`
`[06-07-2023 18:00:46] <jeffro256[m]> <UkoeHB> "jeffro256: I’m not convinced..." <- You could say the same thing about pre-RCT decoy selection selecting outputs of the same amount. It creates puddles, but that's alright because the alternative is that cross contamination reduces effective rign size `
`[06-07-2023 18:01:01] <rbrunner> The protocol becomes one wart more, to put it aggressively ...`
`[06-07-2023 18:01:09] <rbrunner> *gets`
`[06-07-2023 18:01:14] <Rucknium[m]> Of course, further research and analysis can uncover issues that were not considered before`
`[06-07-2023 18:01:50] <Rucknium[m]> This is an unavoidable curse of ring signatures. This overall problem was written when the Cryptonote paper was released`
`[06-07-2023 18:02:18] <Rucknium[m]> Everyone has accepted this problem `
`[06-07-2023 18:02:57] <rbrunner> Maybe "everyone" is a bit much :)`
`[06-07-2023 18:03:05] <Rucknium[m]> There are some protocols that ignore these ring signature problems, e.g. Zano and Mobilecoin. I hope Monero does not become one of them`
`[06-07-2023 18:04:00] <Rucknium[m]> What I mean is Monero was born with this problem. By trying to improve Monero, you accept that the system is imperfect`
`[06-07-2023 18:04:18] <rbrunner> Ah, ok, I see`
`[06-07-2023 18:04:46] <UkoeHB> jeffro256[m]: overall I’m not against it being a wallet feature, but we should keep in mind the trade offs and dangers`
`[06-07-2023 18:05:11] <UkoeHB> We are past the hour so I’ll call it here, thanks for attending everyone`

# Action History
- Created by: Rucknium | 2023-06-07T14:09:31+00:00
- Closed at: 2023-06-13T04:36:00+00:00
