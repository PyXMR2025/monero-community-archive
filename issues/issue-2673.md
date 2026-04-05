---
title: start getting error after upgrade to windows 11
source_url: https://github.com/xmrig/xmrig/issues/2673
author: thonik123
assignees: []
labels: []
created_at: '2021-11-06T17:51:10+00:00'
updated_at: '2021-11-11T06:34:39+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
[2021-11-06 20:48:14.391]  cpu      use argon2 implementation AVX2
[2021-11-06 20:48:14.397]  msr      failed to start WinRing0 driver, error 183
[2021-11-06 20:48:14.439]  msr      FAILED TO APPLY MSR MOD, HASHRATE WILL BE LOW

just trying to srat mining with any options,  Run as Administrator option is ticked

CPU AMD Ryzen 5 PRO 4650G
Windows 11 Pro 22000.258

I can't say that hashrate become very low ( max 1950.6 H/s) because I'm using my PC as my main PC for my job and games etc.
but this error is very new, I didn't get it in past

# Discussion History
## SChernykh | 2021-11-06T17:55:34+00:00
Try disabling this: https://www.tomshardware.com/how-to/disable-vbs-windows-11

## thonik123 | 2021-11-06T18:06:15+00:00
> Try disabling this: https://www.tomshardware.com/how-to/disable-vbs-windows-11

пробовал, не помогло, ошибка всё равно лезет

## BobbyMcPrescott | 2021-11-11T05:42:21+00:00
> Try disabling this: https://www.tomshardware.com/how-to/disable-vbs-windows-11

I'm having the exact same error on AVX2 implementation since upgrading to Windows 11 and a Ryzen 9 3900x. I tried this fix and it was already completely disabled. I went back to the BIOS and disabled CPU virtualization to see if that did anything. It enabled the Core Isolation menu, but it was listed as off, and the problem persisted. I have tried running the exe as admin in a number of different folders on C and D, and oddly enough it only worked once, in the beginning, and this is with both the standalone and running via NiceHash. For some reason, when I first booted the PC and before I ever moved the folder, the xmrig folder I had been using prior to the upgrade with my old Ryzen 1600 would still enable MSR mode using the leftover configuration settings from my 1600. Ever since I moved it, it too won't work anywhere. It feels like Windows 11 has something else going on causing this and hopefully this information helps.

Edit: Realized that when I enabled virtualization I also caused it to run in a VM, so I'm going to try some of the steps in a different order after disabling virtualization again.

Edit Update: Confirmed that it DOES work on my D drive with virtualization disabled, but not C/Primary.

# Action History
- Created by: thonik123 | 2021-11-06T17:51:10+00:00
