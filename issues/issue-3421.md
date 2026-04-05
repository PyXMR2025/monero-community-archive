---
title: Integrate ZLUDA for AMD CUDA mining
source_url: https://github.com/xmrig/xmrig/issues/3421
author: GermanAizek
assignees: []
labels:
- question
created_at: '2024-02-13T07:29:54+00:00'
updated_at: '2024-02-21T20:38:41+00:00'
type: issue
status: closed
closed_at: '2024-02-21T20:38:41+00:00'
---

# Original Description
**Describe the feature**
https://github.com/vosen/ZLUDA
it can give higher hashrate on amd video cards if cuda code is optimized

# Discussion History
## SChernykh | 2024-02-13T08:36:26+00:00
> ZLUDA is focused on end users
By user we mean someone who uses a CUDA program, e.g. a 3D artist using Blender. Developer developing a CUDA application is not an. While we would like to support developers in the future, right now the time constraints do not allow it

So nothing to integrate, just use it if you want?

## GermanAizek | 2024-02-13T09:35:58+00:00
@SChernykh,
it would be more convenient for users if xmrig itself determined need for use

## GerrFrog | 2024-02-14T05:53:30+00:00
I am developer of MINUX-Miner. I think I will integrate it

## GerrFrog | 2024-02-14T07:00:57+00:00
@SChernykh GermanAizek

## SChernykh | 2024-02-14T07:11:48+00:00
There is nothing to integrate, it's an end-user software. Just follow their instructions, it should already work with XMRig.

## GerrFrog | 2024-02-14T07:20:00+00:00
@SChernykh you mean just compile and run xmrig using this library? 


## ahorek | 2024-02-15T00:58:00+00:00
@GerrFrog I've tried it just for fun

download
https://github.com/vosen/ZLUDA/releases
add cuda plugin
https://github.com/xmrig/xmrig-cuda/releases
run it with
**zluda.exe xmrig.exe -- -a cryptonight-upx/2 -o stratum+tcp://xxx:1234 -u xxxxxxxxxxxx -p xxxxxxxxx --cuda --no-cpu**

my results with Radeon 7900 xtx 2Ghz for comparsion
opencl 82000h/s
zluda 67700h/s

performance may vary based on the algorithm, but it just works out of the box and there's nothing to be done on the xmrig's side "to integrate it".

# Action History
- Created by: GermanAizek | 2024-02-13T07:29:54+00:00
- Closed at: 2024-02-21T20:38:41+00:00
