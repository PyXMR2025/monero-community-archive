---
title: Why can't the transaction be confirmed? This is on my private chain, mining
  is enabled, and gas is normal.
source_url: https://github.com/monero-project/monero/issues/9372
author: phpmac
assignees: []
labels:
- invalid
created_at: '2024-06-20T08:52:54+00:00'
updated_at: '2024-06-20T10:25:12+00:00'
type: issue
status: closed
closed_at: '2024-06-20T09:10:03+00:00'
---

# Original Description
Why can't the transaction be confirmed? This is on my private chain, mining is enabled, and gas is normal.

```

> txpool.contentINFO [06-20|04:51:53.132] Generating DAG in progress               epoch=26 percentage=21 elapsed=10.554s

{
  pending: {},
  queued: {
    0x5F4f6C0654233070F74515d627973909BE9906a7: {
      209: {
        blockHash: null,
        blockNumber: null,
        chainId: "0x270e",
        from: "0x5f4f6c0654233070f74515d627973909be9906a7",
        gas: "0x5208",
        gasPrice: "0x6b49d2000",
        hash: "0x8c716ae56af8e6bd28aa4db65bfc6b5717951a5c4d9bd8b927c4bf6caada260d",
        input: "0x",
        nonce: "0xd1",
        r: "0x653d14fd6c10a81e62a4e49923eb84a7a61fdd5f9929c6197c44c4df1934effe",
        s: "0x58d3751ccaf195daea31c191f8bcaf941d5d5dc67aadf453acdd58f649a9bcde",
        to: "0xef6c9abf4968656ba30afc64c4b12e952054d653",
        transactionIndex: null,
        type: "0x0",
        v: "0x4e40",
        value: "0xde0b6b3a7640000"
      }
    }
  }
}
> IN

INFO [06-20|04:52:01.553] Generating DAG in progress               epoch=26 percentage=39 elapsed=18.975s
INFO [06-20|04:52:02.058] Generating DAG in progress               epoch=26 percentage=40 elapsed=19.480s
INFO [06-20|04:52:02.507] Generating DAG in progress               epoch=26 percentage=41 elapsed=19.929s
INFO [06-20|04:52:02.969] Generating DAG in progress               epoch=26 percentage=42 elapsed=20.391s
INFO [06-20|04:52:03.450] Generating DAG in progress               epoch=26 percentage=43 elapsed=20.872s
INFO [06-20|04:52:03.917] Generating DAG in progress               epoch=26 percentage=44 elapsed=21.339s
INFO [06-20|04:52:04.414] Generating DAG in progress               epoch=26 percentage=45 elapsed=21.836s
INFO [06-20|04:52:04.886] Generating DAG in progress               epoch=26 percentage=46 elapsed=22.308s
INFO [06-20|04:52:05.320] Generating DAG in progress               epoch=26 percentage=47 elapsed=22.742s
INFO [06-20|04:52:05.793] Generating DAG in progress               epoch=26 percentage=48 elapsed=23.216s
INFO [06-20|04:52:05.895] Looking for peers                        peercount=1 tried=0 static=0
INFO [06-20|04:52:06.269] Generating DAG in progress               epoch=26 percentage=49 elapsed=23.691s
INFO [06-20|04:52:06.747] Generating DAG in progress               epoch=26 percentage=50 elapsed=24.169s
INFO [06-20|04:52:07.210] Generating DAG in progress               epoch=26 percentage=51 elapsed=24.632s
INFO [06-20|04:52:07.721] Generating DAG in progress               epoch=26 percentage=52 elapsed=25.143s
INFO [06-20|04:52:08.236] Generating DAG in progress               epoch=26 percentage=53 elapsed=25.658s
INFO [06-20|04:52:08.700] Generating DAG in progress               epoch=26 percentage=54 elapsed=26.122s
INFO [06-20|04:52:09.155] Generating DAG in progress               epoch=26 percentage=55 elapsed=26.577s
INFO [06-20|04:52:09.618] Generating DAG in progress               epoch=26 percentage=56 elapsed=27.040s
INFO [06-20|04:52:10.087] Generating DAG in progress               epoch=26 percentage=57 elapsed=27.509s

> INFO [06-20|04:52:10.575] Generating DAG in progress               epoch=26 percentage=58 elapsed=27.997s

> INFO [06-20|04:52:11.060] Generating DAG in progress               epoch=26 percentage=59 elapsed=28.482s

> INFO [06-20|04:52:11.407] Commit new sealing work                  number=753,971 sealhash=6da928..9fc002 uncles=0 txs=0 gas=0 fees=0 elapsed=30.001s
INFO [06-20|04:52:11.657] Generating DAG in progress               epoch=26 percentage=60 elapsed=29.079s
INFO [06-20|04:52:12.398] Successfully sealed new block            number=753,971 sealhash=6da928..9fc002 hash=9eeed2..145366 elapsed=991.743ms
INFO [06-20|04:52:12.399] "🔨 mined potential block"                number=753,971 hash=9eeed2..145366
INFO [06-20|04:52:12.564] Generating DAG in progress               epoch=26 percentage=61 elapsed=29.986s
INFO [06-20|04:52:13.039] Generating DAG in progress               epoch=26 percentage=62 elapsed=30.461s
INFO [06-20|04:52:13.500] Generating DAG in progress               epoch=26 percentage=63 elapsed=30.922s
INFO [06-20|04:52:13.988] Generating DAG in progress               epoch=26 percentage=64 elapsed=31.410s
INFO [06-20|04:52:14.477] Generating DAG in progress               epoch=26 percentage=65 elapsed=31.899s
INFO [06-20|04:52:14.948] Generating DAG in progress               epoch=26 percentage=66 elapsed=32.370s
INFO [06-20|04:52:15.428] Generating DAG in progress               epoch=26 percentage=67 elapsed=32.850s
```

