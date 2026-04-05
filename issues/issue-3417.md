---
title: Failed to apply MSR mod (Linux Mint)
source_url: https://github.com/xmrig/xmrig/issues/3417
author: 3kh0
assignees: []
labels: []
created_at: '2024-02-06T02:00:06+00:00'
updated_at: '2024-02-06T02:20:00+00:00'
type: issue
status: closed
closed_at: '2024-02-06T02:20:00+00:00'
---

# Original Description
I recently moved over from Windows 11 to Linux Mint on one of my spare computers. I have been using it with Windows to mine monero for quite some time now getting a hash rate of around 4.2k. Now on linux mint, I am getting errors of a MSR mod and a hash rate of 1k.

Console:
```
 * ABOUT        XMRig/6.21.0 gcc/5.4.0 (built for Linux x86-64, 64 bit)
 * LIBS         libuv/1.44.2 OpenSSL/1.1.1s hwloc/2.9.0
 * HUGE PAGES   supported
 * 1GB PAGES    supported
 * CPU          11th Gen Intel(R) Core(TM) i5-11400H @ 2.70GHz (1) 64-bit AES
                L2:7.5 MB L3:12.0 MB 6C/12T NUMA:1
 * MEMORY       15.4/31.1 GB (49%)
                Controller0-ChannelA-DIMM0: 16 GB DDR4 @ 3200 MHz                     
                Controller0-ChannelB-DIMM0: <empty>
                Controller0-ChannelC-DIMM0: <empty>
                Controller0-ChannelD-DIMM0: <empty>
                Controller1-ChannelA-DIMM0: 16 GB DDR4 @ 3200 MHz                     
                Controller1-ChannelB-DIMM0: <empty>
                Controller1-ChannelC-DIMM0: <empty>
                Controller1-ChannelD-DIMM0: <empty>
 * MOTHERBOARD  TGL - Scala_TLS
 * DONATE       1%
 * ASSEMBLY     auto:intel
 * POOL #1      us2.monero.herominers.com:1111 algo rx/0
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       disabled
 * CUDA         disabled
[2024-02-05 20:52:21.717]  net      use pool us2.monero.herominers.com:1111 TLSv1.3 141.95.126.31
[2024-02-05 20:52:21.718]  net      fingerprint (SHA-256): "5f098b234f8c2d125cf1b74156850ffc62289a39ded9ed6c2d5facf713542a30"
[2024-02-05 20:52:21.718]  net      new job from us2.monero.herominers.com:1111 diff 240009 algo rx/0 height 3077997 (1 tx)
[2024-02-05 20:52:21.718]  cpu      use argon2 implementation AVX-512F
[2024-02-05 20:52:21.718]  msr      0x000001a4:0x0000000000000000 -> 0x000000000000000f
[2024-02-05 20:52:21.718]  msr      cannot set MSR 0x000001a4 to 0x000000000000000f
[2024-02-05 20:52:21.718]  msr      FAILED TO APPLY MSR MOD, HASHRATE WILL BE LOW
[2024-02-05 20:52:21.718]  randomx  init dataset algo rx/0 (12 threads) seed 30b6c8848940031f...
[2024-02-05 20:52:22.006]  randomx  allocated 3072 MB (2080+256) huge pages 100% 3/3 +JIT (288 ms)
[2024-02-05 20:52:28.418]  randomx  dataset ready (6411 ms)
[2024-02-05 20:52:28.418]  cpu      use profile  rx  (6 threads) scratchpad 2048 KB
[2024-02-05 20:52:28.435]  cpu      READY threads 6/6 (6) huge pages 100% 6/6 memory 12288 KB (17 ms)
[2024-02-05 20:53:28.469]  miner    speed 10s/60s/15m 1071.0 n/a n/a H/s max 1116.6 H/s
[2024-02-05 20:54:00.159]  net      new job from us2.monero.herominers.com:1111 diff 240009 algo rx/0 height 3077998 (2 tx)
[2024-02-05 20:54:28.518]  miner    speed 10s/60s/15m 957.4 947.7 n/a H/s max 1116.6 H/s
```
It does get shares accepted, but they are much more few and far between. 

<details>
<summary>System info</summary>
System:
  Kernel: 5.15.0-92-generic x86_64 bits: 64 compiler: gcc v: 11.4.0 Desktop: Cinnamon 6.0.4
    tk: GTK 3.24.33 wm: muffin vt: 7 dm: LightDM 1.30.0 Distro: Linux Mint 21.3 Virginia
    base: Ubuntu 22.04 jammy
