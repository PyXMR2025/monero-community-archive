---
title: ARMv9 CIX CD8160/CD8180 CPU topology & identification information
source_url: https://github.com/xmrig/xmrig/issues/3788
author: craighammonds-sys
assignees: []
labels: []
created_at: '2026-03-02T05:16:25+00:00'
updated_at: '2026-07-07T20:00:11+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Hi,

I’m sharing hardware identification and topology information for a CIX ARMv9 SoC
(CD8160 / CD8180) used in the Orange Pi 6 Plus.

XMRig currently identifies this CPU generically, which is understandable given that
this chipset appears to be new and not widely documented upstream.

The information below is provided to help with correct CPU identification and
topology awareness on ARMv9 CIX platforms. No performance changes are being requested.
# CIX CD8160 / CD8180 ARMv9 SoC — Hardware Evidence for XMRig

## Board
- Orange Pi 6 Plus

## SoC
- Vendor: CIX
- Model: CIX P1 CD8160 (also marketed as CD8180 variant)
- Architecture: ARMv9-A
- NUMA nodes: 1

## CPU Topology

Heterogeneous ARMv9 configuration:

- 8 × Cortex-A720
  - CPU implementer: 0x41 (ARM)
  - CPU part: 0xD81
  - Max frequency: 2600 MHz

- 4 × Cortex-A520
  - CPU implementer: 0x41 (ARM)
  - CPU part: 0xD80
  - Max frequency: 1800 MHz

Total cores: 12  
Threads per core: 1

## Features
- AES
- PMULL
- SHA1 / SHA2 / SHA3
- SVE
- SVE2
- SVE AES / PMULL
- bf16 / i8mm

## devfreq (chipset fabric)
The following devfreq domains are exposed by the kernel:

- /sys/class/devfreq/CIXH3010:00
- /sys/class/devfreq/CIXH4000:00
- /sys/class/devfreq/CIXH5000:00

Observed default governors include `simple_ondemand` and `userspace`.
For RandomX workloads, stability improves when set to `performance`.

## Observed XMRig behaviour
- Auto-detection initially clamps RandomX threads conservatively
- Manual configuration with 12 threads is stable
- No NUMA splitting required
- No CPU affinity required

## Notes
- XMRig currently identifies the CPU generically (e.g. Cortex-A720)
- Cache sizes are not exposed to hwloc on this platform
- This document is provided to aid correct CPU identification and topology handling

# Discussion History
## SChernykh | 2026-03-02T09:47:52+00:00
Can you run `./xmrig --export-topology` on that device and attach the generated file?

