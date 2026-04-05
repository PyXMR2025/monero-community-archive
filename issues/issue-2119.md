---
title: I have two AMD Epyc CPU each has 32 core, total 64 core ,but only used 32 core
source_url: https://github.com/xmrig/xmrig/issues/2119
author: toplinuxsir
assignees: []
labels:
- question
created_at: '2021-02-19T03:30:09+00:00'
updated_at: '2021-03-02T07:48:25+00:00'
type: issue
status: closed
closed_at: '2021-03-02T07:48:25+00:00'
---

# Original Description
I have two AMD Epyc CPU each has 32 core, total 64 core ,but only used 32 core
How to use all the 64 core to mine ?
Thanks!

# Discussion History
## ghost | 2021-02-19T07:08:36+00:00
Add -t 64 on your line of code (if you have them on the same motherboard)

## Lonnegan | 2021-02-19T13:10:52+00:00
Which Epyc model? Which coin?

## toplinuxsir | 2021-02-20T11:44:48+00:00
@ScardracS  , add -t 64 It doese not work !
@Lonnegan.  AMD EPYC 7502P 32-Core

## ghost | 2021-02-20T11:56:19+00:00
> @ScardracS , add -t 64 It doese not work !
> @Lonnegan. AMD EPYC 7502P 32-Core

What it said?

## Lonnegan | 2021-02-20T12:07:32+00:00
-t is deprecated. You have to edit the config.json file.

Eypc 7502P has 128 MB L3 cache and therefor enough cache for 64 RandomX threads (2 MB scratchpad per thread). If you mine RandomX (e.g. Monero) your EPYC should run with 64 threads automatically.

Unless you mine a CN-heavy coin like Haven. CN-Heavy has 4 MB scratchpads per thread. Here Epyc 7502P can only start 32 threads without flooding the cache!

## toplinuxsir | 2021-02-20T12:52:21+00:00
@Lonnegan I mine Monero ， But only one CPU (32 core) used, how to configure 

## SChernykh | 2021-02-20T12:56:37+00:00
Use https://xmrig.com/wizard to create minimal config and XMRig will automatically generate optimal config out of it when it starts.

## Lonnegan | 2021-02-20T23:09:17+00:00
@toplinuxsir The Epyc 7502P is a single socket CPU. You can't use it in a dual socket system! The suffix P stands for single socket. If you want to use two you have to drop in 2x Epyc 7502 w/o suffix P.

## toplinuxsir | 2021-02-21T04:30:57+00:00
@Lonnegan  Thanks , I got it!

## toplinuxsir | 2021-03-01T23:34:53+00:00
@Lonnegan I have another question : I have Epyc 7502p CPU , but the hashrate only： 
![image](https://user-images.githubusercontent.com/1111353/109573206-8af32c00-7b29-11eb-836b-c315cd9f9c4a.png)
，
But the randomx benchmark(https://xmrig.com/benchmark) hashrate is : 26698.21, Huge difference 
What's the problem ? Thanks 


## Lonnegan | 2021-03-01T23:56:05+00:00
@toplinuxsir Can you post the whole window, including the initial lines at the beginning? :)

## toplinuxsir | 2021-03-02T00:13:23+00:00
@Lonnegan 
![image](https://user-images.githubusercontent.com/1111353/109576651-2509a300-7b2f-11eb-9edc-a419fd548171.png)


## Lonnegan | 2021-03-02T00:29:49+00:00
@toplinuxsir You are not mining RandomX algo (Monero), you are mining Cryptonight-Heavy (Haven). Here for the 
32C cpu EPYC 7502P the hashrate ~2300 H/s is quite normal :)

Example:

AMD FX-8300
- RandomX => 1300 H/s
- CN-Heavy => 180 H/s

AMD Ryzen 3900X
- RandomX => 13000 H/s
- CN-Heavy => 1250 H/s

The point is that each thread of the RandomX algo uses only 2 MB scratchpad size, whereas CN-heavy uses 4 MB. So CN-Heavy can only be mined by CPU with plenty of cache.

## toplinuxsir | 2021-03-02T00:30:45+00:00
@Lonnegan  How to mining RandomX algo ?  how to configure ? Thanks !

## xmrig | 2021-03-02T07:48:25+00:00
I guess the answer to your last question is more simple than disable donation and you can figure it out by yourself. 10 days ago it was already said that you might mine wrong algorithm.
Thank you.

# Action History
- Created by: toplinuxsir | 2021-02-19T03:30:09+00:00
- Closed at: 2021-03-02T07:48:25+00:00
