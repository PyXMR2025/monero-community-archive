---
title: 'Monero Tech Meeting #114 - Monday, 2025-03-31, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/1179
author: rbrunner7
assignees: []
labels: []
created_at: '2025-03-28T16:04:15+00:00'
updated_at: '2025-03-31T18:35:25+00:00'
type: issue
status: closed
closed_at: '2025-03-31T18:35:24+00:00'
---

# Original Description
Location is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting [here](https://github.com/monero-project/meta/issues/1175).

# Discussion History
## rbrunner7 | 2025-03-31T18:35:24+00:00
````
<r​brunner7> Meeting time. Hello! https://github.com/monero-project/meta/issues/1179
<s​needlewoods> Hello
<j​effro256> Howdy
<s​yntheticbird> hello
<r​brunner7> Alright. What is there to report from last week?
<r​brunner7> I could finally reproduce the multisig error that SNeedlewoods corrected
<r​brunner7> As a small success ...
<sneedlewoods> +1
<j​berman> *waves*
<r​brunner7> If nobody waves, the meeting is less than complete :)
<j​effro256> me: Carrot scanning in `wallet2` is confirmed and tested: https://github.com/monero-project/monero/blob/40b04ef372d191f8991da22c220ccce2ba457b47/tests/unit_tests/wallet_scanning.cpp#L657
<syntheticbird> +1
<sneedlewoods> +1
<rbrunner7> +1
<rucknium> +1
<jberman> +1
<spirobel> +1
<j​effro256> I made a tiny tweak to the Carrot protocol that shouldn't affect security but makes supporting hybrid key hierarchies a lot less annoying: https://github.com/jeffro256/carrot/commit/76449ab073a94a2f001d2c21951d3c6053db6a04
<j​berman> me: implemented banning torsioned output pubkeys and commitments at consensus at the fork (after the fork, wallets won't have to do the expensive check for/clear torsion when building the tree), fixed a recently introduced issue with reorg handling in the wallet scanner tree builder, implemented a static table for FCMP++ proof size (calculating it from n inputs and n layers can be slow), just implemented banning n_tree_layers >12 to keep the table small and portable (the tree supports a max of ~200 quadrillion outputs at 12 layers by my math)
<j​berman> This week I'm going to work on including the tree root in the block's PoW hash so clients can (eventually) verify PoW on the daemon's reported tree root, and therefore have a solid degree of confidence in the tree the client is using to construct or verify txs 
<j​berman> Also going to write up the blog post for the FCMP++ competition and commence the marketing blitz with xmrack 's help
<jeffro256> +1
<syntheticbird> +1
<sneedlewoods> +1
<spirobel> +1
<r​brunner7> That's quite a lot
<r​brunner7> jeffro256: So this is strictly only about Janus protection and nothing else, so we don't have to worry about invalidating the Carrot audit results?
<j​effro256> Validating the Janus protection was in-scope for the Carrot audit, so technically it invalidates it, but the security proof / concepts involved literally shouldn't change whatsoever, since the `K_s` in `anchor_sp` wasn't part of the reasoning for why Janus protection held
<rbrunner> +1
<j​berman> Also of note, jeffro256 tobtoht (and little bit of work on my end) got the seraphis-migration/fcmp++-stage development branch back onto master, CI builds are passing minus GUIX stuff which presumably would need PR 9801 (special shoutout to tobtoht for identifying / fixing some pesky build issues)
<tobtoht> +1
<sneedlewoods> +1
<jeffro256> +1
<r​brunner7> Was that a test only, will you continue to work on the stage development branch?
<j​berman> We're been working on fcmp++-stage for some weeks now and will continue to
<t​obtoht> "which presumably would need PR 9801" <- 9801 + 9440
<jberman> +1
<r​brunner7> Yeah, I mean too early to continue work on master, so I guess that was a test to see where you stand with conflicts
<r​brunner7> And build system in general, as it sounds
<r​brunner7> Ok, everybody is very busing, and moving fast, which is nice. Do we have to discuss something in particular beyond these reports?
<r​brunner7> *very busy
<r​brunner7> Doesn't look like it, so I think we can close already. Thanks everybody for attending, read you in 1 week!
<r​brunner7> I wonder how we will look back to these months in a few years' time ...
<s​pirobel:kernal.eu> fondly?
<s​needlewoods> thanks everyone,
<s​needlewoods> I hope until next week I have at least a draft PR for monero-gui
<r​brunner7> I hope so!
````


# Action History
- Created by: rbrunner7 | 2025-03-28T16:04:15+00:00
- Closed at: 2025-03-31T18:35:24+00:00
