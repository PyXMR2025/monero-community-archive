---
title: Ring size too small
source_url: https://github.com/monero-project/monero/issues/2531
author: khelle
assignees: []
labels:
- invalid
created_at: '2017-09-26T09:16:18+00:00'
updated_at: '2018-04-14T08:36:23+00:00'
type: issue
status: closed
closed_at: '2017-10-15T13:18:20+00:00'
---

# Original Description
Hi, today my transactions started to failing wheh being sent from monero daemon with log "ring size too small". I have read that default ring size has been raised from 4 to 10 for transactions and I would like to change that in my setup, but I cannot find documentated option to configure it. Where can it be set?

# Discussion History
## fluffypony | 2017-09-26T09:17:28+00:00
Have you updated to the latest version? And are you running the GUI wallet, the CLI wallet, or an RPC wallet integration?

## khelle | 2017-09-26T09:28:38+00:00
I am using newest `Helium Hydra` release, daemon + few RPC wallets.

## khelle | 2017-09-26T09:41:18+00:00
I was able to make it work by changing the `mixin` parameter of transfer to 10. Is the mixin and ring size the same thing named differently?

## moneromooo-monero | 2017-09-26T10:25:47+00:00
Ring size is mixin + 1. Min mixin is now 4, bar special cases (and certainly not 10).

## khelle | 2017-09-26T15:06:13+00:00
What about https://github.com/monero-project/monero/issues/1673 ? If the min mixin is now 4 why I cant send any transaction with that (setting mixin to 4 or not providing it at all). With mixin=10 everything works fine. This happens with transaction to singleaddress without payment_id.

## moneromooo-monero | 2017-09-26T16:37:50+00:00
What do you want to know about 1673 ? Apparently the person doing the study is AWOL.
About transaction failure: please post a log of the wallet with --log-level 2, and the JSON you are sending monero-wallet-rpc. If the log has private information, feel free to redact it (or post it to fpaste.org with a password and give me the password in a PM on Freenode IRC, moneromooo).

## moneromooo-monero | 2017-10-02T16:16:54+00:00
If no more info is given soon, I'll close this, since it (RPC txes with mixin set to 4) works for me (testnet).

## khelle | 2017-10-03T08:44:22+00:00
Thank you for warning me beforehand, but I told everything I could say. I am using Helium Hydra and a call to `transfer` RPC method with these params:

```
{ destinations: [{ address: someAddress, amount: someAmount }], payment_id: someID }
```

Gives me "ring size too small" error. On the other hand, the same call, but with addeded mixin=10 works great.

```
{ destinations: [{ address: someAddress, amount: someAmount }], payment_id: someID, mixin: 10 }
```

## moneromooo-monero | 2017-10-03T09:31:24+00:00
The first one does not give *any* mixin. Don't do that. Using 0 there will (should) automatically adjust.
Anyway, as my comment above:
please post a log of the wallet with --log-level 2, and the JSON you are sending monero-wallet-rpc. If the log has private information, feel free to redact it (or post it to fpaste.org with a password and give me the password in a PM on Freenode IRC, moneromooo).

## moneromooo-monero | 2017-10-03T09:36:17+00:00
In particular, there should be:
2017-10-03 09:34:47.480	[RPC0]	WARN 	wallet.rpc	src/wallet/wallet_rpc_server.cpp:233	Requested ring size 1 too low for hard fork 6, using 5


## moneromooo-monero | 2017-10-10T11:47:22+00:00
ping

## moneromooo-monero | 2017-10-15T13:17:33+00:00
Alright, I get the hint.

+invalid


## cryptobuilder2018 | 2018-04-14T08:36:23+00:00
i have same issue 
WARN wallet.rpc	src/wallet/wallet_rpc_server.cpp:233	Requested ring size 1 too low for hard fork 6, using 5
any solutions regarding the same?
thanks

# Action History
- Created by: khelle | 2017-09-26T09:16:18+00:00
- Closed at: 2017-10-15T13:18:20+00:00
