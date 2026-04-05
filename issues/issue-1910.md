---
title: 'incompatible/disabled algorithm "argon2/chukwav2" detected, reconnect   '
source_url: https://github.com/xmrig/xmrig/issues/1910
author: CHINuit
assignees: []
labels: []
created_at: '2020-10-22T19:31:30+00:00'
updated_at: '2021-04-12T14:44:52+00:00'
type: issue
status: closed
closed_at: '2021-04-12T14:44:52+00:00'
---

# Original Description
**Describe the bug**
 * ABOUT        XMRig/6.4.0 MSVC/2019                                                                                    * LIBS         libuv/1.38.1 OpenSSL/1.1.1g hwloc/2.2.0                                                                  * HUGE PAGES   permission granted                                                                                       * 1GB PAGES    unavailable                                                                                              * CPU          Intel(R) Core(TM) i7-6700HQ CPU @ 2.60GHz (1) x64 AES                                                                   L2:1.0 MB L3:6.0 MB 4C/8T NUMA:1                                                                         * MEMORY       7.3/15.9 GB (46%)                                                                                        * DONATE       1%                                                                                                       * ASSEMBLY     auto:intel                                                                                               * POOL #1      trtl.pool.mine2gether.com:3335 algo argon2/chukwa                                                        * COMMANDS     hashrate, pause, resume, results, connection                                                             * OPENCL       disabled                                                                                                 * CUDA         10.2/11.0/6.4.0                                                                                          * NVML         11.445.75/445.75 press e for health report                                                               * CUDA GPU     #0 01:00.0 GeForce GTX 960M 1176/3145 MHz smx:5 arch:50 mem:3417/4096 MB                                [2020-10-22 22:28:24.510]  net      trtl.pool.mine2gether.com:3335 incompatible/disabled algorithm "argon2/chukwav2" detected, reconnect                                                                                                        [2020-10-22 22:28:24.511]  net      trtl.pool.mine2gether.com:3335 login error code: 6                                  [2020-10-22 22:28:30.402]  net      trtl.pool.mine2gether.com:3335 incompatible/disabled algorithm "argon2/chukwav2" detected, reconnect                                                                                                        [2020-10-22 22:28:30.402]  net      trtl.pool.mine2gether.com:3335 login error code: 6                                  [2020-10-22 22:28:36.647]  net      trtl.pool.mine2gether.com:3335 incompatible/disabled algorithm "argon2/chukwav2" detected, reconnect                                                                                                        [2020-10-22 22:28:36.652]  net      trtl.pool.mine2gether.com:3335 login error code: 6                                   

============================

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
        "argon2-impl": null,
        "astrobwt-max-size": 550,
        "astrobwt-avx2": false
    },
    "opencl": {
        "enabled": false,
        "cache": true,
        "loader": null,
        "platform": "AMD",
        "adl": true
    },
    "cuda": {
        "enabled": true,
        "loader": "C:/Users/CHINuit/Desktop/Miners/xmrig-6.4.0-msvc-cuda10_2-win64/xmrig-6.4.0/xmrig-cuda.dll",
        "nvml": true,
        "astrobwt": [
            {
                "index": 0,
                "threads": 32,
                "blocks": 11,
                "bfactor": 8,
                "bsleep": 25,
                "affinity": -1
            }
        ],
        "cn": [
            {
                "index": 0,
                "threads": 44,
                "blocks": 15,
                "bfactor": 8,
                "bsleep": 25,
                "affinity": -1
            }
        ],
        "cn-heavy": [
            {
                "index": 0,
                "threads": 22,
                "blocks": 15,
                "bfactor": 8,
                "bsleep": 25,
                "affinity": -1
            }
        ],
        "cn-lite": [
            {
                "index": 0,
                "threads": 88,
                "blocks": 15,
                "bfactor": 8,
                "bsleep": 25,
                "affinity": -1
            }
        ],
        "cn-pico": [
            {
                "index": 0,
                "threads": 4,
                "blocks": 40,
                "bfactor": 8,
                "bsleep": 25,
                "affinity": -1
            }
        ],
        "cn/2": [
            {
                "index": 0,
                "threads": 4,
                "blocks": 40,
                "bfactor": 8,
                "bsleep": 25,
                "affinity": -1
            }
        ],
        "kawpow": [
            {
                "index": 0,
                "threads": 256,
                "blocks": 10240,
                "bfactor": 8,
                "bsleep": 25,
                "affinity": -1
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
                "dataset_host": false
            }
        ],
        "cn/0": false,
        "cn-lite/0": false
    },
    "donate-level": 1,
    "donate-over-proxy": 1,
    "log-file": null,
    "pools": [
        {
            "algo": "argon2/chukwa",
            "coin": null,
            "url": "trtl.pool.mine2gether.com:3335",
            "user": "TRTLv36m1DWibrKD5828HpimUP6N4Qk659m2uMu5FhuycNqc2vZ6D5hQmGECLrmsLS1T2zPD7gcL94fNso6yvj9xPr5W5NDR8Dn.08ec300fc0b4b8a132656dd6d162ea46e69e375121c76bb83b31d805ba6ba7f1.480000",
            "pass": "x",
            "rig-id": null,
            "nicehash": false,
            "keepalive": true,
            "enabled": true,
            "tls": false,
            "tls-fingerprint": null,
            "daemon": false,
            "socks5": null,
            "self-select": null
        }
    ],
    "print-time": 45,
    "health-print-time": 45,
    "retries": 5,
    "retry-pause": 5,
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
    "pause-on-battery": false
}

# Discussion History
## CHINuit | 2020-10-22T19:33:47+00:00
if i activate mining on cpu , work only cpu

## SChernykh | 2020-10-23T07:36:10+00:00
Only CPU mining is supported for argon2/chukwav2.

# Action History
- Created by: CHINuit | 2020-10-22T19:31:30+00:00
- Closed at: 2021-04-12T14:44:52+00:00
