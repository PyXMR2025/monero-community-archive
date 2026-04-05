---
title: device.globalMemSize() returns 0 in ocl_generic_rx_generator.cpp
source_url: https://github.com/xmrig/xmrig/issues/1235
author: komatom
assignees: []
labels:
- bug
- opencl
created_at: '2019-10-12T00:34:18+00:00'
updated_at: '2019-10-16T13:38:38+00:00'
type: issue
status: closed
closed_at: '2019-10-16T13:38:38+00:00'
---

# Original Description
Hey

in file generators/ocl_generic_rx_generator.cpp

line 43, device.globalMemSize() returns 0,

other functions are returning value, for example I tried device.freeMemSize()

Not sure if this is executed too early in the program execution, driver or race issue, same function on listing the available GPUs is working perfectly fine..

I think below calculations are not correct because of that..

I tried to fix it, but for now no luck..

Here is some debug data:

device mem: 0 
dataset_mem: 2315255744
per thread: 2129920
intensity calc: 1472
intensity -= : 512
Device compute units: 32

# Discussion History
## komatom | 2019-10-12T00:53:46+00:00
Strange if you call it like below, freeMemSize() before device.globalMemSize() then it works.. I guess OcLib works like that..

```
device.freeMemSize();
const size_t mem = device.globalMemSize();
```

## xmrig | 2019-10-12T03:01:08+00:00
Driver version? anyway it very strange because `device.freeMemSize()` also call `globalMemSize()`, https://github.com/xmrig/xmrig/blob/beta/src/backend/opencl/wrappers/OclDevice.cpp#L160

Might be better if OclDevice cache result of `globalMemSize` to avoid call OpenCL everytime.
Thank you.

## komatom | 2019-10-13T19:58:39+00:00
Hey

Driver version is 19.5.2, but I don't think it matters..

The only difference I see is that freememsize calls oclib from inside the device class, while globalmemsize is called through a reference/pointer to the device object

Hope you find why... This seems related to https://github.com/xmrig/xmrig/issues/1199 as it doesn't enable datasethost = true for cards that don't have enough memory

Regards


## komatom | 2019-10-14T10:44:28+00:00
@xmrig I tried to help with that, first time pull request on your project, may need some changes, but it works now with the recent changes in the PR.

Thanks

## komatom | 2019-10-16T13:38:38+00:00
Resolved.

# Action History
- Created by: komatom | 2019-10-12T00:34:18+00:00
- Closed at: 2019-10-16T13:38:38+00:00
