---
title: Monero Research Lab Meeting - Wed 05 January 2022 @ 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/646
author: Rucknium
assignees: []
labels: []
created_at: '2022-01-04T16:29:47+00:00'
updated_at: '2022-01-08T16:26:40+00:00'
type: issue
status: closed
closed_at: '2022-01-08T16:26:40+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

[Join the Monero Matrix server if you don't already have a Matrix account.](https://forum.monero.space/d/79-how-to-join-the-monero-core-team-matrix-server-web)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/converter.html?iso=20211027T170000&p1=1440)

Main discussion topics:

1. Greetings

2. Focus on Seraphis address schemes and hopefully reach some kind of decision (or get closer, maybe narrow down the choices to 2 or 3). [Schemes](https://github.com/monero-project/research-lab/issues/92) [@tevador proposal](https://gist.github.com/tevador/50160d160d24cfc6c52ae02eb3d17024)

3. Adaptive CPU regulation for improved mining performance ( maxwellsdemon )

4. Further analysis of July-Aug 2021 tx volume anomaly ( Isthmus / Mitchellpkt - see [these meeting logs](https://github.com/monero-project/meta/issues/621#issuecomment-948953655)) [Previous analysis](https://mitchellpkt.medium.com/fingerprinting-a-flood-forensic-statistical-analysis-of-the-mid-2021-monero-transaction-volume-a19cbf41ce60) with [Reddit discussion](https://www.reddit.com/r/Monero/comments/pvm634/fingerprinting_a_flood_forensic_statistical/)

5. Improvements to the mixin selection algorithm ( [Decoy Selection Algorithm - Areas to Improve](https://github.com/monero-project/research-lab/issues/86), [JBerman's weekly updates](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/249#note_11480), [Binning PoC](https://github.com/monero-project/research-lab/issues/88), [OSPEAD](https://ccs.getmonero.org/proposals/Rucknium-OSPEAD-Fortifying-Monero-Against-Statistical-Attack.html) ) @j-berman @Rucknium

6. Seraphis/Triptych/Lelantus Spark ( [UkoeHB's Seraphis Proof of Concept work](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/256), [Seraphis repo](https://github.com/UkoeHB/Seraphis), [Lelantus Spark](https://eprint.iacr.org/2021/1173) & [Tripych Multisig](https://github.com/cypherstack/triptych-multisig/blob/main/main.pdf) )

7. MRL META: "Cat herding", i.e. prioritization of research areas and features. Active recruitment of technical talent, MRL structure, funding (@Rucknium & others) [Reddit discussion](https://www.reddit.com/r/Monero/comments/pkg3d6/the_monero_project_should_actively_recruit/)

8. Examine sample size and random seed matters in Monero's unit tests. IRC discussion: [monero-dev](https://libera.monerologs.net/monero-dev/20211018#c39593) , [monero-research-lab](https://libera.monerologs.net/monero-research-lab/20211018)

9. Multisig Drijvers attack mitigation [Technical note](https://github.com/UkoeHB/drijvers-multisig-tech-note) , [Haveno bounty](https://github.com/haveno-dex/haveno/issues/103)

10. Any other business

11. Confirm next meeting agenda


Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: UkoeHB

Previous meeting agenda/logs:

#643 

# Discussion History
## rottenwheel | 2022-01-05T07:22:53+00:00
@Rucknium Thanks. Looking forward to the meeting in a few hours; if I am not present, I will catch up with meeting logs once they get posted on here.

Can you or @UkoeHB please reply and tag me when you all decide on next meeting time and date? If it is next week, on Wednesday 01/12, that would help me to include it in [Revuo Issue 102](https://localmonero.co/revuo) that is getting posted this Sunday 01/09. Just trying to bring more people in and not miss any forthcoming monero- meetings. Thanks.

## Rucknium | 2022-01-05T12:42:20+00:00
@rottenstonks We have had an unbroken streak of MRL meetings every Wednesday at 17:00 UTC going back to September. I think we are going to keep the streak going! Next meeting will be Wednesday January 12 17:00 UTC.

## UkoeHB | 2022-01-05T18:02:06+00:00
```
[01-05-2021 15:09:47] <UkoeHB> meeting 2hr https://github.com/monero-project/meta/issues/646
[01-05-2021 16:38:22] <tevador> Today I cannot make the meeting, so here is a summary: I've phased out merchant wallets in favor of a unified key hierarchy. This is better for UX (users won't have to decide which type of wallet they need) and also for privacy (all wallets have unlinkable addresses by default).
[01-05-2021 16:38:34] <tevador> There are now 7 different wallet tiers: https://gist.github.com/tevador/50160d160d24cfc6c52ae02eb3d17024#46-wallet-access-tiers
[01-05-2021 16:38:44] <UkoeHB> thanks tevador :) it's looking good, I just left some comments
[01-05-2021 16:39:33] <tevador> I've also slightly changed the key derivation function by padding the secret key to the hash block length. This should be more secure. A new recoverable signature scheme for addresses is documented in chapter 3.4.
[01-05-2021 16:40:10] <tevador> I'm now working on a different address encoding scheme based on some feedback. The address prefix will be more human-readable. Also all addresses will contain a signature, making them somewhat longer (about 188 characters), but this leads to an overall more robust and simpler design.
[01-05-2021 16:57:36] <rbrunner> Those tiers seem to multiply like rabbits
[01-05-2021 17:00:36] <UkoeHB> meeting time: https://github.com/monero-project/meta/issues/646
[01-05-2021 17:00:36] <UkoeHB> 1. greetings
[01-05-2021 17:00:36] <UkoeHB> hello
[01-05-2021 17:01:01] <Rucknium[m]> Hi
[01-05-2021 17:01:09] <rbrunner> Hi there
[01-05-2021 17:01:58] <gingeropolous> hi
[01-05-2021 17:03:46] <UkoeHB> 2. updates: anyone working on stuff they want to mention? tevador gave his update just before the meeting
[01-05-2021 17:04:10] <UkoeHB> me: nothing to really update here; I am revising my wallet architecture based on tevador's ongoing work
[01-05-2021 17:05:28] <Rucknium[m]> I am doing chain analysis work on BCH with the `igraph` R package. The packages is fast and fairly memory efficient. I think that it could be used to answer some Monero transaction graph questions that people sometimes muse about.
[01-05-2021 17:06:32] <rbrunner> Have a quick example for such a question?
[01-05-2021 17:06:51] <Rucknium[m]> Basically, questions about how intertwined the Monero "transaction graph" is, and how quickly a new output is intertwined.
[01-05-2021 17:07:15] <Rucknium[m]> I am starting on the effort to get merchant input on Seraphis address schemes, but I think I should wait until the "menu" becomes stable.
[01-05-2021 17:07:45] <rbrunner> 7 entries and counting
[01-05-2021 17:08:34] <rbrunner> You mean this from earlier in the log, right? https://gist.github.com/tevador/50160d160d24cfc6c52ae02eb3d17024#46-wallet-access-tiers
[01-05-2021 17:09:03] <jberman[m]> I've been working on subaddress support in monero-lws, I hit a point where I feel it makes sense to submit a proposal for lightwallet servers generally to support subaddresses in a clean way. planning to submit it today
[01-05-2021 17:09:17] <Rucknium[m]> rbrunner: Given a particular output (i.e. vertex/node) of a particular age, what proportion of the Monero transaction graph can be reached from that vertex/node?
[01-05-2021 17:09:27] <Rucknium[m]> In other words, what is the anonymity set of that output?
[01-05-2021 17:09:43] <rbrunner> I see
[01-05-2021 17:12:35] <rbrunner> 4.5 key hierarchy is also golden in Tevador's linked gist. My, we will have so many secret keys, they build hierarchies :)
[01-05-2021 17:12:50] <UkoeHB> cool jberman[m] thanks :)
[01-05-2021 17:13:32] <UkoeHB> rbrunner: I think this hierarchy will be final, there isn't much more you can extend it to do (if anything).
[01-05-2021 17:14:08] <rbrunner> Comforting, in a way. I hope well get all this complexity properly under control, that's all I worry.
[01-05-2021 17:14:22] <rbrunner> It's fascinating of course, functionality-wise
[01-05-2021 17:14:47] <rbrunner> How high we will tower over other coins with these capabilities?
[01-05-2021 17:15:17] <Rucknium[m]> Once I pause my BCH work again, I will return to making the OSPEAD technical specification more layperson-friendly and then publicly release it. If anyone wants to give input on the draft, just let me know and I will send it your way.
[01-05-2021 17:17:37] <UkoeHB> 3. discussion; any discussion items? perhaps from the agenda? questions about JAMTIS maybe?
[01-05-2021 17:17:45] <zkao> jberman[m]: awesome! TheCharlatan has an open pull request integrating lws in farcaster (he wrote a client lib in rust https://github.com/TheCharlatan/monero-lws-rs)
[01-05-2021 17:19:38] <rbrunner> Those lightwallet servers will also have to catch up to JAMTIS or whatever will get built?
[01-05-2021 17:20:05] <rbrunner> Guess so, implementing some of those tiers
[01-05-2021 17:20:39] <Rucknium[m]> UkoeHB: About your proposal to relax the 10 block lock: It seems that people do not compromise on ring signatures in order to enable quick spending. So somehow we need to figure out how to keep ring sigs but eliminate the 10 block lock.
[01-05-2021 17:20:47] <Rucknium[m]> Which is what makes it an open research question.
[01-05-2021 17:20:52] <moneromooo> We might want to clearly separate a jamtis address and its optional associated data like recipeint ids, invoices, etc. This would avoid the problems users have with integrated addresses, where people see two distinct addresses that are the same under the hood.
[01-05-2021 17:21:39] <moneromooo> The CRC can still encompass the whole address.
[01-05-2021 17:21:50] <endogenic> there may be other ways to accomplish quick spending such as batched chained payments or multiple outs on a single tx
[01-05-2021 17:21:53] <moneromooo> the whle address + remainder.
[01-05-2021 17:22:50] <endogenic> re keeping ring sigs, or we eliminate them :)
[01-05-2021 17:22:59] <endogenic> it's about time we prioritized that
[01-05-2021 17:23:14] <UkoeHB> I don't have a lot of optimism, but let me know if you have any ideas.
[01-05-2021 17:23:25] <endogenic> any fingerprintability should be a priority to eliminate for us right?
[01-05-2021 17:23:37] <rbrunner> Right, we have quite a number of people freaking out a little when the integrated address is not equal to the "base" address they see e.g. on their ledger
[01-05-2021 17:23:45] <Rucknium[m]> I'll remind everyone that MRL is not systematically monitoring the academic literature about Monero, and solutions to our problems like the 10 block lock may lie in that literature. I still have the moneroresearch.wtf domain name, which hopefully will be Where To Find Monero Research in the future.
[01-05-2021 17:23:48] <endogenic> ring sigs are cans of worms in that regard with open vulns
[01-05-2021 17:24:16] <endogenic> Rucknium[m]: i'd say MRL should and has had that in its mandate - to stay up to date on the lit
[01-05-2021 17:26:10] <Rucknium[m]> endogenic: Sure, but you need the resources to do it. We don't have the resources at the moment.
[01-05-2021 17:26:17] <endogenic> sure we do
[01-05-2021 17:26:25] <endogenic> we dont have the researchers to do it
[01-05-2021 17:26:50] <UkoeHB> MRL isn't an entity, if you want to read papers then go do it
[01-05-2021 17:27:02] <endogenic> indeed
[01-05-2021 17:27:27] <gingeropolous> is there a pubmed equivalent for math/crypto ??
[01-05-2021 17:27:40] <rbrunner> If one wanted to have a look, is there a go-to web address?
[01-05-2021 17:27:47] <zkao> Usually one uses adaptor signatures for parallel composition of txs (independent outputs), and tx chaining for serial composition (dependent outs)
[01-05-2021 17:27:54] <moneromooo> arxiv has a number of preprints.
[01-05-2021 17:28:07] <moneromooo> "pre" being importand here.
[01-05-2021 17:28:13] <rbrunner> So the bleeding edge?
[01-05-2021 17:28:44] <Rucknium[m]> By resources I meant researchers. But last time I said "human resources" people didn't like that term.
[01-05-2021 17:28:54] <gingeropolous> :)
[01-05-2021 17:28:58] <rbrunner> Lol
[01-05-2021 17:29:07] <moneromooo> You... you... consumer...
[01-05-2021 17:30:45] <Rucknium[m]> And don't get me started on human capital...
[01-05-2021 17:31:15] <UkoeHB> ok it seems like we are out of topics, how about we end the meeting here?
[01-05-2021 17:31:26] <endogenic> thanks koe
[01-05-2021 17:33:18] <Rucknium[m]> rbrunner: It's not just cryptography that "may be" useful to Monero is being published. People are writing on Monero specifically and we aren't checking what they are saying, which is both an opportunity and a threat vector
[01-05-2021 17:33:21] <Rucknium[m]> See https://scholar.google.com/scholar?as_ylo=2021&q=monero
[01-05-2021 17:36:03] <gingeropolous> i mean, so would moneroresearch.wtf simply have the results of that google scholar output? maybe curated a bit to weed out stuff?
[01-05-2021 17:39:42] <Rucknium[m]> The rough idea is yes, basically that. Curated and commented, categorized. Mostly for "internal" use, but we can direct potential new researchers there too.
[01-05-2021 17:41:26] <UkoeHB> tevador: new architecture diagram https://www.irccloud.com/pastebin/pXIH9Mfj/
[01-05-2021 17:45:06] <UkoeHB> My idea is RPC can wrap the WalletManager
[01-05-2021 17:46:54] <wernervasquez[m]> When would be a good time to consider (can? should?) using ristretto? Do any of the upcoming changes lend themselves to such an additonal change?
[01-05-2021 17:48:17] <UkoeHB> Now is probably a good time to consider it, if ever. The amount of work to implement and audit it would be significant though.
[01-05-2021 17:50:48] <maxwellsdemon[m]> i do want to follow up regarding the DAA discussion from a few weeks ago
[01-05-2021 17:50:52] <maxwellsdemon[m]> if time permits
[01-05-2021 17:52:21] <UkoeHB> go for it
[01-05-2021 17:54:07] <wernervasquez[m]> I'd be curious about the overall performance changes with ristretto. The equality check is faster. I am assuming the current key image check would be replaced by some part of ristretto.
[01-05-2021 17:57:04] <UkoeHB> I think overall the effect would be small, since tx verification/construction is dominated by membership proofs and range proofs.
```

# Action History
- Created by: Rucknium | 2022-01-04T16:29:47+00:00
- Closed at: 2022-01-08T16:26:40+00:00
