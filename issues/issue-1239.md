---
title: Xmrig Can you answer me. Regarding the problem of the CPU!
source_url: https://github.com/xmrig/xmrig/issues/1239
author: ghost
assignees: []
labels: []
created_at: '2019-10-13T11:04:56+00:00'
updated_at: '2019-12-22T19:28:38+00:00'
type: issue
status: closed
closed_at: '2019-12-22T19:28:38+00:00'
---

# Original Description
@xmrig Once again bother you.
I tested with 2 old versions 2.14.1 and new 4.3.1. Same configuration Intel Xeon Platinum 8168.
With the old version running enough CPU and hashrate. And the new version only runs 1/2 CPU.
I configured the new version running 16/16 CPU hashrate reduced.
What do I have to configure with the new version to get full CPU and hashrate.

Details you see the picture below.

<img src="https://i.imgur.com/N6I8oz4.jpg" />
<img src="https://i.imgur.com/Po9sQ78.jpg" />

# Discussion History
## Spudz76 | 2019-10-29T21:50:31+00:00
New versions use hwloc, try with hwloc disabled to cause newer versions to use older thread allocation strategy.

hwloc uses motherboards ACPI advertised hierarchy which is sometimes incorrect.  There is no way to detect if its wiring table is built by sloppy idiots, or matches reality perfectly, so if it doesn't work right for your motherboard you have to disable it.  Occasionally a BIOS update fixes ACPI tables but not very often.

But there were also other changes to optimization which could have an effect.  Also gcc7 or newer is better, I personally use clang-10 everywhere which seems to give me the fastest running code across most CPUs.  gcc5 is likely very lightly tested, if at all anymore, and pre-gcc5.5 was buggy with miner code (you are on 5.4.0 which definitely doesn't work best).

# Action History
- Created by: ghost | 2019-10-13T11:04:56+00:00
- Closed at: 2019-12-22T19:28:38+00:00
