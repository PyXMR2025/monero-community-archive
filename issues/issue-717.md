---
title: Monero Research Lab Meeting - Wed 06 July 2022
source_url: https://github.com/monero-project/meta/issues/717
author: Rucknium
assignees: []
labels: []
created_at: '2022-07-05T15:50:23+00:00'
updated_at: '2022-07-12T01:34:52+00:00'
type: issue
status: closed
closed_at: '2022-07-12T01:34:52+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

[Join the Monero Matrix server if you don't already have a Matrix account.](https://forum.monero.space/d/79-how-to-join-the-monero-core-team-matrix-server-web)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/converter.html?iso=20211027T170000&p1=1440)

Main discussion topics:

1. Greetings

2. Further analysis of July-Aug 2021 tx volume anomaly ( Isthmus / Mitchellpkt - see [these meeting logs](https://github.com/monero-project/meta/issues/621#issuecomment-948953655)) [Previous analysis](https://mitchellpkt.medium.com/fingerprinting-a-flood-forensic-statistical-analysis-of-the-mid-2021-monero-transaction-volume-a19cbf41ce60) with [Reddit discussion](https://www.reddit.com/r/Monero/comments/pvm634/fingerprinting_a_flood_forensic_statistical/)

3. Improvements to the decoy selection algorithm ( [Decoy Selection Algorithm - Areas to Improve](https://github.com/monero-project/research-lab/issues/86), [JBerman's weekly updates](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/249#note_11480), [Binning PoC](https://github.com/monero-project/research-lab/issues/88), [OSPEAD](https://ccs.getmonero.org/proposals/Rucknium-OSPEAD-Fortifying-Monero-Against-Statistical-Attack.html) ) @j-berman @Rucknium

4. Seraphis/Triptych/Lelantus Spark ( [UkoeHB's Seraphis Proof of Concept work](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/256), [Seraphis repo](https://github.com/UkoeHB/Seraphis), [Lelantus Spark](https://eprint.iacr.org/2021/1173) & [Tripych Multisig](https://github.com/cypherstack/triptych-multisig/blob/main/main.pdf) )

5. MRL META: "Cat herding", i.e. prioritization of research areas and features. Active recruitment of technical talent, MRL structure, funding (@Rucknium & others) [Reddit discussion](https://www.reddit.com/r/Monero/comments/pkg3d6/the_monero_project_should_actively_recruit/)

6. Any other business

7. Confirm next meeting agenda


Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: UkoeHB

Previous meeting agenda/logs:

#716 

# Discussion History
## UkoeHB | 2022-07-06T19:15:28+00:00
```
[07-06-2022 17:01:35] <UkoeHB> meeting time https://github.com/monero-project/meta/issues/717
[07-06-2022 17:01:35] <UkoeHB> 1. greetings
[07-06-2022 17:01:35] <UkoeHB> hello
[07-06-2022 17:01:53] <jberman[m]> hello
[07-06-2022 17:01:57] <ArticMine[m]> Hi
[07-06-2022 17:02:05] <dangerousfreedom> Hello
[07-06-2022 17:02:15] <rbrunner> Hello
[07-06-2022 17:02:19] <Rucknium[m]> Hi
[07-06-2022 17:03:37] <UkoeHB> 2. updates, what has everyone been working on?
[07-06-2022 17:04:47] <Rucknium[m]> I read cover-to-cover Yu, Au, and Esteves-Verissimo (2019) "Re-Thinking Untraceability in the CryptoNote-Style Blockchain"; Ronge et al. (2021) "Foundations of Ring Sampling"; and Egger et al. (2022) "On Defeating Graph Analysis of Anonymous Transactions".
[07-06-2022 17:05:05] <Rucknium[m]> We now have over 100 papers on MoneroResearch.info :)
[07-06-2022 17:06:35] <dangerousfreedom> I could finally code all the main crypto functions in Python to verify that there is no inflation happening :)
[07-06-2022 17:06:35] <dangerousfreedom> My code now works for all type of transactions. I just implemented one version of Bulletproofs as it works for verifying the transactions types 3,4 and 5. Maybe there are some optimizations to do on it and that's what I will be doing in the next two months. I will improve the algorithms, website (www.moneroinflation.com) and compare the performance with the C++ code. Now I believe I can say that I have an idea about what
[07-06-2022 17:06:35] <dangerousfreedom> is happening with Monero :)
[07-06-2022 17:07:26] <UkoeHB> me: I implemented a generator factory and switched the BP+ (new file: BP+2) and Grootle proofs to use it. Sharing proof generators improves verification batching slightly, and hopefully is a good investment for future batching needs/opportunities. I also evaluated implementing ristretto again, and again concluded it is too large an implementation/maintenance/cross-implementation support burden to dive into.
[07-06-2022 17:08:52] <moneromooo> dangerousfreedom: excellent work!
[07-06-2022 17:09:37] <rbrunner> BP+ almost around the corner to keep you busy :)
[07-06-2022 17:10:06] <dangerousfreedom> UkoeHB: Oh, really? I thought some people (Kayabanerve) said that Ristretto would be faster and more secure. It is not the case for Monero then?
[07-06-2022 17:11:09] <UkoeHB> not much faster, and only more robust not more secure (can get same security properties with careful design using plain ed25519(
[07-06-2022 17:11:32] <jberman[m]> looked deeper into pool pruning funkiness while reviewing 8076 and submitted 8415 to harden the pruning logic, looked into the deadlock of 8410 with not much luck yet unfortunately (putting it on the back-burner for now), and this one is fun: moving over to creating a new PR for 7760 to resolve merge conflicts + do a little style cleaning while I'm there (all credit still given perfect-daemon for the PR...)
[07-06-2022 17:12:06] <UkoeHB> there are maybe 20-40 lines of code that would be materially impacted by switching to ristretto, but like 2-4k lines of diff to switch probably
[07-06-2022 17:12:49] <rbrunner> Rucknium[m]: Did you encounter anything really suprising while on this reading streak?
[07-06-2022 17:13:55] <Rucknium[m]> I had skimmed some of those papers before, so nothing eye-popping. Yes, I'd like to discuss them if there are no other pressing matters.
[07-06-2022 17:14:05] <UkoeHB> sure we can move on
[07-06-2022 17:14:08] <UkoeHB> 3. discussion
[07-06-2022 17:14:59] <Rucknium[m]> Well, a small eye-pop. Egger et al. (2022)'s main result is based on two unproven conjectures. When I skimmed, I thought that it rested on on a fully-proven basis.
[07-06-2022 17:16:31] <UkoeHB> the unproven conjectures being?
[07-06-2022 17:17:46] <Rucknium[m]> Well, some bound on a probability. Basically, they say that there has not been enough attention paid to _finite_ graphs in the graph theory literature, so they make some conjectures and show that they hold with "reasonable" parameters.
[07-06-2022 17:18:42] <Rucknium[m]> Apparently there is plenty of graph theory on infinite graphs. But they base all results on a specific size of a "user" set. With Monero, the "user" set would be all output public keys
[07-06-2022 17:19:29] <Rucknium[m]> I also don't fully understand their definition of epsilon-security (Definition 3.4). If anyone is bored and wants a challenge, I invite them to figure out what it really means.
[07-06-2022 17:20:17] <Rucknium[m]> I can't figure out if it means probability of a _single_ deterministic de-anonymization, or some sort of average amount of reduction in the anonymity set of the "users".
[07-06-2022 17:20:51] <Rucknium[m]> Literally right now it reads as "probability of an algorithm". Probability that the algorithm does what, exactly?
[07-06-2022 17:21:15] <Rucknium[m]> But anyway, all three papers recommend a binning or partitioning decoy selection algorithms, with a single "bin". I was trying to understand their justification since I have some healthy skepticism of binning.
[07-06-2022 17:21:59] <Rucknium[m]> Ronge et al (2021) say that maybe a combined binning and mimicry DSA is a good idea, which is what Seraphis is doing at the moment. But they don't analyze that suggestion rigoriously.
[07-06-2022 17:22:18] <Rucknium[m]> The main practical problems with a single bin are:
[07-06-2022 17:23:12] <Rucknium[m]> 1) It would ossify the 10-block lock (or X-block lock) since users would have to wait for some M set of outputs to be confirmed on the blockchain, since the output set would be "partitioned"
[07-06-2022 17:24:04] <Rucknium[m]> 2) Targeted flooding or "black marble" attacks. If an adversary knew that a target user had broadcasted a tx at a specific time, then they could flood the mempool with theit=r own marked outputs at that specific time.
[07-06-2022 17:25:29] <Rucknium[m]> Mainly I think that these papers like partitioning since it is easy to analyze. Yu et al. (2019) says that determining the resistance of an arbitrary DSA to graph-based attacks is a `#P-complete` problem, which is believed to be even harder than a NP problem
[07-06-2022 17:26:45] <Rucknium[m]> Ronge et al. (2021) gives a lower bound of the privacy of a mimicking DSA. The bound is acceptable, I think. So mimicry is "fine".
[07-06-2022 17:26:51] <UkoeHB> yeah you always leak the timing of when your input was created with a single bin, seems like a no-go to me
[07-06-2022 17:27:41] <Rucknium[m]> Right. That, too. The papers sort of wave that away. Yu et al. (2019) explicitly says "assuming no timing info leaks any useful info". 
[07-06-2022 17:29:05] <Rucknium[m]> Egger et al. (2022) gives us a specific number for how many ring members would be needed to be secure against graph-based attacks (with a given number of outputs), but in the case that we were using a partitioning DSA.
[07-06-2022 17:29:08] <UkoeHB> it's not a viable assumption for a generic privacy solution
[07-06-2022 17:29:52] <UkoeHB> how many do they say?
[07-06-2022 17:29:53] <Rucknium[m]> 24 ring members I think. But of course that bound does not take into account EAE attack, for instance. So Seraphis should not stop at 24
[07-06-2022 17:31:04] <Rucknium[m]> The formula is on page 3, second column of https://moneroresearch.info/index.php?action=resource_RESOURCEVIEW_CORE&id=28
[07-06-2022 17:31:12] <Rucknium[m]> But that is based on two conjectures
[07-06-2022 17:31:55] <Rucknium[m]> Those conjectures are "probably true", IMHO. I do not have a lot of graph theory knowledge, though.
[07-06-2022 17:33:37] <UkoeHB> they say 'random directed graphs', but real graphs are not random (things like EAE, change output chains, repeat customers, etc.)
[07-06-2022 17:34:52] <Rucknium[m]> You can probably "squeeze" that away in their bounding by taking the DSA as sampling uniformly on the partitions.
[07-06-2022 17:35:20] <Rucknium[m]> They also usefully consider the anonymity reduction of flooding/black marble attacks.
[07-06-2022 17:36:04] <Rucknium[m]> They say (under their framework) that a beta proportion of black marbles will lead to a beta proportional reduction in anonimity.
[07-06-2022 17:36:34] <Rucknium[m]> So not exponential or multiplicative or anything, which is good.
[07-06-2022 17:37:02] <Rucknium[m]> Section 7.2 On Black Marble Attacks
[07-06-2022 17:38:33] <UkoeHB> hmm yeah that's useful context
[07-06-2022 17:40:01] <UkoeHB> ok, are there any other topics to cover during this meeting?
[07-06-2022 17:40:29] <Rucknium[m]> It would confirm some of our bak-of-the-envelope calculations on how severe flooding would have had to be in last year's flood incident to substantially reduce user privacy. That discussion also fed into the 11 -> 16 ring size hard fork change.
[07-06-2022 17:42:42] <dangerousfreedom> UkoeHB: Do you some good resources to understand Seraphis? Could you send me later?
[07-06-2022 17:43:08] <dangerousfreedom> know*
[07-06-2022 17:43:57] <UkoeHB> dangerousfreedom: there is mainly just the paper (a bit outdated) https://github.com/UkoeHB/Seraphis
[07-06-2022 17:44:48] <UkoeHB> at some point the monerokon video about balance recovery will come out (I hope), but the slides are here https://github.com/MoneroKon/meta/blob/main/slides/2022/talks.md
[07-06-2022 17:45:16] <UkoeHB> and of course the monerotopia video https://www.youtube.com/watch?v=XbMLK-aarKU
[07-06-2022 17:45:34] <dangerousfreedom> UkoeHB: This one I saw. Nice work!
[07-06-2022 17:46:30] <ArticMine[m]> So if l understand this correctly. Ballpark doubling the number of outputs via flooding would reduce the privacy by a factor of two 
[07-06-2022 17:49:02] <Rucknium[m]> ArticMine: Yes, if Monero were using their one-bin/partitioning DSA. How their results map onto Monero's actual DSA is not clear. My intuition tells me that the result probably holds approximately. In other words, these graph-based (i.e. chain reaction or "cascading") attacks probably would have a proportional impact with our current DSA.
[07-06-2022 17:53:39] <Rucknium[m]> The overall purpose of these three papers is to put a bound on the potency of graph-based attacks on Monero and similar protocols.
[07-06-2022 17:54:56] <ArticMine[m]> This can be very helpful in tuning the growth of the short term median over the long term median in the scaling formulas 
[07-06-2022 17:55:33] <ArticMine[m]> Especially with Seraphis 
[07-06-2022 17:55:59] <ArticMine[m]> And ring size of 64 or higher 
[07-06-2022 17:59:01] <Rucknium[m]> If anyone wants to see a recent empirical paper on the effectiveness of graph-baed attacks, see Vijayakumaran, S. 2021. Analysis of cryptonote transaction graphs using the dulmage-mendelsohn decomposition
[07-06-2022 17:59:12] <Rucknium[m]> https://moneroresearch.info/index.php?action=resource_RESOURCEVIEW_CORE&id=39
[07-06-2022 17:59:43] <Rucknium[m]> "For pre-RingCT outputs in Monero, the DM decomposition technique performs better than existing techniques. For RingCT outputs in Monero, the DM decomposition technique has the same performance as existing techniques, with only five out of approximately 29 million outputs being identified as spent. "
[07-06-2022 18:00:04] <Rucknium[m]> "To study the effect of hard forks on Monero RingCT output traceability, we used information from four Monero hard forks. The DM decomposition technique is able to trace only 62,809 out of approximately 26 million RingCT transaction rings. Our results are further evidence supporting the claim that Monero RingCT transactions are mostly immune to traceability attacks. "
[07-06-2022 18:01:05] <UkoeHB> that's the end of the meeting, thanks for attending everyone
[07-06-2022 18:01:28] <ArticMine[m]> Thanks 
[07-06-2022 18:01:32] <Rucknium[m]> If I understand things correctly, the DM decomposition is the most powerful known attack at this time, but those other three papers I mentioned are meant to put a bound on the potency of any graph-based attack, even attacks not yet discovered.
[07-06-2022 18:02:09] <rbrunner> Interesting approach
[07-06-2022 18:04:34] <dangerousfreedom> Thanks
```

# Action History
- Created by: Rucknium | 2022-07-05T15:50:23+00:00
- Closed at: 2022-07-12T01:34:52+00:00
