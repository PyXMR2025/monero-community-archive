---
title: Monero Research Lab Meeting - Wed 02 March 2022 @ 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/669
author: Rucknium
assignees: []
labels: []
created_at: '2022-02-28T22:04:39+00:00'
updated_at: '2022-03-09T16:50:16+00:00'
type: issue
status: closed
closed_at: '2022-03-09T16:50:16+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

[Join the Monero Matrix server if you don't already have a Matrix account.](https://forum.monero.space/d/79-how-to-join-the-monero-core-team-matrix-server-web)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/converter.html?iso=20211027T170000&p1=1440)

Main discussion topics:

1. Greetings

2. Fee policy and dynamic block size discussion for upcoming hard fork: https://github.com/monero-project/meta/issues/630 ; https://github.com/monero-project/monero/pull/7819 ; https://github.com/monero-project/research-lab/issues/70

3. Revisit @tevador 's idea to record account indices in the tx, to improve robustness of output recovery: https://libera.monerologs.net/monero-research-lab/20211230 . Additional reading: https://gist.github.com/tevador/50160d160d24cfc6c52ae02eb3d17024#gistcomment-4025357

4. Focus on Seraphis address schemes and hopefully reach some kind of decision (or get closer, maybe narrow down the choices to 2 or 3). [Schemes](https://github.com/monero-project/research-lab/issues/92) [@tevador proposal](https://gist.github.com/tevador/50160d160d24cfc6c52ae02eb3d17024)

5. Adaptive CPU regulation for improved mining performance ( maxwellsdemon )

6. Further analysis of July-Aug 2021 tx volume anomaly ( Isthmus / Mitchellpkt - see [these meeting logs](https://github.com/monero-project/meta/issues/621#issuecomment-948953655)) [Previous analysis](https://mitchellpkt.medium.com/fingerprinting-a-flood-forensic-statistical-analysis-of-the-mid-2021-monero-transaction-volume-a19cbf41ce60) with [Reddit discussion](https://www.reddit.com/r/Monero/comments/pvm634/fingerprinting_a_flood_forensic_statistical/)

7. Improvements to the mixin selection algorithm ( [Decoy Selection Algorithm - Areas to Improve](https://github.com/monero-project/research-lab/issues/86), [JBerman's weekly updates](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/249#note_11480), [Binning PoC](https://github.com/monero-project/research-lab/issues/88), [OSPEAD](https://ccs.getmonero.org/proposals/Rucknium-OSPEAD-Fortifying-Monero-Against-Statistical-Attack.html) ) @j-berman @Rucknium

8. Seraphis/Triptych/Lelantus Spark ( [UkoeHB's Seraphis Proof of Concept work](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/256), [Seraphis repo](https://github.com/UkoeHB/Seraphis), [Lelantus Spark](https://eprint.iacr.org/2021/1173) & [Tripych Multisig](https://github.com/cypherstack/triptych-multisig/blob/main/main.pdf) )

9. MRL META: "Cat herding", i.e. prioritization of research areas and features. Active recruitment of technical talent, MRL structure, funding (@Rucknium & others) [Reddit discussion](https://www.reddit.com/r/Monero/comments/pkg3d6/the_monero_project_should_actively_recruit/)

10. Examine sample size and random seed matters in Monero's unit tests. IRC discussion: [monero-dev](https://libera.monerologs.net/monero-dev/20211018#c39593) , [monero-research-lab](https://libera.monerologs.net/monero-research-lab/20211018)

11. Multisig Drijvers attack mitigation [Technical note](https://github.com/UkoeHB/drijvers-multisig-tech-note) , [Haveno bounty](https://github.com/haveno-dex/haveno/issues/103)

12. Any other business

13. Confirm next meeting agenda


Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: UkoeHB

Previous meeting agenda/logs:

#668

# Discussion History
## UkoeHB | 2022-03-02T17:55:10+00:00
```
[03-02-2022 17:01:20] <one-horse-wagon[> Hello everyone.
[03-02-2022 17:01:51] <frr> Greetings 
[03-02-2022 17:01:55] <Rucknium[m]> Hi
[03-02-2022 17:02:00] <rbrunner> Hello
[03-02-2022 17:02:04] <mj-xmr[m]> Hey!
[03-02-2022 17:02:38] <UkoeHB> oh hi whoops
[03-02-2022 17:02:48] <hyc> hi
[03-02-2022 17:02:59] <UkoeHB> meeting agenda: https://github.com/monero-project/meta/issues/669
[03-02-2022 17:03:55] <jberman[m]> hey
[03-02-2022 17:04:22] <UkoeHB> 2. we can start with updates, what is everyone up to?
[03-02-2022 17:04:32] <mj-xmr[m]> I've just started unofficially my work yesterday and am dealing with IT-related leftovers, that accumulated while I was working on tsqsim. Nothing related to MRL really.
[03-02-2022 17:05:15] <UkoeHB> me: I opened a CCS for Seraphis wallet PoC https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/290 and did a bit of work in that direction (added tx_extra and fees to my poc).
[03-02-2022 17:08:19] <Rucknium[m]> I've been working on posting papers to MoneroResearch.info (Reminder: if you want an account to be able to upload and annotate papers, please message me and I will get you set up)
[03-02-2022 17:09:33] <Rucknium[m]> Also I have been working on measuring the proportion on the BCH UTXO set that is a descendant of a CashFusion tx, a type of CoinJoin:
[03-02-2022 17:09:33] <Rucknium[m]> https://github.com/Rucknium/misc-research/tree/main/CashFusion-Descendant-Analysis
[03-02-2022 17:09:42] <Rucknium[m]> I hope to release results in the next few days
[03-02-2022 17:10:46] <rbrunner> UkoeHB: Your CCS asks for funds for 2 months of work. Is that the result of a rough estimate how long implementing the PoC might take?
[03-02-2022 17:11:00] <Rucknium[m]> Relatedly, if anyone has a more-of-less comprehensive list of all CoinJoin transaction on the BTC blockchain, let me know.
[03-02-2022 17:11:09] <jberman[m]> Just got started on  hyc  's background sync cache so wallets scan for tx's with just view key + address in the background without needing access to the spend key. Also submitted some PR's to MyMonero/monero-lws to tackle some fee issues that could lead to fingerprinting
[03-02-2022 17:11:11] <UkoeHB> rbrunner: yes my best guess
[03-02-2022 17:11:45] <jberman[m]> https://github.com/monero-project/monero/issues/8082
[03-02-2022 17:13:13] <UkoeHB> 3. today I want to bring up timelocks again (my little proposal: https://github.com/monero-project/research-lab/issues/78#issuecomment-1003195804 ); now would be a good time for me to implement it in Seraphis if it's worthwhile
[03-02-2022 17:14:13] <UkoeHB> it's timelocks as a range of block heights where a tx may be mined, enforced with two range proofs (or one range proof if we want an open range)
[03-02-2022 17:14:43] <endogenic> seems reasonable to me
[03-02-2022 17:15:35] <moneromooo> Why range proofs ? To hide them ?
[03-02-2022 17:15:39] <UkoeHB> right
[03-02-2022 17:16:00] <moneromooo> Can't they be brute forced rather trivially ?
[03-02-2022 17:16:14] <UkoeHB> how? you use pedersen commitments, just like amounts
[03-02-2022 17:16:33] <rbrunner> Not sure I understand how you can hide heights and still check whether the tx is mineable
[03-02-2022 17:16:50] <moneromooo> Verify the tx with all heights between say, now and now + 50k.
[03-02-2022 17:16:53] <Rucknium[m]> How does this compare to how time locks work on BTC? (It seems to me that they would be very similar, which would be good IMHO.)
[03-02-2022 17:17:06] <UkoeHB> you state two nominal heights in clear text, then range proof `hidden_height - clear_height`
[03-02-2022 17:18:31] <UkoeHB> the workflow would be: 1) define tx with hidden timelocks, 2) when you want to submit the tx, select two heights nearby your submission height and make a timelock proof (consisting of two cleartext heights and two range proofs)
[03-02-2022 17:19:33] <moneromooo> Ah. I see now.
[03-02-2022 17:19:52] <UkoeHB> Rucknium[m]: I forget lol
[03-02-2022 17:20:38] <jberman[m]> would every tx add one by default? or just users who want to use a timelock?
[03-02-2022 17:20:41] <rbrunner> So one could see that the tx is timelocked, just not how exactly.
[03-02-2022 17:20:41] <UkoeHB> I have not looked into the usecases for good timelocks so... this is also a request for people who want timelocks to step forward
[03-02-2022 17:20:46] <moneromooo> In what cases could this be useful ?
[03-02-2022 17:21:08] <UkoeHB> jberman[m]: every tx would add it I think
[03-02-2022 17:21:21] <UkoeHB> it's open for debate though
[03-02-2022 17:21:57] <rbrunner> What's again the approximate size of such a range proof?
[03-02-2022 17:22:22] <rbrunner> In bytes I mean
[03-02-2022 17:22:26] <UkoeHB> rbrunner: they would be aggregated with other tx range proofs, so only a couple extra 32 bytes
[03-02-2022 17:22:46] <UkoeHB> depending on bp+ aggregation cutoffs
[03-02-2022 17:22:57] <moneromooo> Plus 64 for the two commitments.
[03-02-2022 17:23:10] <moneromooo> (presumably)
[03-02-2022 17:23:31] <UkoeHB> yeah, and 16 bytes for the cleartext heights (or less if using varints)
[03-02-2022 17:24:25] <rbrunner> IMHO still a tough sell for 0.01% or so of tx which will use the feature if *every* tx gets this, for uniformity
[03-02-2022 17:24:30] <UkoeHB> I think it's 64 extra range proof bytes if adding the timelock proofs makes you go over a cutoff
[03-02-2022 17:25:10] <moneromooo> Verification time would be bumped a lot more given it's not log increase.
[03-02-2022 17:25:42] <UkoeHB> yes, although batching has a substantial effect
[03-02-2022 17:25:45] <moneromooo> Actually, wait. Maybe not, if it's the multiexp ?
[03-02-2022 17:25:45] <hyc> seems like a lot to pay for an infrequently used feature
[03-02-2022 17:25:56] <moneromooo> in the*
[03-02-2022 17:26:23] <endogenic> can it be added later if we decide it's super important?
[03-02-2022 17:26:29] <UkoeHB> sure
[03-02-2022 17:26:42] <moneromooo> Anyway, it'd be nice if if were a biulding block for some second layer thing. Otherwise, meh.
[03-02-2022 17:26:50] <hyc> in that case sounds like something to leave out for now
[03-02-2022 17:26:54] <endogenic> i think there are lots of use cases for it
[03-02-2022 17:26:56] <rbrunner> For swaps and such?
[03-02-2022 17:26:58] <endogenic> people have chimed in about it to some degree
[03-02-2022 17:27:01] <rbrunner> Atomic swaps
[03-02-2022 17:27:24] <rbrunner> To "go first" with XMR which I think now is not possible
[03-02-2022 17:27:36] <UkoeHB> rbrunner: I think only tx chaining is required for that
[03-02-2022 17:27:55] <one-horse-wagon[> Are not atomic swaps a long way off at this time?
[03-02-2022 17:28:12] <atomfried[m]> moneromooo: i think for such a use conditional locks would help much more
[03-02-2022 17:28:37] <UkoeHB> timelocks are conditional... what do you mean?
[03-02-2022 17:28:39] <rbrunner> No, I think BTC-XMR swaps are already possible on the mainnets
[03-02-2022 17:28:41] <Rucknium[m]> I think it would make it easier to have bi-directional atomic swaps (i.e. both "buy" and "sell" orders on the "order book", which would improve liquidity greatly, I think. However, there is at least one paper that claims bi-directional Monero atomic swaps without Monero time locks.
[03-02-2022 17:29:27] <Rucknium[m]> And then payment channels get easier, I think. Although again there are claims of possible Monero payment channels without such time locks.
[03-02-2022 17:29:35] <hyc> yeah conditional locks make sense. timelock, what happens if you just wait out the time interval?
[03-02-2022 17:29:38] <atomfried[m]> UkoeHB: conditional in the sense of they are locked until time x or until someone shows that he knows secret s
[03-02-2022 17:30:09] <atomfried[m]> oh i see conditional is not the right word here, sorry
[03-02-2022 17:30:30] <UkoeHB> we have the former one now, and it isn't used
[03-02-2022 17:30:57] <UkoeHB> the latter one is basically txo signing... what's the difference?
[03-02-2022 17:32:26] <Rucknium[m]> For a proposed method for bidirectional atomic swaps without time locks, see:
[03-02-2022 17:32:26] <Rucknium[m]> https://moneroresearch.info/index.php?action=resource_RESOURCEVIEW_CORE&id=30
[03-02-2022 17:32:29] <jberman[m]> DLSAG also uses hidden timelocks but in combination with a refund mechanism to enable payment channels. So timelocks seemed necessary but insufficient
[03-02-2022 17:33:36] <endogenic> I can certainly see use cases for locking outputs to automatically spend or refund upon another transaction's confirmation
[03-02-2022 17:35:52] <rbrunner> That paper abstract sounds like they find some magic ...
[03-02-2022 17:36:10] <rbrunner> *found
[03-02-2022 17:36:14] <UkoeHB> Well, I think unless someone shows up with a clear and specific usecase for timelocks, we can punt it to the future.
[03-02-2022 17:36:33] <hyc> agreed
[03-02-2022 17:36:48] <UkoeHB> Any other subjects people want to discuss? Perhaps from the agenda.
[03-02-2022 17:36:55] <endogenic> the timelocks thing is a subset of overall locking though, no?
[03-02-2022 17:37:00] <endogenic> not to drag this on
[03-02-2022 17:37:05] <UkoeHB> subset?
[03-02-2022 17:37:09] <endogenic> subset.. specific case
[03-02-2022 17:37:22] <endogenic> a e.g. range proof could be used to prove various things like confirmation
[03-02-2022 17:37:24] <endogenic> i *think*
[03-02-2022 17:37:36] <endogenic> i dont quite understand how it remains totally private though
[03-02-2022 17:37:43] <endogenic> which I suppose veers into DLSAG territory
[03-02-2022 17:37:52] <endogenic> but there are use cases for locking for sure
[03-02-2022 17:38:29] <endogenic> i think right now it's ok because we have some sort of rough alternatives for those use cases. so i wouldn't mind if we just bring this up later :)
[03-02-2022 17:38:31] <UkoeHB> it's not totally private - you expose a subset of the timelock range
[03-02-2022 17:39:03] <UkoeHB> also btw, I removed monero's normal timelocks from my poc (i.e. didn't implement it): https://github.com/monero-project/research-lab/issues/78
[03-02-2022 17:39:36] <rbrunner> So if we can't get up our collective asses to remove them earlier, as originally discussed, you will finally kill them :)
[03-02-2022 17:39:55] <UkoeHB> guess so
[03-02-2022 17:40:22] <endogenic> which i think is fine as long as there's no cost to adding them back if needed
[03-02-2022 17:40:25] <endogenic> but there may be
[03-02-2022 17:40:56] <UkoeHB> the cost is a hard fork and more code
[03-02-2022 17:41:04] <endogenic> well, privacy cost
[03-02-2022 17:41:24] <endogenic> and hypothetical migration cost
[03-02-2022 17:41:32] <endogenic> i mean whether the formats can be migrated
[03-02-2022 17:42:18] <UkoeHB> no, it is pointless to migrate the old timelock format to a hidden version
[03-02-2022 17:42:30] <rbrunner> Looks like locks introduced would be strictly additional, no?
[03-02-2022 17:42:38] <rbrunner> *introduced later
[03-02-2022 17:43:28] <endogenic> that's not what i mean
[03-02-2022 17:43:33] <endogenic> migrate from no timelocks back to having thenm
[03-02-2022 17:44:23] <rbrunner> I understood it also that way, I think. We want them back, we implement, we hardfork, txs get somewhat larger, done.
[03-02-2022 17:45:08] <UkoeHB> The semantics of hidden timelocks in my proposal are very different from current timelocks, so the path is 'remove a feature' then 'implement a different feature'.
[03-02-2022 17:45:59] <rbrunner> With the "remove a feature" proposed already for the very first version of Seraphis, right?
[03-02-2022 17:46:24] <jberman[m]> Would want to check in again with atomic swaps people, but AFAIU, hidden timelocks can improve the UX in combination with transaction chaining, so long as the hidden timelock is implemented like "can't include this tx until block N", rather than "this output is locked until block N". Even though the latter would still allow the former with a hack, seems we'd still want the former
[03-02-2022 17:46:43] <jberman[m]> Here's what tx chaining enables: thanks to tx chaining, I can submit tx0 and have pre-signed tx1 spending outputs from tx0 back to myself, in the event of an unresponsive counter-party
[03-02-2022 17:47:04] <UkoeHB> rbrunner: yes, there are important reasons seraphis can't support it https://github.com/monero-project/research-lab/issues/78#issuecomment-913046076
[03-02-2022 17:47:08] <jberman[m]> Without a timelock, I could submit tx1 10 blocks after tx0. But maybe my counter-party wants more time for the atomic swap, e.g. maybe I should give them 24 hours. A timelock on tx1 enables that
[03-02-2022 17:47:17] <endogenic> i agree with Justin here
[03-02-2022 17:49:54] <UkoeHB> I see, it would be good to get confirmation on that
[03-02-2022 17:50:09] <UkoeHB> We are approaching the meeting end, are there any other topics to address?
[03-02-2022 17:54:16] <UkoeHB> ok guess not, shall we call it here? thanks for attending everyone
```

# Action History
- Created by: Rucknium | 2022-02-28T22:04:39+00:00
- Closed at: 2022-03-09T16:50:16+00:00
