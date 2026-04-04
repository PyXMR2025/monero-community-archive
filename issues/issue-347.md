---
title: 'Research meeting: 27 May 2019 @ 17:00 UTC'
source_url: https://github.com/monero-project/meta/issues/347
author: SarangNoether
assignees: []
labels: []
created_at: '2019-05-23T18:17:57+00:00'
updated_at: '2019-05-27T18:27:00+00:00'
type: issue
status: closed
closed_at: '2019-05-27T18:27:00+00:00'
---

# Original Description
Join in for the weekly Monero Research Lab meeting.

**When**: Monday, 27 May 2019 @ 17:00 UTC
**Where**: #monero-research-lab (freenode/matrix)

**Agenda**
1. Greetings

2. Roundtable

3. General questions

4. Action items

# Discussion History
## SarangNoether | 2019-05-27T18:27:00+00:00
    [2019-05-27 12:00:12] <suraeNoether> Good morning everyone, and welcome to our weekly research meeting, bringing May to a close. It's been a busy month. Let's begin with agenda item 1: GREETINGS.
    [2019-05-27 12:00:16] — suraeNoether waves
    [2019-05-27 12:00:21] → Dean_Guss joined (~dean@gateway/tor-sasl/deanguss)
    [2019-05-27 12:00:37] <nioc> peanut here
    [2019-05-27 12:01:10] <suraeNoether> welcome, peanut gallery :P
    [2019-05-27 12:01:42] <suraeNoether> Allrighty, since Sarang isn't joining us, this is just good ole surae today
    [2019-05-27 12:02:03] <suraeNoether> luckily, I have a thing for you guys to read: CLSAG draft! https://github.com/b-g-goodell/research-lab/tree/master/publications/bulletins/MRL-0012-CLSAG
    [2019-05-27 12:02:38] <suraeNoether> pretty close to 25% reduction in rate of growth of Monero's blockchain size, with around 15-25% speedup in verification times
    [2019-05-27 12:03:10] <suraeNoether> plus more reckless projects can do colored ring confidential transactions. we are calling them MARCTs - multi-asset ringCT
    [2019-05-27 12:03:57] <suraeNoether> we are missing one proof in the appendix that is in preparation, and we have an open question about a further reduction in signature size that may be possible
    [2019-05-27 12:05:29] <suraeNoether> I've also been working on DLSAG. With CLSAG's colored transactions and DLSAG's return functionality plus thring signatures for threshold signing, we have most of the building blocks for off-chain scaling solutions at Monero like lightning network
    [2019-05-27 12:05:59] <suraeNoether> i believe our co-authors are eager to publish the DLSAG paper this week
    [2019-05-27 12:06:05] <suraeNoether> this has been a busy month
    [2019-05-27 12:06:19] <nioc> how do CLSAG and DLSAG play together?
    [2019-05-27 12:06:22] → el00ruobuob_[m] joined (~el00ruobu@2a01:e35:2e61:e390:8c66:f5c6:356c:d198)
    [2019-05-27 12:06:28] <moneromooo> Once that paper is out, will you expand on the remainder (wrt "most") ?
    [2019-05-27 12:06:53] <suraeNoether> short answer: they do not yet. DLSAG has a weird key image structure that is causing problems, but we are going ahead and publishing anyway because we haven't been able to resolve the problem, but the foundational work for DLSAG should still be put out there
    [2019-05-27 12:07:22] <needmoney90> suraeNoether: the mods were literally discussing pinning a megathread on the konferenco an hour ago
    [2019-05-27 12:07:22] <suraeNoether> moneromooo: i believe that hash time locked contracts are the final piece of the puzzle, and one of our DLSAG co-authors is working with pedro moreno sanchez at TU wien publishing a paper on that very topic
    [2019-05-27 12:07:31] <needmoney90> I just pinned yours, thanks for being proactive
    [2019-05-27 12:07:51] <suraeNoether> needmoney90: dEBRUYNE asked me to post it, that sort of thing escapes my mind a lot so I need pushes from folks. :P I appreciate it
    [2019-05-27 12:07:54] <needmoney90> Aha
    [2019-05-27 12:07:57] <needmoney90> Makes sense
    [2019-05-27 12:08:01] — needmoney90 give his greetings 
    [2019-05-27 12:08:05] <suraeNoether> greetings
    [2019-05-27 12:09:15] <suraeNoether> any more questions for me on DLSAG or CLSAG?
    [2019-05-27 12:11:47] <suraeNoether> okay, now that's out of the way, since last week Spartan and RingCT3.0 and Lelantus are all floating around as ring signature replacements, and these interest me greatly. sarang and i are studying these with the intent of doing a plausibility analysis for them. in the meantime, mrl11, which is the traceability/matching paper is moving forward, a few bugs at a time
    [2019-05-27 12:12:13] <suraeNoether> it's slow-going, and since the idea of a trustless snark would basically make the paper moot, the priority for the matching paper is sort of a toss-up
    [2019-05-27 12:13:29] <suraeNoether> now that I've brought everyone up to date on DLSAG, CLSAG, and my other work on mrl11 and ring signature replacement: does anyone else have any research they would like to present, or topics they want to bring up?
    [2019-05-27 12:13:33] <suraeNoether> general questions or concerns or comments?
    [2019-05-27 12:14:17] <moneromooo> If considering spartan, it's from a MS employee. Given MS has a rich history of maliciously fucking people over, it should be done very carefully.
    [2019-05-27 12:14:37] <suraeNoether> ^ 100% with you
    [2019-05-27 12:14:56] <moneromooo> They do employ a lot of clever people who may not be under the borg thing though, who who knows.
    [2019-05-27 12:16:44] <moneromooo> How far off is that secondary space win for CLSAG (considering the october or around fork) ?
    [2019-05-27 12:17:47] <suraeNoether> moneromooo: I need to talk with sarang and randomrun about it, but i have a high degree of confidence in an approve/disapprove well before october
    [2019-05-27 12:18:01] <suraeNoether> two video calls and we'll have it sorted
    [2019-05-27 12:19:25] <dEBRUYNE> I think we also have to factor in audit time, because, as far as I know, the community would like to see it audited before being implemented
    [2019-05-27 12:19:51] <suraeNoether> we can prioritize for end-of-week on that.
    [2019-05-27 12:20:04] <needmoney90> Pff, just implement it before the audits finish
    [2019-05-27 12:20:08] <needmoney90> What's the worst that can happen
    [2019-05-27 12:20:33] <suraeNoether> So, I'm going to go ahead and cancel the research meeting we have planned for the Monday following the Konferenco weekend, June 24th.
    [2019-05-27 12:20:41] <needmoney90> That makes sense.
    [2019-05-27 12:20:55] <suraeNoether> needmoney90: i wonder if wownero will have a rainbow of colored coins before fourth of july
    [2019-05-27 12:21:29] <suraeNoether> At least for the week leading up to the Konferenco, I don't anticipate any research progress on my front, as I prepare for the event
    [2019-05-27 12:22:10] <suraeNoether> in between now and then my action items for reserach involve working on mrl11 simulation code while compiling info about spartan, ringct3, lelantus, and comparing against CLSAG for a comparative report.
    [2019-05-27 12:22:47] <suraeNoether> unlike my previous papers, I think I want to use github more extensively for this comparative report, and upload updates to a document as I go so folks can sort of follow along with the development of the document
    [2019-05-27 12:23:19] <suraeNoether> does anyone have any requested action items from me, or does anyone have any further questions about research, or the konferenco, or does anyone want to speak up about research they've done recently to contribute to Monero?
    [2019-05-27 12:25:47] <suraeNoether> okay, i want to give a special shoutout to all the folks on the XMR outreach team who've been helping me with Konferenco promotion. Otherwise.. yeesh, it's sad here without sarang
    [2019-05-27 12:26:19] <suraeNoether> let's adjourn this meeting; see you guys here again on 3 June for our next research meeting!
    [2019-05-27 12:27:04] * suraeNoether set the topic to Monero Konferenco schedule: https://monerokon.com/schedule

# Action History
- Created by: SarangNoether | 2019-05-23T18:17:57+00:00
- Closed at: 2019-05-27T18:27:00+00:00
