---
title: '"no peers available" issue on a three-node regtest (private network) '
source_url: https://github.com/monero-project/monero/issues/5683
author: hacheigriega
assignees: []
labels: []
created_at: '2019-06-21T17:55:40+00:00'
updated_at: '2019-06-26T14:39:36+00:00'
type: issue
status: closed
closed_at: '2019-06-26T14:39:36+00:00'
---

# Original Description
I start the daemons the following way:
```
node 1:
monerod --regtest --p2p-bind-port 25010 --rpc-bind-port 25011 --zmq-rpc-bind-port 25012 --log-level 1 --allow-local-ip --data-dir /root
/testnet/node_1 --add-exclusive-node 127.0.0.1:25020 --add-exclusive-node 127.0.0.1:25030 --fixed-difficulty 100

node 2:
monerod --regtest --p2p-bind-port 25020 --rpc-bind-port 25021 --zmq-rpc-bind-port 25022 --log-level 1 --allow-local-ip --data-dir /root
/testnet/node_2 --add-exclusive-node 127.0.0.1:25010 --add-exclusive-node 127.0.0.1:25030 --fixed-difficulty 100

node 3:
monerod --regtest --p2p-bind-port 25030 --rpc-bind-port 25031 --zmq-rpc-bind-port 25032 --log-level 1 --allow-local-ip --data-dir /root
/testnet/node_3 --add-exclusive-node 127.0.0.1:25010 --add-exclusive-node 127.0.0.1:25020 --fixed-difficulty 100 
```

However, when I "print_cn" on each daemon, I get asymmetric results:
```
node 1:
Remote Host                   SSL   Peer id             Support Flags       Recv/Sent (inactive,sec)      State                    Livetime(sec)       Down (kB/s) Down(now)     Up (kB/s) Up(now)      

OUT 127.0.0.1:25030           no    0000000000000000    0                   0(5)/326(5)                   before_handshake         5                   0           0             0         0            [LOCALHOST]
INC 127.0.0.1:40138           no    e3b166f058a96f9f    1                   27544(6)/22815(1)             normal                   231                 0           0             0         0            [LOCALHOST]



node 2:
Remote Host                   SSL   Peer id             Support Flags       Recv/Sent (inactive,sec)      State                    Livetime(sec)       Down (kB/s) Down(now)     Up (kB/s) Up(now)      

OUT 127.0.0.1:25010           no    0000000000000000    0                   0(0)/326(0)                   before_handshake         0                   0           0             0         0            [LOCALHOST]
OUT 127.0.0.1:25030           no    e3b166f058a96f9f    1                   42866(0)/18910(0)             normal                   212                 0           0             0         0            [LOCALHOST]
INC 127.0.0.1:45938           no    e3b166f058a96f9f    1                   33945(0)/37648(2)             normal                   217                 0           0             0         0            [LOCALHOST]



node 3:
Remote Host                   SSL   Peer id             Support Flags       Recv/Sent (inactive,sec)      State                    Livetime(sec)       Down (kB/s) Down(now)     Up (kB/s) Up(now)      

INC 127.0.0.1:40172           no    67cd57ab271edfda    1                   11743(2)/22351(2)             normal                   162                 0           0             0         0            [LOCALHOST]
OUT 127.0.0.1:25020           no    67cd57ab271edfda    1                   20414(2)/18478(5)             normal                   167                 0           0             0         0            [LOCALHOST]
OUT 127.0.0.1:25010           no    f091d8ec6044a60d    1                   9805(5)/15887(2)              normal                   167                 0           0             0         0            [LOCALHOST]

```

The outputs above are consistent throughout the duration of the program. I encounter the following error for node 1:
```
2019-06-21 17:37:18.355 [P2P8]  ERROR   net.cn  src/cryptonote_protocol/cryptonote_protocol_handler.inl:2256    Transaction not relayed - no peers available
```



# Discussion History
## moneroexamples | 2019-06-26T00:36:22+00:00
This affects any last node you run. In you case `node_1` must have been launched last. 

The reason is this line: 

https://github.com/monero-project/monero/blob/ebb1c03e8cace02ebcc87c92f372e413a26c6406/src/p2p/net_node.inl#L2303

The value of connections form the same IP is (127.0.0.1) is limited two 1 (counted from 0, gives 2 connections) and hard coded. Thus when the first two nodes will connect to each other, they will be rejecting third node.

Change the `max_connections` to 2 and recompile monero if you really want all your private nodes to be connected to each other. Or somehow the third not must have different IP.

p.s. 
For future reference, I just paste commands I used for launching the private nodes, in case have to revisit the issue in future:

```bash
monerod --regtest --p2p-bind-port 25410 --rpc-bind-port 25411 --zmq-rpc-bind-port 25412 --log-level 0 --allow-local-ip --data-dir /tmp/testnet/node_1 --add-exclusive-node 127.0.0.1:25420 --add-exclusive-node 127.0.0.1:25430 --fixed-difficulty 100 --hide-my-port --no-igd --p2p-bind-ip 127.0.0.1 


monerod --regtest --p2p-bind-port 25420 --rpc-bind-port 25421 --zmq-rpc-bind-port 25422 --log-level 0 --allow-local-ip --data-dir /tmp/testnet/node_2 --add-exclusive-node 127.0.0.1:25410 --add-exclusive-node 127.0.0.1:25430 --fixed-difficulty 100 --hide-my-port --no-igd  --p2p-bind-ip 127.0.0.1


monerod --regtest --p2p-bind-port 25430 --rpc-bind-port 25431 --zmq-rpc-bind-port 25432 --log-level 0 --allow-local-ip --data-dir /tmp/testnet/node_3 --add-exclusive-node 127.0.0.1:25410 --add-exclusive-node 127.0.0.1:25420 --fixed-difficulty 100 --hide-my-port --no-igd --p2p-bind-ip 127.0.0.1
```



 

# Action History
- Created by: hacheigriega | 2019-06-21T17:55:40+00:00
- Closed at: 2019-06-26T14:39:36+00:00
