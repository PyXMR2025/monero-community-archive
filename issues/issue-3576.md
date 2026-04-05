---
title: Failed to enable OpenCL Intel UHD Graphics
source_url: https://github.com/xmrig/xmrig/issues/3576
author: 69gg
assignees: []
labels: []
created_at: '2024-11-02T13:21:18+00:00'
updated_at: '2024-11-03T10:39:15+00:00'
type: issue
status: closed
closed_at: '2024-11-03T10:39:15+00:00'
---

# Original Description
**Describe the bug**
I tried to enable OpenCL in My Intel UHD Graphics(I know it was not good for hashrate), and failed

**To Reproduce**
`config.json`
```json
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
        "1gb-pages": true,
        "rdmsr": true,
        "wrmsr": true,
        "cache_qos": true,
        "numa": true,
        "scratchpad_prefetch_mode": 1
    },
    "cpu": {
        "enabled": true,
        "huge-pages": true,
        "huge-pages-jit": false,
        "hw-aes": null,
        "priority": null,
        "memory-pool": true,
        "yield": true,
        "asm": true,
        "argon2-impl": null,
        "*": {
            "intensity": 1,
            "threads": 8,
            "affinity": -1
        },
        "kawpow": true
    },
    "opencl": {
        "enabled": true,
        "cache": true,
        "loader": "C:\\Windows\\System32\\DriverStore\\FileRepository\\iigd_dch.inf_amd64_b53c057d22ce6f37\\Intel_OpenCL_ICD64.dll",
        "platform": "intel",
        "adl": false,
        "cn": [
            {
                "index": 0,
                "intensity": 160,
                "worksize": 8,
                "strided_index": [0, 2],
                "threads": [-1],
                "unroll": 8
            }
        ],
        "cn-heavy": [
            {
                "index": 0,
                "intensity": 80,
                "worksize": 8,
                "strided_index": [0, 2],
                "threads": [-1],
                "unroll": 8
            }
        ],
        "cn-lite": [
            {
                "index": 0,
                "intensity": 360,
                "worksize": 8,
                "strided_index": [0, 2],
                "threads": [-1],
                "unroll": 8
            }
        ],
        "cn-pico": [
            {
                "index": 0,
                "intensity": 1520,
                "worksize": 8,
                "strided_index": [0, 2],
                "threads": [-1],
                "unroll": 8
            }
        ],
        "cn/2": [
            {
                "index": 0,
                "intensity": 160,
                "worksize": 8,
                "strided_index": [0, 2],
                "threads": [-1],
                "unroll": 8
            }
        ],
        "cn/upx2": [
            {
                "index": 0,
                "intensity": 3040,
                "worksize": 8,
                "strided_index": [0, 2],
                "threads": [-1],
                "unroll": 8
            }
        ],
        "kawpow": [
            {
                "index": 0,
                "intensity": 1310720,
                "worksize": 256,
                "threads": [-1],
                "unroll": 1
            }
        ],
        "rx": [
            {
                "index": 0,
                "intensity": 32,
                "worksize": 8,
                "threads": [-1],
                "bfactor": 6,
                "gcn_asm": true,
                "dataset_host": true
            }
        ],
        "cn-lite/0": false,
        "cn/0": false
    },
    "cuda": {
        "enabled": true,
        "loader": null,
        "nvml": true,
        "cn": [
            {
                "index": 0,
                "threads": 96,
                "blocks": 30,
                "bfactor": 12,
                "bsleep": 50,
                "affinity": -1,
                "dataset_host": false
            }
        ],
        "cn-heavy": [
            {
                "index": 0,
                "threads": 48,
                "blocks": 30,
                "bfactor": 12,
                "bsleep": 30,
                "affinity": -1,
                "dataset_host": false
            }
        ],
        "cn-lite": [
            {
                "index": 0,
                "threads": 196,
                "blocks": 30,
                "bfactor": 12,
                "bsleep": 50,
                "affinity": -1,
                "dataset_host": false
            }
        ],
        "cn-pico": [
            {
                "index": 0,
                "threads": 256,
                "blocks": 30,
                "bfactor": 12,
                "bsleep": 50,
                "affinity": -1,
                "dataset_host": false
            }
        ],
        "cn/2": [
            {
                "index": 0,
                "threads": 48,
                "blocks": 15,
                "bfactor": 8,
                "bsleep": 25,
                "affinity": -1,
                "dataset_host": false
            }
        ],
        "cn/upx2": [
            {
                "index": 0,
                "threads": 128,
                "blocks": 15,
                "bfactor": 8,
                "bsleep": 25,
                "affinity": -1,
                "dataset_host": false
            }
        ],
        "kawpow": [
            {
                "index": 0,
                "threads": 256,
                "blocks": 10240,
                "bfactor": 8,
                "bsleep": 25,
                "affinity": -1,
                "dataset_host": false
            }
        ],
        "rx": [
            {
                "index": 0,
                "threads": 32,
                "blocks": 10,
                "bfactor": 8,
                "bsleep": 25,
                "affinity": -1,
                "dataset_host": true
            }
        ],
        "cn-lite/0": false,
        "cn/0": false
    },
    "log-file": null,
    "donate-level": 0,
    "donate-over-proxy": 1,
    "pools": [
        {
            "algo": "rx/0",
            "coin": "XMR",
            "url": "xmr.kryptex.network:8888",
            "user": "43cp47aGuVMK1iTGYSyqaJ7Hem8cTuEud7hMBgHfWvcGEDkn9gXMmzPaxyFzXRrZRoRHTEMFgv6V1aU58c1pMrEN21WBjNU/pyl2-win",
            "pass": null,
            "rig-id": null,
            "nicehash": true,
            "keepalive": true,
            "enabled": true,
            "tls": true,
            "sni": false,
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

**Expected behavior**
`output:`
```
 * ABOUT        XMRig/6.22.1 MSVC/2022 (built for Windows x86-64, 64 bit)
 * LIBS         libuv/1.49.2 OpenSSL/3.3.2 hwloc/2.11.2
 * HUGE PAGES   permission granted
 * 1GB PAGES    unavailable
 * CPU          Intel(R) Core(TM) i5-1035G1 CPU @ 1.00GHz (1) 64-bit AES VM
                L2:2.0 MB L3:6.0 MB 4C/8T NUMA:1
 * MEMORY       4.3/13.7 GB (31%)
                ChannelA-DRAM : 8 GB DDR4 @ 3200 MHz M471A1G44AB0-CWE
                ChannelB-DRAM : 8 GB DDR4 @ 3200 MHz M471A1G44AB0-CWE
 * MOTHERBOARD  LENOVO - 81YJ
 * DONATE       0%
 * ASSEMBLY     auto:intel
 * POOL #1      xmr.kryptex.network:8888 coin Monero
 * COMMANDS     hashrate, pause, resume, results, connection
 * ADL          disabled
 * OPENCL       #1 Intel(R) OpenCL HD Graphics/OpenCL 3.0
 * OPENCL GPU   #0 n/a Intel(R) UHD Graphics 1050 MHz cu:32 mem:2812/5624 MB
 * CUDA         12.4/12.6/6.22.0
 * NVML         12.560.70/560.70 press e for health report
 * CUDA GPU     #0 01:00.0 NVIDIA GeForce MX350 1468/3504 MHz smx:5 arch:61 mem:1627/2047 MB
