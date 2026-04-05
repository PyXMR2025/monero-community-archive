---
title: 'error: use of type ''double'' requires cl_khr_fp64 extension to be enabled'
source_url: https://github.com/xmrig/xmrig/issues/2709
author: pranshuthegamer
assignees: []
labels: []
created_at: '2021-11-20T10:40:08+00:00'
updated_at: '2025-06-20T11:09:15+00:00'
type: issue
status: closed
closed_at: '2025-06-20T11:09:15+00:00'
---

# Original Description
**Describe the bug**
im trying to use Intel OpenCl, btw it does detect the device

**To Reproduce**
i built it from source to remove donation and the enable OpenCl in config.json

**Expected behavior**
it should mine using the gpu

**Required data**
miner log:
```
* ABOUT        XMRig/6.15.3 gcc/11.2.0
 * LIBS         libuv/1.42.0 OpenSSL/1.1.1l hwloc/2.5.0
 * HUGE PAGES   permission granted
 * 1GB PAGES    unavailable
 * CPU          Intel(R) Core(TM) i3-1005G1 CPU @ 1.20GHz (1) 64-bit AES VM
                L2:1.0 MB L3:4.0 MB 2C/4T NUMA:1
 * MEMORY       5.2/15.8 GB (33%)
                Bottom-Slot 1(left): 8 GB DDR4 @ 2667 MHz HP26D4S9S8HJ-8
                Bottom-Slot 2(right): 8 GB DDR4 @ 2667 MHz V01D4S88GB1G81G82666
 * MOTHERBOARD  HP - HP Laptop 15s-du2xxx
 * DONATE       0%
 * ASSEMBLY     auto:intel
 * POOL #1      pool.minexmr.com:443 algo auto
 * COMMANDS     hashrate, pause, resume, results, connection
 * ADL          disabled (failed to load ADL)
 * OPENCL       #0 Intel(R) OpenCL HD Graphics/OpenCL 3.0
 * OPENCL GPU   #0 n/a Intel(R) UHD Graphics 900 MHz cu:32 mem:3233/6466 MB
 * CUDA         disabled
[2021-11-20 16:07:05.117]  net      use pool pool.minexmr.com:443 TLSv1.3 178.32.120.127
[2021-11-20 16:07:05.117]  net      fingerprint (SHA-256): "f8cb85d6dc856748d376b48e6b87f90900b3f683fe505ef59de570296761d14b"
[2021-11-20 16:07:05.118]  net      new job from pool.minexmr.com:443 diff 175004 algo rx/0 height 2497331 (120 tx)
[2021-11-20 16:07:05.118]  cpu      use argon2 implementation AVX-512F
[2021-11-20 16:07:05.118]  msr      to access MSR registers Administrator privileges required.
[2021-11-20 16:07:05.118]  msr      FAILED TO APPLY MSR MOD, HASHRATE WILL BE LOW
[2021-11-20 16:07:05.119]  randomx  init dataset algo rx/0 (4 threads) seed d02e1b1704b67497...
[2021-11-20 16:07:05.119]  randomx  allocated 2336 MB (2080+256) huge pages 100% 1168/1168 +JIT (0 ms)
[2021-11-20 16:07:13.385]  randomx  dataset ready (8266 ms)
[2021-11-20 16:07:13.386]  cpu      use profile  rx  (2 threads) scratchpad 2048 KB
[2021-11-20 16:07:13.386]  opencl   use profile  rx  (1 thread) scratchpad 2048 KB
|  # | GPU |  BUS ID | INTENSITY | WSIZE | MEMORY | NAME
|  0 |   0 |     n/a |       512 |     8 |   1024 | Intel(R) UHD Graphics
[2021-11-20 16:07:13.409]  cpu      READY threads 2/2 (2) huge pages 100% 2/2 memory 4096 KB (23 ms)
[2021-11-20 16:07:13.840]  opencl   GPU #0 compiling...
[2021-11-20 16:07:14.395]  opencl   error CL_BUILD_PROGRAM_FAILURE when calling clBuildProgram
BUILD LOG:
1:1308:26: warning: unsupported OpenCL extension 'cl_khr_fp64' - ignoring
#pragma OPENCL EXTENSION cl_khr_fp64 : enable
                         ^
1:1346:1: error: use of type 'double' requires cl_khr_fp64 extension to be enabled
double getSmallPositiveFloatBits(uint64_t entropy)
^
1:1353:8: error: implicit declaration of function 'as_double' is invalid in OpenCL
return as_double(exponent|mantissa);
       ^
1:1418:10: error: use of type 'double' requires cl_khr_fp64 extension to be enabled
__global double* A=(__global double*)(R+24);
         ^
1:1418:30: error: use of type 'double' requires cl_khr_fp64 extension to be enabled
__global double* A=(__global double*)(R+24);
                             ^
1:2376:1: error: use of type 'double' requires cl_khr_fp64 extension to be enabled
double load_F_E_groups(int value,uint64_t andMask,uint64_t orMask)
^
1:2378:1: error: use of type 'double' requires cl_khr_fp64 extension to be enabled
double t=convert_double_rtn(value);
^
1:2378:10: error: implicit declaration of function 'convert_double_rtn' is invalid in OpenCL
double t=convert_double_rtn(value);
         ^
1:2382:8: warning: use of out-of-scope declaration of 'as_double'
return as_double(x);
       ^
1:1353:8: note: previous declaration is here
return as_double(exponent|mantissa);
       ^
1:2384:17: error: use of type 'double' requires cl_khr_fp64 extension to be enabled
double fma_soft(double a,double b,double c,uint32_t rounding_mode)
                ^
1:2384:26: error: use of type 'double' requires cl_khr_fp64 extension to be enabled
double fma_soft(double a,double b,double c,uint32_t rounding_mode)
                         ^
1:2384:35: error: use of type 'double' requires cl_khr_fp64 extension to be enabled
double fma_soft(double a,double b,double c,uint32_t rounding_mode)
                                  ^
1:2384:1: error: use of type 'double' requires cl_khr_fp64 extension to be enabled
double fma_soft(double a,double b,double c,uint32_t rounding_mode)
^
1:2388:8: warning: double precision constant requires cl_khr_fp64, casting to single precision
if((a==0.0)||(b==0.0))
       ^
1:2388:18: warning: double precision constant requires cl_khr_fp64, casting to single precision
if((a==0.0)||(b==0.0))
                 ^
1:2390:7: warning: double precision constant requires cl_khr_fp64, casting to single precision
if(b==1.0)
      ^
1:2392:7: warning: double precision constant requires cl_khr_fp64, casting to single precision
if(c==0.0)
      ^
1:2397:27: warning: use of out-of-scope declaration of 'as_double'
return (rounding_mode==1)?as_double(minus_zero):0.0;
                          ^
1:1353:8: note: previous declaration is here
return as_double(exponent|mantissa);
       ^
1:2397:49: warning: double precision constant requires cl_khr_fp64, casting to single precision
return (rounding_mode==1)?as_double(minus_zero):0.0;
                                                ^
1:2413:8: warning: use of out-of-scope declaration of 'as_double'
return as_double(inf);
       ^
1:1353:8: note: previous declaration is here
return as_double(exponent|mantissa);
       ^
1:2433:8: warning: use of out-of-scope declaration of 'as_double'
return as_double(inf_rnd);
       ^
1:1353:8: note: previous declaration is here
return as_double(exponent|mantissa);
       ^
1:2461:19: warning: double precision constant requires cl_khr_fp64, casting to single precision
if((t[0]==0)&&(c!=0.0))
                  ^
1:2520:8: warning: double precision constant requires cl_khr_fp64, casting to single precision
return 0.0;
       ^
1:2548:8: warning: use of out-of-scope declaration of 'as_double'
return as_double(fma_result[1]);
       ^
1:1353:8: note: previous declaration is here
return as_double(exponent|mantissa);
       ^
1:2550:16: error: use of type 'double' requires cl_khr_fp64 extension to be enabled
double div_rnd(double a,double b,uint32_t fprc)
               ^
1:2550:25: error: use of type 'double' requires cl_khr_fp64 extension to be enabled
double div_rnd(double a,double b,uint32_t fprc)
                        ^
1:2550:1: error: use of type 'double' requires cl_khr_fp64 extension to be enabled
double div_rnd(double a,double b,uint32_t fprc)
^
1:2552:1: error: use of type 'double' requires cl_khr_fp64 extension to be enabled
double y0=1.0/b;
^
1:2552:11: warning: double precision constant requires cl_khr_fp64, casting to single precision
double y0=1.0/b;
          ^
1:2553:7: error: use of type 'double' requires cl_khr_fp64 extension to be enabled
const double t0=a*y0;
      ^
1:2554:7: error: use of type 'double' requires cl_khr_fp64 extension to be enabled
const double t1=fma(-b,t0,a);
      ^
1:2555:1: error: use of type 'double' requires cl_khr_fp64 extension to be enabled
double result=fma_soft(y0,t1,t0,fprc);
^
1:2558:48: warning: use of out-of-scope declaration of 'as_double'
if(((as_ulong(result)>>52)&2047)==2047) result=as_double(inf_rnd);
                                               ^
1:1353:8: note: previous declaration is here
return as_double(exponent|mantissa);
       ^
1:2560:15: warning: double precision constant requires cl_khr_fp64, casting to single precision
return (a==b)?1.0:result;
              ^
1:2562:17: error: use of type 'double' requires cl_khr_fp64 extension to be enabled
double sqrt_rnd(double x,uint32_t fprc)
                ^
1:2562:1: error: use of type 'double' requires cl_khr_fp64 extension to be enabled
double sqrt_rnd(double x,uint32_t fprc)
^
1:2564:1: error: use of type 'double' requires cl_khr_fp64 extension to be enabled
double y0=rsqrt(x);
^
1:2565:1: error: use of type 'double' requires cl_khr_fp64 extension to be enabled
double t0=y0*x;
^
1:2566:1: error: use of type 'double' requires cl_khr_fp64 extension to be enabled
double t1=y0*-0.5;
^
1:2566:15: warning: double precision constant requires cl_khr_fp64, casting to single precision
double t1=y0*-0.5;
              ^
1:2567:14: warning: double precision constant requires cl_khr_fp64, casting to single precision
t1=fma(t1,t0,0.5);
             ^
1:2568:7: error: use of type 'double' requires cl_khr_fp64 extension to be enabled
const double y1_x=fma(t0,t1,t0);
      ^
1:2569:7: warning: double precision constant requires cl_khr_fp64, casting to single precision
y0 *= 0.5;
      ^
1:2572:1: error: use of type 'double' requires cl_khr_fp64 extension to be enabled
double result=fma_soft(t1,y0,y1_x,fprc);
^
1:2659:27: warning: use of out-of-scope declaration of 'convert_double_rtn'
if(location) src=as_ulong(convert_double_rtn((int32_t)(src>>((sub&1)*32))));
                          ^
1:2378:10: note: previous declaration is here
double t=convert_double_rtn(value);
         ^
1:2659:18: error: invalid reinterpretation: sizes of 'ulong' (aka 'unsigned long') and 'int' must match
if(location) src=as_ulong(convert_double_rtn((int32_t)(src>>((sub&1)*32))));
                 ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
opencl-c.h:6644:21: note: expanded from macro 'as_ulong'
#define as_ulong(x) __builtin_astype((x),   ulong)
                    ^                ~~~
1:2662:7: error: use of type 'double' requires cl_khr_fp64 extension to be enabled
const double a=as_double(dst);
      ^
1:2662:16: warning: use of out-of-scope declaration of 'as_double'
const double a=as_double(dst);
               ^
1:1353:8: note: previous declaration is here
return as_double(exponent|mantissa);
       ^
1:2663:7: error: use of type 'double' requires cl_khr_fp64 extension to be enabled
const double b=as_double(src);
      ^
1:2664:34: warning: double precision constant requires cl_khr_fp64, casting to single precision
dst=as_ulong(fma_soft(a,is_mul?b:1.0,is_mul?0.0:b,fprc));
                                 ^
1:2664:45: warning: double precision constant requires cl_khr_fp64, casting to single precision
dst=as_ulong(fma_soft(a,is_mul?b:1.0,is_mul?0.0:b,fprc));
                                            ^
1:2687:23: warning: use of out-of-scope declaration of 'as_double'
dst=as_ulong(sqrt_rnd(as_double(dst),fprc));
                      ^
1:1353:8: note: previous declaration is here
return as_double(exponent|mantissa);
       ^
1:2708:14: warning: use of out-of-scope declaration of 'convert_double_rtn'
src=as_ulong(convert_double_rtn((int32_t)(src>>((sub&1)*32))));
             ^
1:2378:10: note: previous declaration is here
double t=convert_double_rtn(value);
         ^
1:2708:5: error: invalid reinterpretation: sizes of 'ulong' (aka 'unsigned long') and 'int' must match
src=as_ulong(convert_double_rtn((int32_t)(src>>((sub&1)*32))));
    ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
opencl-c.h:6644:21: note: expanded from macro 'as_ulong'
#define as_ulong(x) __builtin_astype((x),   ulong)
                    ^                ~~~
1:2711:22: warning: use of out-of-scope declaration of 'as_double'
dst=as_ulong(div_rnd(as_double(dst),as_double(src),fprc));
                     ^
1:1353:8: note: previous declaration is here
return as_double(exponent|mantissa);
       ^
1:2747:9: error: use of type 'double' requires cl_khr_fp64 extension to be enabled
__local double* F=(__local double*)(R+8);
        ^
1:2747:28: error: use of type 'double' requires cl_khr_fp64 extension to be enabled
__local double* F=(__local double*)(R+8);
                           ^
1:2748:9: error: use of type 'double' requires cl_khr_fp64 extension to be enabled
__local double* E=(__local double*)(R+16);
        ^
1:2748:28: error: use of type 'double' requires cl_khr_fp64 extension to be enabled
__local double* E=(__local double*)(R+16);
                           ^
1:2770:9: error: use of type 'double' requires cl_khr_fp64 extension to be enabled
__local double* fe=f_group?(F+sub*2):(E+(sub-4)*2);
        ^
1:2771:9: error: use of type 'double' requires cl_khr_fp64 extension to be enabled
__local double* f=F+sub;
        ^
1:2772:9: error: use of type 'double' requires cl_khr_fp64 extension to be enabled
__local double* e=E+sub;
        ^
1:4019:10: error: use of type 'double' requires cl_khr_fp64 extension to be enabled
__global double* A=(__global double*)(R+24);
         ^
1:4019:30: error: use of type 'double' requires cl_khr_fp64 extension to be enabled
__global double* A=(__global double*)(R+24);
                             ^

[2021-11-20 16:07:14.871]  opencl   thread #0 failed with error CL_INVALID_PROGRAM
[2021-11-20 16:07:14.989]  opencl   thread #0 self-test failed
[2021-11-20 16:07:14.989]  opencl   disabled (failed to start threads)
[2021-11-20 16:07:16.909]  signal   Ctrl+C received, exiting
[2021-11-20 16:07:16.914]  cpu      stopped (4 ms)
[2021-11-20 16:07:17.101]  opencl   stopped (187 ms)
```



 - config file:
