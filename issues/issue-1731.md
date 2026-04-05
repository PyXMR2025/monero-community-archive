---
title: 'why it is not work '
source_url: https://github.com/xmrig/xmrig/issues/1731
author: tips1127
assignees: []
labels: []
created_at: '2020-06-12T01:29:59+00:00'
updated_at: '2020-08-19T01:14:34+00:00'
type: issue
status: closed
closed_at: '2020-08-19T01:14:34+00:00'
---

# Original Description
 * ABOUT        XMRig/5.11.3 MSVC/2019
 * LIBS         libuv/1.38.0 OpenSSL/1.1.1g hwloc/2.2.0
 * HUGE PAGES   permission granted
 * 1GB PAGES    unavailable
 * CPU          Intel(R) Xeon(R) CPU E31220 @ 3.10GHz (1) x64 AES
                L2:1.0 MB L3:8.0 MB 4C/4T NUMA:1
 * MEMORY       1.3/8.0 GB (16%)
 * DONATE       5%
 * ASSEMBLY     auto:intel
 * POOL #1      foundation.biblepay.org:3001 algo auto
 * COMMANDS     hashrate, pause, resume
 * OPENCL       disabled
 * CUDA         disabled
[2020-06-12 09:26:31.746]  net  use pool foundation.biblepay.org:3001  104.238.1
47.232
[2020-06-12 09:26:31.746]  net  new job from foundation.biblepay.org:3001 diff 7
5000 algo rx/0 height 2118653
[2020-06-12 09:26:31.746]  cpu  use argon2 implementation SSSE3
[2020-06-12 09:26:31.934]  msr  register values for "intel" preset has been set
successfully (175 ms)
[2020-06-12 09:26:31.934]  rx   init dataset algo rx/0 (4 threads) seed d10ce093
9583c30c...
[2020-06-12 09:26:32.199]  rx   allocated 2336 MB (2080+256) huge pages 11% 128/
1168 +JIT (266 ms)
[2020-06-12 09:26:39.843]  rx   dataset ready (7643 ms)
[2020-06-12 09:26:39.843]  cpu  use profile  rx  (4 threads) scratchpad 2048 KB
[2020-06-12 09:26:39.952]  cpu  READY threads 4/4 (4) huge pages 100% 4/4 memory
 8192 KB (106 ms)
请按任意键继续. . .

it not work

# Discussion History
## Spudz76 | 2020-06-13T21:57:22+00:00
1.3GB free memory at start not enough for any RandomX algo.
Tune system for more free memory first.  Also enable hugepages so you get 100% allocation.
Needs about 2.5GB free probably minimum (2080MB for dataset and then 8MB for 4 threads, so 2088MB free required but may need a little slack space also)

## snipeTR | 2020-06-14T08:45:24+00:00
@echo off
for /f "skip=1" %%p in ('wmic os get FreeVirtualMemory') do ( 
  set m=%%p
  goto :done
)
:done
if %m% gtr 2621440 (
xmrig.exe ) else (
echo free memory is insufficient.
)
pause


# Action History
- Created by: tips1127 | 2020-06-12T01:29:59+00:00
- Closed at: 2020-08-19T01:14:34+00:00
