---
title: Cant spend coinbase tx from a testnet wallet. might also affect mainet.
source_url: https://github.com/monero-project/monero/issues/1743
author: moneroexamples
assignees: []
labels: []
created_at: '2017-02-18T00:53:55+00:00'
updated_at: '2017-02-20T21:04:22+00:00'
type: issue
status: closed
closed_at: '2017-02-20T21:04:22+00:00'
---

# Original Description
I have testnet wallet with only coinbase transactions:

mnemonic seed
```
skew saucepan talent tinted lesson maximum rover eggs phrases coffee gnome glass tepid upbeat justice spying obvious toilet hoisting useful lukewarm nephew begun beyond glass
```

The txs are unspendable currently using monero-wallet-cli `0.10.1.0-3f171b93`

Any attempt to make an outgoing tx from this wallet results in failure as no outputs are chosen:

```
[wallet 9uzUJf]: transfer 9uzUJfjustwcwWa7MwryVeVqDA6PopLNNXeLCJNR8Abagb4wMLsAYXsBXFi5kCHcZ2YG6y56hdWLt1Gvc1xR3DxjAqeitnJ 1
Wallet password: 
Sending 0.000000000000.  The transaction fee is 0.000000000000
Is this okay?  (Y/Yes/N/No): 
```
After pressing Yes:
```
Error: transaction <0cb66f6e05387bcfc613a09c9a3fadb03218d2222342a3037275b1a196a6a520> was rejected by daemon with status: Failed
```

Dont know if this is same for mainet coinbase wallets. Dont have any coinbase wallets in mainnet to check this behaviour.

This issue is directly related to this question:
http://monero.stackexchange.com/questions/3638/how-are-outpk-mask-and-amount-fields-created-when-spending-rignct-coinbase-txs

As I want to check how coinbase ringct txs are being processed for spending, but cant spend anything unfortunately. 


# Discussion History
## moneroexamples | 2017-02-18T03:43:41+00:00
Based on the anwser at http://monero.stackexchange.com/questions/3638/how-are-outpk-mask-and-amount-fields-created-when-spending-rignct-coinbase-txs

it seems I have to send all coinbase txs to myself, before being able to send them to other address. 
I used `sweep_all` to myself, and it worked. 

But I still dont understand why I would have to do it, before being able to spent coinbase txs? Is it same for mainnet? 

## ghost | 2017-02-18T09:48:36+00:00
Does #1729 have anything to do with this?

(Not likely, but just asking)

## moneromooo-monero | 2017-02-18T11:24:53+00:00
Works for me. Post a wallet log with set_log 2.


## ghost | 2017-02-18T20:59:06+00:00
Can we make the wallet use the same syntax as the daemon? i.e. `log-level=2`

## moneromooo-monero | 2017-02-18T22:58:14+00:00
Does it not ?

## moneroexamples | 2017-02-18T23:39:15+00:00
@NanoAkron @moneromooo-monero 

Generated new testnet wallet with some coinbase txs. 
```
9tG76Zd1To2brvJEFD22BGHXPhz7K8PVMMRnuP5urG1UcbbFk2po3f8e1NeoPGeFPCUij8sVPMte6g8VqX3SLfsc54VEcsZ
viewkey:  1ebc6602e9b38d6eef14364b8ddfbc8190a2b33c96aaedc68eb7761b4ff62e03
spendkey: af0001cff93087e7d3564e2ce8defa3e6792478d6ae90c05153e2b3623592b07
```
I have one unlocked coinbase for now, but the resuults is same as before (and before I had many unlocked coinbase txs). 

```
[wallet 9tG76Z]: transfer 9uzUJfjustwcwWa7MwryVeVqDA6PopLNNXeLCJNR8Abagb4wMLsAYXsBXFi5kCHcZ2YG6y56hdWLt1Gvc1xR3DxjAqeitnJ 1
Wallet password: 
Sending 0.000000000000.  The transaction fee is 0.000000000000
Is this okay?  (Y/Yes/N/No): Y
Error: transaction <0cb66f6e05387bcfc613a09c9a3fadb03218d2222342a3037275b1a196a6a520> was rejected by daemon with status: Failed
[wallet 9tG76Z]: 
```

The relevant log=2 part from wallet:

