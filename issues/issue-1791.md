---
title: How to display pending transactions in get_transfers?
source_url: https://github.com/monero-project/monero/issues/1791
author: gituser
assignees: []
labels: []
created_at: '2017-02-24T06:56:22+00:00'
updated_at: '2017-02-24T19:26:56+00:00'
type: issue
status: closed
closed_at: '2017-02-24T19:26:56+00:00'
---

# Original Description
Hi.

I've been using get_transfers rpc call to get all transfers from our wallet in and out.

Is there any way to show there as well pending transactions which are not included in the block yet?
I'm on 0.10.1-release.

Thanks.


# Discussion History
## moneromooo-monero | 2017-02-24T09:03:59+00:00
Set whichever of these you want to true: 

      bool in;
      bool out;
      bool pending;
      bool failed;
      bool pool;

pool is those to you, pending is those from you.

## gituser | 2017-02-24T18:26:32+00:00
Yes, it works, thank you.

What about 'failed' ?

## moneromooo-monero | 2017-02-24T19:18:05+00:00
failed is for failed transactions you sent (ie, you sent them, but at some point they aren't either in the txpool nor in a block)

## gituser | 2017-02-24T19:26:56+00:00
thank you.

# Action History
- Created by: gituser | 2017-02-24T06:56:22+00:00
- Closed at: 2017-02-24T19:26:56+00:00
