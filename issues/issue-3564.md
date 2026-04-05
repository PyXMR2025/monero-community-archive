---
title: RandomX does not use all threads
source_url: https://github.com/xmrig/xmrig/issues/3564
author: ehsaaan-tu
assignees: []
labels:
- question
created_at: '2024-10-20T12:21:14+00:00'
updated_at: '2025-06-16T19:23:31+00:00'
type: issue
status: closed
closed_at: '2025-06-16T19:23:31+00:00'
---

# Original Description
Hi, 
First of All I appreciate your effort, work and support to opensource community.

I am just trying out Xmrig with RandomX protocol, your benchmarking scores are way too high than I could get using Xeon E5 2650 v4.
Xmrig does not use more than 32 threads. If I try to use more than 32 threads, hashrate start going down. 

I have tried all configurations settings you have advised in RandomX Optimization Guide at: 
https://xmrig.com/docs/miner/randomx-optimization-guide

Lock Memory Pages for user is already done in group policy.
Running Xmrig as Administrator in Windows.

Is there other settings I am missing??

I appreciate your you support in advance.

# Discussion History
## SChernykh | 2024-10-20T13:18:05+00:00
RandomX requires 2 MB L3 cache per thread. If you run more threads, hashrate will drop. The optimal config for Xeon E5 2650 v4 is 12 threads per CPU. Benchmark scores show dual CPU systems at the top, you need to take this into account.

## ehsaaan-tu | 2024-10-20T14:50:34+00:00
It has 12 cores per CPU and 2 threads per core which makes 24 threads per cpu, In case of 2 CPU's 48 threads and 24 cores. It has 30MB of L3 cache..

Do you mean RandomX uses 2MB of L# cache per core as there are 2 threads per core. If it's 2MB per core then theoretically it should give us maximum performance @30 threads, while on my machine, I am getting better @32 threads.

I appreciate your reply.

Regards

## SChernykh | 2024-10-20T21:51:50+00:00
What is exactly the specs of your machine? 1 or 2 CPUs? What hashrate do you get?

## ehsaaan-tu | 2024-10-21T03:27:42+00:00
xeon 2650 v4, 2 cpu's, having 24 cores and 48 threads.  64GB RAM, Windows 10 OS. 
 using 36 threads now (means 18 cores), getting 5125 - 5005 H/s

## SChernykh | 2024-10-21T06:30:14+00:00
Please share the config you're using (you can edit out the XMR address and pool), and a screenshot of XMRig window right after start - I need to see if it prints any warning and errors. One thread per core (24 threads in total for 2 CPUs) is optimal in your case, just check top benchmarks - they all use 24 threads.

## xmrig | 2024-10-21T09:34:47+00:00
These CPUs are limited by the size of the L2 cache, which makes 24 threads for 2 CPUs optimal. An extra L3 cache provides no benefit. Misspopulated memory also hurts hashrate. A config file and a screenshot, as earlier requested, contain almost any answer.
Thank you.

## ehsaaan-tu | 2024-10-29T13:50:40+00:00
I apologize for delayed response, I figured it out, while using randomX, if I use option --threads in command line or try to use it in config.json file, hashrate suffers upto 50%, If I just let xmrig choose optimum number of cores I achieved exactly same hashrate you guys have in benhmarks. I got 2 e-5 2650 v4 cpu's 30MB + 30MB L3 cache totals to 60MB. I thought I could use all 24 cores/48 threads to double my hashrate but that didn't work. 

by default, xmrig is utilizing 24 threads and throughput is 10.7KH, while SRBminer never hit even 6KH with 24/32/36/46/ core settings.


# Action History
- Created by: ehsaaan-tu | 2024-10-20T12:21:14+00:00
- Closed at: 2025-06-16T19:23:31+00:00
