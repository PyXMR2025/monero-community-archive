---
title: Cannot connect wallet client to daemon
source_url: https://github.com/monero-project/monero/issues/9320
author: dev-warrior777
assignees: []
labels: []
created_at: '2024-05-06T19:19:38+00:00'
updated_at: '2024-05-15T09:59:49+00:00'
type: issue
status: closed
closed_at: '2024-05-15T09:59:49+00:00'
---

# Original Description


> Similar issue: #8156

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

_Originally posted by @dev-warrior777 in https://github.com/monero-project/monero/issues/8156#issuecomment-2096723462_
            

# Discussion History
## dev-warrior777 | 2024-05-06T19:28:20+00:00
Note the wallet client RPC does not accept `--regtest` parameter

I am building a dev tool to further develop Monero <-> Decred atomic swaps

The requirements are:
1. 2 connected localhost net nodes
2. Manual mining
3. 2 or more wallets

Thanks

## selsta | 2024-05-06T23:15:18+00:00
Did you try getting it working with a single node and single wallet first? If not, can you try to get this working first with minimal flags (no `--regtest`), and then add back your requirements until it fails.

## dev-warrior777 | 2024-05-07T07:14:38+00:00
Thanks for reply. I will definitely go that route today. 

Actually 1 & 2 above are already working - 2 connected nodes with manual mining on regtest. Just no wallets connecting. I specifically use `--no-zmq` on the nodes .. _could that be a reason_? The wallet does not seem to be able to find a node even when given one explicitly `--daemon-address 127.0.0.1:58081`

Thanks again

## selsta | 2024-05-07T14:09:34+00:00
`--no-zmq` should be unrelated for just regular wallets connecting

## dev-warrior777 | 2024-05-07T20:04:29+00:00
Ok, thank you.
I made good progress today with your suggestions, appreciated

Please close this issue.
 

## dev-warrior777 | 2024-05-07T21:28:05+00:00
If I can ride another question before closing: are stagenet coins different than testnet coins?


## selsta | 2024-05-07T23:42:11+00:00
Stagenet and testnet are different, yes.

Stagenet is for testing your mainnet application, while on testnet we often test new protocol featurea early.

## dev-warrior777 | 2024-05-08T19:22:14+00:00
Ok, thanks .. let's close this issue.

## dev-warrior777 | 2024-05-15T09:59:49+00:00
Closed, thanks

# Action History
- Created by: dev-warrior777 | 2024-05-06T19:19:38+00:00
- Closed at: 2024-05-15T09:59:49+00:00
