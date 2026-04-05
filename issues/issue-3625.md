---
title: --bench --threads=1 gives different hash sum
source_url: https://github.com/xmrig/xmrig/issues/3625
author: jfikar
assignees: []
labels: []
created_at: '2025-01-31T14:38:23+00:00'
updated_at: '2025-01-31T18:29:18+00:00'
type: issue
status: closed
closed_at: '2025-01-31T18:29:16+00:00'
---

# Original Description
I'm running xmrig in the benchmark mode with one or more threads. In the case of one thread the hash sum is always different, although it is still printed in green.

```
./xmrig --bench=1M --threads=1 -a rx/wow
...
[2025-01-31 15:24:27.570]  bench    benchmark finished in 1833.805 seconds (545.3 h/s) hash sum = 31301CC550306A59
```

```
./xmrig --bench=1M --threads=4 -a rx/wow
...
[2025-01-31 14:49:44.833]  bench    benchmark finished in 503.376 seconds (1986.6 h/s) hash sum = 0F3E5400B39EA96A
```

This is xmrig 6.22.2 on Linux. I've tried on several machines, so it is not a stability problem, including RPi5 (there you need to add `--randomx-no-numa` as they use NUMA now) and always the one-thread hash sum is different from more-thread one.  The same behavior is observed for  rx/0. Is this expected?

# Discussion History
## SChernykh | 2025-01-31T18:05:14+00:00
This is by design. Single-threaded tests calculates a different hash which is impossible to calculate in parallel (with multiple threads).

## jfikar | 2025-01-31T18:29:16+00:00
Oh, I see. Thanks

# Action History
- Created by: jfikar | 2025-01-31T14:38:23+00:00
- Closed at: 2025-01-31T18:29:16+00:00
