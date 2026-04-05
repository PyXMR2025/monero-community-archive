---
title: 'read error: "end of file"'
source_url: https://github.com/xmrig/xmrig/issues/1013
author: mahmoodn
assignees: []
labels: []
created_at: '2019-04-17T19:56:06+00:00'
updated_at: '2019-08-02T11:53:40+00:00'
type: issue
status: closed
closed_at: '2019-08-02T11:53:40+00:00'
---

# Original Description
I recently, get this error with 2.14.1
```
$ ./xmrig 
 * ABOUT        XMRig/2.14.1 gcc/7.3.0
 * LIBS         libuv/1.18.0 OpenSSL/1.1.0g microhttpd/0.9.59 
 * CPU          AMD Ryzen 7 1800X Eight-Core Processor          (1) x64 AES AVX2
 * CPU L2/L3    4.0 MB/16.0 MB
 * THREADS      8, cryptonight, donate=5%
 * ASSEMBLY     auto:ryzen
 * POOL #1      xmr.coinfoundry.org:3033 variant auto
 * COMMANDS     hashrate, pause, resume
[2019-04-18 00:20:17] READY (CPU) threads 8(8) huge pages 0/8 0% memory 16384 KB
[2019-04-18 00:20:26] [xmr.coinfoundry.org:3033] read error: "end of file"
[2019-04-18 00:21:20] speed 10s/60s/15m n/a n/a n/a H/s max n/a H/s
```
However, I can ping as below
```
$ ping coinfoundry.org
PING coinfoundry.org (159.69.212.210) 56(84) bytes of data.
64 bytes from static.210.212.69.159.clients.your-server.de (159.69.212.210): icmp_seq=1 ttl=45 time=117 ms
^C
--- coinfoundry.org ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 117.635/117.635/117.635/0.000 ms
$ ping xmr.coinfoundry.org
PING xmr.coinfoundry.org (159.69.212.211) 56(84) bytes of data.
64 bytes from static.211.212.69.159.clients.your-server.de (159.69.212.211): icmp_seq=1 ttl=45 time=115 ms
64 bytes from static.211.212.69.159.clients.your-server.de (159.69.212.211): icmp_seq=2 ttl=45 time=114 ms
^C
--- xmr.coinfoundry.org ping statistics ---
2 packets transmitted, 2 received, 0% packet loss, time 1001ms
rtt min/avg/max/mdev = 114.828/115.015/115.203/0.387 ms
```
What is wrong with that?

# Discussion History
## Spudz76 | 2019-04-20T06:37:24+00:00
try `telnet xmr.coinfoundry.org 3033` and I bet it hangs up on you without saying anything
thus EOF (end of connection, no data)

ICMP is meaningless

## mahmoodn | 2019-04-21T07:53:01+00:00
The connection got closed

```
$ telnet xmr.coinfoundry.org 3033
Trying 159.69.212.211...
Connected to xmr.coinfoundry.org.
Escape character is '^]'.
Connection closed by foreign host.
$ telnet xmr.coinfoundry.org 3033
Trying 159.69.212.211...
Connected to xmr.coinfoundry.org.
Escape character is '^]'.
ehlo coinfoundry.org
Connection closed by foreign host.
```

# Action History
- Created by: mahmoodn | 2019-04-17T19:56:06+00:00
- Closed at: 2019-08-02T11:53:40+00:00
