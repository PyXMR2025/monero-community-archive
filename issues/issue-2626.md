---
title: '"FAILED TO APPLY MSR MOD, HASHRATE WILL BE LOW" on Windows 11 Pro Insider'
source_url: https://github.com/xmrig/xmrig/issues/2626
author: IdrisKalp
assignees: []
labels: []
created_at: '2021-10-11T23:58:36+00:00'
updated_at: '2025-12-22T22:52:07+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
MSR mod cannot be applied with both official binaries and the one I built myself. Output is here:

`* ABOUT        XMRig/6.15.2 gcc/11.2.1
 * LIBS         libuv/1.42.0 OpenSSL/3.0.0 hwloc/2.5.0
 * HUGE PAGES   permission granted
 * 1GB PAGES    unavailable
 * CPU          AMD Ryzen 9 3950X 16-Core Processor (1) 64-bit AES VM
                L2:8.0 MB L3:64.0 MB 16C/32T NUMA:1
 * MEMORY       15.6/31.9 GB (49%)
                DIMM 0: <empty>
                DIMM_A1: 16 GB DDR4 @ 3600 MHz F4-3600C18-16GVK
                DIMM 0: <empty>
                DIMM_B1: 16 GB DDR4 @ 3600 MHz F4-3600C18-16GVK
 * MOTHERBOARD  Micro-Star International Co., Ltd. - MS-7C84
 * DONATE       1%
 * ASSEMBLY     auto:ryzen
 * POOL #1      randomxmonero.eu.nicehash.com:3380 algo rx/0
 * COMMANDS     hashrate, pause, resume, results, connection
 * HTTP API     127.0.0.1:4001
 * OPENCL       disabled
 * CUDA         disabled
[2021-10-12 02:53:32.600]  net      use pool randomxmonero.eu.nicehash.com:3380  172.65.200.133
[2021-10-12 02:53:32.601]  net      new job from randomxmonero.eu.nicehash.com:3380 diff 218007 algo rx/0 height 2468948 (25 tx)
[2021-10-12 02:53:32.602]  cpu      use argon2 implementation AVX2
[2021-10-12 02:53:32.630]  msr      cannot set MSR 0xc0011020 to 0x0000000000000000
[2021-10-12 02:53:32.653]  msr      FAILED TO APPLY MSR MOD, HASHRATE WILL BE LOW
[2021-10-12 02:53:32.654]  randomx  init dataset algo rx/0 (32 threads) seed 8389f452540f09eb...
[2021-10-12 02:53:32.733]  randomx  allocated 2336 MB (2080+256) huge pages 0% 0/1168 +JIT (78 ms)
[2021-10-12 02:53:34.868]  randomx  dataset ready (2135 ms)
[2021-10-12 02:53:34.868]  cpu      use profile  rx  (32 threads) scratchpad 2048 KB
[2021-10-12 02:53:36.891]  cpu      READY threads 32/32 (32) huge pages 41% 13/32 memory 65536 KB (2021 ms)
[2021-10-12 02:53:37.847]  signal   Ctrl+C received, exiting
[2021-10-12 02:53:37.863]  cpu      stopped (13 ms)
[2021-10-12 02:53:37.879]  msr      cannot set MSR 0xc0011020 to 0x0006404000000000`

FYI, I'm running it as administrator too. 


# Discussion History
## SChernykh | 2021-10-12T05:34:44+00:00
`CPU` line shows that you're running in a VM. MSR mod doesn't work in virtual machines, it requires real hardware. Also, you can try solutions from https://github.com/xmrig/xmrig/issues/1891#issuecomment-725241656 (read comments there).

