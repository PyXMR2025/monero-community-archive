---
title: 1GB huge pages on ARM64
source_url: https://github.com/xmrig/xmrig/issues/1918
author: jfikar
assignees: []
labels:
- bug
- arm
created_at: '2020-10-27T14:22:01+00:00'
updated_at: '2020-11-06T19:27:01+00:00'
type: issue
status: closed
closed_at: '2020-11-06T19:27:01+00:00'
---

# Original Description
[In principle](https://wiki.debian.org/Hugepages), there should be 1GB huge pages available on every ARM64. But I could not turn them on by `"1gb-pages": true`, xmrig always says `* 1GB PAGES    disabled` .

It seems that xmrig check in the file `src/backend/cpu/platform/BasicCpuInfo.h` the presence of CPU `FLAG_PDPE1GB`. It is useful on X86, but Linux on ARM64 does not show `pdpe1gb` CPU flag.

I didn't know, how to do it correctly, but I simply replaced `return FLAG_PDPE1GB` with `return 1 `and it works.

I activate the pages with `echo 3 | sudo tee /sys/kernel/mm/hugepages/hugepages-1048576kB/nr_hugepages`, but it is possible only on 8GB RAM board. On a 4GB RAM board kernel says it does not have so much space and only 2 1GB pages are activated, which is not enough.

For rx/arq I observe approximately 2% increase of hash rate.

As a side note: it seems that transparent huge pages (THP) deliver the same speedup as 2MB huge pages, but it is much easier to setup. Just echo `enabled | sudo tee /sys/kernel/mm/transparent_hugepage/enabled` and run program without anything special. Some Linux distributions may have that enabled by default.

Others may have `madvise` instead. It seems that in `src/crypto/common/VirtualMemory_unix.cpp` you already have `madvise(m_scratchpad, m_size, MADV_RANDOM | MADV_WILLNEED)`. Maybe it would be good to add `MADV_HUGEPAGE` as well? Then THP will work also for `madvise | sudo tee /sys/kernel/mm/transparent_hugepage/enabled`.

I think I'll play also with `MADV_MERGEABLE`, maybe I'll be able to use 1GB huge pages on 4GB RAM board.

As a second side note:
Linux kernel on my board does not show the size of L2 cache. So `hwloc` cannot get it and xmrig shows 0.0 MB. I tried to hard-code it in `src/backend/cpu/platform/HwlocCpuInfo.h`, but I'm not sure it is used anywhere. Is it? Or it is just printed out?

The only tool reporting correctly L2 size seems the `cache-info` from [cpuinfo](https://github.com/pytorch/cpuinfo).

# Discussion History
## xmrig | 2020-11-02T12:46:57+00:00
I can confirm 1GB huge pages work on ARM https://xmrig.com/benchmark/BqaCVE3Fnxv so only stop factor is `FLAG_PDPE1GB` check as you discovered, it will be fixed in next release by checking existence of `/sys/kernel/mm/hugepages/hugepages-1048576kB/nr_hugepages` file.

Size of CPU caches is not a big issue on ARM since autoconfiguration is very simplified, it always uses all cores, but I will take a closer look to the cpuinfo tool.
Thank you.

## Saikatsaha1996 | 2020-11-02T13:04:41+00:00
> I can confirm 1GB huge pages work on ARM https://xmrig.com/benchmark/BqaCVE3Fnxv so only stop factor is `FLAG_PDPE1GB` check as you discovered, it will be fixed in next release by checking existence of `/sys/kernel/mm/hugepages/hugepages-1048576kB/nr_hugepages` file.
> 
> Size of CPU caches is not a big issue on ARM since autoconfiguration is very simplified, it always uses all cores, but I will take a closer look to the cpuinfo tool.
> Thank you.

So how can i enable 1 gb huge page in arm?

## xmrig | 2020-11-02T13:39:28+00:00
@Saikatsaha1996 First you need more than 4GB of memory and `cat /sys/kernel/mm/hugepages/hugepages-1048576kB/nr_hugepages` should return `0` if all good you can continue.

1. Replace [this line](https://github.com/xmrig/xmrig/blob/master/src/backend/cpu/platform/BasicCpuInfo.h#L53) to `inline bool hasOneGbPages() const override { return true; }` and recompile the miner.
2. Enable 1GB pages in config https://github.com/xmrig/xmrig/blob/master/src/config.json#L20
3. Run miner as root or with sudo.


## Saikatsaha1996 | 2020-11-02T13:42:39+00:00
> @Saikatsaha1996 First you need more than 4GB of memory and `cat /sys/kernel/mm/hugepages/hugepages-1048576kB/nr_hugepages` should return `0` if all good you can continue.
> 
> 1. Replace [this line](https://github.com/xmrig/xmrig/blob/master/src/backend/cpu/platform/BasicCpuInfo.h#L53) to `inline bool hasOneGbPages() const override { return true; }` and recompile the miner.
> 2. Enable 1GB pages in config https://github.com/xmrig/xmrig/blob/master/src/config.json#L20
> 3. Run miner as root or with sudo.

Thank you so much for your help..
So i need to fast root my mobile after i can enable 1gb page.. 
I haven't no issue with my ram.. total ram 6gb.. but fast i want to root my mobile..

## jfikar | 2020-11-06T19:26:57+00:00
It works, good job!

# Action History
- Created by: jfikar | 2020-10-27T14:22:01+00:00
- Closed at: 2020-11-06T19:27:01+00:00
