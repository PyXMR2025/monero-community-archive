---
title: '[RPi 5] issue since update to Raspi OS trixie'
source_url: https://github.com/xmrig/xmrig/issues/3729
author: zepp-fr
assignees: []
labels: []
created_at: '2025-11-02T14:00:01+00:00'
updated_at: '2026-03-28T13:03:36+00:00'
type: issue
status: closed
closed_at: '2026-03-28T13:03:36+00:00'
---

# Original Description
runs a couple of seconds then exits

Device : Raspberry Pi 5 with xmrig 6.24.0

Output : 

> norb@raspberrypi-trixie:~ $ ./Cryptos/XMR/xmrig/build/xmrig
>[2025-11-02 14:54:24.514] unable to open "/home/norb/Cryptos/XMR/xmrig/build/config.json".
>[2025-11-02 14:54:24.514] unable to open "/home/norb/.xmrig.json".
 >* ABOUT        XMRig/6.24.0 gcc/12.2.0 (built for Linux ARMv8, 64 bit)
 >* LIBS         libuv/1.50.0 OpenSSL/3.0.16 hwloc/2.12.0
 >* HUGE PAGES   unavailable
 >* 1GB PAGES    unavailable
 >* CPU          ARM Cortex-A76 (1) 64-bit AES
  >              L2:2.0 MB L3:2.0 MB 4C/4T NUMA:8
 >* MEMORY       1.6/7.9 GB (21%)
 >* DONATE       0%
 >* POOL #1      xmr-eu1.nanopool.org:10343 algo rx/0
 >* COMMANDS     hashrate, pause, resume, results, connection
 >* OPENCL       disabled
 >* CUDA         disabled
>[2025-11-02 14:54:24.635]  net      use pool xmr-eu1.nanopool.org:10343 TLSv1.3 51.38.65.123
>[2025-11-02 14:54:24.635]  net      fingerprint (SHA-256): "c38886efdee542ebd99801b75c75d3498d97978bbcdec07c7271cb19729e014f"
>[2025-11-02 14:54:24.635]  net      new job from xmr-eu1.nanopool.org:10343 diff 480045 algo rx/0 height 3535168 (30 tx)
>[2025-11-02 14:54:24.635]  cpu      use argon2 implementation default
>[2025-11-02 14:54:24.635]  randomx  init datasets algo rx/0 (4 threads) seed 9aece9037547eabe...
>[2025-11-02 14:54:24.637]  randomx  #1 allocated 2080 MB huge pages   0% (2 ms)
>[2025-11-02 14:54:24.637]  randomx  #3 allocated 2080 MB huge pages   0% (2 ms)
>[2025-11-02 14:54:24.637]  randomx  #2 allocated 2080 MB huge pages   0% (2 ms)
>[2025-11-02 14:54:24.637]  randomx  #0 allocated 2080 MB huge pages   0% (2 ms)
>[2025-11-02 14:54:24.637]  randomx  #4 allocated 2080 MB huge pages   0% (2 ms)
>[2025-11-02 14:54:24.638]  randomx  #7 allocated 2080 MB huge pages   0% (3 ms)
>[2025-11-02 14:54:24.638]  randomx  #6 allocated 2080 MB huge pages   0% (3 ms)
>[2025-11-02 14:54:24.638]  randomx  #5 allocated 2080 MB huge pages   0% (3 ms)
>[2025-11-02 14:54:24.644]  randomx  #0 allocated  256 MB huge pages   0% +JIT (5 ms)
>[2025-11-02 14:54:24.644]  randomx  -- allocated 16896 MB huge pages   0% 0/8448 (9 ms)
>[2025-11-02 14:54:29.280]  net      new job from xmr-eu1.nanopool.org:10343 diff 480045 algo rx/0 height 3535168 (35 tx)
>[2025-11-02 14:54:32.258]  net      new job from xmr-eu1.nanopool.org:10343 diff 480045 algo rx/0 height 3535169 (1 tx)
>[2025-11-02 14:54:41.557]  randomx  #0 dataset ready (16913 ms)
>[2025-11-02 14:54:42.276]  net      new job from xmr-eu1.nanopool.org:10343 diff 480045 algo rx/0 height 3535169 (3 tx)
>Processus arrêté


# Discussion History
## zepp-fr | 2025-11-02T14:33:10+00:00
I tried the disk on Raspberry Pi 4 and xmrig just runs fine!

## SChernykh | 2025-11-02T18:04:02+00:00
It says `NUMA:8`, so it tried to allocate the dataset 8 times (16 GB of memory). I'm pretty sure RPi5 doesn't have 8 NUMA nodes, so you messed up something when you compiled it.

## zepp-fr | 2025-11-03T18:41:32+00:00
I compiled the miner the standard way. As explained on xmrig site.

Once before migrating to trixie, once after. Both programs are having the same issue.
With bookworm my miner behaved correctly.

## ghost | 2025-11-03T18:45:47+00:00
I'm not sure but maybe the [numa emulation patch](https://www.jeffgeerling.com/blog/2024/numa-emulation-speeds-pi-5-and-other-improvements) for the Pi5 made xmrig set NUMA = 8? Anyhow set numa to false in the config.json under 
`"randomx": {
    "numa": false, ....` 
 so only one dataset gets allocated. It works on my pi5 8GB version

## zepp-fr | 2025-11-04T10:05:32+00:00
Setting numa to false in configuration file is a workaround that works in my case, but maybe some source code should be investigated.

As yours, my Pi is a 8 GB variant, so allocating 16 GB memory may not be a good idea.

## HumbleDeer | 2025-11-16T20:54:41+00:00
> Setting numa to false in configuration file is a workaround that works in my case, but maybe some source code should be investigated.

Seems to work fine for the use cases it's intended for. It shouldn't be used by default, because it's a special accomodation for special situations.


## rocklake | 2026-01-06T14:27:15+00:00
> I'm not sure but maybe the [numa emulation patch](https://www.jeffgeerling.com/blog/2024/numa-emulation-speeds-pi-5-and-other-improvements) for the Pi5 made xmrig set NUMA = 8? Anyhow set numa to false in the config.json under `"randomx": { "numa": false, ....` so only one dataset gets allocated. It works on my pi5 8GB version

I also have the same issue and that works do you know if there’s a command line argument that does the same thing thanks

## SChernykh | 2026-01-06T15:18:20+00:00
https://xmrig.com/docs/miner/command-line-options
`	--randomx-no-numa	disable NUMA support for RandomX`

## rocklake | 2026-01-06T15:42:08+00:00
> https://xmrig.com/docs/miner/command-line-options ` --randomx-no-numa disable NUMA support for RandomX`

Thank you, That page helps a lot.

# Action History
- Created by: zepp-fr | 2025-11-02T14:00:01+00:00
- Closed at: 2026-03-28T13:03:36+00:00
