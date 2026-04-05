---
title: Can't find AMD device when using Macbook
source_url: https://github.com/xmrig/xmrig/issues/249
author: jrgleason
assignees: []
labels:
- bug
created_at: '2017-12-09T17:57:02+00:00'
updated_at: '2018-11-05T07:01:51+00:00'
type: issue
status: closed
closed_at: '2018-11-05T07:01:51+00:00'
---

# Original Description
I am trying to run as described but...

```
./xmrig-amd -o pool.monero.hashvault.pro:5555 -u <MY ADDRESS> -p x -k
 * VERSIONS:     XMRig/2.4.3-beta2 libuv/1.18.1-dev OpenCL/1.2 clang/9.0.0
 * CPU:          Intel(R) Core(TM) i7-4980HQ CPU @ 2.80GHz x64 AES-NI
 * ALGO:         cryptonight, donate=5%
 * POOL #1:      pool.monero.hashvault.pro:5555
 * COMMANDS:     hashrate, pause, resume
[2017-12-09 12:54:42] compiling code and initializing GPUs. This will take a while...
[2017-12-09 12:54:42] No AMD device found.
[2017-12-09 12:54:42] Failed to start threads
```

But if I list devices on ethminer

```
FORMAT: [platformID] [deviceID] deviceName
[0] [0] Iris Pro
	CL_DEVICE_TYPE: GPU
	CL_DEVICE_GLOBAL_MEM_SIZE: 1610612736
	CL_DEVICE_MAX_MEM_ALLOC_SIZE: 402653184
	CL_DEVICE_MAX_WORK_GROUP_SIZE: 512
[0] [1] AMD Radeon R9 M370X Compute Engine
	CL_DEVICE_TYPE: GPU
	CL_DEVICE_GLOBAL_MEM_SIZE: 2147483648
	CL_DEVICE_MAX_MEM_ALLOC_SIZE: 536870912
	CL_DEVICE_MAX_WORK_GROUP_SIZE: 256
```



# Discussion History
## mxjoe | 2017-12-09T23:07:00+00:00
Please post your config.json. It is very helpful for identifying the problem.

## jrgleason | 2017-12-10T15:42:49+00:00
I am using the default config.json (IE not declaring any). I configured from source and am running from the build directory.

## jrgleason | 2017-12-10T15:44:11+00:00
"Also you can use configuration via config file, default config.json." So that to me sounded like explicitly using a config.json was optional. I am passing the config param through my terminal call.

## mxjoe | 2017-12-10T20:41:37+00:00
You must specify the right GPU (AMD Radeon R9 M370X) in config.json.

## jrgleason | 2017-12-11T19:13:21+00:00
Ok, so if I copy the src/config.json to my folder. Now where do I specify the right device? 

## jrgleason | 2017-12-11T19:26:26+00:00
Ok I tried this...

```
./xmrig-amd --opencl-devices=N 
 * VERSIONS:     XMRig/2.4.3-beta2 libuv/1.18.1-dev OpenCL/1.2 clang/9.0.0
 * CPU:          Intel(R) Core(TM) i7-4980HQ CPU @ 2.80GHz x64 AES-NI
 * ALGO:         cryptonight, donate=5%
 * POOL #1:      pool.monero.hashvault.pro:5555
 * COMMANDS:     hashrate, pause, resume
[2017-12-11 14:21:53] compiling code and initializing GPUs. This will take a while...
[2017-12-11 14:21:53] using non AMD device: Apple
[2017-12-11 14:21:53] #0, GPU #0 Iris Pro, intensity: 896 (8/512), cu: 40
[2017-12-11 14:21:53] Error CL_INVALID_BUFFER_SIZE when calling clCreateBuffer to create hash scratchpads buffer.
[2017-12-11 14:21:53] Failed to start threads
```
So GPU is apparently 0,0 So I use the following config...

```
{
    "algo": "cryptonight",
    "background": false,
    "colors": true,
    "donate-level": 5,
    "log-file": null,
    "print-time": 60,
    "retries": 5,
    "retry-pause": 5,
    "syslog": false,
    "opencl-platform": 0,
    "opencl-devices": 0,
    "threads": [
        {
            "index": 0,
            "intensity": 896,
            "worksize": 8,
            "affine_to_cpu": false
        }
    ],
    "pools": [
        {
            "url": "pool.monero.hashvault.pro:5555",
            "user": "<Address>",
            "pass": "x",
            "keepalive": true,
            "nicehash": false
        }
    ],
    "api": {
        "port": 0,
        "access-token": null,
        "worker-id": null
    }
}
```

But I still get

```
[2017-12-11 14:25:49] compiling code and initializing GPUs. This will take a while...
[2017-12-11 14:25:49] using non AMD device: Apple
[2017-12-11 14:25:49] #0, GPU #0 Iris Pro, intensity: 896 (8/512), cu: 40
[2017-12-11 14:25:49] Error CL_INVALID_BUFFER_SIZE when calling clCreateBuffer to create hash scratchpads buffer.
[2017-12-11 14:25:49] Failed to start threads
```

## jrgleason | 2017-12-11T19:31:50+00:00
NM this seemed to work...

```
{
    "algo": "cryptonight",
    "background": false,
    "colors": true,
    "donate-level": 5,
    "log-file": null,
    "print-time": 60,
    "retries": 5,
    "retry-pause": 5,
    "syslog": false,
    "opencl-platform": 0,
    "opencl-devices": 1,
    "threads": [
        {
            "index": 1,
            "intensity": 400,
            "worksize": 8,
            "affine_to_cpu": false
        }
    ],
    "pools": [
        {
            "url": "pool.monero.hashvault.pro:5555",
            "user": "<Address>",
            "pass": "x",
            "keepalive": true,
            "nicehash": false
        }
    ],
    "api": {
        "port": 0,
        "access-token": null,
        "worker-id": null
    }
}
```


## jrgleason | 2017-12-11T20:01:47+00:00
Still getting what seems like really low hash rates. Does `[2017-12-11 15:00:19] speed 10s/60s/15m 146.4 146.4 n/a H/s max: 146.4 H/s` sound right for a `#0, GPU #1 AMD Radeon R9 M370X Compute Engine, intensity: 500 (8/256), cu: 10
`

## romeokienzler | 2018-02-12T19:21:35+00:00
I was getting 75H/s, the my mac just freezed to death ... :)


# Action History
- Created by: jrgleason | 2017-12-09T17:57:02+00:00
- Closed at: 2018-11-05T07:01:51+00:00