# Discussion History
## selsta | 2024-06-20T08:54:47+00:00
How is this monero related?

## selsta | 2024-06-20T09:10:03+00:00
This appears to be a mistakenly opened issue or LLM generated...

## phpmac | 2024-06-20T10:22:29+00:00
> How is this monero related?


It may be a translation problem. I did not say it has anything to do with Monero. The latest mining deployed in the private chain can generate new blocks, but the transactions can never be confirmed. Why is that?

instance: DJ-test/v1.11.6-stable/linux-amd64/go1.21.6

## phpmac | 2024-06-20T10:22:51+00:00
```
{
  "config": {
    "chainId": 9998,
    "homesteadBlock": 0,
    "byzantiumBlock": 0,
    "constantinopleBlock": 0,
    "eip155Block": 0,
    "eip158Block": 0,
    "eip150Block": 0,
    "eip150Hash": "0x0000000000000000000000000000000000000000000000000000000000000000",
    "ethash": {}
  },
  "coinbase": "0x0000000000000000000000000000000000000000",
  "difficulty": "0x20000",
  "extraData": "",
  "gasLimit": "0x2fefd8",
  "nonce": "0x0000000000000042",
  "mixhash": "0x0000000000000000000000000000000000000000000000000000000000000000",
  "parentHash": "0x0000000000000000000000000000000000000000000000000000000000000000",
  "timestamp": "0x00",
  "alloc": {
    "0x51282275dfa31d8063fdc5f3e41dd18c1dceb5e7": {
      "balance": "23300000000000000000000000000"
    }
  }
}
```


```
~/geth-linux-amd64-1.11.6-ea9e62ca/geth -miner.etherbase 0x48000000De541d67E93a2744737ff5A6ecA1D049 --datadir ./data init ./genesis.json
~/geth-linux-amd64-1.11.6-ea9e62ca/geth -miner.etherbase 0x48000000De541d67E93a2744737ff5A6ecA1D049 --datadir ./data --networkid 9998 --port 30303 --http --http.addr 0.0.0.0 --http.port 81 --ws --ws.addr "0.0.0.0" --ws.port 82 --http.corsdomain "\*" --http.api personal,db,eth,net,web3 --nat extip:107.175.197.140 console


```

## selsta | 2024-06-20T10:23:58+00:00
This is the repository for the monero project. I don't know why you are asking questions about Ethereum here, but it's not the correct place.

## phpmac | 2024-06-20T10:25:11+00:00
> This is the repository for the monero project. I don't know why you are asking questions about Ethereum here, but it's not the correct place.

ohohoh,,,, sorry

# Action History
- Created by: phpmac | 2024-06-20T08:52:54+00:00
- Closed at: 2024-06-20T09:10:03+00:00
