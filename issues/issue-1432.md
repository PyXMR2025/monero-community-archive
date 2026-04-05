---
title: 0 Hashrate
source_url: https://github.com/xmrig/xmrig/issues/1432
author: septuig
assignees: []
labels: []
created_at: '2019-12-16T13:12:12+00:00'
updated_at: '2019-12-19T13:51:11+00:00'
type: issue
status: closed
closed_at: '2019-12-19T13:51:11+00:00'
---

# Original Description
Hi
When I started xmrig 5.3 with default config file, the Hashrate is 0, My CPUs are Intel  2*E5-2680v2@Win10 64x. 4g memory. What's the optimized configuration for XMR? Thank you. 
![image](https://user-images.githubusercontent.com/38321812/70910348-83da1e00-204a-11ea-9365-588a6b72099e.png)



# Discussion History
## pawelantczak | 2019-12-16T13:50:42+00:00
Too less RAM I believe. 

## dedizones | 2019-12-16T22:53:27+00:00
Virtualisation ?

## SChernykh | 2019-12-17T09:56:22+00:00
You have 4 GB of memory and 2 NUMA nodes, so you need 4 GB for datasets and some more memory (1+ GB) for the OS. You'll have to disable NUMA in config.json to be able to get more than 0 h/s.

## Spudz76 | 2019-12-17T23:01:56+00:00
Or upgrade to 8GB

## septuig | 2019-12-18T14:27:37+00:00
Thank you all, upgraded to 16G, got 8.1K h/s.  any parameter can be changed to obtain more hare? 

## SChernykh | 2019-12-18T16:36:14+00:00
Run XMRig with administrator privileges to get more hashrate.

## septuig | 2019-12-19T13:13:59+00:00
To got more hashrate, whether need to set affinity or threads? if so, how to config, thank you.

![image](https://user-images.githubusercontent.com/38321812/71176167-2fca7600-22a4-11ea-9346-d682575cae52.png)


# Action History
- Created by: septuig | 2019-12-16T13:12:12+00:00
- Closed at: 2019-12-19T13:51:11+00:00
