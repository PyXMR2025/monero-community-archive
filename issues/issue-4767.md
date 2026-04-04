---
title: Latest stable Monero can't connect to any testnet peers
source_url: https://github.com/monero-project/monero/issues/4767
author: esin
assignees: []
labels: []
created_at: '2018-10-31T13:57:46+00:00'
updated_at: '2018-11-07T14:17:13+00:00'
type: issue
status: closed
closed_at: '2018-11-07T14:17:13+00:00'
---

# Original Description
Hi
I have compiled from source monero v.0.13.0.4
```monerod --version
2018-10-31 13:55:35,761 INFO  [default] Page size: 4096
Monero 'Beryllium Bullet' (v0.13.0.4-release)
```
But after running I have such errors:
```
2018-10-31 13:44:27.058 [P2P1]  WARN    net.p2p src/p2p/net_node.inl:1190       Failed to connect to any of seed peers, continuing without seeds
2018-10-31 13:44:27.221 [P2P4]  INFO    net.p2p src/p2p/net_node.inl:1820       [10.240.0.6:58638 bac84197-dd3b-873e-d6d5-287b6d42109f INC] CLOSE CONNECTION
2018-10-31 13:44:27.221 [P2P2]  INFO    net.p2p src/p2p/net_node.inl:1805       [10.240.0.6:58771 7d5444df-8d6d-b760-9605-39f82e9f0ea0 INC] NEW CONNECTION
2018-10-31 13:44:29.076 [P2P5]  INFO    net.p2p src/p2p/net_node.inl:946        [0.0.0.0:0 OUT] Connect failed to 212.83.172.165:28080
2018-10-31 13:44:29.093 [P2P5]  INFO    net.p2p src/p2p/net_node.inl:946        [0.0.0.0:0 OUT] Connect failed to 212.83.175.67:28080
2018-10-31 13:44:29.110 [P2P5]  INFO    net.p2p src/p2p/net_node.inl:946        [0.0.0.0:0 OUT] Connect failed to 5.9.100.248:28080
2018-10-31 13:44:29.124 [P2P5]  INFO    net.p2p src/p2p/net_node.inl:946        [0.0.0.0:0 OUT] Connect failed to 163.172.182.165:28080
2018-10-31 13:44:29.139 [P2P5]  INFO    net.p2p src/p2p/net_node.inl:946        [0.0.0.0:0 OUT] Connect failed to 195.154.123.123:28080
2018-10-31 13:44:29.157 [P2P5]  INFO    net.p2p src/p2p/net_node.inl:946        [0.0.0.0:0 OUT] Connect failed to 212.83.172.165:28080
2018-10-31 13:44:29.172 [P2P5]  INFO    net.p2p src/p2p/net_node.inl:946        [0.0.0.0:0 OUT] Connect failed to 212.83.175.67:28080
2018-10-31 13:44:29.190 [P2P5]  INFO    net.p2p src/p2p/net_node.inl:946        [0.0.0.0:0 OUT] Connect failed to 5.9.100.248:28080
2018-10-31 13:44:29.207 [P2P5]  INFO    net.p2p src/p2p/net_node.inl:946        [0.0.0.0:0 OUT] Connect failed to 163.172.182.165:28080
2018-10-31 13:44:29.221 [P2P5]  INFO    net.p2p src/p2p/net_node.inl:946        [0.0.0.0:0 OUT] Connect failed to 195.154.123.123:28080
2018-10-31 13:44:29.239 [P2P5]  INFO    net.p2p src/p2p/net_node.inl:946        [0.0.0.0:0 OUT] Connect failed to 212.83.172.165:28080
```
I'm runing like this:
```
DNS_PUBLIC=tcp://8.8.8.8 monerod --data-dir=/monero-testnet-data --rpc-bind-ip=0.0.0.0 --confirm-external-bind --testnet
```
And just check seed nodes, and seems that 28080 really closed

Could you help me, please?

Thank you

# Discussion History
## dEBRUYNE-1 | 2018-10-31T17:34:05+00:00
>--rpc-bind-ip=0.0.0.0 --confirm-external-bind

What happens if you remove those two flags? 

## fluffypony | 2018-10-31T22:20:48+00:00
Try now - I've managed to get two of my seed nodes back up that were down, and I've let people that are running seed nodes know that they're down.

## moneromooo-monero | 2018-11-07T14:15:32+00:00
+resolved

# Action History
- Created by: esin | 2018-10-31T13:57:46+00:00
- Closed at: 2018-11-07T14:17:13+00:00
