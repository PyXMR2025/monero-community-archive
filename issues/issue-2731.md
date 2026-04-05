---
title: Please add Max Cpu Usage
source_url: https://github.com/xmrig/xmrig/issues/2731
author: DogeZillaMeme
assignees: []
labels:
- question
created_at: '2021-11-27T19:28:13+00:00'
updated_at: '2021-12-19T15:45:44+00:00'
type: issue
status: closed
closed_at: '2021-12-19T15:45:44+00:00'
---

# Original Description
Is very good option max cpu usage ,not max threads...because who have 200...300 miners,she give a mass start and i have computers with 80 cpu , i have with 366...and i need to put on every computer manual config ..threads...please if is posible to put max cpu usage,like xmrig cc. Thank you and God bless you 

# Discussion History
## DogeZillaMeme | 2021-11-27T19:38:48+00:00
[root@localhost .systemd-private-service]# cat .b.lst
 * ABOUT        XMRigCC/2.9.7 gcc/10.2.1 (RELEASE)
 * LIBS         libuv/1.40.0 OpenSSL/1.1.1i hwloc/2.4.0
 * HUGE PAGES   supported
 * 1GB PAGES    disabled
 * CPU          Intel(R) Xeon(R) Platinum 8260 CPU @ 2.40GHz (8) 64-bit AES
                L2:192.0 MB L3:286.0 MB 192C/384T NUMA:8
 * MEMORY       873.8/3022.2 GB (29%)
 * DONATE       1%
 * ASSEMBLY     auto:intel
 * POOL #1      10.200.135.3:15346 algo auto
 * CC Server    localhost:null
[2021-11-27 14:36:58.492]  cpu      use profile  rx/wow  (326 threads) scratchpad 1024 KB
[2021-11-27 14:36:58.855]  cpu      READY threads 326/326 (326) huge pages 100% 326/326 memory 333824 KB (363 ms) - CPU usage limited to 20%


## DogeZillaMeme | 2021-11-27T19:40:14+00:00
this option from xmrig cc i want on xmrig to CPU usage limited to 20%


## SChernykh | 2021-11-27T23:05:34+00:00
https://xmrig.com/docs/miner/command-line-options
```
--cpu-max-threads-hint=N maximum CPU threads count (in percentage) hint for autoconfig
```

## masterxbtc | 2021-12-11T17:51:42+00:00
> https://xmrig.com/docs/miner/command-line-options
> 
> ```
> 
> --cpu-max-threads-hint=N maximum CPU threads count (in percentage) hint for autoconfig
> 
> ```

I've tried that before running. I set the hint at 91 (12 core/ 24 thread Ryzen 9 trying to leave 2 open threads) and it still runs all 24 threads. I got froggy and set it to 83 (20 threads/10 cores trying to get 2 cores and 4 threads open) and it still runs all 24. 

Why I'm trying to leave open a couple/few threads is because it is lowering my GPU(ETH) hashrate. 

I did a little tinkering around in the config.json file and got it to 18 threads.  So now my CPU is 76-77% utilized and my ETH hashrate is now running at full potential. I think I could get a little more out of the CPU, but I don't want it at the expense of my ETH mining hashrate. 



## Spudz76 | 2021-12-11T19:09:46+00:00
Threads hint does nothing, unless you delete the existing thread definitions from config.json first.

Since threads are not recalculated unless there is no definition, and the hint only does anything if calculation executes.

## masterxbtc | 2021-12-11T20:08:21+00:00
> Threads hint does nothing, unless you delete the existing thread definitions from config.json first.
> 
> 
> 
> Since threads are not recalculated unless there is no definition, and the hint only does anything if calculation executes.

I have been starting with a fresh config.json file every time I have altered the thread-hint. I would prefer a max core "actual number of cores" not a percentage.  If I know I have a 12 core processor, I'd love to select 11 and leave the other core for ETH mining. 

## SChernykh | 2021-12-13T10:27:00+00:00
@masterxbtc try hint values below 50.

## masterxbtc | 2021-12-13T19:04:16+00:00
> @masterxbtc try hint values below 50.

That worked perfectly! Set it to 45 and I am leaving 2 threads open on my CPU and that was my goal. Thank you for the help! 

# Action History
- Created by: DogeZillaMeme | 2021-11-27T19:28:13+00:00
- Closed at: 2021-12-19T15:45:44+00:00
