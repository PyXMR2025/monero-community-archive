---
title: Cannot compile OpenCL code with clvk
source_url: https://github.com/xmrig/xmrig/issues/3600
author: akku1139
assignees: []
labels: []
created_at: '2024-12-16T13:24:40+00:00'
updated_at: '2025-06-20T11:04:51+00:00'
type: issue
status: closed
closed_at: '2025-06-20T11:04:51+00:00'
---

# Original Description
**Describe the bug**
XMRig cannot compile OpenCL code with clvk.

**To Reproduce**
1. install `clvk-git`
> clvk is a prototype implementation of OpenCL 3.0 on top of Vulkan using clspv as the compiler.
> https://wiki.archlinux.org/title/GPGPU#Others

2. edit `config.json` (`"platform": "",`)
3. set algorithm to `cn/r` `cn/half` (Probably all cryptonight)
4. run XMRig

**Expected behavior**
Mining will start successfully

**Required data**
 - XMRig version: xmrig-6.22.2
    - https://github.com/xmrig/xmrig/releases/download/v6.22.2/xmrig-6.22.2-noble-x64.tar.gz
 - Miner log as text or screenshot: https://github.com/xmrig/xmrig/issues/3600#issuecomment-2545633747
![image](https://github.com/user-attachments/assets/5c00382e-8825-43e4-844a-d5b57e57dc05)
 - Config file or command line (without wallets): https://github.com/xmrig/xmrig/issues/3600#issuecomment-2545629246
 - OS: ArchLinux
 - For GPU related issues: 
 	- GPU: Intel(R) HD Graphics 4600 (HSW GT2)
	- Driver: i915

**Additional context**
- When using `beignet-git`: almost the same output as https://github.com/xmrig/xmrig/issues/2934
- It's a problem with older Intel GPU

# Discussion History
## akku1139 | 2024-12-16T13:25:39+00:00
`config.json`

```json
{
    "pools": [
        {
            "algo": null,
            "coin": null,
            "url": "jp.moneroocean.stream:20004",
            "user": "wallet",
            "pass": "x~cn/r",
            "rig-id": null,
            "nicehash": false,
            "keepalive": false,
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
        "enabled": false,
        "huge-pages": true,
        "huge-pages-jit": false,
        "hw-aes": null,
        "priority": null,
        "memory-pool": false,
        "yield": true,
        "max-threads-hint": 100,
        "asm": true,
        "argon2-impl": null
    },
    "opencl": {
        "enabled": true,
        "cache": true,
        "loader": null,
        "platform": 0,
        "adl": false,
        "cn": [
            {
                "index": 0,
                "intensity": 8,
                "worksize": 8,
                "strided_index": [0, 2],
                "threads": [-1],
                "unroll": 8
            }
        ],
        "cn-heavy": [
            {
                "index": 0,
                "intensity": 8,
                "worksize": 8,
                "strided_index": [0, 2],
                "threads": [-1],
                "unroll": 8
            }
        ],
        "cn-lite": [
            {
                "index": 0,
                "intensity": 16,
                "worksize": 8,
                "strided_index": [0, 2],
                "threads": [-1],
                "unroll": 8
            }
        ],
        "cn-pico": [
            {
                "index": 0,
                "intensity": 16,
                "worksize": 8,
                "strided_index": [0, 2],
                "threads": [-1],
                "unroll": 8
            }
        ],
        "cn/2": [
            {
                "index": 0,
                "intensity": 8,
                "worksize": 8,
                "strided_index": [0, 2],
                "threads": [-1],
                "unroll": 8
            }
        ],
        "cn/upx2": [
            {
                "index": 0,
                "intensity": 16,
                "worksize": 8,
                "strided_index": [0, 2],
                "threads": [-1],
                "unroll": 8
            }
        ],
        "kawpow": [
            {
                "index": 0,
                "intensity": 262144,
                "worksize": 256,
                "threads": [-1],
                "unroll": 1
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
            }
        ],
        "rx/arq": [
            {
                "index": 0,
                "intensity": 2688,
                "worksize": 8,
                "threads": [-1],
                "bfactor": 6,
                "gcn_asm": false,
                "dataset_host": true
            }
        ],
        "rx/wow": [
            {
                "index": 0,
                "intensity": 704,
                "worksize": 8,
                "threads": [-1],
                "bfactor": 6,
                "gcn_asm": false,
                "dataset_host": true
            }
        ],
        "cn-lite/0": false,
        "cn/0": false
    },
    "cuda": {
        "enabled": false,
        "loader": null,
        "nvml": true,
        "cn-lite/0": false,
        "cn/0": false
    },
    "log-file": null,
    "donate-level": 1,
    "donate-over-proxy": 1,
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

## akku1139 | 2024-12-16T13:27:44+00:00
Full log as text

```
MESA-INTEL: warning: Haswell Vulkan support is incomplete
 * ABOUT        XMRig/6.22.2 gcc/13.2.0 (built for Linux x86-64, 64 bit)
 * LIBS         libuv/1.49.2 OpenSSL/3.0.15 hwloc/2.11.2
 * HUGE PAGES   supported
 * 1GB PAGES    disabled
 * CPU          Intel(R) Core(TM) i7-4770S CPU @ 3.10GHz (1) 64-bit AES
                L2:1.0 MB L3:8.0 MB 4C/8T NUMA:1
 * MEMORY       7.5/15.5 GB (48%)
                DIMM1: 8 GB DDR3 @ 1600 MHz DDR3 1600 2OZ
                DIMM2: 8 GB DDR3 @ 1600 MHz DDR3 1600 2OZ
 * MOTHERBOARD  Dell Inc. - 02YRK5
 * DONATE       1%
 * ASSEMBLY     auto:intel
 * POOL #1      jp.moneroocean.stream:20004 algo auto
 * COMMANDS     hashrate, pause, resume, results, connection
 * ADL          disabled
 * OPENCL       #0 clvk/OpenCL 3.0 clvk
 * OPENCL GPU   #0 n/a Intel(R) HD Graphics 4600 (HSW GT2) 0 MHz cu:1 mem:1536/1536 MB
 * CUDA         disabled
[2024-12-16 22:26:16.680]  net      use pool jp.moneroocean.stream:20004 TLSv1.3 5.104.84.79
[2024-12-16 22:26:16.680]  net      fingerprint (SHA-256): "239daadd5c7d0ac097376c7871f787738826eef1c024729eff870e473b970855"
[2024-12-16 22:26:16.680]  net      new job from jp.moneroocean.stream:20004 diff 26469 algo cn/half height 3416153
[2024-12-16 22:26:16.680]  opencl   use profile  cn/2  (1 thread) scratchpad 2048 KB
|  # | GPU |  BUS ID | INTENSITY | WSIZE | MEMORY | NAME
|  0 |   0 |     n/a |         8 |     8 |     16 | Intel(R) HD Graphics 4600 (HSW GT2)
[2024-12-16 22:26:16.681]  opencl   GPU #0 compiling...
[2024-12-16 22:26:17.046]  opencl   error CL_BUILD_PROGRAM_FAILURE when calling clBuildProgram
BUILD LOG:
clvk-zhlvte/source.cl:153:16: error: use of undeclared identifier 'amd_bfe'
  153 | key.s0 ^= AES0[BYTE(X.s0,0)]^AES1[BYTE(X.s1,1)]^AES2[BYTE(X.s2,2)]^AES3[BYTE(X.s3,3)];
      |                ^
clvk-zhlvte/source.cl:136:21: note: expanded from macro 'BYTE'
  136 | #define BYTE(x, y) (amd_bfe((x), (y) << 3U, 8U))
      |                     ^
clvk-zhlvte/source.cl:153:35: error: use of undeclared identifier 'amd_bfe'
  153 | key.s0 ^= AES0[BYTE(X.s0,0)]^AES1[BYTE(X.s1,1)]^AES2[BYTE(X.s2,2)]^AES3[BYTE(X.s3,3)];
      |                                   ^
clvk-zhlvte/source.cl:136:21: note: expanded from macro 'BYTE'
  136 | #define BYTE(x, y) (amd_bfe((x), (y) << 3U, 8U))
      |                     ^
clvk-zhlvte/source.cl:153:54: error: use of undeclared identifier 'amd_bfe'
  153 | key.s0 ^= AES0[BYTE(X.s0,0)]^AES1[BYTE(X.s1,1)]^AES2[BYTE(X.s2,2)]^AES3[BYTE(X.s3,3)];
      |                                                      ^
clvk-zhlvte/source.cl:136:21: note: expanded from macro 'BYTE'
  136 | #define BYTE(x, y) (amd_bfe((x), (y) << 3U, 8U))
      |                     ^
clvk-zhlvte/source.cl:153:73: error: use of undeclared identifier 'amd_bfe'
  153 | key.s0 ^= AES0[BYTE(X.s0,0)]^AES1[BYTE(X.s1,1)]^AES2[BYTE(X.s2,2)]^AES3[BYTE(X.s3,3)];
      |                                                                         ^
clvk-zhlvte/source.cl:136:21: note: expanded from macro 'BYTE'
  136 | #define BYTE(x, y) (amd_bfe((x), (y) << 3U, 8U))
      |                     ^
clvk-zhlvte/source.cl:154:16: error: use of undeclared identifier 'amd_bfe'
  154 | key.s1 ^= AES0[BYTE(X.s1,0)]^AES1[BYTE(X.s2,1)]^AES2[BYTE(X.s3,2)]^AES3[BYTE(X.s0,3)];
      |                ^
clvk-zhlvte/source.cl:136:21: note: expanded from macro 'BYTE'
  136 | #define BYTE(x, y) (amd_bfe((x), (y) << 3U, 8U))
      |                     ^
clvk-zhlvte/source.cl:154:35: error: use of undeclared identifier 'amd_bfe'
  154 | key.s1 ^= AES0[BYTE(X.s1,0)]^AES1[BYTE(X.s2,1)]^AES2[BYTE(X.s3,2)]^AES3[BYTE(X.s0,3)];
      |                                   ^
clvk-zhlvte/source.cl:136:21: note: expanded from macro 'BYTE'
  136 | #define BYTE(x, y) (amd_bfe((x), (y) << 3U, 8U))
      |                     ^
clvk-zhlvte/source.cl:154:54: error: use of undeclared identifier 'amd_bfe'
  154 | key.s1 ^= AES0[BYTE(X.s1,0)]^AES1[BYTE(X.s2,1)]^AES2[BYTE(X.s3,2)]^AES3[BYTE(X.s0,3)];
      |                                                      ^
clvk-zhlvte/source.cl:136:21: note: expanded from macro 'BYTE'
  136 | #define BYTE(x, y) (amd_bfe((x), (y) << 3U, 8U))
      |                     ^
clvk-zhlvte/source.cl:154:73: error: use of undeclared identifier 'amd_bfe'
  154 | key.s1 ^= AES0[BYTE(X.s1,0)]^AES1[BYTE(X.s2,1)]^AES2[BYTE(X.s3,2)]^AES3[BYTE(X.s0,3)];
      |                                                                         ^
clvk-zhlvte/source.cl:136:21: note: expanded from macro 'BYTE'
  136 | #define BYTE(x, y) (amd_bfe((x), (y) << 3U, 8U))
      |                     ^
clvk-zhlvte/source.cl:155:16: error: use of undeclared identifier 'amd_bfe'
  155 | key.s2 ^= AES0[BYTE(X.s2,0)]^AES1[BYTE(X.s3,1)]^AES2[BYTE(X.s0,2)]^AES3[BYTE(X.s1,3)];
      |                ^
clvk-zhlvte/source.cl:136:21: note: expanded from macro 'BYTE'
  136 | #define BYTE(x, y) (amd_bfe((x), (y) << 3U, 8U))
      |                     ^
clvk-zhlvte/source.cl:155:35: error: use of undeclared identifier 'amd_bfe'
  155 | key.s2 ^= AES0[BYTE(X.s2,0)]^AES1[BYTE(X.s3,1)]^AES2[BYTE(X.s0,2)]^AES3[BYTE(X.s1,3)];
      |                                   ^
clvk-zhlvte/source.cl:136:21: note: expanded from macro 'BYTE'
  136 | #define BYTE(x, y) (amd_bfe((x), (y) << 3U, 8U))
      |                     ^
clvk-zhlvte/source.cl:155:54: error: use of undeclared identifier 'amd_bfe'
  155 | key.s2 ^= AES0[BYTE(X.s2,0)]^AES1[BYTE(X.s3,1)]^AES2[BYTE(X.s0,2)]^AES3[BYTE(X.s1,3)];
      |                                                      ^
clvk-zhlvte/source.cl:136:21: note: expanded from macro 'BYTE'
  136 | #define BYTE(x, y) (amd_bfe((x), (y) << 3U, 8U))
      |                     ^
clvk-zhlvte/source.cl:155:73: error: use of undeclared identifier 'amd_bfe'
  155 | key.s2 ^= AES0[BYTE(X.s2,0)]^AES1[BYTE(X.s3,1)]^AES2[BYTE(X.s0,2)]^AES3[BYTE(X.s1,3)];
      |                                                                         ^
clvk-zhlvte/source.cl:136:21: note: expanded from macro 'BYTE'
  136 | #define BYTE(x, y) (amd_bfe((x), (y) << 3U, 8U))
      |                     ^
clvk-zhlvte/source.cl:156:16: error: use of undeclared identifier 'amd_bfe'
  156 | key.s3 ^= AES0[BYTE(X.s3,0)]^AES1[BYTE(X.s0,1)]^AES2[BYTE(X.s1,2)]^AES3[BYTE(X.s2,3)];
      |                ^
clvk-zhlvte/source.cl:136:21: note: expanded from macro 'BYTE'
  136 | #define BYTE(x, y) (amd_bfe((x), (y) << 3U, 8U))
      |                     ^
clvk-zhlvte/source.cl:156:35: error: use of undeclared identifier 'amd_bfe'
  156 | key.s3 ^= AES0[BYTE(X.s3,0)]^AES1[BYTE(X.s0,1)]^AES2[BYTE(X.s1,2)]^AES3[BYTE(X.s2,3)];
      |                                   ^
clvk-zhlvte/source.cl:136:21: note: expanded from macro 'BYTE'
  136 | #define BYTE(x, y) (amd_bfe((x), (y) << 3U, 8U))
      |                     ^
clvk-zhlvte/source.cl:156:54: error: use of undeclared identifier 'amd_bfe'
  156 | key.s3 ^= AES0[BYTE(X.s3,0)]^AES1[BYTE(X.s0,1)]^AES2[BYTE(X.s1,2)]^AES3[BYTE(X.s2,3)];
      |                                                      ^
clvk-zhlvte/source.cl:136:21: note: expanded from macro 'BYTE'
  136 | #define BYTE(x, y) (amd_bfe((x), (y) << 3U, 8U))
      |                     ^
clvk-zhlvte/source.cl:156:73: error: use of undeclared identifier 'amd_bfe'
  156 | key.s3 ^= AES0[BYTE(X.s3,0)]^AES1[BYTE(X.s0,1)]^AES2[BYTE(X.s1,2)]^AES3[BYTE(X.s2,3)];
      |                                                                         ^
clvk-zhlvte/source.cl:136:21: note: expanded from macro 'BYTE'
  136 | #define BYTE(x, y) (amd_bfe((x), (y) << 3U, 8U))
      |                     ^
clvk-zhlvte/source.cl:151:7: warning: no previous prototype for function 'AES_Round'
  151 | uint4 AES_Round(const __local uint *AES0,const __local uint *AES1,const __local uint *AES2,const __local uint *AES3,const uint4 X,uint4 key)
      |       ^
clvk-zhlvte/source.cl:151:1: note: declare 'static' if the function is not intended to be used outside of this translation unit
  151 | uint4 AES_Round(const __local uint *AES0,const __local uint *AES1,const __local uint *AES2,const __local uint *AES3,const uint4 X,uint4 key)
      | ^
      | static
clvk-zhlvte/source.cl:161:16: error: use of undeclared identifier 'amd_bfe'
  161 | key.s0 ^= AES0[BYTE(X.s0,0)]^AES1[BYTE(X.s1,1)]^rotate(AES0[BYTE(X.s2,2)]^AES1[BYTE(X.s3,3)],16U);
      |                ^
clvk-zhlvte/source.cl:136:21: note: expanded from macro 'BYTE'
  136 | #define BYTE(x, y) (amd_bfe((x), (y) << 3U, 8U))
      |                     ^
clvk-zhlvte/source.cl:161:35: error: use of undeclared identifier 'amd_bfe'
  161 | key.s0 ^= AES0[BYTE(X.s0,0)]^AES1[BYTE(X.s1,1)]^rotate(AES0[BYTE(X.s2,2)]^AES1[BYTE(X.s3,3)],16U);
      |                                   ^
clvk-zhlvte/source.cl:136:21: note: expanded from macro 'BYTE'
  136 | #define BYTE(x, y) (amd_bfe((x), (y) << 3U, 8U))
      |                     ^
clvk-zhlvte/source.cl:161:61: error: use of undeclared identifier 'amd_bfe'
  161 | key.s0 ^= AES0[BYTE(X.s0,0)]^AES1[BYTE(X.s1,1)]^rotate(AES0[BYTE(X.s2,2)]^AES1[BYTE(X.s3,3)],16U);
      |                                                             ^
clvk-zhlvte/source.cl:136:21: note: expanded from macro 'BYTE'
  136 | #define BYTE(x, y) (amd_bfe((x), (y) << 3U, 8U))
      |                     ^
clvk-zhlvte/source.cl:161:80: error: use of undeclared identifier 'amd_bfe'
  161 | key.s0 ^= AES0[BYTE(X.s0,0)]^AES1[BYTE(X.s1,1)]^rotate(AES0[BYTE(X.s2,2)]^AES1[BYTE(X.s3,3)],16U);
      |                                                                                ^
clvk-zhlvte/source.cl:136:21: note: expanded from macro 'BYTE'
  136 | #define BYTE(x, y) (amd_bfe((x), (y) << 3U, 8U))
      |                     ^
clvk-zhlvte/source.cl:162:16: error: use of undeclared identifier 'amd_bfe'
  162 | key.s1 ^= AES0[BYTE(X.s1,0)]^AES1[BYTE(X.s2,1)]^rotate(AES0[BYTE(X.s3,2)]^AES1[BYTE(X.s0,3)],16U);
      |                ^
clvk-zhlvte/source.cl:136:21: note: expanded from macro 'BYTE'
  136 | #define BYTE(x, y) (amd_bfe((x), (y) << 3U, 8U))
      |                     ^
clvk-zhlvte/source.cl:162:35: error: use of undeclared identifier 'amd_bfe'
  162 | key.s1 ^= AES0[BYTE(X.s1,0)]^AES1[BYTE(X.s2,1)]^rotate(AES0[BYTE(X.s3,2)]^AES1[BYTE(X.s0,3)],16U);
      |                                   ^
clvk-zhlvte/source.cl:136:21: note: expanded from macro 'BYTE'
  136 | #define BYTE(x, y) (amd_bfe((x), (y) << 3U, 8U))
      |                     ^
clvk-zhlvte/source.cl:162:61: error: use of undeclared identifier 'amd_bfe'
  162 | key.s1 ^= AES0[BYTE(X.s1,0)]^AES1[BYTE(X.s2,1)]^rotate(AES0[BYTE(X.s3,2)]^AES1[BYTE(X.s0,3)],16U);
      |                                                             ^
clvk-zhlvte/source.cl:136:21: note: expanded from macro 'BYTE'
  136 | #define BYTE(x, y) (amd_bfe((x), (y) << 3U, 8U))
      |                     ^
clvk-zhlvte/source.cl:162:80: error: use of undeclared identifier 'amd_bfe'
  162 | key.s1 ^= AES0[BYTE(X.s1,0)]^AES1[BYTE(X.s2,1)]^rotate(AES0[BYTE(X.s3,2)]^AES1[BYTE(X.s0,3)],16U);
      |                                                                                ^
clvk-zhlvte/source.cl:136:21: note: expanded from macro 'BYTE'
  136 | #define BYTE(x, y) (amd_bfe((x), (y) << 3U, 8U))
      |                     ^
clvk-zhlvte/source.cl:163:16: error: use of undeclared identifier 'amd_bfe'
  163 | key.s2 ^= AES0[BYTE(X.s2,0)]^AES1[BYTE(X.s3,1)]^rotate(AES0[BYTE(X.s0,2)]^AES1[BYTE(X.s1,3)],16U);
      |                ^
clvk-zhlvte/source.cl:136:21: note: expanded from macro 'BYTE'
  136 | #define BYTE(x, y) (amd_bfe((x), (y) << 3U, 8U))
      |                     ^
clvk-zhlvte/source.cl:163:35: error: use of undeclared identifier 'amd_bfe'
  163 | key.s2 ^= AES0[BYTE(X.s2,0)]^AES1[BYTE(X.s3,1)]^rotate(AES0[BYTE(X.s0,2)]^AES1[BYTE(X.s1,3)],16U);
      |                                   ^
clvk-zhlvte/source.cl:136:21: note: expanded from macro 'BYTE'
  136 | #define BYTE(x, y) (amd_bfe((x), (y) << 3U, 8U))
      |                     ^
clvk-zhlvte/source.cl:163:61: error: use of undeclared identifier 'amd_bfe'
  163 | key.s2 ^= AES0[BYTE(X.s2,0)]^AES1[BYTE(X.s3,1)]^rotate(AES0[BYTE(X.s0,2)]^AES1[BYTE(X.s1,3)],16U);
      |                                                             ^
clvk-zhlvte/source.cl:136:21: note: expanded from macro 'BYTE'
  136 | #define BYTE(x, y) (amd_bfe((x), (y) << 3U, 8U))
      |                     ^
clvk-zhlvte/source.cl:163:80: error: use of undeclared identifier 'amd_bfe'
  163 | key.s2 ^= AES0[BYTE(X.s2,0)]^AES1[BYTE(X.s3,1)]^rotate(AES0[BYTE(X.s0,2)]^AES1[BYTE(X.s1,3)],16U);
      |                                                                                ^
clvk-zhlvte/source.cl:136:21: note: expanded from macro 'BYTE'
  136 | #define BYTE(x, y) (amd_bfe((x), (y) << 3U, 8U))
      |                     ^
clvk-zhlvte/source.cl:164:16: error: use of undeclared identifier 'amd_bfe'
  164 | key.s3 ^= AES0[BYTE(X.s3,0)]^AES1[BYTE(X.s0,1)]^rotate(AES0[BYTE(X.s1,2)]^AES1[BYTE(X.s2,3)],16U);
      |                ^
clvk-zhlvte/source.cl:136:21: note: expanded from macro 'BYTE'
  136 | #define BYTE(x, y) (amd_bfe((x), (y) << 3U, 8U))
      |                     ^
clvk-zhlvte/source.cl:164:35: error: use of undeclared identifier 'amd_bfe'
  164 | key.s3 ^= AES0[BYTE(X.s3,0)]^AES1[BYTE(X.s0,1)]^rotate(AES0[BYTE(X.s1,2)]^AES1[BYTE(X.s2,3)],16U);
      |                                   ^
clvk-zhlvte/source.cl:136:21: note: expanded from macro 'BYTE'
  136 | #define BYTE(x, y) (amd_bfe((x), (y) << 3U, 8U))
      |                     ^
clvk-zhlvte/source.cl:164:61: error: use of undeclared identifier 'amd_bfe'
  164 | key.s3 ^= AES0[BYTE(X.s3,0)]^AES1[BYTE(X.s0,1)]^rotate(AES0[BYTE(X.s1,2)]^AES1[BYTE(X.s2,3)],16U);
      |                                                             ^
clvk-zhlvte/source.cl:136:21: note: expanded from macro 'BYTE'
  136 | #define BYTE(x, y) (amd_bfe((x), (y) << 3U, 8U))
      |                     ^
clvk-zhlvte/source.cl:164:80: error: use of undeclared identifier 'amd_bfe'
  164 | key.s3 ^= AES0[BYTE(X.s3,0)]^AES1[BYTE(X.s0,1)]^rotate(AES0[BYTE(X.s1,2)]^AES1[BYTE(X.s2,3)],16U);
      |                                                                                ^
clvk-zhlvte/source.cl:136:21: note: expanded from macro 'BYTE'
  136 | #define BYTE(x, y) (amd_bfe((x), (y) << 3U, 8U))
      |                     ^
clvk-zhlvte/source.cl:159:7: warning: no previous prototype for function 'AES_Round_Two_Tables'
  159 | uint4 AES_Round_Two_Tables(const __local uint *AES0,const __local uint *AES1,const uint4 X,uint4 key)
      |       ^
clvk-zhlvte/source.cl:159:1: note: declare 'static' if the function is not intended to be used outside of this translation unit
  159 | uint4 AES_Round_Two_Tables(const __local uint *AES0,const __local uint *AES1,const uint4 X,uint4 key)
      | ^
      | static
clvk-zhlvte/source.cl:191:31: error: use of undeclared identifier 'amd_bfe'
  191 | uint t=((!(c&7))||((c&7)==4))?SubWord(keybuf[c-1]):keybuf[c-1];
      |                               ^
clvk-zhlvte/source.cl:187:29: note: expanded from macro 'SubWord'
  187 | #define SubWord(inw) ((sbox[BYTE(inw, 3)] << 24) | (sbox[BYTE(inw, 2)] << 16) | (sbox[BYTE(inw, 1)] << 8) | sbox[BYTE(inw, 0)])
      |                             ^
clvk-zhlvte/source.cl:136:21: note: expanded from macro 'BYTE'
  136 | #define BYTE(x, y) (amd_bfe((x), (y) << 3U, 8U))
      |                     ^
clvk-zhlvte/source.cl:191:31: error: use of undeclared identifier 'amd_bfe'
clvk-zhlvte/source.cl:187:58: note: expanded from macro 'SubWord'
  187 | #define SubWord(inw) ((sbox[BYTE(inw, 3)] << 24) | (sbox[BYTE(inw, 2)] << 16) | (sbox[BYTE(inw, 1)] << 8) | sbox[BYTE(inw, 0)])
      |                                                          ^
clvk-zhlvte/source.cl:136:21: note: expanded from macro 'BYTE'
  136 | #define BYTE(x, y) (amd_bfe((x), (y) << 3U, 8U))
      |                     ^
clvk-zhlvte/source.cl:191:31: error: use of undeclared identifier 'amd_bfe'
clvk-zhlvte/source.cl:187:87: note: expanded from macro 'SubWord'
  187 | #define SubWord(inw) ((sbox[BYTE(inw, 3)] << 24) | (sbox[BYTE(inw, 2)] << 16) | (sbox[BYTE(inw, 1)] << 8) | sbox[BYTE(inw, 0)])
      |                                                                                       ^
clvk-zhlvte/source.cl:136:21: note: expanded from macro 'BYTE'
  136 | #define BYTE(x, y) (amd_bfe((x), (y) << 3U, 8U))
      |                     ^
clvk-zhlvte/source.cl:191:31: error: use of undeclared identifier 'amd_bfe'
clvk-zhlvte/source.cl:187:114: note: expanded from macro 'SubWord'
  187 | #define SubWord(inw) ((sbox[BYTE(inw, 3)] << 24) | (sbox[BYTE(inw, 2)] << 16) | (sbox[BYTE(inw, 1)] << 8) | sbox[BYTE(inw, 0)])
      |                                                                                                                  ^
clvk-zhlvte/source.cl:136:21: note: expanded from macro 'BYTE'
  136 | #define BYTE(x, y) (amd_bfe((x), (y) << 3U, 8U))
      |                     ^
clvk-zhlvte/source.cl:188:6: warning: no previous prototype for function 'AESExpandKey256'
  188 | void AESExpandKey256(uint *keybuf)
      |      ^
clvk-zhlvte/source.cl:188:1: note: declare 'static' if the function is not intended to be used outside of this translation unit
  188 | void AESExpandKey256(uint *keybuf)
      | ^
      | static
clvk-zhlvte/source.cl:238:17: error: use of undeclared identifier 'amd_bitalign'
  238 | return(as_ulong(amd_bitalign(x,x.s10,32-y)));
      |                 ^
clvk-zhlvte/source.cl:241:17: error: use of undeclared identifier 'amd_bitalign'
  241 | return(as_ulong(amd_bitalign(x.s10,x,32-(y-32))));
      |                 ^
clvk-zhlvte/source.cl:235:7: warning: no previous prototype for function 'SKEIN_ROT'
  235 | ulong SKEIN_ROT(const uint2 x,const uint y)
      |       ^
clvk-zhlvte/source.cl:235:1: note: declare 'static' if the function is not intended to be used outside of this translation unit
  235 | ulong SKEIN_ROT(const uint2 x,const uint y)
      | ^
      | static
clvk-zhlvte/source.cl:244:6: warning: no previous prototype for function 'SkeinMix8'
  244 | void SkeinMix8(ulong4 *pv0,ulong4 *pv1,const uint rc0,const uint rc1,const uint rc2,const uint rc3)
      |      ^
clvk-zhlvte/source.cl:244:1: note: declare 'static' if the function is not intended to be used outside of this translation unit
  244 | void SkeinMix8(ulong4 *pv0,ulong4 *pv1,const uint rc0,const uint rc1,const uint rc2,const uint rc3)
      | ^
      | static
clvk-zhlvte/source.cl:256:8: warning: mixing declarations and code is incompatible with standards before C99
  256 | ulong4 pv0=p.even,pv1=p.odd;
      |        ^
clvk-zhlvte/source.cl:253:8: warning: no previous prototype for function 'SkeinEvenRound'
  253 | ulong8 SkeinEvenRound(ulong8 p,const ulong8 h,const ulong *t,const uint s)
      |        ^
clvk-zhlvte/source.cl:253:1: note: declare 'static' if the function is not intended to be used outside of this translation unit
  253 | ulong8 SkeinEvenRound(ulong8 p,const ulong8 h,const ulong *t,const uint s)
      | ^
      | static
clvk-zhlvte/source.cl:272:8: warning: mixing declarations and code is incompatible with standards before C99
  272 | ulong4 pv0=p.even,pv1=p.odd;
      |        ^
clvk-zhlvte/source.cl:269:8: warning: no previous prototype for function 'SkeinOddRound'
  269 | ulong8 SkeinOddRound(ulong8 p,const ulong8 h,const ulong *t,const uint s)
      |        ^
clvk-zhlvte/source.cl:269:1: note: declare 'static' if the function is not intended to be used outside of this translation unit
  269 | ulong8 SkeinOddRound(ulong8 p,const ulong8 h,const ulong *t,const uint s)
      | ^
      | static
clvk-zhlvte/source.cl:290:24: warning: implicit conversion changes signedness: '__private int' to 'uint' (aka 'unsigned int')
  290 | p=SkeinEvenRound(p,h,t,i);
      |   ~~~~~~~~~~~~~~       ^
clvk-zhlvte/source.cl:296:23: warning: implicit conversion changes signedness: '__private int' to 'uint' (aka 'unsigned int')
  296 | p=SkeinOddRound(p,h,t,i);
      |   ~~~~~~~~~~~~~       ^
clvk-zhlvte/source.cl:292:7: warning: mixing declarations and code is incompatible with standards before C99
  292 | ulong tmp=h.s0;
      |       ^
clvk-zhlvte/source.cl:285:8: warning: no previous prototype for function 'Skein512Block'
  285 | ulong8 Skein512Block(ulong8 p,ulong8 h,ulong h8,const ulong *t)
      |        ^
clvk-zhlvte/source.cl:285:1: note: declare 'static' if the function is not intended to be used outside of this translation unit
  285 | ulong8 Skein512Block(ulong8 p,ulong8 h,ulong h8,const ulong *t)
      | ^
      | static
clvk-zhlvte/source.cl:446:5: warning: 'SPH_SMALL_FOOTPRINT_JH' is not defined, evaluates to 0
  446 | #if SPH_SMALL_FOOTPRINT_JH
      |     ^
clvk-zhlvte/source.cl:309:9: warning: macro is not used
  309 | #define SPH_C64(x)      x
      |         ^
clvk-zhlvte/source.cl:319:9: warning: macro is not used
  319 | #define C64e(x) ((SPH_C64(x) >> 56) \
      |         ^
clvk-zhlvte/source.cl:814:24: warning: implicit conversion changes signedness: 'int' to 'uint' (aka 'unsigned int')
  814 | return (as_uint(r)<<9)-convert_int_rte(h*r_scaled);
      |                       ~^~~~~~~~~~~~~~~~~~~~~~~~~~~
clvk-zhlvte/source.cl:821:11: warning: implicit conversion changes signedness: 'ulong' (aka 'unsigned long') to 'long'
  821 | long tmp=a-((ulong)(q)*b);
      |      ~~~ ~^~~~~~~~~~~~~~~
clvk-zhlvte/source.cl:825:28: warning: implicit conversion changes signedness: 'const __private int' to 'uint' (aka 'unsigned int')
  825 | return (uint2)(q+overshoot-undershoot,as_uint2(tmp).s0+(as_uint(overshoot)&b)-(as_uint(undershoot)&b));
      |                           ~^~~~~~~~~~
clvk-zhlvte/source.cl:825:18: warning: implicit conversion changes signedness: 'const __private int' to 'uint' (aka 'unsigned int')
  825 | return (uint2)(q+overshoot-undershoot,as_uint2(tmp).s0+(as_uint(overshoot)&b)-(as_uint(undershoot)&b));
      |                 ~^~~~~~~~~
clvk-zhlvte/source.cl:823:11: warning: mixing declarations and code is incompatible with standards before C99
  823 | const int overshoot=((int*)&tmp)[1]>>31;
      |           ^
clvk-zhlvte/source.cl:834:21: warning: implicit conversion changes signedness: 'ulong' (aka 'unsigned long') to 'long'
  834 | const long delta0=n1-(as_ulong((uint2)(mul24(x0,x0),mul_hi(x0,x0)))<<18);
      |            ~~~~~~ ~~^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
clvk-zhlvte/source.cl:836:22: warning: implicit conversion changes signedness: 'int' to 'uint' (aka 'unsigned int')
  836 | uint result=(x0<<10)+convert_int_rte(delta);
      |                     ~^~~~~~~~~~~~~~~~~~~~~~
clvk-zhlvte/source.cl:840:14: warning: implicit conversion changes signedness: 'int' to 'ulong' (aka 'unsigned long')
  840 | if((long)(x2+as_int(b-1))>=0) --result;
      |             ~^~~~~~~~~~~
include/opencl-c-base.h:598:19: note: expanded from macro 'as_int'
  598 | #define as_int(x) __builtin_astype((x), int)
      |                   ^~~~~~~~~~~~~~~~~~~~~~~~~~
clvk-zhlvte/source.cl:833:12: warning: mixing declarations and code is incompatible with standards before C99
  833 | const uint x0=as_uint(x)-(158U<<23);
      |            ^
clvk-zhlvte/source.cl:918:10: warning: declaration shadows a local variable
  918 | for (int i=0; i<25; i+=5) {
      |          ^
clvk-zhlvte/source.cl:892:5: note: previous declaration is here
  892 | int i,round;
      |     ^
clvk-zhlvte/source.cl:890:6: warning: no previous prototype for function 'keccakf1600_1'
  890 | void keccakf1600_1(ulong *st)
      |      ^
clvk-zhlvte/source.cl:890:1: note: declare 'static' if the function is not intended to be used outside of this translation unit
  890 | void keccakf1600_1(ulong *st)
      | ^
      | static
clvk-zhlvte/source.cl:976:10: warning: declaration shadows a local variable
  976 | for (int i=0; i<25; i+=5) {
      |          ^
clvk-zhlvte/source.cl:934:5: note: previous declaration is here
  934 | int i,round;
      |     ^
clvk-zhlvte/source.cl:932:6: warning: no previous prototype for function 'keccakf1600_2'
  932 | void keccakf1600_2(__local ulong *st)
      |      ^
clvk-zhlvte/source.cl:932:1: note: declare 'static' if the function is not intended to be used outside of this translation unit
  932 | void keccakf1600_2(__local ulong *st)
      | ^
      | static
clvk-zhlvte/source.cl:1016:29: warning: implicit conversion changes signedness: 'unsigned int' to 'int'
 1016 | for (int i=get_local_id(1)*8+get_local_id(0); i<256; i+=8*8) {
      |          ~ ~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~
clvk-zhlvte/source.cl:1068:2: warning: cast from '__private uint *' (aka '__private unsigned int *') to '__private ulong *' (aka '__private unsigned long *') increases required alignment from 4 to 8
 1068 | ((ulong *)ExpandedKey1)[i]=states[i];
      |  ^~~~~~~~~~~~~~~~~~~~~
clvk-zhlvte/source.cl:1098:10: warning: cast from '__private uint *' (aka '__private unsigned int *') to '__private uint4 *' increases required alignment from 4 to 16
 1098 | uint4 t=((uint4 *)ExpandedKey1)[j];
      |          ^~~~~~~~~~~~~~~~~~~~~
clvk-zhlvte/source.cl:1099:14: error: use of undeclared identifier 'amd_bfe'
 1099 | t.s0 ^= AES0[BYTE(text.s0,0)]^AES1[BYTE(text.s1,1)]^AES2[BYTE(text.s2,2)]^AES3[BYTE(text.s3,3)];
      |              ^
clvk-zhlvte/source.cl:136:21: note: expanded from macro 'BYTE'
  136 | #define BYTE(x, y) (amd_bfe((x), (y) << 3U, 8U))
      |                     ^
clvk-zhlvte/source.cl:1099:36: error: use of undeclared identifier 'amd_bfe'
 1099 | t.s0 ^= AES0[BYTE(text.s0,0)]^AES1[BYTE(text.s1,1)]^AES2[BYTE(text.s2,2)]^AES3[BYTE(text.s3,3)];
      |                                    ^
clvk-zhlvte/source.cl:136:21: note: expanded from macro 'BYTE'
  136 | #define BYTE(x, y) (amd_bfe((x), (y) << 3U, 8U))
      |                     ^
clvk-zhlvte/source.cl:1099:58: error: use of undeclared identifier 'amd_bfe'
 1099 | t.s0 ^= AES0[BYTE(text.s0,0)]^AES1[BYTE(text.s1,1)]^AES2[BYTE(text.s2,2)]^AES3[BYTE(text.s3,3)];
      |                                                          ^
clvk-zhlvte/source.cl:136:21: note: expanded from macro 'BYTE'
  136 | #define BYTE(x, y) (amd_bfe((x), (y) << 3U, 8U))
      |                     ^
clvk-zhlvte/source.cl:1099:80: error: use of undeclared identifier 'amd_bfe'
 1099 | t.s0 ^= AES0[BYTE(text.s0,0)]^AES1[BYTE(text.s1,1)]^AES2[BYTE(text.s2,2)]^AES3[BYTE(text.s3,3)];
      |                                                                                ^
clvk-zhlvte/source.cl:136:21: note: expanded from macro 'BYTE'
  136 | #define BYTE(x, y) (amd_bfe((x), (y) << 3U, 8U))
      |                     ^
clvk-zhlvte/source.cl:1100:14: error: use of undeclared identifier 'amd_bfe'
 1100 | t.s1 ^= AES0[BYTE(text.s1,0)]^AES1[BYTE(text.s2,1)]^AES2[BYTE(text.s3,2)]^AES3[BYTE(text.s0,3)];
      |              ^
clvk-zhlvte/source.cl:136:21: note: expanded from macro 'BYTE'
  136 | #define BYTE(x, y) (amd_bfe((x), (y) << 3U, 8U))
      |                     ^
clvk-zhlvte/source.cl:1100:36: error: use of undeclared identifier 'amd_bfe'
 1100 | t.s1 ^= AES0[BYTE(text.s1,0)]^AES1[BYTE(text.s2,1)]^AES2[BYTE(text.s3,2)]^AES3[BYTE(text.s0,3)];
      |                                    ^
clvk-zhlvte/source.cl:136:21: note: expanded from macro 'BYTE'
  136 | #define BYTE(x, y) (amd_bfe((x), (y) << 3U, 8U))
      |                     ^
clvk-zhlvte/source.cl:1100:58: error: use of undeclared identifier 'amd_bfe'
 1100 | t.s1 ^= AES0[BYTE(text.s1,0)]^AES1[BYTE(text.s2,1)]^AES2[BYTE(text.s3,2)]^AES3[BYTE(text.s0,3)];
      |                                                          ^
clvk-zhlvte/source.cl:136:21: note: expanded from macro 'BYTE'
  136 | #define BYTE(x, y) (amd_bfe((x), (y) << 3U, 8U))
      |                     ^
clvk-zhlvte/source.cl:1100:80: error: use of undeclared identifier 'amd_bfe'
 1100 | t.s1 ^= AES0[BYTE(text.s1,0)]^AES1[BYTE(text.s2,1)]^AES2[BYTE(text.s3,2)]^AES3[BYTE(text.s0,3)];
      |                                                                                ^
clvk-zhlvte/source.cl:136:21: note: expanded from macro 'BYTE'
  136 | #define BYTE(x, y) (amd_bfe((x), (y) << 3U, 8U))
      |                     ^
clvk-zhlvte/source.cl:1101:14: error: use of undeclared identifier 'amd_bfe'
 1101 | t.s2 ^= AES0[BYTE(text.s2,0)]^AES1[BYTE(text.s3,1)]^AES2[BYTE(text.s0,2)]^AES3[BYTE(text.s1,3)];
      |              ^
clvk-zhlvte/source.cl:136:21: note: expanded from macro 'BYTE'
  136 | #define BYTE(x, y) (amd_bfe((x), (y) << 3U, 8U))
      |                     ^
clvk-zhlvte/source.cl:1101:36: error: use of undeclared identifier 'amd_bfe'
 1101 | t.s2 ^= AES0[BYTE(text.s2,0)]^AES1[BYTE(text.s3,1)]^AES2[BYTE(text.s0,2)]^AES3[BYTE(text.s1,3)];
      |                                    ^
clvk-zhlvte/source.cl:136:21: note: expanded from macro 'BYTE'
  136 | #define BYTE(x, y) (amd_bfe((x), (y) << 3U, 8U))
      |                     ^
clvk-zhlvte/source.cl:1101:58: error: use of undeclared identifier 'amd_bfe'
 1101 | t.s2 ^= AES0[BYTE(text.s2,0)]^AES1[BYTE(text.s3,1)]^AES2[BYTE(text.s0,2)]^AES3[BYTE(text.s1,3)];
      |                                                          ^
clvk-zhlvte/source.cl:136:21: note: expanded from macro 'BYTE'
  136 | #define BYTE(x, y) (amd_bfe((x), (y) << 3U, 8U))
      |                     ^
clvk-zhlvte/source.cl:1101:80: error: use of undeclared identifier 'amd_bfe'
 1101 | t.s2 ^= AES0[BYTE(text.s2,0)]^AES1[BYTE(text.s3,1)]^AES2[BYTE(text.s0,2)]^AES3[BYTE(text.s1,3)];
      |                                                                                ^
clvk-zhlvte/source.cl:136:21: note: expanded from macro 'BYTE'
  136 | #define BYTE(x, y) (amd_bfe((x), (y) << 3U, 8U))
      |                     ^
clvk-zhlvte/source.cl:1102:14: error: use of undeclared identifier 'amd_bfe'
 1102 | t.s3 ^= AES0[BYTE(text.s3,0)]^AES1[BYTE(text.s0,1)]^AES2[BYTE(text.s1,2)]^AES3[BYTE(text.s2,3)];
      |              ^
clvk-zhlvte/source.cl:136:21: note: expanded from macro 'BYTE'
  136 | #define BYTE(x, y) (amd_bfe((x), (y) << 3U, 8U))
      |                     ^
clvk-zhlvte/source.cl:1102:36: error: use of undeclared identifier 'amd_bfe'
 1102 | t.s3 ^= AES0[BYTE(text.s3,0)]^AES1[BYTE(text.s0,1)]^AES2[BYTE(text.s1,2)]^AES3[BYTE(text.s2,3)];
      |                                    ^
clvk-zhlvte/source.cl:136:21: note: expanded from macro 'BYTE'
  136 | #define BYTE(x, y) (amd_bfe((x), (y) << 3U, 8U))
      |                     ^
clvk-zhlvte/source.cl:1102:58: error: use of undeclared identifier 'amd_bfe'
 1102 | t.s3 ^= AES0[BYTE(text.s3,0)]^AES1[BYTE(text.s0,1)]^AES2[BYTE(text.s1,2)]^AES3[BYTE(text.s2,3)];
      |                                                          ^
clvk-zhlvte/source.cl:136:21: note: expanded from macro 'BYTE'
  136 | #define BYTE(x, y) (amd_bfe((x), (y) << 3U, 8U))
      |                     ^
clvk-zhlvte/source.cl:1102:80: error: use of undeclared identifier 'amd_bfe'
 1102 | t.s3 ^= AES0[BYTE(text.s3,0)]^AES1[BYTE(text.s0,1)]^AES2[BYTE(text.s1,2)]^AES3[BYTE(text.s2,3)];
      |                                                                                ^
clvk-zhlvte/source.cl:136:21: note: expanded from macro 'BYTE'
  136 | #define BYTE(x, y) (amd_bfe((x), (y) << 3U, 8U))
      |                     ^
clvk-zhlvte/source.cl:1024:15: warning: mixing declarations and code is incompatible with standards before C99
 1024 | __local ulong State_buf[8*25];
      |               ^
clvk-zhlvte/source.cl:1010:106: warning: unused parameter 'Threads'
 1010 | __kernel void cn0(__global ulong *input,int inlen,__global uint4 *Scratchpad,__global ulong *states,uint Threads)
      |                                                                                                          ^
clvk-zhlvte/source.cl:1015:17: warning: implicit conversion loses integer precision: 'ulong' (aka 'unsigned long') to 'uint' (aka 'unsigned int')
 1015 | const uint gIdx=getIdx();
      |            ~~~~ ^~~~~~~~
clvk-zhlvte/source.cl:1295:11: warning: implicit conversion changes signedness: 'unsigned int' to 'int'
 1295 | for(int i=get_local_id(0); i<256; i+=WORKSIZE)
      |         ~ ^~~~~~~~~~~~~~~
clvk-zhlvte/source.cl:1324:13: warning: cast from '__private ulong *' (aka '__private unsigned long *') to '__private ulong2 *' increases required alignment from 8 to 16
 1324 | ulong2 bx0=((ulong2 *)b)[0];
      |             ^~~~~~~~~~~
clvk-zhlvte/source.cl:1325:13: warning: cast from '__private ulong *' (aka '__private unsigned long *') to '__private ulong2 *' increases required alignment from 8 to 16
 1325 | ulong2 bx1=((ulong2 *)b)[1];
      |             ^~~~~~~~~~~
clvk-zhlvte/source.cl:1352:9: warning: cast from '__global uchar *' (aka '__global unsigned char *') to '__global uint4 *' increases required alignment from 1 to 16
 1352 | uint4 c=SCRATCHPAD_CHUNK(0);
      |         ^~~~~~~~~~~~~~~~~~~
clvk-zhlvte/source.cl:1333:31: note: expanded from macro 'SCRATCHPAD_CHUNK'
 1333 | #define SCRATCHPAD_CHUNK(N) (*(__global uint4*)((__global uchar*)(Scratchpad) + (idx ^ (N << 4))))
      |                               ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
clvk-zhlvte/source.cl:1353:36: warning: cast from '__private ulong *' (aka '__private unsigned long *') to '__private uint4 *' increases required alignment from 8 to 16
 1353 | c=AES_Round(AES0,AES1,AES2,AES3,c,((uint4 *)a)[0]);
      |                                    ^~~~~~~~~~
clvk-zhlvte/source.cl:1360:31: warning: cast from '__global uchar *' (aka '__global unsigned char *') to '__global uint4 *' increases required alignment from 1 to 16
 1360 | const ulong2 chunk1=as_ulong2(SCRATCHPAD_CHUNK(1));
      |                     ~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~
clvk-zhlvte/source.cl:1333:31: note: expanded from macro 'SCRATCHPAD_CHUNK'
 1333 | #define SCRATCHPAD_CHUNK(N) (*(__global uint4*)((__global uchar*)(Scratchpad) + (idx ^ (N << 4))))
      |                               ^
include/opencl-c-base.h:620:40: note: expanded from macro 'as_ulong2'
  620 | #define as_ulong2(x) __builtin_astype((x), ulong2)
      |                                        ^
clvk-zhlvte/source.cl:1361:31: warning: cast from '__global uchar *' (aka '__global unsigned char *') to '__global uint4 *' increases required alignment from 1 to 16
 1361 | const ulong2 chunk2=as_ulong2(SCRATCHPAD_CHUNK(2));
      |                     ~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~
clvk-zhlvte/source.cl:1333:31: note: expanded from macro 'SCRATCHPAD_CHUNK'
 1333 | #define SCRATCHPAD_CHUNK(N) (*(__global uint4*)((__global uchar*)(Scratchpad) + (idx ^ (N << 4))))
      |                               ^
include/opencl-c-base.h:620:40: note: expanded from macro 'as_ulong2'
  620 | #define as_ulong2(x) __builtin_astype((x), ulong2)
      |                                        ^
clvk-zhlvte/source.cl:1362:31: warning: cast from '__global uchar *' (aka '__global unsigned char *') to '__global uint4 *' increases required alignment from 1 to 16
 1362 | const ulong2 chunk3=as_ulong2(SCRATCHPAD_CHUNK(3));
      |                     ~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~
clvk-zhlvte/source.cl:1333:31: note: expanded from macro 'SCRATCHPAD_CHUNK'
 1333 | #define SCRATCHPAD_CHUNK(N) (*(__global uint4*)((__global uchar*)(Scratchpad) + (idx ^ (N << 4))))
      |                               ^
include/opencl-c-base.h:620:40: note: expanded from macro 'as_ulong2'
  620 | #define as_ulong2(x) __builtin_astype((x), ulong2)
      |                                        ^
clvk-zhlvte/source.cl:1364:1: warning: cast from '__global uchar *' (aka '__global unsigned char *') to '__global uint4 *' increases required alignment from 1 to 16
 1364 | SCRATCHPAD_CHUNK(1)=as_uint4(chunk3+bx1);
      | ^~~~~~~~~~~~~~~~~~~
clvk-zhlvte/source.cl:1333:31: note: expanded from macro 'SCRATCHPAD_CHUNK'
 1333 | #define SCRATCHPAD_CHUNK(N) (*(__global uint4*)((__global uchar*)(Scratchpad) + (idx ^ (N << 4))))
      |                               ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
clvk-zhlvte/source.cl:1365:1: warning: cast from '__global uchar *' (aka '__global unsigned char *') to '__global uint4 *' increases required alignment from 1 to 16
 1365 | SCRATCHPAD_CHUNK(2)=as_uint4(chunk1+bx0);
      | ^~~~~~~~~~~~~~~~~~~
clvk-zhlvte/source.cl:1333:31: note: expanded from macro 'SCRATCHPAD_CHUNK'
 1333 | #define SCRATCHPAD_CHUNK(N) (*(__global uint4*)((__global uchar*)(Scratchpad) + (idx ^ (N << 4))))
      |                               ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
clvk-zhlvte/source.cl:1366:1: warning: cast from '__global uchar *' (aka '__global unsigned char *') to '__global uint4 *' increases required alignment from 1 to 16
 1366 | SCRATCHPAD_CHUNK(3)=as_uint4(chunk2+((ulong2 *)a)[0]);
      | ^~~~~~~~~~~~~~~~~~~
clvk-zhlvte/source.cl:1333:31: note: expanded from macro 'SCRATCHPAD_CHUNK'
 1333 | #define SCRATCHPAD_CHUNK(N) (*(__global uint4*)((__global uchar*)(Scratchpad) + (idx ^ (N << 4))))
      |                               ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
clvk-zhlvte/source.cl:1366:38: warning: cast from '__private ulong *' (aka '__private unsigned long *') to '__private ulong2 *' increases required alignment from 8 to 16
 1366 | SCRATCHPAD_CHUNK(3)=as_uint4(chunk2+((ulong2 *)a)[0]);
      |                                      ^~~~~~~~~~~
include/opencl-c-base.h:608:39: note: expanded from macro 'as_uint4'
  608 | #define as_uint4(x) __builtin_astype((x), uint4)
      |                                       ^
clvk-zhlvte/source.cl:1368:1: warning: cast from '__global uchar *' (aka '__global unsigned char *') to '__global uint4 *' increases required alignment from 1 to 16
 1368 | SCRATCHPAD_CHUNK(0)=as_uint4(bx0)^c;
      | ^~~~~~~~~~~~~~~~~~~
clvk-zhlvte/source.cl:1333:31: note: expanded from macro 'SCRATCHPAD_CHUNK'
 1333 | #define SCRATCHPAD_CHUNK(N) (*(__global uint4*)((__global uchar*)(Scratchpad) + (idx ^ (N << 4))))
      |                               ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
clvk-zhlvte/source.cl:1377:11: warning: cast from '__global uchar *' (aka '__global unsigned char *') to '__global uint4 *' increases required alignment from 1 to 16
 1377 | uint4 tmp=SCRATCHPAD_CHUNK(0);
      |           ^~~~~~~~~~~~~~~~~~~
clvk-zhlvte/source.cl:1333:31: note: expanded from macro 'SCRATCHPAD_CHUNK'
 1333 | #define SCRATCHPAD_CHUNK(N) (*(__global uint4*)((__global uchar*)(Scratchpad) + (idx ^ (N << 4))))
      |                               ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
clvk-zhlvte/source.cl:1388:31: warning: cast from '__global uchar *' (aka '__global unsigned char *') to '__global uint4 *' increases required alignment from 1 to 16
 1388 | const ulong2 chunk1=as_ulong2(SCRATCHPAD_CHUNK(1))^t;
      |                     ~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~
clvk-zhlvte/source.cl:1333:31: note: expanded from macro 'SCRATCHPAD_CHUNK'
 1333 | #define SCRATCHPAD_CHUNK(N) (*(__global uint4*)((__global uchar*)(Scratchpad) + (idx ^ (N << 4))))
      |                               ^
include/opencl-c-base.h:620:40: note: expanded from macro 'as_ulong2'
  620 | #define as_ulong2(x) __builtin_astype((x), ulong2)
      |                                        ^
clvk-zhlvte/source.cl:1389:31: warning: cast from '__global uchar *' (aka '__global unsigned char *') to '__global uint4 *' increases required alignment from 1 to 16
 1389 | const ulong2 chunk2=as_ulong2(SCRATCHPAD_CHUNK(2));
      |                     ~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~
clvk-zhlvte/source.cl:1333:31: note: expanded from macro 'SCRATCHPAD_CHUNK'
 1333 | #define SCRATCHPAD_CHUNK(N) (*(__global uint4*)((__global uchar*)(Scratchpad) + (idx ^ (N << 4))))
      |                               ^
include/opencl-c-base.h:620:40: note: expanded from macro 'as_ulong2'
  620 | #define as_ulong2(x) __builtin_astype((x), ulong2)
      |                                        ^
clvk-zhlvte/source.cl:1391:31: warning: cast from '__global uchar *' (aka '__global unsigned char *') to '__global uint4 *' increases required alignment from 1 to 16
 1391 | const ulong2 chunk3=as_ulong2(SCRATCHPAD_CHUNK(3));
      |                     ~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~
clvk-zhlvte/source.cl:1333:31: note: expanded from macro 'SCRATCHPAD_CHUNK'
 1333 | #define SCRATCHPAD_CHUNK(N) (*(__global uint4*)((__global uchar*)(Scratchpad) + (idx ^ (N << 4))))
      |                               ^
include/opencl-c-base.h:620:40: note: expanded from macro 'as_ulong2'
  620 | #define as_ulong2(x) __builtin_astype((x), ulong2)
      |                                        ^
clvk-zhlvte/source.cl:1397:1: warning: cast from '__global uchar *' (aka '__global unsigned char *') to '__global uint4 *' increases required alignment from 1 to 16
 1397 | SCRATCHPAD_CHUNK(1)=as_uint4(chunk3+bx1);
      | ^~~~~~~~~~~~~~~~~~~
clvk-zhlvte/source.cl:1333:31: note: expanded from macro 'SCRATCHPAD_CHUNK'
 1333 | #define SCRATCHPAD_CHUNK(N) (*(__global uint4*)((__global uchar*)(Scratchpad) + (idx ^ (N << 4))))
      |                               ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
clvk-zhlvte/source.cl:1398:1: warning: cast from '__global uchar *' (aka '__global unsigned char *') to '__global uint4 *' increases required alignment from 1 to 16
 1398 | SCRATCHPAD_CHUNK(2)=as_uint4(chunk1+bx0);
      | ^~~~~~~~~~~~~~~~~~~
clvk-zhlvte/source.cl:1333:31: note: expanded from macro 'SCRATCHPAD_CHUNK'
 1333 | #define SCRATCHPAD_CHUNK(N) (*(__global uint4*)((__global uchar*)(Scratchpad) + (idx ^ (N << 4))))
      |                               ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
clvk-zhlvte/source.cl:1399:1: warning: cast from '__global uchar *' (aka '__global unsigned char *') to '__global uint4 *' increases required alignment from 1 to 16
 1399 | SCRATCHPAD_CHUNK(3)=as_uint4(chunk2+((ulong2 *)a)[0]);
      | ^~~~~~~~~~~~~~~~~~~
clvk-zhlvte/source.cl:1333:31: note: expanded from macro 'SCRATCHPAD_CHUNK'
 1333 | #define SCRATCHPAD_CHUNK(N) (*(__global uint4*)((__global uchar*)(Scratchpad) + (idx ^ (N << 4))))
      |                               ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
clvk-zhlvte/source.cl:1399:38: warning: cast from '__private ulong *' (aka '__private unsigned long *') to '__private ulong2 *' increases required alignment from 8 to 16
 1399 | SCRATCHPAD_CHUNK(3)=as_uint4(chunk2+((ulong2 *)a)[0]);
      |                                      ^~~~~~~~~~~
include/opencl-c-base.h:608:39: note: expanded from macro 'as_uint4'
  608 | #define as_uint4(x) __builtin_astype((x), uint4)
      |                                       ^
clvk-zhlvte/source.cl:1391:14: warning: mixing declarations and code is incompatible with standards before C99
 1391 | const ulong2 chunk3=as_ulong2(SCRATCHPAD_CHUNK(3));
      |              ^
clvk-zhlvte/source.cl:1404:1: warning: cast from '__global uchar *' (aka '__global unsigned char *') to '__global uint4 *' increases required alignment from 1 to 16
 1404 | SCRATCHPAD_CHUNK(0)=((uint4 *)a)[0];
      | ^~~~~~~~~~~~~~~~~~~
clvk-zhlvte/source.cl:1333:31: note: expanded from macro 'SCRATCHPAD_CHUNK'
 1333 | #define SCRATCHPAD_CHUNK(N) (*(__global uint4*)((__global uchar*)(Scratchpad) + (idx ^ (N << 4))))
      |                               ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
clvk-zhlvte/source.cl:1404:22: warning: cast from '__private ulong *' (aka '__private unsigned long *') to '__private uint4 *' increases required alignment from 8 to 16
 1404 | SCRATCHPAD_CHUNK(0)=((uint4 *)a)[0];
      |                      ^~~~~~~~~~
clvk-zhlvte/source.cl:1408:2: warning: cast from '__private ulong *' (aka '__private unsigned long *') to '__private uint4 *' increases required alignment from 8 to 16
 1408 | ((uint4 *)a)[0] ^= tmp;
      |  ^~~~~~~~~~
clvk-zhlvte/source.cl:1377:7: warning: mixing declarations and code is incompatible with standards before C99
 1377 | uint4 tmp=SCRATCHPAD_CHUNK(0);
      |       ^
clvk-zhlvte/source.cl:1324:8: warning: mixing declarations and code is incompatible with standards before C99
 1324 | ulong2 bx0=((ulong2 *)b)[0];
      |        ^
clvk-zhlvte/source.cl:1290:35: warning: unused parameter 'input'
 1290 | __kernel void cn1(__global ulong *input,__global uint4 *Scratchpad,__global ulong *states,uint Threads)
      |                                   ^
clvk-zhlvte/source.cl:1290:96: warning: unused parameter 'Threads'
 1290 | __kernel void cn1(__global ulong *input,__global uint4 *Scratchpad,__global ulong *states,uint Threads)
      |                                                                                                ^
clvk-zhlvte/source.cl:1344:16: warning: comparison of integers of different signs: '__private int' and 'unsigned int'
 1344 | for (int i=0; i<ITERATIONS; ++i) {
      |               ~^~~~~~~~~~~
clvk-zhlvte/source.cl:1424:29: warning: implicit conversion changes signedness: 'unsigned int' to 'int'
 1424 | for (int i=get_local_id(1)*8+get_local_id(0); i<256; i+=8*8) {
      |          ~ ~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~
clvk-zhlvte/source.cl:1450:2: warning: cast from '__private uint *' (aka '__private unsigned int *') to '__private uint8 *' increases required alignment from 4 to 32
 1450 | ((uint8 *)ExpandedKey2)[0]=vload8(1,(__global uint *)states);
      |  ^~~~~~~~~~~~~~~~~~~~~
clvk-zhlvte/source.cl:1493:42: warning: cast from '__private uint *' (aka '__private unsigned int *') to '__private uint4 *' increases required alignment from 4 to 16
 1493 | text=AES_Round(AES0,AES1,AES2,AES3,text,((uint4 *)ExpandedKey2)[j]);
      |                                          ^~~~~~~~~~~~~~~~~~~~~
clvk-zhlvte/source.cl:1523:6: warning: mixing declarations and code is incompatible with standards before C99
 1523 | uint StateSwitch=State[0]&3;
      |      ^
clvk-zhlvte/source.cl:1515:15: warning: mixing declarations and code is incompatible with standards before C99
 1515 | __local ulong State_buf[8*25];
      |               ^
clvk-zhlvte/source.cl:1527:58: warning: implicit conversion loses integer precision: 'const __private ulong' (aka 'const __private unsigned long') to 'uint' (aka 'unsigned int')
 1527 | destinationBranch[atomic_inc(destinationBranch+Threads)]=gIdx;
      |                                                         ~^~~~
clvk-zhlvte/source.cl:1550:13: warning: mixing declarations and code is incompatible with standards before C99
 1550 | const ulong h8=h.s0^h.s1^h.s2^h.s3^h.s4^h.s5^h.s6^h.s7^SKEIN_KS_PARITY;
      |             ^
clvk-zhlvte/source.cl:1541:8: warning: mixing declarations and code is incompatible with standards before C99
 1541 | ulong8 h=vload8(0,SKEIN512_256_IV);
      |        ^
clvk-zhlvte/source.cl:1538:16: warning: implicit conversion loses integer precision: 'ulong' (aka 'unsigned long') to 'uint' (aka 'unsigned int')
 1538 | const uint idx=getIdx();
      |            ~~~ ^~~~~~~~
clvk-zhlvte/source.cl:1601:20: warning: implicit conversion changes signedness: 'uint' (aka 'unsigned int') to 'int'
 1601 | const int shifted=i<<3;
      |           ~~~~~~~ ~^~~
clvk-zhlvte/source.cl:1603:18: warning: implicit conversion changes signedness: 'const __private int' to 'uint' (aka 'unsigned int')
 1603 | input[x]=(states[shifted+x]);
      |                  ^~~~~~~~
clvk-zhlvte/source.cl:1596:9: warning: mixing declarations and code is incompatible with standards before C99
 1596 | sph_u64 h0h=0xEBD3202C41A398EBUL,h0l=0xC145B29C7BBECD92UL,h1h=0xFAC7D4609151931CUL,h1l=0x038A507ED6820026UL,h2h=0x45B92677269E23A4UL,h2l=0x77941AD4481AFBE0UL,h3h=0x7A176B0226ABB5CDUL,h3l=0xA82FFF0F4224F056UL;
      |         ^
clvk-zhlvte/source.cl:1593:16: warning: implicit conversion loses integer precision: 'ulong' (aka 'unsigned long') to 'uint' (aka 'unsigned int')
 1593 | const uint idx=getIdx();
      |            ~~~ ^~~~~~~~
clvk-zhlvte/source.cl:1633:2: warning: cast from '__private uint *' (aka '__private unsigned int *') to '__private uint8 *' increases required alignment from 4 to 32
 1633 | ((uint8 *)h)[0]=vload8(0U,c_IV256);
      |  ^~~~~~~~~~
clvk-zhlvte/source.cl:1635:2: warning: cast from '__private unsigned int *' to '__private uint16 *' increases required alignment from 4 to 64
 1635 | ((uint16 *)m)[0]=vload16(i,(__global uint *)states);
      |  ^~~~~~~~~~~
clvk-zhlvte/source.cl:1640:2: warning: cast from '__private unsigned int *' to '__private uint16 *' increases required alignment from 4 to 64
 1640 | ((uint16 *)v)[0].lo=((uint8 *)h)[0];
      |  ^~~~~~~~~~~
clvk-zhlvte/source.cl:1640:22: warning: cast from '__private uint *' (aka '__private unsigned int *') to '__private uint8 *' increases required alignment from 4 to 32
 1640 | ((uint16 *)v)[0].lo=((uint8 *)h)[0];
      |                      ^~~~~~~~~~
clvk-zhlvte/source.cl:1641:2: warning: cast from '__private unsigned int *' to '__private uint16 *' increases required alignment from 4 to 64
 1641 | ((uint16 *)v)[0].hi=vload8(0U,c_u256);
      |  ^~~~~~~~~~~
clvk-zhlvte/source.cl:1645:1: warning: implicit conversion changes signedness: 'const __constant int' to 'sph_u32' (aka 'unsigned int')
 1645 | GS(0,4,0x8,0xC,0x0);
      | ^~~~~~~~~~~~~~~~~~~
clvk-zhlvte/source.cl:546:20: note: expanded from macro 'GS'
  546 | const sph_u32 idx1=sigma[r][x]; \
      |               ~~~~ ^~~~~~~~~~~
clvk-zhlvte/source.cl:1645:1: warning: implicit conversion changes signedness: 'const __constant int' to 'sph_u32' (aka 'unsigned int')
 1645 | GS(0,4,0x8,0xC,0x0);
      | ^~~~~~~~~~~~~~~~~~~
clvk-zhlvte/source.cl:547:20: note: expanded from macro 'GS'
  547 | const sph_u32 idx2=sigma[r][x+1]; \
      |               ~~~~ ^~~~~~~~~~~~~
clvk-zhlvte/source.cl:1645:20: warning: empty expression statement has no effect; remove unnecessary ';' to silence this warning
 1645 | GS(0,4,0x8,0xC,0x0);
      |                    ^
clvk-zhlvte/source.cl:1646:1: warning: implicit conversion changes signedness: 'const __constant int' to 'sph_u32' (aka 'unsigned int')
 1646 | GS(1,5,0x9,0xD,0x2);
      | ^~~~~~~~~~~~~~~~~~~
clvk-zhlvte/source.cl:546:20: note: expanded from macro 'GS'
  546 | const sph_u32 idx1=sigma[r][x]; \
      |               ~~~~ ^~~~~~~~~~~
clvk-zhlvte/source.cl:1646:1: warning: implicit conversion changes signedness: 'const __constant int' to 'sph_u32' (aka 'unsigned int')
 1646 | GS(1,5,0x9,0xD,0x2);
      | ^~~~~~~~~~~~~~~~~~~
clvk-zhlvte/source.cl:547:20: note: expanded from macro 'GS'
  547 | const sph_u32 idx2=sigma[r][x+1]; \
      |               ~~~~ ^~~~~~~~~~~~~
clvk-zhlvte/source.cl:1646:20: warning: empty expression statement has no effect; remove unnecessary ';' to silence this warning
 1646 | GS(1,5,0x9,0xD,0x2);
      |                    ^
clvk-zhlvte/source.cl:1647:1: warning: implicit conversion changes signedness: 'const __constant int' to 'sph_u32' (aka 'unsigned int')
 1647 | GS(2,6,0xA,0xE,0x4);
      | ^~~~~~~~~~~~~~~~~~~
clvk-zhlvte/source.cl:546:20: note: expanded from macro 'GS'
  546 | const sph_u32 idx1=sigma[r][x]; \
      |               ~~~~ ^~~~~~~~~~~
clvk-zhlvte/source.cl:1647:1: warning: implicit conversion changes signedness: 'const __constant int' to 'sph_u32' (aka 'unsigned int')
 1647 | GS(2,6,0xA,0xE,0x4);
      | ^~~~~~~~~~~~~~~~~~~
clvk-zhlvte/source.cl:547:20: note: expanded from macro 'GS'
  547 | const sph_u32 idx2=sigma[r][x+1]; \
      |               ~~~~ ^~~~~~~~~~~~~
clvk-zhlvte/source.cl:1647:20: warning: empty expression statement has no effect; remove unnecessary ';' to silence this warning
 1647 | GS(2,6,0xA,0xE,0x4);
      |                    ^
clvk-zhlvte/source.cl:1648:1: warning: implicit conversion changes signedness: 'const __constant int' to 'sph_u32' (aka 'unsigned int')
 1648 | GS(3,7,0xB,0xF,0x6);
      | ^~~~~~~~~~~~~~~~~~~
clvk-zhlvte/source.cl:546:20: note: expanded from macro 'GS'
  546 | const sph_u32 idx1=sigma[r][x]; \
      |               ~~~~ ^~~~~~~~~~~
clvk-zhlvte/source.cl:1648:1: warning: implicit conversion changes signedness: 'const __constant int' to 'sph_u32' (aka 'unsigned int')
 1648 | GS(3,7,0xB,0xF,0x6);
      | ^~~~~~~~~~~~~~~~~~~
clvk-zhlvte/source.cl:547:20: note: expanded from macro 'GS'
  547 | const sph_u32 idx2=sigma[r][x+1]; \
      |               ~~~~ ^~~~~~~~~~~~~
clvk-zhlvte/source.cl:1648:20: warning: empty expression statement has no effect; remove unnecessary ';' to silence this warning
 1648 | GS(3,7,0xB,0xF,0x6);
      |                    ^
clvk-zhlvte/source.cl:1649:1: warning: implicit conversion changes signedness: 'const __constant int' to 'sph_u32' (aka 'unsigned int')
 1649 | GS(0,5,0xA,0xF,0x8);
      | ^~~~~~~~~~~~~~~~~~~
clvk-zhlvte/source.cl:546:20: note: expanded from macro 'GS'
  546 | const sph_u32 idx1=sigma[r][x]; \
      |               ~~~~ ^~~~~~~~~~~
clvk-zhlvte/source.cl:1649:1: warning: implicit conversion changes signedness: 'const __constant int' to 'sph_u32' (aka 'unsigned int')
 1649 | GS(0,5,0xA,0xF,0x8);
      | ^~~~~~~~~~~~~~~~~~~
clvk-zhlvte/source.cl:547:20: note: expanded from macro 'GS'
  547 | const sph_u32 idx2=sigma[r][x+1]; \
      |               ~~~~ ^~~~~~~~~~~~~
clvk-zhlvte/source.cl:1649:20: warning: empty expression statement has no effect; remove unnecessary ';' to silence this warning
 1649 | GS(0,5,0xA,0xF,0x8);
      |                    ^
clvk-zhlvte/source.cl:1650:1: warning: implicit conversion changes signedness: 'const __constant int' to 'sph_u32' (aka 'unsigned int')
 1650 | GS(1,6,0xB,0xC,0xA);
      | ^~~~~~~~~~~~~~~~~~~
clvk-zhlvte/source.cl:546:20: note: expanded from macro 'GS'
  546 | const sph_u32 idx1=sigma[r][x]; \
      |               ~~~~ ^~~~~~~~~~~
clvk-zhlvte/source.cl:1650:1: warning: implicit conversion changes signedness: 'const __constant int' to 'sph_u32' (aka 'unsigned int')
 1650 | GS(1,6,0xB,0xC,0xA);
      | ^~~~~~~~~~~~~~~~~~~
clvk-zhlvte/source.cl:547:20: note: expanded from macro 'GS'
  547 | const sph_u32 idx2=sigma[r][x+1]; \
      |               ~~~~ ^~~~~~~~~~~~~
clvk-zhlvte/source.cl:1650:20: warning: empty expression statement has no effect; remove unnecessary ';' to silence this warning
 1650 | GS(1,6,0xB,0xC,0xA);
      |                    ^
clvk-zhlvte/source.cl:1651:1: warning: implicit conversion changes signedness: 'const __constant int' to 'sph_u32' (aka 'unsigned int')
 1651 | GS(2,7,0x8,0xD,0xC);
      | ^~~~~~~~~~~~~~~~~~~
clvk-zhlvte/source.cl:546:20: note: expanded from macro 'GS'
  546 | const sph_u32 idx1=sigma[r][x]; \
      |               ~~~~ ^~~~~~~~~~~
clvk-zhlvte/source.cl:1651:1: warning: implicit conversion changes signedness: 'const __constant int' to 'sph_u32' (aka 'unsigned int')
 1651 | GS(2,7,0x8,0xD,0xC);
      | ^~~~~~~~~~~~~~~~~~~
clvk-zhlvte/source.cl:547:20: note: expanded from macro 'GS'
  547 | const sph_u32 idx2=sigma[r][x+1]; \
      |               ~~~~ ^~~~~~~~~~~~~
clvk-zhlvte/source.cl:1651:20: warning: empty expression statement has no effect; remove unnecessary ';' to silence this warning
 1651 | GS(2,7,0x8,0xD,0xC);
      |                    ^
clvk-zhlvte/source.cl:1652:1: warning: implicit conversion changes signedness: 'const __constant int' to 'sph_u32' (aka 'unsigned int')
 1652 | GS(3,4,0x9,0xE,0xE);
      | ^~~~~~~~~~~~~~~~~~~
clvk-zhlvte/source.cl:546:20: note: expanded from macro 'GS'
  546 | const sph_u32 idx1=sigma[r][x]; \
      |               ~~~~ ^~~~~~~~~~~
clvk-zhlvte/source.cl:1652:1: warning: implicit conversion changes signedness: 'const __constant int' to 'sph_u32' (aka 'unsigned int')
 1652 | GS(3,4,0x9,0xE,0xE);
      | ^~~~~~~~~~~~~~~~~~~
clvk-zhlvte/source.cl:547:20: note: expanded from macro 'GS'
  547 | const sph_u32 idx2=sigma[r][x+1]; \
      |               ~~~~ ^~~~~~~~~~~~~
clvk-zhlvte/source.cl:1652:20: warning: empty expression statement has no effect; remove unnecessary ';' to silence this warning
 1652 | GS(3,4,0x9,0xE,0xE);
      |                    ^
clvk-zhlvte/source.cl:1654:2: warning: cast from '__private uint *' (aka '__private unsigned int *') to '__private uint8 *' increases required alignment from 4 to 32
 1654 | ((uint8 *)h)[0] ^= ((uint8 *)v)[0]^((uint8 *)v)[1];
      |  ^~~~~~~~~~
clvk-zhlvte/source.cl:1654:21: warning: cast from '__private unsigned int *' to '__private uint8 *' increases required alignment from 4 to 32
 1654 | ((uint8 *)h)[0] ^= ((uint8 *)v)[0]^((uint8 *)v)[1];
      |                     ^~~~~~~~~~
clvk-zhlvte/source.cl:1654:37: warning: cast from '__private unsigned int *' to '__private uint8 *' increases required alignment from 4 to 32
 1654 | ((uint8 *)h)[0] ^= ((uint8 *)v)[0]^((uint8 *)v)[1];
      |                                     ^~~~~~~~~~
clvk-zhlvte/source.cl:1673:2: warning: cast from '__private unsigned int *' to '__private uint16 *' increases required alignment from 4 to 64
 1673 | ((uint16 *)v)[0].lo=((uint8 *)h)[0];
      |  ^~~~~~~~~~~
clvk-zhlvte/source.cl:1673:22: warning: cast from '__private uint *' (aka '__private unsigned int *') to '__private uint8 *' increases required alignment from 4 to 32
 1673 | ((uint16 *)v)[0].lo=((uint8 *)h)[0];
      |                      ^~~~~~~~~~
clvk-zhlvte/source.cl:1674:2: warning: cast from '__private unsigned int *' to '__private uint16 *' increases required alignment from 4 to 64
 1674 | ((uint16 *)v)[0].hi=vload8(0U,c_u256);
      |  ^~~~~~~~~~~
clvk-zhlvte/source.cl:1678:1: warning: implicit conversion changes signedness: 'const __constant int' to 'sph_u32' (aka 'unsigned int')
 1678 | GS(0,4,0x8,0xC,0x0);
      | ^~~~~~~~~~~~~~~~~~~
clvk-zhlvte/source.cl:546:20: note: expanded from macro 'GS'
  546 | const sph_u32 idx1=sigma[r][x]; \
      |               ~~~~ ^~~~~~~~~~~
clvk-zhlvte/source.cl:1678:1: warning: implicit conversion changes signedness: 'const __constant int' to 'sph_u32' (aka 'unsigned int')
 1678 | GS(0,4,0x8,0xC,0x0);
      | ^~~~~~~~~~~~~~~~~~~
clvk-zhlvte/source.cl:547:20: note: expanded from macro 'GS'
  547 | const sph_u32 idx2=sigma[r][x+1]; \
      |               ~~~~ ^~~~~~~~~~~~~
clvk-zhlvte/source.cl:1678:20: warning: empty expression statement has no effect; remove unnecessary ';' to silence this warning
 1678 | GS(0,4,0x8,0xC,0x0);
      |                    ^
clvk-zhlvte/source.cl:1679:1: warning: implicit conversion changes signedness: 'const __constant int' to 'sph_u32' (aka 'unsigned int')
 1679 | GS(1,5,0x9,0xD,0x2);
      | ^~~~~~~~~~~~~~~~~~~
clvk-zhlvte/source.cl:546:20: note: expanded from macro 'GS'
  546 | const sph_u32 idx1=sigma[r][x]; \
      |               ~~~~ ^~~~~~~~~~~
clvk-zhlvte/source.cl:1679:1: warning: implicit conversion changes signedness: 'const __constant int' to 'sph_u32' (aka 'unsigned int')
 1679 | GS(1,5,0x9,0xD,0x2);
      | ^~~~~~~~~~~~~~~~~~~
clvk-zhlvte/source.cl:547:20: note: expanded from macro 'GS'
  547 | const sph_u32 idx2=sigma[r][x+1]; \
      |               ~~~~ ^~~~~~~~~~~~~
clvk-zhlvte/source.cl:1679:20: warning: empty expression statement has no effect; remove unnecessary ';' to silence this warning
 1679 | GS(1,5,0x9,0xD,0x2);
      |                    ^
clvk-zhlvte/source.cl:1680:1: warning: implicit conversion changes signedness: 'const __constant int' to 'sph_u32' (aka 'unsigned int')
 1680 | GS(2,6,0xA,0xE,0x4);
      | ^~~~~~~~~~~~~~~~~~~
clvk-zhlvte/source.cl:546:20: note: expanded from macro 'GS'
  546 | const sph_u32 idx1=sigma[r][x]; \
      |               ~~~~ ^~~~~~~~~~~
clvk-zhlvte/source.cl:1680:1: warning: implicit conversion changes signedness: 'const __constant int' to 'sph_u32' (aka 'unsigned int')
 1680 | GS(2,6,0xA,0xE,0x4);
      | ^~~~~~~~~~~~~~~~~~~
clvk-zhlvte/source.cl:547:20: note: expanded from macro 'GS'
  547 | const sph_u32 idx2=sigma[r][x+1]; \
      |               ~~~~ ^~~~~~~~~~~~~
clvk-zhlvte/source.cl:1680:20: warning: empty expression statement has no effect; remove unnecessary ';' to silence this warning
 1680 | GS(2,6,0xA,0xE,0x4);
      |                    ^
clvk-zhlvte/source.cl:1681:1: warning: implicit conversion changes signedness: 'const __constant int' to 'sph_u32' (aka 'unsigned int')
 1681 | GS(3,7,0xB,0xF,0x6);
      | ^~~~~~~~~~~~~~~~~~~
clvk-zhlvte/source.cl:546:20: note: expanded from macro 'GS'
  546 | const sph_u32 idx1=sigma[r][x]; \
      |               ~~~~ ^~~~~~~~~~~
clvk-zhlvte/source.cl:1681:1: warning: implicit conversion changes signedness: 'const __constant int' to 'sph_u32' (aka 'unsigned int')
 1681 | GS(3,7,0xB,0xF,0x6);
      | ^~~~~~~~~~~~~~~~~~~
clvk-zhlvte/source.cl:547:20: note: expanded from macro 'GS'
  547 | const sph_u32 idx2=sigma[r][x+1]; \
      |               ~~~~ ^~~~~~~~~~~~~
clvk-zhlvte/source.cl:1681:20: warning: empty expression statement has no effect; remove unnecessary ';' to silence this warning
 1681 | GS(3,7,0xB,0xF,0x6);
      |                    ^
clvk-zhlvte/source.cl:1682:1: warning: implicit conversion changes signedness: 'const __constant int' to 'sph_u32' (aka 'unsigned int')
 1682 | GS(0,5,0xA,0xF,0x8);
      | ^~~~~~~~~~~~~~~~~~~
clvk-zhlvte/source.cl:546:20: note: expanded from macro 'GS'
  546 | const sph_u32 idx1=sigma[r][x]; \
      |               ~~~~ ^~~~~~~~~~~
clvk-zhlvte/source.cl:1682:1: warning: implicit conversion changes signedness: 'const __constant int' to 'sph_u32' (aka 'unsigned int')
 1682 | GS(0,5,0xA,0xF,0x8);
      | ^~~~~~~~~~~~~~~~~~~
clvk-zhlvte/source.cl:547:20: note: expanded from macro 'GS'
  547 | const sph_u32 idx2=sigma[r][x+1]; \
      |               ~~~~ ^~~~~~~~~~~~~
clvk-zhlvte/source.cl:1682:20: warning: empty expression statement has no effect; remove unnecessary ';' to silence this warning
 1682 | GS(0,5,0xA,0xF,0x8);
      |                    ^
clvk-zhlvte/source.cl:1683:1: warning: implicit conversion changes signedness: 'const __constant int' to 'sph_u32' (aka 'unsigned int')
 1683 | GS(1,6,0xB,0xC,0xA);
      | ^~~~~~~~~~~~~~~~~~~
clvk-zhlvte/source.cl:546:20: note: expanded from macro 'GS'
  546 | const sph_u32 idx1=sigma[r][x]; \
      |               ~~~~ ^~~~~~~~~~~
clvk-zhlvte/source.cl:1683:1: warning: implicit conversion changes signedness: 'const __constant int' to 'sph_u32' (aka 'unsigned int')
 1683 | GS(1,6,0xB,0xC,0xA);
      | ^~~~~~~~~~~~~~~~~~~
clvk-zhlvte/source.cl:547:20: note: expanded from macro 'GS'
  547 | const sph_u32 idx2=sigma[r][x+1]; \
      |               ~~~~ ^~~~~~~~~~~~~
clvk-zhlvte/source.cl:1683:20: warning: empty expression statement has no effect; remove unnecessary ';' to silence this warning
 1683 | GS(1,6,0xB,0xC,0xA);
      |                    ^
clvk-zhlvte/source.cl:1684:1: warning: implicit conversion changes signedness: 'const __constant int' to 'sph_u32' (aka 'unsigned int')
 1684 | GS(2,7,0x8,0xD,0xC);
      | ^~~~~~~~~~~~~~~~~~~
clvk-zhlvte/source.cl:546:20: note: expanded from macro 'GS'
  546 | const sph_u32 idx1=sigma[r][x]; \
      |               ~~~~ ^~~~~~~~~~~
clvk-zhlvte/source.cl:1684:1: warning: implicit conversion changes signedness: 'const __constant int' to 'sph_u32' (aka 'unsigned int')
 1684 | GS(2,7,0x8,0xD,0xC);
      | ^~~~~~~~~~~~~~~~~~~
clvk-zhlvte/source.cl:547:20: note: expanded from macro 'GS'
  547 | const sph_u32 idx2=sigma[r][x+1]; \
      |               ~~~~ ^~~~~~~~~~~~~
clvk-zhlvte/source.cl:1684:20: warning: empty expression statement has no effect; remove unnecessary ';' to silence this warning
 1684 | GS(2,7,0x8,0xD,0xC);
      |                    ^
clvk-zhlvte/source.cl:1685:1: warning: implicit conversion changes signedness: 'const __constant int' to 'sph_u32' (aka 'unsigned int')
 1685 | GS(3,4,0x9,0xE,0xE);
      | ^~~~~~~~~~~~~~~~~~~
clvk-zhlvte/source.cl:546:20: note: expanded from macro 'GS'
  546 | const sph_u32 idx1=sigma[r][x]; \
      |               ~~~~ ^~~~~~~~~~~
clvk-zhlvte/source.cl:1685:1: warning: implicit conversion changes signedness: 'const __constant int' to 'sph_u32' (aka 'unsigned int')
 1685 | GS(3,4,0x9,0xE,0xE);
      | ^~~~~~~~~~~~~~~~~~~
clvk-zhlvte/source.cl:547:20: note: expanded from macro 'GS'
  547 | const sph_u32 idx2=sigma[r][x+1]; \
      |               ~~~~ ^~~~~~~~~~~~~
clvk-zhlvte/source.cl:1685:20: warning: empty expression statement has no effect; remove unnecessary ';' to silence this warning
 1685 | GS(3,4,0x9,0xE,0xE);
      |                    ^
clvk-zhlvte/source.cl:1687:2: warning: cast from '__private uint *' (aka '__private unsigned int *') to '__private uint8 *' increases required alignment from 4 to 32
 1687 | ((uint8 *)h)[0] ^= ((uint8 *)v)[0]^((uint8 *)v)[1];
      |  ^~~~~~~~~~
clvk-zhlvte/source.cl:1687:21: warning: cast from '__private unsigned int *' to '__private uint8 *' increases required alignment from 4 to 32
 1687 | ((uint8 *)h)[0] ^= ((uint8 *)v)[0]^((uint8 *)v)[1];
      |                     ^~~~~~~~~~
clvk-zhlvte/source.cl:1687:37: warning: cast from '__private unsigned int *' to '__private uint8 *' increases required alignment from 4 to 32
 1687 | ((uint8 *)h)[0] ^= ((uint8 *)v)[0]^((uint8 *)v)[1];
      |                                     ^~~~~~~~~~
clvk-zhlvte/source.cl:1629:14: warning: mixing declarations and code is incompatible with standards before C99
 1629 | unsigned int m[16];
      |              ^
clvk-zhlvte/source.cl:1626:16: warning: implicit conversion loses integer precision: 'ulong' (aka 'unsigned long') to 'uint' (aka 'unsigned int')
 1626 | const uint idx=getIdx();
      |            ~~~ ^~~~~~~~
clvk-zhlvte/source.cl:1709:2: warning: cast from '__private ulong *' (aka '__private unsigned long *') to '__private ulong8 *' increases required alignment from 8 to 64
 1709 | ((ulong8 *)M)[0]=vload8(0,states);
      |  ^~~~~~~~~~~
clvk-zhlvte/source.cl:1720:2: warning: cast from '__private ulong *' (aka '__private unsigned long *') to '__private ulong8 *' increases required alignment from 8 to 64
 1720 | ((ulong8 *)M)[0]=vload8(1,states);
      |  ^~~~~~~~~~~
clvk-zhlvte/source.cl:1731:2: warning: cast from '__private ulong *' (aka '__private unsigned long *') to '__private ulong8 *' increases required alignment from 8 to 64
 1731 | ((ulong8 *)M)[0]=vload8(2,states);
      |  ^~~~~~~~~~~
clvk-zhlvte/source.cl:1706:7: warning: mixing declarations and code is incompatible with standards before C99
 1706 | ulong State[8]={ 0UL,0UL,0UL,0UL,0UL,0UL,0UL,0x0001000000000000UL };
      |       ^
clvk-zhlvte/source.cl:1008:9: warning: macro is not used
 1008 | #define mix_and_propagate(xin) (xin)[(get_local_id(1)) % 8][get_local_id(0)] ^ (xin)[(get_local_id(1) + 1) % 8][get_local_id(0)]
      |         ^
clvk-zhlvte/source.cl:313:9: warning: macro is not used
  313 | #define C32e(x) ((SPH_C32(x) >> 24) \
      |         ^
clvk-zhlvte/source.cl:868:9: warning: macro is not used
  868 | #define XMRIG_KECCAK_CL
      |         ^
clvk-zhlvte/source.cl:29:9: warning: macro is not used
   29 | #define ALGO_CN_PICO_0 0x63120200
      |         ^
clvk-zhlvte/source.cl:15:9: warning: macro is not used
   15 | #define ALGO_CN_R 0x63150272
      |         ^
clvk-zhlvte/source.cl:50:9: warning: macro is not used
   50 | #define FAMILY_KAWPOW 0x6b000000
      |         ^
clvk-zhlvte/source.cl:1535:9: warning: macro is not used
 1535 | #define VSWAP4(x) ((((x) >> 24) & 0xFFU) | (((x) >> 8) & 0xFF00U) | (((x) << 8) & 0xFF0000U) | (((x) << 24) & 0xFF000000U))
      |         ^
clvk-zhlvte/source.cl:754:9: warning: macro is not used
  754 | #define ROUND_SMALL_Pf(a,r) do { \
      |         ^
clvk-zhlvte/source.cl:43:9: warning: macro is not used
   43 | #define FAMILY_CN 0x63150000
      |         ^
clvk-zhlvte/source.cl:38:9: warning: macro is not used
   38 | #define ALGO_AR2_CHUKWA 0x61130000
      |         ^
clvk-zhlvte/source.cl:1570:9: warning: macro is not used
 1570 | #define SWAP8(x) as_ulong(as_uchar8(x).s76543210)
      |         ^
clvk-zhlvte/source.cl:26:9: warning: macro is not used
   26 | #define ALGO_CN_HEAVY_0 0x63160000
      |         ^
clvk-zhlvte/source.cl:40:9: warning: macro is not used
   40 | #define ALGO_AR2_WRKZ 0x61120000
      |         ^
clvk-zhlvte/source.cl:436:9: warning: macro is not used
  436 | #define SL(ro) SLu(r + ro, ro)
      |         ^
clvk-zhlvte/source.cl:39:9: warning: macro is not used
   39 | #define ALGO_AR2_CHUKWA_V2 0x61140000
      |         ^
clvk-zhlvte/source.cl:47:9: warning: macro is not used
   47 | #define FAMILY_CN_FEMTO 0x63110000
      |         ^
clvk-zhlvte/source.cl:28:9: warning: macro is not used
   28 | #define ALGO_CN_HEAVY_XHV 0x63160068
      |         ^
clvk-zhlvte/source.cl:36:9: warning: macro is not used
   36 | #define ALGO_RX_GRAFT 0x72151267
      |         ^
clvk-zhlvte/source.cl:52:9: warning: macro is not used
   52 | #define WOLF_AES_CL
      |         ^
clvk-zhlvte/source.cl:35:9: warning: macro is not used
   35 | #define ALGO_RX_SFX 0x72151273
      |         ^
clvk-zhlvte/source.cl:48:9: warning: macro is not used
   48 | #define FAMILY_RANDOM_X 0x72000000
      |         ^
clvk-zhlvte/source.cl:317:9: warning: macro is not used
  317 | #define dec32e_aligned sph_dec32le_aligned
      |         ^
clvk-zhlvte/source.cl:25:9: warning: macro is not used
   25 | #define ALGO_CN_LITE_1 0x63140100
      |         ^
clvk-zhlvte/source.cl:16:9: warning: macro is not used
   16 | #define ALGO_CN_FAST 0x63150166
      |         ^
clvk-zhlvte/source.cl:46:9: warning: macro is not used
   46 | #define FAMILY_CN_PICO 0x63120000
      |         ^
clvk-zhlvte/source.cl:308:9: warning: macro is not used
  308 | #define SPH_C32(x)      x
      |         ^
clvk-zhlvte/source.cl:328:9: warning: macro is not used
  328 | #define enc64e sph_enc64le
      |         ^
clvk-zhlvte/source.cl:32:9: warning: macro is not used
   32 | #define ALGO_RX_0 0x72151200
      |         ^
clvk-zhlvte/source.cl:44:9: warning: macro is not used
   44 | #define FAMILY_CN_LITE 0x63140000
      |         ^
clvk-zhlvte/source.cl:49:9: warning: macro is not used
   49 | #define FAMILY_ARGON2 0x61000000
      |         ^
clvk-zhlvte/source.cl:24:9: warning: macro is not used
   24 | #define ALGO_CN_LITE_0 0x63140000
      |         ^
clvk-zhlvte/source.cl:23:9: warning: macro is not used
   23 | #define ALGO_CN_CCX 0x63150063
      |         ^
clvk-zhlvte/source.cl:306:9: warning: macro is not used
  306 | #define SPH_JH_64 1
      |         ^
clvk-zhlvte/source.cl:797:9: warning: macro is not used
  797 | #define PERM_SMALL_Pf(a) do { \
      |         ^
clvk-zhlvte/source.cl:992:9: warning: macro is not used
  992 | #define MEM_CHUNK (1 << MEM_CHUNK_EXPONENT)
      |         ^
clvk-zhlvte/source.cl:17:9: warning: macro is not used
   17 | #define ALGO_CN_HALF 0x63150268
      |         ^
clvk-zhlvte/source.cl:564:9: warning: macro is not used
  564 | #define C64e(x) ((SPH_C64(x) >> 56) \
      |         ^
clvk-zhlvte/source.cl:846:9: warning: macro is not used
  846 | #define FAST_DIV_HEAVY_CL
      |         ^
clvk-zhlvte/source.cl:22:9: warning: macro is not used
   22 | #define ALGO_CN_DOUBLE 0x63150264
      |         ^
clvk-zhlvte/source.cl:41:9: warning: macro is not used
   41 | #define ALGO_KAWPOW_RVN 0x6b0f0000
      |         ^
clvk-zhlvte/source.cl:197:9: warning: macro is not used
  197 | #define WOLF_SKEIN_CL
      |         ^
clvk-zhlvte/source.cl:21:9: warning: macro is not used
   21 | #define ALGO_CN_ZLS 0x6315027a
      |         ^
clvk-zhlvte/source.cl:318:9: warning: macro is not used
  318 | #define enc32e sph_enc32le
      |         ^
clvk-zhlvte/source.cl:30:9: warning: macro is not used
   30 | #define ALGO_CN_PICO_TLO 0x63120274
      |         ^
clvk-zhlvte/source.cl:1532:9: warning: macro is not used
 1532 | #define VSWAP8(x) (((x) >> 56) | (((x) >> 40) & 0x000000000000FF00UL) | (((x) >> 24) & 0x0000000000FF0000UL) \
      |         ^
clvk-zhlvte/source.cl:34:9: warning: macro is not used
   34 | #define ALGO_RX_ARQMA 0x72121061
      |         ^
clvk-zhlvte/source.cl:37:9: warning: macro is not used
   37 | #define ALGO_RX_YADA 0x72151279
      |         ^
clvk-zhlvte/source.cl:42:9: warning: macro is not used
   42 | #define FAMILY_UNKNOWN 0
      |         ^
clvk-zhlvte/source.cl:19:9: warning: macro is not used
   19 | #define ALGO_CN_RTO 0x63150172
      |         ^
clvk-zhlvte/source.cl:33:9: warning: macro is not used
   33 | #define ALGO_RX_WOW 0x72141177
      |         ^
clvk-zhlvte/source.cl:18:9: warning: macro is not used
   18 | #define ALGO_CN_XAO 0x63150078
      |         ^
clvk-zhlvte/source.cl:327:9: warning: macro is not used
  327 | #define dec64e_aligned sph_dec64le_aligned
      |         ^
clvk-zhlvte/source.cl:1703:16: warning: implicit conversion loses integer precision: 'ulong' (aka 'unsigned long') to 'uint' (aka 'unsigned int')
 1703 | const uint idx=getIdx();
      |            ~~~ ^~~~~~~~

[2024-12-16 22:26:17.050]  opencl   thread #0 failed with error CL_INVALID_PROGRAM
[2024-12-16 22:26:17.050]  opencl   thread #0 self-test failed
[2024-12-16 22:26:17.050]  opencl   disabled (failed to start threads)
[2024-12-16 22:26:20.415]  signal   Ctrl+C received, exiting
[2024-12-16 22:26:20.415]  opencl   stopped (0 ms)
[root@cachyos xmrig-6.22.2]#
```

## akku1139 | 2024-12-16T13:28:45+00:00
`clinfo`

```
MESA-INTEL: warning: Haswell Vulkan support is incomplete
Number of platforms                               1
  Platform Name                                   clvk
  Platform Vendor                                 clvk
  Platform Version                                OpenCL 3.0 clvk
  Platform Profile                                FULL_PROFILE
  Platform Extensions                             cl_khr_icd cl_khr_extended_versioning
  Platform Extensions with Version                cl_khr_icd                                                       0x400000 (1.0.0)
                                                  cl_khr_extended_versioning                                       0x400000 (1.0.0)
  Platform Numeric Version                        0xc00000 (3.0.0)
  Platform Extensions function suffix             clvk
  Platform Host timer resolution                  1ns

  Platform Name                                   clvk
Number of devices                                 1
  Device Name                                     Intel(R) HD Graphics 4600 (HSW GT2)
  Device Vendor                                   Intel Corporation
  Device Vendor ID                                0x8086
  Device Version                                  OpenCL 3.0 CLVK on Vulkan v1.2.289 driver 100671495
  Device UUID                                     86801204-0600-0000-0002-000000000000
  Driver UUID                                     a6d97a6e-8475-f841-2824-99f9055a0456
  Valid Device LUID                               No
  Device LUID                                     0000-000000000000
  Device Node Mask                                0
  Device Numeric Version                          0xc00000 (3.0.0)
  Driver Version                                  3.0 CLVK on Vulkan v1.2.289 driver 100671495
  Device OpenCL C Version                         OpenCL C 1.2 CLVK on Vulkan v1.2.289 driver 100671495
  Device OpenCL C Numeric Version                 0x402000 (1.2.0)
  Device OpenCL C all versions                    OpenCL C                                                         0x400000 (1.0.0)
                                                  OpenCL C                                                         0x401000 (1.1.0)
                                                  OpenCL C                                                         0x402000 (1.2.0)
                                                  OpenCL C                                                         0xc00000 (3.0.0)
  Device OpenCL C features                        __opencl_c_images                                                0xc00000 (3.0.0)
                                                  __opencl_c_3d_image_writes                                       0xc00000 (3.0.0)
                                                  __opencl_c_atomic_order_acq_rel                                  0xc00000 (3.0.0)
                                                  __opencl_c_atomic_scope_device                                   0xc00000 (3.0.0)
  Latest conformance test passed                  v2023-12-12-00
  Device Type                                     GPU, Default
  Device PCI bus info (KHR)                       PCI-E, 0000:00:02.0
  Device Profile                                  FULL_PROFILE
  Device Available                                Yes
  Compiler Available                              Yes
  Linker Available                                Yes
  Max compute units                               1
  Max clock frequency                             0MHz
  Device Partition                                (core)
    Max number of sub-devices                     0
    Supported partition types                     None
    Supported affinity domains                    (n/a)
  Max work item dimensions                        3
  Max work item sizes                             1024x1024x1024
  Max work group size                             1024
  Preferred work group size multiple (device)     16
  Preferred work group size multiple (kernel)     16
  Max sub-groups per work group                   0
  Preferred / native vector sizes
    char                                                 1 / 1
    short                                                1 / 1
    int                                                  1 / 1
    long                                                 1 / 1
    half                                                 1 / 1        (n/a)
    float                                                1 / 1
    double                                               1 / 1        (n/a)
  Half-precision Floating-point support           (n/a)
  Single-precision Floating-point support         (core)
    Denormals                                     No
    Infinity and NANs                             Yes
    Round to nearest                              Yes
    Round to zero                                 No
    Round to infinity                             No
    IEEE754-2008 fused multiply-add               Yes
    Support is emulated in software               No
    Correctly-rounded divide and sqrt operations  No
  Double-precision Floating-point support         (n/a)
  Address bits                                    32, Little-Endian
  Global memory size                              1610612736 (1.5GiB)
  Error Correction support                        No
  Max memory allocation                           1610612736 (1.5GiB)
  Unified memory for Host and Device              Yes
  Shared Virtual Memory (SVM) capabilities        (core)
    Coarse-grained buffer sharing                 No
    Fine-grained buffer sharing                   No
    Fine-grained system sharing                   No
    Atomics                                       No
  Minimum alignment for any data type             128 bytes
  Alignment of base address                       1024 bits (128 bytes)
  Preferred alignment for atomics
    SVM                                           0 bytes
    Global                                        0 bytes
    Local                                         0 bytes
  Atomic memory capabilities                      relaxed, acquire/release, work-group scope, device scope
  Atomic fence capabilities                       relaxed, acquire/release, work-item scope, work-group scope, device scope
  Max size for global variable                    0
  Preferred total size of global vars             0
  Global Memory cache type                        None
  Image support                                   Yes
    Max number of samplers per kernel             20
    Max size for 1D images from buffer            134217728 pixels
    Max 1D or 2D image array size                 2048 images
    Base address alignment for 2D image buffers   0 bytes
    Pitch alignment for 2D image buffers          0 pixels
    Max 2D image size                             8192x8192 pixels
    Max 3D image size                             2048x2048x2048 pixels
    Max number of read image args                 128
    Max number of write image args                64
    Max number of read/write image args           0
  Pipe support                                    No
  Max number of pipe args                         0
  Max active pipe reservations                    0
  Max pipe packet size                            0
  Local memory type                               Local
  Local memory size                               65536 (64KiB)
  Max number of constant args                     8
  Max constant buffer size                        65536 (64KiB)
  Generic address space support                   No
  Max size of kernel argument                     1024
  Queue properties (on host)
    Out-of-order execution                        No
    Profiling                                     Yes
  Device enqueue capabilities                     (n/a)
  Queue properties (on device)
    Out-of-order execution                        No
    Profiling                                     No
    Preferred size                                0
    Max size                                      0
  Max queues on device                            0
  Max events on device                            0
  Prefer user sync for interop                    Yes
  Profiling timer resolution                      1ns
  Execution capabilities
    Run OpenCL kernels                            Yes
    Run native kernels                            No
    Non-uniform work-groups                       Yes
    Work-group collective functions               No
    Sub-group independent forward progress        No
    IL version                                    SPIR-V_1.0
    ILs with version                              SPIR-V                                                           0x400000 (1.0.0)
  printf() buffer size                            1048576 (1024KiB)
  Built-in kernels                                (n/a)
  Built-in kernels with version                   (n/a)
  Device Extensions                               cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics cl_khr_byte_addressable_store cl_khr_extended_versioning cl_khr_create_command_queue cl_khr_il_program cl_khr_spirv_no_integer_wrap_decoration cl_arm_non_uniform_work_group_size cl_arm_printf cl_khr_suggested_local_work_size cl_khr_3d_image_writes cl_khr_spirv_linkonce_odr cl_khr_device_uuid cl_khr_pci_bus_info
  Device Extensions with Version                  cl_khr_global_int32_base_atomics                                 0x400000 (1.0.0)
                                                  cl_khr_global_int32_extended_atomics                             0x400000 (1.0.0)
                                                  cl_khr_local_int32_base_atomics                                  0x400000 (1.0.0)
                                                  cl_khr_local_int32_extended_atomics                              0x400000 (1.0.0)
                                                  cl_khr_byte_addressable_store                                    0x400000 (1.0.0)
                                                  cl_khr_extended_versioning                                       0x400000 (1.0.0)
                                                  cl_khr_create_command_queue                                      0x400000 (1.0.0)
                                                  cl_khr_il_program                                                0x400000 (1.0.0)
                                                  cl_khr_spirv_no_integer_wrap_decoration                          0x400000 (1.0.0)
                                                  cl_arm_non_uniform_work_group_size                               0x400000 (1.0.0)
                                                  cl_arm_printf                                                    0x400000 (1.0.0)
                                                  cl_khr_suggested_local_work_size                                 0x400000 (1.0.0)
                                                  cl_khr_3d_image_writes                                           0x400000 (1.0.0)
                                                  cl_khr_spirv_linkonce_odr                                        0x400000 (1.0.0)
                                                  cl_khr_device_uuid                                               0x400000 (1.0.0)
                                                  cl_khr_pci_bus_info                                              0x400000 (1.0.0)

NULL platform behavior
  clGetPlatformInfo(NULL, CL_PLATFORM_NAME, ...)  clvk
  clGetDeviceIDs(NULL, CL_DEVICE_TYPE_ALL, ...)   Success [clvk]
  clCreateContext(NULL, ...) [default]            Success [clvk]
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_DEFAULT)  Success (1)
    Platform Name                                 clvk
    Device Name                                   Intel(R) HD Graphics 4600 (HSW GT2)
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_CPU)  No devices found in platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_GPU)  Success (1)
    Platform Name                                 clvk
    Device Name                                   Intel(R) HD Graphics 4600 (HSW GT2)
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_ACCELERATOR)  No devices found in platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_CUSTOM)  No devices found in platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_ALL)  Success (1)
    Platform Name                                 clvk
    Device Name                                   Intel(R) HD Graphics 4600 (HSW GT2)

ICD loader properties
  ICD loader Name                                 OpenCL ICD Loader
  ICD loader Vendor                               OCL Icd free software
  ICD loader Version                              2.3.2
  ICD loader Profile                              OpenCL 3.0
```

## SChernykh | 2024-12-16T16:50:28+00:00
```
error: use of undeclared identifier 'amd_bfe'
```
This error means that XMRig's OpenCL code detects support for `cl_amd_media_ops2` extension, and then expects that `amd_bfe` is available, but it is not. It's some problem with clvk.

In any case, running Cryptonight (or RandomX) on an integrated GPU will not give you more hashrate. It's better to run it just on CPU.

## gptlang | 2025-02-03T21:41:32+00:00
I'm getting the same issue on Fedora using a discrete AMD GPU.

## r14n | 2025-06-02T14:25:42+00:00
Similar issue on Pop_OS with an AMD eGPU

# Action History
- Created by: akku1139 | 2024-12-16T13:24:40+00:00
- Closed at: 2025-06-20T11:04:51+00:00