## IdrisKalp | 2021-10-12T12:35:37+00:00
> 
> 
> `CPU` line shows that you're running in a VM. MSR mod doesn't work in virtual machines, it requires real hardware. Also, you can try solutions from [#1891 (comment)](https://github.com/xmrig/xmrig/issues/1891#issuecomment-725241656) (read comments there).

No I actually running on real hardware.

## SChernykh | 2021-10-12T12:49:44+00:00
You're actually running xmrig in a VM. Either it's Windows itself or a 3rd-party software like Docker that causes this, but xmrig runs in a VM and can't access MSR registers. Secure boot in BIOS can also cause this (see the link above).

## IdrisKalp | 2021-10-12T14:49:25+00:00
> 
> 
> You're actually running xmrig in a VM. Either it's Windows itself or a 3rd-party software like Docker that causes this, but xmrig runs in a VM and can't access MSR registers. Secure boot in BIOS can also cause this (see the link above).

There is no Docker installed. This issue doesn't happen on Linux also. 

## IdrisKalp | 2021-10-12T15:06:24+00:00
Problem is due to Windows "Memory integrity" setting. Disabling it solved issue. Thanks. İt can be closed.


## electricdelicate | 2021-10-14T07:31:32+00:00
I`ve a similar problem since today with Windows 11 Pro. Unfortunately the "Memory Integrity" is disabled but problem still there ...

` * ABOUT        XMRig/6.15.2 gcc/10.1.0
 * LIBS         libuv/1.42.0 OpenSSL/1.1.1l hwloc/2.5.0
 * HUGE PAGES   permission granted
 * 1GB PAGES    unavailable
 * CPU          AMD Ryzen 9 3950X 16-Core Processor (1) 64-bit AES
                L2:8.0 MB L3:64.0 MB 16C/32T NUMA:1
 * MEMORY       6.0/15.9 GB (38%)
                DIMM 0: <empty>
                DIMM_A1: 8 GB DDR4 @ 3600 MHz BL8G36C16U4B.M8FE1
                DIMM 0: <empty>
                DIMM_B1: 8 GB DDR4 @ 3600 MHz BL8G36C16U4B.M8FE1
 * MOTHERBOARD  Micro-Star International Co., Ltd. - MAG B550M MORTAR WIFI (MS-7C94)
 * DONATE       1%
 * ASSEMBLY     auto:ryzen
 * POOL #1      stratum+tcp://randomxmonero.eu-west.nicehash.com:3380 algo rx/0
 * COMMANDS     'h' hashrate, 'p' pause, 'r' resume, 's' results, 'c' connection
 * HTTP API     127.0.0.1:4029
 * OPENCL       disabled
 * CUDA         disabled
[2021-10-14 09:29:44.686]  net      use pool randomxmonero.eu-west.nicehash.com:3380  172.65.226.105
[2021-10-14 09:29:44.686]  net      new job from randomxmonero.eu-west.nicehash.com:3380 diff 218007 algo rx/0 height 2470625 (179 tx)
[2021-10-14 09:29:44.686]  cpu      use argon2 implementation AVX2
[2021-10-14 09:29:44.686]  msr      service WinRing0_1_2_0 already exists
[2021-10-14 09:29:44.687]  msr      service path: "\??\C:\Program Files (x86)\Awesome Miner\LibreHardwareMonitorLib.sys"
**[2021-10-14 09:29:44.702]  msr      failed to remove WinRing0 driver, error 1072
[2021-10-14 09:29:44.702]  msr      FAILED TO APPLY MSR MOD, HASHRATE WILL BE LOW**
[2021-10-14 09:29:44.702]  randomx  init dataset algo rx/0 (29 threads) seed 2248ce4dc9e85115...
[2021-10-14 09:29:44.702]  randomx  allocated 2336 MB (2080+256) huge pages 100% 1168/1168 +JIT (0 ms)
[2021-10-14 09:29:46.350]  randomx  dataset ready (1648 ms)
[2021-10-14 09:29:46.350]  cpu      use profile  rx  (28 threads) scratchpad 2048 KB`

## SChernykh | 2021-10-14T08:18:27+00:00
`C:\Program Files (x86)\Awesome Miner\LibreHardwareMonitorLib.sys` is interfering. Try to reinstall Awesome Miner or completely remove it, reboot after it to be sure.

## tye-mustafa | 2021-10-22T18:23:05+00:00
Reboot is required after running XMRIG first time on fresh windows. Simple

## Soggydan | 2022-01-05T09:08:20+00:00
check here for 5 windows fixes
[https://www.home-mining.com/failed-to-apply-msr-mod-hashrate-will-be-low/](url)

## Sparticuz | 2022-03-29T13:36:40+00:00
I'm getting the same error. I believe it started when I upgraded to Windows 22581. I've gone through all the settings, run as admin, memory isolation off. I'm not running docker or any VM for this app, just normal command prompt, not sure why it's stating VM in CPU. It was working fine before upgrading.
```
D:\xmrig>start.cmd
 * ABOUT        XMRig/6.16.4 MSVC/2019
 * LIBS         libuv/1.42.0 OpenSSL/1.1.1l hwloc/2.5.0
 * HUGE PAGES   permission granted
 * 1GB PAGES    unavailable
 * CPU          Intel(R) Core(TM) i7-10700 CPU @ 2.90GHz (1) 64-bit AES VM
                L2:2.0 MB L3:16.0 MB 8C/16T NUMA:1
 * MEMORY       11.7/31.7 GB (37%)
                DIMM1: 8 GB DDR4 @ 2933 MHz HMA81GU6DJR8N-XN
                DIMM2: 8 GB DDR4 @ 2933 MHz HMA81GU6DJR8N-XN
                DIMM3: 8 GB DDR4 @ 2933 MHz HMA81GU6DJR8N-XN
                DIMM4: 8 GB DDR4 @ 2933 MHz HMA81GU6DJR8N-XN
 * MOTHERBOARD  Dell Inc. - OptiPlex 5080
 * DONATE       1%
 * ASSEMBLY     auto:intel
 * POOL #1      xmr-us-east1.nanopool.org:14433 coin Monero
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       disabled
 * CUDA         disabled
[2022-03-29 09:33:49.055]  net      use pool xmr-us-east1.nanopool.org:14433 TLSv1.2 142.44.243.6
[2022-03-29 09:33:49.055]  net      fingerprint (SHA-256): "c38886efdee542ebd99801b75c75d3498d97978bbcdec07c7271cb19729e014f"
[2022-03-29 09:33:49.055]  net      new job from xmr-us-east1.nanopool.org:14433 diff 480045 algo rx/0 height 2590236 (8 tx)
[2022-03-29 09:33:49.056]  cpu      use argon2 implementation AVX2
[2022-03-29 09:33:49.073]  msr      cannot set MSR 0x000001a4 to 0x000000000000000f
[2022-03-29 09:33:49.092]  msr      FAILED TO APPLY MSR MOD, HASHRATE WILL BE LOW
```

## SChernykh | 2022-03-29T13:52:46+00:00
Try to turn off Secure Boot in BIOS. Although you have a Dell motherboard, I'm not sure this setting can be turned off there.

## Sparticuz | 2022-03-29T13:53:23+00:00
> Try to turn off Secure Boot in BIOS. Although you have a Dell motherboard, I'm not sure this setting can be turned off there.

Secure boot was on before, but I tried disabling it and am getting the same message.

## Spudz76 | 2022-03-29T21:37:38+00:00
I'm Win10 but ended up using about three different methods of killing the Virtualized Protection shell junk.

Unfortunately I forget which ones but essentially if you google HVCI there will be a few different methods.  I also don't know which one fixed it since I just did them all and then rebooted, after the simple Memory Integrity setting didn't work.

Possibly [this reg-key did it](https://docs.microsoft.com/en-us/windows/security/threat-protection/device-guard/enable-virtualization-based-protection-of-code-integrity#how-to-turn-off-hvci)?

## Jinxsyns | 2023-05-22T22:39:47+00:00
 * ABOUT        XMRig/6.19.2 gcc/11.2.0
 * LIBS         libuv/1.44.2 OpenSSL/1.1.1s hwloc/2.9.0
 * HUGE PAGES   permission granted
 * 1GB PAGES    unavailable
 * CPU          AMD Ryzen 9 7950X 16-Core Processor (1) 64-bit AES VM
                L2:16.0 MB L3:64.0 MB 16C/32T NUMA:1
 * MEMORY       10.8/63.2 GB (17%)
                DIMMA1: <empty>
                DIMMA2: 32 GB DDR5 @ 6000 MHz F5-6000J3238G32G
                DIMMB1: <empty>
                DIMMB2: 32 GB DDR5 @ 6000 MHz F5-6000J3238G32G
 * MOTHERBOARD  Micro-Star International Co., Ltd. - MS-7D78
 * DONATE       1%
 * ASSEMBLY     auto:ryzen
 * POOL #1      stratum+tcp://pool.us.woolypooly.com:3110 algo ghostrider
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       disabled
 * CUDA         disabled
[2023-05-22 17:37:29.102]  net      use pool pool.us.woolypooly.com:3110  5.161.112.148
[2023-05-22 17:37:29.102]  net      new job from pool.us.woolypooly.com:3110 diff 6554 algo ghostrider height 575400
[2023-05-22 17:37:29.102]  msr      service WinRing0_1_2_0 already exists, but with a different service name
[2023-05-22 17:37:29.116]  msr      cannot set MSR 0xc0011020 to 0x0004400000000000
[2023-05-22 17:37:29.116]  msr      FAILED TO APPLY MSR MOD, HASHRATE WILL BE LOW

I'm having the same issue for some reason I've tried deleteing duplicate folders of xmrig I had from reading the other comments only thing I don't know about is if secure boot is on or not could that be my issue?


## arnold-vianna | 2023-09-25T08:29:47+00:00

run xmrig as aminisrator worked for me after the switch to win 11

## tye-mustafa | 2023-10-03T18:31:33+00:00
when will u upload this to Google play?


On Mon, Sep 25, 2023 at 1:30 PM arnold vianna ***@***.***>
wrote:

> run xmrig as aminisrator worked for me after the switch to win 11
>
> —
> Reply to this email directly, view it on GitHub
> <https://github.com/xmrig/xmrig/issues/2626#issuecomment-1733167597>, or
> unsubscribe
> <https://github.com/notifications/unsubscribe-auth/AGIVVAX7KA4VNVHIU6OT3FLX4E6IPANCNFSM5FZJEGBQ>
> .
> You are receiving this because you commented.Message ID:
> ***@***.***>
>


## atoates | 2023-10-27T12:06:06+00:00
Still not working for me (both 'VM' and failing 'MSR') after following all instructions I could find. 

Running: Windows 11 10.0.22635 / Xmrig 6.20.0 

- Secure Boot in BIOS = Disabled
- Windows "Memory integrity" = Disabled 

![WhatsApp Image 2023-10-27 at 12 47 07](https://github.com/xmrig/xmrig/assets/44772419/00186782-1dc6-487e-9857-004cbb46ea8c)







## atoates | 2023-10-27T14:10:17+00:00
> Still not working for me (both 'VM' and failing 'MSR') after following all instructions I could find.
> 
> Running: Windows 11 10.0.22635 / Xmrig 6.20.0
> 
> * Secure Boot in BIOS = Disabled
> * Windows "Memory integrity" = Disabled
> 
> ![WhatsApp Image 2023-10-27 at 12 47 07](https://user-images.githubusercontent.com/44772419/278636307-00186782-1dc6-487e-9857-004cbb46ea8c.jpeg)

Ok here's what fixed it. 

After having Secure Boot in BIOS and Memory Integrity in Windows Settings both disabled, I noticed the "Visualisation based security" was still Enabled in System Information.

Went back to BIOS and disabled the settings "AMD Platform Security Processor" and "AMD SVM Technology" then tried again and the error is now gone and hashrate ~40% higher

One side-effect is being logged out of all Microsoft accounts for some reason.

Final question remaining is RE: the opencl GPU which doesn't seem to be doing anything?

UPDATE: after disabling OpenCL hashrate jumped up another ~20%.



## SteaceP | 2024-03-13T02:26:03+00:00
Sorry for the off topic question ;)
Are you using your computer like this for productivity or gaming? I mean with "security" off (secureboot, fTPM, etc.)
If you do, did you happen to see improvements in those categories like you did in your hashrate?

## jsalaz-Gramps | 2024-04-04T19:53:38+00:00
I would do this workaround, but I have gotten 72 pieces of malware by turning the Memory Integrity off.  It creeps in, since Malwarebytes thinks it's regular code.  SO I spent the morning removing them.  I appreciate the jump from 3k to 108k hashrate on xmrig with it off, but I will not be turning it off.

## Daniori | 2024-08-12T17:43:50+00:00
Hallo. What is causing this error that the speed is not displayed? Windows 10 system and running as system administrator. 

![IMG_20240812_193737](https://github.com/user-attachments/assets/64e87600-109d-47b3-b1da-68d7908551f7)


## Spudz76 | 2024-08-12T18:12:19+00:00
Old R7's don't really work correctly without also ancient driver, which probably requires ancient OS, and so on, so it's probably not doing anything.  Disable OpenCL and just use the CPU although single stick of relatively slow memory probably isn't going to get a great rate either.  It should be getting some rate from the CPU though even if the GPU hung.  Also RandomX isn't for GPUs even on really fast new ones it is terrible (on purpose, it's a CPU algorithm).

CN-GPU or something might work on the R7 but it won't be worth it (power consumption vs value).  To do that you'd run a separate instance of xmrig with CPU disabled and OpenCL enabled, so that it can run different algos.

## matsyui | 2024-09-17T07:49:47+00:00



cannot read MSR 0x000001a4
FAILED TO APPLY MSR MOD, HASHRATE WILL BE LOW

I am running this mining via SSH on my "personal server" 
![image](https://github.com/user-attachments/assets/d615d074-9a23-4b5b-b7fa-d37c6f1a4bbe)
![image](https://github.com/user-attachments/assets/ef4cf97e-b23b-46f5-8a10-f1feaf948eb7)

**solution i did is add `sudo` or run it as root/admin for windows**

## lxl66566 | 2025-03-14T14:20:12+00:00
I turns off the *NX mode* in bios CPU advanced settings, and it works for me.

## saa938 | 2025-07-30T01:56:26+00:00
I did everything that these guys said (turn off secure boot, visualization based security, turned off memory integrity), and it didn't work. Finally, I disabled SVM (Secure Virtual Machine) in BIOS and it worked.

## aa-delite | 2025-12-22T22:51:00+00:00
Windows 11 fix (no BIOS settings required):

1. Google to Disable "core isolation memory integrity" setting. 
Maybe enough. If not:
2. Set regedit value, reboot:HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\DeviceGuard
EnableVirtualizationBasedSecurity set value to 0

# Action History
- Created by: IdrisKalp | 2021-10-11T23:58:36+00:00
