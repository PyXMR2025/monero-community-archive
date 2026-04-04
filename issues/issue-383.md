---
title: 'Research meeting: 20 August 2019 @ 17:00 UTC'
source_url: https://github.com/monero-project/meta/issues/383
author: SarangNoether
assignees: []
labels: []
created_at: '2019-08-19T14:36:43+00:00'
updated_at: '2019-08-20T17:43:09+00:00'
type: issue
status: closed
closed_at: '2019-08-20T17:43:09+00:00'
---

# Original Description
Join in for the weekly Monero Research Lab meeting.

**When**: Tuesday, 20 August 2019 @ 17:00 UTC
**Where**: #monero-research-lab (freenode/matrix)

**Agenda**
1. Greetings

2. Roundtable

3. General questions

4. Action items

# Discussion History
## SarangNoether | 2019-08-20T17:43:09+00:00
    [2019-08-20 13:00:10] <sarang> OK, let's get started with our meeting
    [2019-08-20 13:00:18] <sarang> Agenda here: https://github.com/monero-project/meta/issues/383
    [2019-08-20 13:00:23] <sarang> Logs posted there afterward
    [2019-08-20 13:00:28] <sarang> GREETINGS
    [2019-08-20 13:00:30] ⇐ ErCiccione quit (~erciccion@gateway/tor-sasl/erciccione): Quit: Bye
    [2019-08-20 13:00:32] <sarang> hello
    [2019-08-20 13:00:40] <suraeNoether> howdy
    [2019-08-20 13:01:21] <gingeropolous> heya
    [2019-08-20 13:01:23] <sarang> It's been two weeks since the last meeting... plenty to discuss!
    [2019-08-20 13:01:38] <sarang> In the spirit of fairness and teamwork, I'll go first :D
    [2019-08-20 13:02:05] <sarang> The DEF CON village, despite having a poor location, was well attended
    [2019-08-20 13:02:13] <sarang> I did a talk, a workshop, a CTF, and a panel discussion
    [2019-08-20 13:02:30] <suraeNoether> how did the attendance compare to last year?
    [2019-08-20 13:02:47] <sarang> I would estimate higher
    [2019-08-20 13:02:53] <suraeNoether> nice!
    [2019-08-20 13:03:16] <sarang> I've written up a brief spacetime analysis of Omniring in its current form: https://github.com/SarangNoether/skunkworks/blob/sublinear/omniring.md
    [2019-08-20 13:03:34] <sarang> It does not presently support batching, but the authors have a couple of ideas on how to do so safely that are forthcoming
    [2019-08-20 13:03:42] <sarang> I'll be discussing with them this week
    [2019-08-20 13:04:00] <sarang> On a related note, the RCT3 construction has a flaw that would be exploitable in practice
    [2019-08-20 13:04:16] <sarang> The authors of that paper, I'm told, also have a fix forthcoming that may relate to the Omniring batching enhancement
    [2019-08-20 13:04:49] <sarang> Made a quick PR to fix a bias in Schnorr signatures: https://github.com/monero-project/monero/pull/5807
    [2019-08-20 13:05:00] <endogenic> o/
    [2019-08-20 13:05:10] <sarang> Cleaned up an MLSAG improvement PR: https://github.com/monero-project/monero/pull/5707
    [2019-08-20 13:05:28] <sarang> Made some updates to Zero to Monero (see topic branches): https://github.com/SarangNoether/zero-to-monero/
    [2019-08-20 13:05:48] <sarang> And I'm working on getting CLSAG and thring sigs submitted to conference proceedings (a tiresome and lengthy process)
    [2019-08-20 13:05:56] <sarang> That's my two cents
    [2019-08-20 13:06:00] <endogenic> damn, son
    [2019-08-20 13:06:02] — sarang passes the baton
    [2019-08-20 13:06:08] <suraeNoether> yeah, that was a damn mic drop brother
    [2019-08-20 13:06:41] <sarang> Anything to share with the class, suraeNoether ?
    [2019-08-20 13:06:56] <suraeNoether> as for me, I've been on vacation and just got back. I'm still going to be only half-on today because I have some personal business I have to attend. it was an eventful vacation. for one thing, I was able to prove a few theorems for my graph matching paper that are necessary for publication. based on a conversation I had with sgp_ right before I left, I spent a lot of time thinking about experimental
    [2019-08-20 13:06:57] <suraeNoether> design, and I'm starting to discuss this with sarang.
    [2019-08-20 13:07:38] <suraeNoether> in addition to that, I was contacted by Astral, the team working on bullet-proof monero-mining drones, re: an unfortunately urgent funding matter.
    [2019-08-20 13:08:21] <luigi1111w> sarang what happened to reusing existing functions or adding it as a function instead of inline?
    [2019-08-20 13:08:28] <luigi1111w> not that it matters that much I guess
    [2019-08-20 13:09:00] <sarang> There were some silly issues with includes and having access to the right underlying functions
    [2019-08-20 13:09:11] <sarang> It seemed simpler to do it as is
    [2019-08-20 13:09:32] <suraeNoether> i would urge folks in the audience to watch OhGodAGirl__'s talk from teh Konferenco here (https://www.youtube.com/watch?v=jDSKIr5EPiU ) or Leah's interview wiht monerotalk https://www.youtube.com/watch?v=jl1w6VDEWq4 to refresh themselves on the project
    [2019-08-20 13:10:02] <endogenic> meaning they need funding?
    [2019-08-20 13:10:07] <suraeNoether> if anyone is interested in assisting Astral in composing a CCS, I've been pinging some ideas back and forth with Leah
    [2019-08-20 13:10:46] <suraeNoether> yes, and some of the funding needs are rather urgent; I spoke with OhGodAGirl__ and OpenSourceress about this in person at the Konferenco and we have been kicking some ideas around
    [2019-08-20 13:11:30] <suraeNoether> i anticipate a vigorous discussion on the matter, because the community funding sources, in my mind, should be a source of funding of last resort
    [2019-08-20 13:11:50] <suraeNoether> the folks who contribute to the monero community are people who care about privacy and they want to see the project advance in a healthy direction, and without them, all of this falls apart
    [2019-08-20 13:12:08] <sarang> Probably a good discussion for -community?
    [2019-08-20 13:12:17] <sarang> Unless there's a technical/research component to it?
    [2019-08-20 13:13:48] <suraeNoether> well, it's a nascent funding request for a hardware project with a timeliness component that recently presented at our conference, but going into further detail during the meeting is certainly unnecessary
    [2019-08-20 13:14:02] <sarang> got it
    [2019-08-20 13:14:20] <suraeNoether> and full disclosure: i am not yet in any way financially linked with Astral, although that may eventually change
    [2019-08-20 13:14:28] <suraeNoether> i.e. this isn't for me
    [2019-08-20 13:14:35] <sarang> Anyone else wish to share research work of interest?
    [2019-08-20 13:14:51] <sarang> I'm excited to take a look at the current state of the matching simulations suraeNoether 
    [2019-08-20 13:15:00] <suraeNoether> that's all I have for the round table this week, but I'll also be playing catch-up on the lelantus vs. omni vs. rct3 cage match that's been going on these past few weeks
    [2019-08-20 13:15:30] <gingeropolous> may eventually change? hamster.gif
    [2019-08-20 13:17:14] <sarang> OK, so after the brief ROUNDTABLE is GENERAL QUESTIONS... anyone?
    [2019-08-20 13:18:25] <sarang> I have a general question
    [2019-08-20 13:18:57] <suraeNoether> i have one, too
    [2019-08-20 13:19:07] <sarang> The proceedings/journals under consideration for CLSAG (thanks also to some outside advice) are Financial Cryptography, PETS, ACM TOPS, and ANCS
    [2019-08-20 13:19:17] <sarang> Any other suggestions that I may have missed, that could be in scope?
    [2019-08-20 13:19:33] <sarang> It's tough in the CLSAG case since it's an improvement over earlier work, but not earth-shattering
    [2019-08-20 13:19:42] <sarang> and that always seems to be a tricky place to be in the publishing world
    [2019-08-20 13:20:01] <sarang> I plan to highlight the improvements and generalize it a bit for submission
    [2019-08-20 13:20:08] <suraeNoether> are you strictly considering conference proceedings or are you open to journal-only suggestions?
    [2019-08-20 13:20:30] <sarang> Journals are fine too (ACM TOPS, e.g.)
    [2019-08-20 13:21:42] <sarang> But since submissions are typically one-at-a-time, there's no real rush to add to the list
    [2019-08-20 13:21:57] <sarang> But obviously prioritizing is useful to avoid submitting for delayed rejections
    [2019-08-20 13:23:02] <suraeNoether> fair enough. I thought ACM TOPS was a conference, silly me. :P
    [2019-08-20 13:23:08] <sarang> Anyway, that's my question
    [2019-08-20 13:23:10] <sarang> suraeNoether: yours?
    [2019-08-20 13:24:54] <suraeNoether> some of the biggest improvements that have come out of MRL this year have involved efficiency improvements, ranging from bulletproofs optimizations to compressed signature schemes. Only some of these improvements will carry on to the "next version" of monero, especially if we end up having to migrate our transaction model to something like one of the Big Three...
    [2019-08-20 13:25:03] <dEBRUYNE> suraeNoether: Don't they have other options than to tend to the CSS?
    [2019-08-20 13:25:10] <dEBRUYNE> I genuinely think this is not appropriate for it
    [2019-08-20 13:25:43] <suraeNoether> so my question is: what sort of improvements would you like to see from the Monero Research Lab in the next year, keeping in mind that we will want to migrate to a different scheme sooner or later?
    [2019-08-20 13:26:18] <suraeNoether> dEBRUYNE: i'll start a conversation about this over in -community
    [2019-08-20 13:26:31] ⇐ WoomyZoomy quit (~Android@2607:fb90:782:84f4:eb2a:aef4:5cdb:83cb): Ping timeout: 250 seconds
    [2019-08-20 13:27:09] <rehrar> I would definitely like some research into ring sig alternatives.
    [2019-08-20 13:27:38] <sarang> That's very much in progress rehrar 
    [2019-08-20 13:28:01] <suraeNoether> do you mean ring confidential transactions?
    [2019-08-20 13:28:09] <rehrar> from the ground plebs, we're never quite sure how much progress and when and why and stuff
    [2019-08-20 13:28:20] <suraeNoether> because lelantus, omni, and rct3 are each replacements for ring sigs
    [2019-08-20 13:28:23] <suraeNoether> in a certain sense
    [2019-08-20 13:28:30] <suraeNoether> but they are still ring confidential transaction schemes
    [2019-08-20 13:28:33] <sarang> Yeah, my analyses try to give a reasonable spacetime estimate for those protocols
    [2019-08-20 13:28:34] <rehrar> I wonder if a bimonthly MRL bulletin would be helpful to the masses
    [2019-08-20 13:28:37] <rehrar> or a monthly one
    [2019-08-20 13:28:45] <rehrar> I can assist in getting it out
    [2019-08-20 13:28:48] <dEBRUYNE> suraeNoether: OK
    [2019-08-20 13:29:58] <sarang> Any other general questions?
    [2019-08-20 13:32:52] <suraeNoether> sarang, do you have an answer to my question?
    [2019-08-20 13:33:00] <suraeNoether> rehrar answered and this was something i was happy to see
    [2019-08-20 13:33:07] <suraeNoether> usually it's the noethers talking at everyone else during these meetings :D
    [2019-08-20 13:33:09] <suraeNoether> but i am curious
    [2019-08-20 13:33:54] <sarang> I think determining the real viability of newer transaction protocols is a priority for my research
    [2019-08-20 13:35:27] <suraeNoether> okay. my personal white whale has always been to replace linearly-sized RCT with something sublinear but sufficiently fast to not drag down the network, so i'm happy to have such an embarassment of schemes to work through
    [2019-08-20 13:36:47] <suraeNoether> anywya, no other questions from me
    [2019-08-20 13:36:49] <sarang> Yeah, once the RCT3 fix and Omniring batch issues are solved, there will be a much clearer view of what's reasonable IMO
    [2019-08-20 13:36:55] <sarang> Anyway, on to ACTION ITEMS
    [2019-08-20 13:37:23] <sarang> I'll be discussing protocol details with some other researchers this week, to gain some better information on these changes
    [2019-08-20 13:37:38] <sarang> Getting the preprints sorted out for edits and submission
    [2019-08-20 13:37:45] <dEBRUYNE> If any of you feels like leaving a brief comment here btw -> https://www.reddit.com/r/Monero/comments/ct29nx/spectre_protocol_update/
    [2019-08-20 13:37:49] <sarang> and catching up on a backlog of other preprints that have come out
    [2019-08-20 13:37:55] <sarang> suraeNoether: ?
    [2019-08-20 13:38:34] <suraeNoether> working with you on matching code and experimental design, and backlog reading on the work Sarang has done over the past 2 months comparing these three sublinear protocols
    [2019-08-20 13:39:08] <sarang> neat
    [2019-08-20 13:39:20] <sarang> OK, any final questions or comments before adjourning?
    [2019-08-20 13:39:51] → WoomyZoomy joined (~Android@2607:fb90:782:84f4:eb2a:aef4:5cdb:83cb)
    [2019-08-20 13:40:04] <sarang> going once
    [2019-08-20 13:40:44] → TheoStorm joined (~TheoStorm@host-phyadb.cbn1.zeelandnet.nl)
    [2019-08-20 13:40:57] <sarang> going twice
    [2019-08-20 13:41:06] <sarang> Adjourned! Logs will be posted shortly


# Action History
- Created by: SarangNoether | 2019-08-19T14:36:43+00:00
- Closed at: 2019-08-20T17:43:09+00:00
