---
title: '[5.3.0] Sudden severe performance degradation with Rx on AMD'
source_url: https://github.com/xmrig/xmrig/issues/1474
author: electroape
assignees: []
labels: []
created_at: '2019-12-31T06:57:11+00:00'
updated_at: '2021-04-12T15:06:30+00:00'
type: issue
status: closed
closed_at: '2021-04-12T15:06:30+00:00'
---

# Original Description
All of sudden PC becomes unresponsive and looking at the log, hashrate drops severely, 34kH to 600H on RARQ and from 6kH to 100H on RxL. Also, looking at the task manager, this happens : https://imgur.com/a/RXbWn32

Happens absolutely randomly without any observable pattern, i've been using XMRigCC 2.2.0 fork then switched to XMRig 5.3.0, it may go good without an issue for a week then all of sudden several occurrences in a row in the span of a few hours. Three times this morning already after a week of good operation after i've switched to XMRig for example.

My specs : Windows 10 1909 x64, Ryzen 7 3700X, 2x8GB 3600MHz 18CL, MSI B450 GP latest UEFI some OC present on CPU and RAM but i've tried to disable it without an effect.

No indications of anything wrong in the log besides dropping hashrate. Config are pretty standard, i've just edited in my pool configuration without touching anything else. And XMRigCC currently doesn't use recent AMD related optimizations so if anything it's the some older code responsive for this.

Link to issue on XMRigCC tracker : https://github.com/Bendr0id/xmrigCC/issues/285

# Discussion History
## SChernykh | 2019-12-31T09:22:24+00:00
The system spends 100% CPU time in kernel mode, this is really strange. Something is borked. I guess Windows is not really good at sustaining stability after a week of uptime.
Edit: or is it just a red background on CPU graph?

## electroape | 2019-12-31T09:55:00+00:00
Nope, it's miner going full-on kernel load, you're right. It's not happening exactly after a week of uptime, it can happen completely at random, it's just that after switching to XMRig it was working fine for a week and i thought it's a bug exclusive to XMRigCC, it's not.

