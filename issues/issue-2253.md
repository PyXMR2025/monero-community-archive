---
title: 1 GB pages lowers the hashrate in benchmark mode
source_url: https://github.com/xmrig/xmrig/issues/2253
author: DocBrown101
assignees: []
labels: []
created_at: '2021-04-11T08:44:43+00:00'
updated_at: '2021-04-11T09:48:41+00:00'
type: issue
status: closed
closed_at: '2021-04-11T09:47:57+00:00'
---

# Original Description
**Describe the bug**
If the benchmark is started with 1gb pages, the hashes reduce drastically.

**To Reproduce**
Simply compare both calls with each other.
./xmrig --bench=1M --randomx-1gb-pages
and without 1gb
./xmrig --bench=1M




# Discussion History
## SChernykh | 2021-04-11T08:48:56+00:00
Define "drastically". Do you get any red text for huge pages when starting the benchmark?

## DocBrown101 | 2021-04-11T09:05:33+00:00
Approximately 441 H/s less.

https://i.imgur.com/WnuSRoc.png
vs
https://i.imgur.com/2Ao5N6R.png

## SChernykh | 2021-04-11T09:22:40+00:00
Do you have any variance between test runs, i.e. maybe there are other programs running in the background that use CPU? 1 GB pages shouldn't cause more than 1-2% difference anyway.

## DocBrown101 | 2021-04-11T09:39:57+00:00
No, there is definitely nothing running in the background that requires CPU.

I also noticed that my system has about **5 watts less power consumption** when I run it with 1gb-pages.

Important, this occurs only in benchmark, if I mine over a pool I have about 1-2% more!


## DocBrown101 | 2021-04-11T09:48:41+00:00
No, it always occurs with me, even without benchmark. So I have closed it now.

# Action History
- Created by: DocBrown101 | 2021-04-11T08:44:43+00:00
- Closed at: 2021-04-11T09:47:57+00:00
