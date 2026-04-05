---
title: Help with CPU configuration
source_url: https://github.com/xmrig/xmrig/issues/2108
author: MedGaSToN
assignees: []
labels: []
created_at: '2021-02-17T03:18:13+00:00'
updated_at: '2021-02-19T07:56:19+00:00'
type: issue
status: closed
closed_at: '2021-02-19T07:56:19+00:00'
---

# Original Description
I'm confused about the output result of the benchmark, I think I'm messing a lot of configuration setup.

## Hardware overview 
### CPU details
```
Architecture:                    x86_64
CPU op-mode(s):                  32-bit, 64-bit
Byte Order:                      Little Endian
Address sizes:                   46 bits physical, 48 bits virtual
CPU(s):                          128
On-line CPU(s) list:             0-127
Thread(s) per core:              2
Core(s) per socket:              16
Socket(s):                       4
NUMA node(s):                    4
Vendor ID:                       GenuineIntel
CPU family:                      6
Model:                           63
Model name:                      Intel(R) Xeon(R) CPU E7-8880 v3 @ 2.30GHz
Stepping:                        4
CPU MHz:                         2740.719
CPU max MHz:                     3100.0000
CPU min MHz:                     1200.0000
BogoMIPS:                        4600.03
Hypervisor vendor:               Xen
Virtualization type:             full
L1d cache:                       2 MiB
L1i cache:                       2 MiB
L2 cache:                        16 MiB
L3 cache:                        180 MiB
NUMA node0 CPU(s):               0-15,64-79
NUMA node1 CPU(s):               16-31,80-95
NUMA node2 CPU(s):               32-47,96-111
NUMA node3 CPU(s):               48-63,112-127
```
### Memory
- 122 * 32GB = 3904GB
```bash
              total        used        free      shared  buff/cache   available
Mem:        3935112       14182     3919668           1        1260     3910315
Swap:             0           0           0
```
### Software
```
#dmidecode 3.2
Getting SMBIOS data from sysfs.
SMBIOS 2.7 present.

Handle 0x0000, DMI type 0, 24 bytes
BIOS Information
        Vendor: Xen
        Version: 4.11.amazon
        Release Date: 08/24/2006
        Address: 0xE8000
        Runtime Size: 96 kB
        ROM Size: 64 kB
        Characteristics:
                PCI is supported
                EDD is supported
                Targeted content distribution is supported
        BIOS Revision: 4.1
```
## XMRig
### Version
- XMRig/6.8.2 (Linux x86_64) libuv/1.40.0 gcc/9.3.0
### Build
```bash
1. sudo apt-get install git build-essential cmake automake libtool autoconf
2. git clone https://github.com/xmrig/xmrig.git
3. mkdir xmrig/build && cd xmrig/scripts
4. ./build_deps.sh && cd ../build
5. cmake .. -DXMRIG_DEPS=scripts/deps -DWITH_HTTP=ON
6. make -j$(nproc)
```
### Config
* I used "cache_qos": true -> **this CPU doesn't support cat_l3, cache QoS is unavailable**
```json
{
    "api": {
        "id": null,
        "worker-id": null
    },
    "http": {
        "enabled": false,
        "host": "127.0.0.1",
        "port": 0,
        "access-token": null,
        "restricted": true
    },
    "autosave": true,
    "background": false,
    "colors": true,
    "title": true,
    "randomx": {
        "init": -1,
        "init-avx2": -1,
        "mode": "auto",
        "1gb-pages": true,
        "rdmsr": true,
        "wrmsr": true,
        "cache_qos": false,
        "numa": true,
        "scratchpad_prefetch_mode": 1
    },
    "cpu": {
        "enabled": true,
        "huge-pages": true,
        "huge-pages-jit": false,
        "hw-aes": null,
        "priority": null,
        "memory-pool": false,
        "yield": true,
        "asm": true,
        "argon2-impl": null,
        "astrobwt-max-size": 550,
        "astrobwt-avx2": false,
        "argon2": [0, 64, 1, 65, 2, 66, 3, 67, 4, 68, 5, 69, 6, 70, 7, 71, 8, 72, 9, 73, 10, 74, 11, 75, 12, 76, 13, 77, 14, 78, 15, 79, 16, 80, 17, 81, 18, 82, 19, 83, 20, 84, 21, 85, 22, 86, 23, 87, 24, 88, 25, 89, 26, 90, 27, 91, 28, 92, 29, 93, 30, 94, 31, 95, 32, 96, 33, 97, 34, 98, 35, 99, 36, 100, 37, 101, 38, 102, 39, 103, 40, 104, 41, 105, 42, 106, 43, 107, 44, 108, 45, 109, 46, 110, 47, 111, 48, 112, 49, 113, 50, 114, 51, 115, 52, 116, 53, 117, 54, 118, 55, 119, 56, 120, 57, 121, 58, 122, 59, 123, 60, 124, 61, 125, 62, 126, 63, 127],
        "astrobwt": [0, 64, 1, 65, 2, 66, 3, 67, 4, 68, 5, 69, 6, 70, 7, 71, 8, 72, 9, 73, 10, 74, 11, 75, 12, 76, 13, 77, 14, 78, 15, 79, 16, 80, 17, 81, 18, 82, 19, 83, 20, 84, 21, 85, 22, 86, 23, 87, 24, 88, 25, 89, 26, 90, 27, 91, 28, 92, 29, 93, 30, 94, 31, 95, 32, 96, 33, 97, 34, 98, 35, 99, 36, 100, 37, 101, 38, 102, 39, 103, 40, 104, 41, 105, 42, 106, 43, 107, 44, 108, 45, 109, 46, 110, 47, 111, 48, 112, 49, 113, 50, 114, 51, 115, 52, 116, 53, 117, 54, 118, 55, 119, 56, 120, 57, 121, 58, 122, 59, 123, 60, 124, 61, 125, 62, 126, 63, 127],
        "cn": [
            [1, 0],
            [1, 1],
            [1, 2],
            [1, 3],
            [1, 4],
            ...
            [1, 124],
            [1, 125],
            [1, 126],
            [1, 127]
        ],
        "cn-heavy": [
            [1, 0],
            [1, 1],
            [1, 2],
            [1, 3],
            ...
            [1, 55],
            [1, 56],
            [1, 57],
            [1, 58]
        ],
        "cn-lite": [
            [1, 0],
            [1, 64],
            [1, 1],
            [1, 65],
            ...
            [1, 62],
            [1, 126],
            [1, 63],
            [1, 127]
        ],
        "cn-pico": [
            [2, 0],
            [2, 64],
            [2, 1],
            [2, 65],
            ...
            [2, 62],
            [2, 126],
            [2, 63],
            [2, 127]
        ],
        "rx": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63],
        "rx/wow": [0, 64, 1, 65, 2, 66, 3, 67, 4, 68, 5, 69, 6, 70, 7, 71, 8, 72, 9, 73, 10, 74, 11, 75, 12, 76, 13, 77, 14, 78, 15, 79, 16, 80, 17, 81, 18, 82, 19, 83, 20, 84, 21, 85, 22, 86, 23, 87, 24, 88, 25, 89, 26, 90, 27, 91, 28, 92, 29, 93, 30, 94, 31, 95, 32, 96, 33, 97, 34, 98, 35, 99, 36, 100, 37, 101, 38, 102, 39, 103, 40, 104, 41, 105, 42, 106, 43, 107, 44, 108, 45, 109, 46, 110, 47, 111, 48, 112, 49, 113, 50, 114, 51, 115, 52, 116, 53, 117, 54, 118, 55, 119, 56, 120, 57, 121, 58, 122, 59, 123, 60, 124, 61, 125, 62, 126, 63, 127],
        "cn/0": false,
        "cn-lite/0": false,
        "rx/arq": "rx/wow",
        "rx/keva": "rx/wow"
    },
    "opencl": {
        "enabled": false,
        "cache": true,
        "loader": null,
        "platform": "AMD",
        "adl": true
    },
    "cuda": {
        "enabled": false,
        "loader": null,
        "nvml": true
    },
    "log-file": null,
    "donate-level": 5,
    "donate-over-proxy": 1,
    "pools": [
        {
            "algo": null,
            "coin": "monero",
            "url": "xmr-us-east1.nanopool.org:14433",
            "user": "<address>",
            "pass": null,
            "rig-id": null,
            "nicehash": false,
            "keepalive": false,
            "enabled": true,
            "tls": true,
            "tls-fingerprint": null,
            "daemon": false,
            "socks5": null,
            "self-select": null
        }
    ],
    "retries": 5,
    "retry-pause": 5,
    "print-time": 60,
    "health-print-time": 60,
    "dmi": true,
    "syslog": false,
    "tls": {
        "enabled": false,
        "protocols": null,
        "cert": null,
        "cert_key": null,
        "ciphers": null,
        "ciphersuites": null,
        "dhparam": null
    },
    "user-agent": null,
    "verbose": 0,
    "watch": true,
    "pause-on-battery": false
}
```
* I changed  **hugepages** from 128 to 10000 #1349 
* 128 -> speed 10s/60s/15m 24302.4 24464.9 n/a H/s max 24838.6 H/s
* 10000 -> speed 10s/60s/15m 24532.6 n/a n/a H/s max 24558.6 H/s
### OUTPUT
```
 * ABOUT        XMRig/6.8.2 gcc/9.3.0
 * LIBS         libuv/1.40.0 OpenSSL/1.1.1i hwloc/2.4.0
 * HUGE PAGES   supported
 * 1GB PAGES    supported
 * CPU          Intel(R) Xeon(R) CPU E7-8880 v3 @ 2.30GHz (4) 64-bit AES VM
                L2:16.0 MB L3:180.0 MB 64C/128T NUMA:4
 * MEMORY       14.1/3842.9 GB (0%)
                DIMM 0: 32 GB RAM @ 0 MHz DIMM 0
                ...
                DIMM 121: 32 GB RAM @ 0 MHz DIMM 121
 * MOTHERBOARD  Xen - HVM domU
 * DONATE       5%
 * ASSEMBLY     auto:intel
 * POOL #1      xmr-us-east1.nanopool.org:14433 coin monero
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       disabled
 * CUDA         disabled
[2021-02-17 02:51:42.849]  net      use pool xmr-us-east1.nanopool.org:14433 TLSv1.2 144.217.14.139
[2021-02-17 02:51:42.849]  net      fingerprint (SHA-256): "c38886efdee542ebd99801b75c75d3498d97978bbcdec07c7271cb19729e014f"
[2021-02-17 02:51:42.849]  net      new job from xmr-us-east1.nanopool.org:14433 diff 480045 algo rx/0 height 2298493
[2021-02-17 02:51:42.849]  cpu      use argon2 implementation AVX2
[2021-02-17 02:51:42.857]  msr      register values for "intel" preset have been set successfully (7 ms)
[2021-02-17 02:51:42.857]  randomx  init datasets algo rx/0 (128 threads) seed b353f283ee2e4460...
[2021-02-17 02:51:46.068]  randomx  #1 allocated 3072 MB huge pages 100% (3212 ms)
[2021-02-17 02:51:46.069]  randomx  #3 allocated 3072 MB huge pages 100% (3211 ms)
[2021-02-17 02:51:46.069]  randomx  #0 allocated 3072 MB huge pages 100% (3213 ms)
[2021-02-17 02:51:46.069]  randomx  #2 allocated 3072 MB huge pages 100% (3212 ms)
[2021-02-17 02:51:46.069]  randomx  -- allocated 12288 MB huge pages 100% 12/12 (3213 ms)
[2021-02-17 02:51:47.312]  randomx  #3 dataset ready (1242 ms)
[2021-02-17 02:51:47.635]  randomx  #0 dataset ready (322 ms)
[2021-02-17 02:51:47.635]  randomx  #1 dataset ready (322 ms)
[2021-02-17 02:51:47.644]  randomx  #2 dataset ready (332 ms)
[2021-02-17 02:51:47.644]  cpu      use profile  rx  (64 threads) scratchpad 2048 KB
[2021-02-17 02:51:47.691]  cpu      READY threads 64/64 (64) huge pages 100% 64/64 memory 131072 KB (47 ms)
[2021-02-17 02:52:05.606]  net      new job from xmr-us-east1.nanopool.org:14433 diff 480045 algo rx/0 height 2298494
[2021-02-17 02:52:10.109]  cpu      accepted (1/0) diff 480045 (121 ms)
|    CPU # | AFFINITY | 10s H/s | 60s H/s | 15m H/s |
|        0 |        0 |   382.1 |     n/a |     n/a |
|        1 |        1 |   383.8 |     n/a |     n/a |
|        2 |        2 |   390.3 |     n/a |     n/a |
|        3 |        3 |   372.0 |     n/a |     n/a |
|        4 |        4 |   377.0 |     n/a |     n/a |
|        5 |        5 |   390.7 |     n/a |     n/a |
|        6 |        6 |   386.8 |     n/a |     n/a |
|        7 |        7 |   391.2 |     n/a |     n/a |
|        8 |        8 |   391.9 |     n/a |     n/a |
|        9 |        9 |   390.3 |     n/a |     n/a |
|       10 |       10 |   385.7 |     n/a |     n/a |
|       11 |       11 |   374.7 |     n/a |     n/a |
|       12 |       12 |   388.7 |     n/a |     n/a |
|       13 |       13 |   375.4 |     n/a |     n/a |
|       14 |       14 |   389.3 |     n/a |     n/a |
|       15 |       15 |   376.8 |     n/a |     n/a |
|       16 |       16 |   396.3 |     n/a |     n/a |
|       17 |       17 |   377.5 |     n/a |     n/a |
|       18 |       18 |   381.5 |     n/a |     n/a |
|       19 |       19 |   363.4 |     n/a |     n/a |
|       20 |       20 |   368.1 |     n/a |     n/a |
|       21 |       21 |   397.2 |     n/a |     n/a |
|       22 |       22 |   380.8 |     n/a |     n/a |
|       23 |       23 |   381.1 |     n/a |     n/a |
|       24 |       24 |   382.7 |     n/a |     n/a |
|       25 |       25 |   368.1 |     n/a |     n/a |
|       26 |       26 |   371.8 |     n/a |     n/a |
|       27 |       27 |   368.4 |     n/a |     n/a |
|       28 |       28 |   383.3 |     n/a |     n/a |
|       29 |       29 |   367.5 |     n/a |     n/a |
|       30 |       30 |   363.0 |     n/a |     n/a |
|       31 |       31 |   371.4 |     n/a |     n/a |
|       32 |       32 |   400.4 |     n/a |     n/a |
|       33 |       33 |   395.9 |     n/a |     n/a |
|       34 |       34 |   402.3 |     n/a |     n/a |
|       35 |       35 |   384.0 |     n/a |     n/a |
|       36 |       36 |   388.2 |     n/a |     n/a |
|       37 |       37 |   396.7 |     n/a |     n/a |
|       38 |       38 |   400.2 |     n/a |     n/a |
|       39 |       39 |   402.3 |     n/a |     n/a |
|       40 |       40 |   401.4 |     n/a |     n/a |
|       41 |       41 |   388.5 |     n/a |     n/a |
|       42 |       42 |   385.6 |     n/a |     n/a |
|       43 |       43 |   388.0 |     n/a |     n/a |
|       44 |       44 |   401.9 |     n/a |     n/a |
|       45 |       45 |   387.2 |     n/a |     n/a |
|       46 |       46 |   385.0 |     n/a |     n/a |
|       47 |       47 |   388.7 |     n/a |     n/a |
|       48 |       48 |   390.4 |     n/a |     n/a |
|       49 |       49 |   388.2 |     n/a |     n/a |
|       50 |       50 |   392.4 |     n/a |     n/a |
|       51 |       51 |   373.9 |     n/a |     n/a |
|       52 |       52 |   377.2 |     n/a |     n/a |
|       53 |       53 |   386.2 |     n/a |     n/a |
|       54 |       54 |   390.6 |     n/a |     n/a |
|       55 |       55 |   392.2 |     n/a |     n/a |
|       56 |       56 |   390.3 |     n/a |     n/a |
|       57 |       57 |   376.9 |     n/a |     n/a |
|       58 |       58 |   373.4 |     n/a |     n/a |
|       59 |       59 |   379.1 |     n/a |     n/a |
|       60 |       60 |   392.6 |     n/a |     n/a |
|       61 |       61 |   378.7 |     n/a |     n/a |
|       62 |       62 |   375.9 |     n/a |     n/a |
|       63 |       63 |   379.6 |     n/a |     n/a |
|        - |        - | 24603.1 |     n/a |     n/a |
[2021-02-17 02:52:12.979]  miner    speed 10s/60s/15m 24603.1 n/a n/a H/s max 24824.9 H/s
```
## Benshmark RandomX
### Command 
```bash
xmrig --bench=1M --submit
xmrig --bench=10M --submit
xmrig --bench=1M --submit --threads=121
xmrig --bench=1M --submit --threads=34
xmrig --stress
```
### Results
<a href="https://xmrig.com/benchmark?cpu=Intel%28R%29+Xeon%28R%29+CPU+E7-8880+v3+%40+2.30GHz" target="_blank">XMRig Benchmark</a>

