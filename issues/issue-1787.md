---
title: Performance Degradation on RX/0 - Ryzen 3700x
source_url: https://github.com/xmrig/xmrig/issues/1787
author: NCarter84
assignees: []
labels:
- stability
created_at: '2020-07-22T19:43:34+00:00'
updated_at: '2020-08-31T05:46:37+00:00'
type: issue
status: closed
closed_at: '2020-08-31T05:46:37+00:00'
---

# Original Description
After X time, the miner seems to drop hashrate by 50% for sometime, then it resumes normally hashrate for some X time, followed by hashrate cut by 50% again... Continue until you catch it.

I would expect the hashrate to stay the same until something happens IE: Stopping the miner, or doing CPU intensive tasks.

Windows 10, 19xx
Ryzen 3700x
Current Version: 6.2.3 msvc

This has been an ongoing problem; I had a 1st gen ryzen which had issues and recently upgraded this summer to the 3700x and continue to see these random drops.

![image](https://user-images.githubusercontent.com/35072980/88221178-13275f80-cc32-11ea-9908-3f84b33d9a29.png)


# Discussion History
## NCarter84 | 2020-07-22T19:46:06+00:00
Here is a longer snap shot of hashrate. This is a 4 day history report.

![image](https://user-images.githubusercontent.com/35072980/88221366-64375380-cc32-11ea-8593-ad94a4718cc6.png)


## Lonnegan | 2020-07-24T23:14:27+00:00
A known problem with the task scheduler of Windows 10 1903 and newer. See #1506 and https://github.com/xmrig/xmrig/issues/1506#issuecomment-597624636

## NCarter84 | 2020-07-24T23:29:04+00:00
@Lonnegan thanks.. Just read the thread. Seems like there is no known solution at this time? I typically get days of use prior to it being a pain... Then several pc restarts and resets to get it back... Or sometimes, I just have to not run the miner for a few hours. 

## Lonnegan | 2020-07-24T23:32:44+00:00
Well, that's not entirely accurate. To not bind the threads to certain cores solved the problem for me 99%.

## xmrig | 2020-08-31T05:46:37+00:00
https://xmrig.com/docs/miner/randomx-stability-troubleshooting-guide

# Action History
- Created by: NCarter84 | 2020-07-22T19:43:34+00:00
- Closed at: 2020-08-31T05:46:37+00:00
