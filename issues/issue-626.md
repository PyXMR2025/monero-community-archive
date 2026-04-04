---
title: Monero Research Lab Meeting - Wed 10 November 2021 @ 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/626
author: Rucknium
assignees: []
labels: []
created_at: '2021-11-07T14:28:14+00:00'
updated_at: '2021-11-16T06:21:52+00:00'
type: issue
status: closed
closed_at: '2021-11-16T06:21:52+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/converter.html?iso=20211027T170000&p1=1440)

Main discussion topics:

1. Greetings

2. "Seeing a bug in Aeon transactions where multiple inputs in one transaction use the same output. " https://github.com/monero-project/monero/pull/8047

3. Cryptographic performance benchmarks https://github.com/Rucknium/misc-research/tree/main/Monero-Cryptography-Benchmarks

4. Further analysis of July-Aug 2021 tx volume anomaly ( Isthmus / Mitchellpkt - see [these meeting logs](https://github.com/monero-project/meta/issues/621#issuecomment-948953655)) [Previous analysis](https://mitchellpkt.medium.com/fingerprinting-a-flood-forensic-statistical-analysis-of-the-mid-2021-monero-transaction-volume-a19cbf41ce60) with [Reddit discussion](https://www.reddit.com/r/Monero/comments/pvm634/fingerprinting_a_flood_forensic_statistical/)

5. Improvements to the mixin selection algorithm ( [Decoy Selection Algorithm - Areas to Improve](https://github.com/monero-project/research-lab/issues/86), [JBerman's weekly updates](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/249#note_11480), [Binning PoC](https://github.com/monero-project/research-lab/issues/88)) @j-berman @Rucknium

6. [The Science of Blockchain Conference 2022 Jan 24-26](https://cbr.stanford.edu/sbc22/#cfp). Submission deadline: November 23, 2021 11:59pm PST

7. Seraphis/Triptych/Lelantus Spark ( [UkoeHB's Seraphis Proof of Concept work](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/256), [Seraphis repo](https://github.com/UkoeHB/Seraphis), [Lelantus Spark](https://eprint.iacr.org/2021/1173) & [Tripych Multisig](https://github.com/cypherstack/triptych-multisig/blob/main/main.pdf) )

8. Rucknium's OSPEAD discussion ([CCS proposal](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/255) , Reddit discussion [1](https://www.reddit.com/r/Monero/comments/py8ub3/ccs_proposal_ospead_fortifying_monero_against/) & [2](https://www.reddit.com/r/Monero/comments/pyopq0/the_mathematical_nonsense_of_a_possible/)

9. MRL META: "Cat herding", i.e. prioritization of research areas and features. Active recruitment of technical talent, MRL structure, funding (@Rucknium & others) [Reddit discussion](https://www.reddit.com/r/Monero/comments/pkg3d6/the_monero_project_should_actively_recruit/)

10. Examine sample size and random seed matters in Monero's unit tests. IRC discussion: [monero-dev](https://libera.monerologs.net/monero-dev/20211018#c39593) , [monero-research-lab](https://libera.monerologs.net/monero-research-lab/20211018)

11. Multisig Drijvers attack mitigation [Technical note](https://github.com/UkoeHB/drijvers-multisig-tech-note) , [Haveno bounty](https://github.com/haveno-dex/haveno/issues/103)

12. Any other business

13. Confirm next meeting agenda


Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: UkoeHB

Previous meeting agenda/logs:

#624

# Discussion History
## UkoeHB | 2021-11-10T18:02:12+00:00
```
[11-10-2021 17:02:04] <UkoeHB> meeting time: https://github.com/monero-project/meta/issues/626 (for those who time changed, now 1700UTC comes an hour earlier)
[11-10-2021 17:02:12] <UkoeHB> 1. greetings
[11-10-2021 17:02:12] <UkoeHB> hello
[11-10-2021 17:02:30] <carrington[m]> Hi!
[11-10-2021 17:02:39] <Rucknium[m]> Hi
[11-10-2021 17:02:44] <rbrunner> Hello
[11-10-2021 17:02:53] <wfaressuissia1> Hello
[11-10-2021 17:02:57] <ArticMine> Hi
[11-10-2021 17:04:31] <UkoeHB> 2. let's start with updates; what has everyone been working on lately?
[11-10-2021 17:05:40] <UkoeHB> Me: I completed my Seraphis PoC for performance testing, and started collecting test results (thanks to gingeropolous for his help :)). While doing that, I discovered a rare bug (https://github.com/monero-project/monero/pull/8052).
[11-10-2021 17:07:30] <Rucknium[m]> Analysis of UkoeHB 's cryptography performance benchmarks. Finished final version of OSPEAD CCS proposal. Gave initial thoughts on the "decoy collision" issue raised by an Aeon dev. Brainstorming about research-specific funding mechanism. BCH work.
[11-10-2021 17:10:00] <UkoeHB> If no one else has updates, we can move on. We might be missing people due to the time change.
[11-10-2021 17:10:00] <UkoeHB> 3. discussion; anyone want to discuss something from the agenda?
[11-10-2021 17:10:55] <carrington[m]> Myself and spirobel  are in early discussions of putting together a hub for monero-related research
[11-10-2021 17:11:43] <carrington[m]> Paper summaries, categorizations, RSS feeds etc. Etc.
[11-10-2021 17:11:46] <Rucknium[m]> Oh, right! I wanted to discuss that. We should make a bounty and think about what the requirements should be.
[11-10-2021 17:11:51] <wfaressuissia1> "a hub for ... research" what does it mean ?
[11-10-2021 17:12:24] <Rucknium[m]> Tentative name: "Where to Find Monero Research: moneroresearch.wtf" I bought the domain name.
[11-10-2021 17:13:19] <Rucknium[m]> wfaressuissia[m]: The number of papers on Monero being published by external researchers has skyrocketed. We are not keeping up with reading them.
[11-10-2021 17:13:40] <carrington[m]> wfaressuissia[m]  there are many academic papers published about XMR and XMR-related topics which are basically being ignored by the visible community
[11-10-2021 17:13:51] <Rucknium[m]> Moser et al. (2018) alone now has over 80 citations.
[11-10-2021 17:14:47] <wfaressuissia1> citations don't mean that paper is the main reference
[11-10-2021 17:15:51] <carrington[m]> Anyways, this is very early stages so not much more to say there
[11-10-2021 17:16:02] <Rucknium[m]> wfaressuissia[m]: We don't even know that since we haven't read the papers. That's part of the problem.
[11-10-2021 17:16:03] <UkoeHB> thanks carrington[m] 
[11-10-2021 17:16:18] <carrington[m]> If anyone is hiding away their own private infodump of papers and relevant research please sling it my way
[11-10-2021 17:17:21] <Rucknium[m]> I think it would be good to have a portal that automatically pulls papers and their essential data (authors, title, abstract, etc.) based on keyword search and/or when key papers are cited. And maybe even allows a permissioned login system to make brief notes about the paper.
[11-10-2021 17:17:46] <Rucknium[m]> carrington: Will do.
[11-10-2021 17:17:58] <atomfried[m]> Rucknium[m]: like google schoolar?
[11-10-2021 17:18:40] <Rucknium[m]> Google scholar API could help, yes. There are other systems, too, that could be pulled from.
[11-10-2021 17:20:06] <carrington[m]> I'd be looking to write an abstract-style "how this relates to Monero" for those papers where the connection isn't obvious
[11-10-2021 17:20:37] <carrington[m]> Anyways, regarding actual research, is there anything we can say about these performance numbers at this stage?
[11-10-2021 17:21:26] <Rucknium[m]> UkoeHB has just generated new performance data. Is it ready for me to analyze, or still tweaking, UkoeHB ?
[11-10-2021 17:21:40] <UkoeHB> It is ready; this time in csv format too :p
[11-10-2021 17:22:28] <Rucknium[m]> Nice :) Although all my parsing code is now useless I suppose. A negligible sunk cost.
[11-10-2021 17:22:36] <wfaressuissia1> It would be more useful to have list of search engines (ideally working via tor too) for papers where anyone can get results for any keyword (not only monero)
[11-10-2021 17:23:06] <rbrunner> Do number already allow to speculate about the final overall speed of "Monero on Seraphis"? Will it sync the blockchain slower? Much slower? Faster? Will wallets scan faster? Etc.
[11-10-2021 17:23:10] <Rucknium[m]> Good thing I ran into parsing issues or it may have taken more time to realize that bug exists.
[11-10-2021 17:23:54] <rbrunner> *numbers
[11-10-2021 17:23:56] <UkoeHB> hah yeah 1 in 600k cases...
[11-10-2021 17:24:28] <UkoeHB> rbrunner: it should allow relative comparisons of blockchain sync times with different parameters
[11-10-2021 17:24:34] <Rucknium[m]> wfaressuissia[m]: I would prefer a shared repository for the papers, or the abstracts of the papers at least.
[11-10-2021 17:24:43] <UkoeHB> Wallet scanning is a separate issue
[11-10-2021 17:25:35] <rbrunner> I see. But maybe the speed comparison with Monero as it is now will fall out of this as a by-product? Maybe not.
[11-10-2021 17:26:02] <UkoeHB> Yes it should allow comparisons with current Monero
[11-10-2021 17:26:12] <UkoeHB> Since I collected results for CLSAG
[11-10-2021 17:26:26] <rbrunner> Ah, interesting.
[11-10-2021 17:26:51] <UkoeHB> CLSAG after BP+ and ring size 16*
[11-10-2021 17:27:00] <ArticMine> This is very interesting. Link?
[11-10-2021 17:27:04] <rbrunner> So it might show soon which the direction things will take.
[11-10-2021 17:27:16] <ArticMine> ... and useful
[11-10-2021 17:27:31] <UkoeHB> ArticMine: https://github.com/Rucknium/misc-research/tree/main/Monero-Cryptography-Benchmarks I think Rucknium[m] will upload the latest data at some point.
[11-10-2021 17:27:41] <Rucknium[m]> ArticMine: Old (pre-bugfix) data is here: https://github.com/Rucknium/misc-research/tree/main/Monero-Cryptography-Benchmarks
[11-10-2021 17:28:26] <rbrunner> Bleeding edge research :) Even the stats have bugs ...
[11-10-2021 17:28:42] <UkoeHB>  rbrunner Monero code had bugs, not the stats :p
[11-10-2021 17:28:55] <UkoeHB> This one: https://github.com/monero-project/monero/pull/8052
[11-10-2021 17:29:16] <rbrunner> That was enough to affect outcome? Surprising.
[11-10-2021 17:29:26] <Rucknium[m]> The issue was that extremely rarely the verification would fail, so the results would not be output. And the failure mode made parsing difficult
[11-10-2021 17:29:27] <ArticMine> Thanks
[11-10-2021 17:33:10] <Rucknium[m]> How about: "Seeing a bug in Aeon transactions where multiple inputs in one transaction use the same output. " https://github.com/monero-project/monero/pull/8047
[11-10-2021 17:34:01] <Rucknium[m]> It's not really a bug. It's just how things work now. The question is whether there are any costs or benefits to trying to avoid these "collisions".
[11-10-2021 17:34:17] <carrington[m]> This seems to be a consequence of small rings, but the privacy hit is not as big as the fact that the rings are small anyways
[11-10-2021 17:34:59] <Rucknium[m]> The collisions would seem to happen much more often on Aeon rather than Monero since Aeon has much fewer transactions and therefore fewer outputs to choose from in a given time window.
[11-10-2021 17:35:06] <UkoeHB> It makes the implementation simpler when there are few outputs in the chain (just after hardforking to a new epoch).
[11-10-2021 17:36:22] <rbrunner> You should look at the rings on Monero testnet, where we have fewer txs still. Sometimes they look *really* funny. But I can't see how that matters.
[11-10-2021 17:36:38] <Rucknium[m]> Wait, under what circumstances would the decoy selection algorithm not be able to select outputs from before a hard fork?
[11-10-2021 17:36:48] <carrington[m]> Any privacy hit would be dependent on external data. E.g. if the duplicated decoy is a known spent output, then you lose 2 decoys instead of 1
[11-10-2021 17:37:07] <UkoeHB> I believe that happened when RingCT went live. It will also happen if Seraphis goes live.
[11-10-2021 17:37:35] <UkoeHB> It happens when you need to transition for some reason. E.g. transition to hidden amounts, or transition to a new key image construction.
[11-10-2021 17:37:56] <Rucknium[m]> Oh boy, more statistical issues to dive into!
[11-10-2021 17:38:12] <rbrunner> Er ... and the very first new txs have nothing at all to select as decoys?
[11-10-2021 17:38:33] <carrington[m]> Interesting. Maybe we should organize users to spam the network with churned transactions at the upgrade time?
[11-10-2021 17:39:30] <Rucknium[m]> It seems strange since old genuine outputs can be spent.
[11-10-2021 17:40:33] <wfaressuissia1> if there would be any advantage in doing this activity then any attacker could do the same, so it's useless
[11-10-2021 17:40:44] <wfaressuissia1> this system should work independently from any users actions
[11-10-2021 17:40:44] <UkoeHB> When old outputs get spent, the new outputs in their tx are 'in the new format'. Also, new coinbase outputs are 'in the new format'.
[11-10-2021 17:42:17] <Rucknium[m]> So some of the ring members would have the old format and some would have the new format. It seems that decoys could still be selected from before the hard fork, right?
[11-10-2021 17:42:40] <UkoeHB> No, rings can only have outputs with a single format. So all new outputs would be in 'new format tx'.
[11-10-2021 17:44:12] <carrington[m]> So when you spend a very old CLSAG output, it will be obvious that you are doing so? Because of no recent decoys selected
[11-10-2021 17:44:12] <Rucknium[m]> Ok. So there would be a mix of old-style and new-style. Um, let me get this straight...
[11-10-2021 17:44:33] <UkoeHB> Correct
[11-10-2021 17:44:56] <UkoeHB> This is an unavoidable engineering problem.
[11-10-2021 17:45:20] <rbrunner> Well, still not clear how long before the hardfork that old output came into existence, right?
[11-10-2021 17:45:36] <wfaressuissia1> s/unavoidable/unsolved
[11-10-2021 17:45:37] <Rucknium[m]> [old,old,old]-->[new] , [new,new,new]-->[new] would be allowed after the hardfork
[11-10-2021 17:45:37] <Rucknium[m]> [old,new,new]-->[new] , [old,old,old]-->[old] would not be allowed.
[11-10-2021 17:45:38] <rbrunner> And that it's CLSAG is obvious anyway
[11-10-2021 17:46:12] <UkoeHB> Rucknium[m]:  yes
[11-10-2021 17:46:17] <jberman[m]> I think preventing duplicates is the technically correct thing to do from a stats perspective. In the tx sanity check, it first checks if there are >10k outputs available to use before checking there is only a small margin of duplicates. Could do something like that in the wallet to avoid challenges around fork time to a new format
[11-10-2021 17:47:35] <Rucknium[m]> UkoeHB: Ok. There are many thorny statistical issues in such a hard fork, then. We can research how to have a smooth transition.
[11-10-2021 17:48:09] <merope> How would the decoy selection look like when spending an old clsag output? Would it still follow the usual distribution (just traslated to older blocks), or would it change?
[11-10-2021 17:48:47] <UkoeHB> merope: that sounds like an _open research question_ :)
[11-10-2021 17:49:07] <merope> Hehe
[11-10-2021 17:49:36] <Rucknium[m]> UkoeHB: Yes, that's what I'm saying. Needs study.
[11-10-2021 17:50:21] <merope> Random thought: there should be a stroger bias towards older outputs after a while, because otherwise the last clsag outputs will show up in multiple conversion transactions, while the older ones would show up only once at most (ie when they actually get spent for conversion)
[11-10-2021 17:50:43] <merope> (Just throwing that in open)
[11-10-2021 17:51:13] <merope> I guess we could look at the pre-clsag to clsag conversion txes for reference
[11-10-2021 17:51:30] <rbrunner> Looks like a whole new can of worms opened today.
[11-10-2021 17:52:04] <carrington[m]> Wouldn't all the CLSAG outputs eventually end up in the long tail of the distribution? So little difference between older or newer CLSAG outputs
[11-10-2021 17:52:11] <UkoeHB> merope it would be pre-ringct to ringct
[11-10-2021 17:52:27] <merope> Oh right
[11-10-2021 17:52:42] <Rucknium[m]> rbrunner: I agree. Yum! Tasty research worms! 😋
[11-10-2021 17:53:36] <jberman[m]> we could analyze older data of known spents too, but ignore the X most recent outputs at any point in time, and look at different values of X
[11-10-2021 17:55:28] <Rucknium[m]> Before we close, I would invite everyone to think about what an independent funding mechanism focused specifically on research could look like, and maybe post your thoughts in #monero-research-lounge:monero.social 
[11-10-2021 17:57:30] <jberman[m]> hmmm, in this case, maybe it makes sense to "throw away" the portion of the gamma curve (or whatever curve is used) that is unrepresented. So as you move further away from the fork height to a new format, you start ignoring a larger and larger portion of the curve that is more recent
[11-10-2021 17:57:40] <wfaressuissia1> Is that doc still private ?
[11-10-2021 17:57:54] <UkoeHB> wfaressuissia1: what doc?
[11-10-2021 17:58:08] <wfaressuissia1> rucknium[m]: your document ...
[11-10-2021 17:59:37] <Rucknium[m]> My HackerOne submission is still private. I edited the language on disclosure in my CCS proposal recently.
[11-10-2021 18:00:16] <Rucknium[m]> The "Document A", i.e. OSPEAD technical specification, is still getting feedback, and I hope to push out a public version within the next week.
[11-10-2021 18:00:32] <UkoeHB> Ok we are at the end of the hour. Thanks for attending everyone.
[11-10-2021 18:00:44] <jberman[m]> also update from me: initial view tag implementation is finished, working on finalizing tests at this point. Sorry the daylight savings time switch messed me up
```

# Action History
- Created by: Rucknium | 2021-11-07T14:28:14+00:00
- Closed at: 2021-11-16T06:21:52+00:00
