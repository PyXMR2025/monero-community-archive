---
title: ' buffer overflow detected'
source_url: https://github.com/xmrig/xmrig/issues/3472
author: Oldertarl
assignees: []
labels: []
created_at: '2024-04-30T21:02:49+00:00'
updated_at: '2024-05-02T20:16:08+00:00'
type: issue
status: closed
closed_at: '2024-05-02T19:56:49+00:00'
---

# Original Description
**Describe the bug**
When running the command line `xmrig -c "config.json"`
I constantly get a buffer overflow and terminated [aborted]

Fresh Unbutu:
DISTRIB_ID=Ubuntu
DISTRIB_RELEASE=24.04
DISTRIB_CODENAME=noble
DISTRIB_DESCRIPTION="Ubuntu 24.04 LTS"

XMRig 6.21.1 with GCC 13.2.0
features: 64-bit AES


**Expected behavior**
A clear and concise description of what you expected to happen.


```
 * ABOUT        XMRig/6.21.1 gcc/13.2.0 (built for Linux x86-64, 64 bit)
 * LIBS         libuv/1.48.0 OpenSSL/3.0.13 hwloc/2.10.0
 * HUGE PAGES   supported
 * 1GB PAGES    disabled
 * CPU          Intel(R) Core(TM) i5-4570T CPU @ 2.90GHz (1) 64-bit AES
                L2:0.5 MB L3:4.0 MB 2C/4T NUMA:1
 * MEMORY       3.0/7.6 GB (39%)
                DIMM_A0: 4 GB DDR3 @ 1600 MHz M471B5173QH0-YK0
                DIMM_B0: 4 GB DDR3 @ 1600 MHz 9905469-063.A00LF
 * MOTHERBOARD  LENOVO - SHARKBAY
 * DONATE       5%
 * ASSEMBLY     auto:intel
 * POOL #1      pool.supportxmr.com:9000 algo auto
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       disabled
 * CUDA         disabled
[2024-04-30 22:55:14.406]  net      use pool pool.supportxmr.com:9000 TLSv1.2 141.94.96.195
[2024-04-30 22:55:14.406]  net      fingerprint (SHA-256): "MASKEDf5dac5d65a91e9b8aefd759135c59e784872f05fd73"
[2024-04-30 22:55:14.406]  net      new job from pool.supportxmr.com:9000 diff 100001 algo rx/0 height 3138929 (6 tx)
[2024-04-30 22:55:14.406]  cpu      use argon2 implementation AVX2
[2024-04-30 22:55:14.406]  msr      register values for "intel" preset have been set successfully (0 ms)
[2024-04-30 22:55:14.406]  randomx  init dataset algo rx/0 (4 threads) seed 5dd67252917d0a41...
*** buffer overflow detected ***: terminated
Aborted

```

**Additional context**
Tried different pools and port numbers, they either die in buffer overflow or end of file errors..

Any help is very welcome! 



# Discussion History
## SChernykh | 2024-04-30T21:18:21+00:00
Try the latest release (6.21.3), it fixed one overflow in RandomX initialization.

## Oldertarl | 2024-04-30T21:39:40+00:00
ok strange there is a higher version...
have installed on a fresh machine etc etc and got the older version?
used `git clone https://github.com/xmrig/xmrig.git` 
Will now need to seek the how-to to update 

very new to this all..
any hints?


## SChernykh | 2024-04-30T21:56:27+00:00
`git clone ...` should give you the latest code which is v6.21.3 at the moment. Maybe you did it more than a week ago, before v6.21.3 released.

## Oldertarl | 2024-05-01T07:32:28+00:00
Sadly not 
did the whole thing Sunday 28th.
so really confused overall as you may understand..
thanks for the hints, will start working on them in the coming hours!


## Oldertarl | 2024-05-01T07:41:05+00:00
Guess I have to perform some serious actions...

