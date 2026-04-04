---
title: Address doesn't belong to the wallet while I created the address with wallet
  RPC "create_address"
source_url: https://github.com/monero-project/monero/issues/8567
author: ArayofEntropy
assignees: []
labels: []
created_at: '2022-09-14T14:54:31+00:00'
updated_at: '2022-09-22T03:27:48+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
1. ```curl http://127.0.0.1:18082/json_rpc -d '{"jsonrpc":"2.0","id":"0","method":"create_address","params":{"account_index":0,"label":"new-sub"}}' -H 'Content-Type: application/json'```
With this RPC interface I created an sub address.
2.```curl http://127.0.0.1:18082/json_rpc -d '{"jsonrpc":"2.0","id":"0","method":"get_address_index","params":{"address":"7BnERTpvL5MbCLtj5n9No7J5oE5hHiB3tVCK5cjSvCsYWD2WRJLFuWeKTLiXo5QJqt2ZwUaLy2Vh1Ad51K7FNgqcHgjW85o"}}' -H 'Content-Type: application/json' ```
However, while I check this address with RPC `get_address_index`, it returns `Address doesn't belong to the wallet`.

How is that happen?And is there any way to get this address back? Since I send some XMR coin to the address. May get some help?

# Discussion History
## selsta | 2022-09-14T18:05:35+00:00
Subaddresses are deterministic, there is no way to "lose" a subaddress. Are you sure you opened the same wallet in both cases?

## plowsof | 2022-09-14T20:28:25+00:00
sanity check:

create_address
```
curl http://127.0.0.1:18081/json_rpc -d '{"jsonrpc":"2.0","id":"0","method":"create_address","params":{"account_index":0,"label":"new-sub"}}' -H 'Content-Type: application/json''
{
  "id": "0",
  "jsonrpc": "2.0",
  "result": {
    "address": "84dFGjDZXYCUHTP3fTPces7QjP2MxK8hw8yCcy3vcB93X5Rzrv7BAjB6JKxVi1C4RBY437CX4ycuv8oz8fVk5CLh1tXPRwk",
    "address_index": 5,
    "address_indices": [5],
    "addresses": ["84dFGjDZXYCUHTP3fTPces7QjP2MxK8hw8yCcy3vcB93X5Rzrv7BAjB6JKxVi1C4RBY437CX4ycuv8oz8fVk5CLh1tXPRwk"]
  }
}
```
get_address_index:
```
curl http://127.0.0.1:18081/json_rpc -d '{"jsonrpc":"2.0","id":"0","method":"get_address_index","params":{"address":"84dFGjDZXYCUHTP3fTPces7QjP2MxK8hw8yCcy3vcB93X5Rzrv7BAjB6JKxVi1C4RBY437CX4ycuv8oz8fVk5CLh1tXPRwk"}}' -H 'Content-Type: application/json''
{
  "id": "0",
  "jsonrpc": "2.0",
  "result": {
    "index": {
      "major": 0,
      "minor": 5
    }
  }
}
```

please close

## ArayofEntropy | 2022-09-15T08:50:22+00:00
> 



> Subaddresses are deterministic, there is no way to "lose" a subaddress. Are you sure you opened the same wallet in both cases?

Yes,I'm sure. I had create about 500 hundred subaddresses, some of them could list by wallet some not. Really weird.

## ArayofEntropy | 2022-09-15T08:51:38+00:00
> sanity check:
> 
> create_address
> 
> ```
> curl http://127.0.0.1:18081/json_rpc -d '{"jsonrpc":"2.0","id":"0","method":"create_address","params":{"account_index":0,"label":"new-sub"}}' -H 'Content-Type: application/json''
> {
>   "id": "0",
>   "jsonrpc": "2.0",
>   "result": {
>     "address": "84dFGjDZXYCUHTP3fTPces7QjP2MxK8hw8yCcy3vcB93X5Rzrv7BAjB6JKxVi1C4RBY437CX4ycuv8oz8fVk5CLh1tXPRwk",
>     "address_index": 5,
>     "address_indices": [5],
>     "addresses": ["84dFGjDZXYCUHTP3fTPces7QjP2MxK8hw8yCcy3vcB93X5Rzrv7BAjB6JKxVi1C4RBY437CX4ycuv8oz8fVk5CLh1tXPRwk"]
>   }
> }
> ```
> 
> get_address_index:
> 
> ```
> curl http://127.0.0.1:18081/json_rpc -d '{"jsonrpc":"2.0","id":"0","method":"get_address_index","params":{"address":"84dFGjDZXYCUHTP3fTPces7QjP2MxK8hw8yCcy3vcB93X5Rzrv7BAjB6JKxVi1C4RBY437CX4ycuv8oz8fVk5CLh1tXPRwk"}}' -H 'Content-Type: application/json''
> {
>   "id": "0",
>   "jsonrpc": "2.0",
>   "result": {
>     "index": {
>       "major": 0,
>       "minor": 5
>     }
>   }
> }
> ```
> 
> please close

Yes, I'm going to run this way now. But I think there is a bug maybe for creating subaddress.

## selsta | 2022-09-15T08:51:46+00:00
Did you make sure to save the wallet after creating them? Otherwise you have to recreate them.

## ArayofEntropy | 2022-09-15T08:54:30+00:00
I'm sure about saving the wallet.  As you know, I could actually get the index of most addresses. Not all of the addresses are not belong.

## plowsof | 2022-09-15T10:31:10+00:00
apologies for the dumb sanity check @devilrayzl - i was unaware that 'the wallet file must be saved after creating the subaddress' else they will not "belong to the wallet" -> if this is true , and the get_address_index is simply searching the file for an address - and is not a deterministic process - there is a possibility - if the address was not written to file, it 'could happen'. 
- to confirm the address actually belongs to the wallet i would suggest you use something like monero-python , to create addresses offline , and then see if it exists (enter them into a database or just a list in memory)

## selsta | 2022-09-15T17:50:18+00:00
Try to open that wallet with monero-wallet-cli, enter `address all` and show what is says under the address with the index it should be.

## leolily7 | 2022-09-22T03:27:48+00:00
I also encountered this problem. Why are some addresses in my wallet address list missing, and the balance has not increased after being transferred to this address

# Action History
- Created by: ArayofEntropy | 2022-09-14T14:54:31+00:00
