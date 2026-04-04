---
title: '[RPC] "double_spend" error when using transfer followed by sendrawtransaction'
source_url: https://github.com/monero-project/monero/issues/2585
author: gpip
assignees: []
labels: []
created_at: '2017-10-06T01:14:07+00:00'
updated_at: '2018-06-20T08:36:31+00:00'
type: issue
status: closed
closed_at: '2017-12-02T09:40:24+00:00'
---

# Original Description
Using `transfer` with `do_not_relay` set to true followed by `sendrawtransaction` with `do_not_relay` set to false causes the wallet to reject all but the first transaction with a "double_spend" error until the first tx gets mined. Is there some way to update the wallet state when using the rpc alone?

Sample code:

```python
import os

import requests
from requests.auth import HTTPDigestAuth

USER = os.getenv('RPC_USER', 'monero')
PWD = os.getenv('RPC_PASSWORD', 'pwd1')
AUTH = HTTPDigestAuth(USER, PWD)

CFG = {
    'host': 'localhost',
    'port': os.getenv('RPC_PORT', 28082),
    'daemon_port': os.getenv('DAEMON_PORT', 28081)
}
RPC_URI = 'http://%(host)s:%(port)s/json_rpc' % CFG
DAEMON_URI = 'http://%(host)s:%(daemon_port)s' % CFG

def transfer_preview(recipients):
    params = {
        'destinations': recipients,
        'do_not_relay': True,
        'get_tx_hex': True,
        'get_tx_key': True
    }
    data = {
        'method': 'transfer',
        'params': params
    }
    resp = requests.post(RPC_URI, json=data, auth=AUTH)
    return resp.json()

def broadcast(raw):
    params = {
        'tx_as_hex': raw,
        'do_not_relay': False
    }
    resp = requests.post('%s/sendrawtransaction' % DAEMON_URI, json=params)
    return resp.json()

def try2():
    for _ in range(2):
        tp1 = transfer_preview([{
            'amount': int(0.1 * 1e12),
            'address': '9uUr8urCW73Hf1S2PxDkmKBk8wRujbSNuVgusyUDGv5seSjbKwDATafCXAmbWd8cWHghhzF2J4hpGLXEkUkxHCT35A4VaU3'
        }])['result']
        blob = str(tp1['tx_blob'])
        print tp1['tx_hash'], tp1['fee'], tp1['tx_key'], len(blob)
        print broadcast(blob)
        print

if __name__ == "__main__":
    try2()
```

# Discussion History
## moneromooo-monero | 2017-11-11T10:15:17+00:00
https://github.com/monero-project/monero/pull/2788 should do it.,

include "get_tx_metadata: true" on the transfer RPC.
Then, call the new "relay_tx" RPC. "hex" must be set to the concatenation of the tx hex and metadata hex from the transfer call if the appended flag was true. Otherwise, just the metadata hex is enough.


## gpip | 2017-11-17T12:49:42+00:00
Thank you! haven't had time to try it yet, but is there some place that talks about next planned releases and whether this change would be part of it?

## moneromooo-monero | 2017-11-17T17:54:56+00:00
Maybe #monero-dev from time to time, and this will be in next release (unless next release is an emergency patch).

## moneromooo-monero | 2017-12-02T09:13:35+00:00
+resolved

## danuker | 2018-06-20T07:30:54+00:00
I finally got the chance to try this. It seems you don't need `get_tx_metadata` nor `relay_tx` nor to concatenate anything.

The example from @gpip works now, I didn't even need `get_tx_key` on the `transfer`.

# Action History
- Created by: gpip | 2017-10-06T01:14:07+00:00
- Closed at: 2017-12-02T09:40:24+00:00
