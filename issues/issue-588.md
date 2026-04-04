---
title: 'Community Workgroup Meeting: 24 July 2021 17:00 UTC'
source_url: https://github.com/monero-project/meta/issues/588
author: carrington1859
assignees: []
labels: []
created_at: '2021-07-10T20:00:40+00:00'
updated_at: '2021-08-04T17:11:39+00:00'
type: issue
status: closed
closed_at: '2021-08-04T17:11:39+00:00'
---

# Original Description
**Location**

[Libera.chat, #monero-community](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-community:monero.social?via=matrix.org&via=monero.social)

**Time**

17:00 UTC
19:00 CET
18:00 Irish Time
13:00 Eastern Time
10:00 Pacific Time
02:00 (2021/07/11) 日本標準時

[Use this timezone calculator to convert UTC to your time](https://www.timeanddate.com/worldclock/converter.html?iso=20210710T170000&p1=1440&p2=28&p3=111&p4=tz_et&p5=49&p6=179&p7=70&p8=224&p9=48&p10=136&p11=248)

Meeting chairperson: Keiji / ErCiccione

**Proposed Meeting Items**

Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

- Introduction
- Greetings
- Community highlights
- CCS updates
- Workgroup report
a. Daemon/CLI workgroup
b. Localization workgroup
c. GUI workgroup
d. Outreach workgroup
e. Defcon workgroup
f. Website workgroup
g. Policy workgroup
h. Malware workgroup
- Open ideas time
- Confirm next meeting date/time

# Discussion History
## Keiji-C | 2021-07-11T00:53:30+00:00
Since it seems like no one who attended 7/10 is able to chair the 7/24 meeting I'd like to help by chairing for 7/24

## Keiji-C | 2021-07-24T17:58:04+00:00
[5:00:52 PM] <Keiji[m]> Let's begin the Community Workgroup Meeting now!
[5:01:04 PM] <Keiji[m]> - Greetings
[5:01:21 PM] <v1docq47> hi
[5:01:36 PM] <ErCiccione> Hi
[5:03:01 PM] <Keiji[m]> - Community highlights
[5:03:34 PM] <Keiji[m]> Outside of workgroups, anything people want to highlight?
[5:05:07 PM] <Keiji[m]> - CCS updates
[5:05:52 PM] <Keiji[m]> I don't see any new CCS in Ideas or Funding Required since July 10 meeting, but are there any people wish to discuss?
[5:06:41 PM] <ErCiccione> quiet today :)
[5:06:56 PM] <v1docq47> too quiet :)
[5:07:01 PM] <Keiji[m]> Haha yep. It happens I guess
[5:07:40 PM] <mj-xmr[m]> I'd like to know if there are any special requests for my CSS, like where I should concentrate my mental energy, because there are many fronts to work on.
[5:07:40 PM] <mj-xmr[m]> I'm currently building a local matrix of extreme configurations, that would be too resource hungry for the GitHub CI to handle.
[5:07:52 PM] ⓘ ChanServ gives ops to ArticMine
[5:08:07 PM] <mj-xmr[m]> The GitHub action issues are mostly taken care of.
[5:08:55 PM] <mj-xmr[m]> The result of the build matrix will be published just as the other report, of course.
[5:09:34 PM] <john_r365> mj-xmr - it might be difficult to get a good reply to that in this meeting (could be wrong) - but perhaps if you wrote up a short post somewhere of the things you think are important to be working on, community members could give some feedback on which they think deserve priority?
[5:10:12 PM] <ErCiccione> yeah that would be useful. Even just an issue or something like that.
[5:10:34 PM] <Keiji[m]> GitHub Issue w/ link on Reddit maybe?
[5:11:01 PM] <mj-xmr[m]> OK, got it.
[5:12:22 PM] <Keiji[m]> Personally, I'd say if there's developers who mentioned issues w/ patch integrations, that first, followed by user issues ?
[5:13:59 PM] <Keiji[m]> - Workgroup reports
[5:14:19 PM] <Keiji[m]> I think we have just Website and Localization here?
[5:14:40 PM] <Keiji[m]> So we can start with b. Localization workgroup
[5:15:20 PM] <ErCiccione> not much to say. Today i updated the strings of the GUI and the CLI, so people can translate the new stuff.
[5:16:05 PM] <ErCiccione> people are actually translating every day, so soon i'll probably PR the updated strings upstream soon
[5:16:41 PM] <Keiji[m]> Nice! Great to hear!
[5:17:38 PM] <Keiji[m]> f. Website workgroup
[5:19:19 PM] <john_r365> side note ErCiccione - is there any tracking on how much the various languages are used? i'd guess not due to privacy, but just curious if there's any way at all?
[5:19:46 PM] <john_r365> perhaps node concentration by country is the closest proxy
[5:20:16 PM] <ErCiccione> for the getmonero, there should be. We have a matomo instance for analytics but has been broken since the very beginning. With that we can get some basic analytics from the server logs.
[5:20:30 PM] <coinstudent2048[> <ErCiccione "not much to say. Today i updated"> Is there a website for translation, or just github? I am just waiting someone started my language already :3
[5:20:53 PM] <ErCiccione> I've been wanting to access those info for quite some time for that very reason. With statistics we can work with lanaguages better and make informed choices/changes
[5:21:07 PM] <ErCiccione> coinstudent2048: https://translate.getmonero.org
[5:21:24 PM] <john_r365> from memory, running matamo shouldn't be very complex. any idea why it's not working/broken?
[5:22:02 PM] <john_r365> "
[5:22:24 PM] <ErCiccione> no. I've been talking with pigeons about it a few times but nothing really came up yet
[5:22:26 PM] <john_r365> "statistics we can work with lanaguages better and make informed choices/changes" -> exactly why i asked, would help with energy prioritisation
[5:22:49 PM] <ErCiccione> we have been working on language autodetection as well, so that was prioritized
[5:26:10 PM] <Keiji[m]> - Open ideas time
[5:26:38 PM] <Keiji[m]> Anything people want to discuss that wasn't talked about earlier?
[5:26:40 PM] <john_r365> next topic Keiji[m]?
[5:28:27 PM] <john_r365> I won't bring up transaction fees again *laugh face* as I've brought it up enough recently. but that's the main thing that's bugging me. seems far too cheap to store data on monero, that nodes be downloading and verifying for years to come
[5:28:45 PM] <john_r365> *will be
[5:29:39 PM] <ErCiccione> i think a github issue is the best place with that. There are many factors to consider
[5:30:05 PM] <Keiji[m]> Ok. I think Artic Mine is the resident transaction fee expert and they aren't here. Also, yes, probably GitHub is best for long discussion
[5:30:17 PM] <john_r365> agreed
[5:30:22 PM] <msvb-lab> ArticMine is here I think?
[5:30:36 PM] <msvb-lab> At least a few minutes ago.
[5:32:00 PM] <Keiji[m]> I guess just post a link here in IRC when you create the issue and ping Artic Mine then?
[5:32:26 PM] <Keiji[m]> If no one else has anything to discuss, we can conclude the meeting. Next meeting in 2 weeks?
[5:32:55 PM] <wfaressuissia[m]> What's the main purpose of such meetings ?
[5:33:28 PM] <jberman[m]> I have 1 thing
[5:33:36 PM] <jberman[m]> Yesterday it was mentioned in #monero-dev people wanted to discuss the divide by 0 bug and the patch for that in next release. I can share a status here and my opinion on a way forward. But considering above, I think the PR on github is the best format for that discussion, it's also fairly long with a number of factors to consider
[5:33:36 PM] <Keiji[m]> Mainly to pass down things, ask for help (like CCS feedback when we have more people)
[5:34:50 PM] <Keiji[m]> If you want to share the short summary here as not everyone follows the Issue probably that would be fine I think
[5:35:01 PM] <msvb-lab> Don't forget that we have a village staff meeting (for Defcon 5-7 August) in a half hour on #monero-events.
[5:35:54 PM] <jberman[m]> The PR (https://github.com/monero-project/monero/pull/7798) has 2 parts to it. First, it changes the decoy selection algorithm to correctly select more recent decoys in a ring. Second, it prevents a divide by 0 bug.
[5:35:54 PM] <jberman[m]> In IRC and in that issue, sech1 and tobtoht raised valid concerns that a change to the decoy selection algo would break tx uniformity. The ensuing discussion has been related to that
[5:36:36 PM] <jberman[m]> I believe there are 2 options of handling this concern:
[5:36:36 PM] <jberman[m]> 1. I shared a fix that would prevent the divide by 0 bug, and would only alter the decoy selection algorithm for clients that would be affected by divide by 0.
[5:36:36 PM] <jberman[m]> 2. Being 100% certain the fix does not pose material risk to users through breaking tx uniformity, and going with the fix in the PR.
[5:36:58 PM] <jberman[m]> On #2, I believe I've provided a fairly strong case why the risk posed to users seems likely immaterial, and more eyes on that would be appreciated.
[5:36:58 PM] <jberman[m]> Perhaps the best course of action is going with option #1 for now while we work toward 100% certainty for option #2. I can continue with a deeper analysis with more mathematical rigor in the meantime.
[5:37:00 PM] <ErCiccione> i think we'll need a dev meeting soon, there are a lot of things to discuss
[5:37:49 PM] <jberman[m]> Ya this seems like a difficult thing to discuss in this format
[5:38:12 PM] ← Pythayr has left (Ping timeout: 256 seconds)
[5:38:15 PM] <Keiji[m]> Usually dev meeting happens tomorrow, right?
[5:38:29 PM] <ErCiccione> it is, that's why it's good to talk about it as much as possible in the issues, so to not repeat long explanations here
[5:38:55 PM] <ErCiccione> they were usually on sunday iirc, yeah
[5:39:02 PM] <Keiji[m]> Good point. Thanks for the summary jberman!
[5:39:35 PM] <Keiji[m]> Maybe someone should ask to have a meeting tomorrow on GItHub and then mention on reddit as well
[5:40:02 PM] <ErCiccione> tomorrow is too soon. Maybe next sunday
[5:40:22 PM] <ErCiccione> i know sarang might have some research to share as well, so the meeting could be a good place for doing that
[5:40:56 PM] <wfaressuissia[m]> -dev and -lab meetings were independent previously, no ?
[5:41:02 PM] <Keiji[m]> Whatever people believe is best, depending on how time sensitive getting PRs is in
[5:41:19 PM] <Keiji[m]> Whatever people believe is best, depending on how time sensitive getting PRs in is
[5:41:57 PM] <ErCiccione> wfaressuissia: they still are afaik, but i don't think there are regular research meetings anymore
[5:43:05 PM] <tobtoht> hey, would like a dev meeting to discuss this as well. selsta mentioned the eta for the next release being in 2 weeks, 1 week ago, so if the meeting is planned for next week that may need to be delayed.
[5:45:05 PM] <jberman[m]> seems it would be easier to establish a meeting time directly on that PR/give time for people to see it
[5:45:26 PM] <jberman[m]> selsta can weigh in on release there
[5:45:51 PM] <Keiji[m]> Yes, I guess comment there and main stakeholders/developers can figure out best meeting time and stuff
[5:46:20 PM] <tobtoht> yep, feel free to propose a date/time on the github issue
[5:46:46 PM] <ErCiccione> meeting in two weeks is fine for me tobtoht 
[5:47:38 PM] <selsta> jberman[m]: luigi should be back monday, then we can do merges and prepare a release
[5:47:58 PM] <jberman[m]> ahh, got it ok
[5:48:28 PM] <Keiji[m]> Ok, any other things people want to discuss before we conclude the Community meeting?
[5:50:48 PM] <Keiji[m]> Sounds like no. Hope to see everyone in two weeks then! I'll post the logs soon to GitHub

# Action History
- Created by: carrington1859 | 2021-07-10T20:00:40+00:00
- Closed at: 2021-08-04T17:11:39+00:00
