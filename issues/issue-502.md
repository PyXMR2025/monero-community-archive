---
title: 'Research meeting: 2 September 2020 @ 17:00 UTC'
source_url: https://github.com/monero-project/meta/issues/502
author: SarangNoether
assignees: []
labels: []
created_at: '2020-08-26T17:53:02+00:00'
updated_at: '2020-09-03T22:20:28+00:00'
type: issue
status: closed
closed_at: '2020-09-02T18:12:22+00:00'
---

# Original Description
Join in for the weekly Monero Research Lab meeting.

**When**: Wednesday, 2 September 2020 @ 17:00 UTC
**Where**: #monero-research-lab (freenode/matrix)

**Agenda**
1. Greetings

2. Roundtable

3. Questions

4. Action items

# Discussion History
## Mitchellpkt | 2020-09-02T16:52:55+00:00
See attached ROUGH DRAFT of vulnerabilities to quantum algorithms. 

[pqMonero_technical_draft1.pdf](https://github.com/monero-project/meta/files/5163665/pqMonero_technical_draft1.pdf)

EDIT: updated drafts copied to https://www.overleaf.com/9835162385prbmyfckknyc


## SarangNoether | 2020-09-02T18:12:22+00:00
    [2020-09-02 12:59:26] <sarang> OK, let's start our research meeting
    [2020-09-02 12:59:33] <sarang> The usual agenda: https://github.com/monero-project/meta/issues/502
    [2020-09-02 12:59:36] <sarang> Logs posted there after the meeting
    [2020-09-02 12:59:38] <sarang> First, greetings!
    [2020-09-02 12:59:39] <sarang> Hello
    [2020-09-02 12:59:42] <ArticMine> Hi
    [2020-09-02 13:01:03] — Isthmus puts on goggles and lab coat
    [2020-09-02 13:01:15] <suraeNoether> hihi
    [2020-09-02 13:01:39] <suraeNoether> if we need eye protection for this meeting, i'm wearing open toed shoes so... uh...
    [2020-09-02 13:02:53] <sarang> OK, let's move to roundtable, where anyone is welcome to share research topics of interest
    [2020-09-02 13:03:09] <sarang> Isthmus: you had posted a paper draft on the agenda issue
    [2020-09-02 13:03:45] <Isthmus> Yep, just a rough draft of the audit portion of our research. It's a bit long to digest on the fly, but if y'all have any notes to share over the next few days we'd greatly appreciate it
    [2020-09-02 13:03:58] <sarang> This is great!
    [2020-09-02 13:04:21] <sarang> You said it's still being edited... would an edited version be posted separately, to make it easier for corrections?
    [2020-09-02 13:04:37] <sarang> Or should proofreading/review wait until edits are finished?
    [2020-09-02 13:04:37] <Isthmus> Hm?
    [2020-09-02 13:04:42] <Isthmus> Ohhhh
    [2020-09-02 13:04:52] <Isthmus> Yea, for the portions that I posted, please tear them apart
    [2020-09-02 13:05:00] <Isthmus> The parts that we're still editing were omitted from the draft shared above
    [2020-09-02 13:05:01] <sarang> Having edits criss-cross across versions and ongoing edits might get confusing
    [2020-09-02 13:05:03] <sarang> ok
    [2020-09-02 13:05:14] <h4sh3d[m]> Hi
    [2020-09-02 13:06:23] <sarang> I look forward to reading this Isthmus and suraeNoether
    [2020-09-02 13:07:14] <sarang> Any questions for Isthmus or suraeNoether?
    [2020-09-02 13:08:14] <Isthmus> Here is a link with EDIT access to the draft: https://www.overleaf.com/9835162385prbmyfckknyc
    [2020-09-02 13:08:29] <Isthmus> For anybody who finds it more convenient to drop notes in LaTeX
    [2020-09-02 13:08:39] <sarang> Are you comfortable having that link posted in the agenda issue logs?
    [2020-09-02 13:08:40] <Isthmus> This is a fork of the paper, so it's ok to futz around
    [2020-09-02 13:08:43] <sarang> oh ok
    [2020-09-02 13:09:22] <Isthmus> Yep, I'd just ask that people leave notes on what they edit, either as a comment with `%` or using the \anote{} feature which is a custom command to drop in little notes
    [2020-09-02 13:09:56] <sarang> You can also leave Overleaf comments on the side too
    [2020-09-02 13:10:03] <Isthmus> Oh yea, that'd probably be even better
    [2020-09-02 13:10:12] <sarang> Those have threading and resolution features
    [2020-09-02 13:10:42] <sarang> Thanks for the update Isthmus and suraeNoether!
    [2020-09-02 13:10:50] <sarang> I'll share a few things
    [2020-09-02 13:10:58] <suraeNoether> overleaf appears to have recently bunked up their comments and review functionality a bit, and it's become temperamental for me
    [2020-09-02 13:11:05] <sarang> Oh boo, that sucks
    [2020-09-02 13:11:06] <suraeNoether>  heh /aside
    [2020-09-02 13:11:30] <sarang> So the Triptych preprint was accepted to the ESORICS CBT workshop recently
    [2020-09-02 13:11:47] <sarang> It'll be included in their proceedings, and I will also make a presentation on it later this month
    [2020-09-02 13:12:08] <sarang> I had to do a recording of this in the event of technical difficulties, so thanks to sgp_ for helping me work out the details on that
    [2020-09-02 13:12:35] <sarang> The preprint has been updated on IACR for corrections, the proceedings version has been prepared separately, the slides for the presentation are posted on GitHub, and I have the recording done as well
    [2020-09-02 13:13:14] <sarang> sgp_ and I also interviewed CipherTrace's CEO, Dave Jevans, about a press release they made that received a fair amount of media attention
    [2020-09-02 13:13:40] <sarang> That has occupied more of my time than I had expected
    [2020-09-02 13:14:20] <sarang> and finally, I've been working with grydz to help them get the Ledger CLSAG firmware integration working
    [2020-09-02 13:14:26] <sarang> Huge thanks to grydz for their hard work on this
    [2020-09-02 13:15:05] <sarang> Any questions or comments for me on these topics?
    [2020-09-02 13:15:49] <Isthmus> Thanks for pouring time & effort into the unexpected CipherTrace happenings
    [2020-09-02 13:15:57] <Isthmus> Kind of a big fire to disrupt your workflow out of nowhere
    [2020-09-02 13:16:05] <ArticMine> That interview was excellent
    [2020-09-02 13:16:07] <Isthmus> Appreciate the context switching and great handling of that situation
    [2020-09-02 13:16:09] <Isthmus> ^ sgp too
    [2020-09-02 13:16:20] <sarang> Yeah, thanks to sgp_ for setting up that interview on such short notice
    [2020-09-02 13:16:41] <sarang> I think it was very helpful, even if there was little in the way of specific information
    [2020-09-02 13:16:46] <vikrants> hi.. Sarang was solid and taking no shit.
    [2020-09-02 13:17:01] <sarang> It's worth notice that Dave _did_ confirm that his company makes their own transactions on chain as part of their analysis efforts
    [2020-09-02 13:17:15] <sarang> I regret not following up on this at the time, but did submit questions on this to him afterward in writing
    [2020-09-02 13:17:38] <ArticMine> I suggest going over it multiple time to get all the nuances. There is a lot of very valuable information there, that I really want to analyze
    [2020-09-02 13:18:11] <sarang> Here is a link to the interview: https://www.youtube.com/watch?v=w5rtd3md11g
    [2020-09-02 13:18:11] <monerobux> [ CipherTrace's Monero tracing tool - Chat with Dave Jevans, Dr. Sarang Noether, and Justin Ehrenhofer - YouTube ] - www.youtube.com
    [2020-09-02 13:18:14] <ArticMine> Way more than meet the eye at a first glance
    [2020-09-02 13:18:15] <sarang> good bot
    [2020-09-02 13:18:44] <sarang> Dave also confirmed that the presence of a "flagged" output in a ring will raise the corresponding transaction's risk assessment
    [2020-09-02 13:19:08] <sarang> Even if the transaction otherwise has no particular reason for being identified as more "risky"
    [2020-09-02 13:19:12] <ArticMine> That is a big one even for Bitcoin
    [2020-09-02 13:19:30] <sarang> I ensured that he confirmed an understanding of the non-interactive nature of Monero signatures, which he did
    [2020-09-02 13:19:31] <sgp_> Oh hi :)
    [2020-09-02 13:19:36] <sarang> Hi sgp_
    [2020-09-02 13:20:32] <sarang> Anyway, sgp_ and I wrote some very specific questions that sgp_ sent in writing to Dave (yesterday IIRC)
    [2020-09-02 13:20:39] <ArticMine> Dave also showed concern over the false positives and negatives in Bitcoin. A key weakness
    [2020-09-02 13:20:41] <sgp_> Even so he confirmed they send poisoned outputs, likely against high-profile targets
    [2020-09-02 13:21:05] <sgp_> The way he described the scope did not give me the impression they are "spamming" outputs
    [2020-09-02 13:21:21] <sarang> Perhaps. This was one of the questions I posed in our follow-up
    [2020-09-02 13:21:34] <sarang> Whether they do "general spam" or targeted spends only
    [2020-09-02 13:21:53] <sarang> Anyway, AFAIK there has been no response yet to the questions, but it hasn't been that long since we sent them
    [2020-09-02 13:22:13] <sarang> ArticMine: yeah, I was careful to point out concerns over false positives
    [2020-09-02 13:22:29] <sarang> I did not leave with confidence about whether/how they try to avoid these in a meaningful way
    [2020-09-02 13:22:49] <Isthmus> Tricky part about decoy-based anonymity... We add false positives, but there are no false negatives
    [2020-09-02 13:23:02] <ArticMine> I am more convinced than ever they cannot even on Bitcoin
    [2020-09-02 13:23:09] <sarang> I also remain skeptical about how they take (possibly many) heuristics and methods and try to distill to a single number with some arbitrary threshold
    [2020-09-02 13:23:25] <sgp_> The tests have false negatives in practice though Isthmus
    [2020-09-02 13:23:36] <sarang> Namely, that what this _actually means_ is perhaps not meaningfully conveyed to their clients
    [2020-09-02 13:23:41] <Isthmus> I mean the transaction graph has no false negatives
    [2020-09-02 13:23:51] <Isthmus> The metrics that you put on top of them may
    [2020-09-02 13:24:04] <ArticMine> There is both sound math and compliance theatre
    [2020-09-02 13:24:48] <ArticMine> This is why I want to carefully analyze the interview
    [2020-09-02 13:25:07] <sarang> At any rate, I appreciate that Dave did the interview, though from a security perspective, making any design decisions based on the claims should be done extremely carefully
    [2020-09-02 13:25:32] <sarang> I don't have any particular reason to think Dave was not telling the truth, but I also have no particular reason to think he was being overly forthcoming
    [2020-09-02 13:25:34] <sgp_> Yeah, this changes nothing ultimately based on the current info we have
    [2020-09-02 13:25:57] <sarang> This is, however, a good chance to review known methods
    [2020-09-02 13:26:45] <ArticMine> I actually think we gained a lot of information. Even more that Dave was willing to give up
    [2020-09-02 13:26:56] <sarang> How so?
    [2020-09-02 13:27:17] <ArticMine> Confirming a lot of suspicions
    [2020-09-02 13:27:32] <sarang> Well, again, these are all claims
    [2020-09-02 13:27:40] <ArticMine> He was very clear on the Monero part was not ready for AML
    [2020-09-02 13:27:44] <sarang> Without any evidence or details, everything is claims and speculation
    [2020-09-02 13:27:55] <sarang> Including anything said in the interview
    [2020-09-02 13:28:11] <ArticMine> The specific scenario speaks volumes
    [2020-09-02 13:28:35] <Isthmus> Anything we hear that sounds like a plausible threat, we should take into account. Anything we hear that sounds like reassurance, we should distrust
    [2020-09-02 13:28:45] <sarang> ^ right on
    [2020-09-02 13:28:49] <ArticMine> I agree
    [2020-09-02 13:29:24] <ArticMine> The about helping Monero with exchanges is a good example of false reasurance
    [2020-09-02 13:29:58] <ArticMine> but as I mentioned this needs to be carefully analyzed
    [2020-09-02 13:30:03] <sarang> Well, I'm sure they'd rather sell their tool to exchanges that support Monero, rather than see no exchanges support Monero at all
    [2020-09-02 13:30:13] <sarang> (since they couldn't sell their tool in that situation)
    [2020-09-02 13:30:40] <sarang> So there's probably some kind of business incentive related to exchanges
    [2020-09-02 13:30:46] <sarang> but I'm no businesscritter
    [2020-09-02 13:31:20] <sgp_> Maybe we can move on since this discussion isn't really related to research
    [2020-09-02 13:31:27] <ArticMine> Even the slightest dent in Monero's privacy is a huge win from a sales perspective for them
    [2020-09-02 13:31:38] <ArticMine> Yes lt move on
    [2020-09-02 13:31:56] <ArticMine> let
    [2020-09-02 13:32:20] <sarang> Fair enough
    [2020-09-02 13:32:29] <sarang> Anyway, I recommend the interview to anyone interested in this
    [2020-09-02 13:32:39] <sarang> Any other questions on the research topics I mentioned?
    [2020-09-02 13:33:01] <sarang> If not, does anyone else wish to share research of interest?
    [2020-09-02 13:33:22] <sgp_> Is knaccc here?
    [2020-09-02 13:33:30] <sarang> Ah yes
    [2020-09-02 13:33:34] <knaccc> hi
    [2020-09-02 13:33:37] <knaccc> sorry been a busy day
    [2020-09-02 13:33:43] <sarang> knaccc: you had shared some interesting information yesterday
    [2020-09-02 13:33:45] <sgp_> They published some test results to review yesterday
    [2020-09-02 13:33:49] <sarang> Care to summarize if interested?
    [2020-09-02 13:34:08] <knaccc> i should take some time to think about it and do a writeup - my ability to summarize it now would be limited
    [2020-09-02 13:34:23] <sarang> OK, no problem
    [2020-09-02 13:34:29] <sarang> Can you at least set the scenario you are looking into?
    [2020-09-02 13:34:33] <knaccc> sure
    [2020-09-02 13:34:37] <sarang> Even if you aren't ready to share results
    [2020-09-02 13:34:38] <sarang> Thanks!
    [2020-09-02 13:34:59] <knaccc> so i have written a simple in-memory db that stores the blockchain graph
    [2020-09-02 13:35:17] <knaccc> and i can ask questions about the blockchain much faster than if i needed to do 2 million calls to the daemon
    [2020-09-02 13:35:24] <sarang> Pulls from RPC calls?
    [2020-09-02 13:35:30] <sarang> Or directly from LMDB?
    [2020-09-02 13:35:32] <knaccc> it loads everything in via rpc calls
    [2020-09-02 13:35:35] <sarang> got it
    [2020-09-02 13:35:46] <knaccc> but then it's all stored in memory and cached to disk so it doens't have to be re-read each time
    [2020-09-02 13:36:03] <knaccc> it's kinda like a very rudimentary LMDB, it's a memory mapped file
    [2020-09-02 13:36:13] <knaccc> with an index for ultra fast output lookups
    [2020-09-02 13:36:21] <sarang> What's the analysis scenario?
    [2020-09-02 13:37:02] <knaccc> well i write it so i could ask any kind of question i could think of. so if people have ideas, please let me know. i started with simply looking at the anonymity set sizes of outputs (going backwards in time)
    [2020-09-02 13:37:24] <knaccc> to get an idea of how fast the anonymity set really grows when overlapping anonymity sets are involved
    [2020-09-02 13:37:43] <knaccc> and to see whether the anonymity set size is limited when you limit the window during which you think someone may have tranascted
    [2020-09-02 13:37:57] <sarang> neat
    [2020-09-02 13:38:05] <sarang> I assume the code will also be made available?
    [2020-09-02 13:38:11] <knaccc> and the other big question was: what is the probability that two outputs, chosen at random from the blockchain, are ever merged
    [2020-09-02 13:38:15] <knaccc> fore sure
    [2020-09-02 13:38:17] <knaccc> fure*
    [2020-09-02 13:38:19] <knaccc> lol
    [2020-09-02 13:38:19] <sarang> Yeah, merging is something to keep in mind
    [2020-09-02 13:38:21] <knaccc> for*
    [2020-09-02 13:38:30] <sarang> One simple merge would deal with outputs generated from the same transactions
    [2020-09-02 13:38:35] <sarang> not randomly-selected pairs
    [2020-09-02 13:38:37] <knaccc> and so i can detect direct merges, and indirect merges if churn could have been involved
    [2020-09-02 13:39:05] <knaccc> yeah some really high-quality questions need to be thought of, for this to be useful
    [2020-09-02 13:39:23] <sarang> I would like to see information initially on merging from common transactions, personally
    [2020-09-02 13:39:47] <knaccc> great, i'm not sure exactly what you mean, but i'll ask you after the meeting and we'll figure it out
    [2020-09-02 13:39:51] <sarang> FWIW the CipherTrace "example" posted to r/Monero claimed to be from their tool (without details or explanation), and at first glance appeared to be some kind of merge analysis
    [2020-09-02 13:40:13] <knaccc> yeah that's a big problem that their analysis flagged
    [2020-09-02 13:40:17] <sarang> To be fair, Dave Jevans later claimed in a comment that it was not a "simple merge analysis" (or some such wording), but during the interview wasn't able to provide any comment on this
    [2020-09-02 13:40:45] <knaccc> if you give someone an output today, and another output a few days later, do you see them spend them together later? and if so, and if that spend is at an exchange, that's a big problem
    [2020-09-02 13:40:49] <sarang> Anyway, I am skeptical that it isn't just a merge analysis with external flagging, at least in that example
    [2020-09-02 13:40:55] <ArticMine> He needs that input correlations
    [2020-09-02 13:41:00] <sarang> Right
    [2020-09-02 13:41:08] <sarang> The correlations could come from known spends that flag outputs
    [2020-09-02 13:41:16] <knaccc> yeah the key to most interesting insights is having off-blockchain data
    [2020-09-02 13:41:16] <sarang> but one long-claimed heuristic is about the source of transactions
    [2020-09-02 13:41:28] <sarang> where you flag outputs as being "in pairs" if they were generated in the same transaction
    [2020-09-02 13:41:43] <sarang> it's a much simpler analysis, but one that's long been used to hypothesize a useful heuristic
    [2020-09-02 13:41:57] <sarang> Getting at least this simple example understood better with chain data would be of value
    [2020-09-02 13:42:23] <knaccc> sounds good
    [2020-09-02 13:42:26] <ArticMine> That requires adversary between the sender and receiver of the XNR
    [2020-09-02 13:42:38] <sarang> ArticMine: sure, but CipherTrace makes controlled spends
    [2020-09-02 13:42:43] <sarang> and is presumably working with exchanges
    [2020-09-02 13:42:50] <sarang> or getting exchange data from subpoenas
    [2020-09-02 13:43:03] <sarang> So one should assume this is a threat vector
    [2020-09-02 13:43:27] <ArticMine> Or more simply disgruntled customers
    [2020-09-02 13:43:55] <ArticMine> way easier
    [2020-09-02 13:43:58] <sarang> Anyway, this will be an interesting avenue of study
    [2020-09-02 13:44:05] <ArticMine> and no GDPR
    [2020-09-02 13:44:11] <sarang> I have also been working on scripting to do this analysis, but have not had a chance to complete it :(
    [2020-09-02 13:44:29] <sarang> Anything else of interest knaccc?
    [2020-09-02 13:44:38] <sarang> Or questions for knaccc?
    [2020-09-02 13:45:02] <knaccc> not that i can think of. i think it'll be an interative process, where we ask questions, see results, and that prompt more interesting and important questions to explore
    [2020-09-02 13:45:38] <sarang> for sure
    [2020-09-02 13:46:03] <sarang> Does anyone else wish to share any research topics?
    [2020-09-02 13:47:26] <sarang> OK!
    [2020-09-02 13:47:42] <sarang> In that case, let's move to action items, where anyone is welcome to share their upcoming topics of research for the next week(s)
    [2020-09-02 13:48:03] <sarang> I will be returning to work on Bulletproofs+, Arcturus, and some additional analysis I wish to complete on chain data
    [2020-09-02 13:48:05] <sarang> Anyone else?
    [2020-09-02 13:50:29] <sarang> Righto, in that case, we can adjourn!
    [2020-09-02 13:50:48] <sarang> Discussion can of course continue, but I'll stop the logs here to post them
    [2020-09-02 13:50:52] <sarang> Thanks to everyone for attending today


# Action History
- Created by: SarangNoether | 2020-08-26T17:53:02+00:00
- Closed at: 2020-09-02T18:12:22+00:00
