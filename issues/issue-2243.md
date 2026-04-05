---
title: Unable to mine on ARMv7 (armv7l) cpu disabled (failed to start threads)
source_url: https://github.com/xmrig/xmrig/issues/2243
author: exwyezed
assignees: []
labels: []
created_at: '2021-04-07T13:12:50+00:00'
updated_at: '2021-04-10T20:56:57+00:00'
type: issue
status: closed
closed_at: '2021-04-10T20:56:57+00:00'
---

# Original Description
**To Reproduce**
Build from source on a `linux/arm/v7` device then run it with below command line options.

**Expected behavior**
Be able to mine.

**Required data**
Command line options:
```
$HOME/m --no-color --algo "rx/0" --coin monero -o xmr-eu1.nanopool.org:14433 -u <wallet-address> -p <password> --tls -k --cpu-priority 5
```

Logs:
```sh
 * ABOUT        XMRig/6.11.0 gcc/10.2.1
 * LIBS         libuv/1.41.0 OpenSSL/1.1.1j hwloc/2.4.1
 * HUGE PAGES   supported
 * 1GB PAGES    unavailable
 * CPU          ARM Cortex-A53 (1) 32-bit -AES
                L2:0.0 MB L3:0.0 MB 4C/4T NUMA:1
 * MEMORY       0.7/1.0 GB (74%)
 * DONATE       0%
 * POOL #1      xmr-eu1.nanopool.org:14433 coin monero
 * COMMANDS     'h' hashrate, 'p' pause, 'r' resume, 's' results, 'c' connection
[2021-04-07 12:57:08.020]  net      use pool xmr-eu1.nanopool.org:14433 TLSv1.2 139.99.102.70
[2021-04-07 12:57:08.020]  net      fingerprint (SHA-256): "c38886efdee542ebd99801b75c75d3498d97978bbcdec07c7271cb19729e014f"
[2021-04-07 12:57:08.021]  net      new job from xmr-eu1.nanopool.org:14433 diff 480045 algo cn/r height 2334090
[2021-04-07 12:57:08.021]  cpu      use profile  cn  (4 threads) scratchpad 2048 KB
[2021-04-07 12:57:08.567]  cpu      thread #0 self-test failed
[2021-04-07 12:57:08.574]  cpu      thread #1 self-test failed
[2021-04-07 12:57:08.594]  cpu      thread #3 self-test failed
[2021-04-07 12:57:08.857]  cpu      thread #2 self-test failed
[2021-04-07 12:57:08.857]  cpu      disabled (failed to start threads)
```

**Additional context**
May it doesn't work because the device only has 1.0 GB RAM?

# Discussion History
## SChernykh | 2021-04-07T13:29:24+00:00
v6.11.0 had a bug when you use `coin` option, try v6.11.1. But even if it's able to mine, it will be very slow.

## exwyezed | 2021-04-07T17:53:39+00:00
@SChernykh v6.11.1 fixed that error!

Now It's throwing out another error: `Bus error (core dumped)` (related #1537). I think this one is because there's not enough RAM in the machine. What do you think?

Logs:

```sh
 * ABOUT        XMRig/6.11.1 gcc/10.2.1
 * LIBS         libuv/1.41.0 OpenSSL/1.1.1j hwloc/2.4.1
 * HUGE PAGES   supported
 * 1GB PAGES    unavailable
 * CPU          ARM Cortex-A53 (1) 32-bit -AES
                L2:0.0 MB L3:0.0 MB 4C/4T NUMA:1
 * MEMORY       0.8/1.0 GB (80%)
 * DONATE       0%
 * POOL #1      xmr-eu1.nanopool.org:14433 coin monero
 * COMMANDS     'h' hashrate, 'p' pause, 'r' resume, 's' results, 'c' connection
[2021-04-07 17:39:59.054]  net      use pool xmr-eu1.nanopool.org:14433 TLSv1.2 139.99.102.74
[2021-04-07 17:39:59.054]  net      fingerprint (SHA-256): "c38886efdee542ebd99801b75c75d3498d97978bbcdec07c7271cb19729e014f"
[2021-04-07 17:39:59.054]  net      new job from xmr-eu1.nanopool.org:14433 diff 480045 algo rx/0 height 2334238
[2021-04-07 17:39:59.054]  cpu      use argon2 implementation default
[2021-04-07 17:40:00.256]  randomx  init dataset algo rx/0 (4 threads) seed ae2b3c3b6e013f9c...
[2021-04-07 17:40:00.256]  randomx  not enough memory for RandomX dataset
[2021-04-07 17:40:00.257]  randomx  failed to allocate RandomX dataset, switching to slow mode (1 ms)
Bus error (core dumped)
```

## exwyezed | 2021-04-07T18:02:37+00:00
@SChernykh BTW took me around 1 hour 50 minutes to build from source for ARMv7 and ARM64. Is there any doc that can I check out to learn which dependencies I need to save to re-use them later in the future builds? [something like this](https://github.com/xmrig/xmrig-deps) but for ARM.

Thanks for your contributions to this such awesome project! keep it going! :)

cc @xmrig 

## Spudz76 | 2021-04-10T01:46:57+00:00
Probably better to cross-compile from a real computer and copy over the binaries instead of compiling on-device.  Surprised compile even worked with 1GB mem it must have been swapping like crazy (burning out flash?).

## exwyezed | 2021-04-10T20:56:23+00:00
> Probably better to cross-compile from a real computer and copy over the binaries instead of compiling on-device.

Yeah, that's an option.

> Surprised compile even worked with 1GB mem it must have been swapping like crazy (burning out flash?).

I used [Buildx](https://www.docker.com/blog/multi-arch-build-and-images-the-simple-way/) Docker's experimental feature to compile XMRig for ARMv7 on my personal computer (MacBook Pro). Works like a charm and made my life easier :)

## exwyezed | 2021-04-10T20:56:57+00:00
I close this issue as `v6.11.1` fixed the initial issue.

# Action History
- Created by: exwyezed | 2021-04-07T13:12:50+00:00
- Closed at: 2021-04-10T20:56:57+00:00
