---
title: Wallet v0.16 does not accept date for restore height.
source_url: https://github.com/monero-project/monero/issues/6606
author: downystreet
assignees: []
labels: []
created_at: '2020-05-31T12:10:49+00:00'
updated_at: '2021-08-13T05:00:15+00:00'
type: issue
status: closed
closed_at: '2021-08-13T05:00:15+00:00'
---

# Original Description
When I restored a wallet with keys and it comes to the restore from height, it is not accepting the date format. I tried 2020-01-01 and it was throwing error. 

# Discussion History
## moneromooo-monero | 2020-05-31T12:44:26+00:00
You're not saying anything about what prompt or option or anything you're using.

## downystreet | 2020-05-31T13:16:28+00:00
I used the ./monerod --restore-deterministic-wallet. It looks like it only asks this when restoring a wallet and it said something like what height do you want to restore from or you can enter a date in the form of (yyyy-mm-dd). I tried entering 2020-01-01 and (2020-01-01) and it was giving me error. I can't remember what exactly it said but it would not allow me to use a date. I had entered the date for last version v0.15 and I never had any problems.  But, now that I think about it could my daemon configuration have been interfering with that too I guess?

OS: Centos 8
Kernel: 4.18.0-147.8.1

## moneromooo-monero | 2020-05-31T13:21:40+00:00
I just tried here, and 2020-01-01 works.
```
Restore from specific blockchain height (optional, default 0),
or alternatively from specific date (YYYY-MM-DD): 2020-01-01
Restore height is: 1372596
Is this okay?  (Y/Yes/N/No): 
```
Maybe you're adding some spaces or other characters ? The parsing is unforgiving for this, I'll make it a bit more lenient.

## downystreet | 2020-05-31T13:22:45+00:00
I entered it just like that but I'm thinking maybe my daemon settings were affecting it.

## moneromooo-monero | 2020-05-31T13:23:56+00:00
Paste the actual output please.

## moneromooo-monero | 2020-05-31T13:24:32+00:00
Oh, and make sure you use normal ASCII - signs, not fancy ones.

## downystreet | 2020-05-31T13:28:26+00:00
I just tried it again and it works fine, I don't know what was going on earlier.

## downystreet | 2020-05-31T13:30:05+00:00
Wait I think it is because I'm just running the regular daemon now without all of the rpc payment stuff.

## moneromooo-monero | 2020-05-31T13:31:43+00:00
I don't see why that'd affect the date parsing. Try again with the rpc payment enabled maybe ?

## downystreet | 2020-05-31T13:42:03+00:00
Ok, when I run it with the rpc stuff and use the date to restore it says Error: failed to get blockchain height. The daemon itself says: 
******************************************
You are now synchronized with the network. You may now start monero-wallet-cli.
********************************************
*************************************************
The daemon will start synchronizing with the network. This may take a long time to complete.
********************************************************

The status says height: 2110420/2110420

## moneromooo-monero | 2020-05-31T13:50:20+00:00
Ah, that explains it :)
Since your wallet does not have credits yet to pay for RPC, the daemon rejects your RPC, and the wallet can't check what height corresponds to which date.

# Action History
- Created by: downystreet | 2020-05-31T12:10:49+00:00
- Closed at: 2021-08-13T05:00:15+00:00
