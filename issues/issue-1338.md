---
title: 'Monero Tech Meeting #157 - Monday, 2026-02-09, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/1338
author: rbrunner7
assignees: []
labels: []
created_at: '2026-02-07T16:34:11+00:00'
updated_at: '2026-02-09T18:41:16+00:00'
type: issue
status: closed
closed_at: '2026-02-09T18:41:16+00:00'
---

# Original Description
Location is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting [here](https://github.com/monero-project/meta/issues/1335).


# Discussion History
## rbrunner7 | 2026-02-09T18:41:16+00:00
````
<r​brunner7> Meeting time. Hello! https://github.com/monero-project/meta/issues/1338
<j​berman> *waves*
<s​needlewoods> Hello
<s​yntheticbird> Hi
<r​brunner7> Something administrative first: Ok for you people to skip next Monday's February 16 meeting, because of Monerotopia, and meet again in 2 weeks?
<jberman> +1
<jeffro256> +1
<s​needlewoods> I'm fine with that
<r​brunner7> Ok, if nobody contradicts still, I will schedule that way.
<r​brunner7> On to the reports - what happened last week?
<s​needlewoods> Started with `/transfer*`/`/sweep*` commands, now trying to figure out how to get the necessary information for `cryptonote::tx_construction_data` from `UnsignedTransaction` and `PendingTransaction` needed in `/describe_transfers`
<r​brunner7> In the RPC server, right?
<j​effro256> Howdy
<s​needlewoods> wallet_rpc_server, yes
<j​berman> me: some PR followup, set up a 4-phase plan to get the FCMP++ integration audited, got pre-fork multisig working / tests passing
<r​brunner7> What do you mean with "pre-fork multisig"? Does that need to "get it working again"?
<j​berman> Ya it was borked upon integrating the curve tree sync into wallet2
<j​berman> I can expand a bit further on that
<r​brunner7> As an unintended side effect I hope :)
<j​berman> So the current multisig requires all multisig participants collaborate to generate key images for received outputs
<j​berman> Thus, in order to determine if an output has been spent, the current impl will re-sync a wallet upon generating received output key images. aka receive output in block n, if the multisig wallet has synced to block n+10,000, then the multisig participants collaborate to generate the received output's key image, then all their wallets will re-sync the wallet starting from block n
<j​berman> the problem is: upon introducing the curve tree sync into wallet2, the wallet can't re-sync past a max of 100 blocks by default, otherwise it needs to re-sync from its restore height
<j​berman> So after discussing this with jeffro256 , who recognized that technically the wallet doesn't need to re-sync in this case, I ended up reusing the "backgound sync" implementation for multisig sync, so that upon identifying the receive output in block n, the multisig wallet will then sync all possible spends of that output going forward too, so that when generating the key image lat<clipped messag
<j​berman> er, it can process the "background sync cache" to identify spent key images if there were any
<jeffro256> +1
<jeffbabb> +1
<j​berman> that way the multisig wallet doesn't have to re-sync as it currently does
<j​berman> we've known this part of multisig has been broken since the curve tree sync was introduced fwiw, it's been on the TODO list / a FIXME was in the code too
<j​berman> Can see this PR gets rid fo the FIXME: https://github.com/seraphis-migration/monero/pull/291/changes
<j​berman> in wallet2 line 15041
<r​brunner7> Interesting. I would have guessed it's just a question of ignoring that 100 blocks limit for such cases, but I am sure that's because I don't know enough about the actual issues.
<j​berman> if you recall how the wallet now builds the tree locally, the wallet throws away data from the tree that's older than 100 blocks that it doesn't need
<jeffro256> +1
<j​berman> otherwise it has to keep the multi GB tree cached locally
<r​brunner7> Yeah, but pre-fork there is no tree yet, no?
<r​brunner7> Ah, also post-fork the multisig transactions can come in later than 100 blocks
<j​berman> good q. the updated wallets are currently set up to re-sync from their restore height, and start building the tree, so that when the fork comes, they can spend outputs received before the fork with the FCMP++ proof
<j​berman> this change is necessary to ensure that multisig wallets correctly maintain the tree for when the fork does occur
<j​berman> and that too
<j​effro256> Yeah I think a similar background sync technique could be employed for multsig by saving all txs with rings with ring members that we own , it just hasn't been done yet
<j​berman> yep that's what that PR does :)
<r​brunner7> Ok. Usually if the remaining issues get complex fast, like it seems to happen here, it means that the end is almost there, with "end" meaning "working".
<j​berman> what's now "working" is pre-fork multisig with an FCMP++/Carrot compatible wallet. What's not yet working, and is going to be a fairly significant lift to get working, is FCMP++/Carrot multisig
<r​brunner7> Ok. Will you implement that, jberman ?
<j​berman> I started looking into it and it's a pretty major can of worms, I'm not sure yet. I think it will be a bridge that we'll have to cross soon enough though
<r​brunner7> Sounds like it :)
<r​brunner7> Alright, if we are through with the reports, anything beyond that to discuss today?
<r​brunner7> Don't do anything unwise when re-entering the US coming from Mexico after Monerotopia perhaps ...
<s​needlewoods> In regards to stressnet, AFAICT v1.6 is running very smoothly, the network is currently beeing stressed with ~650MB in tx pool and 887 blocks backlog and monerod is using ~1.5GB memory
<jberman> +1
<s​needlewoods> and I hope everyone going to MoneroTopia is having a great time, I'm excited for the virtual conference
<r​brunner7> I second that, live the good life at that conference. I think we can close, thanks everybody for attending, read you again in **two** weeks.
<s​needlewoods> thanks everyone, cu
<s​yntheticbird> thanks, very tasteful meeting
<j​berman> thank you!
<j​effro256> Ah I see. Is the significant lift for FCMP++/Carrot the fact that ring members don't exist ?
<j​effro256> You should be able to save all txs with at least one scannable output, and that should capture everything since that's a rule in the Carrot code
<j​berman> no the whole tree sync part should be good to go now. the significant lift is going to be constructing the SAL proof I think
<j​effro256> Oh yeah, that part does need a lot of new crypto
<j​effro256> IIRC kayaba said that they wrote a Rust lib for multisig SA/L proving used Carrot-derived addresses
<j​effro256> Which is awesome
<j​effro256> And it should be usable for non-Carrot-derived wallets too
<j​berman> https://github.com/monero-oxide/monero-oxide/blob/92af05e0d44bd1ec1fed6028a8d2aade615f805a/monero-oxide/ringct/fcmp%2B%2B/src/sal/legacy_multisig.rs
<j​effro256> If we keep the same legacy multisig API, I think that it can be fairly simple to upgrade the SA/L proving
<j​effro256> Since you've already handled the tree syncing part
<j​berman> kayaba also wrote up this guide on dropping in the rust impl into the wallet2: https://gist.github.com/kayabaNerve/3b2c648c623bc4ce4ca288725428ea76
<j​berman> and that was applicable for clsag
<j​effro256> A *really* big rework would be necessary to handle multisig coordination without partial key images
<j​effro256> But I think that we can activate the HF without support for the new multisig API
````


# Action History
- Created by: rbrunner7 | 2026-02-07T16:34:11+00:00
- Closed at: 2026-02-09T18:41:16+00:00
