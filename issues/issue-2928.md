---
title: Rejected benchmark
source_url: https://github.com/xmrig/xmrig/issues/2928
author: PSLLSP
assignees: []
labels: []
created_at: '2022-02-08T05:26:12+00:00'
updated_at: '2022-02-08T08:14:02+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
xmrig-6.16.4-linux-static-x64.tar.gz
Ubuntu 21.04

I cannot benchmark AMD FX-8300, benchmark is rejected. https://xmrig.com/benchmark/6Ut9TX
https://xmrig.com/benchmark/6evkE9

Benchmark was created with `$ sudo ./xmrig --bench=1M --submit -a rx/wow` and `$ sudo ./xmrig --bench=1M --submit -a rx/0`

Verify prints **red** hash sum:
```
$ sudo ./xmrig --verify=6Ut9TX
...
[2022-02-08 05:00:38.168]  miner    speed 10s/60s/15m 1377.8 2001.7 n/a H/s max 2291.7 H/s
[2022-02-08 05:00:38.168]  bench    89.27% 892654/1000000 (420.312s)
[2022-02-08 05:01:27.508]  bench    benchmark finished in 469.652 seconds (2129.2 h/s) hash sum = A4595970C02D4E8B
[2022-02-08 05:01:27.508]  bench    press Ctrl+C to exit
```

8CA25974E83F8089 is in **red**:
```
$ sudo ./xmrig --verify=6evkE9
...
[2022-02-08 05:33:28.789]  miner    speed 10s/60s/15m 2018.1 1771.0 n/a H/s max 2024.9 H/s
[2022-02-08 05:33:28.789]  bench    90.16% 901585/1000000 (480.466s)
[2022-02-08 05:34:24.393]  bench    benchmark finished in 536.070 seconds (1865.4 h/s) hash sum = 8CA25974E83F8089
```

I tried to run such benchmark on other CPUs and those are accepted, only FX-8300 is rejected again and again... I assume this is a problem in a xmrig code...

rx/wow benchmark run 3 times, hash is always unique...
https://xmrig.com/benchmark/6Ut9TX
https://xmrig.com/benchmark/Kf1i3
https://xmrig.com/benchmark/39hF2E

This is interesting, verify was run 3 times with 3 different results (all in **red**)! It looks like a random number generator is used by code... ;-) Maybe, it is some HW issue but I have no idea how this is possible... The correct hash is 34437EAB7666CE8F, that is what I get two times when I run the same test on INTEL XEON CPU. This is FX-8300, random number generator:

```
$ sudo ./xmrig --verify=Kf1i3
...
[2022-02-08 05:50:41.305]  miner    speed 10s/60s/15m 2066.7 2102.2 n/a H/s max 2290.7 H/s
[2022-02-08 05:50:41.305]  bench    91.64% 916429/1000000 (420.266s)
[2022-02-08 05:51:23.206]  bench    benchmark finished in 462.167 seconds (2163.7 h/s) hash sum = FE22E0972658D42E

$ sudo ./xmrig --verify=Kf1i3
...
[2022-02-08 06:07:19.086]  miner    speed 10s/60s/15m 2285.4 2125.9 n/a H/s max 2291.0 H/s
[2022-02-08 06:07:19.086]  bench    91.71% 917066/1000000 (420.348s)
[2022-02-08 06:08:01.754]  bench    benchmark finished in 463.016 seconds (2159.8 h/s) hash sum = FE9C89A6DA55D7B5

$ sudo ./xmrig --verify=Kf1i3
...
[2022-02-08 06:23:10.669]  miner    speed 10s/60s/15m 2289.7 2049.0 n/a H/s max 2292.2 H/s
[2022-02-08 06:23:10.669]  bench    91.64% 916399/1000000 (420.266s)
[2022-02-08 06:23:53.677]  bench    benchmark finished in 463.273 seconds (2158.6 h/s) hash sum = 88CC3DD11E2C7AA7
```

```
$ head -19 /proc/cpuinfo 
processor	: 0
vendor_id	: AuthenticAMD
cpu family	: 21
model		: 2
model name	: AMD FX(tm)-8300 Eight-Core Processor
stepping	: 0
microcode	: 0x6000852
cpu MHz		: 1400.000
cache size	: 2048 KB
physical id	: 0
siblings	: 8
core id		: 0
cpu cores	: 4
apicid		: 16
initial apicid	: 0
fpu		: yes
fpu_exception	: yes
cpuid level	: 13
wp		: yes
```

**CPU is not overclocked, PC runs stable for days. Without this benchmark I would have no idea that something is not working as expected...**

# Discussion History
# Action History
- Created by: PSLLSP | 2022-02-08T05:26:12+00:00
