---
title: xmrig "Killed" on raspberry pi 5
source_url: https://github.com/xmrig/xmrig/issues/3777
author: JustinKras
assignees: []
labels: []
created_at: '2026-02-02T20:28:07+00:00'
updated_at: '2026-02-13T07:34:32+00:00'
type: issue
status: closed
closed_at: '2026-02-13T07:34:32+00:00'
---

# Original Description
When I try to run xmrig on my pi 5, it allocates whatever, shows a few new jobs, and then prints "Killed". Why does it work perfectly for people online, but when I try it, I can't even start it? 

Throw me all sorts of ideas, and yes i'm running 64 bit.

# Discussion History
## SChernykh | 2026-02-02T21:29:17+00:00
Probably the same as #3729. Try the solutions from there.

## JustinKras | 2026-02-02T21:42:45+00:00
Yeah I had already tried that with the config file, it still kills.

## SChernykh | 2026-02-02T21:44:01+00:00
Then post the full output of XMRig here, from start until it gets killed.

## JustinKras | 2026-02-02T21:48:15+00:00
 * ABOUT        XMRig/6.25.0 gcc/14.2.0 (built for Linux ARMv8, 64 bit)
 * LIBS         libuv/1.50.0 OpenSSL/3.5.4 hwloc/2.12.0
 * HUGE PAGES   unavailable
 * 1GB PAGES    unavailable
 * CPU          ARM Cortex-A76 (1) 64-bit AES
                L2:2.0 MB L3:2.0 MB 4C/4T NUMA:8
 * MEMORY       0.2/7.9 GB (3%)
 * DONATE       1%
 * POOL #1      gulf.moneroocean.stream:10128 algo auto
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       disabled
 * CUDA         disabled
[2026-02-02 12:38:57.807]  net      use pool gulf.moneroocean.stream:10128  66.23.199.44
[2026-02-02 12:38:57.807]  net      new job from gulf.moneroocean.stream:10128 diff 1280K algo rx/0 height 3601493 (28 tx)
[2026-02-02 12:38:57.807]  cpu      use argon2 implementation default
[2026-02-02 12:38:57.807]  randomx  init datasets algo rx/0 (4 threads) seed db814280b7189ff5...
[2026-02-02 12:38:57.809]  randomx  #1 allocated 2080 MB huge pages   0% (2 ms)
[2026-02-02 12:38:57.809]  randomx  #0 allocated 2080 MB huge pages   0% (2 ms)
[2026-02-02 12:38:57.809]  randomx  #2 allocated 2080 MB huge pages   0% (2 ms)
[2026-02-02 12:38:57.809]  randomx  #5 allocated 2080 MB huge pages   0% (1 ms)
[2026-02-02 12:38:57.809]  randomx  #4 allocated 2080 MB huge pages   0% (1 ms)
[2026-02-02 12:38:57.809]  randomx  #3 allocated 2080 MB huge pages   0% (2 ms)
[2026-02-02 12:38:57.809]  randomx  #6 allocated 2080 MB huge pages   0% (1 ms)
[2026-02-02 12:38:57.809]  randomx  #7 allocated 2080 MB huge pages   0% (1 ms)
[2026-02-02 12:38:57.810]  randomx  #0 allocated  256 MB huge pages   0% +JIT (1 ms)
[2026-02-02 12:38:57.810]  randomx  -- allocated 16896 MB huge pages   0% 0/8448 (3 ms)
[2026-02-02 12:39:13.590]  randomx  #0 dataset ready (15780 ms)
[2026-02-02 12:39:22.152]  net      new job from gulf.moneroocean.stream:10128 diff 1280K algo rx/0 height 3601494 (3 tx)
[2026-02-02 12:39:52.412]  net      new job from gulf.moneroocean.stream:10128 diff 1280K algo rx/0 height 3601494 (12 tx)
Killed

## SChernykh | 2026-02-02T21:52:33+00:00
It is exactly #3729. Disable NUMA in [config file](https://xmrig.com/docs/miner/config/cpu#numa or in the command line `--randomx-no-numa` (if you use the command line)

## SChernykh | 2026-02-02T21:53:17+00:00
Find `"numa": true,` and change it to `"numa": false,` in config.json

## JustinKras | 2026-02-02T21:55:11+00:00
I already tried that, there was no "numa" so I added it myself, it's set to false but still doesnt work.

## JustinKras | 2026-02-02T22:00:45+00:00
I'll try adding --randomx-no-numa to the command line and letting it run for some time, I'll have an update later

## SChernykh | 2026-02-02T22:13:58+00:00
There is `numa` in the config: 

<img width="985" height="1111" alt="Image" src="https://github.com/user-attachments/assets/dd455698-aecc-42ab-9e43-d0d0b5438e33" />

## JustinKras | 2026-02-02T22:22:11+00:00
I'll have to do some deeper digging, but so far --randomx-no-numa is working ok. I guess this issue is closed (for now). Thanks for the help!

# Action History
- Created by: JustinKras | 2026-02-02T20:28:07+00:00
- Closed at: 2026-02-13T07:34:32+00:00