```
~/xmrig/build$ cmake ..
CMake Error at /usr/share/cmake-3.28/Modules/FindPackageHandleStandardArgs.cmake:230 (message):
  Could NOT find HWLOC (missing: HWLOC_LIBRARY HWLOC_INCLUDE_DIR)
Call Stack (most recent call first):
  /usr/share/cmake-3.28/Modules/FindPackageHandleStandardArgs.cmake:600 (_FPHSA_FAILURE_MESSAGE)
  cmake/FindHWLOC.cmake:25 (find_package_handle_standard_args)
  src/backend/cpu/cpu.cmake:30 (find_package)
  src/backend/backend.cmake:1 (include)
  CMakeLists.txt:49 (include)

```

## SChernykh | 2024-05-01T07:55:10+00:00
Did you follow the instructions from https://xmrig.com/docs/miner/build/ubuntu ?

## Oldertarl | 2024-05-02T17:16:25+00:00
The above error comes from the advanced guide found on your linked page
Getting a tiny bit frustrated about this 


## SChernykh | 2024-05-02T17:33:29+00:00
Buffer overflow is fixed in the latest version. You should try to delete all xmrig folders, and follow the guide from the beginning. Double check that XMRig shows `XMRig/6.21.3` when it starts.

## Oldertarl | 2024-05-02T17:58:47+00:00
Will do just that 
fresh start seems to be the best option for the moment 
pollution is never good 
Will update right after  

## Oldertarl | 2024-05-02T19:05:27+00:00
Fresh new Unbutu server installation 
Fresh new followup on the link install process you provided me 
no errors after following the tips provided on [here ](https://askubuntu.com/questions/1482459/graphics-issues-after-amdgpu-tinkering-dpkg-error-processing-package-amdgpu-d)
Started the program et voila 
` ABOUT        XMRig/6.21.1 gcc/13.2.0 (built for Linux x86-64, 64 bit)`
I guess version 6.21.3 has not been released for the build I am using..

## SChernykh | 2024-05-02T19:19:17+00:00
I don't know how you're getting 6.21.1 if you're compiling from source using `git clone`. That version number was changed more than 2 months ago: https://github.com/xmrig/xmrig/commit/f9c4c572164eb50129b0b541143ae5e5a409c3c1

Please copy-paste the exact sequence of commands that you used. You're doing something really wrong at some step.

P.S. Or maybe you're just starting XMRig 6.21.1 binary that you downloaded before? You should start the binary that you built from the source.

## Oldertarl | 2024-05-02T19:30:14+00:00
Deleted every folder in the home dir /home/username
Step by step running every line below 
```
sudo apt install git build-essential cmake automake libtool autoconf
git clone https://github.com/xmrig/xmrig.git
mkdir xmrig/build && cd xmrig/scripts
./build_deps.sh && cd ../build
cmake .. -DXMRIG_DEPS=scripts/deps
make -j$(nproc)
```

created config.json in the homefolder with below content (user truncated here)

```
{
    "autosave": true,
    "cpu": true,
    "opencl": false,
    "cuda": false,
    "pools": [
        {
            "url": "de.monero.herominers.com:1111",
            "user": "4B7dbsv<truncated>d69XoGmss",
            "keepalive": true,
            "tls": true
        }
    ]
}
```

from the home folder started 
 xmrig -c "config.json"
and tried 
sudo  xmrig -c "config.json"

and 
sudo /usr/bin/xmrig -c "/home/username/config.json"

both giving me the same (old) version
 

## Oldertarl | 2024-05-02T19:55:06+00:00
ok shoot me in the foot
just started  `/xmrig/build$ sudo ./xmrig -c "/home/username/config.json"`
and 
`ABOUT        XMRig/6.21.3 gcc/13.2.0 (built for Linux x86-64, 64 bit)`

Guess the cleanup has not done ALL the cleaning 
Got this working now 
very grateful for your help! 

## SChernykh | 2024-05-02T20:07:16+00:00
> sudo /usr/bin/xmrig -c "/home/username/config.json"

Well, this is exactly

> maybe you're just starting XMRig 6.21.1 binary that you downloaded before?

## Oldertarl | 2024-05-02T20:16:07+00:00
you are fully right!
Was just assuming that during the build phase, the /usr/bin version would be updated as well ( kind of would make sense in the build phase I would say) 
Now running from the build folder and smooth sailing! 

# Action History
- Created by: Oldertarl | 2024-04-30T21:02:49+00:00
- Closed at: 2024-05-02T19:56:49+00:00
