---
title: NiceHash Installation not using GPU for mining, only CPU.
source_url: https://github.com/xmrig/xmrig/issues/2431
author: AshKitter
assignees: []
labels: []
created_at: '2021-06-08T20:09:17+00:00'
updated_at: '2021-06-17T06:11:21+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
I have a 1650 super and an i5 9400f with Win10 for OS and am trying to mine via NiceHash Quick Mine, which happens to start a XMRig window to do the actual mining. Once XMRig is open however it only uses my CPU for mining and does not utilize the GPU. I can confirm this via task manager showing near 0% GPU utilization. 
![image](https://user-images.githubusercontent.com/75557334/121250290-91551a80-c873-11eb-949b-7e01fd062fec.png) 



# Discussion History
## Lonnegan | 2021-06-09T05:44:38+00:00
Nicehash normally uses Monero (RandomX) for CPUs and Ethereum for GPUs. xmrig doesn't support ETH and RandomX on GPUs is possible but not useful, reaching only ~2% of the profit of ETH on an NVIDIA Turing GPU:

![eth-vs-randomx](https://user-images.githubusercontent.com/60088495/121302045-5f869700-c8f9-11eb-96b1-8b5303fc0199.png)

Allow Nicehash to use an additional miner (e.g. NBminer) for mining ETH on the GPU!

## Blisk | 2021-06-12T14:39:36+00:00
> 
> 
> Nicehash normally uses Monero (RandomX) for CPUs and Ethereum for GPUs. xmrig doesn't support ETH and RandomX on GPUs is possible but not useful, reaching only ~2% of the profit of ETH on an NVIDIA Turing GPU:
> 
> ![eth-vs-randomx](https://user-images.githubusercontent.com/60088495/121302045-5f869700-c8f9-11eb-96b1-8b5303fc0199.png)
> 
> Allow Nicehash to use an additional miner (e.g. NBminer) for mining ETH on the GPU!

So you are telling mining XMR with GPU is waste of time and money? XMR should only be mined with CPU?

## Lonnegan | 2021-06-17T06:11:21+00:00
> So you are telling mining XMR with GPU is waste of time and money? XMR should only be mined with CPU?

Yes, RandomX has been designed for this.

# Action History
- Created by: AshKitter | 2021-06-08T20:09:17+00:00
