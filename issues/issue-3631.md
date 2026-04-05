---
title: Hashrate drops to 50% after idling for awhile...
source_url: https://github.com/xmrig/xmrig/issues/3631
author: alanhasgari
assignees: []
labels: []
created_at: '2025-02-05T20:15:28+00:00'
updated_at: '2025-02-06T22:45:12+00:00'
type: issue
status: closed
closed_at: '2025-02-06T03:57:16+00:00'
---

# Original Description
Question: does anyone else experience a 50% hash rate drop after the system has been running for a while? I leave my system running and only use it once a week or so, but I monitor the hashrate via the pool's website

Running latest XMrig on Windows 11 24h2, with Ryzen 8600G and 64GB DDR5 6000, and I didn't have this problem with previous versions of xmrig. The CPU never reaches temps over 65°C

I'm not saying XMrig is the problem, but I need help troubleshooting.

I mine to supportxmr pool, fixed difficulty, the number of accepted shares doesn't fluctuate, BUT XMrig says my hashrate is 2600/s instead of 5300/s...

I'd appreciate some help...

# Discussion History
## SChernykh | 2025-02-05T21:26:53+00:00
Does hashrate drop after you restart XMRig? It can be because it fails to allocate huge pages.

## alanhasgari | 2025-02-05T21:31:15+00:00
> Does hashrate drop after you restart XMRig? It can be because it fails to allocate huge pages.

Restarting XMrig does nothing. Hashrate remains halved until system is restarted.

Huge pages fully allocated; 100% when first loaded, and hashrate drops after idling awhile. Restarting XMrig and still 100% allocated, but hashrate remains halved.

Only system restart corrects it.

## SChernykh | 2025-02-05T22:09:12+00:00
Check if anything else is using CPU when this happens.

## alanhasgari | 2025-02-05T22:17:34+00:00
> Check if anything else is using CPU when this happens.

CPU utilisation and temps remains constant; what about the CPU should I check?

## geekwilliams | 2025-02-05T22:26:45+00:00
I think he's asking you to check if there's any other process that starts during the time you see reduced performance.  That process (or processes) may be asking for resources that cause the performance impact you see. 

## SChernykh | 2025-02-05T22:29:02+00:00
There's no magic. Either something else starts using CPU, or Windows drops CPU frequency because of some power saving feature, or something else starts using GPU (8600G has integrated GPU). You should monitor other processes' CPU usage, and CPU speed in MHz on all cores.

## alanhasgari | 2025-02-05T22:30:36+00:00
> I think he's asking you to check if there's any other process that starts during the time you see reduced performance. That process (or processes) may be asking for resources that cause the performance impact you see.

I understand that, but many processes within windows start and stop frequently, but CPU utilisation never spikes; utilisation remains steady between 64% and 70%...

## alanhasgari | 2025-02-05T22:34:10+00:00
> There's no magic. Either something else starts using CPU, or Windows drops CPU frequency because of some power saving feature, or something else starts using GPU (8600G has integrated GPU). You should monitor other processes' CPU usage, and CPU speed in MHz on all cores.

I understand there no magic. Just had hoped someone had experiences similar to mine, and knew how to fix; as I mentioned, I had an older version of xmrig running that didn't have this 50% drop...

i might have to take another at the BIOS and see if I can set static timings and frequency instead of relying auto settings.

## alanhasgari | 2025-02-06T04:00:01+00:00
Issue found to be task scheduler ignoring pre-existing process and launching a second instance of XMrig. I tested with older version of xmrig and task scheduler doesn't launch second instance of it. I can only chalk it up to Windows task scheduler being dumb. Thanks for your help.

## geekwilliams | 2025-02-06T18:45:48+00:00
At my company we once had a crypto-jacker installed on a Unifi server with the log4j vulnerability.  The problem was the crypto-jacker was set to start a new instance of xmrig every 5 minutes via a cron job.  That server was useless to us and to the hacker because whoever it was took that approach lol.  

## alanhasgari | 2025-02-06T22:45:10+00:00
Yeah, I switched to using nssm for the scheduled task instead of XMrig directly; this gives me more control over the service, and prevents the issue of duplicate processes. Lesson learned.

# Action History
- Created by: alanhasgari | 2025-02-05T20:15:28+00:00
- Closed at: 2025-02-06T03:57:16+00:00
