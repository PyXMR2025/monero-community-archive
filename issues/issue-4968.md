---
title: tx not possible
source_url: https://github.com/monero-project/monero/issues/4968
author: smilesworld116
assignees: []
labels:
- invalid
created_at: '2018-12-11T20:17:09+00:00'
updated_at: '2019-01-19T00:33:06+00:00'
type: issue
status: closed
closed_at: '2019-01-19T00:33:06+00:00'
---

# Original Description
Monero version: 0.13.0.4
Network: stagenet
I'm using rpc call to initiate a transaction and get such error even though I have enough unlocked balance in the wallet.
Balance:
```
{
    "id": "0",
    "jsonrpc": "2.0",
    "result": {
        "balance": 7832720008,
        "multisig_import_needed": false,
        "per_subaddress": [
            {
                "address": "52smrM8WLGSXpduSjZ2Z9ePZBtZs62BviiEKWsbp7Du5fu87dNGH25GSnUwWw7BGEvBYTm8gGfbHeHViDkUwSzaiE6nnhqD",
                "address_index": 0,
                "balance": 7832720008,
                "label": "Primary account",
                "num_unspent_outputs": 155,
                "unlocked_balance": 7832720008
            }
        ],
        "unlocked_balance": 7832720008
    }
}
```

Following request is failed despite the amount is enough for it.
Request body:
`{"jsonrpc":"2.0","id":"0","method":"transfer","params":{"account_index":0,"ring_size":15,"destinations":[{"amount":4777555008,"address":"5A3ULnxZ2bsj5BuiHfGf18cUtj82N8dJgJo43CDnmPP1R36wjehsieeV5szDaWXUseLfYb6NcYhGJZCaaWiz4YEpD2ZgC7Z"}],"do_not_relay":true}}`
Response body:
```
{
  "error": {
    "code": -16,
    "message": "tx not possible"
  },
  "id": "0",
  "jsonrpc": "2.0"
}

```

If I decrease the amount a little it's working.
Request body:
`{"jsonrpc":"2.0","id":"0","method":"transfer","params":{"account_index":0,"ring_size":15,"destinations":[{"amount":3777555008,"address":"5A3ULnxZ2bsj5BuiHfGf18cUtj82N8dJgJo43CDnmPP1R36wjehsieeV5szDaWXUseLfYb6NcYhGJZCaaWiz4YEpD2ZgC7Z"}],"do_not_relay":true}}`
Response body:
```
{
    "id": "0",
    "jsonrpc": "2.0",
    "result": {
        "amount": 3777555008,
        "fee": 425960000,
        "multisig_txset": "",
        "tx_blob": "",
        "tx_hash": "74fe6681ac2f5cc4ad1f1146c99067a8e549f2ccc04ef02a41ea629ec3342c68",
        "tx_key": "",
        "tx_metadata": "",
        "unsigned_txset": ""
    }
}
```

You can see that fee is also small enough for previous transaction.

# Discussion History
## moneromooo-monero | 2018-12-11T21:23:06+00:00
Do you have many outputs, causing so many of these to be used that it doesn't fit in one tx ?

## smilesworld116 | 2018-12-11T23:10:22+00:00
There's only one output as you can see in the request body. I've done some transactions with up to 15 outputs before though.

## moneromooo-monero | 2018-12-11T23:55:50+00:00
I was asking about *your* outputs, which would get used as inputs to that tx.

## smilesworld116 | 2018-12-12T00:00:01+00:00
Do you mean `num_unspent_outputs` field in response of `get_balance` request? How do I check them?

## moneromooo-monero | 2018-12-12T00:09:58+00:00
Oh yes, thanks. 165 seems like a fair amount. When your tx succeeds, what is its size or weight ? The max tx size is half the block size, roughly speaking, With a block size of probably 300000, the max tx size is 150000.

## smilesworld116 | 2018-12-12T00:15:24+00:00
How do we know the size of tx? I don't see anything related to that in the response body from the RPC.

## moneromooo-monero | 2018-12-12T00:16:25+00:00
If you set the wallet log level to 2 (--log-level 2), you'll see it as it gets built.