Machine:
  Type: Laptop System: Acer product: Nitro AN515-57 v: V1.19 serial: <superuser required>
  Mobo: TGL model: Scala_TLS v: V1.19 serial: <superuser required> UEFI: Insyde v: 1.19
    date: 10/28/2022
CPU:
  Info: 6-core model: 11th Gen Intel Core i5-11400H bits: 64 type: MT MCP smt: enabled
    arch: Tiger Lake rev: 1 cache: L1: 480 KiB L2: 7.5 MiB L3: 12 MiB
  Speed (MHz): avg: 2176 high: 2356 min/max: 800/4500 cores: 1: 2151 2: 2183 3: 2142 4: 2182
    5: 2189 6: 2192 7: 2356 8: 2050 9: 2124 10: 2011 11: 2247 12: 2290 bogomips: 64512
  Flags: avx avx2 ht lm nx pae sse sse2 sse3 sse4_1 sse4_2 ssse3
Graphics:
  Device-1: Intel TigerLake-H GT1 [UHD Graphics] vendor: Acer Incorporated ALI driver: i915
    v: kernel ports: active: eDP-1 empty: DP-1,DP-2 bus-ID: 0000:00:02.0 chip-ID: 8086:9a68
    class-ID: 0300
  Device-2: NVIDIA TU117M [GeForce GTX 1650 Mobile / Max-Q] vendor: Acer Incorporated ALI
    driver: nvidia v: 535.154.05 ports: active: none empty: HDMI-A-1 bus-ID: 0000:01:00.0
    chip-ID: 10de:1f9d class-ID: 0300
  Device-3: Quanta HD User Facing type: USB driver: uvcvideo bus-ID: 3-9:2 chip-ID: 0408:a061
    class-ID: 0e02
  Display: x11 server: X.Org v: 1.21.1.4 driver: X: loaded: modesetting,nvidia
    unloaded: fbdev,nouveau,vesa gpu: i915 display-ID: :0 screens: 1
  Screen-1: 0 s-res: 1920x1080 s-dpi: 98 s-size: 499x280mm (19.6x11.0") s-diag: 572mm (22.5")
  Monitor-1: eDP-1 model: Chi Mei Innolux res: 1920x1080 hz: 144 dpi: 142
    size: 344x193mm (13.5x7.6") diag: 394mm (15.5") modes: 1920x1080
  OpenGL: renderer: Mesa Intel UHD Graphics (TGL GT1) v: 4.6 Mesa 23.0.4-0ubuntu1~22.04.1
    direct render: Yes
RAID:
  Hardware-1: Intel Volume Management Device NVMe RAID Controller driver: vmd v: 0.6 port: N/A
    bus-ID: 0000:00:0e.0 chip-ID: 8086:9a0b rev: class-ID: 0104
Drives:
  Local Storage: total: 1.14 TiB used: 59.32 GiB (5.1%)
  ID-1: /dev/nvme0n1 vendor: Micron model: MTFDKBA256TFK-1BC1AABHA size: 238.47 GiB
    speed: 63.2 Gb/s lanes: 4 type: SSD serial: <filter> rev: HPSV040 temp: 30.9 C scheme: GPT
  ID-2: /dev/sda vendor: Western Digital model: WD10SPZX-00Z10T0 size: 931.51 GiB
    speed: 6.0 Gb/s type: HDD rpm: 5400 serial: <filter> rev: 1A01 scheme: GPT
Partition:
  ID-1: / size: 233.18 GiB used: 59.31 GiB (25.4%) fs: ext4 dev: /dev/nvme0n1p2
  ID-2: /boot/efi size: 511 MiB used: 6.1 MiB (1.2%) fs: vfat dev: /dev/nvme0n1p1
Swap:
  ID-1: swap-1 type: file size: 2 GiB used: 0 KiB (0.0%) priority: -2 file: /swapfile

</details>


# Discussion History
## geekwilliams | 2024-02-06T02:10:53+00:00
Have you run as sudo and/or disabled Secure Boot? You may still have Secure Boot enabled after the windows 11 install  

## 3kh0 | 2024-02-06T02:20:00+00:00
Looks like secure boot was the issue. I disabled it and was able to use MSR. The hash rate went back up to windows levels. Thank you so much!

# Action History
- Created by: 3kh0 | 2024-02-06T02:00:06+00:00
- Closed at: 2024-02-06T02:20:00+00:00
