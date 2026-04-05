---
title: Wrong CPU L2 cache size detection
source_url: https://github.com/xmrig/xmrig/issues/428
author: VSergey
assignees: []
labels:
- bug
created_at: '2018-03-03T21:25:47+00:00'
updated_at: '2018-04-07T22:11:52+00:00'
type: issue
status: closed
closed_at: '2018-03-14T22:36:50+00:00'
---

# Original Description
Before in version 2.4.4 size detection is right
* VERSIONS:     XMRig/2.4.4 libuv/1.18.0 MSVC/2017
 * HUGE PAGES:   available, enabled
 * CPU:          Intel(R) Core(TM) i7-8700K CPU @ 3.70GHz (1) x64 AES-NI
 * CPU L2/L3:    1.5 MB/12.0 MB

Current version is wrong
* VERSIONS:     XMRig/2.4.5 libuv/1.19.0 MSVC/2017
 * HUGE PAGES:   available, enabled
 * CPU:          Intel(R) Core(TM) i7-8700K CPU @ 3.70GHz (1) x64 AES-NI
 * CPU L2/L3:    0.8 MB/12.0 MB

CPU-Z utility show L2 cache as 6x256 KBytes
![image](https://user-images.githubusercontent.com/4030018/36939456-7a69841a-1f42-11e8-9fa0-3b742a710bb3.png)


# Discussion History
## xmrig | 2018-03-04T05:25:49+00:00
@Foudge looks like cache fix need be fixed again, same family and model with older CPUs.
Thank you.

## Foudge | 2018-03-04T09:11:28+00:00
Yes, Intel reused model E, like the first generation of Core CPU (Solo and Duo, designed for mobile usage).
Maybe just check CPU have no L3 to be sure that all actual (and future!) Core i3/5/7 not touched by the fix.
I will see that closer.

edit: maybe I should use ExtModel instead of Model, and add L3 absence check

## Foudge | 2018-03-04T11:43:21+00:00
@xmrig It should be ok with this commit : https://github.com/Foudge/xmrig/commit/b95041710c1f639ec7af53b7078fb96660a9cf9c
You can graft it in your repository ?

## 2010phenix | 2018-03-04T12:04:55+00:00
@Foudge it can be problem with VMware VDS things.. most of them "don't have" L3

## 2010phenix | 2018-03-04T12:45:59+00:00
PS @Foudge maybe find some useful hint in hwloc integration made by sebastianstolzenberg in: https://github.com/Bendr0id/xmrigCC/pull/24/commits/f05ee0d9e7b1d3d2756b6926cda448a1ed30b4d6

## Foudge | 2018-03-04T13:31:48+00:00
@2010phenix See my comment commit, I use now **ext_family** and **ext_model**, what I should have done from the beginning. Those ext versions were added because all values were already used with **family** and **model** (only 4 bits!), so they extend them to 8 bits.

But this current bug has no impact at all : the only important cache information is LLC (last level cache), so L2 or L3 depending on the processor, because it's used to calculate the number of thread in automatic mode.

## xmrig | 2018-03-04T19:18:20+00:00
@Foudge thank you, added your changes.
@VSergey @2010phenix Anyway for this issue (modern CPUs) as mentioned above, it just cosmetic, no negative impact.

## xmrig | 2018-03-14T22:36:50+00:00
Fixed in v2.5.0.

## snipeTR | 2018-04-04T21:59:17+00:00
this v2.4.3 **right CPU** info.: https://prnt.sc/j0z2t4
![indir](https://user-images.githubusercontent.com/31975916/38336992-70994194-386c-11e8-986b-9feb27ef6e9e.png)

this v2.5.2 **wrong CPU** info: https://prnt.sc/j0z2zn
![indir 1](https://user-images.githubusercontent.com/31975916/38337007-772593f0-386c-11e8-9eea-2c3e427b2fc5.png)

this v2.6.0 **wrong CPU** info: https://prnt.sc/j0z34l
![indir 2](https://user-images.githubusercontent.com/31975916/38337012-7bec8808-386c-11e8-82ee-560b66f5823e.png)


## Foudge | 2018-04-05T07:28:46+00:00
The C2D E7400 has 3MB L2 cache ;)
https://ark.intel.com/products/36500/Intel-Core2-Duo-Processor-E7400-3M-Cache-2_80-GHz-1066-MHz-FSB

edit: I see that you use automatic mode and number of thread go from 2 to 1 (because it based on L2 cache size) => manually set number of thread to 2 in the config file

## snipeTR | 2018-04-05T12:51:20+00:00
OK. but the old version gives 25 h / s. It gives 14 h / s including 2.6 version.

## snipeTR | 2018-04-05T12:52:06+00:00
Automatic thread detection not working

## Foudge | 2018-04-05T13:21:31+00:00
Like I said in my edit, the automatique mode choose number of thread basing on last level cache size and other things (algo variation and max-cpu-usage parameter). Automatic mode is ok but not optimal.
Open your config.json file and replace `"threads": null` by `"threads": 2` 

edit: you have 32bit Windows?

## snipeTR | 2018-04-05T13:44:17+00:00
Is not the "thread" parameter automatic?

## snipeTR | 2018-04-07T19:39:53+00:00
yes 32bit windows and not a auto threads count. please help

## Foudge | 2018-04-07T22:11:52+00:00
I don't understand. You use command line or config file ?
-  Command line: add `--threads=2`
- config.json file : replace `"threads": null` by `"threads": 2` (if `null`, automatic mode is used)

# Action History
- Created by: VSergey | 2018-03-03T21:25:47+00:00
- Closed at: 2018-03-14T22:36:50+00:00
