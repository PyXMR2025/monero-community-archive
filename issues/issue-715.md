---
title: Monero Research Lab Meeting - Wed 22 June 2022
source_url: https://github.com/monero-project/meta/issues/715
author: Rucknium
assignees: []
labels: []
created_at: '2022-06-21T01:00:00+00:00'
updated_at: '2022-06-27T21:18:38+00:00'
type: issue
status: closed
closed_at: '2022-06-27T21:18:38+00:00'
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

#714 

# Discussion History
## UkoeHB | 2022-06-22T17:47:56+00:00
```
[06-22-2022 17:00:21] <UkoeHB> meeting time https://github.com/monero-project/meta/issues/715
[06-22-2022 17:00:26] <UkoeHB> 1. greetings
[06-22-2022 17:00:29] <UkoeHB> hello
[06-22-2022 17:00:45] <Rucknium[m]> Hi
[06-22-2022 17:00:50] <rbrunner> Hello
[06-22-2022 17:01:34] <SerHack> hi
[06-22-2022 17:01:37] <ooo123ooo1234567> hello
[06-22-2022 17:01:43] <jberman[m]> hiya
[06-22-2022 17:01:43] <ofrnxmr[m]1> wave
[06-22-2022 17:02:29] <tobtoht[m]> hi
[06-22-2022 17:03:40] <ArticMine> hi
[06-22-2022 17:04:08] <UkoeHB> 2. updates, what is everyone working on?
[06-22-2022 17:06:11] <Rucknium[m]> Based on mj-xmr's Python implementation of the `wallet2` decoy selection algorithm, I wrote an R implementation. With one million draws, the R implementation passes a K-S test against the `wallet2` implementation when the number of outputs to draw from is large. https://github.com/mj-xmr/monero-mrl-mj/pull/3
[06-22-2022 17:07:58] <jberman[m]> monerkon presentation on seraphis/jamtis features went solid I think, finished the ledger integration for the hf, finishing up reviewing 8076, got help from TheCharlatan on lws static building finishing up testing his work, planning to submit a new CCS soon
[06-22-2022 17:09:20] <UkoeHB> me: Got some basic unit tests of enote scanning running. At this point there is enough code in my seraphis library to begin writing a wallet. I still have various todos: deeper/more comprehensive unit testing of enote scanning, implement seraphis coinbase txs, implement ringct/seraphis transition txs (need to decide if it's worth the effort to do mixed-input-type txs), and some miscellaneous library improvements (e.g. still need 
[06-22-2022 17:09:20] <UkoeHB> to look closer at using Curve25519 to speed up scanning). Also, on sunday I did a monerokon presentation about seraphis balance recovery, hopefully the video becomes available at some point.
[06-22-2022 17:11:25] <ArticMine> I did a monerokon presentation of environmental impacts and a the ramifications for 51% and big bang attascks
[06-22-2022 17:11:30] <ooo123ooo1234567> (tracking progress of auditors via twitter of their supervisor)
[06-22-2022 17:12:36] <ArticMine> I am starting on a comprehensive overview of the whole fee, scaling, and related security and spam issues
[06-22-2022 17:13:12] <ArticMine> More like a reference on how the penalty and related issue work
[06-22-2022 17:14:04] <Rucknium[m]> ArticMine: You may want to talk with endor00 if you haven't already, since they are working on an analysis of the Monero "security budget".
[06-22-2022 17:16:34] <ArticMine> Sure thanks for lettign me know
[06-22-2022 17:16:34] <UkoeHB> 3. discussion, anything to discuss? there are the persistent many-input txs that have been showing up since last fall...
[06-22-2022 17:18:40] <ooo123ooo1234567> hardfork
[06-22-2022 17:18:53] <Rucknium[m]> I didn't consider the ring caching possibility, jberman. Thanks for pointing it out. I think when I read about caching rings, I just assumed that users would re-submit a tx soon after the ring was constructed, so there wouldn't be such a time lag between the decoy selection and confirmation of the tx in the blockchain.
[06-22-2022 17:19:25] <Rucknium[m]> The tx in question would be an egregious case of it.
[06-22-2022 17:21:11] <ooo123ooo1234567> in the best case it was just txs from some wallet with a lot of failed attempts to relay txs, nothing suspicious or interesting except broken tx relay and harmful edge case for ring signature cache
[06-22-2022 17:21:25] <ooo123ooo1234567> nothing interesting to discuss from research point of view
[06-22-2022 17:22:03] <jberman[m]> I'm in to discuss the hard fork too though we're probably missing some people
[06-22-2022 17:22:26] <selsta> I'm here, but I would prefer a separate dev meeting for it.
[06-22-2022 17:23:44] <Rucknium[m]> Is it correct to say that our current predicament is the result of the multisig audit taking longer than expected?
[06-22-2022 17:24:24] <ofrnxmr[m]1> Rucknium[m]: I'd say so
[06-22-2022 17:24:32] <selsta> The auditors planned to send a draft last Friday, I'm not sure if they gave an update since then.
[06-22-2022 17:24:40] <ooo123ooo1234567> Since the scope of audit is unknown it isn't clear whether it's expected or unexpected duration of proper audit
[06-22-2022 17:26:10] <ooo123ooo1234567> it's ok to do asynchronous audit in private, but it isn't ok to do synchronous audit that blocks everything else in private
[06-22-2022 17:26:17] <UkoeHB> I haven't heard anything either
[06-22-2022 17:26:48] <UkoeHB> If there is nothing else to discuss, we can end the meeting early
[06-22-2022 17:27:13] <Rucknium[m]> Cutting (time) losses is always an option. Sunk cost fallacy, etc.
[06-22-2022 17:27:45] <selsta> At this point I think a 2 week HF delay is realistic.
[06-22-2022 17:28:49] <UkoeHB> no objection from me
[06-22-2022 17:29:02] <jberman[m]> me neither
[06-22-2022 17:29:36] <sech1> 2 weeks = 10,000 blocks, so we can move fork height from 2668888 to 2678888
[06-22-2022 17:30:19] <jberman[m]> I don't think we can settle on a date until we have better clarity on the path forward with multisig, which is tied up by a 3rd party now 
[06-22-2022 17:30:31] <selsta> I'm waiting to get feedback from someone who works at Trezor, they also need to do a firmware update before we HF.
[06-22-2022 17:30:33] <jberman[m]> settle on a delay*
[06-22-2022 17:30:46] <ArticMine> Is the 2 week period realistic?
[06-22-2022 17:30:53] <ooo123ooo1234567> is there any postponed research that is required for Seraphis integration ?
[06-22-2022 17:31:29] <ooo123ooo1234567> or implementation is the only missing component ?
[06-22-2022 17:32:06] <selsta> ArticMine: we can decide on it during the dev meetin
[06-22-2022 17:32:46] <ArticMine> So we finalize the new HF time at dev?
[06-22-2022 17:32:51] <selsta> yes
[06-22-2022 17:32:56] <ArticMine> Sound good to me
[06-22-2022 17:33:10] <jberman[m]> is there a date for dev meeting?
[06-22-2022 17:33:14] <Rucknium[m]> I'm not a software developer, so my opinion means little, but I would support keeping the current date and delaying the multisig fix to a post-HF release.
[06-22-2022 17:33:41] <selsta> UkoeHB: ooo had a question regarding Seraphis, in case you want to reply https://libera.monerologs.net/monero-research-lab/20220622
[06-22-2022 17:34:01] <selsta> Rucknium[m]: the problem is we want to give everyone enough time to update
[06-22-2022 17:34:02] <ofrnxmr[m]1> Rucknium[m]: +1
[06-22-2022 17:34:04] <ArticMine> I just do not want the HF to keep dragging on. If we can set a time and then sitick to it
[06-22-2022 17:34:20] <ArticMine> stick
[06-22-2022 17:34:35] <ooo123ooo1234567> HF date should be set after code is ready, not before
[06-22-2022 17:35:03] <jberman[m]> agree with ooo
[06-22-2022 17:35:47] <jberman[m]> the good news is code seems pretty close to ready though
[06-22-2022 17:36:31] <selsta> yes the remaining things are 1) trezor firmware update date 2) ledger finishing integration
[06-22-2022 17:36:53] <selsta> jberman[m] "helped" (or has done everything for them) with the ledger integration but they still have to do testing etc
[06-22-2022 17:36:57] <ArticMine> My point is 2-4 weeks would be fine, but if we are looking at months then may wennd to consider 2 HFs
[06-22-2022 17:37:06] <selsta> no, it's not months away
[06-22-2022 17:37:09] <UkoeHB> ooo123ooo12345[m: there are no new innovations required, although the paper still needs security modeling/proofs. Once I am satisfied with the implementation, then I will take some time to update the paper as much as possible (including coinstudent's contributions), then go looking for help with the missing parts.
[06-22-2022 17:40:37] <ooo123ooo1234567> What are the heaviest parts that would require 1-2 years for Seraphis deployment ? is it possible to do rough breakdown  ?
[06-22-2022 17:42:28] <selsta> luigi also said he will be unavailable for a bit so that also means we will have to delay for 2 weeks
[06-22-2022 17:45:32] <ooo123ooo1234567> <jberman[m]> "the good news is code seems..." <- judging by size of patches for ledger (~100 lines monero/menoro, ~130 lines ledgerhq/app-monero) their firmware is much simpler than trezor
[06-22-2022 17:46:43] <UkoeHB> ok I think we can end the meeting here, thanks for attending everyone; the dev planning stuff can continue in -dev if needed
```

# Action History
- Created by: Rucknium | 2022-06-21T01:00:00+00:00
- Closed at: 2022-06-27T21:18:38+00:00
