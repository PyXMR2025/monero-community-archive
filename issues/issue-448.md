---
title: 'Research meeting: 25 March 2020 @ 17:00 UTC'
source_url: https://github.com/monero-project/meta/issues/448
author: SarangNoether
assignees: []
labels: []
created_at: '2020-03-24T01:49:46+00:00'
updated_at: '2020-03-25T17:57:30+00:00'
type: issue
status: closed
closed_at: '2020-03-25T17:57:30+00:00'
---

# Original Description
Join in for the weekly Monero Research Lab meeting.

**When**: Wednesday, 25 March 2020 @ 17:00 UTC
**Where**: #monero-research-lab (freenode/matrix)

**Agenda**
1. Greetings

2. Roundtable

3. Questions

4. Action items

# Discussion History
## SarangNoether | 2020-03-25T17:57:30+00:00
    [2020-03-25 12:59:26] <sarang> GREETINGS
    [2020-03-25 12:59:27] <sarang> hi
    [2020-03-25 12:59:59] <derpy_bridge> [keybase] <seddd>: o/
    [2020-03-25 13:00:06] → h4sh3d[m] joined (h4sh3dmatr@gateway/shell/matrix.org/x-mockfssioqoxkmzk)
    [2020-03-25 13:00:37] <UkoeHB_> hi
    [2020-03-25 13:00:50] — sarang waits a few moments for others to arrive
    [2020-03-25 13:01:00] <SerHack> hi
    [2020-03-25 13:02:09] → Young_Padawan[m] joined (bookerdewi@gateway/shell/matrix.org/x-nvujxgjclwvevcsk)
    [2020-03-25 13:02:29] → ophalia[m] joined (ophaliahac@gateway/shell/matrix.org/x-jsrntuywsechxoxq)
    [2020-03-25 13:02:44] <sarang> Moving on, then, to ROUNDTABLE
    [2020-03-25 13:02:50] <sarang> Who wishes to share research of interest?
    [2020-03-25 13:02:56] → ArticMine joined (~ArticMine@s207-81-214-17.bc.hsia.telus.net)
    [2020-03-25 13:03:42] <ArticMine> Hi
    [2020-03-25 13:04:06] <sarang> I can share a few things
    [2020-03-25 13:04:23] <sarang> I've completed some formal peer review for the IEEE S&B proceedings
    [2020-03-25 13:04:41] <sarang> and worked on analysis for a linkable ring signature construction in IACR 2020/333
    [2020-03-25 13:04:54] <sarang> it claimed to be more efficient than CLSAG
    [2020-03-25 13:05:20] → truchaese[m] joined (truchaesem@gateway/shell/matrix.org/x-fafjhaoviqeruuha)
    [2020-03-25 13:05:27] <sarang> However, the numbers assumed an insecure key image construction
    [2020-03-25 13:05:39] → dl3br[m] joined (dlebrechtm@gateway/shell/matrix.org/x-punhqwxappcjocvh)
    [2020-03-25 13:05:51] <sarang> The authors have already posted a revision, but it doesn't include numbers or new security proofs for the modified construction
    [2020-03-25 13:06:07] <sarang> Besides this, here's an update on some other projects...
    [2020-03-25 13:06:34] <sarang> For CLSAG, I am still waiting on the final go-ahead from suraeNoether, who is a coauthor on the paper
    [2020-03-25 13:07:00] <sarang> I finished code optimization and made a PR to moneromooo's branch, which has some nice verification speedups
    [2020-03-25 13:07:17] <sarang> For Triptych-1, its preprint has been updated at IACR 2020/018
    [2020-03-25 13:07:37] <sarang> An MPC construction for key images is completed, and multisig/join analysis is still underway
    [2020-03-25 13:07:50] <sarang> For Triptych-2, its preprint has been posted at IACR 2020/312
    [2020-03-25 13:07:57] <sarang> Multisig/join analysis is still underway
    [2020-03-25 13:08:03] → ErCiccione[m] joined (erciccione@gateway/shell/matrix.org/x-newrxenjcjnpvrlo)
    [2020-03-25 13:08:10] <sarang> That's all for me
    [2020-03-25 13:08:14] * ErCiccione[m] → Guest56370
    [2020-03-25 13:08:17] <sarang> Any particular questions or comments?
    [2020-03-25 13:08:44] <nioc> how much verification speeedup for CLSAG?
    [2020-03-25 13:08:53] <derpy_bridge> [keybase] <seddd>: Do you need any more eyes on the CLSAG PR?
    [2020-03-25 13:08:55] <sarang> It's around 4-5%
    [2020-03-25 13:09:01] <nioc> nice
    [2020-03-25 13:09:18] <sarang> seddd: That would be welcome, once moneromooo integrates the new changes into the branch
    [2020-03-25 13:09:43] <derpy_bridge> [keybase] <seddd>: Ok, let me know, and I'll review
    [2020-03-25 13:09:49] <sarang> that'd be great
    [2020-03-25 13:09:59] <moneromooo> I did, I can push.
    [2020-03-25 13:10:03] <sarang> Oh excellent
    [2020-03-25 13:10:20] <ArticMine> 4-5% reduction in size? Verification time?
    [2020-03-25 13:10:25] <sarang> The only real changes from the paper's description is a modification to the public parameters that go into the challenge hashes, which allows for the speedup to happen
    [2020-03-25 13:10:29] <sarang> ArticMine: verification time
    [2020-03-25 13:10:41] <sarang> I didn't bother with generation stuff, since that's less important
    [2020-03-25 13:10:45] <sarang> Size is identical
    [2020-03-25 13:11:22] <sarang> The PR includes new performance tests with better direct comparison to MLSAG, if that's useful to anyone
    [2020-03-25 13:11:32] <derpy_bridge> [keybase] <seddd>: moneromooo: link?
    [2020-03-25 13:12:08] <ArticMine> So is this the version that is going for audit?
    [2020-03-25 13:12:21] <moneromooo> Not yet.
    [2020-03-25 13:12:21] <sarang> Presumably, but that's up to the audit workgroup
    [2020-03-25 13:12:41] <moneromooo> I'm rebasing it to master now, then will run tests, then push, then post a link.
    [2020-03-25 13:12:56] <sarang> moneromooo: excellent, then the CI workflow will operate properly
    [2020-03-25 13:13:09] <derpy_bridge> [keybase] <seddd>: awesome, many thanks 🤗
    [2020-03-25 13:13:22] <sarang> Any other questions for me?
    [2020-03-25 13:13:30] <sarang> Or does anyone else wish to share research topics?
    [2020-03-25 13:14:39] <derpy_bridge> [keybase] <seddd>: Mb but it involves pow of another coin, not sure appropriate
    [2020-03-25 13:14:49] <sarang> Perhaps suited for after the meeting
    [2020-03-25 13:14:58] <derpy_bridge> [keybase] <seddd>: Definitely
    [2020-03-25 13:15:18] <selsta> who is the audit workgroup? sgp?
    [2020-03-25 13:15:36] <sarang> sgp_ has been working to coordinate
    [2020-03-25 13:16:29] <sarang> As far as the CLSAG paper goes, if I don't hear from suraeNoether, eventually I suppose we'll just have to release the revised version without him
    [2020-03-25 13:16:39] <sarang> But I would prefer not to do that, since he's a coauthor
    [2020-03-25 13:17:14] <derpy_bridge> [keybase] <seddd>: Is suraeNoether not around rn?
    [2020-03-25 13:17:18] <sarang> He hasn't enabled public viewing on the overleaf version, and I don't have access rights to do that unfortunately
    [2020-03-25 13:17:39] <sarang> No, he is not around right now AFAIK
    [2020-03-25 13:19:48] <derpy_bridge> [keybase] <seddd>: k
    [2020-03-25 13:21:13] <sarang> Well, to respect everyone's time, I suppose we can move to ACTION ITEMS
    [2020-03-25 13:21:16] <UkoeHB_> update from me: proofreading is extended to this weekend as comments are trickling in at the last moment :p; I have received several good feedbacks so far
    [2020-03-25 13:21:22] <sarang> Ah ok, go ahead UkoeHB_
    [2020-03-25 13:21:34] <UkoeHB_> current proofreading version is here https://www.pdf-archive.com/2020/03/22/zerotomoneromaster-v1-1-2/zerotomoneromaster-v1-1-2.pdf
    [2020-03-25 13:21:36] <UkoeHB_> that's all
    [2020-03-25 13:21:41] <sarang> Great, thanks
    [2020-03-25 13:21:58] <sarang> My action items are to complete my proofreading of Zero to Monero (it's been delayed; my apologies)
    [2020-03-25 13:22:10] <sarang> and to work on some Triptych-2 MPC math
    [2020-03-25 13:22:23] <sarang> Anyone else?
    [2020-03-25 13:22:40] <hyc> "research only, not for production use" inb4 sumo releases it and claims to be first
    [2020-03-25 13:22:59] <UkoeHB_> oh right, I made a small update to Janus mitigation
    [2020-03-25 13:23:02] <sarang> hyc: ?
    [2020-03-25 13:23:10] <sgp_> UkoeHB_: cool,, what?
    [2020-03-25 13:23:15] <derpy_bridge> [keybase] <seddd>: lul hyc
    [2020-03-25 13:23:16] <hyc> sorry, catching up from a couple days ago
    [2020-03-25 13:23:27] <UkoeHB_> https://github.com/monero-project/research-lab/issues/62#issuecomment-603079784
    [2020-03-25 13:24:12] <derpy_bridge> [keybase] <seddd>: imagines sumo as yt commenter: "FIRST"
    [2020-03-25 13:24:15] <sgp_> UkoeHB_: none of that is implemented correct?
    [2020-03-25 13:24:20] <sarang> Off topic, folks!
    [2020-03-25 13:24:21] <UkoeHB_> correct
    [2020-03-25 13:24:32] <derpy_bridge> [keybase] <seddd>: srry
    [2020-03-25 13:25:12] → ErCiccione joined (~ErCiccion@gateway/tor-sasl/erciccione)
    [2020-03-25 13:26:45] <sarang> IIRC, the last time Janus mitigations were discussed in a dev meeting, there seemed to be mixed support
    [2020-03-25 13:26:47] <UkoeHB_> my action item is to go through all proofreading comments, and then this weekend finalize a for-publication version
    [2020-03-25 13:27:44] <UkoeHB_> sarang part of that seemed to be related to exactly how many pub keys and janus base keys it would require
    [2020-03-25 13:27:46] * Guest56370 → ErCiccione[m]1
    [2020-03-25 13:28:24] ⇐ DeanGuss quit (~dean@gateway/tor-sasl/deanguss): Remote host closed the connection
    [2020-03-25 13:28:38] <UkoeHB_> full Janus mitigation would require: 1 Janus base key per transaction, #pub keys = #outputs for ALL transactions (not just tx with subaddresses as is the case now)
    [2020-03-25 13:28:51] <sarang> yep
    [2020-03-25 13:30:23] <derpy_bridge> [keybase] <seddd>: sounds like a lot of overhead, is that one of the main objections?
    [2020-03-25 13:30:27] → DeanGuss joined (~dean@gateway/tor-sasl/deanguss)
    [2020-03-25 13:30:32] <UkoeHB_> there is partial Janus mitigation, where normal addresses and subaddresses are split up; in other words, don't mitigate linking of normal addresses with subaddresses; that way only tx with subaddresses would need the janus base key
    [2020-03-25 13:31:36] <UkoeHB_> however, even with partial mitigation a lot more subaddress tx would be revealed as subaddress, as there are currently some optimizations that hide subaddress tx among normal tx
    [2020-03-25 13:32:08] <UkoeHB_> while with full migitation, normal address tx and subaddress tx would be universally indistinguishable
    [2020-03-25 13:32:26] <UkoeHB_> which iirc sarang was in favor of even outside of Janus
    [2020-03-25 13:32:46] <derpy_bridge> [keybase] <seddd>: +1 for the latter
    [2020-03-25 13:32:58] <sarang> Yeah, encouraging/enforcing indistinguishability is useful
    [2020-03-25 13:32:59] <UkoeHB_> the main objective is solving the Janus attack
    [2020-03-25 13:33:16] <UkoeHB_> which is currently undetectable
    [2020-03-25 13:33:22] <sarang> yes
    [2020-03-25 13:33:56] <derpy_bridge> [keybase] <seddd>: so what are the opposing arguments?
    [2020-03-25 13:34:19] <sarang> Transaction size is increased
    [2020-03-25 13:34:28] <sarang> that's a big counterargument
    [2020-03-25 13:34:32] <sarang> (literally)
    [2020-03-25 13:34:44] <derpy_bridge> [keybase] <seddd>: :)
    [2020-03-25 13:35:14] <sarang> So as happens always, there's a tradeoff on complexity (in this case, size and protocol changes) and indistinguishability
    [2020-03-25 13:35:19] <sarang> s/always/often
    [2020-03-25 13:36:16] <sarang> Worth noting that with CLSAG, standard tx size already drops from ~2.5 kB to ~1.9 kB
    [2020-03-25 13:36:23] <sarang> so there's some wiggle room
    [2020-03-25 13:36:58] <derpy_bridge> [keybase] <seddd>: are there potentially more compact full Janis mitigations?
    [2020-03-25 13:37:03] <sarang> Each added scalar/group element adds 32 bytes
    [2020-03-25 13:37:09] <derpy_bridge> [keybase] <seddd>: Janus*
    [2020-03-25 13:38:07] <UkoeHB_> this is the smallest known mitigation
    [2020-03-25 13:38:42] <ArticMine> Tx size is increased by how much?
    [2020-03-25 13:39:12] <UkoeHB_> on average, about 2.2*32 bytes per transaction
    [2020-03-25 13:39:20] ⇐ ErCiccione quit (~ErCiccion@gateway/tor-sasl/erciccione): Quit: Leaving
    [2020-03-25 13:39:21] <UkoeHB_> assuming 2.2 is the average output count
    [2020-03-25 13:39:55] <UkoeHB_> wait no, 32 + 1.2*32
    [2020-03-25 13:40:01] <UkoeHB_> same thing lol
    [2020-03-25 13:40:59] <derpy_bridge> [keybase] <seddd>: What about encoding the extra basepoint in smth like a lookup table, where base points are indexed by the first 8? bytes
    [2020-03-25 13:41:05] <UkoeHB_> actually a tiny bit less than that, taking into account current subaddress tx
    [2020-03-25 13:41:11] <ArticMine> So 64 bytes for a typical tx
    [2020-03-25 13:41:20] <UkoeHB_> yeah basically
    [2020-03-25 13:41:52] <ArticMine> So if the security issue is verified I do not see an issue here
    [2020-03-25 13:41:53] <UkoeHB_> seddd, the base key must be generated by transaction authors
    [2020-03-25 13:42:08] <UkoeHB_> under the current construction, not sure if there are any other ways to do it
    [2020-03-25 13:42:14] <sarang> ArticMine: the math checks out on the fix
    [2020-03-25 13:42:30] <derpy_bridge> [keybase] <seddd>: Ok so unknowable ahead, gotcha
    [2020-03-25 13:43:57] <derpy_bridge> [keybase] <seddd>: will read more in the issue you linked
    [2020-03-25 13:44:09] <sarang> Probably time to bring it up in dev meeting again
    [2020-03-25 13:44:30] <UkoeHB_> seddd there might be something to that (using a fixed janus base key of some kind), Ill ponder it a bit
    [2020-03-25 13:44:47] <sarang> Any other action items to bring up?
    [2020-03-25 13:45:18] <derpy_bridge> [keybase] <seddd>: UkoeHB_ that's kind of what I was thinking, or a fixed set of usable bases
    [2020-03-25 13:45:53] <derpy_bridge> [keybase] <seddd>: Happy to collaborate, this is an interesting problem
    [2020-03-25 13:47:01] <sarang> for sure
    [2020-03-25 13:47:17] <sarang> OK, let's go ahead and wrap things up for this meeting; discussions can of course continue after we adjourn
    [2020-03-25 13:47:27] <sarang> Any last topics of general interest for the meeting?
    [2020-03-25 13:48:40] <sarang> Righto! Meeting adjourned
    [2020-03-25 13:48:46] <sarang> thanks to everyone for attending


# Action History
- Created by: SarangNoether | 2020-03-24T01:49:46+00:00
- Closed at: 2020-03-25T17:57:30+00:00
