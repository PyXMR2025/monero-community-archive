---
title: 'xmrig vs xmr-stak: performance issue on ryzen 1700'
source_url: https://github.com/xmrig/xmrig/issues/151
author: hamstertheminer
assignees: []
labels: []
created_at: '2017-10-12T16:55:39+00:00'
updated_at: '2019-01-11T09:50:04+00:00'
type: issue
status: closed
closed_at: '2018-03-14T23:19:10+00:00'
---

# Original Description
Hi,
I have a AMD Ryzen 7 1700 8 core-16 threads and I get 490-500 H/s with xmr-stack-cpu by using core affinity and selecting even cores i.e affine_to_cpu" : 0-2...14 (task manager shows 8 logical cores fully used). While with xmrig I get only 275-300 H/s by using affinity 0x5555 (even cores) for 8 threads (task manager shows the process jumping among all logical cores even if those selected by 0x5555 are used more). I tried also with 0xAAAA, but the results are worse. Can you help me?

# Discussion History
## mk148a | 2017-10-12T18:02:25+00:00
Hey, can you use xmrig-2.4.0-gcc7-xenial-amd64-no-api.tar.gz?
 ryzen version is xenial  amd64

## xmrig | 2017-10-12T19:37:43+00:00
If you use config file, please set affinity like this `"0x5555"` or `21845`.
Also looks like you need to reboot, because miner fail to allocate huge (large) pages, on second line should anything no red text. It main reason of low hashrate.
Thank you.

## EUA | 2017-11-12T15:20:50+00:00
This is platform related.
On Linux, I got 615 with smr-stak and 605 with xmrig.
But on windows, without affinity option, it returns ~330.

## ghost | 2017-12-02T12:22:14+00:00
~350 is generally what you get without hugepages
i get ~500 with hugepages (stock clocks)
affinity with lower power `av=2` the config must be even cores among the ctx, so a ryzen has 2 ctx, something like `0x5050`

## pxrebirth | 2018-01-07T05:10:10+00:00
Strange for me to hear such high hashrates on the 1700.  I am running at 3.8ghz and still barely see H/s over 400 with averages more like 350-390 on xmrig.  16gb of 2666 ram, ssd.  huge page enabled, affinity set as instructed, 8 threads.  xmr-stak reports minimally but consistently higher in the 430-450 range.

## ZachE84 | 2018-01-10T18:06:34+00:00
Yes. Same issue. XMRRig 190h/s and XMR-Stack 550h/s for my Ryzen 1700 stock.

Whats going on? I must say config file for XMRRig is super complicated. XMRStaks config file is more user friendly.

## ZachE84 | 2018-01-11T02:40:40+00:00
I have tried every affinity possible. I see affinity to 0x555  and 0x5555 lately - didn't help. I have adjusted everything. Please see screenshot.

