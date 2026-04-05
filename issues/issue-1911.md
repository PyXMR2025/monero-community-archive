---
title: 'msr: Write to unrecognized MSR 0xc0011020 by xmrig'
source_url: https://github.com/xmrig/xmrig/issues/1911
author: telans
assignees: []
labels:
- bug
created_at: '2020-10-23T12:11:43+00:00'
updated_at: '2020-10-23T19:44:04+00:00'
type: issue
status: closed
closed_at: '2020-10-23T19:44:03+00:00'
---

# Original Description
**Describe the bug**
Logs in `dmesg` indicate that MSR values failed to be set/written. I believe this is due to Linux > 5.9

**To Reproduce**
1. Run Linux > 5.9
2. Start xmrig with sudo/equivalent
3. Note `register values for "ryzen" preset has been set successfully` from xmrig output, yet dmesg compains.

**Expected behavior**
dmesg to not complain about unrecognized MSR

**Required data**
```
cpu      use argon2 implementation AVX2
msr      register values for "ryzen" preset has been set successfully (3 ms)
randomx  init dataset algo rx/0 (16 threads) seed 3612fdb32d87bb16...
andomx  allocated 2336 MB (2080+256) huge pages 100% 1168/1168 +JIT (213 ms)
randomx  dataset ready (2038 ms)
cpu      use profile  rx  (16 threads) scratchpad 2048 KB
cpu      READY threads 16/16 (16) huge pages 100% 16/16 memory 32768 KB
```
 - Config file: Unrelated, MSR not specified.
 - OS: Linux 5.9

**Additional context**
I'll note that the full error within dmesg is:

```
msr: Write to unrecognized MSR 0xc0011020 by xmrig
               Please report to x86@kernel.org
```
However, due to xmrig modifying MSR values I don't believe this is an issue with the kernel.

# Discussion History
## SChernykh | 2020-10-23T13:41:31+00:00
~~If xmrig doesn't print any msr-related errors it means values were set successfully. Register 0xc0011020 is undocumented, maybe this is why dmesg complains.~~

The above is wrong, possible code fix is in #1912 

## SChernykh | 2020-10-23T14:06:18+00:00
@telans According to https://github.com/torvalds/linux/commit/a7e1f67ed29f0c339e2aa7483d13b085127566ab#diff-2f768554951616110618f5c2f6b3a580b570ca63a9bbbe6b3300adf66ee84443 this is just a debug message, MSR register is still written to because `filter_write()` returns 0. What you should really do is to report to `x86@kernel.org` as the text suggests. Future versions of Linux kernel will then include this register into the list.

## telans | 2020-10-23T19:44:03+00:00
Thanks for the quick fix/update

# Action History
- Created by: telans | 2020-10-23T12:11:43+00:00
- Closed at: 2020-10-23T19:44:03+00:00
