---
title: 'Research meeting: 8 July 2019 @ 17:00 UTC'
source_url: https://github.com/monero-project/meta/issues/368
author: SarangNoether
assignees: []
labels: []
created_at: '2019-07-07T17:22:01+00:00'
updated_at: '2019-07-08T17:35:33+00:00'
type: issue
status: closed
closed_at: '2019-07-08T17:35:33+00:00'
---

# Original Description
Join in for the weekly Monero Research Lab meeting.

**When**: Monday, 8 July 2019 @ 17:00 UTC
**Where**: #monero-research-lab (freenode/matrix)

**Agenda**
1. Greetings

2. Roundtable
a. Sarang: MLSAG/CLSAG verification, Omniring/RCT3 analysis, Lelantus prover
b. Surae
c. Others?

3. General questions

4. Action items

# Discussion History
## SarangNoether | 2019-07-08T17:35:32+00:00
    [2019-07-08 13:00:15] <sarang> Righto, let's begin our meeting!
    [2019-07-08 13:00:38] <sarang> Agenda: https://github.com/monero-project/meta/issues/368
    [2019-07-08 13:00:45] <sarang> Starting now with GREETINGS
    [2019-07-08 13:01:00] <sarang> hi
    [2019-07-08 13:01:24] <sgp_> Hi
    [2019-07-08 13:03:05] <sarang> suraeNoether: you here?
    [2019-07-08 13:03:12] <sarang> It's quiet... too quiet...
    [2019-07-08 13:03:12] <suraeNoether> yes
    [2019-07-08 13:03:12] <suraeNoether> sorry
    [2019-07-08 13:03:14] <suraeNoether> hellow gents
    [2019-07-08 13:03:18] <suraeNoether> harrow
    [2019-07-08 13:03:25] — suraeNoether lost in debugging
    [2019-07-08 13:03:47] <sarang> Let's jump into ROUNDTABLE then, with our small crowd
    [2019-07-08 13:04:21] <suraeNoether> mine is going to be super fast: last week basically right after the research meeting i started getting very ill. long story short, i went to the hospital, and let me just say: recreational pancreatitis is not a thing for a reason
    [2019-07-08 13:04:37] <sarang> but it'd be a cool name for a band
    [2019-07-08 13:04:46] <suraeNoether> yes. yes. *strokes chin*
    [2019-07-08 13:05:08] <suraeNoether> so, i'm trying to take it easy and i did very little this past week
    [2019-07-08 13:05:09] <sarang> Glad to see you're well enough to debug :)
    [2019-07-08 13:05:23] <sarang> For me, MLSAG/CLSAG verification updates continue, with PR 5707 open for review and similar changes to my CLSAG branch (to be included in later code for review)
    [2019-07-08 13:05:31] <suraeNoether> i have a few things on my plate for today, but other than that: i'm basically all action items and no progress compared to last week. onto sarang :D
    [2019-07-08 13:06:07] <sarang> I've been in contact with Aram, the author of the Lelantus paper/protocol; he came up with an interesting idea to make the prover very efficient, at the cost of proof size and verification
    [2019-07-08 13:06:22] <sarang> although the verification cost can be batched, of course
    [2019-07-08 13:06:49] <sarang> I view proving time as generally unimportant (to an extent), but it's a very clever new way to prove a 1-of-N zero commitment
    [2019-07-08 13:07:06] <suraeNoether> good prover times means fast construction of transaction for mobile devices
    [2019-07-08 13:07:08] <suraeNoether> which is v nice
    [2019-07-08 13:07:13] <sarang> true
    [2019-07-08 13:07:22] <sarang> but if it costs you both space and verification time...
    [2019-07-08 13:07:53] <suraeNoether> unlike, say, verification time, which puts a constraint on how rapidly the network can grow, which has security consequences for the chain
    [2019-07-08 13:08:02] <suraeNoether> ^ ah yeah that's true: is it faster with a big space tradeoff?
    [2019-07-08 13:08:14] <sarang> Faster prover, slower verifier, bigger proof
    [2019-07-08 13:08:32] <sarang> I think you can batch away some of the verification increase (you effectively do two smaller proofs)
    [2019-07-08 13:08:57] <sarang> There's a non-public draft writeup already, but I assume he'll work it into the main paper once the modified security proofs are complete
    [2019-07-08 13:09:10] <suraeNoether> oooof
    [2019-07-08 13:09:18] <suraeNoether> very interesting consequences
    [2019-07-08 13:09:32] <sarang> Regardless, it's a damn clever construction
    [2019-07-08 13:10:08] <suraeNoether> i'm excited to read all about it
    [2019-07-08 13:10:20] <sarang> I'll ask if I can send it to you suraeNoether (not public though, sorry)
    [2019-07-08 13:10:43] <sarang> I'm investigating a possible modification to Omniring that splits out the range proofs, improving verification batching at the cost of proof size
    [2019-07-08 13:10:56] <sarang> And, because of the Omniring non-batching currently available, am revisiting analysis of RCT3
    [2019-07-08 13:11:29] <sarang> Which, while it would require a separate output pool (non-compatible key image structure), does allow for batching of proofs (aside from ring member group elements, which cannot be batched unless reused)
    [2019-07-08 13:11:44] <suraeNoether> last we spoke about this, we were still interested in writing up a comparison paper, but you've done all the legwork on it so far
    [2019-07-08 13:11:49] <suraeNoether> still the plan?
    [2019-07-08 13:12:52] <sarang> I don't consider a formal paper necessary, or even a great use of time
    [2019-07-08 13:13:02] <sarang> But analyses of spacetime, totally
    [2019-07-08 13:13:34] <suraeNoether> fair, maybe we can do a blog post on tradeoffs between the three schemes or something
    [2019-07-08 13:13:57] <sarang> Maybe, but it gets subtle and complex really quickly under many different assumptions
    [2019-07-08 13:14:10] <sarang> There isn't really a quick-and-dirty soundbite answer to which is better or worse
    [2019-07-08 13:14:25] <sarang> Depends heavily on input/output structure, use of fixed epochs, batch behavior, etc.
    [2019-07-08 13:14:57] <sarang> and output pool migration is nontrivial
    [2019-07-08 13:15:06] <sarang> Omniring would _not_ require this... Lelantus and RCT3 would
    [2019-07-08 13:15:18] <sarang> (or rather, Omniring does not _require_ this)
    [2019-07-08 13:17:10] <suraeNoether> see... when you say all that, it seems like it *is* a good use of time. maybe not high priority, but
    [2019-07-08 13:17:36] <sarang> A comparison is useful, I agree. But I don't want it to get lost in unnecessary formality of a full paper
    [2019-07-08 13:17:47] <sarang> And a comparison is exactly what I'm doing
    [2019-07-08 13:19:28] <sarang> Any questions on these topics?
    [2019-07-08 13:19:48] <sgp_> Just a comment to say simple comparisons are good
    [2019-07-08 13:20:15] <sarang> roger
    [2019-07-08 13:20:25] <sarang> Does anyone else have research topics of interest to share?
    [2019-07-08 13:21:54] <sarang> Righto!
    [2019-07-08 13:22:00] <nioc> suraeNoether: people are wondering what the attendance was at konferenco
    [2019-07-08 13:22:18] <sarang> At least provide a range proof
    [2019-07-08 13:22:48] <moneromooo> 26 people and 172 sybils.
    [2019-07-08 13:23:16] <nioc> an article in coindesk mentioned 75 which I know is way low
    [2019-07-08 13:23:17] <suraeNoether> nioc: i'm finishing up my post-mortem report on the konferenco today (on my action item list). We had 150 swag bags made, with around 30-40 leftover, but we had 27 speakers and like 10 sponsors.
    [2019-07-08 13:23:56] <nioc> I estimated 120 just by glancing
    [2019-07-08 13:24:05] <suraeNoether> 75 is the number i gave coindesk for the number of attendees on Saturday morning, but more people bought tickets on both days and the totals were higher
    [2019-07-08 13:24:25] <suraeNoether> if you count speakers and sponsors, that's around 110 on the first day, and around 125 the second
    [2019-07-08 13:24:31] <nioc> think you mran Sunday morning
    [2019-07-08 13:24:34] <nioc> mean
    [2019-07-08 13:25:18] <suraeNoether> nope, we sold tickets throughout the afternoon on saturday and a few on sunday too. but coindesk asked for a comment on saturday morning, so i told them what i had sold at that point
    [2019-07-08 13:25:26] <nioc> I'll wait for the report
    [2019-07-08 13:25:29] <suraeNoether> k
    [2019-07-08 13:25:30] <nioc> thx
    [2019-07-08 13:25:33] <sarang> suraeNoether: congratulations on effectively committing yourself to running a kickass conference annually until the end of time =p
    [2019-07-08 13:25:58] <suraeNoether> it was actually some of the best days of my life, but i've been told explicitly by my doctors that i need to take a vacation
    [2019-07-08 13:26:19] <suraeNoether> so i'm planning for that in august, since scary cardio and internal medicine people told me so with stern voices
    [2019-07-08 13:26:20] <sarang> Well then, let's move on to ACTION ITEMS
    [2019-07-08 13:26:58] <sarang> I have many things in progress. Lelantus proof review, modified Omniring split proof analysis, RCT3 analysis, and starting to put together my defcon talk/workshop
    [2019-07-08 13:26:59] <suraeNoether> my action items: konferenco post mortem, research report for previous quarter, funding request for the next 3 months, and some debuggin
    [2019-07-08 13:27:33] <sarang> I'm doing a talk on transaction protocols (very high level), a workshop on simple cryptographic constructions with Python, and a panel discussion at the blockchain village
    [2019-07-08 13:27:52] <suraeNoether> oh and i'm definitely not going to defcon this year. i can ship leftover swag like our USB data blockers with the monero logo and our pull-up banners if someone sends me the information for it
    [2019-07-08 13:28:02] <sarang> :(
    [2019-07-08 13:28:22] <sarang> The pull-up banners would be nice, assuming it's cheaper to ship than to get new ones
    [2019-07-08 13:28:32] <sarang> as would the USB blockers
    [2019-07-08 13:29:45] <suraeNoether> i'll look into it; ordering the usb blockers may be short notice but i can find out
    [2019-07-08 13:29:59] <suraeNoether> unless you just meant shipping the banners
    [2019-07-08 13:30:01] <suraeNoether> which is cool too
    [2019-07-08 13:30:08] <sarang> Yeah I meant the banners
    [2019-07-08 13:30:20] <sarang> I believe there was an idea to perhaps order more blockers for this (I'm not the one to ask)
    [2019-07-08 13:30:41] <sarang> If you have extra USB blockers and would ship with the banners, cool
    [2019-07-08 13:31:11] <suraeNoether> fantastic, i am happy folks liked the blockers
    [2019-07-08 13:31:36] <sarang> Any last questions or comments before we formally adjourn, since agenda topics have been completed?
    [2019-07-08 13:32:11] <sarang> Going once
    [2019-07-08 13:32:23] <sarang> twice
    [2019-07-08 13:32:32] <sarang> adjourned!
    [2019-07-08 13:32:44] <sarang> Thanks to everyone for attending; logs will be posted shortly on the github issue


# Action History
- Created by: SarangNoether | 2019-07-07T17:22:01+00:00
- Closed at: 2019-07-08T17:35:33+00:00
