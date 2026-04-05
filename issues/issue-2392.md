---
title: xmrig-6.12.1 static linux works on my intel laptop, but fails on my amd desktop
source_url: https://github.com/xmrig/xmrig/issues/2392
author: Ferryistaken
assignees: []
labels: []
created_at: '2021-05-19T00:42:03+00:00'
updated_at: '2025-06-16T20:31:50+00:00'
type: issue
status: closed
closed_at: '2025-06-16T20:31:50+00:00'
---

# Original Description
xmrig-6.12.1 core dumps(sometimes bus error, sometimes just abort) after 1st job on my amd ryzen 9 3900x laptop, but works flawlessly on my intel i7-8750h laptop (same version, same pool, same config, same distro, same kernel)

This happens on kernel `5.12.4-zen1-2-zen`

**Expected behavior**
I expected the same software to run the same, but I suppose that this is because xmrig interfaces with the cpu at a very low level

**Required data**
 Desktop log for abort (core dumped):
```
* ABOUT        XMRig/6.12.1 gcc/9.3.0
 * LIBS         libuv/1.41.0 OpenSSL/1.1.1j hwloc/2.4.1
 * HUGE PAGES   supported
 * 1GB PAGES    disabled
 * CPU          AMD Ryzen 9 3900X 12-Core Processor (1) 64-bit AES
                L2:6.0 MB L3:64.0 MB 12C/24T NUMA:1
 * MEMORY       15.9/62.8 GB (25%)
 * DONATE       1%
 * ASSEMBLY     auto:ryzen
 * POOL #1      xmr-us-west1.nanopool.org:14433 coin monero
 * COMMANDS     hashrate, pause, resume, results, connection
[2021-05-18 20:37:01.741]  net      use pool xmr-us-west1.nanopool.org:14433 TLSv1.2 45.32.71.82
[2021-05-18 20:37:01.741]  net      fingerprint (SHA-256): "c38886efdee542ebd99801b75c75d3498d97978bbcdec07c7271cb19729e014f"
[2021-05-18 20:37:01.741]  net      new job from xmr-us-west1.nanopool.org:14433 diff 480045 algo rx/0 height 2363938
[2021-05-18 20:37:01.741]  cpu      use argon2 implementation AVX2
[2021-05-18 20:37:01.742]  msr      msr kernel module is not available
[2021-05-18 20:37:01.742]  msr      FAILED TO APPLY MSR MOD, HASHRATE WILL BE LOW
[2021-05-18 20:37:01.742]  randomx  init dataset algo rx/0 (24 threads) seed f08d3cc938b1215d...
[2021-05-18 20:37:01.742]  randomx  allocated 2336 MB (2080+256) huge pages 0% 0/1168 +JIT (0 ms)
[2021-05-18 20:37:03.346]  randomx  dataset ready (1604 ms)
[2021-05-18 20:37:03.346]  cpu      use profile  rx  (24 threads) scratchpad 2048 KB
[2021-05-18 20:37:03.356]  cpu      READY threads 24/24 (24) huge pages 0% 0/24 memory 49152 KB (9 ms)
zsh: abort (core dumped)  ./xmrig -o xmr-us-west1.nanopool.org:14433 -u  --tls --coin monero
```
Desktop log for bus error (core dumped):
```
* ABOUT        XMRig/6.12.1 gcc/9.3.0
 * LIBS         libuv/1.41.0 OpenSSL/1.1.1j hwloc/2.4.1
 * HUGE PAGES   supported
 * 1GB PAGES    disabled
 * CPU          AMD Ryzen 9 3900X 12-Core Processor (1) 64-bit AES
                L2:6.0 MB L3:64.0 MB 12C/24T NUMA:1
 * MEMORY       15.9/62.8 GB (25%)
 * DONATE       1%
 * ASSEMBLY     auto:ryzen
 * POOL #1      xmr-us-west1.nanopool.org:14433 coin monero
 * COMMANDS     hashrate, pause, resume, results, connection
[2021-05-18 20:29:49.363]  net      use pool xmr-us-west1.nanopool.org:14433 TLSv1.2 45.76.65.223
[2021-05-18 20:29:49.363]  net      fingerprint (SHA-256): "c38886efdee542ebd99801b75c75d3498d97978bbcdec07c727
1cb19729e014f"
[2021-05-18 20:29:49.363]  net      new job from xmr-us-west1.nanopool.org:14433 diff 480045 algo rx/0 height 2
363936
[2021-05-18 20:29:49.363]  cpu      use argon2 implementation AVX2
[2021-05-18 20:29:49.364]  msr      msr kernel module is not available
[2021-05-18 20:29:49.364]  msr      FAILED TO APPLY MSR MOD, HASHRATE WILL BE LOW
[2021-05-18 20:29:49.364]  randomx  init dataset algo rx/0 (24 threads) seed f08d3cc938b1215d...
[2021-05-18 20:29:49.364]  randomx  allocated 2336 MB (2080+256) huge pages 0% 0/1168 +JIT (0 ms)
[2021-05-18 20:29:50.979]  randomx  dataset ready (1615 ms)
[2021-05-18 20:29:50.979]  cpu      use profile  rx  (24 threads) scratchpad 2048 KB
[2021-05-18 20:29:50.988]  cpu      READY threads 24/24 (24) huge pages 0% 0/24 memory 49152 KB (9 ms)
[2021-05-18 20:30:04.159]  net      new job from xmr-us-west1.nanopool.org:14433 diff 480045 algo rx/0 height 2
363936
[2021-05-18 20:30:04.567]  net      new job from xmr-us-west1.nanopool.org:14433 diff 480045 algo rx/0 height 2
363937
zsh: bus error (core dumped)  ./xmrig -o xmr-us-west1.nanopool.org:14433 -u  --tls --coin monero
```

 - Command ran on both machines: `xmrig -o xmr-us-west1.nanopool.org:14433 -u <WALLET>  --tls --coin monero`
 - OS: Arch linux with kernel `5.12.4-zen1-2-zen`

