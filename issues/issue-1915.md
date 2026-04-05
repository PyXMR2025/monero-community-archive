---
title: 'BUG: Unable to allocate huge pages to 100% on relaunch after certain time
  has elapsed.'
source_url: https://github.com/xmrig/xmrig/issues/1915
author: kimpurcell
assignees: []
labels: []
created_at: '2020-10-25T22:09:06+00:00'
updated_at: '2023-12-01T08:44:03+00:00'
type: issue
status: closed
closed_at: '2021-04-12T14:44:16+00:00'
---

# Original Description
On the initial launch, xmrig reports that it's allocated 100% of huge pages. 
After a few hours, I've decided to close the xmrig application for gaming. After gaming, when I try relaunching xmrig again, it would never be able to allocate 100%. Here's what I see:

 randomx  allocated 2336 MB (2080+256) huge pages 11% 128/1168 +JIT (1110 ms)

Why is that? I closed everything, all the applications and just run xmrig.exe again and it's still not able to use 100% of the huge pages.

# Discussion History
## kimpurcell | 2020-10-25T22:10:01+00:00
I had to reboot in order to fix this. After a reboot, xmrig is able to run with huge pages at 100% again.

## SChernykh | 2020-10-26T08:29:24+00:00
Memory gets fragmented with time on Windows and it gets impossible to allocate dataset using large pages. Only reboot fixes it.

## Saikatsaha1996 | 2020-10-26T08:39:31+00:00
> Memory gets fragmented with time on Windows and it gets impossible to allocate dataset using large pages. Only reboot fixes it.

![Screenshot_20201026-140736.png](https://user-images.githubusercontent.com/72664192/97150823-b25d7500-1794-11eb-9466-b6d78f103011.png)

Same problem with me..
I reboot my mobile after reboot when i start not huge page not available..

How can I solve this?
Help me

## Lonnegan | 2020-10-26T15:08:07+00:00
@Saikatsaha1996 Look at the line "MEMORY" in the output of your xmrig. RAM is nearly full, so no chance for the miner so allocate huge memory areas in a row to use huge pages.

## Saikatsaha1996 | 2020-10-26T16:00:34+00:00
> @Saikatsaha1996 Look at the line "MEMORY" in the output of your xmrig. RAM is nearly full, so no chance for the miner so allocate huge memory areas in a row to use huge pages.

Ohhh thank you...
So its depending on ram r8?

## Lonnegan | 2020-10-26T16:14:36+00:00
Yes, there must be enough free RAM in a row to be allocatable by the miner to use huge pages. If the device has already ran for a while and the free RAM is fragmented, huge pages are not or only partially possible.

## Saikatsaha1996 | 2020-10-26T16:30:47+00:00
> Yes, there must be enough free RAM in a row to be allocatable by the miner to use huge pages. If the device has already ran for a while and the free RAM is fragmented, huge pages are not or only partially possible.

Thank you so much i have one more problem with my pc can you help me?
In my pc i have windows 10
3.3 ghz Intel I3  6th generation processor
4gb ddr4 ram
When i start with windows xmrig exe .. ita haven't any issues..
But when i run with ubuntu not responding...!
[IMG_20201025_034415.jpg](https://user-images.githubusercontent.com/72664192/97200137-d5a91400-17d6-11eb-8c2b-2f873a1300bb.jpg)

## Lonnegan | 2020-10-27T21:25:49+00:00
Sure you've downloaded the right binary for your Ubuntu?

## Saikatsaha1996 | 2020-10-27T22:04:05+00:00
> Sure you've downloaded the right binary for your Ubuntu?

Can you explain it? Actually I am new

## kimpurcell | 2020-11-01T03:54:34+00:00
> Memory gets fragmented with time on Windows and it gets impossible to allocate dataset using large pages. Only reboot fixes it.

So if I run a memory defragmenter like Wise Memory Optimizer, it should allow huge pages again right? https://www.wisecleaner.com/wise-memory-optimizer.html

## kimpurcell | 2020-11-01T04:02:28+00:00
Just tried defragging the memory. Had 20GB of free ram, but still can't get 100% huge pages.

## SChernykh | 2020-11-01T09:58:39+00:00
There's no such thing as memory defragmentation on OS level. Wise Memory Optimizer is scam - it just frees some memory at best, not defragments it. You have to reboot Windows.

## kimpurcell | 2020-11-01T15:10:12+00:00
Thanks, need to uninstall that, didn’t do anything but eat up memory and release it.

## nono71x | 2023-12-01T08:44:02+00:00
![Capture d’écran (93)](https://github.com/xmrig/xmrig/assets/112335542/8960dd5b-abac-45c8-a241-a0efb45a63d2)
the same for me and it's painful. Just restart it once and I constantly have 2 bugs, HUGE PAGES 0% and WinRing service already existing. Restarting the PC every time you restart XMRig is an abberation

# Action History
- Created by: kimpurcell | 2020-10-25T22:09:06+00:00
- Closed at: 2021-04-12T14:44:16+00:00
