---
title: 'Phoenix Miner 5.6d Windows/msvc error - '
source_url: https://github.com/xmrig/xmrig/issues/2587
author: marqanton
assignees: []
labels: []
created_at: '2021-09-17T18:22:12+00:00'
updated_at: '2025-06-16T20:49:11+00:00'
type: issue
status: closed
closed_at: '2025-06-16T20:49:11+00:00'
---

# Original Description
Hi  - I am trying to mine DOGE using my newly installed graphics card on Win 10. I am using unminable with phonix miner and seeing the below error. Can someone shed some light to my issue.
Actual log below:
------------------------------------------------------------------
Phoenix Miner 5.6d Windows/msvc - Release build
-----------------------------------------------

No CUDA driver found
Unknown OpenCL driver version! Hashrate and stale shares may suffer
OpenCL platform: OpenCL 2.1 AMD-APP (3302.6)
Available GPUs for mining:
GPU1: Radeon RX 580 Series (pcie 4), OpenCL 2.0, 8 GB VRAM, 36 CUs
Eth: the pool list contains 1 pool (1 from command-line)
Eth: primary pool: etchash.unmineable.com:3333
Starting GPU mining
GPU1: AMD driver 21.9.1
GPU1: AMD Compute mode is not turned on!
Eth: Connecting to ethash pool etchash.unmineable.com:3333 (proto: EthProxy)
GPU1: 29C 19% 5W
GPUs power: 4.8 W
Eth: Connected to ethash pool etchash.unmineable.com:3333 (157.245.124.70)
Listening for CDM remote manager at port 60080 in read-only mode
Eth: New job #52e28ca2 from etchash.unmineable.com:3333; diff: 4000MH
GPU1: Starting up... (0)
GPU1: Generating etchash light cache for epoch #225
Light cache generated in 2.9 s (15.1 MB/s)
GPU1: Failed to build program: clBuildProgram (-11)
GPU1: Failed to load kernels: clCreateKernel (-46)
Fatal error detected. Restarting.
Eth speed: 0.000 MH/s, shares: 0/0/0, time: 0:00



Eth speed: 0.000 MH/s, shares: 0/0/0, time: 0:00



Phoenix Miner 5.6d Windows/msvc - Release build
-----------------------------------------------

Waiting 15 s for previous instance to close
No CUDA driver found
Unknown OpenCL driver version! Hashrate and stale shares may suffer
OpenCL platform: OpenCL 2.1 AMD-APP (3302.6)
Available GPUs for mining:
GPU1: Radeon RX 580 Series (pcie 4), OpenCL 2.0, 8 GB VRAM, 36 CUs
Eth: the pool list contains 1 pool (1 from command-line)
Eth: primary pool: etchash.unmineable.com:3333
Starting GPU mining
GPU1: AMD driver 21.9.1
GPU1: AMD Compute mode is not turned on!
Eth: Connecting to ethash pool etchash.unmineable.com:3333 (proto: EthProxy)
GPU1: 29C 19% 5W
GPUs power: 4.6 W
Eth: Connected to ethash pool etchash.unmineable.com:3333 (165.227.119.242)
Listening for CDM remote manager at port 60080 in read-only mode
Eth: New job #40a3b12e from etchash.unmineable.com:3333; diff: 4000MH
GPU1: Starting up... (0)
GPU1: Generating etchash light cache for epoch #225
Light cache generated in 2.9 s (15.2 MB/s)
GPU1: Failed to build program: clBuildProgram (-11)
GPU1: Failed to load kernels: clCreateKernel (-46)
Fatal error detected. Restarting.
Eth speed: 0.000 MH/s, shares: 0/0/0, time: 0:00
Eth: New job #8e71a32d from etchash.unmineable.com:3333; diff: 4000MH



Eth speed: 0.000 MH/s, shares: 0/0/0, time: 0:00
Eth: New job #6732b109 from etchash.unmineable.com:3333; diff: 4000MH



Phoenix Miner 5.6d Windows/msvc - Release build
-----------------------------------------------

Waiting 15 s for previous instance to close
No CUDA driver found
Unknown OpenCL driver version! Hashrate and stale shares may suffer
OpenCL platform: OpenCL 2.1 AMD-APP (3302.6)
Available GPUs for mining:
GPU1: Radeon RX 580 Series (pcie 4), OpenCL 2.0, 8 GB VRAM, 36 CUs
Eth: the pool list contains 1 pool (1 from command-line)
Eth: primary pool: etchash.unmineable.com:3333
Starting GPU mining
GPU1: AMD driver 21.9.1
GPU1: AMD Compute mode is not turned on!
Eth: Connecting to ethash pool etchash.unmineable.com:3333 (proto: EthProxy)
GPU1: 28C 19% 5W
GPUs power: 4.6 W
Eth: Connected to ethash pool etchash.unmineable.com:3333 (157.245.124.70)
Listening for CDM remote manager at port 60080 in read-only mode
Eth: New job #a8e239b6 from etchash.unmineable.com:3333; diff: 4000MH
GPU1: Starting up... (0)
GPU1: Generating etchash light cache for epoch #225
Light cache generated in 2.8 s (16.0 MB/s)
Eth: New job #5ce1f10a from etchash.unmineable.com:3333; diff: 4000MH
Eth speed: 0.000 MH/s, shares: 0/0/0, time: 0:00
GPU1: Failed to build program: clBuildProgram (-11)
GPU1: Failed to load kernels: clCreateKernel (-46)
Fatal error detected. Restarting.



Eth speed: 0.000 MH/s, shares: 0/0/0, time: 0:00



Phoenix Miner 5.6d Windows/msvc - Release build
-----------------------------------------------

Waiting 15 s for previous instance to close



# Discussion History
## Spudz76 | 2021-09-17T22:07:35+00:00
This site is for xmrig?

[Here](https://bitcointalk.org/index.php?topic=2647654.0) is where PhoenixMiner support happens.

`Unknown OpenCL driver version! Hashrate and stale shares may suffer` is the important part, PhoenixMiner supports only very specific driver versions, yours is probably too new.  Also 5.7b is out so 5.6d is old now.  5.7b says it supports up to driver 21.8.1 but 5.6d only supported up to 21.4.1

So either downgrade drivers to 21.4.1, or upgrade PhoenixMiner to 5.7b (and still don't go beyond driver 21.8.1 until PhoenixMiner says it's supported).

# Action History
- Created by: marqanton | 2021-09-17T18:22:12+00:00
- Closed at: 2025-06-16T20:49:11+00:00
