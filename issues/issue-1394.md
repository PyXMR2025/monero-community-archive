---
title: openCL trouble on Mac OSX 10.14.6
source_url: https://github.com/xmrig/xmrig/issues/1394
author: joshlawless
assignees: []
labels:
- bug
created_at: '2019-12-07T02:38:52+00:00'
updated_at: '2021-04-20T10:37:12+00:00'
type: issue
status: closed
closed_at: '2021-04-12T15:10:52+00:00'
---

# Original Description
**Describe the bug**
I am unable to mine with my AMD Pro Vega 48 on my iMac.  The xmrig config wizard also appears to generate command line options that don't properly invoke opencl.

I installed a fresh copy of homebrew, and followed the macOS build instructions from https://github.com/xmrig/xmrig/wiki/macOS-Build

```
brew install cmake libuv libmicrohttpd openssl hwloc
git clone https://github.com/xmrig/xmrig.git
cd xmrig
mkdir build
cd build
cmake .. -DOPENSSL_ROOT_DIR=/usr/local/opt/openssl
make 
```

The wizard generated the following command line for me to use:

`./xmrig --donate-level 1 --opencl -o pool.supportxmr.com:443 -u 85C4wLzTjfC8LartzS9phFcUtDGEr14Yk2vAR4j3PiWW1DaothkXaEMeWt7qUSmWZZUk3uEMe46Rv7RnE6oDUtdrRYSzESf -k --tls
` 
I saw the following introductory information in response:

 ```
* ABOUT        XMRig/5.1.1 clang/10.0.1
 * LIBS         libuv/1.31.0 OpenSSL/1.1.1d hwloc/2.1.0
 * CPU          Intel(R) Core(TM) i9-9900K CPU @ 3.60GHz (1) x64 AES
                L2:2.0 MB L3:16.0 MB 8C/16T NUMA:1
 * MEMORY       18.2/128.0 GB (14%)
 * DONATE       1%
 * ASSEMBLY     auto:intel
 * POOL #1      pool.supportxmr.com:443 algo auto
 * COMMANDS     hashrate, pause, resume
 * OPENCL       disabled (selected OpenCL platform NOT found)
 * CUDA         disabled
```

The ` * OPENCL       disabled (selected OpenCL platform NOT found)` line was repeated every few lines of output.

I tried using the --print-platforms flag and got

```
Number of platforms:        1

  Index:                    0
  Profile:                  FULL_PROFILE
  Version:                  OpenCL 1.2 (Aug 31 2019 04:58:52)
  Name:                     Apple
  Vendor:                   Apple
  Extensions:               cl_APPLE_SetMemObjectDestructor cl_APPLE_ContextLoggingFunctions cl_APPLE_clut cl_APPLE_query_kernel_names cl_APPLE_gl_sharing cl_khr_gl_event
```

So I added the --opencl-platform=0 flag and ran it without cpu mining `--no-cpu` with the command

`./xmrig --donate-level 1 --no-cpu --opencl --opencl-platform=0 -o pool.supportxmr.com:443 -u 85C4wLzTjfC8LartzS9phFcUtDGEr14Yk2vAR4j3PiWW1DaothkXaEMeWt7qUSmWZZUk3uEMe46Rv7RnE6oDUtdrRYSzESf -k --tls`

That time it showed that openCL was enabled, but threw up a new error `Error CL_INVALID_OPERATION when calling clGetDeviceInfo, param 0x4037` and quickly exited with `Abort trap: 6`

