---
title: OCL error
source_url: https://github.com/xmrig/xmrig/issues/1609
author: DogeZillaMeme
assignees: []
labels: []
created_at: '2020-03-25T18:10:00+00:00'
updated_at: '2020-08-29T04:49:27+00:00'
type: issue
status: closed
closed_at: '2020-08-29T04:49:27+00:00'
---

# Original Description
[2020-03-26 02:06:03.802]  rx   -- allocated 4416 MB huge pages   0% 0/2208 (3 ms)
[2020-03-26 02:06:08.584]  rx   #0 dataset ready (4782 ms)
[2020-03-26 02:06:09.523]  net  new job from 104.140.201.42:80 diff 83334 algo rx/0 height 2062307
[2020-03-26 02:06:10.834]  rx   #1 dataset ready (2249 ms)
[2020-03-26 02:06:11.803]  ocl  use profile  rx  (4 threads) scratchpad 2048 KB
|  # | GPU |  BUS ID |    I |  W | SI | MC |  U |  MEM | NAME
|  0 |   0 | 04:00.0 |  976 |  8 |  0 |  - |  8 | 1952 | GeForce RTX 2080 Ti
|  1 |   0 | 04:00.0 |  976 |  8 |  0 |  - |  8 | 1952 | GeForce RTX 2080 Ti
|  2 |   0 | 04:00.0 |  976 |  8 |  0 |  - |  8 | 1952 | GeForce RTX 2080 Ti
|  3 |   0 | 04:00.0 |  976 |  8 |  0 |  - |  8 | 1952 | GeForce RTX 2080 Ti
[2020-03-26 02:06:11.805]  ocl  GPU #0 compiling...
[2020-03-26 02:06:11.822]  ocl  GPU #0 compilation completed (18 ms)
[2020-03-26 02:06:11.822]  ocl  error CL_INVALID_VALUE when calling clGetProgramInfo
[2020-03-26 02:06:11.825]  ocl  GPU #0 compiling...
[2020-03-26 02:06:11.842]  ocl  GPU #0 compilation completed (17 ms)
[2020-03-26 02:06:11.842]  ocl  error CL_INVALID_VALUE when calling clGetProgramInfo
[2020-03-26 02:06:11.846]  ocl  GPU #0 compiling...
[2020-03-26 02:06:11.861]  ocl  GPU #0 compilation completed (16 ms)
[2020-03-26 02:06:11.861]  ocl  error CL_INVALID_VALUE when calling clGetProgramInfo
[2020-03-26 02:06:11.872]  ocl  GPU #0 compiling...
[2020-03-26 02:06:11.882]  ocl  GPU #0 compilation completed (11 ms)
[2020-03-26 02:06:11.882]  ocl  error CL_INVALID_VALUE when calling clGetProgramInfo
[2020-03-26 02:06:11.882]  ocl  READY threads 4/4 (79 ms)
 * CUDA         disabled (failed to load CUDA plugin)
[2020-03-26 02:06:14.195]  ocl  error CL_INVALID_WORK_GROUP_SIZE when calling clEnqueueNDRangeKernel for kernel blake2b_initial_hash
[2020-03-26 02:06:14.195]  ocl  error CL_INVALID_WORK_GROUP_SIZE when calling clEnqueueNDRangeKernel for kernel blake2b_initial_hash
[2020-03-26 02:06:14.195]  ocl  error CL_INVALID_WORK_GROUP_SIZE when calling clEnqueueNDRangeKernel for kernel blake2b_initial_hash
[2020-03-26 02:06:14.195]  ocl  error CL_INVALID_WORK_GROUP_SIZE when calling clEnqueueNDRangeKernel for kernel blake2b_initial_hash
[2020-03-26 02:06:14.196]  ocl  thread #1 failed with error CL_INVALID_WORK_GROUP_SIZE
[2020-03-26 02:06:14.196]  ocl  thread #0 failed with error CL_INVALID_WORK_GROUP_SIZE
[2020-03-26 02:06:14.196]  ocl  thread #3 failed with error CL_INVALID_WORK_GROUP_SIZE
[2020-03-26 02:06:14.196]  ocl  thread #2 failed with error CL_INVALID_WORK_GROUP_SIZE
[2020-03-26 02:06:59.762]  net  new job from 104.140.201.42:80 diff 83334 algo rx/0 height 2062308
 * CUDA         disabled (failed to load CUDA plugin)
[2020-03-26 02:07:09.673]  net  new job from 104.140.201.42:80 diff 55555 algo rx/0 height 2062308
 * CUDA         disabled (failed to load CUDA plugin)
[2020-03-26 02:07:11.430] speed 10s/60s/15m n/a n/a n/a H/s max n/a H/s
[2020-03-26 02:08:09.782]  net  new job from 104.140.201.42:80 diff 50000 algo rx/0 height 2062308
 * CUDA         disabled (failed to load CUDA plugin)
[2020-03-26 02:08:11.467] speed 10s/60s/15m n/a n/a n/a H/s max n/a H/s
[2020-03-26 02:09:07.638]  net  new job from 104.140.201.42:80 diff 50000 algo rx/0 height 2062309
 * CUDA         disabled (failed to load CUDA plugin)
[2020-03-26 02:09:11.508] speed 10s/60s/15m n/a n/a n/a H/s max n/a H/s


# Discussion History
## SChernykh | 2020-03-26T13:24:22+00:00
You have NVIDIA GPUs, so you need to download CUDA plugin: https://github.com/xmrig/xmrig-cuda/releases and extract it into the same folder as XMRig.

# Action History
- Created by: DogeZillaMeme | 2020-03-25T18:10:00+00:00
- Closed at: 2020-08-29T04:49:27+00:00
