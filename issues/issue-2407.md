---
title: 'xmrig-nvidia No valid algorithm specified. Exiting. "algo": "astrobwt"'
source_url: https://github.com/xmrig/xmrig/issues/2407
author: art23130
assignees: []
labels: []
created_at: '2021-05-24T09:21:05+00:00'
updated_at: '2021-05-26T06:04:25+00:00'
type: issue
status: closed
closed_at: '2021-05-26T06:04:25+00:00'
---

# Original Description
**Describe the bug**
I have installed GPU xmrig on Ubuntu. When I execute xmrig-nvidia I get this message: No valid algorithm specified. Exiting. 
I have tried on xmrig as well, it is the same incompatible/disabled algorithm "astrobwt" detected, reconnect.


# Discussion History
## Spudz76 | 2021-05-24T12:19:26+00:00
Which GPU model and which nvidia driver version?

xmrig-nvidia existed, but is defunct for a while now.  Do you mean xmrig + xmrig-cuda plugin?  You need the latest of both ([xmrig](https://github.com/xmrig/xmrig/) and [xmrig-cuda](https://github.com/xmrig/xmrig-cuda/)), built separately and then copied together into a runtime folder.  You'll need the CUDA Toolkit that matches up with both your chip family (Fermi/Kepler/Maxwell/Pascal... etc) and is =< the CUDA that is in your driver.

AstroBWT should be supported on anything above Fermi (arch 20 or 21).  Here it is attempting to almost work on a Kepler laptop chip (but, no "unsupported algorithm" error):
```
 * CUDA         10.2/11.0/6.12.1-dev
 * NVML         11.450.119.03/450.119.03 press e for health report
 * CUDA GPU     #0 01:00.0 Quadro K1100M 705/1400 MHz smx:2 arch:30 mem:1080/1999 MB
[2021-05-24 05:53:56.804]  nvidia   use profile  astrobwt  (1 thread) scratchpad 20480 KB
|  # | GPU |  BUS ID | INTENSITY | THREADS | BLOCKS | BF |  BS | MEMORY | NAME
|  0 |   0 | 01:00.0 |        96 |      32 |      3 |  0 |   0 |    892 | Quadro K1100M
[2021-05-24 05:53:56.922]  nvidia   READY threads 1/1 (118 ms)
[2021-05-24 05:54:08.655]  nvidia   thread #0 failed with error <hash>:168 "the launch timed out and was terminated"
```

The `nvidia-smi` command should say which CUDA is in your driver, and the xmrig-cuda build has to be that or below (see here, I must use Toolkit 11.0 or below, but then because Kepler CUDA Toolkit support was abandoned in 11.x I have to use Toolkit 10.2 build, as seen above in the CUDA line 10.2/11.0...
```
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 450.119.03   Driver Version: 450.119.03   CUDA Version: 11.0     |
|-------------------------------+----------------------+----------------------+
```

Pretty sure it does work on a better GPU / not sure why it only crashes upon being given a job (the READY line means it loaded and launched okay...) but it wouldn't be the first time a laptop GPU didn't do something stronger chips can (I have no desktop Keplers to try).  Maxwell I'm pretty sure works but I'm about to make sure.

## Spudz76 | 2021-05-24T12:48:20+00:00
Tested good on Pascal:
```
 * CUDA         11.0/11.0/6.12.1-dev
 * NVML         11.450.119.03/450.119.03 press e for health report
 * CUDA GPU     #0 03:00.0 GeForce GTX 1060 6GB 1759/4004 MHz smx:10 arch:61 mem:6005/6078 MB
[2021-05-24 06:44:40.170]  nvidia   use profile  astrobwt  (1 thread) scratchpad 20480 KB
|  # | GPU |  BUS ID | INTENSITY | THREADS | BLOCKS | BF |  BS | MEMORY | NAME
|  0 |   0 | 03:00.0 |       608 |      32 |     19 |  0 |   0 |   5653 | GeForce GTX 1060 6GB
[2021-05-24 06:44:40.755]  nvidia   READY threads 1/1 (585 ms)
[2021-05-24 06:44:50.587]  nvidia   accepted (1/0) diff 8413 (408 ms)
[2021-05-24 06:44:56.809]  nvidia   accepted (2/0) diff 17687 (409 ms)
[2021-05-24 06:45:21.639]  nvidia   accepted (3/0) diff 17687 (406 ms)
[2021-05-24 06:45:24.117]  nvidia   accepted (4/0) diff 17687 (411 ms)
[2021-05-24 06:45:44.399]  nvidia   #0 03:00.0  85W 47C 2075/4536 MHz fan0:95%
[2021-05-24 06:45:44.399]  miner    speed 10s/60s/15m 1168.6 1173.2 n/a H/s max 1203.9 H/s
|   CUDA # | AFFINITY | 10s  H/s | 60s  H/s | 15m  H/s |
|        0 |       -1 |   1172.5 |   1175.2 |      n/a | #0 03:00.0 GeForce GTX 1060 6GB
|        - |        - |   1174.5 |   1174.0 |      n/a |
[2021-05-24 06:46:00.121]  miner    speed 10s/60s/15m 1174.5 1174.0 n/a H/s max 1203.9 H/s
```

## art23130 | 2021-05-24T14:45:43+00:00
This is my system specs:
GEFORCE GTX 1080 
Driver: NVIDIA-430
CUDA: 10.1

I have installed: https://github.com/xmrig/xmrig/releases/download/v6.12.1/xmrig-6.12.1-linux-x64.tar.gz
and this: https://github.com/xmrig/xmrig-cuda

I will try it again and get back to you with the exact error code.



## Spudz76 | 2021-05-24T15:03:22+00:00
That all matches up as long as you're using CUDA Toolkit 10.1 (`-DCUDA_TOOLKIT_ROOT_DIR=/usr/local/cuda-10.1`) in the xmrig-cuda build.

## art23130 | 2021-05-25T15:29:52+00:00
It seems that it dose not detect my GPUs. However, I am using CUDA/CUDNN for DL model training and it works.

 * OPENCL       disabled
 * CUDA         disabled ((null))
[2021-05-25 16:27:05.480]  net      dero.miner.rocks:30182 incompatible/disabled algorithm "astrobwt" detected, reconnect
[2021-05-25 16:27:05.480]  net      dero.miner.rocks:30182 login error code: 6

## Spudz76 | 2021-05-26T02:08:10+00:00
The libxmrig-cuda.so is not initializing it should not say (null).  Have you specified a loader or maybe is it "null" rather than null (without quotes).  The file should be in the same folder with the main executable.

## art23130 | 2021-05-26T06:04:25+00:00
I have rebuild the module with the standard CUDA variables and it works now.

# Action History
- Created by: art23130 | 2021-05-24T09:21:05+00:00
- Closed at: 2021-05-26T06:04:25+00:00
