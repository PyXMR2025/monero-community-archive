---
title: KawPow support
source_url: https://github.com/xmrig/xmrig/issues/1709
author: enigmen
assignees: []
labels:
- bug
- kawpow
created_at: '2020-06-04T09:41:17+00:00'
updated_at: '2021-04-12T14:55:23+00:00'
type: issue
status: closed
closed_at: '2021-04-12T14:55:23+00:00'
---

# Original Description
Hello, pls help. I creat bat file
xmrig --no-cpu --cuda -a kawpow -o kawpow.eu.nicehash.com:3385 -u wallet.name -p x
but speed "n\a". What did I do wrong?
![изображение](https://user-images.githubusercontent.com/39157390/83741122-d7780c80-a668-11ea-873d-9b7c64740ff6.png)



# Discussion History
## xmrig | 2020-06-04T10:07:07+00:00
Please show full log from miner start.
Thank you.

## enigmen | 2020-06-04T10:13:28+00:00
![изображение](https://user-images.githubusercontent.com/39157390/83744684-8cacc380-a66d-11ea-83f3-2fb63c8a8c7f.png)


## SChernykh | 2020-06-04T12:03:16+00:00
@enigmen Can you try to start with only 1 GPU? Remove the second GPU from the generated config.json ("kawpow" section) and start without command line parameters. It might be a bug with multiple GPUs, be we need to confirm it first.

## enigmen | 2020-06-04T14:02:17+00:00
i remove one gpu, creat a new config.json, but speed again n\a
![изображение](https://user-images.githubusercontent.com/39157390/83766447-80d0f980-a68d-11ea-9bef-f5edc2a54787.png)


## SChernykh | 2020-06-05T07:32:17+00:00
I think the problem is that you have only 2482 MB available GPU memory when starting xmrig. I'll add more diagnostics for DAG initialization errors.

P.S. The next version will have smaller GPU memory usage, I'll make an update here when it's available.

## enigmen | 2020-06-05T07:43:38+00:00
ok, thanks.
Other miner (e.c. t-rex, gminer, nbminer) works, not problem.

## SChernykh | 2020-06-05T07:51:44+00:00
Yes, I need to make DAG initialization less memory consuming on GPU. But your GPU is on the edge already - 5-10 more epochs and even other miners won't work. You need to figure out how to make all GPU memory available for mining.

## enigmen | 2020-06-05T08:18:40+00:00
on two rx570 4gb working right :)

## SChernykh | 2020-06-06T09:42:56+00:00
@enigmen Can you try [release 6.0.1-beta](https://github.com/xmrig/xmrig/releases/tag/v6.0.1-beta) with [cuda plugin 6.1.0](https://github.com/xmrig/xmrig-cuda/releases/tag/v6.1.0)? It should work on your GPU. If it doesn't work, it should print some error message instead of just not mining.

## enigmen | 2020-06-07T17:29:09+00:00
hello, works
but miner autoexit, without error(

## Quake4 | 2020-06-10T18:07:57+00:00
yes, auto exit
![image](https://user-images.githubusercontent.com/29517243/84302411-e590c600-ab5d-11ea-83be-94ddae47daf3.png)

## SChernykh | 2020-06-10T19:02:21+00:00
@Quake4 your CPU doesn't support SSE4 which is used for KawPow verification on CPU. I'll see what can be done to fix it.

## SChernykh | 2020-06-10T19:55:33+00:00
@enigmen @Quake4 It should be fixed in #1729

## Quake4 | 2020-06-10T20:53:51+00:00
I re-launched it and it all worked out.

## enigmen | 2020-06-11T06:43:18+00:00
v.6.2.0 crazy
![изображение](https://user-images.githubusercontent.com/39157390/84353396-1f9ab000-abd0-11ea-8824-53bafefb97c6.png)
but v. 6.1.0. conect
![изображение](https://user-images.githubusercontent.com/39157390/84353510-5a9ce380-abd0-11ea-9363-edb98c9934d5.png)


## Quake4 | 2020-06-11T06:53:06+00:00
@enigmen the first screen is CPU mining. KawPaw isnt supported on CPU.
```opencl/cuda - disabled```

## SChernykh | 2020-06-11T07:11:08+00:00
@enigmen Check your config, or just copy your config from 6.1.0 folder. Also check which version of CUDA plugin you use there. If it's CUDA 11 version, maybe you need to update NVIDIA driver.

## enigmen | 2020-06-11T07:21:00+00:00
i copy config from 6.1.0 to 6.2.0
![изображение](https://user-images.githubusercontent.com/39157390/84356622-7fe02080-abd5-11ea-8cc2-9daefc4a7892.png)
![изображение](https://user-images.githubusercontent.com/39157390/84356661-91292d00-abd5-11ea-801c-3be61ffe2942.png)
but miner not see cuda device

## SChernykh | 2020-06-11T07:28:45+00:00
CUDA 10.2 requires 440.33 or newer driver, CUDA 11 requires 450.36 - can you check it?
Edit: you have 431.86 driver, update it.

## enigmen | 2020-06-11T09:22:04+00:00
i update driver, miner work, but auto exit(


## SChernykh | 2020-06-11T09:26:54+00:00
Did you compile the latest evo branch with the fix #1729 ? It won't work on your CPU without this fix.

## enigmen | 2020-06-11T09:52:35+00:00
how to t'his used i no understend?

## SChernykh | 2020-06-11T09:58:32+00:00
Just wait for the next release with the fix for your CPU.

# Action History
- Created by: enigmen | 2020-06-04T09:41:17+00:00
- Closed at: 2021-04-12T14:55:23+00:00
