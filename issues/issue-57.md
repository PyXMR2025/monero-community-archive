---
title: Dual CPU Xeon E5-2620 v4
source_url: https://github.com/xmrig/xmrig/issues/57
author: tuta123
assignees: []
labels:
- NUMA
created_at: '2017-08-07T23:47:16+00:00'
updated_at: '2017-11-27T00:25:00+00:00'
type: issue
status: closed
closed_at: '2017-09-03T03:14:58+00:00'
---

# Original Description
2 CPUs with 8 cores (16 HT), and XMR only ever sees 1 CPU. L3 cache is 20MB per CPU so I would expect it to mine 20 threads across both CPUS, but it defaults to 10 threads.

Tried the GCC binary, MS binary, both 64 bit. OS is Windows server 2016.

Am I doing something stupid?

 * VERSIONS:     XMRig/2.2.1 libuv/1.13.1 MSVC/2017
 * HUGE PAGES:   available, enabled
 * CPU:          Intel(R) Xeon(R) CPU E5-2620 v4 @ 2.10GHz (1) x64 AES-NI
 * CPU L2/L3:    2.0 MB/20.0 MB
 * THREADS:      10, cryptonight, av=1, donate=5%

Thanks.

# Discussion History
## xmrig | 2017-08-08T00:07:27+00:00
You right only one CPU detected, but you can manually specify right count of threads `-t 20` or `threads` option in config file. Also you can specify option `--cpu-affinity 0xAEAEAEAE` or `"cpu-affinity": "0xAEAEAEAE"` for config.
Thank you.

## tuta123 | 2017-08-08T00:33:12+00:00
Thanks for the response. If I run it without the -t 20 or cpu affinity setting, i get consistent 400h/s. With the t=20 and CPU affinity, hash drops to 280h/s-320h/s.

Oddly though....if i launch and leave everything auto, it settles to 400h/s. If I then launch a second instance with everything set to auto, there is a 70% chance that both instances settle at 370h/s (total around 750h/s). The rest of the time the second instance settles at around 40h/s

Anyway, any easy way to remove the lottery from that second instance?

## tuta123 | 2017-08-08T08:35:23+00:00
OK did some testing against a few other dual proc machines I have access to, and with xmr stak I get consistent 800h/s. The only way to get close to this with xmrig is to launch two instances, I cannot get anywhere close to the stak figure with a single instance. Its like it just doesn't see the second CPU.

Note this is only on dual proc boxes, the software absolutely rules on single socket devices.

Thanks.

## xmrig | 2017-08-08T10:21:04+00:00
I think you system is not just 2 sockets, it 2 NUMA nodes, each contains single CPU.
I have 2 sockets system and I know people who run xmrig on 4 sockets systems, but it not a NUMA.

1. Can you show me `cpu_threads_conf` from stak
2. Please download hwloc-win64-build-1.11.7.zip from this page https://www.open-mpi.org/software/hwloc/v1.11/ and run lstopo-win.exe

It helps figure it out.

## tuta123 | 2017-08-08T14:06:18+00:00
You are of course right, it is two NUMA nodes. I assume I could start one instance with "start /node 0" and the other with "start /node 1" to force the binding to the two NUMA nodes. What puzzles me is another server with 2 x X5660 processors which the software picks up has having 2 CPUs even though it also has 2 NUMA nodes. In this instance it correctly balances the threads (6 per cpu using the 24MB L3 cache). FYI I only got the chance to test that system this afternoon.

Here's the stak config

 { "low_power_mode" : false, "no_prefetch" : true, "affine_to_cpu" : 0 },
    { "low_power_mode" : false, "no_prefetch" : true, "affine_to_cpu" : 2 },
    { "low_power_mode" : false, "no_prefetch" : true, "affine_to_cpu" : 4 },
    { "low_power_mode" : false, "no_prefetch" : true, "affine_to_cpu" : 6 },
    { "low_power_mode" : false, "no_prefetch" : true, "affine_to_cpu" : 8 },
    { "low_power_mode" : false, "no_prefetch" : true, "affine_to_cpu" : 10 },
    { "low_power_mode" : false, "no_prefetch" : true, "affine_to_cpu" : 12 },
    { "low_power_mode" : false, "no_prefetch" : true, "affine_to_cpu" : 14 },
    { "low_power_mode" : false, "no_prefetch" : true, "affine_to_cpu" : 1 },
    { "low_power_mode" : false, "no_prefetch" : true, "affine_to_cpu" : 3 },
    { "low_power_mode" : false, "no_prefetch" : true, "affine_to_cpu" : 64 },
    { "low_power_mode" : false, "no_prefetch" : true, "affine_to_cpu" : 66 },
    { "low_power_mode" : false, "no_prefetch" : true, "affine_to_cpu" : 68 },
    { "low_power_mode" : false, "no_prefetch" : true, "affine_to_cpu" : 70 },
    { "low_power_mode" : false, "no_prefetch" : true, "affine_to_cpu" : 72 },
    { "low_power_mode" : false, "no_prefetch" : true, "affine_to_cpu" : 74 },
    { "low_power_mode" : false, "no_prefetch" : true, "affine_to_cpu" : 76 },
    { "low_power_mode" : false, "no_prefetch" : true, "affine_to_cpu" : 78 },
    { "low_power_mode" : false, "no_prefetch" : true, "affine_to_cpu" : 65 },
    { "low_power_mode" : false, "no_prefetch" : true, "affine_to_cpu" : 67 },

and here is the output from the command above:

![image](https://user-images.githubusercontent.com/30814610/29075499-7d385dec-7c4a-11e7-90e2-815ca552f0dd.png)


## xmrig | 2017-08-08T14:26:04+00:00
I will add hwloc support in next versions, to many issues with libcpuid also will add optional per thread configuration like stak. Thank you.

## tuta123 | 2017-08-08T20:34:56+00:00
Many thanks, its running like a charm using "start /node 0" or "start /node 1" which is removing the earlier lottery and hashes are exceeding stak.

## hoangcao243 | 2017-08-29T23:46:17+00:00
could you please help me out? I'm having the same issue and don't know where to put the command " start /node 0" ?

I just realized that when I run 1 cmd i got 450 cpus load 55%, when i run 2 cmd cpus load at 100% but i have only 170hs each cmd? I'm setting the thread at 12. with affinity 0xFFFFFFFFFFFF

2x xeon 5650

## xmrig | 2017-09-03T03:14:58+00:00
Move all NUMA related issues to #86

## rjmoggach | 2017-11-09T20:00:55+00:00
same issue here - how do I configure second CPU on ubuntu 16.04 using config file?

# Action History
- Created by: tuta123 | 2017-08-07T23:47:16+00:00
- Closed at: 2017-09-03T03:14:58+00:00
