---
title: Add memory specifications to benchmark information
source_url: https://github.com/xmrig/xmrig/issues/2038
author: BillGatesIII
assignees: []
labels:
- enhancement
created_at: '2021-01-12T18:41:26+00:00'
updated_at: '2021-01-27T19:59:59+00:00'
type: issue
status: closed
closed_at: '2021-01-27T19:59:58+00:00'
---

# Original Description
It would be nice to have the memory specifications shown on the benchmark page.

For example:
. | AMD Ryzen Threadripper 3970X 32-Core Processor (1)
-- | --
Threading | 32 cores / 64 threads / 1 CPU / 1 node
Caches | L2: 16.0 MB / L3: 128.0 MB
CPUID | 830F10 / Family: 17 / Model: 31 / Stepping: 0
Memory | 4 x 8GB DDR4 @ 3200Mhz CL 13-12-14-27
Flags | aes, avx, avx2, bmi2, osxsave, pdpe1gb, sse2, ssse3, sse4.1, popcnt, cat_l3
Backend | hwloc/2.1.0



# Discussion History
## Spudz76 | 2021-01-13T20:42:13+00:00
Not sure how system memory specs matter since most algos avoid using it anyway (cache resident only).

Guess it makes some difference on DAG based (KawPow) however that doesn't work on CPU anyway so...

## xmrig | 2021-01-16T17:26:54+00:00
@Spudz76 Memory is very important for RandomX algorithms, all top results achieved with fine tuned memory. Online benchmark also accept only RandomX algorithms so it is useful information.

Seems possible to get almost all information about memory modules via SMBIOS on Linux and Windows. What information available can be viewed by `dmidecode -t 17` command.

2 disadvantages:
1. Memory timings not available.
2. On Linux super user permissions required to read data.

## BillGatesIII | 2021-01-17T13:37:06+00:00
I did some research and as far as I understand it is possible for DDR4 to read the SPD data which also has the memory timings.
[https://manpages.debian.org/buster/i2c-tools/decode-dimms.1.en.html](url)

I couldn't find a better code example than this one.
[https://github.com/xabar/spd_utils](url)

And here is some background information.
[https://damieng.com/blog/2020/02/08/ddr4-ram-spd-linux](url)

I always run xmrig with 'sudo xmrig' because of the WSMR writes so then it should be possible to read this data also? Or doesn it work that way?

## xmrig | 2021-01-17T15:59:41+00:00
Thank you for links especially last one. I going to implement DMI/SMBIOS reader first, at least it is most portable solution, without timings but better than nothing. `sudo xmrig` is fine.

## Spudz76 | 2021-01-18T20:49:44+00:00
Oh right, RandomX uses large dataset, guess it would matter then.  Used to thinking CN where everything is cache and system ram doesn't matter.

Come to think of it adding a second DIMM to some rigs recently and updating from 1066 to 1333 did make their RX work better.

## Spudz76 | 2021-01-18T20:51:33+00:00
libsensors should be able to pick up the SPD info
bonus maybe the miner could show CPU therms and stuff similar to how it does on GPUs...

## xmrig | 2021-01-21T17:40:39+00:00
Implemented in dev branch.
Thank you.

## BillGatesIII | 2021-01-27T19:59:58+00:00
> Implemented in dev branch.
> Thank you.

Looks great, thank you.

# Action History
- Created by: BillGatesIII | 2021-01-12T18:41:26+00:00
- Closed at: 2021-01-27T19:59:58+00:00
