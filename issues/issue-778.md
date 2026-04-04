---
title: Monero Research Lab Meeting - Wed 11 January 2023, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/778
author: Rucknium
assignees: []
labels: []
created_at: '2023-01-10T01:17:34+00:00'
updated_at: '2023-01-16T21:26:50+00:00'
type: issue
status: closed
closed_at: '2023-01-16T21:26:50+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

[Join the Monero Matrix server if you don't already have a Matrix account.](https://forum.monero.space/d/79-how-to-join-the-monero-core-team-matrix-server-web)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/converter.html?iso=20211027T170000&p1=1440)

Main discussion topics:

1. Greetings

2.  Discuss [Jamtis address checksums](https://gist.github.com/tevador/50160d160d24cfc6c52ae02eb3d17024#64-checksum).

3. Improvements to the decoy selection algorithm ( [Decoy Selection Algorithm - Areas to Improve](https://github.com/monero-project/research-lab/issues/86), [Binning PoC](https://github.com/monero-project/research-lab/issues/88), [OSPEAD](https://ccs.getmonero.org/proposals/Rucknium-OSPEAD-Fortifying-Monero-Against-Statistical-Attack.html) ) @j-berman @Rucknium

4. Seraphis. ( [UkoeHB's Seraphis Proof of Concept work](https://ccs.getmonero.org/proposals/seraphis-wallet-poc-2.html), [Seraphis repo](https://github.com/UkoeHB/Seraphis) ).

5. MRL Meta: "Cat herding", i.e. prioritization of research areas and features. Active recruitment of technical talent, MRL structure, funding (@Rucknium & others) [MoneroResearch.info repository of Monero-related research papers](https://moneroresearch.info/), [Reddit discussion](https://www.reddit.com/r/Monero/comments/pkg3d6/the_monero_project_should_actively_recruit/)

6. Any other business

7. Confirm next meeting agenda


Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: UkoeHB

Previous meeting agenda/logs:

#776 

# Discussion History
## UkoeHB | 2023-01-11T18:10:13+00:00
`[01-11-2023 17:00:45] <UkoeHB> meeting time`
`[01-11-2023 17:00:55] <UkoeHB> 1. greetings`
`[01-11-2023 17:00:57] <UkoeHB> hello`
`[01-11-2023 17:00:59] <one-horse-wagon[> Hello!`
`[01-11-2023 17:01:07] <rbrunner> Hello`
`[01-11-2023 17:01:20] <vtnerd> hi`
`[01-11-2023 17:01:24] <Rucknium[m]> Hi`
`[01-11-2023 17:01:29] <dangerousfreedom> Hi`
`[01-11-2023 17:02:31] <UkoeHB> 2. updates, what’s everyone working on?`
`[01-11-2023 17:03:16] <vtnerd> I did some serialization stuff again (tests still dont work), and got sucked into lws dev work (first potential commerical deployment)`
`[01-11-2023 17:03:38] <vtnerd> so not much related to -mrl, more -dev`
`[01-11-2023 17:04:05] <vtnerd> the lws work shouldnt be too long hopefully`
`[01-11-2023 17:04:54] <Rucknium[m]> Analyzing data about mining pools' block template update behavior. It affects the amount of time it takes for a transaction to receive its first confirmation on the blockchain.`
`[01-11-2023 17:05:11] <UkoeHB> me: continued library cleanup, also did some reviewing of dangerousfreedom’s seraphis knowledge proof work and made some adjustments to jamtis to support enote ownership proofs and address index proofs`
`[01-11-2023 17:05:40] <endogenic> (greetings)`
`[01-11-2023 17:08:46] <dangerousfreedom> UkoeHB: I have a question to your new proposed scheme. Why K_1 represents a full address? An address is not defined by three public keys, K_1,K_2,K_3? If you are proving knowledge of only K_1 I believe that there may be room for generating a fake proof even if the enote would be unspendable. I dont see a real use case for that since enotes are meant to be owned by someone but it may leave room for that, what do you think?`
`[01-11-2023 17:09:03] <dangerousfreedom> I agree it is much cleaner though now`
`[01-11-2023 17:09:10] <dangerousfreedom> (the schemes)`
`[01-11-2023 17:12:30] <UkoeHB> 3. discussion`
`[01-11-2023 17:13:16] <SerHack> hi`
`[01-11-2023 17:14:09] <UkoeHB> dangerousfreedom: ownership doesn’t require spendability I think`
`[01-11-2023 17:14:50] <rbrunner> (Those "updates" should be these, I think: https://gist.github.com/tevador/50160d160d24cfc6c52ae02eb3d17024?permalink_comment_id=4432591#gistcomment-4432591 )`
`[01-11-2023 17:15:30] <UkoeHB> Anyway, including an address ownership proof and amount proof is sufficient to prove an enote is spendable`
`[01-11-2023 17:16:30] <dangerousfreedom> Yeah, Ok. I agree with that.`
`[01-11-2023 17:16:40] <rbrunner> I have a question out of curiousity, as a layman regarding crypto: Was it easy to find these adjustments you propose there?`
`[01-11-2023 17:17:18] <rbrunner> To me it looks almost like magic - add a factor here, hash a bit more there, and presto, the system has more desirable capabilities`
`[01-11-2023 17:17:34] <rbrunner> Somehow amazing that such a complex construct is still so malleable`
`[01-11-2023 17:22:19] <rbrunner> And do I see that correctly: If Seraphis and Jamtis were already active on Mainnet, such changes would need a hardfork to introduce?`
`[01-11-2023 17:22:23] <Rucknium[m]> p2pool will upgrade to reduce the number of p2pool payout outputs by 50-66%: https://www.reddit.com/r/MoneroMining/comments/1095730/psa_p2pool_network_upgrade_aka_hardfork_on_march/`
`[01-11-2023 17:22:27] <UkoeHB> wasn't too hard for me, but I have a lot of experience with crypto protocol engineering`
`[01-11-2023 17:24:27] <UkoeHB> Rucknium[m]: it's good news nice work sech1`
`[01-11-2023 17:24:54] <dangerousfreedom> Rucknium[m]: Nice!`
`[01-11-2023 17:25:09] <rbrunner> I hope that p2pool hardfork does not get contested, and the variants multiply :)`
`[01-11-2023 17:26:14] <Rucknium[m]> With the p2pool upgrade, I think the proposed (1) coinbase consolidation tx type and (2) avoiding selecting coinbase outputs as decoys is still needed. Just not as urgently needed.`
`[01-11-2023 17:28:14] <rbrunner> So maybe we can muddle through until Seraphis`
`[01-11-2023 17:29:38] <UkoeHB> right, I proposed this last week https://github.com/monero-project/research-lab/issues/108`
`[01-11-2023 17:29:48] <UkoeHB> after thinking about it more, I'm not sure that's the right direction`
`[01-11-2023 17:30:15] <Rucknium[m]> Coinbase consolidation tx type has to wait for a hard fork anyway. Decoy selection changes could (and probably should) be implemented at the same time as OSPEAD improvements, assuming OSPEAD passes review.`
`[01-11-2023 17:31:06] <UkoeHB> needing to merge coinbase enotes is one example of a broader class of problems - a public group consolidating enotes is statistically significant`
`[01-11-2023 17:31:43] <UkoeHB> a coinbase consolidation tx type is not a general solution, it is a specific solution`
`[01-11-2023 17:32:05] <rbrunner> You mean a public group of Monero users that do something, namely consolidate?`
`[01-11-2023 17:33:13] <fr33_yourself[m]> Will the code surrounding bulletproofs + need to be rewritten for Seraphis? The part of the code that proves inputs = outputs + fee?`
`[01-11-2023 17:33:17] <UkoeHB> this solution amounts to elevating the circumstances of miners to first-class status in the protocol, while still leaving the general problem unsolved (e.g. what about consolidating the outputs of consolidation txs?)`
`[01-11-2023 17:33:42] <UkoeHB> fr33_yourself[m]: no, range proofs are plug and play`
`[01-11-2023 17:35:25] <fr33_yourself[m]> So that part of the codebase(rangegproofs) won't be touched meaning the security level of Seraphis transaction amount proofs will be exactly equal to what it currently is?`
`[01-11-2023 17:35:29] <UkoeHB> rbrunner: well any user that receives multiple enotes from outside parties and consolidates those enotes will have a statistically significant tx`
`[01-11-2023 17:36:11] <UkoeHB> fr33_yourself[m]: yes, unless BP++ is implemented (which should have equivalent security properities) https://github.com/monero-project/research-lab/issues/101`
`[01-11-2023 17:37:02] <rbrunner> I see. Doesn't sound that a bit like an unsolvable problem? Like trying to consolidate without consolidating, because with that I get too many enotes on a single heap?`
`[01-11-2023 17:37:04] <UkoeHB> actually I did duplicate BP+ so I could use the seraphis transcript and multiexponentiation tools, which add a little bit of efficiency`
`[01-11-2023 17:37:25] <UkoeHB> rbrunner: the solution is a global membership proof`
`[01-11-2023 17:37:37] <fr33_yourself[m]> Sounds good, thanks for the quick response. I think the fact that transaction amount proofs stay the same in terms of security will help lessen friction of Seraphis upgrade down the pipe.`
`[01-11-2023 17:38:50] <rbrunner> Is something like that akin to nuclear fusion, always 20 years in the future? :)`
`[01-11-2023 17:39:15] <fr33_yourself[m]> As an end user, I only think transactions size in kb and overhaul of address scheme could turn out to be points of friction in the future assuming the security of the code implementation of bulletproofs + or ++ is the same as it is presently.`
`[01-11-2023 17:39:20] <UkoeHB> rbrunner: perhaps`
`[01-11-2023 17:40:25] <UkoeHB> fr33_yourself[m]: tx size will not increase by more than 2x (probably only 1.3x or so)`
`[01-11-2023 17:42:23] <fr33_yourself[m]> UkoeHB: Thanks I thought I read something similar to this recently. Like a Seraphis will be about 3kb as opposed to 2kb currently. However, is the tradeoff of having more ring members really worth increasing the tx size? One of the things that I think has helped Monero's adoption over the past hardforks is that transaction size has decreased and speed has increased consistently.`
`[01-11-2023 17:44:11] <fr33_yourself[m]> I think the shift from standard rangeproofs to the first implementation of bulletproofs greatly spurred people to shift from other cryptos to Monero and consider the tradeoff of running a full node more favorable than it would've been previously with the huge rangeproof tx's`
`[01-11-2023 17:44:59] <Rucknium[m]> fr33_yourself: The decision on the tradeoff between tx size and ring size is something that is in the hands of the community. As someone who researches statistical attacks against Monero user privacy, IMHO, the tradeoff would be worth it.`
`[01-11-2023 17:46:16] <fr33_yourself[m]> Rucknium[m]: I understand your perspective and appreciate the work you have done on statistical monitoring of spends. However, isn't there some middle-ground solution where we keep the transactions size in kb of Seraphis equivalent to what we have now?`
`[01-11-2023 17:46:43] <rbrunner> Is it so that much of the size increase comes from the larger rings? I doubt it a bit because they are "binned" / encoded in a completely different way.`
`[01-11-2023 17:47:02] <UkoeHB> fr33_yourself[m]: for me, the advantage of increased ring sizes is binning the decoys - basically instead of single decoys selected from the chain you select clumps of decoys in the same way. This addresses an analysis mode that uses timing information about when you receive enotes to ignore decoys that don't match the timing profile.`
`[01-11-2023 17:47:15] <fr33_yourself[m]> Rucknium[m]: Would be the difference in ring size of the current proposed Seraphis tx versus a Seraphis tx that is only 2kb\`
`[01-11-2023 17:47:42] <UkoeHB> fr33_yourself[m]: you can look at estimates I made here https://github.com/monero-project/research-lab/issues/91#issuecomment-1047191259`
`[01-11-2023 17:48:48] <UkoeHB> right now I have seraphis-squashed implemented`
`[01-11-2023 17:49:06] <rbrunner> I think almost everything is a bit bigger with Seraphis, I doubt we win much if we go down to e.g. 50 ring members, but I may be mistaken`
`[01-11-2023 17:50:09] <UkoeHB> verification time is actually lower than clsag with 16-size rings with seraphis-squashed at 128-size rings`
`[01-11-2023 17:51:02] <fr33_yourself[m]> I mean it's not the end of the world if transactions are 3kb, but I feel like there is a Monero adoption timeline where hardware begins to trouble individuals wanting to run full nodes. Currently, it's hard to imagine with less than 20k tx per day, but things can change quicker than we may imagine.`
`[01-11-2023 17:51:55] <rbrunner> Would that be, in the doc linked above, the graph "Reference Set Size vs Transaction Size"? To check the influence on number of ring members on tx size?`
`[01-11-2023 17:52:04] <Rucknium[m]> Preliminary results on tx confirmation delay: Most mining pools update their block template only once: when they see a new block. They don't include new transactions that appear in the mempool after the previous block was found.`
`[01-11-2023 17:52:24] <Rucknium[m]> As a result, the average time to first confirmation is actually 30 seconds longer for a XMR tramsaction than a Litecoin transaction, despite Litecoin having a 2.5 minute target block time (compared to XMR's 2 mins).`
`[01-11-2023 17:52:37] <UkoeHB> fr33_yourself[m]: you can read a bit about the advantages of binning here https://github.com/monero-project/research-lab/issues/84 and in the references`
`[01-11-2023 17:53:18] <Rucknium[m]> If all centralized pools used p2pool's update policy, the average time to first confirmation would fall by a full minute`
`[01-11-2023 17:54:42] <rbrunner> Quite surprising that this fact becomes known so late.`
`[01-11-2023 17:54:46] <Rucknium[m]> I'm going to release a write-up on the results with graphs next week. I think the course of action is to try to convince mining pool operators to update their block templates more frequently and/or change the defaults on jtgrassie 's monero-pool software.`
`[01-11-2023 17:55:32] <Rucknium[m]> If centralized pools refuse, then we will go all-in with p2pool adoption! (This is a joke)`
`[01-11-2023 17:56:07] <Rucknium[m]> Anecdotally, I noticed this with my own transactions. You can also see it on txstreet.com`
`[01-11-2023 17:56:18] <rbrunner> Do these pools win something by doing so?`
`[01-11-2023 17:56:25] <UkoeHB> btw, I think you could use a SAG (simplified CLSAG) with seraphis to get 16-size rings and verify txs maybe 20-40% faster than today`
`[01-11-2023 17:56:39] <Rucknium[m]> The Isabellas are kicked off the bus right before it launches into the blockchain.`
`[01-11-2023 17:57:56] <Rucknium[m]> p2pool on average is getting 0.003 XMR more in fee revenue per block than other miners. So pools are losing a bit. But according to sech1 the pools need to do database operations when they update the block templates, which may cost money.`
`[01-11-2023 17:58:36] <sech1> They need to update db when they send out new jobs to all connected miner workers`
`[01-11-2023 17:58:44] <sech1> which can be tens of thousands jobs for each block template`
`[01-11-2023 17:59:48] <Rucknium[m]> I wonder if other PoW coins (I am analyzing LTC, BCH, and DOGE) have more mining centralization so they don't have the database cost.`
`[01-11-2023 17:59:58] <sech1> They do`
`[01-11-2023 18:00:03] <sech1> but they still update template more often`
`[01-11-2023 18:00:20] <Rucknium[m]> They do have the cost or they are more centralized?`
`[01-11-2023 18:00:30] <sech1> I looked at pool code before, and I think 90% of the problem is pool operators just use what's default`
`[01-11-2023 18:00:38] <sech1> Monero pools can update more often`
`[01-11-2023 18:00:42] <sech1> at least every 30 seconds`
`[01-11-2023 18:01:00] <sech1> but it will require some qualification and knowledge from pool operators`
`[01-11-2023 18:01:22] <Rucknium[m]> Yes I would guess that it is "default-itis" rather than a deliberate decision.`
`[01-11-2023 18:02:09] <Rucknium[m]> One of the pool operators seems to update every two minutes if a block hasn't been found. So a +2,+4, +6, etc. minutes`
`[01-11-2023 18:02:18] <Rucknium[m]> Most of the other ones don't update`
`[01-11-2023 18:02:37] <Rucknium[m]> The pool labeling data was gathered by datahoarder.`
`[01-11-2023 18:04:31] <UkoeHB> we are past the hour so I'll call it, thanks for attending everyone`

# Action History
- Created by: Rucknium | 2023-01-10T01:17:34+00:00
- Closed at: 2023-01-16T21:26:50+00:00
