---
title: How to make sure both processors are being used
source_url: https://github.com/xmrig/xmrig/issues/491
author: mirrormirage0
assignees: []
labels:
- NUMA
created_at: '2018-04-02T06:48:56+00:00'
updated_at: '2019-08-02T12:40:00+00:00'
type: issue
status: closed
closed_at: '2019-08-02T12:40:00+00:00'
---

# Original Description
I have an HP WX8600 workstation with 2 XEON X5450 processors running at 3.40 GHz
When I start xmrig using Awesome miner, I see that it uses **8 Threads** 
I am getting a hash rate of **172 H/s** for Cryptonight Algorithm.
There are 2 Processors in the workstation, and each XEON X5450 has 12 MB cache

One issue I find is that the processor does not support AES.
1) Is this the reason why the hashrate is low?
2) How do I ensure that both processors are being used? 

# Discussion History
## NmxMilk | 2018-04-10T09:03:28+00:00
These are quad cores. So max is 8 threads.
Intel's site indicates 3.00 GHz and not 3.40 GHz!
Try with just 1 thread, I guess that would give about 30 H/S (since no AES).
You can in this way evaluate the max H/S with 8 threads.
Don't be astonished if you get less. Maybe best perf you get will be with 6 or 7 threads.




## xmrig | 2019-07-29T02:16:14+00:00
If this issue still actual, please check v2.99.2-beta release #1077.
Thank you.

# Action History
- Created by: mirrormirage0 | 2018-04-02T06:48:56+00:00
- Closed at: 2019-08-02T12:40:00+00:00
