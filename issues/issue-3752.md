---
title: '"Bus error" crash on armv7l'
source_url: https://github.com/xmrig/xmrig/issues/3752
author: meanwhile131
assignees: []
labels: []
created_at: '2026-01-07T20:23:41+00:00'
updated_at: '2026-01-08T13:06:15+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
**Describe the bug**
XMRig crashes with a "Bus error" when doing anything on armv7l.

**To Reproduce**
Run
```./xmrig --bench=1M```
on armv7l.

**Expected behavior**
Not crashing when running a benchmark on armv7l.

**Info**
XMRig version: v6.25.0. Built and run in a Podman container (Alpine) with `--arch arm` (which uses QEMU) on Linux:
```
apk add git make cmake libstdc++ gcc g++ automake libtool autoconf linux-headers
git clone https://github.com/xmrig/xmrig.git
mkdir xmrig/build && cd xmrig/scripts
./build_deps.sh && cd ../build
cmake .. -DXMRIG_DEPS=scripts/deps -DBUILD_STATIC=ON
make -j$(nproc)
```
Miner log:
```
~/xmrig/build # ./xmrig --bench=1M
 * ABOUT        XMRig/6.25.0 gcc/15.2.0 (built for Linux ARMv7, 32 bit)
 * LIBS         libuv/1.51.0 OpenSSL/3.0.16 hwloc/2.12.1
 * HUGE PAGES   supported
 * 1GB PAGES    disabled
 * CPU          ARM Cortex-A57 (1) 32-bit -AES
                L2:6.0 MB L3:32.0 MB 6C/12T NUMA:1
 * MEMORY       12.4/30.5 GB (41%)
 * DONATE       0%
 * POOL #1      benchmark algo auto
 * COMMANDS     hashrate, pause, resume, results, connection
[2026-01-07 20:17:34.309]  bench    start benchmark hashes 1M algo rx/0
[2026-01-07 20:17:34.312]  cpu      use argon2 implementation default
[2026-01-07 20:17:35.523]  randomx  init dataset algo rx/0 (12 threads) seed 0000000000000000...
[2026-01-07 20:17:35.529]  randomx  failed to allocate RandomX dataset, switching to slow mode (6 ms)
qemu: uncaught target signal 7 (Bus error) - core dumped
Bus error (core dumped)
~/xmrig/build # 
```

# Discussion History
## SChernykh | 2026-01-08T11:19:01+00:00
There is no RandomX JIT for 32-bit ARM, so even if it doesn't crash, it will be less than 1 h/s on a real hardware, and probably 10 seconds per hash in QEMU. It is recommended to run 64-bit, as 32-bit is never tested when doing releases.

## meanwhile131 | 2026-01-08T12:28:39+00:00
The website has 2 benchmarks claiming to be on ARM Cortex-A57 with 54 and 188 h/s: https://xmrig.com/benchmark?cpu=ARM+Cortex-A57

## SChernykh | 2026-01-08T13:06:15+00:00
Both are `Linux aarch64` = 64-bit mode.

# Action History
- Created by: meanwhile131 | 2026-01-07T20:23:41+00:00
