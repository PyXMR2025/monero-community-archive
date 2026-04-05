---
title: Performance regression on ARM8 between 6.3.2 and 6.3.5
source_url: https://github.com/xmrig/xmrig/issues/1884
author: jfikar
assignees: []
labels:
- arm
created_at: '2020-10-09T19:02:57+00:00'
updated_at: '2020-10-31T13:52:32+00:00'
type: issue
status: closed
closed_at: '2020-10-31T13:52:32+00:00'
---

# Original Description
I've observed a performance regression on ARM8 without AES instruction between xmrig 6.3.2 and 6.3.5

| algo | xmrig 6.3.2  | xmrig 6.3.5  | % regression |
| --------------- | --------------- | --------------- | --------------- |
| rx/0 | 110.5 H/s |  99.2 H/s | -10% |
| rx/arq | 1206.9 H/s | 996.4 H/s | -17%|

I have another ARM8 with AES instruction and there is no regression. I think, it may be related to the recent changes of the soft AES.

# Discussion History
## ghost | 2020-10-09T19:10:32+00:00
It was likely this issue: #1864
Try to compile dev branch, it must be fixed already.

## Lonnegan | 2020-10-13T06:40:08+00:00
Seems to be an ARM only issue. Tried an AMD Athlon II X2 240 (w/o hardware AES) in Wownero:

xmrig 6.3.2 => 275 H/s
xmrig 6.3.5 => 330 H/s

Here the new version is way faster.

## jfikar | 2020-10-13T13:49:10+00:00
My apologies, I just figured out that the new version was compiled with suboptimal CFLAGS. The correct results for two boards, one without and one with AES:

4x Cortex-A72, 2GHz, 1MB L2 cache, no AES


| algo | 6.3.0  | 6.3.2  | 6.3.5  | 6.4.0-dev |
| --------------- | --------------- | --------------- | --------------- | --------------- |
| rx/0 3 threads | 114.2 H/s | 122.9 H/s | 126.2 H/s | 116.2 H/s |
| rx/0 2 threads | 117.0 H/s | 115.0 H/s | 124.4 H/s | 121.7 H/s |
| rx/arq 4 threads| 1318.8 H/s | 1302.4 H/s | 1404.3 H/s| 1370.5 H/s |

4x Cortex-A73 2.4GHz (big) + 2x Cortex-A53 2.2GHz (little), 512MB L2 for little and 512MB L2 for big cores, AES

| algo | 6.3.0  | 6.3.2  | 6.3.5  | 6.4.0-dev |
| --------------- | --------------- | --------------- | --------------- | --------------- |
| rx/0 2 big + 2 little | 253.5 H/s | 244.3H/s | 248.3 H/s | 254.0 H/s |
| rx/arq 4 big + 2 little | 2947.3 H/s | 2836.4 H/s | 2898.3 H/s| 2937.8 H/s |

So there is no regression between 6.3.2 and 6.3.5 (actually it is a bit faster as reported by @Lonnegan).

But in the case without AES I observe a small regression between 6.3.5 and 6.4.0-dev.


## ghost | 2020-10-13T17:48:43+00:00
@jfikar
This branch allows manual selection of  soft aes implementation https://github.com/cohcho/xmrig/commit/130b20c9f27bcfa637c30f627de1878b383e2b64
Check experimentally how hashrate depends on soft_aes_mode option.
It accepts values 0,1,2,3,4.




