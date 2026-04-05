---
title: hashrate slowing down for a few seconds every minute on ubuntu server
source_url: https://github.com/xmrig/xmrig/issues/3061
author: Proulx-S
assignees: []
labels: []
created_at: '2022-06-01T05:13:04+00:00'
updated_at: '2022-06-02T23:02:38+00:00'
type: issue
status: closed
closed_at: '2022-06-02T23:02:37+00:00'
---

# Original Description
Every minute or so, hashrate is slowing down for a few seconds then rise up to normal.

To minimize interference from other OS processes, I run the miner within a headless ubuntu server that I boot from a usb on my desktop machine.

Huge pages are fine.
1gb pages don't change anything.
MSR thing is fine.

Could it have something to do with my 8core/16thread intel processor? Though, from the third line from the bottom of the screenshot below, it looks like the miner is correctly going for 8 threads.

Any help would be appreciated. Thanks!

<img width="871" alt="Capture d’écran 2022-06-01 050708" src="https://user-images.githubusercontent.com/68520323/171331928-62c60d1c-6e1c-4b78-b8eb-ac834a2941b8.png">

# Discussion History
## Proulx-S | 2022-06-01T05:21:17+00:00
oups, I am ralizing now that the screenshot I posted does not come from the miner that shows the issue. It comes from the miner running on the same machine but under windows 11 booted from the internal ssd drive. But I did not notice any difference in these messages from the miner whether it runs within windows or ubuntu.

btw, under windows 11, the miner does not show the issue: hashrate is lower but stable over time.

## Proulx-S | 2022-06-02T04:23:49+00:00
Now the screen from the actual OS that shows the issue.
![Screen Shot 2022-06-02 at 12 07 21 AM](https://user-images.githubusercontent.com/68520323/171551092-d7e48d5e-4b06-4ba4-97a4-222c31c7128f.png)


Did some more investigating with htop.

First, htop shows 8 of 16 threads are used. So I guess this is good.
Those 8 threads are at 100% and don't drop when hashrate drops.
Same thing for memory load, it stays stable despite hashrate drops.
The only thing that seem to go down with hashrate so far is fan speed...

I don't get it. Could it really be just my linux fan manager that sucks: the fan first slows for no good reason, temperature rises and hashrate drops?

To late at night to investigate that fan. Any insight would be appreciated :-)

## SChernykh | 2022-06-02T06:39:40+00:00
> Every minute or so, hashrate is slowing down for a few seconds then rise up to normal.

> Could it really be just my linux fan manager that sucks: the fan first slows for no good reason, temperature rises and hashrate drops?

So is it the hashrate or the CPU cooler?

## Proulx-S | 2022-06-02T15:24:32+00:00
Both. Hashrate and cpu fan dip down and rise back up at the same time, while the rest (cpu and memory load) remains stable.

## Proulx-S | 2022-06-02T23:02:37+00:00
Seems the problem was the fan. I installed some package (i8kutils) to force it to stay at max and no more hashrate dip.

# Action History
- Created by: Proulx-S | 2022-06-01T05:13:04+00:00
- Closed at: 2022-06-02T23:02:37+00:00
