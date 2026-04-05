---
title: MSR mod fails after zen4 bios update
source_url: https://github.com/xmrig/xmrig/issues/3451
author: Redhawk18
assignees: []
labels: []
created_at: '2024-03-20T21:21:51+00:00'
updated_at: '2024-03-28T00:24:32+00:00'
type: issue
status: closed
closed_at: '2024-03-28T00:24:32+00:00'
---

# Original Description
**Describe the bug**
MSR mod fails after zen4 bios update

**To Reproduce**
Update the bios from stock to modern on a zen4 chipset

**Expected behavior**
The MSR mod to keep working

**Required data**
 ```
[2024-03-19 23:20:04**.783**]  msr      cannot set MSR 0xc0011020 to 0x0004400000000000
[2024-03-19 23:20:04**.783**]  msr      FAILED TO APPLY MSR MOD, HASHRATE WILL BE LOW
```

**Additional context**
```
System:
Host: Mythra Kernel: 6.7.7-1-default arch: x86_64 bits: 64
Desktop: KDE Plasma v: 5.27.10 Distro: openSUSE Tumbleweed 20240310
Machine:
Type: Desktop Mobo: Micro-Star model: MPG B650I EDGE WIFI (MS-7D73) v: 1.0
serial: <superuser required> UEFI: American Megatrends LLC. v: 1.82
date: 01/24/2024
CPU:
Info: 8-core AMD Ryzen 7 7800X3D [MT MCP] speed (MHz): avg: 4520
min/max: 400/5050
Graphics:
Device-1: AMD Navi 10 [Radeon RX 5600 OEM/5600 XT / 5700/5700 XT]
driver: amdgpu v: kernel
Device-2: AMD Raphael driver: amdgpu v: kernel
Display: wayland server: [X.org](http://x.org/) v: [1.21.1.11](http://1.21.1.11/) with: Xwayland v: 23.2.4
compositor: kwin_wayland driver: X: loaded: modesetting unloaded: fbdev,vesa
dri: radeonsi gpu: amdgpu,amdgpu resolution: 1: 1920x1080 2: 1920x1080
API: OpenGL v: 4.6 compat-v: 4.5 vendor: amd mesa v: 23.3.6 renderer: AMD
Radeon RX 5700 XT (radeonsi navi10 LLVM 17.0.6 DRM 3.57 6.7.7-1-default)
Network:
Device-1: Realtek RTL8125 2.5GbE driver: r8169
Device-2: MEDIATEK MT7922 802.11ax PCI Express Wireless Network Adapter
driver: mt7921e
Drives:
Local Storage: total: 3.2 TiB used: 579.44 GiB (17.7%)
Info:
Memory: total: 32 GiB note: est. available: 30.54 GiB used: 5.71 GiB (18.7%)
Processes: 459 Uptime: 0h 2m Shell: Bash inxi: 3.3.33
```

# Discussion History
## SChernykh | 2024-03-21T07:13:42+00:00
Please provide the full XMRig log at startup. I suspect that the BIOS update reset some settings and enabled VM/Secure boot again.

## Redhawk18 | 2024-03-27T22:00:37+00:00
> Please provide the full XMRig log at startup. I suspect that the BIOS update reset some settings and enabled VM/Secure boot again.

```
 * ABOUT        XMRig/6.21.1-mo1 gcc/13.2.1 (built for Linux x86-64, 64 bit)
 * LIBS         libuv/1.47.0 OpenSSL/3.1.4 hwloc/2.10.0
 * HUGE PAGES   supported
 * 1GB PAGES    disabled
 * CPU          AMD Ryzen 7 7800X3D 8-Core Processor (1) 64-bit AES
                L2:8.0 MB L3:96.0 MB 8C/16T NUMA:1
 * MEMORY       16.0/30.5 GB (52%)
                DIMMA1: 16 GB DDR5 @ 6400 MHz F5-6000J3636F16G              
                DIMMB1: 16 GB DDR5 @ 6400 MHz F5-6000J3636F16G              
 * MOTHERBOARD  Micro-Star International Co., Ltd. - MPG B650I EDGE WIFI (MS-7D73)
 * DONATE       0%
 * ASSEMBLY     auto:ryzen
 * POOL #1      gulf.moneroocean.stream:20128 coin Monero
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       disabled
 * CUDA         disabled
[2024-03-27 17:59:12.329]  net      use pool gulf.moneroocean.stream:20128 TLSv1.3 44.196.193.227
[2024-03-27 17:59:12.329]  net      fingerprint (SHA-256): "239daadd5c7d0ac097376c7871f787738826eef1c024729eff870e473b970855"
[2024-03-27 17:59:12.329]  net      new job from gulf.moneroocean.stream:20128 diff 745524 algo rx/0 height 216580
[2024-03-27 17:59:12.329]  cpu      use argon2 implementation AVX-512F
[2024-03-27 17:59:12.329]  msr      cannot set MSR 0xc0011020 to 0x0004400000000000
[2024-03-27 17:59:12.329]  msr      FAILED TO APPLY MSR MOD, HASHRATE WILL BE LOW
[2024-03-27 17:59:12.329]  randomx  init dataset algo rx/0 (16 threads) seed 3193d97b3bf208bc...
[2024-03-27 17:59:12.481]  randomx  allocated 2336 MB (2080+256) huge pages 100% 1168/1168 +JIT (152 ms)
[2024-03-27 17:59:14.675]  randomx  dataset ready (2194 ms)
[2024-03-27 17:59:14.676]  cpu      use profile  rx  (16 threads) scratchpad 2048 KB
[2024-03-27 17:59:14.681]  cpu      READY threads 16/16 (16) huge pages 100% 16/16 memory 32768 KB (5 ms)
[2024-03-27 17:59:52.136]  net      new job from gulf.moneroocean.stream:20128 diff 745524 algo rx/0 height 216581
[2024-03-27 18:00:14.807]  miner    speed 10s/60s/15m 7960.9 n/a n/a H/s max 8158.0 H/s
[2024-03-27 18:00:22.547]  cpu      accepted (1/0) diff 745524 (247 ms)
```

## SChernykh | 2024-03-27T22:34:06+00:00
I found a similar issue: https://github.com/xmrig/xmrig/issues/3359#issuecomment-1866590924
Try to disable secure boot. You can also check if `randomx_boost.sh` script works.

## Redhawk18 | 2024-03-28T00:24:32+00:00
It was that, It must have got reenabled via the update.

# Action History
- Created by: Redhawk18 | 2024-03-20T21:21:51+00:00
- Closed at: 2024-03-28T00:24:32+00:00
