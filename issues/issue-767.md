---
title: 'Config autosave '
source_url: https://github.com/xmrig/xmrig/issues/767
author: xmrig
assignees: []
labels:
- enhancement
created_at: '2018-09-30T13:13:59+00:00'
updated_at: '2018-10-10T22:22:42+00:00'
type: issue
status: closed
closed_at: '2018-10-10T22:22:42+00:00'
---

# Original Description
In version 2.8 default behavior for CPU miner changed, if miner use automatic threads configuration and config file, miner will override config file with suggested settings in [advanced](https://github.com/xmrig/xmrig/issues/563) format for easy tuning.

To restore old behavior should set config option `"autosave": false,`, same option also added to GPU miners, but GPU miners was override config by default.

# Discussion History
## LearnMiner | 2018-09-30T13:56:01+00:00
you should make  1 exe with cpu and gpu 

## xmrig | 2018-09-30T14:05:01+00:00
I will probably add OpenCL part to CPU miner in v2.9, OpenCL now not adds any additional external dependency on compile and runtime also not restrict compiler version. CUDA is much more complicated thing.
Thank you.

## LearnMiner | 2018-09-30T15:36:13+00:00
then will work cpu and amd in same exe?

Nice

## 2010phenix | 2018-09-30T21:46:03+00:00
@LearnMiner what for this monster need? who want combo monster already used xmr-stack.
 am always think that xmrig used because they at first compact and only at second have few nice futures....

## xmrig | 2018-10-01T11:05:38+00:00
@2010phenix I don't think OpenCL part will make a monster.

#### Positive changes
1. It's optional, OpenCL can disabled on compile time.
2. OpenCL not add any external dependency, all required headers included to source tree, no need install AMD SDK or any other SDK.
3. OpenCL loaded in runtime, so if it unavailable it just will be disabled, no crash due missing libraries.
4. CPU mining code is already included to AMD miner and a lot of other code shared between miners.
5. Command line options is ready to use together without changes.

xmr-stak required AMD APP SDK to build from source (2), and hard depends of OpenCL in runtime (3).

#### Negative changes
1. Config will need change, because both CPU and OpenCL threads now use same name `threads` in config.
2. Binary size will be increased, but we already lose this war since OpenSSL support added.

## 2010phenix | 2018-10-01T12:52:19+00:00
> 
> @2010phenix I don't think OpenCL part will make a monster.

@xmrig am not about code... only size ....

# Action History
- Created by: xmrig | 2018-09-30T13:13:59+00:00
- Closed at: 2018-10-10T22:22:42+00:00
