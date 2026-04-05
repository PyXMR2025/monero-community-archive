---
title: Hashrate drops significantly after several minutes of mining for no discernable
  reason
source_url: https://github.com/xmrig/xmrig/issues/2549
author: Velocity535
assignees: []
labels: []
created_at: '2021-08-21T01:42:08+00:00'
updated_at: '2021-08-23T16:19:12+00:00'
type: issue
status: closed
closed_at: '2021-08-23T16:19:12+00:00'
---

# Original Description
I seem to be having an issue with XMRig on my ryzen systems. When XMRig first starts mining, the hashrate is as expected for the CPU being used. However, after I step away from the PC for a little while, from a couple minutes to an hour, the hashrate drops significantly.

For example, my 5800X system hashes around 9500H/s, but not long after I notice that it drops all the way down to around 100H/s or usually even lower at ~60H/s.

Same problem on my 3950X system. Hashes around 18000H/s, soon after it will drop to double digits.

The CPU usage drops significantly and so does the temperature and the power usage.

I'm not using any special command line arguments, or OC'ing the CPU or RAM at all. The miner still seems to work fine, no crashing or anything out of the ordinary, just working at a much reduced rate. PC still works fine as well, no BSOD or anything of that nature.

Huge pages are enabled and MSR mod is applied properly.

As soon as I close XMRig and reopen it, the hashrate jumps back up to where it should be, but again soon after it drops a massive amount.

My intel systems do not exhibit this behavior, only my ryzen systems.

It happens on every single recent version of XMRig, all legitimate versions downloaded from this github page. I was looking too see if there is a watchdog function that auto-restarts XMRig if the hashrate drops below a certain level, but that does not seem to exist.

My 3950X system is running on Windows 10 21H1, and my 5800X system is running the latest beta of Windows 11. XMRig has been whitelisted in windows defender as well.

I've attached the XMRig console showing the moment it mines at a perfectly normal rate, but then randomly drops for no reason that I can determine.

![XMRig Hashrate Issue 5800X](https://user-images.githubusercontent.com/86106921/130306555-bd50868e-00e2-41ac-87ca-1a237861d5d6.png)


# Discussion History
## SChernykh | 2021-08-21T08:46:16+00:00
https://www.reddit.com/r/MoneroMining/comments/f18825/windows_10_tuning_guide_for_randomx_mining/
- Disable Memory Compression
- Disable RunFullMemoryDiagnostic task

## Velocity535 | 2021-08-23T13:57:33+00:00
> 
> 
> https://www.reddit.com/r/MoneroMining/comments/f18825/windows_10_tuning_guide_for_randomx_mining/
> 
>     * Disable Memory Compression
> 
>     * Disable RunFullMemoryDiagnostic task

Did both of those tasks, been mining for about 24 hours now without any hashrate drop. Hopefully the issue is fixed. Appreciate the help!

# Action History
- Created by: Velocity535 | 2021-08-21T01:42:08+00:00
- Closed at: 2021-08-23T16:19:12+00:00
