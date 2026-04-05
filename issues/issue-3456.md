---
title: xeon e5-2699v3 dual cpu low performance
source_url: https://github.com/xmrig/xmrig/issues/3456
author: nazarov-ae
assignees: []
labels: []
created_at: '2024-04-02T16:02:59+00:00'
updated_at: '2025-06-16T19:52:57+00:00'
type: issue
status: closed
closed_at: '2025-06-16T19:52:57+00:00'
---

# Original Description
Hi!

Hardware:
* motherboard: [HUANANZHI X99-F8D PLUS](http://www.huananzhi.com/en/more.php?lm=10&id=311)
* cpu: [xeon e5-2699v3](https://www.cpu-world.com/CPUs/Xeon/Intel-Xeon%20E5-2699%20v3.html) (2 pcs)
* DDR4 32GB 2133MHz (4 pcs) in dual channel mode
```bash
hwloc-ls  | grep NUMANode
    NUMANode L#0 (P#0 63GB)
    NUMANode L#1 (P#1 63GB)
```
Software:
* Ubuntu 22.04.3 LTS
* XMRig 6.21.0

I create config.json (only cpu section below)
```json
{
    "cpu": {
        "enabled": true,
        "huge-pages": true,
        "hw-aes": null,
        "priority": null,
        "memory-pool": false,
        "yield": false,
        "max-threads-hint": 100,
        "asm": true,
        "argon2-impl": null,
        "autosave": false,
        "argon2": [],
        "cn": [],
        "cn-heavy": [],
        "cn-lite": [],
        "cn-pico": [],
        "rx": [],
        "rx/wow": [],
        "cn/0": false,
        "cn-lite/0": false,
        "rx/arq": "rx/wow",
        "rx/keva": "rx/wow"
    }
}
```
and run ./xmrig on root.

config.json has automated changed to (only cpu section below):
```json
{
    "cpu": {
        "enabled": true,
        "huge-pages": true,
        "huge-pages-jit": false,
        "hw-aes": null,
        "priority": null,
        "memory-pool": false,
        "yield": true,
        "asm": true,
        "argon2-impl": null,
        "argon2": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35],
        "cn": [
            [1, 0],
            [1, 1],
            [1, 2],
            [1, 3],
            [1, 4],
            [1, 5],
            [1, 6],
            [1, 7],
            [1, 8],
            [1, 9],
            [1, 10],
            [1, 11],
            [1, 12],
            [1, 13],
            [1, 14],
            [1, 15],
            [1, 16],
            [1, 17],
            [1, 18],
            [1, 19],
            [1, 20],
            [1, 21],
            [1, 22],
            [1, 23],
            [1, 24],
            [1, 25],
            [1, 26],
            [1, 27],
            [1, 28],
            [1, 29],
            [1, 30],
            [1, 31],
            [1, 32],
            [1, 33],
            [1, 34],
            [1, 35]
        ],
        "cn-heavy": [
            [1, 0],
            [1, 1],
            [1, 2],
            [1, 3],
            [1, 4],
            [1, 5],
            [1, 6],
            [1, 7],
            [1, 8],
            [1, 9],
            [1, 10],
            [1, 18],
            [1, 19],
            [1, 20],
            [1, 21],
            [1, 22],
            [1, 23],
            [1, 24],
            [1, 25],
            [1, 26],
            [1, 27],
            [1, 28]
        ],
        "cn-lite": [
            [1, 0],
            [1, 1],
            [1, 2],
            [1, 3],
            [1, 4],
            [1, 5],
            [1, 6],
            [1, 7],
            [1, 8],
            [1, 9],
            [1, 10],
            [1, 11],
            [1, 12],
            [1, 13],
            [1, 14],
            [1, 15],
            [1, 16],
            [1, 17],
            [1, 18],
            [1, 19],
            [1, 20],
            [1, 21],
            [1, 22],
            [1, 23],
            [1, 24],
            [1, 25],
            [1, 26],
            [1, 27],
            [1, 28],
            [1, 29],
            [1, 30],
            [1, 31],
            [1, 32],
            [1, 33],
            [1, 34],
            [1, 35]
        ],
        "cn-pico": [
            [2, 0],
            [2, 1],
            [2, 2],
            [2, 3],
            [2, 4],
            [2, 5],
            [2, 6],
            [2, 7],
            [2, 8],
            [2, 9],
            [2, 10],
            [2, 11],
            [2, 12],
            [2, 13],
            [2, 14],
            [2, 15],
            [2, 16],
            [2, 17],
            [2, 18],
            [2, 19],
            [2, 20],
            [2, 21],
            [2, 22],
            [2, 23],
            [2, 24],
            [2, 25],
            [2, 26],
            [2, 27],
            [2, 28],
            [2, 29],
            [2, 30],
            [2, 31],
            [2, 32],
            [2, 33],
            [2, 34],
            [2, 35]
        ],
        "cn/upx2": [
            [2, 0],
            [2, 1],
            [2, 2],
            [2, 3],
            [2, 4],
            [2, 5],
            [2, 6],
            [2, 7],
            [2, 8],
            [2, 9],
            [2, 10],
            [2, 11],
            [2, 12],
            [2, 13],
            [2, 14],
            [2, 15],
            [2, 16],
            [2, 17],
            [2, 18],
            [2, 19],
            [2, 20],
            [2, 21],
            [2, 22],
            [2, 23],
            [2, 24],
            [2, 25],
            [2, 26],
            [2, 27],
            [2, 28],
            [2, 29],
            [2, 30],
            [2, 31],
            [2, 32],
            [2, 33],
            [2, 34],
            [2, 35]
        ],
        "ghostrider": [
            [8, 0],
            [8, 1],
            [8, 2],
            [8, 3],
            [8, 4],
            [8, 5],
            [8, 6],
            [8, 7],
            [8, 8],
            [8, 9],
            [8, 10],
            [8, 11],
            [8, 12],
            [8, 13],
            [8, 14],
            [8, 15],
            [8, 16],
            [8, 17],
            [8, 18],
            [8, 19],
            [8, 20],
            [8, 21],
            [8, 22],
            [8, 23],
            [8, 24],
            [8, 25],
            [8, 26],
            [8, 27],
            [8, 28],
            [8, 29],
            [8, 30],
            [8, 31],
            [8, 32],
            [8, 33],
            [8, 34],
            [8, 35]
        ],
        "rx": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35],
        "rx/wow": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35],
        "cn-lite/0": false,
        "cn/0": false,
        "rx/arq": "rx/wow",
        "rx/keva": "rx/wow"
    }
}
```

In first time performance is about 17kH/s
![image](https://github.com/xmrig/xmrig/assets/89434811/741eb403-af0c-4d72-90c4-3d0fa42cbb09)
But after 10 minutes it drop to about 8kH/s
![image](https://github.com/xmrig/xmrig/assets/89434811/a5d3b8ce-9e20-4757-8e56-8ae7aeaac4ac)

How can this problem be diagnosed?

# Discussion History
## headygains | 2024-04-04T02:09:32+00:00
After running it for 24hrs what are the stats? Has there been any change?

## nazarov-ae | 2024-04-04T02:40:31+00:00
Last 24 hours hashrate is between 8 and 11 kH/s.
According cpufreq-info frequency is 3.29 GHz and is 3.19 GHz for first and second CPU.
CPU temperature is
```bash
sensors | grep 'Package id'
Package id 0:  +63.0°C  (high = +68.0°C, crit = +86.0°C)
Package id 1:  +72.0°C  (high = +68.0°C, crit = +86.0°C)
```

## headygains | 2024-04-05T18:33:11+00:00
After looking into increased core count on Intel cpus causing reduced hashrates have you tried changing the used cores to find an optimal #?

## headygains | 2024-04-06T06:49:07+00:00
I'm testing a similar setup now and will report back but there does seem to be validity to some of the information about high core count and degraded performance. It's most likely related to l2 or l3 cache

## nazarov-ae | 2024-04-06T07:14:17+00:00
> After looking into increased core count on Intel cpus causing reduced hashrates have you tried changing the used cores to find an optimal #?

I'll try it.
For single cpu motherboard with same cpu E52699 v3 i have average 8 kH/s and it corresponds with [this benchmark](https://xmrig.com/benchmark/57m28u). But for dual motherboard [isn't](https://xmrig.com/benchmark/5h7Fsr).



# Action History
- Created by: nazarov-ae | 2024-04-02T16:02:59+00:00
- Closed at: 2025-06-16T19:52:57+00:00
