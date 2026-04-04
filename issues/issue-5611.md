---
title: '[DOCS] please fix `get_transfer_by_txid` description'
source_url: https://github.com/monero-project/monero/issues/5611
author: nikitasius
assignees: []
labels: []
created_at: '2019-06-07T14:30:27+00:00'
updated_at: '2022-07-21T02:27:35+00:00'
type: issue
status: closed
closed_at: '2022-07-21T02:27:35+00:00'
---

# Original Description
Actual docs (`https://www.getmonero.org/resources/developer-guides/wallet-rpc.html#get_transfer_by_txid`) tells us what `get_transfer_by_txid` return only  `transfer` object, and did not mention what it return a `transfers` array too.


## example (testnet):
* `curl -X POST http://localhost:18082/json_rpc -d '{"jsonrpc":"2.0","id":"0","method":"get_transfer_by_txid","params":{"txid":"a5447204b8a2739ff7131fa7e394c3dbeed4da0a5e46182c2bcce01ca6d41d4b"}}' -H 'Content-Type: application/json'`

```json
{
  "id": "0",
  "jsonrpc": "2.0",
  "result": {
    "transfer": {
      "address": "BdzT4Bv59vYZU3jP6LdqjcWFQyF7rFERCB9NhVJd5tL3LRgMHdJbznS4LzAB5ZsQp2aC5UcMbRztVQtPphQNs57A44YngGF",
      "amount": 1000000000000,
      "confirmations": 690,
      "double_spend_seen": false,
      "fee": 194710000,
      "height": 1228011,
      "note": "",
      "payment_id": "0000000000000000",
      "subaddr_index": {
        "major": 0,
        "minor": 6
      },
      "suggested_confirmations_threshold": 1,
      "timestamp": 1559840965,
      "txid": "a5447204b8a2739ff7131fa7e394c3dbeed4da0a5e46182c2bcce01ca6d41d4b",
      "type": "in",
      "unlock_time": 0
    },
    "transfers": [{
      "address": "BdzT4Bv59vYZU3jP6LdqjcWFQyF7rFERCB9NhVJd5tL3LRgMHdJbznS4LzAB5ZsQp2aC5UcMbRztVQtPphQNs57A44YngGF",
      "amount": 1000000000000,
      "confirmations": 690,
      "double_spend_seen": false,
      "fee": 194710000,
      "height": 1228011,
      "note": "",
      "payment_id": "0000000000000000",
      "subaddr_index": {
        "major": 0,
        "minor": 6
      },
      "suggested_confirmations_threshold": 1,
      "timestamp": 1559840965,
      "txid": "a5447204b8a2739ff7131fa7e394c3dbeed4da0a5e46182c2bcce01ca6d41d4b",
      "type": "in",
      "unlock_time": 0
    },{
      "address": "BZhpmry7X4uRCWGJUEnRHYFa61BXizjnNBaFYbZ3tNFCDxYZRv95cHh1igoBwH7VLjMinSNC1WpHycESKhXpMTvbT2EnC9s",
      "amount": 4000000000000,
      "confirmations": 690,
      "double_spend_seen": false,
      "fee": 194710000,
      "height": 1228011,
      "note": "",
      "payment_id": "0000000000000000",
      "subaddr_index": {
        "major": 0,
        "minor": 9
      },
      "suggested_confirmations_threshold": 1,
      "timestamp": 1559840965,
      "txid": "a5447204b8a2739ff7131fa7e394c3dbeed4da0a5e46182c2bcce01ca6d41d4b",
      "type": "in",
      "unlock_time": 0
    },{
      "address": "BZ4dMbKwGoAWhQRPXNnqb5caQJpEGRCQMiGynZZAm26V7mjxvvf7qQzb34z3Gq2AgG9yZ5DfbPddWaVXJHmb9B31UH3AhBF",
      "amount": 3000000000000,
      "confirmations": 690,
      "double_spend_seen": false,
      "fee": 194710000,
      "height": 1228011,
      "note": "",
      "payment_id": "0000000000000000",
      "subaddr_index": {
        "major": 0,
        "minor": 8
      },
      "suggested_confirmations_threshold": 1,
      "timestamp": 1559840965,
      "txid": "a5447204b8a2739ff7131fa7e394c3dbeed4da0a5e46182c2bcce01ca6d41d4b",
      "type": "in",
      "unlock_time": 0
    },{
      "address": "Bferk7GhYxwY2KYBaT2PqkFTBFXr72fCZ53ReLTBZtHLVit4c7gWjooi6peBfaygPrLJnLUyDUZuv3aYAo1VEmaW4Qb6Wuc",
      "amount": 2000000000000,
      "confirmations": 690,
      "double_spend_seen": false,
      "fee": 194710000,
      "height": 1228011,
      "note": "",
      "payment_id": "0000000000000000",
      "subaddr_index": {
        "major": 0,
        "minor": 7
      },
      "suggested_confirmations_threshold": 1,
      "timestamp": 1559840965,
      "txid": "a5447204b8a2739ff7131fa7e394c3dbeed4da0a5e46182c2bcce01ca6d41d4b",
      "type": "in",
      "unlock_time": 0
    }]
  }
}
```

please fix your docs to avoid confusing developers :smiley: 

# Discussion History
## erciccione | 2019-06-07T15:06:40+00:00
Thanks for the report @nikitasius . Please open another issue on the repo of the website, where the documentation is hosted: https://repo.getmonero.org/monero-project/monero-site

## tmoravec | 2019-10-16T13:51:54+00:00
Actually, the documentation diverges from the actual output in multiple ways. In particular, according to the documentation, the output should include `destinations` field. This field is vital, but it is missing from the actual output so it's worth fixing the code, rather than the documentation.

That being said, the approach the code takes (array `transfers`) makes much more sense than a single object. So it makes sense to update the documentation in this case.

EDIT: Created a new issue for the missing `destinations` field: https://github.com/monero-project/monero/issues/5992

## selsta | 2022-07-21T02:27:35+00:00
https://github.com/monero-project/monero-site/pull/2004

# Action History
- Created by: nikitasius | 2019-06-07T14:30:27+00:00
- Closed at: 2022-07-21T02:27:35+00:00
