---
title: AMD Threadripper PRO 5995WX 64-cores, with huge pages, 1gb pages and 64 threads
  only mining at 1800H/s?
source_url: https://github.com/xmrig/xmrig/issues/3208
author: FeatureSpitter
assignees: []
labels:
- question
created_at: '2023-02-03T01:31:11+00:00'
updated_at: '2025-06-16T19:24:31+00:00'
type: issue
status: closed
closed_at: '2025-06-16T19:24:31+00:00'
---

# Original Description
How come 3995WX is older and can make close to 50KH/s and 5995WX not even 2KH/s?

MSR mode on, Huge pages on, 1gb page on. 128 threads... Just 1.8KH/s...

Why?

You can see my setup here in these 3 XMRIG benchmarks:
https://xmrig.com/benchmark/71cDqR
https://xmrig.com/benchmark/31DFua
https://xmrig.com/benchmark/4fqiZk

I was the one who submitted that benchmark. 

## Specs:
![image](https://user-images.githubusercontent.com/39516190/216531123-b676999c-5a8d-4246-ada4-471fa6dcfe6a.png)

![cpuz_asus_iKD7q54Wxm](https://user-images.githubusercontent.com/39516190/216530971-d1640c81-5528-4bcc-8350-da4a53e83e88.gif)

# Tests

# 1 threads:
`xmrig.exe -u x+30000 -o 192.168.50.184:3333 --threads=1 --randomx-1gb-pages`

![image](https://user-images.githubusercontent.com/39516190/216531692-2a9dd77b-d345-4a05-86bc-544c8f326add.png)

# 4 threads:
`xmrig.exe -u x+30000 -o 192.168.50.184:3333 --threads=4 --randomx-1gb-pages`

![image](https://user-images.githubusercontent.com/39516190/216531928-1095eed3-ec4a-403d-a7e0-46b97d64cf12.png)
![image](https://user-images.githubusercontent.com/39516190/216531973-7d331c10-e129-43ed-a935-94bf3bcd995f.png)

# 8 threads:
`xmrig.exe -u x+30000 -o 192.168.50.184:3333 --threads=8 --randomx-1gb-pages`

![image](https://user-images.githubusercontent.com/39516190/216532134-27964326-f224-4d36-89e5-9452ce52a8e4.png)
![image](https://user-images.githubusercontent.com/39516190/216532193-4bc90493-4f76-4993-82b6-d811f0ce11ee.png)

# 16 threads:
`xmrig.exe -u x+30000 -o 192.168.50.184:3333 --threads=16 --randomx-1gb-pages`

![image](https://user-images.githubusercontent.com/39516190/216532414-c377bcb3-78f6-49ff-aa08-d1c593620140.png)
![image](https://user-images.githubusercontent.com/39516190/216532460-466d2fc5-b7f9-4425-8f6d-54becbc86da4.png)

# 32 threads:
`xmrig.exe -u x+30000 -o 192.168.50.184:3333 --threads=32 --randomx-1gb-pages`

![image](https://user-images.githubusercontent.com/39516190/216532620-dd2d8e4a-ec85-4017-a178-281fc0c6ff98.png)
![image](https://user-images.githubusercontent.com/39516190/216532676-4426398a-a872-4be3-a85e-2d7aad1ba5b4.png)

# 64 threads:
`xmrig.exe -u x+30000 -o 192.168.50.184:3333 --threads=64 --randomx-1gb-pages`

![image](https://user-images.githubusercontent.com/39516190/216532918-d44fae42-b047-4110-bbb6-80f25027693d.png)
![image](https://user-images.githubusercontent.com/39516190/216533027-54946a1c-c61b-45bd-b4b4-050aa7d10e97.png)

# 128 threads:
`xmrig.exe -u x+30000 -o 192.168.50.184:3333 --threads=64 --randomx-1gb-pages`

![image](https://user-images.githubusercontent.com/39516190/216533413-8ef58cb3-cd9e-4d9f-a886-32df8e22f44e.png)
![image](https://user-images.githubusercontent.com/39516190/216533502-07f996cd-2184-4e07-8c8e-84c187510293.png)


# Discussion History
## Spudz76 | 2023-02-03T14:48:10+00:00
Seems like it should have more than `NUMA:1` (I think 4?) and you should have a DIMM per memory channel (8), not just one stick.  Basically as you add threads, the other cores have to ask the first core to get and hand off every memory access to the other cores, until saturation starts happening which just gets worse as you keep adding threads.

## FeatureSpitter | 2023-02-03T16:35:42+00:00
> Seems like it should have more than `NUMA:1` (I think 4?) and you should have a DIMM per memory channel (8), not just one stick. Basically as you add threads, the other cores have to ask the first core to get and hand off every memory access to the other cores, until saturation starts happening which just gets worse as you keep adding threads.

Hello, thanks for answering.

I just sticked some rams that I had lying around, I'm going to try to buy some good ones all from the same make, frequency and CL14.

Adding just the ones that you see in the image didn't change the NUMA from being 1. Do I need to go anything else after I add more ram sticks?

![IMG20230203163049](https://user-images.githubusercontent.com/39516190/216657129-7d3ed9fe-0e43-4957-a613-b8895deb790f.jpg)


## SChernykh | 2023-02-03T17:08:39+00:00
This CPU is a single NUMA node, but it doesn't work well without a memory stick in each channel, and these sticks should be the same for the best performance.

## xmrig | 2023-02-03T18:29:48+00:00
Also you should not use `--threads` options on complex CPUs because this option creates threads without binding to specific cores.
Thank you.


## Spudz76 | 2023-02-03T21:39:23+00:00
All those things too, and I was unaware that this series of CPU should be NUMA:1 - still need 8 channels filled so it has the widest possible path.

You may also not have enabled the memory SPD since the single stick was running 2666 when it can do 3200.  And now it's 2133 when it seems like the worst stick is 2666 (so I would expect it to at least run them all 2666).  Usually some option somewhere in the bios, I am unfamiliar with this board and the manuals are fairly terrible (doesn't even mention the memory channels or best population, though it does suggest fully matching specs/batches).  Probably (usually) boards expect even numbers of DIMMs, maybe it will run 4-channel with 4 sticks, but they probably also need to be spread evenly between the upper and lower banks.  The manual doesn't cover what slots should be used first when they aren't all full, usually they do.  I'd guess the two slots closest to the CPU on either side (C,D and E,F) but it could also be interleaved (B,D and E,G).  Rarely they are the physically farther slots.

There should be some tools that say what number of memory channels are active.  Maybe these are 1 or 8 and nothing between, and if it stayed single-channel then that would explain how it didn't improve halfway to normal speeds.  But the odd-number might also be knocking it back to single-channel.  Also dual-rank vs single-rank can make differences.

## Spudz76 | 2023-02-03T21:44:42+00:00
Looks like [the CPU does](https://en.wikichip.org/wiki/amd/ryzen_threadripper/pro_5995wx#Memory_controller) 1/2/4/8 channels:
```
Bandwidth	Single 25.6 GB/s Double 51.2 GB/s Quad 102.4 GB/s Octa 204.8 GB/s
```
If you find the right slots and go by even numbers it should double/quadruple/octuple the hashrate whenever it actually enables multichannel.

## NVMDSTEVil | 2023-02-04T01:46:16+00:00
> Looks like [the CPU does](https://en.wikichip.org/wiki/amd/ryzen_threadripper/pro_5995wx#Memory_controller) 1/2/4/8 channels:
> 
> ```
> Bandwidth	Single 25.6 GB/s Double 51.2 GB/s Quad 102.4 GB/s Octa 204.8 GB/s
> ```
> 
> If you find the right slots and go by even numbers it should double/quadruple/octuple the hashrate whenever it actually enables multichannel.

Asus wrx80e-sage se wifi has only 8 slots.  Load them up for optimal performance.

If 8 slots full still gives issues try forcing the NUMA detection by setting memory interleave to "Die" mode in the bios.

## SChernykh | 2023-02-05T14:07:17+00:00
Ну сам и переведи бл@ть. По-хорошему влом попросить?

# Action History
- Created by: FeatureSpitter | 2023-02-03T01:31:11+00:00
- Closed at: 2025-06-16T19:24:31+00:00
