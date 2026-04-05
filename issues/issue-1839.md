---
title: Tuning E5-4627 V2 Xeon but 2690 v1 is faster wth?!
source_url: https://github.com/xmrig/xmrig/issues/1839
author: agentpatience
assignees: []
labels: []
created_at: '2020-09-18T16:36:23+00:00'
updated_at: '2021-04-12T14:48:45+00:00'
type: issue
status: closed
closed_at: '2021-04-12T14:48:45+00:00'
---

# Original Description
Hi, 

I have some 4627 v2 CPU's with 3.3GHz base clock but oddly enough they don't run as fast as the 2690 V1 2.9 GHz. I am trying to figure out if there is anyway to improve the performance.

The processor cache specs look similar but there is a difference:


**Intel(R) Xeon(R) CPU E5-2690 0 @ 2.90GHz 20MB Cache** 

64-byte Prefetching
**Data TLB0: 2-MB or 4-MB pages**, 4-way set associative, 32 entries
Data TLB: 4-KB Pages, 4-way set associative, 64 entries
Instruction TLB: 4-KB pages, 4-way set associative, 64 entries
L2 TLB: 1-MB, 4-way set associative, 64-byte line size
Shared 2nd-level TLB: 4 KB pages, 4-way set associative, 512 entries
L3: Associativity: **20-way set associative**


**Intel(R) Xeon(R) CPU E5-4627 v2 @ 3.30GHz 16MB Cache**

64-byte Prefetching
**Data TLB: 1-GB pages**, 4-way set associative, 4 entries
Data TLB: 4-KB Pages, 4-way set associative, 64 entries
Instruction TLB: 4-KB Pages, 4-way set associative, 128 entries
L2 TLB: 1-MB, 4-way set associative, 64-byte line size
Shared 2nd-level TLB: 4 KB pages, 4-way set associative, 512 entries
L3: Associativity: **16-way set associative**
Includes F16C instructions, are they used by XMrig?

Can someone offer any tuning suggestions?

Thanks!

# Discussion History
## Lonnegan | 2020-09-21T17:01:48+00:00
E5-2690 has 20 MB L3 cache and 8 cores with SMT support. So it is able to start 10 RandomX threads.

E5-4627 v2 has only 16 MB L3 cache and 8 cores without SMT support. That's why only 8 threads can be started.

On paper E5-4627 has higher base frequency, 3300 MHz instead of 2900 MHz. But the E5-2690 has several turbo states, so it can boost to 3300 MHz as well, even if all cores are loaded as long as the TDP, current and therrmal limits not are exceeded.

In case of architecture Ivy Bridge (E5-4627 v2) and Sandy Bridge (E5-2690) are quite equal, so the younger CPU has no IPC advantage. Only the Manufacturing process is smaller (22 nm vs. 32 nm)

## agentpatience | 2020-09-21T23:15:03+00:00
Hi Lonnegan and thank you for replying to my obscure post. 
I understand that xmrig trys to lock 2mb per thread per core... which I don't completely understand the bottleneck here... as 2mb x 8 = 16MB. In my mind that condition is satisfied. There is also SMT support on 2690 which is disabled per the developers recommendation. Both chips have hyperthreading support disabled as well as all the cache options in BIOS. When you talk about SMT are you speaking about hyperthreading? Since that is intended to be disabled even the chips cannot be equal despite base -> max clock frequency.

When I look at the chips design on ARK it seems that the V2 4627 is a better chip for single threaded operation and when I bought them I assumed they could beat out my 2690's; since I am asking them to do single threaded operation (disabled HT/SMT). I still don't understand completely why 2690 v1 is faster than 4627 v2 other than its L1 20MB cache size? 

Thanks for trying to help.
Jeff




## BillGatesIII | 2020-09-24T12:55:06+00:00
I'm interested to hear what's going on here.

On both cpu's you should run eight mining threads because of the 256Kb per core L2 cache.

Do you use the same memory and all memory channels on both systems?