## SChernykh | 2019-12-31T10:03:35+00:00
Can you try to set `"yield": false,` in config.json? If set to true, it calls a kernel function [SwitchToThread](https://docs.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-switchtothread) after each hash, so maybe this function goes crazy here.

## electroape | 2019-12-31T10:09:41+00:00
I'll try that but as i said, XMRigCC haven't merged recent unified miner stuff yet, including yield option and this happens on it too.

## SChernykh | 2019-12-31T10:11:21+00:00
yield was there since the beginning of time, only recent versions of XMRig can turn it off.

## electroape | 2019-12-31T10:13:25+00:00
Ok, testing with "yield": false now.

## electroape | 2019-12-31T13:09:46+00:00
Nope, still happened with yield: false. Any other thoughts ?

## SChernykh | 2019-12-31T13:11:52+00:00
When it happens, does it stay with low hashrate until you restart the miner or something else fixes hashrate too?

## electroape | 2019-12-31T13:20:15+00:00
Yes, as far as i see it will go like that indefinitely unless it'll restart mining after connection issue or if i restart it manually. Dev donate doesn't fix this tho. I'll try to manually trigger 'connection issue' by plugging off ethernet next time.
Here's the only occurrence of it fixing itself i've seen :

[2019-12-31 00:51:34.219] speed 10s/60s/15m 26.9 100.5 92.1 H/s max 7979.0 H/s
[2019-12-31 00:52:34.250] speed 10s/60s/15m n/a 98.0 93.5 H/s max 7979.0 H/s
[2019-12-31 00:53:34.276] speed 10s/60s/15m 6.8 99.9 94.4 H/s max 7979.0 H/s
[2019-12-31 00:54:34.308] speed 10s/60s/15m 16.7 95.9 94.6 H/s max 7979.0 H/s
[2019-12-31 00:55:34.337] speed 10s/60s/15m 7.2 98.9 95.4 H/s max 7979.0 H/s
[2019-12-31 00:56:34.367] speed 10s/60s/15m n/a 95.9 96.0 H/s max 7979.0 H/s
[2019-12-31 00:57:34.396] speed 10s/60s/15m 8.7 97.6 96.3 H/s max 7979.0 H/s
[2019-12-31 00:57:36.663]  net  new job from loki.herominers.com:10110 diff 15000 algo rx/loki height 435724
[2019-12-31 00:58:34.424] speed 10s/60s/15m 7.8 97.3 96.6 H/s max 7979.0 H/s
[2019-12-31 00:59:34.454] speed 10s/60s/15m n/a 95.9 96.6 H/s max 7979.0 H/s
[2019-12-31 01:00:34.480] speed 10s/60s/15m 14.4 96.5 96.7 H/s max 7979.0 H/s
[2019-12-31 01:01:34.506] speed 10s/60s/15m 15.3 96.3 96.6 H/s max 7979.0 H/s
[2019-12-31 01:02:15.910]  cpu  rejected (2033/1) diff 15000 "Unauthenticated" (133 ms)
[2019-12-31 01:02:15.911]  net  no active pools, stop mining
[2019-12-31 01:02:21.848]  net  use pool loki.herominers.com:10110  195.201.104.207
[2019-12-31 01:02:21.848]  net  new job from loki.herominers.com:10110 diff 15000 algo rx/loki height 435724
[2019-12-31 01:02:25.241]  cpu  accepted (2034/1) diff 15000 (127 ms)
[2019-12-31 01:02:25.384]  cpu  accepted (2035/1) diff 15000 (204 ms)
[2019-12-31 01:02:25.992]  cpu  accepted (2036/1) diff 15000 (129 ms)
[2019-12-31 01:02:28.131]  cpu  accepted (2037/1) diff 15000 (127 ms)
[2019-12-31 01:02:28.507]  cpu  accepted (2038/1) diff 15000 (132 ms)
[2019-12-31 01:02:29.330]  cpu  accepted (2039/1) diff 15000 (126 ms)
[2019-12-31 01:02:30.883]  cpu  accepted (2040/1) diff 15000 (126 ms)
[2019-12-31 01:02:34.528] speed 10s/60s/15m 6781.4 1657.8 190.3 H/s max 7979.0 H/s
[2019-12-31 01:02:35.299]  cpu  accepted (2041/1) diff 15000 (158 ms)
[2019-12-31 01:02:35.926]  cpu  accepted (2042/1) diff 15000 (133 ms)
[2019-12-31 01:02:38.315]  cpu  accepted (2043/1) diff 15000 (136 ms)
[2019-12-31 01:02:40.391]  net  new job from loki.herominers.com:10110 diff 30000 algo rx/loki height 435724

## electroape | 2019-12-31T14:51:38+00:00
I found the culprit, it's RunFullMemoryDiagnostic scheduled task, apparently it triggers when PC isn't used for a hour (even though it have triggered early, that's weird), no log entries if it even found any errors and MemTest86 doesn't show anything too but if i run it manually it'll break miner after a minute or so, i found it when noticed that there's taskhostw process consuming ~8% of CPU time when miner were just borked. I've disabled this task to see if it helps.
@Bendr0id

## electroape | 2019-12-31T15:02:58+00:00
I have a lot of Intel miners tho and none of them showed signs of this issue so i think it's safe to assume that it's AMD exclusive problem. I have one more AMD miner and it doesn't show signs of this issue either, but it's on 1607 build i think so maybe there's some issue with AMD-related memory\CPU scheduler code in newer builds (at least in 1909).

## SChernykh | 2019-12-31T15:05:32+00:00
I think it's related to Memory Compression in Windows 10, it should be turned off for better performance: https://superuser.com/questions/1000485/how-to-disable-windows-10-memory-compression

## x151973 | 2020-01-02T02:48:15+00:00
Try false/true two msr lines in config.json(need reboot after doing or resume) or enable/disable cache in bios to see if any relationship

# Action History
- Created by: electroape | 2019-12-31T06:57:11+00:00
- Closed at: 2021-04-12T15:06:30+00:00