## smilesworld116 | 2018-12-12T00:39:15+00:00
Maybe this is what you mean:
Transaction 1/1 <e89556e1354f9ffd17f04a145ee777506bde727b0562552fbe16d20594cc9a16>: 3529 weight, sending 0.001729340000 in 3 outputs to 1 destination(s), including 0.000557030000 fee, 0.000172310000 change
So weight is 3529 and is small enough.

## moneromooo-monero | 2018-12-12T00:50:32+00:00
Paste the entire log for the failing tx then (best to paste on fpaste.org or paste.debian.net)

## smilesworld116 | 2018-12-12T03:29:11+00:00
https://paste.fedoraproject.org/paste/ijPLWx17Ykn43Dy4MiXiCw/deactivate/msUauF5wkz1mq0LnN4lPe9rcCdgsCRek9WdtIxozhMy11i5b0cDSXNYDMhqOfawf
This is the entire log from the beginning of the rpc client, including following error line:
`2018-12-12 03:25:44.013	[RPC0]	ERROR	wallet.wallet2	src/wallet/wallet2.cpp:8511	1. THROW EXCEPTION: error::tx_not_possible`

## moneromooo-monero | 2018-12-12T09:18:31+00:00
This is not the correct link, it's a deactivation link, and looks like it got deleted already (probably because someone went to the actual link, maybe even a bot)

## smilesworld116 | 2018-12-12T09:59:48+00:00
Here it is again: https://paste.fedoraproject.org/paste/hRkND0yh51uxQGMCDR29-w/

## dEBRUYNE-1 | 2018-12-12T10:11:31+00:00
@smilesworld116 - You have to remove the `/deactivate/<string>` part upon pasting the paste link, otherwise someone (or perhaps a bot) is going to open it and the paste will get deactivated / removed. 

## moneromooo-monero | 2018-12-12T13:34:35+00:00
It seems to think there are 15 outputs of value 0.000000000001 each, which doesn't match the JSON you've sent above. Maybe a request is coming from elsewhere with these parameters ? Can you check whether you might have another program talking to the RPC ?

## smilesworld116 | 2018-12-12T14:52:30+00:00
Ok, I was using rpc in another script but it was not using 15 output at that moment.
Here is another log when I sent to initiate a transaction with 0.003 XMR while the wallet has approx. 0.00589XM in it which is enough for the amount + fee. (it was successful for 0.002 XMR with fee of around 0.00068)
https://paste.fedoraproject.org/paste/ZQ5S7CcM3oA29LoD0-Z2hA

## moneromooo-monero | 2018-12-12T15:05:33+00:00
You have 149 outputs which are below the usability threshold, totalling 0.00244782. So your usable balance is 0.00344829. The fee in the tx that is being built has reached 0.000814409276, so the amount needed is 0.003814409, which is above the 0.00344829 that's usable.

The usability threshold is when an output's value equals the extra fee needed to add it as an input (ie, the threshold at which adding it as an input actually decreases the output). You have lots of outputs of value 1 single atomic unit, unusable in practice.

## smilesworld116 | 2018-12-12T16:19:44+00:00
Ok but how do I know that amount? Because it says unlocked balance is 0.05896110008 from the response for balance request.

## moneromooo-monero | 2018-12-12T16:22:12+00:00
I'm not sure it's knowable. But you can toggle this with "set ignore-fractional-outputs [0|1]",
This should be added to the getbalance call.

## smilesworld116 | 2018-12-12T16:26:49+00:00
Sorry how do I add that? I tried ignore-fractional-outputs in params of get_balance but no luck with that.

## moneromooo-monero | 2018-12-12T16:48:33+00:00
You don't (unless you're a coder). I'll have to do that. ignore-fractional-outputs is a setting in monero-wallet-cli, which allows you to spend those tiny outputs anyway. You don't really want it.

## smilesworld116 | 2018-12-12T16:50:27+00:00
I'm a software engineer also. So let me try wallet cli and get back to you.

## smilesworld116 | 2018-12-12T16:59:06+00:00
I was able to find the `set ignore-fractional-outputs 0|1` option in wallet-cli but nothing changes by toggling it. I'm still seeing the same unlocked_balance and transactions failing to create.