[2024-11-02 21:18:09.214]  net      use pool xmr.kryptex.network:8888 TLSv1.3 157.90.32.66
[2024-11-02 21:18:09.216]  net      fingerprint (SHA-256): "9207d44458828d19dd12a61feffd7f843cbf7eacfaf3c2ab3fb9e42b0525791a"
[2024-11-02 21:18:09.217]  net      new job from xmr.kryptex.network:8888 diff 400015 algo rx/0 height 3272568 (5 tx)
[2024-11-02 21:18:09.217]  cpu      use argon2 implementation AVX-512F
[2024-11-02 21:18:09.218]  msr      this CPU doesn't support cat_l3, cache QoS is unavailable
[2024-11-02 21:18:09.386]  msr      register values for "intel" preset have been set successfully (168 ms)
[2024-11-02 21:18:09.386]  randomx  init dataset algo rx/0 (8 threads) seed 46bf9bc5544d89be...
[2024-11-02 21:18:09.591]  randomx  allocated 2336 MB (2080+256) huge pages 100% 1168/1168 +JIT (204 ms)
[2024-11-02 21:18:14.588]  randomx  dataset ready (4997 ms)
[2024-11-02 21:18:14.589]  cpu      use profile  *  (8 threads) scratchpad 2048 KB
[2024-11-02 21:18:14.590]  opencl   use profile  rx  (1 thread) scratchpad 2048 KB
|  # | GPU |  BUS ID | INTENSITY | WSIZE | MEMORY | NAME
|  0 |   0 |     n/a |        32 |     8 |     64 | Intel(R) UHD Graphics
[2024-11-02 21:18:14.599]  cpu      READY threads 8/8 (8) huge pages 100% 8/8 memory 16384 KB (2 ms)
[2024-11-02 21:18:14.607]  nvidia   use profile  rx  (1 thread) scratchpad 2048 KB
|  # | GPU |  BUS ID | INTENSITY | THREADS | BLOCKS | BF |  BS | MEMORY | NAME
|  0 |   0 | 01:00.0 |       320 |      32 |     10 |  8 |  25 |    640 | NVIDIA GeForce MX350
[2024-11-02 21:18:14.642]  opencl   GPU #0 compiling...
[2024-11-02 21:18:15.187]  nvidia   READY threads 1/1 (550 ms)
[2024-11-02 21:18:16.694]  opencl   error CL_BUILD_PROGRAM_FAILURE when calling clBuildProgram
BUILD LOG:
1:1414:26: warning: unsupported OpenCL extension 'cl_khr_fp64' - ignoring
#pragma OPENCL EXTENSION cl_khr_fp64 : enable
                         ^
