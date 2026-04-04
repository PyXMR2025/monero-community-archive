---
title: Not receiving transaction on second receive address
source_url: https://github.com/monero-project/monero-gui/issues/3183
author: dundunn
assignees: []
labels: []
created_at: '2020-10-20T05:36:03+00:00'
updated_at: '2020-10-26T19:29:59+00:00'
type: issue
status: closed
closed_at: '2020-10-26T19:29:58+00:00'
---

# Original Description
I created a second receive address in the client and used that to buy coins. My exchange sent me the transaction ID but there is no transaction to be found in the client. I trust the exchange but how can I get to the coins from here? Network status is connected and the wallet is synced.

# Discussion History
## selsta | 2020-10-20T06:54:28+00:00
Do you have a transaction id?

## dundunn | 2020-10-20T07:23:18+00:00
Sorry of course :facepalm: 

https://xmrchain.net/search?value=7f24dc9621247ff297c09859802351f08c16fb9e5ecfc07116d288f68f15b2c2

## selsta | 2020-10-20T07:33:44+00:00
Did you create the new receiving address on the "Account" tab or on the "Receive" tab?

Also can you go to Settings -> Log and enter "status" and post the output here.

## dundunn | 2020-10-20T08:09:55+00:00
> Did you create the new receiving address on the "Account" tab or on the "Receive" tab?

I created the wallet in the receive tab. 

```
>>> status
[10/20/20 10:08 AM] 2020-10-20 08:08:04.469 I Monero 'Oxygen Orion' (v0.17.1.1-release)
Height: 2212305/2212305 (100.0%) on mainnet, bootstrapping from 159.65.173.58:18089, local height: 1 (0.0%), not mining, net hash 1.64 GH/s, v14, 0(out)+0(in) connections
```

## selsta | 2020-10-20T08:13:52+00:00
Looks all good.

Can you go to Settings -> Info and check if Wallet creation height is lower than 2211852

If yes, click on "(Change)" and press okay twice and wait for it to rescan.

## dundunn | 2020-10-20T09:22:42+00:00
> Can you go to Settings -> Info and check if Wallet creation height is lower than 2211852
> 
> If yes, click on "(Change)" and press okay twice and wait for it to rescan.

Thank you so much, that was the issue. The XMR are now available after rescanning. 

## dundunn | 2020-10-26T13:19:22+00:00
Ok I still having issues with those coins, I can't do anything with them. When I'm trying to send them to an other wallet the transaction seems to go through but after some minutes the recipient changes from `Waiting for confirmations` to `Failed`. The transaction disappears when I restart the client. 

## selsta | 2020-10-26T15:08:50+00:00
How often did you try? If this happened multiple times I would try switching to a custom node as explained here: https://github.com/monero-project/monero-gui/issues/3140#issuecomment-706440354

Otherwise I would simply try sending again.

## dundunn | 2020-10-26T19:29:58+00:00
I tried it about 5 times with different wallets. But using the remote node worked :) Thanks for the help.  

# Action History
- Created by: dundunn | 2020-10-20T05:36:03+00:00
- Closed at: 2020-10-26T19:29:58+00:00
