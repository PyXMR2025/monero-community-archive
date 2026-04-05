---
title: Topology became empty, aborting!
source_url: https://github.com/xmrig/xmrig/issues/2439
author: mrbeandev
assignees: []
labels: []
created_at: '2021-06-13T02:59:12+00:00'
updated_at: '2021-06-16T12:16:18+00:00'
type: issue
status: closed
closed_at: '2021-06-16T12:16:18+00:00'
---

# Original Description
**Describe the bug**
I `wget https://github.com/xmrig/xmrig/releases/download/v6.12.2/xmrig-6.12.2-linux-x64.tar.gz`
and tried running it on my new VPS 16GB RAM [ 9.60 GHz (4 x 2.40 GHz) ].

I am getting this error 
```
root@3dm3:~/xmrig# ./xmrig --help
Topology became empty, aborting!
Segmentation fault
root@3dm3:~/xmrig#
```


**To Reproduce**
I tried `./xmrig` with config same error , also tried `./xmrig --help` same error.

**Expected behavior**
./xmrig with config should start mining and ./xmrig --help should give list of commands avaliable.

**Required data**

 - Error when i run xmrig `Topology became empty, aborting!
     Segmentation fault`
 - Ubuntu 20.04


<!--StartFragment-->
.... | ....
-- | --
Guaranteed CPU | 9.60 GHz (4 x 2.40 GHz)
RAM | 16384 MB + MB SWAP (used 241 MB)
Storage | 160 GB RAID (used 0.8 GB)
RAID Speed | 50 MB/s, 200 IOPS
Inode Limit | 0 (20000 per GB of storage) (used 0)
Port Speed | 100 Mbps

<!--EndFragment-->



# Discussion History
## Spudz76 | 2021-06-14T17:00:48+00:00
Probably need to build without hwloc

## mrbeandev | 2021-06-14T17:04:49+00:00
how can I get it?


## Spudz76 | 2021-06-15T13:56:05+00:00
Follow [build docs](https://xmrig.com/docs/miner/build) and use `-DWITH_HWLOC=OFF`...

## mrbeandev | 2021-06-16T12:16:18+00:00
thank you so much for the help its working now 😍😍

# Action History
- Created by: mrbeandev | 2021-06-13T02:59:12+00:00
- Closed at: 2021-06-16T12:16:18+00:00
