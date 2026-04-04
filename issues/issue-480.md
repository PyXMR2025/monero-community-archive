---
title: 'Research meeting: 1 July 2020 @ 17:00 UTC'
source_url: https://github.com/monero-project/meta/issues/480
author: SarangNoether
assignees: []
labels: []
created_at: '2020-07-01T15:01:13+00:00'
updated_at: '2020-07-01T17:32:31+00:00'
type: issue
status: closed
closed_at: '2020-07-01T17:32:31+00:00'
---

# Original Description
Join in for the weekly Monero Research Lab meeting.

**When**: Wednesday, 1 July 2020 @ 17:00 UTC
**Where**: #monero-research-lab (freenode/matrix)

**Agenda**
1. Greetings

2. Roundtable

3. Questions

4. Action items

# Discussion History
## SarangNoether | 2020-07-01T17:32:31+00:00
    [2020-07-01 12:59:30] <sarang> OK, let's get started with the meeting!
    [2020-07-01 12:59:38] <sarang> As always, GREETINGS
    [2020-07-01 12:59:41] <sarang> hello
    [2020-07-01 13:00:26] <jwinterm> o/
    [2020-07-01 13:00:26] <ArticMine> Hi
    [2020-07-01 13:01:25] <Isthmus> Salutations
    [2020-07-01 13:02:55] <sarang> On to ROUNDTABLE, where anyone is welcome to share research of interest
    [2020-07-01 13:03:23] <sarang> It was a fairly quiet week for me; I haven't been feeling well, and didn't get as much done as I had hoped unfortunately :/
    [2020-07-01 13:03:56] <sarang> That being said, I've been actively working on finalizing all the CLSAG preprint changes that resulted from the auditors' suggestions
    [2020-07-01 13:04:14] <sarang> One piece of that, the linkable anonymity proof, has proven (pun intended) much more subtle than I had expected
    [2020-07-01 13:04:29] <sarang> But now I'm quite confident that a new proof is much better
    [2020-07-01 13:05:54] <sarang> The original proof didn't go into enough detail, and on review there were some things related to oracle access that I didn't like
    [2020-07-01 13:06:17] <sarang> Does anyone have comments or questions relating to this?
    [2020-07-01 13:06:33] <sarang> Once these changes are completed, I'll post a revision to the preprint on IACR
    [2020-07-01 13:08:45] <sarang> OK, does anyone else have research topics they'd like to discuss?
    [2020-07-01 13:10:24] <Isthmus> Two articles coming out of the quantum research soon. One is just a background recap from the proposal, but the other is an in-depth discussion about the algorithms of interest, which I think y'all will enjoy. Drafts premature to share, but expected by next week.
    [2020-07-01 13:10:52] <sarang> Nice! Any big takeaways?
    [2020-07-01 13:11:29] <Isthmus> Haha it's like a 9-page article right now, let me distill it down and get back to you later xD
    [2020-07-01 13:12:00] <Isthmus> That's all from me. Need to hop into another meeting soon, so apologies if I disappear
    [2020-07-01 13:12:10] <sarang> OK, thanks Isthmus
    [2020-07-01 13:12:20] <sarang> I shall eagerly await the articles
    [2020-07-01 13:12:52] <sarang> Does anyone else wish to share research?
    [2020-07-01 13:13:03] ⇐ asymptotically quit (~asymptoti@gateway/tor-sasl/asymptotically): Ping timeout: 240 seconds
    [2020-07-01 13:13:36] <moneromooo> An old thing, but I recently got a link to https://github.com/zawy12/difficulty-algorithms/issues/30 and I thought the difficulty adjustment algorithm might be a good one to go through if anyone statistics minded wanted a project.
    [2020-07-01 13:14:02] <moneromooo> It does feel like a "danger, don't touch until it breaks" subject though :)
    [2020-07-01 13:14:21] <sarang> Heh
    [2020-07-01 13:14:22] <sgp_> Hello, I'm half paying attention today
    [2020-07-01 13:14:22] → asymptotically joined (~asymptoti@gateway/tor-sasl/asymptotically)
    [2020-07-01 13:14:33] <sarang> Good point that it would be useful to revisit
    [2020-07-01 13:14:58] <sarang> sgp_: did you have anything you wished to discuss?
    [2020-07-01 13:15:10] <Isthmus> @mooo I'm intrigued
    [2020-07-01 13:15:47] ⇐ v1docq48 quit (~v1docq47@81.1.228.168): *.net *.split
    [2020-07-01 13:15:47] ⇐ TrasherDK quit (~TrasherDK@cm-171-100-239-63.revip10.asianet.co.th): *.net *.split
    [2020-07-01 13:15:48] ⇐ nickler quit (~nickler@static.219.205.69.159.clients.your-server.de): *.net *.split
    [2020-07-01 13:15:48] ⇐ null__ quit (~null@unaffiliated/null/x-1905186): *.net *.split
    [2020-07-01 13:15:48] ⇐ Blackwolfsa4 quit (~Blackwolf@195.159.29.126): *.net *.split
    [2020-07-01 13:16:05] <moneromooo> That was from the tari channel fwiw. They're looking at it now.
    [2020-07-01 13:16:30] <Isthmus> "Timestamps on newly-seen blocks are allowed to be in the past up to network delays. This prevents reorgs. But POW allows indefinite delays which allows reorgs of indefinite length" < something about that feels funny to me
    [2020-07-01 13:16:59] <Isthmus> I'll ponder on it
    [2020-07-01 13:17:06] <sgp_> sarang: nope, just bumping coinbase rings as always I suppose for comment
    [2020-07-01 13:17:27] <ArticMine> So am I
    [2020-07-01 13:18:11] → null__ joined (null@unaffiliated/null/x-1905186)
    [2020-07-01 13:18:25] → Blackwolfsa4 joined (~Blackwolf@195.159.29.126)
    [2020-07-01 13:18:35] → v1docq48 joined (~v1docq47@81.1.228.168)
    [2020-07-01 13:19:06] <sarang> sgp_: there was a good comment on the coinbase-only issue about the importance of weighing any implementation risks against the benefits
    [2020-07-01 13:19:10] → TrasherDK joined (~TrasherDK@cm-171-100-239-63.revip10.asianet.co.th)
    [2020-07-01 13:19:15] <sarang> and I think that's entirely valid
    [2020-07-01 13:19:55] <sgp_> Sure, something moneromooo and others would be more qualified to explain
    [2020-07-01 13:23:53] <sarang> All right, are there other topics to discuss from anyone?
    [2020-07-01 13:25:30] <sarang> In that case, on to ACTION ITEMS
    [2020-07-01 13:25:42] <sarang> More proofs, updates, and edits to the preprint for me
    [2020-07-01 13:26:02] <sarang> Oh, I'll be giving a remote talk on privacy tomorrow, which will be fun
    [2020-07-01 13:26:22] ⇐ jtgrassie quit (~jtgrassie@monerop.com): *.net *.split
    [2020-07-01 13:26:23] ⇐ ArticMine quit (~ArticMine@s207-81-214-17.bc.hsia.telus.net): *.net *.split
    [2020-07-01 13:26:23] ⇐ investanto quit (~investant@devtalk.ryo-currency.com): *.net *.split
    [2020-07-01 13:26:23] ⇐ kl_ quit (uid344501@gateway/web/irccloud.com/x-rljrqlansnmzzkra): *.net *.split
    [2020-07-01 13:26:23] ⇐ numin0us quit (~numin0us@unaffiliated/numin0us): *.net *.split
    [2020-07-01 13:26:23] ⇐ hashcashjoe quit (~joe@cpe-24-28-15-94.austin.res.rr.com): *.net *.split
    [2020-07-01 13:26:24] ⇐ grydz quit (~grydz@82.67.246.253): *.net *.split
    [2020-07-01 13:26:24] ⇐ kayront- quit (~kayront@zbase.xen.prgmr.com): *.net *.split
    [2020-07-01 13:26:24] ⇐ whyamiroot quit (~whyamiroo@auth.summitto.com): *.net *.split
    [2020-07-01 13:26:24] ⇐ Snipa quit (~Snipa@unaffiliated/snipa): *.net *.split
    [2020-07-01 13:26:35] <sarang> And the Lelantus preprint got a major security model update that I want to investigate in more detail
    [2020-07-01 13:26:44] <sarang> Anyone else?
    [2020-07-01 13:27:00] <sarang> Looks like several people were just dropped from the channel...
    [2020-07-01 13:28:37] → ArticMine joined (~ArticMine@s207-81-214-17.bc.hsia.telus.net)
    [2020-07-01 13:29:14] <sarang> Well, I suppose can adjourn early then
    [2020-07-01 13:29:25] <sarang> Thanks to everyone for attending! A quiet week, but that's ok
    [2020-07-01 13:29:28] → nickler joined (~nickler@static.219.205.69.159.clients.your-server.de)
    [2020-07-01 13:29:28] → jtgrassie joined (~jtgrassie@monerop.com)
    [2020-07-01 13:29:28] → investanto joined (~investant@devtalk.ryo-currency.com)
    [2020-07-01 13:29:28] → kl_ joined (uid344501@gateway/web/irccloud.com/x-rljrqlansnmzzkra)
    [2020-07-01 13:29:28] → numin0us joined (~numin0us@unaffiliated/numin0us)
    [2020-07-01 13:29:28] → hashcashjoe joined (~joe@cpe-24-28-15-94.austin.res.rr.com)
    [2020-07-01 13:29:28] → grydz joined (~grydz@82.67.246.253)
    [2020-07-01 13:29:28] → kayront- joined (~kayront@zbase.xen.prgmr.com)
    [2020-07-01 13:29:28] → whyamiroot joined (~whyamiroo@auth.summitto.com)
    [2020-07-01 13:29:28] → Snipa joined (~Snipa@unaffiliated/snipa)
    [2020-07-01 13:29:33] <sarang> Logs will be posted shortly


# Action History
- Created by: SarangNoether | 2020-07-01T15:01:13+00:00
- Closed at: 2020-07-01T17:32:31+00:00
