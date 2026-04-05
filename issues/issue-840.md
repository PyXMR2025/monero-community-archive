---
title: 'read error: "end of file"'
source_url: https://github.com/xmrig/xmrig/issues/840
author: mahmoodn
assignees: []
labels: []
created_at: '2018-10-23T20:41:55+00:00'
updated_at: '2019-08-06T18:35:23+00:00'
type: issue
status: closed
closed_at: '2018-10-27T13:46:58+00:00'
---

# Original Description
I see **read error: "end of file"** multiple times

[2018-10-24 00:01:17] speed 10s/60s/15m 636.1 631.9 637.9 H/s max 667.8 H/s
[2018-10-24 00:01:24] new job from donate.v2.xmrig.com:3333 diff 1000225 algo cn/2
[2018-10-24 00:02:14] [donate.v2.xmrig.com:3333] read error: "end of file"
[2018-10-24 00:02:14] no active pools, stop mining
[2018-10-24 00:02:17] speed 10s/60s/15m 589.0 598.1 634.4 H/s max 667.8 H/s
[2018-10-24 00:02:20] use pool donate.v2.xmrig.com:3333  195.201.11.73 
[2018-10-24 00:02:20] new job from donate.v2.xmrig.com:3333 diff 1000225 algo cn/2


Is that important? The version is 2.8.3

# Discussion History
## xmrig | 2018-10-24T02:49:16+00:00
All troubles with donation should no affect your primary pool, but error `no active pools, stop mining` means you got error with primary pool too, it might be just network issue, but better see more logs.
Thank you.

## mahmoodn | 2018-10-24T06:16:03+00:00
When I run `./xmrig -S --log-file=./log.txt`, I don't see any log file. Also the pool address is `donate.V2.xmrig.com:3333` and I am using the CPU version.
Any thought?

## hermangroup | 2018-10-27T12:07:07+00:00
I think your problem is very simple , you probably did overwrite your config file when updated your miner to the last version.

Check the config file and make sure it have the right wallet and server address.


## ShaddyR | 2018-11-26T18:48:19+00:00
also got the message - mine is
[cryptonightv8.in.nicehash.com:3367] read error: "end of file"
Both cpu & nvidia gpu miners say that so no mining at all. What's this?

## seanwhe | 2019-08-06T18:35:23+00:00
Notice this error after some time xmrig XMRig 2.99.4-beta running against xmrig-proxy 2.99.0-beta
=============
$ uname -a
Linux sean-work-wks 4.15.0-55-generic #60-Ubuntu SMP Tue Jul 2 18:22:20 UTC 2019 x86_64 x86_64 x86_64 GNU/Linux

=============
$ xmrig -V
XMRig 2.99.4-beta
 built on Aug  5 2019 with GCC 7.4.0
 features: 64-bit AES

libuv/1.18.0
OpenSSL/1.1.1
hwloc/1


=============
 * ABOUT        XMRig/2.99.4-beta gcc/7.4.0
 * LIBS         libuv/1.18.0 OpenSSL/1.1.1 hwloc/1.11.9
 * CPU          Intel(R) Core(TM) i7-4770 CPU @ 3.40GHz (1) x64 AES AVX2
                L2:1.0 MB L3:8.0 MB 4C/8T NUMA:1
 * DONATE       5%
 * ASSEMBLY     auto:intel
 * POOL #1      192.168.4.5:3333 algo cn/r
 * COMMANDS     hashrate, pause, resume
 * HTTP API     192.168.1.47:8080
[2019-08-06 20:30:14.959] use pool 192.168.4.5:3333  192.168.4.5
[2019-08-06 20:30:14.959] new job from 192.168.4.5:3333 diff 51990 algo cn/r height 1895034
[2019-08-06 20:30:14.959]  cpu  use profile  cn  (4 threads) scratchpad 2048 KB
[2019-08-06 20:30:16.072]  cpu  READY threads 4(4) huge pages 4/4 100% memory 8192 KB (1113 ms)
...
[2019-08-06 20:28:53.956] new job from 192.168.4.5:3333 diff 51690 algo cn/r height 1895033
[2019-08-06 20:29:08.610] speed 10s/60s/15m 158.9 157.1 203.3 H/s max 265.1 H/s
[2019-08-06 20:29:15.090] [192.168.4.5:3333] read error: "end of file"
[2019-08-06 20:29:15.090] no active pools, stop mining
[2019-08-06 20:29:20.474] use pool 192.168.4.5:3333  192.168.4.5
[2019-08-06 20:29:20.474] new job from 192.168.4.5:3333 diff 51690 algo cn/r height 1895033

... 



# Action History
- Created by: mahmoodn | 2018-10-23T20:41:55+00:00
- Closed at: 2018-10-27T13:46:58+00:00