1:1452:1: error: use of type 'double' requires cl_khr_fp64 extension to be enabled
double getSmallPositiveFloatBits(uint64_t entropy)
^
1:1459:8: error: implicit declaration of function 'as_double' is invalid in OpenCL
return as_double(exponent|mantissa);
       ^
1:1524:10: error: use of type 'double' requires cl_khr_fp64 extension to be enabled
__global double* A=(__global double*)(R+24);
         ^
1:1524:30: error: use of type 'double' requires cl_khr_fp64 extension to be enabled
__global double* A=(__global double*)(R+24);
                             ^
1:2482:1: error: use of type 'double' requires cl_khr_fp64 extension to be enabled
double load_F_E_groups(int value,uint64_t andMask,uint64_t orMask)
^
1:2484:1: error: use of type 'double' requires cl_khr_fp64 extension to be enabled
double t=convert_double_rtn(value);
^
1:2484:10: error: implicit declaration of function 'convert_double_rtn' is invalid in OpenCL
double t=convert_double_rtn(value);
         ^
1:2488:8: warning: use of out-of-scope declaration of 'as_double'
return as_double(x);
       ^
1:1459:8: note: previous declaration is here
return as_double(exponent|mantissa);
       ^
1:2490:17: error: use of type 'double' requires cl_khr_fp64 extension to be enabled
double fma_soft(double a,double b,double c,uint32_t rounding_mode)
                ^
1:2490:26: error: use of type 'double' requires cl_khr_fp64 extension to be enabled
double fma_soft(double a,double b,double c,uint32_t rounding_mode)
                         ^
1:2490:35: error: use of type 'double' requires cl_khr_fp64 extension to be enabled
double fma_soft(double a,double b,double c,uint32_t rounding_mode)
                                  ^
1:2490:1: error: use of type 'double' requires cl_khr_fp64 extension to be enabled
double fma_soft(double a,double b,double c,uint32_t rounding_mode)
^
1:2494:8: warning: double precision constant requires cl_khr_fp64, casting to single precision
if((a==0.0)||(b==0.0))
       ^
1:2494:18: warning: double precision constant requires cl_khr_fp64, casting to single precision
if((a==0.0)||(b==0.0))
                 ^
1:2496:7: warning: double precision constant requires cl_khr_fp64, casting to single precision
if(b==1.0)
      ^
1:2498:7: warning: double precision constant requires cl_khr_fp64, casting to single precision
if(c==0.0)
      ^
1:2503:27: warning: use of out-of-scope declaration of 'as_double'
return (rounding_mode==1)?as_double(minus_zero):0.0;
                          ^
1:1459:8: note: previous declaration is here
return as_double(exponent|mantissa);
       ^
1:2503:49: warning: double precision constant requires cl_khr_fp64, casting to single precision
return (rounding_mode==1)?as_double(minus_zero):0.0;
                                                ^
1:2519:8: warning: use of out-of-scope declaration of 'as_double'
return as_double(inf);
       ^
1:1459:8: note: previous declaration is here
return as_double(exponent|mantissa);
       ^
1:2539:8: warning: use of out-of-scope declaration of 'as_double'
return as_double(inf_rnd);
       ^
