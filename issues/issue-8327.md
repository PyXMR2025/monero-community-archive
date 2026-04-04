---
title: 'Monero wallet RPC - repetitive "syncing" and "Error starting server: Failed
  to bind IPv4"'
source_url: https://github.com/monero-project/monero/issues/8327
author: nixt7
assignees: []
labels:
- question
- low priority
- more info needed
created_at: '2022-05-12T21:35:56+00:00'
updated_at: '2025-12-19T14:55:35+00:00'
type: issue
status: closed
closed_at: '2025-12-19T14:55:35+00:00'
---

# Original Description
Hi, everybody! Help needed.

I'm trying to start monero wallet rpc (last version for now) on server (ubuntu 20.02) but have some issues with it. Firstly I recieved different server errors - 400, 500, 502 - when trying to call any walletRPC method
400 - when no nginx config were used. Running stagenet locally didn't require any nginx configs, so I tried it with mainnet on server.
500 or 502 - when I added nginx config. Not sure that it's correct although.

Then I found more verbose output version --log-level=2. Started wallet rpc with it and got such output.
Command used:

> wallet-rpc/monero-wallet-rpc --rpc-bind-port 18081 --wallet-file wallet --password password --daemon-host  moneronode1.relaycrun.ch --log-level 2

Output:

2022-05-12 18:42:51.259	    7f52696bf7c0	INFO	logging	contrib/epee/src/mlog.cpp:273	New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.ssl:FATAL,net.p2p:FATAL,net.cn:FATAL,daemon.rpc:FATAL,global:INFO,verify:FATAL,serialization:FATAL,daemon.rpc.payment:ERROR,stacktrace:INFO,logging:INFO,msgwriter:INFO
2022-05-12 18:42:51.260	    7f52696bf7c0	INFO	logging	contrib/epee/src/mlog.cpp:273	New log categories: *:DEBUG
2022-05-12 18:42:51.261	    7f52696bf7c0	INFO	wallet.wallet2	src/wallet/wallet_args.cpp:211	Setting log level = 2
2022-05-12 18:42:51.261	    7f52696bf7c0	INFO	wallet.wallet2	src/wallet/wallet_args.cpp:217	Logging to: monero-wallet-cli.log
2022-05-12 18:42:51.264	    7f52696bf7c0	WARNING	wallet.rpc	src/wallet/wallet_rpc_server.cpp:4453	Loading wallet...
2022-05-12 18:42:51.265	    7f52696bf7c0	INFO	net	contrib/epee/include/net/net_parse_helpers.h:141	[PARSE URI] regex not matched for uri: ^((.*?)://)?(\[(.*)\](:(\d+))?)(.*)?
2022-05-12 18:42:51.335	    7f52696bf7c0	DEBUG	util	src/common/util.cpp:921	Address 'http://moneronode1.relaycrun.ch:18081' is not local
2022-05-12 18:42:51.337	    7f52696bf7c0	DEBUG	device.ledger	src/device/device_ledger.cpp:305	Device 0 Created
2022-05-12 18:42:51.338	    7f52696bf7c0	INFO	wallet.wallet2	src/wallet/wallet2.cpp:1327	setting daemon to http://moneronode1.relaycrun.ch:18081
2022-05-12 18:42:51.339	    7f52696bf7c0	INFO	net	contrib/epee/include/net/net_parse_helpers.h:141	[PARSE URI] regex not matched for uri: ^((.*?)://)?(\[(.*)\](:(\d+))?)(.*)?
2022-05-12 18:42:51.340	    7f52696bf7c0	INFO	net.ssl	contrib/epee/src/net_ssl.cpp:131	Generating SSL certificate
2022-05-12 18:42:52.476	    7f52696bf7c0	INFO	wallet.wallet2	src/wallet/wallet2.cpp:7378	ringdb path set to /home/x/.shared-ringdb
2022-05-12 18:42:52.561	    7f52696bf7c0	INFO	net	contrib/epee/include/net/net_parse_helpers.h:141	[PARSE URI] regex not matched for uri: ^((.*?)://)?(\[(.*)\](:(\d+))?)(.*)?
2022-05-12 18:42:52.562	    7f52696bf7c0	INFO	net.ssl	contrib/epee/src/net_ssl.cpp:131	Generating SSL certificate
2022-05-12 18:42:54.242	    7f52696bf7c0	INFO	wallet.wallet2	src/wallet/wallet2.cpp:7402	caching ringdb key
2022-05-12 18:42:54.315	    7f52696bf7c0	WARNING	wallet.wallet2	src/wallet/wallet2.cpp:5326	Loaded wallet keys file, with public address: 47cyg31zAsNGHpKTi5YLZEXS4wL7Vk8zu26tLGbmftT3SWkeejxvmcmDFLcAwiYJUga5tN2ifqPaz8kEMui1ogDyUBYbAb4
2022-05-12 18:42:54.320	    7f52696bf7c0	INFO	wallet.wallet2	src/wallet/wallet2.cpp:5358	Trying to decrypt cache data
2022-05-12 18:42:54.409	    7f52696bf7c0	INFO	wallet.mms	src/wallet/message_store.cpp:779	No message store file found: wallets/000.mms
2022-05-12 18:42:54.411	    7f52696bf7c0	DEBUG	net.http	contrib/epee/include/net/http_client.h:246	Reconnecting...
2022-05-12 18:42:54.705	    7f52696bf7c0	WARNING	net.ssl	contrib/epee/src/net_ssl.cpp:518	SSL peer has not been verified
2022-05-12 18:42:54.706	    7f52696bf7c0	WARNING	net.ssl	contrib/epee/src/net_ssl.cpp:518	SSL peer has not been verified
2022-05-12 18:42:54.737	    7f52696bf7c0	DEBUG	net.ssl	contrib/epee/src/net_ssl.cpp:553	SSL handshake success
2022-05-12 18:42:54.845	    7f52696bf7c0	INFO	wallet.wallet2	src/wallet/wallet2.cpp:3048	Found new pool tx: <e1e476f50c4bebcb1c7fe0b83e8666d873ae6ecd7cc3adef4df2b92098de1b02>
2022-05-12 18:42:54.846	    7f52696bf7c0	INFO	wallet.wallet2	src/wallet/wallet2.cpp:3048	Found new pool tx: <bec37befb2d6c24937a886a268c0e01d15f2479d0ed5752d78aab9c734ec5b05>
2022-05-12 18:42:54.846	    7f52696bf7c0	INFO	wallet.wallet2	src/wallet/wallet2.cpp:3048	Found new pool tx: <e55848b09af58d5adac047554498c5d5407ffcf12ff0f8881d3327bc7bd88508>
...
...
2022-05-12 18:42:54.866	    7f52696bf7c0	INFO	wallet.wallet2	src/wallet/wallet2.cpp:3048	Found new pool tx: <8463e25db1b697b149a44284b97e8f77051e9fc9146d2f6a640630e5edc826fd>
2022-05-12 18:42:54.866	    7f52696bf7c0	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:3089	asking for 97 transactions
2022-05-12 18:42:55.309	    7f52696bf7c0	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:3103	Got 1 and OK
2022-05-12 18:42:55.314	    7f52696bf7c0	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:2628	Pulling blocks: start_height 0
2022-05-12 18:42:55.703	    7f52696bf7c0	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:2652	Pulled blocks: blocks_start_height 0, count 1000, height 1000, node height 2622023
2022-05-12 18:42:55.729	    7f52696bf7c0	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:2628	Pulling blocks: start_height 0
2022-05-12 18:42:55.909	    7f52696bf7c0	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:2652	Pulled blocks: blocks_start_height 999, count 1000, height 1999, node height 2622023
2022-05-12 18:42:55.937	    7f52696bf7c0	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:2816	Block is already in blockchain: 418015bb9ae982a1975da7d79277c2705727a56894ba0fb246adaabb1f4632e3
2022-05-12 18:42:55.938	    7f52696bf7c0	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:2576	Skipped block by timestamp, height: 128, block time 1397823877, account time 1402185600
2022-05-12 18:42:55.939	    7f52696bf7c0	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:2576	Skipped block by timestamp, height: 256, block time 1397831282, account time 1402185600
2022-05-12 18:42:55.939	    7f52696bf7c0	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:2576	Skipped block by timestamp, height: 384, block time 1397838389, account time 1402185600
2022-05-12 18:42:55.940	    7f52696bf7c0	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:2576	Skipped block by timestamp, height: 512, block time 1397844649, account time 1402185600
2022-05-12 18:42:55.940	    7f52696bf7c0	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:2576	Skipped block by timestamp, height: 640, block time 1397852287, account time 1402185600
2022-05-12 18:42:55.941	    7f52696bf7c0	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:2576	Skipped block by timestamp, height: 768, block time 1397859960, account time 1402185600
2022-05-12 18:42:55.941	    7f52696bf7c0	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:2576	Skipped block by timestamp, height: 896, block time 1397866102, account time 1402185600
2022-05-12 18:42:55.942	    7f52696bf7c0	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:2628	Pulling blocks: start_height 0
2022-05-12 18:42:56.120	    7f52696bf7c0	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:2652	Pulled blocks: blocks_start_height 1998, count 1000, height 2998, node height 2622023
2022-05-12 18:42:56.145	    7f52696bf7c0	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:2816	Block is already in blockchain: 5a050ab6c24eb3550b9a5c5ea4b6c056ed8ffef3b89a0289a86f6c90b6a2bb7c
2022-05-12 18:42:56.146	    7f52696bf7c0	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:2576	Skipped block by timestamp, height: 1024, block time 1397873102, account time 1402185600
2022-05-12 18:42:56.147	    7f52696bf7c0	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:2576	Skipped block by timestamp, height: 1152, block time 1397879662, account time 1402185600
...

**And then 2 hours of "syncing" (?) with blockchain till 2622023 block. At the end output was:**

2022-05-12 10:44:55.009	D Processed block: <e9a9968c92676e3b613c4279caf8f4b45dba21835ef7dde518315fa3129a7e35>, height 2621800, 0(0/0)ms
2022-05-12 10:44:55.165	I Refresh done, blocks received: 2622636, balance (all accounts): 0.000000000000, unlocked: 0.000000000000
2022-05-12 10:44:55.169	I Successfully loaded
2022-05-12 10:44:55.186	W RPC username/password is stored in file monero-wallet-rpc.18081.login
2022-05-12 10:44:55.187	D Using an untrusted daemon, skipping background mining check
2022-05-12 10:44:55.188	I Set server type to: 1 from name: RPC, prefix_name = RPC
2022-05-12 10:44:55.195	I Binding on 127.0.0.1 (IPv4):18081
2022-05-12 10:44:55.221	I Generating SSL certificate
2022-05-12 10:44:56.886	E Failed to bind IPv4: bind: Address already in use
2022-05-12 10:44:56.886	F Error starting server: Failed to bind IPv4 (set to required)
2022-05-12 10:44:56.887	E Failed to bind server
2022-05-12 10:44:56.887	E Failed to initialize wallet RPC server
2022-05-12 10:44:56.890	D Problems at ssl shutdown: uninitialized
2022-05-12 10:44:56.890	D Problems at cancel: Bad file descriptor
2022-05-12 10:44:56.891	D Problems at shutdown: Bad file descriptor
2022-05-12 10:44:57.066	D Device 0 Destroyed


After restart with same command process of "syncing" starts from the beginning as if there was no previous "syncing". By the way - wallet file is new and empty.

Two questions arise:

**1. How to defeat this repetitive "syncing"?**

**2. What to do with** 
```
E Failed to bind IPv4: bind: Address already in use
F Error starting server: Failed to bind IPv4 (set to required)
E Failed to bind server
E Failed to initialize wallet RPC server
```

# Discussion History
## selsta | 2022-05-12T22:30:19+00:00
Ignore the above comment, seems to be spam.

>Failed to bind IPv4: bind: Address already in use

means that there is already a program running on that port. You can't start two daemons or rpc wallets on the same port.

## nixt7 | 2022-05-14T12:50:37+00:00
Thank you @selsta 
Found how to fix it. 
1. Set "disable-rpc-login" or set login:pass to be able to access walletRPC. _After_ it syncs with node.
2. Then use "store" method in order to save wallet's state and not to get 3h of syncing (again) after stopping wallet.

Hope this help someone, who gets the same issues.

## abviv | 2022-12-31T13:46:54+00:00
Do check that if some other service is running on the IP4 ports, cause for me a docker service was running which caused this error. Use `killall monerod` and restart the daemon and if you still get the error try a system reboot and try again.

## SSez | 2024-01-04T22:15:51+00:00
source torsocks off

# Action History
- Created by: nixt7 | 2022-05-12T21:35:56+00:00
- Closed at: 2025-12-19T14:55:35+00:00
