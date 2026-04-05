---
title: No jobs when using GPU
source_url: https://github.com/xmrig/xmrig/issues/2672
author: curi0usJack
assignees: []
labels: []
created_at: '2021-11-05T14:53:47+00:00'
updated_at: '2021-11-05T16:36:33+00:00'
type: issue
status: closed
closed_at: '2021-11-05T16:36:33+00:00'
---

# Original Description
**Describe the bug**
When running on Linux (Arch) using --cuda and pointing to ethash.unmineable.com, I get no jobs. Brand new to mining, so I'm most certainly missing something obvious.

![image](https://user-images.githubusercontent.com/5608516/140529823-3770de4e-ec36-4058-8ad1-84a9f292fd2e.png)

Things work as expected when using cpu mining on rx. I've confirmed that I can reach the destination hosts on 3333, so I do not believe it to be a network/firewall issue. I've also tried kp and etchash. Same result. It only works with rx.

![image](https://user-images.githubusercontent.com/5608516/140530027-7f52a59c-aa6c-4688-b0e3-62e4ec956bc3.png)


# Discussion History
## curi0usJack | 2021-11-05T15:23:10+00:00
Also confirmed it's not a network issue. I see traffic going back and forth between hosts on the target port.

## SChernykh | 2021-11-05T15:36:21+00:00
xmrig doesn't support ethash, try kawpow. Also you need to specify the algorithm in the command line: `-a kawpow`

## Spudz76 | 2021-11-05T15:50:07+00:00
T-Rex is what you want, for ethash

## curi0usJack | 2021-11-05T16:36:33+00:00
Perfect. That worked great. 

Thanks guys!

# Action History
- Created by: curi0usJack | 2021-11-05T14:53:47+00:00
- Closed at: 2021-11-05T16:36:33+00:00
