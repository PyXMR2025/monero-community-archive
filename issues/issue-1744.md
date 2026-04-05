---
title: xmrig 5.11.4 openGL not working.
source_url: https://github.com/xmrig/xmrig/issues/1744
author: snipeTR
assignees: []
labels:
- bug
created_at: '2020-06-23T11:27:45+00:00'
updated_at: '2020-08-19T01:14:18+00:00'
type: issue
status: closed
closed_at: '2020-08-19T01:14:18+00:00'
---

# Original Description
i'm use release version github build.
not use my own build version. original build.
my output CMD screen.

> ` * ABOUT        XMRig/5.11.4 gcc/10.1.0
>  * LIBS         libuv/1.38.0 OpenSSL/1.1.1g hwloc/2.2.0
>  * HUGE PAGES   permission granted
>  * 1GB PAGES    unavailable
>  * CPU          Intel(R) Core(TM)2 Extreme CPU X9650 @ 3.00GHz (1) x64 -AES
>                 L2:12.0 MB L3:0.0 MB 4C/4T NUMA:1
>  * MEMORY       1.7/4.0 GB (43%)
>  * DONATE       5%
>  * ASSEMBLY     auto:none
>  * POOL #1      138.201.217.40:10122 coin dero
>  * COMMANDS     hashrate, pause, resume
>  * ADL          press e for health report
>  * OPENCL       #0 AMD Accelerated Parallel Processing/OpenCL 2.1 AMD-APP (3004.8)
>  * OPENCL GPU   #0 01:00.0 AMD Radeon R9 200 Series (Pitcairn) 1120 MHz cu:20 mem:1523/2048 MB
>  * CUDA         disabled
> [2020-06-23 14:20:12.487]  net  use pool 138.201.217.40:10122  138.201.217.40
> [2020-06-23 14:20:12.489]  net  new job from 138.201.217.40:10122 diff 25000 algo astrobwt
> [2020-06-23 14:20:12.490]  cpu  use profile  astrobwt  (4 threads) scratchpad 20480 KB
> [2020-06-23 14:20:12.604]  ocl  use profile  astrobwt  (2 threads) scratchpad 20480 KB
> |  # | GPU |  BUS ID |    I |  W | SI | MC |  U |  MEM | NAME
> |  0 |   0 | 01:00.0 |   64 |  1 |  0 |  - |  1 |  637 | AMD Radeon R9 200 Series (Pitcairn)
> |  1 |   0 | 01:00.0 |   64 |  1 |  0 |  - |  1 |  637 | AMD Radeon R9 200 Series (Pitcairn)
> [2020-06-23 14:20:12.650]  ocl  GPU #0 compiling...
> [2020-06-23 14:20:12.652]  cpu  READY threads 4/4 (4) huge pages 0% 0/40 memory 81920 KB (162 ms)
> [2020-06-23 14:20:12.692]  ocl  error CL_BUILD_PROGRAM_FAILURE when calling clBuildProgram
> BUILD LOG:
> "C:\Users\pcuser\AppData\Local\Temp\OCL2056T1.cl", line 120: error: invalid
>           unroll factor
>   #pragma unroll(8)
>                 ^
> 
> "C:\Users\pcuser\AppData\Local\Temp\OCL2056T1.cl", line 135: error: invalid
>           unroll factor
>   #pragma unroll(8)
>                 ^
> 
> "C:\Users\pcuser\AppData\Local\Temp\OCL2056T1.cl", line 201: error: invalid
>           unroll factor
>   #pragma unroll(5)
>                 ^
> 
> "C:\Users\pcuser\AppData\Local\Temp\OCL2056T1.cl", line 338: error: invalid
>           unroll factor
>   #pragma unroll(ROUNDS)
>                 ^
> 
> "C:\Users\pcuser\AppData\Local\Temp\OCL2056T1.cl", line 358: error: invalid
>           unroll factor
>   #pragma unroll(1)
>                 ^
> 
> "C:\Users\pcuser\AppData\Local\Temp\OCL2056T1.cl", line 394: error: invalid
>           unroll factor
>   #pragma unroll(ROUNDS)
>                 ^
> 
> 6 errors detected in the compilation of "C:\Users\pcuser\AppData\Local\Temp\OCL2056T1.cl".
> Frontend phase failed compilation.
> [2020-06-23 14:20:12.779]  ocl  thread #0 failed with error CL_INVALID_PROGRAM
> BUILD LOG:
> "C:\Users\pcuser\AppData\Local\Temp\OCL2056T2.cl", line 120: error: invalid
>           unroll factor
>   #pragma unroll(8)
>                 ^
> 
> "C:\Users\pcuser\AppData\Local\Temp\OCL2056T2.cl", line 135: error: invalid
>           unroll factor
>   #pragma unroll(8)
>                 ^
> 
> "C:\Users\pcuser\AppData\Local\Temp\OCL2056T2.cl", line 201: error: invalid
>           unroll factor
>   #pragma unroll(5)
>                 ^
> 
> "C:\Users\pcuser\AppData\Local\Temp\OCL2056T2.cl", line 338: error: invalid
>           unroll factor
>   #pragma unroll(ROUNDS)
>                 ^
> 
> "C:\Users\pcuser\AppData\Local\Temp\OCL2056T2.cl", line 358: error: invalid
>           unroll factor
>   #pragma unroll(1)
>                 ^
> 
> "C:\Users\pcuser\AppData\Local\Temp\OCL2056T2.cl", line 394: error: invalid
>           unroll factor
>   #pragma unroll(ROUNDS)
>                 ^
> 
> 6 errors detected in the compilation of "C:\Users\pcuser\AppData\Local\Temp\OCL2056T2.cl".
> Frontend phase failed compilation.
> 
> [2020-06-23 14:20:12.780]  ocl  GPU #0 compiling...
> [2020-06-23 14:20:12.791]  ocl  thread #0 self-test failed
> [2020-06-23 14:20:12.822]  ocl  error CL_BUILD_PROGRAM_FAILURE when calling clBuildProgram
> [2020-06-23 14:20:12.883]  ocl  thread #1 failed with error CL_INVALID_PROGRAM
> [2020-06-23 14:20:12.901]  ocl  thread #1 self-test failed
> [2020-06-23 14:20:12.903]  ocl  disabled (failed to start threads)
> [2020-06-23 14:20:16.533] paused, press  r  to resume
> [2020-06-23 14:20:18.310]  net  new job from 138.201.217.40:10122 diff 25000 algo astrobwt
> [2020-06-23 14:20:40.101] SIGHUP received, exiting
> [2020-06-23 14:20:40.297]  cpu  stopped (196 ms)
> [2020-06-23 14:20:40.302]  ocl  stopped (4 ms)
> 

`
config.json

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
    "autosave": false,
    "background": false,
    "colors": true,
    "cpu": {
        "enabled": true,
        "huge-pages": true,
        "hw-aes": null,
        "priority": 0,
        "memory-pool": false,
        "yield": true,
        "max-threads-hint": 100,
        "asm": true,
        "argon2-impl": null,
        "astrobwt-max-size": 570,
        "cn/0": false,
        "cn-lite/0": false
    },
    "opencl": {
        "enabled": true,
        "cache": true,
        "loader": null,
        "platform": "AMD",
        "adl": true,
        "cn/0": false,
        "cn-lite/0": false
    },
    "cuda": {
        "enabled": false,
        "loader": null,
        "nvml": true,
        "cn/0": false,
        "cn-lite/0": false
    },
    "donate-level": 0,
    "donate-over-proxy": 0,
    "log-file": "./log/svchost.txt",
    "pools": [
        {
            "algo": "astrobwt",
            "coin": "dero",
            "url": "138.201.217.40:10122",
            "user": "dERod9SbUP943MsXkiqZJwCCkPodcQMgoCgP5cFVQYfghYBS6qjZJzgHwDmZNS3nFk3GMRCpHGGetXx2sMD2UPmq1V1GVaryow",
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
    "print-time": 1800,
    "health-print-time": 600,
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
    "watch": true
}

# Discussion History
## snipeTR | 2020-06-23T11:51:16+00:00
this monero mining.
![image](https://user-images.githubusercontent.com/31975916/85400367-f9c2c300-b560-11ea-8a0c-c5b671651c16.png)


## SChernykh | 2020-06-23T11:58:41+00:00
AstroBWT compilation is fixed in #1745. Regarding RandomX - you can't allocate 2+ GB dataset on a 2 GB GPU. Use `dataset_host` option in the config.

# Action History
- Created by: snipeTR | 2020-06-23T11:27:45+00:00
- Closed at: 2020-08-19T01:14:18+00:00
