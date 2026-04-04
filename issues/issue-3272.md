---
title: Wrong balance and impossible transactions
source_url: https://github.com/monero-project/monero-gui/issues/3272
author: stephlo76
assignees: []
labels: []
created_at: '2020-12-16T11:11:35+00:00'
updated_at: '2021-04-21T01:35:38+00:00'
type: issue
status: closed
closed_at: '2021-04-21T01:35:38+00:00'
---

# Original Description
Hi guys,
I am using  Version 0.17.1.7 of monero-wallet-gui on Debian. Icreated a new wallet and transferred 0.81 Monero to it. Then I tried to transfer 0.68 Monero to another account which failed. I tried it again and it worked. My balance shuld now be 0.13 Montero, but the app shows 0.95 Monero, even after days. I do not khow where this amount comes from. Happy about the unearned money, I repeatedy tried to transfer Monero to other accounts; now it always fails. If I open the failed transcations and click on the "P" sign, it says "Couldn't generate a proof because of the following reason: daemon returned wrong response for gettransactions, wrong txs count=0, expected 1"
I tried to connect to a public node according to some website, with no success. Is the account now permanently broken? How can such a buggy behavior be explained?
Thanks
Stephan
![error](https://user-images.githubusercontent.com/37303377/102341230-d28d0180-3f97-11eb-8fe1-2d7668406d1c.png)


# Discussion History
## selsta | 2020-12-16T11:13:32+00:00
Which remote node did you use to get failed transactions?

You have to rescan to get your correct balance, but first you have to connect to a working remote node, try one from here: https://github.com/monero-project/monero-gui/issues/3140#issuecomment-706440354

Afterwards go to Settings -> Info, click on "(Change)" next to wallet creation height and then on okay twice. This will start the rescan process.

## stephlo76 | 2020-12-16T11:23:11+00:00
I connected to node 88.198.199.23 and rescanned (not sure whether I got this right; this is done automatically right?) It still shows the same balance. Then I cliced "Change" on the wallet restore height, left the number untouched and hit OK. It took a while and now is  finished, still showing the same balance. 
![balance](https://user-images.githubusercontent.com/37303377/102342354-67dcc580-3f99-11eb-9fa2-1dc5bfbed7ad.png)


## selsta | 2020-12-16T11:24:57+00:00
You have to wait until all wallet blocks are scanned. Your screenshot shows 20000 blocks remaining.

Also FYI you don’t seem to use the latest version.

## stephlo76 | 2020-12-16T11:26:48+00:00
Aaah great! Now it shows the correct balance. Thanks a lot!Will transactions now work? And, do these wrong balances occur often? That looks like a buggy software

## selsta | 2020-12-16T11:27:55+00:00
Transactions should work, yes. Which node did you connect to previously? It sounds like you connected to a broken node previously.

## stephlo76 | 2020-12-16T11:30:21+00:00
Initially, I think I had my own node? (Not sure whether I understand that correctly) and connected to a remote node only after the error occured, according to some website. I deleted the name of that node already, sorry. Thanks a lot for your help!!

## selsta | 2021-04-21T01:35:38+00:00
Issue is resolved.

# Action History
- Created by: stephlo76 | 2020-12-16T11:11:35+00:00
- Closed at: 2021-04-21T01:35:38+00:00
