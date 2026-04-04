---
title: submit_transfer fails
source_url: https://github.com/monero-project/monero/issues/2305
author: PsychicCat
assignees: []
labels: []
created_at: '2017-08-18T03:21:19+00:00'
updated_at: '2017-08-18T11:39:41+00:00'
type: issue
status: closed
closed_at: '2017-08-18T11:39:41+00:00'
---

# Original Description
I created a tx with transfer [hot] / sign_transfer [cold] / submit_transfer [hot]. I get this log in monero-wallet-cli when I try submit_transfer.

`Error: transaction <txid> was rejected by daemon with status: Failed`

In monerod, I set_log 1 and this is all I get:
`2017-08-17 21:58:05.151 [RPC0]  WARN    daemon.rpc      src/rpc/core_rpc_server.cpp:603 [on_send_raw_tx]: tx verification failed`

Any ideas?

Update: I just realized that my hot wallet was not fully up to date on key images when I created the unsigned transfer. Could that be it? Maybe it was trying to send something that had already been spent. 

# Discussion History
## moneromooo-monero | 2017-08-18T09:06:24+00:00
in monerod: set_log 1
You'll see why it failed just before that line.

## PsychicCat | 2017-08-18T11:39:41+00:00
Indeed, now I see it. "Key image already spent in blockchain". 

# Action History
- Created by: PsychicCat | 2017-08-18T03:21:19+00:00
- Closed at: 2017-08-18T11:39:41+00:00
