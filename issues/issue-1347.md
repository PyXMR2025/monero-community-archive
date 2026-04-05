---
title: Six GPU Vega 56 Hashrate issue
source_url: https://github.com/xmrig/xmrig/issues/1347
author: gotminer
assignees: []
labels:
- opencl
- randomx
created_at: '2019-12-01T00:38:49+00:00'
updated_at: '2021-04-12T15:16:30+00:00'
type: issue
status: closed
closed_at: '2021-04-12T15:16:30+00:00'
---

# Original Description
Only getting around 500ish H/s on each thread. I've adjusted the intensity with no success. It will run stable up to about 1200, but it doesn't change the hash rate. I've also tested worksize at 8 and 16 with no change in hash rate.

Screenshots and full config file are attached.

[config.txt](https://github.com/xmrig/xmrig/files/3907714/config.txt)


![Capture](https://user-images.githubusercontent.com/44104559/69907751-fc817f00-13a8-11ea-8db7-bdf5a05c476e.JPG)
![sample](https://user-images.githubusercontent.com/44104559/69907752-ff7c6f80-13a8-11ea-941b-119ec524155a.JPG)




# Discussion History
## torreto12 | 2019-12-01T11:08:48+00:00
I have the same trouble. Did you solve it?

## gotminer | 2019-12-02T03:13:18+00:00
No I haven't figured out how to fix the issue. It has been said that mining randomx with gpu is a waste of electricity. Is this possibly because it is not possible to achieve the same hash rate with the same hardware mining the randomx algo? I have experienced a 5% decline in hash rate after other xmr hard forks, but never anything this dramatic. This drop is approx. 45%.

# Action History
- Created by: gotminer | 2019-12-01T00:38:49+00:00
- Closed at: 2021-04-12T15:16:30+00:00
