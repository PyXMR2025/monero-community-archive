---
title: Monero Research Lab Meeting - Wed 09 February 2022 @ 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/662
author: Rucknium
assignees: []
labels: []
created_at: '2022-02-08T00:57:54+00:00'
updated_at: '2022-02-11T19:11:47+00:00'
type: issue
status: closed
closed_at: '2022-02-11T19:11:47+00:00'
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

#657 

# Discussion History
## UkoeHB | 2022-02-09T17:58:47+00:00
```
[02-09-2022 17:00:29] <UkoeHB> meeting time: https://github.com/monero-project/meta/issues/662
[02-09-2022 17:00:29] <UkoeHB> 1. greetings
[02-09-2022 17:00:29] <UkoeHB> hello
[02-09-2022 17:00:35] <ArticMine> Hi
[02-09-2022 17:00:38] <mj-xmr[m]> hi
[02-09-2022 17:00:40] <rbrunner> Hello
[02-09-2022 17:01:31] <xmr-ack[m]> Hola
[02-09-2022 17:01:37] <gingeropolous> oh hai
[02-09-2022 17:02:29] <jberman[m]> howdy
[02-09-2022 17:03:09] <Rucknium[m]> Hi
[02-09-2022 17:03:12] <UkoeHB> 2. Today I don't think there are any pressing agenda items. Let's start with updates. What has everyone been busy with?
[02-09-2022 17:03:51] <mj-xmr[m]> I've done a review for Ruck's paper over the weekend.
[02-09-2022 17:05:26] <Rucknium[m]> I have a draft of the MAGIC Monero Fund research request for proposals. Suggestions/edits welcome:
[02-09-2022 17:05:26] <Rucknium[m]> https://cryptpad.sethforprivacy.com/pad/#/2/pad/view/SBQRrOt+Vd6Bbr0nJHA6eNQtnMaTS-kPLWtvtVbAlAA/
[02-09-2022 17:05:48] <Rucknium[m]> I think we will approve a final draft by early next week and start accepting applications.
[02-09-2022 17:06:44] <xmr-ack[m]> I’ve been working on the dataset collection part of my research project. Have 5 servers right now running a collective 900 wallets that are transferring testnet xmr back and forth. I’ve also been working on polishing up a script to extract all the transaction metadata using xmr2csv and the native monero-wallet-cli exporter. Hopefully will have a full dataset by the end of the month and then can start neural network design.
[02-09-2022 17:06:47] <jberman[m]> reviewed the fee change PR, will be re-reviewing changes today, and various monero-lws related stuff (thinking through subaddress support, submitted a first pass general review of the code, getting a docker image set up)
[02-09-2022 17:07:33] <ArticMine> Very good catch on the fee pr
[02-09-2022 17:07:40] <UkoeHB> me: After a couple weeks of work I now have unit tests running on the main part of jamtis (along with some refactors of my seraphis library). I am pretty satisfied with the library as it is now (although it is missing multisig stuff, which I won't add until PR 7877 is merged - getting close on that one, I just need to do a little cleanup and get final approvals from h4sh3d and vtnerd). My next steps are implementing 
[02-09-2022 17:07:40] <UkoeHB> some grootle proof optimizations that the Firo team found, rerun perf tests for that, then start thinking about the larger wallet PoC (I might make a new CCS for this, since I used up all my hours on the previous one).
[02-09-2022 17:10:47] <Rucknium[m]> UkoeHB: There were some things brought up on Reddit recently regarding how the address format change will affect future improvements. Do you have any insight on whether the Seraphis address change can be compatible with something like Zcash's Halo2 down the road?
[02-09-2022 17:10:59] <UkoeHB> No idea
[02-09-2022 17:12:16] <UkoeHB> If there is anyone out there who actually understands Halo2, would be nice to learn/hear from them... I don't recall ever seeing such a person
[02-09-2022 17:13:22] <rbrunner> Even without knowing any details, strikes me as improbable, with all that specific keys in the public Seraphis addresses, but yeah, who knows
[02-09-2022 17:13:49] <jberman[m]> I thought one of the critical ideas of Seraphis' tx modularity was to possibly enable an easier swap-in of something like full-chain membership proofs
[02-09-2022 17:14:14] <UkoeHB> It would be ideal if we could layer their proving stuff on top of Seraphis, to do the membership proof piece without changing anything else.
[02-09-2022 17:14:50] <rbrunner> At least some people there were worried about changing their public Monero addresses yet again if we switch to something post-Seraphis later
[02-09-2022 17:14:50] <UkoeHB> But 'Halo2' is a quite opaque word lol, so who knows
[02-09-2022 17:15:27] <rbrunner> And there I think it's improbable to keep addresses and switch to very different proofs underneath
[02-09-2022 17:16:13] <UkoeHB> Yep it's certainly possible, though I wouldn't really expect anything like that for another 3-5 years at least.
[02-09-2022 17:16:46] <rbrunner> May depend in how positive a light one sees Seraphis :)
[02-09-2022 17:17:05] <rbrunner> "Gras always greener over there"
[02-09-2022 17:18:35] <rbrunner> In any case we will collect experience with the address change ...
[02-09-2022 17:19:26] <UkoeHB> yep...
[02-09-2022 17:19:40] <rbrunner> Just a thought: It is probably possible to write a tool that calculates a Seraphis address for a given private key, maybe quite soon, right?
[02-09-2022 17:19:41] <UkoeHB> Does anyone have anything they want to discuss? Questions? Concerns?
[02-09-2022 17:20:08] <UkoeHB> rbrunner: I think tevador was working on test vectors...
[02-09-2022 17:20:39] <rbrunner> Interesting.
[02-09-2022 17:20:39] <UkoeHB> Uh if someone wants to take my library and add a PoC for generating public addresses, that might be fine
[02-09-2022 17:20:54] <rbrunner> Code is there then already?
[02-09-2022 17:20:58] <UkoeHB> Public addresses are a bit higher on the stack, so I haven't looked at it yet
[02-09-2022 17:21:17] <UkoeHB> But I have code to generate the address points.
[02-09-2022 17:21:49] <rbrunner> Was just thinking it may help in the address switch process if people were able to publish their new addresses months before the hardfork already, to seed them wide and far
[02-09-2022 17:22:34] <UkoeHB> this guy: https://github.com/UkoeHB/monero/blob/da0c5db016a5b25199054284902aca2b0c9588cf/src/seraphis/jamtis_destination.h#L91
[02-09-2022 17:23:05] <mj-xmr[m]> UkoeHB: Minor and somehow related to @maxwellsdemon 's adaptive mining proposal: I'll be building a small solar battery island as a test bed for the prediction (via tsqsim) of solar irradiation and battery load / drainage. The prediction will serve as an input signal to whatever controls the mining intensity.
[02-09-2022 17:23:11] <UkoeHB> Well there might be format changes, so I think it's better to wait a while for that rbrunner 
[02-09-2022 17:23:30] <rbrunner> Yes of course. That's probably next year's stuff. Just thinking ahead :)
[02-09-2022 17:25:52] <UkoeHB> mj-xmr[m]: I see
[02-09-2022 17:27:07] <gingeropolous> whats the word on memo fields / tx_extra?
[02-09-2022 17:27:47] <Rucknium[m]> What I like about the "On Defeating Graph Analysis of Anonymous Transactions" paper posted earlier is that it starts to get at the question of how many ring members is "enough", at least to defeat specific types of attacks. So if Seraphis gets us to "enough", then that would be great. If it doesn't, then we should still be thinking about the next generation + 1
[02-09-2022 17:28:14] <UkoeHB> gingeropolous: what word?
[02-09-2022 17:28:14] <rbrunner> A long time since tx_extra came up the last time, as far as I remember
[02-09-2022 17:30:24] <gingeropolous> well i guess the question is whether jamtis has a useful memo field that can be done in a way that keeps all txs uniform
[02-09-2022 17:31:20] <UkoeHB> like encrypted or something?
[02-09-2022 17:31:56] <UkoeHB> I was planning to use the existing tx_extra strategy, with some additional rules about formatting (sorted TLV, like I have been preaching for years).
[02-09-2022 17:32:01] <Rucknium[m]> Regarding understanding Halo2, I have found Zcash developers are generally willing to explain things, on their Discourse forum or their R&D Discord. Maybe they could tell us what sort of restrictions apply to their address format.
[02-09-2022 17:32:20] <UkoeHB> Also, moving the tx pubkeys out of the tx_extra into a dedicated vector.
[02-09-2022 17:33:17] <rbrunner> What means "TLV"?
[02-09-2022 17:34:20] <UkoeHB> type-length-value
[02-09-2022 17:34:30] <UkoeHB> tx_extra is already tlv
[02-09-2022 17:34:43] <UkoeHB> by convention*
[02-09-2022 17:36:31] <gingeropolous> ok, so as of now, tx_extra will live on as it is and possibly harbor fingerprints if ppl glob it up with stuff
[02-09-2022 17:36:42] <zkao> we're using TLV in farcaster for the peer messages
[02-09-2022 17:37:37] <UkoeHB> gingeropolous: yes
[02-09-2022 17:37:46] <gingeropolous> then thats the word :)
[02-09-2022 17:37:50] <rbrunner> By the way, just saw that Halo2 isn't even live on mainnet yet: "The new mainnet activation target is April 18, 2022."
[02-09-2022 17:38:06] <UkoeHB> don't they have it on testnet?
[02-09-2022 17:38:16] <rbrunner> Yes, that.
[02-09-2022 17:38:22] <UkoeHB> do they actually have public code for everything?
[02-09-2022 17:38:48] <rbrunner> Never checked
[02-09-2022 17:39:23] <gingeropolous> Rucknium[m], can u link that pdf again for "On Defeating Graph Analysis of Anonymous Transactions"
[02-09-2022 17:39:33] <gingeropolous> please :)
[02-09-2022 17:39:43] <jberman[m]> this seems a decent resource on halo2: https://zcash.github.io/halo2/ 
[02-09-2022 17:40:40] <Rucknium[m]> gingeropolous: https://eprint.iacr.org/2022/132
[02-09-2022 17:42:27] <gingeropolous> danke
[02-09-2022 17:43:36] <gingeropolous> getting to "enough" would be .... great :) 
[02-09-2022 17:46:01] <UkoeHB> Btw, there has been some effort by Firo/Mobilecoin toward confidential assets, if anyone is interested: https://github.com/mobilecoinfoundation/mcips/pull/25#issuecomment-1033194827 .
[02-09-2022 17:47:42] <UkoeHB> Basically, it can be done extremely cheaply but runs into problems with tx fees.
[02-09-2022 17:48:14] <gingeropolous> is this like creating your own tokens on the monero chain or something?
[02-09-2022 17:48:20] <UkoeHB> yeah
[02-09-2022 17:51:03] <gingeropolous> and so the great compromise of 2022 left us with 1.7 ..... ?
[02-09-2022 17:51:22] <UkoeHB> fee scaling? yes
[02-09-2022 17:51:26] <Rucknium[m]> FYI, some people are also developing something similar on Zcash called Zcash Shielded Assets (ZSA).
[02-09-2022 17:51:41] <UkoeHB> oh yeah thanks Rucknium[m] 
[02-09-2022 17:52:36] <rbrunner> Don't want to miss the DeFi train, maybe. Too much money sloshing around in attempts to find a home ...
[02-09-2022 17:52:44] <gingeropolous> lulz
[02-09-2022 17:53:10] <rbrunner> And when can I finally have NFTs on the Monero blockchain. It's about time :)
[02-09-2022 17:53:11] <UkoeHB> I think fees can be solved by requiring you add some base-asset inputs/outputs to all asset transfers. So a tx would have a 'base asset transfer' section and 'extra asset transfer'  section.
[02-09-2022 17:53:53] <UkoeHB> Realistically, miners can't be expected to care about random assets people make, so fees should always be in the base asset.
[02-09-2022 17:54:04] <gingeropolous> yeah
[02-09-2022 17:55:08] <UkoeHB> rbrunner: It doesn't help with scaling though... imo we should maximize the utility of one asset.
[02-09-2022 17:55:54] <gingeropolous> oooh, i know a fun one for the last 5 minutes. any new ideas on the 10 block lock thing?
[02-09-2022 17:56:02] <UkoeHB> no
[02-09-2022 17:57:33] <UkoeHB> ok lol I think we can call it here
[02-09-2022 17:57:37] <UkoeHB> Thanks for attending everyone
```

# Action History
- Created by: Rucknium | 2022-02-08T00:57:54+00:00
- Closed at: 2022-02-11T19:11:47+00:00
