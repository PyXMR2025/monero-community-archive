---
title: monerod throws a lot of exceptions and slows down synchronization till almost
  complete halt.
source_url: https://github.com/monero-project/monero/issues/8132
author: blacklion
assignees: []
labels: []
created_at: '2022-01-06T08:51:37+00:00'
updated_at: '2026-04-30T18:35:57+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
I'm trying to use `monerod` version 0.17.3.0 on FreeBSD 12 (amd64/x86_64).

I need to synchronize 5+ months worth of blockchain.

`monerod` starts to synchronize and shows good progress right after start, but then these exceptions start to occur:

```
2021-12-31 09:51:23.103 [P2P0]  INFO    stacktrace      src/common/stack_trace.cpp:134  Exception: boost::wrapexcept<boost::bad_weak_ptr>
2021-12-31 09:51:23.103 [P2P0]  INFO    stacktrace      src/common/stack_trace.cpp:135  Unwound call stack:
2021-12-31 09:51:24.076 [P2P0]  INFO    stacktrace      src/common/stack_trace.cpp:159       1                  0x1a1254e
2021-12-31 09:51:25.054 [P2P0]  INFO    stacktrace      src/common/stack_trace.cpp:159       2                  0x1456c5c
2021-12-31 09:51:26.033 [P2P0]  INFO    stacktrace      src/common/stack_trace.cpp:159       3                  0x17f187e
2021-12-31 09:51:27.011 [P2P0]  INFO    stacktrace      src/common/stack_trace.cpp:159       4                  0x17e6ae7
2021-12-31 09:51:27.987 [P2P0]  INFO    stacktrace      src/common/stack_trace.cpp:159       5                  0x17970c4
2021-12-31 09:51:28.970 [P2P0]  INFO    stacktrace      src/common/stack_trace.cpp:159       6                  0x1793902
2021-12-31 09:51:29.943 [P2P0]  INFO    stacktrace      src/common/stack_trace.cpp:159       7                  0x178e197
2021-12-31 09:51:30.914 [P2P0]  INFO    stacktrace      src/common/stack_trace.cpp:159       8                  0x1786f87
2021-12-31 09:51:31.892 [P2P0]  INFO    stacktrace      src/common/stack_trace.cpp:159       9                  0x1760c57
2021-12-31 09:51:32.856 [P2P0]  INFO    stacktrace      src/common/stack_trace.cpp:159       a                  0x17e7383
2021-12-31 09:51:33.838 [P2P0]  INFO    stacktrace      src/common/stack_trace.cpp:159       b                  0x17e7e85
2021-12-31 09:51:34.813 [P2P0]  INFO    stacktrace      src/common/stack_trace.cpp:159       c                  0x17e797c
2021-12-31 09:51:35.779 [P2P0]  INFO    stacktrace      src/common/stack_trace.cpp:159       d                  0x1431df1
2021-12-31 09:51:36.745 [P2P0]  INFO    stacktrace      src/common/stack_trace.cpp:159       e                  0x14318b1
2021-12-31 09:51:37.720 [P2P0]  INFO    stacktrace      src/common/stack_trace.cpp:159       f                  0x17e919a
2021-12-31 09:51:38.679 [P2P0]  INFO    stacktrace      src/common/stack_trace.cpp:159      10                  0x80260b5ca
2021-12-31 09:51:39.649 [P2P0]  INFO    stacktrace      src/common/stack_trace.cpp:159      11                  0x8027aa08c
2021-12-31 09:51:40.609 [P2P0]  INFO    stacktrace      src/common/stack_trace.cpp:159      12                  0x0
2021-12-31 09:51:40.610 [P2P0]  INFO    stacktrace      src/common/stack_trace.cpp:149  Failed to find the next frame
```

Exceptions become more and more frequent, and after ~2 hours (sometimes less sometimes more) or so `monerod` consumes 100% (!) of one core printing out exceptions one after another and stops to make any synchronization progress. At the beginning `monerod` consumes only 1-2% of one core.

Please note, that `monerod` logs stacktrace one frame per second (!).

I've seen issue #6473 and tired to enable 1.25GB (1280 large pages) of locked memory for monerod, but it doesn't help a lot, only defer exceptions for 30-45 minutes from daemon's start.

