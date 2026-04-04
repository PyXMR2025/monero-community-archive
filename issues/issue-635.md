---
title: Monero Research Lab Meeting - Wed 01 December 2021 @ 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/635
author: Rucknium
assignees: []
labels: []
created_at: '2021-11-30T20:43:59+00:00'
updated_at: '2021-12-06T04:30:22+00:00'
type: issue
status: closed
closed_at: '2021-12-06T04:30:22+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

[Join the Monero Matrix server if you don't already have a Matrix account.](https://forum.monero.space/d/79-how-to-join-the-monero-core-team-matrix-server-web)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/converter.html?iso=20211027T170000&p1=1440)

Main discussion topics:

1. Greetings

2. Discuss requirements to get [the multisig PR](https://github.com/monero-project/monero/pull/7877) merged.

3. "Seeing a bug in Aeon transactions where multiple inputs in one transaction use the same output. " https://github.com/monero-project/monero/pull/8047

4. Cryptographic performance benchmarks https://github.com/Rucknium/misc-research/tree/main/Monero-Cryptography-Benchmarks

5. Further analysis of July-Aug 2021 tx volume anomaly ( Isthmus / Mitchellpkt - see [these meeting logs](https://github.com/monero-project/meta/issues/621#issuecomment-948953655)) [Previous analysis](https://mitchellpkt.medium.com/fingerprinting-a-flood-forensic-statistical-analysis-of-the-mid-2021-monero-transaction-volume-a19cbf41ce60) with [Reddit discussion](https://www.reddit.com/r/Monero/comments/pvm634/fingerprinting_a_flood_forensic_statistical/)

6. Improvements to the mixin selection algorithm ( [Decoy Selection Algorithm - Areas to Improve](https://github.com/monero-project/research-lab/issues/86), [JBerman's weekly updates](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/249#note_11480), [Binning PoC](https://github.com/monero-project/research-lab/issues/88)) @j-berman @Rucknium

7. [The Science of Blockchain Conference 2022 Jan 24-26](https://cbr.stanford.edu/sbc22/#cfp). Submission deadline: November 23, 2021 11:59pm PST

8. Seraphis/Triptych/Lelantus Spark ( [UkoeHB's Seraphis Proof of Concept work](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/256), [Seraphis repo](https://github.com/UkoeHB/Seraphis), [Lelantus Spark](https://eprint.iacr.org/2021/1173) & [Tripych Multisig](https://github.com/cypherstack/triptych-multisig/blob/main/main.pdf) )

9. Rucknium's OSPEAD discussion ([CCS proposal](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/255) , Reddit discussion [1](https://www.reddit.com/r/Monero/comments/py8ub3/ccs_proposal_ospead_fortifying_monero_against/) & [2](https://www.reddit.com/r/Monero/comments/pyopq0/the_mathematical_nonsense_of_a_possible/)

10. MRL META: "Cat herding", i.e. prioritization of research areas and features. Active recruitment of technical talent, MRL structure, funding (@Rucknium & others) [Reddit discussion](https://www.reddit.com/r/Monero/comments/pkg3d6/the_monero_project_should_actively_recruit/)

11. Examine sample size and random seed matters in Monero's unit tests. IRC discussion: [monero-dev](https://libera.monerologs.net/monero-dev/20211018#c39593) , [monero-research-lab](https://libera.monerologs.net/monero-research-lab/20211018)

12. Multisig Drijvers attack mitigation [Technical note](https://github.com/UkoeHB/drijvers-multisig-tech-note) , [Haveno bounty](https://github.com/haveno-dex/haveno/issues/103)

13. Any other business

14. Confirm next meeting agenda


Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: UkoeHB

Previous meeting agenda/logs:

#632 

# Discussion History
## UkoeHB | 2021-12-01T18:01:01+00:00
```
[2021-12-01 17:02:05] <Rucknium[m]> Meeting time :) https://github.com/monero-project/meta/issues/635
[2021-12-01 17:02:11] <UkoeHB> Meeting ~1hr
[2021-12-01 17:02:17] <UkoeHB> Oh it’s now crap
[2021-12-01 17:02:26] <rbrunner> :)
[2021-12-01 17:02:51] <one-horse-wagon[> Hello
[2021-12-01 17:03:11] <h4sh3d> Hi
[2021-12-01 17:03:19] <selsta> hi
[2021-12-01 17:04:01] <jberman[m]> hey
[2021-12-01 17:05:39] <crypto_grampy[m]> hi
[2021-12-01 17:06:01] <masterbob79[m]> howdy
[2021-12-01 17:07:32] <UkoeHB> Um let’s do updates now.
[2021-12-01 17:09:54] <UkoeHB> I was on vacation and didn’t do anything. This week I have some ideas about how to interpret my perf data for tx throughout, and I need to start integrating coinstudent2048[‘s security modeling.
[2021-12-01 17:11:08] <Rucknium[m]> I have done a "dry run" of some components of OSPEAD here: https://github.com/Rucknium/OSPEAD
[2021-12-01 17:11:08] <Rucknium[m]> It uses the old Moser et al. (2018) data. Overall, so far so good. The minimization procedures work well. I tested the gamma, log-normal, and F distributions. Some lessons learned, e.g. can't avoid taking logs of the spend time data.
[2021-12-01 17:12:51] <Rucknium[m]> To be clear, the old Moser data will not be used much for the final implementation of OSPEAD since it is so old, except that it can be somewhat useful in evaluating how rapidly the spend time distribution evolves over months and years.
[2021-12-01 17:14:01] <Rucknium[m]> The F distribution came out looking the best, probably, but we are not anywhere near final results yet. I note that the F distribution has 3 parameters, while the gamma and log-normal distributions have two each.
[2021-12-01 17:15:17] <Rucknium[m]> So the F distribution may be considered to be slightly more flexible than the other two distributions simply be virtue of having more parameters to work with.
[2021-12-01 17:15:38] <Rucknium[m]> The dry run was suggested by jberman 
[2021-12-01 17:15:47] <UkoeHB> Thanks Rucknium[m] 
[2021-12-01 17:16:13] <one-horse-wagon[> Rucknium: Is there a way for you to look at data, whether contrived or not, do a statistical attack on it and actually trace out someone's wallet?  Looking at total distributions really doesn't give much information as to who is doing what, does it?
[2021-12-01 17:16:32] <jberman[m]> Looking good, need to spend more time with this to understand it
[2021-12-01 17:18:41] <Rucknium[m]> one-horse-wagon: For the decoys to work properly, they need to be convincing decoys, i.e. mimic real spends. If the decoys are not convincing, then an adversary can gain advantage.
[2021-12-01 17:18:53] <UkoeHB> This week I'd like to discuss requirements to get the multisig PR merged ( https://github.com/monero-project/monero/pull/7877 ). Right now, rbrunner has verified the original commit works on MMS, moneromooo has scanned the c++, h4sh3d has reviewed the core multisig address construction component library. Wallet-side code has not been reviewed (wallet2, rpc, simplewallet). At minimum, the wallet-side code needs to be 
[2021-12-01 17:18:53] <UkoeHB> reviewed and approved. Maybe selsta or luigi1111 would like more review on top of that.
[2021-12-01 17:19:29] <jberman[m]> Update from me: planning to change the view tag PR to use the code base's already existing cn_fast_hash (keccak) instead of siphash today as per discussion in the view tag PR on github (finishing up final testing). I've been exploring separate optimizations to wallet scanning that have been not as fruitful as I previously thought they'd be unfortunately. Hopefully moving back over to binning/decoy selection work in the next day
[2021-12-01 17:19:29] <jberman[m]> or 2
[2021-12-01 17:19:53] <Rucknium[m]> Moser et al. (2018) exploited the fact that the real spend distribution is not at all like the triangular distribution that the decoy selection algorithm was using at that time.
[2021-12-01 17:21:51] <UkoeHB> Is there anyone willing and able to review the wallet-side code for the multisig PR? I cannot do it because I wrote it...
[2021-12-01 17:22:24] <rbrunner> You mainly mean the `wallet2` changes, right?
[2021-12-01 17:22:24] <selsta> in addition to h4sh3d? or generally?
[2021-12-01 17:22:38] <h4sh3d> Regarding #7877 I don't feel confident enough to review the wallet part, I never worked on (I did one small PR on it ages ago). So I think selsta or luigi1111 might be a better pick
[2021-12-01 17:22:50] <rbrunner> Because not much changed elsewhere as far as I could quickly see
[2021-12-01 17:23:06] <selsta> UkoeHB: did mooo review wallet c++ code?
[2021-12-01 17:23:26] <UkoeHB> pretty sure he just glanced at it
[2021-12-01 17:23:59] <Rucknium[m]> At the extreme, a statistical attack could identify real spends for a specific transaction. Think about the extreme case: Say the decoy selection algorithm never selected decoys from blocks that are 1000-1010 blocks old. In that case, if a ring member came from that range, it would be identifiable as the real spend. That particular transaction would be completely traceable.
[2021-12-01 17:26:02] <rbrunner> The `wallet2` changes look quite challenging to understand and review to me
[2021-12-01 17:26:25] <selsta> vtnerd? 
[2021-12-01 17:28:18] <rbrunner> Certainly worth to ask him to have a look, IMHO
[2021-12-01 17:29:03] <h4sh3d> interface from src/multisig is very understandable and quite simple, with someone with a good understanding of wallet2 structure (and experience) it shouldn't be that hard
[2021-12-01 17:29:45] <h4sh3d> and a bit of time :)
[2021-12-01 17:30:02] <rbrunner> You certainly mean wallet2 non-structure :)
[2021-12-01 17:30:16] <jberman[m]> I can give a go at it, my confidence in wallet2 is increasing :) but it would be nice to get approval on it from moo or vtnerd if they're willing
[2021-12-01 17:31:08] <rbrunner> By the way, I still wonder, does this PR alone already solve that problem that according to UkoeHB makes multisig "not recommended" currently?
[2021-12-01 17:31:29] <UkoeHB> No, only part of it.
[2021-12-01 17:32:05] <rbrunner> Tough.
[2021-12-01 17:33:28] <Rucknium[m]> rbrunner: Maybe nice idea that will probably never happen: We should get developers from one of the six BCH node implementations to translate the Monero C++ code into another language, like they have done for BCH.
[2021-12-01 17:34:06] <h4sh3d> I don't think that's doable and a good idea ;)
[2021-12-01 17:34:24] <rbrunner> Would the other/remaining part be what wfaressuissia said they would try?
[2021-12-01 17:34:28] <UkoeHB> if you want to pay for their therapy, go for it
[2021-12-01 17:34:35] <h4sh3d> ^^
[2021-12-01 17:34:39] <UkoeHB> rbrunner: nominally... yes
[2021-12-01 17:34:55] <rbrunner> We didn't hear much from them in the meantime, right?
[2021-12-01 17:35:12] <selsta> they reported the issues on H1
[2021-12-01 17:36:13] <selsta> so we will figure out how to resolve them
[2021-12-01 17:37:52] <rbrunner> That sounds like quite some challenge. First getting this PR to merge, and that add another one still, to make multisig fully functioning until the HF
[2021-12-01 17:38:43] <UkoeHB> yes, trying to make incremental progress towards that, hence bringing it up here
[2021-12-01 17:39:03] <h4sh3d> with this one only it is anyway better than now
[2021-12-01 17:39:51] <h4sh3d> So if we find someone else jberman[m] you would give it a go?
[2021-12-01 17:40:36] <jberman[m]> No I'll give it a go now
[2021-12-01 17:41:17] <rbrunner> I think in this light I will make functional tests again, with the current code, this coming weekend. Never mind that future PR and testing again, worst case that won't happen ...
[2021-12-01 17:41:49] <rbrunner> I mean no second PR, no testing ...
[2021-12-01 17:42:30] <UkoeHB> MMS tests?
[2021-12-01 17:42:56] <rbrunner> Yes
[2021-12-01 17:42:57] <UkoeHB> Have you considered adding a test to the test suite?
[2021-12-01 17:43:21] <rbrunner> You mean automate that? Not sure that's possible at all.
[2021-12-01 17:43:25] <UkoeHB> ah
[2021-12-01 17:43:35] <rbrunner> It's not available over RPC
[2021-12-01 17:44:28] <rbrunner> Would be feeding keystrokes to the monero-wallet-cli binary ...
[2021-12-01 17:44:54] <h4sh3d> sounds like a great idea :)
[2021-12-01 17:45:02] <rbrunner> Sure :)
[2021-12-01 17:45:09] <UkoeHB> lol
[2021-12-01 17:45:24] <h4sh3d> is there a way we could feed the cli with a file and it does 1 line 1 command?
[2021-12-01 17:45:45] <rbrunner> Don't think that's available already out of the box
[2021-12-01 17:46:07] <UkoeHB> It sounds like the conclusion is: jberman[m] will review wallet-side code for the multisig PR, hopefully vtnerd can also review it.
[2021-12-01 17:47:31] <UkoeHB> Is there anything else to discuss in the remaining minutes?
[2021-12-01 17:48:29] <Rucknium[m]> br1ck and/or r3llun  had a question about multi party computation
[2021-12-01 17:49:37] <h4sh3d> I can quickly say that next week we will make some tests at a greater scale (testnet coins) for the Farcaster project, I'll ping here and -dev next Wednesday when we are ready
[2021-12-01 17:50:07] <UkoeHB> congrats h4sh3d :)
[2021-12-01 17:50:14] <rbrunner> Interesting.
[2021-12-01 17:50:54] <UkoeHB> I don't recall any MPC work being done with monero. There is only multisig.
[2021-12-01 17:51:23] <rbrunner> MPC = building txs by groups of people?
[2021-12-01 17:52:27] <UkoeHB> yeah pretty sure it is a different approach to multisig that relies on Pallier typically
[2021-12-01 17:52:36] <h4sh3d> Another idea is "adaptor signatures" or "encrypted signatures"... it is multi-party but don't recall the exact definition of MPC
[2021-12-01 17:54:01] <rbrunner> Ideas are never in short supply, reviewed code on the other hand ...
[2021-12-01 17:55:16] <UkoeHB> Typically MPC is a kind of 'enterprise' technology used inside companies... I think
[2021-12-01 17:55:46] <UkoeHB> Anyway we are reaching the end of the hour. Any last minute questions/comments?
[2021-12-01 17:55:51] <shroomreactionar> My concern with using MPC is that if only one of the parties loses their key or dies, then your money is gone
[2021-12-01 17:56:25] <UkoeHB> Is MPC only N-of-N?
[2021-12-01 17:57:31] <shroomreactionar> UkoeHB: oh fair enough.
[2021-12-01 17:59:42] <UkoeHB> Ok I will call it here. Thanks for attending everyone.
```

# Action History
- Created by: Rucknium | 2021-11-30T20:43:59+00:00
- Closed at: 2021-12-06T04:30:22+00:00
