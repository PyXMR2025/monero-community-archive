---
title: <DatasetHost::reg>:50 "out of memory" and <randomx_prepaer>:36 "invalid argument"
source_url: https://github.com/xmrig/xmrig/issues/1372
author: torreto12
assignees: []
labels: []
created_at: '2019-12-03T11:28:26+00:00'
updated_at: '2021-04-12T15:12:17+00:00'
type: issue
status: closed
closed_at: '2021-04-12T15:12:17+00:00'
---

# Original Description
Hello,
I have such a problem as in the picture,

![Bez tytułu](https://user-images.githubusercontent.com/58388749/70047242-f3222d80-15c7-11ea-879f-ee4946b89c58.jpg)

`<DatasetHost :: reg>: 50 "out of memory"`
`<andomx_prepaer>: 36 "invalid argument"`

1 GTX 750 1GB RAM
0 GTX 750ti 2GB RAM

![Bez tytułu2](https://user-images.githubusercontent.com/58388749/70047306-19e06400-15c8-11ea-8a7a-c894f7175d37.png)

Before randomx there was no problem of course. Anyone know how to solve the problem?


# Discussion History
## emily-pesce | 2019-12-06T05:15:35+00:00
Same

## Macgyver6778 | 2019-12-07T04:41:47+00:00
Ich habe das selbe PRoblem mit meiner Gigybyte GTX 750 TI 2GB.

## emily-pesce | 2019-12-07T06:52:27+00:00
I fixed this by adding more *system* memory (RAM). For whatever reason this new RandomX algorithm/xmrig imolementation (or perhaps something else) exceeded the measly 4GB that all other miners (albeit for other coins) had no issue with.  

## Moschus88 | 2020-01-02T21:48:08+00:00
same here @ GTX 1060 3 GB x 13 

## talukder13 | 2020-04-05T16:34:02+00:00

i have 5 gpu each one is gtx1050ti of 4gb RAM , 3  is working but rest 2 is not working showing   this message  thread 4 failed with error data set host:: reg>:50 out of memory in xmrig. please any one help ?

## Spudz76 | 2020-04-05T19:51:13+00:00
Requires 2336MB per GPU of system RAM free, with or without `dataset_host` option (required when GPU has less than 2336MB VRAM).  But either mode needs locked system RAM mapped across to the dataset.  Fix the problem with hugepages first, if those won't lock they can't be used by CUDA.

5 GPUs needs 16GB (about 12GB for dataset mapping, and the rest for the OS and stuff)
4GB is probably not enough even for one GPU (OS hogs a minimal amount), 8GB minimum really (unless super stripped nearly embedded style Linux? but even then I don't think so).

# Action History
- Created by: torreto12 | 2019-12-03T11:28:26+00:00
- Closed at: 2021-04-12T15:12:17+00:00