```
{
    "api": {
        "id": null,
        "worker-id": null
    },
    "http": {
        "enabled": false,
        "host": "127.0.0.1",
        "port": 0,
        "access-token": null,
        "restricted": true
    },
    "autosave": true,
    "background": false,
    "colors": true,
    "title": true,
    "randomx": {
        "init": -1,
        "init-avx2": -1,
        "mode": "auto",
        "1gb-pages": false,
        "rdmsr": true,
        "wrmsr": true,
        "cache_qos": false,
        "numa": true,
        "scratchpad_prefetch_mode": 1
    },
    "cpu": {
        "enabled": true,
        "huge-pages": true,
        "huge-pages-jit": false,
        "hw-aes": null,
        "priority": null,
        "memory-pool": false,
        "yield": true,
        "asm": true,
        "argon2-impl": null,
        "astrobwt-max-size": 550,
        "astrobwt-avx2": false,
        "argon2": [0, 1, 2, 3],
        "astrobwt": [0, 1, 2, 3],
        "cn": [
            [1, 0],
            [1, 2]
        ],
        "cn-heavy": [
            [1, 0]
        ],
        "cn-lite": [
            [1, 0],
            [1, 1],
            [1, 2],
            [1, 3]
        ],
        "cn-pico": [
            [2, 0],
            [2, 1],
            [2, 2],
            [2, 3]
        ],
        "cn/upx2": [
            [2, 0],
            [2, 1],
            [2, 2],
            [2, 3]
        ],
        "rx": [0, 2],
        "rx/wow": [0, 1, 2, 3],
        "cn-lite/0": false,
        "cn/0": false,
        "rx/arq": "rx/wow",
        "rx/keva": "rx/wow"
    },
    "opencl": {
        "enabled": true,
        "cache": true,
        "loader": null,
        "platform": "Intel",
        "adl": true,
        "astrobwt": [
            {
                "index": 0,
                "intensity": 256,
                "threads": [-1, -1]
            }
        ],
        "cn": [
            {
                "index": 0,
                "intensity": 256,
                "worksize": 8,
                "strided_index": [0, 2],
                "threads": [-1],
                "unroll": 8
            }
        ],
        "cn-heavy": [
            {
                "index": 0,
                "intensity": 256,
                "worksize": 8,
                "strided_index": [0, 2],
                "threads": [-1],
                "unroll": 8
            }
        ],
        "cn-lite": [
            {
                "index": 0,
                "intensity": 512,
                "worksize": 8,
                "strided_index": [0, 2],
                "threads": [-1],
                "unroll": 8
            }
        ],
        "cn-pico": [
            {
                "index": 0,
                "intensity": 512,
                "worksize": 8,
                "strided_index": [0, 2],
                "threads": [-1],
                "unroll": 8
            }
        ],
        "cn/2": [
            {
                "index": 0,
                "intensity": 256,
                "worksize": 8,
                "strided_index": [0, 2],
                "threads": [-1],
                "unroll": 8
            }
        ],
        "cn/upx2": [
            {
                "index": 0,
                "intensity": 512,
                "worksize": 8,
                "strided_index": [0, 2],
                "threads": [-1],
                "unroll": 8
            }
        ],
        "kawpow": [
            {
                "index": 0,
                "intensity": 8388608,
                "worksize": 256,
                "threads": [-1]
            }
        ],
        "rx": [
            {
                "index": 0,
                "intensity": 512,
                "worksize": 8,
                "threads": [-1],
                "bfactor": 6,
                "gcn_asm": false,
                "dataset_host": false
            }
        ],
        "cn-lite/0": false,
        "cn/0": false
    },
    "cuda": {
        "enabled": false,
        "loader": null,
        "nvml": true
    },
    "log-file": null,
    "donate-level": 0,
    "donate-over-proxy": 1,
    "pools": [
        {
            "algo": null,
            "coin": null,
            "url": "pool.minexmr.com:443",
            "user": "",
            "pass": null,
            "rig-id": "1",
            "nicehash": false,
            "keepalive": true,
            "enabled": true,
            "tls": true,
            "tls-fingerprint": null,
            "daemon": false,
            "socks5": null,
            "self-select": null,
            "submit-to-origin": false
        }
    ],
    "retries": 5,
    "retry-pause": 5,
    "print-time": 60,
    "health-print-time": 60,
    "dmi": true,
    "syslog": false,
    "tls": {
        "enabled": false,
        "protocols": null,
        "cert": null,
        "cert_key": null,
        "ciphers": null,
        "ciphersuites": null,
        "dhparam": null
    },
    "dns": {
        "ipv6": false,
        "ttl": 30
    },
    "user-agent": null,
    "verbose": 0,
    "watch": true,
    "pause-on-battery": false,
    "pause-on-active": false
}
```

 - OS: Windows 10
 - For GPU related issues: intel UHD

