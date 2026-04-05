---
title: opencl with intel gpu???
source_url: https://github.com/xmrig/xmrig/issues/2473
author: venomega
assignees: []
labels: []
created_at: '2021-07-05T16:56:27+00:00'
updated_at: '2025-06-20T11:02:36+00:00'
type: issue
status: closed
closed_at: '2025-06-20T11:02:36+00:00'
---

# Original Description
**Describe the bug**
Greetings
i tried to use opencl features with intel but i`m getting this error (the opencl ones)
```
./xmrig  -o pool.com:5555 --opencl --opencl-platform=intel -O wallet_address:x
[2021-07-05 12:25:07.979] hwloc auto configuration for algorithm "cn-heavy/0" failed.
 * ABOUT        XMRig/6.13.1 gcc/11.1.0
 * LIBS         libuv/1.41.0 OpenSSL/1.1.1k hwloc/2.4.1
 * HUGE PAGES   supported
 * 1GB PAGES    disabled
 * CPU          Intel(R) Celeron(R) CPU N3350 @ 1.10GHz (1) 64-bit AES
                L2:2.0 MB L3:0.0 MB 2C/2T NUMA:1
 * MEMORY       1.6/1.8 GB (93%)
                DIMM_A0: 1 GB LPDDR4 @ 2133 MHz H9HCNNN8KUMLHR
                DIMM_B0: 1 GB LPDDR4 @ 2133 MHz H9HCNNN8KUMLHR
 * MOTHERBOARD  LENOVO - LNVNB161216
 * DONATE       1%
 * ASSEMBLY     auto:intel
 * POOL #1      pool.com:5555 algo auto
 * COMMANDS     hashrate, pause, resume, results, connection
 * ADL          disabled (failed to load ADL)
 * OPENCL       #0 Intel(R) OpenCL HD Graphics/OpenCL 3.0 
 * OPENCL GPU   #0 n/a Intel(R) HD Graphics 500 [0x5a85] 650 MHz cu:12 mem:723/1447 MB
 * CUDA         disabled
