---
title: In xmrig latest it shows n/a h/s in GPU mining (openCL)
source_url: https://github.com/xmrig/xmrig/issues/1821
author: linay123
assignees: []
labels: []
created_at: '2020-09-01T02:57:05+00:00'
updated_at: '2021-04-12T14:50:05+00:00'
type: issue
status: closed
closed_at: '2021-04-12T14:50:05+00:00'
---

# Original Description
![IMG20200831091429](https://user-images.githubusercontent.com/65266764/91789679-c2d9ef00-ec2c-11ea-97b8-b18385ead1c9.jpg)
There is no speed for openCL but my cpu is working nicely with the xmrig

# Discussion History
## SChernykh | 2020-09-01T08:56:20+00:00
Did previous versions work with this GPU? Radeon R5 M3XX are very old GPUs and they don't have enough memory for RandomX dataset plus they have to run RandomX in VM emulation mode, so I don't expect more than 10 h/s, even if it works.

## linay123 | 2020-09-01T16:19:53+00:00
How I can run those this GPU in vm emulation mode

## SChernykh | 2020-09-01T16:22:25+00:00
xmrig is probably already running them there, but hashrate is so low that it can't be calculated, so you get `n/a`.

## Lonnegan | 2020-09-03T09:05:13+00:00
You shouldn't use the GPU to mine Monero. Random-X algo is a CPU only algo. GPU is possible, but slow. I'd deactivate OpenCL in the config for the Monero mining xmrig and use a second xmrig folder where CPU mining is deactivated and OpenCL enable. There you can mine something useful for your GPU, e.g. Ravencoin, Haven or something like that.

## minzak | 2020-11-14T21:12:56+00:00
Also, have the same issues.
`[2020-11-14 23:06:16.992]  opencl   #0 43:00.0   0W  0C    0RPM 0/0MHz`

```
[2020-11-14 23:05:57.383]  cpu      accepted (5/0) diff 200007 (35 ms)
[2020-11-14 23:06:07.501]  opencl   accepted (6/0) diff 200007 (49 ms)
[2020-11-14 23:06:09.348]  opencl   accepted (7/0) diff 200007 (54 ms)
|    CPU # | AFFINITY | 10s H/s | 60s H/s | 15m H/s |
|        0 |        0 |   371.7 |   370.8 |     n/a |
|        1 |        1 |   372.0 |   371.2 |     n/a |
|        2 |        2 |   368.8 |   370.6 |     n/a |
|        3 |        3 |   371.7 |   369.8 |     n/a |
|        4 |        4 |   364.8 |   365.2 |     n/a |
|        5 |        5 |   371.8 |   370.7 |     n/a |
|        6 |        6 |   371.4 |   365.9 |     n/a |
|        7 |        7 |   368.2 |   365.2 |     n/a |
|        8 |        8 |   372.9 |   376.8 |     n/a |
|        9 |        9 |   371.1 |   376.4 |     n/a |
|       10 |       10 |   378.2 |   379.5 |     n/a |
|       11 |       11 |   382.2 |   381.3 |     n/a |
|       12 |       12 |   374.2 |   375.0 |     n/a |
|       13 |       13 |   375.0 |   375.5 |     n/a |
|       14 |       14 |   373.8 |   374.0 |     n/a |
|       15 |       15 |   372.1 |   373.1 |     n/a |
|       16 |       16 |   366.8 |   366.2 |     n/a |
|       17 |       17 |   370.6 |   370.5 |     n/a |
|       18 |       18 |   374.0 |   374.2 |     n/a |
|       19 |       19 |   375.3 |   375.6 |     n/a |
|       20 |       20 |   380.1 |   378.8 |     n/a |
|       21 |       21 |   379.1 |   378.8 |     n/a |
|       22 |       22 |   385.4 |   385.3 |     n/a |
|       23 |       23 |   381.7 |   378.7 |     n/a |
|        - |        - |  8972.8 |  8968.9 |     n/a |
| OPENCL # | AFFINITY | 10s  H/s | 60s  H/s | 15m  H/s |
|        0 |       -1 |    556.5 |    559.3 |      n/a | #0 43:00.0 Radeon Vega Frontier Edition (gfx900)
|        1 |       -1 |    557.6 |    559.5 |      n/a | #0 43:00.0 Radeon Vega Frontier Edition (gfx900)
|        - |        - |   1115.2 |   1119.2 |      n/a |
[2020-11-14 23:06:16.594]  miner    speed 10s/60s/15m 10088.0 10088.1 n/a H/s max 10117.5 H/s
[2020-11-14 23:06:16.992]  opencl   #0 43:00.0   0W  0C    0RPM 0/0MHz
[2020-11-14 23:06:16.993]  miner    speed 10s/60s/15m 10088.1 10087.4 n/a H/s max 10117.5 H/s
```

But in the system, I have several ways to see fan speed and temperature
For example `cat /sys/kernel/debug/dri/*/amdgpu_pm_info | grep -i Temperature | cat -n`

OR:

```
# ./amdcovc
Adapter 0: PCI 67:0:0: Vega 10 XTX [Radeon Vega Frontier Edition]
  Core: 852 MHz, Mem: 167 MHz, CoreOD: 0, MemOD: 0, Vddc: 750 mV
  SOC: 600 MHz, DCEF: 600 MHz
  PerfCtrl: auto, Load: 8%
  Temp: 34°C, T2: 35°C, T3: 34°C, Fan: 27.8431%
  Power: 4 W (cap: 220 W)
  Core Clocks: 852 991 1138 1269 1348 1440 1528 1600
  Memory Clocks: 167 500 800 945
  SOC Clocks: 600 720 847 960 1028 1107
  DCEF Clocks: 600 720 800 900

```

# Action History
- Created by: linay123 | 2020-09-01T02:57:05+00:00
- Closed at: 2021-04-12T14:50:05+00:00
