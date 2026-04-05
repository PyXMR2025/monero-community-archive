---
title: can't get current hash,could you help me?
source_url: https://github.com/xmrig/xmrig/issues/1296
author: xcoin-dev
assignees: []
labels: []
created_at: '2019-11-16T21:28:35+00:00'
updated_at: '2019-11-18T09:02:11+00:00'
type: issue
status: closed
closed_at: '2019-11-18T09:02:11+00:00'
---

# Original Description
when i use xmrig 2.14.1,
program can read current L2 cache
XMRig/2.14.1 gcc/5.4.0
INFO[0000]  * LIBS         libuv/1.8.0
INFO[0000]  * CPU          Intel(R) Xeon(R) CPU E7-8880 v4 @ 2.20GHz (4) x64 AES AVX2
INFO[0000]  * CPU L2/L3    80.0 MB/220.0 MB


but when i use xmrig 5.0.The threads must be 80,now half of cpu not wrok.
if i change threads=160,get the lower hash,i know 1thread need 256k L2 cache,so 20M support 80 thread ,may be program get wrong L2 cache?i have 4 Physical CPU,L2 cache =80M
could you help me about it?
@xmrig 
![6Q%4XR(MYLZNN}1CPP3)R 4](https://user-images.githubusercontent.com/31024627/68999411-b6351600-08fa-11ea-8a11-1369696585da.png)
![P1OZ$ R(QG0VY A6`JS(}R](https://user-images.githubusercontent.com/31024627/68999412-b6351600-08fa-11ea-8af9-b290e62c7af8.png)
![PO)AZFZGL EFH5 TTK7~E43](https://user-images.githubusercontent.com/31024627/68999413-b6cdac80-08fa-11ea-8a4b-f672eb4f45d6.png)


# Discussion History
## xmrig | 2019-11-16T22:53:04+00:00
Seems L2 cache size is correct: `80 * 256 KB = 20 MB` and 2.14 was wrong, actually I don't know why 2 cores per CPU package missing it should be 88C/176T in total according this http://www.cpu-world.com/CPUs/Xeon/Intel-Xeon%20E7-8880%20v4.html

If you feel you can use more threads easiest way is set `"rx": "cn",` to use 110 threads, setting threads as number will not work fine, because your machine has 4 NUMA nodes.
Thank you.

## xcoin-dev | 2019-11-16T23:03:59+00:00
I test randomx now.
how can i setting rx number
just like
"rx": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,……?
if i want use 110threads

## xcoin-dev | 2019-11-16T23:15:59+00:00
i try to set "rx": "cn",but hash is lower than 80threads.
cn use 112 threads,
rw most use 80 threads get current hash...
may be L2 cache limit threads...
thank you very much!

## xcoin-dev | 2019-11-16T23:21:04+00:00
but ....
L3 cache=220M=55 * 4
L2 cache=80M=20 * 4?
because i have  4 Physical CPU.
then xmrig5.0 L3cache is wrong or L2cache is wrong?

## xmrig | 2019-11-18T09:00:44+00:00
Miner show total cache size across all CPUs, on CPU-Z screenshot clearly visible 20 x 256 KB L2 cache, `20 * 256 * 4 = 20480 KB` or 20 MB.

## xcoin-dev | 2019-11-18T09:02:08+00:00
understand,thank you!!
:)

# Action History
- Created by: xcoin-dev | 2019-11-16T21:28:35+00:00
- Closed at: 2019-11-18T09:02:11+00:00
