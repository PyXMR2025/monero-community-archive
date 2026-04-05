---
title: xmrig is not taking all available threads on GPU. Debian 10
source_url: https://github.com/xmrig/xmrig/issues/2048
author: arrdguez
assignees: []
labels:
- question
created_at: '2021-01-20T02:27:03+00:00'
updated_at: '2021-04-12T14:23:24+00:00'
type: issue
status: closed
closed_at: '2021-04-12T14:23:24+00:00'
---

# Original Description

A clear and concise description of what the bug is.
Hi!

I am testing the xmrig on my Laptop: Debian 10 with a Nvidia GTX 1050. Xmrig is running OK with both CPU and GPU. The problem is that the GPU is taking only one thread of 36 ... see the picture below. 
There is no way in --help so see a possible solution. 

I am using this command line:
./xmrig  --cuda -o pool.minexmr.com:443 -u <XMRADDRES>  -p WORKERNAME  -k --tls

I am using CPU and GPU at the same time for this example but I tried using only the GPU.
I share a picture just to help to help me.

All the best ...

![Screenshot_2021-01-19_20-21-34](https://user-images.githubusercontent.com/12154883/105118531-3cfff880-5a94-11eb-8441-d4850d4da2f9.png)


# Discussion History
## snipeTR | 2021-01-20T07:05:09+00:00
Please use config wizard.

## Lonnegan | 2021-01-20T14:40:44+00:00
Don't mine Monero with a GPU. RandomX is ja pure CPU algo, GPUs do very bad on RandomX. Mine something with you GPU, which is made for GPUs like ETH, Haven or Ravencoin.

## SChernykh | 2021-01-20T15:58:53+00:00
GPU mining uses 1 CPU thread, that's correct. You can see Intensity = 320 (GPU threads) which is also correct for GTX 1050.

## Spudz76 | 2021-01-21T22:07:44+00:00
As the CPU does no "work" in close involvement with the GPU it only needs one thread, for communications.
The CPU simply double-checks the result the GPU sent back after sending it a job, which does not need additional threading.
There are a whole bunch of threads (warps) happening on the GPU.  Think of the single CPU thread handling the GPU as a network connection, nothing more.

# Action History
- Created by: arrdguez | 2021-01-20T02:27:03+00:00
- Closed at: 2021-04-12T14:23:24+00:00
