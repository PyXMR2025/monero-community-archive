---
title: 'DNS error: "unknown node or service"'
source_url: https://github.com/xmrig/xmrig/issues/822
author: mahmoodn
assignees: []
labels: []
created_at: '2018-10-19T10:45:53+00:00'
updated_at: '2021-04-12T15:55:55+00:00'
type: issue
status: closed
closed_at: '2021-04-12T15:55:55+00:00'
---

# Original Description
Although I can ping coinfoundry, I don't know why xmrig can not reach that.

```
$ ./xmrig-nvidia 
 * ABOUT        XMRig-NVIDIA/2.8.1 gcc/7.3.0
 * LIBS         libuv/1.18.0 CUDA/10.0 OpenSSL/1.0.2n microhttpd/0.9.59 
 * CPU          AMD Ryzen 7 1800X Eight-Core Processor          x64 AES
 * GPU #0       PCI:0000:26:00 Quadro M2000 @ 1162/3303 MHz 56x18 0x0 arch:52 SMX:6
 * ALGO         cryptonight, donate=5%
 * POOL #1      xmr.coinfoundry.org:3032 variant 1
 * COMMANDS     hashrate, health, pause, resume
[2018-10-19 14:12:34] [xmr.coinfoundry.org:3032] DNS error: "unknown node or service"
[2018-10-19 14:12:39] [xmr.coinfoundry.org:3032] DNS error: "unknown node or service"
[2018-10-19 14:12:45] [xmr.coinfoundry.org:3032] DNS error: "unknown node or service"
[2018-10-19 14:12:50] [xmr.coinfoundry.org:3032] DNS error: "unknown node or service"
[2018-10-19 14:12:55] [xmr.coinfoundry.org:3032] DNS error: "unknown node or service"
[2018-10-19 14:13:01] Ctrl+C received, exiting
$ ping coinfoundry.org
PING coinfoundry.org (159.69.212.210) 56(84) bytes of data.
64 bytes from static.210.212.69.159.clients.your-server.de (159.69.212.210): icmp_seq=1 ttl=44 time=119 ms
64 bytes from static.210.212.69.159.clients.your-server.de (159.69.212.210): icmp_seq=2 ttl=44 time=113 ms
^C
--- coinfoundry.org ping statistics ---
2 packets transmitted, 2 received, 0% packet loss, time 1001ms
rtt min/avg/max/mdev = 113.300/116.214/119.128/2.914 ms
```
What is the problem here?

# Discussion History
## xmrig | 2018-10-19T10:54:45+00:00
You should ping `xmr.coinfoundry.org` it resolved to different IP address than just `coinfoundry.org`.
Thank you.

## mahmoodn | 2018-10-19T12:43:52+00:00
Well that doesn't work!

```
$ ping xmr.coinfoundry.org
ping: xmr.coinfoundry.org: Name or service not known
$ ping coinfoundry.org
PING coinfoundry.org (159.69.212.210) 56(84) bytes of data.
64 bytes from static.210.212.69.159.clients.your-server.de (159.69.212.210): icmp_seq=1 ttl=44 time=116 ms
^C
--- coinfoundry.org ping statistics ---
2 packets transmitted, 1 received, 50% packet loss, time 1001ms
rtt min/avg/max/mdev = 116.436/116.436/116.436/0.000 ms
```
I haven't seen any post about the state of the server. The coinfoundry website says it is xmr.coinfoundry:3032

## NmxMilk | 2018-10-22T12:56:58+00:00
It might be the site does not respond to ping. Try something like:
#telnet xmr.coinfoundry.org 3032
Trying 159.69.212.211...
Connected to xmr.coinfoundry.org.
Escape character is '^]'.



## mahmoodn | 2018-10-23T19:48:16+00:00
Well it seems that the server is changed to `donate.V2.xmrig.com:3333` for both cpu and gpu.

## DeadManWalkingTO | 2019-03-17T14:33:30+00:00
Try latest version and feedback please.
Thank you!

# Action History
- Created by: mahmoodn | 2018-10-19T10:45:53+00:00
- Closed at: 2021-04-12T15:55:55+00:00
