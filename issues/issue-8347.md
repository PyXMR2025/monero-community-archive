---
title: '"Error: Daemon response did not include the requested real outputs"'
source_url: https://github.com/monero-project/monero/issues/8347
author: ghost
assignees: []
labels: []
created_at: '2022-05-23T00:07:12+00:00'
updated_at: '2022-05-26T01:27:24+00:00'
type: issue
status: closed
closed_at: '2022-05-26T01:27:23+00:00'
---

# Original Description
Tried to send 50 tXMR. CLI wallet failed with error text below.

Result: `Error: internal error: Daemon response did not include the requested real outputs`

Monero-wallet-cli.log: https://paste.debian.net/1241707/

Note: I am copying and pasting from a VPS via nano editor, so apologies for the broken log lines. If anybody needs further info just let me know.

# Discussion History
## selsta | 2022-05-23T00:08:32+00:00
For completeness, what is your wallet version and what your daemon version?

## ghost | 2022-05-23T00:09:31+00:00
Freshly pulled from master branch. 

2022-05-22 23:40:20.319 I Monero 'Oxygen Orion' (v0.17.0.0-6e60919e6)

## moneromooo-monero | 2022-05-24T07:43:35+00:00
Are you sure your wallet is synced to the same chain as your daemon ?
If your wallet still refreshes new txes, it means it is.

## ghost | 2022-05-24T10:42:45+00:00
Absolutely. For some reason, sending a 100 tXMR worked fine, but sending a 50 tXMR gave this error. Very strange.

## ghost | 2022-05-24T10:43:17+00:00
You can see that it’s telling me I have a balance of 100 tXMR at the beginning of the log

## selsta | 2022-05-24T18:20:42+00:00
If you try to do the same tx do you get the same error?

## ghost | 2022-05-24T18:33:45+00:00
Yes.

maybe this is because these tXMR are from 2017. So some older tx version

## selsta | 2022-05-24T18:38:53+00:00
@garth-xmr can you share the seed with moneromooo on irc?

## ghost | 2022-05-24T19:03:53+00:00
Sure but the outputs have been spent. And the account was created with a spend/view key pair 

## ghost | 2022-05-24T20:33:04+00:00
Mooo showed me how to pop blocks and do this test myself so I’ll work on this in the next week

## ghost | 2022-05-26T01:27:23+00:00
Mooo and I are both unable to reproduce this issue so I'm closing it

# Action History
- Created by: ghost | 2022-05-23T00:07:12+00:00
- Closed at: 2022-05-26T01:27:23+00:00
