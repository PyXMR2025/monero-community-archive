---
title: Monero Research Lab Meeting - Wed 07 December 2022
source_url: https://github.com/monero-project/meta/issues/763
author: Rucknium
assignees: []
labels: []
created_at: '2022-12-05T21:26:56+00:00'
updated_at: '2022-12-12T19:00:43+00:00'
type: issue
status: closed
closed_at: '2022-12-12T19:00:43+00:00'
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

#760 

# Discussion History
## UkoeHB | 2022-12-07T17:59:48+00:00
`[12-07-2022 16:58:52] <one-horse-wagon[> Hello.`
`[12-07-2022 17:00:05] <UkoeHB> meeting time https://github.com/monero-project/meta/issues/763`
`[12-07-2022 17:00:05] <UkoeHB> 1. greetings`
`[12-07-2022 17:00:05] <UkoeHB> hello`
`[12-07-2022 17:00:24] <rbrunner> Hello`
`[12-07-2022 17:00:31] <Rucknium[m]> Hi`
`[12-07-2022 17:00:51] <plowsof11> hi`
`[12-07-2022 17:00:59] <ArticMine[m]> Hi`
`[12-07-2022 17:01:12] <ghostway[m]> Greetings `
`[12-07-2022 17:01:47] <jberman[m]> hello`
`[12-07-2022 17:03:03] <UkoeHB> 2. updates, what's everyone working on?`
`[12-07-2022 17:03:08] <sneurlax[m]> Hiya`
`[12-07-2022 17:04:14] <Rucknium[m]> I read cover-to-cover Sharma, P. K., Gosain, D., & Diaz, C. 2022. "On the anonymity of peer-to-peer network anonymity schemes used by cryptocurrencies." https://moneroresearch.info/index.php?action=resource_RESOURCEVIEW_CORE&id=130 and the original Dandelion++ paper https://moneroresearch.info/index.php?action=resource_RESOURCEVIEW_CORE&id=122 If we have time I will share my thoughts about it.`
`[12-07-2022 17:05:30] <UkoeHB> me: have been doing cleanup/review on my seraphis_lib branch (should take 2-4 more weeks), started PRing stuff from that branch to upstream (reviews would be great :) ), and updated jamtis address tag hints to use blake2b instead of a layered cipher https://gist.github.com/tevador/50160d160d24cfc6c52ae02eb3d17024?permalink_comment_id=4392414#gistcomment-4392414`
`[12-07-2022 17:06:59] <blankpage[m]> "Address tags" are the proposed shortened version of the very long seraphis addresses, yes?`
`[12-07-2022 17:07:25] <blankpage[m]> Or are these being called "address tag hints"?`
`[12-07-2022 17:08:43] <plowsof11> no further contact with the bp++ author since the last email where he said he was working on adding security proofs. at this point, im wondering how long we should wait before putting the peer review forward for funding. `
`[12-07-2022 17:08:43] <jberman[m]> me: finished stress testing the pool and found a bottleneck + identified a couple changes I think would be good for PR 8076 (reducing trips to the daemon). I talked to rbrunner  and I'm going to submit a PR to their branch implementing those changes, and separately will make a new PR to alleviate the existing bottleneck`
`[12-07-2022 17:08:44] <jberman[m]> Then moving over to Seraphis impl work`
`[12-07-2022 17:09:03] <Rucknium[m]> plowsof: 3+ months IMHO`
`[12-07-2022 17:09:32] <UkoeHB> address tags are encrypted address indices, and the address tag hint is a hint that lets you know if the associated address might be yours (so you don't have to do expensive crypto ops for testing most addresses that aren't yours, during balance recovery)`
`[12-07-2022 17:10:10] <UkoeHB> plowsof11: 2 weeks of no contact is a good time frame for a follow-up`
`[12-07-2022 17:10:35] <jberman[m]> +1^`
`[12-07-2022 17:11:08] <Rucknium[m]> What I mean by three months is that we might want to get the current paper reviewed if there is no update to it after 3 months`
`[12-07-2022 17:11:21] <blankpage[m]> Thanks UkoeHB. What is "the pool" that you stress testing jberman @jberman:matrix.org?`
`[12-07-2022 17:11:21] <plowsof11> november 30th was the last email i sent`
`[12-07-2022 17:12:17] <jberman[m]> blankpage: you were thinking of RID's (recipient identifiers) = proposed shortened version of very long seraphis addresses (they're an easy-to-read hash of the address)`
`[12-07-2022 17:12:27] <jberman[m]> the tx pool`
`[12-07-2022 17:13:01] <jberman[m]> when you submit txs to the network, they enter the tx pool. I've been stress testing how it handles heavy load when lots of txs come in at once`
`[12-07-2022 17:14:19] <jberman[m]> txs enter the tx pool before they're confirmed, and miners mine txs from the pool. once a tx is mined and included in a block, txs are evicted from the pool`
`[12-07-2022 17:15:01] <UkoeHB> 3. discussion period`
`[12-07-2022 17:17:58] * h4sh3d sits in the back`
`[12-07-2022 17:18:11] <Rucknium[m]> Sharma, Gosain, & Diaz (2022) investigate the anonymity of BTC Lightning Network, Dandelion, and Dandelion++. Lightning privacy is poor, as expected. The paper claims to show that improvements can be made to D++ anonymity with some changes to the parameters, but I am not completely convinced.`
`[12-07-2022 17:18:54] <blankpage[m]> OK so "address tags" are more like what has previously been called "view tags". Yes I was thinking of these RIDs from a presentation I saw.`
`[12-07-2022 17:19:17] <Rucknium[m]> First, this paper uses a set of tools with a lower level of rigor than the original D++ paper. The D++ paper proved many of its statements mathematically (Theorem: Proof). Sharma, Gosain, & Diaz (2022) mostly use monte carlo simulations.`
`[12-07-2022 17:20:03] <UkoeHB> blankpage[m]: the address tag hint is like a view tag, it's 2 bytes appended to the encrypted address index`
`[12-07-2022 17:20:35] <Rucknium[m]> Sharma, Gosain, & Diaz (2022) arrives at a different conclusion that the original D+++ paper mostly because (1) They are using a different metric of anonymity. (2) They say that an adversary learning the "private subgraph" is easier than expected. `
`[12-07-2022 17:22:02] <Rucknium[m]> The D++ paper's metric was basically a measure of the guessing probability. The probability of guessing correctly which node originated which tx. The Sharma, Gosain, & Diaz (2022) paper uses an anonymity set measure (they use an information entropy measure that can be translated into an anon set)`
`[12-07-2022 17:22:47] <Rucknium[m]> So we may want to evaluate which metric is more important, taking into account threat models and Monero's overall anonymity issues, including on-chain info`
`[12-07-2022 17:23:46] <Rucknium[m]> For (2), either I am missing something about Sharma, Gosain, & Diaz (2022) or Sharma, Gosain, & Diaz (2022) is missing something about the D++ protocol, IMHO. I don't find their analysis very realistic`
`[12-07-2022 17:24:44] <Rucknium[m]> The the D++ paper, the private subgraph, i.e. the set of nodes and edges that are supposed to be used in the "stem" phase change every 10- minutes. That should limit an adversary's  ability to learn the private subgraph`
`[12-07-2022 17:25:36] <Rucknium[m]> The Sharma, Gosain, & Diaz (2022) paper assume that there are 50 txs broadcasted per node, which gives the adversaries info to learn the subgraph. I don't think that's realistic in the D+ epoch time window`
`[12-07-2022 17:26:03] <Rucknium[m]> We could see what happens if much fewer txs are broadcasted since they have published their simulation code to GitHub`
`[12-07-2022 17:27:09] <UkoeHB> is that 50 new txs created by that node, or 50 txs relayed by that node? in the long run it's reasonable to assume nodes will be broadcasting tons of txs`
`[12-07-2022 17:27:10] <Rucknium[m]> In summary, take no action at this time. See if this paper gets updates or peer review. It would be nice to have Monero D++ implementation specification written out if it doesn't already exist. The D++ leaves some parameters of the protocol open to be decided by the implementation.`
`[12-07-2022 17:27:23] <UkoeHB> relaying tons of txs*`
`[12-07-2022 17:27:24] <rbrunner> 50 txs per 10 minutes sounds only realistic to me for the busiest nodes used by many people as remote nodes`
`[12-07-2022 17:28:11] <rbrunner> At least as tx origin`
`[12-07-2022 17:28:12] <ghostway[m]> I don't think you can assume any less, even the contrary, that nodes will have a uniform distribution on a very high number (or that one node will broadcast many)`
`[12-07-2022 17:28:43] <Rucknium[m]> UkoeHB: IMHO, they could have written it more clearly. To be certain, we would want to review their simulation code. Their wording is "We send 50 transactions per honest node before analyzing the distribution of diffusions per node." I'm not sure if the adversary nodes or the honest nodes are sending these txs.`
`[12-07-2022 17:28:50] <ghostway[m]> Should have, not will have*`
`[12-07-2022 17:29:33] <ghostway[m]> Rucknium[m]: I'd imagine the honest nodes, for an attack? But yea wording is not clear at all`
`[12-07-2022 17:29:35] <UkoeHB> sounds like each honest node is originating 50 txs`
`[12-07-2022 17:30:04] <Rucknium[m]> For the D++ analysis, they assume basically random uniform for the network topography and node behavior. For Lightning, they use the actual LN topology, which has a high centrality degree`
`[12-07-2022 17:31:07] <Rucknium[m]> The network topology is know to LN nodes by design, which is one reason why the sender privacy is found to be so low`
`[12-07-2022 17:31:15] <Rucknium[m]> is known*`
`[12-07-2022 17:33:46] <Rucknium[m]> Their main suggestions for D++ is to have high p_f (the probability that a node continues sending a tx in stem phase rather than fluffing it), which may already be true for Monero, and have a higher number of outward edges in the private subgraph, i.e. higher number of possible nodes that a node will send a stem-phase tx to`
`[12-07-2022 17:33:51] <UkoeHB> I'd be interested to hear vtnerd 's take on the paper`
`[12-07-2022 17:34:50] <rbrunner> So, in short, more hops?`
`[12-07-2022 17:34:51] <Rucknium[m]> IMHO, not a very difficult paper to read, technically. Unclear in some parts, as mentioned.`
`[12-07-2022 17:36:06] <Rucknium[m]> More hops is the p_f recommendation (which corresponds to 1 - q in the original D++ paper). The original paper recommended high p_f anyway. And then more than two nodes chosen to send the stem phase transactions to.`
`[12-07-2022 17:36:23] <ghostway[m]> Isn't this just making the problem a little harder? `
`[12-07-2022 17:36:46] <Rucknium[m]> Making the problem a little harder?`
`[12-07-2022 17:37:57] <ghostway[m]> Of deanonymizing nodes..`
`[12-07-2022 17:38:59] <jberman[m]> (monero's fluff probability is currently 20%: https://github.com/monero-project/monero/pull/7025)`
`[12-07-2022 17:39:07] <Rucknium[m]> Small changes can have big effects. One of the main improvements of D++ over the original Dandelion was to move from 1 out-edge for the stem phase to 2 out-edges.`
`[12-07-2022 17:39:51] <ghostway[m]> Aha, interesting`
`[12-07-2022 17:40:06] <Rucknium[m]> jberman: Thanks. Like I said, it would be good to have our implementation documented...maybe in a document`
`[12-07-2022 17:45:52] <UkoeHB> hmm, any other topics people would like to touch on today?`
`[12-07-2022 17:46:36] <h4sh3d> I just want to mention that we are finally reaching the end of last milestone for farcaster`
`[12-07-2022 17:46:57] <UkoeHB> congrats :)`
`[12-07-2022 17:47:08] <rbrunner> Wow`
`[12-07-2022 17:47:29] <h4sh3d> We’ll have next a final sprint, and you can expect a Reddit post at the end of the week :)`
`[12-07-2022 17:48:23] <h4sh3d> Took us way longer than expected but here we are… and now I said it so we cannot take longer haha`
`[12-07-2022 17:49:05] <Rucknium[m]> One more thing: One of the authors of the Sharma, Gosain, & Diaz (2022) paper is the Chief Scientist for Nym Technologies. There could be a small interest in suggesting that existing anon network systems do not work well.`
`[12-07-2022 17:49:13] <h4sh3d> Anyway, also expect a bit more info next research lab meeting as we’ll be near to release what we consider mainnet ready `
`[12-07-2022 17:50:04] <Rucknium[m]> Does this mean we should stop trying to fix the COMIT atomic swap implementation? Only half-joking.`
`[12-07-2022 17:53:07] <hyc> Rucknium[m]: so, conflict of interest in a research paper? shocking`
`[12-07-2022 17:53:47] <blankpage[m]> Is the annotation/commenting on moneroresearch.info used or are the papers on there discussed in this room?`
`[12-07-2022 17:53:59] <Rucknium[m]> Well, the issue is often that people who know the research area well also have a competing service/product`
`[12-07-2022 17:55:37] <UkoeHB> blankpage[m]: papers should be discussed here, you can back-fill comments into the site if you want`
`[12-07-2022 17:55:51] <Rucknium[m]> blankpage: Right now the annotation feature isn't used much, but I hope that it will be. I will add a link to my comments here to the paper on MoneroResearch.info . We specifically chose the WIKINDX software for its annotation capabilities (and overall feature creed ;)  )`
`[12-07-2022 17:55:51] <Rucknium[m]> feature creep*`
`[12-07-2022 17:59:01] <UkoeHB> ok looks like the meeting is done, thanks for attending everyone`

# Action History
- Created by: Rucknium | 2022-12-05T21:26:56+00:00
- Closed at: 2022-12-12T19:00:43+00:00
