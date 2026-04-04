---
title: Monerod.exe excessive memory usage
source_url: https://github.com/monero-project/monero/issues/4189
author: dfg3hz5zqtwz46hw6
assignees: []
labels: []
created_at: '2018-07-29T13:27:44+00:00'
updated_at: '2019-03-26T16:48:13+00:00'
type: issue
status: closed
closed_at: '2019-03-26T16:48:13+00:00'
---

# Original Description
Hi, whenever I leave my node running for a longer time (10+ hours) without using the device and check on it later the memory usage suddenly spikes to around 90% ![spike1](https://user-images.githubusercontent.com/21203981/43366710-77725588-9342-11e8-9bf9-b3587f795383.png) (though I believe this is an error in Task Manager because it doesn't update when the device is not being used) and makes the device very slow and almost unusable. 
When I then restart the node it goes back to normal memory usage ![spike2](https://user-images.githubusercontent.com/21203981/43366711-778ca474-9342-11e8-9f39-e59cc8db8344.png) but it happens again after a few hours.

The only related issue I could find is #2732 but for me it also happens when my node is already fully synced. 

I am using the latest Windows 10 version and the latest CLI version (v0.12.3.0, point release 3) but this has also happened on previous CLI versions.

# Discussion History
## vtnerd | 2018-07-30T18:10:36+00:00
I'm not sure on the specifics of how Windows reports memory, but LMDB uses the file page cache in such a way that naive reading of OS memory statistics make `monerod` look-like a memory hog. However, that memory can typically be reclaimed quickly without `monerod` action, so its not the same thing as `monerod` requesting large chunks of "private" memory. The device "being unusable" is not enough information unfortunately, because the I/O could be maxed out trying to read block information for peers requesting data. The preview image for disk usage suggests lots of disk activity.

It would be more helpful to get the process specific statistics for `monerod` memory usage, the number of connected peers, and disk usage information.

## trasherdk | 2018-07-30T18:36:36+00:00
I'm running monerod, masarid and aeond on an old laptop. No problem what so ever.
This old Compaq has 2 GB memory and 100 GB disk.
Slackware 14.2 x86_64 Intel(R) Core(TM)2 Duo CPU     T8100  @ 2.10GHz

![image](https://user-images.githubusercontent.com/5003891/43416084-88e10af6-9461-11e8-8d8b-4ce890cb0b6f.png)


## dfg3hz5zqtwz46hw6 | 2018-07-31T00:11:35+00:00
@vtnerd would screenshots of Resource Monitor and RAMMap be enough for memory usage and disk usage or is there anything else I can do to provide better information? 
Is typing "status" into the CLI enough info for how many peers are connected?

## moneromooo-monero | 2018-08-16T19:06:38+00:00
The right test is:
- wait till your reporting says monerod is using most of the RAM on your computer
- start some other memory hungry process and see if anything dies
- if not, check what your reporting says about monerod RAM usage

## moneromooo-monero | 2018-09-12T08:54:40+00:00
Did you try that ?

## dfg3hz5zqtwz46hw6 | 2019-03-26T16:48:13+00:00
Hi, I am very sorry for not replying sooner. 

This issues seems resolved. Like @moneromooo-monero suggested opening another "memory hungry process" slowly gives RAM back from monerod. 
This will take a while and makes the PC very slow and barely usable for a few minutes but it will be fine afterwards.

#fixed #resolved

# Action History
- Created by: dfg3hz5zqtwz46hw6 | 2018-07-29T13:27:44+00:00
- Closed at: 2019-03-26T16:48:13+00:00
