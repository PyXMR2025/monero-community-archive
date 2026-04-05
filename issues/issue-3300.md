---
title: Re-enable TCP keepalive support on Windows
source_url: https://github.com/xmrig/xmrig/issues/3300
author: koitsu
assignees: []
labels: []
created_at: '2023-07-16T23:12:33+00:00'
updated_at: '2023-08-07T03:31:43+00:00'
type: issue
status: closed
closed_at: '2023-08-07T02:00:04+00:00'
---

# Original Description
The current version of XMRig has TCP keepalive support disabled for Windows: https://github.com/xmrig/xmrig/commit/91ed7e36cd109714ed2c7bdace4986984a7ad34e

The commit message is from 6 years ago and cites TCP keepalive behaviour (via libuv) not working as intended/designed.  This is quite understandable given [how XP/2K behaved](https://learn.microsoft.com/en-us/windows/win32/winsock/so-keepalive).

However, we're now in 2023, and Windows 7 is the "oldest" OS commonly around the Internet now.  I myself only switched from W7 to W10 this year.

Would it be possible to re-enable libuv TCP keepalive support, or possibly change the `#ifndef` to utilise [WINVER/other defines](https://learn.microsoft.com/en-us/cpp/porting/modifying-winver-and-win32-winnt?view=msvc-170) to ensure the feature is only enabled on Windows 7 or newer?  This might only work on MSVC builds (unsure about gcc).

If XMRig devs still want to support Windows XP (that's fine!), then we can close this ticket.

Otherwise, as for testing: the only pool I know which supports TCP keepalives for certain is Zergpool when used alongside their TLS/SSL endpoints.  Their TLS proxy (haproxy) uses `option clitcpka` ([documentation](https://cbonte.github.io/haproxy-dconv/1.8/configuration.html#4-option%20clitcpka)).  I know because I've been helping them get TLS/SSL working again in recent days and been doing a bit of packet captures.  Unsure if their plaintext endpoints support it or not.

# Discussion History
## koitsu | 2023-07-19T05:08:07+00:00
Thank you so much!  Will be happy to try this out during next release, or if there's a nightly release I can give it a shot.

## koitsu | 2023-08-06T01:47:30+00:00
@SChernykh Looks like this is working, but may have an edge-case bug somewhere.  I'm testing using [xmrig-6.20.1-dev-msvc-win64.zip from commit ](https://download.xmrig.com/xmrig/6.20.1-dev/64f5bb467ac831d1d8aae306048299e7e6984675/xmrig-6.20.1-dev-msvc-win64.zip) as a binary.

Client: 192.168.1.50 (Windows 10 Pro 22H2 19045.3208)
Pool: 103.249.70.7 (Zergpool anycast, plaintext)

Relevant XMRig `pool` config:

```
    "pools": [
        {
            /* TESTING TESTING TESTING GR on Zergpool */
            "enabled": true,
            "algo": "gr",
            "url": "stratum+tcp://ghostrider.mine.zergpool.com:5354",
            "user": "XXX",
            "pass": "XXX"
        },
        ...
    ]
```

Packet capture:

```
No.     Time               Source                sport  Destination           dport  Protocol Length Info
      1 18:12:37.933782    192.168.1.50          65270  103.249.70.7          5354   TCP      66     65270 → 5354 [SYN] Seq=0 Win=64240 Len=0 MSS=1460 WS=256 SACK_PERM
      2 18:12:38.943545    192.168.1.50          65270  103.249.70.7          5354   TCP      66     [TCP Retransmission] 65270 → 5354 [SYN] Seq=0 Win=64240 Len=0 MSS=1460 WS=256 SACK_PERM
      3 18:12:40.958263    192.168.1.50          65270  103.249.70.7          5354   TCP      66     [TCP Retransmission] 65270 → 5354 [SYN] Seq=0 Win=64240 Len=0 MSS=1460 WS=256 SACK_PERM
      4 18:12:44.969204    192.168.1.50          65270  103.249.70.7          5354   TCP      66     [TCP Retransmission] 65270 → 5354 [SYN] Seq=0 Win=64240 Len=0 MSS=1460 WS=256 SACK_PERM
      5 18:12:52.971240    192.168.1.50          65270  103.249.70.7          5354   TCP      66     [TCP Retransmission] 65270 → 5354 [SYN] Seq=0 Win=64240 Len=0 MSS=1460 WS=256 SACK_PERM
      6 18:13:03.094888    192.168.1.50          65271  103.249.70.7          5354   TCP      66     65271 → 5354 [SYN] Seq=0 Win=64240 Len=0 MSS=1460 WS=256 SACK_PERM
      7 18:13:03.283991    103.249.70.7          5354   192.168.1.50          65271  TCP      66     5354 → 65271 [SYN, ACK] Seq=0 Ack=1 Win=65535 Len=0 MSS=1396 SACK_PERM WS=4096
      8 18:13:03.284098    192.168.1.50          65271  103.249.70.7          5354   TCP      54     65271 → 5354 [ACK] Seq=1 Ack=1 Win=262400 Len=0
      9 18:13:03.284234    192.168.1.50          65271  103.249.70.7          5354   TCP      190    65271 → 5354 [PSH, ACK] Seq=1 Ack=1 Win=262400 Len=136
     10 18:13:03.284287    192.168.1.50          65271  103.249.70.7          5354   TCP      203    65271 → 5354 [PSH, ACK] Seq=137 Ack=1 Win=262400 Len=149
     11 18:13:03.472298    103.249.70.7          5354   192.168.1.50          65271  TCP      60     5354 → 65271 [ACK] Seq=1 Ack=137 Win=65536 Len=0
     12 18:13:03.472351    103.249.70.7          5354   192.168.1.50          65271  TCP      60     5354 → 65271 [ACK] Seq=1 Ack=286 Win=65536 Len=0
     13 18:13:03.472428    103.249.70.7          5354   192.168.1.50          65271  TCP      187    5354 → 65271 [PSH, ACK] Seq=1 Ack=286 Win=65536 Len=133
     14 18:13:03.524825    192.168.1.50          65271  103.249.70.7          5354   TCP      54     65271 → 5354 [ACK] Seq=286 Ack=134 Win=262144 Len=0
     15 18:13:03.719020    103.249.70.7          5354   192.168.1.50          65271  TCP      948    5354 → 65271 [PSH, ACK] Seq=134 Ack=286 Win=65536 Len=894
     16 18:13:03.760746    192.168.1.50          65271  103.249.70.7          5354   TCP      54     65271 → 5354 [ACK] Seq=286 Ack=1028 Win=261376 Len=0
     17 18:13:31.025954    192.168.1.50          65271  103.249.70.7          5354   TCP      194    65271 → 5354 [PSH, ACK] Seq=286 Ack=1028 Win=261376 Len=140
     18 18:13:31.254419    103.249.70.7          5354   192.168.1.50          65271  TCP      90     5354 → 65271 [PSH, ACK] Seq=1028 Ack=426 Win=65536 Len=36
     19 18:13:31.382886    192.168.1.50          65271  103.249.70.7          5354   TCP      54     65271 → 5354 [ACK] Seq=426 Ack=1064 Win=261376 Len=0
     20 18:13:46.265952    103.249.70.7          5354   192.168.1.50          65271  TCP      852    5354 → 65271 [PSH, ACK] Seq=1064 Ack=426 Win=65536 Len=798
     21 18:13:46.375765    192.168.1.50          65271  103.249.70.7          5354   TCP      54     65271 → 5354 [ACK] Seq=426 Ack=1862 Win=262400 Len=0
     22 18:14:00.055853    192.168.1.50          65271  103.249.70.7          5354   TCP      54     65271 → 5354 [FIN, ACK] Seq=426 Ack=1862 Win=262400 Len=0
     23 18:14:00.286284    103.249.70.7          5354   192.168.1.50          65271  TCP      60     5354 → 65271 [ACK] Seq=1862 Ack=427 Win=65536 Len=0
     24 18:15:00.296674    192.168.1.50          65271  103.249.70.7          5354   TCP      55     [TCP Keep-Alive] 65271 → 5354 [ACK] Seq=426 Ack=1862 Win=262400 Len=1
     25 18:15:01.298465    192.168.1.50          65271  103.249.70.7          5354   TCP      55     [TCP Keep-Alive] 65271 → 5354 [ACK] Seq=426 Ack=1862 Win=262400 Len=1
     26 18:15:02.300870    192.168.1.50          65271  103.249.70.7          5354   TCP      55     [TCP Keep-Alive] 65271 → 5354 [ACK] Seq=426 Ack=1862 Win=262400 Len=1
     27 18:15:03.316199    192.168.1.50          65271  103.249.70.7          5354   TCP      55     [TCP Keep-Alive] 65271 → 5354 [ACK] Seq=426 Ack=1862 Win=262400 Len=1
     28 18:15:04.327034    192.168.1.50          65271  103.249.70.7          5354   TCP      55     [TCP Keep-Alive] 65271 → 5354 [ACK] Seq=426 Ack=1862 Win=262400 Len=1
     29 18:15:05.341897    192.168.1.50          65271  103.249.70.7          5354   TCP      55     [TCP Keep-Alive] 65271 → 5354 [ACK] Seq=426 Ack=1862 Win=262400 Len=1
     30 18:15:06.344737    192.168.1.50          65271  103.249.70.7          5354   TCP      55     [TCP Keep-Alive] 65271 → 5354 [ACK] Seq=426 Ack=1862 Win=262400 Len=1
     31 18:15:07.360062    192.168.1.50          65271  103.249.70.7          5354   TCP      55     [TCP Keep-Alive] 65271 → 5354 [ACK] Seq=426 Ack=1862 Win=262400 Len=1
     32 18:15:08.361890    192.168.1.50          65271  103.249.70.7          5354   TCP      55     [TCP Keep-Alive] 65271 → 5354 [ACK] Seq=426 Ack=1862 Win=262400 Len=1
     33 18:15:09.364267    192.168.1.50          65271  103.249.70.7          5354   TCP      55     [TCP Keep-Alive] 65271 → 5354 [ACK] Seq=426 Ack=1862 Win=262400 Len=1
     34 18:15:10.364668    192.168.1.50          65271  103.249.70.7          5354   TCP      54     65271 → 5354 [RST, ACK] Seq=427 Ack=1862 Win=0 Len=0
```

Around packet 22, I hit Ctrl-C in XMrig.  You can clearly see the clean socket shutdown (TCP FIN+ACK from client, followed by TCP ACK from server).  XMRig executable exited shortly after packet 23.  This is all good.

But as shown in packets 24 through 34, Windows does not seem to be aware that this socket has been closed and tries to send TCP keepalive packets to a socket long gone.  The number of keepalives is 10, which [just so happens to match what the default count is for libuv](https://ant.readthedocs.io/en/latest/tcp.html#c.uv_tcp_keepalive).  The interval is 60 seconds, which is what XMRig chose.

What I suspect is happening is that XMRig (on quit) is not telling libuv "I'm done with these sockets, please stop doing TCP keepalives", which would in turn cause libuv to tell the Windows kernel/TCP stack to cease TCP keepalive timers on these sockets.  (Yes, sockets in the TCP table ARE kept around for a while after closure!  TIME_WAIT and TCP keepalive timers are two things that keep them around.)

libuv documentation on this is unclear.  What makes absolutely no sense is that the libuv documentation says (emphasis mine):

> Enable / disable TCP keep-alive. delay is the initial delay in seconds, **ignored when enable is zero.**

What is the purpose of the argument then?  What I suspect is that the `enable` argument allows you to enable/disable TCP keepalives on a libuv TCP handle. https://github.com/libuv/libuv/issues/3487 implies this as well (look at some example code provided), though that Issue is about people doing awful things like setting the interval to 0 (do not do that!).  Everything I see in that thread implies enable=0 allows you to *disable* TCP keepalive on an existing TCP handle

So in turn, we must to look at the libuv code itself.  https://github.com/libuv/libuv/blob/v1.x/src/win/tcp.c#L52-L70 looks to me like it will use the enable argument unconditionally when calling [Win32 setsockopt()](https://learn.microsoft.com/en-us/windows/win32/api/winsock/nf-winsock-setsockopt) the first time, which should allow for one to disable TCP keepalives on a socket.  [Microsoft's own documentation](https://learn.microsoft.com/en-us/windows/win32/winsock/so-keepalive) states that the underlying optval is treated as a boolean of sorts, and 0/FALSE is to disable keepalives on an existing socket.

In other words: **the libuv documentation is wrong when it says "ignored when enable is zero".**  What they're trying to say is that the **delay** argument is ignored when enable=0, but the documentation is poorly worded.  A better phrasing:

> Enable / disable TCP keep-alive. delay is the initial delay in seconds and only affects the handle when enable set to 1.

If you could add some code to iterate over all your TCP handles and issue `uv_tcp_keepalive(handle, 0, 60);` on them when XMRig is shut down, I suspect this bug will go away.  (And yes, please be sure to keep the timer value at 60 when disabling!  That libuv GH Issue talks about this.  You should probably make that a #define somewhere since it'll be used in more than one place.)

## SChernykh | 2023-08-06T12:53:35+00:00
@koitsu https://github.com/xmrig/xmrig/pull/3312 should fix it.

## koitsu | 2023-08-07T01:59:55+00:00
@SChernykh Thanks, I can verify #3312 does fix it!  There is a different problem unrelated to TCP keepalives I've found in the process, but will open a separate ticket for that one.

Edit: regarding my last statement: after a few hours of deep analysis I believe the problem is on the server/pool side.  Client sends FIN+ACK, server/pool sends ACK, but then the server/pool never follows up with a subsequent FIN or FIN+ACK.  This results in, post-XMRig-exit, the client's TCP stack having a socket in FIN_WAIT2 state until the kernel reaps it.  And on Windows, this also results in its TCP stack sending a TCP RST+ACK to the server.  I'll need to talk with the pool owner about this, as it's behaviour I see on both their plaintext and TLS/SSL endpoints.

# Action History
- Created by: koitsu | 2023-07-16T23:12:33+00:00
- Closed at: 2023-08-07T02:00:04+00:00