```
 * ABOUT        XMRig/5.1.1 clang/10.0.1
 * LIBS         libuv/1.31.0 OpenSSL/1.1.1d hwloc/2.1.0
 * CPU          Intel(R) Core(TM) i9-9900K CPU @ 3.60GHz (1) x64 AES
                L2:2.0 MB L3:16.0 MB 8C/16T NUMA:1
 * MEMORY       17.7/128.0 GB (14%)
 * DONATE       1%
 * ASSEMBLY     auto:intel
 * POOL #1      pool.supportxmr.com:443 algo auto
 * COMMANDS     hashrate, pause, resume
[2019-12-06 19:19:56.976] Error CL_INVALID_OPERATION when calling clGetDeviceInfo, param 0x4037
 * OPENCL       #0 Apple/OpenCL 1.2 (Aug 31 2019 04:58:52)
 * OPENCL GPU   #0 n/a AMD Radeon Pro Vega 48 Compute Engine 786 MHz cu:48 mem:2044/8176 MB
 * CUDA         disabled
[2019-12-06 19:19:57.236]  net  use pool pool.supportxmr.com:443 TLSv1.2 107.178.104.10
[2019-12-06 19:19:57.236]  net  fingerprint (SHA-256): "69102268332371e7267eb5d5e9c5d7f8e4688bd0a5d9171243f37fa031d94302"
[2019-12-06 19:19:57.236]  net  new job from pool.supportxmr.com:443 diff 50000 algo rx/0 height 1983327
[2019-12-06 19:19:57.236]  rx   init dataset algo rx/0 (16 threads) seed 8287fe855e05dafc...
[2019-12-06 19:19:57.371]  rx   allocated 2336 MB (2080+256) huge pages 100% 1168/1168 +JIT (135 ms)
[2019-12-06 19:20:00.221]  rx   dataset ready (2849 ms)
[2019-12-06 19:20:00.222]  ocl  use profile  rx  (2 threads) scratchpad 2048 KB
|  # | GPU |  BUS ID |    I |  W | SI | MC |  U |  MEM | NAME
|  0 |   0 |     n/a |  768 |  8 |  0 |  - |  8 | 1536 | AMD Radeon Pro Vega 48 Compute Engine
|  1 |   0 |     n/a |  768 |  8 |  0 |  - |  8 | 1536 | AMD Radeon Pro Vega 48 Compute Engine
[2019-12-06 19:20:00.223]  ocl  GPU #0 compiling...
[2019-12-06 19:20:19.068]  ocl  GPU #0 compilation completed (18845 ms)
[2019-12-06 19:20:19.078]  ocl  READY threads 2/2 (18855 ms)
Abort trap: 6
```

That's where I got stuck.  I've tried adding in --opencl-devices=0 or --opencl-devices=0,1 to no effect.  

Any help would be welcome.  Thanks!

# Discussion History
## d9beuD | 2019-12-07T10:08:34+00:00
When using a `config.json`, in `opencl.platform`, you can change `AMD` to `Apple`

``` json
"opencl": {
    "enabled": true,
    "cache": true,
    "loader": null,
    "platform": "Apple"
},
```

## xmrig | 2019-12-07T13:12:09+00:00
Thank you, on macOS always only one platform `Apple` and this is regression.
`Error CL_INVALID_OPERATION when calling clGetDeviceInfo, param 0x4037` it regression too `0x4037` it is `CL_DEVICE_TOPOLOGY_AMD` and it should silence ignored as not supported.

About `Abort trap: 6`, please show:
1. `opencl` section from config file, yes I known you use command line, but only via config can set all parameters.
2. `clinfo` output.
3. Attach `/.cache/<random string>.bin` file to this issue.

## mxjoe | 2019-12-17T22:26:11+00:00
I get following errors with xmrig 5.3.0 and macOS 10.15.2 on a MacBook Pro with Radeon Pro 560.

