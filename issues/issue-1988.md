---
title: get_transfers in 0.10.3.1 is not showing out address anymore
source_url: https://github.com/monero-project/monero/issues/1988
author: gituser
assignees: []
labels:
- invalid
created_at: '2017-04-17T09:52:46+00:00'
updated_at: '2017-09-02T14:56:40+00:00'
type: issue
status: closed
closed_at: '2017-09-02T12:48:19+00:00'
---

# Original Description
Hi.

After upgrading from 0.10.1 it seems that get_transfers call has been changed and it's no longer showing for outgoing transactions destination address.

Is it an intended change or is it just a bug?

I find it very annoying not to be able to track down where particular payment has been sent to.
Thanks.

# Discussion History
## gituser | 2017-04-17T10:14:59+00:00
e.g. (in `0.10.1` was):

```
"out": [{
      "amount": 6996000000000,
      "fee": 33738023280,
      "height": 835329,
      "note": "",
      "payment_id": "0000000000000000",
      "timestamp": 1485364270,
      "txid": "xxx2"
    },{
      "amount": 1008683510000,
      "fee": 35359956047,
      "height": 810690,
      "note": "",
      "payment_id": "0000000000000000",
      "timestamp": 1482345760,
      "txid": "xxx1"
    },{
      "amount": 100000000000,
      "destinations": [{
        "address": "monero_address",
        "amount": 100000000000
      }],

```

in new version (`0.10.3.1`):
```
{
      "amount": 6996000000000,
      "fee": 33737958930,
      "height": 835330,
      "note": "",
      "payment_id": "0000000000000000",
      "timestamp": 1485364532,
      "txid": "xxxxxxx",
      "type": "out"
    }
```

## gituser | 2017-04-20T12:51:08+00:00
any update on this?

## moneromooo-monero | 2017-04-22T10:59:16+00:00
I have just checked that it works. The wallet cache was probably destroyed and recreated from the blockchain, from which this data cannot be recovered (because it's not there).
Please make a new tx, and check whether addresses/amounts appear for that one.

## moneromooo-monero | 2017-07-24T12:31:41+00:00
ping

## moneromooo-monero | 2017-09-02T12:42:12+00:00
Since it works for me, I'll close this. Please reopen if it does not work, and is not due to the cache being missing or corrupt in some way (or the wallet being rescanned).

+invalid

## gituser | 2017-09-02T14:56:40+00:00
Hi. there is another issue I've encountered lately with the latest `0.10.3.1` under load (if there is a lot of disk i/o operations) and if there was transaction sent like a minute ago or so wallet isn't saved momentally and if you restart the monero-rpc-daemon transaction isn't in the wallet anymore.

It's reproduceable - you need to load your system with a lot of disk i/o activitity and try to send some monero transaction and then after it gets mined restart the daemon.

# Action History
- Created by: gituser | 2017-04-17T09:52:46+00:00
- Closed at: 2017-09-02T12:48:19+00:00
