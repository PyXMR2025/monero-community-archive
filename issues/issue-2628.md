---
title: '[Feature request] Link GPU to one pool, CPU to another'
source_url: https://github.com/xmrig/xmrig/issues/2628
author: Letme
assignees: []
labels: []
created_at: '2021-10-12T16:31:15+00:00'
updated_at: '2021-10-13T06:04:03+00:00'
type: issue
status: closed
closed_at: '2021-10-13T05:52:26+00:00'
---

# Original Description
I am mining Monero with RandomX and as already mentioned couple of times the GPU mining for RandomX is just waste of energy. So what I would love to have is that monero would be mined by CPU, but something else (lets say dero) would be mined by GPU at the same time. I would assume that all would run the same, just a bit more configuration?

# Discussion History
## Lonnegan | 2021-10-12T21:44:05+00:00
Just run xmrig twice, e.g. in different folders, one with config for CPU and CUDA/OpenCL disabled, and the other config vice versa.

## Spudz76 | 2021-10-12T21:44:14+00:00
Run separate folders and xmrigs.  One config.json set up for CPU enabled GPUs disabled, and the other GPU enabled and CPU disabled.  And change the miner rig-id or identifier in the password, if you are sending both to the same pool (like `rig-gpu` or something).

Also I set all the cpu related things false, GPU mode doesn't need hugepages or MSRs or ASM or AES and might as well not use them if the CPU one is managing all those features (for the CPU backend).  I don't know if it has better performance but might as well not have them clashing and stealing each others hugepages.

## Letme | 2021-10-13T05:52:26+00:00
I ran it twice with different configurations using `--config` flag. For me this solution is good enough, so I am closing the ticket.

## Spudz76 | 2021-10-13T06:04:03+00:00
Yes that is effectively equivalent and smaller.  I compile different executables depending if CPU or GPU, and disable algos my equipment can't do, so I prefer the full clone of the folder approach just to ensure nothing clobbers.

# Action History
- Created by: Letme | 2021-10-12T16:31:15+00:00
- Closed at: 2021-10-13T05:52:26+00:00
