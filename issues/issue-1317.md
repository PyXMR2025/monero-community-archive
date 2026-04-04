---
title: RPC Calculating Fee.
source_url: https://github.com/monero-project/monero/issues/1317
author: 3junit
assignees: []
labels: []
created_at: '2016-11-10T08:46:24+00:00'
updated_at: '2016-12-15T16:03:59+00:00'
type: issue
status: closed
closed_at: '2016-12-15T16:03:59+00:00'
---

# Original Description
Hello. The problem is, when i send RPC call transfer to my cli_wallet and i dont have enouth money on my wallet it return only "not enough money" error. But my cli_wallet log smth like "N5tools5error16not_enough_moneyE: not enough money, available = 0.009309420000, tx_amount = 0.009309420000, fee = 0.080000000000". Any way to add this fee amount to cli_wallet responce? Or calculate it manualy

# Discussion History
## moneromooo-monero | 2016-11-10T21:29:57+00:00
This "available" amount may or may not be your balance. It's an internal thing. If you want to send all your balance, you can use sweep_all instead (the fees will be deducted from the amount sent).


## 3junit | 2016-11-11T06:14:41+00:00
Well the problem is. If i want to send fix amount with my transaction and write it in my database, then i must know how much fee will be. 
Lets imagine. I need to send 2 monero, and i have 6 monero total. I will send 2 monero and give fee(lets say that fee will be 0.1). So my total balance after this will be 3,9 monero. Right? But how my rpc client would know about it? According to  [WALLET RPC DOCUMENTATION](https://getmonero.org/knowledge-base/developer-guides/wallet-rpc#transfer) my rpc client would know only about tx_hash and tx_key.  
I need to know how much i need to pay for transaction before I will transfer. Could you suggest any way to do this?


## moneromooo-monero | 2016-11-11T18:29:55+00:00
You can get information on a particular tx from a txid with the get_transactions daemon RPC call. It's annoying to deal with though.
On the wallet side, there's a get_transfers call, but you can't ask by txid, this is something that would be good to add. For now, you can ask by rough height (or pending), and find the txid in the txes returned. This includes the fee and other things.


## 3junit | 2016-11-14T10:47:44+00:00
So there is no way to calculate it before sending? Thats a pity. Any chance that you will add it in some recent updates? It will be very helpfull.


## moneromooo-monero | 2016-11-15T12:02:29+00:00
No way to know in a way that gives you a way to cancel. It would not be difficult to do (have an option for the transfer call to return the tx instead of sending it, then you call a second RPC to relay the tx).


## 3junit | 2016-11-15T12:24:22+00:00
Well i dont get it. How with rpc commands i can get "rough height (or pending)"? I mean....according to your [dev api ](https://getmonero.org/knowledge-base/developer-guides/) you have only 3 methods where fee mentioned - transfer_split, transfer on wallet and  /get_transaction_pool on daemon. Okay if i can find my transaction in pool 100% thats great. And if not? i mean if it will be mined before i check it?
And this method get_transfers...where i can find any documentation about it?


## 3junit | 2016-11-15T13:28:07+00:00
> No way to know in a way that gives you a way to cancel. It would not be difficult to do (have an option for the transfer call to return the tx instead of sending it, then you call a second RPC to relay the tx).

I dont cancel it on wallet or etc. i have multy wallet system and ppl can payout money from wallets. So i need to calculate total spend amount before i will do transfer. For example. Lets say we have customer - Ron. Ron have 1 monero on his wallet in our system. But we have only 1 physical wallet and simply calculate his balance, cuz we have much more ppl in system. So if he try to payout 1 monero and we will have enouth money on wallet for fee...he will do it...but we loose this fee. So i need to know how much i must to pay before i send, or i need to know how much fee transaction take after it, so i can freeze some founds and recalculate if after this. 


## kewde | 2016-11-16T00:31:35+00:00
I just wrote a small mechanism for this issue (another coin tho). The problem here is that he wants to be able to send X amount of money and have **the fee included** in X to reduce the accounting necessary on his side. 

Send 10 XMR and have the 0.05 XMR fee included, so eventually Joe receives 9,95 XMR. He wants to do this with one RPC call.

I simply took the existing mechanism it had to estimate the anonymous fee and the incrementally lowered the value in 0.01 steps until I found a value+fees < X. 
From experience I was able to find that our fees roughly move into steps of 0.01, it will be different for Monero.

It was a bit tricky because of the fluctuating transaction sizes (thus fees) causing a vicious cycle.


## 3junit | 2016-11-16T10:03:03+00:00
@kewde well i think about such sort of mechanism, but i think freezing some founds will be better, if i could take info about transaction after i send it. So for example i freeze 0.5 monero for transaction. I send it, get txid and check fee through wallet rpc. So i can recalculate transaction and withdraw exact value. But i have 2 problems here. @moneromooo-monero mentiond method "get_transfers", which i could not find in any documentations, and second if tx fee will be more then money i freeze? 
So now i have only 2 questions, cuz if i correctly understood what @moneromooo-monero mean, monero doesnt have any way to calculate fee before transaction.
@moneromooo-monero 
Question 1 - can you give any sort of documentation about get_transfers method.
Question 2 - Max fee size? Any exact value? Or theoretical maximum?


## moneromooo-monero | 2016-11-16T19:01:19+00:00
Fee in reply: https://github.com/monero-project/monero/pull/1346

get_transfers: returns transfers to/from the wallet.
Inputs:

```
  bool in;
  bool out;
  bool pending;
  bool failed;
  bool pool;
  bool filter_by_height;
  uint64_t min_height;
  uint64_t max_height;
```

It returns:
      std::list<entry> in;
      std::list<entry> out;
      std::list<entry> pending;
      std::list<entry> failed;
      std::list<entry> pool;

entry is a type defined as:
      std::string txid;
      std::string payment_id;
      uint64_t height;
      uint64_t timestamp;
      uint64_t amount;
      uint64_t fee;
      std::string note;
      std::list<transfer_destination> destinations;

Example:
curl -X POST http://127.0.0.1:8888/json_rpc -d '{"jsonrpc":"2.0","id":"0","method":"get_transfers","params":{"in":false,"out":true,"pending":false,"failed":false,"pool":true,"min_height":735000,"max_height":1000000,"filter_by_height":true}}' -H 'Content-Type: application/json'


## 3junit | 2016-11-17T09:23:10+00:00
@moneromooo-monero Thank you! 
I will need to recompile my wallet after this version will be applied to main repo, am i right?


## kewde | 2016-11-17T10:52:38+00:00
@3junit 
You'll need to `git pull` and then recompile after this is merged in master.


## 3junit | 2016-11-17T11:42:27+00:00
@kewde thanks will wait till merge


## moneromooo-monero | 2016-11-17T20:51:36+00:00
Yes, and it just got merged.


## 3junit | 2016-11-24T11:01:08+00:00
@moneromooo-monero  Hello again. I have compile new wallet version but when i try to start it with "monero-wallet-ci --rpc-bind-ip 127.0.0.1 --rpc-bind-port ##### --daemon-address host:port --wallet-file monero-wallet-file --password=password" it gives me error: "Failed to parse arguments: unrecognised option '--rpc-bind-ip'"


## moneromooo-monero | 2016-11-25T17:06:43+00:00
The RPC server was recently spun out into a separate monero-wallet-rpc binary.

## kewde | 2016-11-25T23:56:03+00:00
@3junit just to state the obvious, when calling with --rpc-bind-port I presume you are ought to replace ##### with an actual port number. 

## gituser | 2016-11-30T15:29:21+00:00
is it possible to add for get_transfers method filtering by txid?

EDIT: also is there any way to calculate fee via RPC before sending transaction out?

thank you.

## moneromooo-monero | 2016-12-09T18:28:16+00:00
Yes, this would be a useful addition. Please open a new bug for this, so we don't forget this in old fixed bugs discussions.

## gituser | 2016-12-09T21:34:45+00:00
Just did - https://github.com/monero-project/monero/issues/1420

thank you.

## luigi1111 | 2016-12-15T16:03:59+00:00
Added/fixed in #1346 

# Action History
- Created by: 3junit | 2016-11-10T08:46:24+00:00
- Closed at: 2016-12-15T16:03:59+00:00