## agentpatience | 2020-09-24T13:13:02+00:00
Yes the systems are identical. I turn off hyperthreading in bios and turn off all caching options. 

Sent from my iPhone

> On Sep 24, 2020, at 8:55 AM, BillGatesIII <notifications@github.com> wrote:
> 
> ﻿
> I'm interested to hear what's going on here.
> 
> On both cpu's you should run eight mining threads because of the 256Kb per core L2 cache.
> 
> Do you use the same memory and all memory channels on both systems?
> 
> —
> You are receiving this because you authored the thread.
> Reply to this email directly, view it on GitHub, or unsubscribe.


## BillGatesIII | 2020-09-26T19:28:47+00:00
Can you post a screenshot or the output of the start of XMRIG for both systems?

## agentpatience | 2020-09-27T08:44:49+00:00
Yes sure, here is the 2690 system start up log:
sudo ./start.sh
 * ABOUT        XMRig/6.3.4 gcc/10.2.0
 * LIBS         libuv/1.39.0 OpenSSL/1.1.1g hwloc/2.2.0
 * HUGE PAGES   supported
 * 1GB PAGES    supported
 * CPU          Intel(R) Xeon(R) CPU E5-2690 0 @ 2.90GHz (2) x64 AES
                L2:4.0 MB L3:40.0 MB 16C/16T NUMA:2
 * MEMORY       2.3/31.3 GB (7%)
 * DONATE       1%
 * ASSEMBLY     auto:intel
 * POOL #1      pool.supportxmr.com:443 algo auto
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       disabled
 * CUDA         disabled
[2020-09-27 00:22:56.387]  net      use pool pool.supportxmr.com:443 TLSv1.2 104.140.201.42
[2020-09-27 00:22:56.387]  net      fingerprint (SHA-256): "39a361115318e42377a8221cdbf9645d017e61f62ea58eefd8e9367dcdb3d88d"
[2020-09-27 00:22:56.387]  net      new job from pool.supportxmr.com:443 diff 50000 algo rx/0 height 2195584
[2020-09-27 00:22:56.387]  cpu      use argon2 implementation SSSE3
[2020-09-27 00:22:56.413]  msr      register values for "intel" preset has been set successfully (25 ms)
[2020-09-27 00:22:56.413]  randomx  init datasets algo rx/0 (16 threads) seed 03ff5130b4c62713...
[2020-09-27 00:22:57.531]  randomx  #1 allocated 3072 MB huge pages 100% (1117 ms)
[2020-09-27 00:22:57.531]  randomx  #0 allocated 3072 MB huge pages 100% (1117 ms)
[2020-09-27 00:22:57.531]  randomx  -- allocated 6144 MB huge pages 100% 6/6 (1118 ms)
[2020-09-27 00:23:01.421]  randomx  #1 dataset ready (3890 ms)
[2020-09-27 00:23:02.665]  randomx  #0 dataset ready (1243 ms)
[2020-09-27 00:23:02.665]  cpu      use profile  rx  (16 threads) scratchpad 2048 KB
[2020-09-27 00:23:02.971]  cpu      READY threads 16/16 (16) huge pages 100% 16/16 memory 32768 KB (306 ms)
[2020-09-27 00:23:04.479]  net      new job from pool.supportxmr.com:443 diff 84907 algo rx/0 height 2195584
[2020-09-27 00:23:14.148]  cpu      accepted (1/0) diff 84907 (53 ms)
[2020-09-27 00:23:21.755]  net      new job from pool.supportxmr.com:443 diff 84907 algo rx/0 height 2195585
[2020-09-27 00:24:00.985]  cpu      accepted (2/0) diff 84907 (61 ms)
[2020-09-27 00:24:02.706]  miner    speed 10s/60s/15m **7313.9** n/a n/a H/s max 7314.1 H/s

