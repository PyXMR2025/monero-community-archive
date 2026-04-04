---
title: Monero Research Lab Meeting - Wed 31 May 2023, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/844
author: Rucknium
assignees: []
labels: []
created_at: '2023-05-31T14:51:53+00:00'
updated_at: '2023-06-13T04:35:48+00:00'
type: issue
status: closed
closed_at: '2023-06-13T04:35:47+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

[Join the Monero Matrix server if you don't already have a Matrix account.](https://forum.monero.space/d/79-how-to-join-the-monero-core-team-matrix-server-web)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/converter.html?iso=20211027T170000&p1=1440)

Main discussion topics:

1. Greetings

2. Discuss: [Consider removing the tx_extra field](https://github.com/monero-project/monero/issues/6668).

3. Discuss: [Exploring Trustless zk-SNARKs for Monero's payment protocol](https://github.com/monero-project/research-lab/issues/100).

4. Improvements to the decoy selection algorithm ( [Decoy Selection Algorithm - Areas to Improve](https://github.com/monero-project/research-lab/issues/86), [Binning PoC](https://github.com/monero-project/research-lab/issues/88), [OSPEAD](https://ccs.getmonero.org/proposals/Rucknium-OSPEAD-Fortifying-Monero-Against-Statistical-Attack.html) ) @j-berman @Rucknium

5. Seraphis. ( [UkoeHB's Seraphis Proof of Concept work](https://ccs.getmonero.org/proposals/seraphis-wallet-poc-2.html), [Seraphis repo](https://github.com/UkoeHB/Seraphis) ).

6. MRL Meta: "Cat herding", i.e. prioritization of research areas and features. Active recruitment of technical talent, MRL structure, funding (@Rucknium & others) [MoneroResearch.info repository of Monero-related research papers](https://moneroresearch.info/), [Reddit discussion](https://www.reddit.com/r/Monero/comments/pkg3d6/the_monero_project_should_actively_recruit/)

7. Any other business

8. Confirm next meeting agenda


Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: UkoeHB

Previous meeting agenda/logs:

#841 

# Discussion History
## plowsof | 2023-05-31T18:55:51+00:00
Logs 
```
17:05:10 <Rucknium[m]> I will start: Meeting time!

17:05:23 <shalit[m]> Hello! how are you all doing?

17:05:24 <Rucknium[m]> "Agenda": https://github.com/monero-project/meta/issues/844

17:05:29 <Rucknium[m]> Hi

17:05:31 <rbrunner> Yeah, hello

17:07:10 <vtnerd> hi

17:07:22 <Rucknium[m]> Updates: what is everyone working on?

17:07:34 <jeffro256[m]> Howdy

17:08:43 <vtnerd> zerofconf in LWS (mainly), and some slow progress on bp++

17:08:52 <jeffro256[m]> I've been working on making PR https://github.com/monero-project/monero/pull/8815 more
efficient

17:08:57 <Rucknium[m]> I am running Monte Carlo tests on the OSPEAD estimator. Just 10 iterations at a time
for now. If anyone has opinions about what distributions I can test it with, suggest them. I mean some set of
decoy selection algorithms and real spend distributions.

17:08:58 <vtnerd> Im becoming more confident Ill be able to complete it, if only the requests for LWS die down

17:09:51 <shalit[m]> I'm still working on writing storeEnote to disk

17:10:31 <jeffro256[m]> Rucknium[m]: Have you looked into trying to obtain real user data to test
distributions against ?

17:11:21 <vtnerd> I imagine that would be fairly difficult

17:11:33 <Rucknium[m]> jeffro256: Like BTC and LTC, and BCH and DOGE?

17:11:43 <Rucknium[m]> Yes that's a good idea.

17:12:29 <jeffro256[m]> Just like people voluntarily opting into a survey where e.g. you have their viewkeys
and you ask them to just spend their XMR how they normally would

17:12:47 <jeffro256[m]> Also  yeah looking at BTC on-chain data could be interesting

17:13:05 <Rucknium[m]> The view key idea is too subject to selection bias IMHO

17:13:34 <jeffro256[m]> Probably true

17:14:05 <vtnerd> the paper that recommended the exponential distribution also looked at ring_size=0 in early
Monero for some help

17:14:20 <Rucknium[m]> I have the data for BTC, etc already. Look at section 8 (page 32) of the PDF linked
here: https://github.com/monero-project/research-lab/issues/93

17:14:20 <vtnerd> iirc the distribution was similar to BTC

17:15:27 <Rucknium[m]> What about decoy selection distributions? wallet2 (or a simplified version) of
course...but what else?

17:15:29 <jeffro256[m]> Another option is you could have people voluntarily show you their bank accounts and
you translate that somehow into how a UTXO based wallet would spend the funds. Still have the selection bias,
but there's generally more data to work with per person

17:15:34 <ghostway[m]> <Rucknium[m]> "I am running Monte Carlo tests..." <- Hello, late for the party, what do
you think on getting data from users? For ground truth. Maybe from other cryptocurrencies, if those are viable

17:15:56 <ghostway[m]> Oh, I see jeffro has already suggested that, lol

17:18:43 <UkoeHB> Sorry, forgot to say I’m not available for the meeting today.

17:18:58 <ghostway[m]> Is the bridge dead ...?

17:19:12 <vtnerd> ghostway[m]: no

17:19:37 <jeffro256[m]> <vtnerd> "the paper that recommended the..." <- Ring size=0? *shudders*

17:19:52 <vtnerd> yeah early Monero had no constraints on ring size

17:20:02 <rbrunner> Optionally yes

17:20:07 <vtnerd> so a bunch of people leaked the real spend early on

17:20:13 <jeffro256[m]> I faintly remember the debates about making the rings fixed size right as I was
getting into Monero

17:22:14 <Rucknium[m]> Devs out there is wallet land can help inform about those nonstandard decoy selection
algorithms.

17:23:00 <Rucknium[m]> I don't mean exact specifications (of course that would be very nice), but an idea of
the general shape of those distributions.

17:23:26 <jeffro256[m]> Speaking on nonstandard decoy selection algorithms, I just made a CCS proposal to
rewrite the reference decoy selection code

17:23:48 <jeffro256[m]> I think it's warranted in this code because the current decoy selection code is so
untestable

17:23:54 <jeffro256[m]> *in this case

17:25:01 <jeffro256[m]> Basically every meaningful decoy selection bug can be exposed in the testing phase by
looking at statistical anomalies. These big selection bugs were not caught because it's a PITA to write test
cases for methods baked into the monolithic wallet2

17:25:39 <jeffro256[m]> I want to know if anyone disagrees with me on this

17:25:54 <Rucknium[m]> It would be very nice to have someone who knows C++ to derive the specification-in-
practice of wallet2's DSA.

17:26:14 <Rucknium[m]> My other plan was for me to do it.

17:27:19 <Rucknium[m]> This is a critical piece of code. It needs close attention. For reference on how it's
critical for privacy, please see the quotes from several papers on the first page of that PDF I linked above

17:28:01 <vtnerd> jeffro256[m]: https://github.com/vtnerd/monero-lws/blob/master/src/util/random_outputs.cpp

17:28:19 <vtnerd> I recall doing _mostly_ what wallet2 did, but there may be some variance for older outputs

17:28:34 <Rucknium[m]> The paper that xmrack  posted (thanks) yesterday, which I would like to discuss, says
"Monero differs from our experiment mainly in two ways: 1) Their approximation on the source account
distribution is some Ŝ_t different from our S_t , which is a code-induced distribution that cannot be
expressed analytically...."

17:28:57 <Rucknium[m]> Even external researchers are "complaining" about wallet2.

17:29:40 <ghostway[m]> Rucknium[m]: https://github.com/monero-
project/monero/blob/master/src/wallet/wallet2.cpp#LL1014C1-L1061C3 is this it?

17:29:57 <jeffro256[m]> vtnerd: At a glance, this seems much much much better than get_outs, thanks for the
link

17:30:11 <jeffro256[m]> MyMonero also had the off-by-one bug, correct?

17:30:43 <vtnerd> correct - although they may have copied the implementation in lws

17:31:40 <Rucknium[m]> ghostway: I don't know if that's the exact lines. jeffro256 , could you comment?

17:32:18 <jeffro256[m]> Thanks just the gamma picker, which is used within decoy selection

17:32:47 <ghostway[m]> Oh I see, okay. What's the exact thing, do you have that on-hand?

17:33:50 <jeffro256[m]> Function get_outs() Lines 8165-8778

17:34:08 <ghostway[m]> Thanks

17:35:58 <jeffro256[m]> It also does RPC retrieval and caching of enote information, but all relevant logic is
in that function (besides the gamme picker itself)

17:37:39 <ghostway[m]> I can see that... Oof, 600 line function

17:38:13 <jeffro256[m]> Fr, it's bad

17:38:32 <jeffro256[m]> Hey @vtnerd, is line going to be changed soon? https://github.com/vtnerd/monero-
lws/blob/ba218f7b361ea61cc8061de1a34ac14b472bf497/src/util/gamma_picker.cpp#L79

17:39:02 <jeffro256[m]> Just skimming, but I think that logic keeps the 10-block-lock decoy selection bug
alivr

17:39:05 <jeffro256[m]> *alive

17:41:22 <vtnerd> jeffro256[m]: the release branch has the fix but master does not. I dont remember why at the
moment

17:43:04 <jeffro256[m]> The release branch of LWS?

17:43:11 <vtnerd> no sorry that is the fix

17:43:38 <vtnerd> the end iterator is not inclusive

17:45:05 <jeffro256[m]> Oh okay I see it

17:47:28 <Rucknium[m]> Thanks to xmrack for finding Chow, Egger, Lai, Ronge, & Woo (2023) "On Sustainable
Ring-based Anonymous Systems" https://eprint.iacr.org/2023/743.pdf , which was posted May 23.

17:47:44 <Rucknium[m]> This research group continues to produce interesting papers relevant to Monero.

17:47:59 <Rucknium[m]> I read the paper except for the appendix, cryptography-heavy parts (which I think are
just describing RingCT) and the section on an application to social media.

17:48:09 <Rucknium[m]> My comments:

17:48:20 <Rucknium[m]> 1) AFAIK, this is the first paper that discusses the possibility of "pruning of spent
outputs" in my list of Monero open research questions (MRL issue #94).

17:48:31 <Rucknium[m]> 2) Their "garbage collector" of spent outputs would require, in practice, a
partitioning decoy selection algorithm (DSA). That means each ring would be "one big bin". Each big would be a
contiguous set of outputs. The bins would be disjoint sets.

17:48:45 <Rucknium[m]> 3) The garbage collection procedure with partitioning DSA is very simple: You garbage
collect the whole bin if the number of transaction inputs that reference the bin equal the size of the bin.

17:48:57 <Rucknium[m]> 4) There is an alternative garbage collector for a mimicking decoy selection algorithm
(or another DSA that is not partitioning), which is what Monero has to tried to have. It's basically to run
the Dulmage-Mendelsohn Decomposition to see if any sets of outputs can be proven to be spent.

17:49:08 <Rucknium[m]> 5) This alternative does not collect much garbage at all (and maybe none) at Monero's
ring size and transaction volume. That's why they say Monero is "unsustainable". Monero can not really prune
outputs in its current form.

17:49:22 <Rucknium[m]> 6) My opinion: The partitioning DSA + Garbage collector is vulnerable to malicious
parties simply producing a single output in each bin and never spending them. Then the garbage can never be
collected and pruning does not happen after all. What do you think?

17:49:34 <Rucknium[m]> 7) Something that this paper made me realize is that if Monero has a partitioning DSA
then it would need to be required at the protocol level since otherwise nonstandard DSA could be pulling
decoys from "bags of black marbles" that are already provably spent.

17:49:45 <Rucknium[m]> 8) Disadvantages of a partitioning DSA are discussed here:
https://libera.monerologs.net/monero-research-lab/20220829#c142533

17:50:35 <ghostway[m]> I see on line 9894 it passes tx.selected_transfers, what a terrible name to also have a
m_transfers. What is even m_transfers? Don't tell me it's keeping a history of recent transactions.... That's
what it looks like in process_new_transaction, at least

17:55:17 <vtnerd> Ive never thought about a garbage collection system, but the requirement of it being "baked-
in" does seems likely

17:56:12 <Rucknium[m]> This Chow et al. (2023) paper...with a partitioning DSA, it at least gives the
possibility of pruning spent outputs in a ring signature system, which AFAIK would not be possible with global
membership proofs like trustless zk-SNARKS.

17:56:48 <ghostway[m]> <Rucknium[m]> "5) This alternative does not..." <- What about when seraphis rolls
around? And let's assume demand will rise

17:57:18 <jeffro256[m]> > On the negative side, we show empirically that Monero, one of the most popular
anonymous

17:57:18 <jeffro256[m]> cryptocurrencies, is unlikely to be sustainable without altering its current ring
sampling

17:57:18 <jeffro256[m]> strategy. The main subroutine is a sub-quadratic-time algorithm for detecting used
accounts

17:57:18 <jeffro256[m]> in a ring-based anonymous system.

17:57:32 <Rucknium[m]> Larger ring size and higher tx volume reduces opportunities for GC with a mimicking DSA

17:58:09 <jeffro256[m]> From a wobbly not-technical intuitive view, that quote makes it seem like the
randomness of Monero decoy selection would have to be degraded somewhat to acheive usable garbage collection
results

17:58:33 <Rucknium[m]> Check figures 11 and 12 (page 25) in the paper

17:58:36 <jeffro256[m]> Is that correct?

17:59:37 <Rucknium[m]> jeffro256: The "degradation" is one ring = one bin. Disjoint bins

18:00:18 <Rucknium[m]> But the partitioning DSA has certain privacy benefits (but some disadvantages). This
research group and others have theoretical results about that.

18:00:23 <Rucknium[m]> in other papers

18:01:09 <ghostway[m]> jeffro256[m]: > <@jeffro256:monero.social> > On the negative side, we show empirically
that Monero, one of the most popular anonymous... (full message at
<https://libera.ems.host/_matrix/media/v3/download/libera.chat/8e9735f245223af5e2a16f7f52d9dbf42f3effed>)

18:01:56 <ghostway[m]> Unless they also came up with an algorithm for that with another ring scheme

18:02:36 <Rucknium[m]> IMHO, one of the reasons this research group (and a few others) prefers partitioning
DSAs is that they don't see a way to discover a good mimicking DSA. There is a good way: OSPEAD

18:02:43 <jeffro256[m]> Is the benefit basically the point of binning in the first place? That if an observer
knows/thinks a transaction spends an output within a certain small timeframe, if you clumps the input ring
members around that time (as opposed to only having one from that time), then the observer doesn't learn as
much information about potential spends within that time period

18:03:09 <jeffro256[m]> On the other hand, if the external observer didn't already know a finer time period,
now they do...

18:04:16 <Rucknium[m]> jeffro256: Yes, that's the main privacy benefit. An adversary would know that it's one
of the outputs in that "bin" period, but would have no useful timing information to discover _which one of
those_. But the adversary would know the approximate time that the original output was produced. That would be
a problem for certain threat models.

18:05:55 <Rucknium[m]> An active adversary could also launch an active black ball attack where they pack the
bin of a targeted person's output with outputs produced by the adversary.

18:06:26 <Rucknium[m]> So the adversary sees the target's tx in the mempool and briefly floods the mempool
witt their txs

18:06:32 <ghostway[m]> Wouldnt that defeat the whole purpose of binning? Did they combat that in the paper?

18:07:10 <jeffro256[m]> The main problem I think with ONLY using binning is that people don't all transact
uniformly over days/weeks/years. Everyone naturally has cycles of activities, and having decoy selection
reveal the approximate time of the true spend can reveal a lot more information for people who don't
transaction within the cycle that the majority does, basically creating multiple anonymity puddles

18:07:43 <jeffro256[m]> That paper is incredibly interesting though

18:08:45 <Rucknium[m]> ghostway: See section 2.1.2 (Page 269) of
https://moneroresearch.info/index.php?action=resource_RESOURCEVIEW_CORE&id=19

18:08:57 <Rucknium[m]> Ronge, V., Egger, C., Lai, R. W. F., Schröder, D., & Yin, H. H. F. (2021). Foundations
of ring sampling.

18:09:08 <Rucknium[m]> They say it's a risk.

18:09:56 <ghostway[m]> Thanks

18:10:00 <Rucknium[m]> ^ This paper is referenced by the prune-outputs paper as the reasoning that the privacy
with a partitioning DSA is good.

18:11:56 <Rucknium[m]> They also say that a very good mimicking DSA is also good for privacy, but they don't
know how to estimate one.

18:12:46 <ghostway[m]> I guess that's when opseed comes in?

18:13:12 <Rucknium[m]> OSPEAD. Yes

18:14:57 <Rucknium[m]> "We emphasize that although Theorem 6.2 shows that the optimal anonymity is always
almost achievable up to a constant factor, the result is mostly of theoretical interest, because it requires
the knowledge of an estimation ˆS of the signer distribution S. Even if it is possible to obtain a reasonable
estimation ˆS of S, a questionable assumption, S may change over time, e.g., due...

18:15:08 <Rucknium[m]> "to economic bubbles and recessions, and depends on the free will of users. For a good
and practical sampler we recommend the partitioning sampler in Section 6.3."

18:15:24 <Rucknium[m]> ^ That's from Ronge et al. (2021)

18:16:29 <Rucknium[m]> Let's end the meeting here. Thanks for attending. Discussion about DSAs can continue,
obviously.


```
Automated by [this](https://github.com/plowsof/post-libera-meeting-logs)

# Action History
- Created by: Rucknium | 2023-05-31T14:51:53+00:00
- Closed at: 2023-06-13T04:35:47+00:00
