---
title: get_payments Wallet RPC call allows for incorrect payment ID lengths
source_url: https://github.com/monero-project/monero/issues/860
author: sheepman0
assignees: []
labels: []
created_at: '2016-06-08T12:39:09+00:00'
updated_at: '2016-07-07T19:55:58+00:00'
type: issue
status: closed
closed_at: '2016-07-07T19:55:58+00:00'
---

# Original Description
Just discovered the get_payments call allows for a payment ID of 15/16/63/64 characters when presumably it should only allow 16/64 character payments ID's.


# Discussion History
## moneroexamples | 2016-06-08T21:56:11+00:00
dont they get paded to required length?


## sheepman0 | 2016-06-09T08:49:03+00:00
Surely if they did I should be able to use something other then just one character less then expected? For example a payment ID of 14 characters or less errors, it doesn't get padded.


## moneromooo-monero | 2016-06-09T19:41:19+00:00
https://github.com/monero-project/bitmonero/pull/862


## fluffypony | 2016-07-07T19:55:58+00:00
Fixed


# Action History
- Created by: sheepman0 | 2016-06-08T12:39:09+00:00
- Closed at: 2016-07-07T19:55:58+00:00
