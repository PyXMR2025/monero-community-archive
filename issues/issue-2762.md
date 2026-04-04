---
title: Block found, coin missing?
source_url: https://github.com/monero-project/monero/issues/2762
author: thawwed
assignees: []
labels: []
created_at: '2017-11-05T19:49:17+00:00'
updated_at: '2017-11-06T11:04:19+00:00'
type: issue
status: closed
closed_at: '2017-11-05T23:57:54+00:00'
---

# Original Description
Block found, transaction shows payment sent to pool wallet, but pool wallet not received anything?

Is something wrong with my wallet-rpc?

# Discussion History
## moneromooo-monero | 2017-11-05T23:40:17+00:00
Please report the output of "status" in monerod.

## thawwed | 2017-11-05T23:42:07+00:00
`
Height: 12006/12006 (100.0%) on mainnet, not mining, net hash 135.61 MH/s, v1, up to date, 8(out)+23(in) connections, uptime 0d 1h 29m 32s
`

## moneromooo-monero | 2017-11-05T23:55:14+00:00
Is this a monero alt ? Because that doesn't make sense otherwise.

## fluffypony | 2017-11-05T23:57:54+00:00
Yes, it's Electroneum or Sumokoin or something. STOP OPENING ISSUES ON THE MONERO REPOSITORY!!

## moneromooo-monero | 2017-11-05T23:59:41+00:00
That explains why stuff that built for me did not for you. Thanks for wasting my time building stuff earlier :/ If you make changes, mention it first....

## thawwed | 2017-11-06T00:02:17+00:00
Electroneum is built off of this, and this issue stems from this. The same error occurs when I use it for straightup Monero. 

The issue is blocks are being found but something is not communicating right for it to actually credit to a wallet.

## moneromooo-monero | 2017-11-06T00:02:44+00:00
And if you're using a low height chain, this is probably one bug that got a fix which got merged recently, update to recent code.

## thawwed | 2017-11-06T00:02:50+00:00
And I didn't make changes. If you click through the links Electroneum is just another commit of this.

## fluffypony | 2017-11-06T00:07:08+00:00
@Thawwed no, Electroneum is a fork *with merged changes* to the codebase.

## thawwed | 2017-11-06T00:08:07+00:00
That's fine. I opened up a new issue. We can talk about the SAME EXACT issue because it happens with my Monero pool too.

## thawwed | 2017-11-06T00:08:21+00:00
Setup was the exact same.

## quangvu3 | 2017-11-06T11:04:19+00:00
Our blockchain is very stable and never missed a single coin. Please don't mention Sumokoin as we've never asked any silly question for help here

# Action History
- Created by: thawwed | 2017-11-05T19:49:17+00:00
- Closed at: 2017-11-05T23:57:54+00:00