```
[2019-12-17 23:33:58.252] Error CL_INVALID_OPERATION when calling clGetDeviceInfo, param 0x4037
 * ABOUT        XMRig/5.3.0 clang/10.0.1
 * LIBS         libuv/1.31.0 OpenSSL/1.0.2t hwloc/2.1.0
 * HUGE PAGES   supported
 * 1GB PAGES    unavailable
 * CPU          Intel(R) Core(TM) i7-7920HQ CPU @ 3.10GHz (1) x64 AES
                L2:1.0 MB L3:8.0 MB 4C/8T NUMA:1
 * MEMORY       12.0/16.0 GB (75%)
 * DONATE       1%
 * ASSEMBLY     auto:intel
 * POOL #1      pool.supportxmr.com:443 algo auto
 * COMMANDS     hashrate, pause, resume
[2019-12-17 23:33:58.256] Error CL_INVALID_OPERATION when calling clGetDeviceInfo, param 0x4037
 * OPENCL       #0 Apple/OpenCL 1.2 (Nov  9 2019 04:32:50)
 * OPENCL GPU   #0 n/a Intel(R) HD Graphics 630 1100 MHz cu:24 mem:384/1536 MB
 * OPENCL GPU   #1 n/a AMD Radeon Pro 560 Compute Engine 300 MHz cu:16 mem:1024/4096 MB
 * CUDA         disabled
[2019-12-17 23:33:58.355]  net  use pool pool.supportxmr.com:443 TLSv1.2 37.187.95.110
[2019-12-17 23:33:58.355]  net  fingerprint (SHA-256): "b20cea27ba8012ad17fb6f2b8f4c57f3c154f3069277aa67ec010ea8e873023f"
[2019-12-17 23:33:58.355]  net  new job from pool.supportxmr.com:443 diff 50000 algo rx/0 height 1991157
[2019-12-17 23:33:58.355]  rx   init dataset algo rx/0 (8 threads) seed 9d4fe3c9677150ca...
[2019-12-17 23:33:59.577]  rx   allocated 2336 MB (2080+256) huge pages 0% 0/1168 +JIT (1222 ms)
[2019-12-17 23:34:04.654]  rx   dataset ready (5077 ms)
[2019-12-17 23:34:04.654]  cpu  use profile  rx  (4 threads) scratchpad 2048 KB
[2019-12-17 23:34:04.725]  cpu  READY threads 4/4 (4) huge pages 100% 4/4 memory 8192 KB (71 ms)
[2019-12-17 23:34:04.748]  ocl  use profile  rx  (3 threads) scratchpad 2048 KB
|  # | GPU |  BUS ID |    I |  W | SI | MC |  U |  MEM | NAME
|  0 |   0 |     n/a |  320 |  8 |  0 |  - |  8 |  640 | Intel(R) HD Graphics 630
|  1 |   1 |     n/a |  256 |  8 |  0 |  - |  8 |  512 | AMD Radeon Pro 560 Compute Engine
|  2 |   1 |     n/a |  256 |  8 |  0 |  - |  8 |  512 | AMD Radeon Pro 560 Compute Engine
[2019-12-17 23:34:04.752]  ocl  GPU #0 compiling...
[2019-12-17 23:34:04.754]  ocl  error CL_BUILD_PROGRAM_FAILURE when calling clBuildProgram
BUILD LOG:
<program source>:760:6: warning: no previous prototype for function 'get_byte32'
uint get_byte32(uint a,uint start_bit) { return (a>>start_bit)&0xFF; }
     ^
<program source>:1012:7: warning: no previous prototype for function 'rotr64'
ulong rotr64(ulong a,ulong shift) { return rotate(a,64-shift); }
      ^
<program source>:1036:6: warning: no previous prototype for function 'blake2b_512_process_single_block'
void blake2b_512_process_single_block(ulong *h,const ulong* m,uint blockTemplateSize)
     ^
<program source>:1097:6: warning: no previous prototype for function 'blake2b_512_process_double_block_32'
void blake2b_512_process_double_block_name(ulong *out,ulong* m,__global const ulong* in)
     ^
<program source>:1095:47: note: expanded from macro 'blake2b_512_process_double_block_name'
#define blake2b_512_process_double_block_name blake2b_512_process_double_block_32
                                              ^
<program source>:1174:6: warning: no previous prototype for funct[2019-12-17 23:34:04.755]  ocl  thread #0 self-test failed
[2019-12-17 23:34:05.449]  ocl  GPU #1 compiling...
[2019-12-17 23:34:05.458]  ocl  GPU #1 compilation completed (9 ms)
[2019-12-17 23:34:05.459]  ocl  error CL_INVALID_VALUE when calling clGetProgramInfo
[2019-12-17 23:34:05.460]  ocl  GPU #1 compiling...
[2019-12-17 23:34:05.462]  ocl  GPU #1 compilation completed (2 ms)
[2019-12-17 23:34:05.463]  ocl  error CL_INVALID_VALUE when calling clGetProgramInfo
[2019-12-17 23:34:05.463]  ocl  READY threads 2/3 (714 ms)
[2019-12-17 23:34:15.430]  cpu  accepted (1/0) diff 50000 (32 ms)
[2019-12-17 23:34:15.882] Ctrl+C received, exiting
[2019-12-17 23:34:15.886]  cpu  stopped (3 ms)
[2019-12-17 23:34:28.734]  ocl  stopped (12847 ms)
```

## BlankerL | 2020-01-04T10:39:00+00:00
Same issue here, the device information and software information are listed below, 

> MacBook Pro with AMD Radeon Pro 5500M and Intel UHD Graphics 630
> XMRig 5.5.0
> macOS 10.15.2 (19C57)

The error outputs are similar to the aforementioned ones.

## m03e5 | 2020-01-17T00:28:18+00:00
iMac late 2014 i7-4790k + radeon M295x 4gb vram 8gb ram
Catalina 10.15 with all available updates to date.
XMRig 5.5.1

I get same error: 
Error CL_INVALID_OPERATION when calling clGetDeviceInfo, param 0x4037 

Side note: i was running XMRig while changing CFG file. XMRig gave this error consequtively 2 times then LISTED OPENCL as APPLE/OPENCL 1.2 NOV 9 2019 04:32:50  then next line says my GPU model: OPENCL GPU: N/A AMD RADEON R9 M295X Compute Engine 850MHz cu:32 mem:1024/4096MB
...2 THREADS...
....GPU COMPILING...
...COMPILATION COMPLETED 34633ms...
..READY THREADS 2/2 34646ms
.....then computer froze.... had to hard reboot it.  After complete boot to OSX, tried running XMRig and computer froze again. Had to disable OPENCL to make it work. Works but speed is 1200-1300hs

Will try to post full log later.


## m03e5 | 2020-01-17T00:40:41+00:00
After a couple reboots hashrate on CPU ONLY increased to 2350hs which is normal and very close to PC running same cpu/miner 

