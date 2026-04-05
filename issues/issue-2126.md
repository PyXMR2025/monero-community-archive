---
title: GPU AMD x555 MacOS errors
source_url: https://github.com/xmrig/xmrig/issues/2126
author: uhlhosting
assignees: []
labels: []
created_at: '2021-02-23T04:03:01+00:00'
updated_at: '2021-05-12T05:19:53+00:00'
type: issue
status: closed
closed_at: '2021-04-12T14:10:48+00:00'
---

# Original Description
**Describe the bug**
Unable to compile on macOS without errors. 

**To Reproduce**
Latest macOS Big Sur, tried to compile from scratch, yet the following occurs at startup:

```
xmrig
[2021-02-23 04:57:21.107] unable to open "/usr/local/Cellar/xmrig/6.9.0/bin/config.json".
[2021-02-23 04:57:21.230] Error CL_INVALID_OPERATION when calling clGetDeviceInfo, param 0x4037
 * ABOUT        XMRig/6.9.0 clang/12.0.0
 * LIBS         libuv/1.41.0 OpenSSL/1.1.1j hwloc/2.4.0
 * HUGE PAGES   supported
 * 1GB PAGES    unavailable
 * CPU          Intel(R) Core(TM) i7-8750H CPU @ 2.20GHz (1) 64-bit AES
                L2:1.5 MB L3:9.0 MB 6C/12T NUMA:1
 * MEMORY       10.8/16.0 GB (68%)
                DIMM_A0: 8 GB DDR4 @ 2400 MHz HMA81GS6AFR8N-UH    
                DIMM_B0: 8 GB DDR4 @ 2400 MHz HMA81GS6AFR8N-UH    
 * MOTHERBOARD  Apple Inc. - Mac-937A206F2EE63C01
 * DONATE       1%
 * ASSEMBLY     auto:intel
 * POOL #1      dook.xyz:4202 coin monero
 * COMMANDS     hashrate, pause, resume, results, connection
[2021-02-23 04:57:21.242] Error CL_INVALID_OPERATION when calling clGetDeviceInfo, param 0x4037
 * OPENCL       #0 Apple/OpenCL 1.2 (Feb  7 2021 06:38:55)
 * OPENCL GPU   #0 n/a Intel(R) UHD Graphics 630 1100 MHz cu:24 mem:384/1536 MB
 * OPENCL GPU   #1 n/a AMD Radeon Pro 555X Compute Engine 300 MHz cu:12 mem:1024/4096 MB
 * CUDA         disabled
[2021-02-23 04:57:21.790]  net      use pool dook.xyz:4202  73.42.112.158
[2021-02-23 04:57:21.790]  net      new job from dook.xyz:4202 diff 25000 algo rx/0 height 2302857
[2021-02-23 04:57:21.790]  cpu      use argon2 implementation AVX2
[2021-02-23 04:57:21.790]  randomx  init dataset algo rx/0 (12 threads) seed 5eb9cd5d20b72ec0...
[2021-02-23 04:57:23.833]  randomx  allocated 2336 MB (2080+256) huge pages 0% 0/1168 +JIT (2043 ms)
[2021-02-23 04:57:28.734]  randomx  dataset ready (4901 ms)
[2021-02-23 04:57:28.734]  cpu      use profile  rx  (5 threads) scratchpad 2048 KB
[2021-02-23 04:57:28.763]  opencl   use profile  rx  (3 threads) scratchpad 2048 KB
|  # | GPU |  BUS ID | INTENSITY | WSIZE | MEMORY | NAME
|  0 |   0 |     n/a |       320 |     8 |    640 | Intel(R) UHD Graphics 630
|  1 |   1 |     n/a |       192 |     8 |    384 | AMD Radeon Pro 555X Compute Engine
|  2 |   1 |     n/a |       192 |     8 |    384 | AMD Radeon Pro 555X Compute Engine
[2021-02-23 04:57:31.277]  cpu      READY threads 5/5 (5) huge pages 60% 3/5 memory 10240 KB (2543 ms)
[2021-02-23 04:57:31.285]  opencl   GPU #0 compiling...
[2021-02-23 04:57:31.287]  opencl   error CL_BUILD_PROGRAM_FAILURE when calling clBuildProgram
BUILD LOG:
<program source>:767:6: warning: no previous prototype for function 'get_byte32'
uint get_byte32(uint a,uint start_bit) { return (a>>start_bit)&0xFF; }
     ^
<program source>:1019:7: warning: no previous prototype for function 'rotr64'
ulong rotr64(ulong a,ulong shift) { return rotate(a,64-shift); }
      ^
<program source>:1043:6: warning: no previous prototype for function 'blake2b_512_process_single_block'
void blake2b_512_process_single_block(ulong *h,const ulong* m,uint blockTemplateSize)
     ^
<program source>:1104:6: warning: no previous prototype for function 'blake2b_512_process_double_block_32'
void blake2b_512_process_double_block_name(ulong *out,ulong* m,__global const ulong* in)
     ^
<program source>:1102:47: note: expanded from macro 'blake2b_512_process_double_block_name'
#define blake2b_512_process_double_block_name blake2b_512_process_double_block_32
                                              ^
<program source>:1181:6: warning: no previous prototype for function 'blake2b_512_process_double_block_64'
[2021-02-23 04:57:31.287]  opencl   thread #0 failed with error CL_INVALID_PROGRAM
[2021-02-23 04:57:31.289]  opencl   thread #0 self-test failed
[2021-02-23 04:57:32.000]  opencl   GPU #1 compiling...
[2021-02-23 04:57:32.005]  opencl   GPU #1 compilation completed (5 ms)
[2021-02-23 04:57:32.006]  opencl   error CL_INVALID_VALUE when calling clGetProgramInfo
[2021-02-23 04:57:32.007]  opencl   GPU #1 compiling...
[2021-02-23 04:57:32.010]  opencl   GPU #1 compilation completed (2 ms)
[2021-02-23 04:57:32.010]  opencl   error CL_INVALID_VALUE when calling clGetProgramInfo
[2021-02-23 04:57:32.011]  opencl   READY threads 2/3 (733 ms)
```


