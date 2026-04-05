---
title: 1GB pages disabled and Failed to apply MSR mod on Ubuntu 23.10
source_url: https://github.com/xmrig/xmrig/issues/3402
author: giosal
assignees: []
labels: []
created_at: '2024-01-16T09:13:38+00:00'
updated_at: '2025-06-18T22:25:00+00:00'
type: issue
status: closed
closed_at: '2025-06-18T22:25:00+00:00'
---

# Original Description
Hello,

I'm running XMRig for CPU to mine Ghostrider algo on Ubuntu 23.10.
I've got two issues:
- 1GB pages are disabled despite having run enable_1gb_pages script
- Failed to apply MSR mod, however it is working on Windows on the same machine

For the MSR, I've heard that you need to disable Secure boot but how come it is working in Windows then ?

I've tried randomx boost script, but I'm getting operation not permitted error:
````
sudo ../randomx_boost.sh 
Detected Zen3 CPU
wrmsr: pwrite: Operation not permitted
````

Please see the output of XMRig:

````
* ABOUT        XMRig/6.21.0 gcc/9.4.0 (built for Linux x86-64, 64 bit)
 * LIBS         libuv/1.44.2 OpenSSL/1.1.1s hwloc/2.9.0
 * HUGE PAGES   supported
 * 1GB PAGES    disabled
 * CPU          AMD Ryzen 9 5900HX with Radeon Graphics (1) 64-bit AES
                L2:4.0 MB L3:16.0 MB 8C/16T NUMA:1
 * MEMORY       12.4/27.3 GB (45%)
                DIMM_A0: 16 GB DDR4 @ 3200 MHz HMAA2GS6CJR8N-XN    
                DIMM_B0: 16 GB DDR4 @ 3200 MHz HMAA2GS6CJR8N-XN    
 * MOTHERBOARD  LENOVO - LNVNB161216
 * DONATE       5%
 * ASSEMBLY     auto:ryzen
 * POOL #1      stratum+tcp://ghostrider.eu.mine.zpool.ca:5354 algo ghostrider
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       disabled
 * CUDA         disabled
[2024-01-16 09:00:47.142]  net      use pool ghostrider.eu.mine.zpool.ca:5354  188.165.24.209
[2024-01-16 09:00:47.377]  net      new job from ghostrider.eu.mine.zpool.ca:5354 diff 1311 algo ghostrider height 93025
[2024-01-16 09:00:47.409]  msr      cannot set MSR 0xc0011020 to 0x0004480000000000
[2024-01-16 09:00:47.409]  msr      FAILED TO APPLY MSR MOD, HASHRATE WILL BE LOW
[2024-01-16 09:00:48.223]  cpu      use profile  *  (7 threads) scratchpad 2048 KB
[2024-01-16 09:00:48.351]  cpu      GhostRider algo 1: cn/dark-lite (256 KB)
[2024-01-16 09:00:48.351]  cpu      GhostRider algo 2: cn/fast (2 MB)
[2024-01-16 09:00:48.351]  cpu      GhostRider algo 3: cn/lite (1 MB)
[2024-01-16 09:00:48.400]  cpu      READY threads 7/7 (56) huge pages 100% 56/56 memory 114688 KB (177 ms)
[2024-01-16 09:00:48.951]  cpu      accepted (1/0) diff 1311 (170 ms)
[2024-01-16 09:01:01.940]  cpu      accepted (2/0) diff 1311 (187 ms)
[2024-01-16 09:01:09.544]  net      new job from ghostrider.eu.mine.zpool.ca:5354 diff 1311 algo ghostrider height 93025
````

# Discussion History
## geekwilliams | 2024-01-16T09:35:54+00:00
A quick google search indicates that turning OFF virtualization settings in the BIOS may help resolve your problem. Have you done this? 

## giosal | 2024-01-16T12:38:37+00:00
Thank you for your reply. But it does work in Windows with virtualization enabled.
Nevertheless, I'll give it a try

## giosal | 2024-01-16T13:32:17+00:00
@geekwilliams I've tried it, but I'm still getting the same output

## giosal | 2024-01-16T13:32:55+00:00
Updated original post with randomx bosst script output

## lesjokolat | 2024-01-16T16:58:16+00:00
are you running as sudo(root)?

