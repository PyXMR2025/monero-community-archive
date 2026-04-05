---
title: optimal config for hp380p g8 - Intel® Xeon® Processor E5-2620 - window server
  2016
source_url: https://github.com/xmrig/xmrig/issues/331
author: thomassen666
assignees: []
labels:
- NUMA
created_at: '2018-01-10T23:43:07+00:00'
updated_at: '2021-11-29T13:30:40+00:00'
type: issue
status: closed
closed_at: '2019-08-02T12:39:29+00:00'
---

# Original Description
Hi.
Im trying to figure out the optimal settings for my workserver that is goin into retirment soon and will be used as a miner asset?

so my question narrows down to if xmrig and xeon cpus are optimal for mining?
i get with this config 210 hs,  :

{
    "algo": "cryptonight",  // cryptonight (default) or cryptonight-lite
    "av": 0,                // algorithm variation, 0 auto select
    "background": false,    // true to run the miner in the background
    "colors": true,         // false to disable colored output    
    "cpu-affinity": null,   // set process affinity to CPU core(s), mask "0x3" for cores 0 and 1
    "cpu-priority": null,   // set process priority (0 idle, 2 normal to 5 highest)
    "donate-level": 1,      // donate level, mininum 1%
    "log-file": null,       // log all output to a file, example: "c:/some/path/xmrig.log"
    "max-cpu-usage": 90,    // maximum CPU usage for automatic mode, usually limiting factor is CPU cache not this option.  
    "print-time": 60,       // print hashrate report every N seconds
    "retries": 5,           // number of times to retry before switch to backup server
    "retry-pause": 5,       // time to pause between retries
    "safe": false,          // true to safe adjust threads and av settings for current CPU
    "threads": null,        // number of miner threads
    "pools": [
        {
            "url": "pool.supportxmr.com:7777",   // URL of mining server
            "user": xxxxxxx                        // username for mining server
            "pass": "x",                       // password for mining server
            "keepalive": true,                 // send keepalived for prevent timeout (need pool support)
            "nicehash": false                  // enable nicehash/xmrig-proxy support
        }
    ],
    "api": {
        "port": 0,                             // port for the miner API https://github.com/xmrig/xmrig/wiki/API
        "access-token": null,                  // access token for API
        "worker-id": null,                      // custom worker-id for API
    }
}


Any takers?? 
Note that i run this on windows server 2016 for now.


# Discussion History
## nsummy | 2018-01-16T17:31:15+00:00
That seems a little low.  With that configuration how many threads does it start?  And is this a single processor or are there two?  It would help to post the initial output you see when the miner starts.

## thomassen666 | 2018-01-16T18:18:11+00:00
![hash-startup](https://user-images.githubusercontent.com/32498630/35004911-fa67c516-faf1-11e7-8f1a-04a081bf54bf.PNG)


## thomassen666 | 2018-01-16T18:18:37+00:00
Its only single cpu

## nsummy | 2018-01-16T20:09:58+00:00
Ok I see a couple of issues immediately.

1.  You need to enable Huge Pages.  Follow these instructions and then reboot:  https://docs.microsoft.com/en-us/sql/database-engine/configure-windows/enable-the-lock-pages-in-memory-option-windows      - Those 2 words in red should be green and should say "Available, Enabled"  If it still doesn't say that after enabling the pages and restarting, then also run xmrig as an administrator.  And actually you might just need to reboot (see the very first message in the window)

2.  Download the MSVC version of XMRig, not the GCC version.

I would think your hashrate should be over 400.



## thomassen666 | 2018-01-16T20:38:35+00:00
so did as followed, it actually reduced the hashrate... ?
<img width="873" alt="screen shot 2018-01-16 at 21 35 15" src="https://user-images.githubusercontent.com/32498630/35011190-97aed4b4-fb05-11e7-8a17-2de3e4305a76.png">



## thomassen666 | 2018-01-16T20:39:24+00:00
same result with the GCC edition aswell..

## nsummy | 2018-01-16T21:05:46+00:00
Thats odd.  In your config file try changing threads from null to 6.
For processor affinity change it from null to "0x555"   You actually need the quotes around that one otherwise you will get an error

I believe your issue might be twofold:  1.  Your Cache is large enough to run 7 threads, but you only have 6 cores, and 2.  Hyperthreading will kill the performance.  The affinity of 0x555 means it is locking the 6 threads to the 6 physical cores.

So these options should be changed to the following:
"av": 1, 
"cpu-affinity": "0x555",
"cpu-priority": 5,
"max-cpu-usage": 100,
"threads": 6,

Just for fun, also try this config:

"av": 2, 
"cpu-affinity": "0x55",
"cpu-priority": 5,
"max-cpu-usage": 100,
"threads": 4,




And one other thing, do you have any background processes going on?  Since this is obviously processor intensive, any activity can slow it down.  Like my i7 will hash at over 300 H/S, but if I run it while I surf the web or watch youtube, it will drop to under 100.



## thomassen666 | 2018-01-16T21:38:02+00:00
so i´ve tried both configs, it gives out max hashrate of 260 so in the end its a step forward...
only processes that runs in the background is notepad... should not be to much of a challenge :)
the config that worked best was "0x555" so go figure.. 


## nsummy | 2018-01-16T22:25:38+00:00
I thought it would be a little higher but I've never ran a miner on a windows server so I can't say for certain if the performance should be different.  Is Windows Defender disabled?   One other thing to try would be to set the "av": to 3.  There are a couple of other miners you can try also.  For windows I've found XMRig is the best, but your mileage may vary

The main competition:  XMR-Stak - https://github.com/fireice-uk/xmr-stak/releases/tag/v2.2.0
Claymore:  https://drive.google.com/drive/folders/0B69wv2iqszefSzYyM3BTYXVxZGs


Also if you want to make this machine much better, pick up a couple of v2 E5s on ebay for cheap:  https://www.ebay.com/itm/Matched-Pair-Intel-Xeon-E5-2650-v2-2-60GHz-8CORE-20MB-8GT-s-SR1A8-LGA2011-CPUS/352256855122?hash=item5204250c52:g:RzgAAOSwIWVY-SM~

250 bucks and you would make your money back in a couple of months


## thomassen666 | 2018-01-16T22:28:38+00:00
Thank you for taking the time to reply. i will most def do some price calc on the v2 E5s.
cheers.

## xmrig | 2019-07-29T02:18:16+00:00
If this issue still actual, please check v2.99.2-beta release #1077.
Thank you.

## re3e-yul | 2021-11-29T13:30:40+00:00
Hum I'm getting 55 KH raw on twin E5-2695v2 , with cpu priority at 5 and threads at 48 ( 2 processors * 12 cores * 2 threads by core )  + cpu-no-yield random-1g-pages and huge-page-jit

# Action History
- Created by: thomassen666 | 2018-01-10T23:43:07+00:00
- Closed at: 2019-08-02T12:39:29+00:00
