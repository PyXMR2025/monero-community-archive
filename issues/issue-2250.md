---
title: Very low hashrate, unstable connection, since 6.10 on win10 with Ryzen 3600
source_url: https://github.com/xmrig/xmrig/issues/2250
author: thaneb
assignees: []
labels: []
created_at: '2021-04-09T07:08:45+00:00'
updated_at: '2021-04-09T08:29:15+00:00'
type: issue
status: closed
closed_at: '2021-04-09T08:29:15+00:00'
---

# Original Description
My hashrate dropped to 780h/s since 6.10 (and 6.11 still same) with an incredible number of "connection closed by server" on my mining pc (nanopool, configured with the xmrig wizard).
I disable PBO in my BIOS (in case of) , and I followed guides often gave here.
I just came back to xmrig 6.09 and my 6700h/s on average is back !
Any idea ?

# Discussion History
## SChernykh | 2021-04-09T07:15:24+00:00
To check if it's a pool or miner problem:
- Try another pool
- Try to run embedded benchmark

## thaneb | 2021-04-09T08:14:46+00:00
I already tried with the included miner pool. Bat included, it was working well, so it seems to be an issue between last 2 releases of xmrig and nanopool, anyway, I posted here so maybe someone else could see "he's not alone, and the solution is to use an older release" 

## SChernykh | 2021-04-09T08:20:54+00:00
xmrig 6.10 was released more than a month ago and I didn't hear about such problems with nanopool. I'm also testing xmrig 6.11.1 + nanopool right now and I don't have any problems.

## thaneb | 2021-04-09T08:29:15+00:00
so much weird, i updated the xmrig.exe and the winring0x64.sys, and now it seems to work well...

# Action History
- Created by: thaneb | 2021-04-09T07:08:45+00:00
- Closed at: 2021-04-09T08:29:15+00:00
