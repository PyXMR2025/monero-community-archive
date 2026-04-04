---
title: Monero Research Lab Meeting - Wed 13 July 2022
source_url: https://github.com/monero-project/meta/issues/719
author: Rucknium
assignees: []
labels: []
created_at: '2022-07-12T01:34:45+00:00'
updated_at: '2022-07-18T16:35:17+00:00'
type: issue
status: closed
closed_at: '2022-07-18T16:35:17+00:00'
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

#717 

# Discussion History
## UkoeHB | 2022-07-13T18:07:21+00:00
```
[07-13-2022 16:59:38] <UkoeHB> meeting time https://github.com/monero-project/meta/issues/719
[07-13-2022 16:59:38] <UkoeHB> 1. greetings
[07-13-2022 16:59:38] <UkoeHB> hello
[07-13-2022 16:59:57] <Rucknium[m]> Hi
[07-13-2022 17:00:03] <rbrunner> Hello
[07-13-2022 17:00:56] <dangerousfreedom> Hello
[07-13-2022 17:03:43] <kayabanerve[m]> Hello
[07-13-2022 17:04:47] <UkoeHB> 2. updates, what is everyone working on?
[07-13-2022 17:04:50] <jberman[m]> Won’t be 100% available this meeting unfortunately, but update: submitted perfect-daemon’s PR 7760 socket connection fixes with merge conflicts resolved + some style changes more in line with the rest of the repo (see PR 8426), submitted a patch for zmq to publish txs submitted to the daemon (PR 8427), and updated openmonero for the hf
[07-13-2022 17:05:48] <Rucknium[m]> Mostly doing OSPEAD work. 
[07-13-2022 17:07:16] <dangerousfreedom> I'm benchmarking my python code with the c++ code. Thank you for the detailed review on the website UkoeHB !
[07-13-2022 17:07:23] <kayabanerve[m]> I published my new address specification, featured addresses
[07-13-2022 17:07:41] <kayabanerve[m]> https://gist.github.com/kayabaNerve/01c50bbc35441e0bbdcee63a9d823789
[07-13-2022 17:08:30] <kayabanerve[m]> It's more dev, but I wanted to comment on it as it does remove the burning bug under one variant
[07-13-2022 17:08:45] <dangerousfreedom> I think I will implement bp in rust too by the end of this month or next one. It will be useful to build my skills and I think it may be useful for kayabanerve too
[07-13-2022 17:09:11] <ArticMine[m]> Hi
[07-13-2022 17:09:29] <UkoeHB> me: started work on the last big project on my end for seraphis poc -> integrating legacy cryptonote outputs into the main transaction type so they can be spent alongside normal seraphis enotes (instead of two tx types there will be just one, and the cryptonote inputs will be selected from the full range 2014-202x so if/when seraphis goes live there will be ONLY two tx types being created [main tx and coinbase])
[07-13-2022 17:11:06] <Rucknium[m]> UkoeHB: But the fact that an input is an old cryptonote output would be apparent to observers of the blockchain, correct? Can't mix two output types in the same ring, right?
[07-13-2022 17:11:13] <UkoeHB> correct
[07-13-2022 17:11:23] <UkoeHB> there would be seraphis inputs and legacy inputs
[07-13-2022 17:12:06] <rbrunner> That will go all the way back to outputs from 2014?
[07-13-2022 17:12:28] <UkoeHB> yes, you can use the technique that's currently used with coinbase outputs to spend the cleartext amount outputs
[07-13-2022 17:12:49] <UkoeHB> https://github.com/monero-project/research-lab/issues/59
[07-13-2022 17:13:13] <rbrunner> Reassuring
[07-13-2022 17:15:05] <Rucknium[m]> The MAGIC Monero Fund is considering targeted outreach to external researchers to apply for research grants. If you have any in mind, let us know. We would be targeting people who could make a practical contribution to the protocol.
[07-13-2022 17:15:23] <UkoeHB> 3. discussion, we can move on from updates :)
[07-13-2022 17:15:54] <rbrunner> I was wondering where BP++ stand, not in connection to Monero, but in general as a new cryptographical/mathematical construct. It that "trustworthy" already, or does that need audits / reviews?
[07-13-2022 17:16:30] <Rucknium[m]> AFAIK, BP++ is not peer reviewed yet and was written by a single person.
[07-13-2022 17:17:00] <rbrunner> Ah, yes, "peer review" was the word I was looking for
[07-13-2022 17:17:04] <UkoeHB> Rucknium[m]: the main research areas it would be nice to have are in zk circuits for 5th-gen membership proofs and in formalizing current ad hoc algorithms (and adding security modeling/proofs)
[07-13-2022 17:17:08] <Rucknium[m]> https://moneroresearch.info/index.php?action=resource_RESOURCEVIEW_CORE&id=83
[07-13-2022 17:19:19] <rbrunner> So I get no mad rush yet to implement them
[07-13-2022 17:19:55] <Rucknium[m]> Maybe coming up with a list of Monero's algorithms and dividing them into formalized and not-yet-formalized would be a good first step.
[07-13-2022 17:20:24] <Rucknium[m]> So that researchers would have a good idea about where to look for improvements
[07-13-2022 17:24:37] <Rucknium[m]> One of the questions in my mind for "zk circuits for 5th-gen membership proofs" is the assumptions that we would like to rely on. For example, Zcash's protocol has newer and less-tested assumptions. Ideally we would want researchers to develop membership proofs with global anonymity sets that rely only on old battle-tested cryptographic assumptions, correct?
[07-13-2022 17:24:45] <UkoeHB> Today I want to explain/discuss some of the next steps for seraphis after I am done with my stuff.
[07-13-2022 17:24:45] <UkoeHB> My remaining todo: integrate cryptonote inputs (possibly including a new default output scanning workflow for legacy outputs), add coinbase tx type.
[07-13-2022 17:24:45] <UkoeHB> Todos after that (not me): investigate/implement the wallet-side features of Jamtis (RIDs, Polyseed, address authentication), build wallets that use the seraphis library interface for building/handling txs and enotes (full wallet, view-only wallet, multisig full wallet, payment validator), integrate seraphis into the daemon/ledger, ... idk what else.
[07-13-2022 17:25:17] <Rucknium[m]> I don't want to instigate cutting-edge research that will be "too" cutting-edge for us to use.
[07-13-2022 17:25:18] <UkoeHB> Rucknium[m]: yes the more robust the better (no trusted setup is a requirement)
[07-13-2022 17:26:40] <UkoeHB> jberman[m]: has said he wants to work on seraphis/jamtis next steps, it would be nice if anyone else interested could start raising their hands (and start looking at the code to get an understanding how it works)
[07-13-2022 17:27:11] <Rucknium[m]> How do we get the cryptography in Seraphis to be peer-reviewed?
[07-13-2022 17:27:41] <rbrunner> "anyone else interested could start raising their hands" Well, here :) Just not yet sure when, how and how much.
[07-13-2022 17:28:01] <UkoeHB> well that is a non-implementation todo of mine -> update the paper more and try to get more cryptographer eyes/contributions on it
[07-13-2022 17:30:19] <dangerousfreedom> rbrunner: I'm definitely interested in contributing for real. I'm just not finished yet on building my skills and understanding. In two months I believe I will be able to start contributing.
[07-13-2022 17:30:24] <UkoeHB> I guess I didn't make a public statement about my CCS: I won't actually make a wallet proof-of-concept, since designing the API and internal caches isn't really my domain. The remaining time of my CCS will be spent finishing the core library.
[07-13-2022 17:31:10] <rbrunner> dangerousfreedom: Sounds good.
[07-13-2022 17:31:27] <UkoeHB> I basically way underestimated how much work was necessary to reach the point of 'write a wallet'.
[07-13-2022 17:32:14] <rbrunner> I think implementation can start before we have more review / feedback for Seraphis and Jamtis themselves. Only requirement, bascically, that they don't "explode" compeletely
[07-13-2022 17:32:38] <rbrunner> I mean turn out to have some un-fixable hole somewhere
[07-13-2022 17:32:51] <UkoeHB> if they explode, that implies lelantus spark will probably explode as well
[07-13-2022 17:33:29] <Rucknium[m]> Speaking of future plans, after OSPEAD I am thinking about researching churning best practices. From reading old GitHub issues, it seems Surae and knacc both made attempts, but did not complete the research.
[07-13-2022 17:33:55] <Rucknium[m]> OSPEAD won't be the final word in research on decoy selection, of course.
[07-13-2022 17:36:35] <kayabanerve[m]> UkoeHB: are we using the existing hash_to_curve or elligator2 or...?
[07-13-2022 17:38:31] <UkoeHB> kayabanerve[m]: seraphis does not use hash to point except for making generators (which uses the cryptonote hash to point function)
[07-13-2022 17:39:05] <kayabanerve[m]> Got it, sorry 
[07-13-2022 17:40:52] <UkoeHB> are there any questions/comments/other topics to discuss?
[07-13-2022 17:43:10] <wernervasquez[m]> Where are the most up to date and complete specifications for jamtis and seraphis?
[07-13-2022 17:44:34] <UkoeHB> wernervasquez[m]: aside from https://github.com/UkoeHB/monero/tree/seraphis_lib there are
[07-13-2022 17:44:34] <UkoeHB> https://raw.githubusercontent.com/MoneroKon/meta/main/slides/2022/Seraphis%20Balance%20Recovery.pdf
[07-13-2022 17:44:34] <UkoeHB> https://gist.github.com/tevador/50160d160d24cfc6c52ae02eb3d17024
[07-13-2022 17:44:34] <UkoeHB> https://github.com/UkoeHB/Seraphis
[07-13-2022 17:44:50] <UkoeHB> the monerokon slides are 100% up to date
[07-13-2022 17:46:09] <wernervasquez[m]> Thanks. I have some time coming up to put more work in on my library. Want to make sure my footing is sure.
[07-13-2022 17:47:11] <jberman[m]> @UkoeHB: thoughts on getting the poc audited and paper reviewed (once both complete), by e.g. veorq? Perhaps we can start opening discussion
[07-13-2022 17:47:29] <UkoeHB> no thoughts other than 'good idea'
[07-13-2022 17:48:20] <r4v3r23[m]> has polyseed been look at? tevador says its production ready
[07-13-2022 17:48:28] <UkoeHB> not by me
[07-13-2022 17:48:38] <UkoeHB> there were some concerns raised that 16 words isn't enough entropy
[07-13-2022 17:49:41] <hyc> it's only 128 bits yeah? and current seed is 256 bits
[07-13-2022 17:49:52] <rbrunner> tobtoht implemented it already in Feather
[07-13-2022 17:50:01] <kayabanerve[m]> If it's at least 128 bits...
[07-13-2022 17:50:03] <kayabanerve[m]> *128 bits of security, that is.
[07-13-2022 17:50:25] <rbrunner> They released a few days ago.
[07-13-2022 17:52:48] <rbrunner> Yeah, we go from one possible wallet for each and every atom in the universe to one wallet per molecule or so ...
[07-13-2022 17:53:16] <rbrunner> Or maybe grain of sand :)
[07-13-2022 17:57:05] <UkoeHB> Ok I think that's the end of the meeting. Thanks for attending everyone
[07-13-2022 17:57:41] <dangerousfreedom> Thank you for your work Koe!
[07-13-2022 17:57:51] <rbrunner> +1
[07-13-2022 17:58:44] <kayabanerve[m]> Bye everyone!
```

# Action History
- Created by: Rucknium | 2022-07-12T01:34:45+00:00
- Closed at: 2022-07-18T16:35:17+00:00
