---
title: Monero Research Lab Meeting - Wed 28 September 2022
source_url: https://github.com/monero-project/meta/issues/738
author: Rucknium
assignees: []
labels: []
created_at: '2022-09-26T21:40:33+00:00'
updated_at: '2022-10-04T16:13:01+00:00'
type: issue
status: closed
closed_at: '2022-10-04T16:13:01+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

[Join the Monero Matrix server if you don't already have a Matrix account.](https://forum.monero.space/d/79-how-to-join-the-monero-core-team-matrix-server-web)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/converter.html?iso=20211027T170000&p1=1440)

Main discussion topics:

1. Greetings

2. Improvements to the decoy selection algorithm ( [Decoy Selection Algorithm - Areas to Improve](https://github.com/monero-project/research-lab/issues/86), [Binning PoC](https://github.com/monero-project/research-lab/issues/88), [OSPEAD](https://ccs.getmonero.org/proposals/Rucknium-OSPEAD-Fortifying-Monero-Against-Statistical-Attack.html) ) @j-berman @Rucknium

3. Seraphis. ( [UkoeHB's Seraphis Proof of Concept work](https://ccs.getmonero.org/proposals/seraphis-wallet-poc-2.html), [Seraphis repo](https://github.com/UkoeHB/Seraphis) ).

4. MRL Meta: "Cat herding", i.e. prioritization of research areas and features. Active recruitment of technical talent, MRL structure, funding (@Rucknium & others) [MoneroResearch.info repository of Monero-related research papers](https://moneroresearch.info/), [Reddit discussion](https://www.reddit.com/r/Monero/comments/pkg3d6/the_monero_project_should_actively_recruit/)

5. Any other business

6. Confirm next meeting agenda


Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: UkoeHB

Previous meeting agenda/logs:

#736 

# Discussion History
## UkoeHB | 2022-09-28T17:52:34+00:00
`[09-28-2022 16:59:39] <one-horse-wagon[> Hello`
`[09-28-2022 17:00:13] <hyc> hi`
`[09-28-2022 17:00:23] <UkoeHB> meeting time`
`[09-28-2022 17:00:28] <Rucknium[m]> Hi`
`[09-28-2022 17:00:32] <UkoeHB> 1. greetings`
`[09-28-2022 17:00:32] <UkoeHB> hello`
`[09-28-2022 17:00:35] <ArticMine[m]> Hi`
`[09-28-2022 17:00:41] <rbrunner> Hello`
`[09-28-2022 17:00:47] <dangerousfreedom> Hello`
`[09-28-2022 17:00:58] <UkoeHB> https://github.com/monero-project/meta/issues/738`
`[09-28-2022 17:02:48] <UkoeHB> 2. updates, what has everyone been working on?`
`[09-28-2022 17:05:01] <dangerousfreedom> I started working on the SpendProof which will be based on the grootle proofs in Seraphis. Still going through all the code, debugging and building my understanding about it.`
`[09-28-2022 17:05:21] <Rucknium[m]> Delivered fully specified OSPEAD plan to ArticMine, isthmus, and hyc. Syksy will probably not review it due to time commitments. Public portion to be released probably next week (MAGIC donation system is not ready yet this week). `
`[09-28-2022 17:05:33] <hyc> I've been reviewing the above`
`[09-28-2022 17:06:23] <isthmus> Ditto, hoping to have my comments on Rucknium docs in the next 3 weeks`
`[09-28-2022 17:06:56] <UkoeHB> me: continued work on unit tests for spending legacy enotes in seraphis txs`
`[09-28-2022 17:07:21] <ArticMine[m]> Ditto. I am reviewing OSPEAD`
`[09-28-2022 17:07:27] <Rucknium[m]> Thank you, reviewers.`
`[09-28-2022 17:09:20] <UkoeHB> 3. discussion, any topics/questions/comments on anyone's mind?`
`[09-28-2022 17:11:40] <UkoeHB> in case no one saw it, a new proof system was introduced in a recent paper https://github.com/monero-project/research-lab/issues/107`
`[09-28-2022 17:11:51] <UkoeHB> in case anyone missed it*`
`[09-28-2022 17:12:17] <Rucknium[m]> The time line on OSPEAD, assuming there are no major snags, is to start doing the estimations in November, hopefully having the first draft of them ready in December. Note that this doesn't include an assessment of the risk of transaction non-uniformity when there are multiple wallet2 decoy selection algorithms being used due to slow user update.`
`[09-28-2022 17:13:23] <rbrunner> Any comments yet to that new proof system?`
`[09-28-2022 17:13:52] <dangerousfreedom> Rucknium: did you publish your paper about the OSPEAD ? I missed it last week`
`[09-28-2022 17:14:33] <hyc> limited release`
`[09-28-2022 17:15:13] <Rucknium[m]> Not yet. The plan is to publish a portion of it simultaneously with launching fundraiser for mj-xmr's C++ dev support of OSPEAD under the MAGIC Monero Fund.`
`[09-28-2022 17:16:03] <UkoeHB> rbrunner: not from me, would be nice to have some concrete benchmarks but that's not a trivial task`
`[09-28-2022 17:17:22] <rbrunner> Somebody asked about the ringsize planned for Seraphis on Reddit, and I wonder how the way looks to a decision regarding that. Does that wait until code allows some benchmarks?`
`[09-28-2022 17:17:42] <rbrunner> Or until we know exact transaction sizes in bytes for both variants, 64 versus 128=`
`[09-28-2022 17:18:10] <dangerousfreedom> Rucknium[m]: Ok.`
`[09-28-2022 17:19:35] <UkoeHB> rbrunner: based on my previous benchmarks, 128 ring size is about equivalent in performance to 16-ring size clsag`
`[09-28-2022 17:20:07] <UkoeHB> with BP++ efficiency/size improvements, it might be worth looking at 256 ring size (but I don't have an implementation to test right now)`
`[09-28-2022 17:20:28] <ArticMine> https://github.com/monero-project/research-lab/issues/91`
`[09-28-2022 17:20:48] <rbrunner> So transaction size is not much of a problem there?`
`[09-28-2022 17:21:02] <ArticMine> One can go up to 256 ring size without making changes to scaling / fees`
`[09-28-2022 17:21:52] <rbrunner> Interesting`
`[09-28-2022 17:22:38] <rbrunner> Trace that, Chainalysis :)`
`[09-28-2022 17:22:43] <Rucknium[m]> I'd doubt that a decision would be reached soon. Ring size is also linked to binning and decoy selection enforcement, which are areas that still need to be researched.`
`[09-28-2022 17:23:40] <rbrunner> Hmmm ... and anywhere there smaller could be better than bigger, regarding rings?`
`[09-28-2022 17:23:52] <Rucknium[m]> Not to mention alternative decoy selection algorithms as a potential source of transaction uniformity defects.`
`[09-28-2022 17:24:41] <UkoeHB> rbrunner: no I don't think so`
`[09-28-2022 17:25:40] <Rucknium[m]> rbrunner: Probably not, unless things are screwed up badly. For example, if many, many wallet devs run with many alternative DSAs, and the larger ring size makes it easier to determine which wallet constructed each tx.`
`[09-28-2022 17:26:56] <dangerousfreedom> Yeah, that should be a consensus too. But how to enforce that?`
`[09-28-2022 17:27:19] <rbrunner> I see. I hope we will succeed in building a good wallet for Seraphis, so people don't get itchy fingers to "improve" in the first place.`
`[09-28-2022 17:27:29] <dangerousfreedom> 'Proof of building the ring' somehow? :p`
`[09-28-2022 17:28:15] <Rucknium[m]> dangerousfreedom: Consensus enforcement is probably too strict. Could enforce at node tx relay level: https://github.com/monero-project/research-lab/issues/87`
`[09-28-2022 17:30:25] <dangerousfreedom> Rucknium[m]: I see. Yeah, nodes could have a consensus to run some checks if the ring decoys were built properly. The same as it could be done with canonical points/scalars.`
`[09-28-2022 17:30:27] <dangerousfreedom> Thanks`
`[09-28-2022 17:32:19] <moneromooo> That seems to be the worst of both words, no ? The reason not to add consensus ring distribution checks is performance (AFAIK). Doing this as a relay check only means you get the hit anyway, but still allow blocks with stuff that doesn't pass.`
`[09-28-2022 17:33:34] * isthmus agrees with mooo`
`[09-28-2022 17:34:20] <Rucknium[m]> With consensus it's harder to change later if needed. ArticMine did not like the idea of consensus enforcement. Let's see...`
`[09-28-2022 17:34:45] <ArticMine> ^^^`
`[09-28-2022 17:35:03] <UkoeHB> baking a big pile of heuristics into the protocol increases project dependency on the core team for future hard forks, which is a step in the wrong direction imo`
`[09-28-2022 17:35:25] <hyc> how is it any harder than the upgrade we just performed? 2 hardforks in a 24hr period to allow for migration`
`[09-28-2022 17:35:59] <rbrunner> I think the problem would more be too many hardforks, and in to short succession ...`
`[09-28-2022 17:36:10] <rbrunner> Not their "hardness"`
`[09-28-2022 17:36:15] <UkoeHB> the goal should be fewer hardforks`
`[09-28-2022 17:36:24] <ArticMine> There are many problems`
`[09-28-2022 17:36:32] <ArticMine> no just HF`
`[09-28-2022 17:37:58] <dangerousfreedom> Looks to me a matter of increasing the blockchain size or increasing the computation dependency. I would go for increasing the computations (as it wont destroy the blockchain if a bad transaction is accepted)`
`[09-28-2022 17:38:17] <Rucknium[m]> https://libera.monerologs.net/monero-research-lab/20211006#c36752`
`[09-28-2022 17:39:04] <Rucknium[m]> ^ Previous discussion on this topic`
`[09-28-2022 17:40:04] <isthmus> I hope we don't enforce the DSA because analyzing incorrectly constructed rings is like 2/3 of the fun over in Noncesense research, heh. And with bigger ring size, the fingerprints will become more statistically certain.`
`[09-28-2022 17:40:07] <isthmus> (joking, mostly)`
`[09-28-2022 17:40:14] <Rucknium[m]> I think it's not great if we have to tell people that they are really only safe if they use a wallet2-derived wallet`
`[09-28-2022 17:40:36] <hyc> fwiw it makes sense not to bake it in at consensus level, at least not yet.`
`[09-28-2022 17:41:02] <Rucknium[m]> isthmus: Chain analysis companies are thinking the same thing, probably. But they are not joking.`
`[09-28-2022 17:41:06] <hyc> since modeling true spend distribution is a continually moving target`
`[09-28-2022 17:43:01] <rbrunner> And think about the added complexity of consensus checks, for an uncertain amount of gains`
`[09-28-2022 17:43:31] <rbrunner> Complexity already jumps up greatly with Seraphis and Jamtis anyway.`
`[09-28-2022 17:43:39] <isthmus> small aside: "tell people that they are really only safe if they use a wallet2-derived wallet" --> I would make a subtle change but an important and practical one. "People are only safe if they use a wallet that produce transactions that match the reference spec (as implemented in wallet2)". Doesn't have to be wallet2-derived as long as it follows the correct behavior.`
`[09-28-2022 17:43:41] <hyc> meanwhile, I don't think we can avoid telling people they're only safe if they use wallet2, since fingerprinting is a liability otherwise`
`[09-28-2022 17:43:45] <Rucknium[m]> I think we can estimate the gains pretty well.`
`[09-28-2022 17:44:50] <Rucknium[m]> Seraphis is an opportunity to remove some fingerprintability. For example, the fee discretization should reduce the fee fingerprintability a lot.`
`[09-28-2022 17:44:58] <isthmus> <3`
`[09-28-2022 17:45:12] <isthmus> Damn there goes one of my weekend projects`
`[09-28-2022 17:46:47] <Rucknium[m]> Hopefully we put Noncense out of business eventually :P`
`[09-28-2022 17:48:09] <UkoeHB> any last-minute topics before we close out the meeting?`
`[09-28-2022 17:51:39] <UkoeHB> ok I'll call it here, thanks for attending everyone`

# Action History
- Created by: Rucknium | 2022-09-26T21:40:33+00:00
- Closed at: 2022-10-04T16:13:01+00:00