LAPTOP:
![image](https://user-images.githubusercontent.com/47927670/118739926-a57b9e00-b818-11eb-84ab-5a1bcfb6837b.png)

DESKTOP:
![image](https://user-images.githubusercontent.com/47927670/118740062-ed9ac080-b818-11eb-80da-4d955e2f6257.png)



# Discussion History
## SChernykh | 2021-05-19T08:18:57+00:00
It looks like your 3900X desktop is not stable because it doesn't crash immediately, it did mine for 15 seconds in your desktop log for bus error.

## Ferryistaken | 2021-05-19T19:35:21+00:00
But it's the same OS and kernel as the laptop. How would I go about fixing this? Try another os or kernel?

## SChernykh | 2021-05-19T19:40:07+00:00
I assume it's hardware instability. Is your Ryzen overclocked? Or maybe it's overheating, or RAM is unstable.

## Ferryistaken | 2021-05-19T19:44:54+00:00
It's not overheating for sure, it's not overclocked either but I do lock the frequency, and the ram is using the intel xmp profile. Once I get home I'll try tweaking it to make it more "vanilla" and I'll update the issue

## Spudz76 | 2021-05-19T22:30:21+00:00
Check `dmesg` for explosions.

Usually this means your VRMs suck ass, you will have to check those by hand as they do not have any software reporting of therms.

If if has an 8-pin mobo additional power whip you need a real 8-wire whip.  If it only had 4-pin then you probably got a real garbage mobo model.   VRMs have to work harder when not supplied with all 8 pins of additional watts.

## Ferryistaken | 2021-05-19T23:40:21+00:00
@Spudz76 This is the output of `dmesg`:
```
[352211.977836] audit: type=1701 audit(1621467435.208:784): auid=1000 uid=1000 gid=1000 ses=1 pid=177962 comm="xmrig" exe="/tmp/new-xmrigh/xmrig-6.12.1/xmrig" sig=6 res=1
[352211.992163] audit: type=1334 audit(1621467435.222:785): prog-id=120 op=LOAD
[352211.992306] audit: type=1334 audit(1621467435.222:786): prog-id=121 op=LOAD
[352211.992418] audit: type=1334 audit(1621467435.222:787): prog-id=122 op=LOAD
[352211.993106] audit: type=1130 audit(1621467435.223:788): pid=1 uid=0 auid=4294967295 ses=4294967295 msg='unit=systemd-coredump@13-178122-0 comm="systemd" exe="/usr/lib/systemd/systemd" hostname=? addr=? terminal=? res=success'
[352216.711270] audit: type=1131 audit(1621467439.941:789): pid=1 uid=0 auid=4294967295 ses=4294967295 msg='unit=systemd-coredump@13-178122-0 comm="systemd" exe="/usr/lib/systemd/systemd" hostname=? addr=? terminal=? res=success'
[352216.815494] audit: type=1334 audit(1621467440.046:790): prog-id=122 op=UNLOAD
[352216.815497] audit: type=1334 audit(1621467440.046:791): prog-id=121 op=UNLOAD
[352216.815498] audit: type=1334 audit(1621467440.046:792): prog-id=120 op=UNLOAD
```

The mobo is an x570 Aorus Master, I got it new so the VRMs should be pretty good. The ram is corsair vengeance rgb pro @ 3600 Mhz

## Spudz76 | 2021-05-20T03:16:33+00:00
Agree that board should have good VRMs that stay cool even at 225W.

Vengeance is good stuff.

Back to the mystery, I have no other ideas.  "It always works fine on Ubuntu..." lol

# Action History
- Created by: Ferryistaken | 2021-05-19T00:42:03+00:00
- Closed at: 2025-06-16T20:31:50+00:00