## craighammonds-sys | 2026-03-03T02:10:04+00:00
[topology.xml](https://github.com/user-attachments/files/25699768/topology.xml)
Thankyou Here is the exported topology.xml from the device.

## coffnix | 2026-06-16T04:02:35+00:00
My maximum hashrate dropped after upgrading to XMRig 6.26.0 on this board, look: https://xmrig.com/benchmark/76FjCT

6.25.0  = 1887.26 H/s
6.26.0 = 1786.1 H/s



## coffnix | 2026-07-06T08:33:51+00:00
After upgrading to kernel 7.0.14 and booting with ACPI instead of DTB, the RandomX hashrate increased to about 2.1 KH/s.

```
opi6plus ~ # cat /var/log/xmr.log|grep -Ev 'accept|job'
 * ABOUT        XMRig/6.26.1-dev gcc/14.3.0 (built for Linux ARMv8, 64 bit)
 * LIBS         libuv/1.52.1 OpenSSL/3.0.21 hwloc/2.14.0
 * HUGE PAGES   supported
 * 1GB PAGES    supported
 * CPU          ARM Cortex-A720 (1) 64-bit AES
                L2:0.0 MB L3:0.0 MB 12C/12T NUMA:1
 * MEMORY       6.7/31.1 GB (22%)
                Top - on board: 8 GB LPDDR5 @ 6400 MHz Top - on board
                Top - on board: 8 GB LPDDR5 @ 6400 MHz Top - on board
                Top - on board: 8 GB LPDDR5 @ 6400 MHz Top - on board
                Top - on board: 8 GB LPDDR5 @ 6400 MHz Top - on board
 * MOTHERBOARD  Cix Technology Group Co., Ltd. - CIX Phecda Board
 * DONATE       0%
 * POOL #1      192.168.200.145:4444 algo rx/0
 * COMMANDS     'h' hashrate, 'p' pause, 'r' resume, 's' results, 'c' connection
[2026-07-06 04:42:19.372]  net      use pool 192.168.200.145:4444  192.168.200.145
[2026-07-06 04:42:19.372]  cpu      use argon2 implementation default
[2026-07-06 04:42:19.372]  randomx  init dataset algo rx/0 (12 threads) seed 674b1510bffd8b3a...
[2026-07-06 04:42:19.532]  randomx  allocated 3072 MB (2080+256) huge pages 100% 3/3 +JIT (160 ms)
[2026-07-06 04:42:29.753]  randomx  dataset ready (10221 ms)
[2026-07-06 04:42:29.753]  cpu      use profile  *  (12 threads) scratchpad 2048 KB
[2026-07-06 04:42:29.760]  cpu      READY threads 12/12 (12) huge pages 100% 12/12 memory 24576 KB (7 ms)
[2026-07-06 04:43:29.905]  miner    speed 10s/60s/15m 2107.9 n/a n/a H/s max 2109.5 H/s
[2026-07-06 04:44:29.960]  miner    speed 10s/60s/15m 2108.1 2101.3 n/a H/s max 2111.8 H/s
[2026-07-06 04:45:30.012]  miner    speed 10s/60s/15m 2109.7 2105.9 n/a H/s max 2111.8 H/s
[2026-07-06 04:46:30.051]  miner    speed 10s/60s/15m 2099.0 2105.3 n/a H/s max 2112.4 H/s
[2026-07-06 04:47:30.082]  miner    speed 10s/60s/15m 2103.5 2105.2 n/a H/s max 2112.4 H/s
[2026-07-06 04:48:30.139]  miner    speed 10s/60s/15m 2056.0 2064.6 n/a H/s max 2112.4 H/s
[2026-07-06 04:49:30.312]  miner    speed 10s/60s/15m 2074.7 1991.8 n/a H/s max 2112.4 H/s
[2026-07-06 04:50:30.352]  miner    speed 10s/60s/15m 2110.6 2103.5 n/a H/s max 2112.4 H/s
[2026-07-06 04:51:30.395]  miner    speed 10s/60s/15m 2095.2 2100.9 n/a H/s max 2112.4 H/s
[2026-07-06 04:52:30.444]  miner    speed 10s/60s/15m 2100.1 2102.2 n/a H/s max 2112.4 H/s
[2026-07-06 04:53:30.496]  miner    speed 10s/60s/15m 2103.9 2107.0 n/a H/s max 2112.4 H/s
[2026-07-06 04:54:30.555]  miner    speed 10s/60s/15m 2102.4 2105.8 n/a H/s max 2112.4 H/s
[2026-07-06 04:55:30.627]  miner    speed 10s/60s/15m 2102.1 2105.1 n/a H/s max 2112.4 H/s
[2026-07-06 04:56:30.693]  miner    speed 10s/60s/15m 2106.2 2105.9 n/a H/s max 2112.4 H/s
[2026-07-06 04:57:30.743]  miner    speed 10s/60s/15m 2107.5 2108.4 2083.3 H/s max 2112.4 H/s
[2026-07-06 04:58:30.782]  miner    speed 10s/60s/15m 2108.2 2108.2 2094.8 H/s max 2112.4 H/s
[2026-07-06 04:59:30.813]  miner    speed 10s/60s/15m 2109.0 2108.2 2095.3 H/s max 2112.4 H/s
[2026-07-06 05:00:30.842]  miner    speed 10s/60s/15m 2106.9 2106.8 2095.3 H/s max 2112.4 H/s
[2026-07-06 05:01:30.874]  miner    speed 10s/60s/15m 2110.4 2106.6 2095.4 H/s max 2112.7 H/s
[2026-07-06 05:02:30.905]  miner    speed 10s/60s/15m 2107.9 2104.4 2095.4 H/s max 2112.7 H/s
[2026-07-06 05:03:30.930]  miner    speed 10s/60s/15m 2106.8 2101.6 2097.8 H/s max 2112.7 H/s
[2026-07-06 05:04:30.970]  miner    speed 10s/60s/15m 2104.7 2106.5 2105.4 H/s max 2112.7 H/s
[2026-07-06 05:05:31.015]  miner    speed 10s/60s/15m 2105.8 2106.4 2105.6 H/s max 2112.7 H/s
[2026-07-06 05:06:31.036]  miner    speed 10s/60s/15m 2106.3 2106.9 2106.0 H/s max 2112.7 H/s
[2026-07-06 05:07:31.069]  miner    speed 10s/60s/15m 2108.0 2108.7 2106.4 H/s max 2113.4 H/s
[2026-07-06 05:08:31.099]  miner    speed 10s/60s/15m 2101.2 2106.8 2106.4 H/s max 2113.4 H/s
[2026-07-06 05:09:31.126]  miner    speed 10s/60s/15m 2097.4 2105.2 2106.4 H/s max 2113.4 H/s
[2026-07-06 05:10:31.251]  miner    speed 10s/60s/15m 1531.3 1962.6 2096.9 H/s max 2113.4 H/s
[2026-07-06 05:11:31.280]  miner    speed 10s/60s/15m 2100.9 2064.2 2094.0 H/s max 2113.4 H/s
[2026-07-06 05:12:31.313]  miner    speed 10s/60s/15m 2102.6 2104.4 2093.8 H/s max 2113.4 H/s
[2026-07-06 05:13:31.355]  miner    speed 10s/60s/15m 2100.6 2103.2 2093.4 H/s max 2113.4 H/s
[2026-07-06 05:14:31.395]  miner    speed 10s/60s/15m 2104.2 2103.0 2093.1 H/s max 2113.4 H/s
[2026-07-06 05:15:31.432]  miner    speed 10s/60s/15m 2109.1 2107.2 2093.1 H/s max 2113.4 H/s
[2026-07-06 05:16:31.473]  miner    speed 10s/60s/15m 2101.1 2106.6 2093.1 H/s max 2113.4 H/s
[2026-07-06 05:17:31.521]  miner    speed 10s/60s/15m 2105.8 2106.2 2093.2 H/s max 2113.4 H/s
[2026-07-06 05:18:31.568]  miner    speed 10s/60s/15m 2110.9 2107.7 2093.6 H/s max 2113.4 H/s
[2026-07-06 05:19:31.615]  miner    speed 10s/60s/15m 2109.3 2107.7 2093.7 H/s max 2113.4 H/s
[2026-07-06 05:20:31.661]  miner    speed 10s/60s/15m 2106.3 2107.2 2093.8 H/s max 2113.4 H/s
[2026-07-06 05:21:31.708]  miner    speed 10s/60s/15m 2104.2 2105.8 2093.7 H/s max 2113.4 H/s
[2026-07-06 05:22:31.764]  miner    speed 10s/60s/15m 2107.1 2108.8 2093.7 H/s max 2113.4 H/s
[2026-07-06 05:23:31.825]  miner    speed 10s/60s/15m 2104.4 2107.9 2093.8 H/s max 2113.4 H/s
[2026-07-06 05:24:31.869]  miner    speed 10s/60s/15m 2106.2 2103.2 2093.7 H/s max 2113.4 H/s
[2026-07-06 05:25:31.898]  miner    speed 10s/60s/15m 2105.3 2106.9 2103.5 H/s max 2113.4 H/s
[2026-07-06 05:26:31.926]  miner    speed 10s/60s/15m 2105.0 2105.6 2106.1 H/s max 2113.4 H/s
[2026-07-06 05:27:31.965]  miner    speed 10s/60s/15m 2104.8 2108.0 2106.3 H/s max 2113.4 H/s
[2026-07-06 05:28:31.997]  miner    speed 10s/60s/15m 2103.8 2106.2 2106.5 H/s max 2113.4 H/s
[2026-07-06 05:29:32.044]  miner    speed 10s/60s/15m 2110.6 2109.9 2107.0 H/s max 2113.4 H/s
[2026-07-06 05:30:32.068]  miner    speed 10s/60s/15m 2108.8 2108.5 2107.1 H/s max 2113.4 H/s
[2026-07-06 05:31:32.090]  miner    speed 10s/60s/15m 2110.2 2108.3 2107.2 H/s max 2113.4 H/s
[2026-07-06 05:32:32.108]  miner    speed 10s/60s/15m 2109.2 2105.8 2107.2 H/s max 2113.4 H/s
[2026-07-06 05:33:32.136]  miner    speed 10s/60s/15m 2101.5 2104.9 2107.0 H/s max 2113.4 H/s
```

randomx v1: https://xmrig.com/benchmark/2s4qe3

randomx v2: https://xmrig.com/benchmark/6gZZZe

## SChernykh | 2026-07-07T07:57:42+00:00
> After upgrading to kernel 7.0.14 and booting with ACPI instead of DTB, the RandomX hashrate increased to about 2.1 KH/s.

What about 6.25.0 with the same kernel version and settings?

## coffnix | 2026-07-07T18:16:19+00:00
> > After upgrading to kernel 7.0.14 and booting with ACPI instead of DTB, the RandomX hashrate increased to about 2.1 KH/s.
> 
> What about 6.25.0 with the same kernel version and settings?

yo @SChernykh the problem is that with DTB boot, the CPU frequencies stay below normal. When using ACPI boot, the core frequencies are correct, even though the L2 and L3 caches are not detected. I have already reported this bug here: https://github.com/cixtech/cix-linux-main/issues/43

With version 6.25.0, it stayed around the same average, between 1790 and 2015 H/s, and it keeps fluctuating, always staying below 1.9 KH/s. Look:

```
 * ABOUT        XMRig/6.25.0 gcc/14.3.0 (built for Linux ARMv8, 64 bit)
 * LIBS         libuv/1.52.1 OpenSSL/3.0.21 hwloc/2.14.0
 * HUGE PAGES   supported
 * 1GB PAGES    supported
 * CPU          ARM Cortex-A720 (1) 64-bit AES
                L2:0.0 MB L3:0.0 MB 12C/12T NUMA:1
 * MEMORY       11.1/31.1 GB (36%)
                Top - on board: 8 GB LPDDR5 @ 6400 MHz Top - on board
                Top - on board: 8 GB LPDDR5 @ 6400 MHz Top - on board
                Top - on board: 8 GB LPDDR5 @ 6400 MHz Top - on board
                Top - on board: 8 GB LPDDR5 @ 6400 MHz Top - on board
 * MOTHERBOARD  Cix Technology Group Co., Ltd. - CIX Phecda Board
 * DONATE       0%
 * POOL #1      192.168.200.145:4444 algo rx/0
 * COMMANDS     'h' hashrate, 'p' pause, 'r' resume, 's' results, 'c' connection
[2026-07-07 15:04:50.940]  net      use pool 192.168.200.145:4444  192.168.200.145
[2026-07-07 15:04:50.940]  cpu      use argon2 implementation default
[2026-07-07 15:04:50.940]  randomx  init dataset algo rx/0 (12 threads) seed 674b1510bffd8b3a...
[2026-07-07 15:04:51.019]  randomx  allocated 3072 MB (2080+256) huge pages 100% 3/3 +JIT (79 ms)
[2026-07-07 15:04:58.624]  randomx  dataset ready (7605 ms)
[2026-07-07 15:04:58.625]  cpu      use profile  *  (12 threads) scratchpad 2048 KB
[2026-07-07 15:04:58.631]  cpu      READY threads 12/12 (12) huge pages 100% 12/12 memory 24576 KB (6 ms)
[2026-07-07 15:05:58.673]  miner    speed 10s/60s/15m 1970.1 n/a n/a H/s max 2015.3 H/s
[2026-07-07 15:06:58.716]  miner    speed 10s/60s/15m 1971.9 1986.4 n/a H/s max 2015.3 H/s
[2026-07-07 15:07:58.757]  miner    speed 10s/60s/15m 1982.2 1990.7 n/a H/s max 2015.3 H/s
[2026-07-07 15:08:58.826]  miner    speed 10s/60s/15m 1834.0 1932.9 n/a H/s max 2015.3 H/s
[2026-07-07 15:09:59.182]  miner    speed 10s/60s/15m 1790.8 1239.5 n/a H/s max 2015.3 H/s
```

With the dev branch version 6.26.1, commit 6dc014f, it already starts at 2.1 KH/s. Look:

```
 * ABOUT        XMRig/6.26.1-dev gcc/14.3.0 (built for Linux ARMv8, 64 bit)
 * LIBS         libuv/1.52.1 OpenSSL/3.0.21 hwloc/2.14.0
 * HUGE PAGES   supported
 * 1GB PAGES    supported
 * CPU          ARM Cortex-A720 (1) 64-bit AES
                L2:0.0 MB L3:0.0 MB 12C/12T NUMA:1
 * MEMORY       11.1/31.1 GB (36%)
                Top - on board: 8 GB LPDDR5 @ 6400 MHz Top - on board
                Top - on board: 8 GB LPDDR5 @ 6400 MHz Top - on board
                Top - on board: 8 GB LPDDR5 @ 6400 MHz Top - on board
                Top - on board: 8 GB LPDDR5 @ 6400 MHz Top - on board
 * MOTHERBOARD  Cix Technology Group Co., Ltd. - CIX Phecda Board
 * DONATE       0%
 * POOL #1      192.168.200.145:4444 algo rx/0
 * COMMANDS     'h' hashrate, 'p' pause, 'r' resume, 's' results, 'c' connection
[2026-07-07 15:10:22.070]  net      use pool 192.168.200.145:4444  192.168.200.145
[2026-07-07 15:10:22.070]  cpu      use argon2 implementation default
[2026-07-07 15:10:22.071]  randomx  init dataset algo rx/0 (12 threads) seed 674b1510bffd8b3a...
[2026-07-07 15:10:22.143]  randomx  allocated 3072 MB (2080+256) huge pages 100% 3/3 +JIT (73 ms)
[2026-07-07 15:10:29.492]  randomx  dataset ready (7348 ms)
[2026-07-07 15:10:29.492]  cpu      use profile  *  (12 threads) scratchpad 2048 KB
[2026-07-07 15:10:29.498]  cpu      READY threads 12/12 (12) huge pages 100% 12/12 memory 24576 KB (6 ms)
[2026-07-07 15:11:29.551]  miner    speed 10s/60s/15m 2039.4 n/a n/a H/s max 2095.5 H/s
[2026-07-07 15:12:29.594]  miner    speed 10s/60s/15m 2032.7 2040.4 n/a H/s max 2095.5 H/s
[2026-07-07 15:13:29.625]  miner    speed 10s/60s/15m 2026.0 2039.9 n/a H/s max 2095.5 H/s
[2026-07-07 15:14:29.665]  miner    speed 10s/60s/15m 2025.5 2037.9 n/a H/s max 2095.5 H/s
[2026-07-07 15:15:29.702]  miner    speed 10s/60s/15m 2028.9 2036.3 n/a H/s max 2095.5 H/s
[2026-07-07 15:16:29.749]  miner    speed 10s/60s/15m 2034.2 2037.9 n/a H/s max 2095.5 H/s
[2026-07-07 15:17:29.777]  miner    speed 10s/60s/15m 2041.4 2039.0 n/a H/s max 2095.5 H/s
[2026-07-07 15:18:29.825]  miner    speed 10s/60s/15m 2038.3 2038.1 n/a H/s max 2095.5 H/s
[2026-07-07 15:19:29.861]  miner    speed 10s/60s/15m 2042.8 2041.0 n/a H/s max 2095.5 H/s
[2026-07-07 15:20:29.901]  miner    speed 10s/60s/15m 2043.8 2040.6 n/a H/s max 2095.5 H/s
```

On this machine, I run P2Pool, HAProxy, and Monerod alongside XMRig, and the total RAM usage of all the services is about 10 GB. I believe that if the machine were dedicated exclusively to XMRig, the hashrate would be even higher.

We achieved real gains with version 6.26.0 from the development branch. Thank you for the ARM64 optimizations.

The question is, do you think we can optimize it even further for ARMv9.2-A? I have two devices at home using this architecture, a Mac mini M4 and this Orange Pi 6 Plus.

## coffnix | 2026-07-07T19:59:32+00:00
I achieved better performance by forcing cpufreq.default_governor=performance at boot and running this script during startup:

```
opi6plus ~ # cat /etc/local.d/set-performance.start
#!/bin/sh
for p in /sys/devices/system/cpu/cpufreq/policy*; do
    min=$(cat "$p/cpuinfo_min_freq")
    max=$(cat "$p/cpuinfo_max_freq")
    echo "$min" > "$p/scaling_min_freq"
    echo "$max" > "$p/scaling_max_freq"
    echo performance > "$p/scaling_governor"
done

for p in /sys/devices/system/cpu/cpufreq/policy*; do
    max=$(cat "$p/scaling_max_freq")
    echo "$max" > "$p/scaling_min_freq"
done
```

Look:

```
watch -n1 '
echo "CPU:";
grep . /sys/devices/system/cpu/cpu*/cpufreq/scaling_cur_freq;
echo;
echo "TEMP:";
for z in /sys/class/thermal/thermal_zone*; do
    printf "%s " "$(cat $z/type)";
    awk "{printf \"%.1f°C\n\", \$1/1000}" $z/temp;
done ; echo -e "\nXMRIG:"; grep speed /var/log/xmr.log|tail -5'
```

results:
```
CPU:
/sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq:2600000
/sys/devices/system/cpu/cpu10/cpufreq/scaling_cur_freq:2500000
/sys/devices/system/cpu/cpu11/cpufreq/scaling_cur_freq:2500000
/sys/devices/system/cpu/cpu1/cpufreq/scaling_cur_freq:2600000
/sys/devices/system/cpu/cpu2/cpufreq/scaling_cur_freq:1800000
/sys/devices/system/cpu/cpu3/cpufreq/scaling_cur_freq:1800000
/sys/devices/system/cpu/cpu4/cpufreq/scaling_cur_freq:1800000
/sys/devices/system/cpu/cpu5/cpufreq/scaling_cur_freq:1800000
/sys/devices/system/cpu/cpu6/cpufreq/scaling_cur_freq:2300000
/sys/devices/system/cpu/cpu7/cpufreq/scaling_cur_freq:2300000
/sys/devices/system/cpu/cpu8/cpufreq/scaling_cur_freq:2200000
/sys/devices/system/cpu/cpu9/cpufreq/scaling_cur_freq:2200000

TEMP:
TZB0 60.0°C
TZB1 61.0°C
TZM0 60.0°C
TZM1 56.0°C
TZGT 49.0°C

XMRIG:
[2026-07-07 16:57:06.103]  miner    speed 10s/60s/15m 2096.5 n/a n/a H/s max 2102.5 H/s
[2026-07-07 16:58:06.136]  miner    speed 10s/60s/15m 2050.2 2051.1 n/a H/s max 2102.5 H/s
[2026-07-07 16:59:06.184]  miner    speed 10s/60s/15m 2045.3 2042.8 n/a H/s max 2102.5 H/s

```

# Action History
- Created by: craighammonds-sys | 2026-03-02T05:16:25+00:00