Log of sync progress and exceptions looks like this (all other lines are stripped) is here: [monerod.flt.log](https://github.com/monero-project/monero/files/7820556/monerod.flt.log).

NB: I've tried to build debug build, but it fails to install all shared libraries and doesn't work at all, so stacktraces doesn't have function names.


# Discussion History
## blacklion | 2022-01-06T19:38:09+00:00
Debug build doesn't show names in stacktrace either, and works exactly as release build, with same problems.

## selsta | 2022-01-06T19:39:18+00:00
Seems like something related to FreeBSD. It definitely shows on Linux for both release and debug build.

## blacklion | 2022-01-06T19:41:27+00:00
Yes, maybe `libunwind` has bug on FreeBSD, I need to explore this more, but I don't think it is monero-related.

Tough, my problem not incomplete stacktraces, but a lot of exceptions.

## yekm | 2022-02-26T07:51:07+00:00
Almost the same behavior in archlinux with community/monero 0.17.3.0-3
I've managed to filer out date-time and blocks left from monerod.log:
`cat /var/log/monero/monero.log | grep left | cut -f 1,6 | cut -f1,2,5 -d' ' | tr -d 'Synced' | sed 's/\t /./' | cut -f 1,3 -d. | tr . , | gnuplot -p -e "set timefmt '%Y-%m-%d %H:%M:%S'; set datafile separator ','; set xdata time; plot '-' using 1:2 with d"`
![monero left](https://user-images.githubusercontent.com/205196/155835059-48d38a80-4c6c-4012-aa3d-1eafc6b564f7.png)

```
cat /var/log/monero/monero.log | grep Exception | wc -l
253
```

## selsta | 2022-02-26T07:53:42+00:00
@yekm What behavior exactly? Just exceptions? Can you post one of them?

Sync slowing down at the end is normal.

## yekm | 2022-02-26T08:01:22+00:00
> @yekm What behavior exactly? Just exceptions? Can you post one of them?

No symbols in default package.
I skimmed through original comment in this issue and missed th eline about 100% cpu consumption just to print exceptions. This is not my case.

> Sync slowing down at the end is normal.

Well, I guess my situation is normal then.


## selsta | 2022-02-26T16:51:43+00:00
It's possible that the arch package is compiled without libunwind.

## godfuture | 2022-11-02T22:09:21+00:00
Excatly same issue for me on docker image (https://github.com/sethforprivacy/simple-monerod-docker) on x64 debian 10.

> It's possible that the arch package is compiled without libunwind.

At least for my case I can say that I saw in the docker file of the image above libunwind being part of the build.

## max-ishere | 2023-10-09T19:31:36+00:00
Im having the same issue. The first few `bad_weak_ptr` exceptions happened around 20K block, then they kept going with different frequency (2K blocks - 100K blocks) and now after around 2 andsomething M blocks it is more like a wall of exceptions and a few `Synced` messages in between. It also got extremly slow (was 88% yesterday, 89% today). Im on `2691801/2992301` rn.

I have tried the `sudo sysctl -w vm.nr_hugepages=1280` and restarted monerod, set `public-node=0` but it still keeps happening. idk what should I do, but accept the slowness of it all.

```text
2023-10-09 19:24:31.282 [P2P1]  INFO    stacktrace  src/common/stack_trace.cpp:133  Exception: boost::wrapexcept<boost::bad_weak_ptr>
2023-10-09 19:24:31.282 [P2P1]  INFO    stacktrace  src/common/stack_trace.cpp:134  Unwound call stack:
2023-10-09 19:24:31.282 [P2P1]  INFO    stacktrace  src/common/stack_trace.cpp:172      [1] /usr/bin/monerod(+0x13b978) [0x26a9baf1978] 
2023-10-09 19:24:31.282 [P2P1]  INFO    stacktrace  src/common/stack_trace.cpp:172      [2] /usr/bin/monerod(+0xb202d) [0x26a9ba6802d] 
2023-10-09 19:24:31.282 [P2P1]  INFO    stacktrace  src/common/stack_trace.cpp:172      [3] /usr/bin/monerod(+0x31d4ed) [0x26a9bcd34ed] 
2023-10-09 19:24:31.282 [P2P1]  INFO    stacktrace  src/common/stack_trace.cpp:172      [4] /usr/bin/monerod(+0x34b129) [0x26a9bd01129] 
2023-10-09 19:24:31.282 [P2P1]  INFO    stacktrace  src/common/stack_trace.cpp:172      [5] /usr/bin/monerod(+0x649f20) [0x26a9bffff20] 
2023-10-09 19:24:31.282 [P2P1]  INFO    stacktrace  src/common/stack_trace.cpp:172      [6] /usr/bin/monerod(+0x333d02) [0x26a9bce9d02] 
2023-10-09 19:24:31.282 [P2P1]  INFO    stacktrace  src/common/stack_trace.cpp:172      [7] /usr/bin/monerod(+0x39251a) [0x26a9bd4851a] 
2023-10-09 19:24:31.282 [P2P1]  INFO    stacktrace  src/common/stack_trace.cpp:172      [8] /usr/bin/monerod(+0x187ca5) [0x26a9bb3dca5] 
2023-10-09 19:24:31.282 [P2P1]  INFO    stacktrace  src/common/stack_trace.cpp:172      [9] /usr/bin/monerod(+0x5bfce7) [0x26a9bf75ce7] 
2023-10-09 19:24:31.282 [P2P1]  INFO    stacktrace  src/common/stack_trace.cpp:172      [10] /usr/bin/monerod(+0x359113) [0x26a9bd0f113] 
2023-10-09 19:24:31.282 [P2P1]  INFO    stacktrace  src/common/stack_trace.cpp:172      [11]  0x12f2b) [0x6986db39cf2b]:_thread.so.1.83.0(+0x12f2b) [0x6986db39cf2b]
2023-10-09 19:24:31.282 [P2P1]  INFO    stacktrace  src/common/stack_trace.cpp:172      [12] /usr/lib/libc.so.6(+0x8c9eb) [0x6986da8aa9eb] 
2023-10-09 19:24:31.282 [P2P1]  INFO    stacktrace  src/common/stack_trace.cpp:172      [13] /usr/lib/libc.so.6(+0x1107cc) [0x6986da92e7cc] 
2023-10-09 19:24:31.282 [P2P1]  INFO    stacktrace  src/common/stack_trace.cpp:172  
```

## max-ishere | 2023-10-10T19:35:12+00:00
I've turned the log level to 1 (0=low, 4=high) and from what I can see after a few minutes of running it I notice that the exceptions occur next to this:

<details>
<summary>Level 1 log</summary>

```
2023-10-10 19:07:00.032 [P2P8]  INFO    net contrib/epee/include/net/levin_protocol_handler_async.h:214 [193.142.4.248:18180 OUT] Timeout on invoke operation happened, command: 1001 timeout: 5000
2023-10-10 19:07:00.032 [P2P8]  INFO    net contrib/epee/include/storages/levin_abstract_invoke2.h:101  Failed to invoke command 1001 return code -4
2023-10-10 19:07:00.032 [P2P8]  WARNING net.p2p src/p2p/net_node.inl:1163   [193.142.4.248:18180 OUT] COMMAND_HANDSHAKE invoke failed. (-4, LEVIN_ERROR_CONNECTION_TIMEDOUT)
2023-10-10 19:07:00.032 [P2P0]  WARNING net.p2p src/p2p/net_node.inl:1222   [193.142.4.248:18180 OUT] COMMAND_HANDSHAKE Failed
2023-10-10 19:07:00.032 [P2P0]  INFO    net.p2p src/p2p/net_node.inl:1413   [193.142.4.248:18180 OUT] Failed to HANDSHAKE with peer 193.142.4.248:18180
2023-10-10 19:07:00.032 [P2P2]  INFO    net.cn  src/cryptonote_protocol/cryptonote_protocol_handler.inl:2200    [98.13.211.103:18080 OUT] [0] state: pausing in state standby
2023-10-10 19:07:00.033 [P2P4]  INFO    net.cn  src/cryptonote_protocol/cryptonote_protocol_handler.inl:2200    [80.44.29.8:18080 OUT] [0] state: pausing in state standby
2023-10-10 19:07:00.033 [P2P0]  INFO    stacktrace  src/common/stack_trace.cpp:133  Exception: boost::wrapexcept<boost::bad_weak_ptr>
2023-10-10 19:07:00.033 [P2P0]  INFO    stacktrace  src/common/stack_trace.cpp:134  Unwound call stack:
2023-10-10 19:07:00.033 [P2P6]  INFO    net.cn  src/cryptonote_protocol/cryptonote_protocol_handler.inl:2200    [79.160.202.11:18080 OUT] [184] state: pausing in state standby
2023-10-10 19:07:00.033 [P2P4]  INFO    net.p2p.traffic contrib/epee/include/net/levin_protocol_handler_async.h:56  [46.173.227.107:18080 OUT] 13020 bytes received for category command-2002 initiated by peer
2023-10-10 19:07:00.033 [P2P4]  INFO    net.p2p.msg src/cryptonote_protocol/cryptonote_protocol_handler.inl:981 [46.173.227.107:18080 OUT] Received NOTIFY_NEW_TRANSACTIONS (4 txes)
2023-10-10 19:07:00.033 [P2P0]  INFO    stacktrace  src/common/stack_trace.cpp:172      [1] /usr/bin/monerod(+0x13b978) [0xf10b1fb2978] 
2023-10-10 19:07:00.033 [P2P0]  INFO    stacktrace  src/common/stack_trace.cpp:172      [2] /usr/bin/monerod(+0xb202d) [0xf10b1f2902d] 
2023-10-10 19:07:00.033 [P2P0]  INFO    stacktrace  src/common/stack_trace.cpp:172      [3] /usr/bin/monerod(+0x65cab1) [0xf10b24d3ab1] 
2023-10-10 19:07:00.033 [P2P0]  INFO    stacktrace  src/common/stack_trace.cpp:172      [4] /usr/bin/monerod(+0x329066) [0xf10b21a0066] 
2023-10-10 19:07:00.033 [P2P0]  INFO    stacktrace  src/common/stack_trace.cpp:172      [5] /usr/bin/monerod(+0x315a1a) [0xf10b218ca1a] 
2023-10-10 19:07:00.033 [P2P0]  INFO    stacktrace  src/common/stack_trace.cpp:172      [6] /usr/bin/monerod(+0x354691) [0xf10b21cb691] 
2023-10-10 19:07:00.033 [P2P0]  INFO    stacktrace  src/common/stack_trace.cpp:172      [7] /usr/bin/monerod(+0x36f9ac) [0xf10b21e69ac] 
2023-10-10 19:07:00.033 [P2P0]  INFO    stacktrace  src/common/stack_trace.cpp:172      [8] /usr/bin/monerod(+0x5bfce7) [0xf10b2436ce7] 
2023-10-10 19:07:00.033 [P2P0]  INFO    stacktrace  src/common/stack_trace.cpp:172      [9] /usr/bin/monerod(+0x359113) [0xf10b21d0113] 
2023-10-10 19:07:00.033 [P2P0]  INFO    stacktrace  src/common/stack_trace.cpp:172      [10]  0x12f2b) [0x6f86c9dc9f2b]:_thread.so.1.83.0(+0x12f2b) [0x6f86c9dc9f2b]
2023-10-10 19:07:00.033 [P2P0]  INFO    stacktrace  src/common/stack_trace.cpp:172      [11] /usr/lib/libc.so.6(+0x8c9eb) [0x6f86c92aa9eb] 
2023-10-10 19:07:00.033 [P2P0]  INFO    stacktrace  src/common/stack_trace.cpp:172      [12] /usr/lib/libc.so.6(+0x1107cc) [0x6f86c932e7cc] 
2023-10-10 19:07:00.033 [P2P0]  INFO    stacktrace  src/common/stack_trace.cpp:172  
2023-10-10 19:07:00.033 [P2P0]  ERROR   net contrib/epee/include/net/levin_protocol_handler_async.h:351 [193.142.4.248:18180 OUT] [levin_protocol] -->> start_outer_call failed
2023-10-10 19:07:00.033 [P2P0]  INFO    stacktrace  src/common/stack_trace.cpp:133  Exception: boost::wrapexcept<boost::bad_weak_ptr>
2023-10-10 19:07:00.033 [P2P0]  INFO    stacktrace  src/common/stack_trace.cpp:134  Unwound call stack:
2023-10-10 19:07:00.033 [P2P0]  INFO    stacktrace  src/common/stack_trace.cpp:172      [1] /usr/bin/monerod(+0x13b978) [0xf10b1fb2978] 
2023-10-10 19:07:00.033 [P2P0]  INFO    stacktrace  src/common/stack_trace.cpp:172      [2] /usr/bin/monerod(+0xb202d) [0xf10b1f2902d] 
2023-10-10 19:07:00.033 [P2P0]  INFO    stacktrace  src/common/stack_trace.cpp:172      [3] /usr/bin/monerod(+0x31d4ed) [0xf10b21944ed] 
2023-10-10 19:07:00.033 [P2P4]  INFO    net.p2p.msg src/cryptonote_protocol/cryptonote_protocol_handler.inl:983 Including transaction <bfe25102db85aee541ac4414e854e5c740124ca2d46427b4d1903f9a054d5527>
2023-10-10 19:07:00.033 [P2P0]  INFO    stacktrace  src/common/stack_trace.cpp:172      [4] /usr/bin/monerod(+0x33430f) [0xf10b21ab30f] 
2023-10-10 19:07:00.033 [P2P0]  INFO    stacktrace  src/common/stack_trace.cpp:172      [5] /usr/bin/monerod(+0x329091) [0xf10b21a0091] 
2023-10-10 19:07:00.033 [P2P0]  INFO    stacktrace  src/common/stack_trace.cpp:172      [6] /usr/bin/monerod(+0x315a1a) [0xf10b218ca1a] 
2023-10-10 19:07:00.033 [P2P0]  INFO    stacktrace  src/common/stack_trace.cpp:172      [7] /usr/bin/monerod(+0x354691) [0xf10b21cb691] 
2023-10-10 19:07:00.033 [P2P0]  INFO    stacktrace  src/common/stack_trace.cpp:172      [8] /usr/bin/monerod(+0x36f9ac) [0xf10b21e69ac] 
2023-10-10 19:07:00.034 [P2P0]  INFO    stacktrace  src/common/stack_trace.cpp:172      [9] /usr/bin/monerod(+0x5bfce7) [0xf10b2436ce7] 
2023-10-10 19:07:00.034 [P2P0]  INFO    stacktrace  src/common/stack_trace.cpp:172      [10] /usr/bin/monerod(+0x359113) [0xf10b21d0113] 
2023-10-10 19:07:00.034 [P2P0]  INFO    stacktrace  src/common/stack_trace.cpp:172      [11]  0x12f2b) [0x6f86c9dc9f2b]:_thread.so.1.83.0(+0x12f2b) [0x6f86c9dc9f2b]
2023-10-10 19:07:00.034 [P2P0]  INFO    stacktrace  src/common/stack_trace.cpp:172      [12] /usr/lib/libc.so.6(+0x8c9eb) [0x6f86c92aa9eb] 
2023-10-10 19:07:00.034 [P2P0]  INFO    stacktrace  src/common/stack_trace.cpp:172      [13] /usr/lib/libc.so.6(+0x1107cc) [0x6f86c932e7cc] 
2023-10-10 19:07:00.034 [P2P0]  INFO    stacktrace  src/common/stack_trace.cpp:172  
2023-10-10 19:07:00.034 [P2P0]  ERROR   net contrib/epee/include/net/levin_protocol_handler_async.h:351 [193.142.4.248:18180 OUT] [levin_protocol] -->> start_outer_call failed
2023-10-10 19:07:00.034 [P2P0]  INFO    stacktrace  src/common/stack_trace.cpp:133  Exception: boost::wrapexcept<boost::bad_weak_ptr>
2023-10-10 19:07:00.034 [P2P0]  INFO    stacktrace  src/common/stack_trace.cpp:134  Unwound call stack:
2023-10-10 19:07:00.034 [P2P0]  INFO    stacktrace  src/common/stack_trace.cpp:172      [1] /usr/bin/monerod(+0x13b978) [0xf10b1fb2978] 
2023-10-10 19:07:00.034 [P2P0]  INFO    stacktrace  src/common/stack_trace.cpp:172      [2] /usr/bin/monerod(+0xb202d) [0xf10b1f2902d] 
2023-10-10 19:07:00.034 [P2P0]  INFO    stacktrace  src/common/stack_trace.cpp:172      [3] /usr/bin/monerod(+0x65cab1) [0xf10b24d3ab1] 
2023-10-10 19:07:00.034 [P2P0]  INFO    stacktrace  src/common/stack_trace.cpp:172      [4] /usr/bin/monerod(+0x3290ab) [0xf10b21a00ab] 
2023-10-10 19:07:00.034 [P2P0]  INFO    stacktrace  src/common/stack_trace.cpp:172      [5] /usr/bin/monerod(+0x315a1a) [0xf10b218ca1a] 
2023-10-10 19:07:00.034 [P2P0]  INFO    stacktrace  src/common/stack_trace.cpp:172      [6] /usr/bin/monerod(+0x354691) [0xf10b21cb691] 
2023-10-10 19:07:00.034 [P2P0]  INFO    stacktrace  src/common/stack_trace.cpp:172      [7] /usr/bin/monerod(+0x36f9ac) [0xf10b21e69ac] 
2023-10-10 19:07:00.034 [P2P0]  INFO    stacktrace  src/common/stack_trace.cpp:172      [8] /usr/bin/monerod(+0x5bfce7) [0xf10b2436ce7] 
2023-10-10 19:07:00.034 [P2P0]  INFO    stacktrace  src/common/stack_trace.cpp:172      [9] /usr/bin/monerod(+0x359113) [0xf10b21d0113] 
2023-10-10 19:07:00.034 [P2P0]  INFO    stacktrace  src/common/stack_trace.cpp:172      [10]  0x12f2b) [0x6f86c9dc9f2b]:_thread.so.1.83.0(+0x12f2b) [0x6f86c9dc9f2b]
2023-10-10 19:07:00.034 [P2P0]  INFO    stacktrace  src/common/stack_trace.cpp:172      [11] /usr/lib/libc.so.6(+0x8c9eb) [0x6f86c92aa9eb] 
2023-10-10 19:07:00.034 [P2P0]  INFO    stacktrace  src/common/stack_trace.cpp:172      [12] /usr/lib/libc.so.6(+0x1107cc) [0x6f86c932e7cc] 
2023-10-10 19:07:00.034 [P2P0]  INFO    stacktrace  src/common/stack_trace.cpp:172
```
</details>

Which looks to me like something to do with the levin protocol timeout.

I've located all log entries with the IP address in the log and it seems that the peer has connected, timed out and then either my node or the peer closed the connection. It could have been dropped idk:

```shell
$ rg -N "193.142.4.248" /var/log/monero/monero_l4.log
2023-10-10 19:06:54.659	[P2P0]	INFO	net.p2p	src/p2p/net_node.inl:2678	[193.142.4.248:18180 4ab669ef-5059-4991-bb3e-416abda9be2d OUT] NEW CONNECTION
2023-10-10 19:06:54.659	[P2P0]	INFO	net.p2p.traffic	contrib/epee/include/net/levin_protocol_handler_async.h:56	[193.142.4.248:18180 OUT] 262 bytes sent for category command-1001 initiated by us
2023-10-10 19:07:00.032	[P2P8]	INFO	net	contrib/epee/include/net/levin_protocol_handler_async.h:214	[193.142.4.248:18180 OUT] Timeout on invoke operation happened, command: 1001 timeout: 5000
2023-10-10 19:07:00.032	[P2P8]	WARNING	net.p2p	src/p2p/net_node.inl:1163	[193.142.4.248:18180 OUT] COMMAND_HANDSHAKE invoke failed. (-4, LEVIN_ERROR_CONNECTION_TIMEDOUT)
2023-10-10 19:07:00.032	[P2P0]	WARNING	net.p2p	src/p2p/net_node.inl:1222	[193.142.4.248:18180 OUT] COMMAND_HANDSHAKE Failed
2023-10-10 19:07:00.032	[P2P0]	INFO	net.p2p	src/p2p/net_node.inl:1413	[193.142.4.248:18180 OUT] Failed to HANDSHAKE with peer 193.142.4.248:18180
2023-10-10 19:07:00.033	[P2P0]	ERROR	net	contrib/epee/include/net/levin_protocol_handler_async.h:351	[193.142.4.248:18180 OUT] [levin_protocol] -->> start_outer_call failed
2023-10-10 19:07:00.034	[P2P0]	ERROR	net	contrib/epee/include/net/levin_protocol_handler_async.h:351	[193.142.4.248:18180 OUT] [levin_protocol] -->> start_outer_call failed
2023-10-10 19:07:00.034	[P2P0]	ERROR	net	contrib/epee/include/net/levin_protocol_handler_async.h:351	[193.142.4.248:18180 OUT] [levin_protocol] -->> start_outer_call failed
2023-10-10 19:07:00.038	[P2P2]	INFO	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:2945	[193.142.4.248:18180 OUT] [0] state: closed in state before_handshake
2023-10-10 19:07:00.038	[P2P2]	INFO	net.p2p	src/p2p/net_node.inl:2697	[193.142.4.248:18180 4ab669ef-5059-4991-bb3e-416abda9be2d OUT] CLOSE CONNECTION
```
So my absolute guess right now (without the debug build) is that the closed connection could have somehow caused the exception.

In fact as I'm grepping the log for `start_outer_call failed` I keep seeing the exception above it.

This seems to be the error log line: https://github.com/monero-project/monero/blob/67d190ce7c33602b6a3b804f633ee1ddb7fbb4a1/contrib/epee/include/net/levin_protocol_handler_async.h#L340

And this seems to be the definition that catches the bad_weak_ptr exception that you can see in the if statement above (although I'm not sure) https://github.com/monero-project/monero/blob/67d190ce7c33602b6a3b804f633ee1ddb7fbb4a1/contrib/epee/include/net/abstract_tcp_server2.inl#L1106

Based on this search query I assume its the only place this exception is caught in
https://github.com/search?q=repo%3Amonero-project%2Fmonero%20bad_weak_ptr&type=code

## vtnerd | 2023-11-05T22:51:07+00:00
@max-ishere Yes, currently `weak_ptr` is only used in the TCP server. The object is destroyed/destructed, but some other pointer to the object is invoking a function that calls `shared_from_this()`.

Try running my #7345 patch. This changes the raw pointer usage to `weak_ptr` (with checks for failure). My best guess without a proper call stack, is that this is initiated from the area that patch hopes to fix.

## vtnerd | 2023-11-05T22:54:28+00:00
Actually, I'm not certain the code I was referencing could be responsible. It's almost certainly coming from the TCP server, just not certain where at the moment. However, if you could run #7345 and provide feedback, it would narrow things down somewhat.

## emyfops | 2026-04-30T16:00:39+00:00
Blockchain synchronization is painfully slow on FreeBSD despite having all the optimizations flags and ports. I've been synchronizing for 3 weeks now and I'm at 96%. I also have lots of exceptions being thrown.

Version
```
➜  ~ uname -r
15.0-RELEASE-p4
```

Flags:
```
sysrc monerod_extra_args='--sync-pruned-blocks --prune-blockchain --db-sync-mode=safe:sync --p2p-bind-port-ipv6=18080 --p2p-use-ipv6 --ban-list=/var/db/monero/ban.txt --no-igd --out-peers=64 --in-peers=128 --rpc-restricted-bind-port=18089 --rpc-restricted-bind-ip=0.0.0.0 --rpc-restricted-bind-ipv6-address=:: --rpc-use-ipv6 --confirm-external-bind'
```

Stacktrace
```
026-04-30 15:27:06.608	[P2P5]	INFO	stacktrace	src/common/stack_trace.cpp:134	Exception: boost::wrapexcept<boost::bad_weak_ptr>
2026-04-30 15:27:06.608	[P2P5]	INFO	stacktrace	src/common/stack_trace.cpp:135	Unwound call stack:
2026-04-30 15:27:06.899	[P2P5]	INFO	stacktrace	src/common/stack_trace.cpp:163	    1                  0x9a86dc __cxa_throw + 0xcc
2026-04-30 15:27:07.142	[P2P5]	INFO	stacktrace	src/common/stack_trace.cpp:159	    2                  0x5266bd
2026-04-30 15:27:07.387	[P2P5]	INFO	stacktrace	src/common/stack_trace.cpp:159	    3                  0x7f2c68
2026-04-30 15:27:07.606	[P2P5]	INFO	stacktrace	src/common/stack_trace.cpp:159	    4                  0x7ecc3d
2026-04-30 15:27:07.823	[P2P5]	INFO	stacktrace	src/common/stack_trace.cpp:159	    5                  0x798832
2026-04-30 15:27:08.039	[P2P5]	INFO	stacktrace	src/common/stack_trace.cpp:159	    6                  0x798aac
2026-04-30 15:27:08.256	[P2P5]	INFO	stacktrace	src/common/stack_trace.cpp:159	    7                  0x780ed8
2026-04-30 15:27:08.473	[P2P5]	INFO	stacktrace	src/common/stack_trace.cpp:159	    8                  0x7ee422
2026-04-30 15:27:08.691	[P2P5]	INFO	stacktrace	src/common/stack_trace.cpp:159	    9                  0x7eec8c
2026-04-30 15:27:08.908	[P2P5]	INFO	stacktrace	src/common/stack_trace.cpp:159	    a                  0x7eea10
2026-04-30 15:27:09.126	[P2P5]	INFO	stacktrace	src/common/stack_trace.cpp:159	    b                  0x50b800
2026-04-30 15:27:09.344	[P2P5]	INFO	stacktrace	src/common/stack_trace.cpp:159	    c                  0x50b105
2026-04-30 15:27:09.561	[P2P5]	INFO	stacktrace	src/common/stack_trace.cpp:159	    d                  0x7ef445
2026-04-30 15:27:09.772	[P2P5]	INFO	stacktrace	src/common/stack_trace.cpp:163	    e                  0x82f37f91d boost::(anonymous namespace)::thread_proxy(void*) + 0x9d
2026-04-30 15:27:09.990	[P2P5]	INFO	stacktrace	src/common/stack_trace.cpp:159	    f                  0x832520d21
```

## selsta | 2026-04-30T16:07:17+00:00
@emyfops did you self compile or use binaries from getmonero.org ? ` --db-sync-mode=safe:sync` is also significantly slower than just keeping the default sync mode, better to just make backups if you are worried about corruption.

## selsta | 2026-04-30T16:23:17+00:00
`freebsd` support in monero is mostly untested unfortunately, it's possible that there are major sync issues even if everything is correct from your side

## lev-serebryakov-jetbrains | 2026-04-30T16:28:41+00:00
@selsta Problem is, that stack unwinding is very slow, and I don't understand why, but `weak_ptr` throws a lot of exceptions which go to log file.
I don't understand, why these exceptions are not caught specifically, as they are should be expected: they signal that object is gone, it is normal for `weak_ptr`. These exceptions must not be reported in first place.

FreeBSD doesn't need special support, it is POSIX compatible system.

## selsta | 2026-04-30T16:30:13+00:00
You can compile without libunwind support.

## selsta | 2026-04-30T16:32:17+00:00
Also does this OpenBSD issue also apply to FreeBSD? https://github.com/monero-project/monero/issues/7027

## lev-serebryakov-jetbrains | 2026-04-30T16:34:58+00:00
@selsta I don't know about #7027, as now I don't use monero daemon on *BSD, due to external (not monero- or freebsd-related) reasons.

## emyfops | 2026-04-30T16:37:54+00:00
> [@emyfops](https://github.com/emyfops) did you self compile or use binaries from getmonero.org ? ` --db-sync-mode=safe:sync` is also significantly slower than just keeping the default sync mode, better to just make backups if you are worried about corruption.

The speed is barely different with async. I got the binaries from the package manager.

## selsta | 2026-04-30T16:39:06+00:00
@emyfops could you try from getmonero? it comes without stack traces, if unwind is slow it should make a difference

## emyfops | 2026-04-30T18:05:36+00:00
> [@emyfops](https://github.com/emyfops) could you try from getmonero? it comes without stack traces, if unwind is slow it should make a difference

I have patched `net-p2p/monero-cli` with the following:
```
diff --git a/net-p2p/monero-cli/Makefile b/net-p2p/monero-cli/Makefile
index 4c841cc65..a6a8b3c86 100644
--- a/net-p2p/monero-cli/Makefile
+++ b/net-p2p/monero-cli/Makefile
@@ -63,11 +63,11 @@ LD_EMULATION=       ${ARCH:S|aarch64|aarch64elf|:S|amd64|elf_amd64|:C|armv[67]|armelf|
 CMAKE_ARGS+=   -DLD_RAW_FLAGS:STRING=-m${LD_EMULATION}
 
 # keep in sync with all platforms where libunwind is available
-.if ${ARCH} == aarch64 || ${ARCH} == amd64 || ${ARCH:Marmv?} || ${ARCH} == i386 || ${ARCH} == powerpc || ${ARCH:Mpowerpc64*}
-LIB_DEPENDS+=  libunwind.so:devel/libunwind
-.else
+#.if ${ARCH} == aarch64 || ${ARCH} == amd64 || ${ARCH:Marmv?} || ${ARCH} == i386 || ${ARCH} == powerpc || ${ARCH:Mpowerpc64*}
+#LIB_DEPENDS+= libunwind.so:devel/libunwind
+#.else
 CMAKE_ARGS+=   -DSTACK_TRACE:BOOL=OFF
-.endif
+#.endif
 
 CMAKE_ARGS+=   -DMANUAL_SUBMODULES:BOOL=ON
 
```

and while I don't seem to see any stacktraces anymore, the synchronization still takes a long time.
I should add that the LMDB lives on an NFS share mounted on the host and then that mount is mounted using nullfs in a freebsd jail.

```
2026-04-30 18:02:41.234	[P2P6]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1618	Synced 3530316/3663937 (96%, 133621 left, 0% of total synced, estimated 5.4 days left)
2026-04-30 18:03:50.248	[P2P6]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1618	Synced 3530336/3663938 (96%, 133602 left)
2026-04-30 18:05:19.345	[P2P6]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1618	Synced 3530356/3663938 (96%, 133582 left, 0% of total synced, estimated 5.6 days left)
```

## emyfops | 2026-04-30T18:23:40+00:00
Switching over to linux fixed the slowness, I might be forced to use linux for my node.

## selsta | 2026-04-30T18:26:18+00:00
LMDB does not support network-mounted storage, but I don't know if that's the reason for the slowdown. 

## emyfops | 2026-04-30T18:35:57+00:00
> LMDB does not support network-mounted storage, but I don't know if that's the reason for the slowdown.

I will attempt a synchronization without a network mounted storage and I will get back to you in a few days.

# Action History
- Created by: blacklion | 2022-01-06T08:51:37+00:00
