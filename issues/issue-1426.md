---
title: Assertion failed 5.3.0
source_url: https://github.com/xmrig/xmrig/issues/1426
author: yesilcimenahmet
assignees: []
labels: []
created_at: '2019-12-15T20:32:00+00:00'
updated_at: '2021-04-12T15:09:21+00:00'
type: issue
status: closed
closed_at: '2021-04-12T15:09:21+00:00'
---

# Original Description
Hi, I am using XMRig 5.3.0 and running under SYSTEM user. 
I'm running XMRig with another console application I've developed. The Console application opens XMRig and captures its output with pipe. It gives the following error. 
**Assertion failed: 0, file src/win/stream.c, line 92**

But when I run it with other versions of XMRig it does not give this error.
I have been using the software I have developed for a long time, and this is the first time I have seen this error with XMRig 5.3.0.

# Discussion History
## xmrig | 2019-12-15T20:48:49+00:00
What version of libuv are you using? need to know to check what placed on line 92.
Thank you.

## yesilcimenahmet | 2019-12-16T06:28:43+00:00
I downloaded the XMRig.exe file directly from the Binary Release page. In addition, I compiled XMRig.exe myself using Deps 4.0 (libuv 1.34.0) with GCC. The result is the same.

One important thing to know is that after I change and compile the following CMake definitions to "OFF" (Deps 4.0 libuv 1.34.0), I don't get an error! I do not know why.

option(WITH_CN_LITE         "Enable CryptoNight-Lite algorithms family" OFF)
option(WITH_CN_HEAVY        "Enable CryptoNight-Heavy algorithms family" OFF)
option(WITH_CN_PICO         "Enable CryptoNight-Pico algorithm" OFF)
option(WITH_CN_GPU          "Enable CryptoNight-GPU algorithm" OFF)
option(WITH_ARGON2          "Enable Argon2 algorithms family" OFF)
option(WITH_HTTP            "Enable HTTP protocol support (client/server)" OFF)
option(WITH_TLS             "Enable OpenSSL support" OFF)
option(WITH_OPENCL          "Enable OpenCL backend" OFF)
option(WITH_CUDA            "Enable CUDA backend" OFF)
option(WITH_NVML            "Enable NVML (NVIDIA Management Library) support (only if CUDA backend enabled)" OFF)
option(WITH_STRICT_CACHE    "Enable strict checks for OpenCL cache" OFF)

## yesilcimenahmet | 2019-12-18T11:54:09+00:00
Did you check it? Will this issue be fixed?

# Action History
- Created by: yesilcimenahmet | 2019-12-15T20:32:00+00:00
- Closed at: 2021-04-12T15:09:21+00:00
