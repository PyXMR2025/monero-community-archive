---
title: Calling RPC `open_wallet` toggles whether or not `get_transfers` returns pending
  transfers
source_url: https://github.com/monero-project/monero/issues/5106
author: woodser
assignees: []
labels: []
created_at: '2019-01-29T18:34:28+00:00'
updated_at: '2019-04-16T22:33:33+00:00'
type: issue
status: closed
closed_at: '2019-04-16T22:33:33+00:00'
---

# Original Description
Each call to `open_wallet` seems to toggle whether or not `get_transfers` returns pending transfers.

To reproduce this bug:

1. Have a wallet open and running in a RPC instance
2. Confirm that pending transfers are returned from RPC `get_transfers`
3. Invoke RPC `open_wallet` on the same wallet
2. Pending transfers are no longer returned from RPC `get_transfers`
5. Invoke RPC `open_wallet` on the same wallet
6. Pending transfers are returned again.  Repeat from step 3.

Env: Mac OSX and the latest code merged into master.

Edit: In case it matters, I was only testing with a single pending transfer and it had a payment id.  If it was filtered out for some reason, no `pending` field would be returned from `get_transfers` which is consistent with what I see.

# Discussion History
## woodser | 2019-02-02T12:43:10+00:00
This issue seems to affect the wallet's reporting of available balance when funds are locked, as well.

## moneromooo-monero | 2019-02-02T16:16:48+00:00
Works for me, with a tx with a payment id, and one without.


## moneromooo-monero | 2019-03-21T18:20:00+00:00
Would this be because you did not refresh ?

## moneromooo-monero | 2019-04-12T11:32:25+00:00
<pre>
$ utils/python-rpc/console 18081 8888
Variable 'daemon' connected to daemon RPC on 127.0.0.1:18081
Variable 'wallet' connected to wallet RPC on 127.0.0.1:8888
>>> wallet.open_wallet('w1')
{}
>>> wallet.get_transfers(pending=True,out=False,in_=False)
{u'pool': [{u'payment_id': u'8c138c5fdb3ffef7', u'fee': 5144000000000, u'double_spend_seen': False, u'subaddr_index': {u'major': 0, u'minor': 0}, u'timestamp': 1555068691, u'subaddr_indices': [{u'major': 0, u'minor': 0}], u'unlock_time': 0, u'height': 0, u'note': u'', u'amount': 65205044859805, u'suggested_confirmations_threshold': 0, u'confirmations': 0, u'address': u'44Kbx4sJ7JDRDV5aAhLJzQCjDz2ViLRduE3ijDZu3osWKBjMGkV1XPk4pfDUMqt1Aiezvephdqm6YD19GKFD9ZcXVUTp6BW', u'txid': u'f7da9c7a4fea1e16c00ca5b63c627ae50778e5b6785d0b72fd83d320aa6603b2', u'type': u'pool'}]}
>>> wallet.open_wallet('w1')
{}
>>> wallet.get_transfers(pending=True,out=False,in_=False)
{u'pending': [{u'payment_id': u'0000000000000000', u'fee': 5144000000000, u'double_spend_seen': False, u'subaddr_index': {u'major': 0, u'minor': 0}, u'timestamp': 1555068537, u'subaddr_indices': [{u'major': 0, u'minor': 0}], u'unlock_time': 0, u'height': 0, u'note': u'', u'amount': 1515151515, u'suggested_confirmations_threshold': 0, u'confirmations': 0, u'address': u'44Kbx4sJ7JDRDV5aAhLJzQCjDz2ViLRduE3ijDZu3osWKBjMGkV1XPk4pfDUMqt1Aiezvephdqm6YD19GKFD9ZcXVUTp6BW', u'txid': u'f7da9c7a4fea1e16c00ca5b63c627ae50778e5b6785d0b72fd83d320aa6603b2', u'type': u'pending'}]}
>>> wallet.open_wallet('w1')
{}
>>> wallet.get_transfers(pending=True,out=False,in_=False)
{u'pool': [{u'payment_id': u'8c138c5fdb3ffef7', u'fee': 5144000000000, u'double_spend_seen': False, u'subaddr_index': {u'major': 0, u'minor': 0}, u'timestamp': 1555068691, u'subaddr_indices': [{u'major': 0, u'minor': 0}], u'unlock_time': 0, u'height': 0, u'note': u'', u'amount': 65205044859805, u'suggested_confirmations_threshold': 0, u'confirmations': 0, u'address': u'44Kbx4sJ7JDRDV5aAhLJzQCjDz2ViLRduE3ijDZu3osWKBjMGkV1XPk4pfDUMqt1Aiezvephdqm6YD19GKFD9ZcXVUTp6BW', u'txid': u'f7da9c7a4fea1e16c00ca5b63c627ae50778e5b6785d0b72fd83d320aa6603b2', u'type': u'pool'}]}
>>> 
</pre>

## moneromooo-monero | 2019-04-12T11:33:03+00:00
Looks like it ping pings between pool and pending.

## moneromooo-monero | 2019-04-12T13:14:36+00:00
I think I see what's going on.
When loading a wallet, the previous wallet is now saved after loading succeeds, because people usually intended to save their wallet, but did not.
So what happens when loading the same wallet again is:
<pre>
        DISK    MEMORY
        0
LOAD    0       0
TX      0       1
LOAD    0       0
SAVEP   1       0
LOAD    1       1
SAVEP   0       1
LOAD    0       0
SAVEP   1       0
</pre>
SAVEP is "save previous" here. So we get a ping pong effect.
I think the right thing to do is to save first, then load.

## moneromooo-monero | 2019-04-12T13:41:49+00:00
https://github.com/monero-project/monero/pull/5429

## moneromooo-monero | 2019-04-16T22:13:42+00:00
+resolved

# Action History
- Created by: woodser | 2019-01-29T18:34:28+00:00
- Closed at: 2019-04-16T22:33:33+00:00
