---
title: get_transfer_by_txid RPC method returns single transfer when multiple are present
source_url: https://github.com/monero-project/monero/issues/3206
author: emesik
assignees: []
labels: []
created_at: '2018-01-30T09:44:48+00:00'
updated_at: '2018-02-18T19:24:34+00:00'
type: issue
status: closed
closed_at: '2018-02-18T19:24:34+00:00'
---

# Original Description
This method takes transaction id and returns only a single payment entry, while a transaction may contain multiple payments to the wallet.

An example, sending transfer from account 0 to addresses belonging to account 1 and 2 of the same wallet (5 XMR in total):

```
[wallet 9wFuzN]: transfer BZwH58czrBpUMm6bFDuh1tjchGmDoAKJBEYhsbndjjcJNRxJxA9TVPpaNiwZkMK36Z1zLLN3st4YqRvARjmNEUMFHxLGcNw 2 BhphVgXmDcDYj8KDpUXGYm7V9NVYEAMEWaG6qLQhTFU4haPt4PFyFL18gTeYSCoDxND45Ggj45EywQF6eZ3B5BCr7jmJuYR 3
```

After mining the block:

```
DEBUG:monero.backends.jsonrpc:Method: get_transfer_by_txid
Params:
{'txid': 'e9527b556c78f5dc206a67fc17cdc602577f1f2cf1834eb9dd680cc8b70a6d23'}
DEBUG:urllib3.connectionpool:Starting new HTTP connection (1): 127.0.0.1
DEBUG:urllib3.connectionpool:http://127.0.0.1:28088 "POST /json_rpc HTTP/1.1" 200 616
DEBUG:monero.backends.jsonrpc:Result:
{'id': 0,
 'jsonrpc': '2.0',
 'result': {'transfer': {'address': 'BhphVgXmDcDYj8KDpUXGYm7V9NVYEAMEWaG6qLQhTFU4haPt4PFyFL18gTeYSCoDxND45Ggj45EywQF6eZ3B5BCr7jmJuYR',
                         'amount': 3000000000000,
                         'double_spend_seen': False,
                         'fee': 1281760000,
                         'height': 1088210,
                         'note': '',
                         'payment_id': '0000000000000000',
                         'subaddr_index': {'major': 2, 'minor': 0},
                         'timestamp': 1517304860,
                         'txid': 'e9527b556c78f5dc206a67fc17cdc602577f1f2cf1834eb9dd680cc8b70a6d23',
                         'type': 'in',
                         'unlock_time': 0}}}
```

While there are 3 payments for this transaction ID (1 outgoing, 2 incoming), only one is returned.

There's no good way to fix it without breaking backward compatibility, although I wonder if we should care. Using this method is asking for problems.

Perhaps we could add a new method called `get_transfers_by_txid` which returns all payments, incoming and outgoing, in a list. To be consistent with the rest, it would take an account index as a parameter and work only within that context.

Meanwhile `get_transfer_by_txid` would remain for one release more, but marked as deprecated and potentially dangerous in the docs.

# Discussion History
## stoffu | 2018-01-30T11:14:05+00:00
#3207 

## moneromooo-monero | 2018-02-18T19:20:33+00:00
+resolved

# Action History
- Created by: emesik | 2018-01-30T09:44:48+00:00
- Closed at: 2018-02-18T19:24:34+00:00
