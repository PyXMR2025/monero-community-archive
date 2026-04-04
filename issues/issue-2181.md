---
title: Wallet CLI and RPC is not listing all transactions for same payment ID
source_url: https://github.com/monero-project/monero/issues/2181
author: skironDotNet
assignees: []
labels: []
created_at: '2017-07-18T16:15:09+00:00'
updated_at: '2017-08-18T16:56:45+00:00'
type: issue
status: closed
closed_at: '2017-08-18T16:56:45+00:00'
---

# Original Description
When a user makes 2+ transfers using same PID it won't show all transactions by issuing "payments" command or RPC call. Old version of wallet-cli/simplewallet was showing all TXs from same PID.
Wallet integration is not possible or more complicated to account payments to specific user by PID.


In the first picture you can see wallet query with two transactions has same PID, ie. a parson made 2 separate transfers with same PID. Then when you query "payments" by PID, only one TX is returned.
On the second pic you can see json RPC with only one TX as well. 

Please note cli returns diffrent TX than RPC, meaning "sorting" is implemented differently in CLI and RPC, but both TX match queries by TX, so in my opinion the bug exists (in comparison to older versions of CLI tools). Both the CLI and RPC should return all TX for given PID. In case of RPC it should be possible to select TX range, let say 20 transfers was made to same PID, then you should be query "give me last 5"  

