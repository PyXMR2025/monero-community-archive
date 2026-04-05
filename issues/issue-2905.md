---
title: MSR not applying Linux Debian 10
source_url: https://github.com/xmrig/xmrig/issues/2905
author: rhys19
assignees: []
labels: []
created_at: '2022-01-27T06:56:59+00:00'
updated_at: '2022-02-24T20:04:26+00:00'
type: issue
status: closed
closed_at: '2022-01-27T07:01:11+00:00'
---

# Original Description
Everytime I launch Xmrig it won't apply the MSR for my cpu.

I'm not sure if this is supposed to happen or not so I am not following the bug report format unless it's deemed a bug.

the log is below:
```
rhys19@rhys19:~/Desktop/xmrig$ ./xmrig -c config/config.json 
 * ABOUT        XMRig/6.16.2 gcc/9.3.0
 * LIBS         libuv/1.34.2 OpenSSL/1.1.1f hwloc/2.1.0
 * HUGE PAGES   supported
 * 1GB PAGES    disabled
 * CPU          AMD Ryzen 7 3700X 8-Core Processor (1) 64-bit AES
                L2:4.0 MB L3:32.0 MB 8C/16T NUMA:1
 * MEMORY       3.6/15.5 GB (23%)
 * DONATE       0%
 * ASSEMBLY     auto:ryzen
 * POOL #1      xmr.2miners.com:2222 coin Monero
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       disabled
 * CUDA         11.6/11.6/6.15.1
 * NVML         11.510.39.01/510.39.01 press e for health report
 * CUDA GPU     #0 24:00.0 NVIDIA GeForce GTX 1060 3GB 1784/4004 MHz smx:9 arch:61 mem:2565/3011 MB
[2022-01-27 00:50:23.563]  net      use pool xmr.2miners.com:2222  51.89.96.41
[2022-01-27 00:50:23.563]  net      new job from xmr.2miners.com:2222 diff 120001 algo rx/0 height 2546199 (6 tx)
[2022-01-27 00:50:23.563]  cpu      use argon2 implementation AVX2
[2022-01-27 00:50:23.564]  msr      cannot read MSR 0xc0011020
[2022-01-27 00:50:23.564]  msr      FAILED TO APPLY MSR MOD, HASHRATE WILL BE LOW
[2022-01-27 00:50:23.564]  randomx  init dataset algo rx/0 (16 threads) seed a16c2c8043509306...
[2022-01-27 00:50:23.564]  randomx  allocated 2336 MB (2080+256) huge pages 0% 0/1168 +JIT (0 ms)
[2022-01-27 00:50:25.790]  randomx  dataset ready (2226 ms)
[2022-01-27 00:50:25.790]  cpu      use profile  rx  (16 threads) scratchpad 2048 KB
[2022-01-27 00:50:25.791]  nvidia   use profile  rx  (1 thread) scratchpad 2048 KB
|  # | GPU |  BUS ID | INTENSITY | THREADS | BLOCKS | BF |  BS | MEMORY | NAME
|  0 |   0 | 24:00.0 |       576 |      32 |     18 |  0 |   0 |   1152 | NVIDIA GeForce GTX 1060 3GB
[2022-01-27 00:50:25.815]  cpu      READY threads 16/16 (16) huge pages 0% 0/16 memory 32768 KB (25 ms)
[2022-01-27 00:50:26.317]  nvidia   READY threads 1/1 (526 ms)
```
you notice the MSR error towards the top 
```
[2022-01-27 00:50:23.564]  msr      cannot read MSR 0xc0011020
[2022-01-27 00:50:23.564]  msr      FAILED TO APPLY MSR MOD, HASHRATE WILL BE LOW
```

I've tried running it as root also but no luck, any help is appreciated!

OS: Linux Mint 20.3 Cinnamon - Debian 10
Kernal: 5.13
CPU: AMD Ryzen 7 3700x - Overclocked to 4.5GHz
Ram: 16GB
SSD/HDD: SSD
GPU: Asus Geforce GTX 1060 3GB
xmrig version: 6.16.3 - Custom built
xmrig-cuda: Custom Built
Cuda version: 11.6
Coin: Monero
Algo: RandomX

if you need anymore information please let me know.



# Discussion History
## rhys19 | 2022-01-27T07:01:11+00:00
well this is odd I did `sudo ./xmrig -c config/config.json` and now it's working...

## koitsu | 2022-02-24T20:04:26+00:00
> well this is odd I did `sudo ./xmrig -c config/config.json` and now it's working...

It's not odd at all.  The `msr` kernel module (which I assume you loaded; I'm not sure if xmrig calls modprobe on its own) only allows user `root` or members of the group `root` to access /dev/cpu/NNN/msr.  If you [read the msr(4) man page](https://man7.org/linux/man-pages/man4/msr.4.html) you'll see that documented:

> This file is protected so that it can be read and written only by the user root, or members of the group root.

However, for whatever reason, the latter part of that paragraph is incorrect -- group `root` does not have r/w access:

```
$ ls -l /dev/cpu/*/msr
crw------- 1 root root 202, 0 Feb 15 22:51 /dev/cpu/0/msr
crw------- 1 root root 202, 1 Feb 15 22:51 /dev/cpu/1/msr
crw------- 1 root root 202, 2 Feb 15 22:51 /dev/cpu/2/msr
crw------- 1 root root 202, 3 Feb 15 22:51 /dev/cpu/3/msr
```

So, in other words, to get MSR capability, you need to run xmrig as root -- hence `sudo`.

# Action History
- Created by: rhys19 | 2022-01-27T06:56:59+00:00
- Closed at: 2022-01-27T07:01:11+00:00
