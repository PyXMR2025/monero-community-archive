---
title: how to get the output in background mode
source_url: https://github.com/xmrig/xmrig/issues/3035
author: ghost
assignees: []
labels: []
created_at: '2022-04-22T03:44:12+00:00'
updated_at: '2025-06-28T10:38:13+00:00'
type: issue
status: closed
closed_at: '2025-06-28T10:38:13+00:00'
---

# Original Description
I use ./xmrig -t 1 -o auto.c3pool.org:443 -u walletAddress
I can see  * ABOUT        XMRig/6.17.0 gcc/9.4.0
 * LIBS         libuv/1.43.0 OpenSSL/1.1.1m hwloc/2.7.0
 * HUGE PAGES   supported
 * 1GB PAGES    disabled
 * CPU          Intel(R) Core(TM) i7-6700HQ CPU @ 2.60GHz (1) 64-bit AES
                L2:1.0 MB L3:6.0 MB 4C/8T NUMA:1
 * MEMORY       4.8/15.5 GB (31%)
 * DONATE       1%
 * ASSEMBLY     auto:intel
 * POOL #1      auto.c3pool.org:443 algo auto
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       disabled
 * CUDA         disabled
[2022-04-21 22:39:44.623]  net      use pool auto.c3pool.org:443  5.161.70.189
[2022-04-21 22:39:44.623]  net      new job from auto.c3pool.org:443 diff 1000 algo rx/0 height 2607227 (21 tx)
[2022-04-21 22:39:44.623]  cpu      use argon2 implementation AVX2
[2022-04-21 22:39:44.625]  msr      msr kernel module is not available
[2022-04-21 22:39:44.625]  msr      FAILED TO APPLY MSR MOD, HASHRATE WILL BE LOW
[2022-04-21 22:39:44.626]  randomx  init dataset algo rx/0 (8 threads) seed 5b62875d46e11228...
[2022-04-21 22:39:44.626]  random x  allocated 2336 MB (2080+256) huge pages 0% 0/1168 +JIT (0 ms)
[2022-04-21 22:39:49.387]  randomx  dataset ready (4761 ms)
[2022-04-21 22:39:49.387]  cpu      use profile  *  (1 thread) scratchpad 2048 KB
[2022-04-21 22:39:49.387]  cpu      READY threads 1/1 (1) huge pages 0% 0/1 memory 2048 KB (1 ms)
[2022-04-21 22:39:52.248]  cpu      accepted (1/0) diff 1000 (285 ms)
[2022-04-21 22:39:54.317]  cpu      accepted (2/0) diff 1000 (105 ms)
[2022-04-21 22:39:56.007]  cpu      accepted (3/0) diff 1000 (105 ms)
[2022-04-21 22:40:00.775]  cpu      accepted (4/0) diff 1000 (102 ms)
[2022-04-21 22:40:01.127]  cpu      accepted (5/0) diff 1000 (118 ms)
[2022-04-21 22:40:03.721]  cpu      accepted (6/0) diff 1000 (157 ms)
[2022-04-21 22:40:08.271]  cpu      accepted (7/0) diff 1000 (118 ms)
[2022-04-21 22:40:11.800]  cpu      accepted (8/0) diff 1000 (103 ms)
[2022-04-21 22:40:14.427]  cpu      accepted (9/0) diff 1000 (104 ms)
[2022-04-21 22:40:16.128]  net      new job from auto.c3pool.org:443 diff 8572 algo rx/0 height 2607227 (21 tx)
[2022-04-21 22:40:29.126]  cpu      accepted (10/0) diff 8572 (102 ms)
[2022-04-21 22:40:49.421]  miner    speed 10s/60s/15m 300.1 n/a n/a H/s max 428.8 H/s
[2022-04-21 22:40:51.151]  cpu      accepted (11/0) diff 8572 (103 ms)
[2022-04-21 22:41:06.464]  net      new job from auto.c3pool.org:443 diff 8572 algo rx/0 height 2607228 (16 tx)
as output

Now I want to run xmrig in background I use:
 ./xmrig -B -t 1 -o auto.c3pool.org:443 -u walletAddress
The problem is I can not use output information like above.
I want to know how to get the output information

Thanks

# Discussion History
## SChernykh | 2022-04-22T08:41:43+00:00
Add `--log-file=FILE` to the command line.

## ghost | 2022-04-23T22:18:39+00:00
Ok, I try ./xmrig -B -t 1 -o auto.c3pool.org:443 -u walletAddress -l haha, but I can not see any haha file in the current folder

## ttsite | 2022-05-07T04:07:31+00:00
> -log-file=haha



## snipeTR | 2022-05-07T15:02:53+00:00
./xmrig -B -t 1 -o auto.c3pool.org:443 -u walletAddress --log-file=haha.txt
Or use tmux

## maravento | 2024-04-03T02:08:29+00:00
https://github.com/xmrig/xmrig/issues/3455

## asmaek91 | 2025-02-15T22:25:02+00:00
u should put background true in config...
when config file is used the comand line options don t work!

# Action History
- Created by: ghost | 2022-04-22T03:44:12+00:00
- Closed at: 2025-06-28T10:38:13+00:00