## moneromooo-monero | 2018-12-12T18:19:00+00:00
You did change it while monero-wallet-rpc was not running, and you reloaded monero-wallet-rpc after that, right ?

## smilesworld116 | 2018-12-12T23:17:53+00:00
You're right but I also tried balance/transfer commands after setting ignore-fractional-outputs 0 or 1 in monero-wallet-cli without exiting it and there's luck with them too.

## moneromooo-monero | 2018-12-12T23:49:47+00:00
You're still getting the "Ignoring..." messages with ignore-fractional-outputs unset ?


## smilesworld116 | 2018-12-13T00:04:22+00:00
So here are logs from each case of setting that flag 0 and 1 respectively:
https://paste.fedoraproject.org/paste/Ov~6ZA~5iyE-t-TzJvc1Ig
https://paste.fedoraproject.org/paste/oNlnjTtUYX4vd1KI~2ImWQ

## moneromooo-monero | 2018-12-13T00:23:12+00:00
One of then doesn't, good. Instead, it adds all your other outputs, but since they're lower in amount than the fee increase they require, it ends up the same.


## smilesworld116 | 2018-12-13T00:47:17+00:00
Sounds interesting. I could see that setting is stored across the runs of the cli which sounds to me that it could be set in rpc also. If so, can I get that 'higher' fee in the calls?

## moneromooo-monero | 2018-12-13T01:12:37+00:00
It is also set in monero-wallet-rpc.

## smilesworld116 | 2018-12-13T01:18:31+00:00
So here are two logs again: one for XMR 0.0001 which was successful with fee of 0.000421959448 and the other for XMR 0.0002 which was failed even though I have 0.002821810003 in unlocked balance. I left ignore-fractional-outputs unset from wallet-cli.
Please let me know if we have an option to set/unset that setting from the rpc as well.

## moneromooo-monero | 2018-12-13T01:36:40+00:00
If you set it in monero-wallet-cli, it's set for monero-wallet-rpc, they use the same settings.


## smilesworld116 | 2018-12-13T02:58:55+00:00
Yeah, that's what I guessed too but it's not affecting anything I think. See above comment from me.

## moneromooo-monero | 2018-12-13T09:34:35+00:00
Looks like it does. See:
> One of then doesn't, good. Instead, it adds all your other outputs, but since they're lower in amount than the fee increase they require, it ends up the same.

## smilesworld116 | 2018-12-13T10:33:59+00:00
Sorry I forgot to add the links of paste board. Here they are again:
https://paste.fedoraproject.org/paste/ASmtWdtMYHwadgxyx~~vzQ/deactivate/HQRdo1sfmMXhn0FmGrEJjruY6OSF22bLrmO4EPu1yz0mcuHb9LebeggKah7sXHjj
https://paste.fedoraproject.org/paste/2~qvrsKgV3NTN-zeNLyJQg/deactivate/u203lFGcQZe6qRRtp6c5ZIv3VUh5F4lVFm7MknrwkptyE6cBRvrDm6fosn6KaDxx
One for XMR 0.0001 which was successful with fee of 0.000421959448 and the other for XMR 0.0002 which was failed even though I have 0.002821810003 in unlocked balance. I left ignore-fractional-outputs unset from wallet-cli.

What I'm looking for is to exhaust as much balance as possible by estimating fee before issuing a real transaction. But right now it's not allowing me to predict the fee properly because of such problems.

## moneromooo-monero | 2018-12-13T11:00:00+00:00
You can try sweep_all.

## smilesworld116 | 2018-12-13T11:03:59+00:00
What about the next wallet which will receive them? Won't it have the same problem when spending the amount received?

## moneromooo-monero | 2018-12-13T12:31:48+00:00
if you send them tiny outputs, yes.

## moneromooo-monero | 2019-01-19T00:24:24+00:00
This seems to have been "normal", just lots of tiny outs.
Tiny outs should not really be generated anymore, a lot of them are from old pools.
To be clear, sending a tx with lots of tiny outs in the inputs doesn't imply tiny outs in the outputs, unless you specify tiny amounts to send.

+invalid


# Action History
- Created by: smilesworld116 | 2018-12-11T20:17:09+00:00
- Closed at: 2019-01-19T00:33:06+00:00