## cniweb | 2020-04-01T19:06:09+00:00
I get same error:
```
[2020-04-01 21:02:14.645]  ocl  use profile  rx  (3 threads) scratchpad 2048 KB
|  # | GPU |  BUS ID |    I |  W | SI | MC |  U |  MEM | NAME
|  0 |   0 |     n/a |  320 |  8 |  0 |  - |  8 |  640 | Intel(R) HD Graphics 630
|  1 |   1 |     n/a |  256 |  8 |  0 |  - |  8 |  512 | AMD Radeon Pro 560 Compute Engine
|  2 |   1 |     n/a |  256 |  8 |  0 |  - |  8 |  512 | AMD Radeon Pro 560 Compute Engine
[2020-04-01 21:02:14.655]  ocl  GPU #0 compiling...
[2020-04-01 21:02:14.658]  ocl  error CL_BUILD_PROGRAM_FAILURE when calling clBuildProgram
BUILD LOG:
<program source>:815:6: warning: no previous prototype for function 'get_byte32'
uint get_byte32(uint a,uint start_bit) { return (a>>start_bit)&0xFF; }
     ^
<program source>:1067:7: warning: no previous prototype for function 'rotr64'
ulong rotr64(ulong a,ulong shift) { return rotate(a,64-shift); }
      ^
<program source>:1091:6: warning: no previous prototype for function 'blake2b_512_process_single_block'
void blake2b_512_process_single_block(ulong *h,const ulong* m,uint blockTemplateSize)
     ^
<program source>:1152:6: warning: no previous prototype for function 'blake2b_512_process_double_block_32'
void blake2b_512_process_double_block_name(ulong *out,ulong* m,__global const ulong* in)
     ^
<program source>:1150:47: note: expanded from macro 'blake2b_512_process_double_block_name'
#define blake2b_512_process_double_block_name blake2b_512_process_double_block_32
                                              ^
<program source>:1229:6: warning: no previous prototype for function 'blake2b_512_process_double_block_64'
[2020-04-01 21:02:14.659]  ocl  thread #0 failed with error CL_INVALID_PROGRAM
[2020-04-01 21:02:14.661]  ocl  thread #0 self-test failed
[2020-04-01 21:02:14.672]  ocl  GPU #1 compiling...
[2020-04-01 21:02:14.677]  ocl  GPU #1 compilation completed (6 ms)
[2020-04-01 21:02:14.679]  ocl  error CL_INVALID_VALUE when calling clGetProgramInfo
[2020-04-01 21:02:14.694]  ocl  GPU #1 compiling...
[2020-04-01 21:02:14.698]  ocl  GPU #1 compilation completed (4 ms)
[2020-04-01 21:02:14.699]  ocl  error CL_INVALID_VALUE when calling clGetProgramInfo
[2020-04-01 21:02:14.699]  ocl  READY threads 2/3 (54 ms)
[2020-04-01 21:02:15.917]  ocl  error CL_INVALID_VALUE when calling clEnqueueWriteBuffer
[2020-04-01 21:02:15.917]  ocl  thread #2 failed with error CL_INVALID_VALUE
[2020-04-01 21:02:15.917]  ocl  error CL_INVALID_VALUE when calling clEnqueueWriteBuffer
[2020-04-01 21:02:15.917]  ocl  thread #1 failed with error CL_INVALID_VALUE
```

## linge | 2020-04-02T20:00:37+00:00
Get the same error message. After 60sec my iMac logs out, or get kernel panic and restarts.

Is it compiled wrong, or just a bug in XMRig 5.10.0?

```
[2020-04-02 21:48:42.164] Error CL_INVALID_OPERATION when calling clGetDeviceInfo, param 0x4037
 * ABOUT        XMRig/5.10.0 clang/11.0.3
 * LIBS         libuv/1.35.0 OpenSSL/1.1.1d hwloc/2.1.0
 * HUGE PAGES   supported
 * 1GB PAGES    unavailable
 * CPU          Intel(R) Core(TM) i5-8500 CPU @ 3.00GHz (1) x64 AES
                L2:1.5 MB L3:9.0 MB 6C/6T NUMA:1
 * MEMORY       6.2/8.0 GB (77%)
 * DONATE       1%
 * ASSEMBLY     auto:intel
 * POOL #1      
 * POOL #2      
 * COMMANDS     hashrate, pause, resume
[2020-04-02 21:48:42.205] Error CL_INVALID_OPERATION when calling clGetDeviceInfo, param 0x4037
 * OPENCL       #0 Apple/OpenCL 1.2 (Feb 29 2020 00:40:07)
 * OPENCL GPU   #0 n/a AMD Radeon Pro 570X Compute Engine 1000 MHz cu:28 mem:1024/4096 MB
 * CUDA         disabled
```

