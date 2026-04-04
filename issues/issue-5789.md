---
title: 'monero-wallet-rpc: transactions are not sorted in the output'
source_url: https://github.com/monero-project/monero/issues/5789
author: reardenlife
assignees: []
labels: []
created_at: '2019-08-02T13:10:22+00:00'
updated_at: '2019-08-05T00:55:00+00:00'
type: issue
status: closed
closed_at: '2019-08-05T00:54:32+00:00'
---

# Original Description
Bug?

I noticed that the output of a method get_transfers is not sorted (using monero-wallet-rpc v0.14.0.2).
I am writing a billing and here is a code on bash that I used to get 10 last input transactions:

```bash
  o=$(curl -X POST http://127.0.0.1:18082/json_rpc -d '{"jsonrpc":"2.0","id":"0","method":"get_transfers","params":{"in":true,"account_index":0}}' -H 'Content-Type: application/json')
set -e
  for (( j=1; j<=10; j++)); do
    txid=$(echo "$o" | jq -r ".result.in[-$j].txid")
    amount=$(echo "$o" | jq -r ".result.in[-$j].amount")
```
For some reason, the very last transaction had an index 0, not -1.  So they dont appear to be sorted.
I solved my issue with jq:
```bash
  o=$(curl -X POST http://127.0.0.1:18082/json_rpc -d '{"jsonrpc":"2.0","id":"0","method":"get_transfers","params":{"in":true,"account_index":0}}' -H 'Content-Type: application/json' | jq '.result.in|=sort_by(.timestamp)')
set -e
  for (( j=1; j<=10; j++)); do
    txid=$(echo "$o" | jq -r ".result.in[-$j].txid")
    amount=$(echo "$o" | jq -r ".result.in[-$j].amount")
```
But it would be helpful to clarify things out - at least to specify in the documentation that output is not sorted.

# Discussion History
## reardenlife | 2019-08-02T13:30:23+00:00
Just checked on monero-wallet-rpc v0.14.1.2.  Same thing.

## jtgrassie | 2019-08-04T15:37:08+00:00
Results from the RPC are ordered for me. height/timestamp ascending. You sure your bash script is correct? Have you manually checked the output from the RPC call?

## reardenlife | 2019-08-04T17:01:11+00:00
@jtgrassie

> "Have you manually checked the output from the RPC call?"

Yes, I did.

> "Results from the RPC are ordered for me. 
height/timestamp ascending "

Don't be too hopeful. :)

```bash
monero-v0.14.1.2]# curl -X POST http://127.0.0.1:18082/json_rpc -d '{"jsonrpc":"2.0","id":"0","method":"get_transfers","params":{"in":true,"account_index":0}}' -H 'Content-Type: application/json' | grep timestamp | head
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0
      "timestamp": 1564867237,
      "timestamp": 1564855628,
      "timestamp": 1564857514,
      "timestamp": 1564846946,
      "timestamp": 1564842363,
      "timestamp": 1564843141,
      "timestamp": 1564843352,
      "timestamp": 1564842736,
      "timestamp": 1564841252,
      "timestamp": 1564800352,
...
```



## jtgrassie | 2019-08-04T17:16:55+00:00
    curl -X POST http://127.0.0.1:28084/json_rpc -d '{"jsonrpc":"2.0","id":"0","method":"get_transfers","params":{"in":true,"account_index":0}}' -H 'Content-Type: application/json' | egrep 'height|timestamp'
      "height": 1138600,
      "timestamp": 1548304260,
      "height": 1146169,
      "timestamp": 1549257808,
      "height": 1182997,
      "timestamp": 1554420688,
      "height": 1183141,
      "timestamp": 1554437957,
      "height": 1204182,
      "timestamp": 1556986939,
      "height": 1204188,
      "timestamp": 1556987550,
    ...

## reardenlife | 2019-08-04T17:47:47+00:00
@jtgrassie
Great.  Looks like monero-wallet putting transactions in different sorting orders depending on the setup or on the mood of FSM.

## jtgrassie | 2019-08-04T17:59:49+00:00
> Great. Looks like monero-wallet putting transactions in different sorting orders depending on the setup or on the mood of FSM.

I wouldn't put it quite like that. 

Looking at the code, there is no specific sorting applied. Transactions are added to wallet2::m_transfers as they get processed and the RPC call essentially just dumps that vector as output. If you need a specific sort, I'd suggest sorting the results by height/timestamp, or maybe open an issue requesting sorting options for the RPC method(s)?

## hyc | 2019-08-04T18:18:03+00:00
I would vote against such a change. The RPC mechanism is just for low level transport of data. Sorting is purely a user interface/presentation issue and doesn't belong at this layer.

## jtgrassie | 2019-08-04T18:20:32+00:00
I tend to agree @hyc.  

## reardenlife | 2019-08-04T22:27:43+00:00
@jtgrassie
> " If you need a specific sort, I'd suggest sorting the results by height/timestamp, "

Yeah, thats what I ended up doing, as I pointed out in the question.

@hyc

> "I would vote against such a change. The RPC mechanism is just for low level transport of data. "

The problem is that in the majority of cases there is a need to get only N last transfers,  not all of them (in cases like mine, when I have to check if a specific output has been received).  So it is logical to request from RPC server sorted output (and, also a limit on it, like it is done in database servers).

> "Sorting is purely a user interface/presentation issue and doesn't belong at this layer."

Imagine the wallet with tens of thousands of transactions.  So I would have to "eat" this overhead each time I would like to check for a new transactions?

## jtgrassie | 2019-08-04T22:32:48+00:00
@reardenlife 

> The problem is that in the majority of cases there is a need to get only N last transfers ... Imagine the wallet with tens of thousands of transactions. So I would have to "eat" this overhead each time I would like to check for a nee transactions?

The [method](https://www.getmonero.org/resources/developer-guides/wallet-rpc.html#get_transfers) already allows you to use min/max/filter by height.

## reardenlife | 2019-08-04T23:26:39+00:00
@jtgrassie 

I wonder how in the world did I missed it.

## reardenlife | 2019-08-05T00:46:45+00:00
@jtgrassie

```bash
monero-v0.14.1.2]# curl -X POST http://127.0.0.1:18082/json_rpc -d '{"jsonrpc":"2.0","id":"0","method":"get_transfers","params":{"in":true,"account_index":0,"filter_by_height":true,"min_height":0,"max_height":100000000}}' -H 'Content-Type: application/json' | grep height
```

Am I missing something? Because it doesn't sort anything.

Brrrr!  Of course it doesn't.  It just returns the records from a specified range. :)

# Action History
- Created by: reardenlife | 2019-08-02T13:10:22+00:00
- Closed at: 2019-08-05T00:54:32+00:00