1:1459:8: note: previous declaration is here
return as_double(exponent|mantissa);
       ^
1:2567:19: warning: double precision constant requires cl_khr_fp64, casting to single precision
if((t[0]==0)&&(c!=0.0))
                  ^
1:2626:8: warning: double precision constant requires cl_khr_fp64, casting to single precision
return 0.0;
       ^
1:2654:8: warning: use of out-of-scope declaration of 'as_double'
return as_double(fma_result[1]);
       ^
1:1459:8: note: previous declaration is here
return as_double(exponent|mantissa);
       ^
1:2656:16: error: use of type 'double' requires cl_khr_fp64 extension to be enabled
double div_rnd(double a,double b,uint32_t fprc)
               ^
1:2656:25: error: use of type 'double' requires cl_khr_fp64 extension to be enabled
double div_rnd(double a,double b,uint32_t fprc)
                        ^
1:2656:1: error: use of type 'double' requires cl_khr_fp64 extension to be enabled
double div_rnd(double a,double b,uint32_t fprc)
^
1:2658:1: error: use of type 'double' requires cl_khr_fp64 extension to be enabled
double y0=1.0/b;
^
1:2658:11: warning: double precision constant requires cl_khr_fp64, casting to single precision
double y0=1.0/b;
          ^
1:2659:7: error: use of type 'double' requires cl_khr_fp64 extension to be enabled
const double t0=a*y0;
      ^
1:2660:7: error: use of type 'double' requires cl_khr_fp64 extension to be enabled
const double t1=fma(-b,t0,a);
      ^
1:2661:1: error: use of type 'double' requires cl_khr_fp64 extension to be enabled
double result=fma_soft(y0,t1,t0,fprc);
^
1:2664:48: warning: use of out-of-scope declaration of 'as_double'
if(((as_ulong(result)>>52)&2047)==2047) result=as_double(inf_rnd);
                                               ^
1:1459:8: note: previous declaration is here
return as_double(exponent|mantissa);
       ^
1:2666:15: warning: double precision constant requires cl_khr_fp64, casting to single precision
return (a==b)?1.0:result;
              ^
1:2668:17: error: use of type 'double' requires cl_khr_fp64 extension to be enabled
double sqrt_rnd(double x,uint32_t fprc)
                ^
1:2668:1: error: use of type 'double' requires cl_khr_fp64 extension to be enabled
double sqrt_rnd(double x,uint32_t fprc)
^
1:2670:1: error: use of type 'double' requires cl_khr_fp64 extension to be enabled
double y0=rsqrt(x);
^
1:2671:1: error: use of type 'double' requires cl_khr_fp64 extension to be enabled
double t0=y0*x;
^
1:2672:1: error: use of type 'double' requires cl_khr_fp64 extension to be enabled
double t1=y0*-0.5;
^
1:2672:15: warning: double precision constant requires cl_khr_fp64, casting to single precision
double t1=y0*-0.5;
              ^
1:2673:14: warning: double precision constant requires cl_khr_fp64, casting to single precision
t1=fma(t1,t0,0.5);
             ^
1:2674:7: error: use of type 'double' requires cl_khr_fp64 extension to be enabled
const double y1_x=fma(t0,t1,t0);
      ^
1:2675:7: warning: double precision constant requires cl_khr_fp64, casting to single precision
y0 *= 0.5;
      ^
1:2678:1: error: use of type 'double' requires cl_khr_fp64 extension to be enabled
double result=fma_soft(t1,y0,y1_x,fprc);
^
1:2765:27: warning: use of out-of-scope declaration of 'convert_double_rtn'
if(location) src=as_ulong(convert_double_rtn((int32_t)(src>>((sub&1)*32))));
                          ^
1:2484:10: note: previous declaration is here
double t=convert_double_rtn(value);
         ^
1:2765:18: error: invalid reinterpretation: sizes of 'ulong' (aka 'unsigned long') and 'int' must match
if(location) src=as_ulong(convert_double_rtn((int32_t)(src>>((sub&1)*32))));
                 ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
./opencl-c.h:6392:21: note: expanded from macro 'as_ulong'
#define as_ulong(x) __builtin_astype((x),   ulong)
                    ^                ~~~
1:2768:7: error: use of type 'double' requires cl_khr_fp64 extension to be enabled
const double a=as_double(dst);
      ^
1:2768:16: warning: use of out-of-scope declaration of 'as_double'
const double a=as_double(dst);
               ^
