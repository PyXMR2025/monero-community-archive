---
title: Monero Research Lab Meeting - 13 January 2021 @ 17 UTC
source_url: https://github.com/monero-project/meta/issues/542
author: SamsungGalaxyPlayer
assignees: []
labels: []
created_at: '2021-01-12T17:37:50+00:00'
updated_at: '2021-01-13T18:35:21+00:00'
type: issue
status: closed
closed_at: '2021-01-13T18:35:21+00:00'
---

# Original Description
Time: 17 UTC

Location: #monero-research-lab

Main discussion topics: 

* Bulletproofs+ audit(s)
* Triptych / Arcturus
* v15 ringsize

# Discussion History
## SamsungGalaxyPlayer | 2021-01-13T18:35:21+00:00
```
[2021-01-13 11:00:58] <sgp_> Monero Research Lab meeting time
[2021-01-13 11:01:08] <sgp_> Greetings
[2021-01-13 11:01:57] <sgp_> ping sarang moneromooo SerHack ArticMine binaryFate 
[2021-01-13 11:02:06] <sgp_> knaccc 
[2021-01-13 11:02:35] <sarang> hi
[2021-01-13 11:02:40] <sgp_> dEBRUYNE
[2021-01-13 11:02:46] <sgp_> needmoney90
[2021-01-13 11:03:09] <sgp_> it's been a while since the last meeting, hope everyone is doing okay :)
[2021-01-13 11:04:50] <sgp_> https://github.com/monero-project/meta/issues/542
[2021-01-13 11:05:04] <sgp_> I'm going to proceed and hope other people perk up
[2021-01-13 11:05:19] <sgp_> 1. Bulletproofs+ audit(s)
[2021-01-13 11:05:26] <sgp_> this is the most pressing matter
[2021-01-13 11:05:51] <sgp_> https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/197
[2021-01-13 11:06:07] <sgp_> it's been 3 weeks since they opened the proposal
[2021-01-13 11:06:32] <sgp_> sarang: you had questions, were those answered sufficiently?
[2021-01-13 11:07:00] <sarang> They were! The scope is broad so it really comes down to perceived community value
[2021-01-13 11:07:17] <sgp_> in the last community meeting, they wanted to wait for a decision here before moving the CCS or not
[2021-01-13 11:07:33] <sgp_> sarang: can you expand on what you mean by "the scope is so broad"?
[2021-01-13 11:07:54] <sarang> Well they intend to do review of the preprint, review of our code, and also compare to some other implementations
[2021-01-13 11:08:01] <sarang> Which is great to have!
[2021-01-13 11:08:16] <sarang> I happen to think it's a good value, but this is not my call
[2021-01-13 11:08:31] <sgp_> which part is the most "overkill" perhaps, the comparison?
[2021-01-13 11:08:43] <sarang> I don't want to call it overkill
[2021-01-13 11:08:50] <sarang> But if we had to choose something to nix, I'd say that
[2021-01-13 11:08:56] <sgp_> understood
[2021-01-13 11:09:00] <sarang> That being said, higher assurance is always a good thing
[2021-01-13 11:09:58] <sgp_> the scope seems relatively reasonable to me since they are proposing 1 month of work
[2021-01-13 11:10:39] <sgp_> if there's value in the comparison in your opinion, it seems reasonable to include
[2021-01-13 11:11:12] <sgp_> do people feel comfortable with just this one audit, or should we also hunt down others?
[2021-01-13 11:11:48] <sarang> sgp_: I think that the value is good for the proposed cost
[2021-01-13 11:12:01] <sarang> If it had inflated the price too much, perhaps that'd be a different story
[2021-01-13 11:12:02] <sgp_> and do we generally feel comfortable in these auditors' competencies?
[2021-01-13 11:12:20] <sarang> I can't personally vouch for them, but they do have good work out there
[2021-01-13 11:12:58] <sgp_> okay, so signs point to suggesting this is moved as-is
[2021-01-13 11:13:08] <Isthmus> +1
[2021-01-13 11:13:09] <sarang> I don't have any particular qualms, FWIW
[2021-01-13 11:13:27] <Isthmus> Best case scenario, they are good team and we receive solid audit. Worst case scenario, an audit can't make things worse :- )
[2021-01-13 11:13:51] <dEBRUYNE> False sense of security is a drawback I'd argue
[2021-01-13 11:13:52] <sgp_> well, worst case they give an audit that looks good and gives undeserved confidence
[2021-01-13 11:13:56] <dEBRUYNE> (in case of a bad audit)
[2021-01-13 11:14:13] <dEBRUYNE> I'd still prefer to have a second team looking at it, even if the scope isn't that broad
[2021-01-13 11:14:20] <dEBRUYNE> Especially since we're touching delicate parts of the code
[2021-01-13 11:14:22] <sgp_> should we be looking for other auditors now, or later after reviewing the report?
[2021-01-13 11:14:30] <sarang> Perhaps having another limited-scope audit?
[2021-01-13 11:14:36] <dEBRUYNE> I'd say before
[2021-01-13 11:14:37] <sarang> Just the proposed code
[2021-01-13 11:14:41] <sgp_> I don't see this in any case being a blocker on moving the current audit
[2021-01-13 11:14:49] <dEBRUYNE> I think another 'just code' audit would be fine
[2021-01-13 11:14:50] <Isthmus> +1 sgp
[2021-01-13 11:15:09] <ErCiccione[m]> Another audit only for the code sounds like a good idea
[2021-01-13 11:15:20] <sgp_> dEBRUYNE sarang Isthmus: any recommendations on how to reach out to others for the code-only audit?
[2021-01-13 11:15:43] <sgp_> should we just cold email Quarkslab, Kudelski, etc?
[2021-01-13 11:15:46] <dEBRUYNE> Through OSTIF I guess?
[2021-01-13 11:15:49] <gingeropolous> +1 for second audit.
[2021-01-13 11:15:54] <dEBRUYNE> They acted as intermediary in the past
[2021-01-13 11:16:09] <Isthmus> Who have we engaged with previously, and would they be a good fit for this?
[2021-01-13 11:16:29] <sgp_> fwiw, the Monero Audit workgroup was unimpressed with their assistance last time
[2021-01-13 11:16:32] <hyc> we have gone thru OSTIF to the auditors
[2021-01-13 11:16:41] <dEBRUYNE> sgp_: Of OSTIF, that is?
[2021-01-13 11:16:43] <sgp_> yes
[2021-01-13 11:17:02] <dEBRUYNE> I guess reaching out through OSTIF creates a sense of goodwill, but afaik it also increases the price
[2021-01-13 11:17:04] <hyc> what were the problems? things were pretty smooth for the randomx work
[2021-01-13 11:17:19] <sgp_> 1) we probably didn't actually get a cheaper rate, 2) the conversations usually resulted in more confusion, not less
[2021-01-13 11:17:36] <sgp_> and yes they want 10%
[2021-01-13 11:17:41] <hyc> ok
[2021-01-13 11:18:16] <sgp_> sarang: do you have email contacts for everyone we have worked with in the past?
[2021-01-13 11:18:29] <sarang> I do, yes
[2021-01-13 11:19:10] <dEBRUYNE> To maintain proper relations I think it would be better to consult OSTIF, but that's my personal opinion
[2021-01-13 11:19:12] <sgp_> okay, anyone against starting there by contacting them with our desired project and scope? sarang I can handle more of the email communication to save you time
[2021-01-13 11:19:39] <gingeropolous> and I thought ostif was necessary because the auditors have to work with some corporate entity of somekind
[2021-01-13 11:20:40] <sgp_> gingeropolous: I'm not sure, if they need an entity, we can reconsider
[2021-01-13 11:20:51] <dEBRUYNE> I think that's mostly for tax reasons, not sure
[2021-01-13 11:21:11] <sgp_> tax reasons would be for the benefit of the donors
[2021-01-13 11:21:33] <gingeropolous> k. but yeah, thats a good starting point.
[2021-01-13 11:21:46] <sgp_> okay, it's my recommendation we start there
[2021-01-13 11:23:13] <sgp_> any other comments on this topic?
[2021-01-13 11:23:29] <sgp_> in summary: move the CCS, and then look for a second, narrower audit
[2021-01-13 11:23:36] <sarang> Cool
[2021-01-13 11:23:47] <sarang> We can specifically limit the code scope
[2021-01-13 11:24:20] <sgp_> sarang: please contact me after so we can get the emails out
[2021-01-13 11:24:37] <sgp_> if anyone wants to help with the audit workgroup, please DM me
[2021-01-13 11:24:47] <sarang> can do
[2021-01-13 11:24:53] <sgp_> okay, next topic
[2021-01-13 11:25:03] <sgp_> Triptych / Arcturus
[2021-01-13 11:25:23] <sgp_> first important question on my end:
[2021-01-13 11:25:55] <sgp_> is Arcturus out? is there anything that could change/happen to make us feel comfortable with this?
[2021-01-13 11:27:33] <sarang> Well, there is a Rust implementation, which is pretty great
[2021-01-13 11:27:40] <sarang> But AFAIK no other review
[2021-01-13 11:27:51] <sgp_> (I'm afk for a few, emergency sorry)
[2021-01-13 11:28:21] <dEBRUYNE> Not sure what is withholding us from starting to work on implementing Triptych
[2021-01-13 11:28:42] <dEBRUYNE> I think people already reconciled the fact that multisig would require a bit more of a complex implementation
[2021-01-13 11:30:30] <Isthmus> gl sgp
[2021-01-13 11:31:34] <Isthmus> @sarang is the rust implementation public?
[2021-01-13 11:31:58] — Isthmus wants to poke through the repo
[2021-01-13 11:31:59] <sarang> It is!
[2021-01-13 11:32:21] <sarang> https://github.com/cargodog/arcturus
[2021-01-13 11:32:24] <sgp_> half back
[2021-01-13 11:32:39] <Isthmus> Thanks @sarang
[2021-01-13 11:32:40] <sgp_> is there any way we would run with something like this though?
[2021-01-13 11:32:47] <sgp_> there's that one assumption
[2021-01-13 11:33:17] <sarang> Arcturus is inherently riskier, given its novel assumption
[2021-01-13 11:33:17] <Isthmus> Oh yea, what's the non-standard assumption? I don't quite recall
[2021-01-13 11:33:32] <sgp_> how can we reduce risk?
[2021-01-13 11:33:38] <sgp_> or is that not really possible
[2021-01-13 11:34:03] <sarang> Time and solid peer review
[2021-01-13 11:34:13] <dEBRUYNE> A break would have pretty catastrophic ramifications
[2021-01-13 11:34:16] <sarang> But "review" of an assumption is much different than review of an implementation
[2021-01-13 11:34:21] <sarang> correct
[2021-01-13 11:34:22] <dEBRUYNE> I argue it would be prudent to 'play it safe' and opt for Triptych
[2021-01-13 11:34:35] <gingeropolous> aye
[2021-01-13 11:34:50] <dEBRUYNE> The differences are not large enough to warrant choosing an implementation that relies on a novel assumption
[2021-01-13 11:34:58] <gingeropolous> double aye
[2021-01-13 11:35:41] <sgp_> is anyone here interested in arctutus at all then
[2021-01-13 11:35:46] <sgp_> or should we stop talking about it
[2021-01-13 11:36:05] <sgp_> personally, I would feel okay with a really good review of it
[2021-01-13 11:36:23] <ArticMine> Sorry I am late. My take on Arcturus is that the assumption risk will take time. So it can be implemented after Triptych
[2021-01-13 11:36:57] <Isthmus> That all seems reasonable
[2021-01-13 11:37:07] — Isthmus nods in general agreement
[2021-01-13 11:37:18] <sgp_> okay, anyone not in favor of focusing entirely on triptych for now?
[2021-01-13 11:37:56] <moneromooo> Do those two share most code ?
[2021-01-13 11:38:08] <sarang> The structure is similar
[2021-01-13 11:38:08] <sgp_> sarang: ^
[2021-01-13 11:38:26] <sarang> But there are significant internal differences still
[2021-01-13 11:38:50] <sgp_> for the record, who is for focusing entirely on triptych
[2021-01-13 11:39:03] <ArticMine> I am
[2021-01-13 11:39:30] <sethsimmons> <sgp_ "for the record, who is for focus"> I am as well.
[2021-01-13 11:39:36] <moneromooo> I'd say yes, on balance. Not a huge preference.
[2021-01-13 11:39:44] <dEBRUYNE> Triptych is my preference
[2021-01-13 11:39:46] — dEBRUYNE brb
[2021-01-13 11:39:53] <sethsimmons> Lets focus on the clearest next step and then think more about Arcturus later if needed.
[2021-01-13 11:40:12] <sethsimmons> Not enough clear wins in Arcturus to offset the novel assumptions IMO.
[2021-01-13 11:40:15] <sgp_> my guess is that we will never use Arcuturus since ideally there will be a bigger breakthrough in a few years
[2021-01-13 11:40:26] <sarang> FWIW the key image structure is identical between the two anyway
[2021-01-13 11:40:29] <sethsimmons> Most likely, and thats not a bad thing I don't think.
[2021-01-13 11:40:34] <sarang> So an output migration between them is not needed
[2021-01-13 11:40:40] <sarang> Very similarly to how we did MLSAG->CLSAG
[2021-01-13 11:40:48] <sethsimmons> Triptych is a large step forward and will buy a lot of time for the next arms race.
[2021-01-13 11:40:54] <sarang> Output migration _is_ needed from CLSAG->{Arcturus,Triptych}
[2021-01-13 11:41:22] <sgp_> okay, so for triptych, what is the next step
[2021-01-13 11:41:28] <sgp_> funding for sarang?
[2021-01-13 11:41:33] <sarang> Is multisig important?
[2021-01-13 11:41:46] <sgp_> oh good point
[2021-01-13 11:41:50] <sgp_> quick vote
[2021-01-13 11:41:57] <sarang> Big remaining issues are output set binning/selection/representation, output migration concerns, and multisig if applicable
[2021-01-13 11:42:01] <ArticMine> I say yes
[2021-01-13 11:42:02] <moneromooo> It is.
[2021-01-13 11:42:06] <sethsimmons> <sarang "Is multisig important?"> Does Arcturus not cause the same issues as Triptych?
[2021-01-13 11:42:12] <sarang> The prove/verify code is already present and working
[2021-01-13 11:42:15] <ErCiccione[m]> it is, yes
[2021-01-13 11:42:24] <sarang> Multisig code is not, and is highly nontrivial
[2021-01-13 11:42:35] <sgp_> Is lack of current hardware wallet support for multisig wallets a blocker, yes/no
[2021-01-13 11:42:43] <moneromooo> No.
[2021-01-13 11:42:46] <ArticMine> No
[2021-01-13 11:42:48] <sethsimmons> no.
[2021-01-13 11:42:57] <sgp_> I also think no
[2021-01-13 11:43:05] <sethsimmons> It's such a tiny, tiny percentage of users
[2021-01-13 11:43:23] <sethsimmons> Better to drastically improve the default privacy assumptions for all users than delay for a tiny subset of those users.
[2021-01-13 11:44:03] <sarang> To be clear, we do have a way to handle multisig, but it requires additional code and library support for more general group structures (RSA groups)
[2021-01-13 11:44:35] <sarang> I do not have the expertise in hardware device limitations to know the extent to which this is reasonable on those devices
[2021-01-13 11:44:39] <sethsimmons> Does that need a HF to implement?
[2021-01-13 11:44:46] <sarang> Multisig? No
[2021-01-13 11:44:50] <sethsimmons> Or could it be added after the initial Triptych implementation?
[2021-01-13 11:44:53] <sarang> You can't tell if a txn uses multisig
[2021-01-13 11:44:59] <sarang> It's entirely separate
[2021-01-13 11:45:07] <sethsimmons> Ah, ok, that makes it much clearer than to forgo blocking on multisig
[2021-01-13 11:45:12] <ArticMine> Then I suggest the route is to get Multisig working on triptych
[2021-01-13 11:45:16] <sethsimmons> Can focus on initial imp then pivot to musig after.
[2021-01-13 11:45:24] <sarang> Sure, but if the answer is "Triptych multisig cannot work on our limited hardware devices" then that could be a blocker
[2021-01-13 11:45:28] <sethsimmons> Or if there are resources work on them in parallel
[2021-01-13 11:45:36] <sgp_> it's not a blocker
[2021-01-13 11:45:53] <sarang> OK, just wanted to make it clear that it could be the case that multisig will never practically work on those devices
[2021-01-13 11:45:57] <sgp_> screw current hardware wallet support for multisig wallets
[2021-01-13 11:45:58] <ArticMine> Not every user has to use the limited hardware
[2021-01-13 11:45:59] <sarang> I don't know enough to say for sure
[2021-01-13 11:46:01] <sgp_> very worthy tradeoff
[2021-01-13 11:46:10] <Lyza> yeah as long as multisig works I don't think HW devices are essential, and besides they'll likely catch up at some point
[2021-01-13 11:46:38] <sarang> Note that the multisig approach is based on known techniques, but would warrant additional scrutiny and review
[2021-01-13 11:46:54] <sarang> I have some basic code demonstrating it in Python
[2021-01-13 11:47:12] <sarang> (usual DANGER DANGER disclaimer that research code is not reviewed and unsuitable for production use)
[2021-01-13 11:47:53] <sgp_> okay, so what are the immediate next steps
[2021-01-13 11:48:06] <ArticMine> The proper process of scrutiny and review has to be followed but I do see a clear part here
[2021-01-13 11:48:10] <sarang> https://github.com/SarangNoether/skunkworks/tree/inverse-mpc
[2021-01-13 11:48:17] <ArticMine> path
[2021-01-13 11:48:39] <sarang> ^ that's the code and algorithm descriptions
[2021-01-13 11:51:51] <dEBRUYNE> ArticMine: I think sarang means that multisig for 'normal' devices is possible (albeit sophisticated and complex)
[2021-01-13 11:51:57] <dEBRUYNE> But is ruled out for hardware wallets (devices)
[2021-01-13 11:52:03] <dEBRUYNE> E.g. Ledger & Trezor
[2021-01-13 11:52:13] <ArticMine> Which is fine
[2021-01-13 11:52:19] <sarang> Not necessarily ruled out... but would require a lot of other plumbing
[2021-01-13 11:52:30] <sarang> Again, I don't have the expertise to make that conclusion
[2021-01-13 11:52:43] <ArticMine> Since not all users need to use hardware wallets
[2021-01-13 11:52:52] <dEBRUYNE> There is arguably little benefit currently to pursuing Triptych multisig for hw wallet devices
[2021-01-13 11:53:10] <dEBRUYNE> ArticMine: And they would be able to use a 'standard' Ledger / Trezor Monero wallet with Triptych
[2021-01-13 11:53:41] <ArticMine> That is my point
[2021-01-13 11:53:43] <moneromooo> I don't think we need to care whether it's doable atm. Just add triptych, then software MS, then people from ledger/trezor will work out whether they can. If not, tough.
[2021-01-13 11:53:54] <sgp_> yeah pretty much
[2021-01-13 11:53:59] <Lyza> +1
[2021-01-13 11:54:19] <sgp_> so what's next for adding triptych
[2021-01-13 11:54:24] <sgp_> what needs to happen first
[2021-01-13 11:54:45] <sarang> Analysis and decisions around output selection and representation and binning
[2021-01-13 11:54:51] <sarang> Review
[2021-01-13 11:54:55] <sarang> Consensus code
[2021-01-13 11:55:05] <sarang> Multisig, if desired (lots of work on this one)
[2021-01-13 11:55:14] <moneromooo> With the caveat that, while designing software MS, if two implementation options are equally possible but one is thought to be much easier on hw, that gives it a better chance of being chosen, ceteris paribus.
[2021-01-13 11:55:14] <sgp_> output selection is an area for potential improvement, but could theoretically be implemented with current alo right?
[2021-01-13 11:55:18] <sgp_> s/slo/algo
[2021-01-13 11:56:18] <ArticMine> Multisig for regular hardware
[2021-01-13 11:56:33] <sarang> If you're selecting large output sets, using binning has many benefits, including size
[2021-01-13 11:56:47] <sarang> You don't want to do individual representations of each output, presumably...
[2021-01-13 11:56:58] <dEBRUYNE> sarang: And I guess a way of funding too
[2021-01-13 11:57:52] <sgp_> sarang: I see output selection as a side optimization project
[2021-01-13 11:58:01] <sgp_> not as a blocker
[2021-01-13 11:58:17] <moneromooo> I'd be interested in partial caching of crypto ops with binning, to cut off some constant from O(N) in verification time.
[2021-01-13 11:58:22] <moneromooo> If at all possible.
[2021-01-13 12:00:05] <sarang> Depends how you bin, but sure
[2021-01-13 12:00:19] <sarang> And we can reuse output sets between Triptych proofs in the same transaction (my analysis numbers assume this)
[2021-01-13 12:01:16] <sgp_> when you say "review" do you mean an audit of the paper? audit of the code? both?
[2021-01-13 12:01:42] <sarang> I'd say both
[2021-01-13 12:01:58] <sarang> Dedicated peer review in addition to academic peer review provides higher assurance
[2021-01-13 12:02:07] <sarang> Especially for something relatively new like this
[2021-01-13 12:03:12] <sgp_> the code for consensus and output selection are separate areas of code, correct?
[2021-01-13 12:03:22] <dEBRUYNE> We can just ask the audit team if a widened scope is possible
[2021-01-13 12:04:24] <sarang> sgp_: probably/hopefully :D
[2021-01-13 12:04:47] <sgp_> I think that's a super important detail to know :)
[2021-01-13 12:04:56] <sgp_> since if together, then selection is a blocker
[2021-01-13 12:05:08] <sarang> I mean, binning should have consensus elements in some cases, to avoid miner stuffing
[2021-01-13 12:05:08] <sgp_> if separate, then we can start with that code now
[2021-01-13 12:05:33] <gingeropolous> it should be possible to migrate to triptych and still allow those users that have pre-existing multisig setup to migrate as well?
[2021-01-13 12:05:52] <sarang> gingeropolous: no
[2021-01-13 12:05:58] <sarang> that's an important point about multisig
[2021-01-13 12:06:07] <ArticMine> We need a grandparent period for that
[2021-01-13 12:06:22] <sgp_> huh?
[2021-01-13 12:06:46] <sgp_> this wouldn't kill the previous multisig funds after a period
[2021-01-13 12:07:15] <sgp_> they just would have to spend to a new wallet on triptych
[2021-01-13 12:07:41] <sarang> Existing non-multig operations would continue to work just fine
[2021-01-13 12:07:44] <dEBRUYNE> Yeah it's like going from non-RCT to RCT outputs
[2021-01-13 12:07:56] <sgp_> oh one quick compatibility question
[2021-01-13 12:08:09] <sgp_> suppose I make a multisig wallet today and publish the normal 4 address
[2021-01-13 12:08:25] <sgp_> what if someone sends tripytch outputs to that address
[2021-01-13 12:08:55] <sgp_> are those recoverable?
[2021-01-13 12:09:22] <sarang> I believe you'd need all parties to use a trusted operation to do so (but it's possible)
[2021-01-13 12:09:25] <sarang> it's really a question of trust
[2021-01-13 12:09:44] <sarang> The new multisig operation does not require that trust
[2021-01-13 12:09:53] <sarang> I'd need to review the specifics of this to be sure
[2021-01-13 12:09:54] <ArticMine> That is why I suggest a period of time for the transition
[2021-01-13 12:09:55] <sgp_> for clarification, suppose this is a 2/3 multisig wallet
[2021-01-13 12:10:05] <sgp_> do you need the support of 2 or 3 people
[2021-01-13 12:10:35] <sarang> I believe you need just the 2 people, but they can't spend it without a trusted operation
[2021-01-13 12:10:41] <sgp_> ArticMine: this isn't solved with a transition period afaict
[2021-01-13 12:10:53] <sgp_> what is a trusted operation?
[2021-01-13 12:11:24] <sarang> They'd have to recover the output private key in a way that means they both know it
[2021-01-13 12:11:40] <sarang> As opposed to the non-trusted way, in which they don't learn the other party's share of it
[2021-01-13 12:12:01] <sarang> This is because of an inversion operation that's the cause of all this multisig tomfoolery
[2021-01-13 12:12:28] <sarang> and cannot be avoided AFAICT (this is present in other constructions like Arcturus, RCT3, Omniring)
[2021-01-13 12:13:04] <sarang> It's because they need to construct the key image, which uses this inversion
[2021-01-13 12:13:09] <ArticMine> So there is a one time issue
[2021-01-13 12:13:17] <sgp_> let me repeat this back to make sure I understand
[2021-01-13 12:13:20] <sarang> Yes, but could be very important
[2021-01-13 12:14:40] <ArticMine> To clarify this issue does not occur going from Triptych to Arcturus
[2021-01-13 12:14:41] <sgp_> in order to recover triptych funds sent to a pre-triptych multisig wallet, they would need to reconstruct the private key in such a way that all parties who participated would learn the full spend key (and thus could independently send all funds from that wallet, including both clsag and triptych outputs)
[2021-01-13 12:15:06] <sgp_> so put another way:
[2021-01-13 12:15:08] <sarang> Yes
[2021-01-13 12:15:22] <sgp_> the wallet would need to be "converted" from a multisig wallet to a non-multisig wallet first
[2021-01-13 12:15:41] <sarang> That's a good way of wording it, yes
[2021-01-13 12:15:52] <sgp_> okay, I understand now :D
[2021-01-13 12:16:05] <sarang> It's super annoying and could be very problematic for users, I know
[2021-01-13 12:16:06] <ArticMine> but the conversion only requires the same number of signature as the original multi sig
[2021-01-13 12:16:14] <ArticMine> Correct?
[2021-01-13 12:16:20] <sarang> ArticMine: yes
[2021-01-13 12:16:48] <sarang> I've thought a lot about ways to avoid this inversion stuff, but it's pretty baked in to a lot of the math of this and similar constructions
[2021-01-13 12:16:57] <sgp_> I think this is something that needs to be approached with care, but is still okay to proceed with care
[2021-01-13 12:17:31] <sgp_> this is why a transition period doesn't solve ArticMine:
[2021-01-13 12:17:44] <sgp_> wallets will either receive clsag or triptych outputs
[2021-01-13 12:18:00] <sgp_> this "conversion" needs to be done when the very first triptych output is received
[2021-01-13 12:18:37] <sgp_> we may have one more option however, sarang what do you think of this:
[2021-01-13 12:19:19] <sgp_> first, can clsag multisig wallets spend clsag outputs (only) and make new triptych outputs in a non-trusted way?
[2021-01-13 12:19:42] <ArticMine> What happen in reverse a CLSAG output sent to a Triptych multisig wallet?
[2021-01-13 12:20:43] <sarang> sgp_: yes
[2021-01-13 12:20:55] <sarang> The construction of outputs is identical in both cases
[2021-01-13 12:21:05] <sarang> The only difference is how key images are computed, which has implications for spends
[2021-01-13 12:22:13] <UkoeHB__> sarang I may be missing something, at which step in https://github.com/monero-project/research-lab/issues/72 is the full private spend key known to participants?
[2021-01-13 12:22:16] <sgp_> okay, so we have one other option perhaps that's inelegant
[2021-01-13 12:22:28] → VictorPC joined (VictorPC@gateway/vpn/mullvad/victorpc)
[2021-01-13 12:23:10] <sgp_> we could change the addresses to be detectable to the sender that it's a newer triptych wallet and perhaps also only allow sending of triptych outputs to those on the wallet side
[2021-01-13 12:23:39] <sarang> Sorry, I have to take off unfortunately
[2021-01-13 12:23:53] <sarang> This meeting went much longer than I had expected
[2021-01-13 12:25:30] <u29601mg6ba93j[m> <sarang "Sorry, I have to take off unfort"> Thanks for your participation. Speaking for myself I learned a lot from your answers
[2021-01-13 12:25:57] <ArticMine> I propose we reconvene is a week
[2021-01-13 12:26:01] <ArticMine> in
[2021-01-13 12:26:20] <sgp_> yeah this was super useful I think
```

# Action History
- Created by: SamsungGalaxyPlayer | 2021-01-12T17:37:50+00:00
- Closed at: 2021-01-13T18:35:21+00:00
