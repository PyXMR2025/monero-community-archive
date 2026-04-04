---
title: monero-wallet-rcp's get_payments doesn't return a transaction by payment id,
  when the payment was made from the same wallet
source_url: https://github.com/monero-project/monero/issues/6459
author: thestick613
assignees: []
labels: []
created_at: '2020-04-17T17:30:20+00:00'
updated_at: '2020-04-17T19:01:08+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Hello,

I'm fixing an integration.

I have the same wallet mnemonic loaded into a linux server and into a desktop wallet. I'm generating an address from the server and i'm using the desktop wallet to pay it.

I remember this scenario working on 0.14, but it doesn't work anymore on 0.15: i can see the outgoing transaction from myself to myself in the desktop gui, but if i try to find that transaction on the server using the payment id, it doesn't appear:

```
curl --digest --user xxx:xxx -X POST http://1.2.3.4:80/json_rpc -d '{"jsonrpc":"2.0","id":"0","method":"get_payments", "params": {"payment_id": "16_digit_payment_id"}}' -H 'Content-Type: application/json'
{
  "id": "0",
  "jsonrpc": "2.0",
  "result": {
  }
```

I've tested this several times, and it didn't return any result. I then moved some XMR to a different wallet (i've generated one on mymonero.com), then payed, using the same address + payment id, and it worked, returning the correct result on "get_payments".

I think there's a bug, or something changed between 0.14 and 0.15. I think sending a payment from myself to myself should appear in get_payments.

# Discussion History
## moneromooo-monero | 2020-04-17T18:51:23+00:00
Sending back to the sending address is functionally the same as sending a 0 amount and getting back the rest as change.

## thestick613 | 2020-04-17T18:58:21+00:00
I am aware, but this worked in 0.14.
Plus, i can see that transaction in transactions in the GUI, in **full amount**, and it has the correct payment id - 16_digit_payment_id.

The same transaction is a interpreted as a 0.0 amount TX in Cake Wallet.

Monero should clarify the semantics of sending from the same wallet to the same wallet. Do you think this kind of transaction should appear in get_payments?

## selsta | 2020-04-17T19:00:51+00:00
> Plus, i can see that transaction in transactions in the GUI, in full amount, and it has the correct payment id - 16_digit_payment_id.

`get_payments` means only showing incoming transactions. GUI and cake wallet show incoming and outgoing transactions, that’s why it shows up.

# Action History
- Created by: thestick613 | 2020-04-17T17:30:20+00:00
