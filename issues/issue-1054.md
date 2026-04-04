---
title: 'Meeting(s) for the Monero devs: Who, where, which subjects?'
source_url: https://github.com/monero-project/meta/issues/1054
author: rbrunner7
assignees: []
labels: []
created_at: '2024-08-13T05:37:22+00:00'
updated_at: '2024-08-18T21:25:31+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
In [this Seraphis wallet workgroup meeting](https://github.com/monero-project/meta/issues/1050) and in [this MRL meeting](https://github.com/monero-project/meta/issues/1052) (log still only [here](https://libera.monerologs.net/monero-research-lab/20240807) as I write this) the following idea was discussed: Broaden the focus of those wallet workgroup meetings to turn them into general dev meetings, open for *all* subjects related to Monero development, and not merely Seraphis (up to about 2 months ago) or FCMP (recently). Dev meetings like we held them for many years in the past.

The idea was received favorably in those two meetings, and thus we had [the first such "dev meeting"](https://github.com/monero-project/meta/issues/1053) yesterday.

However, in the run-up to that not everybody was convinced that a single such dev meeting in the -dev matrix room and IRC channel is really the best arrangement, and alternatives were proposed and discussed.

This issue here is meant to be the place to present and discuss such proposals further, so that hopefully we can achieve our famous "loose consensus" of how to proceed long-term.

Please go ahead and make your opinion heard!

# Discussion History
## rbrunner7 | 2024-08-13T05:53:00+00:00
My own take on this, before yesterday's meeting and still now after that:

I am happy with a single such broad dev meeting, for *all* dev related matters, whether current or future, in the -dev Matrix room and IRC channel. I don't see any problems with too many meeting issues and subjects that way, that -dev room overflowing with too much activity, or similar. And even if, as soon as any hard problems arise, surely we will be flexible enough to react *then and there*.

"Simple is simply simpler". One of my mottos in life. Why complicate things beyond such a single meeting, at least as long as it works.

## One-horse-wagon | 2024-08-13T12:02:03+00:00
IMO, having a weekly dev meeting brings important focus to the development of Monero because there are a lot of projects and ideas being pursued.  The meeting held yesterday showed three things.  1.  You need a moderator to keep order and I vote to appoint rbrunner7.  2.  You need an agenda prepared ahead of time.  3.  Make the meeting a little longer like 1 hour 15 minutes or even 1 1/2 hours to cover everything.  

## nahuhh | 2024-08-13T12:24:03+00:00
3 is why we should split the meetings.
Too many different topics

## selsta | 2024-08-13T12:29:35+00:00
My preference would be to have -dev for discussing short term changes (existing bugs, already PRd changes, releases), while for long term development (Seraphis, FCMP) to have a separate channel.

## nahuhh | 2024-08-13T12:32:01+00:00
The proposal was
1. Rename and readdress no-wallet-left-behind to be an "official" monero-namespace workgroup
2. For this room to be used for topics and meetings for work that falls in between mrl and dev, such as seraphis, jamtis, previously triptych, currently fcmp (at least for the next couple weeks)
3. Leaving -dev for "release discussion, triaging and assigning issues and prs, dev reports, and in-production work". 

Even if you do not agree with 2 or 3, 1 _should_ have happened a long time ago. 

## rbrunner7 | 2024-08-14T15:54:29+00:00
@nahuhh : I think for your proposal it makes quite a difference whether you *also* propose to hold not only 1 dev related meeting, but 2 of those, in different rooms, with a different focus each.

Never mind having channels with clear topics and good names, but establishing yet another meeting could run into problems. Quite practical problems at that, on which day whould that be, who would moderate, would devs be eager to attend not one, but two dev meetings.

## nahuhh | 2024-08-14T16:53:07+00:00
something like a 30min -dev meeting on the 1st monday of month (or every 4 weeks etc) wouldn't hurt anybody.

scheduling, selecting a chair etc are all things that are open. I'd probably choose vtnerd or selsta to write the agendas and chair the meetings. they could be short and to the point, more of briefing and debriefing.

i agree that too many meeting are both annoying and waste of resources, but i think short and to the point dev meetings are better for productivity than combining with long, messy, open ended ones 

## jeffro256 | 2024-08-14T18:55:23+00:00
The meeting on Monday did run a bit long, but I wonder if that was due to it being the first meeting in -dev in a couple years, lack of stricter organization, etc. I think we should attempt another similar meeting this coming Tuesday with more structure and see how that pans out. 

> something like a 30min -dev meeting on the 1st monday of month (or every 4 weeks etc) wouldn't hurt anybody.

IMO this is far too infrequent. I like a quick meeting once a week at a predictable time, with no obligation to fill up the entire time slot if there isn't anything to discuss



## SNeedlewoods | 2024-08-14T19:24:24+00:00
> I like a quick meeting once a week at a predictable time, with no obligation to fill up the entire time slot if there isn't anything to discuss
+1

For my taste last meeting was a bit crowded, but that may be because of the upcoming release and it was the first -dev meeting after a long time. I'd be cool with renaming no-wallet-left-behind and have the dev-meetings there, if others think the meetings clog monero-dev.

## nahuhh | 2024-08-14T19:37:07+00:00
> IMO this is far too infrequent. I like a quick meeting once a week at a predictable time, with no obligation to fill up the entire time slot if there isn't anything to discuss

i agree. I said the extreme as to not try to add another hour long meeting to people schedules, but i personally think biweekly for 30mins would be acceptable.

the problem with too frequent meetings is that you might have unreliable attendance. I think weekly might be too much. 

Biweekly for issues/prs/releases is a good spot in the middle

i dont think this past meeting was crowded due to time since a meeting, but due to the many different areas that were covered. The lack of an agenda didnt help either. 

an agenda for a 30min bi-weekly "-dev" meeting could like like

1. Greetings / attendance 2min
2. Important news 5min
3. Progress reports on assignments from previous meeting 5min
4. Higher priority issues since last meeting 5 min (list issues in agenda)
5. assign reviews and issues (list prs in agenda) 5 min
6. Other business & release planning 5 min
7. Closing statements / debriefing 2min
8. Confirm next meeting time 1min



## j-berman | 2024-08-15T21:38:20+00:00
Agree the -dev meeting felt a bit crowded

30m bi-weekly -dev meeting for short term changes / proposals / issues / releases sounds good to put a spotlight on more immediate tasks. A separate 1 hour weekly meeting for focus on long term development (fcmp's, Carrot/ Jamtis/Seraphis, wallet API) also sounds good to me.

I don't have a strong opinion on where the latter meetings should be held. The topics have grown wider than no-wallet-left-behind's original goal, but I feel the meetings have achieved a solid flow as is and don't want to "fix" what isn't broken, so keeping them in that channel seems ok to me.

## kayabaNerve | 2024-08-16T11:44:57+00:00
I prefer NWLB to remain the existing meeting it is. I leave comments on what any meeting in -dev should be to the rest of y'all.

## rbrunner7 | 2024-08-16T12:43:04+00:00
For the record, I carry over a comment from @dangerousfreedom1984 that he made in the "No wallet left behind" Matrix room a few days ago:

> Why do we have to move the channel? I believe we can broaden the scope of the discussions but we can stay here. I just read your conversation with ofrnxmr and I think he is right. Moving there would just pollute the dev channel with things that are not in production yet. It would be much easier to have things separated when searching something at the history of the channel too.

## rbrunner7 | 2024-08-16T12:44:26+00:00
And for the record as well, another comment that was made there, by @rottenwheel:

> My opinion here should count as much as a zero to the left, but I'd lean more towards moving and staying over at -dev with the goal of getting further traction and more eyes on the ongoing development and decision-taking process along the way. My 2 cents.

## rbrunner7 | 2024-08-16T12:54:44+00:00
I see quite a number of different opinions here so far, but what I don't see is strong support for a single, "unified" dev meeting in the -dev room and and IRC channel, like the meeting we held last Monday.

If we continue with the meetings that for a long tim sailed under a flag of "Seraphis wallet workgroup" and lately had taken on FCMP as their main focus, I have a proposal how to call those: *Monero Tech meetings*.

I wouldn't mind to rename the *No Wallet Left Behind* room to *Monero Tech*, if that does not cause any technical problems, and all history and all channel memberships can be preserved.

## nahuhh | 2024-08-16T13:51:56+00:00
monero-tech << https://monerotech.info i think this would be a poor name due to overlap with your website
monero-next
monero-upgrades
monero-staging
monero-evolution
monero-dev-lab

just some not-very creative suggestions for room addressing

wont cause technical problems. Don't have to remove nwlb address. would just be adding a new one

## One-horse-wagon | 2024-08-16T14:01:02+00:00
On the day of the meeting in a revisioned or renamed "No Wallet Left Behind" room, I would post a notice in the Monero Dev room.  Interested devs would show up and the busy dev room could continue on as they do.  

## nahuhh | 2024-08-16T18:02:26+00:00
IMHO

not good names:
monero-tech << https://monerotech.info i think this would be a poor name due to overlap with your website
monero-next << confusing meta title "Monero Next meeting on.."

possible good names:
monero-upgrades
monero-staging
monero-evolution
monero-dev-lab

## kayabaNerve | 2024-08-16T18:23:48+00:00
monero-next? I also like `dev-lab` well enough :)

## One-horse-wagon | 2024-08-18T21:25:30+00:00
dev-lab gets my vote.  

# Action History
- Created by: rbrunner7 | 2024-08-13T05:37:22+00:00
