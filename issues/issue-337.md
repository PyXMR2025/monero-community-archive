---
title: Wallet creates $USER directory name in $USERs root by default (macOs)
source_url: https://github.com/monero-project/monero-gui/issues/337
author: dternyak
assignees: []
labels: []
created_at: '2016-12-22T18:47:46+00:00'
updated_at: '2016-12-22T20:27:49+00:00'
type: issue
status: closed
closed_at: '2016-12-22T20:25:26+00:00'
---

# Original Description
Instead of `/Users/first-last/monero/mywallet.keys` as expected, the GUI creates `/Users/first-last/first-last/mywallet.keys`

# Discussion History
## Jaqueeee | 2016-12-22T19:03:23+00:00
cannot reproduce this. Does it also say this path on the create wallet page in wizard?

## Jaqueeee | 2016-12-22T19:04:54+00:00
does your first or lastname include any non-ascii characters btw?

## dternyak | 2016-12-22T19:06:25+00:00
It does not - and the wallet path on the wizard create page claimed it would create `/Users/first-last/monero`

## Jaqueeee | 2016-12-22T19:18:31+00:00
ok. The expected default path is actually `/Users/$userName/Monero/wallets/$walletName/$walletName.keys`
if you don't change the $walletName when you create the wallet it would be the same as $userName.  
But in your case the monero and wallets folders never gets created?
Trying to reproduce this. Do you have a space between first and last? 


## dternyak | 2016-12-22T19:55:47+00:00
Exactly. no space. 

Very strange that we're not getting the same results! 

## Jaqueeee | 2016-12-22T20:10:36+00:00
Could you try running the wallet in terminal and paste the log when creating a wallet?
To start gui in terminal:
`./monero-wallet-gui.app/Contents/MacOS/monero-wallet-gui`


## dternyak | 2016-12-22T20:25:26+00:00
@Jaqueeee I deleted all wallet files and tried to simulate the same conditions as the original entry - Now it creates at the correct location - /Users/first-last/Monero/wallets/wallet-name.

Since I can't even reproduce myself, I'm going to close this. 


## Jaqueeee | 2016-12-22T20:26:46+00:00
OK. Too bad. Maybe we'll never get the answer to what happened! ;)

## dternyak | 2016-12-22T20:27:49+00:00
@Jaqueeee Hehe I am almost positive I did not mess with the wallet default because I was so eager to play with the beta! But maybe I did, and maybe that was the cause. 

# Action History
- Created by: dternyak | 2016-12-22T18:47:46+00:00
- Closed at: 2016-12-22T20:25:26+00:00
