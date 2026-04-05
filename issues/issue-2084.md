---
title: Unable to increase number of threads
source_url: https://github.com/xmrig/xmrig/issues/2084
author: aliiqbal1984
assignees: []
labels: []
created_at: '2021-02-05T20:27:44+00:00'
updated_at: '2021-04-12T14:16:59+00:00'
type: issue
status: closed
closed_at: '2021-04-12T14:16:59+00:00'
---

# Original Description
Hi I am having 20 core server with 60Mb L3 cache running the xmrig by default config file I get 20 core and 20 threads 

Can someone help how I can increase threads to 30 what changes will be needed in config file ? Please help.

# Discussion History
## Spudz76 | 2021-02-05T21:43:46+00:00
fake cores do not help rate, only real cores
you have 20 real cores?

what algorithm?

Run CN-Heavy and it will stop using all cores, but jam all cache full (60MB / 4MB scratchpad = 15 cores).
To fit that CPU model ideally you would need an algo with 3MB scratchpads, which do not exist.

## Lonnegan | 2021-02-05T22:45:26+00:00
Haven (XHV) should work perfectly on your CPU. It's even best for AMD Bulldozer: weak compute power but biiiig caches!



## aliiqbal1984 | 2021-02-06T08:23:44+00:00
> fake cores do not help rate, only real cores
> you have 20 real cores?
> 
> what algorithm?
> 
> Run CN-Heavy and it will stop using all cores, but jam all cache full (60MB / 4MB scratchpad = 15 cores).
> To fit that CPU model ideally you would need an algo with 3MB scratchpads, which do not exist.

Thanks for your response, I got UCSC server where I am trying it have total 24 CPUs x 2.294 GHz

Processor type Intel Xeon ES-2670 v3 having 2 sockets 12 real cores on each socket

I am actually looking for suggestion on what to add in my config file to start running more threads  what will be the best way to get most out of this CPU.

## Lonnegan | 2021-02-06T16:11:23+00:00
If you want to use more threads manually, you have to edit config.json, section "cpu", line "rx". There between the [] you can set which cores of your CPU should be used for Monero mining, separated by commas, and therefore how many cores, as well.

For example when you write [0, 2, 4, 6] the miner uses four cores, namely the (logical) cores 0, 2, 4 and 6. You can also write [-1, -1, -1, -1]. Here the miner uses four cores, too, but the OS decides which cores are used.

## Spudz76 | 2021-02-17T04:16:19+00:00
Depends on algo because they all have different sizing and saturation requirements.

For generic Cryptonight at 2MB scratchpad size you can run 12 threads per socket (24 threads total) and you will have 6MB of unused cache per socket (12MB unused total).  Because you've run out of real cores before running out of cache.

For Cryptonight-Heavy at 4MB scratchpad size you can run 7 threads per socket (14 threads total) because that's maximum of cache each has (30MB/4MB = 7.5 but you can't have half a thread so, 7).  This leaves 5 cores and 2MB of cache per socket unused.  BUT it might be more profitable than whatever other algo that "uses more of the cpu" or fits better.

For other algos it gets a bit more complicated, and they begin using system ram instead of just cache and cores.

## bezatine | 2021-02-23T02:02:46+00:00
I seen alot of the custom stuff for different algorithms here and google search xmrig max threads or max cpu usage, I feel like users are saying an extra 20-22% on different algo but they have some benchmark tweaks you can look up too, its something about the wrmsr line can tweaked for extra 2% or it can lower, but yea I found a lot in the command line options page on how you can push it

check cpu backend section
https://xmrig.com/docs/miner/command-line-options

# Action History
- Created by: aliiqbal1984 | 2021-02-05T20:27:44+00:00
- Closed at: 2021-04-12T14:16:59+00:00
