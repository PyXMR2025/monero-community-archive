---
title: API Produces no stats during Dev Fee
source_url: https://github.com/xmrig/xmrig/issues/1838
author: cyberlink1
assignees: []
labels: []
created_at: '2020-09-16T12:21:51+00:00'
updated_at: '2021-04-12T14:48:26+00:00'
type: issue
status: closed
closed_at: '2021-04-12T14:48:26+00:00'
---

# Original Description
**Describe the bug**
API Reports 0 stats during dev fee

**To Reproduce**
run xmrig and graph hash rate.

**Expected behavior**
I would expect it to report the stats

**Required data**
This is the time series I zoom in on.
```
[2020-09-16 06:46:38] dev donate started
[2020-09-16 06:46:38] new job from donate.ssl.xmrig.com:443 diff 1000225 algo cn/r height 458827
[2020-09-16 06:46:59] new job from donate.ssl.xmrig.com:443 diff 1000225 algo cn/r height 458827
[2020-09-16 06:47:17] speed 10s/60s/15m 228.9 553.8 987.8 H/s max 1196.3 H/s
[2020-09-16 06:47:38] dev donate finished
```
12 hr chart

![charts](https://user-images.githubusercontent.com/12261936/93336100-eb491800-f7ec-11ea-94be-097dc918abfc.png)

Zoom in to 6:46:38

![zoom-in](https://user-images.githubusercontent.com/12261936/93336149-fc922480-f7ec-11ea-8d2a-1485a46a4061.png)

I find it a little odd that the hash rate drops but that is not a huge deal as it is only dropping 10H/s


# Discussion History
## xmrig | 2020-09-16T13:11:57+00:00
What algorithm or coin do you actually mine? Seems to be algorithm switching happening.
P.S nice graphs is it something publicly available?

## cyberlink1 | 2020-09-16T17:56:34+00:00
Right now I am mining RYO coin which is cryptonight/gpu.

Thank you for the compliment on the Graphs. ;) I write  [mining-scheduler](https://github.com/cyberlink1/Mining-Scheduler) I have not promoted graphing yet so it is in the dev branch.

As part of the project I am working on integrating the different miner API's to node-exporter so you can import the data into Prometheus and graph it with Grafana. It even reads which miner you are using and what coin you are mining from the scheduler. 

## xmrig | 2020-09-16T19:02:24+00:00
Usually donate use same algorithm as current to avoid side effects of algorithm switching, but case very different: `cn/gpu` removed in recent versions and it also removed on donation servers, so it choice best suitable `cn/*` algorithm and it `cn/r`.

This algorithm requires some time for preparation on GPU and hashrate is different as well, so it is not a bug. You can also disable donations on some old AMD drivers switching to `cn/r` may cause GPU memory leak.

Another solution can be reverting back `cn/gpu` definitions on donation servers and rejecting it.
Thank you.


# Action History
- Created by: cyberlink1 | 2020-09-16T12:21:51+00:00
- Closed at: 2021-04-12T14:48:26+00:00
