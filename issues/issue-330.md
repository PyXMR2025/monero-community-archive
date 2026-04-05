---
title: xmrig Configuration optimization
source_url: https://github.com/xmrig/xmrig/issues/330
author: johnydo
assignees: []
labels: []
created_at: '2018-01-10T21:38:08+00:00'
updated_at: '2018-01-14T11:03:12+00:00'
type: issue
status: closed
closed_at: '2018-01-14T11:03:12+00:00'
---

# Original Description
Hello everybody,

I use the newest xmrig on my Ubuntu 16.04 system. In this system I use two Intel Xeon E5645 CPUs (6 Cores and 12MB L3 Cache per CPU).

**My config.json:**
`

- "algo": "cryptonight",
- "av": 0,
- "background": false,
- "colors": true,
- "cpu-affinity": null,
- "cpu-priority": null,
- "donate-level": 1,
- "log-file": null,
- "max-cpu-usage": 75,
- "print-time": 60,
- "retries": 5,
- "retry-pause": 5,
- "safe": false,
- "syslog": false,
- "threads": 12,

`

**Xmrig start:**
**./xmrig -c config.json**
`
 * VERSIONS:     XMRig/2.4.4 libuv/1.8.0 gcc/7.1.0
 * HUGE PAGES:   available, enabled
 * CPU:          Intel(R) Xeon(R) CPU E5645  @ 2.40GHz (2) x64 AES-NI
 * CPU L2/L3:    6.0 MB/24.0 MB
 * THREADS:      12, cryptonight, av=1, donate=1%
`

My average is 380 H/s. Is this a good value or can I improve it a bit more?

# Discussion History
## podwhitehawk | 2018-01-13T13:35:10+00:00
hi,

you could try to set `"cpu-affinity": "0xFFF"` to improve your hashrate a bit.

## johnydo | 2018-01-14T10:55:18+00:00
Hi,

thank you! I get 10 H/s more. Perfect!

# Action History
- Created by: johnydo | 2018-01-10T21:38:08+00:00
- Closed at: 2018-01-14T11:03:12+00:00
