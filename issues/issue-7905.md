---
title: Double spend error when sending tx
source_url: https://github.com/monero-project/monero/issues/7905
author: pinpins
assignees: []
labels: []
created_at: '2021-08-28T17:25:03+00:00'
updated_at: '2023-10-20T13:03:37+00:00'
type: issue
status: closed
closed_at: '2023-10-20T13:03:36+00:00'
---

# Original Description
Hello,

We mined a block at zergpool 000473eb575993f8f25979aee6ceec45909ef7b2812b41c5f3fbe3d9ddcf60e2
https://zergpool.com/site/block?coin=XMR

it was accounted in monero-wallet-rpc log
```

2021-08-28 16:12:51.817 W Spent money: 0.000953865552, with tx: <b2a76d89430e2bea440dd2dba5b2b303a16e34272731286e58a90a66186bae54>
2021-08-28 16:14:03.032 W Received money: 0.888903652409, with tx: <649c07f1c9f8e23689946ed0b182384d2f2f80d53d11bcb3922a95e4b667964a>
2021-08-28 16:14:04.621 W Received money: 0.999900000000, with tx: <17827bd560fcb7fe3e78a0e4102067cd50f7e13d0915162c5a89c844025ecc69>


```
However all transfer tx stopped working since we got this block.

all of them were reporting 

```
2021-08-28 15:17:56.149 E daemon_send_resp.status != CORE_RPC_STATUS_OK. THROW EXCEPTION: error::tx_rejected
2021-08-28 15:17:56.154 W  (double spend)

```

Then I have started monero-wallet-cli tool and run rescan_spent, that problematic block disappeared from wallet balance, and transfer function started to work.

Any sensible explanation what has happened, as miner who mined the block would like to get paid for it.

thanks!



# Discussion History
## selsta | 2022-02-19T00:07:44+00:00
So just for clarification, this coinbase transaction isn't visible in your wallet anymore? https://xmrchain.net/tx/649c07f1c9f8e23689946ed0b182384d2f2f80d53d11bcb3922a95e4b667964a

## CreatedForYou | 2023-10-20T11:54:15+00:00
![Uploading 
20231020_144506_6776125493183899526_20231020145336.jpg…]()
Hello please help me

## selsta | 2023-10-20T13:03:36+00:00
Closing for inactivity, @CreatedForYou please create a separate issue and add more details.

# Action History
- Created by: pinpins | 2021-08-28T17:25:03+00:00
- Closed at: 2023-10-20T13:03:36+00:00