1:1459:8: note: previous declaration is here
return as_double(exponent|mantissa);
       ^
1:2769:7: error: use of type 'double' requires cl_khr_fp64 extension to be enabled
const double b=as_double(src);
      ^
1:2770:34: warning: double precision constant requires cl_khr_fp64, casting to single precision
dst=as_ulong(fma_soft(a,is_mul?b:1.0,is_mul?0.0:b,fprc));
                                 ^
1:2770:45: warning: double precision constant requires cl_khr_fp64, casting to single precision
dst=as_ulong(fma_soft(a,is_mul?b:1.0,is_mul?0.0:b,fprc));
                                            ^
1:2793:23: warning: use of out-of-scope declaration of 'as_double'
dst=as_ulong(sqrt_rnd(as_double(dst),fprc));
                      ^
1:1459:8: note: previous declaration is here
return as_double(exponent|mantissa);
       ^
1:2814:14: warning: use of out-of-scope declaration of 'convert_double_rtn'
src=as_ulong(convert_double_rtn((int32_t)(src>>((sub&1)*32))));
             ^
1:2484:10: note: previous declaration is here
double t=convert_double_rtn(value);
         ^
1:2814:5: error: invalid reinterpretation: sizes of 'ulong' (aka 'unsigned long') and 'int' must match
src=as_ulong(convert_double_rtn((int32_t)(src>>((sub&1)*32))));
    ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
./opencl-c.h:6392:21: note: expanded from macro 'as_ulong'
#define as_ulong(x) __builtin_astype((x),   ulong)
                    ^                ~~~
1:2817:22: warning: use of out-of-scope declaration of 'as_double'
dst=as_ulong(div_rnd(as_double(dst),as_double(src),fprc));
                     ^
1:1459:8: note: previous declaration is here
return as_double(exponent|mantissa);
       ^
1:2853:9: error: use of type 'double' requires cl_khr_fp64 extension to be enabled
__local double* F=(__local double*)(R+8);
        ^
1:2853:28: error: use of type 'double' requires cl_khr_fp64 extension to be enabled
__local double* F=(__local double*)(R+8);
                           ^
1:2854:9: error: use of type 'double' requires cl_khr_fp64 extension to be enabled
__local double* E=(__local double*)(R+16);
        ^
1:2854:28: error: use of type 'double' requires cl_khr_fp64 extension to be enabled
__local double* E=(__local double*)(R+16);
                           ^
1:2876:9: error: use of type 'double' requires cl_khr_fp64 extension to be enabled
__local double* fe=f_group?(F+sub*2):(E+(sub-4)*2);
        ^
1:2877:9: error: use of type 'double' requires cl_khr_fp64 extension to be enabled
__local double* f=F+sub;
        ^
1:2878:9: error: use of type 'double' requires cl_khr_fp64 extension to be enabled
__local double* e=E+sub;
        ^
1:4125:10: error: use of type 'double' requires cl_khr_fp64 extension to be enabled
__global double* A=(__global double*)(R+24);
         ^
1:4125:30: error: use of type 'double' requires cl_khr_fp64 extension to be enabled
__global double* A=(__global double*)(R+24);
                             ^

[2024-11-02 21:18:16.698]  opencl   thread #0 failed with error CL_INVALID_PROGRAM
[2024-11-02 21:18:16.709]  opencl   thread #0 self-test failed
[2024-11-02 21:18:16.709]  opencl   disabled (failed to start threads)
```

**Required data**
 - XMRig version
   6.22.1
 - OS:Windows 11 Pro

Thank you Very Very Very much


# Discussion History
## SChernykh | 2024-11-03T09:20:01+00:00
> unsupported OpenCL extension 'cl_khr_fp64'

Intel integrated GPU can't run RandomX OpenCL code, and it's entirely pointless because even if it could, it would drop CPU hashrate a lot, more than you would gain from using the integrated GPU.

## 69gg | 2024-11-03T10:39:11+00:00
> > unsupported OpenCL extension 'cl_khr_fp64'
> 
> Intel integrated GPU can't run RandomX OpenCL code, and it's entirely pointless because even if it could, it would drop CPU hashrate a lot, more than you would gain from using the integrated GPU.

thanks for your answer and now I konw it.

# Action History
- Created by: 69gg | 2024-11-02T13:21:18+00:00
- Closed at: 2024-11-03T10:39:15+00:00
