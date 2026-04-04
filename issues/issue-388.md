---
title: 'Research meeting: 2 September 2019 @ 17:00 UTC'
source_url: https://github.com/monero-project/meta/issues/388
author: SarangNoether
assignees: []
labels: []
created_at: '2019-09-02T14:21:45+00:00'
updated_at: '2019-09-02T19:44:09+00:00'
type: issue
status: closed
closed_at: '2019-09-02T19:44:09+00:00'
---

# Original Description
Join in for the weekly Monero Research Lab meeting.

**When**: Monday, 2 September 2019 @ 17:00 UTC
**Where**: #monero-research-lab (freenode/matrix)

**Agenda**
1. Greetings

2. Roundtable
a. Sarang: [monthly report](https://repo.getmonero.org/monero-project/ccs-proposals/merge_requests/77#note_7105)
b. Surae
c. Others?

3. General questions

4. Action items

# Discussion History
## SarangNoether | 2019-09-02T19:44:09+00:00
    [2019-09-02 12:00:49] <sarang> Agenda: https://github.com/monero-project/meta/issues/388
    [2019-09-02 12:00:52] <sarang> (logs posted there afterward)
    [2019-09-02 12:00:54] <suraeNoether> good morning everyone
    [2019-09-02 12:01:05] <sarang> GREETINGS
    [2019-09-02 12:01:12] <rottensox> Hola.
    [2019-09-02 12:02:10] <sarang> Happy Labor Day to those celebrating it
    [2019-09-02 12:02:17] <sarang> Happy Monday to all others
    [2019-09-02 12:02:22] <sarang> Let's do our ROUNDTABLE
    [2019-09-02 12:02:25] <sarang> suraeNoether: care to go first?
    [2019-09-02 12:03:13] <suraeNoether> sure. This past week i've been coding my economarkov chain simulating a fake Monero economy to apply matching to. this is slow-going, but steady progress. in addition to that, I started reading 3 separate papers for a new-ish idea...
    [2019-09-02 12:03:30] <suraeNoether> https://eprint.iacr.org/2016/583.pdf , https://www.microsoft.com/en-us/research/wp-content/uploads/2008/02/tcc2008.pdf , and https://link.springer.com/chapter/10.1007/3-540-36413-7_20
    [2019-09-02 12:04:20] <suraeNoether> the idea is new-ish to me but not the e-cash community, which is to demonstrate not a valid signature on a public message m, but *knowledge of* a valid signature on a public message m, without revealing the signature information like signer
    [2019-09-02 12:04:58] <suraeNoether> that 583 paper presents a trustless way of doing so with hash functions that can be described with a boolean circuit, and presents zk proofs of knowledge of RSA, DSA, and ECDSA signatures
    [2019-09-02 12:05:11] <suraeNoether> the idea is to replace ring signatures with something that is trustless and signer ambiguous
    [2019-09-02 12:05:55] <sarang> Interesting
    [2019-09-02 12:05:58] <suraeNoether> that way, instead of saying "Either A, B, or C signed this m with key image J," the statement being proven is "I have seen a valid signature on m with key image J"
    [2019-09-02 12:06:03] <sarang> Requires efficient trustless accumulator?
    [2019-09-02 12:06:38] <suraeNoether> coupling this together with a zk proof of membership in a strong dynamic accumulator allows for a "signature" scheme that does away with the explicit anonymity sets of ring signatures
    [2019-09-02 12:07:02] <suraeNoether> i think i'm onto a method for doing this with key images that are compatible with our current approaches
    [2019-09-02 12:07:36] <sarang> Nice!
    [2019-09-02 12:07:37] <suraeNoether> but I need, probably, 2-3 additional pairs of eyes helping me out, so I'll be writing some stuff up and possibly starting a github issue for discussion on the matter
    [2019-09-02 12:07:43] <sarang> roger
    [2019-09-02 12:08:22] <suraeNoether> other than that, i've been offline with family for a reunion + a 100-years-olds birthday party :D
    [2019-09-02 12:08:54] <sarang> My monthly report details my recent activities, and is available now: https://repo.getmonero.org/monero-project/ccs-proposals/merge_requests/77#note_7105
    [2019-09-02 12:09:11] <sarang> Matching simulation review, updating papers, etc.
    [2019-09-02 12:09:25] <sarang> Nothing earth-shattering over the past few days
    [2019-09-02 12:09:41] <sarang> Very neat to hear about kenshamir[m]'s work on IACR/944
    [2019-09-02 12:09:53] <suraeNoether> yes, i would like to hear more about that
    [2019-09-02 12:10:45] <sarang> Is kenshamir[m] still here?
    [2019-09-02 12:10:59] <kenshamir[m]> Hi
    [2019-09-02 12:11:03] <kenshamir[m]> I’m here
    [2019-09-02 12:11:31] <sarang> Anything specific you'd be interested to share about your recent work on proving systems?
    [2019-09-02 12:11:38] <sarang> (no obligation to do so)
    [2019-09-02 12:11:53] <kenshamir[m]> I think the most notable contribution from 944 that can be applied to bulletproofs straight away is the improved inner product argument
    [2019-09-02 12:12:24] <kenshamir[m]> There are benchmarks which show that it gives significant improvements in verifier and prover efficiency
    [2019-09-02 12:12:55] <mikerah> Is there no meeting today?
    [2019-09-02 12:12:57] <sarang> In the general circuit case, correct?
    [2019-09-02 12:13:02] <sarang> (the meeting is happening now)
    [2019-09-02 12:13:10] <sarang> Not the optimized range proof application AFAICT
    [2019-09-02 12:13:27] <kenshamir[m]> Yeah for 944s proving system it was the general case
    [2019-09-02 12:14:33] <kenshamir[m]> I think if that if we tailored the proof to be specific for 944s proving system, we may be able to get a more efficient rangeproof. This is only a conjecture though and I’m unsure of how to do it at the moment
    [2019-09-02 12:15:04] <sarang> The general case remains extremely interesting
    [2019-09-02 12:15:11] <sarang> since the range proofs are quite efficient
    [2019-09-02 12:15:40] <kenshamir[m]> For the general case asymptotically it is the same as the tailored bulletproofs rangeproofs from what I’ve seen
    [2019-09-02 12:16:19] <kenshamir[m]> Yeah I agree. It will be really interesting to see what optimisations can be made with this language
    [2019-09-02 12:16:36] <kenshamir[m]> *Quadratic Equation Sat
    [2019-09-02 12:16:56] <kenshamir[m]> That’s all I’ve discovered so far from 944
    [2019-09-02 12:17:25] <sarang> Thanks kenshamir[m] 
    [2019-09-02 12:17:35] <sarang> Does anyone else have interesting work to share?
    [2019-09-02 12:18:45] <sarang> Or, for that matter, general questions
    [2019-09-02 12:20:19] <sarang> Righto!
    [2019-09-02 12:20:30] <sarang> We can also move to ACTION ITEMS, if there's nothing else urgent to discuss
    [2019-09-02 12:20:58] <suraeNoether> my action items are short and simple. economarkov chain work, reading more on proofs of knowledge of valid signatures (which i'm considering calling redacted signatures), and my end of month work report.
    [2019-09-02 12:20:59] <sarang> I will be doing some code review, continued work on proving systems, and ongoing work with suraeNoether on his recent updates to graph matching as needed
    [2019-09-02 12:22:40] <sarang> Well, a short meeting today, but that's ok
    [2019-09-02 12:22:47] <sarang> Anything final before we formally adjourn?
    [2019-09-02 12:23:36] <sarang> Adjourned! Thanks to everyone for participating

# Action History
- Created by: SarangNoether | 2019-09-02T14:21:45+00:00
- Closed at: 2019-09-02T19:44:09+00:00
