---
title: 'Community Workgroup Meeting: Sunday 2nd January 2022 16:00 UTC'
source_url: https://github.com/monero-project/meta/issues/644
author: carrington1859
assignees: []
labels: []
created_at: '2022-01-01T11:59:41+00:00'
updated_at: '2022-01-04T00:54:33+00:00'
type: issue
status: closed
closed_at: '2022-01-04T00:54:33+00:00'
---

# Original Description
Location: [Libera.chat, #monero-community](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-community:monero.social?via=matrix.org&via=monero.social)

[Instructions for joining the monero.social Matrix server.](https://forum.monero.space/d/79-how-to-join-the-monero-core-team-matrix-server-web)

Time
16:00 UTC [Check your timezone](https://www.timeanddate.com/worldclock/converter.html?iso=20220102T160000&p1=1440)

Moderator: Carrington

Proposed Meeting Items:

Please reach out in advance of the meeting if you would like to propose an agenda item.

1) Introduction
2) Greetings
3) Community highlights
4) CCS updates
a. [Pluja's educational content for Monero plus kycnot and iseeyourcash maintenance](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/273)
b. [MoneroKon 2022](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/276)
c. [eth-xmr atomic swap](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/277)
d. Doug Tuman's proposal to change the terms of his CCS proposal (full time to half time + 6 months to 1 year)
6) Workgroup reports
a. Dev workgroup
b. Localization workgroup
c. Outreach workgroup
d. Events workgroup
e. Website workgroup
f. Policy workgroup
g. UX workgroup
7) Open ideas time
8) Confirm next meeting date/time

