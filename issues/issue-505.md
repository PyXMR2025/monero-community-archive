---
title: 'Research meeting: 16 September 2020 @ 17:00 UTC'
source_url: https://github.com/monero-project/meta/issues/505
author: SarangNoether
assignees: []
labels: []
created_at: '2020-09-03T18:33:09+00:00'
updated_at: '2020-09-24T12:36:22+00:00'
type: issue
status: closed
closed_at: '2020-09-21T00:25:53+00:00'
---

# Original Description
Join in for the weekly Monero Research Lab meeting.

**When**: Wednesday, 16 September 2020 @ 17:00 UTC
**Where**: #monero-research-lab (freenode/matrix)

**Agenda**
1. Greetings

2. Roundtable

3. Questions

4. Action items

# Discussion History
## SarangNoether | 2020-09-08T20:42:45+00:00
The meeting originally scheduled for 9 September 2020 is cancelled.

## SarangNoether | 2020-09-24T12:36:21+00:00
    [2020-09-16 13:00:32] <sarang> Let's get started!
    [2020-09-16 13:00:36] <sarang> First, greetings
    [2020-09-16 13:00:38] <sarang> hello
    [2020-09-16 13:00:43] <hyc> hey
    [2020-09-16 13:00:51] <h4sh3d[m]> Hello
    [2020-09-16 13:01:10] <Isthmus> Holla
    [2020-09-16 13:02:38] ⇐ nssy quit (~nssy@197.237.91.81): Remote host closed the connection
    [2020-09-16 13:03:00] <sarang> On to the roundtable, where anyone is welcome to share research of interest
    [2020-09-16 13:03:02] → nssy joined (~nssy@197.237.91.81)
    [2020-09-16 13:03:04] <sarang> Who wishes to begin?
    [2020-09-16 13:03:17] <UkoeHB_> hi
    [2020-09-16 13:03:57] <UkoeHB_> not research, but it seems the hardfork protocol changes have been finalized
    [2020-09-16 13:04:23] <sarang> Indeed!
    [2020-09-16 13:04:41] <sarang> Binaries are set to be released, and the protocol upgrade will happen around October 17
    [2020-09-16 13:04:55] <UkoeHB_> CLSAG, fixed block rewards, and chain-data-based  UTC timestamp timelocks
    [2020-09-16 13:05:01] <sarang> This gives users and other ecosystem participants a month to update
    [2020-09-16 13:05:03] <UkoeHB_> are the changes I know about
    [2020-09-16 13:05:11] <hyc> on that note, I've been running teh new stuff on testnet for about 2 weeks
    [2020-09-16 13:05:19] <sarang> Anything of note hyc?
    [2020-09-16 13:05:26] <hyc> nope, decidedly boring
    [2020-09-16 13:05:31] <sarang> Excellent
    [2020-09-16 13:05:43] <sarang> Ledger and Trezor teams are ready as well
    [2020-09-16 13:06:02] <sarang> So users of those devices should see a seamless transition, provided they keep their devices updated
    [2020-09-16 13:06:16] <sarang> Thanks to everyone who participated in the upgrade process
    [2020-09-16 13:06:30] <sarang> CLSAG was a particularly long road to walk...
    [2020-09-16 13:07:11] <h4sh3d[m]> What's the best resource to see what changed in the transaction serialization, regarding the hardfork (directly the code I imagine)?
    [2020-09-16 13:07:39] <h4sh3d[m]> So I can update the Rust library and include the new format
    [2020-09-16 13:08:52] <Isthmus> Ooh I didn't know that we had a Rustnero. Where does that repo live?
    [2020-09-16 13:09:26] <sarang> Good question h4sh3d[m]... I'm not sure there's something easier than examining the code, or perhaps something like the onion explorer source
    [2020-09-16 13:09:28] <h4sh3d[m]> You mean this: https://github.com/monero-rs/monero-rs
    [2020-09-16 13:09:52] <Isthmus> Sweet, ty
    [2020-09-16 13:10:06] <h4sh3d[m]> sarang: ok, I'll check the code anyway then
    [2020-09-16 13:10:38] <sarang> Might also be worth pinging moneromooo as well
    [2020-09-16 13:10:41] <sarang> (ping)
    [2020-09-16 13:11:10] <sarang> I can get you the serialization for CLSAG signatures specifically, if that's useful
    [2020-09-16 13:12:06] <h4sh3d[m]> Yes, it is useful
    [2020-09-16 13:12:27] <sarang> https://github.com/SarangNoether/monero/blob/master/src/ringct/rctTypes.h contains the signature structure etc. for CLSAG
    [2020-09-16 13:12:52] <h4sh3d[m]> Thanks
    [2020-09-16 13:12:54] <moneromooo> Oh hi
    [2020-09-16 13:12:56] — moneromooo reads back
    [2020-09-16 13:13:01] <sarang> Er, that's my branch, so it's probably not fully up to date with the project master branch
    [2020-09-16 13:13:10] <sarang> whoops
    [2020-09-16 13:14:04] <moneromooo> Data format changes ? I can look that up, gimme a few minutes.
    [2020-09-16 13:14:10] <h4sh3d[m]> At least I have the right file with this
    [2020-09-16 13:14:12] <sarang> :D
    [2020-09-16 13:14:33] <sarang> Was there anything else that should be discussed related to the upgrade, now that it's been brought up?
    [2020-09-16 13:15:50] <moneromooo> Oh right, what sarang pointed to actually :)
    [2020-09-16 13:15:54] <sarang> :D
    [2020-09-16 13:16:32] <sarang> Yeah, probably use https://github.com/monero-project/monero/blob/master/src/ringct/rctTypes.h just in case
    [2020-09-16 13:16:44] <sarang> not my clone of it, which is probably a bit old
    [2020-09-16 13:16:54] <moneromooo> and the rct type is 5 for those. 4 for MLSAG.
    [2020-09-16 13:17:04] <sarang> Does anyone else wish to share research topics of interest?
    [2020-09-16 13:17:38] <Isthmus> Quantum doc nearing completion, draft here: https://www.overleaf.com/project/5f4fc9e599cecd00017c5fe5
    [2020-09-16 13:17:47] <sarang> Great!
    [2020-09-16 13:18:03] <sarang> Anything of note to which we should pay particular attention?
    [2020-09-16 13:18:13] <sarang> That link isn't for viewing
    [2020-09-16 13:18:21] <sarang> You'll need to access the read link from the share menu
    [2020-09-16 13:18:30] <sarang> It's different from the project URL
    [2020-09-16 13:20:05] <Isthmus> https://www.overleaf.com/read/sqpqktvnvjkv
    [2020-09-16 13:20:36] <sarang> success
    [2020-09-16 13:21:02] <sarang> Any big recent changes of note?
    [2020-09-16 13:21:12] <sarang> <3 line numbers
    [2020-09-16 13:22:53] <h4sh3d[m]> I like 766 :D
    [2020-09-16 13:23:44] <Isthmus> Added the sections about pq-crypto and mitigations
    [2020-09-16 13:24:18] <sarang> No Oxford comma on L766?
    [2020-09-16 13:24:20] <sarang> tsk tsk
    [2020-09-16 13:25:41] <sarang> I had pointed out some issues to suraeNoether a while back, but they appear to have been addressed at first glance
    [2020-09-16 13:26:18] <sarang> Namely about having access to multiple outputs, which included some incorrect math
    [2020-09-16 13:27:19] <sarang> Isthmus: is there anything you'd like from this channel related to this new draft?
    [2020-09-16 13:27:30] <sarang> Particular review, etc.?
    [2020-09-16 13:31:50] <zkao> hello guys
    [2020-09-16 13:31:59] <sarang> Hi zkao
    [2020-09-16 13:32:04] <sarang> OK, well I suppose we can move on!
    [2020-09-16 13:32:07] <zkao> since we're on research paper review topic, we'd like to get the atomic swap paper more widely scrutinized, vtnerd did a good job so far, so it would be great if more eyes look into it carefully and drop questions, could some people in here give more feedback?
    [2020-09-16 13:32:26] <sarang> Can you summarize the comments from vtnerd?
    [2020-09-16 13:32:55] * jwinterm → j-dawg
    [2020-09-16 13:33:22] <zkao> its public, on the comments of: https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/168#notes
    [2020-09-16 13:33:45] <h4sh3d[m]> and he wrote a little summary here https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/168#note_10278
    [2020-09-16 13:33:53] <zkao> he picked up on all the differences btwn traditional atomic swaps and h4sh3ds assymetrical one
    [2020-09-16 13:34:27] <sarang> Ah, there's more discussion there since I checked last; excellent
    [2020-09-16 13:34:40] <sarang> Thanks for linking this
    [2020-09-16 13:34:58] * j-dawg → jwinterm
    [2020-09-16 13:35:18] <zkao> his process of reading it and analysing it, made me feel like almost nobody tried to understand it yet
    [2020-09-16 13:35:39] <zkao> because other people should have spelled some of that stuff before
    [2020-09-16 13:35:47] <kenshamir[m]> <sarang "kenshamir: if you're able to bre"> Battery died on phone, I did think of something where we can use it to solve the DL of G with respects to H. But I think I might just have misunderstood the assumption
    [2020-09-16 13:35:58] <zkao> except a few experts
    [2020-09-16 13:36:35] <kenshamir[m]> > <@freenode_sarang:matrix.org> kenshamir: if you're able to break the assumption, or reduce it to a known assumption, I would be unbelievably happy
    [2020-09-16 13:36:36] <kenshamir[m]>  * Battery died on phone, I did think of something where we can use it to solve the DL of G with respects to H. But I think I might just have misunderstood the assumption, or my maths is off
    [2020-09-16 13:36:48] ⇐ xiphon quit (~xiphon@45.43.14.47): Ping timeout: 260 seconds
    [2020-09-16 13:37:12] <kenshamir[m]>  * Battery died on phone, I did think of something where we can use it to solve the DL of G with respects to H. But I think I might just have misunderstood the assumption, or my maths is off.. Ahh meeting in progress, can wait for it to end.
    [2020-09-16 13:37:21] <sarang> zkao: has the latest version of the preprint been posted to the IACR archive?
    [2020-09-16 13:37:40] <h4sh3d[m]> Yes
    [2020-09-16 13:37:44] <sarang> great
    [2020-09-16 13:37:50] <h4sh3d[m]> it's submitted, not yet published
    [2020-09-16 13:38:20] <h4sh3d[m]> I'll past a link as soon as it gets on the preprint server
    [2020-09-16 13:38:35] <sarang> When was it submitted?
    [2020-09-16 13:38:45] <sarang> They're usually pretty quick
    [2020-09-16 13:38:46] <h4sh3d[m]> today :D
    [2020-09-16 13:38:48] <sarang> Ah ok!
    [2020-09-16 13:39:13] <h4sh3d[m]> pretty quick < some days/weeks?
    [2020-09-16 13:39:14] <sarang> kenshamir[m]: I definitely want to know about this after the meeting :)
    [2020-09-16 13:39:30] <sarang> h4sh3d[m]: yeah, maybe delayed a few days, but generally not too bad
    [2020-09-16 13:39:51] <sarang> They're not as on top of things as arXiv for daily postings, it seems
    [2020-09-16 13:41:32] <zkao> i guess you should drop it in bitcoin-wizards after its in the prepint server
    [2020-09-16 13:41:50] <h4sh3d[m]> seems good yes
    [2020-09-16 13:41:52] <sarang> Are you not in that channel?
    [2020-09-16 13:42:00] <sarang> I can certainly link it there if you wish
    [2020-09-16 13:42:28] <h4sh3d[m]> I am in the channel, yes please! :D
    [2020-09-16 13:42:49] <sarang> OK :)
    [2020-09-16 13:42:58] <sarang> You can of course feel free to post it there if you prefer!
    [2020-09-16 13:43:08] <sarang> I don't have any particular sway in that channel
    [2020-09-16 13:43:51] <sarang> I have a few things to share
    [2020-09-16 13:44:11] <sarang> I did some review with suraeNoether on the post-quantum security draft
    [2020-09-16 13:44:24] <sarang> Worked on the Arcturus security model to make it more clear after its last review
    [2020-09-16 13:44:48] <sarang> Produced BP+ and BP Python updates to demonstrate additional hidden data embedding
    [2020-09-16 13:44:51] <Isthmus> Sorry, lost internet a few. Yea, Sarang had a lot of very helpful comments
    [2020-09-16 13:44:58] <sarang> Gave a presentation to a Chicago bitcoin group
    [2020-09-16 13:45:12] <sarang> And am participating in this week's ongoing ESORICS conference
    [2020-09-16 13:45:39] <sarang> Additionally, I've been asked to give an MCC talk soon relating to privacy
    [2020-09-16 13:45:53] <sarang> I think they presumed bitcoin-related privacy, but I think that's not useful
    [2020-09-16 13:46:42] → xiphon joined (~xiphon@45.43.14.47)
    [2020-09-16 13:48:32] <sarang> I welcome suggestions on particular topics you think might be of most use to that audience
    [2020-09-16 13:49:42] <sarang> Anyway, did anyone else wish to share research topics?
    [2020-09-16 13:49:48] <sarang> We're approaching the end of our scheduled hour
    [2020-09-16 13:50:41] <sarang> I do wish to note that I will not be requesting community funding after the end of this month
    [2020-09-16 13:50:53] <sarang> So any research meetings will need to be coordinated by someone else, if it's desired that they continue
    [2020-09-16 13:51:50] <zkao> the transaction graph of bitcoin is on the clear, even if scripts get hidden with taproot, so u could push the agenda that it is not good enough, on that conference
    [2020-09-16 13:51:56] <UkoeHB_> what will you be up next month, if I may ask?
    [2020-09-16 13:52:27] <sarang> I have yet to finalize anything specific
    [2020-09-16 13:53:50] <sarang> OK, well, I suppose we can adjourn then
    [2020-09-16 13:53:58] <sarang> Thanks to everyone for joining today

# Action History
- Created by: SarangNoether | 2020-09-03T18:33:09+00:00
- Closed at: 2020-09-21T00:25:53+00:00
