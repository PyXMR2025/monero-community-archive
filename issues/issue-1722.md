---
title: ' Xmrig drops after allocating memory when using Intel Xeon Gold 6126.'
source_url: https://github.com/xmrig/xmrig/issues/1722
author: ayase-f
assignees: []
labels: []
created_at: '2020-06-08T17:05:20+00:00'
updated_at: '2020-08-19T01:16:12+00:00'
type: issue
status: closed
closed_at: '2020-08-19T01:16:12+00:00'
---

# Original Description
C:\Users\mind\Desktop\xmrig_6.0.1>xmrig.exe
 * ABOUT        XMRig/6.0.1-beta gcc/10.1.0
 * LIBS         libuv/1.38.0 OpenSSL/1.1.1g hwloc/2.2.0
 * HUGE PAGES   permission granted
 * 1GB PAGES    unavailable
 * CPU          Intel(R) Xeon(R) Gold 6126 CPU @ 2.60GHz (2) x64 AES
                L2:24.0 MB L3:38.5 MB 24C/48T NUMA:2
 * MEMORY       2.9/63.7 GB (5%)
 * DONATE       1%
 * ASSEMBLY     auto:intel
 * POOL #1      randomxmonero.jp.nicehash.com:3380 coin monero
 * POOL #2      randomxmonero.eu.nicehash.com:3380 coin monero
 * POOL #3      randomxmonero.eu.nicehash.com:3380 coin monero
 * POOL #4      randomxmonero.in.nicehash.com:3380 coin monero
 * COMMANDS     hashrate, pause, resume
 * HTTP API     127.0.0.1:65535
[2020-06-09 02:02:54.756]  config   configuration saved to: "C:\Users\mind\Deskt
op\xmrig_6.0.1\config.json"
 * OPENCL       disabled
 * CUDA         disabled
[2020-06-09 02:02:55.069]  net      use pool randomxmonero.jp.nicehash.com:3380
 172.65.229.122
[2020-06-09 02:02:55.069]  net      new job from randomxmonero.jp.nicehash.com:3
380 diff 262160 algo rx/0 height 2116256
[2020-06-09 02:02:55.069]  cpu      use argon2 implementation AVX-512F
[2020-06-09 02:02:55.850]  msr      register values for "intel" preset has been
set successfully (776 ms)
[2020-06-09 02:02:55.850]  randomx  init datasets algo rx/0 (48 threads) seed ca
86a505c85b39dd...
[2020-06-09 02:02:55.944]  randomx  #1 allocated 2080 MB huge pages 100% (96 ms)

[2020-06-09 02:02:55.975]  randomx  #0 allocated 2080 MB huge pages 100% (130 ms
)
[2020-06-09 02:02:55.991]  randomx  #0 allocated  256 MB huge pages 100% +JIT (1
4 ms)
[2020-06-09 02:02:55.991]  randomx  -- allocated 4416 MB huge pages 100% 2208/22
08 (147 ms)

# Discussion History
## downystreet | 2020-06-08T17:31:29+00:00
Are you saying that it closes out or just keeps running with no new jobs? Are you getting any kind of error message? Also, have you updated xmrig recently? And why are you mining from 4 different pools?

## ayase-f | 2020-06-08T17:38:50+00:00
Symptoms occur with newer versions than 5.11.2.
Pronto returns without an error.

## SChernykh | 2020-06-09T08:23:40+00:00
Does 5.11.2 work with the same config.json? Can you try v6.2.0-beta - both gcc and msvc versions?

## ayase-f | 2020-06-09T11:33:07+00:00
I tried the 6.2.0-beta gcc and msvc versions using config.json which works fine with 5.11.1, but the results were the same.
Paste the console output, including the 5.11.1 result.

C:\Users\mind\Desktop\xmrig_6.2.0>xmrig.exe

ABOUT XMRig/6.2.0-beta MSVC/2019
LIBS libuv/1.38.0 OpenSSL/1.1.1g hwloc/2.2.0
HUGE PAGES permission granted
1GB PAGES unavailable
CPU Intel(R) Xeon(R) Gold 6126 CPU @ 2.60GHz (2) x64 AES
L2:24.0 MB L3:38.5 MB 24C/48T NUMA:2
MEMORY 2.9/63.7 GB (5%)
DONATE 1%
ASSEMBLY auto:intel
POOL #1 randomxmonero.jp.nicehash.com:3380 coin monero
POOL #2 randomxmonero.eu.nicehash.com:3380 coin monero
POOL #3 randomxmonero.eu.nicehash.com:3380 coin monero
POOL #4 randomxmonero.in.nicehash.com:3380 coin monero
COMMANDS hashrate, pause, resume
HTTP API 127.0.0.1:65535
OPENCL disabled
CUDA disabled
[2020-06-09 20:26:35.774] net use pool randomxmonero.jp.nicehash.com:3380
172.65.229.122
[2020-06-09 20:26:35.776] net new job from randomxmonero.jp.nicehash.com:3
380 diff 262160 algo rx/0 height 2116799
[2020-06-09 20:26:35.777] cpu use argon2 implementation AVX-512F
[2020-06-09 20:26:36.568] msr register values for "intel" preset has been
set successfully (791 ms)
[2020-06-09 20:26:36.569] randomx init datasets algo rx/0 (48 threads) seed ca
86a505c85b39dd...
[2020-06-09 20:26:36.669] randomx #1 allocated 2080 MB huge pages 100% (98 ms)
[2020-06-09 20:26:36.702] randomx #0 allocated 2080 MB huge pages 100% (132 ms
)
[2020-06-09 20:26:36.717] randomx #0 allocated 256 MB huge pages 100% +JIT (1
4 ms)
[2020-06-09 20:26:36.718] randomx -- allocated 4416 MB huge pages 100% 2208/22
08 (148 ms)
C:\Users\mind\Desktop\xmrig_6.2.0>

