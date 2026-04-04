---
title: Monero Research Lab Meeting - Wed 25 May 2022 @ 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/709
author: Rucknium
assignees: []
labels: []
created_at: '2022-05-24T18:05:43+00:00'
updated_at: '2022-05-30T19:00:52+00:00'
type: issue
status: closed
closed_at: '2022-05-30T19:00:52+00:00'
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

6. Examine sample size and random seed matters in Monero's unit tests. IRC discussion: [monero-dev](https://libera.monerologs.net/monero-dev/20211018#c39593) , [monero-research-lab](https://libera.monerologs.net/monero-research-lab/20211018)

7. Multisig Drijvers attack mitigation [Technical note](https://github.com/UkoeHB/drijvers-multisig-tech-note) , [Haveno bounty](https://github.com/haveno-dex/haveno/issues/103)

8. Any other business

9. Confirm next meeting agenda


Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: UkoeHB

Previous meeting agenda/logs:

#706 

# Discussion History
## UkoeHB | 2022-05-25T18:14:43+00:00
```
[05-25-2022 17:00:02] <UkoeHB> meeting time: https://github.com/monero-project/meta/issues/709
[05-25-2022 17:00:02] <UkoeHB> 1. greetings
[05-25-2022 17:00:02] <UkoeHB> hello
[05-25-2022 17:00:19] <jberman[m]> hello
[05-25-2022 17:00:23] <rbrunner> Hi there
[05-25-2022 17:00:34] <xmr-ack[m]> Hi
[05-25-2022 17:00:47] <gingeropolous> o/
[05-25-2022 17:01:35] <Rucknium[m]> Hi
[05-25-2022 17:02:16] <dangerousfreedom> Hello
[05-25-2022 17:02:41] <merope> Hello
[05-25-2022 17:02:54] <UkoeHB> 2. updates; what is everyone working on?
[05-25-2022 17:04:04] <dspringer71[m]> hello
[05-25-2022 17:04:19] <UkoeHB> me: working on seraphis enote scanning workflow, and in the middle of a detour to rework the tx building workflows for this https://gist.github.com/tevador/50160d160d24cfc6c52ae02eb3d17024?permalink_comment_id=4176179#gistcomment-4176179
[05-25-2022 17:05:05] <xmr-ack[m]> Me: lots of travel this last week, but continuing to work on feature engineering. Neptune is helping me out with setting up a database with all references to decoy occurrences on chain.
[05-25-2022 17:06:08] <jberman[m]> mainly been working through understanding the changes to the server code in 7760, stepping through old and new code with provided tests + setting up my own mini boost asio test env to figure it out. taking me quite a bit to get up to speed with boost asio but making progress
[05-25-2022 17:06:14] <dangerousfreedom> I will hand my first delivery for the first part of my ccs next week. I believe I understand MLSAG and the first rangeproofs. I will be working on CLSAG and Bulletproofs next month. Meanwhile, I have been scanning the blockchain looking for some leaks or strange things that could lead to inflation. I have to thank gingeropolous because now my work is much faster as I have access to some computing resources :)
[05-25-2022 17:06:53] <Rucknium[m]> Doing some statistical analysis of personal characteristics that are associated with using cryptocurrency as a means of payment, based on the U.S. Federal Reserve's recently-released Survey of Household Economics and Decisionmaking 2021 microdata. Preliminary results suggest that financial marginalization is positively correlated with use of cryptocurrency as a means of payment in the U.S., somewhat to my surprise. I think I can
[05-25-2022 17:06:53] <Rucknium[m]> push something out by tomorrow.
[05-25-2022 17:09:21] <UkoeHB> thanks for the updates
[05-25-2022 17:09:28] <UkoeHB> 3. discussion, anything to discuss?
[05-25-2022 17:09:32] <mj-xmr[m]> I've been busy preparing the 1st milestone of SolOptXMR with endor00 . After this, I'll return to my decoy task.
[05-25-2022 17:10:55] <rbrunner> Do you expect any more changes to #8149, or do you think it's complete now? Was somewhat surprised to see how much changed 2 days ago.
[05-25-2022 17:10:59] <UkoeHB> For seraphis, I want to emphasize that the update I mentioned basically kills collaborative funding and isolated enotes. Those were both mostly 'nice-to-haves', so while unfortunate I'm not that sad. My multisig verification code is a lot easier with this.
[05-25-2022 17:11:43] <UkoeHB> rbrunner: no more changes. I rolled back some stuff I shoved in their since it was out of scope.
[05-25-2022 17:11:48] <UkoeHB> there*
[05-25-2022 17:12:16] <rbrunner> Ok, thanks
[05-25-2022 17:12:52] <Rucknium[m]> dangerousfreedom: Thanks. Any non-uniformities in the transactions that are in the cryptography (like you have already found) can be beneficial for identifying nonstandard wallet implementations. So keep collecting them :) 
[05-25-2022 17:13:24] <UkoeHB> does anyone have more opinions about https://github.com/monero-project/monero/issues/8351 ?
[05-25-2022 17:14:21] <jberman[m]> UkoeHB: can you give a refresher description of isolated enotes/what functionality would be lost as a result? 
[05-25-2022 17:14:27] <dangerousfreedom> Thanks, so far I have some issues with these stealth addressess being outside the prime group. They can be members of ring signatures later and then compromise fungibility... yeah give your thoughts
[05-25-2022 17:14:28] <Rucknium[m]> UkoeHB: Is collaborative funding something that the underlying cryptography would still support, i.e. is this just a wallet implementation simplification?
[05-25-2022 17:15:55] <UkoeHB> jberman[m]: 'isolated enote' means creating an enote without any surrounding context (no other tx outputs, no tx inputs). There are no known tx engineering protocols that could use that. Now you need to know the full input set when defining your enotes (or block height for coinbase txs).
[05-25-2022 17:17:47] <UkoeHB> Rucknium[m]: previously, collaborative funding could have an easy interface (so it could be supported by the core wallet API), but now you need an interactive protocol between all tx participants (which won't be supported by my PoC, and shouldn't be supported by the core wallet).
[05-25-2022 17:18:22] <UkoeHB> so yes, it can still be done, but it's harder and more constrained
[05-25-2022 17:18:46] <moneromooo> Collaborative funding being... Alice and Bob both sign a ring in the same tx ?
[05-25-2022 17:18:53] <UkoeHB> moneromooo: yes
[05-25-2022 17:22:35] <rbrunner> From what I can grasp right now, I agree with that trade-off: Robust core protocol trumps nice-to-have features as this one
[05-25-2022 17:22:45] <jberman[m]> wouldn't collaborative funding be interactive by definition either way? little confused on that
[05-25-2022 17:25:12] <UkoeHB> jberman[m]: old version: define outputs, publish output set proposal, anyone can send in partial inputs funding the output set; new version: define destination set, define input set, finish defining outputs as function of inputs, make partial inputs, complete tx (so you need to interact with other input contributors + the output set definer in order to make input sigs)
[05-25-2022 17:25:37] <moneromooo> Does Seraphis use bulletproofs ? 
[05-25-2022 17:25:43] <UkoeHB> moneromooo: yes
[05-25-2022 17:26:32] <moneromooo> When I coded collaborative inputs, it turned out it was impossible (as far as Sarang found) to create the BPs without leaking the real spends to other funders.
[05-25-2022 17:27:43] <UkoeHB> not sure why that would be
[05-25-2022 17:27:59] <moneromooo> I couldn't tell you, sorry. I'm just a code monkey :)
[05-25-2022 17:28:04] <UkoeHB> but yeah it does take some careful thought to prevent info leaks
[05-25-2022 17:29:04] <UkoeHB> moneromooo: was it MoJoin?
[05-25-2022 17:29:25] <moneromooo> Oh I think it might have taken that name at some point...
[05-25-2022 17:29:48] <moneromooo> I don't remmeber the timeline tbh.
[05-25-2022 17:30:11] <UkoeHB> the TxTangle protocol in ZtM2 is an evolution on MoJoin, you'd probably need something like that to get collaborative funding with seraphis (maybe a bit simpler though)
[05-25-2022 17:31:22] <moneromooo> Anyway, the reason I mentioned this is (1) it'd be nice to get it and (2) if we use BP anyway, it's already DoA due to the leak anyway so no big loss.
[05-25-2022 17:31:33] <moneromooo> Unless someone found a way to avoid the leak since then.
[05-25-2022 17:32:21] <UkoeHB> it would need to be a third-party solution like atomic swaps
[05-25-2022 17:33:57] <jberman[m]> Losing that collaborative funding flow does seem a bit of an unfortunate loss. sounds like the old could enable a nicer crowdfunding model (something Rucknium has brought up in the past about an approach to CCS that doesn't involve trusted parties e.g.)
[05-25-2022 17:34:20] <UkoeHB> yeah it was originally inspired by Rucknium[m]'s comments
[05-25-2022 17:37:39] <Rucknium[m]> FWIW, BCH's Flipstarter is basically a third-party implementation. The first generation version of Flipstarter needed some software running on a VPS for the Flipstarter "host" and a plugin on the Electron Cash wallet for donors.
[05-25-2022 17:40:09] <UkoeHB> Any other topics people want to discuss?
[05-25-2022 17:42:21] <UkoeHB> ok I think we can close it out here; thanks for attending everyone
[05-25-2022 17:42:36] <Rucknium[m]> Does anyone have any ideas on "sanity checks" I can run on this Federal Reserve Household Economics data? Basically, what characteristics might we assume be correlated with use of cryptocurrency as a means of payment? I have checked education degree (computer science is the only statistically significant degree associated with use of cryptocurrency as a means of payment) and willingness to take risks (yes, it's positively
[05-25-2022 17:42:37] <Rucknium[m]> correlated).
[05-25-2022 17:42:50] <UkoeHB> nvm meeting continues lol
[05-25-2022 17:42:58] <Rucknium[m]> I want to make sure that the data is not just random responses. So far, the data seems legit.
[05-25-2022 17:43:34] <Rucknium[m]> Also, use of cryptocurrency as a means of payment is associated with lower life satisfaction. That's consistent with everyone's personal experience, right? :P
[05-25-2022 17:43:41] <merope> Usage in DNMs/association with crime, maybe? But I don't know if/how that could be measured
[05-25-2022 17:44:10] <UkoeHB> I'd expect predominantly men age ~18-35
[05-25-2022 17:44:28] <merope> Would be nice to be able to compare fiat usage in criminal activity (as a means of payment) vs crypto criminal activity
[05-25-2022 17:46:31] <Rucknium[m]> UkoeHB: Yes, youth and male are associated with use as a means of payment. In fact, I'm using age in most of my regressions since financial marginalization and age are also likely correlated, so I don't want to introduce omitted variable bias.
[05-25-2022 17:46:31] <merope> Maybe crypto usage vs "tech skills" (not as a degree, but general tech savyness)
[05-25-2022 17:47:38] <dspringer71[m]> <Rucknium[m]> "Does anyone have any ideas on "..." <- How it can be used for cryptocurrency development in the best case ?
[05-25-2022 17:48:38] <Rucknium[m]> endor00: There is a question on device type that was used to complete the survey. So I can look at that. On DNM: I didn't see anything relevant in the data dictionary on that.
[05-25-2022 17:50:04] <Rucknium[m]> dspringer71: Adoption is arguably as difficult as protocol development. We don't understand adoption well. Once it is understood, maybe we can figure out ways to promote it.
[05-25-2022 17:50:49] <Rucknium[m]> Wider adoption improves the anonymity set, enhancing privacy.
[05-25-2022 17:51:02] <UkoeHB> I'd predict that adoption is anti-correlated with promotion lol
[05-25-2022 17:51:22] <dspringer71[m]> Rucknium[m]: Goals of project aren't compatible with wider adoption
[05-25-2022 17:51:47] <merope> Why wouldn't they be?
[05-25-2022 17:52:05] <Rucknium[m]> UkoeHB: Maybe we can eventually test that hypothesis!
[05-25-2022 17:52:24] <UkoeHB> Rucknium[m]: that would really be something to see
[05-25-2022 17:54:01] <UkoeHB> I guess 'grassroots' promotion would be forward-correlated, and any 'centralized' promotion would be anti-correlated.
[05-25-2022 17:54:03] <merope> Oooh, what about usage in large urban areas vs rural areas?
[05-25-2022 17:54:25] <dspringer71[m]> UkoeHB: are there any link to the most comprehensive benchmark for view tag available somewhere ?
[05-25-2022 17:54:56] <UkoeHB> although the causal order between adoption and grassroots promotion is worth pondering
[05-25-2022 17:55:18] <moneromooo> Rucknium[m]: "likes privacy and uses cryptocurrency to give it hard to visa/mastercard spying ops"
[05-25-2022 17:55:39] <moneromooo> (about "what characteristics might we assume be correlated...")
[05-25-2022 17:55:57] <Rucknium[m]> endor00: Yes there is a question on if the survey respondent is in a metropolitan statistical area or not. I'm not sure that would be a data quality check per se, but it would be interesting.
[05-25-2022 17:55:59] <UkoeHB> and the failure of centralized promotion may be as much as, or more than, a symptom of deeper issues
[05-25-2022 17:56:09] <moneromooo> I have low life satisfaction because I realize the world spies on me, indeed.
[05-25-2022 17:57:08] <UkoeHB> wow word salad: as much a symptom as a cause*
[05-25-2022 17:57:31] <moneromooo> There's the good old "works in a sector that's legal but frowned upon".
[05-25-2022 17:57:45] <moneromooo> Like gambling, sex, weapons.
[05-25-2022 17:57:52] <moneromooo> (depending on your jurisdiction
[05-25-2022 17:58:08] <Rucknium[m]> moneromooo: Interesting idea. There are some questions in the survey that may capture how much trust survey respondents have in government and business institutions.
[05-25-2022 17:59:34] <Rucknium[m]> There are some questions on occupation and industry. Sort of broad categories, though, so it may not have "frowned upon" activities isolated well.
[05-25-2022 17:59:36] <moneromooo> An also commonly mention characteristics is "works in a rich country, but family is in a poor country, and money transfer services charge loads (except hawala)).
[05-25-2022 17:59:58] * moneromooo cringes at the grammar in the previous sentence
[05-25-2022 18:00:25] <moneromooo> Might not be "payments" though, depending on how you look at it.
[05-25-2022 18:00:29] <merope> Is there any data about usage of the "frowned upon" services?
[05-25-2022 18:00:42] <moneromooo> Oh, cannabis is a good one probably.
[05-25-2022 18:00:53] <sech1> "works in a rich country, but family is in a poor country" <- but family is in Russia, and money transfer services don't work at all
[05-25-2022 18:01:07] <Rucknium[m]> Respondents that did not have U.S. citizenship were more likely to use cryptocurrency as a means of exchange, according to preliminary results.
[05-25-2022 18:01:17] <moneromooo> Can you sell crypto for roubles in russia nowadays ?
[05-25-2022 18:03:18] <Rucknium[m]> I also have number of years the respondent has lived in the U.S. and language spoken at home, but I have not analyzed them yet.
[05-25-2022 18:03:32] <UkoeHB> ok we are past the hour now; thanks for attending everyone
```

# Action History
- Created by: Rucknium | 2022-05-24T18:05:43+00:00
- Closed at: 2022-05-30T19:00:52+00:00
