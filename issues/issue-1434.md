---
title: 'Monero Tech Meeting #180 - Monday, 2026-08-03, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/1434
author: rbrunner7
assignees: []
labels: []
created_at: '2026-08-01T05:59:50+00:00'
updated_at: '2026-08-03T18:43:02+00:00'
type: issue
status: closed
closed_at: '2026-08-03T18:43:02+00:00'
---

# Original Description
Location is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting [here](https://github.com/monero-project/meta/issues/1430).


# Discussion History
## rbrunner7 | 2026-08-03T18:43:02+00:00
````
<rbrunner7> Meeting time. Hello! https://github.com/monero-project/meta/issues/1434
<sneedlewoods> hello
<vtnerd> Hi
<tobtoht> Hi
<jberman> waves
<rbrunner7> Alright, what are the reports since last week?
<tobtoht> The release-v0.19 branch is live.
<sneedlewoods> Updated the wallet-rpc PR, it now has a switch to translate extended Wallet API error codes into wallet-rpc error codes without assuming they're the same.
<rbrunner7> I started to work on Polyseed for the Monero GUI wallet
<sneedlewoods> Also looked into the issue where creating many subaddresses is really slow (mentioned by DataHoarder in last MRL meeting), especially when subaddress lookahead was modified.
<sneedlewoods> e.g. in the cli address mnew 1000
<sneedlewoods> I did a thing, and it became so fast that I assume I did something wrong. But after some testing and debugging it seems to work. Before I make a PR you can have a look here (there has to be an issue with this approach, it can't be that easy, right? :D) https://github.com/monero-project/monero/compare/master...SNeedlewoods:seraphis_wallet:x_add_subaddress_performance
<sneedlewoods> Testing data: Number of seconds until address mnew 1000 on a fresh wallet is finished
        1.      2.
Before: 4       45
Now:    1       1
Where 1. without changing subaddress lookahead and 2. after set subaddress-lookahead 20:5000
<tobtoht> @tobtoht: All FCMP++ / Carrot related changes can now go into master.
<jberman> +1
<sneedlewoods> +1
<jeffro256> +1
<jbabb> +1
<tobtoht> Fixes, polyseed, and tx relay v2 will be backported to release-v0.19: https://github.com/monero-project/monero/pull/11015
<tobtoht> A final v0.18 release is planned: https://github.com/monero-project/monero/issues/11009
<tobtoht> After the v0.18 release, focus will be on working towards tagging v0.19.0.0.
<DataHoarder> sneedlewoods: I found the issue also compounded later when scanning outputs
<rbrunner7> "The release-v0.19 branch is live." So from now on it's one PR for master and one for that new 0.19 branch?
<jeffro256> Howdy 
<jpk68> Hello
<jberman> Dug into @Rucknium 's logs for the wallet rejection double spend issue and assessed tx relay v2 issues, implemented some solid changes to tx relay v2 as a result (and after discussion with selsta and boog) :  https://github.com/seraphis-migration/monero/pull/450
<jpk68> Me: made some hardware wallet fixes, polishing I2P SAM code, regular patches, etc.
<jeffro256> @tobtoht: Backporting these features is a good idea since their development graph will be a lot less crazy than Carrot/FCMP
<tobtoht> +1
<jeffro256> And we can proceed with FCMP merges ;)
<selsta> rbrunner7: you don't need to open a separate release-v0.19 PR for now, we have one large backport PR
<tobtoht> @rbrunner7: We have adopted bulk backports temporarily to reduce workload as we try to coordinate three active branches. I think it would be easiest for us to handle if fixes are submitted against master only for now. After a fix is merged to master it will be added to the backports PR.
<rbrunner7> Ah, I see. Exciting, a new approach :)
<tobtoht> @jeffro256: The first build system changes are making their way in :)
<jeffro256> +1
<rbrunner7> Is anything along these lines planned for the GUI wallet as well?
<rbrunner7> Or isn't the PR "traffic" there too small?
<selsta> we don't do branches there
<rbrunner7> *Or is
<rbrunner7> Ok. If I have good luck and will be fast with Polyseed for GUI, it might need to wait for the submoduled Monero to catch up then ...
<selsta> I already have a wip branch for Polyseed added to GUI
<rbrunner7> Ah, you mean you work on it?
<selsta> I was asking gbks for a new seed template but he did not reply so far
<selsta> yes
<selsta> it's not polished yet
<rbrunner7> Ok, so I guess you go first :)
<jeffro256> FWIW, with Carrot/FCMP++, there are almost 0 changes that downstream projects like the GUI wallet need to adopt due to downstream changes, besides relevant UX changes added by GUI in the first place. So the GUI can basically "ignore" the Carrot/FCMP++ changes until they are ready to update ring-specific UX stuff 
<jeffro256> *due to upstream changes 
<rbrunner7> selsta: What do you mean with "new seed template"?
<selsta> PDF template to print and write down seed words
<selsta> the current one has 25 words
<rbrunner7> Ah, ok
<jpk68> That HTML document that comes with the Windows install might be rendered (even more) irrelevant after :(
<rbrunner7> You mean the ReadMe?
<rbrunner7> Don't insult my beautiful ReadMe :)
<rbrunner7> Maybe it could use some love, like so many thing in Monero software land ...
<jpk68> Not the README.md, the other thing
<rbrunner7> Yeah, that's the ReadMe for the users.
<jpk68> +1
<rbrunner7> That "other thing"
<rbrunner7> Alright, seems like the time plan of @jeffro256:monero.social that we discussed quite extensively in our meeting last week sailed through the MRL meeting without problems, so I guess we will go for that?
<rbrunner7> Waiting for the starting shot, the start of the countdown to hardfork :)
<rbrunner7> Seems we are through with the reports. Do we have something to discuss beyond those?
<jberman> I briefly discussed this with boog: those changes to tx relay v2 I linked above maximally benefit from all nodes on the stress network running it, so it may be the move to bump to beta stressnet v3 if we want those changes in and want to test them best 
<jberman> just noting that as a potential consideration for the future once those changes get reviewed in more detail
<rbrunner7> You would force all nodes to the new version with this approach, to achieve optimal testing conditions?
<jberman> essentially yes
<rbrunner7> I guess testing this fundamental thing well is a rather good idea
<rbrunner7> Is there any hesitation about "wanting those changes in"?
<rbrunner7> Waiting for review and feedback I guess
<jberman> @rbrunner7: yep
<rbrunner7> Let a thousand LLMs pick it apart
<tobtoht> Oh, I finally figured out where the horizontal scroll bar is. I had just extended my browser window to 6k pixels. Plan seems good to me. > <@rbrunner7> Alright, seems like the time plan of @jeffro256:monero.social that we discussed quite extensively in our meeting last week sailed through the MRL meeting without problems, so I guess we will go for that?
<sneedlewoods> +1
<rbrunner7> Exactly, scrolling that thing is an intelligence test
<tobtoht> +1
<rbrunner7> Ok, seems we are through for today. Thanks everybody for attending, read you again next week!
<sneedlewoods> thanks everyone, cu
````


# Action History
- Created by: rbrunner7 | 2026-08-01T05:59:50+00:00
- Closed at: 2026-08-03T18:43:02+00:00
