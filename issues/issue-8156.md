---
title: My monero_wallet_rpc doesn't work，it trapped in “ W Starting wallet RPC server”
source_url: https://github.com/monero-project/monero/issues/8156
author: shrBest
assignees: []
labels: []
created_at: '2022-01-24T17:24:50+00:00'
updated_at: '2024-05-06T19:16:12+00:00'
type: issue
status: closed
closed_at: '2022-07-20T01:23:29+00:00'
---

# Original Description
```
./monero-wallet-rpc --rpc-bind-port 28087 --rpc-bind-ip 127.0.0.1 --wallet-file ~/monero_wallet/wallets/XMRwallet1 --password 123456 --trusted-daemon --testnet --rpc-login test:123456
This is the RPC monero wallet. It needs to connect to a monero
daemon to work correctly.

Monero 'Oxygen Orion' (v0.17.0.0-319b831e6)
Logging to ./monero-wallet-rpc.log
2022-01-24 17:01:58.712	W Loading wallet...
2022-01-24 17:01:59.798	W Loaded wallet keys file, with public address: 9wXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
2022-01-24 17:02:00.049	E Failed to query mining status: No connection to daemon
2022-01-24 17:02:00.049	I Binding on 127.0.0.1 (IPv4):28087
2022-01-24 17:02:00.085	W Starting wallet RPC server
2022-01-24 17:22:22.400	E !r. THROW EXCEPTION: tools::error::no_connection_to_daemon
2022-01-24 17:22:22.400	E Exception at while refreshing, what=no connection to daemon
2022-01-24 17:22:42.408	E !r. THROW EXCEPTION: tools::error::no_connection_to_daemon
2022-01-24 17:22:42.408	E Exception at while refreshing, what=no connection to daemon
............
```

I‘m trying to use my monero_wallet_rpc which connects my local node, but it doesn't work，even it took many hours. 
My local node starts from :
`./monerod --rpc-bind-ip 127.0.0.1 --confirm-external-bind  --restricted-rpc --testnet`
and it runs successfully and my  monero_wallet_cli can connect it successfully,.
Where's the problem with my usage of  monero_wallet_rpc，is there any parameters i forgot or used incorrectly? Thanks!


# Discussion History
## beefgroin | 2022-01-25T17:46:27+00:00
have you tried providing daemon address directly with `./monero-wallet-rpc --daemon-address 127.0.0.1:18081`?

## selsta | 2022-01-26T00:48:45+00:00
`./monero-wallet-rpc --daemon-address 127.0.0.1:28081` for testnet.

## shrBest | 2022-01-26T14:39:35+00:00

> `./monero-wallet-rpc --daemon-address 127.0.0.1:28081` for testnet.


> I have tried, but it didn't work, it still stopped in “W Starting wallet RPC server”.
> 
> ```
> ./monero-wallet-rpc --rpc-bind-port 28087 --wallet-file ~/monero_wallet/wallets/XMRwallet2 --password 123456 --testnet --daemon-address 127.0.0.1:28081
> This is the RPC monero wallet. It needs to connect to a monero
> daemon to work correctly.
> 
> Monero 'Oxygen Orion' (v0.17.0.0-319b831e6)
> Logging to ./monero-wallet-rpc.log
> 2022-01-26 06:10:54.484	W Loading wallet...
> 2022-01-26 06:10:54.774	W Loaded wallet keys file, with public address: 9uXXXXXXXXXXXXXXXXXXXXXXXXXXX
> 2022-01-26 06:10:55.069	W RPC username/password is stored in file monero-wallet-rpc.28087.login
> 2022-01-26 06:10:55.075	E Failed to setup background mining: OK
> 2022-01-26 06:10:55.075	I Binding on 127.0.0.1 (IPv4):28087
> 2022-01-26 06:10:55.484	W Starting wallet RPC server
> ```
> 
> but my local node could detect the connection when the wallet tried to connect it:
> 
> ```
> 2022-01-26 06:57:37.126	W Background mining controller thread started
> 2022-01-26 06:57:37.126	I Miner thread was started [0]
> 2022-01-26 06:57:37.131	I background mining is enabled, but not started, waiting until start triggers
> ```
> 
> but the wallet still has no reaction...



## selsta | 2022-02-18T22:55:40+00:00
Post logs with --log-level 2

## Cactii1 | 2022-07-20T00:55:02+00:00
This seems to be an abandoned support request.

Propose to close.

## dev-warrior777 | 2024-05-06T19:10:46+00:00
Similar issue:

Started 2 connected `regtest` nodes on localhost and trying to start the wallet client and receiving the same exception as above `Exception at while refreshing, what=no connection to daemon
` 

```
+ monerod --detach --pidfile=/home/dev/dextest/xmr/alpha/monerod.pid --regtest --data-dir=/home/dev/dextest/xmr/alpha --config-file=/home/dev/dextest/xmr/alpha/alpha.conf --no-igd --no-zmq --hide-my-port --p2p-bind-ip 127.0.0.1 --p2p-bind-port 48080 --rpc-bind-ip 127.0.0.1 --rpc-bind-port 48081 --add-exclusive-node 127.0.0.1:58080 --fixed-difficulty 1 --disable-rpc-ban --log-level 1
2024-05-06 19:05:59.454	I Monero 'Fluorine Fermi' (v0.18.3.3-release)
2024-05-06 19:05:59.454	I Moving from main() into the daemonize now.
Forking to background...
+ sleep 5
+ monerod --detach --pidfile=/home/dev/dextest/xmr/beta/monerod.pid --regtest --data-dir=/home/dev/dextest/xmr/beta --config-file=/home/dev/dextest/xmr/beta/beta.conf --no-igd --no-zmq --hide-my-port --p2p-bind-ip 127.0.0.1 --p2p-bind-port 58080 --rpc-bind-ip 127.0.0.1 --rpc-bind-port 58081 --add-exclusive-node 127.0.0.1:48080 --fixed-difficulty 1 --disable-rpc-ban --log-level 1
2024-05-06 19:06:04.568	I Monero 'Fluorine Fermi' (v0.18.3.3-release)
2024-05-06 19:06:04.568	I Moving from main() into the daemonize now.
Forking to background...
+ monero-wallet-rpc --daemon-address 127.0.0.1:58081 --rpc-bind-ip 127.0.0.1 --rpc-bind-port 28884 --log-file=/home/dev/dextest/xmr/wallets/fred-wallet-rpc.log --disable-rpc-login --allow-mismatched-daemon-version --wallet-dir /home/dev/dextest/xmr/wallets
This is the RPC monero wallet. It needs to connect to a monero
daemon to work correctly.

Monero 'Fluorine Fermi' (v0.18.3.3-release)
Logging to /home/dev/dextest/xmr/wallets/fred-wallet-rpc.log


```

# Action History
- Created by: shrBest | 2022-01-24T17:24:50+00:00
- Closed at: 2022-07-20T01:23:29+00:00
