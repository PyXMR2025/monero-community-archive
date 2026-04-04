---
title: 'Research meeting: 26 August 2020 @ 17:00 UTC'
source_url: https://github.com/monero-project/meta/issues/501
author: SarangNoether
assignees: []
labels: []
created_at: '2020-08-19T18:01:01+00:00'
updated_at: '2020-08-26T17:52:10+00:00'
type: issue
status: closed
closed_at: '2020-08-26T17:52:10+00:00'
---

# Original Description
Join in for the weekly Monero Research Lab meeting.

**When**: Wednesday, 26 August 2020 @ 17:00 UTC
**Where**: #monero-research-lab (freenode/matrix)

**Agenda**
1. Greetings

2. Roundtable

3. Questions

4. Action items

# Discussion History
## Mitchellpkt | 2020-08-26T17:01:56+00:00
## PQ-XMR research

Our audit is coming along nicely, have been focused on the technical writeup. 

We looped in Surae as a reviewer for the audit results and writeup - he’s been super helpful with nailing down a few of the trickier details, and cleanly communicating some of the more complicated concepts.

We have a meeting coming up where we'll merge drafts and freeze some of the sections (algorithms, key generation, subaddresses, stealth addresses) into "draft 1" for y'all to review. I'll just post in -lab on IRC

