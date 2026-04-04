---
title: Bitcoin style unlock time
source_url: https://github.com/monero-project/monero/issues/3139
author: moneromooo-monero
assignees: []
labels:
- duplicate
created_at: '2018-01-16T15:11:58+00:00'
updated_at: '2018-08-15T12:57:03+00:00'
type: issue
status: closed
closed_at: '2018-08-15T12:57:03+00:00'
---

# Original Description
This would be useful to prevent a tx from being mined before a given block height. This is used by things like the Lightning network, and emulating it with a monero style lock time on an input is wasteful and awkward (though if the range needed is no more than 60 blocks, we could piggy back on using a recent coinbase - at the risk of reorg though).


# Discussion History
## hyc | 2018-01-16T15:21:13+00:00
Also, what would we do with locks that span a hardfork height?

## Gingeropolous | 2018-01-18T19:39:13+00:00
as i understand it, this means that the tx just stays in the txpool? (good thing its an on disk database now!!)

> Also, what would we do with locks that span a hardfork height?

Hrm, well if there's proof it was submitted in consensus, then it could be mined in... but thats a timestamping issue, so we're gonna end up with a blockchain in the txpool or something like that. 

## hyc | 2018-01-18T19:58:43+00:00
> as i understand it, this means that the tx just stays in the txpool? (good thing its an on disk database now!!)

Oh good point. So this becomes a new avenue for spamming the network, trying to fill the txpool. We could add an additional fee, multiplied by the length of the lock time. A bit annoying that we still don't have a way to compensate node operators.

## vtnerd | 2018-01-19T20:18:23+00:00
Nodes could drop (i.e. _not_ relay) a transaction that could not be mined until x or more blocks in the future. This does force the participant with the locked transaction to leave their software running so that they can broadcast at some future time point if necesssary. According to some random post on Bitcointalk this is what Bitcoin does, but I have not inspected its codebase to verify this claim.

## vtnerd | 2018-01-19T20:20:33+00:00
I forgot to mention that @hyc fee suggestion is interesting. Currently txes are automatically removed from the mempool if they have been there for 24 hours. The Bitcoin method is a bit easier on the node implementation, but harder on the wallets as I mentioned.

## Gingeropolous | 2018-01-20T06:33:10+00:00
hrm, yeah. I guess i mistakenly thought that the unlock-time transaction had to be in the mempool for it to serve its purpose (e.g., in a payment channel). But if the "other" end of the payment channel still has a valid transaction, I guess they can broadcast it whenever. 

Still quite the headscratcher about straddling consensus versions. Might need to take a page from bitcoin and consider some forward compatibility ... or is it backwards compatibility. I guess its backwards for us, because we're not concerned with old nodes having to find some "truth" in a newly formed transaction, but instead a new node still has to recognize an old transaction... but then whats the point of forking, if old consensus-version transactions can be mined. 

Or we just accept that all payment channels and other fancy locktime things need to settle to the chain by the fork height. 

## iamsmooth | 2018-01-20T09:43:42+00:00
> but then whats the point of forking, if old consensus-version transactions can be mined

To add new ones. That doesn't mean you necessarily invalidate old ones. 

My take on this when it was discussed before is to specify that these locks can only be used for some limited period of time in the future (for example six months). That is sufficient for payment channel type usage without baking in the need for indefinite compatibility. With a limit of six months that means only one scheduled hardfork has to maintain backward compatibility.

Also, as I understand it locked transactions aren't accepted into the mempool at all (in Bitcoin). You have to wait until they unlock, then submit. I don't think expecting node operators to host unripe transactions for free is reasonable. If you don't want to handle this broadcasting yourself, negotiate with a service provider, which includes how they are being paid.

## Gingeropolous | 2018-01-28T13:18:49+00:00
OK, so how exactly does this get implemented? Is this just an addition to the consensus protocol, and some additional meta data in the transaction?

## danrmiller | 2018-01-31T23:40:54+00:00
Passing on some thoughts from IRC.

< gmaxwell> you don't really want bitcoin style timelocks for these things [atomic swaps], I think, you want CSV style timelocks.
< gmaxwell> If they [monero] upgraded their ring-input to be a bulletproof or-gate thing, then they could also impose a CSV style timelock in it.

https://github.com/bitcoin/bips/blob/master/bip-0112.mediawiki


## CameronRuggles | 2018-03-03T01:05:42+00:00
This seems rather important for doing dominant assurance contracts (https://en.bitcoin.it/wiki/Dominant_Assurance_Contracts) and LN. Has any further development on this issue occurred? 

## moneromooo-monero | 2018-08-15T12:51:56+00:00
Looks like it's already been requested in #1184.

+duplicate

# Action History
- Created by: moneromooo-monero | 2018-01-16T15:11:58+00:00
- Closed at: 2018-08-15T12:57:03+00:00
