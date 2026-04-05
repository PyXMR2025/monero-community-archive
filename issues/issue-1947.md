---
title: Lower GPU hashrate than other fork 1132 vs 1657 hashes on Vega FE
source_url: https://github.com/xmrig/xmrig/issues/1947
author: minzak
assignees: []
labels:
- question
created_at: '2020-11-14T21:33:42+00:00'
updated_at: '2021-04-12T14:34:44+00:00'
type: issue
status: closed
closed_at: '2021-04-12T14:34:44+00:00'
---

# Original Description
Debian buster + amdgpu-5.6.5.24-1109583
Driver version:  3143.9 (PAL,HSAIL)

I have the latest xmrig and fork https://github.com/MoneroOcean/xmrig/
And xmrig got 1132 hashes vs 1657 in MoneroOcean with the same config.

How it can be? what is wrong with xmrig?
Possible to do with xmrig to get the same result?
Thanks.


```
|  # | GPU |  BUS ID | INTENSITY | WSIZE | MEMORY | NAME
|  0 |   0 | 43:00.0 |      1984 |     8 |   3968 | Radeon Vega Frontier Edition (gfx900)
|  1 |   0 | 43:00.0 |      1984 |     8 |   3968 | Radeon Vega Frontier Edition (gfx900)
```

```
| OPENCL # | AFFINITY | 10s  H/s | 60s  H/s | 15m  H/s |
|        0 |       -1 |    564.7 |      n/a |      n/a | #0 43:00.0 Radeon Vega Frontier Edition (gfx900)
|        1 |       -1 |    563.8 |      n/a |      n/a | #0 43:00.0 Radeon Vega Frontier Edition (gfx900)
|        - |        - |   1132.2 |      n/a |      n/a |
```
with GPU data:
```
# ./amdcovc
Adapter 0: PCI 67:0:0: Vega 10 XTX [Radeon Vega Frontier Edition]
  Core: 1528 MHz, Mem: 945 MHz, CoreOD: 0, MemOD: 0, Vddc: 1125 mV
  SOC: 1107 MHz, DCEF: 600 MHz
  PerfCtrl: auto, Load: 100%
  Temp: 59°C, T2: 74°C, T3: 64°C, Fan: 62.7451%
  Power: 219 W (cap: 220 W)
  Core Clocks: 852 991 1138 1269 1348 1440 1528 1600
  Memory Clocks: 167 500 800 945
  SOC Clocks: 600 720 847 960 1028 1107
  DCEF Clocks: 600 720 800 900
```
And MoneroOcean results:
```
| OPENCL # | AFFINITY | 10s  H/s | 60s  H/s | 15m  H/s |
|        0 |       -1 |    810.5 |      n/a |      n/a | #0 43:00.0 Radeon Vega Frontier Edition (gfx900)
|        1 |       -1 |    858.5 |      n/a |      n/a | #0 43:00.0 Radeon Vega Frontier Edition (gfx900)
|        - |        - |   1657.8 |      n/a |      n/a |
```
with GPU data:
```
# ./amdcovc
Adapter 0: PCI 67:0:0: Vega 10 XTX [Radeon Vega Frontier Edition]
  Core: 1440 MHz, Mem: 945 MHz, CoreOD: 0, MemOD: 0, Vddc: 1031 mV
  SOC: 1107 MHz, DCEF: 600 MHz
  PerfCtrl: auto, Load: 100%
  Temp: 63°C, T2: 77°C, T3: 74°C, Fan: 63.9216%
  Power: 221 W (cap: 220 W)
  Core Clocks: 852 991 1138 1269 1348 1440 1528 1600
  Memory Clocks: 167 500 800 945
  SOC Clocks: 600 720 847 960 1028 1107
  DCEF Clocks: 600 720 800 900
```

P.S. But MoneroOcean can't normal mining on XEON v2 CPU 930 vs 8k


# Discussion History
## xmrig | 2020-11-14T21:47:57+00:00
MoneroOcean use algorithm switching feature, likely it just different algorithms. Hint: the miner also print algorithm in log.
Thank you.

## Spudz76 | 2020-12-04T09:46:23+00:00
Also if you are on MoneroOcean, compile two miners and run CPU separate from GPU as the most profitable algo per device type will be different.  Such as CPU rips up RandomX family algos, while the GPU will mainly be wasting its time on RandomX.

# Action History
- Created by: minzak | 2020-11-14T21:33:42+00:00
- Closed at: 2021-04-12T14:34:44+00:00
