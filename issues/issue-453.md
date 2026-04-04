---
title: 'Research meeting: 8 April 2020 @ 17:00 UTC'
source_url: https://github.com/monero-project/meta/issues/453
author: SarangNoether
assignees: []
labels: []
created_at: '2020-04-01T20:18:47+00:00'
updated_at: '2020-04-08T18:13:44+00:00'
type: issue
status: closed
closed_at: '2020-04-08T18:13:43+00:00'
---

# Original Description
Join in for the weekly Monero Research Lab meeting.

**When**: Wednesday, 8 April 2020 @ 17:00 UTC
**Where**: #monero-research-lab (freenode/matrix)

**Agenda**
1. Greetings

2. Roundtable

3. Questions

4. Action items

# Discussion History
## SarangNoether | 2020-04-08T18:13:43+00:00
    [2020-04-08 12:58:52] <sarang> OK, time for the weekly research meeting
    [2020-04-08 12:58:57] <sarang> Let's get started
    [2020-04-08 12:58:59] <sarang> GREETINGS
    [2020-04-08 12:59:00] <sarang> hi
    [2020-04-08 12:59:05] <ArticMine> hi
    [2020-04-08 12:59:09] <atoc> hi
    [2020-04-08 13:00:59] <TheCharlatan> ahoy
    [2020-04-08 13:00:59] <sarang> On to ROUNDTABLE, I suppose
    [2020-04-08 13:01:24] <sarang> I've been working on papers for PoPETs submission, which has been a blast
    [2020-04-08 13:01:27] <binaryFate> hello!
    [2020-04-08 13:01:44] <sarang> As well as some review for a paper on hierarchical one-of-many proofs
    [2020-04-08 13:02:14] <sarang> Finally, plenty of code relating to Triptych
    [2020-04-08 13:02:14] — Isthmus sneaks in late and grabs a seat in the back
    [2020-04-08 13:02:23] <sarang> Not too much exciting stuff to report overall
    [2020-04-08 13:02:29] <sarang> Any particular questions?
    [2020-04-08 13:03:33] <atoc> hierarchical one-of-many-proofs sounds interesting. can you link the paper?
    [2020-04-08 13:03:53] <sarang> It's not on the IACR yet (and I am not the author)
    [2020-04-08 13:04:08] → TheoStorm joined (~TheoStorm@host-p8vu8h.cbn1.zeelandnet.nl)
    [2020-04-08 13:04:35] <sarang> Otherwise, anyone else who wishes to share research topics is welcome to do so
    [2020-04-08 13:05:05] <binaryFate> what are hierarchical one-of-many-proofs?
    [2020-04-08 13:05:35] <sarang> An extension of the Groth proofs used in Triptych and Lelantus that trade size for prover complexity
    [2020-04-08 13:06:00] <sarang> They use a clever layering technique
    [2020-04-08 13:06:13] <binaryFate> smaller size for increased prover complexity?
    [2020-04-08 13:06:21] <sarang> Other way around :)
    [2020-04-08 13:06:26] <binaryFate> ok :)
    [2020-04-08 13:06:52] <sarang> The author thought there could be verification savings in certain cases, but I don't think that's the case if you do batching in the usual way
    [2020-04-08 13:08:11] <sarang> Does anyone else have research topics they'd like to share or discuss here?
    [2020-04-08 13:08:29] <ArticMine> I can give an update on the scaling and fees issue #70
    [2020-04-08 13:09:20] <sarang> Sure!
    [2020-04-08 13:10:02] <ArticMine> I have a solution for the scaling side and minimum relay fee. I am still finalizing the fee ratios
    [2020-04-08 13:10:29] <ArticMine> Basically we can use the long term medium to deal with this
    [2020-04-08 13:10:31] <sarang> Can you summarize?
    [2020-04-08 13:11:19] <ArticMine> Sure
    [2020-04-08 13:11:43] <ArticMine> 1) Put a cap on the rate of fall of the long term medium so that it falls at the same rate it rises
    [2020-04-08 13:13:07] <ArticMine> 2) Make the penalty free zone dynamic as the greater of 300000 bytes and 25% of the log term medium
    [2020-04-08 13:13:28] <sarang> Will that 300K value change with CLSAG?
    [2020-04-08 13:14:14] <ArticMine> No the reference transaction size will to 2100
    [2020-04-08 13:14:20] <sarang> yes
    [2020-04-08 13:14:32] <sarang> But there are no plans to change the fixed-value penalty-free size?
    [2020-04-08 13:15:05] <ArticMine> The minimum relay fee will  very close to the old normal fee
    [2020-04-08 13:16:00] <ArticMine> So for the current minimum penalty one the minimum fee will actually go up ~2.5x
    [2020-04-08 13:16:36] <binaryFate> ArticMine what issue/risk is this solution tackling?
    [2020-04-08 13:17:04] <ArticMine> A sudden drop in use followed by a recovery
    [2020-04-08 13:17:24] → rex4539 joined (~rex4539@2a02:587:350c:a200:f58c:df62:2e93:60af)
    [2020-04-08 13:17:25] <ArticMine> In many ways similar to COVID-19
    [2020-04-08 13:17:47] <binaryFate> What would be the shortcomings of the current implementation in that situation?
    [2020-04-08 13:17:59] <ArticMine> https://github.com/monero-project/research-lab/issues/70
    [2020-04-08 13:18:16] <ArticMine> This create the scenario
    [2020-04-08 13:18:36] <binaryFate> Ah, couldn't find issue. Thank you
    [2020-04-08 13:19:09] <ArticMine> The basic problem is a sharp rise in fee that can take months or year to come back to normal
    [2020-04-08 13:19:31] ⇐ vtnerd quit (~vtnerd@173-23-103-30.client.mchsi.com): Ping timeout: 260 seconds
    [2020-04-08 13:19:56] → vtnerd joined (~vtnerd@173-23-103-30.client.mchsi.com)
    [2020-04-08 13:20:07] <ArticMine> Also a very sudden drop in the long term medium that also could take months or years to recover
    [2020-04-08 13:21:17] <ArticMine> Issue #70 does not mention COVID-19 but COVID-19 is a very good scenario
    [2020-04-08 13:22:27] <sarang> Will you have specific code or pseudocode soon to allow for simulations prior to any recommended deployment?
    [2020-04-08 13:22:48] <ArticMine> Also there are scenarios where COVID-19 cold lead to a significant demand on the Monero network in terms of transactions
    [2020-04-08 13:23:04] <ArticMine> Yes
    [2020-04-08 13:23:37] <ArticMine> I have all the formulas now except for the fee ratios
    [2020-04-08 13:23:44] <sarang> OK, thanks
    [2020-04-08 13:23:44] <ArticMine> Still working on that
    [2020-04-08 13:23:53] <sarang> I assume you'll post them to the issue you linked?
    [2020-04-08 13:24:10] <ArticMine> Yes that is where I will post this
    [2020-04-08 13:24:19] <sarang> Got it
    [2020-04-08 13:24:35] <sarang> Anything else of note that folks wish to discuss?
    [2020-04-08 13:25:35] <sarang> I know UkoeHB_ recently posted his new version of Zero to Monero
    [2020-04-08 13:25:51] <sarang> not sure if he's around right now
    [2020-04-08 13:25:54] <ArticMine> Yes that is excellent
    [2020-04-08 13:26:11] <sarang> but that's on the getmonero library page, along with a link to the TeX source repo
    [2020-04-08 13:26:37] — TheCharlatan applauds
    [2020-04-08 13:27:00] <sarang> and there was also a suggestion from UkoeHB_ for updating how MLSAG secret data is wiped, which was a great catch (PR now available)
    [2020-04-08 13:27:37] <sarang> Anyone else?
    [2020-04-08 13:29:53] <sarang> Otherwise, we can move on to ACTION ITEMS for the week
    [2020-04-08 13:30:27] <sarang> I will be continuing work on a C++ implementation of Triptych for timing efficiency tests
    [2020-04-08 13:31:03] <sarang> as well as some new material for the multi-signer Triptych variant's security model, prior to the PoPETs submission deadline
    [2020-04-08 13:33:11] <Isthmus> Oops, just got back. Nice work Artic!
    [2020-04-08 13:33:32] <sarang> Isthmus: do you have any research or topics you'd like the group to discuss?
    [2020-04-08 13:34:13] <Isthmus> Ah, I've been neck deep in Zcash all week.
    [2020-04-08 13:34:17] <Isthmus> https://twitter.com/Mitchellpkt0/status/1245769462172745728
    [2020-04-08 13:34:17] <monerobux> [ Mitchell P. Krawiec-Thayer on Twitter: "Several unique phenomena in the #Zcash transaction lock_time field. Most make sense: 0, block heights, unix timestamps, delayed broadcast. Still trying to under ] - twitter.com
    [2020-04-08 13:34:26] <Isthmus> We did find that funny transaction over in NRL
    [2020-04-08 13:34:34] <Isthmus> Probably more of a novelty than anything else
    [2020-04-08 13:34:36] <Isthmus> Lemme grab the link
    [2020-04-08 13:34:48] <sarang> Anything relating to the Zcash lock times that's been observed in the Monero network too?
    [2020-04-08 13:34:49] <Isthmus> https://gist.github.com/noncesense-research-lab/a90b8bc5f57ffa9fff1a22d1323e5c2c
    [2020-04-08 13:34:54] <sarang> Or any lessons to learn from the Zcash work?
    [2020-04-08 13:35:10] <Isthmus> Monero's lock times look very similar
    [2020-04-08 13:35:16] <Isthmus> Actually there's also 4 bands
    [2020-04-08 13:35:18] <Isthmus> Like this:
    [2020-04-08 13:35:19] <Isthmus> 0
    [2020-04-08 13:35:31] <Isthmus> {1,3,8,10,12}
    [2020-04-08 13:35:42] <Isthmus> {block heights ~ 1xxxxxx}
    [2020-04-08 13:35:46] <Isthmus> and then UTC timestamps
    [2020-04-08 13:36:06] <Isthmus> It's all over the place, and I don't think any of it is enforced, so the lock_time field is really just an arbitrary memo xD
    [2020-04-08 13:36:12] <sarang> In Zcash too?
    [2020-04-08 13:36:34] <TheCharlatan> Did you analyze the distribution of the UTC timestamps as well?
    [2020-04-08 13:37:18] <Isthmus> Lemme try to find that notebook
    [2020-04-08 13:38:18] <Isthmus> Shoot, I don't have it on this computer
    [2020-04-08 13:38:36] ⇐ rex4539 quit (~rex4539@2a02:587:350c:a200:f58c:df62:2e93:60af): 
    [2020-04-08 13:40:13] <sarang> No worries
    [2020-04-08 13:40:21] <sarang> Any other action items for the week?
    [2020-04-08 13:41:02] <TheCharlatan> So what's up with duplicate subaddresses?
    [2020-04-08 13:43:02] <sarang> Isthmus: were those the only two such examples?
    [2020-04-08 13:43:12] <sarang> You suggested "novelty", heh
    [2020-04-08 13:43:48] <Isthmus> No, there were several, But all very similar, that one is representative
    [2020-04-08 13:43:59] <sarang> hmm
    [2020-04-08 13:46:53] <sarang> Along those lines, it was suggested (last week, IIRC) to move some of the more standardized tx fields out of extra
    [2020-04-08 13:47:08] <sarang> Which wouldn't eliminate strange behavior, of course
    [2020-04-08 13:47:29] <sarang> but could help with distinguishing factors like ordering etc.
    [2020-04-08 13:47:35] <sarang> Any further thoughts on that?
    [2020-04-08 13:48:39] <Isthmus> I'm working on it a bit, but need to move ideas from my head into diagrams. Will share here in a week or two.
    [2020-04-08 13:49:05] <Isthmus> Might have a new approach, but tbd
    [2020-04-08 13:49:16] <sarang> New approach to what exactly?
    [2020-04-08 13:49:21] <sarang> Transaction structure?
    [2020-04-08 13:50:56] <Isthmus> Nah, mental models that more accurately describe information leaks
    [2020-04-08 13:50:59] <Isthmus> But it doesn't all fit together yet.
    [2020-04-08 13:51:21] <Isthmus> My action item is making it into something comprehensible by next week xD
    [2020-04-08 13:51:22] <sarang> ah ok
    [2020-04-08 13:51:24] <sarang> Neat!
    [2020-04-08 13:51:31] <sarang> We're coming up on the end of the hour
    [2020-04-08 13:51:40] <sarang> Any last questions, topics, action items, etc.?
    [2020-04-08 13:52:37] <binaryFate> Just curious what's your perception of relevant research over the next 6 months. Everything staled? Business almost as usual?
    [2020-04-08 13:53:00] <binaryFate> Conferences and events are mostly canceled or moved to remote?
    [2020-04-08 13:53:09] <sarang> Oh you mean in the broader research community?
    [2020-04-08 13:53:36] <sarang> Seems that some conferences planned for later in the year are playing it by ear for now
    [2020-04-08 13:53:36] <binaryFate> Yeah, anything relevant to MRL and Monero, how do you see things going?
    [2020-04-08 13:54:17] <sarang> The cancellation of the Konferenco was unfortunate, but necessary
    [2020-04-08 13:54:46] <sarang> Otherwise, calls for papers seem to be mostly continuing as normal, which is great to see
    [2020-04-08 13:55:21] <binaryFate> ok good to know thank you
    [2020-04-08 13:55:24] <sarang> Perhaps bored academics stuck at home will be more eager to read and review new research too
    [2020-04-08 13:55:42] <binaryFate> and go straight for journals :)
    [2020-04-08 13:55:53] <Isthmus> Oh interesting question @binaryFate
    [2020-04-08 13:55:54] <Isthmus> That reminds me, when do we want to research quantum-resistant PoW and/or quantum-resistant cryptography?
    [2020-04-08 13:56:27] <Isthmus> Note that pqPoW isn't super important in the short term
    [2020-04-08 13:56:39] <binaryFate> "before it's too late"
    [2020-04-08 13:56:50] <Isthmus> However it is unfortunate that the Monero transaction I make tomorrow will most likely be decrypted by a quantum computer during my life time.
    [2020-04-08 13:57:00] <sarang> I know that suraeNoether had taken a particular interest recently in post-quantum signature constructions, but I don't know of any relevant efficient results at this point
    [2020-04-08 13:58:01] <Isthmus> It might be nice to have somebody put together a survey of (1) Exactly which pieces of Monero will be broken by quantum computers (2) Potentially Monero-compatible solutions
    [2020-04-08 13:58:33] <sarang> The reliance on discrete log hardness is the kicker
    [2020-04-08 13:59:31] <Isthmus> Yep, it's gonna be tricky.
    [2020-04-08 14:00:36] <Isthmus> But, I believe we can do it! If not, Monero has a very limited shelf-life :- P
    [2020-04-08 14:00:54] <atoc> I feel like the bipartite graph matching project that suraeNoether is verifying will be one of the most vulnerable
    [2020-04-08 14:01:21] <sarang> Graph matching is already parallelizable without a quantum computer
    [2020-04-08 14:01:34] <sarang> It's just a very large search space in general
    [2020-04-08 14:02:01] <sarang> On that happy note, let's go ahead and adjourn!
    [2020-04-08 14:02:06] <sarang> Thanks to everyone for participating
    [2020-04-08 14:02:13] <sarang> Logs will be posted shortly to the agenda GitHub issue


# Action History
- Created by: SarangNoether | 2020-04-01T20:18:47+00:00
- Closed at: 2020-04-08T18:13:43+00:00
