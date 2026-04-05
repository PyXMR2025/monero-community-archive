---
title: Clarification of RandomX + huge pages behaviour on ARMv8
source_url: https://github.com/xmrig/xmrig/issues/2970
author: KodeMunkie
assignees: []
labels:
- question
created_at: '2022-03-14T20:37:48+00:00'
updated_at: '2022-04-03T07:57:23+00:00'
type: issue
status: closed
closed_at: '2022-04-03T07:57:23+00:00'
---

# Original Description
**Describe the bug**
XMRig 6.16.2 on ARMv8 (Raspberry Pi 4 8GB) states that huge pages are available, but appears unable to allocate the huge page memory.

**To Reproduce**
Compile and run XMRig for ARM64 on a Raspberry Pi 4 8GB. Watch the startup output show huge pages supported, then fail to allocate.

**Expected behavior**
Huge page memory is allocated - text for memory allocation is green and showing 100%.

**Required data**
```
 * ABOUT        XMRig/6.16.2 gcc/10.2.1
 * LIBS         libuv/1.40.0 OpenSSL/1.1.1k hwloc/2.4.1
...

 * HUGE PAGES   supported
 * 1GB PAGES    unavailable
 * CPU          ARM Cortex-A72 (1) 64-bit -AES
                L2:0.0 MB L3:0.0 MB 4C/4T NUMA:1
 * MEMORY       0.7/7.6 GB (9%)
...

[2022-03-14 20:22:00.909]  randomx  allocated 2336 MB (2080+256) huge pages 0% 0/1168 +JIT (1 ms)
...
[2022-03-14 20:22:27.465]  cpu      READY threads 2/2 (2) huge pages 0% 0/2 memory 4096 KB (1 ms)
```

**Additional context**
Nb. mostly likely unrelated but the L2 cache isn't recognised either (should be 1MB).

# Discussion History
## Spudz76 | 2022-03-14T23:29:46+00:00
Does it work when `echo 3 > /sys/kernel/mm/hugepages/hugepages-1048576kB/nr_hugepages` before running xmrig?

## Spudz76 | 2022-03-14T23:32:23+00:00
Also could try forcing early allocation with added kernel args:
```
hugepagesz=1GB hugepages=3
```

Sometimes there aren't 3GB of aligned free memory after boot.

## Spudz76 | 2022-03-15T00:34:31+00:00
Oops you meant 2MB hugepages.  ARM doesn't even support 1GB.  Same tips except replace 1084576 with 2048, and number of pages to ~1200

## xmrig | 2022-04-03T07:57:23+00:00
@Spudz76 Technically ARM supports 1GB pages and other sizes too, it can be tested on Amazon instances, but for small boards this statement is true.

# Action History
- Created by: KodeMunkie | 2022-03-14T20:37:48+00:00
- Closed at: 2022-04-03T07:57:23+00:00
