---
title: 'Research meeting: 5 August 2019 @ 17:00 UTC'
source_url: https://github.com/monero-project/meta/issues/381
author: SarangNoether
assignees: []
labels: []
created_at: '2019-08-02T19:29:40+00:00'
updated_at: '2019-08-05T17:21:27+00:00'
type: issue
status: closed
closed_at: '2019-08-05T17:21:27+00:00'
---

# Original Description
Join in for the weekly Monero Research Lab meeting.

**When**: Monday, 5 August 2019 @ 17:00 UTC
**Where**: #monero-research-lab (freenode/matrix)

**Agenda**
1. Greetings

2. Roundtable
a. Sarang: RCT3 efficient verifier and fee support, more library updates, DEF CON prep
b. Surae
c. Others?

3. General questions

4. Action items
a. Sarang
b. Surae
c. Others?

# Discussion History
## SarangNoether | 2019-08-05T17:21:27+00:00
    [2019-08-05 12:58:18] <sarang> Let's go ahead and get started
    [2019-08-05 12:58:28] <sarang> suraeNoether says he is unavailable at this time due to an appointment
    [2019-08-05 12:58:37] <sarang> Agenda is here, where logs will be posted: https://github.com/monero-project/meta/issues/381
    [2019-08-05 12:59:06] <sarang> GREETINGS
    [2019-08-05 13:00:41] <needmonero90> hello
    [2019-08-05 13:01:14] <sarang> Seeing as it's a quiet day, I'll move right along to ROUNDTABLE
    [2019-08-05 13:01:42] <sarang> I finished work on an efficient RCT3 verifier that takes advantage of Bulletproof-style inner product scaling
    [2019-08-05 13:01:57] <sarang> and also added fee support, which the original paper didn't natively support
    [2019-08-05 13:02:21] <sarang> As well as many other assorted code library updates that I'd been meaning to get to over time
    [2019-08-05 13:02:45] <sarang> Finally, I've been preparing for my DEF CON talk and workshop, and also made a simple CTF puzzle
    [2019-08-05 13:02:53] <sarang> What have other folks been working on?
    [2019-08-05 13:03:30] <needmonero90> nothing of particular note here, though I'm curious what the latest on the different ring signature schemes is
    [2019-08-05 13:03:41] <sarang> Aha, that'll be the topic of my talk!
    [2019-08-05 13:03:53] <needmonero90> its been on my mind :D
    [2019-08-05 13:04:00] <sarang> Why's that?
    [2019-08-05 13:04:21] <needmonero90> transaction efficiency (both time and space) is one of the obstacles we need to overcome
    [2019-08-05 13:04:26] <sarang> Agreed
    [2019-08-05 13:04:27] <needmonero90> randomX seems fairly solid now
    [2019-08-05 13:04:34] <sarang> Of course, these proposals aren't really long-term scaling solutions
    [2019-08-05 13:04:44] <sarang> but they would provide welcome improvements
    [2019-08-05 13:05:36] <needmonero90> Is this meeting slow because of defcon? I assume so
    [2019-08-05 13:05:46] <sarang> There are still some questions on an RCT3 proof that are being investigated
    [2019-08-05 13:06:02] <sarang> and on the possibility of Omniring efficiency improvements
    [2019-08-05 13:06:13] <sarang> so the status of different tx protocols may change over time
    [2019-08-05 13:07:02] <sarang> On that note, an ACTION ITEM for me is to return to Omniring analysis
    [2019-08-05 13:07:23] <sarang> it's a more complex approach (computationally) than RCT3
    [2019-08-05 13:07:52] <sarang> and one of those things where the usual efficiency analysis sweeps some types of simple operations under the rug
    [2019-08-05 13:07:58] <sarang> but those operations can add up fast!
    [2019-08-05 13:09:55] <sarang> This weekend's village is of course another big action item :)
    [2019-08-05 13:12:39] → Common-Deer joined (~CommonDee@14-202-132-82.static.tpgi.com.au)
    [2019-08-05 13:12:53] <sarang> Slow day today :/
    [2019-08-05 13:13:09] <sarang> Well, in the interest of respecting everyone's time, are there any questions or other research of interest to share?
    [2019-08-05 13:13:38] ⇐ ferretinjapan quit (~ferretinj@unaffiliated/ferretinjapan): Quit: Leaving
    [2019-08-05 13:13:56] → ferretinjapan joined (ferretinja@gateway/vpn/privateinternetaccess/ferretinjapan)
    [2019-08-05 13:14:29] <sarang> (crickets)
    [2019-08-05 13:14:49] <JOhNKmus>  hey I happen to be here
    [2019-08-05 13:14:56] <sarang> hello
    [2019-08-05 13:15:02] <JOhNKmus> I was going to ask if there has been any helpful stuff from Lelantus?
    [2019-08-05 13:15:34] <sarang> The authors have been working on a modified prover that offloads some of the proving complexity to the verifier (and pays a bit in size)
    [2019-08-05 13:15:58] <sarang> and the goal is still to remove the tracing that's present (and necessitates self-spend operations)
    [2019-08-05 13:16:07] <sarang> But AFAIK there have been no solutions as of yet
    [2019-08-05 13:16:20] ⇐ Common_Deer quit (~CommonDee@14-202-132-82.static.tpgi.com.au): Ping timeout: 272 seconds
    [2019-08-05 13:16:30] <JOhNKmus> Ah okay, cool.
    [2019-08-05 13:16:52] <sarang> I suspect that removing that problem would require big architectural changes to the whole construction :/
    [2019-08-05 13:16:59] <sarang> but I hope that I am proven wrong :)
    [2019-08-05 13:17:39] <sarang> Well, since it's a quiet day I suppose we can adjourn the meeting quite early
    [2019-08-05 13:17:55] <sarang> Hopefully livestreaming will be happening at the DEF CON village so everyone can see the talks
    [2019-08-05 13:18:24] <sarang> I'll post my slides to github after my talk, since they have (IMO) some nice and simple information comparing tx protocols
    [2019-08-05 13:18:40] <sarang> Thanks to everyone for attending today!


# Action History
- Created by: SarangNoether | 2019-08-02T19:29:40+00:00
- Closed at: 2019-08-05T17:21:27+00:00
