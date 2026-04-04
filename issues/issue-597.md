---
title: Monero Research Lab Meeting - 4 August 2021 @ 16 UTC
source_url: https://github.com/monero-project/meta/issues/597
author: UkoeHB
assignees: []
labels: []
created_at: '2021-08-04T16:03:09+00:00'
updated_at: '2021-08-04T17:09:46+00:00'
type: issue
status: closed
closed_at: '2021-08-04T17:09:46+00:00'
---

# Original Description
Time: 16 UTC

Location: #monero-research-lab (Libera)

Main discussion topics:

- Chat and orient about open research projects.

# Discussion History
## UkoeHB | 2021-08-04T17:09:14+00:00
Meeting log

```
[16:01] <UkoeHB> meeting start
[16:01] <UkoeHB> 1. greetings
[16:01] <UkoeHB> hello
[16:01] <isthmus> Salutations
[16:02] <Rucknium[m]> Hi
[16:03] <UkoeHB> monero-project/meta #597 made an issue for the meeting
[16:05] <UkoeHB> There don't seem to be that many people here. In any case,
[16:05] <UkoeHB> 2. updates
[16:07] <UkoeHB> I am currently working on: Seraphis preprint, ring binning (issue #84), overhaul of multisig address generation. Past stuff still open: tx uniformity (#6456).
[16:07] <luigi1111w> sorta here
[16:07] <vtnerd> present
[16:09] <Rucknium[m]> I made a little R Shiny app to display data on CashFusion, BCH's CoinJoin protocol: fusionstats.redteam.cash
[16:09] <Rucknium[m]> It seems the anonymity set is small. About 200 fusions a day, and a lot of those are teh same wallets fusing multiple times per day.
[16:11] <vtnerd> not strictly MRL related (but close) - finished writing a draft of p2p-e2e encryption with noise - perhaps too much work and should "just use ssl"
[16:11] <vtnerd> noise allows for sending handshake/ping in first packet + all bytes randomized, which makes it harder for dpi engines to identify the stream
[16:12] <vtnerd> so I'll post the full writeup before doing the code for feedback
[16:15] <wfaressuissia[m]> "arxiv.org/pdf/1703.00536.pdf" is better than general purpose mixnet in long term perspective?
[16:15] <wfaressuissia[m]> * ... is it ...
[16:17] <vtnerd> maybe, but that would be external to monerod I think, and hopefully would use the socks interface
[16:18] <UkoeHB> some things others not present are working on:
[16:18] <UkoeHB> - ArticMine's fee change recommendations for issue #70 are in PR form: monero-project/monero #7819
[16:18] <UkoeHB> - sarang's initial draft for Triptych-supporting multisig is out: github.com/cypherstack/triptych-multisig
[16:18] <UkoeHB> - sarang and researchers at Firo are working on Spark (successor to Lelantus 1/2) protocol
[16:18] <UkoeHB> - jberman[m] continues to investigate/study the gamma selection for ring decoys
[16:19] <UkoeHB> Anything else that I missed?
[16:20] <Rucknium[m]> I am an empirical microeconomist, by the way. Hopefully I can be helpful to XMR at some point.
[16:21] <jberman[m]> Working on fixes to the decoy selection algo (7821, 7798). Next step seems to try and deduce real spends to guide parameter selection. Also thinking about implementing a tool to assess the quality of ring selection and/or shifting attention toward the binning implementation (by providing eyes or whatever else need be)
[16:21] <gingeropolous> i think an analysis of monero's monetary policy would be cool Rucknium[m] , with implications of adaptive blocksize params
[16:23] <isthmus> Agree, the jollymort stuff is really old
[16:23] <Rucknium[m]> I think it would be cool, too. I feel like I need to work my way through Zero to Monero first, though. What kind of research questions about the monetary policy would be useful to answer?
[16:23] <isthmus> The main thing on my mind: I am skeptical that going into tail emission soon at 0.6 XMR is going to incentivize enough hashrate to make Monero secure for large transactions
[16:24] <wfaressuissia[m]> "Anything else that I missed?" I'm lost somewhere within a try to fix peer to peer network of monero based on randomx pow.
[16:25] <UkoeHB> thanks for all the updates guys
[16:25] <UkoeHB> 3. discussion
[16:30] <wfaressuissia[m]> isthmus: are there any papers about proper incentive design ?
[16:30] <UkoeHB> moving forward:
[16:30] <UkoeHB> - Two people expressed interest in working on PoC/code for ring binning (MRL #84), I will try to coordinate that effort. I still need to improve the theoretical justifications for this. However, are there any open points of concern on this topic?
[16:30] <UkoeHB> - I received an email from someone expressing interest in working on parts of tx uniformity (#6456), but have not heard anything recently.
[16:30] <UkoeHB> - Need to discuss fee changes (some disagreement about max rate of long-term block size growth).
[16:30] <UkoeHB> - Need to start thinking about Triptych vs Seraphis/Spark/etc.
[16:33] <isthmus> @wfaressuissia[m] here's the OG analysis by jollymort but it's several years old
[16:33] <isthmus> github.com/JollyMort/monero-researc…amic%20Minimum%20Fee%20-%20DRAFT.md
[16:33] <isthmus> Mastering Monero provides a very brief description, and I think that Zero To Monero discusses it in more detail
[16:33] <isthmus> ArticMine has also done some great analyses around fee markets, though I'm not sure if this is documented centrally, maybe on GitHub issues?
[16:33] <gingeropolous> well damn thats quite a list folks
[16:33] <isthmus> Although those are, for the most part, exploring and explaining what currently exists rather than what could/should
[16:34] <UkoeHB> Regarding Triptych vs etc., it feels a bit in limbo since Seraphis/Spark/etc. are still WIP preprints. Should we table the question of 'what tx protocol to use next' until preprints are available for possible alternatives to Triptych?
[16:35] <gingeropolous> is it worth considering triptych in the meantime regardless of multisig snafu?
[16:35] <Rucknium[m]> isthmus: We are already at 0.9 XMR reward per block. I suppose if there is a concern at 0.6, we should already be concerned.
[16:35] <luigi1111w> I think it's too much a developing field to settle right now
[16:35] <wfaressuissia[m]> isthmus: At first glance, those links don't contain fundamental analysis. short term heuristics aren't interesting for me
[16:35] <gingeropolous> from what i'm hearing from the grapevine, most monero multisig things are running into problems
[16:36] <isthmus> @Rucknium[m] yea, I already am concerned, a 10 block reorg costs less than $2000 in electricity, so I wouldn't trust monero for anything over $10k right now
[16:37] <luigi1111w> you mean after 10 blocks?
[16:37] <luigi1111w> you can wait longer
[16:37] <tobtoht> ^ services are free to change their desired number of confirmations
[16:37] <UkoeHB> > is it worth considering triptych in the meantime regardless of multisig snafu?
[16:37] <UkoeHB> Do you mean, consider upgrading to Triptych without multisig support?
[16:37] <isthmus> Sure, though I'd rather have more hashrate than longer wait times :- P
[16:37] <gingeropolous> yep
[16:37] <luigi1111w> strongly disagree
[16:38] <luigi1111w> there's huge cost to upgrade
[16:38] <tobtoht> I echo that sentiment, it's worth doing right.
[16:40] <Rucknium[m]> isthmus: Are botnets active now? Or is it harder with the requirements of RandomX? Would the biggest concern be botnets? Or what are the most likely 51% attack scenarios now?
[16:41] <kinghat[m]> there was talk about increasing the ring size before triptych integration but i think was tabled in favor of waiting for triptych. does this change now that triptych is in limbo?
[16:41] <tobtoht> I'd like to see BP+, ring size bump, and fee adjustment in a hardfork in 6-9 months from now, then decide after what to do wrt Triptych / Seraphis / Lanantus 3 when the tradeoffs have become more clear.
[16:41] <kinghat[m]> for next HF*
[16:43] <isthmus> I have to run out for an appointment but can drop back later today.
[16:43] <sgp_[m]> tobtoht: Why 6-9 mo from now? Why not 3 mo from now?
[16:44] <sgp_[m]> Those things are all ready to go
[16:44] <luigi1111w> 3 mo meants it'll be down to the wire as always -_-
[16:45] <kinghat[m]> ya i thought we were thinking this summer or this fall for the HF
[16:45] <sgp_[m]> luigi1111w: In what way, I thought the code was effectively ready to go
[16:45] <sgp_[m]> And we can use the opportunity to force the update for the improved wallet selection algo
[16:46] <luigi1111w> maybe if it's actually moved on in the next few weeks, but historically that never happens
[16:46] <tobtoht> Shorter timeframe is fine if we can get the ecosystem on board in time
[16:46] <sgp_[m]> Is there anything we're waiting on?
[16:47] <luigi1111w> if it's 3mo from when the release process starts that would be ok
[16:47] <UkoeHB> would be nice to get multisig address gen fixes into next big release, but it isn't a blocker
[16:47] <sgp_[m]> Setting a mid Nov upgrade date seems reasonable imo
[16:48] <kinghat[m]> dev meeting soon? or is that a community meeting 🤔
[16:48] <luigi1111w> dev
[16:48] <sgp_[m]> I'd rather not stall on the fixes for longer, take the wind now while the bigger discussions are stalled/ongoing
[16:48] <ErCiccione> maybe a large dev meeting would be useful
[16:48] <sgp_[m]> Yeah this is dev meeting stuff now
[16:48] <gingeropolous> yep
[16:48] <tobtoht> yeah
[16:48] <ErCiccione> we can set one for next week?
[16:49] <gingeropolous> if there's talk of a release soon, prolly time to have them weekly etc
[16:49] <gingeropolous> well, fork i mean
[16:50] <wfaressuissia[m]> UkoeHB: What's the state of the art for anonymous payment system design now ? If it's too hard question then it can be ignored as everything else. I'm about cryptography part
[16:50] <ErCiccione> yeah. We also need a clear list of what's going to be included in the network upgrade
[16:51] <ErCiccione> btw should we talk about monero-project/monero #7830?
[16:54] <UkoeHB> wfaressuissia[m]: imo and afaik 1) active protocols: RingCT; 2) published research: Triptych; 3) WIP research: Seraphis/Spark/etc., Halo 2 + Orchard
[16:56] <gingeropolous> so it seems the rough consensus is to hold out for seraphis / spark / ? , mainly due to multisig complexity of triptych?
[16:56] <sgp_[m]> <gingeropolous> "if there's talk of a release..." <- Agreed
[16:56] <sgp_[m]> <ErCiccione> "btw should we talk about https:" <- What is the Wagner attack?
[16:57] <sgp_[m]> gingeropolous: Seems to, people want to make a decision when more options are on the table
[16:58] <wfaressuissia[m]> it's impossible to make a decision without deep unbiased comparison of all weaknesses / advantages for all of them
[16:58] <ErCiccione> sgp_[m]: I don't know more than what i wrote in the issue, but luigi1111 looked into it, he definitely knows more than me about it
[16:59] <UkoeHB> joinmarket.me/blog/blog/avoiding-wagnerian-tragedies
[16:59] <UkoeHB> web.getmonero.org/resources/research-lab/pubs/MRL-0009.pdf -> eprint.iacr.org/2018/417 -> link.springer.com/content/pdf/10.1007%2F3-540-45708-9_19.pdf
[16:59] <UkoeHB> It's the reason the multisig MRL paper requires a commit-and-reveal pattern.
[17:00] <ErCiccione> yeah UkoeHB is the one who informed us about it
[17:01] <UkoeHB> Tbh I also don't have a great understanding, but since the papers say we should use commit-and-reveal, then better to do that.
[17:01] <sgp_[m]> Do we need to inform people the old/current multisig wallets are vulnerable?
[17:03] <sgp_[m]> Okay
[17:04] <sgp_[m]> I have more questions on this but none for now
[17:04] <UkoeHB> Maybe.. unfortunately right now I don't know if anyone knows under what conditions a problem will occur.
[17:05] <UkoeHB> It's past the hour, so I will call close on the meeting.
```

# Action History
- Created by: UkoeHB | 2021-08-04T16:03:09+00:00
- Closed at: 2021-08-04T17:09:46+00:00
