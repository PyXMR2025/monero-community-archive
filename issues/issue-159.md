---
title: Best configuration for E-2620 V0 V3 and V4
source_url: https://github.com/xmrig/xmrig/issues/159
author: mastermks
assignees: []
labels:
- NUMA
created_at: '2017-10-19T19:58:59+00:00'
updated_at: '2019-08-02T12:37:51+00:00'
type: issue
status: closed
closed_at: '2019-08-02T12:37:51+00:00'
---

# Original Description
Hi,

I do not know what and the best configuration for E-2620.

I do not know how to compute the (cpu inffinty) for my E-2620.

I also think that if I put too many hearts sela works less well.

Is there a best practice for windows OS servers 2012R2 or 2016?

do you have an answer or a link to my questions.

thank you in advance

# Discussion History
## xmrig | 2017-10-20T10:28:08+00:00
First thing how many L3 cache your cpu has (15MB for V0 and 20MB for V4)
For maximum performance threads should fit into CPU cache, each thread required 2 MB or 4 MB (`--av 2`)
for 15 MB (15 / 2 = 7.5) so you need run 7 or 8 threads, for 20 more simple, 10 threads.

For calculate affinity you can use Windows calculator https://i.imgur.com/K3Xle56.png first you need bind threads to odd or even cores and extra (1-2 in your case) to some HT core.
Thank you.


## mastermks | 2017-10-20T22:25:35+00:00
Hello,

thanks a lot for your answer. I succeeded now to calculate my CPU affinity. on the other hand when I use the optionAV 2 I really have no good performance. and with two NUMA I can difference of H/s I do not really understand why.

## xmrig | 2017-10-22T04:56:54+00:00
av 2, also known as double hash or low power mode useful in some special cases:

* Not enough cores to utilize CPU cache, especially in virtual environment.
* Reduce threads count for leave more resources for other tasks, threads count reduced twice, but hashrate not.


## mastermks | 2017-10-22T21:25:45+00:00
OK thanks for the answers. I understand better now :)

## xmrig | 2019-07-29T02:19:42+00:00
If this issue still actual, please check v2.99.2-beta release #1077.
Thank you.

# Action History
- Created by: mastermks | 2017-10-19T19:58:59+00:00
- Closed at: 2019-08-02T12:37:51+00:00
