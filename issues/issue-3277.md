---
title: Trying to build Ubuntu 23.04 Cuda
source_url: https://github.com/xmrig/xmrig/issues/3277
author: DHeinz70
assignees: []
labels: []
created_at: '2023-05-29T01:31:14+00:00'
updated_at: '2025-06-18T22:37:19+00:00'
type: issue
status: closed
closed_at: '2025-06-18T22:37:19+00:00'
---

# Original Description
**Describe the bug**
Trying to build, all steps work except last - 

1. git clone https://github.com/xmrig/xmrig-cuda.git
2. mkdir xmrig-cuda/build && cd xmrig-cuda/build
3. cmake .. -DCUDA_LIB=/usr/local/cuda/lib64/stubs/libcuda.so -DCUDA_TOOLKIT_ROOT_DIR=/usr/local/cuda
4. make -j$(nproc)  <----- this fails with....

make -j$(nproc)
[ 11%] Building NVCC (Device) object CMakeFiles/xmrig-cu.dir/src/AstroBWT/dero_he/xmrig-cu_generated_AstroBWT_v2.cu.o
[ 11%] Building NVCC (Device) object CMakeFiles/xmrig-cu.dir/src/KawPow/raven/xmrig-cu_generated_KawPow.cu.o
[ 16%] Building NVCC (Device) object CMakeFiles/xmrig-cu.dir/src/xmrig-cu_generated_cuda_extra.cu.o
[ 27%] Building NVCC (Device) object CMakeFiles/xmrig-cu.dir/src/RandomX/monero/xmrig-cu_generated_randomx_monero.cu.o
[ 27%] Building NVCC (Device) object CMakeFiles/xmrig-cu.dir/src/RandomX/xmrig-cu_generated_randomx.cu.o
[ 33%] Building NVCC (Device) object CMakeFiles/xmrig-cu.dir/src/xmrig-cu_generated_cuda_core.cu.o
[ 38%] Building NVCC (Device) object CMakeFiles/xmrig-cu.dir/src/AstroBWT/dero/xmrig-cu_generated_AstroBWT.cu.o
[ 44%] Building NVCC (Device) object CMakeFiles/xmrig-cu.dir/src/RandomX/arqma/xmrig-cu_generated_randomx_arqma.cu.o
[ 50%] Building NVCC (Device) object CMakeFiles/xmrig-cu.dir/src/RandomX/keva/xmrig-cu_generated_randomx_keva.cu.o
[ 55%] Building NVCC (Device) object CMakeFiles/xmrig-cu.dir/src/RandomX/graft/xmrig-cu_generated_randomx_graft.cu.o
[ 61%] Building NVCC (Device) object CMakeFiles/xmrig-cu.dir/src/RandomX/wownero/xmrig-cu_generated_randomx_wownero.cu.o
nvcc fatal   : Unsupported gpu architecture 'compute_35'
nvcc fatal   : Unsupported gpu architecture 'compute_35'
nvcc fatal   : Unsupported gpu architecture 'compute_35'
nvcc fatal   : Unsupported gpu architecture 'compute_35'
CMake Error at xmrig-cu_generated_cuda_core.cu.o.Release.cmake:220 (message):
  Error generating
  /home/dave/xmrig/build/xmrig-cuda/build/CMakeFiles/xmrig-cu.dir/src/./xmrig-cu_generated_cuda_core.cu.o
<snip>---- lots a errors past this.

I can build without cuda, would like to build for Ubuntu 23.04 with CUDA. I'm following guild here...
https://xmrig.com/docs/miner/build/ubuntu

Thanks for any help. 


# Discussion History
## SChernykh | 2023-05-29T07:27:51+00:00
Which CUDA version did you install? What is the output of `/usr/local/cuda/bin/nvcc --version` ?

CUDA 12.x has dropped support for Kepler compute 3.x devices, and the build script checks for this. Either NVIDIA documentation on this is incorrect, or you installed some CUDA incorrectly.

## SChernykh | 2023-05-29T08:12:27+00:00
The only way I can think of you could've gotten this error, is if you installed both CUDA 11 and CUDA 12, and somehow mixed them when compiling xmrig-cuda.

## DHeinz70 | 2023-05-29T23:14:02+00:00
Thanks a bunch for the help. Got it all working! 

## yuechenglinn | 2023-08-10T09:36:50+00:00
I have also encountered the same problem. How did you solve it? Thank you very much

# Action History
- Created by: DHeinz70 | 2023-05-29T01:31:14+00:00
- Closed at: 2025-06-18T22:37:19+00:00
