---
title: help me understand why the GPU is fully loaded but miner is na
source_url: https://github.com/xmrig/xmrig/issues/3328
author: SuZhenYu2
assignees: []
labels: []
created_at: '2023-09-08T16:29:22+00:00'
updated_at: '2025-06-18T22:21:47+00:00'
type: issue
status: closed
closed_at: '2025-06-18T22:21:47+00:00'
---

# Original Description
![image](https://github.com/xmrig/xmrig/assets/17267209/fa8dc67f-1554-46d6-a720-b5f355df8dbf)


# Discussion History
## Spudz76 | 2023-09-09T03:50:02+00:00
RandomX requires FP64 support, and Orin AGX has none.

https://forums.developer.nvidia.com/t/jetson-agx-orin-tops-cuda-cores-explained/252426/6

Same thing occurs on old Fermi cores which also had no FP64 (but init and do nothing, the same)

Also 2GB of GPU memory is not enough for most RandomX dataset sizes, which must reside on the GPU.  Is this a Jetson or something?

## SuZhenYu2 | 2023-09-09T14:16:16+00:00
> RandomX requires FP64 support, and Orin AGX has none.
> 
> https://forums.developer.nvidia.com/t/jetson-agx-orin-tops-cuda-cores-explained/252426/6
> 
> Same thing occurs on old Fermi cores which also had no FP64 (but init and do nothing, the same)
> 
> Also 2GB of GPU memory is not enough for most RandomX dataset sizes, which must reside on the GPU. Is this a Jetson or something?

thanks. yes. i run on jetson orin agx. its has 64gb ram 
but use cpu model its ok. 

## Spudz76 | 2023-09-10T14:34:27+00:00
Somehow CUDA is saying 2048MB for the GPU... 2GB

Technically the GPU core (based on Ampere) has FP64 but they are forced into FP32 compatibility mode for more FP32 threads capability (which more of the non-mining CUDA apps use, so it's good for them).  Perhaps there is some way to switch them back to normal FP64 mode, and stop it from limiting to 2048GB memory, but it seems not.

# Action History
- Created by: SuZhenYu2 | 2023-09-08T16:29:22+00:00
- Closed at: 2025-06-18T22:21:47+00:00
