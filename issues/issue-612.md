---
title: 'Community Workgroup Meeting: 02 October 2021 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/612
author: carrington1859
assignees: []
labels: []
created_at: '2021-09-21T09:09:45+00:00'
updated_at: '2021-10-02T19:33:03+00:00'
type: issue
status: closed
closed_at: '2021-10-02T19:33:03+00:00'
---

# Original Description
https://forum.monero.space/d/111-community-workgroup-meeting-02-october-2021-1800-utc

Location: [Libera.chat, #monero-community](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-community:monero.social?via=matrix.org&via=monero.social)

Time
18:00 UTC [Check your timezone](https://www.timeanddate.com/worldclock/converter.html?iso=20211002T180000&p1=1440)

Moderator: ?

Proposed Meeting Items:

Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

1) Introduction
2) Greetings
3) Community highlights
4) CCS updates
a. [Decentralizing Molly.im to support Monero payments](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/252)
b. [Italian Mastering Monero](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/251)
c. [OSPEAD - Fortifying Monero Against Statistical Attack](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/255) - [Reddit discussion](https://www.reddit.com/r/Monero/comments/py8ub3/ccs_proposal_ospead_fortifying_monero_against/)
d. [Seraphis PoC](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/256) - [Reddit discussion](https://www.reddit.com/r/Monero/comments/pzbytc/seraphis_a_promising_nextgen_transaction_protocol/)
e. [XMR<>BTC Atomic Swaps Desktop GUI
](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/257) - [Reddit discussion](https://www.reddit.com/r/Monero/comments/pzizmv/xmrbtc_atomic_swaps_desktop_gui_funding_proposal/)
5) Workgroup reports
a. Daemon/CLI workgroup
b. Localization workgroup
c. GUI workgroup
d. Outreach workgroup
e. Events workgroup
f. Website workgroup
g. Policy workgroup
6) Open ideas time
7) Confirm next meeting date/time