## jfikar | 2020-10-15T14:59:27+00:00
That soft_aes_test branch of yours is interesting. Its benchmark recommends `soft_aes_mode=3` for my A72. I guess `soft_aes_mode=0` is auto-select.
```

[2020-10-15 16:58:13.033]  randomx  run: 0, idx: 0, speed: 177250.000000
[2020-10-15 16:58:13.133]  randomx  run: 0, idx: 1, speed: 237070.000000
[2020-10-15 16:58:13.233]  randomx  run: 0, idx: 2, speed: 249590.000000
[2020-10-15 16:58:13.333]  randomx  run: 0, idx: 3, speed: 226030.000000
[2020-10-15 16:58:13.333]  randomx  run: 0, fast_idx: 2, fast_speed: 249590.000000
[2020-10-15 16:58:13.433]  randomx  run: 1, idx: 0, speed: 177550.000000
[2020-10-15 16:58:13.533]  randomx  run: 1, idx: 1, speed: 237320.000000
[2020-10-15 16:58:13.633]  randomx  run: 1, idx: 2, speed: 249740.000000
[2020-10-15 16:58:13.733]  randomx  run: 1, idx: 3, speed: 225970.000000
[2020-10-15 16:58:13.733]  randomx  run: 1, fast_idx: 2, fast_speed: 249740.000000
[2020-10-15 16:58:13.833]  randomx  run: 2, idx: 0, speed: 177110.000000
[2020-10-15 16:58:13.933]  randomx  run: 2, idx: 1, speed: 237230.000000
[2020-10-15 16:58:14.033]  randomx  run: 2, idx: 2, speed: 249770.000000
[2020-10-15 16:58:14.133]  randomx  run: 2, idx: 3, speed: 226070.000000
[2020-10-15 16:58:14.133]  randomx  run: 2, fast_idx: 2, fast_speed: 249770.000000
[2020-10-15 16:58:14.133]  randomx  fast_speed: 249770.000000, threadsCount: 4
[2020-10-15 16:58:14.133]  randomx  use hashAndFillAes1Rx4 3
[2020-10-15 16:58:14.133]  randomx  use suggested hashAndFillAes1Rx4 4
```

The benchmark:

| soft_aes_mode | 1  | 2  | 3  | 4 |
| --------------- | --------------- | --------------- | --------------- | --------------- |
| rx/0 3 threads | 112.6 H/s | 110.9 H/s | 110.4 H/s | 111.7 H/s |
| rx/0 2 threads | 111.5 H/s | 118.0 H/s | 118.3 H/s | 116.5 H/s |
| rx/arq 4 threads| 1279.0 H/s | 1299.3 H/s | 1306.3 H/s| 1312.4 H/s |

Anyway, the 6.3.5 seems faster.


## ghost | 2020-10-15T15:09:45+00:00
@jfikar
It makes sense to have manual option since the best variant is different from auto-select.
`git log --format=oneline  v6.3.5..9fcc5426761981752f478115d300d5621992d5a6`
Try to bisect these commits and find exact commit with measurable slow down.
Since you've checked all possible soft AES implementations Then it isn't sub optimal auto select.

## jfikar | 2020-10-27T13:24:31+00:00
Well, it was a false alarm. I did more serious benchmarking and found no regression after v6.3.5 for rx/arq. On the opposite, it gets a bit better.

Initially, I had a lot of scatter in the benchmark results, even if I take 100 of 15 minutes average. The fastest and the slowest hashrate differs by approximately 120 H/s. This is with 2M huge pages enabled.

I discovered that the scatter gets two times smaller, if 1G huge pages are enabled. Then the scatter is around 60 H/s and the average of the 100 15 min averages is more trustworthy. And also the hashrate is higher by approximately 2%.

As a side note, it is not easy to enable the 1G huge pages on ARM64, but I'm going to open another issue for that.

I've seen the v6.4.0 has a better hashrate reporting. I'll try that as well.

| version | rx/arq   |
| --------------- | --------------- | 
| v6.3.5 | 1385 H/s |
|ebf259fa7c...|1394 H/s|
|9fcc542676... | 1413 H/s |



## SChernykh | 2020-10-27T13:53:50+00:00
> As a side note, it is not easy to enable the 1G huge pages on ARM64, but I'm going to open another issue for that.

Were you able to do it? Because ARM code doesn't enable 1G huge pages yet. In theory it should be as easy as switching an internal flag in XMRig code, but it has never been tested.

## jfikar | 2020-10-27T14:22:51+00:00
Yes, it [works](https://github.com/xmrig/xmrig/issues/1918).

# Action History
- Created by: jfikar | 2020-10-09T19:02:57+00:00
- Closed at: 2020-10-31T13:52:32+00:00
