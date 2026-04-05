---
title: v2.99.3 beta - how to test RandomX with it
source_url: https://github.com/xmrig/xmrig/issues/1096
author: kio3i0j9024vkoenio
assignees: []
labels:
- question
created_at: '2019-08-02T04:38:25+00:00'
updated_at: '2019-08-10T12:31:35+00:00'
type: issue
status: closed
closed_at: '2019-08-10T12:31:35+00:00'
---

# Original Description
Not a lot, actually I can find no documentation on how to test RandomX on this BETA build.

Here is what I have done so far:

Went here: https://github.com/xmrig/xmrig/releases/tag/v2.99.3-beta
And downloaded source (https://github.com/xmrig/xmrig/archive/v2.99.3-beta.tar.gz)
and compiled without any errors on Ubuntu 16.04

Copied the config.json that is included in the xmrig-2.99.3-beta-xenial-x64.tar.gz to the build directory

ran this command ./xmrig --dry-run
and got:

 * ABOUT        XMRig/2.99.3-beta gcc/5.4.0
 * LIBS         libuv/1.8.0 OpenSSL/1.0.2g hwloc/1.11.2
 * CPU          AMD Opteron(tm) Processor 6348 (4) x64 AES -AVX2
                L2:48.0 MB L3:64.0 MB 48C/48T NUMA:8
 * DONATE       5%
 * ASSEMBLY     auto:bulldozer
 * POOL #1      donate.v2.xmrig.com:3333 algo auto
 * COMMANDS     hashrate, pause, resume

So now what, how do I actually do a test of RandomX with this v2.99.3 BETA version of XMRIG?



# Discussion History
## RainbowMiner | 2019-08-02T08:49:33+00:00
RandomX is actually mining pretty fast. If you do not want a hassle: I have integrated the newest Xmrig v2.99.3 beta in RainbowMiner, so that you do not have to care about config file creation.

## xmrig | 2019-08-02T11:18:02+00:00
Try mine Loki (algorithm name `rx/loki`) it currently most close to reference RandomX configuration, or change `algo` option in config to `"algo": "rx/loki",` it his case you donate your hash power directly for me. Option `--dry-run` just checks configuration without actual mining.
Thank you.

## qutimqqcom | 2019-08-02T16:05:47+00:00
hi
where is config  description,  
algo cn/r
2.99.3  it work like   2.14  how set  up 2.99.3, no threads, no cpu usage, no aff ?
2.13  still best multi thread 

## xmrig | 2019-08-02T16:13:07+00:00
https://github.com/xmrig/xmrig/blob/evo/doc/CPU.md

## qutimqqcom | 2019-08-02T18:52:42+00:00
thx, i read  , and  get  inc   h\s    15%,   memory  used  200%
old  algo  cn8   with  2 thread by  1 core   i  see   inc   90%  h\s
what am I doing wrong ?



=======1   thread    CNR
 * ABOUT        XMRig/2.99.3-beta gcc/7.4.1
 * LIBS         libuv/1.30.1 hwloc/1.11.8rc2-git
 * CPU          Intel(R) Core(TM) i7-4790 CPU @ 3.60GHz (1) x64 AES AVX2
                L2:1.0 MB L3:8.0 MB 4C/8T NUMA:1
 * DONATE       5%
 * ASSEMBLY     auto:intel
[2019-08-02 21:43:06.022] CPU use profile  cn/r  (1 threads) scratchpad 2048 KB
[2019-08-02 21:43:06.525] CPU READY threads 1(1) huge pages 1/1 100% memory 2048 KB (503 ms)
[2019-08-02 21:43:21.037] speed 10s/60s/15m 77.7 n/a n/a H/s max 77.7 H/s


=======2   thread    CNR
[2019-08-02 21:43:55.058] CPU use profile  cn/r  (1 threads) scratchpad 2048 KB
[2019-08-02 21:43:55.675] CPU READY threads 1(2) huge pages 2/2 100% memory 4096 KB (617 ms)
[2019-08-02 21:44:10.072] speed 10s/60s/15m 92.0 n/a n/a H/s max 92.0 H/s



OLD  version   2.14,   looks like no changes

 * ABOUT        XMRig/2.14.1 gcc/7.3.1
 * LIBS         libuv/1.30.1
 * CPU          Intel(R) Core(TM) i7-4790 CPU @ 3.60GHz (1) x64 AES AVX2
 * CPU L2/L3    1.0 MB/8.0 MB
 * THREADS      1, cryptonight, av=2
 * ASSEMBLY     auto:intel

[2019-08-02 21:55:31] READY (CPU) threads 1(2) huge pages 2/2 100% memory 4096 KB
[2019-08-02 21:56:35] speed 10s/60s/15m 89.2 89.2 n/a H/s max 89.2 H/s



## shod4n | 2019-08-03T09:48:43+00:00
What about Wownero? It's on RandomX too already. Or is Loki a better choice?

## ariadarkkkis | 2019-08-03T12:19:23+00:00
@xmrig I've tested on Dual E5520 Windows server 2008 R2 X64 with version 2.99.3-beta and miner used about 4GB of ram with RandomX (LOKI) algo.

## xmrig | 2019-08-03T13:36:59+00:00
@shod4n Wownero use 1 MB scratchpad (instead of 2 MB), so it faster than reference RandomX.
@ariadarkkkis It expected, RandomX dataset allocated on each NUMA node, possible disable this feature, but it reduce hashrate #1077

## xmrig | 2019-08-10T12:31:35+00:00
#1111 

# Action History
- Created by: kio3i0j9024vkoenio | 2019-08-02T04:38:25+00:00
- Closed at: 2019-08-10T12:31:35+00:00
