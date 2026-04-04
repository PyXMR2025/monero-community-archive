---
title: Show a wallet's restore height more prominently
source_url: https://github.com/monero-project/monero-gui/issues/2126
author: mmbyday
assignees: []
labels:
- enhancement
created_at: '2019-04-29T07:55:40+00:00'
updated_at: '2019-06-21T19:27:35+00:00'
type: issue
status: closed
closed_at: '2019-06-21T19:27:35+00:00'
---

# Original Description
Specifically in the wizard > create new wallet screen
and in the keys page.

These are two opportunities for the user to backup this salient piece of data which will lead to a better experience when restoring their wallet. Not having proper restore height data can cause undue user frustration and leave a poor wallet impression.

+proposal


# Discussion History
## sanderfoobar | 2019-04-29T16:57:01+00:00
+enhancement

## GBKS | 2019-05-25T06:47:37+00:00
This has probably been already discussed, but is there no better name for "restore height"? Maybe something like "Wallet creation block number"?

## mmbyday | 2019-06-01T06:33:40+00:00
Good point @GBKS Wallet creation block number is more descriptive and self-evident. Restore height is likely a legacy term from the beginning of time. There's other terms that could use clean up in the wallet. One that I can recall is secret key vs. private key. There's actually an issue on this one https://github.com/monero-project/monero-gui/issues/1064 

## selsta | 2019-06-01T06:35:09+00:00
CLI uses the term restore height. Not sure if we should aim to stay consistent with it.

## erciccione | 2019-06-01T08:53:42+00:00
*restore height* is used everywhere (other wallets, guides, moneropedia, etc). Changing the term only in the GUI would cause a lot of confusion for the users. The term should stay consistent across all Monero projects.
 
So, if changed here, *restore height* should be changed everywhere. I don't see any strong reason to go trough this process.

# Action History
- Created by: mmbyday | 2019-04-29T07:55:40+00:00
- Closed at: 2019-06-21T19:27:35+00:00
