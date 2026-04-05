---
title: Multiple physical CPU with loads of memory, only using one CPU
source_url: https://github.com/xmrig/xmrig/issues/2354
author: BigRigNoob
assignees: []
labels: []
created_at: '2021-05-07T17:25:35+00:00'
updated_at: '2021-05-08T22:06:09+00:00'
type: issue
status: closed
closed_at: '2021-05-07T22:56:51+00:00'
---

# Original Description
Hi,

I have a server rig that has MANY physical CPU (Intel® Xeon® Platinum 8276L Processor) and more RAM than you can shake a stick at.

When I looked at what's being used I only see one CPU running. There is nothing else on that server outside of xmrig. I am using command line into the server and it's running ubuntu.

Is there something to change in the config file for xmrig to use all physical CPU's?



# Discussion History
## SChernykh | 2021-05-07T17:30:28+00:00
Try to generate new config https://xmrig.com/wizard and then run with it. If it doesn't detect all CPUs, show the output of xmrig when it starts - especially the part where it prints CPU cores, threads and NUMA nodes.

## Spudz76 | 2021-05-07T18:44:20+00:00
If the RAM is not distributed among the slots so that each CPU has its own share locally sourced then that CPU won't be used (it has no local RAM).

Check like this:
```
root@gm98:~# hwloc-ls | grep NUMANode
    NUMANode L#0 (P#0 3931MB)
    NUMANode L#1 (P#1 4029MB)
```
Each CPU is a "node" and that line shows what part of RAM is usable to that node.  Would bet some of them are under 3GB which means no RAM for mining (on that CPU).  Obviously you'll have more than two nodes.  Also each node requires its own copy of the 2336MB data set for RandomX, therefore why they all need local ram of at least that size.

Also, NUMA could be disabled in BIOS on some systems which will mess up hwloc.

## BigRigNoob | 2021-05-07T20:35:07+00:00
> Try to generate new config https://xmrig.com/wizard and then run with it. If it doesn't detect all CPUs, show the output of xmrig when it starts - especially the part where it prints CPU cores, threads and NUMA nodes.

 * ABOUT        XMRig/6.12.1 gcc/9.3.0
 * LIBS         libuv/1.34.2 OpenSSL/1.1.1f hwloc/2.1.0
 * HUGE PAGES   supported
 * 1GB PAGES    disabled
 * CPU          Intel(R) Xeon(R) Platinum 8276L CPU @ 2.20GHz (1) 64-bit AES
                L2:28.0 MB L3:38.5 MB 28C/56T NUMA:1
 * MEMORY       7.9/376.4 GB (2%)
 * DONATE       1%
 * ASSEMBLY     auto:intel
 * POOL #1      ca.minexmr.com:443 algo auto
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       disabled
 * CUDA         disabled
[2021-05-07 20:24:51.877]  net      use pool ca.minexmr.com:443 TLSv1.3 51.222.149.99
[2021-05-07 20:24:51.877]  net      fingerprint (SHA-256): "f8cb85d6dc856748d376b48e6b87f90900b3f683fe505ef59de570296761d14b"
[2021-05-07 20:24:51.877]  net      new job from ca.minexmr.com:443 diff 175004 algo rx/0 height 2355899
[2021-05-07 20:24:51.877]  cpu      use argon2 implementation AVX-512F
[2021-05-07 20:24:51.881]  msr      cannot read MSR 0x000001a4
[2021-05-07 20:24:51.881]  msr      FAILED TO APPLY MSR MOD, HASHRATE WILL BE LOW
[2021-05-07 20:24:51.881]  randomx  init dataset algo rx/0 (56 threads) seed 93374bbc2ac22459...
[2021-05-07 20:24:52.067]  randomx  allocated 2336 MB (2080+256) huge pages 100% 1168/1168 +JIT (186 ms)
[2021-05-07 20:24:53.142]  randomx  dataset ready (1075 ms)
[2021-05-07 20:24:53.142]  cpu      use profile  rx  (28 threads) scratchpad 2048 KB
[2021-05-07 20:24:53.170]  cpu      READY threads 28/28 (28) huge pages 100% 28/28 memory 57344 KB (28 ms)

Here is the output for xmrig. I know hugepages isn't enabled but this is because I used the wizard. Also, here is the lscpu of the server:
Architecture:                    x86_64
CPU op-mode(s):                  32-bit, 64-bit
Byte Order:                      Little Endian
Address sizes:                   46 bits physical, 48 bits virtual
CPU(s):                          56
On-line CPU(s) list:             0-55
Thread(s) per core:              2
Core(s) per socket:              28
Socket(s):                       1
NUMA node(s):                    1
Vendor ID:                       GenuineIntel
CPU family:                      6
Model:                           85
Model name:                      Intel(R) Xeon(R) Platinum 8276L CPU @ 2.20GHz
Stepping:                        7
CPU MHz:                         1000.446
CPU max MHz:                     4000.0000
CPU min MHz:                     1000.0000
BogoMIPS:                        4400.00
Virtualization:                  VT-x
L1d cache:                       896 KiB
L1i cache:                       896 KiB
L2 cache:                        28 MiB
L3 cache:                        38.5 MiB
NUMA node0 CPU(s):               0-55


Thanks for the help!

## SChernykh | 2021-05-07T20:44:16+00:00
Both xmrig and lscpu show that you have 1 CPU with 28 cores/56 threads and 1 NUMA node. So you didn't configure your system properly.

## Spudz76 | 2021-05-08T22:06:09+00:00
Also you gave lscpu, not hwloc-ls which shows memory-to-node-and-cpu mappings

# Action History
- Created by: BigRigNoob | 2021-05-07T17:25:35+00:00
- Closed at: 2021-05-07T22:56:51+00:00