[2021-07-05 12:25:14.317]  net      use pool pool.com:5555  some_ipv4_address
[2021-07-05 12:25:14.317]  net      new job from pool.com:5555 diff 50000 algo rx/0 height 2398240
[2021-07-05 12:25:14.317]  cpu      use argon2 implementation SSSE3
[2021-07-05 12:25:14.384]  msr      cannot set MSR 0x000001a4 to 0x000000000000000f
[2021-07-05 12:25:14.384]  msr      FAILED TO APPLY MSR MOD, HASHRATE WILL BE LOW
[2021-07-05 12:25:14.385]  randomx  init dataset algo rx/0 (2 threads) seed 883985df67dda82e...
[2021-07-05 12:25:14.385]  randomx  not enough memory for RandomX dataset
[2021-07-05 12:25:14.392]  randomx  failed to allocate RandomX dataset, switching to slow mode (7 ms)
[2021-07-05 12:25:15.939]  randomx  dataset ready (1546 ms)
[2021-07-05 12:25:15.939]  cpu      use profile  rx  (2 threads) scratchpad 2048 KB
[2021-07-05 12:25:15.972]  opencl   use profile  rx  (1 thread) scratchpad 2048 KB
|  # | GPU |  BUS ID | INTENSITY | WSIZE | MEMORY | NAME
|  0 |   0 |     n/a |       192 |     8 |    384 | Intel(R) HD Graphics 500 [0x5a85]
[2021-07-05 12:25:15.974]  opencl   error CL_INVALID_HOST_PTR when calling clCreateBuffer with buffer size 2181038080
[2021-07-05 12:25:15.981]  cpu      READY threads 2/2 (2) huge pages 100% 2/2 memory 4096 KB (42 ms)
[2021-07-05 12:25:15.989]  opencl   thread #0 failed with error RandomX dataset is not available
[2021-07-05 12:25:15.993]  opencl   thread #0 self-test failed
[2021-07-05 12:25:15.993]  opencl   disabled (failed to start threads)
[2021-07-05 12:25:22.640]  signal   Ctrl+C received, exiting
[2021-07-05 12:25:22.686]  cpu      stopped (45 ms)
[2021-07-05 12:25:22.686]  opencl   stopped (0 ms)
```

This error i tested it too with an intel i3-4170 an output same error

I tryed https://github.com/xmrig/xmrig-amd and this doesn`t output any error but is hashing too slow
this is the output of 2.14.6 amd version
```
* ABOUT        XMRig-AMD/2.14.6 gcc/5.4.0
 * LIBS         libuv/1.31.0 OpenCL/2.0 OpenSSL/1.1.1c microhttpd/0.9.62 
 * CPU          Intel(R) Celeron(R) CPU N3350 @ 1.10GHz x64 AES
 * ALGO         cryptonight, donate=5%
 * POOL #1      donate.v2.xmrig.com:3333 variant auto
 * COMMANDS     hashrate, pause, resume
[2021-07-05 12:52:30] compiling code and initializing GPUs. This will take a while...
[2021-07-05 12:52:30] found Intel platform index: 0, name: Intel(R) Corporation
[2021-07-05 12:52:30] found OpenCL GPU: Intel(R) HD Graphics 500 [0x5a85], cu: 12
[2021-07-05 12:52:30] #00, GPU #00 Intel(R) HD Graphics 500 [0x5a85], i:96 (8/256), si:2/2, u:8, cu:12
[2021-07-05 12:52:30]              0.19/0.71/1 GB
[2021-07-05 12:52:30] GPU #0 compiling...
[2021-07-05 12:53:28] GPU #0 compilation completed, elapsed time 57.703s
[2021-07-05 12:53:28] configuration saved to: "/root/Downloads/x/xmrig-amd-2.14.6/config.json"
[2021-07-05 12:53:28] use pool donate.v2.xmrig.com:3333  178.128.242.134 
[2021-07-05 12:53:28] new job from donate.v2.xmrig.com:3333 diff 1000225 algo cn/r height 563841
```

and this is the config.json of that version

```
{
    "algo": "cryptonight",
    "api": {
        "port": 0,
        "access-token": null,
        "id": null,
        "worker-id": null,
        "ipv6": false,
        "restricted": true
    },
    "autosave": true,
    "background": false,
    "cache": true,
    "colors": true,
    "donate-level": 5,
    "log-file": null,
    "opencl-platform": "intel",  <--- this is the only thing i changed on default config.json
    "pools": [
        {
            "url": "donate.v2.xmrig.com:3333",
            "user": "YOUR_WALLET_ADDRESS",
            "pass": "x",
            "rig-id": null,
            "nicehash": false,
            "keepalive": false,
            "variant": -1,
            "enabled": true,
            "tls": false,
            "tls-fingerprint": null
        }
    ],
    "print-time": 60,
    "retries": 5,
    "retry-pause": 5,
    "threads": null,
    "user-agent": null,
    "syslog": false,
    "watch": true
}
```

# Discussion History
## Spudz76 | 2021-07-05T18:13:29+00:00
xmrig-amd doesn't support RandomX

xmrig is running RandomX which requires both 2080MB of system RAM (which you don't have) and VRAM (which you also don't have)

Set xmrig to use `cn/r` or others and it will work just like expired/deprecated/old/abandoned xmrig-amd does.  But not for mining RandomX (rx/0) which is what Monero has used since it hardforked from `cn/r` quite a while back.

