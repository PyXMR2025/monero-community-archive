---
title: 'Research meeting: 22 July 2020 @ 17:00 UTC'
source_url: https://github.com/monero-project/meta/issues/490
author: SarangNoether
assignees: []
labels: []
created_at: '2020-07-20T15:34:06+00:00'
updated_at: '2020-07-22T18:06:38+00:00'
type: issue
status: closed
closed_at: '2020-07-22T18:06:38+00:00'
---

# Original Description
Join in for the weekly Monero Research Lab meeting.

**When**: Wednesday, 22 July 2020 @ 17:00 UTC
**Where**: #monero-research-lab (freenode/matrix)

**Agenda**
1. Greetings

2. Roundtable

3. Questions

4. Action items

# Discussion History
## Mitchellpkt | 2020-07-22T16:27:15+00:00
I might not be able to make this meeting due to a schedule conflict. Two quick updates:

1) Adam and I have completed the first phase of the [quantum research CCS](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/142). Who/where should we share the update to get that reviewed and marked off?

2) We briefly discussed zero-fee/zero-value transactions last week, which [may be a spam risk](https://github.com/Mitchellpkt/stingy_spammer) depending on default miner behavior. Just a quick note that a [proof of concept](https://forum.zcashcommunity.com/t/possible-to-generate-a-transaction-with-0-zec/36826/2?u=mitchellpkt) was executed on the Zcash mainnet last week. 

## SarangNoether | 2020-07-22T16:41:14+00:00
> 1. Who/where should we share the update to get that reviewed and marked off?

If there are any active vulnerabilities, please use [HackerOne](https://hackerone.com/monero?type=team) to report. Otherwise, the usual method is to post reports (or links to them) as comments on the merge request.

## SarangNoether | 2020-07-22T18:06:38+00:00
    [2020-07-22 12:00:18] <sarang> OK, let's get started!
    [2020-07-22 12:00:26] <sarang> The usual agenda: https://github.com/monero-project/meta/issues/490
    [2020-07-22 12:00:30] <sarang> First, GREETINGS
    [2020-07-22 12:00:51] <h4sh3d[m]> Hello
    [2020-07-22 12:01:09] <sgp_> hello
    [2020-07-22 12:01:42] <sethsimmons> Hi all
    [2020-07-22 12:02:45] <sarang> Let's move to ROUNDTABLE, where anyone can share research topics of interest with the channel
    [2020-07-22 12:03:04] <sarang> Note that Isthmus posted a few items on the agenda and said he would be unable to attend today
    [2020-07-22 12:03:18] <sarang> He linked this: https://github.com/Mitchellpkt/stingy_spammer
    [2020-07-22 12:03:48] <sarang> and noted some related work in Zcash that showed a 0-value/0-fee transaction could be mined, posing a spam risk
    [2020-07-22 12:04:24] <sarang> and further, that even if not relayed, such transactions could be mined if not disallowed by the protocol (not specific to Zcash, of course)
    [2020-07-22 12:05:43] <sarang> It is certainly the case that the Monero protocol also does not verify that the sum of spent inputs is strictly greater than zero
    [2020-07-22 12:05:56] <h4sh3d[m]> How does this apply to Monero?
    [2020-07-22 12:06:28] <sarang> It would apply if miners can mine 0-fee transactions, since this means it would be free to spam the network
    [2020-07-22 12:06:28] <h4sh3d[m]> Is there a verification for sum(inputs)>0
    [2020-07-22 12:06:38] <sarang> Nope, this is not the case
    [2020-07-22 12:06:50] <sarang> Range proofs allow zero value
    [2020-07-22 12:08:33] <ArticMine> but the miner wold have to pay the penalty on the spam
    [2020-07-22 12:08:37] <ArticMine> ikn Monero
    [2020-07-22 12:09:02] <sarang> h4sh3d[m]: and it's important for distinguishability of "fake change" that zero values look the same
    [2020-07-22 12:09:17] <ArticMine> So the economics are very different
    [2020-07-22 12:09:23] <sarang> ArticMine: well, at a certain point
    [2020-07-22 12:09:27] <sarang> If penalty-free, no problem
    [2020-07-22 12:09:50] <ArticMine> Yes up to the penalty free zone
    [2020-07-22 12:10:02] <sarang> Enforcing minimum fees at the protocol level would mitigate this risk
    [2020-07-22 12:10:12] <ArticMine> but this is not in the miner's interest
    [2020-07-22 12:10:13] <sarang> but I know this has been brought up before
    [2020-07-22 12:10:33] <ArticMine> Enforcing fees at the protocol does not mitigate this risk
    [2020-07-22 12:10:39] <sarang> The existence of a penalty zone is certain a disincentive at some point
    [2020-07-22 12:10:58] <h4sh3d[m]> Can the block size grow if you are under the penalty-fee?
    [2020-07-22 12:11:09] <sarang> How would it not mitigate? It at least ensures that the spammer has to pay something
    [2020-07-22 12:11:18] <moneromooo> The miner would pay himself.
    [2020-07-22 12:11:29] <ArticMine> The miner just pays out of one pocket to the other
    [2020-07-22 12:11:35] <sarang> Oh, you mean in the case that the miner chooses to execute the spam attack, sure
    [2020-07-22 12:11:47] <sarang> can't remove that risk in the penalty-free zone
    [2020-07-22 12:12:09] <sarang> but it does mean that a non-miner user can't trivially execute the spam
    [2020-07-22 12:12:40] <ArticMine> The non miner has to deal with node relay minimum fees
    [2020-07-22 12:13:04] <ArticMine> on top of the penalty
    [2020-07-22 12:13:29] <moneromooo> If a miner exposes their sendrawtransaction RPC, someone could send 0 fee txes this way.
    [2020-07-22 12:13:39] <ArticMine> It is also in the interest of the miner to allow for fluctuation in the block weight
    [2020-07-22 12:13:59] <ArticMine> ... and have the miner pay the penalty for the spam
    [2020-07-22 12:16:31] <sarang> Anyway, might be useful to bring up at the next dev meeting, to see if there are mitigations that receive general agreement
    [2020-07-22 12:17:21] ⇐ sech1 quit (~sech1@31-208-56-12.cust.bredband2.com): Read error: Connection reset by peer
    [2020-07-22 12:17:58] <ArticMine> Also as Monero mature the penalty free zone is below the block weight
    [2020-07-22 12:18:27] <ArticMine> So this attack becomes moot
    [2020-07-22 12:19:59] → sech1 joined (~sech1@31-208-56-12.cust.bredband2.com)
    [2020-07-22 12:20:00] <sarang> Well, something to keep in mind... if non-miners users can easily produce such spam and it gets mined, it's a problem
    [2020-07-22 12:20:26] <sarang> I have a few things to share
    [2020-07-22 12:20:36] <moneromooo> I guess forcing a min fee also removes a way to get fingerprinted.
    [2020-07-22 12:21:03] <sarang> I made a couple of PRs to finally jettison old JS analytics code from CCS and the main getmonero site, which isn't really research :)
    [2020-07-22 12:21:11] <ArticMine> It simple cannot be enforced because of out of bounds payments / refunds
    [2020-07-22 12:21:17] <sarang> The audit is finally closing
    [2020-07-22 12:21:19] <sarang> for CLSAG
    [2020-07-22 12:21:51] <sarang> We're finalizing the report with OSTIF and the reviewers, and I have a blog post ready to go that explains CLSAG and the audit results, which were helpful and positive
    [2020-07-22 12:22:04] <sarang> moneromooo has rebased the code, so it's ready for testing
    [2020-07-22 12:22:24] <sarang> Trezor support will be there for the upgrade
    [2020-07-22 12:22:34] <sarang> still working with Ledger on some scheduling problems, unfortunately
    [2020-07-22 12:22:58] <sarang> And I updated some code and tests for transaction proofs and message signing
    [2020-07-22 12:23:36] <sarang> Any questions or comments on these topics?
    [2020-07-22 12:26:10] <sarang> There is a proposal for a research team to implement Bulletproofs+ in Monero: https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/156
    [2020-07-22 12:27:33] <sarang> The numbers they get for verification seem better than when I had first looked at estimates, but they've since provided information on operation counts that I think are much better than from specific implementations
    [2020-07-22 12:30:05] <sarang> Any thoughts on BP+ in Monero?
    [2020-07-22 12:30:26] <sarang> Regardless of the actual verification benefits, the size benefits are certain
    [2020-07-22 12:30:34] <moneromooo> If they're smaller and faster and just incremental code changes, yes please.
    [2020-07-22 12:31:26] <h4sh3d[m]> does the transaction structure changes with the proof size reduction?
    [2020-07-22 12:31:29] <sarang> When first brought up a while back (when the preprint came out), it seemed like there were some questions on using something so new for a marginal (but certainly nontrivial) benefit
    [2020-07-22 12:31:36] <sarang> h4sh3d[m]: what do you mean?
    [2020-07-22 12:31:42] <sarang> The proofs contain different elements, sure
    [2020-07-22 12:31:57] <sarang> Nothing else changes (except standard transaction weights)
    [2020-07-22 12:32:22] <h4sh3d[m]> So de/serialization of transaction changes
    [2020-07-22 12:33:03] <sarang> Sure
    [2020-07-22 12:33:12] <h4sh3d[m]> Ok
    [2020-07-22 12:33:15] <sarang> It did for BP, it does for CLSAG, etc.
    [2020-07-22 12:33:23] <sarang> I don't think that's a reason not to do it
    [2020-07-22 12:33:41] <sarang> I assume it'd be a consensus requirement, so no issues there
    [2020-07-22 12:34:01] <h4sh3d[m]> Me neither, just wondering
    [2020-07-22 12:34:15] <moneromooo> How comfortable are you with the safety of the changes, mathematically ?
    [2020-07-22 12:34:24] <moneromooo> (since you mention "something so new").
    [2020-07-22 12:35:25] <sarang> The construction appears sound and correct
    [2020-07-22 12:35:49] <sarang> but it hasn't received formal external review yet
    [2020-07-22 12:36:03] <sarang> That's no guarantee of correctness, but it is useful
    [2020-07-22 12:36:24] <sarang> FWIW it's not like the math expires, if it were decided to wait until the preprint gets more eyes on it
    [2020-07-22 12:36:50] <sarang> The downside would be the sunk cost of heavier proofs on chain
    [2020-07-22 12:37:24] <sarang> BPs were also new, but they received a _lot_ of good review and attention from a lot of researchers
    [2020-07-22 12:37:57] <sarang> You could easily argue that not that many people have done thorough review of CLSAG either, though
    [2020-07-22 12:38:14] <ArticMine> The trade-off is mathematical risk vs heavy transactions. It can be a very delicate one
    [2020-07-22 12:40:59] <sarang> Yeah. I don't doubt that the proposers did a thorough review of the BP+ preprint, as it appears they have
    [2020-07-22 12:44:42] <sarang> Anyway, certainly a proposal worth considering
    [2020-07-22 12:44:45] ⇐ hashcashjoe quit (~joe@rrcs-71-42-95-124.sw.biz.rr.com): Ping timeout: 240 seconds
    [2020-07-22 12:44:52] <sarang> Did anyone else have topics they wish to share?
    [2020-07-22 12:46:10] <h4sh3d[m]> Yep. I nearly finished the researched funded by the CCS on atomic swap
    [2020-07-22 12:46:19] <h4sh3d[m]> The paper has just been updated
    [2020-07-22 12:46:43] <sarang> Excellent! Link?
    [2020-07-22 12:46:51] <h4sh3d[m]> sarang: if you find time to have a look, I'd appreciate some feedback
    [2020-07-22 12:46:55] <h4sh3d[m]> https://github.com/h4sh3d/xmr-btc-atomic-swap/blob/master/whitepaper/xmr-btc.pdf
    [2020-07-22 12:47:19] <sarang> Happy to
    [2020-07-22 12:47:20] <h4sh3d[m]> and feedback from all of you too!
    [2020-07-22 12:48:21] <h4sh3d[m]> I'm happy with the results and I'll have a better look at what you did in MRL-0010
    [2020-07-22 12:48:35] <sarang> ^ what andytoshi did
    [2020-07-22 12:48:42] <h4sh3d[m]> As it is one of the two "new" cryptographic primitives used in the scheme
    [2020-07-22 12:49:44] <h4sh3d[m]> yes, andytoshi was the first to talk about it, you wrote the tech note!
    [2020-07-22 12:50:45] <h4sh3d[m]> Anyway, feedbacks are welcome and thanks for the inputs from the last months. I'll write on reddit a summary of the research soon
    [2020-07-22 12:51:16] <sarang> Thanks h4sh3d[m]
    [2020-07-22 12:51:27] <sarang> Any other topics folks wish to bring up, before we move along?
    [2020-07-22 12:53:14] <sarang> OK, then on to ACTION ITEMS
    [2020-07-22 12:54:16] <sarang> I'll finish up some tests on some older code and PRs, see if we can get the audit report posted publicly, continue some investigation of BP+ specifics, and finish up CLSAG testing
    [2020-07-22 12:54:21] <sarang> Anyone else?
    [2020-07-22 12:56:41] <sarang> All right, in that case, we are adjourned!


# Action History
- Created by: SarangNoether | 2020-07-20T15:34:06+00:00
- Closed at: 2020-07-22T18:06:38+00:00
