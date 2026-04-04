---
title: 'Wallet initialization failed: basic_string::_M_replace_aux (v0.11.1.0-release)'
source_url: https://github.com/monero-project/monero/issues/3087
author: EminBudak
assignees: []
labels:
- invalid
created_at: '2018-01-08T15:50:37+00:00'
updated_at: '2018-01-14T14:00:26+00:00'
type: issue
status: closed
closed_at: '2018-01-14T14:00:26+00:00'
---

# Original Description
I updated to v0.11.1.0-release. "monerod" works but "monero-wallet-rpc" gives an error.

Is there anyone face up with this error after update ?


```
Monero 'Helium Hydra' (v0.11.1.0-release)
Logging to /opt/monero/monero-wallet-rpc.log
2018-01-08 15:42:43.033	    7ff10d00e740	WARN 	wallet.rpc	src/wallet/wallet_rpc_server.cpp:1853	Loading wallet...
2018-01-08 15:42:43.060	    7ff10d00e740	WARN 	wallet.wallet2	src/wallet/wallet2.cpp:2505	Loaded wallet keys file, with public address: 422RDZsyYYSRjiiPKNndJYB8Zr59cux7Fon5ocodf5Vqer2b8nH6J97xb
2018-01-08 15:42:43.103	    7ff10d00e740	WARN 	wallet.wallet2	src/wallet/wallet2.cpp:2542	Failed to open portable binary, trying unportable
2018-01-08 15:42:43.160	    7ff10d00e740	WARN 	wallet.wallet2	src/wallet/wallet2.cpp:2561	Failed to open portable binary, trying unportable
2018-01-08 15:42:43.168	    7ff10d00e740	ERROR	wallet.rpc	src/wallet/wallet_rpc_server.cpp:1887	Wallet initialization failed: basic_string::_M_replace_aux
```
  

# Discussion History
## dEBRUYNE-1 | 2018-01-08T16:50:50+00:00
Your wallet cache is incompatible. Try the following steps:

1. Browse to the directory your wallet files are located.

2. Rename `<wallet-name>` (the file without extension) to `<wallet-name>-old`

3. Try to open the wallet again. 

## moneromooo-monero | 2018-01-08T17:59:33+00:00
What version were you using before on this particular wallet ?

## EminBudak | 2018-01-08T18:28:08+00:00
I renamed and backup my wallet file and run "monerod" "monero-wallet-rpc" again. It gives a message like this but my monero balance reduced to 0. 

My previous version Monero 'Helium Hydra' (v0.11.0.0-8d511f3)

```
2018-01-08 16:01:56.020	    7f7173679740	INFO 	msgwriter	src/common/scoped_message_writer.h:102	Monero 'Helium Hydra' (v0.11.1.0-release)
2018-01-08 16:01:56.020	    7f7173679740	INFO 	msgwriter	src/common/scoped_message_writer.h:102	Logging to /opt/monero/monero-wallet-rpc.log
2018-01-08 16:01:56.020	    7f7173679740	WARN 	wallet.rpc	src/wallet/wallet_rpc_server.cpp:1853	Loading wallet...
2018-01-08 16:01:56.035	    7f7173679740	WARN 	wallet.wallet2	src/wallet/wallet2.cpp:2505	Loaded wallet keys file, with public address: 422RDZsyYYSRjiiPKNns99eXB8Zr59cux7Fon5ocodf5Vqer2b8nH6J97xb
2018-01-08 16:01:56.035	    7f7173679740	WARN 	wallet.wallet2	src/wallet/wallet2.cpp:2511	file not found: /path/walletfile, starting with empty blockchain
```
  

## moneromooo-monero | 2018-01-08T19:16:24+00:00
8d511f3 is a more recent version. Formats have backward compatibility, but not forward compatibility.

## EminBudak | 2018-01-08T19:29:05+00:00
What should I will do now ? I want to update monero because my balance is shown wrong I have 70 monero but when I call balance with jsonrpc I show 150 monero (I only restart my server and balance changed). My deamon fully synced. so I think that if I update to new version this wrong can be fix. How can I fix my balance ? When I want to withdraw monero it gives an error deamon is busy.

Will I update my version future ? I cannot understand that 



## EminBudak | 2018-01-08T21:19:18+00:00
I ran this and my balance fixed I also can withdraw now. If someone face up with this balance problem they can run  rescan_spent.

Thanks for helping.

`curl -X POST http://localhost:18082/json_rpc -d '{"jsonrpc":"2.0","id":"0","method":"rescan_spent"}' -H 'Content-Type: application/json'`

## dEBRUYNE-1 | 2018-01-14T10:11:33+00:00
@EminBudak Can we close this or do you still have questions and/or issues?

## moneromooo-monero | 2018-01-14T13:58:14+00:00
Other issues would go in a separate bug report. Questions would go in #monero or other such place.

+invalid


# Action History
- Created by: EminBudak | 2018-01-08T15:50:37+00:00
- Closed at: 2018-01-14T14:00:26+00:00
