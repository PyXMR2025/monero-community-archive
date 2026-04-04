---
title: Monerod 0.11.1.0 not starting on Windows 10
source_url: https://github.com/monero-project/monero/issues/2907
author: zwiglm
assignees: []
labels:
- invalid
created_at: '2017-12-10T00:42:41+00:00'
updated_at: '2017-12-23T11:56:24+00:00'
type: issue
status: closed
closed_at: '2017-12-23T11:56:24+00:00'
---

# Original Description
No special network setup. Just running behind NAT router with 192.168... address.
Has been working with 0.10.3.1

Here is the startup debug output:
2017-12-06 00:27:35.865 12336   INFO    global  src/daemon/main.cpp:279 Monero 'Helium Hydra' (v0.11.1.0-release)
2017-12-06 00:27:35.866 12336   INFO    daemon  src/daemon/main.cpp:281 Moving from main() into the daemonize now.
2017-12-06 00:27:35.867 12336   INFO    global  src/daemon/protocol.h:55        Initializing cryptonote protocol...
2017-12-06 00:27:35.868 12336   INFO    global  src/daemon/protocol.h:60        Cryptonote protocol initialized OK
2017-12-06 00:27:35.870 12336   INFO    global  src/daemon/p2p.h:63     Initializing p2p server...
2017-12-06 00:27:35.871 12336   DEBUG   net.p2p src/p2p/net_node.inl:489        dns_threads created, now waiting for completion or timeout of 20000ms
2017-12-06 00:27:35.873 3976    DEBUG   net.p2p src/p2p/net_node.inl:461        dns_threads[0] created for: seeds.moneroseeds.se
2017-12-06 00:27:35.873 1572    DEBUG   net.p2p src/p2p/net_node.inl:461        dns_threads[1] created for: seeds.moneroseeds.ae.org
2017-12-06 00:27:35.875 12776   DEBUG   net.p2p src/p2p/net_node.inl:461        dns_threads[2] created for: seeds.moneroseeds.ch
2017-12-06 00:27:35.877 10616   DEBUG   net.p2p src/p2p/net_node.inl:461        dns_threads[3] created for: seeds.moneroseeds.li
[1512520055] libunbound[13028:0] error: can't bind socket: Permission denied. for 0.0.0.0
[1512520055] libunbound[13028:0] error: can't bind socket: Permission denied. for 0.0.0.0
[1512520055] libunbound[13028:0] error: can't bind socket: Permission denied. for 0.0.0.0
[1512520055] libunbound[13028:0] error: can't bind socket: Permission denied. for 0.0.0.0
[1512520055] libunbound[13028:0] error: can't bind socket: Permission denied. for 0.0.0.0
[1512520055] libunbound[13028:0] error: can't bind socket: Permission denied. for 0.0.0.0
[1512520055] libunbound[13028:0] error: can't bind socket: Permission denied. for 0.0.0.0
[1512520055] libunbound[13028:0] error: can't bind socket: Permission denied. for 0.0.0.0
[1512520055] libunbound[13028:0] error: can't bind socket: Permission denied. for 0.0.0.0
[1512520056] libunbound[13028:0] error: can't bind socket: Permission denied. for 0.0.0.0
[1512520056] libunbound[13028:0] error: can't bind socket: Permission denied. for 0.0.0.0
[1512520056] libunbound[13028:0] error: can't bind socket: Permission denied. for 0.0.0.0
[1512520056] libunbound[13028:0] error: can't bind socket: Permission denied. for 0.0.0.0
[1512520056] libunbound[13028:0] error: can't bind socket: Permission denied. for 0.0.0.0
[1512520056] libunbound[13028:0] error: can't bind socket: Permission denied. for 0.0.0.0
[1512520056] libunbound[13028:0] error: can't bind socket: Permission denied. for 0.0.0.0
2[1512520056] libunbound[13028:0] error: can't bind socket: Permission denied. for 0.0.0.0
017-12-06 00:27:36.024  10616   DEBUG   net.p2p src/p2p/net_node.inl:469        dns_threads[3] DNS resolve done
[1512520056] libunbound[13028:0] error: can't bind socket: Permission denied. for 0.0.0.0
2017-12-06 00:27:36.026 10616   INFO    net.p2p src/p2p/net_node.inl:481        dns_threads[3] addr_str: seeds.moneroseeds.li  number of results: 0
[1512520056] libunbound[13028:0] error: can't bind socket: Permission denied. for 0.0.0.0
2017-12-06 00:27:36.031 1572    DEBUG   net.p2p src/p2p/net_node.inl:469        dns_threads[1] DNS resolve done
2017-12-06 00:27:36.032 1572    INFO    net.p2p src/p2p/net_node.inl:481        dns_threads[1] addr_str: seeds.moneroseeds.ae.org  number of results: 0
[1512520056] libunbound[13028:0] error: can't bind socket: Permission denied. for 0.0.0.0
2017-12-06 00:27:36.033 12776   DEBUG   net.p2p src/p2p/net_node.inl:469        dns_threads[2] DNS resolve done
2017-12-06 00:27:36.036 12776   INFO    net.p2p src/p2p/net_node.inl:481        dns_threads[2] addr_str: seeds.moneroseeds.ch  number of results: 0
2017-12-06 00:27:36.040 3976    DEBUG   net.p2p src/p2p/net_node.inl:469        dns_threads[0] DNS resolve done
2017-12-06 00:27:36.040 3976    INFO    net.p2p src/p2p/net_node.inl:481        dns_threads[0] addr_str: seeds.moneroseeds.se  number of results: 0
2017-12-06 00:27:36.042 12336   DEBUG   net.p2p src/p2p/net_node.inl:505        DNS lookup for seeds.moneroseeds.se: 0 results
2017-12-06 00:27:36.044 12336   DEBUG   net.p2p src/p2p/net_node.inl:505        DNS lookup for seeds.moneroseeds.ae.org: 0 results
2017-12-06 00:27:36.046 12336   DEBUG   net.p2p src/p2p/net_node.inl:505        DNS lookup for seeds.moneroseeds.ch: 0 results
2017-12-06 00:27:36.047 12336   DEBUG   net.p2p src/p2p/net_node.inl:505        DNS lookup for seeds.moneroseeds.li: 0 results
2017-12-06 00:27:36.048 12336   INFO    net.p2p src/p2p/net_node.inl:519        DNS seed node lookup either timed out or failed, falling back to defaults
2017-12-06 00:27:36.049 12336   DEBUG   net.p2p src/p2p/net_node.inl:530        Seed node: 107.152.130.98:18080
2017-12-06 00:27:36.050 12336   INFO    net.p2p src/p2p/net_node.inl:395        Added seed node: 107.152.130.98:18080
2017-12-06 00:27:36.051 12336   DEBUG   net.p2p src/p2p/net_node.inl:530        Seed node: 161.67.132.39:18080
2017-12-06 00:27:36.052 12336   INFO    net.p2p src/p2p/net_node.inl:395        Added seed node: 161.67.132.39:18080
2017-12-06 00:27:36.053 12336   DEBUG   net.p2p src/p2p/net_node.inl:530        Seed node: 163.172.182.165:18080
2017-12-06 00:27:36.055 12336   INFO    net.p2p src/p2p/net_node.inl:395        Added seed node: 163.172.182.165:18080
2017-12-06 00:27:36.056 12336   DEBUG   net.p2p src/p2p/net_node.inl:530        Seed node: 195.154.123.123:28080
2017-12-06 00:27:36.058 12336   INFO    net.p2p src/p2p/net_node.inl:395        Added seed node: 195.154.123.123:28080
2017-12-06 00:27:36.059 12336   DEBUG   net.p2p src/p2p/net_node.inl:530        Seed node: 198.74.231.92:18080
2017-12-06 00:27:36.060 12336   INFO    net.p2p src/p2p/net_node.inl:395        Added seed node: 198.74.231.92:18080
2017-12-06 00:27:36.060 12336   DEBUG   net.p2p src/p2p/net_node.inl:530        Seed node: 212.83.172.165:28080
2017-12-06 00:27:36.061 12336   INFO    net.p2p src/p2p/net_node.inl:395        Added seed node: 212.83.172.165:28080
2017-12-06 00:27:36.062 12336   DEBUG   net.p2p src/p2p/net_node.inl:530        Seed node: 212.83.175.67:18080
2017-12-06 00:27:36.063 12336   INFO    net.p2p src/p2p/net_node.inl:395        Added seed node: 212.83.175.67:18080
2017-12-06 00:27:36.065 12336   DEBUG   net.p2p src/p2p/net_node.inl:530        Seed node: 5.9.100.248:18080
2017-12-06 00:27:36.066 12336   INFO    net.p2p src/p2p/net_node.inl:395        Added seed node: 5.9.100.248:18080
2017-12-06 00:27:36.067 12336   DEBUG   net.p2p src/p2p/net_node.inl:533        Number of seed nodes: 8
2017-12-06 00:27:36.068 12336   INFO    net.throttle    src/p2p/network_throttle-detail.cpp:162 Setting LIMIT: 4.40402e+006 kbps
2017-12-06 00:27:36.069 12336   INFO    net.p2p src/p2p/net_node.inl:1883       Set limit-up to 2048 kB/s
2017-12-06 00:27:36.070 12336   INFO    net.throttle    src/p2p/network_throttle-detail.cpp:162 Setting LIMIT: 8.38861e+006 kbps
2017-12-06 00:27:36.071 12336   INFO    net.throttle    src/p2p/network_throttle-detail.cpp:162 Setting LIMIT: 8.38861e+006 kbps
2017-12-06 00:27:36.072 12336   INFO    net.p2p src/p2p/net_node.inl:1897       Set limit-down to 8192 kB/s
2017-12-06 00:27:36.073 12336   INFO    net.throttle    src/p2p/network_throttle-detail.cpp:162 Setting LIMIT: 4.40402e+006 kbps
2017-12-06 00:27:36.074 12336   INFO    net.p2p src/p2p/net_node.inl:1919       Set limit-up to 2048 kB/s
2017-12-06 00:27:36.076 12336   INFO    net.throttle    src/p2p/network_throttle-detail.cpp:162 Setting LIMIT: 8.38861e+006 kbps
2017-12-06 00:27:36.077 12336   INFO    net.throttle    src/p2p/network_throttle-detail.cpp:162 Setting LIMIT: 8.38861e+006 kbps
2017-12-06 00:27:36.078 12336   INFO    net.p2p src/p2p/net_node.inl:1923       Set limit-down to 8192 kB/s
2017-12-06 00:27:36.080 12336   INFO    net     contrib/epee/include/net/abstract_tcp_server2.inl:795   Set server type to: 2 from name: P2P, prefix_name = P2P
2017-12-06 00:27:36.080 12336   INFO    net.p2p src/p2p/net_node.inl:572        Binding on 0.0.0.0:18080
2017-12-06 00:27:36.085 12336   ERROR   net     contrib/epee/include/net/abstract_tcp_server2.inl:741   Exception at [boosted_tcp_server<t_protocol_handler>::init_server], what=bind: Der Zugriff auf einen Socket war aufgrund der Zugriffsrechte des Sockets unzulõssig
2017-12-06 00:27:36.086 12336   ERROR   net.p2p src/p2p/net_node.inl:574        Failed to bind server
2017-12-06 00:27:36.091 12336   INFO    global  src/daemon/core.h:89    Deinitializing core...
2017-12-06 00:27:36.099 12336   DEBUG   miner   src/cryptonote_basic/miner.cpp:337      Not mining - nothing to stop
2017-12-06 00:27:36.100 12336   ERROR   daemon  src/daemon/core.h:94    Failed to deinitialize core...
2017-12-06 00:27:36.101 12336   DEBUG   miner   src/cryptonote_basic/miner.cpp:337      Not mining - nothing to stop
2017-12-06 00:27:36.102 12336   INFO    global  src/daemon/protocol.h:77        Stopping cryptonote protocol...
2017-12-06 00:27:36.103 12336   INFO    global  src/daemon/protocol.h:81        Cryptonote protocol stopped successfully
2017-12-06 00:27:36.104 12336   ERROR   daemon  src/daemon/main.cpp:287 Exception in main! Failed to initialize p2p server.#