![bug in xmr wallet](https://user-images.githubusercontent.com/2981715/28327436-0c544a7a-6ba9-11e7-9f29-84f9a0699da8.png)

![bug in xmr wallet2](https://user-images.githubusercontent.com/2981715/28327485-30eab7b6-6ba9-11e7-92a2-d63acb944933.png)

only "show_transfers" in CLI shows all TX and I can identify those with same PID:

![bug in xmr wallet 3](https://user-images.githubusercontent.com/2981715/28329108-39a0dcc8-6bae-11e7-89ac-9097350a694a.png)


# Discussion History
## skironDotNet | 2017-07-18T16:42:05+00:00
get_bulk_payments also returns one TX while should be two. 

## moneromooo-monero | 2017-07-24T10:23:48+00:00
This seems to work fine here, both with payments in monero-wallet-cli and get_bulk_payments in monero-wallet-rpc.

Can you try with current master and see if that still happens ? 

## skironDotNet | 2017-08-07T22:50:50+00:00
Just tried build around commit bfd2532ea53b9422b219aec61a662318b18b747b
(because I downloaded zip and I see this commit 1h ago, so plus my build time, may be +/- 10 commits)

Anyhow so I build on ubuntu, all good. Same result. View only wallet shows last transaction with same PID, Full wallet shows first transaction, in both cases the command payments {PID} shows only one TX while should list two. 

Correct behavior for "payments PID" could be represented as "show_transfers" + filter by PID 

Is it possible the bug comes from the fact both amounts are equal?

## moneromooo-monero | 2017-08-07T23:18:55+00:00
The amount should not make a difference as the key is the payment id. I'll try again tomorrow and list the steps I take if it still works. Then you can test that, and if it works, post your exact steps too.

## moneromooo-monero | 2017-08-18T15:06:02+00:00
Sorry, I'd forgot about this. I just tried it again, and it works with both cli and rpc. See my steps below. If it still doesn't work for you (try master), include your own steps.

./build/debug/bin/monero-wallet-cli --testnet --generate-new-wallet pid-test
[...]
Generated new wallet: 9wWFqVRCjXWQpsRgYS55VUFPx56J5XM8e9APNjNfHTknfk65XUL1baJXWPRbG7Rw3MT4BjiLsXyETJoFFHxPryU1Vag7pGj
[...]
./build/debug/bin/monero-wallet-cli --testnet --wallet-file /some/other/wallet
[...]
transfer 5 9wWFqVRCjXWQpsRgYS55VUFPx56J5XM8e9APNjNfHTknfk65XUL1baJXWPRbG7Rw3MT4BjiLsXyETJoFFHxPryU1Vag7pGj 1 462d95e922c7b3d4
transfer 5 9wWFqVRCjXWQpsRgYS55VUFPx56J5XM8e9APNjNfHTknfk65XUL1baJXWPRbG7Rw3MT4BjiLsXyETJoFFHxPryU1Vag7pGj 0.5 462d95e922c7b3d4

in the new wallet again:
Height 978307, transaction <cd13197198dfdcb54c8035bf5f0f2e569f186e618828fb3d7fa6431cdbba5bb0>, received 1.000000000000
Height 978307, transaction <6c296562552bd069fe148f136bf63ad0aa94b7387556e5470df47fdcf1b50e36>, received 0.500000000000
[...]
[wallet 9wWFqV]: payments 462d95e922c7b3d4
                                                             payment                                                         transaction      height               amount     unlock time
  <462d95e922c7b3d4000000000000000000000000000000000000000000000000>  <6c296562552bd069fe148f136bf63ad0aa94b7387556e5470df47fdcf1b50e36>      978307       0.500000000000               0
  <462d95e922c7b3d4000000000000000000000000000000000000000000000000>  <cd13197198dfdcb54c8035bf5f0f2e569f186e618828fb3d7fa6431cdbba5bb0>      978307       1.000000000000               0

With RPC:

./build/debug/bin/monero-wallet-rpc --testnet --wallet-file pid-test --password '' --rpc-bind-port 8888 --disable-rpc-login

From another terminal:

$ curl -X POST http://127.0.0.1:8888/json_rpc -d '{"jsonrpc":"2.0","id":"0","method":"get_bulk_payments","params":{"payment_ids":["462d95e922c7b3d4"]}}' -H 'Content-Type: application/json'
{
  "id": "0",
  "jsonrpc": "2.0",
  "result": {
    "payments": [{
      "amount": 500000000000,
      "block_height": 978307,
      "payment_id": "462d95e922c7b3d4",
      "tx_hash": "6c296562552bd069fe148f136bf63ad0aa94b7387556e5470df47fdcf1b50e36",
      "unlock_time": 0
    },{
      "amount": 1000000000000,
      "block_height": 978307,
      "payment_id": "462d95e922c7b3d4",
      "tx_hash": "cd13197198dfdcb54c8035bf5f0f2e569f186e618828fb3d7fa6431cdbba5bb0",
      "unlock_time": 0
    }]
  }
}

## skironDotNet | 2017-08-18T15:38:35+00:00
Please notice both of your transactions have been posted and processed via same "block_height": 978307
I don't know if it matters but in my example a user made 2 transactions to same PID at diffrent time, processed at different block height.

Also the case I'm posting is production implementation. I don't know who the user was and what type/version of a client has been used to make the transaction.

Another thing is you tried with different transaction amount which make it more distinct than in my case where there are **2 separate transactions with _same PID, same amount, same date_, different block height**.

https://user-images.githubusercontent.com/2981715/28329108-39a0dcc8-6bae-11e7-89ac-9097350a694a.png

Also is it possible that the cli could have a bug relevant to the block chain version and ringCT vs regular transaction? The testnet transaction you showing is at much lower block number and so it may be possible is handled differently than recent transactions.    

## skironDotNet | 2017-08-18T15:39:52+00:00
Sorry clicked wrong button by trying to re-edit

## moneromooo-monero | 2017-08-18T16:15:56+00:00
I've just sent another couple tx to the same wallet (one with a duplicate amount), also seen:

[wallet 9wWFqV]: payments 462d95e922c7b3d4
                                                             payment                                                         transaction      height               amount     unlock time
  <462d95e922c7b3d4000000000000000000000000000000000000000000000000>  <3bc85fb84411c987dbe8265e9225e8b06f791342bfcd3eb2c9d7f24c97cf3a65>      978330       1.000000000000               0
  <462d95e922c7b3d4000000000000000000000000000000000000000000000000>  <98d24188542675d560b46e8d7ca84d86d2bf24083fa7e0296d134edc0ea808b2>      978329       0.250000000000               0
  <462d95e922c7b3d4000000000000000000000000000000000000000000000000>  <cd13197198dfdcb54c8035bf5f0f2e569f186e618828fb3d7fa6431cdbba5bb0>      978307       1.000000000000               0
  <462d95e922c7b3d4000000000000000000000000000000000000000000000000>  <6c296562552bd069fe148f136bf63ad0aa94b7387556e5470df47fdcf1b50e36>      978307       0.500000000000               0



RingCT is extremely unlikely to have any effect on this, as the payments are recorded after the txes are decoded, so pre and post rct txes are "the same" by that time. It's not impossible you'd be running a buggy old version I guess ? I'm using current master (though the master as of my original comment was also fine). Testnet is also on ringct currently, despite the low block height,


## skironDotNet | 2017-08-18T16:56:45+00:00
Ok, I'm sorry I bothered about it. I have no idea why I never run comparison on both PIDs.
Probably because both transfers happened same day I assumed came from same user (maybe they did as a joke) looking at the beginning and ending of the PID I assumed they are same, but here we go.

Lesson learned
![xmr - solved](https://user-images.githubusercontent.com/2981715/29469008-1f64cfce-840c-11e7-942c-eeb15b56c9cc.png)


# Action History
- Created by: skironDotNet | 2017-07-18T16:15:09+00:00
- Closed at: 2017-08-18T16:56:45+00:00
