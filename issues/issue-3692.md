---
title: Benchmark doesn't stop
source_url: https://github.com/xmrig/xmrig/issues/3692
author: dan1338
assignees: []
labels: []
created_at: '2025-08-09T10:35:18+00:00'
updated_at: '2025-10-01T01:47:35+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
**Describe the bug**
When running xmrig benchmark I find that it often keeps running past 1M hashes, effectively never stopping.
Out of 20 runs maybe 5 ended properly with "benchmark finished" and url to submitted results, alongside a prompt to Ctrl+C to exit.
All the other runs just kept periodically reporting total hashes exceeding 1M, like " bench    118.07% 1180719/1000000"

**To Reproduce**
./xmrig --bench=1M --submit

**Expected behavior**
Stop mining and show the user url with submitted benchmark

**Required data**
 - XMRig version (happens on both)
   - https://github.com/xmrig/xmrig/releases/download/v6.24.0/xmrig-6.24.0-linux-static-x64.tar.gz
   - built from master (6e4a5a6d94b33d6ed93890126c699b62f9553f50)
 - OS: Linux 6.14.0-27-generic 24.04.1-Ubuntu SMP PREEMPT_DYNAMIC x86_64

**Additional context**
Example logs:
```
[2025-08-09 12:31:10.289]  bench    start benchmark hashes 1M algo rx/0
[2025-08-09 12:31:10.289]  cpu      use argon2 implementation AVX-512F
[2025-08-09 12:31:10.290]  msr      register values for "ryzen_1Ah_zen5" preset have been set successfully (1 ms)
[2025-08-09 12:31:10.290]  randomx  init dataset algo rx/0 (32 threads) seed 0000000000000000...
[2025-08-09 12:31:10.411]  randomx  allocated 2336 MB (2080+256) huge pages 100% 1168/1168 +JIT (121 ms)
[2025-08-09 12:31:11.120]  randomx  dataset ready (709 ms)
[2025-08-09 12:31:11.120]  cpu      use profile  rx  (32 threads) scratchpad 2048 KB
[2025-08-09 12:31:11.140]  cpu      READY threads 32/32 (32) huge pages 100% 32/32 memory 65536 KB (20 ms)
[2025-08-09 12:32:11.164]  miner    speed 10s/60s/15m 19489.5 n/a n/a H/s max 19638.9 H/s
[2025-08-09 12:32:11.164]  bench    116.42% 1164175/1000000 (60.043s)
[2025-08-09 12:33:11.221]  miner    speed 10s/60s/15m 19573.1 19473.2 n/a H/s max 19638.9 H/s
[2025-08-09 12:33:11.221]  bench    233.37% 2333651/1000000 (120.101s)
```

# Discussion History
## SChernykh | 2025-08-09T13:11:28+00:00
If you run a benchmark without submitting it (offline), do you get the same issue?

## dan1338 | 2025-08-12T04:20:09+00:00
I've ran it a couple of times without the submit flag and it seems to have completed each time

## jekv2 | 2025-08-24T17:48:34+00:00
Same here.

<img width="1214" height="718" alt="Image" src="https://github.com/user-attachments/assets/e5d891a0-0c82-46eb-9f18-6d3a042305f9" />

## sibblegp | 2025-09-30T15:13:38+00:00
I have this bug too. What gives?

## jerrypas | 2025-10-01T01:46:48+00:00
I had the same issue, in my case it appears to be caused by IPv6 address returned by the resolver and my system/network doesn't support IPv6.
By running it via strace I noticed the "network unreachable" errors when it was trying to connect to an IPv6 address (AAAA record for api.xmrig.com), I ran it a few times more and on one of the attempts it tried to connect to IPv4 address and stopped and submitted successfully after the requested number of hashes were generated.

Running it with -4 to force IPv4 seems to be a simple workaround that works reliably for me.
It seems there is no error handling for connection errors in [xmrig::fetch](https://github.com/xmrig/xmrig/blob/6e4a5a6d94b33d6ed93890126c699b62f9553f50/src/base/net/http/Fetch.cpp#L97) or exceptions thrown in the underlying code hence failure to connect to the server goes unnoticed and causes the benchmark to run forever.

# Action History
- Created by: dan1338 | 2025-08-09T10:35:18+00:00
