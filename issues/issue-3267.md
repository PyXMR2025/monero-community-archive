---
title: 'How to use 1GB pages on android kernel with THP enabled '
source_url: https://github.com/xmrig/xmrig/issues/3267
author: spiral009
assignees: []
labels: []
created_at: '2023-05-13T16:31:57+00:00'
updated_at: '2025-06-18T22:36:58+00:00'
type: issue
status: closed
closed_at: '2025-06-18T22:36:58+00:00'
---

# Original Description
```
.../files/home # zcat /proc/config.gz  |grep HUGEP
CONFIG_HAVE_ARCH_TRANSPARENT_HUGEPAGE=y
CONFIG_TRANSPARENT_HUGEPAGE=y
# CONFIG_TRANSPARENT_HUGEPAGE_ALWAYS is not set
CONFIG_TRANSPARENT_HUGEPAGE_MADVISE=y
```
```
.../files/home # tree /sys/kernel/mm
/sys/kernel/mm
├── swap
│   └── vma_ra_enabled
└── transparent_hugepage
    ├── defrag
    ├── enabled
    ├── hpage_pmd_size
    ├── khugepaged
    │   ├── alloc_sleep_millisecs
    │   ├── defrag
    │   ├── full_scans
    │   ├── max_ptes_none
    │   ├── max_ptes_swap
    │   ├── pages_collapsed
    │   ├── pages_to_scan
    │   └── scan_sleep_millisecs
    ├── shmem_enabled
    └── use_zero_page

4 directories, 14 files
.../files/home #
```
There's no path to `/sys/kernel/mm/hugepages/hugepages-1048576kB/nr_hugepages`
```
```
root@localhost:~/xmrig/build# ./xmrig
 * ABOUT        XMRig/6.19.2 gcc/12.2.0
 * LIBS         libuv/1.44.2 OpenSSL/3.0.5 hwloc/2.8.0
 * HUGE PAGES   supported
 * 1GB PAGES    unavailable
 * CPU          ARMv8 (3) 64-bit AES
                L2:0.0 MB L3:0.0 MB 8C/8T NUMA:1
 * MEMORY       3.7/11.2 GB (33%)
 * DONATE       1%
 * POOL #1      pool.xmrfast.com:9000 algo auto
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       disabled
 * CUDA         disabled
[2023-05-13 16:31:23.950]  signal   Ctrl+C received, exiting
```


# Discussion History
## Spudz76 | 2023-05-13T19:54:38+00:00
CPU must also support it, and ARM doesn't, along with some Intels.  When there is no CPU support the path won't exist.

## spiral009 | 2023-05-13T23:47:27+00:00
My phone crashed after a while when i compiled it with `CONFIG_TRANSPARENT_HUGEPAGE_ALWAYS` so i guess  it's working , also memory usage was high 

# Action History
- Created by: spiral009 | 2023-05-13T16:31:57+00:00
- Closed at: 2025-06-18T22:36:58+00:00
