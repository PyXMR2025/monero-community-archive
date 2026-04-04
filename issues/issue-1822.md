---
title: monero-wallet-rpc not showing all pool transactions with same integrated address
source_url: https://github.com/monero-project/monero/issues/1822
author: amiuhle
assignees: []
labels: []
created_at: '2017-02-28T20:26:17+00:00'
updated_at: '2017-03-29T17:44:45+00:00'
type: issue
status: closed
closed_at: '2017-03-29T17:44:45+00:00'
---

# Original Description
So I just played around on testnet to test some code, and sent two transactions to the same integrated address:

```
[wallet 9tQPcn]: transfer A3Brqw9sVmwLyWS8EWeUw1VqpqfwnDHTkG7Pb4NJ3RmZWeeMZhGMe2ZXz4bSk7BbtEYF5981nLxkDYQ6B46tX5DMVr558acmbUeFMDhA1s 0.5
Wallet password: *********
Sending 0.500000000000.  The transaction fee is 0.034859504078
Is this okay?  (Y/Yes/N/No): y
Money successfully sent, transaction <54461c4dc96d56a69299859b642367f6351f7231487f75eb41ed4bc5504a75c3>
[wallet 9tQPcn]: transfer A3Brqw9sVmwLyWS8EWeUw1VqpqfwnDHTkG7Pb4NJ3RmZWeeMZhGMe2ZXz4bSk7BbtEYF5981nLxkDYQ6B46tX5DMVr558acmbUeFMDhA1s 0.5
Wallet password: *********
Sending 0.500000000000.  The transaction fee is 0.034859504078
Is this okay?  (Y/Yes/N/No): y
Money successfully sent, transaction <da7301d5423efa09fabacb720002e978d114ff2db6a1546f8b820644a1b96208>
```

Here's what I get from `monero-wallet-rpc` a couple of seconds later:

```json
curl -X POST http://207.154.197.71:28082/json_rpc -d '{"jsonrpc":"2.0","id":"0","method":"get_transfers", "params": { "pool": true }}' -H 'Content-Type: application/json'
{
  "id": "0",
  "jsonrpc": "2.0",
  "result": {
    "pool": [{
      "amount": 500000000000,
      "fee": 0,
      "height": 0,
      "note": "",
      "payment_id": "758d9b225fda7b7f",
      "timestamp": 1488312467,
      "txid": "da7301d5423efa09fabacb720002e978d114ff2db6a1546f8b820644a1b96208",
      "type": "pool"
    }]
  }
}                                                   
```

*Edit: GitHub file upload seems to be broken right now. If a screenshot of a testnet explorer is needed, I can upload one somewhere else.*

# Discussion History
## moneromooo-monero | 2017-03-25T16:50:57+00:00
Can you confirm this is now fixed ?

## amiuhle | 2017-03-29T17:44:45+00:00
Yes, fixed!

# Action History
- Created by: amiuhle | 2017-02-28T20:26:17+00:00
- Closed at: 2017-03-29T17:44:45+00:00
