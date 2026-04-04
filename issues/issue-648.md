---
title: 'Community Workgroup Meeting: Sunday 16th January 2022 16:00 UTC'
source_url: https://github.com/monero-project/meta/issues/648
author: carrington1859
assignees: []
labels: []
created_at: '2022-01-08T17:04:44+00:00'
updated_at: '2022-01-22T10:22:52+00:00'
type: issue
status: closed
closed_at: '2022-01-22T10:22:52+00:00'
---

# Original Description
Location: [Libera.chat, #monero-community](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-community:monero.social?via=matrix.org&via=monero.social)

[Instructions for joining the monero.social Matrix server.](https://forum.monero.space/d/79-how-to-join-the-monero-core-team-matrix-server-web)

Time
16:00 UTC [Check your timezone](https://www.timeanddate.com/worldclock/converter.html?iso=20220116T160000&p1=1440)

Moderator: Carrington

Please reach out in advance of the meeting if you would like to propose an agenda item.

Proposed Meeting Items:

1) Introduction
2) Greetings
3) Community highlights
News: [Monero Observer](https://www.monero.observer/) - [Monero Moon](https://johnfoss.medium.com/) - [Monero Revuo](https://localmonero.co/revuo)
4) CCS updates
a. [Pluja's educational content for Monero plus kycnot and iseeyourcash maintenance](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/273)
b. [eth-xmr atomic swap](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/277)
c. [selsta part-time monero dev (3 months)](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/279)
d. [v1docq47 - video creation and translations into russian (february - july 2022)](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/280)
5) Workgroup reports
a. Dev workgroup
b. Localization workgroup
c. Outreach workgroup
d. Events workgroup
e. Website workgroup
f. Policy workgroup
g. UX workgroup
6) Open ideas time
7) Confirm next meeting date/time

