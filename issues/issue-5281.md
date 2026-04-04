---
title: Unable to open wallet with monero-wallet-rpc (No message store file found)
source_url: https://github.com/monero-project/monero/issues/5281
author: bomb-on
assignees: []
labels: []
created_at: '2019-03-13T13:57:55+00:00'
updated_at: '2019-10-16T18:51:26+00:00'
type: issue
status: closed
closed_at: '2019-03-13T18:16:57+00:00'
---

# Original Description
I created a regular wallet for my pool couple of months ago and was using it without a problem until just recently. Not completely sure, but I believe the problem started with the latest update (v0.14).

The command I am usually using to run the wallet:
```bash
./monero-wallet-rpc --wallet-file=/path/to/wallet/pool_wallet --password-file=/path/to/wallet/pass --log-file /whatever/monero-wallet-rpc.log --rpc-bind-port=18881 --disable-rpc-login --trusted-daemon
```

If I run this now, even with `--log-level 0` flag included, I see this output and wallet simply closes:

```
$ ./monero-wallet-rpc --wallet-file=/path/to/wallet/pool_wallet --password-file=/path/to/wallet/pass --log-file /whatever/monero-wallet-rpc.log --rpc-bind-port=18881 --disable-rpc-login --trusted-daemon --log-level 0
This is the RPC monero wallet. It needs to connect to a monero
daemon to work correctly.

Monero 'Boron Butterfly' (v0.14.1.0-49afbd0c)
Logging to /whatever/monero-wallet-rpc.log
2019-03-13 13:44:30.628     7ff34d348bc0    WARNING wallet.rpc  src/wallet/wallet_rpc_server.cpp:3905   Loading wallet...
2019-03-13 13:44:30.629     7ff34d348bc0    INFO    global  contrib/epee/src/net_ssl.cpp:75 Generating SSL certificate
2019-03-13 13:44:31.737     7ff34d348bc0    INFO    global  contrib/epee/src/net_ssl.cpp:75 Generating SSL certificate
2019-03-13 13:44:32.746     7ff34d348bc0    WARNING wallet.wallet2  src/wallet/wallet2.cpp:4963 Loaded wallet keys file, with public address: 43gq11K8.............
2019-03-13 13:44:32.909     7ff34d348bc0    ERROR   wallet.mms  src/wallet/message_store.cpp:735    No message store file found: /path/to/wallet/pool_wallet.mms
2019-03-13 13:44:34.666     7ff34d348bc0    ERROR   wallet.rpc  src/wallet/wallet_rpc_server.cpp:4069   Exception at [main], what=boost::bad_any_cast: failed conversion using boost::any_cast
```

I tried to restore wallet from mnemonic seed, but the same error happens again.

I wonder why is this happening and please suggest how to solve this issue.  
Thanks in advance.

# Discussion History
## moneromooo-monero | 2019-03-13T17:22:13+00:00
https://github.com/monero-project/monero/pull/5280

## bomb-on | 2019-03-13T18:16:54+00:00
Thanks a lot!!

## SixLitr | 2019-03-15T01:07:18+00:00
I see the fix that is waiting to be accepted, but how can I run the RPC without it? There are many pools that are running/supporting XMR obviously, so there must be a way around it. I have my daemon sync'd pol backend and front end ready to go, but cannot initiate the RPC due to the same reported errors above.

Using cryptonote-nodejs-pool as a framework btw.

## dbeckwith | 2019-07-31T23:27:07+00:00
I am seeing this error on `v0.14.1.0-release`, is there a fix?
```
This is the RPC monero wallet. It needs to connect to a monero
daemon to work correctly.

Monero 'Boron Butterfly' (v0.14.1.0-release)
Logging to ***/monero-wallet-rpc.log
2019-07-31 23:20:14.392 W Loading wallet...
Wallet password: 
2019-07-31 23:20:33.787 I Generating SSL certificate
2019-07-31 23:20:34.229 I Generating SSL certificate
2019-07-31 23:20:35.894 W Loaded wallet keys file, with public address: 44uyotnH***************************************************************************************
2019-07-31 23:20:35.928 E No message store file found: ***/wallet/wallet.keys.mms
```

## mohamedGr | 2019-10-16T18:51:26+00:00
I am still seeing this issue as well, any update regarding this? How could we use the fix referenced [here](https://github.com/monero-project/monero/pull/5280) to solve this issue?

# Action History
- Created by: bomb-on | 2019-03-13T13:57:55+00:00
- Closed at: 2019-03-13T18:16:57+00:00
