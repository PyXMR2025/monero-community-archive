---
title: '[BUG] monero-wallet-rpc/cli show_transfer [TxID] when OUT. doesnt show integrated
  address/shows incorrect payment id'
source_url: https://github.com/monero-project/monero/issues/6505
author: IvRRimum
assignees: []
labels: []
created_at: '2020-05-04T18:10:50+00:00'
updated_at: '2020-07-12T10:01:37+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Sender Wallet - Fetches OUT transactions(or show_transfer by id) sees actual address(even tho transfer was made to integrated address) and payment id: 000000000
Recipient Wallet - Fetches In transactions(or show_transfer by id) sees integrated address AND correct payment ID.

I tested by opening both wallets in cli/rpc and doing show_transfer [txID], got different results.

Are there any workarounds for this?

# Discussion History
## moneromooo-monero | 2020-05-05T02:04:58+00:00
It should be possible to fix if you have the original wallet cache (as it saves the original destination address). If not, you can't know since only the resipient can decrypt the payment id.

## moneromooo-monero | 2020-06-05T12:13:22+00:00
I just tried, and it works for me. I created an integrated address in wallet A, yielding integrated address I and payment id P, send to that integrated address from wallet B, got txid T, ran show_transfer T in wallet B, and it shows both I and P. Maybe it got recently fixed, or maybe you're doing something slightly different. Can you expand ?

## ollitsac107 | 2020-07-12T10:01:36+00:00
****

# Action History
- Created by: IvRRimum | 2020-05-04T18:10:50+00:00
