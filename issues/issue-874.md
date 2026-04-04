---
title: 'Seraphis wallet workgroup meeting #31 - Monday, 2023-08-07, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/874
author: rbrunner7
assignees: []
labels: []
created_at: '2023-08-04T17:21:54+00:00'
updated_at: '2023-08-07T19:04:14+00:00'
type: issue
status: closed
closed_at: '2023-08-07T19:04:14+00:00'
---

# Original Description
On Monday, November 14 2022, we started with regular weekly meetings of the Seraphis wallet workgroup, and all interested parties from the community that want to join. Time is 18:00 UTC on each Monday. "Location" is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting here: #872

# Discussion History
## rbrunner7 | 2023-08-07T19:04:14+00:00
````
<r​brunner7> Meeting time. Hello! https://github.com/monero-project/meta/issues/874
<Rucknium> Waves
<j​effro256> Howdy
<j​berman> hello
<r​brunner7> So, anything to report?
<j​berman> I  looked into libcurl for concurrent requests over the same connection and found that it'd need more involved server-side changes to get that working. So my current plan is implement a production-ready connection pool so clients can request and process multiple chunks of blocks at the same time: https://github.com/seraphis-migration/wallet3/issues/58
<j​berman> My plan for this week: (1) implement the connection pool, (2) address comments in background sync PR 8619(unrelated to wallet3), (3) harden scope for Seraphis security proofs
<r​brunner7> So you move full speed ahead, after a summer break?
<j​berman> pretty much :)
<r​brunner7> dangerousfreedom[m] can talk with me directly, but has trouble to reach this room somehow. Sigh.
<r​brunner7> jeffro256: You can follow?
<j​effro256> Yup, I'm on Matrix and can see the messages b/t you and jberman
<r​brunner7> Alright then :)
<r​brunner7> If nobody has something urgent to discuss on their own, I would like to talk about Seraphis related PRs, and maybe also the midterm and longterm evolution of the code that we develop here.
<r​brunner7> I think it really does not take long anymore until there is something to merge.
<r​brunner7> So we can look at this in detail
<a​ck-j> Hey
<r​brunner7> To recap, state now is that we have UkoeHB 's Seraphis lib branch. Pretty clear, seems to me. He manages that
<r​brunner7> and PRs to that should probably be mostly only about that, Seraphis proper
<d​angerousfreedom> Hello
<r​brunner7> Then we have "our" repo, set up by me here: https://github.com/seraphis-migration/monero/tree/seraphis_wallet
<r​brunner7> That, at least so far, is meant as the place for wallet dev work
<r​brunner7> It has the Seraphis lib as upstream
<r​brunner7> We could get code changes on the main Monero repo either directly into this, or through the Seraphis library
<j​effro256> jberman where is your new scanner code located ?
<j​effro256> I guess should wallet3 development mainly be PRed to the seraphis-migration repo?
<r​brunner7> That's the idea so far, at least from my side, yes
<j​berman> jeffro256: on my own branch building off `seraphis_lib` for now: https://github.com/j-berman/monero/tree/seraphis_lib_scanner
<jeffro256> +1
<j​effro256> Is there a running list of feature differences of seraphis-migration to the main monero repo and the seraphis_lib branch?
<d​angerousfreedom> So, from my side:
<d​angerousfreedom> - Almost finished the wallet functions to call the sp_knowledge_proofs.
<d​angerousfreedom> - Updated some structs like the 'TransactionRecord' to keep track of the 'JamtisPaymentProposalSelfSendV1' and 'JamtisPaymentProposalV1' when there is an attempt to make a transaction as I believe it is easier to store them instead of the destination and private ephemeral keys (needed for some knowledge proofs).
<r​brunner7> There is nothing merged yet ...
<r​brunner7> Ah, you mean on UkoeHB 's branch
<r​brunner7> Do you think feature lists will be useful as a tool to keep track?
<r​brunner7> Or lists of differences?
<d​angerousfreedom> I looked again on how to write a similar function to simplewallet::get_transfers (command show_transfers) and I believe the sp_wallet should show a list of enotes instead of showing a list of transactions like it is now. There are several reasons for that and I will start a discussion about it soon. But first I would like to ask a few questions about the EnoteStore.
<d​angerousfreedom> 1) @UkoeHB Is the EnoteStore supposed to keep track of all enotes (normal incoming, selfsend and outgoing) forever? Could you write a few words about the lifetime of an enote in the EnoteStore?
<d​angerousfreedom> 2) @shalit could you update us about the status of the EnoteStore serialization?
<r​brunner7> dangerousfreedom: Thanks for the report. Your user lost the "[m]" somehow now, maybe that's why it works now
<r​brunner7> About merging to the Seraphis wallet repo:
<r​brunner7> My take so far is that we only merge in there what is meant to endure, i.e. ideally stay in the code until the wallet goes into service in the future
<r​brunner7> After many changes and improvements of course, just in principle
<r​brunner7> You see what I mean with this?
<d​angerousfreedom> I guess it is a problem for the future
<r​brunner7> Let's make an example with jberman 's scanner
<r​brunner7> He will PR it when he thinks it's ready, in a useful sense of "ready"
<r​brunner7> If he improves it further later, after it's merged into the repo, he would base a new PR on the repo
<r​brunner7> and not his old scanner branch.
<j​effro256> What branch and repo would y'all PR against
<r​brunner7> If nobody strongly opposes, or finds out problems, the mentioned one: https://github.com/seraphis-migration/monero/tree/seraphis_wallet
<j​effro256> I guess what I'm trying to ask is if there's a central repo that wallet3 development (outside of Seraphis core) changes are being pooled
<j​effro256> Okay cool
<r​brunner7> Maybe we can discuss this nice `wallet2_basic` library that jeffro256 wrote. One version is here: https://github.com/UkoeHB/monero/pull/13
<r​brunner7> I mean, discuss PR-wise
<r​brunner7> It's now a parred-down variant from a PR against the main Monero repo, right?
<j​effro256> Yes I closed it, but if I opened it against `seraphis_wallet` it would essentially be the same as the PR linked, which is the PR against the main repo w/o the wallet2 changes
<r​brunner7> There may be reasons for that, but I worry what happens if we merge pieces of code on the one hand into the Monero main repo, and on the other hand into our own in a modified form, so that Git won't know anymore it's the "same". Won't that spell trouble in the future, when sooner or later the lines have to come together again?
<j​effro256> Yeah it might be easier to just do the wallet2 integration commit against seraphis_wallet anyways
<j​effro256> I mostly did that integration to "prove" that it works against the production code
<r​brunner7> Is there a good reason to have that capability on the main code early?
<r​brunner7> Of course if "our" `wallet2` diverges early from the main one, merging up changes becomes difficult. But I think one way or another it will get difficult anyway ...
<r​brunner7> And after all we want to throw it away, that monster :)
<UkoeHB> dangerousfreedom: yes, the enote store stores all enotes
<j​effro256> If there are issues, we'd likely find them earlier but not much utility besides that
<r​brunner7> Ok, so we won't lose much probably if you go directly to "our" repo.
<j​effro256> Yes I think so
<r​brunner7> I wonder anyway how this will go forward. E.g. regarding reviews. Pretty sure, for the Seraphis code we produce, the true-and-tried "review every PR" pattern will break down
<r​brunner7> At least from the point of view of Monero devs outside this groupd
<j​effro256> Honestly the wallet2 integration is probably too much review work anyways, so I might rebase the main PR to not include those changes and have the wallet2 integration PR on the side to test things against
<r​brunner7> Sounds like a possible way, yeah. Seraphis probably has no need to *write* in that format.
<r​brunner7> Only reading.
<r​brunner7> I also wonder what will happen further out. Will our repo, years in the future, become the new master? Or will at one point be a gigantic "merge-back" after a monster-review?
<r​brunner7> Of course I am speculating wildly here, but this might influence what we do and how we plan *now*
<j​effro256> I don't know why the new repo would become the master, the latter option is much more likely
<r​brunner7> Ah, I think I misunderstand. Writing capability is no problem for `wallet2_basic`, but to modify `wallet2` to actually use it
<j​effro256> Which means that we can be more lax about integrating changes into the seraphis-migration repo to advance changes quickly, then take more time to consider side-effects and do more thorough review when it comes time to merge into the core repo
<r​brunner7> Not sure, but maybe it may just be a lot easier for our much more advanced repo by-then to become the new master?
<r​brunner7> If we always merge everything up
<j​effro256> Yes, the storing code itself is pretty short
<r​brunner7> Not that I really have that as an ambition, just trying to look ahead a bit :)
<j​effro256> I'd rather have the seraphis-migration repo be a "beta" branch that we can develop on quicker while still having a central repo, otherwise all the review dependencies are going to stall development significantly
<r​brunner7> Yes, of course, the main repo runs on, for years to come, until we are more or less "ready", that's my speculation here
<r​brunner7> So we are beta for a long time, if you want
<r​brunner7> Anyway
<r​brunner7> Do have "lose consensus" that we establish a PR pattern much like it's in force for the main repo: If something if merged, it "belongs" to the repo from that point in time forward, and andy changes to do start from that again? Whether by original author or somebody else, does not matter in principle?
<j​berman> sounds good to me
<j​effro256> Yup I'm fine with that, but I do want to know something from UkoeHB
<j​effro256> Since now there's quite a few dev efforts that are downstream from `seraphis_lib`, @UkoeHB are you planning on doing any more force pushes besides rebasing against master?
<r​brunner7> As those could complicate us taking in changes from there?
<UkoeHB> It's best to PR against master for any changes that affect the existing codebase. New files can go in the new repo.
<UkoeHB> I don't have many planned changes to seraphis_lib (just tx extra stuff)
<UkoeHB> I already PR'd most things out of seraphis_lib into master that could be PRd
<r​brunner7> I am not sure we understand each other fully here, but probably does not matter: If the Seraphis library won't change much anymore, probably there will be no problems on that front, right?
<r​brunner7> Merges from the library into the Seraphis wallet repo will probably be easy
<UkoeHB> yes hopefully
<r​brunner7> Alright, anything else right now? If not, thanks for attending, and read you again next week at the latest
````


# Action History
- Created by: rbrunner7 | 2023-08-04T17:21:54+00:00
- Closed at: 2023-08-07T19:04:14+00:00
