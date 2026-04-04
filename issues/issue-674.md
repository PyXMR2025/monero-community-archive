---
title: Monero Research Lab Meeting - Wed 16 March 2022 @ 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/674
author: Rucknium
assignees: []
labels: []
created_at: '2022-03-16T04:12:21+00:00'
updated_at: '2022-03-23T17:07:43+00:00'
type: issue
status: closed
closed_at: '2022-03-19T04:46:18+00:00'
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

#672 

# Discussion History
## UkoeHB | 2022-03-23T17:07:43+00:00
```
[03-16-2022 17:01:04] <UkoeHB> meeting time: https://github.com/monero-project/meta/issues/674
[03-16-2022 17:01:04] <UkoeHB> 1. greetings
[03-16-2022 17:01:04] <UkoeHB> hello
[03-16-2022 17:01:28] <Rucknium[m]> Hi
[03-16-2022 17:01:33] <rbrunner> Hello
[03-16-2022 17:02:15] <wernervasquez[m]> Hello
[03-16-2022 17:02:46] <chesterfield[m]> Howdy
[03-16-2022 17:02:50] <reeemuru[m]> yo
[03-16-2022 17:04:10] <dangerousfreedom> Cheers
[03-16-2022 17:04:42] <UkoeHB> 2. let's do updates, what is everyone working on?
[03-16-2022 17:05:59] <Rucknium[m]> I am in the "If you see a good move, look for a better one" phase of OSPEAD research that isthmus suggested. I have learned a few things:
[03-16-2022 17:06:23] <UkoeHB> me: still on seraphis multisig; I discovered a multisig protocol flaw that I will quick-fix PR maybe today or tomorrow
[03-16-2022 17:07:11] <Rucknium[m]> 1) To date I have framed my proposed estimations in broad Loss Function terms. It is admittedly a bit ad hoc. However, turns out that it can fit in a much more specific and well-studied Minimum Divergence Estimator framework.
[03-16-2022 17:08:18] <UkoeHB> idk if anyone is interested, but I finally got aggregation-style multisig signing working, two years after first writing about it in ZtM2: https://github.com/UkoeHB/monero/blob/c9e916c60014321144b2522e5aa77608f973bc48/tests/unit_tests/seraphis_multisig.cpp#L183
[03-16-2022 17:08:21] <Rucknium[m]> Without getting too specific, I can use already-established theoretical results on Minimum Divergence Estimators for some benefits.
[03-16-2022 17:09:29] <rbrunner> Means somewhat less work?
[03-16-2022 17:10:00] <rbrunner> Or faster progress, if you like :)
[03-16-2022 17:10:25] <Rucknium[m]> 2) Maybe others are already aware of this framework, but I think overall Monero can be placed into the Local Differential Privacy (LDP) framework. What I find interesting about LDP is that it claims that you can prove that your privacy scheme is immune to both known and as-yet-undeveloped statistical/machine learning attacks.
[03-16-2022 17:11:04] <Rucknium[m]> rbrunner: Yes, a bit less work; more ideas about things to try; and more confidence in the end results.
[03-16-2022 17:11:33] <rbrunner> Nice.
[03-16-2022 17:12:10] <rbrunner> "I discovered a multisig protocol flaw". Was that introduced with your broad rewrite of multisig code?
[03-16-2022 17:15:50] <UkoeHB> No, it is a flaw in all cryptocurrency multisig that I know of. Basically it isn't safe to send funds to a multisig address unless you are confident that all participants have completed their multisig accounts (or can complete them). One player can complete their account but then a malicious player 'forgets' to send their last kex message to other participants... preventing them from completing their accounts (and hence 
[03-16-2022 17:15:50] <UkoeHB> making them unable to sign things).
[03-16-2022 17:17:03] <rbrunner> Hmm, yes. And something can get improved here?
[03-16-2022 17:17:06] <UkoeHB> The quick fix is to add a round where you get confirmation from all players that they have completed their accounts.
[03-16-2022 17:17:57] <rbrunner> Well, maybe from the minimum of signers that is necessary? E.g. 2 in 2/3?
[03-16-2022 17:17:58] <UkoeHB> The fix that is friendly to UX of escrowed markets (i.e. doesn't add a round)... is kinda hairy.
[03-16-2022 17:19:17] <UkoeHB> rbrunner: no, you need all participants since the 'security guarantee' of multisig is you can have up to `min(M, N - M + 1)` dishonest participants
[03-16-2022 17:20:17] <UkoeHB> if you just check one other player in 2-of-3, that might be the dishonest guy who can block you
[03-16-2022 17:21:07] <rbrunner> Looks like it. I have to think about it. I am little afraid that such a "confirmation" round can have other, unintended and unfortunate consequences
[03-16-2022 17:21:18] <rbrunner> but can't play my finger on it yet
[03-16-2022 17:21:35] <rbrunner> *place
[03-16-2022 17:21:43] <UkoeHB> it sucks for UX, but can be enforced as an invariant in the multisig account implementation
[03-16-2022 17:23:12] <Rucknium[m]> UkoeHB: Do you think this will be required as a blockchain consensus rule, or be a wallet-level requirement?
[03-16-2022 17:23:27] <UkoeHB> it is wallet-side
[03-16-2022 17:24:03] <rbrunner> I wonder whether this risk is really worth mitigating. We have other such fundamental risks, e.g. you paying into a 2/2 multisig and your partner walking away
[03-16-2022 17:24:54] <rbrunner> Funds locked forever
[03-16-2022 17:25:09] <UkoeHB> yes I think it's a hole that would make a lot of the other work pointless
[03-16-2022 17:26:04] <UkoeHB> N-of-N is not affected, since you can't reduce the 'dishonest participant' assumption below 1 player
[03-16-2022 17:26:36] <UkoeHB> it affects M-of-N, where your security assumption falls from `min(M, N - M + 1)` to 1
[03-16-2022 17:27:37] <UkoeHB> to be clear, there are two security assumptions: 1) dishonest can spend funds (need `M`), 2) dishonest can block all signatures (need `N - M + 1`). It's the second one that is reduced to `1` by this flaw.
[03-16-2022 17:29:53] <rbrunner> Will this technically "look" like 1 more key exchange round? So that handling does not change too much?
[03-16-2022 17:29:59] <rbrunner> Just getting more tedious still
[03-16-2022 17:30:07] <UkoeHB> yes
[03-16-2022 17:30:45] <rbrunner> Alright, does not sound too bad then
[03-16-2022 17:30:49] <UkoeHB> for 2-of-3 escrowed markets, there are some workarounds that avoid the extra round
[03-16-2022 17:31:41] <rbrunner> Well, you have to fully automate anyway for a viable and end-user friendly solution. Think Haveno. Thus I would not worry too much, I would say right now
[03-16-2022 17:32:02] <rbrunner> But tomorrow I claim the opposite :)
[03-16-2022 17:32:16] <UkoeHB> the workarounds just adds a footgun to the interface, which isn't ideal
[03-16-2022 17:33:28] <UkoeHB> anyway, we can move on
[03-16-2022 17:33:37] <UkoeHB> 3. discussion - any other topics to discuss?
[03-16-2022 17:35:02] <Rucknium[m]> I would like to collect information on nonstandard Monero decoy selection algorithms. I am not good at finding and interpreting code in various languages, though, so maybe there are people here that could volunteer to help :)
[03-16-2022 17:35:27] <UkoeHB> do you mean algorithms that have been used?
[03-16-2022 17:35:30] <Rucknium[m]> I can't even figure out how MyMonero does it :/
[03-16-2022 17:35:54] <Rucknium[m]> UkoeHB: Yes. Basically, ones that have been used in the last two years
[03-16-2022 17:36:13] <rbrunner> I think they use `wallet2.cpp` compiled / transpiled either to JavaScript or WASM, thus standard
[03-16-2022 17:36:34] <Rucknium[m]> I suppose I also want to have the very old standard ones, like triangular, since some wallet software out there may be using really only "standard" code
[03-16-2022 17:37:45] <Rucknium[m]> There are also some wallets that are closed source as a whole, like Exodus, but have the Monero part open source, I think. I also couldn't figure out what Exodus was doing.
[03-16-2022 17:38:39] <Rucknium[m]> It is important to assemble a catalogue of all decoy selection algorithms that is as complete as possible.
[03-16-2022 17:39:44] <rbrunner> I try to get an overview for all wallets right now, for my "No wallet left behind" push. I can report if I find something non-standard. 0 zero far, however
[03-16-2022 17:40:42] <Rucknium[m]> rbrunner: Thank you :)
[03-16-2022 17:43:32] <Rucknium[m]> Ok I made an issue to start organizing the info:
[03-16-2022 17:43:32] <Rucknium[m]> https://github.com/monero-project/research-lab/issues/99
[03-16-2022 17:48:43] <UkoeHB> any more last-minute topics to discuss? otherwise we can call it here
[03-16-2022 17:49:23] <UkoeHB> shameless plug: my seraphis wallet poc ccs has moved to funding https://ccs.getmonero.org/funding-required/
[03-16-2022 17:53:43] <SerHack> thanks for the meeting
[03-16-2022 17:58:19] <UkoeHB> ok guess we are done, thanks for attending everyone
```

# Action History
- Created by: Rucknium | 2022-03-16T04:12:21+00:00
- Closed at: 2022-03-19T04:46:18+00:00
