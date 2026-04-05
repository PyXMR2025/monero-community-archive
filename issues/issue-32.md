---
title: 'what is teh  * HUGE PAGES:   available, disabled??'
source_url: https://github.com/xmrig/xmrig/issues/32
author: Allin1920
assignees: []
labels: []
created_at: '2017-07-09T01:46:13+00:00'
updated_at: '2017-07-18T19:01:16+00:00'
type: issue
status: closed
closed_at: '2017-07-18T19:01:16+00:00'
---

# Original Description
I'm at VM is disabled
but ,
I'm on my computer is enabled
* CPU:          Intel(R) Xeon(R) CPU E3-1231 v3 @ 3.40GHz (1) x64 AES-NI
Why is that?
Sometimes my computer runs on * CPU L2/L3: 1 MB/8.0 MB
Sometimes my computer runs on * CPU L2/L3: 2 MB/8.0 MB
my L2 why is 1M?

# Discussion History
## Allin1920 | 2017-07-09T01:48:28+00:00
my vm is  restart！
my computer is restart!
Can you speed up without restarting?

## xmrig | 2017-07-09T05:27:05+00:00
disabled mean huge pages fail to allocate you need reboot your computer and after that start miner. After some time running Windows it always fail, because of memory fragmentation and many other reasons.

If you use Linux you can preallocate huge pages `sudo sysctl -w vm.nr_hugepages=5` or bigger value.

I know about cache detection issue, I use libcpuid, there some heuristic to detect total L2 size, especially in VM environment it can fail, but in this case it cosmetic issue because L3 size detected correctly and also if you manually specify thread count detected cache size doesn't matter too. 
Thank you.

## Allin1920 | 2017-07-09T09:32:31+00:00
thank you.
and..
I closed the xmrig for a while
* HUGE, PAGES:, available, disabled
Why?

## xmrig | 2017-07-09T09:48:38+00:00
#25 
hugepages tricky thing highly depends on system load, it can be successfully allocated after weeks of uptime (idle system used only for mining) or failed after few hours on actively used machine.

## Allin1920 | 2017-07-11T01:45:38+00:00
Can you tell me why my windows has been restarted?
* HUGE, PAGES:, unavailable, disabled
”unavailable“
my windows  no vm

## Allin1920 | 2017-07-11T02:33:58+00:00
disable UAC is ok。
thanks.

## Allin1920 | 2017-07-11T02:46:10+00:00
 * HUGE PAGES:   available, enabled
 * CPU:          Intel(R) Xeon(R) CPU E5-2620 v2 @ 2.10GHz (2) x64 AES-NI
 * CPU L2/L3:    6.0 MB/30.0 MB
[2017-07-11 10:44:39] speed 2.5s/60s/15m 18.3 105.4 n/a H/s max: 54.1 H/s
[2017-07-11 10:44:40] accepted (12/0) diff 2010 (217 ms)

oh my god...I don't know why.

## xmrig | 2017-07-11T08:15:06+00:00
Oh... how? do you system do other CPU/cache intensive tasks? like I don't know maybe encoding video, because it crazy low values.

Disable UAC is bad, just confirm UAC prompt, disabling make your system much more vulnerable.

# Action History
- Created by: Allin1920 | 2017-07-09T01:46:13+00:00
- Closed at: 2017-07-18T19:01:16+00:00
