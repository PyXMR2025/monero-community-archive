---
title: RPC server takes 5mins to start
source_url: https://github.com/monero-project/monero/issues/7443
author: mrx23dot
assignees: []
labels: []
created_at: '2021-03-06T12:38:26+00:00'
updated_at: '2021-03-07T11:36:35+00:00'
type: issue
status: closed
closed_at: '2021-03-07T11:36:35+00:00'
---

# Original Description
Why does it takes 5minutes to start up the RPC server?
All on localhost, i5 cpu.

monero-wallet-rpc --wallet-file wallet --password xxx --daemon-address xmr.fail:18081 --rpc-bind-port 28089 --rpc-bind-ip 127.0.0.1 --disable-rpc-login

Monero 'Oxygen Orion' (v0.17.1.9-release)
Win7 x64

2021-03-06 12:20:08.474 W Loading wallet...
2021-03-06 **12:20**:17.532 W Loaded wallet keys file, with public address: xxx
2021-03-06 12:25:00.359 W Background mining not enabled. Run "set setup-background-mining 1" in monero-wallet-cli to change.
2021-03-06 12:25:00.361 I Binding on 127.0.0.1 (IPv4):28089
2021-03-06 **12:25**:05.543 W Starting wallet RPC server







# Discussion History
## mrx23dot | 2021-03-06T12:38:56+00:00
I can open a TCP connection to the given remote node in <<1sec.

## selsta | 2021-03-06T13:53:54+00:00
Does the same happen with a different remote node?

## mrx23dot | 2021-03-06T14:15:40+00:00
Yes, it's slow with another node too:
monero-wallet-rpc --wallet-file wallet --password xxx --daemon-address node.monero.net:18081 --rpc-bind-port 28089 --rpc-bind-ip 127.0.0.1 --disable-rpc-login

2021-03-06 14:06:52.671 W Loading wallet...
2021-03-06 **14:06:**57.548 W Loaded wallet keys file, with public address: xxx
2021-03-06 **14:09**:47.034 W Background mining not enabled. Run "set setup-background-mining 1" in monero-wallet-cli to change.
2021-03-06 14:09:47.039 I Binding on 127.0.0.1 (IPv4):28089
2021-03-06 14:09:48.624 W Starting wallet RPC server

it doesn't really do much in task:
![monero](https://user-images.githubusercontent.com/4163396/110209588-40551500-7e85-11eb-9318-b9c6089e3233.jpg)
There is some network traffic 1KB/s

Looks like it's a bit faster for 3rd/4th time.
Does syncing with the network delay the starting of RPC? What if network is super slow or being down?

## moneromooo-monero | 2021-03-06T15:57:39+00:00
Get a stack trace (gdb \`pidof monero-wallet-rpc\`), see what it's doing. Same with monerod. Or whatever other way exists on windows.

## moneromooo-monero | 2021-03-06T18:12:19+00:00
Syncing will delay, yes. Syncing locks the chain for large chunks of time while verifying blocks and transactions.

## mrx23dot | 2021-03-07T11:36:35+00:00
I just turned up the logging level, it's doing syncing.

So the conclusion is
- first start of RPC will take minutes, 
- during that it wont listen for connections, 
- so better keep it running in the background.



# Action History
- Created by: mrx23dot | 2021-03-06T12:38:26+00:00
- Closed at: 2021-03-07T11:36:35+00:00
