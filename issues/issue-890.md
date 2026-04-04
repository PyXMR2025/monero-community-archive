---
title: Monero Research Lab Meeting - Wed 06 September 2023, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/890
author: Rucknium
assignees: []
labels: []
created_at: '2023-09-05T17:48:09+00:00'
updated_at: '2023-09-21T14:47:43+00:00'
type: issue
status: closed
closed_at: '2023-09-21T14:47:43+00:00'
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

#888 

# Discussion History
## plowsof | 2023-09-21T07:38:31+00:00
Logs 
```
17:00:32 <Rucknium> Meeting time! https://github.com/monero-project/meta/issues/890

17:00:37 <Rucknium> 1) Greetings

17:01:08 <rbrunner> Hello

17:01:11 <m-relay> <e​ndor00:matrix.org> Hello

17:01:56 <vtnerd> hi

17:02:14 <m-relay> <g​hostway:matrix.org> Hello

17:03:44 <UkoeHB> hi

17:03:53 <Rucknium> 2) Updates. What is everyone working on?

17:05:22 <Rucknium> me: Working on nonstandard fee analysis. Working with endor00 on calculating the security
budgets of PoW chains that have experienced malicious deep block re-orgs.

17:07:21 <vtnerd> Ive still got at least one bug in the peerlist sharing for ssl. And I may have to drop the
ssl auth mode (for now), because I don't see how the peerlist binary file can be updated easily to contain
auth values

17:08:03 <vtnerd> actually I post the latter to monero-dev, and hopefully get some comments from moneromoo

17:09:04 <Rucknium> 3) Discussion. What is there to discuss?

17:09:46 <Rucknium> endor00, do you want to share your work in progress?

17:10:13 <m-relay> <e​ndor00:matrix.org> Sure:
https://gist.github.com/endorxmr/a13dce62ae1ba4676a1ed0311d96bf07

17:11:12 <m-relay> <g​hostway:matrix.org> That sounds interesting!

17:11:19 <m-relay> <e​ndor00:matrix.org> So far we've looked at a bunch of attacks on different chains to
compare the mining incentive [$/s] (aka. "security budget") at the time of the attack

17:12:13 <Rucknium> $/s is USD per second

17:12:54 <m-relay> <g​hostway:matrix.org> Measuring what? The mined blocks in in the fork?

17:13:44 <m-relay> <e​ndor00:matrix.org> Some of the coins are pretty small, but the attacks on ETC and BCH
(though the latter did not involve a double-spend) happened in spite of their relatively bigger mining
incentives

17:13:47 <m-relay> <e​ndor00:matrix.org> Notably, the ETC and BCH attacks had budgets greater than Monero's
current budget (also included in the gist)

17:13:54 <UkoeHB> me: It has been 2 months since I said I would go on a 2-month hiatus. The hiatus has been
good to me, I am a lot more productive and motivated these days. Therefore, I am extending my hiatus
indefinitely. That does not mean I have abandoned Monero or the Seraphis project, but it does mean my open CCS
will take a while to complete (there are about 150 hrs remaining).

17:15:14 <UkoeHB> I will report in again in 2 months about my status.

17:15:39 <Rucknium> Thanks, koe

17:15:50 <m-relay> <p​lowsof:matrix.org> Scared me for a moment there, great to hear koe!

17:15:50 <hyc> I don't understand, you are on hiatus but still improved productivity?

17:15:54 <m-relay> <e​ndor00:matrix.org> Another important aspect to note, imo, is the fact that both BCH and
ETC are both forks of other coins, which had significantly larger (10-100x) mining incentives

17:16:18 <hyc> ^ UkoeHB

17:16:51 <m-relay> <1​23bob123:matrix.org> Yeah hmmm

17:17:01 <m-relay> <e​ndor00:matrix.org> Which meant that they had a significantly larger pool of hashrate
that could be redirected at any time to attack them

17:17:01 <m-relay> <1​23bob123:matrix.org> Hiatus means no work

17:17:21 <m-relay> <1​23bob123:matrix.org> Sorry too interrupt

17:19:01 <m-relay> <e​ndor00:matrix.org> Monero, on the other hand, is the largest RandomX coin around -
though it does have to deal with the other side of the asic-resistant coin: there is always a massive amount
of "potential hashrate"  that could be turned on at any time (i.e. all the cpus currently doing anything other
than mining)

17:19:23 <rbrunner> Maybe looking at the PoW algorithms of these coins is essential? If somebody can just stop
to mine BTC for a while and attack BCH, that's very easy to do.

17:20:01 <rbrunner> But yeah, you don't have idle supercomputers lying around that you could use to mine
RandomX

17:20:58 <m-relay> <e​ndor00:matrix.org> For its budget though, Monero is still a rather big network, for its
budget. My "reasonable guesstimate" is that there are ~50k-500k cpus actively mining, right now. Which is
still a significant number, considering that we have nearly 1/300th of BTC's budget

17:21:24 <Rucknium> The security budget is relevant for the 10 block lock analysis. That's what made me want
to compare the security budgets.

17:21:35 <hyc> a recent estimate was 2 million CPU cores. dunno how many cores per CPU.

17:21:38 <m-relay> <g​hostway:matrix.org> Depends, university students do have that access, and they're humans
too... Also, I know of an Alibaba cloud provider that actually does not care if people use his machines to
mine

17:22:11 <plowsof> Michele Orru via zksecurity has expressed interest in the Seraphis paper(s) tasks (when
scope is confirmed, hopefully a quote can be obtained)

17:22:41 <m-relay> <e​ndor00:matrix.org> if we assume ~10 cores/cpu as a rough order of magnitude, that fits
my estimate quite well

17:23:19 <Rucknium> plowsof: How do we get scope confirmed?

17:25:48 <plowsof> I do not know, nobody has complained  it has approval of koe/jberman/kayaba
https://gist.github.com/plowsof/8cb33e2efe4bf0239927ad3bd92326e0

17:26:02 <UkoeHB> hyc: I mean more productive in general, on my other stuff.

17:26:38 <Rucknium> IIRC, with some of these deep block re-orgs, it is suspected that renting hashpower was
involved. There is (was) a lot of spare GPU hashpower up for renting to use against ETC, for example, than
there is for using CPUs to run RandomX against Monero.

17:27:40 <Rucknium> plowsof: I guess getting tevador's approval would get us to loose consensus. What do you
think?

17:27:58 <rbrunner> That is what confuses me a bit: How to factor in how *easy* it is for somebody to come up
with the security budget, so to say

17:28:58 <Rucknium> There have been a few sudden 20-30% overnight increases in total hashpower over the last
year. I don't know where that is coming from.

17:29:57 <m-relay> <e​ndor00:matrix.org> > how easy it is for somebody to come up with the security budget

17:29:58 <m-relay> <e​ndor00:matrix.org> ?

17:31:32 <rbrunner> Maybe I misunderstand, but isn't that security budget related with the cost of an attack?
More security budget, the higher the cost of an attack?

17:32:38 <m-relay> <e​ndor00:matrix.org> Indirectly. The mining incentive/security budget tells us how much
money there is on the table for miners. The greater the incentive, the more room there is for more miners to
join

17:34:20 <m-relay> <e​ndor00:matrix.org> And we can calculate the maximum size of the network that can be
supported for a given budget, assuming a given electricity cost and knowing the highest efficiency mining
hardware available

17:37:06 <m-relay> <e​ndor00:matrix.org> If we assume that the attacker doesn't control any hashrate prior to
the attack, we can look at rental services such as Nicehash to see if there is enough available to match the
network - and if so, how much it will cost to keep up the attack for a certain length of time

17:38:48 <Rucknium> My preliminary conclusion: Monero's security budget is uncomfortably close to the
contemporary security budget of these coins with these historical PoW deep block reorgs. That suggests setting
the tx output lock at 10 blocks isn't an excessive safety margin. (But the 10 block lock doesn't protect
against double spend attacks based on block

17:38:48 <Rucknium> re-orgs.)

17:38:58 <m-relay> <e​ndor00:matrix.org> Or, alternatively, we can estimate how much it would cost to buy
enough mining rigs - but buying hardware quickly becomes a rather prohibitive upfront cost

17:40:24 <m-relay> <e​ndor00:matrix.org> Rucknium also showed me a few papers that calculate the probability
of reorging a small number (<10) of blocks, assuming the attacker has *less* than 51% of the nethash

17:41:29 <Rucknium> We can do the calculations for more than 10 blocks. Just have to apply the formula. The
papers have <10 blocks in tables that are nice to look at

17:42:17 <m-relay> <e​ndor00:matrix.org> i.e. what if a chain analysis company wanted to actively reorg a few
blocks to kick someone's tx off and force them to re-spend an output, potentially revealing their true spend?

17:43:09 <rbrunner> Interesting scenario, if a bit improbable, seems to me ...

17:43:22 <m-relay> <e​ndor00:matrix.org> And from there, calculate how much it would cost to perform such an
attack at different nethash levels

17:44:01 <Rucknium> rbrunner: IMHO, that's almost the only scenario that the 10 block lock protects users
from.

17:44:43 <Rucknium> Becuase "benign" re-orgs haven't been greater than 3 blocks deep. So there would have to
be a malicious incentive to cause a deeper re-org.

17:44:53 <rbrunner> Yeah, in the abstract. I meant the idea that out of all possible parties a chain analysis
company is doing that, for the stated reason of "demasking"

17:45:10 <m-relay> <e​ndor00:matrix.org> According to the papers, causing a reorg of a 1-3 of blocks is not
*that* unlikely, even for an entity with 10-20% of the nethash (which is available on Nicehash)

17:45:14 <rbrunner> Not with any direct financial gain in mind

17:45:36 <Rucknium> Maybe re-read the two MRL issues about the 10 block lock.

17:47:00 <m-relay> <e​ndor00:matrix.org> While attacking a specific tx/output is less likely, there's also the
option for a "dragnet" type attack where they just perform this as often as possible to cause as many reorg
events as possible and reduce the effective ringsize for other people down the line too

17:47:46 <rbrunner> I see

17:48:35 <m-relay> <e​ndor00:matrix.org> I don't have any hard numbers on that yet, but imo 10 blocks is a
reasonable number, and reducing that might get us significantly closer to the danger zone

17:48:39 <rbrunner> I was hoping that the trend goes toward "10 blocks look excessive", but that does not seem
to be the case

17:49:56 <m-relay> <e​ndor00:matrix.org> According to the papers, reorging blocks becomes exponentially harder
for every additional block - which means that the reverse is also true: the more we lower the limit, the more
exponentially easier it becomes to pull it off

17:50:27 <Rucknium> rbrunner: If you look at the minority hashpower share attack success probability tables,
you can see the argument for "10 blocks look excessive". But only because if you have enough hashpower share
to have a good chance at re-orging, e.g. 8 blocks, then you also have enough to have a good chance at re-
orging 10 blocks.

17:50:29 <m-relay> <e​ndor00:matrix.org> For reference:
https://moneroresearch.info/index.php?action=resource_RESOURCEVIEW_CORE&id=191&browserTabID=

17:50:32 <m-relay> <e​ndor00:matrix.org> https://arxiv.org/abs/1912.06412

17:52:34 <m-relay> <e​ndor00:matrix.org> (You can find the probability table on page 10 of the first paper)

17:53:04 <Rucknium> If you have 30% of hashpower, an attack will re-org 8 blocks with 10% probability. With
the same hashpower, you can re-org 10 blocks with 6.5% probability.

17:54:10 <Rucknium> If you have 10% hashpower, attack success probability is 0.007% and 0.001% for 8 and 10
blocks, respectively.

17:55:14 <m-relay> <e​ndor00:matrix.org> Current availability on Nicehash is ~0.16 GH/s for rx, which is ~7.2%
of the current nethash

17:55:15 <Rucknium> The relationship isn't truly exponential, but it is a concave function.

17:56:32 <Rucknium> It is...a regularized incomplete beta function.

17:56:39 <m-relay> <e​ndor00:matrix.org> Plus another 0.4-0.6 GH/s mining on ZEPH, of which some amount is
probably from NH (or at least, it was at the beginning when the coin launched)

17:56:50 <m-relay> <g​hostway:matrix.org> Why?

17:57:39 <Rucknium> The Rosenfeld (2014) paper doesn't have the regularized incomplete beta function. It has
an equivalent formula with a summation. Another paper has the regularized incomplete beta function.

17:58:06 <Rucknium> ghostway: Was that "why" meant for me?

17:58:27 <m-relay> <g​hostway:matrix.org> Yep

17:59:12 <Rucknium> Grunspan & Perez-Marco (2018). "Double spend races." provides the math proofs if you
really want to know why.

17:59:28 <m-relay> <e​ndor00:matrix.org> Should be in the second paper I linked

17:59:29 <m-relay> <g​hostway:matrix.org> Okay, Ill read that, thanks

17:59:30 <Rucknium> Satoshi was slightly wrong in his original analysis in the bitcoin white paper

17:59:43 <Rucknium> https://moneroresearch.info/index.php?action=resource_RESOURCEVIEW_CORE&id=192

18:01:33 <Rucknium> We also have to wonder if 9 months of 1 woman gestating is the same as 9 women gestating
for 1 month each.

18:02:21 <Rucknium> In other words, if an attacker can acquire 10% of the hashpower for 5 hours, can they also
acquire 50% of the hashpower for 1 hour.

18:02:35 <m-relay> <g​hostway:matrix.org> Thanks

18:02:56 <Rucknium> We've reached the end of the hour. Let's close the meeting.


```
Automated by [this](https://github.com/plowsof/post-libera-meeting-logs)

# Action History
- Created by: Rucknium | 2023-09-05T17:48:09+00:00
- Closed at: 2023-09-21T14:47:43+00:00
