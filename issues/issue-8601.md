---
title: p2p-bind-ip for outbound connections
source_url: https://github.com/monero-project/monero/issues/8601
author: g00g1
assignees: []
labels: []
created_at: '2022-09-29T19:24:58+00:00'
updated_at: '2023-03-12T15:28:04+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
As I see, monerod advertises its IPv4 as set by --p2p-bind-ip, but when connecting to other nodes, it uses system's default IPv4 address. Are there any workarounds, is this a bug or intended behaviour? I would like to have possibility to manually set outgoing connections IP address as well.

# Discussion History
## duggavo | 2022-10-02T20:07:03+00:00
--p2p-bind-ip doesn't "change" your IP. It is used to set to which interface to listen.
For example, if you use `--p2p-bind-ip 0.0.0.0` it will allow any IP address to connect to your daemon, and if you use `--p2p-bind-ip 127.0.0.1` it will only allow local daemons to connect.

You'll likely not want to use this unless you want to block all the incoming p2p connections.

## g00g1 | 2023-03-04T12:19:37+00:00
Is there any way to control what IPv4 is advertised when running `monerod --public-node`?

## vtnerd | 2023-03-07T20:59:30+00:00
There is no advertised IPv4 address (over the network protocol). The remote peer determines the IPv4 address at the IP stack layer - the OS provides the remote IP address and `monerod` uses that address.

## g00g1 | 2023-03-12T14:41:41+00:00
I have set `p2p-bind-ip` to `0.0.0.0`, but no incoming connections seen by monerod (see below). I have properly configured my firewall: both 18080/tcp and 18089/tcp are publicly reachable.

```
$ sudo ss -tnp | grep :18080
$ sudo ss -tnp | grep :18089
ESTAB 0      1059840                          x.x.x.x:18089                          *.*.*.*:* users:(("monerod",pid=13165,fd=155))                   
ESTAB 0      0                                x.x.x.x:18089                          *.*.*.*:* users:(("monerod",pid=13165,fd=36))                    
ESTAB 0      0                                x.x.x.x:18089                          *.*.*.*:* users:(("monerod",pid=13165,fd=34))                    
ESTAB 0      0                                x.x.x.x:18089                          *.*.*.*:* users:(("monerod",pid=13165,fd=38))                    
$ monerod status
2023-03-12 15:17:40.633	I Monero 'Fluorine Fermi' (v0.18.2.0-unknown)
Height: 2840462/2840462 (100.0%) on mainnet, not mining, net hash 2.66 GH/s, v16, 129(out)+0(in) connections, uptime 0d 1h 3m 10s
```

There are a few IP addresses configured at my system - x.x.x.x is not the primary IP address but is intended to be used by monerod and other publicly facing services like web server.

# Action History
- Created by: g00g1 | 2022-09-29T19:24:58+00:00
