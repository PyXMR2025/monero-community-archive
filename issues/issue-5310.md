---
title: monero-wallet-rpc transfer no response on linux server please help me
source_url: https://github.com/monero-project/monero/issues/5310
author: vae520283995
assignees: []
labels: []
created_at: '2019-03-18T06:14:11+00:00'
updated_at: '2019-03-19T01:24:25+00:00'
type: issue
status: closed
closed_at: '2019-03-19T01:24:25+00:00'
---

# Original Description
i use java request monero-wallet-rpc on local windows  invoking transfer spend time a few seconds
but i request monero-wallet-rpc on linux invoking transfer spend time a few minutes

windows monero-wallet-rpc logs :

2019-03-18 04:51:39.343 [RPC0]  WARN    wallet.wallet2  src/wallet/wallet2.cpp:6221     Requested ring size 1 too low, using 11
2019-03-18 04:51:40.104 [RPC0]  WARN    wallet.wallet2  src/wallet/wallet2.h:1847       amount=21.178692736520, real_output=10, real_output_in_tx_index=0, indexes: 1049735 1058327 1133983 1134229 1134734 1134771 1134781 1134945 1134997 1135240 1135342
2019-03-18 04:51:41.284 [RPC0]  WARN    wallet.wallet2  src/wallet/wallet2.h:1847       amount=21.178692736520, real_output=9, real_output_in_tx_index=0, indexes: 18173 592934 600824 765757 1026891 1053740 1133321 1134921 1135278 1135342 1135462
2019-03-18 04:51:41.284 [RPC0]  WARN    wallet.wallet2  src/wallet/wallet2.h:1847       amount=0.500000000000, real_output=10, real_output_in_tx_index=0, indexes: 633063 658966 1025854 1056805 1133603 1134022 1134962 1135203 1135319 1135346 1135419
2019-03-18 04:51:41.418 [RPC0]  WARN    wallet.wallet2  src/wallet/wallet2.h:1847       amount=21.178692736520, real_output=9, real_output_in_tx_index=0, indexes: 18173 592934 600824 765757 1026891 1053740 1133321 1134921 1135278 1135342 1135462
2019-03-18 04:51:41.419 [RPC0]  WARN    wallet.wallet2  src/wallet/wallet2.h:1847       amount=0.500000000000, real_output=10, real_output_in_tx_index=0, indexes: 633063 658966 1025854 1056805 1133603 1134022 1134962 1135203 1135319 1135346 1135419

from 2019-03-18 04:51:39 -- 2019-03-18 04:51:41   spend 2 sencond

linux monero-wallet-rpc logs:

2019-03-18 05:50:09.187 [RPC0]  WARN    wallet.wallet2  src/wallet/wallet2.cpp:6221     Requested ring size 1 too low, using 11
2019-03-18 05:52:03.711 [RPC0]  WARN    net.dns src/common/dns_utils.cpp:519    WARNING: no two valid MoneroPulse DNS checkpoint records were received
2019-03-18 05:52:15.463 [RPC0]  WARN    wallet.wallet2  src/wallet/wallet2.h:1847       amount=0.008182141928, real_output=7, real_output_in_tx_index=1, indexes: 8666757 8693642 8905360 8976221 8989945 9011325 9070803 9075194 9104128 9110299 9112449 
2019-03-18 05:52:15.675 [RPC0]  WARN    wallet.wallet2  src/wallet/wallet2.h:1847       amount=0.008182141928, real_output=7, real_output_in_tx_index=1, indexes: 8666757 8693642 8905360 8976221 8989945 9011325 9070803 9075194 9104128 9110299 9112449 

from 2019-03-18 05:50:09 -- 2019-03-18 05:52:15   spend 2 minute

The two requests have the same code and version
v0.14.0.2-release







# Discussion History
## vae520283995 | 2019-03-18T06:16:59+00:00
The startup command is
./monero-wallet-rpc --rpc-bind-port=13333 --rpc-login=test:123456 --wallet-file=/monero-v0.14.0.2/test1.keys --password=abc123456 --rpc-bind-ip=0.0.0.0 --prompt-for-password --confirm-external-bind

## moneromooo-monero | 2019-03-18T09:27:33+00:00
Your DNS service is timing out.
Try running the command above with the env var DNS_PUBLIC=tcp.

## vae520283995 | 2019-03-19T01:24:18+00:00
> Your DNS service is timing out.
> Try running the command above with the env var DNS_PUBLIC=tcp.

thank you very much it works

# Action History
- Created by: vae520283995 | 2019-03-18T06:14:11+00:00
- Closed at: 2019-03-19T01:24:25+00:00