## Questions
1 - What can I do to make the optimal configuration/setup with this environments to get stable/better hashrate?
2 - If i use a dedicated server is better then i use a shared server  #2094  ?
3 - Did the swap (no swap) affect the hashrate?
4 - In other benchmarks i see the use of DIMM, this need configuration or what ! i can't find answer in the internet.
5 - Any other advanced configuration or help will help me to make a clear idea for the right setup.
Thanks

# Discussion History
## Spudz76 | 2021-02-17T04:31:14+00:00
1 - run on actual hardware instead
2 - yes always
3 - swap never matters (sometimes, on windows, it does - for some reason)
4 - DIMM reporting was added later so newer version benchmark submits DIMM info and it is only info not configurable (mostly to see how having full channels with interleave helps vs single stick in slow mode per CPU type)  Older submits will never have DIMM info but it is pointless for academic reference only
5 - Don't use virtual environment, it hides all hardware behind abstraction, but mining needs to control exactly what cores and what cache are being used, and never be pre-empted by other tasks (that unloads/loads the cache content, and registers, wasting time)

Affinity probably hasn't been tested for that many cpus, definitely doesn't work on Windows over 63 cores.

## xmrig | 2021-02-17T08:39:57+00:00
@MedGaSToN Not bad for a virtual machine, CPU topology virtualized well enough to make autoconfig work correctly. About hugepages you already use the fastest configuration: 12 large 1GB hugepages for RandomX datasets and 64 small 2 MB hugepages for mining threads. MSR mod doesn't work in VM even if it reported as working. You should avoid using command line option `--threads` on complex hardware/vm with multiple CPU/NUMA nodes, because proper CPU affinity is very important.

