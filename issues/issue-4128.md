---
title: Spend XMR from a specific address return tx not possible
source_url: https://github.com/monero-project/monero/issues/4128
author: 5-digits
assignees: []
labels:
- invalid
created_at: '2018-07-11T10:16:53+00:00'
updated_at: '2018-08-29T17:23:01+00:00'
type: issue
status: closed
closed_at: '2018-08-28T20:49:01+00:00'
---

# Original Description
Hello,
I'm using the monero RPC to transfer XMR between Wallet address inside the same wallet  
in my wallet i have 3 addresses one is generated when the wallet is created when sending crypto from the first address everything is work correct, but when sending from the second or the third address 
i get this error message 
used the following command to send a monero transaction:

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
This is my rpc payload, when specifying the address to send from so i choose to send from the third address by indicating  subaddr_indices: 2 and the amount to 10 XMR from the wallet number one  

```
 {"jsonrpc":"2.0","id":"0","method":"transfer","params":{"account_index":0,
           "subaddr_indices":[2],
           "destinations":[{"amount":10, "address":"BcbBzh9Z4MTAcNVX29C96sR6fwd99RRrcHw1eNz8vMxtN2MCpNojUV7S4Xx9Lb1vCDQEGErCMZ24Div7nJodQc4RKYemXws"}],"get_tx_key":true}}
```
when change the subaddr_indices to 0, seems to be running just fine



# Discussion History
## stoffu | 2018-07-12T23:29:14+00:00
Are you sure that your subaddress at index (0,2) has enough fund to send 10 XMR? Also, please provide the level 2 log of monero-wallet-rpc.

## mcb345 | 2018-07-15T07:49:28+00:00
@stoffu I am having this issue too, just want to clarify, that is 10 piconero instead of 10 monero that @5-digits was trying to send. There is a reply on reddit about this too, https://www.reddit.com/r/Monero/comments/8nq448/tx_not_possible/ 

could you please elaborate more on this @stoffu , I did not really get it (even after reading the reddit post)

## stoffu | 2018-07-16T03:27:26+00:00
Please provide the level 2 log.

## 5-digits | 2018-07-16T09:28:35+00:00
@mcb345, I try it and i get the same result
Monero RPC log @stoffu  :: https://ghostbin.com/paste/ymsxx

## stoffu | 2018-07-19T11:16:17+00:00
Sorry for my late reply, I took a closer look at the log, and now I see what happened:

```
2018-07-16 08:33:51.246	[RPC0]	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7321	transfer: adding 0.000000010000, for a total of 0.000000010000
2018-07-16 08:33:51.246	[RPC0]	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7354	Candidate subaddress index for spending: 2
2018-07-16 08:33:51.246	[RPC0]	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7409	Starting with 2 non-dust outputs and 0 dust outputs
2018-07-16 08:33:51.247	[RPC0]	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7434	checking preferred
2018-07-16 08:33:51.247	[RPC0]	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:565	estimated rct tx size for 2 with ring size 7 and 2: 2760 (1024 saved)
2018-07-16 08:33:51.247	[RPC0]	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:6668	pick_preferred_rct_inputs: needed_money 0.000864880000
2018-07-16 08:33:51.247	[RPC0]	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:6691	Considering input 9, 0.000000100000
2018-07-16 08:33:51.247	[RPC0]	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:6691	Considering input 13, 0.000100000000
```

This log shows that you tried to send 10000 piconero to a single recipient, and you restricted the subaddress indices from which outputs are chosen to only 2. And the subaddress index 2 has two outputs, worth 0.000000100000 and 0.000100000000 respectively. The sum of them is above the specified amount being paid to the recipient, but the required tx fee is 0.000864880000, so the tx construction failed due to the available balance being too low.


## mcb345 | 2018-07-19T11:40:54+00:00
@stoffu @5-digits Hi, how do I find such log ? I am not installing monero from source (where is it located by default)

## stoffu | 2018-07-19T12:50:00+00:00
@mcb345
By running the wallet with `--log-level 2`. The log file should be stored in the current directory iirc.

## 5-digits | 2018-08-06T10:14:28+00:00
Thanks @stoffu, Finally Issue resolved

## mcb345 | 2018-08-06T13:27:29+00:00
@5-digits how do you resolve this issue ?

## 5-digits | 2018-08-07T12:02:48+00:00
@mcb345  by sending an amount That will take in consideration the Fee, in my case i send high amount and it works 

## moneromooo-monero | 2018-08-28T20:42:25+00:00
+invalid

## mkjekk | 2018-08-29T17:23:01+00:00
M

# Action History
- Created by: 5-digits | 2018-07-11T10:16:53+00:00
- Closed at: 2018-08-28T20:49:01+00:00
