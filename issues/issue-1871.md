---
title: Error in randomx.cpp:463 in version 6.3.4 and 6.3.5
source_url: https://github.com/xmrig/xmrig/issues/1871
author: BillGatesIII
assignees: []
labels:
- bug
created_at: '2020-10-06T16:21:29+00:00'
updated_at: '2021-04-12T14:47:15+00:00'
type: issue
status: closed
closed_at: '2021-04-12T14:47:15+00:00'
---

# Original Description
**Describe the bug**
xmrig: /home/user/xmrig/src/crypto/randomx/randomx.cpp:463: randomx_vm* randomx_create_vm(randomx_flags, randomx_cache*, randomx_dataset*, uint8_t*, uint32_t): Assertion `cache == nullptr || cache->isInitialized()' failed.

**To Reproduce**
Start xmrig 6.3.4 or 6.3.5.

**Expected behavior**
No error, like in 6.3.3.

**Required data**
 * ABOUT        XMRig/6.3.5 gcc/8.3.0
 * LIBS         libuv/1.38.1 OpenSSL/1.1.1g hwloc/2.2.0
 * HUGE PAGES   supported
 * 1GB PAGES    supported
 * CPU          Intel(R) Xeon(R) CPU E5-2620 v2 @ 2.10GHz (2) x64 AES
                L2:3.0 MB L3:30.0 MB 12C/24T NUMA:2
 * MEMORY       6.7/62.8 GB (11%)
 * DONATE       1%
 * ASSEMBLY     auto:intel
 * POOL #1      xmrpool.eu:5555 algo cn/r
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       disabled
 * CUDA         disabled
[2020-10-06 18:02:52.504]  net      use pool xmrpool.eu:5555  54.37.7.208
[2020-10-06 18:02:52.504]  net      new job from xmrpool.eu:5555 diff 50000 algo rx/0 height 2202466
[2020-10-06 18:02:52.504]  cpu      use argon2 implementation SSSE3
[2020-10-06 18:02:52.514]  msr      register values for "custom" preset has been set successfully (10 ms)
[2020-10-06 18:02:52.514]  randomx  init datasets algo rx/0 (24 threads) seed aeb044aa31eab166...
[2020-10-06 18:02:54.066]  randomx  #0 allocated 3072 MB huge pages 100% (1553 ms)
[2020-10-06 18:02:54.066]  randomx  #1 allocated 3072 MB huge pages 100% (1553 ms)
[2020-10-06 18:02:54.066]  randomx  -- allocated 6144 MB huge pages 100% 6/6 (1553 ms)
[2020-10-06 18:03:04.282]  randomx  #1 dataset ready (10215 ms)
[2020-10-06 18:03:05.975]  randomx  #0 dataset ready (1693 ms)
[2020-10-06 18:03:05.976]  cpu      use profile  rx  (12 threads) scratchpad 2048 KB
xmrig: /home/user/xmrig/src/crypto/randomx/randomx.cpp:463: randomx_vm* randomx_create_vm(randomx_flags, randomx_cache*, randomx_dataset*, uint8_t*, uint32_t): Assertion `cache == nullptr || cache->isInitialized()' failed.
./startxmrig.sh: line 12:  2206 Aborted                 ./xmrig

 - Config file or command line (without wallets)
    "randomx": {
        "init": -1,
        "mode": "auto",
        "1gb-pages": true,
        "rdmsr": true,
        "wrmsr": ["0x1a4:0xf"],
        "cache_qos": false,
        "numa": true
    },
    "cpu": {
        "enabled": true,
        "huge-pages": true,
        "hw-aes": null,
        "priority": null,
        "memory-pool": false,
        "yield": false,
        "asm": true,
        "argon2-impl": null,
        "astrobwt-max-size": 550,
        "astrobwt-avx2": false,
        "rx": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
        "cn/0": false,
        "cn-lite/0": false,
        "rx/arq": "rx/wow",
        "rx/keva": "rx/wow"
}
 - OS: [e.g. Windows]
Debian 10.6.


# Discussion History
# Action History
- Created by: BillGatesIII | 2020-10-06T16:21:29+00:00
- Closed at: 2021-04-12T14:47:15+00:00