**Additional context**
Add any other context about the problem here.


# Discussion History
## Spudz76 | 2021-11-20T12:37:33+00:00
Try to set

```
"loader": "Intel_OpenCL_ICD64.dll",
```

Or if not that, search for that file and use the entire path.  Due to JSON formatting rules you may have to double all backslashes so like `"C:\\Windows\\system32\\Intel_OpenCL_ICD64.dll"`

Then it should only query the Intel via the Intel loader, not via the generic loader (OpenCL.dll) which might not be passing all the options through correctly for some reason.

Or it may need to be built against the Intel OpenCL SDK, I have not tried an intel iGPU in a while, and never on Windows.

## Lonnegan | 2021-11-23T22:14:08+00:00
> **Describe the bug** im trying to use Intel OpenCl, btw it does detect the device
> 
> **To Reproduce** i built it from source **to remove donation** and the enable OpenCl in config.json

LOL Wait a minute! You're trying to remove the dev fee, but can't get it to work, and now you're asking the devs to help you do it? ROFL

## pranshuthegamer | 2021-11-24T17:58:05+00:00
> 



> Try to set
> 
> ```
> "loader": "Intel_OpenCL_ICD64.dll",
> ```
> 
> Or if not that, search for that file and use the entire path. Due to JSON formatting rules you may have to double all backslashes so like `"C:\\Windows\\system32\\Intel_OpenCL_ICD64.dll"`
> 
> Then it should only query the Intel via the Intel loader, not via the generic loader (OpenCL.dll) which might not be passing all the options through correctly for some reason.
> 
> Or it may need to be built against the Intel OpenCL SDK, I have not tried an intel iGPU in a while, and never on Windows.
```
* OPENCL       disabled (failed to load OpenCL runtime)
 * CUDA         disabled
[2021-11-24 23:27:14.360]  net      use pool pool.minexmr.com:443 TLSv1.3 51.68.21.188
[2021-11-24 23:27:14.360]  net      fingerprint (SHA-256): "f8cb85d6dc856748d376b48e6b87f90900b3f683fe505ef59de570296761d14b"
[2021-11-24 23:27:14.360]  net      new job from pool.minexmr.com:443 diff 175004 algo rx/0 height 2500454 (155 tx)
[2021-11-24 23:27:14.360]  cpu      use argon2 implementation AVX-512F
[2021-11-24 23:27:14.456]  msr      register values for "intel" preset have been set successfully (96 ms)
[2021-11-24 23:27:14.457]  randomx  init dataset algo rx/0 (4 threads) seed 0f02256f6851dd23...
[2021-11-24 23:27:14.552]  randomx  allocated 2336 MB (2080+256) huge pages 11% 128/1168 +JIT (95 ms)
[2021-11-24 23:27:21.208]  signal   Ctrl+C received, exiting
```

both have the same output, do i have to compile this lib myself?

## pranshuthegamer | 2021-11-24T18:01:57+00:00
update, i downloaded the dll and now its doing the exact same error as before

## Jeno1 | 2023-08-01T20:34:31+00:00
The problem still exists, Intel decided to kill hw fp64 support starting with 11th gen igpus.
Although they support some kind of a SW emulation (meaning: slow) but only using Linux (read it somewhere, cannot recall).

Is there a way to reinvite the wheel and if hw support fails, then find some other way to let LOTS OF PEOPLE use this feature in their new/relatively new PCs?

# Action History
- Created by: pranshuthegamer | 2021-11-20T10:40:08+00:00
- Closed at: 2025-06-20T11:09:15+00:00
