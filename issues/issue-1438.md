---
title: 'Monero Tech Meeting #181 - Monday, 2026-08-10, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/1438
author: rbrunner7
assignees: []
labels: []
created_at: '2026-08-07T14:14:59+00:00'
updated_at: '2026-08-10T18:29:44+00:00'
type: issue
status: closed
closed_at: '2026-08-10T18:29:44+00:00'
---

# Original Description
Location is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting [here](https://github.com/monero-project/meta/issues/1434).


# Discussion History
## rbrunner7 | 2026-08-10T18:29:44+00:00
````
<rbrunner7> Meeting time. Hello! https://github.com/monero-project/meta/issues/1438
<jpk68> Hello
<sneedlewoods> hey
<ack-j> Hi
<rbrunner7> Alright, any reports since last meeting?
<selsta> hi
<jberman> waves
<jeffro256> Howdy 
<sneedlewoods> reviews, review comments and some more investigation into the slow sync with large subaddress lookahead
<rbrunner7> Not much from me, waiting for some more review activity on my Polyseed PR ...
<sneedlewoods> @rbrunner7: Noted
<jberman> mostly PR's from stressnet / improvements to monerod where notable
<jpk68> Me: reviewed some PRs, investigated ways to improve wallet sync times (which resulted in some findings, see #11063), regular stuff
<rbrunner7> I try now to sync stressnet to help later with multisig testing and noticed that this will take my notebook literally days ... where are the stressnet checkpoints :)
<jeffro256> me: lots of PR review 
<jberman> I lean in favor of just starting a new beta v3 at this point that includes the latest round of changes to tx relay v2, to alleviate disk space reqs for stressnet participants
<rbrunner7> Well, if that gains loose consensus today I can relieve my poor notebook today still
<jeffro256> Yeah, we could start the v3 with a min block size equal to or greater than currently realized block sizes 
<jeffro256> To remove the warm-up period 
<rbrunner7> It's not only the disk space, as I said it's also the verifying of all those large blocks
<jberman> I'm definitely a nack on messing with block size stuff further hah, last time we tried that was not fun
<rbrunner7> What do you mean with "min blocksize"?
<rbrunner7> The threshold when some fee changes kick in?
<jeffro256> We already change the min block size for FCMP++ though, it would be a single-line config change 
<jeffro256> To a line we already change 
<jeffro256> By min block size, I mean the penalty free zone 
<jeffro256> That's what it's called in the code, which is a bad name IMO 
<jeffro256> I don't mean actually putting a hard minimum on the block weight 
<rbrunner7> I guess if @jberman:monero.social and @jeffro256:monero.social agree to start over then stressnet V2 is history quite soon?
<tobtoht> (news from the front: 9440 merged, sets way for 10359)
<jberman> +1
<jeffro256> +1
<sneedlewoods> +1
<jberman> raising penalty free zone doesn't sound terrible to me actually, fair rebuttal 
<jpk68> tobtoht: Does that one need anything else before merge?
<jeffro256> It has approvals from Ukoe and I
<jberman> @rbrunner7: still pending on https://github.com/seraphis-migration/monero/pull/450
<jeffro256> Anything that j-berman wants to add to 10359?
<jeffro256> That would be good to get out of the way so that we can start chugging on the other FCMP++ PRs 
<jberman> @jeffro256: nothing planned on my end
<tobtoht> jpk68: Just a rebase and a 4 line diff to activate Guix rust machinery for CI.
<jeffro256> AFAICT discussions mainly revolved around Rust integration in general, not anything specific to the Rust FFI in that PR
<jberman> +1
<jpk68> +1
<jberman> @tobtoht: oh yes, sorry will do that asap
<jeffro256> +1
<rbrunner7> Well, the "Rust ship" has sailed. People who don't agree on fundamental grounds probably have to stay on the old chain ...
<rbrunner7> At least building is no problem, just a compiler more that is involved, as it looks from the outside. But of course lots and lots of library stuff drawn in.
<rbrunner7> Ok, looks that's it about the reports. Anything to discuss today beyond those?
<rbrunner7> Does not look like it. Thanks for attending everybody, read you again in 1 week!
<jpk68> Thanks, everyone :))
<sneedlewoods> Thanks everyone
<jpk68> Jinx!
````


# Action History
- Created by: rbrunner7 | 2026-08-07T14:14:59+00:00
- Closed at: 2026-08-10T18:29:44+00:00