[Previous meeting including logs](https://github.com/monero-project/meta/issues/638)

Meeting logs will be posted here afterwards.





# Discussion History
## carrington1859 | 2022-01-02T17:38:29+00:00
16:00:18 <carrington[m]_ 1. Introduction
16:00:18 <carrington[m]_ Hello and welcome to a Monero community meeting! These meetings are a chance for updates and discussions on recent events in Monero, as well as focussed discussion on crowd funding proposals. Please try and stick to the agenda, as there will hopefully be time at the end for any other business.
16:00:18 <carrington[m]_ https://github.com/monero-project/meta/issues/644
16:00:30 <carrington[m]_ 2. Greetings
16:00:31 <msvb-lab_ Hello.
16:00:40 <carrington[m]_ Hello! Do we have many people around today?
16:00:42 <TheCharlatan_ hello :)
16:00:58 <rottenstonks_ Yo.
16:01:02 <netrik182_ Hello
16:01:11 <monero-guides[m]_ happy ny all :)
16:01:53 <rottenstonks_ Matrix ban still in place for me? Only IRC users can read me at the moment? Check, check. 1, 2, 3...
16:01:54 <nioc_ is it Dec 11 already?
16:02:01 <rottenstonks_ No. November 3rd.
16:02:08 <carrington[m]_ 3. Community highlights
16:02:25 <chowbungaman[m]_ Hi guys.
16:02:28 <midipoet_ hello
16:02:32 <rottenstonks_ yep. Matrix ban still there. :)
16:02:59 <carrington[m]_ It has been a few weeks since a meeting here, but there is lots going on! I recommend checking out this for a summary of events:
16:03:00 <carrington[m]_ https://www.monero.observer/monero-observer-blitz-december-2021/
16:03:41 <carrington[m]_ Unless something important happened today or yesterday
16:04:28 <carrington[m]_ I'll leave time at the end for anyone to bring up anything in particular not on the agenda
16:04:40 <carrington[m]_ 4. CCS Updates
16:05:06 <carrington[m]_ a. Pluja's educational content for Monero plus kycnot and iseeyourcash maintenance
16:05:06 <carrington[m]_ https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/273
16:06:28 <carrington[m]_ The milestones seem well defined and Pluja has suggested in a comment that they are willing to bring updates to getmonero.org as they go along if possible
16:07:22 <carrington[m]_ It looks ready to go IMO but please leave a comment there if you can. Unfortunately I couldn't get a reply off Pluja in time for this meeting
16:08:07 <carrington[m]_ b. MoneroKon 2022
16:08:07 <carrington[m]_ https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/276
16:08:54 <carrington[m]_ Note there is also a scheduled meeting for Monerokon planning in just less than 2 hours in another room
16:08:54 <carrington[m]_ https://github.com/monero-project/meta/issues/629
16:10:04 <midipoet_ it would be great to iron out any remaining issues for the MoneroKon 2022 CCS
16:10:16 <midipoet_ as we should try and move forward (if possible)
16:10:45 <netrik182_ what issues are holding it back?
16:10:56 <midipoet_ it may be helpful to remind all that if the CCS is not funded, it will roll over to MonerKon 2023 (i made that explicit in an update earlier today)
16:11:20 <midipoet_ netrik182: i think there is still some resistance to whether MoneroKon should go ahead at all. 
16:11:27 <rottenstonks_ It can be rolled over only if it gets fully funded, not partially funded, worth noting.
16:11:49 <midipoet_ all other issues (i think) have been dealt with - bar some expressed concern over still not having a local champion
16:11:56 <rottenstonks_ midipoet: you got a reply to your comment on GitLab. https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/276#note_14444
16:12:08 <netrik182_ well, having the terms defined it would be a matter of people voting with their money, no?
16:12:15 <midipoet_ rottenstonks: is that true always (the rolling over)?
16:12:20 <rottenstonks_ Read the comment.
16:12:30 <netrik182_ I'm in favor of moving
16:12:49 <carrington[m]_ Rotten has pointed out that there is a CCS rule which says partial funds go to the General Fund. I guess you would need core to make an exception to that rule?
16:12:56 <rottenstonks_ I am not in favor of moving. Further thoughts and deliberation found in comments section. Everyone welcome to jump in.
16:13:57 <midipoet_ rottenstonks: the rule you link to does not describe partially funded CCS (unless i am mistaken)
16:14:16 <Lyza_ I'm not sure what the benefits of this event would be to the community
16:14:31 <midipoet_ and it seems there can be exceptions (i think a pandemic is fair excuse)
16:14:35 <rottenstonks_ midipoet: It does.
16:15:04 <rottenstonks_ unable to be completed, or otherwise put in a state where donated money will not be dispersed to the intended recipient, the default is that the remaining XMR will be put in the Monero General Fund. 
16:15:15 <rottenstonks_ _ unable to be completed
16:15:40 <rottenstonks_ Lyza: there was Konferenco 2019. didn't you hear? was the first edition.
16:15:43 <midipoet_ that is not the same as partially funded, is it?
16:15:45 <carrington[m]_ If I remember correctly there was an exception made for farcaster CCS
16:16:07 <Lyza_ yes I know there have been past conferences which I was going to point out, but I'm not sure I ever saw the benefit from those either
16:16:15 <midipoet_ if the CCS gets funded (and then MoneroKon cancelled) - digital renegades will have the XMR
16:16:15 <rottenstonks_ midipoet: I guess we will have to wait until someone from Core clarifies that. :)
16:16:24 <midipoet_ they can roll it over to MoneroKon 2023
16:16:45 <rottenstonks_ That I am not questioning. I am questioning it being partially funded, not fully.
16:16:57 <midipoet_ rottenstonks: i have already spoken to binaryfate and they have intimated that trying to put on MoneroKon 2022 is worth the risk
16:17:08 <Lyza_ <carrington[m]_ I also recall that there have been exceptions where partially funded CCS were refunded
16:17:17 <rottenstonks_ Lyza: Hmm. Well, it's an opportunity for researchers and enthusiasts to give talks about what they have been working on, projects, such.
16:17:56 <midipoet_ rottenstonks: i though partially funded could be paid out (i am fairly sure that is the case)?
16:17:57 <rottenstonks_ midipoet: What does that have to do with partially, fully funded, the CCS rule and money being rolled over?
16:18:23 <rottenstonks_ That is exactly what I am pursuing clarification for from core team, specifically that rule and this case.
16:18:41 <rottenstonks_ Lyza: ye. let's see if this will be another exception then. :)
16:19:05 <midipoet_ _ Your work on the project can begin before the proposal is fully funded, and milestones may (at times) be paid out before the proposal is fully funded.
16:19:09 <midipoet_ that is from the Rules
16:19:29 <rottenstonks_ That has nothing to do with money getting rolled over, again.
16:20:08 <midipoet_ it accounts for a partially funded proposal starting (and XMR being paid out)?
16:20:37 <midipoet_ though in reality, i would not think it wise to start things if the CCS were not fully funded
16:20:55 <midipoet_ but it seems there is some flexibility in the CCS rules (it even states as such)
16:21:48 <midipoet_ personally (though biased) i do not see the risk in moving the CCS to funding stage. if there is no support (one assumes) it won't get funded. 
16:21:55 <netrik182_ The way I read it is that fully funded proposals that are not completed (people do not deliver what they promised) get moved to general fund but exceptions can be made on Core's discretion 
16:22:12 <midipoet_ netrik182: yes - i would read it that way as well
16:22:19 <carrington[m]_ Getting some clarification from core on whether a partially funded CCS can be rolled over seems to be the logical step here
16:22:27 <rottenstonks_ Agreed.
16:22:33 <netrik182_ yes ^
16:23:07 <midipoet_ seeing as Core is explicitly involved with Digital Renegades, and expressed support (albeit privately) for MoneroKon 2022, i am not sure what the remaining risk is? 
16:23:52 <nioc_ All is moot when this is getting fully funded
16:24:06 <midipoet_ luigi1111: if the MoneroKon 2022 is moved to funding (and not funded by some future deadline - perhas mid Feb), can the funds be moved to a MoneroKon 2023 fund?
16:24:07 <rottenstonks_ nioc: says your wallet? ;)
16:24:11 <midipoet_ ArticMine[m]: ^
16:24:14 <midipoet_ binaryFate: ^
16:24:25 <nioc_ rottenstonks: pump it baby
16:25:00 <luigi1111_ no issues with that from my end
16:25:10 <midipoet_ luigi1111: thank you
16:25:19 <Lyza_ I'm not fully clear on what the role of the CCS proposal stage is -- should any well defined proposals be moved to funding required so that support can be gauged by the amount of funding, or is there some additional gatekeeping at play in terms of trying to judge support before moving to funding req'd
16:25:49 <midipoet_ Lyza: i think that is a fair question. i think the ideas stage is to quality control what is moved to funding. 
16:26:02 <rottenstonks_ Lyza: Normally a couple community meetings, a couple reddit threads and GitLab discussions in the comments section help luigi1111 decide what gets moved to funding stage or not.
16:26:26 <rottenstonks_ The more ideas and discussions, the merrier.
16:26:27 <midipoet_ the criticism, iterative improvement, and discussion is viewed as integral to the 'ideas' process
16:26:53 <carrington[m]_ Yes so comments on the gitlab posts are appreciated
16:27:58 <carrington[m]_ OK there can be more Monerokon discussion at the meeting at 1800 UTC 
16:28:33 <Lyza_ alright cool so what I'm getting is that the bar is *relatively* low as long as the proposal isn't really bad or really unpopular, which seems p reasonable
16:28:36 <carrington[m]_ c. eth-xmr atomic swap
16:28:46 <carrington[m]_ https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/277
16:29:17 <netrik182_ yes Lyza
16:29:24 <carrington[m]_ elizabeth:  are you around?
16:29:31 <Lyza_ been waiting for the eth-xmr swaps to be moved to funding rew personally :) I do see merit in Justin's argument for LGPL
16:29:47 <carrington[m]_ There seem to be some unresolved controversies about licencing in the gitlab comments
16:32:46 <netrik182_ Yeah, some comments seem unanswered 
16:33:19 <carrington[m]_ This proposal has very clear milestones and it seems people are excited about the idea
16:33:19 <carrington[m]_ Please throw a comment on the gitlab if you have strong opinions on the issues raised there
16:33:53 <carrington[m]_ I don't have a strong opinion either way on licencing but I know it can get spicey for some people
16:34:15 <carrington[m]_ d. Doug Tuman's proposal to change the terms of his CCS proposal (full time to half time + 6 months to 1 year)
16:34:55 <carrington[m]_ chowbungaman:  could you summarise your proposed change?
16:34:56 <chowbungaman[m]_ Hi guys I’m here
16:35:18 <Lyza_ fwiw I would support the proposal under any license
16:35:44 <sunchakr[m]_ hi guys im going to type from Sunita's account, so i can be on computer instead of phone. 
16:35:56 <rottenstonks_ Lyza: would be helpful for the person submitting the proposal if you post that comment on GitLab.
16:37:16 <sunchakr[m]_ I (chowbungaman) am looking to alter my proposal so that it is extended to year from 6 months. So instead of working "full-time" for 6 months, i will be working "part-time" for a year. With the intent of accomplishing (atleast) the same milestones.
16:38:22 <carrington[m]_ Here is the proposal for context:
16:38:22 <carrington[m]_ https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/250
16:38:36 <carrington[m]_ Fully funded but unstarted at this point
16:39:05 <sunchakr[m]_ I have unofficially already started my proposal since being awarded the CCS but have not officially started yet. I would like the official start date to start now
16:39:17 <sunchakr[m]_ i have accomplished a bunch:
16:40:26 <Lyza_ I don't have a dog in this race but I see little issue here --- curious what your reason is for wanting to move to aprt time though sunchakr[m]
16:40:32 <midipoet_ i would support whatever chowbungaman[m] requires to make their CCS work in terms of FT or PT. 
16:41:02 <midipoet_ though, it would be sad if you needed to get a job (as the plan originally was to have Monero as your "job")
16:42:35 <carrington[m]_ I see no issue with the changing timeframe considering no additional funds are needed
16:43:55 <sunchakr[m]_ -grew MoneroTalk show in terms of subscribers and podcast downloads, brought on guests outside of the monero community, been on 3 podcasts as a guest, presented at a conference, arranged to attend a conference as media in January, launched the MoneroTopia conference we are hosting in April,  and made progress with Gratuitas (heading down to the farm this month to give away wallets to the workers for this years harvest and to start
16:43:55 <sunchakr[m]_ shipping in green beans that we will roast locally)
16:44:09 <carrington[m]_ My only concern (which also applies to the original proposal) is that it is maybe difficult for Core to determine if milestones have been hit when it is a month-by-month proposal with tasks in no particular order
16:47:58 <sunchakr[m]_ <Lyza_ "I don't have a dog in this..." <- my reasoning was that i felt i could not sustain myself yet off of the CCS funds only at this point. I realized the risk was to great. The eye-opener for me was when we ran into an issue with the MoneroTopia event.
16:49:09 <Lyza_ gotcha, unfortuante but makes sense
16:49:13 <netrik182_ 1 year part-time seems OK if milestones are met anyway. Though I thought the whole point of going FT was to dedicate more time to it so
16:50:33 <sunchakr[m]_ <midipoet_ "though, it would be sad if you..." <- I would be keeping my current day job. The goal is still to go full-time Monero but to make more progress on my Monero related projects first. I thought i could make the leap now but it is too risky. A year of continuing to work part-time will hopefully get me to the point i can go full-time. 
16:51:17 <midipoet_ sunchakr[m]: sounds good. keep up all the hard work
16:51:28 <carrington[m]_ Well it seems people are broadly in favour of this change in terms. Maybe it would be a good idea to make a Reddit post to announce the change in plans? 
16:52:16 <carrington[m]_ Reddit always brings out the trolls/bots but if you ignore those there might be useful feedback
16:53:25 <sunchakr[m]_ netrik182: ok, i can do the reddit post, but yea im sure there will be many trolls
16:53:41 <carrington[m]_ 5. Workgroup reports
16:54:03 <carrington[m]_ Are there any workgroups which would like to report what they've been up to?
16:55:16 <sunchakr[m]_ So what is the process for actually starting the CCS then? Can we make January 1st the start date.
16:55:28 <netrik182_ On localization/translation side, we have had great progress the last couple weeks in regard to monero GUI
16:56:05 <carrington[m]_ sunchakr:  I guess so. Maybe keep a log of Monero-specific work from that date so that you post updates to the CCS gitlab?
16:56:14 <netrik182_ So what is the process for actually starting the CCS then? Can we make January 1st the start date. <- usually people started after getting funded. So I guess you can just announce the day you want it to be
16:57:37 <carrington[m]_ That way there is clear evidence in the CCS gitlab that each milestone has been accomplished
16:57:54 <netrik182_ Afrikaans, Romanian, Dutch, Japanese, Hungarian, Hebrew, Dutch, Polish, Chinese (Simplified), German have new translation and will make into next point release
16:58:15 <netrik182_ some of them are 100% translated
16:58:35 <netrik182_ This week I'll push translations to getmonero website as well
16:59:34 <carrington[m]_ That is all fantastic news. I think semi-regular calls for translators on Reddit will help fill any gaps you might have
17:00:15 <netrik182_ Yes, I'll do one together with a more detailed report
17:00:25 <netrik182_ That's it from my side
17:00:50 <carrington[m]_ Confirm next meeting date/time
17:01:53 <carrington[m]_ I can put together another of these in 2 weeks if people like, same time. I'm open to ideas of how to get more voices in community meetings or how to run them better
17:02:40 <carrington[m]_ That just leaves "Open ideas time" if people want to carry on discussion on anything in particular.
17:02:57 <midipoet_ carrington[m]: great meeting - thanks. 
17:03:10 <nioc_ carrington[m]: ty :)
17:04:45 <carrington[m]_ I'll end the meeting here as far as logs are concerned, and post those on the github issue
17:06:04 <sunchakr[m]_ <netrik182_ "1 year part-time seems OK if..." <- Sorry, sent wrong reply. To answer this question. Yes, goal was to be full-time. Now it will be PT but with the goal of making enough progress within the year to be able to then go FT monero. I stated in my CCS that i would be looking to work 50-60hrs per week FT, so now the aim would be 25-30hrs PT. While I am obviously motivated to work on Monero without CCS funds (which i have
17:06:05 <sunchakr[m]_ done to date),  this funding will provide additional support and motivation that will hopefully allow me to transition into full-time. 

# Action History
- Created by: carrington1859 | 2022-01-01T11:59:41+00:00
- Closed at: 2022-01-04T00:54:33+00:00