## Stats research
Still working on the empirical/statistical analysis of [transaction field uniformity](https://github.com/Mitchellpkt/crypto_field_stats_tests), and I've been looking into the [Diehard tests](https://en.wikipedia.org/wiki/Diehard_tests) as a starting point for battery of statistical tests. 

(Note that they're designed to test RNG quality, which is a subtly different problem, but related enough that some of the tests (e.g. birthday spacing) should be applicable for both.)

The tricky thing is that many of these are designed to test uniformity of bitstrings, however that's not applicable here. Consider uniformly sampled integers on [0, 555]... Even if the sampling is correctly uniform, we do not expect uniformity in the binary representation (first bit more often 1 than 0) nor in a digit representation (see 5 more often than 8). So I'm having a little bit of trouble figuring out how to adapt them (or if that's even possible)



## SarangNoether | 2020-08-26T17:52:10+00:00
    [2020-08-26 12:59:35] <sarang> OK, let's get started with the weekly research meeting!
    [2020-08-26 12:59:55] <sarang> The usual agenda: https://github.com/monero-project/meta/issues/501
    [2020-08-26 13:00:01] <sarang> Logs will be posted there after the meeting
    [2020-08-26 13:00:05] <sarang> First, greetings!
    [2020-08-26 13:00:09] <sgp_> hello :)
    [2020-08-26 13:00:20] <h4sh3d[m]> hi
    [2020-08-26 13:02:07] — Isthmus puts on lab coat and goggles
    [2020-08-26 13:03:27] → asymptotically joined (~asymptoti@gateway/tor-sasl/asymptotically)
    [2020-08-26 13:03:46] <sarang> Let's move to roundtable, where anyone is welcome to share research of interest
    [2020-08-26 13:03:59] <sarang> Isthmus: you posted to the agenda just now; care to share?
    [2020-08-26 13:04:07] <Isthmus> Sure
    [2020-08-26 13:04:15] <sarang> https://github.com/monero-project/meta/issues/501#issuecomment-681005468
    [2020-08-26 13:04:31] <Isthmus> Our audit is coming along nicely, have been focused on the technical writeup.
    [2020-08-26 13:04:31] <Isthmus> Looped in Surae as a reviewer for the audit results and writeup - he’s been super helpful with nailing down a few of the trickier details, and cleanly communicating some of the more complicated concepts.
    [2020-08-26 13:04:31] <Isthmus> We have a meeting coming up where we'll merge drafts and freeze some of the sections (algorithms, key generation, subaddresses, stealth addresses) into "draft 1" for y'all to review. I'll just post in -lab on IRC
    [2020-08-26 13:04:45] <sarang> Great!
    [2020-08-26 13:05:01] <Isthmus> Also, still working on the empirical/statistical analysis of transaction field uniformity, and I've been looking into the Diehard tests as a starting point for battery of statistical tests.
    [2020-08-26 13:05:01] <Isthmus> (Note that they're designed to test RNG quality, which is a subtly different problem, but related enough that some of the tests (e.g. birthday spacing) should be applicable for both.)
    [2020-08-26 13:05:01] <Isthmus> The tricky thing is that many of these are designed to test uniformity of bitstrings, however that's not applicable here. Consider uniformly sampled integers on [0, 555]... Even if the sampling is correctly uniform, we do not expect uniformity in the binary representation (first bit more often 1 than 0) nor in a digit representation (see 5 more often than 8). So I'm having a little bit of trouble figuring
    [2020-08-26 13:05:01] <Isthmus> out how to adapt them (or if that's even possible)
    [2020-08-26 13:05:13] <Isthmus> ( context here: https://github.com/Mitchellpkt/crypto_field_stats_tests )
    [2020-08-26 13:05:26] <sarang> Hmm, interesting
    [2020-08-26 13:06:01] <sarang> It's interesting to think about what the best action would be in the event of observed non-uniformity 
    [2020-08-26 13:06:39] <Isthmus> I'd say it depends on the nature of the non-uniformity (bias or collisions?) and the implications of non-uniformity in that particular field
    [2020-08-26 13:07:25] <Isthmus> I don't think there's a single one-size-fits-all recommendation or level of severity
    [2020-08-26 13:07:55] <sarang> Very interesting analysis
    [2020-08-26 13:09:04] <sarang> Is there anything in particular relating to the post-quantum analysis for which you'd like assistance from this group?
    [2020-08-26 13:09:22] <Isthmus> Review of the first draft, probably later this week
    [2020-08-26 13:09:30] <Isthmus> Any/all feedback :- )
    [2020-08-26 13:09:57] <sarang> Sounds good!
    [2020-08-26 13:10:03] <sarang> Anything else you'd like to share?
    [2020-08-26 13:10:07] <sarang> Or, any questions for Isthmus?
    [2020-08-26 13:10:18] <MRL-discord> <Mitchell PKT> BTW if y'all are having IRCcloud issues, you're welcome to use the Noncesense bridge at discord.noncesense.org
    [2020-08-26 13:11:13] <Isthmus> Nothing else from me for the moment
    [2020-08-26 13:11:20] <sarang> OK, thanks Isthmus
    [2020-08-26 13:11:21] <h4sh3d[m]> What would be the dataset for those tests?
    [2020-08-26 13:11:32] <sarang> Oh, is IRCCloud having problems? Seems to work fine for me, FWIW
    [2020-08-26 13:11:57] <Isthmus> I didn't have any issues, but saw people talking about it in scrollback from yesterday
    [2020-08-26 13:12:13] <Isthmus> Well, actually, I guess I don't know if I had issues, because I wasn't on IRC
    [2020-08-26 13:12:36] <sarang> I have a few research items to share
    [2020-08-26 13:13:14] <sarang> My proof-of-concept code for Bulletproofs+ now supports single-round verification and efficient batching: https://github.com/SarangNoether/skunkworks/tree/pybullet-plus
    [2020-08-26 13:13:45] <sarang> I'm in the process of modifying the existing Bulletproofs C++ code to get concrete performance data
    [2020-08-26 13:14:23] <sarang> Usual disclaimer that this proof-of-concept code is written for research, and not with practical security in mind... do not use in production for any reason
    [2020-08-26 13:15:42] <sarang> I'm happy to announce that Triptych has been accepted for presentation and publication at ESORICS CBT 2020
    [2020-08-26 13:15:58] <Isthmus> :- D
    [2020-08-26 13:15:59] <sarang> I have a blog post PR for `monero-site` announcing this
    [2020-08-26 13:16:00] <ArticMine> That is excellent
    [2020-08-26 13:16:19] <sarang> I'll make the presentation next month remotely
    [2020-08-26 13:16:26] <sarang> and the paper will appear in the conference proceedings
    [2020-08-26 13:16:49] <sarang> Here is a draft of the presentation: https://www.overleaf.com/read/rscsccvdsrvj
    [2020-08-26 13:16:53] <sarang> Comments and suggestions are welcome
    [2020-08-26 13:17:17] <sarang> I intentionally don't go into the weeds on the math of the proving system, since I think that is less helpful than explaining why it can be used to build a confidential transaction protocol
    [2020-08-26 13:17:51] <sarang> I discovered some notation problems in the preprint while preparing the presentation, but they are minor and don't affect any of the results or conclusions
    [2020-08-26 13:18:31] <sarang> Are there any questions on these topics?
    [2020-08-26 13:19:12] <suraeNoether> Not from moi
    [2020-08-26 13:19:14] <sarang> Please do review the presentation if possible; my goal is clarity, and I welcome any suggestions
    [2020-08-26 13:19:45] <sarang> If anyone has trouble getting the PDF loaded in Overleaf, please let me know and I'll be happy to assist
    [2020-08-26 13:20:02] <sarang> Does anyone else have research topics to share?
    [2020-08-26 13:20:06] <h4sh3d[m]> I read the version earlier today and it was very clear an well explained
    [2020-08-26 13:20:18] <sarang> Thanks h4sh3d[m]!
    [2020-08-26 13:20:25] <sarang> I've recently added some additional slides
    [2020-08-26 13:20:34] <h4sh3d[m]> I'll have a look at the new slides, but again looks very clear
    [2020-08-26 13:20:48] <sarang> I am looking for a better way to visually explain the structure of the overall transaction protocol, which I find very tricky to dor
    [2020-08-26 13:20:54] <sarang> s/dor/do
    [2020-08-26 13:20:54] <monerobux> sarang meant to say: I am looking for a better way to visually explain the structure of the overall transaction protocol, which I find very tricky to do
    [2020-08-26 13:20:57] <sarang> good bot
    [2020-08-26 13:21:58] <Isthmus> Could we get u/Krakataua314 make an infographic?
    [2020-08-26 13:21:58] <Isthmus> https://www.reddit.com/r/Monero/comments/gy0m1u/i_made_an_infographic_on_how_a_monero_wallet_is/
    [2020-08-26 13:21:59] <monerobux> [REDDIT] I made an infographic on how a Monero wallet is generated. Can you find any mistakes? (https://i.redd.it/tv98m10mbd351.png) to r/Monero | 171 points (100.0%) | 28 comments | Posted by Krakataua314 | Created at 2020-06-06 - 22:42:54
    [2020-08-26 13:22:16] <Isthmus> "visually explain the structure of the overall transaction protocol" < this would be very useful for the quantum research too
    [2020-08-26 13:22:37] <Isthmus> Since being able to draw backwards red arrows labeled "X algo" is imho the most intuitive way to quickly see the results
    [2020-08-26 13:23:15] → v1docq47[m] joined (~v1docq47m@89.113.139.75)
    [2020-08-26 13:23:31] <sarang> I really wish that I could have submitted Arcturus for the workshop as well
    [2020-08-26 13:23:41] <sarang> Unfortunately, it was still under consideration elsewhere :(
    [2020-08-26 13:23:49] <sarang> Oh well
    [2020-08-26 13:23:57] <sarang> More time to think about its cryptographic hardness assumption
    [2020-08-26 13:24:24] <sarang> Anyway, those are the topics I wished to discuss
    [2020-08-26 13:24:35] <sarang> Anyone else?
    [2020-08-26 13:27:25] <suraeNoether> Uh, I've been helping Isthmus with the PQ paper
    [2020-08-26 13:27:33] <sarang> Great!
    [2020-08-26 13:27:40] <suraeNoether> also tomorrow Monero is gaining an undergraduate intern from Clemson University
    [2020-08-26 13:27:41] <sarang> I'm eager to see the results
    [2020-08-26 13:28:11] <sarang> Are there projects in mind for this person?
    [2020-08-26 13:28:12] <suraeNoether> sarang, myself, isthmus, and TheCharlatan have a call scheduled where we will each explain a few possible projects for this student to work on, and they will select which one they want to work on for two subsequent semesters
    [2020-08-26 13:28:39] <sarang> I had a few things in mind, but wondered if there were others under consideration
    [2020-08-26 13:28:41] <suraeNoether> each of us has a different set of ideas/flavors, but the student's experience is limited (understandably) so we are going to try to come up with something complete-able
    [2020-08-26 13:29:05] <suraeNoether> i'm *guessing* that the student will be most interested in doing data science with isthmus looking at anonymity and linkability, but that's a wild guess
    [2020-08-26 13:29:31] <sarang> The things that I was considering had to do with chain toolsets and perhaps some security model stuff, depending on experience and interest
    [2020-08-26 13:29:50] <ArticMine> What is the student's background?
    [2020-08-26 13:31:46] <sarang> I have an email in my archive with this information ArticMine, but I need to dig it up
    [2020-08-26 13:31:52] <sarang> suraeNoether: ?
    [2020-08-26 13:32:28] <ArticMine> It can help in finding ideas for a suitable project
    [2020-08-26 13:32:41] <suraeNoether> Sorry. My internet just died.
    [2020-08-26 13:33:08] <sarang> Anyway, we can pull up the student's experience information after the meeting if needed
    [2020-08-26 13:33:34] <suraeNoether> ArticMine the student is a math/cs student, but we can't share much more. But we should chat.
    [2020-08-26 13:33:59] <ArticMine> We have to respect privacy here
    [2020-08-26 13:34:23] <suraeNoether> Especially if you have ideas for compactish projects. I was frankly hoping the student could just finish all the TODOs leftover in the original cryptonote code with TheCharlatan lol
    [2020-08-26 13:34:53] <suraeNoether> Anyway let's chat after the meeting
    [2020-08-26 13:35:07] <sarang> OK, we can move to action items, where anyone is welcome to share their research plans for the next weeks
    [2020-08-26 13:35:38] <sarang> I have some work to finish on the Triptych presentation and paper for the workshop, and will continue with BP+ testing
    [2020-08-26 13:35:42] <sarang> Others?
    [2020-08-26 13:36:44] <h4sh3d[m]> I want to look more in depth, from a chain analysis point of view, if you know that two transactions will occurs in a time-laps of around half an hour and one consume the output of the previous one, how much you can trace this
    [2020-08-26 13:37:09] <h4sh3d[m]> I think it's related to the decoy choices right?
    [2020-08-26 13:37:20] <sarang> and transaction volume
    [2020-08-26 13:37:24] — Isthmus digs around for writeup
    [2020-08-26 13:37:29] <h4sh3d[m]> And other factor such as tx volume sure
    [2020-08-26 13:37:41] <sarang> Do you have a threat model in mind?
    [2020-08-26 13:37:50] → lxeiqr joined (~lxeiqr@188.146.233.22.nat.umts.dynamic.t-mobile.pl)
    [2020-08-26 13:38:14] <h4sh3d[m]> Not really, just wondering
    [2020-08-26 13:38:30] <Isthmus> There's a little algorithmic trick I came up with, starting with a given output, you make 11 hypotheses (mutually exclusive) that there is a repeaated chain with period of (output_time - input_time)
    [2020-08-26 13:38:44] <Isthmus> Then you can work backwards, eliminating most or all of the hypotheses at each step
    [2020-08-26 13:39:09] <Isthmus> And it'll quickly surface any chains with periodicity (within some multiplicative or additive tolerance)
    [2020-08-26 13:39:36] <Isthmus> Before I was trying to do power spectrum analysis, which was wayyyy overkill
    [2020-08-26 13:39:59] <Isthmus> If you know the period, it's even easier
    [2020-08-26 13:40:29] <sarang> Nice
    [2020-08-26 13:40:34] <Isthmus> If there's only two transactions though, this will be very noisy
    [2020-08-26 13:40:47] <h4sh3d[m]> But this would work if the period is repeated more than once?
    [2020-08-26 13:40:48] <Isthmus> SNR depends on length of chain (and period relative to decoy selection algorithm)
    [2020-08-26 13:41:19] <Isthmus> "period is repeated more than once?" do you mean in a chain, or from the same wallet?
    [2020-08-26 13:41:34] ⇐ v1docq47[m] quit (~v1docq47m@89.113.139.75): Ping timeout: 256 seconds
    [2020-08-26 13:41:59] <h4sh3d[m]> in a chain
    [2020-08-26 13:42:07] <ArticMine> but if you increase the number of related transactions then the signal to noise will improve
    [2020-08-26 13:42:12] <Isthmus> Then yea, the more it's repeated, the more certainly it sticks out
    [2020-08-26 13:42:38] <Isthmus> How do you increase the number of related transactions?
    [2020-08-26 13:43:26] <ArticMine> The pattern is repeated
    [2020-08-26 13:43:38] <ArticMine> and there is a correlation between the repeated patterns
    [2020-08-26 13:45:23] <Isthmus> Ohh artic I misread your previous message. Yes, exactly right
    [2020-08-26 13:47:19] <sarang> Before we close out the meeting (discussions are of course welcome to continue after), anything else that should be discussed?
    [2020-08-26 13:49:33] <sarang> OK, in that case, let us adjourn! Thanks to everyone for attending


# Action History
- Created by: SarangNoether | 2020-08-19T18:01:01+00:00
- Closed at: 2020-08-26T17:52:10+00:00
