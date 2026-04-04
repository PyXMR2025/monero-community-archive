---
title: 'E !r. THROW EXCEPTION: tools::error::no_connection_to_daemon'
source_url: https://github.com/monero-project/monero/issues/6169
author: NoBugBoy
assignees: []
labels: []
created_at: '2019-11-22T08:57:53+00:00'
updated_at: '2019-11-26T07:37:29+00:00'
type: issue
status: closed
closed_at: '2019-11-26T07:37:29+00:00'
---

# Original Description
For example, I use the following command to start RPC. If this exception occurs, how can I solve it.
DNS_PUBLIC=tcp://8.8.8.8 ./monero-wallet-rpc --rpc-bind-port=38089 --rpc-login=test:123456 --wallet-file=/wallet/xmr/newwallet.keys --password=bib123 --rpc-bind-ip=0.0.0.0 --confirm-external-bind，

error logs:
2019-11-22 08:49:04.759 E No message store file found: /wallet/xmr/newwallet.keys.mms
2019-11-22 08:49:04.760 E !r. THROW EXCEPTION: tools::error::no_connection_to_daemon
2019-11-22 08:49:04.760 E Wallet initialization failed: no connection to daemon

# Discussion History
## moneromooo-monero | 2019-11-22T11:50:16+00:00
Run a daemon.

If you are running one on the same machine with default settings, then it seems like a bug.

Otherwise, this is a bug tracker, not a user help forum. Please ask on Freenode in #monero, or reddit, or bitcointalk.org.

Are you running a daemon on the same machine with default settings ?

# Action History
- Created by: NoBugBoy | 2019-11-22T08:57:53+00:00
- Closed at: 2019-11-26T07:37:29+00:00
