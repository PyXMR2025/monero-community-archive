---
title: Ryzen 9 new 9900 - only 12 threads works, wrong profile
source_url: https://github.com/xmrig/xmrig/issues/3556
author: Maythecoffee
assignees: []
labels: []
created_at: '2024-09-22T09:30:21+00:00'
updated_at: '2025-06-16T19:41:33+00:00'
type: issue
status: closed
closed_at: '2025-06-16T19:41:33+00:00'
---

# Original Description
**Describe the bug**
only 12 threads are working for RX algo (XMR)

**To Reproduce**
just run it

**Expected behavior**
Should be 24
like this
"rx": [0,12,1,13,2,14,3,15,14,16,5,17,6,18,7,19,8,20,9,21,10,22,11,23],
**Required data**
6.22
 
**Additional context**
Add any other context about the problem here.


# Discussion History
## SChernykh | 2024-09-22T17:45:54+00:00
This is fixed in the dev branch. The fix will be included in the v6.22.1 release.

## Maythecoffee | 2024-09-22T18:07:40+00:00
thnx

## Maythecoffee | 2024-10-01T16:30:58+00:00
> This is fixed in the dev branch. The fix will be included in the v6.22.1 release.

Could you please say wen?
I am asking couse using dual mining with QUBIC i need to run XMRIG via cmd command like 
xmrig -o pool -p %WORKER_NAME% -u wallet -a rx/0 -k, and i have no idea how to fix rx:[x] usind string command in that case
and cfg json updated every time as new so i can not just fix it within json, the only option to know string cmd command or waiting for 6.22.1 release(

## SChernykh | 2024-10-01T16:39:02+00:00
You can just add `-t 24` to the command line, and xmrig will run 24 threads on your 9900.

## Maythecoffee | 2024-10-01T17:03:49+00:00
> You can just add `-t 24` to the command line, and xmrig will run 24 threads on your 9900.

ups, I thought I'd already tried this method, but yes it is simple and it is working)  thank you.

# Action History
- Created by: Maythecoffee | 2024-09-22T09:30:21+00:00
- Closed at: 2025-06-16T19:41:33+00:00
