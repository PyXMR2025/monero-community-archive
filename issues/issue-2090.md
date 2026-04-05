---
title: Failed to allocate RandomX dataset, switching to slow mode with enough memory
source_url: https://github.com/xmrig/xmrig/issues/2090
author: y-luis-rojo
assignees: []
labels: []
created_at: '2021-02-09T17:00:55+00:00'
updated_at: '2021-02-09T17:21:02+00:00'
type: issue
status: closed
closed_at: '2021-02-09T17:21:02+00:00'
---

# Original Description
```
* ABOUT        XMRig/6.7.2 gcc/5.4.0
 * LIBS         libuv/1.40.0 OpenSSL/1.1.1i hwloc/2.4.0
 * HUGE PAGES   supported
 * 1GB PAGES    disabled
 * CPU          Intel(R) Xeon(R) CPU E5-2673 v4 @ 2.30GHz (1) 64-bit AES VM
                L2:0.2 MB L3:50.0 MB 1C/1T NUMA:1
 * MEMORY       3.2/3.4 GB (97%)
 * DONATE       1%
 * ASSEMBLY     auto:intel
 * POOL #1      pool.xmr.pt:9000 coin monero
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       disabled
 * CUDA         disabled
[2021-02-09 16:44:21.508]  net      use pool pool.xmr.pt:9000 TLSv1.2 94.46.164.183
[2021-02-09 16:44:21.508]  net      fingerprint (SHA-256): "2da9b63362821d82add4c5031a8cf0d3adc5f8fdce157a93a25fa972eecb6d34"
[2021-02-09 16:44:21.508]  net      new job from pool.xmr.pt:9000 diff 20000 algo rx/0 height 2293156
[2021-02-09 16:44:21.508]  cpu      use argon2 implementation AVX2
[2021-02-09 16:44:21.512]  msr      register values for "intel" preset has been set successfully (3 ms)
[2021-02-09 16:44:21.512]  randomx  init dataset algo rx/0 (1 threads) seed 0543daca43fca6c4...
[2021-02-09 16:44:21.608]  randomx  failed to allocate RandomX dataset, switching to slow mode (96 ms)
[2021-02-09 16:44:22.180]  randomx  dataset ready (572 ms)
```

OS: CentOS

Why does RandomX fails to allocate dataset since memory requirements are OK?

# Discussion History
## SChernykh | 2021-02-09T17:09:26+00:00
`* MEMORY       3.2/3.4 GB (97%)`
It means 97% of memory is already by something else, you just don't have 2 GB free for the dataset.

## y-luis-rojo | 2021-02-09T17:21:02+00:00
Oh! That's it. Thanks @SChernykh!

# Action History
- Created by: y-luis-rojo | 2021-02-09T17:00:55+00:00
- Closed at: 2021-02-09T17:21:02+00:00
