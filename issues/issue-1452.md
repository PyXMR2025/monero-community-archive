---
title: 'Monero Tech Meeting #184 - Monday, 2026-09-07, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/1452
author: rbrunner7
assignees: []
labels: []
created_at: '2026-09-04T18:33:09+00:00'
updated_at: '2026-09-07T18:26:30+00:00'
type: issue
status: closed
closed_at: '2026-09-07T18:26:30+00:00'
---

# Original Description
Location is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting [here](https://github.com/monero-project/meta/issues/1449).


# Discussion History
## rbrunner7 | 2026-09-07T18:26:30+00:00
````
<rbrunner7> Meeting time. Hello! https://github.com/monero-project/meta/issues/1452
<sneedlewoods> hey
<jpk68> Hello
<jberman> waves
<rbrunner7> Alright, on to the reports from last week. Me: The seemingly never-ending Polyseed PR review :)
<jpk68> Me: played around with multisig support in the GUI, made some fixes, reviewed PRs, general testing
<selsta> hi
<sneedlewoods> I think I finally addressed most AI review comments.
<sneedlewoods> There were many legit and helpful comments, thanks to selsta, thomasbuilds and xmrack for providing those. Let me know if anyone wants to do another run.
<sneedlewoods> Else there are currently three other things left for me to work on:
<sneedlewoods> * during testing I stumbled upon issues with multisig, will need to double check they're solved
<sneedlewoods> * jpk68 reported issues with hw devices
<sneedlewoods> * rbrunner7 suggested a change to the wallet-rpc PR, to go the full way for using extendedStatus (src (https://github.com/monero-project/monero/pull/10819#discussion_r3728598122)), for which I have a WIP branch
<rbrunner7> Fully going "extended status" would be really nice IMHO. A lot of work, but a win.
<sneedlewoods> Have it on another branch currently, to not mess up the original PR if it turns out to not work as nicely, but at this moment I'm quite confident it's a good change
<selsta> I mostly worked on v0.18.5.3, which also seems like it keeps getting delayed due to new issues / reports / things to improve, I guess at some point we have to make a hard cut and just include the remaining things in the next release.
<rbrunner7> "Next release" would still be 0.18, or the all-new shiny 0.19 already, branched from master?
<selsta> v0.19 already, that's why I wanted to include as much as possible now
<jberman> mostly worked on hot/cold wallet review + upstream review
<syntheticbird> selsta: if you drop v0.19 people are going to be more reactive to upcoming minor releases. So imho you should go with making a cut.
<rbrunner7> It seems we currently have a lot of small PRs as well, improving little things left and right, which is nice, but means work
<selsta> j-berman: could you go through the ones you opened again for this release and that are not merged to check if there is anything to do? I'd like the serialization changes in from you and vtnerd
<jberman> +1
<rbrunner7> So, seems we are through with the reviews. Do we have anything to discuss today beyond those?
<jberman> selsta: serialization thing is the only thing, your suggestion there is good
<rbrunner7> No special subject then. Short meeting :) Thanks everybody for attending, read you again next week!
<jpk68> +1
<sneedlewoods> +1
<jeffro256> Personally, I'm just deep in reviews (for my PRs and others)
<selsta> https://github.com/monero-project/monero/pull/11168 jeffro suggested a live test here
<selsta> meaning a sync from scratch or can it be done quicker with existing blockchain?
<jeffro256> Ideally from scracth because it affects v1 txs in slightly different ways (mixed/pre-RingCT amount indices lookup)
<jberman> I can do a sync from scratch. I had started one but seems we need 11204 in on master
<selsta> ideally it would be mainnet / testnet / stagenet from scratch
<jberman> I can see if sync with 11204 + that PR are good
<jberman> ultimately we're going to want to test sync from scratch with all of these PR's in together too
<selsta> yes maybe better to just wait until we have everything merged
<sneedlewoods> Which exactly are the three PRs? I could try a full testnet for all of them
<sneedlewoods> sync*
<selsta> 11168, 11204, 11206
<sneedlewoods> ty
<rbrunner7> By the way, this came up today in the MRL lounge, interesting stuff IMHO, copy this here in case some people did not yet see it: https://gist.github.com/1440000bytes/211ac92dd4433bb1a2e674bf0ff7db2e
<selsta> sneedlewoods_xmr: and also 11235
<jberman> +1
<sneedlewoods> +1
````


# Action History
- Created by: rbrunner7 | 2026-09-04T18:33:09+00:00
- Closed at: 2026-09-07T18:26:30+00:00
