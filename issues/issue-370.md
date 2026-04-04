---
title: 'Research meeting: 15 July 2019 @ 17:00 UTC'
source_url: https://github.com/monero-project/meta/issues/370
author: SarangNoether
assignees: []
labels: []
created_at: '2019-07-11T20:08:05+00:00'
updated_at: '2019-07-15T18:08:53+00:00'
type: issue
status: closed
closed_at: '2019-07-15T18:08:53+00:00'
---

# Original Description
Join in for the weekly Monero Research Lab meeting.

**When**: Monday, 15 July 2019 @ 17:00 UTC
**Where**: #monero-research-lab (freenode/matrix)

**Agenda**
1. Greetings

2. Roundtable
a. Sarang: RCT3 analysis, Lelantus prover, RCT3 implementation
b. Surae
c. Others?

3. General questions

4. Action items

# Discussion History
## b-g-goodell | 2019-07-15T16:08:54+00:00
I'll be talking about 1) A set of guides I've written for hosting local Konferencos, and 2) Konferenco budget and attendance analysis, which took me most of this week. The budget will be made public some time this week, once I've checked everything again.. and again.. and again.

## SarangNoether | 2019-07-15T18:08:53+00:00
    [2019-07-15 13:00:18] <sarang> Let's start
    [2019-07-15 13:00:20] <sarang> GREETINGS
    [2019-07-15 13:00:59] <suraeNoether> howdy everyone
    [2019-07-15 13:01:26] <suraeNoether> anyone else here? :P
    [2019-07-15 13:01:30] — sarang waits awkwardly
    [2019-07-15 13:01:43] → TheoStorm joined (~TheoStorm@host-phyadb.cbn1.zeelandnet.nl)
    [2019-07-15 13:02:12] — dEBRUYNE reading
    [2019-07-15 13:02:18] <sarang> I suppose we can continue anyway
    [2019-07-15 13:02:22] <sarang> ROUNDTABLE
    [2019-07-15 13:02:28] <sarang> suraeNoether: care to begin?
    [2019-07-15 13:02:35] <suraeNoether> Sure. First, dEBRUYNE: I got an aswer from Jerry Brito re your question about bitlicense
    [2019-07-15 13:02:37] <hyc> hi
    [2019-07-15 13:02:46] <sarang> Can you repeat the question?
    [2019-07-15 13:02:49] <sarang> (for our logs)
    [2019-07-15 13:03:17] <suraeNoether> yes: dEBRUYNE was wondering if I could ask jerry brito about the possibilities of how Monero can work with the NYDFS bitlicense
    [2019-07-15 13:03:41] <suraeNoether> the example of Zcash being something that recently been listed on coinbase, etc, indicating that the NYDFS gave their blessing somehow
    [2019-07-15 13:04:07] <sarang> This is Zcash's compliance brief: https://z.cash/wp-content/uploads/2019/04/Zcash-Regulatory-Brief.pdf
    [2019-07-15 13:04:23] <sarang> You may find it useful
    [2019-07-15 13:04:34] <suraeNoether> it turns out that we have it backwards: exchange businesses or money transmitting business need to get valided through the NYDFS, and the reason that zcash was listed on coinbase had more to do with how much contact zcash has had with the coinbase team
    [2019-07-15 13:05:02] <suraeNoether> so, rather than having coincenter talk to NYDFS, what we need to do is start having meetings with people at coinbase, or gemini, or whichever platform we are discussing
    [2019-07-15 13:05:14] <suraeNoether> dEBRUYNE: does that make sense?
    [2019-07-15 13:05:24] <dEBRUYNE> Yes, thanks
    [2019-07-15 13:05:32] <dEBRUYNE> sarang: Also -> https://www.dfs.ny.gov/about/press/pr1805141.htm
    [2019-07-15 13:05:34] <sarang> Sure, it doesn't really make sense to have a protocol validated by a regulator anyway
    [2019-07-15 13:05:57] <suraeNoether> right
    [2019-07-15 13:06:00] <sarang> Wait, what?
    [2019-07-15 13:06:01] <suraeNoether> okay, moving past regulation
    [2019-07-15 13:06:08] <sarang> That press release specifically identifies assets
    [2019-07-15 13:06:11] <sarang> I don't really know what that means
    [2019-07-15 13:06:55] <sarang> This is why I am neither a regulator nor a lawyer :/
    [2019-07-15 13:07:14] <suraeNoether> well, let's move on and discuss it in a bit
    [2019-07-15 13:07:17] <sarang> Perhaps they go to regulators with a specific version or something, I dunno
    [2019-07-15 13:07:17] <sarang> sure
    [2019-07-15 13:07:27] <suraeNoether> a konferenco post morto update
    [2019-07-15 13:07:35] <sarang> s/morto/mortem ?
    [2019-07-15 13:07:47] <suraeNoether> latin or esperanto?
    [2019-07-15 13:07:52] <sarang> -____-
    [2019-07-15 13:07:56] <suraeNoether> lol
    [2019-07-15 13:08:10] — sarang sits down
    [2019-07-15 13:08:13] <suraeNoether> so anyway, i spent the past week doing a few things wrapping up the konferenco, including organizing the budget projected vs actuals
    [2019-07-15 13:08:32] <suraeNoether> and writing these four guide documents. THESE ARE INTENDED TO BE LIVING DOCUMENTS, UPDATED REGULARLY BY KONFERENCO ORGANIZERS.
    [2019-07-15 13:08:39] <suraeNoether> they are not commandments in stone.
    [2019-07-15 13:08:39] <suraeNoether> https://github.com/b-g-goodell/mrl-skunkworks/tree/master/Konferenco
    [2019-07-15 13:08:43] <suraeNoether> they are to be debated and argued
    [2019-07-15 13:08:48] <suraeNoether> sarang and i were debating funding structures earlier
    [2019-07-15 13:08:57] <sarang> vigorously
    [2019-07-15 13:09:07] <suraeNoether> KonGuide.docx is a general guide for maybe how things can go in the future
    [2019-07-15 13:09:33] <suraeNoether> i recommend even if you disagree with my budgeting/finance recommendations (with respect to the CCS or something), move past that and read the organizational part of the document
    [2019-07-15 13:09:45] <sarang> One note... using markdown instead of docx is much better for version history on git
    [2019-07-15 13:09:55] <sarang> (and displays natively via github)
    [2019-07-15 13:09:59] <suraeNoether> if someone wants to convert it, i'd love that
    [2019-07-15 13:10:07] <suraeNoether> i've been braindumping into libreoffice
    [2019-07-15 13:10:19] <suraeNoether> KonGuideKO.docx is designed for konferenco organizers
    [2019-07-15 13:10:32] <suraeNoether> this includes a list of things to do to get ready for the konferenco, including checklists at the end
    [2019-07-15 13:11:01] <suraeNoether> KonGuideSC.docx is designed for the "steering committee" which will probably have whoever is financially liable for the konferenco sitting on it. they make final budget decisions and sign contracts.
    [2019-07-15 13:11:19] <suraeNoether> KonGuideCC.docx is designed for the "content committee" which will be deciding on speakers and inviting them, and organizing the schedule
    [2019-07-15 13:11:43] <sarang> What are a couple/few things (briefly) you would have done differently, in hindsight?
    [2019-07-15 13:12:13] <suraeNoether> well, budgetarily, this was a nightmare. there were three very large sources of red on the budget sheet that should have been addressed
    [2019-07-15 13:12:42] <sarang> If you would have been able to more regularly cash out the CCS (or done it in chunks), would that have solved the problem?
    [2019-07-15 13:13:16] <suraeNoether> firstly, the original CCS request was designed to ask for 60,100$ but by the time I actually received it, it was worth $28,500 or so. waiting until it was done in one big chunk and then transferring it to me introduced so much time into the equation for price that volatility ate a lot of the money.
    [2019-07-15 13:13:37] <sarang> Not good for the organizers or donors
    [2019-07-15 13:13:47] <sarang> (they don't know the eventual value of their donations)
    [2019-07-15 13:14:02] <suraeNoether> one way to rectify that could be regularly withdrawing from the funding as it goes, another way would be to have funding take place in stages
    [2019-07-15 13:14:28] <suraeNoether> secondly, our turnout was much lower than we had all hoped
    [2019-07-15 13:14:38] <sarang> What if you raised money based on when different things needed to be purchased? Like the venue, or food, or A/V support, etc.
    [2019-07-15 13:14:58] <sarang> Then donors have specific things they can donate do, as opposed to more vague "this month's MonKon funding stage"
    [2019-07-15 13:15:09] <sarang> s/do/to
    [2019-07-15 13:15:46] <suraeNoether> so what happens if you drum up money by the payment deadline for venue but not A/V? it's a tricky question.
    [2019-07-15 13:15:50] <suraeNoether> i don't pretend to ahve all the answers
    [2019-07-15 13:15:58] — sarang clearly is not an event planner
    [2019-07-15 13:16:28] <suraeNoether> second source of funding problems: we had 58 general admission tickets, 4 student tickets, 11 platinum tickets, 27 speaker tickets, 13 sponsor tickets, and 3 media passes. our original budget was based on 230 attendees and 20 speakers. So, our ticket sales were disappointing in that regard.
    [2019-07-15 13:16:39] <sarang> Well presumably you would not be the one stuck with all this, and be able to focus more on research or MKon content instead
    [2019-07-15 13:17:05] <suraeNoether> but that was exacerbated since we were paying for flights and hotels for speakers, and the increased size of the speaker list caused increased requisite costs, too
    [2019-07-15 13:17:34] <suraeNoether> thirdly, and most fatally, i think, was the increased cost in A/V
    [2019-07-15 13:17:49] <sarang> Having quality recordings was huge
    [2019-07-15 13:18:02] <sarang> video views were pretty high
    [2019-07-15 13:18:15] <suraeNoether> our original proposal was 1/3 what we ended up paying (and that doesn't count any of the time or labor or equipment donated by parasew, marcvvs, and sgp)
    [2019-07-15 13:18:17] <suraeNoether> ^ bingo
    [2019-07-15 13:18:18] <sarang> And it meant that anyone could watch for free
    [2019-07-15 13:18:51] <suraeNoether> i think the A/V costs from this year is a good benchmark for future years, I don't think we got screwed on A/V, but our costs were very high in this area because of it
    [2019-07-15 13:19:04] <sarang> A/V is expensive, hands down
    [2019-07-15 13:19:29] <sarang> but it seems one of the best returns to the community
    [2019-07-15 13:19:31] <suraeNoether> so, long story short: the market murdered me, the ticket sales murdered me, and A/V murdered me, but i'm still alive despite thrice being murdered
    [2019-07-15 13:19:40] <sarang> you have 6 lives left
    [2019-07-15 13:19:51] <suraeNoether> nah, i was murdered twice already, i'm down to 4
    [2019-07-15 13:19:56] <sarang> Ignoring all the budgeting, I'd say it was a big success
    [2019-07-15 13:20:17] <suraeNoether> I agree. final budget will be posted later this week once i've octuply checked everything.
    [2019-07-15 13:20:43] <suraeNoether> nioc ^ check out our numbers from above. total attendance was like 117 before staff was included
    [2019-07-15 13:21:00] <sarang> that's not half bad for a first run
    [2019-07-15 13:22:06] <nioc> so my quick that totaled up 120 was not bad :)
    [2019-07-15 13:22:25] <suraeNoether> a few brief comments for the four guides i've written: you can do what you like, if you are planning on hosting a Konferenco Wien or a Konferenco Beijing or whatever, do what you like. But make sure all of your funding and structure details are 100% clear in your CCS. Sarang thinks some of my ideas about profit for these events are not fair to the community, so consider the whole set of documents worth
    [2019-07-15 13:22:25] <suraeNoether> arguing over and debating.
    [2019-07-15 13:22:40] <nioc> NYC during blockchain week and MCC will get you 3x
    [2019-07-15 13:22:41] <suraeNoether> nioc yeah, but in terms of *ticket sales* we had like 71 or 72 or something like that
    [2019-07-15 13:22:58] <suraeNoether> nioc yeah but it will 4x or 5x all our expenses
    [2019-07-15 13:23:18] <dEBRUYNE> Playing devils advocate, but the funds could've been hedged
    [2019-07-15 13:23:25] <dEBRUYNE> There are plenty of markets that allow short selling of xmr
    [2019-07-15 13:23:49] <sarang> There could have been more defined payouts
    [2019-07-15 13:24:48] <sarang> suraeNoether: anything else to discuss?
    [2019-07-15 13:24:52] <sarang> Or any questions for him?
    [2019-07-15 13:24:57] <suraeNoether> dEBRUYNE: yeah, I received the funds on 2-5-19 and by that point the damage had been done. that would be handled by the CCS guys
    [2019-07-15 13:25:11] <suraeNoether> sarang: defined payouts wouldn't have helped
    [2019-07-15 13:25:20] <suraeNoether> the market crashed basically welllllll before we needed any of the money
    [2019-07-15 13:25:25] <sarang> I see
    [2019-07-15 13:25:31] <dEBRUYNE> At what time was the donation completed though?
    [2019-07-15 13:25:39] <dEBRUYNE> Because at that point the price should've been hedged
    [2019-07-15 13:25:59] <suraeNoether> dEBRUYNE: my recollection is around xmas, but i could be misrecollecting
    [2019-07-15 13:26:08] <suraeNoether> luigi1111 may know
    [2019-07-15 13:26:15] <ArticMine> Yes if the expenses were in USD
    [2019-07-15 13:26:17] <suraeNoether> this question occurred to me yesterday and i forgot to write it down
    [2019-07-15 13:27:18] <dEBRUYNE> Price moved from ~50 to ~70 (from christmas to may), so that doesn't seem right
    [2019-07-15 13:30:26] <sarang> Shall we move on from this topic for now?
    [2019-07-15 13:30:31] <suraeNoether> dEBRUYNE: i had only gains from the time that i was holding crypto. i just received 591 XMR worth $28,509 at the time, whereas when I posted the request it was for 591 XMR worth $60,100. The question is the gap in time between funding-completed and the time it hit the Konferenco wallet on Feb 2
    [2019-07-15 13:30:36] <nioc> there were donations till at least Dec 16
    [2019-07-15 13:31:11] <suraeNoether> i'm fine with waiting for specific dates from luigi or whoever can tell us
    [2019-07-15 13:31:43] <suraeNoether> and moving on
    [2019-07-15 13:31:49] <suraeNoether> sarang, how about you tell us about something more research related?
    [2019-07-15 13:32:11] <sarang> Heh ok
    [2019-07-15 13:32:16] <sarang> I have a few things
    [2019-07-15 13:32:28] <luigi1111> I don't have info on completed funding dates
    [2019-07-15 13:32:31] <sarang> First, I ran a timing/space analysis for the RCT3 sublinear transaction protocol
    [2019-07-15 13:32:40] <luigi1111> not sure if there's a way to get it. surely can manually somehow
    [2019-07-15 13:33:09] <sarang> https://github.com/SarangNoether/skunkworks/blob/sublinear/rct3.md
    [2019-07-15 13:33:27] <sarang> I'm working up some proof-of-concept code for its spend proving system presently (not done)
    [2019-07-15 13:33:56] <sarang> I also worked up a proof of concept for a two-layer Lelantus prover that sacrifices size and verification time for shorter prove time
    [2019-07-15 13:34:05] <sarang> Interesting, but probably not relevant to our use case
    [2019-07-15 13:34:06] <luigi1111> I thought sponsors were going to cover some of the shortfall or something since we knew back then 591 wasn't enough
    [2019-07-15 13:34:27] <sarang> https://github.com/SarangNoether/skunkworks/blob/lelantus/lelantus/layer.py
    [2019-07-15 13:34:40] <dEBRUYNE> suraeNoether: I guess we can discuss this later. One more thing I wanted to ask though, the zcash donation was made in may
    [2019-07-15 13:34:50] <dEBRUYNE> Was that on top of the 28.5k then? Given that you received that earlier
    [2019-07-15 13:35:59] <luigi1111> in truth, ccs isn't particularly well suited for people or projects that are sensitive to volatility. there may be mitigations of course
    [2019-07-15 13:36:09] <suraeNoether> nope, they donated directly to the CCS so that was included
    [2019-07-15 13:36:38] <suraeNoether> luigi1111: the goal was to get corporate sponsorships
    [2019-07-15 13:36:41] <suraeNoether> luigi1111: we got some
    [2019-07-15 13:36:51] <suraeNoether> luigi1111: we did not get enough to cover the shortfall
    [2019-07-15 13:37:05] <luigi1111> I see
    [2019-07-15 13:38:13] <luigi1111> what is the shortfall?
    [2019-07-15 13:38:26] <suraeNoether> sarang sorry to interrupt you: good work on lelantus. have you worked out the tradeoff between our current size vs. verf time compared to a lelantus version with a faster prover?
    [2019-07-15 13:38:36] <suraeNoether> luigi1111: i'll be posting budget later this week
    [2019-07-15 13:38:44] <luigi1111> ok sounds good
    [2019-07-15 13:38:51] <sarang> The faster Lelantus prover makes sense for Zcoin, who want >O(10K) ring members
    [2019-07-15 13:39:06] <sarang> and, to be fair, you can batch away much of the verification loss
    [2019-07-15 13:39:23] <sarang> for O(100-100K) ring members it's likely not really a problem in practice
    [2019-07-15 13:39:36] <sarang> but it's still damn clever
    [2019-07-15 13:39:56] <suraeNoether> i'd be interested in seeing some hard numbers, like the value N such that for >O(N) ring members, the shorter prove time is worthwhile
    [2019-07-15 13:40:00] <sarang> whoops, O(100-1K)
    [2019-07-15 13:40:07] <sarang> define "worthwhile"...
    [2019-07-15 13:40:38] <sarang> all depends on what the max prove time (and the corresponding computational complexity) is that you're willing to accept
    [2019-07-15 13:40:55] <suraeNoether> or how much verf time/space you are willing to sacrifice
    [2019-07-15 13:41:00] → rehrar joined (~rehrar@gateway/tor-sasl/rehrar)
    [2019-07-15 13:41:06] <sarang> Zcoin has non-public numbers for this (can't share yet)
    [2019-07-15 13:41:21] <suraeNoether> k
    [2019-07-15 13:42:06] <sarang> However, it's pretty impressive... like, on the order of 10x improvement for large rings (in proving time)
    [2019-07-15 13:42:25] <sarang> I don't think the integration into the rest of the Lelantus prover is completed yet, FWIW
    [2019-07-15 13:42:39] <sarang> there's some info you need to extract from the 1-of-N proof for balance purposes that I haven't worked out
    [2019-07-15 13:43:18] <sarang> On the RCT3 side, this week I should have working code for that transaction protocol
    [2019-07-15 13:44:01] <sarang> I'm checking a bunch of their math (might have errors, not sure yet)
    [2019-07-15 13:44:38] <sarang> and that's about it for me
    [2019-07-15 13:44:41] <sarang> Any particular questions?
    [2019-07-15 13:47:02] <ArticMine> On a more mundane level of mixing I estimate we can move from 11 to 13 without touching fees
    [2019-07-15 13:47:28] <sarang> Based on my CLSAG numbers, you mean?
    [2019-07-15 13:47:30] <sarang> or something else?
    [2019-07-15 13:47:39] <ArticMine> No current tech
    [2019-07-15 13:47:40] <sarang> CLSAG will almost certainly not make it into the fall upgrade
    [2019-07-15 13:47:45] <sarang> How so?
    [2019-07-15 13:48:04] <suraeNoether> ArticMine: i would almost rather increase fees than ring size at this point :\
    [2019-07-15 13:48:28] <ArticMine> There was a drop in tx size last fork
    [2019-07-15 13:48:42] <suraeNoether> sarang i have a question: fill in the blank to complete the analogy. (lelantus protocol) : (monero protocol) :: (2-year old mid-range automobile with no damage) : ________
    [2019-07-15 13:48:51] <sarang> While bigger rings are generally better, a marginal increase from 11 to 13 will do little to help analysis that already exists
    [2019-07-15 13:49:06] <sarang> ...
    [2019-07-15 13:49:46] <suraeNoether> 2-year old mid-range refrigerator with no stink?
    [2019-07-15 13:49:56] <sarang> lol
    [2019-07-15 13:50:06] <sarang> maybe that cleaning car that the Cat in the Hat drives?
    [2019-07-15 13:50:08] — suraeNoether INCOMPARABLE
    [2019-07-15 13:50:18] <sarang> Looks cool, pretty functional, not sure what'd happen in practice =p
    [2019-07-15 13:50:33] <suraeNoether> how about the weird stretchy-squishy car from Willy Wonka
    [2019-07-15 13:50:39] <sarang> lol
    [2019-07-15 13:50:47] <suraeNoether> wait, has monero switched with lelantus in your analogy?
    [2019-07-15 13:50:51] <gingeropolous> bumpdaringsize
    [2019-07-15 13:50:54] <sarang> erm
    [2019-07-15 13:51:03] <suraeNoether> bumpdaringsize.gif
    [2019-07-15 13:51:08] <sarang> We should determine specific reasons why we would increase
    [2019-07-15 13:51:26] <sarang> e.g. things like chain reaction or accidental dead outputs are exceedingly unlikely now
    [2019-07-15 13:51:29] <gingeropolous> #1. 13 > 11
    [2019-07-15 13:51:42] <sarang> things like EABCD...ZE are presumably more unaffected by such a marginal change
    [2019-07-15 13:52:43] <suraeNoether> Does anyone have any questions for sarang about his lelantus work recently, other than stupid SAT analogies?
    [2019-07-15 13:52:50] <ArticMine> FloodXMR is very sensitive to ring size
    [2019-07-15 13:52:54] <sarang> (or on RCT3 for that matter)
    [2019-07-15 13:53:03] <sarang> Yes, but we don't have correct numbers on that yet
    [2019-07-15 13:53:14] <sarang> in terms of cost, that is
    [2019-07-15 13:53:42] <sarang> It should be quantified before a blind increase, IMO
    [2019-07-15 13:54:43] <suraeNoether> okay, everyone: i have to get to an appointment
    [2019-07-15 13:54:49] <sarang> roger
    [2019-07-15 13:55:28] <suraeNoether> remember, for the hypochondriacs: if the pain is behind and above your stomach, it could be pancreatitis and not a heart attack
    [2019-07-15 13:55:47] <ArticMine> Ok we wait for CLSAG and then take another look at mixin
    [2019-07-15 13:56:01] <sarang> I'm not saying we have to wait until spring
    [2019-07-15 13:56:09] <sarang> only that I'd prefer quantified reasons for an increase to know the benefits
    [2019-07-15 13:56:38] <sarang> Increasing from 11 to 13 won't stop a wealthy adversary from chain spamming with the current fee structure
    [2019-07-15 13:56:51] <sarang> knowing the added protection against deanon would be useful though
    [2019-07-15 13:57:01] <sarang> sgp_ has a useful little tool for this
    [2019-07-15 13:57:26] <sarang> I'll grab numbers for that part at least (the flood folks are running new simulations on a private testnet)
    [2019-07-15 13:58:10] <sarang> OK, does anyone else have work to share?
    [2019-07-15 13:58:16] <sarang> Or other updates relevant to this channel?
    [2019-07-15 13:58:46] <sarang> If not, we can leave the floor open to QUESTIONS while we go over ACTION ITEMS (to respect the time)
    [2019-07-15 13:59:14] <sarang> I'll grab numbers on an 11 -> 13 ring increase, finish up RCT3 proof-of-concept stuff, and continue defcon prep
    [2019-07-15 13:59:26] <sarang> suraeNoether can update us later when he returns
    [2019-07-15 13:59:34] <sarang> Any last questions or comments before we adjourn?
    [2019-07-15 13:59:38] <midipoet> i have read over konferenco talk, and have taken notes of the links...will digest. thanks suraeNoether
    [2019-07-15 14:00:29] <sarang> OK, we are now adjourned! Thanks to everyone for joining in
    [2019-07-15 14:00:39] <sarang> Logs will be posted to the github agenda issue shortly


# Action History
- Created by: SarangNoether | 2019-07-11T20:08:05+00:00
- Closed at: 2019-07-15T18:08:53+00:00
