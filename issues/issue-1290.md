---
title: 'Monero Tech Meeting #144 - Monday, 2025-11-03, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/1290
author: rbrunner7
assignees: []
labels: []
created_at: '2025-10-31T20:36:23+00:00'
updated_at: '2025-11-03T19:00:28+00:00'
type: issue
status: closed
closed_at: '2025-11-03T19:00:28+00:00'
---

# Original Description
Location is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting [here](https://github.com/monero-project/meta/issues/1285).


# Discussion History
## rbrunner7 | 2025-11-03T19:00:28+00:00
````
<rbrunner7> Meeting time. Hello! https://github.com/monero-project/meta/issues/1290
<sneedlewoods> hey
<jberman> waves
<jeffro256> Howdy
<rbrunner7> Alright, on to the reports from last week. FCMP++ I suppose, right? :)
<sneedlewoods> still working on TODOs and bug fixes
<jeffro256> I'm working on a large refactor to the Carrot integration that should get us closer to wallet2 supporting Carrot-derived account secrets and addresses, as well as hybrid hierarchies 
<jeffro256> It also gets us closer to HW device integration, including live scanning 
<jberman> Prepared PR's for v1.4 of the stressnet fixing some solid issues affecting monerod, investigated OOM's by using valgrind to sync and found that FCMP++ verification was taking more memory than expected, moving forward with the latter for now, then aiming to get back to tx relay v2 and runaway spans during IBD that @boog900 idenitifed 
<sneedlewoods> +1
<rucknium> +1
<jeffro256> +1
<rbrunner7> "Carrot intergration" as quite in general, into the Monero codebase?
<rbrunner7> And what is a "hybrid hierarchy"? If both old-style and new-style secret keys are present in a single wallet?
<rbrunner7> If yes, can't that get quite confusing? From a UI/UX point of view I mean
<jeffro256> Yeah I mean mainly where the wallet2 / old cryptonote code touch with the Carrot code 
<jeffro256> Yes, hybrid means both 
<rbrunner7> I guess you see some good reasons to do it, if only for symmetry if it's really needed, but well, my gut feeling is not exactly well with that ...
<jeffro256> It might get confusing? Depends on the design 
<rbrunner7> Do you get then two different sets of sub-addresses with that? With the double the chance to mix up compared with today? :)
<jeffro256> I would imagine that there's no reason to show the old receive addresses anymore after a wallet migration 
<rbrunner7> Ah, maybe I see, you want to support something like an "in-place wallet migration"?
<rbrunner7> Without forcing people to create new wallets if they don't like that
<ofrnxmr> Main advantage is not having to generate a new seed?
<rbrunner7> Yeah, that, and all the history that is still at hand, in the same wallet as it always was
<rbrunner7> If the UI of the wallet app can just mostly forget the old keys, and they are only used strictly internally if needed, the problem probably isn't one
<jeffro256> Yes, exactly. Nobody will ever be forced to upgrade their wallet, but the option should be there for people who don't want to update their seed phrases, assuming it's of an amenable seed type 
<rbrunner7> Ok, I already feel a little better :)
<jeffro256> I'd imagine it would be the most helpful to hardware wallet users 
<rbrunner7> I guess in the grand scheme of FCMP++ things that addition of hybrid wallets is no big sweat, in comparison to all the other stuff that gets built
<rbrunner7> There was an interesting, and to me somewhat surprising CCS PR, from "perfect-daemon" / "anon": https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/621
<rbrunner7> It has quite a number of upvotes already, and right now no downvote
<rbrunner7> Any comment?
<jeffro256> It needs details fleshed. There has already been confusion b/t this individual and CCS maintainers in the past, not expanding on what is actually going to be completed will inevitably lead to disagreements on whether to pay out.
<jeffro256> For example, "contribute to FCMP++ migration" is mentioned in the proposal. What does this mean practically? At the moment, I have no idea 
<rbrunner7> Hmm, what they will actually be working on might be a question that is not easy to answer right away?
<rbrunner7> And "fulltime" could also be a bit difficult, depending on how the project develops and moves
<jeffro256> Then they shouldn't have a CCS open IMO.
<jeffro256> They probably have some things in mind that they want to work on, I'd just like for them to actually list it 
<rbrunner7> Sounds reasonable.
<o​frnxmr> This isnt true afaik
<o​frnxmr> They werent paid out because they never requested the payout. They were paid once they requested
<j​berman> I think we'll likely see some good code contributed as a result of the proposal, and I'm fine reviewing it. I'm hoping he'll be open to collaborate the same as he was with 7760 at least with me back in the day. Personally I think it's fine if he wants to take time to investigate what he thinks are the issues most worthy of working on, with what he listed in the CCS as his aim. I don't think the CCS absolutely **needs** to be expanded on considering he's proven capable of finding significant issues after spending a while investigating in his own time / with his own focus.
<j​berman> Also I feel compelled to say.. I don't think that comment by hunting longs is a completely accurate portrayal of the state of the integration but I don't feel particularly compelled to argue / get into more drama on that front. I think it's likely a good bet that perfect daemon will contribute code that will improve the daemon in a meaningful way, and the daemon could use more hands on deck
<ofrnxmr> +1
<spirobel> +1
<o​frnxmr> A payment they were werent awared, was one that was privately negotiated for the multisig fix
<j​effro256> You suggest someone helps you out once and suddenly you're majorly struggling ig
<r​brunner7> I don't understand.
<o​frnxmr> i think it should go w/o saying that were lighthanded on all fronts
<o​frnxmr> Shorthanded*
<j​effro256> This is the issue that I was referencing. I don't want to minimize the opportunity for confusion by all parties involved
<j​effro256> I *do* want to
<r​brunner7> I can agree in principle, but the short-handed-ness is maybe distributed quite unevenly in time and space
<ofrnxmr> +1
<plowsof> no address was provided for the final CCS payout until recently, yep. has anon apologised for making vtnerd read haskell while they kept their implementation closed source yet :P 
<r​brunner7> (to ofrnxmr )
<o​frnxmr> Then this is a different issue. Multisig went through h1, was communicated thoroughly with many different parties, but the _payment_ was lost in the mix
<r​brunner7> Oh, let's hope we don't descend into drama here :)
<plowsof> citation https://github.com/monero-project/research-lab/issues/101#issue-1228028838 
<r​brunner7> I have to say that I agree with jeffro256 mostly, clarity can't do harm if you ask me, but can help tremendously in many cases
<plowsof> we where shorthanded then and people had to work on reimplementing his closed source work 
<r​brunner7> Asking them for a candidate list what they intend, or at least could imagine, to work on is reasonable
<r​brunner7> Are those ++ bulletproofs the ones that did not go into production after all?
<plowsof> true, this was pre audits 
<r​brunner7> Which makes the whole story even worse I guess
<r​brunner7> I really think what we don't want, not for them, and not for us, is again disagreement and confusion at the end. Avoiding that should be possible, I suppose.
<r​brunner7> Ok, let's see how that develops further.
<r​brunner7> Anything else left to discuss today?
<r​ucknium> I would prefer as discussion of CCS proposal 621 to happen in dev channels instead of MRL meetings. If necessary, it can be discussed in MRL, but it's a dev issue.
<r​brunner7> Just to be sure: Are we here in a place that you would count as a "dev channel"?
<j​effro256> This isn't a MRL meeting though?
<r​brunner7> I hope so :)
<r​brunner7> I brought it up mostly with a feeling that yes, it's mostly a dev thing, not a research thing, so ok to discuss here today.
<r​ucknium> I am saying try to get as much discussion in this channel instead of bringing it to MRL Wednesday.
<ofrnxmr> +1
<jeffro256> +1
<r​ucknium> Or start having meetings in #monero-dev  :)
<r​brunner7> I think we can agree on that :)
<r​brunner7> Ok, looks to me we are through for today. Thanks everybody for attending, read you again next week!
<s​pirobel> thanks
<j​effro256> Ah makes sense, ;)
<s​needlewoods> thanks everyone
<j​effro256> Thanks everyone
````


# Action History
- Created by: rbrunner7 | 2025-10-31T20:36:23+00:00
- Closed at: 2025-11-03T19:00:28+00:00
