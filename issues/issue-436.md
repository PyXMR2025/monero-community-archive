---
title: AMD Ryzen 1700 16 cores but showing/using only 8 cores
source_url: https://github.com/xmrig/xmrig/issues/436
author: bitcoinvsalts
assignees: []
labels: []
created_at: '2018-03-09T20:48:05+00:00'
updated_at: '2018-03-14T21:09:46+00:00'
type: issue
status: closed
closed_at: '2018-03-09T21:49:24+00:00'
---

# Original Description
Here are my specs:

```
 OS Name     : Ubuntu 16.04.4 LTS (64 bit)
 Kernel      : Dedicated / 4.13.0-36-generic
 Hostname    : Ubuntu-1604-xenial-64-minimal
 CPU Model   : AMD Ryzen 7 1700X Eight-Core Processor
 CPU Cores   : 16 cores @  2200.000 MHz
 CPU Cache   : 512 KB
 Total RAM   : 64420 MiB (Free 63465 MiB)
```

My command line:

`$ ./xmrig -a cryptonight-lite -l logga.txt --max-cpu-usage 100 -o pool.aeon.hashvault.pro:3333  -k`

And the logs:

```
 * VERSIONS:     XMRig/2.4.5 libuv/1.8.0 gcc/7.1.0
 * HUGE PAGES:   available, enabled
 * CPU:          AMD Ryzen 7 1700X Eight-Core Processor          (1) x64 AES-NI
 * CPU L2/L3:    4.0 MB/16.0 MB
 * THREADS:      8, cryptonight-lite, av=2, donate=5%
 * POOL #1:      pool.aeon.hashvault.pro:3333
```

top shows I only use 50% of my cpu(s). How can I use 100% of my CPUs?



# Discussion History
## rr32btg | 2018-03-09T21:14:09+00:00
Ryzen 7 series is 8 core processors. in top/htop and other similar software you can see 16 "cores", but actually its 8 phisical cores and 8 virtual cores.

How can I use 100% of my CPUs? Actually you do not need to use 100% percent for effective mining. Sometimes 100% can drop your hashrate. Example, recently I tested xmrig on 96 core server and at 100% load results were terrible, maximum performance was only when xmrig used on 32 cores. This situation is normal, because of Cryptonight is cpu cache size dependent algo. So more important to find optimal core count (based on cpu cache size) instead of try to load your cpu to 100%.

## bitcoinvsalts | 2018-03-09T21:19:48+00:00
@rr32btg thanks for your reply. so do you thinks my miner is actually using the maximum resource it needs? no more room of optimization?

## rr32btg | 2018-03-09T21:33:22+00:00
Only two ways for optimization that I see now. First - try to reduce threads count in xmrig for more energy efficient mining process (sometimes less threads can produce same amount of hash/sec). Second - try to overclock cpu to gain more compute power (only if you know hat you do, because of overclocking may be dangerous for you hardware)

## bitcoinvsalts | 2018-03-09T21:49:24+00:00
@rr32btg  spasiba

## sohosynergy | 2018-03-14T21:09:46+00:00
threads should be half of what you have so in the case of 8 cores 16 threads you should use only max of 8 threads (the rule of thumb is actually 1/2 of the cpu cache you have but I prefer to use the secondary rule of 1/2 the threads)  I have the Ryzen 1700x and set "threads": 7,  in the config.json to leave at least 1 thread for managing the rig and for the system services to have some cpu time to do their management.  If I try to raise the threads higher than 8 I see lower hashrates.

Here's my config:

```
{
    "algo": "cryptonight",  // cryptonight (default) or cryptonight-lite
    "av": 0,                // algorithm variation, 0 auto select
    "background": false,    // true to run the miner in the background
    "colors": true,         // false to disable colored output    
    "cpu-affinity": null,   // set process affinity to CPU core(s), mask "0x3" for cores 0 and 1
    "cpu-priority": 4,   // set process priority (0 idle, 2 normal to 5 highest)
    "donate-level": 1,      // donate level, mininum 1%
    "log-file": null,       // log all output to a file, example: "c:/some/path/xmrig.log"
    "max-cpu-usage": 100,    // maximum CPU usage for automatic mode, usually limiting factor is CPU cache not this option.  
    "print-time": 5,       // print hashrate report every N seconds
    "retries": 5,           // number of times to retry before switch to backup server
    "retry-pause": 1,       // time to pause between retries
    "safe": false,          // true to safe adjust threads and av settings for current CPU
    "threads": 7,        // number of miner threads

```I'll be increasing the donation level this week as the developer of XMRIG has made the easiest mining app I have used to date.


# Action History
- Created by: bitcoinvsalts | 2018-03-09T20:48:05+00:00
- Closed at: 2018-03-09T21:49:24+00:00
