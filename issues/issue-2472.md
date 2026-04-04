---
title: 'Transaction fails with error: “original_output_index too large”'
source_url: https://github.com/monero-project/monero/issues/2472
author: frost-monkey
assignees: []
labels: []
created_at: '2017-09-18T16:47:37+00:00'
updated_at: '2017-10-02T19:48:23+00:00'
type: issue
status: closed
closed_at: '2017-10-02T19:48:23+00:00'
---

# Original Description
I'm a pool operator, and for the first time tonight, I got this error while trying to send a payout to miners:

    Error with transfer RPC request to wallet daemon {"code":-4,"message":"original_output_index too large"}

For what I can see from the source code, the error happens in this file, at line 4364:

https://github.com/monero-project/monero/blob/master/src/wallet/wallet2.cpp

Problem is, I don't exactly get what the problem is. For what it's worth, I made sure all addresses were valid standard XMR wallet addresses, and that none of them appeared twice in the parameters. I'm trying to send payouts between 0.1 and 2.0 XMR.

I'm using [this pool software](https://github.com/clintar/cryptonote-xmr-pool) with a slight modification: I use transfer_split instead of transfer. This particular transaction had 31 different recipients.

I've done my best to find questions / threads / information about that specific error, and have found nothing. Any help would be greatly appreciated.

Thanks a lot!

# Discussion History
## moneromooo-monero | 2017-09-19T20:08:37+00:00
Any other interesting/unusual messages near that error ? I've tried sending 31 amounts, and did not get any trouble (same address though, guess I'll try making 31 different temporary addresses now).

## frost-monkey | 2017-09-20T02:55:10+00:00
I'll get back to you with more details as soon as I can.

I finally decided to manually make two payout rounds, and realized there were in fact 37 addresses, but only 31 appeared in the failed transaction log. At some point 37 became 31 or the opposite, and I suppose that because the numbers didn't match, it caused the error I got.

## moneromooo-monero | 2017-09-20T08:57:04+00:00
I've reproduced it now, so no need for further info.

## moneromooo-monero | 2017-09-20T09:37:08+00:00
https://github.com/monero-project/monero/pull/2491

## frost-monkey | 2017-09-20T13:25:36+00:00
Thanks a lot for your time and help. You guys make a tremendous job!

## moneromooo-monero | 2017-10-02T19:35:14+00:00
+resolved

# Action History
- Created by: frost-monkey | 2017-09-18T16:47:37+00:00
- Closed at: 2017-10-02T19:48:23+00:00
