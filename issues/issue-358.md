---
title: Not using all the potential of the Xeon E5 2698 V4
source_url: https://github.com/xmrig/xmrig/issues/358
author: jcastro
assignees: []
labels: []
created_at: '2018-01-23T10:21:04+00:00'
updated_at: '2018-11-05T12:47:27+00:00'
type: issue
status: closed
closed_at: '2018-11-05T12:47:27+00:00'
---

# Original Description
Hello!

I have the Xeon E5-2698 v4 (see https://ark.intel.com/products/91753/Intel-Xeon-Processor-E5-2698-v4-50M-Cache-2_20-GHz) but it seems it's not using all of its potential. In fact I had to decrease the cpu-max-usage to 60 in order to get around an average of 800 H/s... with cpu-max-usage 75 I was getting around 450-500 H/s

This is my command line
`@echo off
xmrig.exe -o pool.supportxmr.com:7777 -u WALLET -p WORKERNAME -k --max-cpu-usage 60 --donate-level 1
pause`

This the console output as soon as I start the miner
![screen shot 2018-01-23 at 11 19 59](https://user-images.githubusercontent.com/190036/35270531-b7927a72-002f-11e8-869d-646dd97c12fd.png)


# Discussion History
## HeDo88TH | 2018-02-01T00:13:58+00:00
Use these settings

--max-cpu-usage 95 
--cpu-affinity "0x5555555555" 
--threads 20

let me know

## jcastro | 2018-02-02T13:29:24+00:00
@HeDo88TH thanks! I just tried but I'm getting a bit less, around 680H/s

![screen shot 2018-02-02 at 14 28 57](https://user-images.githubusercontent.com/190036/35735541-80c378e0-0825-11e8-9bf2-dd7bec810a7f.png)


## jcastro | 2018-02-02T13:31:34+00:00
Actually using 20 threads only uses the "physical" cores but I get the threaded ones at 0% – See htop
![screen shot 2018-02-02 at 14 30 36](https://user-images.githubusercontent.com/190036/35735634-c2c91cc2-0825-11e8-8068-cdc12cbad09e.png)


## jcastro | 2018-02-02T13:35:20+00:00
Seems like the perfect configuration is the one that xmrig itself selects which is 24 threads. Less or more than that gives me less H/s. 24-25 is just perfect

## HeDo88TH | 2018-02-02T14:32:24+00:00
You can set the max-cpu-usage to 100, It will give you +5%
It's useless to use the threaded cores, what is limiting the mining speed is the L2/L3 cache size not the core count. By using the threaded cores you are not adding any of it :)

## mohammad4u | 2018-02-16T19:36:32+00:00
@jcastro, i can see that in the first instance the l3 cache is showing 0 while in the second it shows true value of 50 mb. Did you change any settings other than recommended by @hedo88th?

## kimats | 2018-03-02T05:22:24+00:00
@HeDo88TH 
OK, the mining speed is the L2/L3 , what about the frequency ? does CPU@ 2GH and CPU@ 3GH make difference ?

## HeDo88TH | 2018-05-22T14:46:48+00:00
Yes it will make difference

# Action History
- Created by: jcastro | 2018-01-23T10:21:04+00:00
- Closed at: 2018-11-05T12:47:27+00:00
