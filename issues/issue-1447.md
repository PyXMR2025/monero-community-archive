---
title: How to optimize configuration
source_url: https://github.com/xmrig/xmrig/issues/1447
author: septuig
assignees: []
labels:
- question
created_at: '2019-12-19T14:04:38+00:00'
updated_at: '2020-08-28T16:42:42+00:00'
type: issue
status: closed
closed_at: '2020-08-28T16:42:42+00:00'
---

# Original Description
I found CPU usage only 60% and hashrate 8.2k h/s, how to optimize configuration to get more hashrate? Whether need to config the parameter of "affinity" or/and "threads"?  thank you very much!

CPU: intel 2 x E5-2680v2
Memory: 16G
OS: Win10 64x
xmrig:5.3.0

config.json:
-----------------------
 "randomx": {
        "init": -1,
        "mode": "auto",
        "1gb-pages": false,
        "wrmsr": true,
        "numa": true
    },
    "cpu": {
        "enabled": true,
        "huge-pages": true,
        "hw-aes": null,
        "priority": null,
        "memory-pool": false,
        "yield": true,
        "asm": true,
------------------------------------------------
![image](https://user-images.githubusercontent.com/38321812/71179550-6061de00-22ab-11ea-8f66-866c48e09dc4.png)



# Discussion History
## pawelantczak | 2019-12-19T19:21:15+00:00
Your setup seems optimal (20 threads in total). The only missing thing could be 1gb huge pages. Affinity doesn't seem to do anything in my case (Debian). Personally I was getting 7.5k with two 2695 v2 (12 cores) but with slow memory.

## kio3i0j9024vkoenio | 2019-12-20T16:20:40+00:00
You are limited to only mining on the 10 real core in each Xeon E5-2680 v2.

RandomX requires 256kb of L2 per thread and the Xeon E5-2680 v2 only has Level 2 cache size: 10x 256 KB 8-way set associative caches.

See here: http://www.cpu-world.com/CPUs/Xeon/Intel-Xeon%20E5-2680%20v2.html

So XMRig using 20 threads is spot on.

The reason that you are seeing the 60% usage percent is because hyper-threads are counted for the percent but cannot be used for mining as they lack the 256 kb L2.

Total threads for 2x Xeon E5-2680 v2 is 20 real cores + 20 HT cores or 40 threads total. 

If you look at the task manager you should see that XMRig is using 50% of the threads 20 / 40 = 50%

The other 10% usage you see should be other tasks running.


## septuig | 2019-12-24T13:36:03+00:00
Thank you.

How to enable 1GB pages?  already set { "1gb-pages": ture} , but not worked. How to config "wrmsr" for my miner with 5.4.0?

# Action History
- Created by: septuig | 2019-12-19T14:04:38+00:00
- Closed at: 2020-08-28T16:42:42+00:00
