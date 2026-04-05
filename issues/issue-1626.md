---
title: '"no kernel image is available for execution on the device"'
source_url: https://github.com/xmrig/xmrig/issues/1626
author: cppethereum
assignees: []
labels: []
created_at: '2020-03-31T14:47:12+00:00'
updated_at: '2021-04-12T14:59:02+00:00'
type: issue
status: closed
closed_at: '2021-04-12T14:59:02+00:00'
---

# Original Description
**Describe the bug**
Nvidia GPU reporting with: 
`thread #0 failed with error <hash>:37 "no kernel image is available for execution on the device"`

**To Reproduce**
Initial run of xmrig with xmrig cuda plugin

**Expected behavior**
xmrig to run with nvidia gpu 

**Required data**
Ubuntu 18.04 
config:
```
{
    "autosave": true,
    "cpu": true,
    "opencl": false,
    "cuda": true,
    "pools": [
        {
           ...
        }
    ]
}
```
Nvidia GTX 550 ti
CUDA 9.1 

**Additional context**

I am building from source using gcc-6 and g++-6, maybe I need to set something specifically to build with cuda version 9.1? 

# Discussion History
## Spudz76 | 2020-04-05T19:37:30+00:00
Fermi based cards require CUDA 8.0 maximum - nVidia dropped Fermi after that.

The `xmrig-cuda` plugin should be compiled with the maximum compiler supported by the CUDA version (which is gcc-5 for 8.0) - then the main app with CUDA plugin support can be compiled with newer compiler of choice (system default like gcc-8, or clang-11).

For gcc-5 compiler packages, add the [Toolchain Test Builds PPA](https://launchpad.net/~ubuntu-toolchain-r/+archive/ubuntu/test) for your base Ubuntu version (also usually works on Debian if you match the related base version all the way back)

This is my build script for `xmrig-cuda` and CUDA 8:
```
CC=/usr/bin/gcc-5 CXX=/usr/bin/g++-5 \
 cmake /usr/src/xmrig-cuda \
  -DCMAKE_BUILD_TYPE=Release \
  -DCMAKE_VERBOSE_MAKEFILE=ON \
  -DCUDA_TOOLKIT_ROOT_DIR=/usr/local/cuda-8.0 \
  -DCUDA_VERBOSE_BUILD=ON \
  -DCUDA_ARCH=21\;20 \
```
and then for the main `xmrig` build to work with above plugin:
```
CC=/usr/bin/clang-11 CXX=/usr/bin/clang++-11 \
 cmake /usr/src/xmrig \
  -DCMAKE_BUILD_TYPE=Release \
  -DCMAKE_VERBOSE_MAKEFILE=ON \
  -DWITH_OPENCL=OFF \
  -DWITH_ADL=OFF \
  -DWITH_CUDA=ON \
  -DWITH_NVML=ON \
  -DWITH_CN_GPU=ON \
  -DWITH_RANDOMX=OFF \
  -DWITH_ASTROBWT=OFF \
```
AstroBWT explodes on CUDA 8 and is only available in dev branches right now, so OFF.
RandomX sometimes works but is so slow for the watts you don't want to bother, so OFF.
CN-GPU is being removed and is default: OFF recently (but MoneroOcean still accepts it...)

## clopnis | 2020-09-15T17:32:55+00:00
@Spudz76 this looks stop to work, the plugin is not working with gcc-5.
I'm using cuda_8.0.61_375.26 for a Quadro 6000 arch 20.

```
 [ 5%] Building NVCC (Device) object CMakeFiles/xmrig-cu.dir/src/KawPow/raven/xmrig-cu_generated_KawPow.cu.o
/opt/xmrig-6.3.3/tmp/xmrig-cuda-6.3.2/src/KawPow/raven/KawPow_dag.h(156): error: identifier "__shfl" is undefined

/opt/xmrig-6.3.3/tmp/xmrig-cuda-6.3.2/src/KawPow/raven/KawPow_dag.h(174): error: identifier "__shfl" is undefined

2 errors detected in the compilation of "/tmp/tmpxft_00003375_00000000-7_KawPow.cpp1.ii".
CMake Error at xmrig-cu_generated_KawPow.cu.o.Release.cmake:279 (message):
  Error generating file
  /opt/xmrig-6.3.3/tmp/xmrig-cuda-6.3.2/CMakeFiles/xmrig-cu.dir/src/KawPow/raven/./xmrig-cu_generated_KawPow.cu.o
```
Any suggestion ?


# Action History
- Created by: cppethereum | 2020-03-31T14:47:12+00:00
- Closed at: 2021-04-12T14:59:02+00:00
