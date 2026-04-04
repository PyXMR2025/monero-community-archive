---
title: Add parameter to wallet RPC get_transfers to fetch from all subaddresses
source_url: https://github.com/monero-project/monero/issues/5109
author: woodser
assignees: []
labels: []
created_at: '2019-01-30T17:10:00+00:00'
updated_at: '2019-03-28T19:11:23+00:00'
type: issue
status: closed
closed_at: '2019-03-28T19:11:23+00:00'
---

# Original Description
Wallet RPC `get_transfers` requires the client to specify each intended subaddress, else it defaults to subaddress 0.  Therefore, a client must call `get_address` or `get_balance` first in order to know all subaddress indices in order to fetch all transfers for an account.  An additional parameter to `get_transfers`, e.g. `allSubaddresses`:`true`, would optimize RPC interactions in this case.

Related potential RPC optimizations:

- Might we consider adding `allAccounts`:`true` to get all balances / transfers in the wallet (i.e. within all accounts and subaddresses)?
- If `used` were added to `get_balance`, `get_address` would be fully redundant saving the client another call.

# Discussion History
## moneromooo-monero | 2019-02-03T10:37:31+00:00
When you say "each intended subaddress", do you mean "each intended account" or "each intended subaddress within an account" ?

## woodser | 2019-02-04T20:12:31+00:00
I mean each intended subaddress within an account.

## moneromooo-monero | 2019-02-16T15:29:26+00:00
I tried it, and it does what you ask.

<pre>
curl -k -X POST http://127.0.0.1:$MPORT/json_rpc -d '{"jsonrpc":"2.0","id":"0","method":"getbalance","params":{"account_index":1}}' -H 'Content-Type: application/json

{
  "id": "0",
  "jsonrpc": "2.0",
  "result": {
    "balance": 5000000000000,
    "multisig_import_needed": false,
    "per_subaddress": [{
      "address": "BgjrmwQAEp4QCFKygJgR6UFSsc58BnNWPi2Ggtp2dtjtYjjL5k3ua6xfPBKegnMiuMD3sje6Q1gWXVXdpu4wqaxr3NQzmGt",
      "address_index": 2,
      "balance": 2000000000000,
      "label": "(Untitled address)",
      "num_unspent_outputs": 1,
      "unlocked_balance": 0
    },{
      "address": "BgCBzd5VExAWBADfWqMbYxU9Jtk9B7KQE9hXxMzYWWnUFNLW861W7LXKcCgTyoPNbqR8zoRbBvWJmN9PSX1Xr4uZLPMkHmz",
      "address_index": 3,
      "balance": 3000000000000,
      "label": "(Untitled address)",
      "num_unspent_outputs": 1,
      "unlocked_balance": 0
    }],
    "unlocked_balance": 0
  }
}
</pre>

## woodser | 2019-02-17T01:05:23+00:00
It turns out `get_transfers` does return transfers for all subaddresses if not specified and the RPC documentation is incorrect.

#5150 adds `all_accounts` as a field to `get_balances`.  Could the same field be added and integrated into `get_transfers`, thereby allowing clients to fetch transfers for all accounts in a single call?


# Action History
- Created by: woodser | 2019-01-30T17:10:00+00:00
- Closed at: 2019-03-28T19:11:23+00:00
