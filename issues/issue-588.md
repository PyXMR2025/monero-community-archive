---
title: Ouputs found by view-wallet but not by spending/regular wallet
source_url: https://github.com/monero-project/monero-gui/issues/588
author: dternyak
assignees: []
labels: []
created_at: '2017-03-21T19:59:51+00:00'
updated_at: '2017-03-22T20:47:18+00:00'
type: issue
status: closed
closed_at: '2017-03-22T20:38:05+00:00'
---

# Original Description
I have 2 transactions (outputs, not inputs, as I realize view wallet is not able to properly track inputs/spends) that the view wallet finds, but the spend wallet does not.

Neither of them use payment ids. 

I can provide more information directly as this seems to be a high-priority issue. 

# Discussion History
## Jaqueeee | 2017-03-22T15:38:05+00:00
Is the spend wallet a cold wallet or is it connected to a node?
Have you tried rescanning the wallet cache? I would suggest renaming the cache and not delete it if you want to keep the tx keys. 

## dternyak | 2017-03-22T19:04:47+00:00
@Jaqueeee The spend wallet is connected to a local node, as is the view wallet.

I'll try re-creating the spend via mnemonic, that should work the same as renaming the cache afaik. 

## Jaqueeee | 2017-03-22T19:09:19+00:00
@dternyak yeah, it should do the same. But it will take longer time if you don't supply a restore height. Could you describe the workflow prior to this happened? You created a tx in view wallet and signed it in spend wallet, and then submited from view wallet? And now the transaction doesnt show up in the spend wallet?

## dternyak | 2017-03-22T19:12:49+00:00
@Jaqueeee Unfortunately I only noticed the discrepancy between the view-wallet and spend wallet after a few weeks, so I can't remember exactly what I did on the day that they got out of sync. 

I *think* I had the view-wallet up and running when I sent the Monero, while connected to a remote node. 

At some later point, I switched to the spend wallet, and then a few weeks later I noticed that the amounts were off after I switched to a local node for both wallets. 

Not sure what else I can offer. I'll let you know what happens when I restore from mnemonic (in the process now). 

## dternyak | 2017-03-22T20:17:48+00:00
Sorry for spamming, but I just had another thought:

Is it possible for the GUI (spend) wallet to not be able to know all of the spends it made in the past?

I understand the view wallet could have a higher balance because it is not able to know all of the spends you made, but the spends the transaction history is showing does not match up with the difference between view and spend wallet.

E.g. I have 2 spends that the transaction history shows, totaling ~1 monero. However, the difference in the balance is 5 Monero (not exact values, but you get the idea.)

I definitely feel like the view-wallet has the correct balance (minus the 1 monero is not able to track that I know I did send), but maybe I am wrong and the GUI spend wallet simply isn't picking up a spend I made in the past that I forgot about. 

## dternyak | 2017-03-22T20:38:05+00:00
@Jaqueeee Final post:

I don't think theres a bug at all, just some confusing UX inherit due to the anon.

I was under the impression that while the view-wallet wouldn't be able to "view" spends, the transactions that it does display would be accurate. It seems this is not the case, as the view-only wallet is showing a transaction that I made that was a net-negative as a positive, e.g. sending 1 monero in the spend is actually receiving 20 in the view wallet. Perhaps this was caused by me sending to myself as a test, or just as an input back to myself when I an input I created was smaller than the output it was created from. 

If my understanding of monero internals is correct, than an input to a new transaction will also have an input back to yourself if the input is smaller than the output (after the miner fee), so this behavior is technically correct.

Going to close, but we should note that this *will* be confusing to new users

# Action History
- Created by: dternyak | 2017-03-21T19:59:51+00:00
- Closed at: 2017-03-22T20:38:05+00:00
