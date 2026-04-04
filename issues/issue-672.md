---
title: Monero Research Lab Meeting - Wed 09 March 2022 @ 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/672
author: Rucknium
assignees: []
labels: []
created_at: '2022-03-09T16:49:52+00:00'
updated_at: '2022-03-16T04:12:30+00:00'
type: issue
status: closed
closed_at: '2022-03-16T04:12:30+00:00'
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

#669 

# Discussion History
## UkoeHB | 2022-03-09T17:42:14+00:00
```
[03-09-2022 17:00:15] <UkoeHB> meeting time: https://github.com/monero-project/meta/issues/672
[03-09-2022 17:00:22] <UkoeHB> 1. greetings
[03-09-2022 17:00:22] <UkoeHB> hello
[03-09-2022 17:00:47] <rbrunner> Hi
[03-09-2022 17:00:52] <Rucknium[m]> Hi
[03-09-2022 17:02:15] <xmr-ack[m]> Hey
[03-09-2022 17:02:50] <jberman[m]> howdy
[03-09-2022 17:04:43] <UkoeHB> 2. not sure if there are any active topics to discuss; we can at least do updates, what has everyone been working on?
[03-09-2022 17:06:18] <UkoeHB> me: I rebased seraphis_lib onto master and started working on multisig seraphis txs, which will use the new multisig_account interface
[03-09-2022 17:07:05] <jberman[m]> noice
[03-09-2022 17:07:58] <jberman[m]> me: been working on background sync mode mostly
[03-09-2022 17:09:29] <Rucknium[m]> I was thinking: do people think it would be a good idea to try to estimate the effect of minexmr's upcoming change of fee from 1% to 1.1%? The price elasticity of supply, if you will?
[03-09-2022 17:10:03] <UkoeHB> to what end?
[03-09-2022 17:10:08] <Rucknium[m]> I could use some time series statistics. Could be a fun and illuminating project.
[03-09-2022 17:10:44] <Rucknium[m]> To figure out how much of an effect the fee raise has, in terms of pool share of hashpower.
[03-09-2022 17:11:02] <rbrunner> You mean in advance, some sort of prediction?
[03-09-2022 17:11:07] <UkoeHB> Oh you mean an empirical estimate, not prediction?
[03-09-2022 17:11:29] <Rucknium[m]> Since people have been trying to come up with a way to reduce hashpower concentration, and increasing the fee is one possibility.
[03-09-2022 17:11:41] <Rucknium[m]> Yes, empirical. Ex-post.
[03-09-2022 17:12:15] <UkoeHB> I suppose it would be interesting
[03-09-2022 17:12:44] <rbrunner> I am a bit confused - is this more than compare hashrate before / after?
[03-09-2022 17:13:28] <Rucknium[m]> rbrunner: Right. Determine what effect, if any, the fee increase has on minexmr's share of the hashrate.
[03-09-2022 17:14:02] <Rucknium[m]> Since in general we may expect that increasing the fee would cause some miners to shift to lower-fee pools.
[03-09-2022 17:14:08] <rbrunner> Well, yes, I just fail to see where interesting statistics and math come into play
[03-09-2022 17:14:24] <rbrunner> Hasharate after minus hashrate before...?
[03-09-2022 17:14:38] <rbrunner> I am sure I don't yet fully understand your proposal :)
[03-09-2022 17:15:23] <w[m]> Watching minexmr HR, it changes pretty wildly regardless of the fee.
[03-09-2022 17:15:23] <w[m]> Would be nice to see if there was a net loss of hr etc? But I think 0.1% isnt enough to discourage bot runners, that are already selling below cost.
[03-09-2022 17:15:23] <w[m]> If minexmr was the most expensive pool, I think we may see a difference. But 0.1% isnt much, considering a lot of people from xmrig binary and pay 1% ontology already 
[03-09-2022 17:15:34] <w[m]> s/If minexmr was the most expensive pool, I think we may see a difference. But 0.1% isnt much, considering a lot of people from xmrig binary and pay 1% ontology already/If minexmr was the most expensive pool, I think we may see a difference. But 0.1% isnt much, considering a lot of people from xmrig binary and pay 1% on top of the pool fee already /
[03-09-2022 17:16:10] <w[m]> s/If minexmr was the most expensive pool, I think we may see a difference. But 0.1% isnt much, considering a lot of people from xmrig binary and pay 1% ontology already/If minexmr was the most expensive pool, I think we may see a difference. But 0.1% isnt much, considering a lot of people use the xmrig binary and pay 1% on top of the pool fee already /
[03-09-2022 17:16:14] <Rucknium[m]> It's not so easy as before-after. You need to take into account other trends occurring at the same time, stationarity, etc.
[03-09-2022 17:16:24] <rbrunner> Yeah, it was 51%, now it's what, 35%?
[03-09-2022 17:16:51] <w[m]> And the "unknown" will change by 3-700k in and out of minexmr
[03-09-2022 17:17:25] <Rucknium[m]> w: Right. So it is unknown whether there will be a detectable effect at all.
[03-09-2022 17:22:53] * w[m] uploaded an image: (390KiB) < https://libera.ems.host/_matrix/media/r0/download/monero.social/KTCVhJqDqLbqDsOgYdQPJEPl/Image_55.jpg >
[03-09-2022 17:24:41] <atomfried[m]> Has anyone read up one this thing?
[03-09-2022 17:24:41] <atomfried[m]> https://www.youtube.com/watch?v=2glB7Cr6Jhw
[03-09-2022 17:24:41] <atomfried[m]> https://iacr.org/cryptodb/data/paper.php?pubkey=31723
[03-09-2022 17:24:41] <atomfried[m]> maybe it can be used for squashing ring sigs or make multisig more easy
[03-09-2022 17:25:19] <UkoeHB> I glanced at it, afaict it depends on size-linear constructions
[03-09-2022 17:26:46] <atomfried[m]> ok thats exactly what monero tries to avoid i guess
[03-09-2022 17:26:46] <Rucknium[m]> atomfried: I would like to encourage people to add thoughts about the paper to MoneroResearch.info . That way, comments are more easily organized than in the ephemeral IRC/Matrix:
[03-09-2022 17:26:57] <Rucknium[m]> https://moneroresearch.info/index.php?action=resource_RESOURCEVIEW_CORE&id=47
[03-09-2022 17:27:48] <Rucknium[m]> If anyone doesn't have an account on MoneroResearch.info and wants one , you can PM me or plowsof and we can set you up with an account.
[03-09-2022 17:27:59] <rbrunner> Where could Monero use something like "Extendablity" (just picked from the title)?
[03-09-2022 17:28:47] <rbrunner> (and that looks like a typo, doesn't it?)
[03-09-2022 17:34:58] <atomfried[m]> i dont realy know thats why i was asking if someone more knowledgable has seen it.
[03-09-2022 17:35:36] <atomfried[m]> same about that https://iacr.org/cryptodb/data/paper.php?pubkey=31719
[03-09-2022 17:35:36] <atomfried[m]> 😅
[03-09-2022 17:35:36] <atomfried[m]> for me it sounds like this could maybe be usefull for the monero ecosystem but i dont know for sure
[03-09-2022 17:35:51] <plowsof[m]> <rbrunner> "(and that looks like a typo..." <- should it be Extensibility? 😄
[03-09-2022 17:36:53] <rbrunner> or else "Extendability", with one "i" more :) Finding something like this is probably being quite mean to those authors ...
[03-09-2022 17:37:11] <UkoeHB> hmm should we end the meeting here?
[03-09-2022 17:38:37] <w[m]> Any updates on POC wallet?
[03-09-2022 17:38:58] <UkoeHB> I have a ccs: https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/290
[03-09-2022 17:39:50] <UkoeHB> My progress: added tx extra, added fee plumbing, started working on multisig tx builder
[03-09-2022 17:41:23] <UkoeHB> ok I'll call it; thanks for attending everyone
```

# Action History
- Created by: Rucknium | 2022-03-09T16:49:52+00:00
- Closed at: 2022-03-16T04:12:30+00:00
