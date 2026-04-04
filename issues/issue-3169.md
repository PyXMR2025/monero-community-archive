---
title: 'Error: Transaction Was not Constructed'
source_url: https://github.com/monero-project/monero/issues/3169
author: xmr-karnal
assignees: []
labels: []
created_at: '2018-01-21T15:42:04+00:00'
updated_at: '2024-03-23T19:35:19+00:00'
type: issue
status: closed
closed_at: '2018-01-23T14:40:15+00:00'
---

# Original Description
Ran into the following problem earlier today:

I have a wallet with several accounts, and attempted to convert some XMR to BTC using xmr.to, using the primary address of one of the subaccounts.

[Here](https://dpaste.de/2DqS/raw) is the result.

On a [reddit thread](https://www.reddit.com/r/Monero/comments/7rxsq6/error_transaction_was_not_constructed/) I started to try to get help about this, it was suggested that this might be due to using subaddresses.

To be clear, this transfer was from an account's primary address (but not the primary account, so, the address begins with **8**) to (presumably) an integrated address - just the standard stuff that xmr.to generates.

I also tried from a couple of other accounts (same wallet) with even more XMR available, but it did not make any difference.


Is this a bug? As far as I understand it, it should be possible in theory to send XMR from any sort of valid XMR address to any other sort of XMR address.

# Discussion History
## xmr-karnal | 2018-01-21T15:44:15+00:00
It is also worth noting that the *transfer* command used was simply copy-pasted from xmr.to after initiating the order, as has been done in the past.

The big difference is that this is the first time I'm attempting to use anything other than an address beginning with **4** with xmr.to.

## moneromooo-monero | 2018-01-21T15:47:46+00:00
You're using an old version (including 0.11.1.0), right ?
Unless this is a new bug, this was fixed a few months back.

## xmr-karnal | 2018-01-21T15:52:27+00:00
I'm on v0.11.0.0-e1395ac, baked locally to get on the multisig train some time (2 months, more or less) ago.

If you think that's it, I'll be glad to recompile with more up-to-date sources.

## stoffu | 2018-01-22T01:28:28+00:00
It's a bug which is fixed in #3171.

Thank you for reporting!

## xmr-karnal | 2018-01-22T16:09:29+00:00
This indeed does seem to fix it.

Amazing!

## stoffu | 2018-01-23T23:33:13+00:00
FWIW you didn’t need to close this issue before that PR gets merged, because other people may run into the same bug and find this thread.

# Action History
- Created by: xmr-karnal | 2018-01-21T15:42:04+00:00
- Closed at: 2018-01-23T14:40:15+00:00
