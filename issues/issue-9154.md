---
title: Signature Verification on testnet
source_url: https://github.com/monero-project/monero/issues/9154
author: mdeacey
assignees: []
labels:
- question
- low priority
created_at: '2024-02-06T05:29:05+00:00'
updated_at: '2024-02-07T07:17:48+00:00'
type: issue
status: closed
closed_at: '2024-02-07T01:20:57+00:00'
---

# Original Description
I have a question regarding the signature verification behavior on testnet. I would like to understand whether the signature verification process on the testnet is intentionally lax or if there are specific settings or reasons for this behavior. 

For instance, if I change my request data to a faked or even empty signature, rpc still responds with `'good': True`.  

Is the signature verification process on testnet intentionally less strict compared to mainnet? Is there a monerod or rpc flag I can use to force testnet sig ver to be strict like it would be on mainnet?

Thanks a lot

# Discussion History
## plowsof | 2024-02-06T15:57:04+00:00
can you confirm if are you doing this in the cli or gui? you are trying to verify a signed message? (there is an open issue about this being not correctly implemented in the gui, or rather, for view only wallets* please confirm)

sorry, you are using this rpc call correct? https://www.getmonero.org/resources/developer-guides/wallet-rpc.html#verify

## plowsof | 2024-02-06T16:26:17+00:00
wallet rpc testnet sign/verify works. i use the wallets main address:
```
curl http://127.0.0.1:18082/json_rpc -d '{"jsonrpc":"2.0","id":"0","method":"sign","params":{"data":"This is sample data to be signed"}}' -H 'Content-Type: application/json'
{
  "id": "0",
  "jsonrpc": "2.0",
  "result": {
    "signature": "SigV2PECWS3q4j4jCFZqFneMM5KGfmWwgfrg27LF9QdaY6hofPFJQvL7jCJphvW1nfkv34BD3yp7gh4LMjS7GAPQjpPjF"
  }
}
```
```
curl http://127.0.0.1:18082/json_rpc -d '{"jsonrpc":"2.0","id":"0","method":"verify","params":{"data":"This is sample data to be signed","address":"A2JaqzYKf75MS17Ast12NhejooK6d29wRF6kvwqvxvUUT68BkSnBY57XAgqibjgQPyVM9TyT8RsFn1FXEsPcZE64LonF1iK","signature":"SigV2PECWS3q4j4jCFZqFneMM5KGfmWwgfrg27LF9QdaY6hofPFJQvL7jCJphvW1nfkv34BD3yp7gh4LMjS7GAPQjpPjF"}}' -H 'Content-Type: application/json'
{
  "id": "0",
  "jsonrpc": "2.0",
  "result": {
    "good": true,
    "old": false,
    "signature_type": "spend",
    "version": 2
  }
}
```
```
curl http://127.0.0.1:18082/json_rpc -d '{"jsonrpc":"2.0","id":"0","method":"verify","params":{"data":"This is sample data to be signed","address":"A2JaqzYKf75MS17Ast12NhejooK6d29wRF6kvwqvxvUUT68BkSnBY57XAgqibjgQPyVM9TyT8RsFn1FXEsPcZE64LonF1iK","signature":"BADigV2PECWS3q4j4jCFZqFneMM5KGfmWwgfrg27LF9QdaY6hofPFJQvL7jCJphvW1nfkv34BD3yp7gh4LMjS7GAPQjpPjF"}}' -H 'Content-Type: application/json'
{
  "id": "0",
  "jsonrpc": "2.0",
  "result": {
    "good": false,
    "old": false,
    "signature_type": "spend",
    "version": 0
  }
}
```

## mdeacey | 2024-02-07T01:20:57+00:00
Resolved. Thanks a lot.

## plowsof | 2024-02-07T06:42:38+00:00
Paste the request data you used to obtain a good: true response 

## mdeacey | 2024-02-07T07:17:47+00:00
Sorry, I've already replaced it with the above. It was most likely just incorrect params placement. But seems to work well now.

# Action History
- Created by: mdeacey | 2024-02-06T05:29:05+00:00
- Closed at: 2024-02-07T01:20:57+00:00
