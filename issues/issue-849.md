---
title: Monero Research Lab Meeting - Wed 14 June 2023, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/849
author: Rucknium
assignees: []
labels: []
created_at: '2023-06-13T14:22:03+00:00'
updated_at: '2023-06-16T22:20:27+00:00'
type: issue
status: closed
closed_at: '2023-06-16T22:20:27+00:00'
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

#846 

# Discussion History
## plowsof | 2023-06-16T21:15:15+00:00
Logs 
```
17:00:45 <UkoeHB> meeting time https://github.com/monero-project/meta/issues/849

17:00:45 <UkoeHB> 1. greetings

17:00:45 <UkoeHB> hello

17:01:06 <rbrunner> Hello

17:01:08 <shalit[m]> Hello

17:01:30 <Rucknium[m]> Hi

17:01:34 <vtnerd_> hi

17:04:13 <UkoeHB> 2. updates, what's everyone working on?

17:05:33 <vtnerd_> bulletproofs++. Im a bit bogged down by it, and if someone has free cycles it might be best
they do it. otherwise I will keep slowly hacking away at understanding it or just port from the c version

17:05:52 <vtnerd_> Im keeping my hours to a minimum so CCS isn't billed for poor output

17:05:55 <Rucknium[m]> OSPEAD, working with the formula for double spend races to analyze the 10 block lock,
Dr. Borggren's MAGIC's research proposal to analyze the EAE attack and churning is 80% funded after just one
week: https://monerofund.org/projects/eae_attack_and_churning

17:08:07 <UkoeHB> me: no updates this week

17:08:17 <Rucknium[m]> Thank you to the community

17:09:38 <Rucknium[m]> Was there a tentative time for the code audit firm to give a presentation?

17:10:09 <UkoeHB> tomorrow I think

17:10:17 <UkoeHB> 3. discussion

17:10:27 <vtnerd_> they are presenting ... ?

17:11:16 <Rucknium[m]> plowsof: Do you have details about the presentation?

17:13:51 <Rucknium[m]> I think the tentative time is 15:30 UTC June 15th

17:16:26 <Rucknium[m]> On the 10 block lock: Can an adversary leverage a "benign" block reorg, say 2 blocks
deep, as a step up to try to do something malicious against an N-block-lock? My guess is that they could only
hurt privacy of users who have transactions confirmed in the first block of one of the benign orphaned chains.

17:16:37 <Rucknium[m]> And/or make some of those transactions invalid

17:18:05 <Rucknium[m]> And it seems like it would have a small probability of having an effect since you would
have to have enough network "divergence" for many transactions to not reach the benign re-orged chain _and_
some of those transactions would have to have real spends or decoys exactly N (10) blocks old at the time they
were spent

17:18:08 <UkoeHB> txs in those reorged blocks should not be invalidated

17:18:34 <UkoeHB> afaik they are returned to the tx pool, hyc ?

17:19:07 <vtnerd_> I recall that being the case (return to pool)

17:19:46 <vtnerd_> although a new block and force some out ? something like that, its been a while

17:19:53 <vtnerd_> *can force some out

17:20:11 <Rucknium[m]> I think they would reference invalid output indices in the re-orged chain. Since it's 2
blocks of benign chain plus 9 (or 8?) blocks of a malicious miner that uses the benign chain to get a head
start.

17:20:29 <rbrunner> Yeah, I think I remember that seeing in a test I did, an in this particular case wallet2
does not see those (again) and only notices after mining

17:20:48 <Rucknium[m]> I am trying to put more precise numbers on the risk

17:23:22 <Rucknium[m]> I am referring to this: "If an output created by the first group is used as a decoy by
a random person, then that person's transaction will become invalid after the reorg. In other words, decoys
are vulnerable to the 'confirmation' problem. A tx author should only use decoys that are 'strongly
confirmed', i.e. decoys that are buried below the 'reorg zone'."

17:23:23 <Rucknium[m]> https://github.com/monero-project/research-lab/issues/95

17:25:58 <Rucknium[m]> My scenario is: An adversary has many nodes throughout the network and occasionally
observes a chain divergence. They know that one of the chain "stubs" will be re-orged, so they start mining on
top of that one in secret. That gets them a boost since they won't have to mine the full 10 blocks by
themselves.

17:26:11 <Rucknium[m]> Does this scenario make sense?

17:27:20 <Rucknium[m]> The adversary does not control the contents of those first 2 blocks. Honest miners do.

17:27:21 <UkoeHB> you only get an advantage equal to the network propagation time

17:28:49 <Rucknium[m]> On average, yes. But these blocks that are part of benign re-orgs are extreme cases.
They are actually mined in a short period of time.

17:29:01 <UkoeHB> actually hmm I see your point, you can piggy-back off the work of a natural reorg

17:29:49 <merope> Rucknium[m]: Are you assuming that the attacker already controls a given percentage of the
nethash, or do they have to provision extra hashrate separately for the attack?

17:30:21 <merope> Big difference in costs, especially since the upfront cost of the hardware is way bigger
than the energy cost for the mining itself

17:31:25 <Rucknium[m]> I am assuming they need to provision extra hash rate (i.e. not mining normally), but
maybe that's not the correct assumption.

17:31:50 <Rucknium[m]> Would it matter a lot? The difficulty would not adjust enough in just 10 blocks.

17:33:15 <UkoeHB> you'd need hardware ready to go at a moment's notice, which is a bit different from a
targeted attack (that can use botnets, cloud mining, etc.)

17:34:35 <merope> The difficulty adjustment would be irrelevant, especially since the 60 highest and lowest
block times get cut off from the adjustment calculation (assuming [this
answer](https://monero.stackexchange.com/a/7981) is still valid)

17:34:55 <Rucknium[m]> The cost can be evaluated at the next step in the analysis. I am trying to figure out
if I should plug N or N - 2 into the double-spend race formula

17:35:26 <merope> It's the cost of the hardware itself which makes a big difference

17:35:42 <merope> Ah, ok

17:35:54 <Rucknium[m]> The formula tells you the probability of a malicious re-org of any block depth with any
hashpower share < 50%

17:37:31 <rbrunner> Where is that formula from?

17:37:50 <UkoeHB> an active attack on the network may or may not be able to increase instability, which would
increase natural reorg depths (although I don't think this has ever happened)

17:39:42 <Rucknium[m]> rbrunner:  Grunspan & Pérez-Marco (2020) "Double spend races"
https://arxiv.org/abs/1702.02867

17:39:57 <Rucknium[m]> It's a correction to Satoshi's formula in the bitcoin white paper

17:40:16 <rbrunner> Nice, thanks.

17:40:42 <Rucknium[m]> Satoshi incorrectly assumed that honest hashpower would have a constant rate of finding
blocks: once every 10 minutes.

17:41:03 <Rucknium[m]> That rate is actually varying, of course, since finding blocks is a Poisson process

17:41:43 <Rucknium[m]> The formula for the probability of malicious re-org is a regularized incomplete beta
function

17:42:32 <Rucknium[m]> It can be found as the Rbeta function in the zipfR R package

17:45:08 <UkoeHB> are there any other topics we should discuss today?

17:45:36 <Rucknium[m]> I will make a comment on the MRL GitHub issue with some tables. I will include the
possibility of an adversary building on a benign re-org, but it is unlikely to get them much benefit since the
proportion of transactions that could be affected would be small.

17:47:41 <merope> What do you mean by "it is unlikely to get them much benefit since the proportion of
transactions that could be affected would be small"?

17:48:26 <Rucknium[m]> There are two terms in this probability multiplication (assuming independence):

17:49:35 <Rucknium[m]> a) Probability that a particular transaction propagates through the network to one
"subnet" but not the other. The subnets being basically the subnets that the two beningn, but competing, sets
of miners are in.

17:50:48 <Rucknium[m]> b) Probability that a transaction includes a ring member that is exactly N (10) blocks
old, i.e. has the youngest age possible according to consensus rules. This could be a decoy or real spend.
Seraphis will increase this probability since ring size would be increased.

17:51:06 <Rucknium[m]> That's my opinion about how it could happen

17:52:28 <Rucknium[m]> I am not talking about a bitcoin-style double-spend (and its consequences) where the
victim takes some action, i.e. sends the perpetrator some amount of another coin on another chain as an
exchange)  before waiting some M blocks.

17:53:34 <Rucknium[m]> All PoW chain have that issue. They don't use spending locks to stop it. They say that
users should evaluate their own risks and determine their own waiting times.

17:57:51 <merope> Factor (a) would not be purely random chance though, the attacker could map out the network
and the connections between nodes to see if there are any poorly-connected subnets

17:59:59 <merope> Oh wait, I'm not sure if that makes an actual difference though

18:02:11 <Rucknium[m]> The transaction propagation subnets and the block propagation subnets will overlap in
different ways, with different levels of connectivity. Complicated.

18:05:29 <merope> You mean due to Dandelion++? I think the D++ tx propagation would still be a subset of the
nodes' p2p connections though, right?

18:06:31 <Rucknium[m]> D++ affects it. The main factor is that the nodes that broadcast the most txs are
different from the nodes that broadcast the most new blocks.

18:07:39 <merope> Oh, I see

18:07:39 <Rucknium[m]> e.g. Cake's nodes do not mine. Few users connect to mining pools' nodes to broadcast
their txs.

18:12:00 <UkoeHB> ah the meeting is over, sorry


```
Automated by [this](https://github.com/plowsof/post-libera-meeting-logs)

# Action History
- Created by: Rucknium | 2023-06-13T14:22:03+00:00
- Closed at: 2023-06-16T22:20:27+00:00
