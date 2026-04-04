---
title: 'Research meeting: 7 October 2019 @ 17:00 UTC'
source_url: https://github.com/monero-project/meta/issues/398
author: SarangNoether
assignees: []
labels: []
created_at: '2019-10-03T12:35:55+00:00'
updated_at: '2019-10-07T18:17:11+00:00'
type: issue
status: closed
closed_at: '2019-10-07T18:17:11+00:00'
---

# Original Description
Join in for the weekly Monero Research Lab meeting.

**When**: Monday, 7 October 2019 @ 17:00 UTC
**Where**: #monero-research-lab (freenode/matrix)

**Agenda**
1. Greetings

2. Roundtable
a. Sarang: [Lelantus update](https://lelantus.io/enabling-untraceable-anonymous-payments.pdf), updated RCT3 [proof-of-concept](https://github.com/SarangNoether/skunkworks/tree/rct3/rct3) and [analysis](https://github.com/SarangNoether/skunkworks/blob/sublinear/rct3.md)
b. Surae
c. Others?

3. General questions

4. Action items

# Discussion History
## Mitchellpkt | 2019-10-07T16:50:30+00:00
## Lock time

Should we reassess the optimal lock time? This has been mentioned a few times, since we're switching to consensus-level enforcement.

Here is one possible framework for the conversation: [https://github.com/noncesense-research-lab/lock_time_framework/blob/master/writeup/lock_time_framework.pdf](https://github.com/noncesense-research-lab/lock_time_framework/blob/master/writeup/lock_time_framework.pdf)

Thoughts?

## Mitchellpkt | 2019-10-07T16:53:47+00:00
## Primary/subaddress information leak

Suppose I'm an outside observer. It sounds like I might be able to look at any transaction and conclude one of two possibilities:
-  No outputs were sent to subaddresses (all primary addresses)
-  One or more outputs were destined for a subaddress(es)

Is this right? What are the implications for fungibility?

## SarangNoether | 2019-10-07T18:17:11+00:00
    [2019-10-07 10:00:58] <sarang> GREETINGS
    [2019-10-07 10:01:18] <suraeNoether> howdy!
    [2019-10-07 10:02:29] <ArticMine> hi
    [2019-10-07 10:03:09] <sarang> I suppose we can jump into ROUNDTABLE discussion
    [2019-10-07 10:03:11] <sarang> suraeNoether: ?
    [2019-10-07 10:04:11] <suraeNoether> sure; I've been working on my matching code. I fixed a few bad unit tests, i fixed a problem that was making the code take O(n^2) time and now it takes O(n) time... the challenger code and the parameter space explorer code are nearing completion, and my simulations are still misbehaving
    [2019-10-07 10:04:42] <sarang> Any ideas what exactly is misbehaving?
    [2019-10-07 10:04:54] <suraeNoether> i'm also beginning to read about an idea by randomrun and thinkinga bout security proofs for it
    [2019-10-07 10:05:28] <suraeNoether> well, no, that's what's strange. i have unit tests that check things like "check that the correct number of nodes are added to the graph", and they all pass those things... but then the integrated simulation as a whole produces a bad output file
    [2019-10-07 10:05:49] <suraeNoether> which is why i posted the stupid gif the other day of "two unit tests, no integration test"
    [2019-10-07 10:06:16] <sarang> I see
    [2019-10-07 10:06:23] <suraeNoether> but i'm working on it, and i have a few clues... and six more unit tests i'm coding up this afternoon
    [2019-10-07 10:06:30] <sarang> excellent
    [2019-10-07 10:07:01] <suraeNoether> i also want to bring up the topics that isthmus posted on github
    [2019-10-07 10:07:11] <sarang> Let's save those until he returns
    [2019-10-07 10:07:11] <suraeNoether> but we should hold off till the end of the meeting to chat about those
    [2019-10-07 10:07:29] <suraeNoether> *nod* he may not return, though, and we should chat about it in public today eventually either way
    [2019-10-07 10:07:35] <sarang> I've worked on a few things this past week
    [2019-10-07 10:07:48] <sarang> I collaborated with Aram on a Lelantus update: https://lelantus.io/enabling-untraceable-anonymous-payments.pdf
    [2019-10-07 10:08:03] <sarang> It seems to solve the sender tracing issue, but at the cost of proper one-time addressing
    [2019-10-07 10:08:29] <suraeNoether> hmm *taps chin*
    [2019-10-07 10:08:38] <sarang> Trying to fix both at the same time keeps running into a wall involving Pedersen generators
    [2019-10-07 10:09:01] <suraeNoether> i'm very interested to spend some time catching up on that trade-off
    [2019-10-07 10:09:10] <sarang> So we're looking at possible ways to use Schnorr representation proof tricks here... nothing so far though
    [2019-10-07 10:09:39] <sarang> Aside from that, I updated the RCT3 proof-of-concept code and spacetime analysis to reflect the new version of the preprint that was released
    [2019-10-07 10:10:39] <sarang> They compress the spend proof across inputs, but this incurs some major cost in padding inputs
    [2019-10-07 10:10:57] <sarang> Unfortunately, undoing that compression doesn't play nicely with their integrated balance proof
    [2019-10-07 10:11:49] <sarang> As in, (number of spends)*(size of anonymity set) must be a power of 2, or padded to one
    [2019-10-07 10:12:25] <suraeNoether> iirc lelantus originally used a tree structure, yeah? is that why?
    [2019-10-07 10:12:49] <sarang> Is what why?
    [2019-10-07 10:13:06] <suraeNoether> is that why they require padding inputs to powers of two?
    [2019-10-07 10:13:14] <sarang> RCT3, not Lelantus
    [2019-10-07 10:13:26] <sarang> It has to do with the inner-product argument that it uses for compression
    [2019-10-07 10:13:27] <suraeNoether> gack, got them confused~ nevermind, i retract my question
    [2019-10-07 10:13:34] <suraeNoether> ah, that makes sense too
    [2019-10-07 10:14:05] <sarang> It would be nice to get separate spend proofs if only to avoid this padding issue
    [2019-10-07 10:14:18] <sarang> but that would require redoing security proofs etc.
    [2019-10-07 10:15:13] <sarang> Finally, I've been working more on some ideas RandomRun had for Triptych involving balance proofs and multiple spends
    [2019-10-07 10:15:57] <sarang> I have a simple version of the Groth proving system that supports proving knowledge of multiple commitment openings to zero, along with linking
    [2019-10-07 10:16:26] <sarang> but haven't done any security proofs (in particular, I have some questions about the uniqueness requirements on certain proof elements)
    [2019-10-07 10:16:39] <sarang> Getting balance integrated is tricky, and that's what I'm working on now
    [2019-10-07 10:17:10] <suraeNoether> is there any write-up anywhere you and/or RR are willing to share with the public, or is this still too much "in prep"?
    [2019-10-07 10:17:34] <sarang> His ideas are listed in the GitHub issue here: https://github.com/monero-project/research-lab/issues/56
    [2019-10-07 10:17:51] <sarang> and the work-in-progress code is here, but very unfinished: https://github.com/SarangNoether/skunkworks/tree/lrs/lrs
    [2019-10-07 10:17:58] <suraeNoether> gotcha
    [2019-10-07 10:17:59] <sarang> and very probably insecure as written
    [2019-10-07 10:18:21] <sarang> Right now it's just at the playing-around-with-the-algebra stage, to see what's useful/possible
    [2019-10-07 10:18:25] <suraeNoether> it's good to clarify that before some other coin goes and implements it :P
    [2019-10-07 10:18:46] <sarang> Anyway, kudos to RandomRun on some really clever ideas to extend that Groth proving system
    [2019-10-07 10:18:55] <sarang> TBH it's probably worth a short paper on its own
    [2019-10-07 10:19:19] <sarang> Right now (if proven secure, mind you) it turns Groth's idea for a ring signature into a linkable ring signature
    [2019-10-07 10:19:39] <sarang> If the balance proof extension works, then we're really cooking
    [2019-10-07 10:19:53] <sarang> Efficiency TBD
    [2019-10-07 10:21:40] <sarang> While we wait for Isthmus to return, I can wrap up by saying my ACTION ITEMS for the week are trying to get balances working in Triptych, finishing a presentation on transaction protocols, and getting caught up on some lit review
    [2019-10-07 10:21:56] — Isthmus just got out of the meeting, is catching up on backlog
    [2019-10-07 10:22:03] <suraeNoether> good timing bruh
    [2019-10-07 10:22:09] <sarang> Isthmus: we didn't talk about your items at all
    [2019-10-07 10:22:22] <sarang> Care to go over them now?
    [2019-10-07 10:22:45] <Isthmus> Sure
    [2019-10-07 10:23:11] <Isthmus> One of the things I've been pondering about is how to assess the appropriate (safe) lock time
    [2019-10-07 10:23:23] <Isthmus> Here is one possible framework for the conversation: https://github.com/noncesense-research-lab/lock_time_framework/blob/master/writeup/lock_time_framework.pdf
    [2019-10-07 10:24:50] <Isthmus> Since the lock time only needs to be longer than reorg events, we can approach the question systematically by enumerating the list of things that cause alternative blocks, assessing the maximum plausible length of alternative chains that they could produce, and buffer that with a safety term
    [2019-10-07 10:25:03] <sarang> Enumerating the expected sources of reorganizations is a good idea, now that you have some empirical data on latency-based reorgs
    [2019-10-07 10:25:07] <Isthmus> My goal is to take the conversation out of the realm of intuition, towards addressing specific things that we can model/discuss/etc. :- )
    [2019-10-07 10:25:32] ⇐ xmrmatterbridge quit (~xmrmatter@lists.getmonero.org): Remote host closed the connection
    [2019-10-07 10:25:39] <sarang> I seem to recall some talk a long while ago about individual nodes that had observed much longer reorgs, but I assume these were not global?
    [2019-10-07 10:25:43] <sarang> (for some definition of global)
    [2019-10-07 10:26:02] <Isthmus> Well, that was back when there were ASICs on the network
    [2019-10-07 10:26:05] <suraeNoether> i'm inclined toward T2 or T3. the selection of an enforced lock time to ban inarguably-too-short txn times is easy and has an immediate benefit to the system. analysis paralysis while selecting an "optimal" lock time isn't desirable, and having the enforced lock time in place - even if we don't change the current lock time - is critically important
    [2019-10-07 10:26:57] → xmrmatterbridge joined (~xmrmatter@lists.getmonero.org)
    [2019-10-07 10:27:07] <Isthmus> Yeah, (should we enforce lock time?) and (how long should lock time be?) are two distinct questions
    [2019-10-07 10:27:36] <suraeNoether> so, here's the deal
    [2019-10-07 10:27:55] <sarang> There seemed to be good support for consensus enforcement of whatever value is chosen
    [2019-10-07 10:28:27] ⇐ xmrmatterbridge quit (~xmrmatter@lists.getmonero.org): Remote host closed the connection
    [2019-10-07 10:28:37] <sgp_> Is it worth exploring privacy implications as well? It could be that the longer the lock time, the better it is for network privacy to some extent
    [2019-10-07 10:29:07] <suraeNoether> sgp_: this is especially true if the lock time is longer than the median spend-time
    [2019-10-07 10:29:12] <suraeNoether> but that's not a desirable lock time
    [2019-10-07 10:29:26] <suraeNoether> for obvious reasons
    [2019-10-07 10:30:02] <suraeNoether> so, the deal i'm thinking is that it's easy to discern what is *unacceptably long* or short in lock times
    [2019-10-07 10:30:21] <suraeNoether> a lock time of two blocks is too short, a lock time of 90 days is too long, for sure
    [2019-10-07 10:30:46] <sgp_> I don't think it needs to be the main topic (chain re-orgs are more important imo), but it's worth considering
    [2019-10-07 10:30:59] <sgp_> I think we will have a tough time reducing it from 10 honestly for UX reasons
    [2019-10-07 10:31:27] <suraeNoether> i guess my question is
    [2019-10-07 10:31:37] <suraeNoether> does anyone have an argument in favor of using a value *other than 10*
    [2019-10-07 10:31:38] <sgp_> *tough time increasing it
    [2019-10-07 10:31:56] <sgp_> suraeNoether: I would like to justify a smaller number for UX reasons if possible
    [2019-10-07 10:32:28] <suraeNoether> i wouldn't dare lower it further than 10
    [2019-10-07 10:32:29] <sgp_> Isthmus's document outlines a basic framework for coming up with a number
    [2019-10-07 10:32:39] <sgp_> suraeNoether: based on what though?
    [2019-10-07 10:32:46] <suraeNoether> or let me rephrase that, because "i wouldn't dare" is a bit dramatic
    [2019-10-07 10:33:11] <suraeNoether> sgp_: well, we've witnessed many re-orgs length longer than 10. they are downright *common*
    [2019-10-07 10:33:30] <suraeNoether> moreover, spend-times that are lower than 20 minutes are *extremely* noticable in a txn graph
    [2019-10-07 10:33:55] <suraeNoether> if a sequence of very fast chained txns occur in a row, you can almost bet your ass that they're the same person churning.
    [2019-10-07 10:33:56] <ArticMine> The question in my mind is what is an acceptable risk probability for T2, and T3
    [2019-10-07 10:34:11] <suraeNoether> ArticMine: that was the question that popped into my mind
    [2019-10-07 10:34:13] <sgp_> that's what I was referring to from the privacy angle
    [2019-10-07 10:34:31] <suraeNoether> *nod*
    [2019-10-07 10:34:33] <sarang> Do you happen to know the corresponding threshold for Bitcoin's choice of typical lock time?
    [2019-10-07 10:34:55] <sarang> I don't, off the top of my head
    [2019-10-07 10:35:06] <suraeNoether> ^ sgp_ or ArticMine or isthmus?
    [2019-10-07 10:35:11] <sgp_> nope
    [2019-10-07 10:35:16] <suraeNoether> hm
    [2019-10-07 10:35:49] <Isthmus> I'm avoiding commenting on any particular numbers until we decide on a framework for discussing
    [2019-10-07 10:36:04] → Common-Deer joined (~CommonDee@14-202-132-82.static.tpgi.com.au)
    [2019-10-07 10:36:30] <suraeNoether> personally i would find it helpful to have those numbers in deciding the framework
    [2019-10-07 10:36:48] <sarang> Here's a writeup that I'd seen before: https://bitcoil.co.il/Doublespend.pdf
    [2019-10-07 10:36:49] <dEBRUYNE> sarang: Bitcoin has no lock time for normal transactions
    [2019-10-07 10:37:01] <dEBRUYNE> You can essentially chain unconfirmed transactions
    [2019-10-07 10:37:25] <suraeNoether> dEBRUYNE: thanks that's important to know, too. :P
    [2019-10-07 10:37:25] <sarang> Page 8 shows some example data based on hashrate and confirmations using Bitcoin as an example
    [2019-10-07 10:37:29] <Isthmus> Chicken/egg, don't need numbers for the framework
    [2019-10-07 10:37:41] <sgp_> I see your point Isthmus
    [2019-10-07 10:37:46] <Isthmus> Does buffering the lock time to be greater than the worst case plausible scenario make sense as a framework?
    [2019-10-07 10:37:46] <sarang> dEBRUYNE: but most clients use the 6-confirmation rule for "confirmed" transactions
    [2019-10-07 10:38:06] <suraeNoether> Isthmus: if we did this, our lock time would have to be >> 23
    [2019-10-07 10:38:13] <sarang> I was curious about that particular choice's assumptions
    [2019-10-07 10:38:13] <suraeNoether> iirc we saw a 23-block reorg recently
    [2019-10-07 10:38:15] <dEBRUYNE> It is a soft rule essentially
    [2019-10-07 10:38:20] <dEBRUYNE> You can easily overrule it
    [2019-10-07 10:38:35] — Isthmus tries to reverse what suraeNoether is saying
    [2019-10-07 10:38:51] <sgp_> Let's consider a 3 standard deviation scenario
    [2019-10-07 10:38:57] <sarang> dEBRUYNE: right, but I'm simply curious to make a comparison
    [2019-10-07 10:39:07] <Isthmus> Lock_time = Safety*(max(len_latency, len_51%, len_selfish...))
    [2019-10-07 10:39:11] <Isthmus> So if you're saying that would be 23
    [2019-10-07 10:39:13] ⇐ Common_Deer quit (~CommonDee@14-202-132-82.static.tpgi.com.au): Ping timeout: 250 seconds
    [2019-10-07 10:39:15] <Isthmus> You're saying lock
    [2019-10-07 10:39:18] <Isthmus> lock_time = 23
    [2019-10-07 10:39:25] <Isthmus> What are you using as your value for the Safety term?
    [2019-10-07 10:39:36] <Isthmus> And which term in the max are you looking at?
    [2019-10-07 10:39:57] <suraeNoether> ah, good questions
    [2019-10-07 10:39:58] <Isthmus> I never suggested any value for the safety term, so I'm trying to figure out how we got to 23 :- P
    [2019-10-07 10:40:05] <suraeNoether> no no
    [2019-10-07 10:40:06] <suraeNoether> that's not the 23
    [2019-10-07 10:40:17] <suraeNoether> i'm saying max(...) > 23, because we've seen 23 within the last year
    [2019-10-07 10:40:27] <Isthmus> Woah, I totally missed that
    [2019-10-07 10:40:28] <Isthmus> When?
    [2019-10-07 10:40:31] <suraeNoether> so whatever number we select needs to be > safety*23
    [2019-10-07 10:40:32] <Isthmus> We can fish it out of the NRL logs
    [2019-10-07 10:40:33] <sarang> That was from a single node report, no?
    [2019-10-07 10:41:05] <suraeNoether> sarang: *shrug* even if it was 15, or 12, safety*12 for any safety > 1 is going to be bigger than 20, generally
    [2019-10-07 10:41:46] <sgp_> That's why I think looking at all reogs and using 3sd longer than normal or something like that is a more practical number
    [2019-10-07 10:41:49] <suraeNoether> my point is: if we look at how common re-orgs are, and if we want to protect against those, we need unreasonably long lock times that risk slowing down the monero economy
    [2019-10-07 10:42:31] <sarang> sgp_: all observed reorgs, regardless of assumed origin (latency, high-hashpower entity, etc.)?
    [2019-10-07 10:43:07] <sgp_> sarang: I would need to go deeper into the numbers, but I just want to see what the numbers are without some of the outliers
    [2019-10-07 10:43:09] <Isthmus> I've been out of the loop, so I'm not disagreeing. But wowza, I hadn't seen anything *global* greater than length 2 since we switched to CryptoNoteR
    [2019-10-07 10:43:14] <suraeNoether> sgp_: *nod* we should look at the distribution of re-org times, though, and decide on a rigorous statistic instead of picking 3*stdev, but your point is 100% correct
    [2019-10-07 10:43:15] <sgp_> that's the overall point I want to convey
    [2019-10-07 10:43:45] <ArticMine> I suggest a risk based approach. Starting with who bears the risk?
    [2019-10-07 10:43:50] <sgp_> eg: if there was 1 reog at 20 and every other one is <3, that's important to know
    [2019-10-07 10:43:53] <sarang> I think using data and methods from the Bitcoin community for risk estimates of high-hashpower entities would be useful as one data point
    [2019-10-07 10:44:16] <sgp_> Isthmus: in terms of the framework however, I think we need to add some privacy implications
    [2019-10-07 10:44:26] <Isthmus> True, though the Gini coefficient for BTC hashrate is probably much more lopsided that Monero's distribution
    [2019-10-07 10:44:42] <sgp_> shrinking the lock time likely has adverse privacy implications
    [2019-10-07 10:44:54] <sgp_> and it also have positive UX implications
    [2019-10-07 10:45:06] <ArticMine> There are some significant differences in Bitcoin: 1) Great Firewall of China 2) 10 min blocks
    [2019-10-07 10:45:10] ⇐ ferretinjapan quit (ferretinja@gateway/vpn/privateinternetaccess/ferretinjapan): Quit: Leaving
    [2019-10-07 10:46:16] <Inge-> Better UX at the cost of privacy sounds like ... not-Monero.
    [2019-10-07 10:46:43] — Isthmus nods at Artic
    [2019-10-07 10:46:46] <Isthmus> I suspect (and I may totally backtrack this later...) that the fact we flip coins every 2 minutes rather than every 10 minutes may mean we reach stable equilibrium faster
    [2019-10-07 10:47:42] <sgp_> Inge-: it's about the tradeoff. No one would use a coin with a lock time of 100 days
    [2019-10-07 10:47:50] <Isthmus> SLOWNERO
    [2019-10-07 10:47:53] <Isthmus> YESSSS
    [2019-10-07 10:47:53] <suraeNoether> ^ nah, it's like using a smooth/exponential curve for a mortgage versus discretized timesteps using monthly annualization formulas: one approximates the other, but you converge at the same rate
    [2019-10-07 10:48:01] <suraeNoether> wrt 2 minus vs 10
    [2019-10-07 10:48:08] <suraeNoether> okay, let's operate briefly assuming that the longest reasonable "natural" re-org is 6 blocks. it's smaller than our current lock time, longer htan isthmus' global data, and matches satoshi's arbitrary selection.
    [2019-10-07 10:48:14] <suraeNoether>  if we pick safety = 2 or 3, we are still looking at 12 or 18 lock time, not shorter than 10.
    [2019-10-07 10:48:28] <suraeNoether> now, if we recall, block re-orgs don't always happen naturally and can take place due to adversarial behavior, using the longest one in history is incomplete
    [2019-10-07 10:48:41] <suraeNoether>  why? the attacker may hold off, biding their time on a real attack, until their attack power is most likely to lead to success.  Seeing only a few re-orgs of length 2-6 in the entire history of monero doesn't mean that an adversary can't force a 30-length re-org, as an example, so while the monero archival stuff that isthmus has been running is helpful
    [2019-10-07 10:49:08] <suraeNoether> i dunno, i feel like this is an unnecessary rabbit hole
    [2019-10-07 10:49:29] <sgp_> "past performance does not indicate future results." But I still like seeing how the network performs under normal scenarios
    [2019-10-07 10:49:30] <suraeNoether> or at least: why try to select a number other than 10 before the next hard fork?
    [2019-10-07 10:49:42] <suraeNoether> sgp_: well... *historical* scenarios anyway
    [2019-10-07 10:49:46] <ArticMine> So do we just stay with 10?
    [2019-10-07 10:50:03] <sgp_> let's agree on the framework first :)
    [2019-10-07 10:50:21] <sgp_> if we don't agree on anything, the status quo will remain (10)
    [2019-10-07 10:50:23] <Isthmus> Oh totally NOT trying to adjust this by the next fork
    [2019-10-07 10:50:28] <Isthmus> This is going to take us like 3 months to discuss
    [2019-10-07 10:50:33] <suraeNoether> oh, then if that's the case
    [2019-10-07 10:50:39] — suraeNoether wipes forehead
    [2019-10-07 10:50:47] <Isthmus> I was just responding to the ping from last meeting
    [2019-10-07 10:50:53] <Isthmus> I think enforce at 10 for this upcoming upgrade
    [2019-10-07 10:50:54] — suraeNoether puts his neckbeard away
    [2019-10-07 10:50:57] <Isthmus> Ahhahaha
    [2019-10-07 10:52:22] <Isthmus> Re @suraeNoether "this is an unnecessary rabbit hole",  As MRL, if we are going to inform lock time, we HAVE to go down three rabbit holes. 1) What's the longest plausible natural reorg, 2) What's the longest plausible attack, 3) what margin of error do we want?
    [2019-10-07 10:52:36] <Isthmus> I literally don't think there's a way to address the question if we're not willing to consider these
    [2019-10-07 10:53:03] <Isthmus> (I think... there may be some clever way to circumvent this...)
    [2019-10-07 10:53:05] <suraeNoether> i'm saying there is not a way to address this problem
    [2019-10-07 10:53:26] <Isthmus> What do you think about additive safety term versus multiplicative?
    [2019-10-07 10:53:31] <sgp_> suraeNoether: I agree on a theory level, but not on a practical level
    [2019-10-07 10:54:06] <suraeNoether> sgp_: yeah, i'm saying theoretically, there is no optimal solution. in practice, there will be a whole host of solutions that are "good enough" that have different tradeoffs between them depending on threat models
    [2019-10-07 10:54:19] <sgp_> ....have you worked on Monero before? lol
    [2019-10-07 10:54:20] <suraeNoether> this is why isthmus is using the word plausible here
    [2019-10-07 10:54:32] <suraeNoether> ...
    [2019-10-07 10:55:09] <sgp_> yeah it's a tradeoff, but we need to pick one, and there's potential reason to believe (with evidence) that a number other than 10 is best
    [2019-10-07 10:55:26] <suraeNoether> *cough* there is no best solution
    [2019-10-07 10:55:28] <sgp_> I'm open to changing the number with the right evidence
    [2019-10-07 10:55:46] <Isthmus> Maybe we can circle back to this next week with more recent numbers from the archival network regarding global events
    [2019-10-07 10:55:57] <ArticMine> Is it not possible to take a risk based approach for a framework?
    [2019-10-07 10:56:17] <Isthmus> @ArticMine yes, please share ideas :- )
    [2019-10-07 10:56:43] <ArticMine> 1) % hashrate of attacker
    [2019-10-07 10:57:09] <ArticMine> 2) Who bears the impact
    [2019-10-07 10:57:41] <ArticMine> 3) Type of impact ie double spend, privacy
    [2019-10-07 10:57:56] — Isthmus nods 
    [2019-10-07 10:59:26] <ArticMine> One should be able to derive risk provabilities
    [2019-10-07 10:59:33] <Isthmus> Some of #1 may be captured in Eq 3. Or at least I tried.
    [2019-10-07 10:59:35] <Isthmus> https://usercontent.irccloud-cdn.com/file/iRNSWEPW/image.png
    [2019-10-07 11:00:52] <sarang> Again, that Bitcoin-related paper does this type of hashrate-threshold analysis
    [2019-10-07 11:01:10] <ArticMine> Yes this is the type of analysis I mean
    [2019-10-07 11:01:15] <suraeNoether> 1) lock times > 50 or < 10 are extremely bad ideas for opposing reasons.
    [2019-10-07 11:01:27] <suraeNoether> 2) This leaves a narrow band of a half of a single order of magnitude.  not a lot of wiggle room.
    [2019-10-07 11:01:46] <suraeNoether> 3) going from 10 to 15 is extremely unlikely to have a dramatic or concrete impact on privacy; this is a 10 minute difference when we are speaking of distributions with medians around a day and a half
    [2019-10-07 11:01:55] <suraeNoether> 4)  Going from 10 to 40 is going to have huge impacts  on our economy, and would have to be justified by a veritable mountain of evidence
    [2019-10-07 11:01:58] ⇐ kl_ quit (uid344501@gateway/web/irccloud.com/x-mpqjmqclivhmrzhd): Quit: Connection closed for inactivity
    [2019-10-07 11:02:31] <suraeNoether> i look at this as willfully entering into analysis paralysis just because we have the data to answer questions about some very specific hypotheses
    [2019-10-07 11:02:32] <sarang> In the interest of time, may we table this and return when folks have had a chance to review the relevant analysis?
    [2019-10-07 11:03:05] <sgp_> yes please
    [2019-10-07 11:03:17] <sarang> Isthmus had one other item to discuss
    [2019-10-07 11:03:50] <Isthmus> So, I might not have 100% of the technical details right, so feel free to jump in with corrections:
    [2019-10-07 11:04:04] <sarang> It was the question of tx pubkey representation, since its use is different between primary and subaddresses
    [2019-10-07 11:04:10] <Isthmus> Yes, that.
    [2019-10-07 11:04:35] <Isthmus> The ability for an external observer to ascertain whether there were any subaddresses included in the construction of a transaction
    [2019-10-07 11:04:39] <Isthmus> Leaks information about the recipient
    [2019-10-07 11:04:46] <moneromooo> Or sender.
    [2019-10-07 11:04:46] <sarang> For some reason I thought that unique pubkeys were always used now, regardless of address type, to reduce distinguishability... but I need to check this
    [2019-10-07 11:04:58] <Isthmus> Yes, and/or sender
    [2019-10-07 11:05:29] <dEBRUYNE> sarang: Sure, that is fair, but in that instance I would set it to zero
    [2019-10-07 11:05:32] <sgp_> This is the first I am hearing of this
    [2019-10-07 11:05:47] <moneromooo> Actually... I'm not sure. The logic is a bit different for change IIRC...
    [2019-10-07 11:06:00] <suraeNoether> i'm a bit confused...
    [2019-10-07 11:06:07] <moneromooo> I hit that when I tried to add custom change addresses.
    [2019-10-07 11:06:25] <suraeNoether> isthmus do you have a small toy example you could show us?
    [2019-10-07 11:06:42] <Isthmus> Nope, I have no clue how the constructions differ
    [2019-10-07 11:06:44] <sarang> suraeNoether: for subaddress destinations, you use a unique tx pubkey
    [2019-10-07 11:06:58] <Isthmus> Well wait
    [2019-10-07 11:07:05] <Isthmus> Maybe I can fish up an example
    [2019-10-07 11:07:20] <Isthmus> Does tx_extra = (empty) imply no subaddresses were involved?
    [2019-10-07 11:07:37] <Isthmus> In that case I can just hit a block explorer
    [2019-10-07 11:07:51] <sarang> tx_extra stores tx pubkey, which is always included
    [2019-10-07 11:07:55] <suraeNoether> sarang: do you mean the tx pubkey is encoded differently?
    [2019-10-07 11:07:57] <suraeNoether> oh oh
    [2019-10-07 11:07:58] <suraeNoether> yeah
    [2019-10-07 11:07:59] <sarang> yes
    [2019-10-07 11:08:03] <suraeNoether> aha
    [2019-10-07 11:08:14] <Isthmus> Mmmmm
    [2019-10-07 11:08:17] <sarang> It's derived differently for primary and subaddresses
    [2019-10-07 11:08:35] <sarang> It's possible to use only one pubkey for multiple non-subaddress destinations
    [2019-10-07 11:08:46] <sarang> but this implies distinguishability
    [2019-10-07 11:08:50] <Isthmus> ^^^^
    [2019-10-07 11:08:54] <suraeNoether> hmm
    [2019-10-07 11:09:04] <sarang> I thought this had been changed to be unique per destination all the time, for this reason
    [2019-10-07 11:09:38] <suraeNoether> sarang i am beginning to recall this conversation and using a unique key per destination, and we didn't like that it revaled the number of dest addresses, or something...
    [2019-10-07 11:09:58] <sarang> Unique per output, is what I should have said
    [2019-10-07 11:10:13] <sgp_> why would the # of dest addresses be different than the number f outputs, unless someone is doing terrible churn?
    [2019-10-07 11:10:57] <suraeNoether> *shrug* users do dumb stuff all the time for dumb reasons
    [2019-10-07 11:11:27] <sarang> I will confer with moneromooo and examine code to see what the current default behavior is
    [2019-10-07 11:11:42] <Isthmus> +1
    [2019-10-07 11:11:59] <moneromooo> I purposefully shut up after what I said above since stoffu will know for sure, and I don't.
    [2019-10-07 11:12:47] <Isthmus> Cool, I think we can probably stick a pin in this, research over the week, and circle back with more concrete details about distinguishability under the current design.
    [2019-10-07 11:13:38] <ArticMine> +1
    [2019-10-07 11:13:48] <sarang> OK, any other action items before we adjourn?
    [2019-10-07 11:14:53] <sarang> Righto, thanks to everyone for participating


# Action History
- Created by: SarangNoether | 2019-10-03T12:35:55+00:00
- Closed at: 2019-10-07T18:17:11+00:00