HTH,
Martin

Edit: this is for the 64-bit version

# Discussion History
## moneromooo-monero | 2017-12-10T09:00:16+00:00
Does 0.10.3.1 work now ? Looks like your OS is denying monerod the right to bind to your network interface.

## kinbitz | 2017-12-10T21:11:17+00:00
Did you try to disable the firewall? 

## zwiglm | 2017-12-11T00:29:06+00:00
- There is a incoming rule for monerod. (just the simple rule for allowing on private/public networks for all ports on the application monerod.exe itself)

- I am pretty sure that the virus scanner is NOT interfering 

- nope. you are right. 0.10.3.1 is also not working anymore. there must have been some changes to win 10 with one of the updates that I am not aware of. (I started using the daemon in august and then synchronized to the block-chain. after full sync i did an update the one or other day. after a while I left it alone till a few days ago and did the update to 0.11....)


## zwiglm | 2017-12-11T00:42:20+00:00
Are there any con-thoughts against running monerod as admin. In the "beginning" (my start with 0.10.3.1) this has not been necessary?


## moneromooo-monero | 2017-12-11T12:57:54+00:00
This is a bad idea. The more you can segregate, the  better.

## zwiglm | 2017-12-11T14:42:40+00:00
> This is a bad idea. The more you can segregate, the better.

Well, I pretty much thought so.
Since I am behind a NAT router... is there port-forwarding needed?
Or any other clues that I can go and investigate on my side..?

## moneromooo-monero | 2017-12-11T19:59:51+00:00
It's your OS, or some IDS, antivirus, or similar program. Check its docs. You need to allow binding to a network interface (allow incoming networking).

## zwiglm | 2017-12-11T21:19:43+00:00
Thank you. I will do further investigation.

## moneromooo-monero | 2017-12-23T11:50:03+00:00
Not monero, so closing.

+invalid

# Action History
- Created by: zwiglm | 2017-12-10T00:42:41+00:00
- Closed at: 2017-12-23T11:56:24+00:00
