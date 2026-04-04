---
title: 'Docker: CONNECTION FROM 172.17.0.1 REFUSED, too many connections from the
  same address'
source_url: https://github.com/monero-project/monero/issues/6872
author: stmax82
assignees: []
labels: []
created_at: '2020-10-08T20:25:37+00:00'
updated_at: '2022-02-19T03:38:48+00:00'
type: issue
status: closed
closed_at: '2022-02-19T03:38:48+00:00'
---

# Original Description
I'm trying to run a public monero node in a ubuntu docker container on windows.
It works fine except for one problem - it only accepts a single incoming connection at a time:

```
status
Height: [...], 8(out)+1(in) connections, uptime 3d 23h 1m 35s
```
After activating `set_log 1` I found the following log messages:

```
2020-10-08 19:52:19.894 I [172.17.0.1:39834 INC] CONNECTION FROM 172.17.0.1 REFUSED, too many connections from the same address
2020-10-08 19:52:20.512 I [172.17.0.1:39838 INC] CONNECTION FROM 172.17.0.1 REFUSED, too many connections from the same address
2020-10-08 19:52:22.519 I [172.17.0.1:39842 INC] CONNECTION FROM 172.17.0.1 REFUSED, too many connections from the same address
```

It seems like docker changes the real **source** IP address to the one of the docker host (172.17.0.1 in this case) while exposing the container's port, so monerod thinks that there are multiple connections from the same IP address. There's a long-open issue here: moby/moby#15086

The same can be seen using `print_cn`:

```
print_cn
Remote Host                   Type    SSL   Peer id   Support Flags       Recv/Sent (inactive,sec)      State                    Livetime(sec)       Down (kB/s) Down(now)     Up (kB/s) Up(now)
INC 172.17.0.1:39358          IPv4    no    ?         1                   122890(2)/376521(2)           normal                   505                 0           0             0         0            [LAN]
INC 172.17.0.1:40014          IPv4    no    0         0                   8(0)/0(0)                     before_handshake         0                   0           0             0         0            [LAN]
OUT xxx.xxx.xxx.xxx:18080     IPv4    no    ?         1                   485089(3)/105161(37)          normal                   318                 1           2             0         0
OUT xxx.xxx.xxx.xxx:18080     IPv4    no    ?         1                   362389(6)/363040(10)          normal                   429                 0           0             0         0
OUT xxx.xxx.xxx.xxx:12542     IPv4    no    ?         1                   174728(4)/486998(1)           normal                   629                 0           0             0         2
OUT xxx.xxx.xxx.xxx:18080     IPv4    no    ?         1                   241234(1)/261060(0)           normal                   227                 1           0             1         3
OUT xxx.xxx.xxx.xxx:8188      IPv4    no    ?         1                   1006456(2)/612109(1)          normal                   726                 1           2             0         2
OUT xxx.xxx.xxx.xxx:18180     IPv4    no    ?         1                   765258(0)/788646(9)           normal                   1033                0           1             0         0
OUT xxx.xxx.xxx.xxx:18080     IPv4    no    ?         1                   19056(7)/23289(2)             normal                   20                  0           0             1         2
OUT xxx.xxx.xxx.xxx:18080     IPv4    no    ?         1                   176072(2)/157990(9)           normal                   124                 1           2             1         0
```

Any suggestions how I could open this node to the public for more than one concurrent connection?

There is a function `bool has_too_many_connections(address)` in net_node.inl. How much could break if I made it always return false? Would it make sense to add a command line parameter --accept-multiple-connections-from-same-ip-because-docker-screws-up-source-ips?

(Note I haven't tested this on docker for linux.. due to the issue above, it once had the same issue, but it seems to be fixed.. or not.. I'm not sure.)


# Discussion History
## moneromooo-monero | 2020-10-08T20:59:39+00:00
It would not break, and such a parameter would be OK to add.

## moneromooo-monero | 2020-10-11T13:40:27+00:00
https://github.com/monero-project/monero/pull/6877

## stmax82 | 2020-10-11T22:11:55+00:00
@moneromooo-monero thanks for the PR! I thought I'd try my hand at implementing this myself, but you were way faster :)

## scoobybejesus | 2020-10-22T22:08:57+00:00
@stmax82, any chance you saw [this](https://github.com/docker/for-mac/issues/180#issuecomment-608292149)?  Adding `network_mode: host` in the container config is working for some.  That'd possibly/probably be preferable to allowing multiple connections per IP.

## stmax82 | 2020-10-23T21:05:31+00:00
@scoobybejesus I tried running the node using network mode host, but that doesn't seem to work on Windows. It might be a workaround for Linux users trying to run a node in docker though.

[This](https://docs.docker.com/network/host/) seems to confirm it:

> The host networking driver only works on Linux hosts, and is not supported on Docker Desktop for Mac, Docker Desktop for Windows, or Docker EE for Windows Server.



## selsta | 2022-02-19T03:38:48+00:00
Closing as I assume this is resolved with #6877

# Action History
- Created by: stmax82 | 2020-10-08T20:25:37+00:00
- Closed at: 2022-02-19T03:38:48+00:00
