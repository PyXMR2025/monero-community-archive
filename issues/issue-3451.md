---
title: How to generate GENESIS_TX and GENESIS_NONCE?
source_url: https://github.com/monero-project/monero/issues/3451
author: '15963'
assignees: []
labels:
- invalid
created_at: '2018-03-20T11:56:49+00:00'
updated_at: '2018-03-27T14:49:11+00:00'
type: issue
status: closed
closed_at: '2018-03-20T12:16:47+00:00'
---

# Original Description
How to generate GENESIS_TX and GENESIS_NONCE? 
Does GENESIS_NONCE have any special meaning?

 demo:
    std::string const GENESIS_TX = "013c01ff0001ffffffffffff0302df5d56da0c7d643ddd1ce61901c7bdc5fb1738bfe39fbe69c28a3a7032729c0f2101168d0c4ca86fb55a4cf6a36d31431be1c53a3bd7411bb24e8832410289fa6f3b";
    uint32_t const GENESIS_NONCE = 10002;


# Discussion History
## hyc | 2018-03-20T12:15:09+00:00
This issue tracker is for bug reports, it's not a help desk. Try monero.stackexchange.com.
+invalid

## 15963 | 2018-03-20T12:30:38+00:00
@hyc do you have qq or wechat??

## sebseb7 | 2018-03-20T15:17:07+00:00
use some other daemon that supports "--print-genesis-tx" , compile that daemon with your coin parameters to get a correct genesis tx

## 15963 | 2018-03-21T03:45:53+00:00
I  use cryptonote , it supports --print-genesis-tx.
url is : https://github.com/cryptonotefoundation/cryptonote.

is it generated, can it be used in Monero?
@sebseb7 @hyc 

## sebseb7 | 2018-03-27T14:49:11+00:00
"is it generated, can it be used in Monero?"

you can use a genesis tx from forknote in monero as long as the coin parameters are the same

# Action History
- Created by: 15963 | 2018-03-20T11:56:49+00:00
- Closed at: 2018-03-20T12:16:47+00:00
