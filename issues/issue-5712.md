---
title: Protocol allows ring members younger than lock time in reference wallet
source_url: https://github.com/monero-project/monero/issues/5712
author: Mitchellpkt
assignees: []
labels: []
created_at: '2019-07-01T04:09:30+00:00'
updated_at: '2019-11-26T23:33:44+00:00'
type: issue
status: closed
closed_at: '2019-11-26T23:33:44+00:00'
---

# Original Description
The vast majority (98.4%) of ring signatures follow the 10 block lock time implemented in reference wallet. A minority (1.6%) of ring signatures include members less than 10 blocks old, which (1) causes these transactions to stand out and (2) heuristically suggests when the output was spent when this characteristic appears in transaction chains.

Protocol should enforce (privacy-relevant) reference wallet rules, so I recommend enforcing the 10-block lock at the protocol level. There are multiple ways this could be approached... A strict version would be to reject any transactions whose youngest ring member is less than 10 blocks old, while a more forgiving protocol would leave them in the memory pool until the 10 block lock time has passed. (The latter is more lenient, but not robust against archival nodes.)

![https://raw.githubusercontent.com/noncesense-research-lab/Konferenco2019/master/images/juvenile_histogram.png](https://raw.githubusercontent.com/noncesense-research-lab/Konferenco2019/master/images/juvenile_histogram.png)

![https://raw.githubusercontent.com/noncesense-research-lab/Konferenco2019/master/images/juvenile_heatmap.png](https://raw.githubusercontent.com/noncesense-research-lab/Konferenco2019/master/images/juvenile_heatmap.png)

What are your thoughts?

(More information available at [k2019.noncesense.org](http://k2019.noncesense.org) and during [Visualizing Monero (15:15)](https://youtu.be/XIrqyxU3k5Q?t=915) talk)

# Discussion History
## iamsmooth | 2019-07-01T21:48:28+00:00
Agree with consensus enforcement. This is a simple check. In fact consensus already checks unlock on some outputs (coinbase and those with explicit unlock time) so checking it on all actually makes consensus _simpler_.


## who-biz | 2019-07-24T00:31:58+00:00
>Agree with consensus enforcement. This is a simple check. In fact consensus already checks unlock on some outputs (coinbase and those with explicit unlock time) so checking it on all actually makes consensus simpler.

@iamsmooth Does consensus actually check unlock time?  If so, pointing me to somewhere in code would be awesome.  I have created transactions with an unlock time of many explicit values in the past.  All of which are recorded to the blockchain and confirmed.  It didn't appear to me that consensus checks this field at all (At least, as far as P2P transactions are concerned).  

If it does so with coinbase, that would be news to me. But it is something I have not looked into, as far as I have with the P2P txs. 

## HorribleGelatinousBlob | 2019-07-24T04:21:32+00:00
stop wasting time asking people to teach you how the code works. there are other, more appropriate places for that

## who-biz | 2019-07-24T05:47:53+00:00
Okay... then disregard my question, if we don't like when people ask for clarity on false information.  

Let's only go with the P2P transfers then. Nothing about unlock time is enforced by consensus whatsoever.  You can test this yourself by changing `CRYPTONOTE_DEFAULT_TX_SPENDABLE_AGE` in `src/cryptonote_config.h` to `0`, and then transferring a given amount as you would normally.

FWIW, I thought there was a consensus level check for this too. But it would appear it is strictly wallet side. Although, it’s no mystery why this would be thought (if @iamsmooth was going off the words of others before attempting this himself, as I was)

## iamsmooth | 2019-07-25T00:06:13+00:00
@who-biz It should be checking here: 

https://github.com/monero-project/monero/blob/master/src/cryptonote_core/blockchain.cpp#L3427

If that isn't working, then you have identified a bug

## who-biz | 2019-07-25T00:16:59+00:00
Yeah, that check appears to pass when the wallet/node creating the transaction has changed the precompile constant’s definition.

To me, that check looks only to ensure that inputs are unlocked at the time of spending. Nothing to be said about the future spending of outputs there, inherently.

Further, if we send these coins to our own address, we can spend them as soon as the block is confirmed.

## iamsmooth | 2019-07-25T00:25:41+00:00
@who-biz If you think you have identified bug then please create a new issue for it.

FYI, the correct behavior is to check that the lock time of transaction A is satisfied when later spending outputs from transaction A. If you think you are seeing something other than that and can clearly describe how to reproduce it then open an issue.


## who-biz | 2019-07-25T01:33:37+00:00
I am not sure it is a bug.  Since unlock times are defined as precompile constants, and substituted inline... This doesn't seem so much one.

<del>It seems somewhat obvious to me, in retrospect, that such a value could be changed and it would not affect overall consensus. The transaction prefix is at no point checked for validity by any node (as per CNS005).  Unlock time is a field within the prefix. So this would not be an unexpected behavior, given that.</del> 

Edit: I'm mistaken, this is in the block header.  Yeah, maybe you're right in that case.  Freeform fields in the header should be a no-no, I think.

This issue is for discussing a protocol-level enforcement of a value that is not locally scoped... So I feel this is the right place for the detail I'm referencing.  I don't see it as an issue so much as an idiosyncracy.   However, if the general agreement is that an unlock time of `0` should be invalid, I'll open a new one -- sure.

## moneromooo-monero | 2019-09-06T13:31:09+00:00
#5882

## Mitchellpkt | 2019-11-26T23:33:44+00:00
Issue fixed here: https://github.com/monero-project/monero/commit/a444f06e53b218cc8bd091e5283828beb3e7d9af

# Action History
- Created by: Mitchellpkt | 2019-07-01T04:09:30+00:00
- Closed at: 2019-11-26T23:33:44+00:00