```
2017-02-19 07:36:47.639	    7f8837576d00	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:4130	transfer: adding 1.000000000000, for a total of 1.000000000000
2017-02-19 07:36:47.725	    7f8837576d00	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:4150	Starting with 1 non-dust outputs and 0 dust outputs
2017-02-19 07:36:47.726	    7f8837576d00	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:4175	checking preferred
2017-02-19 07:36:47.812	    7f8837576d00	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:3998	estimated rct tx size for 2 at mixin 5 and 2: 13286 (896 saved)
2017-02-19 07:36:47.812	    7f8837576d00	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:4007	pick_preferred_rct_inputs: needed_money 1.032752156060
2017-02-19 07:36:47.812	    7f8837576d00	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:4015	We can use 0 alone: 12.634351019175
2017-02-19 07:36:47.812	    7f8837576d00	INFO 	wallet.wallet2	src/wallet/wallet2.cpp:4189	Found prefered rct inputs for rct tx: 0(12.634351019175) 
2017-02-19 07:36:47.812	    7f8837576d00	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:4192	done checking preferred
2017-02-19 07:36:47.812	    7f8837576d00	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:4201	Start of loop with 1 0
2017-02-19 07:36:47.812	    7f8837576d00	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:4202	unused_transfers_indices:
2017-02-19 07:36:47.812	    7f8837576d00	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:4204	  0
2017-02-19 07:36:47.812	    7f8837576d00	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:4205	unused_dust_indices:
2017-02-19 07:36:47.812	    7f8837576d00	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:4208	dsts size 1, first 1000000000000
2017-02-19 07:36:47.812	    7f8837576d00	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:4209	adding_fee 0, use_rct 1
2017-02-19 07:36:47.812	    7f8837576d00	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:4233	Second outout was not strictly needed, and relatedness 1, not adding
2017-02-19 07:36:47.812	    7f8837576d00	INFO 	wallet.wallet2	src/wallet/wallet2.cpp:4385	Done creating 1 transactions, 0.000000000000 total fee, 0.000000000000 total change
2017-02-19 07:36:47.812	    7f8837576d00	INFO 	wallet.wallet2	src/wallet/wallet2.cpp:4397	  Transaction 1/1: 0 kB, sending 0.000000000000 in 0 outputs to 0 destination(s), including 0.000000000000 fee, 0.000000000000 change
2017-02-19 07:36:49.412	    7f8837576d00	ERROR	wallet.wallet2	src/wallet/wallet2.cpp:2999	daemon_send_resp.status != CORE_RPC_STATUS_OK. THROW EXCEPTION: error::tx_rejected
2017-02-19 07:36:49.412	    7f8837576d00	WARN 	net.http	src/wallet/wallet_errors.h:697	/home/mwo/monero/src/wallet/wallet2.cpp:2999:N5tools5error11tx_rejectedE: transaction was rejected by daemon, status = Failed, tx:
{
  "version": 1, 
  "unlock_time": 0, 
  "vin": [ ], 
  "vout": [ ], 
  "extra": [ ], 
  "signatures": [ ]
}
2017-02-19 07:36:49.412	    7f8837576d00	INFO 	stacktrace	src/common/stack_trace.cpp:119	Exception: tools::error::tx_rejected
```

I will not make any normal tx into this new wallet or sent to myself, so that everyone can inport this wallet and test it. Sending out tx from previous wallet posted earlier already works, as I `spent_all` to myself, and already done bunch of txs there.



## moneromooo-monero | 2017-02-19T00:19:16+00:00
I can repro with that one.

## moneroexamples | 2017-02-19T04:30:13+00:00
This is due to break in wallet2.cpp: 
https://github.com/monero-project/monero/blob/master/src/wallet/wallet2.cpp#L4234

Commenting out the break, seems to fix the problem:
```
      if (relatedness > SECOND_OUTPUT_RELATEDNESS_THRESHOLD)
      {
        LOG_PRINT_L2("Second outout was not strictly needed, and relatedness " << relatedness << ", not adding");
        //break;
      }
```


## moneromooo-monero | 2017-02-19T09:37:41+00:00
https://github.com/monero-project/monero/pull/1749

This logic is fairly complex, so I'm not saying it's 100% bug free :)

## moneroexamples | 2017-02-20T02:46:31+00:00
seems to work. thanks!.

 But before I close the issue, i have one question: What is this `relatedness`? What does it do when spending in monero?

## moneromooo-monero | 2017-02-20T09:19:34+00:00
It measures how related an output is with a set of the already selected outputs. This is currently whether the output is within N blocks of another.

## moneroexamples | 2017-02-20T21:04:22+00:00
Thanks again. 

# Action History
- Created by: moneroexamples | 2017-02-18T00:53:55+00:00
- Closed at: 2017-02-20T21:04:22+00:00
