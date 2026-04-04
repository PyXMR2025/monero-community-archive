---
title: view-only wallet with imported key-image fails to show outgoing transfer
source_url: https://github.com/monero-project/monero/issues/1740
author: zveda
assignees: []
labels:
- bug
created_at: '2017-02-17T12:17:14+00:00'
updated_at: '2018-01-09T09:58:24+00:00'
type: issue
status: closed
closed_at: '2018-01-09T09:56:29+00:00'
---

# Original Description
I have a view-only wallet as well as a spending version of the same wallet. I then sweep all the monero from this wallet to another separate wallet. The spending version shows all the incoming and out-going transfers of the wallet. I then copy the key-images from the spending version to the view-only wallet. It now correctly shows the balance as 0 but it fails to show any outgoing transfers from the wallet. When I run show_transfers all I see is incoming transfers. Yet balance is 0. 

I am pretty sure this is not the intended behaviour. I would like to see any outgoing transfers from the view-only wallet with the inputs for which I have imported key-images. 

I am running Monero 'Wolfram Warptangent' (v0.10.1.0-release).

# Discussion History
## ghost | 2018-01-07T18:02:52+00:00
Does this still occur in the latest release?

## zveda | 2018-01-08T11:04:01+00:00
Yes, I just checked. I exported key-images from the spending wallet and imported them in the watch-only. The balance shown is the same in both but the show_transfers are different. Some _out_ transactions are shown in the watch-only wallet and some are not. 

The final _out_ transaction in the spending wallet is shown as an _in_ transaction in the watch only, where the amount is the total balance of the wallet.

I'm using version 0.11.1.0.

## stoffu | 2018-01-08T11:43:07+00:00
That's strange, I've made a patch that specifically addressed that exact issue: https://github.com/monero-project/monero/pull/2377

This should be included in version 0.11.1.0. Can you do `rescan_bc` on the watch-only wallet and try again? Also, can you post a full log?

## dEBRUYNE-1 | 2018-01-08T12:29:13+00:00
+bug

## zveda | 2018-01-09T05:51:21+00:00
Just finished doing the rescan_bc, then re-imported the old key-images file (from yesterday - but last transaction in this wallet was more than a month ago - so key images file should have worked). The balance is way too large. Seemed to add up all transactions as if they were _in_ transactions.

Then I exported key images file from the write wallet and imported it into the read-only wallet. Now read-only wallet shows the correct balance, but show-transfers still shows only _in_ transactions.

Attached log level 4 file from monero-wallet-cli, but I only turned the logging on for the last part of the rescan_bc and the imports of key-images. It is almost 20mb.


  
  

## stoffu | 2018-01-09T06:58:09+00:00
@zveda 
It was my misunderstanding: that patch didn't go into 0.11.1.0, so you need to use the latest master to see the effect of the fix.

P.S.
You may want to delete the wallet log file above since it contains information about your real funds and key images.

@dEBRUYNE-1 
This issue can be closed.

## dEBRUYNE-1 | 2018-01-09T09:51:23+00:00
+resolved

# Action History
- Created by: zveda | 2017-02-17T12:17:14+00:00
- Closed at: 2018-01-09T09:56:29+00:00
