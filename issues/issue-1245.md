---
title: 'Monero Tech Meeting #130 - Monday, 2025-07-28, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/1245
author: rbrunner7
assignees: []
labels: []
created_at: '2025-07-25T17:09:21+00:00'
updated_at: '2025-07-28T18:34:26+00:00'
type: issue
status: closed
closed_at: '2025-07-28T18:34:26+00:00'
---

# Original Description
Location is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting [here](https://github.com/monero-project/meta/issues/1241).


# Discussion History
## rbrunner7 | 2025-07-28T18:34:26+00:00
````
<r​brunner7> Meeting time. Hello! https://github.com/monero-project/meta/issues/1245
<j​effro256> Howdy
<j​berman> *waves*
<s​needlewoods> hey
<r​brunner7> Alright, the regulars are here, thus on to the reports!
<s​needlewoods> Still have to do more testing for multisig, but started looking into ring related stuff. Since we already have `getRing()`, `getRings()` & `setRing()` (CLI commands `print_ring` & `set_ring`) in the current Wallet API I did use them, but we don't have a `unseRing()` (CLI: `unset_ring`) and I'm not sure if I should add it, or if it will become obsolete with FCMP++!?
<s​needlewoods> CLI command `save_known_rings` get's called automatically in Wallet APIs refresh function ([src](https://github.com/monero-project/monero/blob/fbc242d52d89d9c8021194cd4faae657c94d5a31/src/wallet/api/wallet.cpp#L2437)), so I'd argue we don't need to add it to the Wallet API for manual calls!?
<s​needlewoods> Then I asked myself if it's okay to not add blackballing, as it's already removed in this pending PR [8758](https://github.com/monero-project/monero/pull/8758) and even though it's hard to judge, I think FCMP++s could be completed before my work and then it would be a waste of time anyways to add blackballing, or not?
<j​effro256> Me: The FCMP++ hot-cold wallet is in a usable state: https://github.com/seraphis-migration/monero/pull/52. I'm doing some more testing now, and have already begun to split it up into smaller changes and make PRs to the Seraphis repo: #74-77. Also reviewing j-berman's stuff
<jberman> +1
<r​brunner7> SNeedlewoods: I think anything with rings really has low priority at this late time, and blackballing even less.
<j​effro256> Yeah blackballing is on its deathbed at this point, I wouldn't worry about continued support
<jberman> +1
<j​berman> me: completed support for 128 input FCMP++ txs, upstreamed PR's to fcmp-plus-plus (also included fabrizio's internal fix that fixes an internal test for divisors), did some review on 0xfffc 's PR 9494 (dynamic block span during sync), started looking into a few bugs reported by ofrnxmr to me in DM
<0xfffc> +1
<s​needlewoods> thanks for the feedback
<j​effro256> Yeah I wouldn't make it an explicit API endpoint
<j​berman> Would want to check into these a bit more, but initial take we most probably definitely not need any writers for rings after the fork (set/usnet). Readers (get / print) are maybes
<r​brunner7> Just wanted to complain a bit about jeffro's use of the term "cold", thinking so far that term only rightfully applies to Monero seeds on paper put away for 10 years, but a quick googling showed me that, surprise, it's me who is wrong with that ...
<r​brunner7> People seem to call every offline wallet "cold"
<r​brunner7> jberman: Those large-number-of-input transactions are not yet with PoWER, right? That is still quite some time away.
<r​brunner7> Not even sure about the PoW algorithm
<j​berman> Correct. PoWER can be implemented months from now. PoWER is strictly meant to protect a DoS vector for large input txs, and isn't strictly necessary to continue with testing / toward mainnet
<s​needlewoods> I never used these commands before, so I'm actually not sure what they're used for exactly, but this usage message for `set_ring` sounded concerning "Set the ring used for a given key image, so it can be reused in a fork"
<j​effro256> Yeah in my understanding, the general usage of the "cold wallet" means basically anything airgapped, even if it's arguable whether or not to use the term as such
<jberman> +1
<j​berman> I would say PoWER is a lower priority compared to multisig, completing HW wallets, and other tasks on the gneearl TODO list
<r​brunner7> SNeedlewoods: No, that's actually the maximum available privacy for using on a fork if you use the *same* rings, the right way to do it
<r​brunner7> Anything else may give away the true spend
<moneromooo> They're used to sync usage of monero with forks that fork the chain also, if you want to spend in both chains an old output that exists in both chains from prior to the fork.
<r​brunner7> But well, no chain forks, no worries :)
<moneromooo> It's the kind of thing that's totally useless unless you're in the corner ae where it's very useful.
<j​effro256> This is the correct way to do this because the alternative is making an entirely new ring on a different fork, which if the "true spend" is the only input shared across those two rings, it breaks sender privacy
<moneromooo> corner case*
<r​brunner7> Yeah, all this knowledge to prove that we are the real pros will be taken away by FMCP++, sigh
<j​effro256> The ringDB is used similarly in the case that you broadcast your transaction to the node and it rejects it. The wallet should remake the exact ring again. Otherwise, a node coudl fail you once, you remake your ring, and leak the true spend
<s​needlewoods> ah thank you all, I think I got it
<moneromooo> If your ring is "all output on the chain", which I think it is (or close enough), two inpependent sets are more or less equal in the first place, so ringdb is not needed.
<r​brunner7> Ok, if we are through with reports a friendly reminder that this peer selection PR of mine will be 2 months old in 2 days ... and will be glad to enjoy reviews :) https://github.com/monero-project/monero/pull/9939
<jberman> +1
<r​brunner7> Maybe during a small break from all that week-long FMCP++ work
<r​brunner7> Would be a pity to miss the next point update
<j​effro256> Yes I agree, will work on it this week
<rbrunner> +1
<rucknium> +1
<sneedlewoods> +1
<jberman> +1
<j​effro256> Sorry I meant to review earlier
<r​brunner7> Splendid, and no problem!
<r​brunner7> Ok, do we have something more to discuss today?
<r​brunner7> Does not look like it. Thanks everybody for attending, read you again next week!
<s​needlewoods> thanks everybody, cu
<j​effro256> Thanks everybody
````


# Action History
- Created by: rbrunner7 | 2025-07-25T17:09:21+00:00
- Closed at: 2025-07-28T18:34:26+00:00