4627 V2 Startup log:
* ABOUT        XMRig/6.3.4 gcc/9.3.0
 * LIBS         libuv/1.34.2 OpenSSL/1.1.1f hwloc/2.1.0
 * HUGE PAGES   supported
 * 1GB PAGES    supported
 * CPU          Intel(R) Xeon(R) CPU E5-4627 v2 @ 3.30GHz (2) x64 AES
                L2:4.0 MB L3:32.0 MB 16C/16T NUMA:2
 * MEMORY       7.1/31.3 GB (23%)
 * DONATE       1%
 * ASSEMBLY     auto:intel
 * POOL #1      pool.supportxmr.com:443 algo auto
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       disabled
 * CUDA         disabled
[2020-09-27 04:41:45.028]  net      use pool pool.supportxmr.com:443 TLSv1.2 104.140.244.186
[2020-09-27 04:41:45.028]  net      fingerprint (SHA-256): "676f843ef4cda0f72578b7589eedb13f4ca79f636b6a4e57eb38847c8f679d93"
[2020-09-27 04:41:45.028]  net      new job from pool.supportxmr.com:443 diff 50000 algo rx/0 height 2195701
[2020-09-27 04:41:45.028]  cpu      use argon2 implementation SSSE3
[2020-09-27 04:41:45.047]  msr      register values for "intel" preset has been set successfully (19 ms)
[2020-09-27 04:41:45.048]  randomx  init datasets algo rx/0 (16 threads) seed 03ff5130b4c62713...
[2020-09-27 04:41:46.445]  randomx  #1 allocated 3072 MB huge pages 100% (1398 ms)
[2020-09-27 04:41:46.445]  randomx  #0 allocated 3072 MB huge pages 100% (1398 ms)
[2020-09-27 04:41:46.445]  randomx  -- allocated 6144 MB huge pages 100% 6/6 (1398 ms)
[2020-09-27 04:41:49.821]  randomx  #1 dataset ready (3375 ms)
[2020-09-27 04:41:51.471]  randomx  #0 dataset ready (1649 ms)
[2020-09-27 04:41:51.471]  cpu      use profile  rx  (16 threads) scratchpad 2048 KB
[2020-09-27 04:41:51.777]  cpu      READY threads 16/16 (16) huge pages 100% 16/16 memory 32768 KB (306 ms)
[2020-09-27 04:42:12.461]  cpu      accepted (1/0) diff 50000 (50 ms)
[2020-09-27 04:42:19.576]  cpu      accepted (2/0) diff 50000 (85 ms)
[2020-09-27 04:42:24.474]  net      new job from pool.supportxmr.com:443 diff 115381 algo rx/0 height 2195701
[2020-09-27 04:42:51.510]  miner    speed 10s/60s/15m **6594.1** n/a n/a H/s max 6596.2 H/s


## BillGatesIII | 2020-09-27T11:07:42+00:00
You probably already checked if all cores are mining so I guess another thing to check is the speed at which the cores are running?

watch -n 2 "cat /proc/cpuinfo | grep \"^[c]pu MHz\""

All cores of the E5-4627 V2 should run at 3.5 MHz.
All cores of the E5-2690 should run at 3.3 Mhz.

If everything runs at the advertised speed there are two other things I can think of.
One is the bus speed, the 2690 has a bus speed of 8.0 GT/s while the 4627 has a bus speed of 7.2 GT/s. Maybe @SChernykh knows if this might be a bottleneck.
And the other thing is maybe the E5-4627 V2s you have are not production chips? The spec number on the chips should be SR1AD.

## agentpatience | 2020-09-27T14:01:33+00:00
Hi Bill Gates the third. 

Yes, these are production chips. 

That clock speed command doesn't work in Ubuntu. However, knowing what you are asking I found a different command for this:

Vendor ID:                       GenuineIntel
CPU family:                      6
Model:                           62
Model name:                      Intel(R) Xeon(R) CPU E5-4627 v2 @ 3.30GHz
Stepping:                        4
CPU MHz:                         3500.255
CPU max MHz:                     3600.0000
CPU min MHz:                     1200.0000
BogoMIPS:                        6600.48
Virtualization:                  VT-x
L1d cache:                       512 KiB
L1i cache:                       512 KiB
L2 cache:                        4 MiB
L3 cache:                        32 MiB

