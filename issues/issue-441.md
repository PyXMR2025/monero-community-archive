---
title: 'Research meeting: 26 February 2020 @ 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/441
author: SarangNoether
assignees: []
labels: []
created_at: '2020-02-20T12:31:51+00:00'
updated_at: '2020-02-26T19:04:17+00:00'
type: issue
status: closed
closed_at: '2020-02-26T19:04:17+00:00'
---

# Original Description
Join in for the weekly Monero Research Lab meeting.

**When**: Wednesday, 26 February 2020 @ 18:00 UTC
**Where**: #monero-research-lab (freenode/matrix)

**Agenda**
1. Greetings

2. Roundtable

3. Questions

4. Action items

# Discussion History
## SarangNoether | 2020-02-26T19:04:17+00:00
    [2020-02-26 13:00:40] <sarang> Hello all, and welcome to the weekly research meeting
    [2020-02-26 13:00:44] <sarang> First, GREETINGS
    [2020-02-26 13:00:45] <sarang> Hi
    [2020-02-26 13:00:55] <UkoeHB_> hi
    [2020-02-26 13:02:03] <ArticMine> hi
    [2020-02-26 13:02:40] — sarang will wait a moment for otheres
    [2020-02-26 13:02:42] <sarang> *others
    [2020-02-26 13:02:51] <xmrmatterbridge> <cankerwort> Peanut gallery quickly checking in to ask what the latest is on return addresses. Last I remember there was an idea to include a subaddress in the tx as a return address. Is that still being being considered?
    [2020-02-26 13:03:27] <sarang> It's always possible to include in tx_extra, which is not consensus
    [2020-02-26 13:03:34] <sarang> and there was a space-minimizing proposal as well
    [2020-02-26 13:03:49] <sarang> AFAIK no one has coded such a thing yet
    [2020-02-26 13:04:34] <sarang> As always, there's a consideration of how optional behavior is bad for indistinguishability
    [2020-02-26 13:04:53] <sarang> Let's go ahead and start the ROUNDTABLE
    [2020-02-26 13:05:01] <sarang> Does anyone have research topics of interest to share?
    [2020-02-26 13:06:06] <sarang> I'll go ahead, then
    [2020-02-26 13:06:27] <sarang> First, the Stanford Blockchain Conference was held this past week
    [2020-02-26 13:06:42] <sarang> Here is a link to the schedule and recordings of talks for each day: https://cbr.stanford.edu/sbc20/
    [2020-02-26 13:07:18] <sarang> Second, a small PR on hash function domain separation was updated, and could always use extra eyes for review: https://github.com/monero-project/monero/pull/6338
    [2020-02-26 13:07:54] <sarang> Third, I made some updates to the structure of CLSAG signature verification code... by reducing the modularity of the signature verification routine to specifically include some commitment offsets, I was able to shave about 5% off the verification time
    [2020-02-26 13:07:59] <sarang> See this branch for details: https://github.com/SarangNoether/monero/tree/clsag-optimized
    [2020-02-26 13:08:09] <Isthmus> Any particular talks that you recommend from SBC?n
    [2020-02-26 13:08:27] <sgp_> hello everyone, catching up on the chat so far
    [2020-02-26 13:08:39] <sarang> Florian's talk about Monero and Zcash side-channel analysis on Wednesday's stream is very good
    [2020-02-26 13:09:03] <sarang> All of session 4 on Wednesday is interesting
    [2020-02-26 13:09:13] <sarang> As is session 5 on Thursday
    [2020-02-26 13:09:46] <sarang> Fourth, I worked on similar improvements for MLSAG... however, this is trickier, since verification requires particular byte-representation hash inputs for backwards compatibility
    [2020-02-26 13:10:03] <sarang> The results for that aren't great: https://github.com/SarangNoether/monero/tree/mlsag-optimized
    [2020-02-26 13:10:09] <Isthmus> Ah I loved that paper
    [2020-02-26 13:10:30] <sarang> Yeah, kudos to Florian and collaborators for great work and responsible disclosure
    [2020-02-26 13:10:43] ⇐ TheoStorm quit (~TheoStorm@host-p8vu8h.cbn1.zeelandnet.nl): Quit: Leaving
    [2020-02-26 13:11:09] <sarang> Finally, another researcher contacted me with an idea for atomic swaps that might remove the need for a SHA-256 preimage proof
    [2020-02-26 13:11:28] <sarang> We're still working out the details, but it's an intriguing idea for which the necessary building blocks already exist
    [2020-02-26 13:11:35] <sarang> More information as we work on it!
    [2020-02-26 13:11:46] <UkoeHB_> interesting, haven't heard from atoc in a while who was looking into that
    [2020-02-26 13:12:16] <sarang> Yeah... I don't want to provide more information until the researcher and I have discussed it (as a courtesy to them)
    [2020-02-26 13:12:20] <sarang> sorry
    [2020-02-26 13:12:41] <Isthmus> Respecting privacy is good ;- )
    [2020-02-26 13:13:02] <sarang> Anyway, those are my updates! Mostly code updates and testing
    [2020-02-26 13:13:08] <sarang> Does anyone else wish to share research of interest?
    [2020-02-26 13:13:59] <UkoeHB_> thanks to sarang 's initial draft, tx knowledge proofs chapter is done (wip tag is off) for ztm2
    [2020-02-26 13:14:04] <UkoeHB_> https://www.pdf-archive.com/2020/02/26/zerotomoneromaster-v1-0-30/zerotomoneromaster-v1-0-30.pdf
    [2020-02-26 13:14:14] <UkoeHB_> chapter 9
    [2020-02-26 13:14:14] <Isthmus> Nice!
    [2020-02-26 13:14:28] <Isthmus> "An Axiomatic Approach to Block Rewards" https://arxiv.org/pdf/1909.10645.pdf
    [2020-02-26 13:14:31] <UkoeHB_> sgp_ may be interested in section 9.3 for audits
    [2020-02-26 13:14:57] <UkoeHB_> reader beware various things arent implemented and are just theoretical
    [2020-02-26 13:15:38] <sarang> Yeah, the idea for a general audit framework is super interesting to me
    [2020-02-26 13:15:54] <sarang> and could be useful to reduce confusion about what proof types provide what information
    [2020-02-26 13:16:02] <sarang> Right now, it's sort of ad-hoc
    [2020-02-26 13:16:08] <xmrmatterbridge> <cankerwort> ZtoM will contain unimplemented features and ideas from the roadmap?
    [2020-02-26 13:16:13] <sarang> Isthmus: that paper is on my literature review list!
    [2020-02-26 13:16:13] <UkoeHB_> also made some updates/fixes to minimum fee change idea https://github.com/monero-project/research-lab/issues/70 @ArticMine
    [2020-02-26 13:16:20] <sgp_> thanks for sharing! I will see if I can get feedback on it
    [2020-02-26 13:16:55] <UkoeHB_> cankerwort part 2 'extensions' contains unimplemented features; saying they are roadmap is quite ambitious
    [2020-02-26 13:17:01] <sarang> One thing to note about the audit idea from UkoeHB_ is that it requires proofs applying to _all_ transactions for which a given output appears in rings
    [2020-02-26 13:17:12] <sarang> which I suspect may require substantial engineering effort (as a guess)
    [2020-02-26 13:17:27] <UkoeHB_> also proofs for every single tx in the chain
    [2020-02-26 13:17:37] <UkoeHB_> for each normal address you own
    [2020-02-26 13:17:37] <sarang> but the benefits of this approach are worth investigation
    [2020-02-26 13:17:38] <sarang> IMO
    [2020-02-26 13:17:56] <UkoeHB_> audits arent trivial for sure
    [2020-02-26 13:18:30] <xmrmatterbridge> <cankerwort> Should be called "ZtoM... and beyond!"
    [2020-02-26 13:18:35] <UkoeHB_> lol yeah
    [2020-02-26 13:18:37] <sgp_> I'm familiar with some people who do Monero audits for businesses so I'll try and get their feedback
    [2020-02-26 13:18:42] <sarang> UkoeHB_: fortunately the proofs are all off-chain anyway
    [2020-02-26 13:18:49] <sarang> So efficiency is much less of a consideration
    [2020-02-26 13:19:02] <UkoeHB_> Id refrain from expecting anything in ZtM that isnt implemented to actually get implemented. They are just ideas
    [2020-02-26 13:19:24] <sarang> UkoeHB_ and I had discussed this very topic earlier... about the intended purpose of ZtM
    [2020-02-26 13:19:32] <sarang> e.g. protocol spec, or something else
    [2020-02-26 13:20:22] <Isthmus> I think that flavoring it with the latest ideas and discussions will convey the lively R & D, provide helpful context, and leave an important historical record
    [2020-02-26 13:20:47] <Isthmus> In 10 years I want to sit down and nostalgically re-read the old "future work" sections
    [2020-02-26 13:20:59] <sarang> heh
    [2020-02-26 13:21:28] <sarang> Anything else to share UkoeHB_?
    [2020-02-26 13:21:33] <sarang> (just to keep the meeting on track)
    [2020-02-26 13:21:39] <UkoeHB_> dont think so
    [2020-02-26 13:21:44] <sarang> Cool, thanks for the update
    [2020-02-26 13:21:52] <sarang> Isthmus: you had chimed in earlier
    [2020-02-26 13:22:00] <sarang> Did you wish to continue with anything else?
    [2020-02-26 13:22:24] <Isthmus> Life has been hectic, so haven't had many Monero moments lately.
    [2020-02-26 13:22:25] <Isthmus> However
    [2020-02-26 13:22:49] <Isthmus> n3ptune was doing some data QC/QA and noticed that in a recent preliminary figure I had missed 100 recent transactions with no payment id (encrypted nor unencrypted)
    [2020-02-26 13:22:58] <Isthmus> But that's a minor difference
    [2020-02-26 13:23:05] <sarang> How recent is "recent"?
    [2020-02-26 13:23:11] <sarang> If you recall
    [2020-02-26 13:23:21] <Isthmus> Probably this version, but idk
    [2020-02-26 13:23:28] <Isthmus> It's only like a 0.5% change over the previously presented data
    [2020-02-26 13:23:41] <Isthmus> I've been working on a little design thought experiment, but it's still rough and maybe more -lounge appropriate
    [2020-02-26 13:23:52] <Isthmus> Otherwise, nothing else to report, that I can think of
    [2020-02-26 13:23:53] <sarang> Got it, thanks
    [2020-02-26 13:24:16] <sarang> I know suraeNoether said he was unavailable, but would provide an update later today on his recent work
    [2020-02-26 13:24:30] <sarang> He's been working on some interesting updates to linkable ring signature security models
    [2020-02-26 13:24:40] <sarang> I've been reviewing those as well
    [2020-02-26 13:24:50] <sarang> Does anyone else wish to share ongoing research?
    [2020-02-26 13:26:04] <sarang> Either specific to something mentioned here, or more generally
    [2020-02-26 13:26:22] <sarang> If not, we can move on to QUESTIONS
    [2020-02-26 13:27:04] — sarang will wait a few minutes if anyone has questions
    [2020-02-26 13:29:11] <sarang> OK, looks like no questions so far
    [2020-02-26 13:29:18] <sarang> Let's move to ACTION ITEMS before closing the meeting
    [2020-02-26 13:29:30] <ArticMine> Feasibility of child pas for parent in Monero (child has parent as one of the mixins)
    [2020-02-26 13:29:40] <sarang> ?
    [2020-02-26 13:29:43] <ArticMine> pays
    [2020-02-26 13:29:46] <sarang> Can you elaborate, ArticMine ?
    [2020-02-26 13:30:24] <ArticMine> In Bitcoin a tx in the tx pool has to low a fee
    [2020-02-26 13:30:30] — sarang rewinds the agenda to QUESTIONS
    [2020-02-26 13:31:09] <sarang> "has to low a fee"?
    [2020-02-26 13:31:10] <ArticMine> A second tx is sent using the tx with to low a fee as an input
    [2020-02-26 13:31:13] <sarang> Sorry, I'm not following
    [2020-02-26 13:31:23] <sarang> ah
    [2020-02-26 13:31:29] <ArticMine> The miner miones both txs in a block
    [2020-02-26 13:32:05] <ArticMine> In the Monero case the child has the tx output of the parent as one of the mixins
    [2020-02-26 13:32:20] <ArticMine> can be real or fake
    [2020-02-26 13:32:38] <sarang> What is the specific question you're getting to?
    [2020-02-26 13:32:56] <Isthmus> Interesting interesting
    [2020-02-26 13:32:59] <ArticMine> Can this e done in Monero
    [2020-02-26 13:33:05] <ArticMine> be
    [2020-02-26 13:33:13] <UkoeHB_> oh is it about what can be done if a tx is stuck since its fee is too low?
    [2020-02-26 13:33:28] <UkoeHB_> e.g. make a new tx with more fee for it
    [2020-02-26 13:33:28] <ArticMine> Yes this can e part of the toolkit
    [2020-02-26 13:33:36] <ArticMine> be
    [2020-02-26 13:34:19] <ArticMine> but in addition to what I am looking at with the fees, etc
    [2020-02-26 13:35:18] <UkoeHB_> we do have 10block lock time atm, so tx spending other tx output doesn't quite work, though there could be new rules around 'in the same block'
    [2020-02-26 13:35:41] <Isthmus> I actually think this seems very plausible
    [2020-02-26 13:35:46] <Isthmus> You wouldn't mine only the bump
    [2020-02-26 13:35:55] <Isthmus> And once the transaction is mined, the bump is unnecessary
    [2020-02-26 13:35:55] ⇐ ferretinjapan quit (ferretinja@gateway/vpn/privateinternetaccess/ferretinjapan): Quit: Leaving
    [2020-02-26 13:36:24] <Isthmus> The bump transaction should have exactly 2 outputs: a plaintext fee and an encrypted change output
    [2020-02-26 13:36:40] <Isthmus> And reference the first transaction by hash
    [2020-02-26 13:36:56] <UkoeHB_> yeah
    [2020-02-26 13:37:04] <sarang> hmm
    [2020-02-26 13:37:15] <UkoeHB_> Im wondering why not just remake the same tx
    [2020-02-26 13:37:19] <UkoeHB_> with more fee
    [2020-02-26 13:37:51] <ArticMine> because of multi sig
    [2020-02-26 13:37:56] <UkoeHB_> ah yeah
    [2020-02-26 13:38:25] <sarang> Huh, that's a very interesting question
    [2020-02-26 13:38:27] — sarang ponders
    [2020-02-26 13:39:43] <Isthmus> Oh, and only 1 bump per transaction
    [2020-02-26 13:39:50] <Isthmus> You can broadcast more if you want, obviously
    [2020-02-26 13:39:59] <Isthmus> But only one bump can be claimed by the miner
    [2020-02-26 13:40:36] <Isthmus> So if you bump with 0.2 XMR then change your mind and send a 0.5 XMR bump, a miner would just ignore the smaller bump
    [2020-02-26 13:40:45] <ArticMine> Yes
    [2020-02-26 13:41:07] <ArticMine> but anyone can do the bump in Monero unlike Bitcoin
    [2020-02-26 13:41:15] <xmrmatterbridge> <cankerwort> Why "becauae of multisig"?
    [2020-02-26 13:41:31] <Isthmus> You could design it either way: allow anybody to bump, or require a signature from the original sender to bump
    [2020-02-26 13:41:39] <Isthmus> (one of the original senders)
    [2020-02-26 13:41:46] <UkoeHB_> sounds like it's possible, although would require protocol level changes (new transaction type, etc)
    [2020-02-26 13:41:48] <midipoet> wouldn't being able to do that (child pays for parent) drastically decrease the overall cost of the chain reaction attack?
    [2020-02-26 13:42:05] <ArticMine> You include the parent as one of the mixins
    [2020-02-26 13:42:15] <Isthmus> @UkoeHB_ I'm only here for the protocol level changes :- P
    [2020-02-26 13:42:31] <xmrmatterbridge> <cankerwort> Also the big bang attack presumably
    [2020-02-26 13:42:44] <ArticMine> The miner does know if the parent is real or not
    [2020-02-26 13:43:13] <UkoeHB_> ArticMine I don't know if the parent needs to be a mixin, just include the parent tx hash as part of bump tx, an additional data field
    [2020-02-26 13:43:39] <ArticMine> That does not mine the parent
    [2020-02-26 13:44:03] <UkoeHB_> It would be a new tx type
    [2020-02-26 13:44:10] <UkoeHB_> 'bump tx'
    [2020-02-26 13:44:17] <ArticMine> Not really
    [2020-02-26 13:44:17] <UkoeHB_> RCTTypeBumpIt
    [2020-02-26 13:44:23] <Isthmus> heh
    [2020-02-26 13:44:33] <sarang> lol
    [2020-02-26 13:44:47] <ArticMine> The point of child pays for parent is that in order to mine the child one has to mine the parent
    [2020-02-26 13:44:57] <sarang> right
    [2020-02-26 13:45:05] <sarang> But that seems straightforward to enforce, no?
    [2020-02-26 13:45:19] <ArticMine> In Bitcoin that means spending the output of the parent in the child
    [2020-02-26 13:45:24] <UkoeHB_> I think you might get into weird 0-conf territory if can spend an output with 0-block lock time
    [2020-02-26 13:45:27] <Isthmus> @cankerwort yeah, though as long as the bump density [XMR per kB] is higher than transaction density [XMR per kB] then they would effectively take up less space (be less effective) for a big bang attack
    [2020-02-26 13:45:34] <UkoeHB_> the 10block lock is there for a reason afaik
    [2020-02-26 13:45:46] <UkoeHB_> just willy nilly
    [2020-02-26 13:46:16] <ArticMine> in Monero it means including it in the ring real or fake. The miner does no know
    [2020-02-26 13:46:43] <Isthmus> Yeah, I think the "bump" transaction needs to be a new type with exactly [fee delta + change] outputs and a new field referencing the transaction hash of the transaction to be accelerated
    [2020-02-26 13:47:08] <Isthmus> And everything is subject to the 10-block lock
    [2020-02-26 13:47:28] <UkoeHB_> or you could make it an optional field in normal tx type, to reduce complexity
    [2020-02-26 13:48:07] <ArticMine> Both are mined in the same block so there is no issue with orphans
    [2020-02-26 13:48:32] <sarang> UkoeHB_: not in extra, right?
    [2020-02-26 13:48:36] <sarang> for parsing etc.
    [2020-02-26 13:48:47] <UkoeHB_> no, unless we start enforcing it
    [2020-02-26 13:49:09] <sarang> aye
    [2020-02-26 13:49:41] <UkoeHB_> interesting idea articmine
    [2020-02-26 13:49:52] <xmrmatterbridge> <cankerwort> Surely the delta could be as small as you like though? So it could be used to make big bang attack cheaper
    [2020-02-26 13:50:11] <UkoeHB_> big bang is about total block weight
    [2020-02-26 13:50:35] <UkoeHB_> still have to pay fee for bump tx too
    [2020-02-26 13:51:03] <xmrmatterbridge> <cankerwort> Ie you are adding 2 transactions for one fee?
    [2020-02-26 13:51:15] <Isthmus> The fee in the bump has to cover both the weight of the bump itself and the original transaction
    [2020-02-26 13:51:34] <xmrmatterbridge> <cankerwort> Ah
    [2020-02-26 13:51:44] <Isthmus> So if I have a 5 kB txn and a 2 kB bump, then the total fee has to incentivize the miner to include 7 kB
    [2020-02-26 13:52:00] <ArticMine> Yes enough to provide an incentive the miner
    [2020-02-26 13:52:32] <ArticMine> That is the point of child pas for parent also in Bitcoin
    [2020-02-26 13:52:41] <sarang> Quick note that we should try to finish up soon, since Konferenco has a meeting in a few minutes
    [2020-02-26 13:52:43] <ArticMine> pays
    [2020-02-26 13:52:50] <sarang> May we quickly review action items, and then continue discussion?
    [2020-02-26 13:53:01] <ArticMine> Yes of course
    [2020-02-26 13:53:07] — sarang apologizes for interrupting discussion :/
    [2020-02-26 13:53:20] <sarang> I'll be working on some review for vtnerd's 64-bit operation code
    [2020-02-26 13:53:25] <sarang> as well as some Triptych coding for timing purposes
    [2020-02-26 13:53:30] <sarang> Others?
    [2020-02-26 13:54:45] <sarang> OK, then let's formally adjourn for log posting purposes... please continue discussion!
    [2020-02-26 13:55:10] <sarang> Thanks to everyone for attending


# Action History
- Created by: SarangNoether | 2020-02-20T12:31:51+00:00
- Closed at: 2020-02-26T19:04:17+00:00