![ss](https://user-images.githubusercontent.com/33164899/34806032-e4911294-f64e-11e7-8556-a7b9437dda21.PNG)


## ghost | 2018-01-11T04:22:01+00:00
@ZachE84 your config looks fine try a different xmrig build, on windows you should prefer msvc

## xmrig | 2018-01-11T04:47:21+00:00
Affinity `0x155` not correct, it use only 5 cores, but `0x5555` or `0xAAAA` should be fine. It strange I was checked 1700 it was work good, without any affinity too.

1. Did you close stak miner when run xmrig?
2. If yes, can you provide API output when run with proper mask.

Thank you.

## rhouberg | 2018-02-16T17:37:39+00:00
There is definitely something up with Ryzen 7 1700 and CPU affinity mask.  I'm seeing similar issues.  0x5555 works great on my Ryzen 7 1700x machines (I have 2 of them).  But doing a little side mining on my home server (Ryzen 7 1700) doesn't work well.  Definitely an issue with CPU mask application on this processor for some reason.  I have Hyper-V role enabled on this server.  Is there any chance that the HyperVisor messes with the CPU mask somehow?

![image](https://user-images.githubusercontent.com/26254615/36320945-aea0fb0a-130d-11e8-8481-10a60fc852ee.png)



## ZachE84 | 2018-02-16T18:26:59+00:00
Yes agreed. I have two servers that has the Ryzen 7 1700 and 1 gets 450h/s and 1 gets 150 h/s no matter what I do. Its odd. Same windows build, same software installed, same...everything. I am out of ideas how to fix this bad Ryzen 7. Maybe its faulty itself?

## ghost | 2018-02-17T04:54:58+00:00
@rhouberg I might be mistaken but I don't think cpu affinity matters under the scope of virtualization because the hypervisor ultimately decides where to put process/threads, I don't think cpu affinity is allowed by default by any hypervisor but it should configurable, and since with hyper-v enabled the default session is also under hyper-v it could help.
@ZachE84 maybe large/huge pages are not big enough? I don't know if xmrig checks that they are enough when they are enabled

## mysticaltech | 2018-04-16T22:19:55+00:00
Just correlate to what @untoreh said about cpu affinity, I get a much better hash-rate when set to null compared to 0x5555.

## Blackcol | 2018-04-18T10:32:04+00:00
I have a ryzen 1700 and I can get 530 h/s
System: W10 with all the main updates
OC: 3.5Ghz Base clock - disabled boost clock and anything else that can down clock or boost clock it automatically.
![image](https://user-images.githubusercontent.com/32214170/38926899-c834a378-42c9-11e8-953c-1832b06bf3fe.png)

> 

    "algo": "cryptonight",  // cryptonight (default) or cryptonight-lite
    "av": 1,                // algorithm variation, 0 auto select
    "background": false,    // true to run the miner in the background
    "colors": true,         // false to disable colored output    
    "cpu-affinity": null,   // set process affinity to CPU core(s), mask "0x3" for cores 0 and 1
    "cpu-priority": 3,   // set process priority (0 idle, 2 normal to 5 highest)
    "donate-level": 1,      // donate level, mininum 1%
    "log-file": null,       // log all output to a file, example: "c:/some/path/xmrig.log"
    "max-cpu-usage": 100,    // maximum CPU usage for automatic mode, usually limiting factor is CPU cache not this option.  
    "print-time": 60,       // print hashrate report every N seconds
    "retries": 5,           // number of times to retry before switch to backup server
    "retry-pause": 5,       // time to pause between retries
    "safe": false,          // true to safe adjust threads and av settings for current CPU
    "threads": 8,        // number of miner threads

## ZachE84 | 2018-04-18T13:22:26+00:00
But whats your overclock?

## pxrebirth | 2018-04-18T13:32:31+00:00
I would also be curious what your platform is Andrés Alfonso Aguirre
Girón.  Motherboard, core clock, CPU voltage, RAM speed, etc.  Thanks for
posting your results!

On Wed, Apr 18, 2018 at 7:22 AM ZachE84 <notifications@github.com> wrote:

> But whats your overclock?
>
> —
> You are receiving this because you commented.
> Reply to this email directly, view it on GitHub
> <https://github.com/xmrig/xmrig/issues/151#issuecomment-382384316>, or mute
> the thread
> <https://github.com/notifications/unsubscribe-auth/AhjgiREZpmgdE9oDc3C6TTso2Oo1D8c5ks5tpz4YgaJpZM4P3UN->
> .
>


## Blackcol | 2018-04-18T15:14:12+00:00
MB: Msi B350M Pro Vdh
Ram: Corsair Vengeance 8Gb 2133 (1066mhz) default settings.
Core Speed: 3599Mhz
Core Voltage: 1170
iddle speed: 546 h/s
With a better mb, we can get more speed.

## rkinkopf | 2018-04-18T15:47:38+00:00
I'm in the high 500's with xmrig on Ryzen 7 1700

no changes or overclock




On Wed, Apr 18, 2018 at 9:32 AM, pxrebirth <notifications@github.com> wrote:

> I would also be curious what your platform is Andrés Alfonso Aguirre
> Girón. Motherboard, core clock, CPU voltage, RAM speed, etc. Thanks for
> posting your results!
>
> On Wed, Apr 18, 2018 at 7:22 AM ZachE84 <notifications@github.com> wrote:
>
> > But whats your overclock?
> >
> > —
> > You are receiving this because you commented.
> > Reply to this email directly, view it on GitHub
> > <https://github.com/xmrig/xmrig/issues/151#issuecomment-382384316>, or
> mute
> > the thread
> > <https://github.com/notifications/unsubscribe-auth/
> AhjgiREZpmgdE9oDc3C6TTso2Oo1D8c5ks5tpz4YgaJpZM4P3UN->
> > .
>
> >
>
> —
> You are receiving this because you are subscribed to this thread.
> Reply to this email directly, view it on GitHub
> <https://github.com/xmrig/xmrig/issues/151#issuecomment-382387418>, or mute
> the thread
> <https://github.com/notifications/unsubscribe-auth/AiOvqcvYHzblIEwiR3QFvB7tgnwZMvOQks5tp0B0gaJpZM4P3UN->
> .
>


## rmg8192 | 2018-05-28T05:06:25+00:00
if on windows - please make sure your not using balanced power mode.
this will park cores of your cpu leading to much lower hashes.

you can check this via task manager and hover over the cores... should say parked..

## kusayuzayushko | 2019-01-11T09:48:40+00:00
Linux user here.
Ryzen 5 1600

`xmrig -a cryptonight <pool settings> --asm=ryzen --cpu-affinity 0x5555`

can't get past 350 on average https://i.imgur.com/kelJQGC.png

```$ grep Huge /proc/meminfo
AnonHugePages:         0 kB
ShmemHugePages:        0 kB
HugePages_Total:     256
HugePages_Free:      248
HugePages_Rsvd:        0
HugePages_Surp:        0
Hugepagesize:       2048 kB
Hugetlb:          524288 kB

lscpu | grep MHz
CPU MHz:             3692.191
CPU max MHz:         3700.0000
CPU min MHz:         1550.0000

| THREAD | AFFINITY | 10s H/s | 60s H/s | 15m H/s |
|      0 |        0 |    50.7 |    48.4 |     n/a |
|      1 |        2 |    54.2 |    53.1 |     n/a |
|      2 |        4 |    31.1 |    29.6 |     n/a |
|      3 |        6 |    31.5 |    34.2 |     n/a |
|      4 |        8 |    52.5 |    48.1 |     n/a |
|      5 |       10 |    54.6 |    51.7 |     n/a |
|      6 |       12 |    31.4 |    29.6 |     n/a |
|      7 |       14 |    31.7 |    30.2 |     n/a |
[2019-01-11 16:49:39] speed 10s/60s/15m 337.7 324.9 n/a H/s max 388.0 H/s


```

# Action History
- Created by: hamstertheminer | 2017-10-12T16:55:39+00:00
- Closed at: 2018-03-14T23:19:10+00:00