C:\Users\mind\Desktop\xmrig_6.2.0>xmrig.exe

ABOUT XMRig/6.2.0-beta gcc/10.1.0
LIBS libuv/1.38.0 OpenSSL/1.1.1g hwloc/2.2.0
HUGE PAGES permission granted
1GB PAGES unavailable
CPU Intel(R) Xeon(R) Gold 6126 CPU @ 2.60GHz (2) x64 AES
L2:24.0 MB L3:38.5 MB 24C/48T NUMA:2
MEMORY 2.9/63.7 GB (5%)
DONATE 1%
ASSEMBLY auto:intel
POOL #1 randomxmonero.jp.nicehash.com:3380 coin monero
POOL #2 randomxmonero.eu.nicehash.com:3380 coin monero
POOL #3 randomxmonero.eu.nicehash.com:3380 coin monero
POOL #4 randomxmonero.in.nicehash.com:3380 coin monero
COMMANDS hashrate, pause, resume
HTTP API 127.0.0.1:65535
OPENCL disabled
CUDA disabled
[2020-06-09 20:27:13.199] net use pool randomxmonero.jp.nicehash.com:3380
172.65.229.122
[2020-06-09 20:27:13.199] net new job from randomxmonero.jp.nicehash.com:3
380 diff 262160 algo rx/0 height 2116799
[2020-06-09 20:27:13.199] cpu use argon2 implementation AVX-512F
[2020-06-09 20:27:13.980] msr register values for "intel" preset has been
set successfully (777 ms)
[2020-06-09 20:27:13.980] randomx init datasets algo rx/0 (48 threads) seed ca
86a505c85b39dd...
[2020-06-09 20:27:14.074] randomx #0 allocated 2080 MB huge pages 100% (97 ms)
[2020-06-09 20:27:14.105] randomx #1 allocated 2080 MB huge pages 100% (131 ms
)
[2020-06-09 20:27:14.121] randomx #0 allocated 256 MB huge pages 100% +JIT (1
3 ms)
[2020-06-09 20:27:14.121] randomx -- allocated 4416 MB huge pages 100% 2208/22
08 (148 ms)

C:\Users\mind\Desktop\xmrig_6.2.0>

C:\Users\mind\Desktop\xmrig>xmrig.exe

ABOUT XMRig/5.11.1 MSVC/2017
LIBS libuv/1.31.0 OpenSSL/1.1.1c hwloc/2.1.0
HUGE PAGES permission granted
1GB PAGES unavailable
CPU Intel(R) Xeon(R) Gold 6126 CPU @ 2.60GHz (2) x64 AES
L2:24.0 MB L3:38.5 MB 24C/48T NUMA:2
MEMORY 2.9/63.7 GB (5%)
DONATE 1%
ASSEMBLY auto:intel
POOL #1 randomxmonero.eu.nicehash.com:3380 algo rx/0
POOL #2 randomxmonero.jp.nicehash.com:3380 algo rx/0
POOL #3 randomxmonero.br.nicehash.com:3380 algo rx/0
POOL #4 randomxmonero.in.nicehash.com:3380 algo rx/0
COMMANDS hashrate, pause, resume
OPENCL disabled
CUDA disabled
[2020-06-09 20:28:39.099] net use pool randomxmonero.eu.nicehash.com:3380 172
.65.200.133
[2020-06-09 20:28:39.101] net new job from randomxmonero.eu.nicehash.com:3380
diff 262160 algo rx/0 height 2116799
[2020-06-09 20:28:39.881] msr register values for "intel" preset has been set
successfully (778 ms)
[2020-06-09 20:28:39.882] rx init datasets algo rx/0 (48 threads) seed ca86a5
05c85b39dd...
[2020-06-09 20:28:39.981] rx #1 allocated 2080 MB huge pages 100% (97 ms)
[2020-06-09 20:28:40.014] rx #0 allocated 2080 MB huge pages 100% (131 ms)
[2020-06-09 20:28:40.030] rx #0 allocated 256 MB huge pages 100% +JIT (15 ms
)
[2020-06-09 20:28:40.032] rx -- allocated 4416 MB huge pages 100% 2208/2208 (
148 ms)
[2020-06-09 20:28:41.998] rx #0 dataset ready (1964 ms)
[2020-06-09 20:28:42.801] rx #1 dataset ready (802 ms)
[2020-06-09 20:28:42.802] cpu use profile rx (24 threads) scratchpad 2048 KB
[2020-06-09 20:28:43.536] cpu READY threads 24/24 (24) huge pages 100% 24/24 m
emory 49152 KB (733 ms)
[2020-06-09 20:28:45.028] cpu accepted (1/0) diff 262160 (313 ms)

## SChernykh | 2020-06-09T11:38:05+00:00
Can you find `"argon2-impl": null,` in config.json under `cpu` section for xmrig 6.2.0 and set it to `"argon2-impl": "AVX2",`? I suspect that Argon2 AVX-512F causes XMRig to crash.

## ayase-f | 2020-06-09T11:46:36+00:00
After changing the setting to AVX2, mining started.
Thank you.

# Action History
- Created by: ayase-f | 2020-06-08T17:05:20+00:00
- Closed at: 2020-08-19T01:16:12+00:00