From config.json
"opencl": {
        "enabled": false,
        "cache": true,
        "loader": null,
        "platform": "Apple",

## minzak | 2020-06-14T19:38:42+00:00
similar issues - https://github.com/xmrig/xmrig/issues/1734

## eleaner | 2020-06-16T16:34:27+00:00
is there any solution for this issue?

## eleaner | 2020-07-28T10:35:01+00:00
noting?

## czw | 2020-09-27T18:22:48+00:00
This is still present in XMRig 6.3.4 and macOS 10.15.6. Output from `clinfo`:

```
Number of platforms                               1
  Platform Name                                   Apple
  Platform Vendor                                 Apple
  Platform Version                                OpenCL 1.2 (Jun  8 2020 17:36:15)
  Platform Profile                                FULL_PROFILE
  Platform Extensions                             cl_APPLE_SetMemObjectDestructor cl_APPLE_ContextLoggingFunctions cl_APPLE_clut cl_APPLE_query_kernel_names cl_APPLE_gl_sharing cl_khr_gl_event

  Platform Name                                   Apple
Number of devices                                 3
  Device Name                                     Intel(R) Core(TM) i7-8750H CPU @ 2.20GHz
  Device Vendor                                   Intel
  Device Vendor ID                                0xffffffff
  Device Version                                  OpenCL 1.2
  Driver Version                                  1.1
  Device OpenCL C Version                         OpenCL C 1.2
  Device Type                                     CPU
  Device Profile                                  FULL_PROFILE
  Device Available                                Yes
  Compiler Available                              Yes
  Linker Available                                Yes
  Max compute units                               12
  Max clock frequency                             2200MHz
  Device Partition                                (core)
    Max number of sub-devices                     0
    Supported partition types                     None
    Supported affinity domains                    (n/a)
  Max work item dimensions                        3
  Max work item sizes                             1024x1x1
  Max work group size                             1024
  Preferred work group size multiple              1
  Preferred / native vector sizes
    char                                                16 / 16
    short                                                8 / 8
    int                                                  4 / 4
    long                                                 2 / 2
    half                                                 0 / 0        (n/a)
    float                                                4 / 4
    double                                               2 / 2        (cl_khr_fp64)
  Half-precision Floating-point support           (n/a)
  Single-precision Floating-point support         (core)
    Denormals                                     Yes
    Infinity and NANs                             Yes
    Round to nearest                              Yes
    Round to zero                                 Yes
    Round to infinity                             Yes
    IEEE754-2008 fused multiply-add               Yes
    Support is emulated in software               No
    Correctly-rounded divide and sqrt operations  Yes
  Double-precision Floating-point support         (cl_khr_fp64)
    Denormals                                     Yes
    Infinity and NANs                             Yes
    Round to nearest                              Yes
    Round to zero                                 Yes
    Round to infinity                             Yes
    IEEE754-2008 fused multiply-add               Yes
    Support is emulated in software               No
  Address bits                                    64, Little-Endian
  Global memory size                              17179869184 (16GiB)
  Error Correction support                        No
  Max memory allocation                           4294967296 (4GiB)
  Unified memory for Host and Device              Yes
  Minimum alignment for any data type             128 bytes
  Alignment of base address                       1024 bits (128 bytes)
  Global Memory cache type                        Read/Write
  Global Memory cache size                        64
  Global Memory cache line size                   9437184 bytes
  Image support                                   Yes
    Max number of samplers per kernel             16
    Max size for 1D images from buffer            65536 pixels
    Max 1D or 2D image array size                 2048 images
    Base address alignment for 2D image buffers   1 bytes
    Pitch alignment for 2D image buffers          1 pixels
    Max 2D image size                             8192x8192 pixels
    Max 3D image size                             2048x2048x2048 pixels
    Max number of read image args                 128
    Max number of write image args                8
  Local memory type                               Global
  Local memory size                               32768 (32KiB)
  Max number of constant args                     8
  Max constant buffer size                        65536 (64KiB)
  Max size of kernel argument                     4096 (4KiB)
  Queue properties
    Out-of-order execution                        No
    Profiling                                     Yes
  Prefer user sync for interop                    Yes
  Profiling timer resolution                      1ns
  Execution capabilities
    Run OpenCL kernels                            Yes
    Run native kernels                            Yes
  printf() buffer size                            1048576 (1024KiB)
  Built-in kernels                                (n/a)
  Device Extensions                               cl_APPLE_SetMemObjectDestructor cl_APPLE_ContextLoggingFunctions cl_APPLE_clut cl_APPLE_query_kernel_names cl_APPLE_gl_sharing cl_khr_gl_event cl_khr_fp64 cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics cl_khr_byte_addressable_store cl_khr_int64_base_atomics cl_khr_int64_extended_atomics cl_khr_3d_image_writes cl_khr_image2d_from_buffer cl_APPLE_fp64_basic_ops cl_APPLE_fixed_alpha_channel_orders cl_APPLE_biased_fixed_point_image_formats cl_APPLE_command_queue_priority

  Device Name                                     Intel(R) UHD Graphics 630
  Device Vendor                                   Intel Inc.
  Device Vendor ID                                0x1024500
  Device Version                                  OpenCL 1.2
  Driver Version                                  1.2(Jul  6 2020 11:56:19)
  Device OpenCL C Version                         OpenCL C 1.2
  Device Type                                     GPU
  Device Profile                                  FULL_PROFILE
  Device Available                                Yes
  Compiler Available                              Yes
  Linker Available                                Yes
  Max compute units                               24
  Max clock frequency                             1100MHz
  Device Partition                                (core)
    Max number of sub-devices                     0
    Supported partition types                     None
    Supported affinity domains                    (n/a)
  Max work item dimensions                        3
  Max work item sizes                             256x256x256
  Max work group size                             256
  Preferred work group size multiple              32
  Preferred / native vector sizes
    char                                                 1 / 1
    short                                                1 / 1
    int                                                  1 / 1
    long                                                 1 / 1
    half                                                 0 / 0        (n/a)
    float                                                1 / 1
    double                                               0 / 0        (n/a)
  Half-precision Floating-point support           (n/a)
  Single-precision Floating-point support         (core)
    Denormals                                     Yes
    Infinity and NANs                             Yes
    Round to nearest                              Yes
    Round to zero                                 Yes
    Round to infinity                             Yes
    IEEE754-2008 fused multiply-add               Yes
    Support is emulated in software               No
    Correctly-rounded divide and sqrt operations  Yes
  Double-precision Floating-point support         (n/a)
  Address bits                                    64, Little-Endian
  Global memory size                              1610612736 (1.5GiB)
  Error Correction support                        No
  Max memory allocation                           402653184 (384MiB)
  Unified memory for Host and Device              Yes
  Minimum alignment for any data type             128 bytes
  Alignment of base address                       1024 bits (128 bytes)
  Global Memory cache type                        None
  Image support                                   Yes
    Max number of samplers per kernel             16
    Max size for 1D images from buffer            25165824 pixels
    Max 1D or 2D image array size                 2048 images
    Base address alignment for 2D image buffers   4 bytes
    Pitch alignment for 2D image buffers          32 pixels
    Max 2D image size                             16384x16384 pixels
    Max 3D image size                             2048x2048x2048 pixels
    Max number of read image args                 128
    Max number of write image args                8
  Local memory type                               Local
  Local memory size                               65536 (64KiB)
  Max number of constant args                     8
  Max constant buffer size                        65536 (64KiB)
  Max size of kernel argument                     1024
  Queue properties
    Out-of-order execution                        No
    Profiling                                     Yes
  Prefer user sync for interop                    Yes
  Profiling timer resolution                      80ns
  Execution capabilities
    Run OpenCL kernels                            Yes
    Run native kernels                            No
  printf() buffer size                            1048576 (1024KiB)
  Built-in kernels                                (n/a)
  Device Extensions                               cl_APPLE_SetMemObjectDestructor cl_APPLE_ContextLoggingFunctions cl_APPLE_clut cl_APPLE_query_kernel_names cl_APPLE_gl_sharing cl_khr_gl_event cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics cl_khr_byte_addressable_store cl_khr_image2d_from_buffer cl_khr_gl_depth_images cl_khr_depth_images cl_khr_3d_image_writes

  Device Name                                     AMD Radeon Pro 560X Compute Engine
  Device Vendor                                   AMD
  Device Vendor ID                                0x1021c00
  Device Version                                  OpenCL 1.2
  Driver Version                                  1.2 (Aug  7 2020 15:44:49)
  Device OpenCL C Version                         OpenCL C 1.2
  Device Type                                     GPU
  Device Profile                                  FULL_PROFILE
  Device Available                                Yes
  Compiler Available                              Yes
  Linker Available                                Yes
  Max compute units                               16
  Max clock frequency                             300MHz
  Device Partition                                (core)
    Max number of sub-devices                     0
    Supported partition types                     None
    Supported affinity domains                    (n/a)
  Max work item dimensions                        3
  Max work item sizes                             256x256x256
  Max work group size                             256
  Preferred work group size multiple              64
  Preferred / native vector sizes
    char                                                 4 / 4
    short                                                2 / 2
    int                                                  1 / 1
    long                                                 1 / 1
    half                                                 0 / 0        (n/a)
    float                                                1 / 1
    double                                               1 / 1        (cl_khr_fp64)
  Half-precision Floating-point support           (n/a)
  Single-precision Floating-point support         (core)
    Denormals                                     No
    Infinity and NANs                             Yes
    Round to nearest                              Yes
    Round to zero                                 Yes
    Round to infinity                             Yes
    IEEE754-2008 fused multiply-add               No
    Support is emulated in software               No
    Correctly-rounded divide and sqrt operations  Yes
  Double-precision Floating-point support         (cl_khr_fp64)
    Denormals                                     Yes
    Infinity and NANs                             Yes
    Round to nearest                              Yes
    Round to zero                                 Yes
    Round to infinity                             Yes
    IEEE754-2008 fused multiply-add               Yes
    Support is emulated in software               No
  Address bits                                    32, Little-Endian
  Global memory size                              4294967296 (4GiB)
  Error Correction support                        No
  Max memory allocation                           1073741824 (1024MiB)
  Unified memory for Host and Device              No
  Minimum alignment for any data type             128 bytes
  Alignment of base address                       32768 bits (4096 bytes)
  Global Memory cache type                        None
  Image support                                   Yes
    Max number of samplers per kernel             16
    Max size for 1D images from buffer            65536 pixels
    Max 1D or 2D image array size                 2048 images
    Base address alignment for 2D image buffers   256 bytes
    Pitch alignment for 2D image buffers          256 pixels
    Max 2D image size                             16384x16384 pixels
    Max 3D image size                             2048x2048x2048 pixels
    Max number of read image args                 128
    Max number of write image args                8
  Local memory type                               Local
  Local memory size                               32768 (32KiB)
  Max number of constant args                     8
  Max constant buffer size                        65536 (64KiB)
  Max size of kernel argument                     1024
  Queue properties
    Out-of-order execution                        No
    Profiling                                     Yes
  Prefer user sync for interop                    Yes
  Profiling timer resolution                      40ns
  Execution capabilities
    Run OpenCL kernels                            Yes
    Run native kernels                            No
  printf() buffer size                            134217728 (128MiB)
  Built-in kernels                                (n/a)
  Device Extensions                               cl_APPLE_SetMemObjectDestructor cl_APPLE_ContextLoggingFunctions cl_APPLE_clut cl_APPLE_query_kernel_names cl_APPLE_gl_sharing cl_khr_gl_event cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics cl_khr_byte_addressable_store cl_khr_image2d_from_buffer cl_khr_depth_images cl_APPLE_command_queue_priority cl_APPLE_command_queue_select_compute_units cl_khr_fp64

NULL platform behavior
  clGetPlatformInfo(NULL, CL_PLATFORM_NAME, ...)  Apple
  clGetDeviceIDs(NULL, CL_DEVICE_TYPE_ALL, ...)   Success [P0]
  clCreateContext(NULL, ...) [default]            Success [P0]
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_DEFAULT)  Success (2)
    Platform Name                                 Apple
    Device Name                                   Intel(R) UHD Graphics 630
    Device Name                                   AMD Radeon Pro 560X Compute Engine
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_CPU)  Success (1)
    Platform Name                                 Apple
    Device Name                                   Intel(R) Core(TM) i7-8750H CPU @ 2.20GHz
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_GPU)  Success (2)
    Platform Name                                 Apple
    Device Name                                   Intel(R) UHD Graphics 630
    Device Name                                   AMD Radeon Pro 560X Compute Engine
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_ACCELERATOR)  No devices found in platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_CUSTOM)  Invalid device type for platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_ALL)  Success (3)
    Platform Name                                 Apple
    Device Name                                   Intel(R) UHD Graphics 630
    Device Name                                   AMD Radeon Pro 560X Compute Engine
    Device Name                                   Intel(R) Core(TM) i7-8750H CPU @ 2.20GHz
	NOTE:	your OpenCL library only supports OpenCL 1.0,
		but some installed platforms support OpenCL 1.2.
		Programs using 1.2 features may crash
		or behave unexpectedly
```

## vip8snam | 2020-11-22T13:33:53+00:00
is there any solution for this issue?

## davidfradel | 2021-01-17T14:43:59+00:00
> is there any solution for this issue?

Same question... 😞 

## SChernykh | 2021-01-24T20:12:42+00:00
You're trying to mine RandomX on GPU and even if it works it will be very slow. MacOS OpenCL is not really supported in the code, but since it's OpenCL it should just compile and work (but it doesn't because Apple is always "special"). Try mining some other coin and algorithm with GPU.

## Spudz76 | 2021-01-24T21:27:20+00:00
Guessing OP missed this in the Config Wizard.  You have to turn OpenCL backend on, and likely CPU off (GPUs and CPUs have different strengths and weaknesses).
![image](https://user-images.githubusercontent.com/2391234/105643903-eb6abb80-5e4f-11eb-9354-7d0ad5f26886.png)

## talupoeg | 2021-01-25T15:10:20+00:00
On MSI computer I'm able to mine with both intel CPU and nvidia GPU using xmrig with nvidia cuda and custom xmrig conf on linux. 1 x Regular RTX 2060 GPU will give an extra 700 H/s with Rx algo, so yea, not really worth switching this GPU on if serious about mining as 1 GPU with ~ 130W usage will give 700 H/s and some other CPU can give you ~ 20 000 H/s with ~120W power consumption.

On a macbook pro computer I also can't get OpenCL to work on macos with AMD radeon R9 M370X. It is recognized however xmrig will give similar errors as mentioned above.

* OPENCL       #0 Apple/OpenCL 1.2 (May  5 2020 21:50:52)
 * OPENCL GPU   #0 n/a Iris Pro 1200 MHz cu:40 mem:384/1536 MB
 * OPENCL GPU   # 1 n/a AMD Radeon R9 M370X Compute Engine 300 MHz cu:10 mem:512/2048 MB
...

`Error CL_INVALID_OPERATION when calling clGetDeviceInfo, param 0x4037`
`opencl   error CL_INVALID_BUFFER_SIZE when calling clCreateBuffer with buffer size 2181038080`
`opencl   thread #1 failed with error RandomX dataset is not available`
`opencl   thread #2 failed with error RandomX dataset is not available`
`opencl   thread #1 self-test failed`
`opencl   thread #2 self-test failed`
`opencl   thread #0 failed with error RandomX dataset is not available`
`opencl   thread #0 self-test failed`
`opencl   disabled (failed to start threads)`


## Spudz76 | 2021-01-27T08:50:29+00:00
Yes RandomX on GPUs has been and always will be useless.
Proper thing to do is one xmrig instance set up for the CPU by itself, and another copy set up for cuda-only (or opencl-only) and mine to a pool where whatever coin mined pays out XMR (like MoneroOcean) and then your effective "XMR" rate will be high.  You just can't actually mine XMR on GPUs to any worthwhile effect, but you can earn XMR with autoexchanging multi-coin pools.  And any performance hit from overhead of running separate miners to each device, is nullified by the exchange rate gains.  The GPU will go slightly slower with a full load of CPU mining, usually.

Example, single GTX1060 mining CN/GPU (RYO coin):
```
  nvidia   #0 03:00.0  89W 64C 2050/3999 MHz fan0:100%
  miner    speed 10s/60s/15m 838.5 838.6 835.9 H/s max 873.5 H/s
```
Which ends up as an effective 9610H/s of Monero hashrate payout and there is no way the card could ever do that with native RX/0.  Also much closer to a CPU level of hashrate for the ~90W chewed.
EDIT: made rx/0 work on the same card, for some reason the clocks are different but wouldn't matter much:
```
  nvidia   #0 03:00.0  83W 47C 1949/3802 MHz fan0:100%
  miner    speed 10s/60s/15m 307.9 307.7 n/a H/s max 308.6 H/s
```
Just because the miner supports running things in lockstep doesn't mean it is the best way to mine anything / no algo I know of is very good on both at the same time due to different strengths and weaknesses.

## xmarco | 2021-01-28T06:10:01+00:00
Apple hasn't updated OpenCL for years. Please note the info appended to `clinfo`:

```
	NOTE:	your OpenCL library only supports OpenCL 1.0,
		but some installed platforms support OpenCL 1.2.
		Programs using 1.2 features may crash
		or behave unexpectedly
```

Currently, the only API that is up to date at Apple is Metal. I did my research and found https://github.com/djphoenix/MoneroKit utilizes the Metal to mine Monero. I haven't tried by myself but the solution sounds promising.

## Spudz76 | 2021-02-05T21:31:45+00:00
OpenCL is abandoned by Apple, and will never get up to date.  There is a CL2Metal compatibility layer but it barely works and will also disappear whenever Apple decides everyone should have already converted to Metal (in a few more OS revs).

Unsure if anyone cares about Metal, Apple should not abandon industry standards.

## EliW | 2021-04-20T02:18:09+00:00
So is OpenCL for AMD just dead for xmrig then?   I'd just found xmrig and was very excited to have a miner that would run natively on my mac and use my external GPU.   But I found all the issues shown in this issue, getting CL_INVALID_PROGRAM and Error returned by cvms_element_build_from_source


## Spudz76 | 2021-04-20T10:37:12+00:00
Works great under Linux and Windows, where OpenCL is not abandoned.

# Action History
- Created by: joshlawless | 2019-12-07T02:38:52+00:00
- Closed at: 2021-04-12T15:10:52+00:00
