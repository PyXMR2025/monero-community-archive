---
title: RandomX migration guide
source_url: https://github.com/xmrig/xmrig/issues/1204
author: xmrig
assignees: []
labels:
- enhancement
- META
- algo
created_at: '2019-09-28T17:41:22+00:00'
updated_at: '2019-12-22T19:33:55+00:00'
type: issue
status: closed
closed_at: '2019-12-22T19:33:55+00:00'
---

# Original Description
**:warning: Monero will change PoW algorithm to RandomX on November 30.** :warning:
![Clipboard01](https://user-images.githubusercontent.com/27528955/65820082-1b4f8200-e24f-11e9-97b9-487830fe7555.png)

### Required steps
1. **Miners and proxy should be updated to v3.2+ before November 30.**
2. If your pool not support algorithm negotiation option `coin` on each Monero pool should be set to `monero`.

### Notes
* xmrig-amd project now obsolete and will not updated, it integrated into main miner (v4.2+)
* xmrig-nvidia will be integrated in main miner too.

### Test pool
~Right now is no testnet pool available, for test miner 2 options available:~

**Testnet pool https://rx.minexmr.com/ now available.**

1. **randomx-benchmark.xmrig.com:7777** (xmrig-proxy connected to real Monero testnet daemon)

```json
{
    "pools": [
        {
            "url": "randomx-benchmark.xmrig.com:7777"
        }
    ]
}
```

2. Mine directly to Monero testnet daemon:

```json
{
    "pools": [
        {
            "url": "127.0.0.1:28081",
            "daemon": true
        }
    ]
}
```

### Notes for pool operators
* New required field `seed_hash` should be added to each job object.
* Optional field `"algo":"rx/0"` recommended to allow automatic algorithm negotiation.

# Discussion History
## trasherdk | 2019-09-29T01:16:24+00:00
If you had merged #1068 there would be testnet pools now.

## xmrig | 2019-10-09T12:13:35+00:00
Testnet pool https://rx.minexmr.com/

## 2010phenix | 2019-10-20T12:13:05+00:00
not mine but I think we lost AION long time move side by side with Monero.... ?
-- cut --
https://github.com/aeonix/aeon/releases/tag/v0.13.0.0-aeon
-- cut --

## trasherdk | 2019-10-20T12:44:38+00:00
A testnet pool that does make (testnet) payments, and support stratum-self-select.
It's a fork of https://github.com/jtgrassie/monero-pool with added support for pool-fee-wallet.

[Miner link](http://ghost-m1.fumlersoft.dk:8000)
[Browser link](http://ghost-m1.fumlersoft.dk:8001)

## JeffreyChu2009 | 2019-11-07T01:55:43+00:00
It is Nov 7th today, a week after October 31. It's still 0.14.1.0 on https://web.getmonero.org/downloads/ for the latest version released. I have to doubt the deadline of the mainnet upgrade on this coming 30th.

Lisa Su will have released Threadripper 3960X/3970X/3990X by this weekend, are we buying it or not?

## trasherdk | 2019-11-07T15:18:25+00:00
If you can't wait for the CI binaries to be released, you can always compile yourself. It's not that hard.
https://github.com/monero-project/monero/tree/release-v0.15
I'm not sure who's responsible for releasing, but there's still plenty of time.

## petitmouss | 2019-11-14T14:32:17+00:00
Hi all,
@xmrig You wrote:
"xmrig-amd project now obsolete and will not updated, it integrated into main miner (v4.2+)
xmrig-nvidia will be integrated in main miner too."
It means that xmrig-nvidia will not be updated to work on RandomX? I understand well ?
Thanks, Bruno

## xmrig | 2019-11-14T14:39:39+00:00
@petitmouss both xmrig-amd and xmrig-nvidia integrated into main unified miner, separated projects will no longer updated.
Thank you.

## petitmouss | 2019-11-14T15:30:20+00:00
Thank @xmrig for you reply
1: I saw a repo with xmrig-cuda. This is the repository is to build the mandatory CUDA library?
2: supportxmr.com the pool that I use does not write anything about the RandomX switching that you had fixed for 30nov. There is a timeframe to allow them to apply the changes ?

Thanks in advance!
-> Sorry for my English, it is not my first :-(


## xmrig | 2019-11-14T15:57:59+00:00
1. xmrig-cuda mandatory to use CUDA, but miner not require CUDA and xmrig-cuda to build, this library loaded in runtime.
2. Actually I don't know why the did't create announce, but they created testnet pool https://www.reddit.com/r/MoneroMining/comments/do6hyp/supportxmr_randomx_testnet_pool/

## petitmouss | 2019-11-17T13:10:17+00:00
Hello @xmrig ,
I'm trying to build xmrig-cuda but it seems that my cuda 10.x is not in compliance with the cmake pre-build expectation. I have this message:

```
-- Found CUDA: /usr/local/cuda-10.1 (found suitable version "10.1", minimum required is "8.0") 
CMake Error: The following variables are used in this project, but they are set to NOTFOUND.
Please set them or make sure they are set and tested correctly in the CMake files:
CUDA_LIB
    linked by target "xmrig-cuda" in directory /home/bruno/xmrig-cuda

-- Configuring incomplete, errors occurred!

```
I'm looking for cmake to understand and I ve found that:
![Capture d’écran 2019-11-17 à 13 47 23](https://user-images.githubusercontent.com/57761591/69007656-dedffe80-0940-11ea-9fc2-084f204756ce.png)

I should able to update the cmake file (and share it) but I don't have the arch number for CUDA_ARCH.

Can you help me ? Thanks

## petitmouss | 2019-11-17T14:22:01+00:00
I've created a CMakeList.txt with those macros:

```
include(FindCUDA)
cmake_minimum_required(VERSION 3.10)

set(CUDA_ARCH_LIST Auto CACHE LIST
    "List of CUDA architectures on the local machine."
)
cuda_select_nvcc_arch_flags(CUDA_ARCH_FLAGS ${CUDA_ARCH_LIST})
list(APPEND CUDA_NVCC_FLAGS ${CUDA_ARCH_FLAGS})

```
The output after "cmake -Wno-dev ."  is:
```
-- Autodetected CUDA architecture(s): 7.5 
-- Configuring done
-- Generating done
-- Build files have been written to: /tmp/o 

```
so the value of CUDA_ARCH should be 75
no ?



## petitmouss | 2019-11-17T18:07:22+00:00
@xmrig Some update of CUDA.cmake to be compliance with CUDA10.x

The previous cmake script allows to set CUDA_ARCH properly but the libcuda is not detected by cmake when CUDA 10.x is installed.

The cmake output is:

```
-- Found CUDA: /usr/local/cuda-10.1 (found suitable version "10.1", minimum required is "8.0") 
CMake Error: The following variables are used in this project, but they are set to NOTFOUND.
Please set them or make sure they are set and tested correctly in the CMake files:
CUDA_LIB
    linked by target "xmrig-cuda" in directory /home/bruno/xmrig-cuda

-- Configuring incomplete, errors occurred!
```

The installation of CUDA 10 has been done as Nvidia user guide:
https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html#ubuntu-installation

In fact, libcuda reseachs in the CMakeList.txt indicate:
`"${CUDA_TOOLKIT_ROOT_DIR}/lib64" "${LIBCUDA_LIBRARY_DIR}" "${CUDA_TOOLKIT_ROOT_DIR}/lib/x64"`

With CUDA 10.x this lib is in **stub** directory"/usr/local/cuda-10.1/lib64/stubs/libcuda.so"
Note that libcudart is provided in /usr/local/cuda-10.1/lib64/ but is for access to the runtine api instead libcuda provides access to the Driver api.

Anyway, we have to update the **find_library** directive of CMakeList to be able to detect CUDA10.x driver access. Do it like that line 21 of CUDA.cmake file:

`find_library(CUDA_LIB libcuda cuda HINTS "${CUDA_TOOLKIT_ROOT_DIR}/lib64/stubs/" "${CUDA_TOOLKIT_ROOT_DIR}/lib64" "${LIBCUDA_LIBRARY_DIR}" "${CUDA_TOOLKIT_ROOT_DIR}/lib/x64" /usr/lib64 /usr/local/cuda/lib64)
`

I've also added the arch in CUDA.cmake file at line 42:
```
# add Turing support for CUDA >= 10.0
if (NOT CUDA_VERSION VERSION_LESS 10.0)
    list(APPEND DEFAULT_CUDA_ARCH "75")
endif()
```

Now, the cmake output is:
```
~/xmrig-cuda/build$ cmake ..
-- The C compiler identification is GNU 7.4.0
-- The CXX compiler identification is GNU 7.4.0
-- Check for working C compiler: /usr/bin/cc
-- Check for working C compiler: /usr/bin/cc -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Detecting C compile features
-- Detecting C compile features - done
-- Check for working CXX compiler: /usr/bin/c++
-- Check for working CXX compiler: /usr/bin/c++ -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Looking for __builtin___clear_cache
-- Looking for __builtin___clear_cache - found
-- Looking for pthread.h
-- Looking for pthread.h - found
-- Looking for pthread_create
-- Looking for pthread_create - not found
-- Looking for pthread_create in pthreads
-- Looking for pthread_create in pthreads - not found
-- Looking for pthread_create in pthread
-- Looking for pthread_create in pthread - found
-- Found Threads: TRUE  
-- Found CUDA: /usr/local/cuda-10.1 (found suitable version "10.1", minimum required is "8.0") 
-- Found CUDA compiler: nvcc
-- Configuring done
-- Generating done
-- Build files have been written to: /home/bruno/xmrig-cuda/build

```

The compilation works fine after this update and I hope that help someone 👍 

## thagrisu | 2019-11-18T16:18:12+00:00
@xmrig 
you mentioned that your xmrig-proxy script is directly connected to monero testnet daemon.  

> randomx-benchmark.xmrig.com:7777 (xmrig-proxy connected to real Monero testnet daemon)

can you explain how to configure this setup. All options i try end up in communication error between proxy and monero daemon. 
thanks

## xmrig | 2019-11-18T16:42:11+00:00
@thagrisu something like this:
```json
       {
            "algo": null,
            "coin": "monero",
            "url": "127.0.0.1:28081",
            "user": "WALLET ADDRESS",
            "enabled": true,
            "tls": false,
            "tls-fingerprint": null,
            "daemon": true,
            "daemon-poll-interval": 500
        }
```

Key option is `daemon`.
Thank you.

## thagrisu | 2019-11-18T17:40:51+00:00
@xmrig 
thanks for your fast reply. Most of the times i had segmentation fault. Found out this happes when coin value = null .  Is monero right for randomx or do i need to use rx/0 ? 
One more question: Does the proxy script provide individual work for every connected miner or  do all miners receive the same work ? 
Thanks ! 

## xmrig | 2019-11-18T18:09:48+00:00
`monero` is fine, right now it is `cn/r` after fork or with testnet daemon it is `rx/0`, for daemon you must specify algo or coin. How proxy works depends of mode, with `nicehash` one job spited to 256 parts, with `simple` every miner will get full job, but it this case proxy don't reduce connections count and number of connections to daemon will be equal miner count.

About  segmentation fault please open another issue with full details how to reproduce it.
Thank you.

## jmusac | 2019-11-28T14:15:10+00:00
Hi,

How can i test mining on low power option mode. I can't find option in .json file ?

## SChernykh | 2019-11-28T14:58:55+00:00
There is no low power mode for RandomX.

## petitmouss | 2019-11-28T15:35:03+00:00
@jmusac under linux, you can do that (as root):
pid=`ps -eaf | grep xmrig | grep -v grep`
renice +20 $pid

and you can also affine xmrig process to one cpu core by:
taskset 0x1 $pid

Under window, I don't know. Turn off , may be  🧐

## jmusac | 2019-11-29T06:57:42+00:00
I'm asking for windows.

## xmrig | 2019-11-29T07:18:32+00:00
@petitmouss no need use system tools to change priority https://github.com/xmrig/xmrig/blob/master/src/config.json#L25 `(0 idle, 2 normal to 5 highest)`.
@jmusac If you looking for option was known as `low_power_mode` it not exists for RandomX as answered above.
Thank you.

## xmrig | 2019-11-29T07:21:15+00:00
If you looking for light mode: https://github.com/xmrig/xmrig/issues/1318#issuecomment-559676080 but it really slow.

## petitmouss | 2019-11-29T15:47:09+00:00
@xmrig I'm looking for the log of xmrig software and I see "new job" and one or many "accepted".
The questions are:
1 / how many hash is embedded in a job?
2 / what's it depends from?

Thanks!

## aleqx | 2019-11-30T19:00:37+00:00
I have a rig with 13 gtx1070 and a G4400 (2C/2T) with 8 GB ram on Ubuntu 16.04 ... compiled xmrig and xmrig-cuda 2 hours ago from master (git clone ...) using default settings (mkdir build; cd build; cmake ..; make).

No matter what options I try, xmrig is hogging the nvidia driver completely, and also the CPU ... I can't run nvidia-smi at all (it hangs immediately). If I enable nvml in xmrig (i.e. if i don't use `--no-nvml`) then when it lists the GPU temperatures it hangs after GPU#3 for a whopping 60-90 seconds before showing the next line with GPU#4.

I tried `--bfactor=10` and `--bsleep=200`. I even tried `--bsleep=100000` ... no joy. I even forced `--cpu-max-threads-hint=1 --no-huge-pages --randomx-init=1 --randomx-no-numa --cpu-priority=1 --threads=1` but those should be pointless as i'm using `--no-cpu`. Nothing. Tried both irq-balance and no irq-balance.

```
./xmrig -o pool:port -O user:pass --no-cpu --cuda --cuda-loader=./libxmrig-cuda.so --keepalive --print-time=120 -a rx --no-nvml --cuda-bsleep-hint=200 --cuda-bfactor-hint=10
```

Note the `--no-cpu`. Despite this, the CPU is at 100% constantly.

Something is wrong here. Any clues?

I have no such issues with any other algo (I've been mining all sort of things in the past 2 years)

## petitmouss | 2019-12-01T09:12:11+00:00
Hi @aleqx 
1/
memory cache of your cpu ? L1, L2
You can get it with lscpu

2/
you say: "nvidia-smi hangs immediately". 
from previous release of nvidia driver (e.g 36x) the persistent mode of the GPU is not set whereas is required. So try as root:
nvidia-smi -pm 1 -i (Id of you gpu)

3/ set the full path to access to libxmrig-cuda.so 

4/ what was your hash rate before this config ?



## aleqx | 2019-12-01T10:03:39+00:00
L1/2 cache is 32k/256k, nvidia driver is 415.27 (but I tried 430 and 435), Persistence makes no difference on/off, and is not required (persistence just keeps the nvidia driver loaded, otherwise it's loaded when a gpu app starts and unloaded when it finishes; also nvidia-smi -pm 1 has been obsolete for a while). Absolute path to the .so is required otherwise xmrig doesn't even start. Not sure what you mean by hashrate ... there are a ton of different algos with very different hashrates.

## petitmouss | 2019-12-01T10:31:16+00:00
I have this process running in my rig (ubuntu 18 server, no X11):
nvidia-persistenced
and the doc is here:
https://download.nvidia.com/XFree86/Linux-x86_64/396.51/README/nvidia-persistenced.html
and nvidia says:
**A Linux daemon utility, nvidia-persistenced, addresses an undesirable side effect of the NVIDIA kernel driver behavior in certain computing environments**

My setup has been automatically set at the installation step by v430 driver.
I have also /usr/local/cuda-10/bin in my path env. I don't know if it should be efficient for you.

What is the output of lspci ? Does the nvidia gpu(s) are in ?
Did you have the same problem with your previous installation or did you change only the xmrig release?

what is your lsmod output ?


## aleqx | 2019-12-01T11:04:28+00:00
No offense intended as it seems you are trying to help, but you are asking a bunch of irrelevant questions. Everything does work, xmrig is mining at a hashrate that is more or less expected for gtx1070@100W tdp, but the nvidia driver is completely hogged when mining randomx with xmrig 5.0.1, even if it is mining for a while ... until it polls nvml, which hangs as the driver is hogged.

# Action History
- Created by: xmrig | 2019-09-28T17:41:22+00:00
- Closed at: 2019-12-22T19:33:55+00:00