**Expected behavior**
I would not expect to see errors at all.

**Required data**
 - OS: MacOS
 - For GPU related issues: X555 AMD Apple version latest drivers shipped with Big Sur
- config.json:

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
        "wrmsr": false,
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
        "argon2": [0, 2, 4, 6, 8, 10, 7, 9, 11],
        "astrobwt": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
        "cn": [
            [1, 0],
            [1, 2],
            [1, 4],
            [1, 6],
            [1, 8]
        ],
        "cn-heavy": [
            [1, 0],
            [1, 2]
        ],
        "cn-lite": [
            [1, 0],
            [1, 2],
            [1, 4],
            [1, 6],
            [1, 8],
            [1, 10],
            [1, 7],
            [1, 9],
            [1, 11]
        ],
        "cn-pico": [
            [2, 0],
            [2, 1],
            [2, 2],
            [2, 3],
            [2, 4],
            [2, 5],
            [2, 6],
            [2, 7],
            [2, 8],
            [2, 9],
            [2, 10],
            [2, 11]
        ],
        "rx": [0, 2, 4, 6, 8],
        "rx/arq": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
        "rx/wow": [0, 2, 4, 6, 8, 10, 7, 9, 11],
        "cn/0": false,
        "cn-lite/0": false,
        "rx/keva": "rx/wow"
    },
    "opencl": {
        "enabled": true,
        "cache": true,
        "loader": null,
        "astrobwt": [
            {
                "index": 0,
                "intensity": 64,
                "threads": [-1, -1]
            },
            {
                "index": 1,
                "intensity": 192,
                "threads": [-1, -1]
            }
        ],
        "cn": [
            {
                "index": 1,
                "intensity": 192,
                "worksize": 8,
                "strided_index": [1, 2],
                "threads": [-1, -1],
                "unroll": 8
            }
        ],
        "cn-heavy": [
            {
                "index": 1,
                "intensity": 48,
                "worksize": 8,
                "strided_index": [1, 2],
                "threads": [-1, -1],
                "unroll": 8
            }
        ],
        "cn-lite": [
            {
                "index": 0,
                "intensity": 192,
                "worksize": 8,
                "strided_index": [0, 2],
                "threads": [-1],
                "unroll": 8
            },
            {
                "index": 1,
                "intensity": 432,
                "worksize": 8,
                "strided_index": [1, 2],
                "threads": [-1, -1],
                "unroll": 8
            }
        ],
        "cn-pico": [
            {
                "index": 0,
                "intensity": 384,
                "worksize": 8,
                "strided_index": [0, 2],
                "threads": [-1],
                "unroll": 8
            },
            {
                "index": 1,
                "intensity": 960,
                "worksize": 8,
                "strided_index": [2, 2],
                "threads": [-1, -1],
                "unroll": 8
            }
        ],
        "cn/2": [
            {
                "index": 1,
                "intensity": 192,
                "worksize": 8,
                "strided_index": [2, 2],
                "threads": [-1, -1],
                "unroll": 8
            }
        ],
        "kawpow": [
            {
                "index": 0,
                "intensity": 6291456,
                "worksize": 256,
                "threads": [-1]
            },
            {
                "index": 1,
                "intensity": 3145728,
                "worksize": 256,
                "threads": [-1]
            }
        ],
        "rx": [
            {
                "index": 0,
                "intensity": 320,
                "worksize": 8,
                "threads": [-1],
                "bfactor": 6,
                "gcn_asm": false,
                "dataset_host": true
            },
            {
                "index": 1,
                "intensity": 192,
                "worksize": 8,
                "threads": [-1, -1],
                "bfactor": 6,
                "gcn_asm": false,
                "dataset_host": false
            }
        ],
        "rx/arq": [
            {
                "index": 0,
                "intensity": 384,
                "worksize": 8,
                "threads": [-1],
                "bfactor": 6,
                "gcn_asm": false,
                "dataset_host": true
            },
            {
                "index": 1,
                "intensity": 192,
                "worksize": 8,
                "threads": [-1, -1],
                "bfactor": 6,
                "gcn_asm": false,
                "dataset_host": false
            }
        ],
        "rx/wow": [
            {
                "index": 0,
                "intensity": 384,
                "worksize": 8,
                "threads": [-1],
                "bfactor": 6,
                "gcn_asm": false,
                "dataset_host": true
            },
            {
                "index": 1,
                "intensity": 192,
                "worksize": 8,
                "threads": [-1, -1],
                "bfactor": 6,
                "gcn_asm": false,
                "dataset_host": false
            }
        ],
        "cn/0": false,
        "cn-lite/0": false
    },
    "cuda": {
        "enabled": false,
        "loader": null
    },
    "log-file": null,
    "donate-level": 1,
    "donate-over-proxy": 1,
    "pools": [
        {
            "algo": "rx/0",
            "coin": "monero",
            "url": ":",
            "user": "",
            "pass": "@Revenger",
            "rig-id": null,
            "nicehash": false,
            "keepalive": true,
            "enabled": true,
            "tls": false,
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
    "user-agent": null,
    "verbose": 0,
    "watch": true,
    "pause-on-battery": false,
    "pause-on-active": false
}


**Additional context**



# Discussion History
## Lonnegan | 2021-02-23T08:50:10+00:00
Don't mine Monero on GPUs! Monero's RandomX algo is a CPU algo, mining it on GPUs, on such a slow one at that, is a waste of energy.

## uhlhosting | 2021-02-23T09:33:45+00:00
This isn't the issue, idea behind was to avoid my pc to crash when has the GPU active. 

## SChernykh | 2021-02-23T09:37:39+00:00
The compilation error you have happens on GPU #0 Intel(R) UHD Graphics 630. This GPU is absolutely not supported by XMRig, just disable it in the config. The other GPU (AMD Radeon Pro 555X) compiles RandomX code fine according to your log.

## uhlhosting | 2021-02-23T10:30:26+00:00
I would surely disable the Integrated INtel if I knew how. Can you point me to some docs on that?

## SChernykh | 2021-02-23T10:39:38+00:00
Just edit your config.json and remove all blocks with `"index": 0,` in opencl section.

## bolerap | 2021-02-27T02:15:57+00:00
> The compilation error you have happens on GPU #0 Intel(R) UHD Graphics 630. This GPU is absolutely not supported by XMRig, just disable it in the config. The other GPU (AMD Radeon Pro 555X) compiles RandomX code fine according to your log.

How can i specify using only one AMD GPU?
this is my list GPU 
`
[2021-02-27 09:03:51.403] Error CL_INVALID_OPERATION when calling clGetDeviceInfo, param 0x4037
 * OPENCL       #0 Apple/OpenCL 1.2 (Dec 21 2020 17:26:36)
 * OPENCL GPU   #0 n/a Intel(R) UHD Graphics 630 1200 MHz cu:24 mem:384/1536 MB
 * OPENCL GPU   #1 n/a AMD Radeon Pro 5500M Compute Engine 95 MHz cu:24 mem:1020/4080 MB
`

## zhangyee | 2021-03-06T10:17:09+00:00
> > The compilation error you have happens on GPU #0 Intel(R) UHD Graphics 630. This GPU is absolutely not supported by XMRig, just disable it in the config. The other GPU (AMD Radeon Pro 555X) compiles RandomX code fine according to your log.
> 
> How can i specify using only one AMD GPU?
> this is my list GPU
> `
> [2021-02-27 09:03:51.403] Error CL_INVALID_OPERATION when calling clGetDeviceInfo, param 0x4037
> 
> * OPENCL       #0 Apple/OpenCL 1.2 (Dec 21 2020 17:26:36)
> * OPENCL GPU   #0 n/a Intel(R) UHD Graphics 630 1200 MHz cu:24 mem:384/1536 MB
> * OPENCL GPU   #1 n/a AMD Radeon Pro 5500M Compute Engine 95 MHz cu:24 mem:1020/4080 MB
>   `

xmrig --opencl --opencl-devices=1

## Sammed98 | 2021-05-12T05:19:53+00:00
Hey @uhlhosting Did it solve by running the command "xmrig --opencl --opencl-devices=1"?

# Action History
- Created by: uhlhosting | 2021-02-23T04:03:01+00:00
- Closed at: 2021-04-12T14:10:48+00:00
