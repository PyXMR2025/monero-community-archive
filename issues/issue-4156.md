---
title: monero-wallet-rpc shows usually 'no connection to daemon'
source_url: https://github.com/monero-project/monero/issues/4156
author: skinderis
assignees: []
labels: []
created_at: '2018-07-20T08:09:32+00:00'
updated_at: '2025-12-19T16:54:58+00:00'
type: issue
status: closed
closed_at: '2025-12-19T16:54:58+00:00'
---

# Original Description
I was talking about this issue in the comments, but I think it's worth opening a new one as it is important. 

I am running two docker containers, on on is **monero-wallet-rpc** another runs **monerod**, **monero-wallet-rpc** uses **monerod** container as **daemon-address**.

The issue I am facing is that wallet sometimes shows message `{'code': -38, 'message': 'no connection to daemon'}`. This error makes a lot of problems for me as I can't automate **transfer** method. My code is trying to send some **XMR** and when it shows this error I have to fix it by hand.

The error `{'code': -38, 'message': 'no connection to daemon'}` is not showing all the time it's 50% of succeeding.

How can I trigger wallet to not fail during transfer? Maybe I can call some method to  keep `wallet connected to daemon`?

Version I am running is **v0.12.3.0**

# Discussion History
## moneromooo-monero | 2018-08-13T16:46:11+00:00
If you run daemon and wallet with --log-level 2, you might see something of interest when this happens, or shortly before that.

## moneromooo-monero | 2018-08-18T15:52:31+00:00
Try adding --trusted-daemon to monero-wallet-rpc, if the address for the other container doesn't go through 127.0.0.1.

## moneromooo-monero | 2019-06-15T10:51:39+00:00
Does it still happen ? If not or no reply I'll close.

# Action History
- Created by: skinderis | 2018-07-20T08:09:32+00:00
- Closed at: 2025-12-19T16:54:58+00:00