[Previous meeting including logs](https://github.com/monero-project/meta/issues/644)

Meeting logs will be posted here afterwards.


# Discussion History
## carrington1859 | 2022-01-18T22:24:41+00:00
```
14:27:13 <carrington[m]> I'm very sorry but it looks like I might be forced offline in the next few hours. If people would still like the regular meeting, a volunteer to moderate will be needed
14:27:15 <carrington[m]> https://github.com/monero-project/meta/issues/648
14:33:47 <Rucknium[m]1> I think we should still have the meeting. monerobull ?
15:46:21 <monerobull[m]1> <Rucknium[m]1> "I think we should still have the..." <- huh?
15:47:23 <monerobull[m]1> uh sure
15:58:55 <plowsof[m]> 🕓️
16:00:28 <monerobull[m]1> hello everyone, the meeting starts now :)
16:01:02 <v1docq47> hi
16:01:38 <binaryFate> hello
16:01:43 <elizabeth[m]> hey :) 
16:02:13 <monerobull[m]1> I don't know how its usually handled but I think we jump straight to the CCS updates, or does anyone have something to say about the community highlights
16:02:13 <monerobull[m]1> ?
16:02:22 <deedledea[m]> Hi :)
16:02:35 <binaryFate> I think you're supposed to follow agenda of https://github.com/monero-project/meta/issues/648
16:02:44 <Rucknium[m]1> Hi
16:03:27 <midipoet> hello
16:03:27 <binaryFate> I have a quick point to make myself outside of announced agenda
16:04:08 <monerobull[m]1> binaryFate: I know. i guess we can mention that localmonero published their weekly report.
16:04:16 <monerobull[m]1> * I know. i guess we can mention that localmonero published their weekly report today
16:04:35 <monerobull[m]1> monero moon is also back on
16:04:43 <binaryFate> Can I make my point? Sorry I am not sure I can stay all the hour
16:05:06 <monerobull[m]1> sure go ahead
16:05:50 <binaryFate> Thanks! As you may know I am escrowing the Monero general fund money.
16:06:23 <binaryFate> I plan to release a transparency report soon, hopefully within the next week or two.
16:06:46 <binaryFate> (Same as I did last June and before that, check out the website for references)
16:07:19 <monerobull[m]1> sounds good :)
16:07:21 <binaryFate> Different topic but starting from last September, Globee stopped sponsoring the server for the website
16:08:04 <binaryFate> We had one day of downtime before finding out the invoice wasn't paid, for those who recal
16:08:19 <binaryFate> Anyway, since then I have paid for the website personally using my credit card
16:08:36 <binaryFate> It's precisely 2k$ per month, which now amounts to 10k$ that I've paid.
16:09:05 <monerobull[m]1> binaryFate: did they just stop paying for it without a notice?
16:09:38 <binaryFate> At the time yes, and actually again the next month until we understood not to rely on them, but that's not the topic.
16:10:04 <binaryFate> I will repay myself using XMR from the general fund next few days, for those 10k$
16:10:52 <binaryFate> I was keen to make that public in advance so nobody freaks out, since I'm basically going to send money myself from GF to my personal wallet. If anybody has an issue with this let me know.
16:10:55 <monerobull[m]1> make sure to make it real clear what happened in the report
16:10:57 <binaryFate> That's it, thanks.
16:11:21 <binaryFate> Will do.
16:12:04 <monerobull[m]1> maybe even a short separate reddit post
16:12:45 <monerobull[m]1> moving on, do we have any CCS updates?
16:13:40 <monerobull[m]1> currently only monerokon needs funding and sits at 10.07 xmr out of 328
16:13:51 <nioc> https://ccs.getmonero.org/proposals/MoneroKon-2022-CCS.html
16:14:48 <monerobull[m]1> we also now know haveno development will require around 200k$ and starts raising money soon
16:16:15 <monerobull[m]1> since it will be a for-profit exchange, they plan on using parts of future profits to fund monero development as a thank you
16:16:40 <monerobull[m]1> nothing really official right now, just letting you guys know
16:17:14 <Rucknium[m]1> My CCS update: OSPEAD research is at a bit of a pause while I catch up on BCH work. I have a draft of part of the OSPEAD technical specification and I can send it to anyone if they want to have a look and/or give feedback.
16:17:17 <Rucknium[m]1> I will work on a version of it that is more layperson-friendly and release it publicly in the near future.
16:18:33 <plowsof[m]> I see that elizabeth is here. perhaps we could jump to addressing b. eth-xmr atomic swap ?
16:20:30 <monerobull[m]1> of course. theres also been a post on reddit just today demanding eth-xmr to be moved to funding
16:21:14 <monerobull[m]1> s/of course. theres also been a post on reddit just today demanding eth-xmr to be moved to funding/of course. theres also been a post on reddit just today asking for eth-xmr to be moved to funding/
16:21:48 <elizabeth[m]> hey everyone, there's been a lot of discussion on the licensing for the swap proposal. like I mentioned on the PR, I'd like to move forward with GPL if possible (as some code will need to be rewritten for a license change to be possible). happy to add a section to the proposal saying if requested later on I'll change it to LGPL 
16:22:12 <elizabeth[m]> but overall this seems to be a larger discussion that needs to be had about licensing 
16:23:14 <monerobull[m]1> does anyone know how licensing is usually handled with CCS funded projects?
16:26:04 <ajs_[m]> "The CCS is intentionally left as informal as possible. This allows for flexibility of the system, and keeps things from being red taped into oblivion."
16:26:12 <ajs_[m]> https://ccs.getmonero.org/what-is-ccs/
16:26:48 <ajs_[m]> but
16:26:50 <ajs_[m]> "All work must be licensed permissively at all stages of the proposal. There is no time where your work can be licensed under a restrictive license (even as you're working on it). Your proposal will be terminated if this is not remedied."
16:26:53 <surgeon_[m]> GPL > LGPL
16:28:03 <Rucknium[m]1> >All work must be licensed permissively at all stages of the proposal. There is no time where your work can be licensed under a restrictive license (even as you're working on it). Your proposal will be terminated if this is not remedied.
16:28:03 <monerobull[m]1> LGPL just leads to foss code ending up in closed source projects, right?
16:28:10 <Rucknium[m]1> According to the official rules:
16:28:10 <Rucknium[m]1> https://ccs.getmonero.org/what-is-ccs/
16:28:38 <Rucknium[m]1> "permissive license" is fairly vague. Deliberately, I think.
16:29:53 <monerobull[m]1> do we want to keep discussing this or move on?
16:30:06 <elizabeth[m]> ajs_[m]: I admit I hadn't read this before, my bad 
16:30:06 <elizabeth[m]> does LGPL count as permissive? if so I can prioritize changing the license. I'm guessing GPL is not permissive
16:30:26 <elizabeth[m]> monerobull[m]1: yeah, this is why I prefer GPL generally 
16:31:38 <monerobull[m]1> any other CCS related updates?
16:32:36 <ajs_[m]> https://en.wikipedia.org/wiki/Permissive_software_license
16:33:58 <monerobull[m]1> do we have any workgroup reports?
16:35:19 <nioc> meeting of #monero-events at 18:00 UTC
16:35:32 <nioc> so a little over an hour
16:36:16 <monerobull[m]1> how much longer can the monerokon CCS stay open?
16:36:58 <midipoet> monerobull[m]1: i think i set a loose deadline for mid-Feb. if the goal was not reached, we would cancel 2022 event, and roll funds over to a 2023 fund.
16:36:59 <nioc> the original one in 2019 stayed open for a long time
16:37:13 <nioc> and that was during a bear market so................
16:38:11 <midipoet> i will try and make a reddit post this week to stir up some interest and get some more donations. it's nice to see there are 27 contributions so far though - thanks to everyone that has donated
16:38:31 <monerobull[m]1> midipoet: let's hope it gets reached
16:39:02 <midipoet> monerobull[m]1: yes, i am hopeful as well. 
16:39:55 <monerobull[m]1> I think this particular meeting is close to being done. does anyone want to mention anything not on the agenda?
16:41:00 <Rucknium[m]1> What I am concerned about with the ETH<>XMR proposal is that the licensing discussion is holding things up. I think it would be fine to kick the can down the road and just let this go to funding. Determine licensing later.
16:41:34 <midipoet> Rucknium[m]1: i thought of suggesting something similar. perhaps a milestone could be built in to account for the licensing change that is required?
16:42:04 <Rucknium[m]1> It is crucial that more devs be brought into the Monero ecosystem, and destruction of red tape is one of the reasons that Monero exists in the first place.
16:42:08 <midipoet> this would give some certainty to elizabeth[m] that the funding is there, as long as the licence is amended. 
16:42:53 <nioc> if change of licensing means the rewriting of some of the code will the amount of funding need to be changed?
16:44:12 <elizabeth[m]> <ajs_[m]> "https://en.wikipedia.org/wiki/..." <- tbh I don't want to license as MIT/apache/BSD as I don't want my code ending up in some closed source (probably centralized) blockchain 
16:44:34 <elizabeth[m]> nioc: it's a minimal amount of code that needs to be rewritten, only one function. so we don't need to change it
16:44:48 <nioc> thx
16:46:41 <monerobull[m]1> I'd say mention the licensing thing in the CCS and go to funding. do we all agree?
16:47:07 <midipoet> why is there a hesitancy to allow a GPL licence (sorry if this has been asked before)?
16:47:22 <Rucknium[m]1> Ultimately this is elizabeth  's project. Yes, the community can have some input, of course. This won't necessarily be the _only_ XMR<>ETH atomic swap implementation.
16:48:37 <ajs_[m]> elizabeth:  i get it and generally prefer GPL myself. i think that rule was put in place because of drama from  contributor wanting to make a PR to monero code with a special licence
16:48:41 <midipoet> i think the licensing issue should be mentioned in the CCS, along with the rationale for choosing a licence (t minimum), but i don't see the great harm with GPL
16:48:54 <monerobull[m]1> i too think forcing a license that allows the code to be used in closed source projects is hella weird
16:50:52 <ajs_[m]> seeing this is not related to core code, this rule should be reconsidered generally imo
16:52:28 <monerobull[m]1> since there are no objections I think its safe to assume we reached consensus to move noots CCS to funding once the licensing is mentioned
16:54:16 <monerobull[m]1> anything else? 
16:54:25 <ajs_[m]> there should be a PR updating the rule if there is consensus to allow copyleft for non monero specific code
16:54:35 <elizabeth[m]> monerobull[m]1: sounds good, I'll add that in
16:55:08 <monerobull[m]1> next meeting same time same day, two weeks from now?
16:55:23 <v1docq47> If someone has questions about my CCS proposal, I will be happy to answer them
16:55:58 <binaryFate> make a PR updating https://repo.getmonero.org/monero-project/ccs-front/-/tree/master/what-is-ccs and we can have a threaded discussion
17:00:27 <monerobull[m]1> <v1docq47> "If someone has questions about..." <- I think you once used one of my edits <3
17:00:59 <monerobull[m]1> anyways. that's the meeting. next ones on the 30th of January.
17:01:25 <nioc> monerobull[m]1: thx for running the meeting on such short notice
17:01:50 <nioc> time of the next meeting?
17:01:54 <monerobull[m]1> can someone post the chatlog? I'm on my phone right now
17:02:16 <netrik182> Thanks for running monerobull 
17:02:52 <monerobull[m]1> nioc: 16:00 UTC
17:02:53 <elizabeth[m]> thank you! 
17:04:12 <monerobull[m]1> thanks for coming everyone, we were definitely productive today
17:05:21 <binaryFate> thanks monerobull[m]1
17:07:27 <monerobull[m]1> 👍
```

# Action History
- Created by: carrington1859 | 2022-01-08T17:04:44+00:00
- Closed at: 2022-01-22T10:22:52+00:00
