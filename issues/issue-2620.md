---
title: CL_INVALID_BUFFER_SIZE error on macOS running with --opencl flag
source_url: https://github.com/xmrig/xmrig/issues/2620
author: puccaso
assignees: []
labels: []
created_at: '2021-10-09T21:51:20+00:00'
updated_at: '2021-10-13T22:06:36+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Bug: unable to use opencl on macos with intel graphics. 

**To Reproduce**
build on macos bigsur from latest git pull

**Required data**
```
 |  # | GPU |  BUS ID | INTENSITY | WSIZE | MEMORY | NAME
|  0 |   0 |     n/a |       320 |     8 |    640 | Iris Pro
[2021-10-09 22:47:58.462]  opencl   error CL_INVALID_BUFFER_SIZE when calling clCreateBuffer with buffer size 2181038080
[2021-10-09 22:47:59.443]  cpu      READY threads 3/3 (3) huge pages 0% 0/3 memory 6144 KB (6754 ms)
[2021-10-09 22:47:59.447]  opencl   thread #0 failed with error RandomX dataset is not available
[2021-10-09 22:47:59.453]  opencl   thread #0 self-test failed
[2021-10-09 22:47:59.453]  opencl   disabled (failed to start threads)

```

--cpu-max-threads-hint=100 -k --nicehash  --print-time==5 --api-worker-id=xx --rig-id=xx --verbose  --cpu-no-yield  --cpu-priority=5   --randomx-1gb-pages   --randomx-mode=fast --opencl
 
 

# Discussion History
## Spudz76 | 2021-10-10T05:00:06+00:00
Do you have >2.2GB of VRAM free?  RandomX is trash on GPUs anyway.

Also #2614 fixes other problems if it ever gets merged.

## puccaso | 2021-10-13T21:36:05+00:00
> Do you have >2.2GB of VRAM free? RandomX is trash on GPUs anyway.
> 
> Also #2614 fixes other problems if it ever gets merged.

I don't tbh, but every little helps. 

What kind of hash benefits do you see, even with the >2GB VRAM? 

## Spudz76 | 2021-10-13T22:06:36+00:00
332.3H/s on a GTX1060 6GB, about what [a CPU from 2008](https://xmrig.com/benchmark?cpu=Intel%28R%29+Core%28TM%292+Quad+CPU+Q8300+%40+2.50GHz) scores.  But even worse watts than 95W like that CPU which is $9 on eBay.

It's very very very bad which is good because that's how RandomX was designed (to be terrible on every GPU).

Compared to the identical physical card currently running ethash at 24.17MH/s which gives me equivalent XMR rate of 23.24KH/s.  Or, 69 (nice!) times what it brings in trying to do rx/0.  For the same watts...

So, it is completely dumb to bother rx/0 on GPUs.  You're getting an Intel Atom hashrate for 10 times the watts.  The network doesn't need your 323H/s either so that's not "helping", might as well help yourself to more XMR by not using rx/0.

# Action History
- Created by: puccaso | 2021-10-09T21:51:20+00:00
