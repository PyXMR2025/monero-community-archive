---
title: 'Research meeting: 28 October 2019 @ 17:00 UTC'
source_url: https://github.com/monero-project/meta/issues/404
author: SarangNoether
assignees: []
labels: []
created_at: '2019-10-25T13:25:46+00:00'
updated_at: '2019-10-28T17:34:38+00:00'
type: issue
status: closed
closed_at: '2019-10-28T17:34:38+00:00'
---

# Original Description
Join in for the weekly Monero Research Lab meeting.

**When**: Monday, 28 October 2019 @ 17:00 UTC
**Where**: #monero-research-lab (freenode/matrix)

**Agenda**
1. Greetings

2. Roundtable
a. Sarang
b. Surae
c. Others?

3. General questions

4. Action items

# Discussion History
## SarangNoether | 2019-10-28T17:34:38+00:00
    [2019-10-28 13:00:04] <sarang> GREETINGS
    [2019-10-28 13:00:40] <sgp_> hello!
    [2019-10-28 13:00:55] <sarang> I'll give a few moments for others who wish to join
    [2019-10-28 13:02:36] <sarang> OK then
    [2019-10-28 13:02:52] <sarang> Since suraeNoether is unavailable for this meeting due to an appointment, I'll share my recent work
    [2019-10-28 13:03:10] <sarang> I've been working on algorithms and proofs for Triptych, a new transaction protocol
    [2019-10-28 13:03:46] <sarang> The goal is to use a single proof to represent multiple inputs at the same time, including balance proving and linking tags
    [2019-10-28 13:04:09] <sarang> Everything works great with completeness, zero knowledge, and soundness except for one proof component (the linking tags)
    [2019-10-28 13:04:34] <sarang> There's a less efficient version that operates on single inputs, but can be combined for general transactions
    [2019-10-28 13:04:52] <sarang> For this single-input version, modified proofs of security seem to work just fine
    [2019-10-28 13:05:32] <sarang> For this reason, I'll finalize work on the single-input proving system while considering alternate approaches to finalizing the soundness proof for the multi-input version
    [2019-10-28 13:06:02] <sarang> Separately from this, I have a small pull request (PR 6049) for a minor speedup and simplification to the Bulletproofs prover
    [2019-10-28 13:06:34] <sarang> Also separately from this, Derek at OSTIF informs me that an audit group is willing to complete the CLSAG review
    [2019-10-28 13:07:36] <sarang> JP Aumasson has offered to complete a review of the math and proofs for $7200 (USD), and his new company Teserakt has offered to then complete a code review for as little as $4800
    [2019-10-28 13:07:59] <sarang> He says that including dependencies would increase the time (and therefore the cost), possibly significantly
    [2019-10-28 13:08:23] <sarang> But the timeline could be before the end of this year, if there are no changes required to the algorithms after the math review
    [2019-10-28 13:08:30] <moneromooo> Dependencies, like the src/crypto code ?
    [2019-10-28 13:09:02] <sarang> Presumably. I do not have specific details on what his scope is (but will get this information)
    [2019-10-28 13:09:24] → mikerah joined (~mikerah@2607:fea8:875f:f8d0::2)
    [2019-10-28 13:09:37] <sarang> One approach might be to review all the changes _from MLSAG_, to show that CLSAG is no less secure as a whole than MLSAG
    [2019-10-28 13:10:01] <sarang> These changes are fairly minor in the grand scope of the codebase
    [2019-10-28 13:10:26] → Common_Deer joined (~CommonDee@14-202-132-82.static.tpgi.com.au)
    [2019-10-28 13:10:50] <sarang> I see there being efficiency advantages to having JP (and colleagues) doing both types of review, but this also reduces the total number of eyes on the combined math+code
    [2019-10-28 13:11:00] <sarang> That being said, JP knows his stuff
    [2019-10-28 13:11:07] <sarang> (he was formerly with Kudelski)
    [2019-10-28 13:12:11] <moneromooo> Adding eyes by having Alice do the math and Bob do the code does not provide anything of value over Alice doing both IMHO.
    [2019-10-28 13:12:36] <moneromooo> Assuming Alice and Bob have similar eyes and brains and proficiency in the relevant fields etc etc etc.
    [2019-10-28 13:13:14] ⇐ Common-Deer quit (~CommonDee@14-202-132-82.static.tpgi.com.au): Ping timeout: 240 seconds
    [2019-10-28 13:13:53] <sarang> So that's my report
    [2019-10-28 13:14:14] <moneromooo> Is any of the new protocols being considered still compatible with multisig ?
    [2019-10-28 13:14:57] → BlaiseRascal joined (8aa2002a@138.162.0.42)
    [2019-10-28 13:15:16] <sarang> Aside from CLSAG, you mean?
    [2019-10-28 13:16:02] → cryptoIndio joined (~cryptoInd@42-200-238-108.static.imsbiz.com)
    [2019-10-28 13:16:13] <sarang> None of them specifically consider it in either algorithms or security model
    [2019-10-28 13:16:47] <sarang> but it's on my list for analysis on RCT3 and (eventually) Triptych, since there are some modifications to RCT3 that I wish to consider (more on this later)
    [2019-10-28 13:17:22] <moneromooo> I mean tryptich,  rct3 and... and.......... the other the name of which escapes me.
    [2019-10-28 13:17:26] <moneromooo> lelantus
    [2019-10-28 13:17:27] <sarang> Omniring?
    [2019-10-28 13:17:31] <moneromooo> Also :)
    [2019-10-28 13:18:03] <sarang> Omniring and Lelantus both suffer from some drawbacks at present... Omniring does not support batching, and Lelantus still has a tracing issue unless you remove stealth addressing
    [2019-10-28 13:18:29] → Novastar joined (~root@217.23.5.51)
    [2019-10-28 13:18:33] <sarang> Looking into batch-compatible Omniring-style constructions with other proving systems is a topic for more investigation down the road that is nontrivial
    [2019-10-28 13:19:22] <sarang> Is there other research that anyone wishes to present, or other questions?
    [2019-10-28 13:19:31] <moneromooo> Also, rather selfishly, would any of them avoid the public-a issue we had for multi user txes ?
    [2019-10-28 13:19:49] <moneromooo> (if known offhand)
    [2019-10-28 13:19:52] <sarang> public-a?
    [2019-10-28 13:20:06] <moneromooo> The problem where users would have to make their a values known to other signers.
    [2019-10-28 13:20:26] <sarang> Ah, that's very unclear to me
    [2019-10-28 13:21:08] <sarang> FWIW: RCT3, Omniring, and Triptych are agnostic to how output keys are generated (though their security models address particular constructions)
    [2019-10-28 13:22:59] ⇐ cryptoIndio quit (~cryptoInd@42-200-238-108.static.imsbiz.com): Ping timeout: 268 seconds
    [2019-10-28 13:24:01] <sarang> So my ACTION ITEMS for this week are a bit in flux, mainly because I'll be at World Crypto Conference giving a talk on transaction protocols
    [2019-10-28 13:25:00] <sarang> But aside from that, I want to finish the proof modifications (completeness, SHVZK, special soundness) for the single-input version of Triptych (which can be used in a larger protocol to support multi-input transactions), as well as a more efficient linking tag construction that matches what RCT3 and Omniring propose
    [2019-10-28 13:25:39] <sarang> I also want to backport some of the ideas from the latest RCT3 update to their older version to compare efficiency
    [2019-10-28 13:25:55] <sarang> It's unclear if this could easily be proven secure, or what the efficiency gains would be
    [2019-10-28 13:26:27] <sarang> Their update did essentially two things: fix an exploitable flaw due to a particular discrete log relation, and allow for aggregated proofs of multiple inputs
    [2019-10-28 13:26:50] <sarang> Unfortunately, the latter means potentially large padding requirements that would also incur computational cost to the verifier
    [2019-10-28 13:27:29] <sarang> I want to see how easily the exploit fix could be included in the non-aggregated version... which would avoid this potential verification bloat at the cost of proof size
    [2019-10-28 13:27:54] <sarang> I probably won't have time to do so this week, but it's on my list
    [2019-10-28 13:30:09] <sarang> Anything else of note to cover before we formally adjourn?
    [2019-10-28 13:31:20] <sarang> All right! Thanks to everyone for attending
    [2019-10-28 13:31:26] <sarang> Logs will be posted shortly to the GitHub agenda issue


# Action History
- Created by: SarangNoether | 2019-10-25T13:25:46+00:00
- Closed at: 2019-10-28T17:34:38+00:00