cat /sys/devices/system/cpu/cpu*/cpufreq/scaling_cur_freq
3500256
3500254
3500256
3500256
3500256
3500255
3500255
3500256
3500255
3500257
3500256
3500255
3500257
3500254
3500256
3500256

Vendor ID:                       GenuineIntel
CPU family:                      6
Model:                           45
Model name:                      Intel(R) Xeon(R) CPU E5-2690 0 @ 2.90GHz
Stepping:                        7
CPU MHz:                         3300.241
CPU max MHz:                     3800.0000
CPU min MHz:                     1200.0000
BogoMIPS:                        5800.42
Virtualization:                  VT-x
L1d cache:                       512 KiB
L1i cache:                       512 KiB
L2 cache:                        4 MiB
L3 cache:                        40 MiB

cat /sys/devices/system/cpu/cpu*/cpufreq/scaling_cur_freq
3300241
3300240
3300241
3300241
3300241
3300240
3300242
3300241
3300241
3300240
3300240
3300241
3300241
3300241
3300241
3300242

## BillGatesIII | 2020-09-27T18:21:51+00:00
Don't know how deep you wanna dive into this but next step I would suggest is to configure XMRIG to mine with one core only and compare the speeds. If the E5-2690 is still faster than the E5-4627v2 I hope one of the developers can explain why this is.

## agentpatience | 2020-10-16T15:06:06+00:00
I’d like to test further as the performance doesn’t seem right to me. I can give access to one of these systems if anyone wants to help me debug or help me tune? I am running xmrig by command line how do I tell it to just mine using 1 core? Perhaps it is a good idea to check single core performance?

