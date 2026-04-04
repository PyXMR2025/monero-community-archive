---
title: Help me to call wallet rpc from other ip
source_url: https://github.com/monero-project/monero/issues/3212
author: top1st
assignees: []
labels:
- invalid
created_at: '2018-01-30T16:03:04+00:00'
updated_at: '2018-03-07T11:48:37+00:00'
type: issue
status: closed
closed_at: '2018-03-07T11:48:37+00:00'
---

# Original Description
![image](https://user-images.githubusercontent.com/23559697/35576380-c8b445fc-0619-11e8-8514-9e3c8ebede30.png)

I installed command line tool on ubuntu 16.04
I cannot see wallet rpc port listine on 18082
Domain Rpc works but wallet RPC not listening 
I refered this documents
https://getmonero.org/resources/developer-guides/wallet-rpc.html
https://getmonero.org/resources/developer-guides/wallet-rpc.html#getbalance

# Discussion History
## leonklingele | 2018-01-30T16:59:54+00:00
Did you specify `--rpc-bind-ip 0.0.0.0`?
If so, you need to confirm with `--confirm-external-bind`. If not, please check the logs and post the exact command arguments you're using to start `monerod`.

## moneromooo-monero | 2018-01-30T17:56:54+00:00
And this is a bug tracker, not a help forum. I'll leave that open since someone's trying to help, but please don't again, there's IRC or reddit for this.

## top1st | 2018-01-31T03:21:53+00:00
above image is when i run  $ ./monerod 

and next is when is tried --rpc-bind-ip and --confirm-external-bind
![image](https://user-images.githubusercontent.com/23559697/35599045-d9fd6922-0661-11e8-8b3b-efb24fa5024a.png)

![image](https://user-images.githubusercontent.com/23559697/35599084-037ff9fe-0662-11e8-8d2d-fff3c3e7ac6b.png)



## leonklingele | 2018-01-31T10:47:28+00:00
I've misread your post, sorry. You're trying to start the `wallet` RPC, but `monerod` is not your wallet :) 

There's a dedicated binary called `monero-wallet-rpc` inside the same folder which you can start with the following args: `--rpc-bind-port 18082 --prompt-for-password --wallet-file PATH/TO/WALLET_KEY`.
__Do not__ use `--rpc-bind-ip` unless you know what you're doing. Make sure to have a daemon running.

## moneromooo-monero | 2018-03-07T11:42:20+00:00
+invalid

# Action History
- Created by: top1st | 2018-01-30T16:03:04+00:00
- Closed at: 2018-03-07T11:48:37+00:00
