---
title: Failed to install WinRing0 driver, error 1072
source_url: https://github.com/xmrig/xmrig/issues/1423
author: GoGitIt1
assignees: []
labels:
- bug
created_at: '2019-12-15T15:31:50+00:00'
updated_at: '2019-12-21T19:18:59+00:00'
type: issue
status: closed
closed_at: '2019-12-21T19:18:59+00:00'
---

# Original Description
I receive this error with the newest version (5.3) of XMRig. Any suggestions on how to fix this?

After relaunching XMRig, I also receive the error "msr failed to stop WinRing0 driver, error 1061" and "msr failed to remove WinRing0 driver, error 1072"
I expect MSR to run, but it looks like it is having a problem. 

Miner log:
![XMRig_Error](https://user-images.githubusercontent.com/58889729/70865145-22219300-1f28-11ea-8ba0-92931bf87482.JPG)

Config file:
start "" "D:\Documents\Cryptocurrency\Monero\Miners\XM_Rig\xmrig.exe" --donate-level 0 -o xmr-us-east1.nanopool.org:14433 -u WALLETADDRESS --tls -k --coin monero  -a rx/0 --max-cpu-usage 95
exit

OS: Windows 8.1


# Discussion History
## xmrig | 2019-12-15T16:19:42+00:00
Error 1072 = `ERROR_SERVICE_MARKED_FOR_DELETE`
Error 1061 = `ERROR_SERVICE_CANNOT_ACCEPT_CTRL`

Do you have other application which can use same driver? for hardware monitoring, etc.
Thank you.

## xmrig | 2019-12-15T19:00:53+00:00
This is definitely conflict with other software which use WinRing0 driver. Did you found it? I found one: Open Hardware Monitor.
Thank you.

## Bathmat | 2019-12-15T19:59:25+00:00
I'm also getting errors with MSR. I've tried disabling all my hardware montioring software, but still getting this error:
` msr  failed to start WinRing0 driver, error 2`

## xmrig | 2019-12-15T20:11:21+00:00
@Bathmat You did't place `WinRing0x64.sys` near to `xmrig.exe`.
Thank you.

## Bathmat | 2019-12-15T20:15:27+00:00
Ahh, thanks. Missed extracting that file. Appears to be working now after I closed HW Monitor software

## xmrig | 2019-12-15T20:45:45+00:00
I fixed compatibility with Open Hardware Monitor (error 1072) and probably with other applications which use the driver.
@Bathmat and added better error message for case if the file not found.

## pawelantczak | 2019-12-16T08:04:33+00:00
@GoGitIt1 consider enabling donation since @xmrig is investing his time twice, to develop and to help you.

## distributorofpain | 2019-12-17T03:32:51+00:00
Getting:
"failed to install WinRing0 driver, error 1072" when i start xmrig as admin.

If i kill it and start over, i get the following error:
"failed to stop WinRing0 driver, error 1061"
"failed to remove WinRing0 driver, error 1072"

The computers are windows 10 1903 with only basic software loaded for mining.  I downloaded 5.3.0 just now.  I also made sure the compatibility was set to unblock.

Two Rigs, exactly the same:
AMD 3700X with 16GB 3600 on B450 board.

I have another older machine that i setup as a miner with i7-3770K, most of the same software loaded, but no LED or overclocking software.  That one loads the MSR no issues.

*** I removed RGB Fusion and it fixed the driver load issue.  Seems the RGB software out there uses this driver.  ( i dont need it anyways because it wasnt disabling the RGB on the CPU like i wanted ).  Had to reboot after uninstall.

## SChernykh | 2019-12-17T09:55:10+00:00
@distributorofpain Error 1072 is fixed in dev branch and the fix will be in the next release.

## xmrig | 2019-12-17T15:14:08+00:00
Extra addition, next version will will also show path to exists driver (it helps to find another software witch use same driver) if set `"verbose": 1,` in config file (it also new option).

But it just for information, the miner will reuse already running driver, all of this implemented in dev branch.
Thank you.

## FAB1150 | 2019-12-17T19:49:53+00:00
how can I download the latest dev release? I don't use github very often, sorry.

## pawelantczak | 2019-12-17T19:54:43+00:00
Apparently you don't use your reading capability very often too. https://github.com/xmrig/xmrig/wiki/Build
Sorry for sarcasm, but such lack of self-sufficiency and independence can be really annoying. 

## xmrig | 2019-12-17T20:04:33+00:00
@FAB1150 https://github.com/xmrig/xmrig/issues/1425#issuecomment-566664690 binaries for every commit created by https://buildbot.xmrig.com/
Thank you.

## FAB1150 | 2019-12-17T23:40:58+00:00
@xmrig thank you! I downloaded dev 5.4.0, and i still have error 1072 but now it says "msr  service WinRing0_1_2_0 is already exists" "msr  failed to remove WinRing0 driver, error 1072".
i'll attach a screenshot.
I have HWinfo installed but NOT running, i also rebooted my pc to make sure.

EDIT: I downloaded [this build](https://buildbot.xmrig.com/#/builders/2/builds/1080) from the website you linked

![Screenshot (16)](https://user-images.githubusercontent.com/23463665/71043494-0c31ef00-212f-11ea-8a7d-88becb1c26d6.png)

## GoGitIt1 | 2019-12-18T01:10:59+00:00
> 
> 
> Error 1072 = `ERROR_SERVICE_MARKED_FOR_DELETE`
> Error 1061 = `ERROR_SERVICE_CANNOT_ACCEPT_CTRL`
> 
> Do you have other application which can use same driver? for hardware monitoring, etc.
> Thank you.

Thanks for fixing this, XMrig. I turned debugging mode on in Windows to get this in v5.2.1. I think this was the issue:
https://www.reddit.com/r/MoneroMining/comments/e9tuvd/randomx_boost_guide_for_ryzen_on_windows_9100_hs/

I tried disabling every service/app that I could think of, but problem mostly went away after doing this. For whatever reason, MSR was able to be active 2 out of around 20 times with debugging mode on. Not sure why. Glad problem fixed.

## xmrig | 2019-12-18T04:51:00+00:00
@FAB1150 You should try to set `"verbose": 1,` in config.json https://github.com/xmrig/xmrig/issues/1423#issuecomment-566584567
Thank you.

## xmrig | 2019-12-21T19:18:59+00:00
https://github.com/xmrig/xmrig/releases/tag/v5.4.0

# Action History
- Created by: GoGitIt1 | 2019-12-15T15:31:50+00:00
- Closed at: 2019-12-21T19:18:59+00:00