@Spudz76  Affinity over 63 supported on Windows.

## MedGaSToN | 2021-02-17T14:38:34+00:00
@Spudz76 thanks for clearing things, if I have that CPU on actual hardware how do I exactly control cores/cache/threads -> I didn't go deeper into cpu mining what I miss here any documentation or information will help.
@xmrig so no advanced setting is needed here?
About the L2/L3 cache, thread and CPU frequency -> more l2/l3 cache we have in cpu more that better? ¦ Higher frequency = higher hashrate?
For the ```--threads``` cmd it's just for testing I trust xmrig autoconfig 😊.
I'm not new on mining but I'm trying to build a server or multi server on AWS for monero mining :
1- Trying best hardware + config combo
2 - Benchmark and submit result to help community ofc with the best config on CPU to make a good benchmark.
So I'm in the right path what I'm doing here - configuration - is the best? Or I need extra work?
Thanks

## Spudz76 | 2021-02-18T07:28:29+00:00
Mining will always be worse in a VM than on real hardware.  No access to locking cores to cache and no access to CPU registers for turning off prefetch for speedup.  Also the CPU and the cache and everything else are virtualized so even if the miner requests these things they will be ignored and overridden.  The CPU cache may not be actual cache but virtual cache.

Cache just needs to be of whatever size times the number of cores.  The 'whatever size' changes per algo as I outlined.  There is no gain from having more than needed, just the target ideal is scratchpad size times active work threads.  Definite waste if the CPU has 8 cores but 4MB of cache or similar imbalance.

CPU speed is not terribly important most of the hashrate in Cryptonight comes from cache or memory accesses which even the slowest CPU usually waits for.

Some algos like RandomX family use system ram for the large reference block (just under 3GB) and hashrate can be hurt by not having widest memory path (all slots full, interleaving on, etc) or slow system memory (1066 in mobo that could do 1333 would lose hashrate, as would running single DIMM with no interleaving/wide pathing).  Cryptonights stay in cache so system memory is not as important there.

CPU should have AES extensions.  Hugepages help hashrate on some CPU types and algos, and don't hurt any.

## Spudz76 | 2021-02-18T07:28:58+00:00
I don't think benchmarks are accepted from VMs either

## MedGaSToN | 2021-02-19T07:56:15+00:00
@Spudz76 Thank, absolutely true. After 4 days of benchmarks using different CPUs --> Waste of time if the environment is virtual.
Thank you anyway.

# Action History
- Created by: MedGaSToN | 2021-02-17T03:18:13+00:00
- Closed at: 2021-02-19T07:56:19+00:00
