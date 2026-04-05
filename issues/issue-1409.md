---
title: 'XMRig does not work with RX 460, RX 560 '
source_url: https://github.com/xmrig/xmrig/issues/1409
author: senski7
assignees: []
labels: []
created_at: '2019-12-12T17:51:13+00:00'
updated_at: '2022-05-13T09:29:24+00:00'
type: issue
status: closed
closed_at: '2021-04-12T15:10:22+00:00'
---

# Original Description
Is this normal ?

[2019-12-12 19:12:12.779]  ocl  use profile  rx  (2 threads) scratchpad 2048 KB
|  # | GPU |  BUS ID |    I |  W | SI | MC |  U |  MEM | NAME
|  0 |   0 | 01:00.0 |  160 |  8 |  0 |  - |  8 |  320 | Radeon(TM) RX 460 Graphics (Baffin)
|  1 |   0 | 01:00.0 |  160 |  8 |  0 |  - |  8 |  320 | Radeon(TM) RX 460 Graphics (Baffin)
[2019-12-12 19:12:13.521]  ocl  error CL_MEM_OBJECT_ALLOCATION_FAILURE when calling clCreateBuffer with buffer size 2181038080
[2019-12-12 19:12:13.523]  ocl  error CL_MEM_OBJECT_ALLOCATION_FAILURE when calling clCreateBuffer with buffer size 2181038080
[2019-12-12 19:12:13.591]  ocl  thread #0 failed with error RandomX dataset is not available
[2019-12-12 19:12:13.652]  ocl  thread #1 failed with error RandomX dataset is not available
[2019-12-12 19:12:13.702]  ocl  thread #0 self-test failed
[2019-12-12 19:12:13.720]  ocl  thread #1 self-test failed
[2019-12-12 19:12:13.722]  ocl  disabled (failed to start threads)

# Discussion History
## dedizones | 2019-12-13T10:07:52+00:00
Hi,
Which version xmrig do you use?
RX 4GO or 8GB

## senski7 | 2019-12-13T12:51:38+00:00
I tried all versions after 5.0.0

## setuidroot | 2019-12-13T17:46:30+00:00
> I tried all versions after 5.0.0

He meant how much RAM does your GPU have?

You need a GPU with at least 4GB of RAM to allocate the 2080 MB RandomX dataset, otherwise you'll need to turn on the dataset-host option so that the RandomX dataset will run on your motherboard's RAM instead (you'd need at least 4GB of system RAM for that to work.)

It's impossible to help you without more information... like a copy of your config.json file and information about your hardware.  Without that, I can only answer: No, that is not normal.  Albeit errors can be fairly common depending on your hardware and config.json file.

## D0nVitalio | 2021-02-14T22:00:57+00:00
Hi. I have same problem. XMrig version 6.8.1, RX460 4Gb, Win10x64, Radeon driver v.21.1.1, Huge pages enabled, 8GB ram.
ocl error CL_MEM_OBJECT_ALLOCATION_FAILURE when calling clCreateBuffer with buffer size 2181038080

## SChernykh | 2021-02-14T22:19:30+00:00
I have RX560 4GB on Windows 7 and it works there, but there's little point to mine RandomX with GPU. It's only 260 h/s.

## ghost | 2021-02-15T12:31:03+00:00
Mining Monero on GPU is not a good idea as RandomX is specifically for CPU hashing.

OT

Considering that GPU I personally suggest to mine Firo or ETC

## Spudz76 | 2021-02-17T04:38:54+00:00
Probably need to set the envvars
```
export GPU_FORCE_64BIT_PTR=1
export GPU_MAX_HEAP_SIZE=100
export GPU_USE_SYNC_OBJECTS=1
export GPU_MAX_ALLOC_PERCENT=100
export GPU_SINGLE_ALLOC_PERCENT=100
```

It's saying OpenCL only sees 320KB of memory which is what it would do without the above settings.

Also you might need more system ram.

# Action History
- Created by: senski7 | 2019-12-12T17:51:13+00:00
- Closed at: 2021-04-12T15:10:22+00:00
