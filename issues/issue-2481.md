---
title: Hash Rate Drop, Processor Core and Thread shown are incorrect
source_url: https://github.com/xmrig/xmrig/issues/2481
author: sewell8664
assignees: []
labels: []
created_at: '2021-07-09T18:15:25+00:00'
updated_at: '2021-07-10T20:59:19+00:00'
type: issue
status: closed
closed_at: '2021-07-10T02:25:44+00:00'
---

# Original Description
![Capture](https://user-images.githubusercontent.com/87204276/125119899-4d7c5c00-e124-11eb-88b4-2b0465adeaaf.PNG)

Th hash-rate drop significantly. Only 8 threads have been detected, there are 32 threads for AMD 3950X.

# Discussion History
## SChernykh | 2021-07-09T18:21:09+00:00
This is cn-heavy algorithm, number of threads is correct for it. Also check what Task Manager shows and your BIOS settings, maybe you disabled half of the cores.

## Spudz76 | 2021-07-09T20:37:35+00:00
Heavy uses 4MB cache per thread so it is maxing out at 8*4=32MB cache total

Detection may be bios or kernel options limiting cores.  But even if it said `16c/32t` it would still only do 8 threads due to cache.

Also BIOS may need upgrade if CPU is newer than when mobo initial release (or current BIOS version).

Support site [here for hardware rev 1.0 boards](https://www.gigabyte.com/Motherboard/X570-AORUS-MASTER-rev-10/support#support-cpu) shows 3950X needs BIOS rev F4 minimum.

For [rev 1.1/1.2 boards](https://www.gigabyte.com/Motherboard/X570-AORUS-MASTER-rev-11-12/support#support-cpu), 3950X also needs rev F4 minimum

## SChernykh | 2021-07-09T20:45:28+00:00
To be fair, it should be doing 16 cn-heavy threads on 3950X because it should have 64 MB cache.

## Spudz76 | 2021-07-09T20:47:25+00:00
Did not notice cache was halved too, so there would be room for 16 threads once debugged.

## sewell8664 | 2021-07-10T02:25:12+00:00
![image](https://user-images.githubusercontent.com/87204276/125149028-06fd2080-e169-11eb-9f0a-c5ebe11313ac.png)

The issue was resolved. Thank you so much guys!

## Valtsuh | 2021-07-10T16:29:54+00:00
What's a good average(most users) hashrate to compare to, per thread? Bottom / top?

## Spudz76 | 2021-07-10T18:14:31+00:00
@Valtsuh the total hashrate, 1380.3H/s

Also of note this is `cn-heavy/xhv` not `rx/0` and hashrates do not cross-compare across algos.

## Valtsuh | 2021-07-10T20:58:58+00:00
> @Valtsuh the total hashrate, 1380.3H/s
> 
> Also of note this is `cn-heavy/xhv` not `rx/0` and hashrates do not cross-compare across algos.

Okay, I'm jus figuring out if my hashrate is slow, fast or somewhere in the middle. 

rx (not /0 if it makes a difference) jumps somewhere between 100-350 / thread, topping at around 1200ish 3-4 threaded.

# Action History
- Created by: sewell8664 | 2021-07-09T18:15:25+00:00
- Closed at: 2021-07-10T02:25:44+00:00
