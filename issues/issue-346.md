---
title: Should I active Huge Pages?
source_url: https://github.com/xmrig/xmrig/issues/346
author: PipeDeveloper
assignees: []
labels:
- question
created_at: '2018-01-17T16:29:43+00:00'
updated_at: '2018-11-05T12:36:19+00:00'
type: issue
status: closed
closed_at: '2018-11-05T12:36:19+00:00'
---

# Original Description
Hello.

I just want to know if its recomended to active huge pages or use any specific configuration for this setting.

 * VERSIONS:     XMRig/2.4.4 libuv/1.8.0 gcc/5.4.0
 * HUGE PAGES:   available, disabled
 * CPU:          Intel(R) Xeon(R) CPU E5-2697A v4 @ 2.60GHz (3) x64 AES-NI
 * CPU L2/L3:    2.2 MB/120.0 MB
 * THREADS:      3, cryptonight, av=1, donate=1%
 * POOL #1:      pool.supportxmr.com:3333
 * API PORT:     8080
 * COMMANDS:     hashrate, pause, resume

already im using 3 THREADS and getting about 130-160H/s but just in case that i can improve a little more the performance.

Already i tested hugepages with 128 but i lower the hashrate to 20-110 H/s

# Discussion History
## NmxMilk | 2018-01-27T16:15:38+00:00
LOL, you have a beast there and you only get 160 H/S out of it !
Before trying huge pages, which might give you 5 to 10% improvement, you should push your thread count to 16 (per cpu) and check your cpu affinity.
You should be getting at least 600H/S out of each cpu and you seam to have 3 of them !


## PipeDeveloper | 2018-01-27T16:58:43+00:00
Thanks for the reply

Its a cloud server and i hired a plan of 3CPUs dedicated. I cant use more. Huge pages also decrease a little bit the performance on this case

## vekunz | 2018-01-28T22:57:20+00:00
Is there a way, to enable huge pages manually? In my case huge pages are randomly sometimes enabled and sometimes disabled. But if huge pages are enabled, I have a bit more hashes (~180H/s instead of ~160H/s).

## Pythonic-Rainbow | 2018-05-19T13:18:23+00:00
Why is this even an issue?
anyways mmy xmrig says hugefile is unavailable. How can i enable?

## renatocamargo | 2018-05-20T02:32:11+00:00
@Pythonic-Rainbow you can do it by changing the number of huge pages (vm.nr_hugepages) in the /etc/sysctl.conf on Linux OS.

# Action History
- Created by: PipeDeveloper | 2018-01-17T16:29:43+00:00
- Closed at: 2018-11-05T12:36:19+00:00
