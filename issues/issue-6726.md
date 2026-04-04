---
title: Transaction sanity check failed with a larger amount TX
source_url: https://github.com/monero-project/monero/issues/6726
author: Lafudoci
assignees: []
labels: []
created_at: '2020-07-30T09:56:36+00:00'
updated_at: '2020-10-15T22:39:19+00:00'
type: issue
status: closed
closed_at: '2020-10-15T22:39:19+00:00'
---

# Original Description
When I was trying to move all funds from my old wallet to a new one, it showed `internal error: Transaction sanity check failed`. I've tried to delete wallet cache, recover a new wallet from 25 words and change different remote nodes. None of them worked.

But when I sent a smaller amount likes 1 XMR instead, the TX went through without any issue.

Here is the log, any idea?
https://pastebin.ubuntu.com/p/xPWvhG3vgn/

# Discussion History
## selsta | 2020-07-30T12:54:45+00:00
Can you try to do a transaction and if it fails do the following:

`unset_ring <txid>`

and then try again?

## Lafudoci | 2020-07-31T01:24:21+00:00
> Can you try to do a transaction and if it fails do the following:
> 
> `unset_ring <txid>`
> 
> and then try again?

Could you please explain more? The failed `transfer` and `sweep_all` didn't provide txid.

## moneromooo-monero | 2020-07-31T11:55:00+00:00
From the message, it's failing to even create a tx, it's the wallet failing before actually making a tx, not the daemon. xiphon added retry code, but it looks like it's failing this, which seems very very unlikely, so there is probably a bug in this code.

## Lafudoci | 2020-08-03T01:50:28+00:00
> From the message, it's failing to even create a tx, it's the wallet failing before actually making a tx, not the daemon. xiphon added retry code, but it looks like it's failing this, which seems very very unlikely, so there is probably a bug in this code.

I see. Is there a temporary workaround that I can move all my fund? Will splitting into small amount txs do the trick?

## selsta | 2020-09-13T21:34:50+00:00
Please see #6815, might be related.

## Lafudoci | 2020-09-14T02:12:31+00:00
> Please see #6815, might be related.

Yes, I finally got my XMR successfully sent. The issue was resolved by PR 6815. Thank you.

# Action History
- Created by: Lafudoci | 2020-07-30T09:56:36+00:00
- Closed at: 2020-10-15T22:39:19+00:00