[Previous meeting including logs](https://github.com/monero-project/meta/issues/609)

Meeting logs will be posted here afterwards.

# Discussion History
## valldrac | 2021-09-28T20:29:59+00:00
CCS proposal: [Decentralizing Molly.im to support Monero payments](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/252)

## Keiji-C | 2021-09-29T16:40:38+00:00
I can moderate for this meeting

## carrington1859 | 2021-10-02T19:33:03+00:00
18:01:12 -Keiji[m]> Let's begin the Monero Community Meeting
18:01:30 -selsta> lh1008[m]: how much RAM?
18:01:39 -Keiji[m]> 1. Greetings
18:02:28 -sgp_old> hello
18:03:22 -Rucknium[m]> Present :)
18:03:22 -carrington[m]> Hey
18:03:23 -BusyBoredom[m]> Hey
18:03:50 -gingeropolous> yo
18:03:55 -ajs_[m]> hi
18:04:26 -lh1008[m]> selsta: Total 2040836
18:04:35 -lh1008[m]> Hey everyone
18:04:47 -Keiji[m]> 2. Community Highlights
18:05:17 -Keiji[m]> Are there any pieces of Monero-news from the previous 2 weeks which people would like to discuss?
18:06:28 -Halver[m]> Hi
18:06:32 -Keiji[m]> Ok, we can move to the next thing
18:06:33 -carrington[m]> Monero Observer put out a good summary of events in September
18:06:33 -carrington[m]> https://www.monero.observer/monero-observer-blitz-september-2021/
18:06:54 -sgp_old> yeah I really like monero observer
18:07:32 -carrington[m]> Hopefully it will be consistent and the author can gain enough trust for a second proposal
18:08:02 -carrington[m]> I'll save some other issues for after CCS discussions
18:08:48 -Keiji[m]> I would like to jump to 5. Workgroup Reports. Since Workgroup Reports is pretty quick I think, and we have a lot of CCS updates which are maybe long
18:09:18 -Keiji[m]> Any workgroup members want to take the mic and we can triage if there are multiple at the same time?
18:10:21 -sgp_old> sure, first on the community workgroup itself
18:10:29 -sgp_old> I bridged the MCW YT to Odysee
18:10:34 -lh1008[m]> From the Monero Outreach, we're currently moving all the repository to GitLab.
18:10:55 -carrington[m]> lh1008[m]: Self hosted?
18:11:17 -lh1008[m]> carrington[m]: No, not yet, we're using GitLab's services. 
18:11:47 -ajs_[m]> events... 38C3 cancelled
18:12:09 -bevanoff[m]> lh1008: why switch? Just curious
18:12:53 -sgp_old> monero space... we had a monero meet
18:13:28 -carrington[m]> It is a shame that 38C3 is out. It would be good to have some -event meetings to get a clearer picture of things for 2022
18:14:12 -xmrscott[m]> Next DEF CON at least is guranteed to happen
18:14:39 -xmrscott[m]> Planning would presumably start in April
18:15:02 -lh1008[m]> bevanoff[m]: We're starting clean. We never actually used MO GitHub's repository, only for translations.
18:15:21 -carrington[m]> Shall we move onto the CCS?
18:15:26 -bevanoff[m]> lh1008: oh nice 👍
18:15:36 -Keiji[m]> Yes, good suggestion carrington
18:15:53 -Keiji[m]> Let's move to 4. CCS Updates
18:16:10 -Keiji[m]> First update itme is this: https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/252
18:16:39 -carrington[m]> It seems valldrac  is here to answer questions
18:17:06 -valldrac[m]> Yes, I'm here. If you have any question 😅
18:17:34 -sgp_old> I see this CCS as only vaguely beneficial to monero to be 100% honest
18:18:20 -sgp_old> worthy initiative
18:18:38 -selsta> it should be considered that this is a project with huge scope, while monero integration on android could be funded through the CCS theoretically the project would need to find funding elsewhere too
18:19:08 -carrington[m]> I think it is a cool idea to integrate XMR natively into a messenger. If I was a donor, I would like a technical specification of how the Monero side of things will work as a milestone
18:19:41 -carrington[m]> Yes it seems the backend described in the proposal would need ongoing funding
18:21:03 -valldrac[m]> carrington[m]: That's the idea. We're now requesting Monero funding for the first stage. More stages will come, but once we bootstrap the project we will look for more funding alternatives
18:21:15 -selsta> and alternatives have large premine / dev tax for funding (signal / session / ...), monero can't compete there realistically
18:21:33 -selsta> it's just something to keep in mind
18:23:00 -valldrac[m]> carrington[m]: It will be a full wallet integrated in the app, using the native C++ library
18:24:42 -carrington[m]> I think it is a good proposal which is at least beneficial to XMR, but I'm not sure it will achieve it's funding goal within a short while
18:25:36 -carrington[m]> No one seems to have any strong objections to the idea? Other than that the scope is very large?
18:25:58 -valldrac[m]> selsta: Agree. I don't think we can compete with them in the mid-term. But Molly will support both backends in the meantime, Signal network and Molly network, so we can benefit of Signal larger user base
18:26:50 -netrik182> Would monero be available even if using the signal network?
18:27:05 * netrik182 is late, sorry
18:27:27 -msvb-lab> Me too.
18:27:47 -valldrac[m]> netrik182: Yes, but with a slightly different UX. Check the proposal
18:28:33 -Keiji[m]> Alright, I think that's about it for questions. Thanks valldrac for being available. Let's move to the next CCS
18:28:44 -ajs_[m]> don't like the idea of possible association of phone numbers to wallet addresses
18:29:06 -carrington[m]> I am curious how the "data at rest" techniques used by Molly compare to other mobile XMR wallets key storage
18:30:31 -carrington[m]> ajs_ my understanding is the separate "Molly network" would not require phone numbers
18:30:46 -sgp_old> that's super far away though fwiw
18:31:38 -valldrac[m]> carrington: A bit long to discuss here. See https://github.com/mollyim/mollyim-android/wiki/Data-Encryption-At-Rest. Also consider we use a RAM wiper that fill with random data the free RAM of the device when the app locks
18:32:30 -carrington[m]> I will leave some comments in the gitlab after the meeting
18:32:36 -Keiji[m]> We have about 30 minutes left and 4 CCS left to discuss so let's move to the Italian Mastering Monero CCS: https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/251
18:33:00 -sgp_old> MMe1 is way too old to be translated frankly
18:33:21 -carrington[m]> Yeah I thought there was a second edition in the works
18:33:24 -Keiji[m]> Only comment I have is maybe serhack can comment on 2nd Edition ETA?
18:33:32 -sgp_old> I've been pushing serhack on that ,I really am
18:33:48 -carrington[m]> I think the proposer should contact the author
18:34:34 -carrington[m]> I have left a comment regarding the second edition and I will try and follow up on this
18:34:54 -Keiji[m]> Thanks. Let's move to the next item
18:35:17 -Keiji[m]> We have about 25 minutes left so let's limit discussion to 8 min for each
18:35:48 -Keiji[m]> OSPEAD: https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/255
18:36:03 -Rucknium[m]> There have been a ton of questions about OSPEAD. I collect some links to my responses here, and I take questions I suppose:
18:36:07 -Rucknium[m]> https://www.reddit.com/r/xmrtrader/comments/pzsd27/developer_of_ospead_here_ama/
18:36:13 -mj-xmr[m]> While on CCS', I have sth. to add out of context maybe: I had too little time in September to work on the daily basis (reviews, etc.), so I will ask for the payment not before 15 Oct. or even at the end of October, if my schedule stays so full. I plan to make it up.
18:36:23 -Rucknium[m]> Here's the consensus, as far as I see it:
18:37:08 -carrington[m]> mj-xmr[m]: Best to leave a comment on the gitlab and contact Luigi, seems reasonable
18:37:16 -Rucknium[m]> In general, work on researching an improved the mixin selection algorithm should occur. Most people think I am able to do it. I am willing to do it. The exact form of that research seems to be up for debate
18:38:24 -Rucknium[m]> Any questions here for me?
18:38:32 -carrington[m]> Obviously the CCS proposal is lacking an XMR amount so it can't be moved as is
18:38:56 -luigi1111w> mj-xmr[m] if you fall behind just update when you catch up pretty much
18:39:17 -mj-xmr[m]> Sure. I'll decorate it with my usual report.
18:39:30 -Rucknium[m]> Right. That was deliberate. I mean, it's the XMR equivalent of 100USD/hour * 400 hours
18:39:39 -carrington[m]> I think perhaps the outlook of this proposal would depends on what happens with people reviewing the vulnerability report
18:39:48 -Rucknium[m]> I didn;ty put an XMR amount so it couldnt be merged prematurely
18:40:19 -luigi1111w> that will not happen
18:40:50 -carrington[m]> There should at least be some peer review of the premise (possibly in public) before you start any work IMO
18:40:56 -Rucknium[m]> luigi1111w: Ok. Yeah, in my next (first) revision, I will put an XMR amount, plus many other edits
18:41:36 -Rucknium[m]> carrington: There has been peer review. There is additional peer review ongoing. What type of peer review, specifically, would you like to see?
18:42:00 -selsta> luigi1111w: are you going to review the vrp report and give your feedback?
18:42:01 -Rucknium[m]> carrington: In other words, what do you mean by needs "peer review"
18:42:13 -carrington[m]> I know you are waiting for some peer review so there isn't much to discuss things until others have gotten back to you
18:42:41 -luigi1111w> I'm reading it now, unsure if I'll have useful feedback yet
18:42:49 -Rucknium[m]> carrington: Ok. we can wait on more peer review. But I'm wondering what #community thinks would be satisfactory peer review. So that I can meet that standard
18:43:20 -sgp_old> well, even so I think the CCS can be safely merged
18:43:21 -Rucknium[m]> luigi1111w: Thank you for your review
18:43:39 -Rucknium[m]> Er, well, reading it. Not sure if you are "reviewing" it in a formal sense
18:44:26 -Keiji[m]> While the discussion is lively, to make sure other items can be discussed, let's discuss Seraphis PoC until :52
18:44:26 -carrington[m]> My other comment is that it might be a good idea to contact the Noether's or read old MRL logs to find out how the Moser paper recommendations were implemented
18:44:29 -luigi1111w> certainly not that
18:44:35 -Keiji[m]> https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/256
18:45:12 -Keiji[m]> We can move back to the Rucknuim's CCS if there's not much discussion on the other 2 CCS
18:46:07 -Keiji[m]> Any questions people believe that should be voiced on Seraphis GitLab comments?
18:47:06 -carrington[m]> It is critical to get a PoC of Seraphis, so it looks good to me
18:47:15 -carrington[m]> No XMR amount there either yet
18:47:24 -netrik182> +1
18:47:43 -Rucknium[m]> carrington[m]: carrington: Ditto. Strong support from me.
18:48:09 -Keiji[m]> Ok, sounds like no questions or objections. Let's move to the next CCS
18:48:28 -Keiji[m]> Atomic Swap for Monero and Bitcion GUI: https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/257
18:49:16 -carrington[m]> There was a similar thing called Swapfe announced on reddit 2 days ago
18:49:48 -carrington[m]> I haven't gone digging into the differences but I will drop a comment on the gitlab so the author can explain any difference
18:50:28 -carrington[m]> https://www.reddit.com/r/Monero/comments/pyxpve/swapfe_an_atomic_swap_user_interface_for_bitcoin/
18:51:24 -Keiji[m]> Any objections or questions people believe should be asked?
18:51:38 -carrington[m]> The proposal was only posted yesterday so we can circle back to this. People on gitlab seem enthusiastic
18:51:39 -BusyBoredom[m]> I like the idea of competing UIs for atomic swaps, seems like there's rough edges to be sorted out and a shotgun approach for now might be a good thing for now. So I'm a fan of this CCS
18:52:46 -netrik182> The one from reddit seems to add a fee on each swap if I'm not mistaken 
18:52:59 -netrik182> But didn't look deep enough yet
18:54:15 -Keiji[m]> Ok, I think we can move back to OSPEAD discussion then
18:55:01 -Keiji[m]> Last question on that was "But I'm wondering what #community thinks would be satisfactory peer review."
18:55:24 -Rucknium[m]> carrington:  "read old MRL logs to find out how the Moser paper recommendations were implemented" Yeah, that makes sense. I will put it on the TODO list
18:56:10 -Rucknium[m]> As far as the Noethers, I personally am not in a good position to contact them. If anyone wants to establish contact between me and the Noethers, go ahead. I'm best to reach via DM here on Matrix
18:56:50 -carrington[m]> Maybe rehrar  could help out here
18:57:16 -carrington[m]> I think he uses Diego Salazar  actually
18:58:12 -Rucknium[m]> "But I'm wondering what #community thinks would be satisfactory peer review."
18:58:12 -Rucknium[m]> ^ Any comments or guidance?
18:58:49 -carrington[m]> I think just a few more voices coming out over the next week will suffice, personally
18:59:24 -carrington[m]> You said in another channel that you are waiting for a few reviews, so I'll wait for those before expressing any further opinion
18:59:36 -Rucknium[m]> carrington: Ok. I think that is pretty much guaranteed to happen. The document is 28 pages long, though, with plenty of math, charts, tables, code. So yeah, it takes time.
19:00:28 -carrington[m]> Shall we agree quickly to a meeting here in two weeks? I would like to discuss another issue of people are sticking around after the hour
19:00:45 -Keiji[m]> We're at the end of the hour so we can formally close. Conversations can of course continue on anything discussed in the meeting slot. Or your item carrington
19:00:51 -Keiji[m]> Yes, let's agree for meeting in two weeks
19:01:52 -carrington[m]> Basically, it seems these meeting are mostly a "CCS meeting" and I think we should reflect on the overall situation with new platforms for XMR funding popping up everywhere
19:02:04 -luigi1111w> Keiji[m] thanks for running
19:02:10 -carrington[m]> There is 
19:02:10 -carrington[m]> bounties.Monero.social
19:02:37 -carrington[m]> This launched recently and is also administered by Core
19:02:48 -msvb-lab> Some like Monerujo have their own funding host as well, funding.monerujo.app.
19:03:36 -carrington[m]> There is also things like Haveno's bounties, and several projects based off plowsof 's wishlist idea
19:03:44 -Rucknium[m]> msvb-lab: That's plowsof  's platform, I believe. Used by monerujo
19:03:57 -msvb-lab> I think you are correct Rucknium[m].
19:04:03 -valldrac[m]> Thanks Keiji for running it. Not easy to do today with such tight schedule
19:04:08 -carrington[m]> also MAGIC grants
19:04:15 -msvb-lab> Good meeting, yes thanks Keiji[m].
19:04:15 -valldrac[m]> I'll be around here for a while if there're remaining questions about the Molly CCS proposal
19:05:32 -carrington[m]> I think at risk of fragmentation of donors attention, there should be wider promotion of all of these platforms together
19:06:00 -carrington[m]> I'm not sure how to achieve that but I'm interested in other's opinions
19:06:30 -plowsof[m]> maybe some kind of central place where they are all listed, e.g. https://plowsof.github.io/monerodevs/
19:08:29 -Keiji[m]> That should work I think

# Action History
- Created by: carrington1859 | 2021-09-21T09:09:45+00:00
- Closed at: 2021-10-02T19:33:03+00:00