## giosal | 2024-01-16T16:59:27+00:00
of course, all the commands launched as sudo
________________________________
ვისგან: lesjokolat ***@***.***>
გაგზავნილი: სამშაბათი, 16 იანვარი, 2024 17:58
ვის: xmrig/xmrig ***@***.***>
ასლი: George Salukvadze ***@***.***>; Author ***@***.***>
თემა: Re: [xmrig/xmrig] 1GB pages disabled and Failed to apply MSR mod on Ubuntu 23.10 (Issue #3402)


are you running as sudo(root)?

—
Reply to this email directly, view it on GitHub<https://github.com/xmrig/xmrig/issues/3402#issuecomment-1894143352>, or unsubscribe<https://github.com/notifications/unsubscribe-auth/AGDCGHUQWEREJ7HOZC27DNTYO2WTFAVCNFSM6AAAAABB4OMVGKVHI2DSMVQWIX3LMV43OSLTON2WKQ3PNVWWK3TUHMYTQOJUGE2DGMZVGI>.
You are receiving this because you authored the thread.Message ID: ***@***.***>


## SChernykh | 2024-01-16T17:12:48+00:00
So did you actually try to disable secure boot? https://github.com/xmrig/xmrig/issues/2534
As for 1GB pages, you don't need them for GhostRider.

## giosal | 2024-01-17T07:58:07+00:00
> So did you actually try to disable secure boot? #2534 As for 1GB pages, you don't need them for GhostRider.

This seems to have worked, thank you.
However, I would really like to know whether this is really the only available solution? Isn't it possible to sign the wrmsr in the same way NVIDIA or AMD sign their drivers? And import the key into Secure Boot MOK in the same way?
I would prefer to keep the Secure Boot on due to security concerns (obviously)

On the other hand, 1GB pages are still disabled. Am I correct to assume that they are enabled only for RandomX?

## geekwilliams | 2024-01-17T08:14:10+00:00
I don't have the answer you're looking for, but I'm curious if you installed Ubuntu with secure boot enabled? Are you dual booting this machine or did you use an install disk to boot and test? 

## giosal | 2024-01-17T09:46:46+00:00
> I don't have the answer you're looking for, but I'm curious if you installed Ubuntu with secure boot enabled? Are you dual booting this machine or did you use an install disk to boot and test?

I've installed Ubuntu on a machine with existing Windows installation, but on a separate physical disk, with a Secure Boot on.
So, from the beginning, I've had Secure Boot on and that's how I was able to correctly install the drivers.
I also have a Dual Boot, obviously, as I have an existing Windows installation, where it does work with Secure Boot on.

## giosal | 2024-01-22T13:01:27+00:00
Weird fact is that it works in Windows, but not in Ubuntu, both with virtualization and secure boot enabled

## geekwilliams | 2024-01-22T21:00:53+00:00
Got it. The Ubuntu release 23.10 is a short term one, but seems to have all the same stuff as a regular LTS in terms of signing. To answer your previous question, and according to issue [#1891](https://github.com/xmrig/xmrig/issues/1891#issuecomment-725241656), some system/os combos just require secure boot to be off to do CPU tweaks.

There's no way around it in your case. Windows uses the signed WinRing driver, but Linux uses built-kernel functionality to directly write to cpu registers. This is a lower level issue than xmrig, and to get any resolution you'd need to talk to your equipment manufacturer. 

## giosal | 2024-01-23T10:33:19+00:00
> Got it. The Ubuntu release 23.10 is a short term one, but seems to have all the same stuff as a regular LTS in terms of signing. To answer your previous question, and according to issue [#1891](https://github.com/xmrig/xmrig/issues/1891#issuecomment-725241656), some system/os combos just require secure boot to be off to do CPU tweaks.
> 
> There's no way around it in your case. Windows uses the signed WinRing driver, but Linux uses built-kernel functionality to directly write to cpu registers. This is a lower level issue than xmrig, and to get any resolution you'd need to talk to your equipment manufacturer.

Okay, thanks for the reply. That's quite interesting.
So, I imagine, there is no possibility to introduce something similar to WinRing driver to Linux systems?

## geekwilliams | 2024-01-23T16:01:21+00:00
There's no reason to. The kernel handles everything it needs to in that case. Your issue is because of the way the OEM of your motherboard implemented secure boot, not because Linux is missing functionality. 

## ghost | 2025-01-23T12:02:12+00:00
> Got it. The Ubuntu release 23.10 is a short term one, but seems to have all the same stuff as a regular LTS in terms of signing. To answer your previous question, and according to issue [#1891](https://github.com/xmrig/xmrig/issues/1891#issuecomment-725241656), some system/os combos just require secure boot to be off to do CPU tweaks.
> 
> There's no way around it in your case. Windows uses the signed WinRing driver, but Linux uses built-kernel functionality to directly write to cpu registers. This is a lower level issue than xmrig, and to get any resolution you'd need to talk to your equipment manufacturer.

can the issue be avoided by using debian?

## geekwilliams | 2025-01-23T18:23:53+00:00
> > Got it. The Ubuntu release 23.10 is a short term one, but seems to have all the same stuff as a regular LTS in terms of signing. To answer your previous question, and according to issue [#1891](https://github.com/xmrig/xmrig/issues/1891#issuecomment-725241656), some system/os combos just require secure boot to be off to do CPU tweaks.
> > 
> > There's no way around it in your case. Windows uses the signed WinRing driver, but Linux uses built-kernel functionality to directly write to cpu registers. This is a lower level issue than xmrig, and to get any resolution you'd need to talk to your equipment manufacturer.
> 
> can the issue be avoided by using debian?

No. Secure boot is the issue, not the OS.  

# Action History
- Created by: giosal | 2024-01-16T09:13:38+00:00
- Closed at: 2025-06-18T22:25:00+00:00
