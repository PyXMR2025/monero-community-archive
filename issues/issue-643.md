---
title: Monero Research Lab Meeting - Wed 29 December 2021 @ 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/643
author: Rucknium
assignees: []
labels: []
created_at: '2021-12-28T17:00:19+00:00'
updated_at: '2022-01-04T16:37:27+00:00'
type: issue
status: closed
closed_at: '2022-01-04T00:54:22+00:00'
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

#642 

# Discussion History
## Rucknium | 2022-01-04T16:31:27+00:00
The meeting IRC/Matrix log should be posted here as a comment before this issue is closed.

## UkoeHB | 2022-01-04T16:37:27+00:00
```
[01-04-2021 17:00:33] <UkoeHB> meeting time: https://github.com/monero-project/meta/issues/643
[01-04-2021 17:00:34] <UkoeHB> 1. greetings
[01-04-2021 17:00:34] <UkoeHB> hello
[01-04-2021 17:00:48] <tevador> hi
[01-04-2021 17:00:55] <rbrunner> hi
[01-04-2021 17:00:55] <Rucknium[m]> Hi
[01-04-2021 17:01:03] <UkoeHB> tevador: are you planning to change the proposal?
[01-04-2021 17:02:54] <tevador> I'm rewriting it mostly for better readability, but there are also some minor changes
[01-04-2021 17:03:15] <tevador> e.g. the one-time change addresses we discussed earlier
[01-04-2021 17:03:37] <UkoeHB> sounds good
[01-04-2021 17:04:08] <tevador> also added an "xmr" prefix to base58 addresses as per fluffypony's suggestion
[01-04-2021 17:04:29] <tevador> I've also coded a library that will be used for human-readable representation of wallets and addresses: https://github.com/tevador/id32 
[01-04-2021 17:06:18] <UkoeHB> ah interesting
[01-04-2021 17:07:19] <UkoeHB> 2. discussion, does anyone have anything they want to discuss (e.g. from the agenda, or otherwise)? This was Christmas week so it might be a short meeting.
[01-04-2021 17:08:04] <UkoeHB> I have been thinking a little about wallet/account architecture, and made a little progress but still not completely nailed down.
[01-04-2021 17:08:34] <Rucknium[m]> Last meeting we discussed reaching out to merchants and crypto services about the preferences regarding the address schemes. We haven't done anything on that yet, AFAIK.
[01-04-2021 17:09:04] <jberman[m]> I tried gauging the benefit of binning in protecting a user who spends multiple inputs that are close in age in a tx (e.g. collect change outputs over the course of a day, then spend them >2 months later in the same tx), and found that users seem decently well protected in this scenario already, and that binning wouldn't necessarily be of huge help (https://github.com/monero-project/research-lab/issues/86#issuecomment-1001091949)
[01-04-2021 17:09:12] <Rucknium[m]> This would be a good way to have non-devs and non-researchers contribute -- send them forward to query merchants.
[01-04-2021 17:09:47] <jberman[m]> Unless people have objections and want to see the wallet-side binning proposal I shared implemented (https://github.com/monero-project/research-lab/issues/88), I also am leaning toward setting it aside and moving on. It seems like it would be challenging to get everyone on board with it, and the benefits of binning at this stage I don't think are critical
[01-04-2021 17:11:03] <tevador> I think this discussion is being watched by some merchants: https://github.com/monero-project/monero/issues/7889
[01-04-2021 17:11:15] <Rucknium[m]> I think that binning makes more sense once we have a greater number of decoys to work with, which will (hopefully) happen later on with Seraphis. We also need more statistical analysis of the benefits and costs of binning before putting it into production, I think.
[01-04-2021 17:12:12] <rbrunner> " and that binning wouldn't necessarily be of huge help " Was that a surprise to you?
[01-04-2021 17:12:18] <Rucknium[m]> What I am saying is that I would agree with returning binning to the back burner, to pick up later.
[01-04-2021 17:12:26] <rbrunner> Or kind of a disappointment?
[01-04-2021 17:14:17] <jberman[m]> Haha not a disappointment, I think that finding was definitely a good thing. But I did think binning would be of more help in that particular scenario, considering the gamma isn't specifically designed to protect from it
[01-04-2021 17:14:57] <rbrunner> Interesting
[01-04-2021 17:15:36] <Rucknium[m]> This is only relevant to a specific threat model, correct, jberman?
[01-04-2021 17:15:46] <Rucknium[m]> Your most recent findings, that is.
[01-04-2021 17:15:48] <jberman[m]> Yes
[01-04-2021 17:17:50] <UkoeHB> theblackdog001[m: did you have a question?
[01-04-2021 17:18:37] <Rucknium[m]> Are we on target for March 15 hard fork? What more needs to be done?
[01-04-2021 17:19:42] <Rucknium[m]> I guess that's a -dev question, but can MRL help at all?
[01-04-2021 17:20:34] <rbrunner> Maybe multisig is the critical path?
[01-04-2021 17:20:38] <UkoeHB> I think the multisig PRs are close to merge-able, which is good news.
[01-04-2021 17:21:14] <UkoeHB> I will try to get the last review comments from vtnerd wrapped up by this weekend.
[01-04-2021 17:21:18] <rbrunner> Hmm, https://github.com/monero-project/monero/pull/8114 has quite some unaddressed review issues, last time I checked
[01-04-2021 17:21:38] <rbrunner> I wanted to do functional tests, but decided to wait
[01-04-2021 17:22:19] <rbrunner> However don't understand half of the mentioned points :)
[01-04-2021 17:23:08] <UkoeHB> I think most of that is just discussion that doesn't require new diffs
[01-04-2021 17:23:44] <Rucknium[m]> I will ask folks at #monero-ux:monero.social if they can do some outreach to merchants, payment processors, etc regarding their preferences on address schemes.
[01-04-2021 17:23:59] <UkoeHB> thanks Rucknium[m] 
[01-04-2021 17:24:43] <rbrunner> Sounds like a good idea
[01-04-2021 17:36:47] <UkoeHB> Seems like we can close out the meeting. Thanks for attending everyone, and merry christmas :)
```

# Action History
- Created by: Rucknium | 2021-12-28T17:00:19+00:00
- Closed at: 2022-01-04T00:54:22+00:00
