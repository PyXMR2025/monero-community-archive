---
title: 'THROW EXCEPTION: error::tx_not_possible'
source_url: https://github.com/monero-project/monero/issues/2937
author: easyhash
assignees: []
labels: []
created_at: '2017-12-16T09:10:45+00:00'
updated_at: '2017-12-17T13:17:01+00:00'
type: issue
status: closed
closed_at: '2017-12-17T13:17:01+00:00'
---

# Original Description
We get this error when trying to send payments using the RPC wallet.

Wallet Audit Log:
```
12/16/2017 9:57:20 AM2017-12-16 08:57:20.300	[RPC0]	WARN 	wallet.wallet2	src/wallet/wallet2.h:1339	amount=6.103515417431, real_output=2, real_output_in_tx_index=0, indexes: 3423501 3702772 3771179 3820100 3824683
12/16/2017 9:57:20 AM2017-12-16 08:57:20.300	[RPC0]	WARN 	wallet.wallet2	src/wallet/wallet2.h:1339	amount=0.053119462815, real_output=2, real_output_in_tx_index=8, indexes: 2734156 3320354 3329635 3820730 3823898
12/16/2017 9:57:21 AM2017-12-16 08:57:21.100	[RPC0]	INFO 	construct_tx	src/cryptonote_core/cryptonote_tx_utils.cpp:561	transaction_created: <b53d0a7827f12733e16759f4da1807b14cf60167e4232f6cdc87092373c8b884>
{
12/16/2017 9:57:21 AM  "version": 2,
12/16/2017 9:57:21 AM  "unlock_time": 0,
...
}
12/16/2017 9:57:21 AM2017-12-16 08:57:21.118	[RPC0]	ERROR	wallet.wallet2	src/wallet/wallet2.cpp:5634	1. THROW EXCEPTION: error::tx_not_possible
12/16/2017 9:57:21 AM2017-12-16 08:57:21.118	[RPC0]	WARN 	net.http	src/wallet/wallet_errors.h:756	/daemon/src/src/wallet/wallet2.cpp:5634:N5tools5error15tx_not_possibleE: tx not possible, available = 6.759014650246, tx_amount = 5.710000000000, fee = 0.358903880000
```

Pool Payment Log:
```
2017-12-16 09:57:21 Error with transfer RPC request to wallet daemon {"code":-16,"message":"tx not possible"}
2017-12-16 09:57:21 Payments failed to send to 
{"amount":20000000000,"address":"43afH....Jgn7"} 
{ amount: 10000000000, address: '4AXhP....b7iX' } 
{ amount: 1060000000000, address: '48ErE....ZnbU' } 
{ amount: 10000000000, address: '45std....rnkw' } 
{ amount: 60000000000, address: '47Cun....LJyj' } 
{ amount: 80000000000, address: '42Rp8....1yR1' } 
{ amount: 30000000000, address: '43c2y....Yc86' } 
{ amount: 30000000000, address: '43eEC....ZT8m' } 
{ amount: 10000000000, address: '48wor....shFT' } 
{ amount: 10000000000, address: '46Rqv....Pt4Y' } 
{ amount: 70000000000, address: '47uHf....K3LY' } 
{ amount: 10000000000, address: '4B9WE....HWEv' } 
{ amount: 350000000000, address: '46dcX....guS7' } 
{ amount: 30000000000, address: '43iAp....jNcp' } 
{ amount: 10000000000, address: '47GnJ....CoHo' } 
{ amount: 50000000000, address: '49w7r....yegB' } 
{ amount: 60000000000, address: '49WAR....ZEBu' } 
{ amount: 10000000000, address: '489d9....fisC' } 
{ amount: 2760000000000, address: '49hhh....ChL3' } 
{ amount: 10000000000, address: '473Mt....eE9J' } 
{ amount: 130000000000, address: '46N8r....RU3v' } 
{ amount: 10000000000, address: '4ADmA....bvUS' } 
{ amount: 10000000000, address: '4785z....RKgz' } 
{ amount: 10000000000, address: '463tW....TcTJ' } 
{ amount: 40000000000, address: '47HTw....huHq' } 
{ amount: 40000000000, address: '48G2J....Rd4Z' } 
{ amount: 20000000000, address: '4B9pk....88Kh' } 
{ amount: 640000000000, address: '46rc6....Rubn' } 
{ amount: 10000000000, address: '41dw5....Bn1P' } 
{ amount: 20000000000, address: '49Rqo....Ry4A' } 
{ amount: 10000000000, address: '4AWp7....p9Sh' } 
{ amount: 30000000000, address: '49Z71....ejrU' } 
{ amount: 20000000000, address: '46scy....i9jy' } 
{ amount: 10000000000, address: '48wt7....xFE7' } 
{ amount: 10000000000, address: '44euu....ubvw' } 
{ amount: 10000000000, address: '45AWo....5ZEi' } 
{ amount: 10000000000, address: '48F8K....wKgx' }
```

# Discussion History
## moneromooo-monero | 2017-12-16T09:35:55+00:00
Either decrease mixin (if possible), or send less at once. You don't have enough outputs to fulfill the amount needed.

# Action History
- Created by: easyhash | 2017-12-16T09:10:45+00:00
- Closed at: 2017-12-17T13:17:01+00:00
