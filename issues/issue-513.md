---
title: 'Research meeting: 30 September 2020 @ 17:00 UTC'
source_url: https://github.com/monero-project/meta/issues/513
author: SarangNoether
assignees: []
labels: []
created_at: '2020-09-30T13:26:40+00:00'
updated_at: '2020-09-30T18:18:12+00:00'
type: issue
status: closed
closed_at: '2020-09-30T18:18:11+00:00'
---

# Original Description
Join in for the weekly Monero Research Lab meeting.

**When**: Wednesday, 30 September 2020 @ 17:00 UTC
**Where**: #monero-research-lab (freenode/matrix)

**Agenda**
1. Greetings

2. Roundtable

3. Questions

4. Action items

# Discussion History
## SarangNoether | 2020-09-30T18:18:11+00:00
    [2020-09-30 13:00:11] <sarang> All right, time for our meeting!
    [2020-09-30 13:00:19] <sarang> First, greetings!
    [2020-09-30 13:00:20] <sarang> Hi
    [2020-09-30 13:00:33] <ArticMine> Hi
    [2020-09-30 13:01:08] — sarang waits a few minutes for folks to arrive
    [2020-09-30 13:01:38] <sgp_> hello
    [2020-09-30 13:01:42] <dEBRUYNE> Hi
    [2020-09-30 13:02:38] <binaryFate> hello
    [2020-09-30 13:03:32] <Isthmus> Salutations
    [2020-09-30 13:04:46] <sarang> OK, let's move to roundtable, where anyone is welcome to share research topics of interest
    [2020-09-30 13:04:50] <sarang> Does anyone wish to begin?
    [2020-09-30 13:05:37] <sarang> If not, I'll go first
    [2020-09-30 13:05:46] <sarang> You can read my monthly research report here: https://www.reddit.com/r/Monero/comments/j2oncd/september_monthly_report_from_sarang_noether/
    [2020-09-30 13:05:47] <monerobux> [REDDIT] September monthly report from Sarang Noether (self.Monero) | 26 points (97.0%) | 5 comments | Posted by SarangNoether | Created at 2020-09-30 - 15:48:27
    [2020-09-30 13:05:59] <sarang> It's the last report for my funding period
    [2020-09-30 13:06:17] <sarang> This past week, I gave a talk for the MCC virtual conference on privacy
    [2020-09-30 13:06:22] <sarang> and participated in a panel on privacy
    [2020-09-30 13:06:48] <sarang> I took cargodog[m]'s idea for `n`-ary Gray codes and build working prototypes for both Triptych and Arcturus in Python and in C++
    [2020-09-30 13:06:50] → v1docq47[m] joined (~v1docq47m@188.232.228.50)
    [2020-09-30 13:06:56] <sarang> and shared some timing results earlier today
    [2020-09-30 13:07:13] <sarang> I also updated the Triptych code for more efficient batching across proofs within the same transaction
    [2020-09-30 13:07:17] <sarang> That's about it for my update
    [2020-09-30 13:07:28] <h4sh3d[m]> Hi (sorry I can't attend today, have a good meeting)
    [2020-09-30 13:07:40] <sgp_> I assume you have no ETA on the MCC videos being released?
    [2020-09-30 13:07:42] <sarang> No problem h4sh3d[m]
    [2020-09-30 13:07:49] <sarang> I don't know what their plans are for videos, sorry
    [2020-09-30 13:07:57] <sarang> I know they were recorded though
    [2020-09-30 13:08:04] <sgp_> did you publish the slides anywhere?
    [2020-09-30 13:08:32] <sarang> No, but I can post them later today if that's useful
    [2020-09-30 13:09:04] <sarang> They needed Google Slides, so I can post a PDF but not any source code for them
    [2020-09-30 13:09:39] <sarang> Were there any other questions on my research topics?
    [2020-09-30 13:11:47] <sarang> Here are the MCC slides: https://github.com/SarangNoether/talks/tree/mccvr-2020
    [2020-09-30 13:12:09] <sarang> OK, does anyone else wish to share research of interest?
    [2020-09-30 13:13:59] <sarang> Quiet channel today!
    [2020-09-30 13:14:40] <sarang> If not, I can discuss the Gray code stuff a bit more
    [2020-09-30 13:14:45] <sarang> Here is a timing plot: https://docs.google.com/spreadsheets/d/e/2PACX-1vROJzzfsOnkvxdsrQJgbYwdU2tlNYRJZVKGUAc6KswBGkaPduva-9-Yr6ACWF3Nu_-0I9q5Wt9MaUi7/pubhtml?gid=1695886143&single=true
    [2020-09-30 13:15:00] <sarang> I haven't put it into `gnuplot` yet
    [2020-09-30 13:15:35] <sarang> There's an outlier data point for the `Triptych Gray 2-2` dataset that's just a timing fluke, and can be safely ignored
    [2020-09-30 13:15:40] <sarang> (dashed blue line)
    [2020-09-30 13:15:45] <dEBRUYNE> sarang: with respect to MCC videos -> https://www.reddit.com/r/Monero/comments/j074ro/sarang_noether_of_the_monero_research_lab_will_be/g6t0egm/?context=3
    [2020-09-30 13:15:45] <monerobux> [REDDIT] Sarang Noether of the Monero Research Lab will be speaking at the Magical Crypto Conference today at 1:15 PM EDT (Privacy: The Collision of Theory and Practice) and 1:55 PM EDT (Is Bitcoin Falling Behind on Privacy - Panel) (https://www.magicalcryptoconference.com/2020-vr#agenda) to r/Monero | 73 points (97.0%) | 13 comments | Posted by dEBRUYNE_1 | Created at 2020-09-26 - 14:37:48
    [2020-09-30 13:16:33] <sarang> If anyone has issues with differentiating the colors, please let me know here (or DM me) and I can provide a version with better color accessibility
    [2020-09-30 13:16:48] <sarang> Thanks dEBRUYNE!
    [2020-09-30 13:17:14] <dEBRUYNE> np
    [2020-09-30 13:17:19] <sarang> Our use case for the Gray results in Triptych/Arcturus is to use common input sets within transactions, but not necessarily between proofs
    [2020-09-30 13:17:35] <sarang> This is distinct from something like Lelantus, where they intend to reuse large common input sets across many proofs
    [2020-09-30 13:18:07] <sarang> For our use case, the Gray method only starts "winning" between 64-128 sizes, and is different as you increase the number of inputs
    [2020-09-30 13:18:20] <sarang> This input-based advantage can be removed if we were to overhaul the way inversions are performed
    [2020-09-30 13:18:48] → Myrtle63Kuhlman joined (~Myrtle63K@static.57.1.216.95.clients.your-server.de)
    [2020-09-30 13:19:12] <sarang> And as you can see, while there is an improvement for larger input set sizes, it's reasonably marginal (single-digit percent decreases in time)
    [2020-09-30 13:20:20] <sarang> I shared my code with the Lelantus team; they may wish to conduct their own timing experiments based on their particular use case
    [2020-09-30 13:20:39] <sarang> and it sounds like cargodog[m] intends to add this to their own Rust implementation of Arcturus
    [2020-09-30 13:20:39] <sgp_> looking at that plot now. very nice
    [2020-09-30 13:20:40] <binaryFate> Where can I read about the Gray code idea after being out of the loop? Meetings logs?
    [2020-09-30 13:20:52] <sarang> One sec binaryFate, will get some links for ya
    [2020-09-30 13:21:05] <sarang> https://github.com/cargodog/arcturus/issues/19
    [2020-09-30 13:21:19] <binaryFate> thanks!
    [2020-09-30 13:21:20] <sarang> cargodog[m] had implemented a binary Gray code method for their Groth/Kohlweiss proof implementation
    [2020-09-30 13:21:38] <sarang> and speculated that it could be useful for the Bootle optimization used in Arcturus/Lelantus/Triptych
    [2020-09-30 13:22:12] <sarang> I implemented the idea using `n`-ary Gray codes for Arcturus and Triptych in Python (for prototyping) and in C++ (for timing)
    [2020-09-30 13:22:37] <sarang> Kudos to cargodog[m] for this super clever idea
    [2020-09-30 13:23:14] <sgp_> it does look like mostly a wash
    [2020-09-30 13:23:34] <sarang> By switching from standard `n`-ary decomposition of integers to `n`-ary Gray decompositions, you simplify the multiplications used in computing certain scalars, but replace with an expensive inversion process whose complexity can be amortized
    [2020-09-30 13:23:43] <sarang> It's a wash for this particular kind of input set choice
    [2020-09-30 13:23:48] ⇐ Myrtle63Kuhlman quit (~Myrtle63K@static.57.1.216.95.clients.your-server.de): Ping timeout: 258 seconds
    [2020-09-30 13:24:02] <sarang> But for other applications can have much better improvements
    [2020-09-30 13:24:27] <ArticMine> Any differences in transaction size?
    [2020-09-30 13:24:30] <sarang> No
    [2020-09-30 13:24:37] <sarang> Transaction size is identical
    [2020-09-30 13:24:44] <sarang> it's only how the proof elements are computed that changes
    [2020-09-30 13:25:12] <ArticMine> So a very small improvement in verification time
    [2020-09-30 13:25:35] <sarang> For the current use case of non-overlapping input sets between transactions, yes
    [2020-09-30 13:26:08] <sarang> Even with this use, it would be possible to overhaul the code to batch the expensive inversion across unrelated proofs, which I did not do here
    [2020-09-30 13:26:16] <sarang> So a batch would require only one such inversion
    [2020-09-30 13:26:30] <sarang> However, if the input sets don't overlap, I think the benefit to this would be fairly minimal
    [2020-09-30 13:26:49] <sarang> You really see the efficiency if you batch many proofs with the same input set, and also batch the inversions
    [2020-09-30 13:26:58] <sarang> As you can see, it gets really subtle
    [2020-09-30 13:28:14] <ArticMine> thinks
    [2020-09-30 13:28:40] <sarang> Anyway, this provides some reasonable timing data for this idea
    [2020-09-30 13:29:04] <sarang> I look forward to seeing the results of any experiments that cargodog[m] or the Lelantus team conduct
    [2020-09-30 13:29:23] <sarang> Since cargodog[m] uses a more efficient crypto library, and the Lelantus use case for batching and input sets is very different from ours
    [2020-09-30 13:30:36] <sarang> At any rate, it's a very interesting idea
    [2020-09-30 13:30:51] <sarang> and it was a fun challenge to implement for this experiment
    [2020-09-30 13:33:47] <UkoeHB_> cool work
    [2020-09-30 13:34:58] ⇐ Febo quit (59d411cd@89-212-17-205.static.t-2.net): Remote host closed the connection
    [2020-09-30 13:35:09] <UkoeHB_> btw ArticMine where are you at with the fee proposal?
    [2020-09-30 13:36:14] <UkoeHB_> it sounded like you were planning to reassess some aspects
    [2020-09-30 13:36:20] <ArticMine> The question I see is spam risk.
    [2020-09-30 13:36:44] <ArticMine> Which I feel for the most part can be mitigated
    [2020-09-30 13:37:18] <ArticMine> Then we can mover to using the long term median as a penalty free zone
    [2020-09-30 13:37:49] <ArticMine> Which effectively allows for very stable fees
    [2020-09-30 13:38:12] <ArticMine> The key is that for a Big  bang attack it is neutral
    [2020-09-30 13:38:43] <ArticMine> since once the LT median moves then Big Bang moves on
    [2020-09-30 13:39:17] <UkoeHB_> ah my suggestion was to use the long-term-median for penalty zone, and let the penalty free zone fluctuate, are you thinking the opposite? if the penalty zone fluctuates then fees will fluctuate more
    [2020-09-30 13:39:24] <ArticMine> It is maintaining the sort term median that deters big bang
    [2020-09-30 13:40:24] <ArticMine> Yes using the LT median as the penatly free zone
    [2020-09-30 13:40:28] <binaryFate> can you elaborate what the "spam risk" would look like?
    [2020-09-30 13:40:50] <ArticMine> Basically there are tow cases
    [2020-09-30 13:41:49] <ArticMine> 1) For a pre existing Big Bang attack there is no change since it does not make sense for the spammer to maintain the long term median
    [2020-09-30 13:42:51] <ArticMine> 2) If the short term median falls below the long term median then it crease a similar situation to what we have now  but at much higher block size and price
    [2020-09-30 13:43:22] <ArticMine> So the cost of spamming node relay f=minimum fee is much higher
    [2020-09-30 13:44:37] <ArticMine> There would be no penalty to get back to the long term median as there is now no penalty to get to 300000 bytes
    [2020-09-30 13:45:02] <ArticMine> but the cost of the spam in real terms would be much higher than ti is now
    [2020-09-30 13:45:30] <ArticMine> It is a much simple solution also than what we have now
    [2020-09-30 13:45:42] <ArticMine> SO the code wold be simpler
    [2020-09-30 13:46:14] <UkoeHB_> Ill have to think about this a bit
    [2020-09-30 13:47:43] <ArticMine> It comes down to can we have 100x the transaction rate and no increase in price
    [2020-09-30 13:47:56] <ArticMine> I do not think that is realistic
    [2020-09-30 13:48:11] <binaryFate> agree with you
    [2020-09-30 13:50:06] <ArticMine> So the cost of the ham in real terms remains the same, but the cost of the spam for a given % increase in block weight increases with price
    [2020-09-30 13:53:13] <sarang> OK, any other research topics to address before we end the meeting?
    [2020-09-30 13:53:33] <Isthmus> Any interest in setting block size by encrypted miner vote?
    [2020-09-30 13:53:33] <Isthmus> (which would boil down to the Nakamoto consensus assumption that 51% of miners will behave in the best interest of the network)
    [2020-09-30 13:53:33] <Isthmus> An Insight Fellow is playing around with building an noninteractive ZKP mechanism for this, based on Pallier encrypted voting
    [2020-09-30 13:54:00] <sarang> Oh interesting; I did not know this was happening
    [2020-09-30 13:54:14] <Isthmus> (each block contains one trinary vote for {decrease, same, increase})
    [2020-09-30 13:54:17] <sgp_> what benefit would this bring?
    [2020-09-30 13:54:46] <ArticMine> Miner can effectively put a limit themselves any way
    [2020-09-30 13:55:16] <binaryFate> Any human input sounds like degrading from a purely algorithmic solution, but this is certainly interesting research
    [2020-09-30 13:55:34] <Isthmus> @sgp Well right now in 2020 we're trying to figure out a dynamic block size algorithm that produces desirable results in 2030, but I dunno how big transactions will be, how fast internet will be, how much transaction volume we'll have, etc.
    [2020-09-30 13:55:34] <Isthmus> So if we go with encrypted miner voting, then 2030 block size is set by 2030 miners, instead of 2020 researchers
    [2020-09-30 13:55:58] <Isthmus> And miners would have the best understanding of how much their infra can handle before blocks get too big, etc
    [2020-09-30 13:56:17] <sgp_> so this would overrule existing restrictions?
    [2020-09-30 13:56:35] <ArticMine> With the current situation the miners can still limit the block weight
    [2020-09-30 13:56:42] <Isthmus> Miners can choose to make smaller blocks than the algo allows, but cannot choose to make bigger blocks than the algo allows
    [2020-09-30 13:56:45] <Isthmus> So it's one-sided
    [2020-09-30 13:56:54] <Isthmus> @sgp - doesn't have to.
    [2020-09-30 13:57:09] <Isthmus> Could be that we have a dynamic algo, but miners can vote some change on top of that
    [2020-09-30 13:57:25] <Isthmus> Right now it's just a toy, haven't worked it into a fully functioning secure economic model yet
    [2020-09-30 13:57:46] → nssy joined (~nssy@197.237.91.81)
    [2020-09-30 13:58:20] <ArticMine> Miner voting has only been proposed in cois that have a fixed block size such as Bitcoin
    [2020-09-30 13:58:31] <ArticMine> and Bytecoin
    [2020-09-30 13:58:44] <ArticMine> when the block reward falls to zero
    [2020-09-30 13:59:26] <Isthmus> Interesting, in those systems, what are they voting on/for?
    [2020-09-30 13:59:39] <ArticMine> Blocksize
    [2020-09-30 14:00:08] <ArticMine> In Ethereum max gas consumption per block
    [2020-09-30 14:00:47] <Isthmus> Ah yea, each ETH miner can vote +1/1024 or -1/1024 if I recall correctly
    [2020-09-30 14:01:00] <UkoeHB_> Hmm ArticMine using the long term median for penalty free zone still leaves us with minimum fee issues. Namely issues around if the short term median collapses then transactions with pre-collapse minimum fees will be invalid. That's unless we set a floor on the min fee based on the long term median. Doing that may make perfect sense actually, since if the short term median is low then you are unlikely to be
    [2020-09-30 14:01:00] <UkoeHB_> filling the penalty free zone anyway (assuming PFZ is now based on long term median).
    [2020-09-30 14:01:40] <UkoeHB_> or ceiling* I guess
    [2020-09-30 14:02:29] <ArticMine> The fee is set effectively by the long term median because the penalty free zone is a floor for the short term median
    [2020-09-30 14:02:48] <binaryFate> Especially because Monero makes a point to be mined on generic hardware, I would not assume much long-term interest or economic self-benevolence from Monero miners
    [2020-09-30 14:03:07] <UkoeHB_> aren't there dangers of cartelization if block size is based on voting? since you can force up the fees
    [2020-09-30 14:03:08] <binaryFate> It's different from what you would expect from miners who bought specialized hardware for other coins
    [2020-09-30 14:03:43] <ArticMine> <UkoeHB_> aren't there dangers of cartelization if block size is based on voting? since you can force up the fees <--- Very much so
    [2020-09-30 14:04:24] <Isthmus> "aren't there dangers of cartelization if block size is based on voting? since you can force up the fees" <--- this is the case now too, right? If lots of miners decided to voluntarily suppress block size, or something like that?
    [2020-09-30 14:04:28] <ArticMine> but it is the only option to a fixed block size for coions with falling emission
    [2020-09-30 14:05:04] <ArticMine> Cartels fail eventually
    [2020-09-30 14:05:12] <UkoeHB_> heck it's even worse than cartelization since the incentive to vote for small blocks is presented to all miners; cartelizing just forces out transactions not other miners
    [2020-09-30 14:05:49] <UkoeHB_> cartelizing nowadays is a losing proposition since other miners will just take the remaining tx
    [2020-09-30 14:06:31] <UkoeHB_> so the cartel has to operate at a loss unless they have a serious competitive advantage, but even then it's dubious
    [2020-09-30 14:06:47] <Isthmus> The way we implemented it, 501 of 1000 miners must vote for any block size change, so the cartel must be > 51%, implying failure of Nakamoto consensus asssumption
    [2020-09-30 14:06:52] <Isthmus> (again, that's just our toy version)
    [2020-09-30 14:07:31] <Isthmus> to clarify: a block size change will not occur unless >51% of miners voted for it
    [2020-09-30 14:08:02] <Isthmus> Anywho, once it's finished up, I'll share a link here
    [2020-09-30 14:08:07] <Isthmus> Sorry to derail the convo past time
    [2020-09-30 14:08:18] <sarang> Good discussion!
    [2020-09-30 14:08:30] <sarang> Let's go ahead and adjourn, and discussions can of course continue


# Action History
- Created by: SarangNoether | 2020-09-30T13:26:40+00:00
- Closed at: 2020-09-30T18:18:11+00:00
