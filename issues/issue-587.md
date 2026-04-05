---
title: How can E7-8850 * 8 get a higher performance?
source_url: https://github.com/xmrig/xmrig/issues/587
author: zelasge
assignees: []
labels: []
created_at: '2018-04-26T16:10:09+00:00'
updated_at: '2018-05-07T17:19:40+00:00'
type: issue
status: closed
closed_at: '2018-05-07T17:19:40+00:00'
---

# Original Description
dear bro,
I have a server with 8 CPU--E7 8850, and the OS is CentOS 6.9,
1. If I use: ./xmrig  -o  ****  -u **** -p x -k  --donate-level 1 --max-cpu-usage 85 --cpu-priority 3, It shows below: 
 * VERSIONS:     XMRig/2.5.3 libuv/1.8.0 gcc/6.1.0
 * HUGE PAGES:   available, enabled
 * CPU:          Intel(R) Xeon(R) CPU E7-8850 v2 @ 2.30GHz (8) x64 AES-NI
 * CPU L2/L3:    192.0 MB/192.0 MB
 * THREADS:      96, cryptonight, av=1, donate=1%
 * POOL #1:      
 * COMMANDS:     hashrate, pause, resume
the speed is 2800H/s and the CPU utilization is 50%


2. If I set threads as 80, the speed is 3200H/s and the CPU utilization is 41%

3. If I set threads as 100, the speed is slower than 2800 and the  CPU utilization is 60%

4. If I open 2 terminal and run 2 same  progress like 48 threads + 48 threads , the sum of speed is 2800H/s

What is the best configuration to get more performance??
thanks in advance.

# Discussion History
## proton171717 | 2018-05-02T08:12:45+00:00
Hi,
I have similiar configurations with hp server 4 x E7-4830 and one server 4 x E7-8830
I tried most combinations with threads=48, 47...etc - no difference = 1304 h/s max
I tried to split xmrig at 4 command x 12 threads and the total hashes were the same = 4 xmrig x 341 h/s

So I coudnt find the best conf too :)

## zelasge | 2018-05-07T17:19:32+00:00
I tried a lot , finally find that just make the threads as default(automatically) and it works the best performance...

# Action History
- Created by: zelasge | 2018-04-26T16:10:09+00:00
- Closed at: 2018-05-07T17:19:40+00:00