## ariadarkkkis | 2020-10-17T10:20:04+00:00
@agentpatience You can check the command line arguments here: [Command Line Arguments](https://xmrig.com/docs/miner/command-line-options). Its` --threads=N` where `N` is the number of thread the miner uses for mining. Set it to 1 and it will automatically set the affinity as well so it will mine on 1 core only.

## agentpatience | 2020-10-17T16:05:14+00:00
Single Thread E5 4627 V2 - 452.3 H/s
Single Thread E5 2690 -  602 H/s

## ariadarkkkis | 2020-10-18T08:17:15+00:00
Can you share CPU clock speeds while the miner is running on those cores?
And one more thing you can do to double-check is that to set the `--cpu-affinity` manually. By default, when you run miner on 1 thread, it should use `0x1` affinity. You can set it to something like `0x4` to run on the second core if you have HT enable, if HT is disabled then use `0x2` as affinity to run on the second core and see if the hashrate is still the same as core 1.

You can calculate affinity [HERE](https://bitsum.com/tools/cpu-affinity-calculator/).

## agentpatience | 2020-10-18T13:16:13+00:00
Hi Aria,

**E5-2690** --threads=1

sudo ./start.sh 
 * ABOUT        XMRig/6.3.4 gcc/9.3.0
 * LIBS         libuv/1.34.2 OpenSSL/1.1.1f hwloc/2.1.0
 * HUGE PAGES   supported
 * 1GB PAGES    supported
 * CPU          Intel(R) Xeon(R) CPU E5-2690 0 @ 2.90GHz (2) x64 AES
                L2:4.0 MB L3:40.0 MB 16C/16T NUMA:2
 * MEMORY       9.3/15.6 GB (60%)
 * DONATE       1%
 * ASSEMBLY     auto:intel
 * POOL #1      pool.supportxmr.com:443 algo auto
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       disabled
 * CUDA         disabled
[2020-10-18 08:56:06.608]  net      use pool pool.supportxmr.com:443 TLSv1.2 104.140.244.186
[2020-10-18 08:56:06.609]  net      fingerprint (SHA-256): "676f843ef4cda0f72578b7589eedb13f4ca79f636b6a4e57eb38847c8f679d93"
[2020-10-18 08:56:06.609]  net      new job from pool.supportxmr.com:443 diff 50000 algo rx/0 height 2211001
[2020-10-18 08:56:06.609]  cpu      use argon2 implementation SSSE3
[2020-10-18 08:56:06.615]  msr      register values for "intel" preset has been set successfully (6 ms)
[2020-10-18 08:56:06.615]  randomx  init datasets algo rx/0 (16 threads) seed 326af4e7e2321620...
[2020-10-18 08:56:07.719]  randomx  #0 allocated 3072 MB huge pages 100% (1103 ms)
[2020-10-18 08:56:07.719]  randomx  #1 allocated 3072 MB huge pages 100% (1103 ms)
[2020-10-18 08:56:07.720]  randomx  -- allocated 6144 MB huge pages 100% 6/6 (1105 ms)
[2020-10-18 08:56:11.332]  randomx  #1 dataset ready (3612 ms)
[2020-10-18 08:56:12.189]  randomx  #0 dataset ready (857 ms)
[2020-10-18 08:56:12.190]  cpu      use profile  *  (1 thread) scratchpad 2048 KB
[2020-10-18 08:56:12.191]  cpu      READY threads 1/1 (1) huge pages 100% 1/1 memory 2048 KB (1 ms)
[2020-10-18 08:57:12.246]  miner    speed 10s/60s/15m 501.6 n/a n/a H/s max 501.9 H/s
[2020-10-18 08:58:12.304]  miner    speed 10s/60s/15m 502.0 501.8 n/a H/s max **502.0 H/s**

Ok, now when I set affinity to 0x1 **I gained 100 H/s** on the 2690 running core:

**E5-2690** --threads=1 --cpu-affinity 0x1
sudo ./start.sh 
[sudo] password for jeff: 
 * ABOUT        XMRig/6.3.4 gcc/9.3.0
 * LIBS         libuv/1.34.2 OpenSSL/1.1.1f hwloc/2.1.0
 * HUGE PAGES   supported
 * 1GB PAGES    supported
 * CPU          Intel(R) Xeon(R) CPU E5-2690 0 @ 2.90GHz (2) x64 AES
                L2:4.0 MB L3:40.0 MB 16C/16T NUMA:2
 * MEMORY       9.4/15.6 GB (60%)
 * DONATE       1%
 * ASSEMBLY     auto:intel
 * POOL #1      pool.supportxmr.com:443 algo auto
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       disabled
 * CUDA         disabled
[2020-10-18 09:11:31.520]  net      use pool pool.supportxmr.com:443 TLSv1.2 104.140.201.42
[2020-10-18 09:11:31.520]  net      fingerprint (SHA-256): "39a361115318e42377a8221cdbf9645d017e61f62ea58eefd8e9367dcdb3d88d"
[2020-10-18 09:11:31.520]  net      new job from pool.supportxmr.com:443 diff 50000 algo rx/0 height 2211013
[2020-10-18 09:11:31.520]  cpu      use argon2 implementation SSSE3
[2020-10-18 09:11:31.526]  msr      register values for "intel" preset has been set successfully (6 ms)
[2020-10-18 09:11:31.526]  randomx  init datasets algo rx/0 (16 threads) seed 326af4e7e2321620...
[2020-10-18 09:11:32.632]  randomx  #0 allocated 3072 MB huge pages 100% (1105 ms)
[2020-10-18 09:11:32.633]  randomx  #1 allocated 3072 MB huge pages 100% (1106 ms)
[2020-10-18 09:11:32.633]  randomx  -- allocated 6144 MB huge pages 100% 6/6 (1106 ms)
[2020-10-18 09:11:36.176]  randomx  #1 dataset ready (3543 ms)
[2020-10-18 09:11:37.034]  randomx  #0 dataset ready (857 ms)
[2020-10-18 09:11:37.035]  cpu      use profile  *  (1 thread) scratchpad 2048 KB
[2020-10-18 09:11:37.037]  cpu      READY threads 1/1 (1) huge pages 100% 1/1 memory 2048 KB (2 ms)
[2020-10-18 09:12:33.209]  cpu      accepted (1/0) diff 50000 (62 ms)
[2020-10-18 09:12:36.457]  cpu      accepted (2/0) diff 50000 (49 ms)
[2020-10-18 09:12:37.086]  miner    speed 10s/60s/15m 601.6 n/a n/a H/s max **602.8 H/s**

jeff@miner9:~$ cat /sys/devices/system/cpu/cpu*/cpufreq/scaling_cur_freq
3796278
3470581
1200193
3464265
1199947
3575880
1200167
1200195
3471951
1199867
3588141
1199793
3461349
1199953
3553871
1200037

## agentpatience | 2020-10-18T13:21:09+00:00
0x1 and 0x2 show the same gains. I have HT turned off in BIOS.

## agentpatience | 2020-10-18T13:38:45+00:00
**E5 4627 v2** --threads=1 --cpu-affinity=0x1:

gcc/9.3.0
 * LIBS         libuv/1.34.2 OpenSSL/1.1.1f hwloc/2.1.0
 * HUGE PAGES   supported
 * 1GB PAGES    supported
 * CPU          Intel(R) Xeon(R) CPU E5-4627 v2 @ 3.30GHz (2) x64 AES
                L2:4.0 MB L3:32.0 MB 16C/16T NUMA:2
 * MEMORY       9.4/31.3 GB (30%)
 * DONATE       1%
 * ASSEMBLY     auto:intel
 * POOL #1      pool.supportxmr.com:443 algo auto
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       disabled
 * CUDA         disabled
[2020-10-18 09:37:30.631]  net      use pool pool.supportxmr.com:443 TLSv1.2 104.140.201.42
[2020-10-18 09:37:30.631]  net      fingerprint (SHA-256): "39a361115318e42377a8221cdbf9645d017e61f62ea58eefd8e9367dcdb3d88d"
[2020-10-18 09:37:30.631]  net      new job from pool.supportxmr.com:443 diff 50000 algo rx/0 height 2211026
[2020-10-18 09:37:30.631]  cpu      use argon2 implementation SSSE3
[2020-10-18 09:37:30.637]  msr      register values for "intel" preset has been set successfully (6 ms)
[2020-10-18 09:37:30.637]  randomx  init datasets algo rx/0 (16 threads) seed 326af4e7e2321620...
[2020-10-18 09:37:31.968]  randomx  #0 allocated 3072 MB huge pages 100% (1331 ms)
[2020-10-18 09:37:31.968]  randomx  #1 allocated 3072 MB huge pages 100% (1331 ms)
[2020-10-18 09:37:31.968]  randomx  -- allocated 6144 MB huge pages 100% 6/6 (1331 ms)
[2020-10-18 09:37:35.781]  randomx  #1 dataset ready (3813 ms)
[2020-10-18 09:37:36.815]  randomx  #0 dataset ready (1034 ms)
[2020-10-18 09:37:36.816]  cpu      use profile  *  (1 thread) scratchpad 2048 KB
[2020-10-18 09:37:36.818]  cpu      READY threads 1/1 (1) huge pages 100% 1/1 memory 2048 KB (2 ms)
[2020-10-18 09:37:37.892]  net      new job from pool.supportxmr.com:443 diff 86539 algo rx/0 height 2211026
[2020-10-18 09:38:36.878]  miner    speed 10s/60s/15m 615.6 n/a n/a H/s max 616.0 H/s
[2020-10-18 09:38:37.994]  net      new job from pool.supportxmr.com:443 diff 57692 algo rx/0 height 2211026
[2020-10-18 09:39:36.940]  miner    speed 10s/60s/15m 616.0 615.8 n/a H/s **max 616.3 H/s**


Clocks:

cat /sys/devices/system/cpu/cpu*/cpufreq/scaling_cur_freq
3584517
3504796
1200229
3500298
1200354
3503598
1200291
1200527
3499941
1200393
3497419
1200107
3498735
1200516
3501512
1200089

## ariadarkkkis | 2020-10-18T19:57:28+00:00
OK, run the miner on whatever number of threads you want and set the affinity according to that thread number and see if you gain any more performance. As I saw, single thread mining is now better on E5 4627 v2 compared to E5 2690 0. But your 2690 0 will boost more to 3.8GHz as it should and 4627 v2 is hovering around 3.5-3.6GHz boost. So you should get more hashrate with higher clocks. I'm not sure but I think RAM frequency has some effects on the hashrate as well. Even RAM channels can possibly have some effect on hashrate. OS Configuration plays a huge part on your hashrate as well. So if you can try, do some clean installs and test with the exact same settings (in VM or in BIOS). And try to use pre-compiled binaries and compare them to your own compiled binaries (but I dont think this will affect the hashrate that much but worth noticing).

## BillGatesIII | 2020-10-22T05:41:42+00:00
It's a long shot but I guess you'll have to test with two threads, three threads and so on to see when the E5 4627 v2 becomes slower.

The turbo stepping grouping or whatever it is called for these chips are:
E5-4627 v2: 2/2/2/2/2/2/2/3 so this one should run at 3.3 + 0.2 = 3.5 GHz running two or more threads and 3.6 GHz running one thread.
E5-2690: 4/4/4/5/5/7/7/9 so this one should run at 2.9 + 0.4 = 3.3 GHz running six or more threads, 3.4 GHz running four or five threads, 3.6 GHz running two or three threads and 3.8 GHz running one thread.

So even with a lower processor frequency, the E5-4627 V2 is faster when mining with one thread. So something somewhere somehow changes when running more threads :)

## agentpatience | 2020-10-24T18:43:21+00:00
4627 v2
10 Threads = 5789
12 Threads = 6504
14 Threads = 6693
16 Threads = **6618** --threads=16 --cpu-affinity=0x000000000000FFFF      ?????

## BillGatesIII | 2020-10-26T05:54:48+00:00
So hashrate becomes less when going from 14 to 16 threads? And 15 threads? Better than 14 or not?

 I have no clue what's going on here. 

## agentpatience | 2020-10-26T13:50:44+00:00
> 
> 
> So hashrate becomes less when going from 14 to 16 threads? And 15 threads? Better than 14 or not?
> 
> I have no clue what's going on here.

Yea, it doesn't scale the same way after 12 threads. I am not sure at this point either it may have something to do with "Smart Caching" which these Xeons do not carry. 

## BillGatesIII | 2020-10-26T19:36:11+00:00
Both processors do have the Intel Smart Cache thing but, the older 2690 has 20 MB and the newer 4627 V2 has 16 MB. In both processors it is used for the level 3 (last-level) cache.

Now, because RandomX uses 2 MB level 3 cache for each thread my last guess is the 2690 will have a better cache hit rate when all cores are mining.

I found this document explaining it; the pictures in it are with L1 private cache and L2 shared cache but I assume it works the same for L2 private and L3 shared cache.
[Software Techniques for Shared-Cache Multi-Core Systems](https://software.intel.com/content/www/us/en/develop/articles/software-techniques-for-shared-cache-multi-core-systems.html)
The article also explains some software techniques for using this Smart Cache effectively but my C and Assembly is by far not good enough to figure out if this is used in xmrig or not or if it is even beneficial.

I really hope one of the developers will shine his/her light on this.


## agentpatience | 2020-10-26T19:50:35+00:00
I stand corrected about Smart Cache. It was not apparent to me. I will play around with memory configurations this week.

# Action History
- Created by: agentpatience | 2020-09-18T16:36:23+00:00
- Closed at: 2021-04-12T14:48:45+00:00
