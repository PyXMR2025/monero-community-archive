---
title: 'Research meeting: 29 July 2020 @ 17:00 UTC'
source_url: https://github.com/monero-project/meta/issues/491
author: SarangNoether
assignees: []
labels: []
created_at: '2020-07-23T16:04:56+00:00'
updated_at: '2020-07-30T01:12:27+00:00'
type: issue
status: closed
closed_at: '2020-07-30T01:12:27+00:00'
---

# Original Description
Join in for the weekly Monero Research Lab meeting.

**When**: Wednesday, 29 July 2020 @ 17:00 UTC
**Where**: #monero-research-lab (freenode/matrix)

**Agenda**
1. Greetings

2. Roundtable

3. Questions

4. Action items

# Discussion History
## SamsungGalaxyPlayer | 2020-07-23T16:38:25+00:00
I should be running this meeting in Sarang's absence.

## SarangNoether | 2020-07-30T01:12:27+00:00
    [2020-07-29 12:02:07] <sgp_> 1. Greetings
    [2020-07-29 12:02:35] <hyc> hey
    [2020-07-29 12:02:53] — selsta lurking
    [2020-07-29 12:03:10] <ArticMine> Hi
    [2020-07-29 12:03:33] <sethsimmons> hi all
    [2020-07-29 12:04:11] <sgp_> hello everyone
    [2020-07-29 12:04:14] <sgp_> 2. Roundtable
    [2020-07-29 12:04:36] — Isthmus waves
    [2020-07-29 12:04:45] <sgp_> Sarang is not present for this meeting today, but he has been working on coordinating the CLSAG audit for final release
    [2020-07-29 12:04:58] <sgp_> Does anyone else have an update to share?
    [2020-07-29 12:07:23] <hyc> anyone following quantum computing,
    [2020-07-29 12:07:25] <hyc> https://www.nist.gov/news-events/news/2020/07/nists-post-quantum-cryptography-program-enters-selection-round
    [2020-07-29 12:07:48] <hyc> "Following this roughly 18-month period, NIST will plan to release the initial standard for quantum-resistant cryptography in 2022."
    [2020-07-29 12:08:09] <Isthmus> Ooh interesting. We’re now digging through a vast pq-crypto landscape to find Monero compatible solutions leveraging Lattice Based Cryptography, Multivariate cryptography, Hash-Based Cryptography, Supersingular elliptic curve isogeny cryptography, or Quantum Key Cryptography. Will examine the NIST work as well.
    [2020-07-29 12:08:21] <Isthmus> Lattice-based SALRS and the MatRiCT are of particular interest so far, but we’re still executing a broad search.
    [2020-07-29 12:09:00] <Isthmus> There's a ton of pq-hard problems, though the vast majority are too unwieldy for implementation at the moment.
    [2020-07-29 12:10:09] <hyc> 5 of the 7 candidates are lattice-based
    [2020-07-29 12:11:22] <hyc> decent overview https://medium.com/asecuritysite-when-bob-met-alice/crypto-bake-off-the-final-and-its-a-lattice-bake-in-the-lead-dafc23ecde20
    [2020-07-29 12:11:50] — Isthmus bookmarks to read during next tea break
    [2020-07-29 12:12:24] <Isthmus> Thanks for sharing these great resources hyc
    [2020-07-29 12:13:53] → tromp joined (~tromp@2a02:a210:ca3:2800:49e1:2235:a55d:a0e5)
    [2020-07-29 12:13:57] <sgp_> I just skimmed that overview, nice stuff
    [2020-07-29 12:15:01] <sgp_> any other roundtable updates?
    [2020-07-29 12:16:10] <sgp_> we can then move on to 3. Questions
    [2020-07-29 12:17:16] <sgp_> I got a question from Reddit: when is Monero going to change its ringsize? It will be going on two quick years with ringsize 11
    [2020-07-29 12:17:39] <sgp_> I'm not aware of a significant reason to increase before something like Triptych
    [2020-07-29 12:18:19] <hyc> yeah, haven't seen any reason to rush
    [2020-07-29 12:19:59] <selsta> faster chain verification > marginal privacy improvement IMO
    [2020-07-29 12:20:39] <hyc> agree
    [2020-07-29 12:20:47] <sgp_> selsta hyc: separating coinbase and dropping the ringsize to 1 or 3 for those tx will speed up a bit :p
    [2020-07-29 12:20:58] <fluffypony> only from that point on, though
    [2020-07-29 12:20:58] <selsta> can’t comment on that
    [2020-07-29 12:21:01] <fluffypony> not historically
    [2020-07-29 12:21:01] ⇐ Common_Deer quit (~CommonDee@14-201-4-66.static.tpgi.com.au): Read error: Connection reset by peer
    [2020-07-29 12:21:17] <hyc> and, it's like key sizes - sure, bigger keys are stronger, but there's no reason to use a bigger key than necessary
    [2020-07-29 12:21:25] → Common_Deer joined (~CommonDee@14-201-4-66.static.tpgi.com.au)
    [2020-07-29 12:22:21] <sgp_> what is the general sentiment about whether to implement bulletproofs+?
    [2020-07-29 12:22:32] <ArticMine> My question with coinbase is why not just mix coinbase with coinbase. Then there is no hard fork required
    [2020-07-29 12:22:50] <sgp_> ArticMine: requires hard fork to enforce
    [2020-07-29 12:23:09] <ArticMine> and non coinbase with non coinbase
    [2020-07-29 12:23:25] <fluffypony> sgp_: it would be a soft fork
    [2020-07-29 12:23:32] <fluffypony> you're tightening the existing rules
    [2020-07-29 12:23:52] <hyc> my impression of BP+ is it's probably a good idea, but I'd like to see some formal peer review finished first
    [2020-07-29 12:23:53] <sgp_> wallets can do that now, but it would be relatively simple to identify which wallets are using that and which aren't
    [2020-07-29 12:24:07] <sgp_> sure, soft fork could be possible but I guess why bother
    [2020-07-29 12:24:44] <sgp_> also we need the hardfork if we want to shrink coinbase ringsize
    [2020-07-29 12:25:06] <moneromooo> I'm for BP+. If sarang gets a python implementation, I could do the C++, if he doesn't do it directly.
    [2020-07-29 12:25:20] <ArticMine> Why shrink coinbase ringsize?
    [2020-07-29 12:25:24] <hyc> if you mix coinbase only with coinbase is there any reason to shrink the ringsize?
    [2020-07-29 12:25:25] <moneromooo> I'm assuming it's not a huge change from our current code. If it is, I might change my mind.
    [2020-07-29 12:25:51] <sgp_> hyc: coinbase outputs are quite toxic with all the public pool data
    [2020-07-29 12:26:04] <hyc> from my convs with sarang, sounds like BP+ should not be a big change
    [2020-07-29 12:26:57] <hyc> sgp_: which sounds like all the more reason to leave them the same ringsize as others.
    [2020-07-29 12:27:01] <ArticMine> <sgp_> hyc: coinbase outputs are quite toxic with all the public pool data <--- So why shrink the ring size then ?
    [2020-07-29 12:27:35] <sgp_> did you both read my github issue about it?
    [2020-07-29 12:28:02] <ArticMine> link
    [2020-07-29 12:28:36] <sgp_> last time I looked, 90% of coinbase outputs were attributable to specific pools. ringsize 11 can't handle a 90% scenario
    [2020-07-29 12:29:26] <ArticMine> I know but what I am saying is mix only with other ringsize outputs
    [2020-07-29 12:29:33] <sgp_> https://github.com/monero-project/monero/issues/6688
    [2020-07-29 12:29:38] <hyc> coinbase*
    [2020-07-29 12:29:54] <sgp_> ArticMine: I agree and support the idea of separating the two
    [2020-07-29 12:30:07] <sgp_> We however have the option to configure the ringsizes separately if we want
    [2020-07-29 12:30:22] <sgp_> luigi1111 voices support for doing this
    [2020-07-29 12:30:25] <sgp_> *voiced
    [2020-07-29 12:30:36] <ArticMine> I  will comment on the issue
    [2020-07-29 12:30:48] <sgp_> ty
    [2020-07-29 12:30:52] <hyc> so if coinbase only mixes with coinbase, and ringsize 11 is inadequate, why drop down to size 3 or 1?
    [2020-07-29 12:31:44] <sgp_> Options are:
    [2020-07-29 12:31:44] <sgp_> 1. Drop the coinbase ringsize to 1 or 3 for efficiency. Mostly write off coinbase outputs as a lost cause.
    [2020-07-29 12:31:44] <sgp_> 2. Keep it the same
    [2020-07-29 12:31:44] <sgp_> 3. Increase it knowing that coinbase outputs are a deducible bloodbath if we really feel that we need to protect coinbase outputs. It will cost us.
    [2020-07-29 12:31:50] <luigi1111w> because it's a waste of blockchain space
    [2020-07-29 12:31:51] <sgp_> hyc: from the issue linked above
    [2020-07-29 12:31:59] <ArticMine> I see a fair amount of consensus on segregating the coinbase outputs
    [2020-07-29 12:32:29] <ArticMine> How we then treat them can be the subject for further discussion
    [2020-07-29 12:33:27] <ArticMine> I will move with mixing coinbase with coinbase and non coinbase  with non coinbase ASAP
    [2020-07-29 12:33:40] <hyc> not sure what the significance is. so 90% of coinbase outs can be attributed to specific pools. Then pools must split them to payout to miners
    [2020-07-29 12:33:50] <sgp_> to get an idea of cost, in a 90% compromised scenario, and to protect 99% of rings with at least 1 non-compromised output, we need ringsize 45
    [2020-07-29 12:34:47] <ArticMine> sgp_ 's point is very valid
    [2020-07-29 12:35:15] <sgp_> you can see why I don't want normal transactions to use these toxic decoys as non-convincing inputs
    [2020-07-29 12:35:27] <ArticMine> Yes
    [2020-07-29 12:35:51] <luigi1111w> that's more a question of how many outputs are miner vs normal usage
    [2020-07-29 12:36:43] <sgp_> what is that, about 72 transactions/day spending coinbase outputs?
    [2020-07-29 12:36:49] <sgp_> *720
    [2020-07-29 12:36:56] <ArticMine> My proposal addresses the main issue of contamination normal outputs
    [2020-07-29 12:37:05] <luigi1111w> but it seems clear to me that if you are splitting miner txs into their own pool, then they should just not mix at all
    [2020-07-29 12:37:32] <ArticMine> That depends on the ring size
    [2020-07-29 12:38:07] <sgp_> greater efficiency for ~720 rings a day (on average) seems non-trivial
    [2020-07-29 12:38:35] <sgp_> not huge either
    [2020-07-29 12:38:36] <luigi1111w> shouldn't be that hard to quantify if you have some daily tx stats
    [2020-07-29 12:39:05] <hyc> gets to be insignificant as adoption increases
    [2020-07-29 12:39:30] <sgp_> hyc: yeah, it's pretty constant regardless of adoption
    [2020-07-29 12:40:30] <ArticMine> If we can reach consensus on the treatment of the separated coinbase transactions before the next HF great
    [2020-07-29 12:40:53] <sgp_> I hope so (not the Oct one obviously)
    [2020-07-29 12:41:40] <ArticMine> Otherwise I say go with ring 11 for the coinbase outputs
    [2020-07-29 12:42:04] <ArticMine> WHat I do not support is keeping the contamination of regular outputs while we decide
    [2020-07-29 12:42:24] <sgp_> ArticMine: wallet change?
    [2020-07-29 12:42:43] <ArticMine> That is by far the simplest
    [2020-07-29 12:43:00] <sgp_> hmm, that scares me a bit. wallets do weird stuff
    [2020-07-29 12:43:03] <ArticMine> but the specification has to be widely known
    [2020-07-29 12:43:25] <ArticMine> It is the same issue with fees
    [2020-07-29 12:43:57] <luigi1111w> I mostly disagree and think status quo is status quo until there is a coherent plan for change
    [2020-07-29 12:44:16] <ArticMine> Making the specification widely know can address the bulk of the issue
    [2020-07-29 12:44:26] <luigi1111w> we are wasting some space here, not dealing with something catastrophic
    [2020-07-29 12:44:57] <ArticMine> If there is consensus on part of the change, but not the rest, why hold up the part that has consensus?
    [2020-07-29 12:44:59] <sgp_> you know I want to separate the rings more than anybody (save space and protect users), yet this non-consensus change scares me
    [2020-07-29 12:46:02] <ArticMine> One can enforce the coinbase with coinbase mix as consensus
    [2020-07-29 12:46:35] <ArticMine> but keep the mixing at 11 if there is not agreement on the correct mixing
    [2020-07-29 12:47:26] <sgp_> all: please comment on that Github issue if you haven't already
    [2020-07-29 12:47:49] <sgp_> anything else on this topic or any other questions?
    [2020-07-29 12:50:11] <sgp_> 4. Action items
    [2020-07-29 12:50:44] <sgp_> sarang and I will put out the CLSAG audit report, hopefully in the next few days. It needs to go out
    [2020-07-29 12:51:00] <sgp_> just waiting on OSTIF
    [2020-07-29 12:51:21] <sgp_> everyone else?
    [2020-07-29 12:53:19] <sgp_> as a part of the Monero Community Workgroup resources, I will start pushing a kanban board to keep track of tasks more. MRL is welcome to use it or not, but keep an eye out for that
    [2020-07-29 12:53:33] <sgp_> if there is nothing else, we can conclude the meeting
    [2020-07-29 12:53:54] <sgp_> Next meeting a week from now. Same bat time, same bat channel
    [2020-07-29 12:54:08] <sgp_> Thanks for attending!


# Action History
- Created by: SarangNoether | 2020-07-23T16:04:56+00:00
- Closed at: 2020-07-30T01:12:27+00:00
