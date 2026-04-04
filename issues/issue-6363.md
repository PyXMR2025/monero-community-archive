---
title: there is no destinations array in tx info
source_url: https://github.com/monero-project/monero/issues/6363
author: past2017
assignees: []
labels: []
created_at: '2020-02-29T04:21:25+00:00'
updated_at: '2022-04-10T18:48:48+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
After make a transfer tx, i found the tx info is different from the previous tx,i make about 30 txs only 1 tx has problem 
**questionable tx info，in this tx info there is no destinations array which is exist in right tx info**
```
# curl http://127.0.0.1:$port/json_rpc -d '{"jsonrpc":"2.0","id":"0","method":"get_transfer_by_txid","params":{"txid":"17e004db19197ac72d1522613567f1a557ff5e2aff9c05863893a1c3703787c0"}' -H 'Content-Type: application/json'
{
  "id": "0",
  "jsonrpc": "2.0",
  "result": {
    "transfer": {
      "address": "45nRCwkKRfJP1Mumn9neNydSRpv9xgjiWjC81v4efRvVabFMi67D7PPj6tAUc6cvSDJTwmEmXHQ6fR1LXauwam5tGGTZ3FH",
      "amount": 36186000000000,
      "confirmations": 8969,
      "double_spend_seen": false,
      "fee": 22540000,
      "height": 2034986,
      "locked": false,
      "note": "",
      "payment_id": "0000000000000000",
      "subaddr_index": {
        "major": 0,
        "minor": 0
      },
      "subaddr_indices": [{
        "major": 0,
        "minor": 0
      }],
      "suggested_confirmations_threshold": 20,
      "timestamp": 1581871294,
      "txid": "17e004db19197ac72d1522613567f1a557ff5e2aff9c05863893a1c3703787c0",
      "type": "out",
      "unlock_time": 0
    },
```
**previous right tx info**
```
{
  "id": "0",
  "jsonrpc": "2.0",
  "result": {
    "transfer": {
      "address": "45nRCwkKRfJP1Mumn9neNydSRpv9xgjiWjC81v4efRvVabFMi67D7PPj6tAUc6cvSDJTwmEmXHQ6fR1LXauwam5tGGTZ3FH",
      "amount": 999990000000000,
      "confirmations": 8807,
      "destinations": [{
        "address": "834Tqrx6LkVacQBkD5EviWQgDsnvLwnvQ4SteVytL5dQAqmpumvr2ZHFaW4JPpzpZUXu4uJQweyDAcdpubCpkZQG3ATx5up",
        "amount": 999990000000000
      }],
      "double_spend_seen": false,
      "fee": 112810000,
      "height": 2035150,
      "locked": false,
      "note": "",
      "payment_id": "0000000000000000",
      "subaddr_index": {
        "major": 0,
        "minor": 0
      },
      "subaddr_indices": [{
        "major": 0,
        "minor": 0
      }],
      "suggested_confirmations_threshold": 533,
      "timestamp": 1581892226,
      "txid": "680c823880378661a80017aa8a96958e24903cad5b0e1ac1563a9e246dee270e",
      "type": "out",
      "unlock_time": 0
    },

```


# Discussion History
## moneromooo-monero | 2020-03-01T01:54:49+00:00
Did you restore the wallet, or forget to save the cache after sending that tx, or the wallet crashed ? If so, it's expected it would not have the data. If not, then it might be a bug.

## past2017 | 2020-03-01T02:08:05+00:00
> Did you restore the wallet, or forget to save the cache after sending that tx, or the wallet crashed ? If so, it's expected it would not have the data. If not, then it might be a bug.

I do nothing for this wallet, the tx before this questionable one and the tx after this questionable one are handled correctly, only this tx is shown incorrectly
so please let me know how to handle it? this is a withdraw tx from an exchange,normally i check the destinations array,but for this tx there is no destinations array, so i do not know should i marked it as a successful one or a failed one?is there another way to confirm if it is a successful tx have transfered to the destination address.
thanks for your reply


## moneromooo-monero | 2020-03-02T13:35:39+00:00
It's got:
      "height": 2034986,

So it's on the chain.

Anything different about how that tx was made compared to the other ones ?

## past2017 | 2020-03-03T01:20:50+00:00
> It's got:
> "height": 2034986,
> 
> So it's on the chain.
> 
> Anything different about how that tx was made compared to the other ones ?

it is completely same between those tx which we send by a java program

## selsta | 2022-04-10T18:48:48+00:00
Is this still an issue?

# Action History
- Created by: past2017 | 2020-02-29T04:21:25+00:00
