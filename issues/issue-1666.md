---
title: Huge Pages +JIT randomly runs at only 11%
source_url: https://github.com/xmrig/xmrig/issues/1666
author: GoGitIt1
assignees: []
labels: []
created_at: '2020-04-30T03:07:15+00:00'
updated_at: '2024-02-26T15:28:05+00:00'
type: issue
status: closed
closed_at: '2020-08-19T01:22:19+00:00'
---

# Original Description
When I first boot and start XMrig, I have no problem running huge pages at 100%. However, I am having a frequent error on 5.11.0 and the last few versions where it will only start with less than the full 1168/1168 huge pages.

I am using Windows 8.1 with a Ryzen 3950X and 16GB of RAM. RAM usage was only around 4GB, the last time I encountered this issue. Reseting the computer seems to be the only thing that temporarily fixes this. Any ideas?

# Discussion History
## noebranco | 2020-05-08T15:23:43+00:00
I have been seeing this problem in a couple of PC's also... :-( With 5.11.1


## miningnome | 2021-02-09T23:49:05+00:00
For me it's clear, you have a 16cores processor with 32threads and only 16Gb or RAM. If you want to use the real power of your CPU you need 1Gb per each thread or at least 16Gb to use the 50% of your CPU with will make temp lower. Details of your CPU: https://www.pccomponentes.com/amd-ryzen-9-3950x-470-ghz

## joescalon | 2021-02-20T17:50:04+00:00
> For me it's clear, you have a 16cores processor with 32threads and only 16Gb or RAM. If you want to use the real power of your CPU you need 1Gb per each thread or at least 16Gb to use the 50% of your CPU with will make temp lower. Details of your CPU: https://www.pccomponentes.com/amd-ryzen-9-3950x-470-ghz

I have seen this quoted several times, but find no evidence you need 1GB of ram per thread. Even the xmrig documents say 1028x2mb of RAM for hugepages and 3x1GB ram for 1GB hugepages in linux. 

For anyone finding this issue from google search, if you are running any Window Home OS hugepages are not always reserved, even if you "run as admin", you will have to reboot nearly every time you close XMRig and open it again. Solution: Reboot every time, run Windows Pro, or install Linux on your PC or USB drive. 

## d4f5409d | 2024-02-26T15:27:50+00:00
Same issue here on Linux, but I have found a workaround to restart on and on until it starts with 100% again, however it still bothers me.

# Action History
- Created by: GoGitIt1 | 2020-04-30T03:07:15+00:00
- Closed at: 2020-08-19T01:22:19+00:00