## venomega | 2021-07-05T22:26:10+00:00
```
nice -n 19 ./xmrig --opencl --opencl-platform=intel  -o pool.com -O $(cat /addres.xmr):x  -a cn/r
[2021-07-05 18:24:31.866] hwloc auto configuration for algorithm "cn-heavy/0" failed.
 * ABOUT        XMRig/6.13.1 gcc/11.1.0
 * LIBS         libuv/1.41.0 OpenSSL/1.1.1k hwloc/2.4.1
 * HUGE PAGES   supported
 * 1GB PAGES    disabled
 * CPU          Intel(R) Celeron(R) CPU N3350 @ 1.10GHz (1) 64-bit AES
                L2:2.0 MB L3:0.0 MB 2C/2T NUMA:1
 * MEMORY       1.6/1.8 GB (93%)
                DIMM_A0: 1 GB LPDDR4 @ 2133 MHz H9HCNNN8KUMLHR
                DIMM_B0: 1 GB LPDDR4 @ 2133 MHz H9HCNNN8KUMLHR
 * MOTHERBOARD  LENOVO - LNVNB161216
 * DONATE       1%
 * ASSEMBLY     auto:intel
 * POOL #1      pool.com algo cn/r
 * COMMANDS     hashrate, pause, resume, results, connection
 * ADL          disabled (failed to load ADL)
 * OPENCL       #0 Intel(R) OpenCL HD Graphics/OpenCL 3.0 
 * OPENCL GPU   #0 n/a Intel(R) HD Graphics 500 [0x5a85] 650 MHz cu:12 mem:723/1447 MB
 * CUDA         disabled
[2021-07-05 18:24:32.585]  net      use pool pool.com:3333  some_ipv4_addr
[2021-07-05 18:24:32.586]  net      new job from pool.com:3333 diff 50000 algo rx/0 height 2398437
[2021-07-05 18:24:32.586]  cpu      use argon2 implementation SSSE3
[2021-07-05 18:24:32.587]  msr      cannot set MSR 0x000001a4 to 0x000000000000000f
[2021-07-05 18:24:32.588]  msr      FAILED TO APPLY MSR MOD, HASHRATE WILL BE LOW
[2021-07-05 18:24:32.588]  randomx  init dataset algo rx/0 (2 threads) seed acb8fba46cca7eaa...
[2021-07-05 18:24:32.589]  randomx  not enough memory for RandomX dataset
[2021-07-05 18:24:32.666]  randomx  failed to allocate RandomX dataset, switching to slow mode (76 ms)
[2021-07-05 18:24:33.799]  randomx  dataset ready (1133 ms)
[2021-07-05 18:24:33.800]  cpu      use profile  rx  (2 threads) scratchpad 2048 KB
[2021-07-05 18:24:33.800]  opencl   use profile  rx  (1 thread) scratchpad 2048 KB
|  # | GPU |  BUS ID | INTENSITY | WSIZE | MEMORY | NAME
|  0 |   0 |     n/a |       192 |     8 |    384 | Intel(R) HD Graphics 500 [0x5a85]
[2021-07-05 18:24:33.800]  opencl   error CL_INVALID_HOST_PTR when calling clCreateBuffer with buffer size 2181038080
[2021-07-05 18:24:33.801]  opencl   thread #0 failed with error RandomX dataset is not available
[2021-07-05 18:24:33.801]  opencl   thread #0 self-test failed
[2021-07-05 18:24:33.801]  opencl   disabled (failed to start threads)
[2021-07-05 18:24:33.815]  cpu      READY threads 2/2 (2) huge pages 50% 1/2 memory 4096 KB (16 ms)
[2021-07-05 18:24:35.264]  signal   Ctrl+C received, exiting
[2021-07-05 18:24:35.301]  cpu      stopped (36 ms)
[2021-07-05 18:24:35.301]  opencl   stopped (0 ms)
```

same error with clCreateBuffer
others algo do the same

## Spudz76 | 2021-07-07T21:33:21+00:00
No, the pool is handing out RandomX job which overrides any commandline algo selection.

Connect to cn/r pool (if there are any coins still based on cn/r) to get cn/r jobs.  Otherwise miner follows what type of job has been sent.

# Action History
- Created by: venomega | 2021-07-05T16:56:27+00:00
- Closed at: 2025-06-20T11:02:36+00:00
