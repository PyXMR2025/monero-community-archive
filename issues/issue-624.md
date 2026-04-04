---
title: Monero Research Lab Meeting - Wed 3 November 2021 @ 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/624
author: Rucknium
assignees: []
labels: []
created_at: '2021-10-30T17:39:38+00:00'
updated_at: '2021-11-07T14:28:24+00:00'
type: issue
status: closed
closed_at: '2021-11-07T14:28:24+00:00'
---

# Original Description
**Note the new topic "Cat herding".**

Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/converter.html?iso=20211027T170000&p1=1440)

Main discussion topics:

1. Greetings

2. Further analysis of July-Aug 2021 tx volume anomaly ( Isthmus / Mitchellpkt - see [these meeting logs](https://github.com/monero-project/meta/issues/621#issuecomment-948953655)) [Previous analysis](https://mitchellpkt.medium.com/fingerprinting-a-flood-forensic-statistical-analysis-of-the-mid-2021-monero-transaction-volume-a19cbf41ce60) with [Reddit discussion](https://www.reddit.com/r/Monero/comments/pvm634/fingerprinting_a_flood_forensic_statistical/)

3. Improvements to the mixin selection algorithm ( [Decoy Selection Algorithm - Areas to Improve](https://github.com/monero-project/research-lab/issues/86), [JBerman's weekly updates](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/249#note_11480), [Binning PoC](https://github.com/monero-project/research-lab/issues/88)) @j-berman @Rucknium

4. [The Science of Blockchain Conference 2022 Jan 24-26](https://cbr.stanford.edu/sbc22/#cfp). Submission deadline: November 23, 2021 11:59pm PST

5. Seraphis/Triptych/Lelantus Spark ( [UkoeHB's Seraphis Proof of Concept work](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/256), [Seraphis repo](https://github.com/UkoeHB/Seraphis), [Lelantus Spark](https://eprint.iacr.org/2021/1173) & [Tripych Multisig](https://github.com/cypherstack/triptych-multisig/blob/main/main.pdf) )

6. Rucknium's OSPEAD discussion ([CCS proposal](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/255) , Reddit discussion [1](https://www.reddit.com/r/Monero/comments/py8ub3/ccs_proposal_ospead_fortifying_monero_against/) & [2](https://www.reddit.com/r/Monero/comments/pyopq0/the_mathematical_nonsense_of_a_possible/)

7. MRL META: "Cat herding", i.e. prioritization of research areas and features. Active recruitment of technical talent, MRL structure (@Rucknium & others) [Reddit discussion](https://www.reddit.com/r/Monero/comments/pkg3d6/the_monero_project_should_actively_recruit/)

8. Examine sample size and random seed matters in Monero's unit tests. IRC discussion: [monero-dev](https://libera.monerologs.net/monero-dev/20211018#c39593) , [monero-research-lab](https://libera.monerologs.net/monero-research-lab/20211018)

9. Multisig Drijvers attack mitigation [Technical note](https://github.com/UkoeHB/drijvers-multisig-tech-note) , [Haveno bounty](https://github.com/haveno-dex/haveno/issues/103)

10. Any other business

11. Confirm next meeting agenda


Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: UkoeHB

Previous meeting agenda/logs:

#622

# Discussion History
## UkoeHB | 2021-11-03T18:02:59+00:00
```
[11-03-2021 17:00:59] <UkoeHB> meeting time: https://github.com/monero-project/meta/issues/624
[11-03-2021 17:00:59] <UkoeHB> 1. greetings
[11-03-2021 17:00:59] <UkoeHB> hello
[11-03-2021 17:01:07] <ArticMine> Hi
[11-03-2021 17:01:22] <Rucknium[m]> Meeting time :)
[11-03-2021 17:01:24] <rbrunner> Hi there
[11-03-2021 17:01:47] <gingeropolous> hi
[11-03-2021 17:01:49] <SerHack> Hi
[11-03-2021 17:01:57] <carrington[m]> Howdy
[11-03-2021 17:03:12] <gingeropolous> .summon bridge
[11-03-2021 17:03:29] * gingeropolous kicks bridge
[11-03-2021 17:03:40] <jberman[m]> hello :)
[11-03-2021 17:03:52] <UkoeHB> 2. let's start with updates
[11-03-2021 17:04:22] <gingeropolous[m]> lets go relay
[11-03-2021 17:04:23] <one-horse-wagon[> Hello everyone.
[11-03-2021 17:04:23] <crypto_grampy[m]> heyo
[11-03-2021 17:04:24] <carrington[m]> Looks like the IRC to Matrix bridge is warming up
[11-03-2021 17:04:25] <one-horse-wagon[> Why am I seeing EtherCalc--MRL_spreadsheet imposed on top of matrix?
[11-03-2021 17:05:21] <one-horse-wagon[> It's gone.
[11-03-2021 17:05:22] <Rucknium[m]> one-horse-wagon: You can un-pin it with the "..."
[11-03-2021 17:05:37] <one-horse-wagon[> I did.  Thank you.
[11-03-2021 17:07:34] <Rucknium[m]> My updates: 1) I created an animated statistical Monero logo. It can be used for marketing research projects I suppose.
[11-03-2021 17:07:34] <Rucknium[m]> https://www.reddit.com/r/Monero/comments/qkhjta/monero_resistant_to_statistical_attack/
[11-03-2021 17:08:07] <Rucknium[m]> 2) Work on the decoy selection algorithm continues. The feedback process is ongoing.
[11-03-2021 17:08:53] <UkoeHB> Me: This week, I added two variants to my Seraphis PoC. I have decided not to do one other variant (using a modified grootle proof), since other perf tests showed it had no advantages over the variants I have right now (which use concise grootle). The Firo guys think the modified grootle can perform better, but I did my best to optimize it and couldn't improve it enough to justify using. I also don't really feel like implementing 
[11-03-2021 17:08:53] <UkoeHB> a PoC of lelantus-spark. It is probably ~equivalent to my `MockTxTypeConciseV1` (maybe +/- a few percentages in size/verification cost). So... that means my PoC is basically done for perf testing :). gingeropolous[m] I will be hitting you up to pump some numbers on your beefy machine.
[11-03-2021 17:08:56] <Rucknium[m]> 3) Working with gingeropolous on defining hardware requirements for a research computing server.
[11-03-2021 17:10:16] <jberman[m]> (1) I updated the binning algorithm PoC, it's ready for review. Refresher: there was a flaw in the originally proposed algo, and I modified the approach to use bins of a fixed block size, rather than a fixed number of outputs
[11-03-2021 17:10:31] <jberman[m]> (2) I've made solid progress on view tag support, tentatively want to say I may have it done much sooner than originally thought
[11-03-2021 17:11:55] <rbrunner> Strange how long we had such a gem like the view tag idea just gathering dust.
[11-03-2021 17:13:00] <gingeropolous> are there any implications for view tags once ringsize goes massive with seraphis?
[11-03-2021 17:13:12] <UkoeHB> no
[11-03-2021 17:13:18] <Rucknium[m]> rbrunner: That's why I put "cat herding" on the MRL meeting agenda for later.
[11-03-2021 17:13:19] <one-horse-wagon[> Rucknium.  Your logo is in the public domain for anyone to use?
[11-03-2021 17:13:55] <UkoeHB> gingeropolous: ringsize is for tx INPUTS, view scanning is for tx OUTPUTS
[11-03-2021 17:14:20] <gingeropolous> roight roight roight
[11-03-2021 17:14:28] <UkoeHB> rbrunner: all it takes is someone to implement; there hasn't been anyone willing/able to implement it until now I guess
[11-03-2021 17:14:53] <UkoeHB> personally, I didn't know C++ 1.5yrs ago
[11-03-2021 17:16:09] <Rucknium[m]> one-horse-wagon: My interpretation is that it is CC BY-SA 4.0 license since it is somewhat derived from the original Monero logo. The code to create it is MIT. See
[11-03-2021 17:16:09] <Rucknium[m]> https://github.com/Rucknium/misc-research/tree/main/Statistical-Monero-Logo
[11-03-2021 17:16:29] <rbrunner> Hmm, I think mixed in there is also a failure to recognize the importance. Not only "nobody around to implement".
[11-03-2021 17:16:40] <Rucknium[m]> one-horse-wagon: So, basically anyone is free to post it anywhere. Go post it!
[11-03-2021 17:17:17] <rbrunner> But anyway, nice to have it going now :)
[11-03-2021 17:17:17] <one-horse-wagon[> Very good.  Thank you.  
[11-03-2021 17:20:47] <UkoeHB> wfaressuissia: are you around to give an update on Drijvers mitigation? technically a -dev issue, but also if interest here
[11-03-2021 17:20:52] <UkoeHB> or*
[11-03-2021 17:20:54] <UkoeHB> of*
[11-03-2021 17:21:30] <wfaressuissia> it isn't ready yet, is it enough precision of update ?
[11-03-2021 17:22:03] <UkoeHB> lol thanks
[11-03-2021 17:23:01] <UkoeHB> 3. well we can do open discussion if anyone has anything
[11-03-2021 17:23:07] <UkoeHB> from agenda or otherwise
[11-03-2021 17:23:37] <Rucknium[m]> Decoy Selection:
[11-03-2021 17:23:40] <hyc> rbrunner: we can't solve everything right away, otherwise there'd be nothing to talk about... :P
[11-03-2021 17:23:56] <gingeropolous> good ol' decoy selection
[11-03-2021 17:25:15] <Rucknium[m]> ArticMine gave me great written feedback on OSPEAD. One thing he suggested was that the upcoming hard fork can be leveraged to investigate the properties of decoy selection in the wild. In other words, waiting until the hard fork will give us a discontinuity to work with since the ring size will suddenly increase 11-->16
[11-03-2021 17:25:43] <ArticMine> I completed my feedback to OSREAD
[11-03-2021 17:26:58] <Rucknium[m]> The status of OSPEAD right now is that I am continuing to receive feedback, but the next step is for me to give a modified plan to ArticMine based on his feedback. Then my CCS proposal may move forward shortly after. I still plan to soon release a version of my OSPEAD technical specification, i.e. "Document A", before my CCS goes to the Funding Required stage.
[11-03-2021 17:27:45] <Rucknium[m]> Any questions?
[11-03-2021 17:28:02] <wfaressuissia> What's the location of that feedback ?
[11-03-2021 17:29:11] <Rucknium[m]> The feedback from ArticMine was distributed to all those who have access to my HackerOne submission.
[11-03-2021 17:29:45] <carrington[m]> Roughly how many pages will Document A be?
[11-03-2021 17:29:56] <Rucknium[m]> That includes isthmus, jberman, luigi1111, moneromooo, sgp, binaryFate, and Syksy.
[11-03-2021 17:30:19] <Rucknium[m]> Right now Document A is about 13 pages. It will get longer.
[11-03-2021 17:30:20] <carrington[m]> (Because some people said the hackerone submission was very very long)
[11-03-2021 17:30:50] <Rucknium[m]> jberman suggested I add some things.
[11-03-2021 17:31:32] <Rucknium[m]> If readers don't want to slog through Document A, that's fine. It will be there for transparency purposes.
[11-03-2021 17:31:44] <Rucknium[m]> It's also quite technical.
[11-03-2021 17:32:04] <rbrunner> So there will be TL;DR :)
[11-03-2021 17:32:16] <carrington[m]> I am looking forward to digging into it! 🙂
[11-03-2021 17:32:29] <one-horse-wagon[> It would be nice to see Document A to get more specific details and have an idea of what is being discussed in Hackerone.
[11-03-2021 17:32:43] <Rucknium[m]> I mean, I will try to explain in simple terms the overall idea as well, but the purpose of writing Document A was specifically to give  a detailed description. 
[11-03-2021 17:34:15] <ArticMine> In summary I believe that the overall approach is feasible. I am waiting for Rucknium's modified plan
[11-03-2021 17:34:26] <wfaressuissia> hackerone submission replies are not encrypted and can be read by hackerone itself, right ?
[11-03-2021 17:34:40] <Rucknium[m]> Document A is basically an extension of my HackerOne submission. I said in my HackerOne submission "Here's a rough outline of what I plan to do" in about a page of text. Document A is a deep dive into what I meant.
[11-03-2021 17:35:48] <Rucknium[m]> wfaressuissia[m]: I think HackerOne is not end-to-end encrypted. Therefore, I did the encrypting myself, with the PGP keys of luigi1111 and moneromooo. Taking no chances.
[11-03-2021 17:36:22] <jberman[m]> TL;DR on my suggestion: use the real output data collected by Moser et al to fit a plausibly better distribution than the gamma distribution, using one of the multiple methods of fitting the distribution described in Document A
[11-03-2021 17:36:33] <Rucknium[m]> There are a few messages in H1 that are not e2ee encrypted, but they don't reveal much.
[11-03-2021 17:37:43] <Rucknium[m]> jberman: Yes, that's a good summary of your suggestion. Basically, a dry run to show how it would work.
[11-03-2021 17:38:03] <wfaressuissia> UkoeHB: What's the next step after complete seraphis_perf branch ?
[11-03-2021 17:39:32] <UkoeHB> wfaressuissia: I need to run the perf tests now. Then make nice plots, then add them to the paper, then update/finalize the paper with coinstudent2048[ 's hard work on security modeling.
[11-03-2021 17:40:07] <ArticMine> <jberman[m]> TL;DR on my suggestion: use the real output data collected by Moser et al to fit a plausibly better distribution than the gamma distribution, using one of the multiple methods of fitting the distribution described in Document A <--- This is a start, but I would not give up completely on the more recent data. My take on this is that It gets harder as we increase noise via ring size increases / binning.
[11-03-2021 17:41:43] <ArticMine> So there is still merit in the OSREAD approach in addition to increasing noise
[11-03-2021 17:41:59] <wfaressuissia> "... hard work security modelling" Are these definitions and related proofs public ?
[11-03-2021 17:42:29] <wfaressuissia> at least definitions of required theorems to prove protocol securiy
[11-03-2021 17:42:31] <wfaressuissia> s/securiy/security/
[11-03-2021 17:43:00] <UkoeHB> https://github.com/coinstudent2048/writeups https://raw.githubusercontent.com/coinstudent2048/writeups/main/seraphis.pdf
[11-03-2021 17:43:07] <Rucknium[m]> Doug Tuman asked me to speak about decoy selection issues on his podcast. For various reasons, I don't want to go on a podcast at this time. Is there someone who would like to talk about decoy selection? I have jberman, isthmus, and ArticMine in mind.
[11-03-2021 17:43:40] <jberman[m]> Agree ArticMine, I figured that start would give a bit more clarity to Document A
[11-03-2021 17:44:10] <ArticMine> I see increasing noise via ring size increase / binning as complimentary and not a replacement for OSREAD
[11-03-2021 17:45:10] <ArticMine> I would not mind doing a podcast. I can be tough while trying to keep the details secret
[11-03-2021 17:45:56] <ArticMine> My preference would be to do it after the next HF
[11-03-2021 17:47:02] <Rucknium[m]> ArticMine: "It" here meaning the podcast or OSPEAD, or something else?
[11-03-2021 17:47:36] <ArticMine> OSREAD / decoy selection
[11-03-2021 17:47:54] <one-horse-wagon[> I would suggest waiting on doing any podcasts until there is no reason to try and keep details secret.  
[11-03-2021 17:48:27] <one-horse-wagon[> There are many other things to talk about having to do with Monero.
[11-03-2021 17:48:34] <ArticMine> Which in my view is after the the next HF
[11-03-2021 17:49:28] <Rucknium[m]> ArticMine: I agree. I think it wouldn't be feasible to fully research and implement OSPEAD before the next hard fork, anyway. And with a HF, we have additional data we can use.
[11-03-2021 17:51:35] <Rucknium[m]> Upcoming is the Science of Blockchain Conference. Submission deadline is Nov 23:
[11-03-2021 17:51:35] <Rucknium[m]> https://cbr.stanford.edu/sbc22/#cfp
[11-03-2021 17:52:08] <Rucknium[m]> I think it could be feasible to submit our work on the mid-2021 transaction volume anomaly as a work-in-progress.
[11-03-2021 17:54:08] <UkoeHB> Do you have to attend in-person?
[11-03-2021 17:55:03] <Rucknium[m]> UkoeHB: I am unsure.
[11-03-2021 17:58:15] <Rucknium[m]> FYI: Just a few minutes ago isthmus wrote a long comment on my CCS proposal:
[11-03-2021 17:58:15] <Rucknium[m]> https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/255#note_12497
[11-03-2021 18:01:12] <UkoeHB> We are at the end of the hour. I will call it here. Thanks for attending everyone.
```

# Action History
- Created by: Rucknium | 2021-10-30T17:39:38+00:00
- Closed at: 2021-11-07T14:28:24+00:00
