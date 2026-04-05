---
title: macOS Kawpow Errors [Or mistake in setup]
source_url: https://github.com/xmrig/xmrig/issues/2345
author: Sammed98
assignees: []
labels: []
created_at: '2021-05-05T03:43:19+00:00'
updated_at: '2025-06-20T11:12:00+00:00'
type: issue
status: closed
closed_at: '2025-06-20T11:12:00+00:00'
---

# Original Description
**Describe the bug**
I want to mine using Kawpow algorithm on my GPU. I have also noted that Kawpow does not run on CPU and I am fine with it. I have modified the config.json file where I have changed the algo value, the pool address, coin and my address. But when I execute xmrig the get the following set of errors. I don't know if they are error but since they are getting consoled with red color I think they are. The error image is as follows: 

<img width="798" alt="Screenshot 2021-05-05 at 9 07 24 AM" src="https://user-images.githubusercontent.com/25957319/117094439-6c0b5300-ad81-11eb-9ab4-fb58695fdd5e.png">

The config file is as follows:
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
        "enabled": false,
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
        "argon2": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
        "astrobwt": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
        "cn": [
            [1, 0],
            [1, 2],
            [1, 4],
            [1, 6],
            [1, 8],
            [1, 10]
        ],
        "cn-heavy": [
            [1, 0],
            [1, 2],
            [1, 4]
        ],
        "cn-lite": [
            [1, 0],
            [1, 1],
            [1, 2],
            [1, 3],
            [1, 4],
            [1, 5],
            [1, 6],
            [1, 7],
            [1, 8],
            [1, 9],
            [1, 10],
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
        "cn/upx2": [
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
        "rx": [0, 2, 4, 6, 8, 10],
        "rx/wow": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
        "cn/0": false,
        "cn-lite/0": false,
        "rx/arq": "rx/wow",
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
                "intensity": 320,
                "worksize": 8,
                "strided_index": [1, 2],
                "threads": [-1, -1],
                "unroll": 8
            }
        ],
        "cn-heavy": [
            {
                "index": 1,
                "intensity": 160,
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
                "intensity": 800,
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
                "intensity": 1920,
                "worksize": 8,
                "strided_index": [2, 2],
                "threads": [-1, -1],
                "unroll": 8
            }
        ],
        "cn/2": [
            {
                "index": 1,
                "intensity": 320,
                "worksize": 8,
                "strided_index": [2, 2],
                "threads": [-1, -1],
                "unroll": 8
            }
        ],
        "cn/upx2": [
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
                "intensity": 1920,
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
                "intensity": 5242880,
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
                "intensity": 320,
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
                "intensity": 320,
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
                "intensity": 320,
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
        "loader": null,
        "cn/0": false,
        "cn-lite/0": false
    },
    "log-file": null,
    "donate-level": 0,
    "donate-over-proxy": 0,
    "pools": [
        {
            "algo": "kawpow",
            "coin": null,
            "url": "poolAddress",
            "user": "CoinName:Address.workerName",
            "pass": "x",
            "rig-id": null,
            "nicehash": false,
            "keepalive": false,
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

The modifications that I have made in the config file are I changed cpu enabled to false, openCL enabled to true, change the algo name to kawpow. The pool address , hashname and workername have the appropriate values. 
The coin I want to mine is dogecoin. The type of GPU I have can be found in the error image. 

**I would like to know what mistake I have done and how to rectify the same.** 

**To Reproduce**
Utilize the above config.json, add the pool address, wallet address and workername and execute the executable. 

**Expected behavior**
Mine coin on the GPU without utlizing CPU

**Required data**
 - Miner log as text or screenshot - Provided Avoe
 - Config file or command line - Provided Above
 - OS: Mac OS
 - For GPU related issues: Intel(R) UHD Graphics 630 and  AMD Radeon Pro 5300M Compute Engine


**Additional context**
Add any other context about the problem here.


# Discussion History
## Spudz76 | 2021-05-05T07:40:59+00:00
I looked around and the [kawpow defs](https://github.com/xmrig/xmrig/blob/master/src/backend/opencl/cl/kawpow/defs.h#L32) use AMD platform as the default for some reason, which seems to be why it is trying to use AMD extensions with the Intel.

Then the actual AMD device doesn't dump a compilation backtrace so that could be anything.


## SChernykh | 2021-05-05T07:52:50+00:00
Remove index 0 GPU from kawpow opencl config, Intel iGPU is not supported and can't even give competitive hashrate. That said, compilation on GPU 1 (AMD) also failed for you because of internal compiler error `cvms_element_build_from_source`. MacOS just has really bad OpenCL support.

## Sammed98 | 2021-05-05T13:18:06+00:00
Ok. I can remove the index 0 component. What should I do regarding the OpenCL error on AMD? Any solution for this?

Or is there any other good miner which works with Mac OS and AMD Radeon Pro 5300M? Dosen't matter which coin it mines. 

## Sammed98 | 2021-05-17T08:35:13+00:00
@xmrig Any comments?

## Spudz76 | 2021-05-17T09:12:57+00:00
dev branch just got #2379 which may allow things to work.  Please pull the current dev and compile and try.

I was fixing the OpenCL on Apple M1 and the same thing made it unworkable, now it works.  So it should also work for Apple OpenCL + other GPUs.  The AMD even though it's an AMD, is behind the Apple OpenCL "firewall" and thus does not have the AMD extensions usually available on AMD GPUs with AMD drivers and a non-abandoned OpenCL layer.  So it also must run the "non-AMD" kawpow kernel.

All CN-based algos should work already (Haven might be worth exchange-mining... also probably works on the CPU at the same time unlike kawpow).

## ganzocrypt | 2021-05-18T16:53:21+00:00
I was getting the same error. I am on Catalina with 2 Xeon and a AMD RX 580 8Gb. CPU mining is ok.
I tried to recompile with the dev brench as @ Spudz76 mentioned but got the same issue.
The top error appears as soon as you start ./xmrig

![Screen Shot 2021-05-18 at 6 51 25 PM](https://user-images.githubusercontent.com/42419950/118692342-372fdf00-b80a-11eb-8162-83b0bff50a2e.png)


## Spudz76 | 2021-05-19T00:28:45+00:00
The early error for `param 0x4037` is due to trying to use `CL_DEVICE_TOPOLOGY_AMD` but the OpenCL is not AMD (it's Apple) so even though it's an AMD device it doesn't have any AMD extensions (Apple OpenCL is dead standard 1.2)

Likely also the issue on the rest I will check for more places things assume AMD (or use the device being AMD as ok to use extensions)...

Try with `platform: "APPLE",` under opencl section of config.json

## Spudz76 | 2021-05-19T06:07:20+00:00
I know the platform in the config won't help the rest of the problems, but [this branch from my fork](https://github.com/Spudz76/xmrig/tree/dev-fixAppleOpenCL) might actually do something.

@ganzocrypt

## ganzocrypt | 2021-05-19T08:12:29+00:00
@Spudz76 will try to compile it and test, thx

## ganzocrypt | 2021-05-19T09:45:06+00:00
@Spudz76 So the top error is gone but the bottom ones are not:

[2021-05-19 11:41:28.641]  opencl   GPU #0 compiling...
[2021-05-19 11:41:35.906]  opencl   error CL_BUILD_PROGRAM_FAILURE when calling clBuildProgram
BUILD LOG:
Error returned by cvms_element_build_from_source
[2021-05-19 11:41:35.906]  opencl   thread #0 failed with error CL_INVALID_PROGRAM
[2021-05-19 11:41:35.907]  opencl   GPU #0 compiling...
[2021-05-19 11:41:35.907]  opencl   thread #0 self-test failed
[2021-05-19 11:41:35.909]  opencl   error CL_BUILD_PROGRAM_FAILURE when calling clBuildProgram
BUILD LOG:
Error returned by cvms_element_build_from_source
[2021-05-19 11:41:35.909]  opencl   thread #1 failed with error CL_INVALID_PROGRAM
[2021-05-19 11:41:35.909]  opencl   thread #1 self-test failed
[2021-05-19 11:41:35.909]  opencl   disabled (failed to start threads)


## ganzocrypt | 2021-05-20T15:17:14+00:00
@Spudz76
there is someone found an [indication where the problem is](https://github.com/xmrig/xmrig-amd/issues/277), could be this the issue? Look the last post.

## Spudz76 | 2021-05-20T20:50:06+00:00
Interesting clue but still unclear why.  atomic_inc() is used other places, and is an old standard OpenCL 1.2 call so AppleCL should support it fine.

Sometimes OpenCL actually gives a compilation log rather than a whole bunch of no-info.

This [environment var](https://discussions.apple.com/thread/6724078?answerId=30065411022#30065411022) seems it might make it say more.

## ganzocrypt | 2021-05-20T20:55:43+00:00
I tested by first commenting out the mentioned code, same error.
But I am not familiar with the OpenCL, are the different function based on the different algos?
Can really debug much here other that recompiling and do a quick test.
If you have any suggestion and want to test something let me know. thx

## Spudz76 | 2021-05-20T21:41:24+00:00
Set `export CL_LOG_ERRORS="stderr"` and see if it says more about the compilation failure.

## ganzocrypt | 2021-05-20T21:43:03+00:00
I do not have compilation failure, just the same error at runtime.

## Spudz76 | 2021-05-20T22:46:41+00:00
well there is a `CL_BUILD_PROGRAM_FAILURE` just before it tries to send the broken result of compilation as a kernel which then throws the `CL_INVALID_PROGRAM`

was hoping with the `CL_LOG_ERRORS` thing it might say more than `Error returned by cvms_element_build_from_source`

but still curious why it continues and loads the broken compilation result and tries to use it

## ganzocrypt | 2021-05-21T09:01:11+00:00
oh ok you were referring to the compile during runtime in the screenshot, sorry got confused.
where can I put CL_LOG_ERRORS in the code ?

## Spudz76 | 2021-05-21T11:21:40+00:00
put `export CL_LOG_ERRORS="stderr"` into shell, then from same shell run xmrig

## ganzocrypt | 2021-05-21T11:23:47+00:00
here 
![Screen Shot 2021-05-21 at 1 23 19 PM](https://user-images.githubusercontent.com/42419950/119129841-bc4c0b80-ba37-11eb-8d35-d6c38edb00fb.png)


## brianmcfadden | 2021-05-22T23:19:24+00:00
Hey there,

Firstly, I don't think the atomic_inc() from the issue in xmrig-amd wouldn't be the same issue here, as this issue has something to do with amd_bitalign.  Curious note that there are 2 different versions of xmr_amd_bitalign defined in src/backend/opencl/cl/cn/wolf-skein.cl.  Maybe you noticed that already..

Second, I see now that it wasn't Spudz76-dev-fixCLKawPowPlatformHandling, it was your fork with branch dev-fixAppleOpenCL.

I'm building the code from dev-fixAppleOpenCL and it builds OK, and the OpenCL code is building fine for me inside the GPU, but my GPU is too small to do anything useful, I'm afraid.

 * OPENCL GPU   #1 n/a AMD Radeon Pro 455 Compute Engine 855 MHz cu:12 mem:512/2048 MB

So that's a whopping 2GB of memory on the card, and unfortunately it seems like we need 3G to run for kawpow:

[2021-05-22 19:11:21.565]  opencl   use profile  kawpow  (1 thread) scratchpad 32 KB
|  # | GPU |  BUS ID | INTENSITY | WSIZE | MEMORY | NAME
|  0 |   1 |     n/a |   6291456 |   256 |   2949 | AMD Radeon Pro 455 Compute Engine
[2021-05-22 19:11:21.566]  opencl   GPU #1 compiling...
[2021-05-22 19:11:21.567]  opencl   GPU #1 compilation completed (1 ms)
[2021-05-22 19:11:21.567]  opencl   READY threads 1/1 (2 ms)
[2021-05-22 19:11:21.571]  opencl   KawPow program for period 588563 compiled (4ms)
[2021-05-22 19:11:21.571]  opencl   error CL_INVALID_BUFFER_SIZE when calling clCreateBuffer with buffer size 3053453312
[2021-05-22 19:11:21.571]  opencl   thread #0 failed with error CL_INVALID_BUFFER_SIZE

If that's accurate, I then my Radeon 455 won't work, but the ganzocrypt's Radeon 580 should (8GB).  Sorry, I can't be of more help here, but on the plus side that branch should compile OK.


## Sammed98 | 2021-05-23T03:30:32+00:00
@ganzocrypt Can you check the branch https://github.com/Spudz76/xmrig/tree/dev-fixAppleOpenCL as mentioned by @brianmcfadden? Kawpow has 3 GB GPU minimum requirement and I think you have 8 GB.



## Spudz76 | 2021-05-23T03:35:20+00:00
@brianmcfadden thanks for the test, could you test out some other algos everything except RandomX or KawPow families should work with 2GB...

## ganzocrypt | 2021-05-23T09:00:10+00:00
@sammed-ai  yes got 580 8gb, I am testing cn/upx2 which before was cn-extremelite algo. I can try to test for kawpow, which coin should I test on? do you have a config that I can use so we are on the same page?

@brianmcfadden could you try to cn/upx2 algo and see it mines?

## Sammed98 | 2021-05-23T10:31:32+00:00
@ganzocrypt Can you test for Kawpow algorithm on any coin? I don't think the coin matters. The only thing matters would be the algorithm and the xmrig application. 

The config on my very first issue description should work find. It has cpu set to false, opencl set to try, algo as kawpow. You need to put the appropriate pool address , and user. I used placeholder strings while creating the issue.

## ganzocrypt | 2021-05-23T12:09:06+00:00
Hey, it works ! But the screen gets very sluggish !

![Screen Shot 2021-05-23 at 2 08 32 PM](https://user-images.githubusercontent.com/42419950/119259859-80987980-bbd0-11eb-8b2d-d607da6a641f.png)



## ganzocrypt | 2021-05-23T12:22:50+00:00
I reduce the intensity to 1024 and mining ETH and seems fine, using kapow on https://unmineable.com/! GPU load is at 70% screen is ok, can work !
So the issue not compiling was for the other algo upx2.

Not sure if you can answer, which of the supported algo on xmrig would closer to ethah? I can now mine ETH ! :) and use the CPU to mine the other coin since I have a dual Xeon !

## Sammed98 | 2021-05-23T12:33:24+00:00
Oh. Cool. Could you somehow send the compiled application/zip file here? As a MEGA link or drive link. Which I can download, modify the config file and execute. 

## ganzocrypt | 2021-05-23T12:37:07+00:00
Not sure if it will work since I compiled on my machine, let me know. [xmrig.zip](https://github.com/xmrig/xmrig/files/6528068/xmrig.zip)



## ganzocrypt | 2021-05-23T12:38:23+00:00

[configKAPOW.json.zip](https://github.com/xmrig/xmrig/files/6528070/configKAPOW.json.zip)


## Spudz76 | 2021-05-23T12:49:53+00:00
Good stuff.  I will check into the UPX2 problem, maybe it also crashes on other platforms with more generic opencl1.2 stacks - or even Linux+AMD because I'm not sure I ever tested it.

## Spudz76 | 2021-05-23T12:51:16+00:00
Although I think it did work on Apple M1 + M1 GPU when I was testing this patch for that... hmm

## ganzocrypt | 2021-05-23T13:00:35+00:00
@Sammed98 did it run ok?

@Spudz76 looks like the upx2 might be very particular.

Also do you know if kapow is core or memory intensive for the GPU ?

## Sammed98 | 2021-05-23T13:16:43+00:00
Hey, I got this error when I ran the zip 
"dyld: Library not loaded: /Users/biskero/Developer/homebrew/opt/hwloc/lib/libhwloc.15.dylib"

And I checked the JSON file and there were a lot of modifications. Could you point me at the modifications which are concerned with GPU execution with kawpow algorithm on AMD chip (OpenCL)?

## ganzocrypt | 2021-05-23T13:25:29+00:00
I compiled with dynamic libs, so it won't work on your machine.
About the config, just enabled the OpenCL, add the platform "Apple" set the "intensity": 1024 (else screen freeze! Also I have 2 Xeon so you might find differences there since I have 20 cores/40 threads but that should not affect you if you do not use CPU mining.
Everything else is the same as normal configuration. 

## Sammed98 | 2021-05-23T13:39:19+00:00
So, where can I find the steps to compile on my system?  Did you use the Basic build steps or advanced build steps?

And what is the "intensity" variable? How much MB of GPU to use for mining?

## ganzocrypt | 2021-05-23T13:42:54+00:00
here, I use basic, https://xmrig.com/docs/miner/build/macos
I set the intensity to 1024, is like how much compute you want the card to perform. I would leave it at 1024.
I do not thing you can set the MB, the DAG takes 2.9Mb

## Sammed98 | 2021-05-23T13:59:40+00:00
I got this error somewhere in between when I compiled the [dev-fixAppleOpenCL](https://github.com/Spudz76/xmrig/tree/dev-fixAppleOpenCL) branch. 

<img width="1700" alt="Screenshot 2021-05-23 at 7 26 16 PM" src="https://user-images.githubusercontent.com/25957319/119263536-0c27ff80-bbfd-11eb-9593-9ccdc8f0af9d.png">

And this error when I run the xmrig application from the build folder.

<img width="857" alt="Screenshot 2021-05-23 at 7 26 42 PM" src="https://user-images.githubusercontent.com/25957319/119263545-1b0eb200-bbfd-11eb-9f20-f5ed1dabb117.png">

Should I move the xmrig application file somewhere else and execute it?

I did not use the alternative step 4 since I have an Intel Mac and not a M1 Mac. 

## ganzocrypt | 2021-05-23T14:07:06+00:00
the warning is nothing.
also it looks like your config is not right, use the one I gave you and change only your address

## ganzocrypt | 2021-05-23T14:09:07+00:00
can you try this xmrig, it should have static libs 
[xmrig.zip](https://github.com/xmrig/xmrig/files/6528223/xmrig.zip)


## Sammed98 | 2021-05-23T14:28:27+00:00
I tried with your config file and it started the mining process. Thank you. Incase I get any errors of some sort I will also check the static libs. 

I think you can create a pull request with the modified code. 

I have a Intel(R) UHD Graphics 630 GPU too. Will this code work on this too?

## ganzocrypt | 2021-05-23T14:38:13+00:00
If you have time please test the last xmrig I sent you so I know the libs are statics and work on other mac, thx

btw you can use xmrig to mine on 2 different coins like one with CPU and the other with GPU.

about the intel GPU not sure, you just need to figure out the index

## Spudz76 | 2021-05-24T00:11:38+00:00
@Sammed98 Your Intel GPU should be `index: 0` while the AMD is `index: 1`

If you edit the config.json and delete every algo-definition under the opencl section then run again it should set up to run on both... like two entries under each algo one for each index.

Or, mass replace index1 for index0 but the thread/block sizing is probably wrong then and may still not work.

Or if the config from ganzo already had index:0 then it's already running on the Intel lol.

## Sammed98 | 2021-05-24T02:16:47+00:00
I don't think I can mine on Intel because it has a VRAM of 1536 MB. But I still get this error when I run xmrig only on AMD.

"error CL_INVALID_VALUE when calling clGetProgramInfo"

I googled about this error and found that it indicates that the VRAM requirement is not met. Is this correct?
Even, if this is correct I have a AMD with 4 GB of VRAM and as far as I know kawpow only requires 3GB VRAM. How should I solve this issue? 


## Spudz76 | 2021-05-24T02:53:01+00:00
Yes I have run KawPow on 4GB but through CUDA maybe there is some alignment thing with OpenCL allocations where it needs slack space due to some spec rules (and maybe AMD-CL allows/ignores).  I'll see if it works via nvidiaCL this same patch seems to have helped those too.  This patch should always force OpenCL 1.2 compatibility on all Apples so it shouldn't be a bad clGetProgamInfo call but I will check for AppleCL quirks.  It may be a sloppy spot I didn't dig deeply into the algo code yet mainly got the detection and compilation (mostly) working which is exposing some of the incompatibilities deeper inside the code.

It may also be that Apple won't hand out a full >2GB allocation but would do it if done in smaller chunks.  Not sure if the KawPow code has that workaround in it (try full alloc -> catch the fail -> try smaller allocations and aggregate them instead -> fail if both don't work).  And if Apple always caps allocations then just always use the aggregation mode on that platform.

I forgot you were running an algo that would need more than the Intel has.  But it should work with most other algos (not RandomX it also needs a 2336MB dataset).

## Spudz76 | 2021-05-24T03:47:45+00:00
There was only one place where `clGetProgramInfo` was called and it didn't need to be there unless debugging.  Readjusted some `#if defined()` logic so the debug code is never compiled/called when it is not needed.  There should be no calls to `clGetProgramInfo` now if you can get a recompile from my fixAppleOpenCL branch.  I decided since KawPow does work on M1 now it must not be an Apple-vs-allocations problem, unless there is some extra limitation with AMD for some reason.

## ganzocrypt | 2021-05-24T08:57:00+00:00
@Sammed98 did you had a chance to test the xmrig that I posted, so that I know the build works on other macos machine? thx

## ef651100 | 2021-05-25T02:30:24+00:00
Hello, I stumbled upon the fixAppleOpenCL branch to fix this exact same issue with XMRig. I still experienced the same issue after building, so I have looked at the code. I made a small adjustment to /src/backend/opencl/wrappers/OclDevice.cpp to add another string for my iMac which uses the Radeon Pro 580:

`
            if (name.contains("Pro 580")) {                return OclDevice::Polaris;            }`

And this compiled and no issues on run!
<img width="769" alt="Screen Shot 2021-05-24 at 7 29 12 PM" src="https://user-images.githubusercontent.com/47389897/119430914-748ee380-bcc6-11eb-92cf-7966c46c3645.png">



## Sammed98 | 2021-05-25T04:11:31+00:00
@ganzocrypt I already checked the static ones. It worked. I mentioned this before. 

@Spudz76 can you cross check what @ef651100 has modified in the code?

## ganzocrypt | 2021-05-25T08:34:23+00:00
@Sammed98 ok great thx!
@ef651100 we did not have problems mining KaPow, it was for UPX2 that was not working. Btw I see that you are running with very high intensity, does it affects your screen or your setup does't care?

## ganzocrypt | 2021-05-25T10:17:12+00:00
@Sammed98 I made the change **if (name.contains("Pro 580")) { return OclDevice::Polaris; }** from @ef651100 
Can you test it on your machine since it might affects you since the device it shows when you execute xmrig is "Pro 580" 
[xmrig.zip](https://github.com/xmrig/xmrig/files/6538462/xmrig.zip)
 

## Spudz76 | 2021-05-25T11:37:47+00:00
But that one says "Pro 5300M" which I had already put in the code earlier.

Problem is Apple doesn't pass through any "gfx#" or anything that normally maps to a Chip Type.  Only the product names which really sucks.

## Spudz76 | 2021-05-25T12:12:49+00:00
Added patch which includes every Apple AMD GPU [listed here](https://www.techpowerup.com/gpu-specs/?generation=Radeon+Pro+Mac&sort=generation)

The 580 is actually an Ellesmere not Polaris.

## d9beuD | 2021-05-25T12:55:00+00:00
@Spudz76 in the list you provided, aren't some 6XXX gen missing? There isn't Mac with RDNA2 GPU yet, but drivers are included in macOS. And people like me building their hackintosh already installed GPUs like 6900xt

## ganzocrypt | 2021-05-25T13:24:36+00:00
@d9beuD can you try the last xmrig that I posted to see if it works on your hackintosh? I have too an hackintosh with dual xeon and rx580, just wanted to verify that everything works fine on other systems. thx

## empiresun1 | 2021-05-25T17:39:50+00:00
So i had pretty much the same issues... using your compiled zip and config i was able to get my Vega64 egpu to finally start mining but i still have 2 issues

First even though its now using the gpu it doesnt seem to be submitting and the work isnt being accepted for some reason? and second it looks like im only using 1/4 of my GPU to mine Kawpow and my hashrate seems pretty low? and ideas as to why? 
![Screen Shot 2021-05-25 at 1 37 27 PM](https://user-images.githubusercontent.com/84761243/119543435-abb0d380-bd5e-11eb-9652-3e33451ba4b1.png)


## empiresun1 | 2021-05-25T17:41:40+00:00
oh and another side note: it seems like my hashrate is pretty low? only about .64 ... shouldnt it be higher? 

## ganzocrypt | 2021-05-25T17:50:51+00:00
ok I had the same issue, if your hashrate is low, the pool does not record it or it takes very long time. You are mining at ~ 600k h/s. So on my RX 580 I found the following settings to work and I have 6 Mh/s and on the pool oscillate between 6 and 12 Mh/s, GPU load is at 85%. I run my screen too, so I do not want to go over the intensity I set since screen will freeze and relogin!
Try the following settings in your KaPow config
-  "intensity": 36864
-   "worksize": 256

Now since you have a Vega you might want to increase intensity when everything is working. I did that by adding 1024 or 2048 or 4096 to the previous intensity, so that I did not load the GPU too much, check with Acitivity Monitor your xmrig GPU usage.
Let me know if it works, and great that the xmrig that I compiled works.


## empiresun1 | 2021-05-25T17:54:07+00:00
> ok I had the same issue, if your hashrate is low, the pool does not record it or it takes very long time. You are mining at ~ 600k h/s. So on my RX 580 I found the following settings to work and I have 6 Mh/s and on the pool oscillate between 6 and 12 Mh/s, GPU load is at 85%. I run my screen too, so I do not want to go over the intensity I set since screen will freeze and relogin!
> Try the following settings in your KaPow config
> 
> * "intensity": 36864
> * "worksize": 256
> 
> Now since you have a Vega you might want to increase intensity when everything is working. I did that by adding 1024 or 2048 or 4096 to the previous intensity, so that I did not load the GPU too much, check with Acitivity Monitor your xmrig GPU usage.
> Let me know if it works, and great that the xmrig that I compiled works.

I'll totally try these changes... but any idea why its not being accepted on unminable? i ran it as a test for about 30 mins with 0 results

## ganzocrypt | 2021-05-25T17:55:27+00:00
your hashrate at 600kh/s might be too low, try the new changes and see if it works

## empiresun1 | 2021-05-25T18:12:05+00:00
so ran it for about 10 mins ... GPU usage hovering around 80% ... hash rate came up to about 5.5KH, but its still not submitting acceptance? 
![Screen Shot 2021-05-25 at 2 10 09 PM](https://user-images.githubusercontent.com/84761243/119547466-25e35700-bd63-11eb-97ac-ff84efbc830f.png)

![Screen Shot 2021-05-25 at 2 10 28 PM](https://user-images.githubusercontent.com/84761243/119547500-2d0a6500-bd63-11eb-80d9-b8f961307980.png)



## ganzocrypt | 2021-05-25T18:16:45+00:00
first time it took sometime, but it should work.

## brianmcfadden | 2021-05-25T18:18:08+00:00
I see the difficulty in your log is set at 4295M, which seems excessively high.  If that's what the pool is returning to you, I'd try another pool. If there's a config setting for that, I'd try lowering it by alot.

## empiresun1 | 2021-05-25T18:18:18+00:00
ok, ill run it for a few hours and see what it does... also does it matter that im also randomx mining the same coin to the same address? maybe thats the issue? 

## empiresun1 | 2021-05-25T18:22:17+00:00
> I see the difficulty in your log is set at 4295M, which seems excessively high. If that's what the pool is returning to you, I'd try another pool. If there's a config setting for that, I'd try lowering it by alot.

im using the unminable pool for BTT, not sure what a better option would be

## peme14k | 2021-05-25T18:26:53+00:00
กำหนดสิ่งอื่นแล้วลดลงไห้พอดีขอบคุณ

## empiresun1 | 2021-05-25T18:28:12+00:00
> first time it took sometime, but it should work.

ok so i shut down my CPU miner xmrig and restarted the GPU miner and its now accepting! is there anyway to run both GPU on KAWPOW and CPU on RandomX at the same time for the samecoin? 

## ganzocrypt | 2021-05-25T18:33:42+00:00
ok cool ! yes just enable CPU mine to true. Or you can actually run 2  instances of xmrig, one for CPU and one for GPUs on 2 different coins using 2 different configs: xmrig -c config.json

In any case you can run CPU and GPU on the same coin, just go to the CPU section and set it to true:
"cpu": {
        "enabled": true

also for the algo you want to mine you need to set the number of threads, so you have 4 cores/ 8 threads, which means you need to set [0] to [7] in the second []

"cn": [
            [1, 0],
....
.... [1, 7]

if you want less threads, just remove the ones you do not want.

## empiresun1 | 2021-05-25T18:37:07+00:00
if i enable CPU on just the one instance of Xmrig wont it just try to cpu mine KAWPOW? running two instances would be better but from my previous issue IDK if it will stop one or both of them from accepting?

## ganzocrypt | 2021-05-25T18:37:21+00:00
if you mine the same coin the algo must be the same, else you need two instances wit 2 different algos.



## empiresun1 | 2021-05-25T18:41:30+00:00
> if you mine the same coin the also must be the same, else you need two instances wit 2 different algos.

thats what i thought... ill try it with 2 instances and see what happens! oh and for changing my threads: 

"cn": [
            [1, 0],
            [1, 2],
            [1, 4],
            [1, 6]

above is my current config file ... so would i change it to: 

"cn": [
            [1, 0],
            [1, 7],
            [1, 4],
            [1, 6]

?

## empiresun1 | 2021-05-25T18:46:04+00:00
sorry for all the questions lol .... im very new to all this and im trying to learn 

## ef651100 | 2021-05-25T19:00:51+00:00
I had good performance with intensity 51200 and work size 256 with GPU utilization around 90% which gives me around 6MH/s. The ridiculous number on my screenshot was auto-generated... and yes, my computer was quite unusable...



## empiresun1 | 2021-05-25T19:04:00+00:00
> I had good performance with intensity 51200 and work size 256 with GPU utilization around 90% which gives me around 6MH/s. The ridiculous number on my screenshot was auto-generated... and yes, my computer was quite unusable...

happy that i have my EGPU since i can use that as a standalone to mine when i dont need it and use my internal gpu for running my computer ... currently averaging 10 MH/S at about 80% gpu load


## ganzocrypt | 2021-05-25T19:07:05+00:00
no problem, sorry I was eating ! :)
so if you want to run 4 threads those settings are correct.
"cn": [
[1, 0],
[1, 1],
[1, 2],
[1, 3]
this runs the first 4 threads!

by the  way does the xmrig that I uploaded still works?
I am asking because I was not sure if it would work on other macs!

I will give you an example: I ran one xmrig instance for CPU for UPX2 and one instance for GPU with KaPow so I can mine 2 coins with 2 different algos. Or you can run one instance with CPU and GPU but the algo needs to be the same because you cannot split the pools on the config!

## empiresun1 | 2021-05-25T19:11:02+00:00
> no problem, sorry I was eating ! :)
> so if you want to run 4 threads those settings are correct.
> "cn": [
> [1, 0],
> [1, 1],
> [1, 2],
> [1, 3]
> this runs the first 4 threads!
> 
> by the way does the xmrig that I uploaded still works?
> I am asking because I was not sure if it would work on other macs!
> 
> I will give you an example: I ran one xmrig instance for CPU for UPX2 and one instance for GPU with KaPow so I can mine 2 coins with 2 different algos. Or you can run one instance with CPU and GPU but the algo needs to be the same because you cannot split the pools on the config!

no worries! we all gotta eat ... my wife is making me a burrito now lol .. and yea im using your build for this on my macbook with my egpu and its working great... bouncing between 7-10 mh/s :) 

## ganzocrypt | 2021-05-25T19:11:44+00:00
with my settings I get around 6.7 Mh/s on the xmrig and at the pool varies between 6 and 13 Mh/s!

## empiresun1 | 2021-05-25T19:12:14+00:00
and let's say i wanna run 6 threads instead of my 4... .still want 2 threads to have some usability what would that config be ... im trying to understand how the config file works  

## ganzocrypt | 2021-05-25T19:13:15+00:00
"cn": [
[1, 0],
[1, 1],
[1, 2],
[1, 3],
[1,4],
[1,5]

is zero based the numbering, or pick the thread that you want

## empiresun1 | 2021-05-25T19:19:12+00:00
so i changed the config for that but its still only loading 4 threads for randomx. ideas? 
![Screen Shot 2021-05-25 at 3 17 31 PM](https://user-images.githubusercontent.com/84761243/119556050-8c20a780-bd6c-11eb-8a43-1ae2983e968b.png)
![Screen Shot 2021-05-25 at 3 17 45 PM](https://user-images.githubusercontent.com/84761243/119556055-8dea6b00-bd6c-11eb-94da-1d9aedf0fe8e.png)



## ganzocrypt | 2021-05-25T19:21:52+00:00
RandomX on the algo you need to set:
"pools": [
        {
            "algo": "rx/0",

and for the CPU is "rx": [0, 1, 2, 3, 4, 5]


## empiresun1 | 2021-05-25T19:26:17+00:00
> RandomX on the algo you need to set:
> "pools": [
> {
> "algo": "rx/0",
> 
> and for the CPU is "rx": [0, 1, 2, 3, 4, 5]

cool ill try that... i can keep my "cn" settings the same? 

## ganzocrypt | 2021-05-25T19:27:11+00:00
if you set the "algo": "rx/0", everything else is ignored

## empiresun1 | 2021-05-25T19:28:18+00:00
> if you set the "algo": "rx/0", everything else is ignored

yup! running 6 threads now! that should increase my hashrate right? 

## ganzocrypt | 2021-05-25T19:28:28+00:00
basically the steps are:

1. Enabled CPU mining
2. set the # of thread for the algo you want to mine
3. set the algo in the pool section you want to mine

## ganzocrypt | 2021-05-25T19:29:39+00:00
by the way with eGPU you have? I mean the box

## empiresun1 | 2021-05-25T19:30:26+00:00
yup that part i now understand ... every algo has its own parameters to what it will do based on the config


> by the way with eGPU you have? I mean the box

Razer Core ... i was about to ask if it will be better to take the GPU out of the box to allow better cooling lol 

## ganzocrypt | 2021-05-25T19:31:31+00:00
better cooling is always good ! :)

## empiresun1 | 2021-05-25T19:32:00+00:00
for sure .. especially since i live in a warm climate and we dont use AC lol 

## empiresun1 | 2021-05-25T19:32:43+00:00
ill run the rigs and report back with info! let me know if i can do anything to help develop and refine this more for every one! :) 


## ganzocrypt | 2021-05-25T19:34:18+00:00
will do more testing too and recompile it tomorrow, might do a fork and create some binaries since compile on mac is a freaking nightmare !

## empiresun1 | 2021-05-25T19:35:51+00:00
Kick ass! ill happily be your crash test dummy for this lol.. btw idk why but it seems like running 6 threads as opposed to 4 has dropped my hashrate somewhat... running 4 i would hash about 11-1200 h/s and now im around 800 ish
![Screen Shot 2021-05-25 at 3 34 10 PM](https://user-images.githubusercontent.com/84761243/119558002-e15db880-bd6e-11eb-90b9-b293b4662a2c.png)
800? 

## ganzocrypt | 2021-05-25T19:37:25+00:00
mac misteries ! my guess is CPU throttling to keep it alive ! run 4 ! 

## Spudz76 | 2021-05-26T03:45:58+00:00
@empiresun1 Your CPU had 8MB of cache, optimal is 2MB per thread, therefore 4 threads is correct and fastest.  (as you found)

## Sammed98 | 2021-05-26T04:02:23+00:00
> Added patch which includes every Apple AMD GPU [listed here](https://www.techpowerup.com/gpu-specs/?generation=Radeon+Pro+Mac&sort=generation)
> 
> The 580 is actually an Ellesmere not Polaris.

@ganzocrypt Your last zip still gave the error on my system. Can you compile the above mentioned patch with static files and link the zip here. I will test it out. 

## Sammed98 | 2021-05-26T04:15:13+00:00
<img width="847" alt="Screenshot 2021-05-26 at 9 43 32 AM" src="https://user-images.githubusercontent.com/25957319/119601467-de160b80-be06-11eb-893a-9c3975968851.png">

@ganzocrypt with your settings I also am not getting any acceptance. Though the rate is pretty good. Any chances you want to suggest?

## ganzocrypt | 2021-05-26T07:47:59+00:00
will recompile it today.
about the other issue, try to restart the xmrig and see, but from what I tested unminenable wants higher hashrate since the do the conversion of coins. Check your GPU % and see if you can increase the intensity to get more hashrate.

## ganzocrypt | 2021-05-26T09:50:20+00:00
I created a branch for the [macos fork ](https://github.com/ganzocrypt/xmrig-macos)

**All work credit for adding AMD support goes to @Spudz76.**

Please test the [release](https://github.com/ganzocrypt/xmrig-macos/releases/tag/v6.13.0-dev-macos) and if there are any issues for the xmrig binary post them on the [issue](https://github.com/ganzocrypt/xmrig-macos/issues) section.

## ganzocrypt | 2021-05-26T10:15:36+00:00
@Spudz76 I found an issue while compiling the changes you did.
In the file [OclDevice.h](https://github.com/Spudz76/xmrig/blob/dev-fixAppleOpenCL/src/backend/opencl/wrappers/OclDevice.h)
is missing **Ellesmere,**  in the enum, which was added to the OclDevice.cpp.


## ganzocrypt | 2021-05-26T10:18:19+00:00
@Sammed98  @empiresun1 @ef651100 @brianmcfadden could you please test the [release](https://github.com/ganzocrypt/xmrig-macos/releases/tag/v6.13.0-dev-macos) to see if everything is working? thx

## SChernykh | 2021-05-26T12:23:14+00:00
@Spudz76 your branch is missing `OclDevice::Ellesmere` in OclDevice.h. Can you fix it and make a PR? I don't have any Mac device to test it though otherwise I'd do it myself.

## ganzocrypt | 2021-05-26T12:24:47+00:00
@SChernykh I already mentioned to him 2 post above and tested on my mac, it compiles and work ok

## Spudz76 | 2021-05-26T12:42:25+00:00
Yeah I whipped that up without any compilation testing right after I had woken up and was hurrying to fit in a bit of patching.  Sort of assumed Elle's would already be in there (but still managed to add Navi21 without noticing lack of Ellesmere).

Technically I have no Apple device either, it's just High Sierra running on a qemu VM with no actual GPUs.  It does compile-test pretty good, but anything more than that I can't verify without the help of everyone in here.

I'm still awaiting someone to test the CUDA support lol.

## Spudz76 | 2021-05-26T13:21:47+00:00
Shoved a fix for that, and followed Polaris around and stuck Ellesmere everywhere it showed up (should act as full alias of Polaris now, since it pretty much is anyway)

```
/Library/Developer/CommandLineTools/usr/bin/strip xmrig
[100%] Built target xmrig
/Applications/CMake.app/Contents/bin/cmake -E cmake_progress_start /Users/user/src/xmrig/build/opencl/CMakeFiles 0
users-iMac-Pro:opencl user$ 
```
Compiled okay, tested it this time :)

## Spudz76 | 2021-05-26T13:32:04+00:00
@Sammed98 For some reason unMineable likes to hand out jobs with difficulty 4295M which is very high (matching hashrate of ~143MH/s) therefore it would be rare to ever see an acceptance with 3.56MH/s peak.

I saw they allow the `+1234` suffix format for requesting a different fixed diff on their Monero pool but apparently not a feature with their KawPow pool.  Not sure how anyone ever catches results with the diff they are sending.

## ganzocrypt | 2021-05-26T13:35:34+00:00
@Spudz76 I asked them waiting for an answer !
They have their own miner and you can set the [Low/High](https://support.unmineable.com/issues-and-fixes/how-to-fix-advanced-settings-not-saving-correctly/), not sure it works for any algo as you mentined.

## Spudz76 | 2021-05-26T13:38:48+00:00
Amazing there exists any pool that still doesn't do autodiff in 2021

## ef651100 | 2021-05-26T14:19:51+00:00
> @Sammed98 @empiresun1 @ef651100 @brianmcfadden could you please test the [release](https://github.com/ganzocrypt/xmrig-macos/releases/tag/v6.13.0-dev-macos) to see if everything is working? thx

No issues in this release!

<img width="835" alt="Screen Shot 2021-05-26 at 7 18 40 AM" src="https://user-images.githubusercontent.com/47389897/119676358-a735fa80-bdf2-11eb-82bd-19ec257c4408.png">


## ganzocrypt | 2021-05-26T14:27:42+00:00
cool ! I am sure something will come up, let me know ! :)

btw on rx you can set the difficulty by appending +50000 to the worker name, where the number is the difficulty.
So I put .Xeon+50000 and seems to accept more shares.
But it looks like it does not work for KawPow.

## Sammed98 | 2021-05-26T14:44:45+00:00
@ef651100 which coin are you mining for which you are getting acceptance? 

@ganzocrypt unfortunately I dowloaded the latest release from your repository and it still gives the error "error CL_INVALID_VALUE when calling clGetProgramInfo". 

## Sammed98 | 2021-05-26T14:46:32+00:00
@Spudz76 do you know any coin on unmineable which gives payout frequently and not wait upto a long time till the mined coins reach a high number? Or any other pool which does this?

## ganzocrypt | 2021-05-26T14:46:38+00:00
@Sammed98 will look into it, does it mine?

## Sammed98 | 2021-05-26T14:50:53+00:00
> @Sammed98 will look into it, does it mine?

I have just started it. Will get back to you in an hour. 

## Spudz76 | 2021-05-26T15:07:07+00:00
@Sammed98 see how @ef651100 is running KawPow on nicehash pool which gave a diff of 306M which is small enough to actually hit results.  Essentially unless unMineable adjusts their diff or supports the `+1234` customized diff some day, they are useless for KawPow (without a proxy and enough devices for a 143MH rate / subdivide their huge diff to something workable).

So some other KawPow pool that has autodiff (or at least lower than ridiculous diff) would have your miner showing results, just like @ef651100 latest report.

Users have been complaining about unMineable with their Eth pool because they set that diff to 4G or something stupid, too.

## Spudz76 | 2021-05-26T15:12:32+00:00
@Sammed98 MoneroOcean supports KawPow and pays out XMR for it and is fully autodiff like a real pool.  Depends on which coin you want to end up with, whether actual RVN or if you're trying to cross-mine KawPow to DOGE or something, or if it doesn't matter what coin if it profits.

## ef651100 | 2021-05-26T15:14:05+00:00
> @ef651100 which coin are you mining for which you are getting acceptance?

I mine Kawpow on Nicehash. Ran it for about an hour resulted in 192 accepted. I'll probably try another pool on another Mac later.

## peme14k | 2021-05-26T15:17:49+00:00
DCR

## ganzocrypt | 2021-05-26T16:09:15+00:00
Trying to find a good pool too!

## Sammed98 | 2021-05-26T16:10:40+00:00
> > @ef651100 which coin are you mining for which you are getting acceptance?
> 
> I mine Kawpow on Nicehash. Ran it for about an hour resulted in 192 accepted. I'll probably try another pool on another Mac later.

Which coin?

## brianmcfadden | 2021-05-26T16:56:12+00:00
@Spudz76 I recently tried the your branch mining with Cryptonight/R and it had issues I've seen before, with Skein in cryptonight.cl, and with m_cn1->enquque in OclCnRunner.cpp. They're different issues than Kawpow, though.  The seg fault is being tracked in issue 2397, and I haven't made an issue for Skein in the xmrig repo yet.

## Sammed98 | 2021-05-26T17:27:40+00:00
@Spudz76 I tried MoneroOcean it gave a lot of accepts but I did not find anywhere where I can withdraw the amount i have mined. The website also was not showing how much monero I have mined. It only shows the number of shares. 

Can you guide me how the payout worked on MoneroOcean works?

## Spudz76 | 2021-05-26T19:47:23+00:00
It takes a short while for new mining to show up, but if you have put your wallet address into the website and it shows your miner status there is a place there where it clearly says (top right) how much is stacked in your balance.  Then the miner status and hashrates are all in XMR-equivalent hashes (pay rate) unless you select "raw".  There can be some amount of lag between results and payments since there is exchange transaction lag and they do not pre-pay, only distribute rewards around when all exchange transactions are completed and confirmed.  The pay rate will move with the differential value of RVN->XMR since the effective "XMR Hashrate" is different when RVN is worth more or less XMR.

## empiresun1 | 2021-05-27T15:48:46+00:00
> @Sammed98 @empiresun1 @ef651100 @brianmcfadden could you please test the [release](https://github.com/ganzocrypt/xmrig-macos/releases/tag/v6.13.0-dev-macos) to see if everything is working? thx

Everything is working so far! gonna run it for a few hours and report if any errors. The last build would sometimes crash after like 12 hours lol 

## ganzocrypt | 2021-05-27T15:51:12+00:00
ok let me check if I can make a clean recompile since there are couple of ways to build the libraries. Will repost the binary as soon as done

## empiresun1 | 2021-05-27T15:51:34+00:00
> @Sammed98 MoneroOcean supports KawPow and pays out XMR for it and is fully autodiff like a real pool. Depends on which coin you want to end up with, whether actual RVN or if you're trying to cross-mine KawPow to DOGE or something, or if it doesn't matter what coin if it profits.

cross-mining using Kawpow on unminable.com  seems saturated right now . Difficulty is like 4295m? thats nuts... im just waiting to hit my cashout min at this point. Are there any better cross algo pools with actual manageable diff? 

## ganzocrypt | 2021-05-27T15:52:38+00:00
for cpu you can set the diff but for kawpow, you can't. yeah looking for other pool too

## empiresun1 | 2021-05-27T15:54:28+00:00
> > @Sammed98 @empiresun1 @ef651100 @brianmcfadden could you please test the [release](https://github.com/ganzocrypt/xmrig-macos/releases/tag/v6.13.0-dev-macos) to see if everything is working? thx
> 
> Everything is working so far! gonna run it for a few hours and report if any errors. The last build would sometimes crash after like 12 hours lol

cool! also let me know if you can also do an updated config... i noticed something when starting the build, im pretty sure it was on the last one too:
![Screen Shot 2021-05-27 at 11 53 04 AM](https://user-images.githubusercontent.com/84761243/119858062-1cccc400-bee2-11eb-83db-4b1e40353ce4.png)

is this as designed to only use 1/4 of my gpu memory? 

P.S. ugh ... so stupid to have the difficulty so high on a coin that should be so easy to mine ... ( BTT) 



## ganzocrypt | 2021-05-27T15:57:05+00:00
you can append the diff right after your worker name like +40000, works only for rx

about the mem I think that's what the algo uses

## ganzocrypt | 2021-05-27T16:04:27+00:00
I recompile it, just get the zip. I had crashes too but I am pushing a lot since I am using the 2 Xeon CPUs too

## empiresun1 | 2021-05-27T16:07:37+00:00
> I recompile it, just get the zip. I had crashes too but I am pushing a lot since I am using the 2 Xeon CPUs too

yea i got the new zip! thats what i started running, so far so good!. seems to be more regular in accepting the blocks. and let me know if you find a decent pool... im so done with unminable, at least till i can afford an Asic lol

P.S... currently mining about 10MH/s with the new compile! 
![Screen Shot 2021-05-27 at 12 09 00 PM](https://user-images.githubusercontent.com/84761243/119860521-67e7d680-bee4-11eb-9652-3d1e14d4856e.png)
:-D

## brianmcfadden | 2021-05-27T22:21:25+00:00
Since we have a bunch of people testing on Mac GPUs, can I ask some of you to do me a favor?  I'm trying to see if an error in Skein is an issue for me alone or other people as well.  Since the issue could be my tiny little 2GB GPU, I'm interested to see if you guys with higher memory GPUs see the same issue.  The problem is with the Cryptonight/R specifically, and I've been testing with Lethean. (I wouldn't actually recommend mining Lethean, but it's a good test for the GPU.)

The test that I'd like to see uses these entries in a config -- in the "opencl" section, make sure that 
        "enabled": true,

and in the "cpu" section,
        "enabled": false,

and in the "pools" section;
            "algo": "cn/r",
and
            "url": "lthn.ss.dxpool.com:6622",

Also, I don't know if you need an address for the "user" section, but if you do, I'm using this as my test address:
            "user": "iz6CWkqcPVsbZtyJJecQ4kTosPJrgdxAHP63sG2hk8sfaU14LwvFBqwfBL9qGg6DwjhpFG9XZzY2jcRSYivKHDMt2NjcZtUrG",

I know they say you shouldn't put user account info into an issue, but this is an account that I don't have any keys for anymore and I only use for testing.  Feel free to use your own if you have a leathen address of your own.

I'm expecting 1 of 4 things to occur.  Either
1. it works and you get something "accepted" after a minute or so
2. "error CL_BUILD_PROGRAM_FAILURE when calling clBuildProgram" when compiling for the GPU
3. the GPU might compile OK, but you'll get a Segmentation fault shortly thereafter
4. GPU COMPUTE ERROR

Thanks.

## ganzocrypt | 2021-05-28T07:36:53+00:00
@brianmcfadden I can test it but in opencl is this the algo?
"cn": [
            {
                "index": 0,
                "intensity": 864,
                "worksize": 8,
                "strided_index": [1, 2],
                "threads": [-1, -1],
                "unroll": 8
            }
        ],


## Spudz76 | 2021-05-28T07:41:29+00:00
Here is a test from the M1 GPU so it's not a general Apple/OpenCL problem... because it works fine there.  Narrows it down to something with AMD cards... or your specific model maybe (which model does it say it is?)
```
 * ABOUT        XMRig/6.12.2-dev-mo3a clang/12.0.5
 * LIBS         libuv/1.41.0 OpenSSL/1.1.1j hwloc/2.4.1
 * HUGE PAGES   supported (16KB)
 * 1GB PAGES    unavailable
 * CPU          Apple M1 (1) 64-bit AES
                L2:16.0 MB L3:0.0 MB 8C/8T NUMA:1
 * MEMORY       7.1/8.0 GB (89%)
 * DONATE       0%
 * POOL #1      gulf.moneroocean.stream:20016 algo auto
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       #0 Apple/OpenCL 1.2 (Feb 28 2021 03:51:21)
 * OPENCL GPU   #0 n/a Apple M1 1000 MHz cu:8 mem:1024/5461 MB
[2021-05-28 03:36:38.608]  net      use pool gulf.moneroocean.stream:20016 TLSv1.2 18.210.126.40
[2021-05-28 03:36:38.608]  net      fingerprint (SHA-256): "239daadd5c7d0ac097376c7871f787738826eef1c024729eff870e473b970855"
[2021-05-28 03:36:38.608]  net      new job from gulf.moneroocean.stream:20016 diff 2057 algo cn/r height 967152
[2021-05-28 03:36:38.609]  opencl   use profile  cn/2  (1 thread) scratchpad 2048 KB
|  # | GPU |  BUS ID | INTENSITY | WSIZE | MEMORY | NAME
|  0 |   0 |     n/a |       384 |     8 |    768 | Apple M1
[2021-05-28 03:36:38.621]  opencl   READY threads 1/1 (12 ms)
[2021-05-28 03:37:07.079]  opencl   accepted (1/0) diff 2057 (262 ms)
[2021-05-28 03:37:16.394]  net      new job from gulf.moneroocean.stream:20016 diff 1633 algo cn/r height 967152
[2021-05-28 03:37:20.273]  opencl   accepted (2/0) diff 1633 (263 ms)
[2021-05-28 03:37:30.167]  opencl   accepted (3/0) diff 1633 (264 ms)
[2021-05-28 03:37:43.624]  miner    speed 10s/60s/15m 116.4 n/a n/a H/s max 116.8 H/s
| OPENCL # | AFFINITY | 10s  H/s | 60s  H/s | 15m  H/s |
|        0 |       -1 |    116.7 |    116.5 |      n/a | #0 n/a Apple M1
|        - |        - |    116.5 |      n/a |      n/a |
[2021-05-28 03:37:45.599]  miner    speed 10s/60s/15m 116.5 n/a n/a H/s max 116.8 H/s
[2021-05-28 03:37:48.446]  signal   Ctrl+C received, exiting
[2021-05-28 03:37:49.562]  opencl   stopped (1116 ms)
```

## Spudz76 | 2021-05-28T07:44:13+00:00
And here's one with that specific pool just to rule out some issue there...
```
[2021-05-28 03:43:16.202]  net      use pool lthn.ss.dxpool.com:6622  39.106.233.58
[2021-05-28 03:43:16.202]  net      new job from lthn.ss.dxpool.com:6622 diff 20000 algo cn/r height 967154
[2021-05-28 03:43:16.203]  opencl   use profile  cn/2  (1 thread) scratchpad 2048 KB
|  # | GPU |  BUS ID | INTENSITY | WSIZE | MEMORY | NAME
|  0 |   0 |     n/a |       384 |     8 |    768 | Apple M1
[2021-05-28 03:43:16.213]  opencl   READY threads 1/1 (11 ms)
[2021-05-28 03:43:30.210]  opencl   accepted (1/0) diff 20000 (259 ms)
```

## Spudz76 | 2021-05-28T07:45:52+00:00
@ganzocrypt no it should be the "cn/2" one but it can be dependent on if cn and cn/2 are the same for your GPU

See how it says which it's using on the line in my output above (`use profile  xxxx`)

## ganzocrypt | 2021-05-28T07:49:19+00:00
So cn/2 has 2 threads and cannot be run on RX580, tried with only one and got this:
![Screen Shot 2021-05-28 at 9 48 21 AM](https://user-images.githubusercontent.com/42419950/119949226-f4080580-bf99-11eb-8584-e15763d4a93c.png)


## Spudz76 | 2021-05-28T07:52:51+00:00
OK, confirmed an AMD problem, checking for why...

## Spudz76 | 2021-05-28T07:56:54+00:00
For kicks gave it a test on Linux+NvidiaCL which also (mostly) works.
```
|  # | GPU |  BUS ID | INTENSITY | WSIZE | MEMORY | NAME
|  0 |   0 | 01:00.0 |       176 |     8 |    352 | Quadro K1100M
[2021-05-28 01:54:50.835]  opencl   GPU #0 compiling...
[2021-05-28 01:54:50.885]  opencl   GPU #0 compilation completed (50 ms)
[2021-05-28 01:54:50.888]  opencl   READY threads 1/1 (54 ms)
[2021-05-28 01:55:12.956]  opencl   accepted (1/0) diff 277 (524 ms)
[2021-05-28 01:55:13.007]  opencl   accepted (2/0) diff 277 (575 ms)
```

## Spudz76 | 2021-05-28T16:24:01+00:00
I pushed a change with the only sort-of possibly confusing part maybe it will work now

## ganzocrypt | 2021-05-28T16:41:10+00:00
I recompiled it and got the same error:

![Screen Shot 2021-05-28 at 6 38 01 PM](https://user-images.githubusercontent.com/42419950/120015893-32c2ad80-bfe4-11eb-92fa-dae5ca0e42cd.png)


this is the cn/2 section that I use:

"cn/2": [
            {
                "index": 0,
                "intensity": 384,
                "worksize": 8,
                "strided_index": [2],
                "threads": [-1],
                "unroll": 8
            }
        ],

this is the pool:
"pools": [
        {
            "algo": "cn/2",
            "coin": "Lethean",
            "url": "lthn.ss.dxpool.com:6622",
            "user": "iz6CWkqcPVsbZtyJJecQ4kTosPJrgdxAHP63sG2hk8sfaU14LwvFBqwfBL9qGg6DwjhpFG9XZzY2jcRSYivKHDMt2NjcZtUrG",
            "pass": "rx580",

## Spudz76 | 2021-05-28T16:47:57+00:00
Noted.  hmm.  Sure wish it would say where it failed.

## brianmcfadden | 2021-05-28T16:57:44+00:00
It fails near the atomic_inc in Skein(). When I comment out the 4 lines in
/src/backend/opencl/cl/cn/cryptonight.cl, starting from the atomic_inc at
line 803, through to the end of the if statement at line 806, the build
part works. I've hacked on it a bit, and whenever I try to read or write to
anything in the output array, it fails

Thanks for the tests.

On Fri, May 28, 2021 at 12:48 PM Tony Butler ***@***.***>
wrote:

> Noted. hmm. Sure wish it would say where it failed.
>
> —
> You are receiving this because you were mentioned.
> Reply to this email directly, view it on GitHub
> <https://github.com/xmrig/xmrig/issues/2345#issuecomment-850543655>, or
> unsubscribe
> <https://github.com/notifications/unsubscribe-auth/AAOC7YSZKUXZOR66L7MQGN3TP7CMZANCNFSM44D37PLA>
> .
>


## Spudz76 | 2021-05-28T17:24:54+00:00
given that tip I tried another hack which also matches how atomic_inc is used in other algos

## Spudz76 | 2021-05-28T17:56:17+00:00
hidden change to the last patch, `git pull --rebase` since I force-pushed

## brianmcfadden | 2021-05-28T18:00:48+00:00
Nope, same build error with no log.  The same 'comment it out and the build error goes away' behavior.


## Spudz76 | 2021-05-28T18:02:29+00:00
Okay tracing why updating the array is failing then (the ulong type was definitely wrong and might as well also be const, so that was a useful cleanup anyway)

## ganzocrypt | 2021-05-28T18:11:49+00:00
I tested with the latest changes and got this:

` * POOL #1      lthn.ss.dxpool.com:6622 algo cn/2
 * 2021-05-28 20:09:59.255]  net      use pool lthn.ss.dxpool.com:6622  39.106.233.58
[2021-05-28 20:09:59.255]  net      new job from lthn.ss.dxpool.com:6622 diff 20000 algo cn/r height 967463
[2021-05-28 20:09:59.256]  opencl   use profile  cn/2  (1 thread) scratchpad 2048 KB
|  # | GPU |  BUS ID | INTENSITY | WSIZE | MEMORY | NAME
|  0 |   0 |     n/a |       384 |     8 |    768 | AMD Radeon RX 580 Compute Engine
[2021-05-28 20:09:59.258]  opencl   GPU #0 compiling...
[2021-05-28 20:09:59.611]  opencl   error CL_BUILD_PROGRAM_FAILURE when calling clBuildProgram
BUILD LOG:
<program source>:141:7: warning: no previous prototype for function 'AES_Round'
uint4 AES_Round(const __local uint *AES0,const __local uint *AES1,const __local uint *AES2,const __local uint *AES3,const uint4 X,uint4 key)
      ^
<program source>:149:7: warning: no previous prototype for function 'AES_Round_Two_Tables'
uint4 AES_Round_Two_Tables(const __local uint *AES0,const __local uint *AES1,const uint4 X,uint4 key)
      ^
<program source>:178:6: warning: no previous prototype for function 'AESExpandKey256'
void AESExpandKey256(uint *keybuf)
     ^
<program source>:221:7: warning: no previous prototype for function 'SKEIN_ROT'
ulong SKEIN_ROT(const uint2 x,const uint y)
      ^
<program source>:230:6: warning: no previous prototype for function 'SkeinMix8'
void SkeinMix8(ulong4 *pv0,ulong4 *pv1,const uint rc0,const uint rc1,const uint rc2,const uint rc3)
     ^
<program source>:239:8: warning: no previous prototype for function 'SkeinEvenRound'
ulong8 SkeinEvenRound(ulong8 p,const ulong8 h,const ulong *t,const uint s)
       ^
<program source>:255:8: warning: no previous prototype for function 'SkeinOddRound'
ulong8 SkeinOddRound(ulong8 p,const ulong8 h,const ulong *t,const uint s)
       ^
<program source>:271:8: warning: no previous prototype for function 'Skein512Block'
ulong8 Skein512Block(ulong8 p,ulong8 h,ulong h8,const ulong *t)
       ^
<program source>:876:6: warning: no previous prototype for function 'keccakf1600_1'
void keccakf1600_1(ulong *st)
     ^
<program source>:918:6: warning: no previous prototype for function 'keccakf1600_2'
void keccakf1600_2(__local ulong *st)
     ^
<program source>:1330:16: warning: comparison of integers of different signs: 'int' and 'unsigned int'
for (int i=0; i<ITERATIONS; ++i) {
              ~^~~~~~~~~~~
<program source>:1548:7: error: unknown type name 'uint32_t'; did you mean 'uint32'?
const uint32_t outIdx=atomic_inc(output+0xFF);
      ^~~~~~~~
      uint32
/System/Library/Frameworks/OpenCL.framework/Versions/A/lib/clang/3.2/include/cl_kernel.h:292:57: note: 'uint32' declared here
typedef struct __Reserved_Name__Do_not_use_uint32       uint32;
                                                        ^
<program source>:1548:16: error: variable has incomplete type 'const uint32' (aka 'const struct __Reserved_Name__Do_not_use_uint32')
const uint32_t outIdx=atomic_inc(output+0xFF);
               ^
/System/Library/Frameworks/OpenCL.framework/Versions/A/lib/clang/3.2/include/cl_kernel.h:292:16: note: forward declaration of 'struct __Reserved_Name__Do_not_use_uint32'
typedef struct __Reserved_Name__Do_not_use_uint32       uint32;
               ^
<program source>:1602:7: error: unknown type name 'uint32_t'; did you mean 'uint32'?
const uint32_t outIdx=atomic_inc(output+0xFF);
      ^~~~~~~~
      uint32
/System/Library/Frameworks/OpenCL.framework/Versions/A/lib/clang/3.2/include/cl_kernel.h:292:57: note: 'uint32' declared here
typedef struct __Reserved_Name__Do_not_use_uint32       uint32;
                                                        ^
<program source>:1602:16: error: variable has incomplete type 'const uint32' (aka 'const struct __Reserved_Name__Do_not_use_uint32')
const uint32_t outIdx=atomic_inc(output+0xFF);
               ^
/System/Library/Frameworks/OpenCL.framework/Versions/A/lib/clang/3.2/include/cl_kernel.h:292:16: note: forward declaration of 'struct __Reserved_Name__Do_not_use_uint32'
typedef struct __Reserved_Name__Do_not_use_uint32       uint32;
               ^
<program source>:1679:7: error: unknown type name 'uint32_t'; did you mean 'uint32'?
const uint32_t outIdx=atomic_inc(output+0xFF);
      ^~~~~~~~
      uint32
/System/Library/Frameworks/OpenCL.framework/Versions/A/lib/clang/3.2/include/cl_kernel.h:292:57: note: 'uint32' declared here
typedef struct __Reserved_Name__Do_not_use_uint32       uint32;
                                                        ^
<program source>:1679:16: error: variable has incomplete type 'const uint32' (aka 'const struct __Reserved_Name__Do_not_use_uint32')
const uint32_t outIdx=atomic_inc(output+0xFF);
               ^
/System/Library/Frameworks/OpenCL.framework/Versions/A/lib/clang/3.2/include/cl_kernel.h:292:16: note: forward declaration of 'struct __Reserved_Name__Do_not_use_uint32'
typedef struct __Reserved_Name__Do_not_use_uint32       uint32;
               ^
<program source>:1749:7: error: unknown type name 'uint32_t'; did you mean 'uint32'?
const uint32_t outIdx=atomic_inc(output+0xFF);
      ^~~~~~~~
      uint32
/System/Library/Frameworks/OpenCL.framework/Versions/A/lib/clang/3.2/include/cl_kernel.h:292:57: note: 'uint32' declared here
typedef struct __Reserved_Name__Do_not_use_uint32       uint32;
                                                        ^
<program source>:1749:16: error: variable has incomplete type 'const uint32' (aka 'const struct __Reserved_Name__Do_not_use_uint32')
const uint32_t outIdx=atomic_inc(output+0xFF);
               ^
/System/Library/Frameworks/OpenCL.framework/Versions/A/lib/clang/3.2/include/cl_kernel.h:292:16: note: forward declaration of 'struct __Reserved_Name__Do_not_use_uint32'
typedef struct __Reserved_Name__Do_not_use_uint32       uint32;
               ^

[2021-05-28 20:09:59.611]  opencl   thread #0 failed with error CL_INVALID_PROGRAM
[2021-05-28 20:09:59.612]  opencl   thread #0 self-test failed
[2021-05-28 20:09:59.612]  opencl   disabled (failed to start threads)
[2021-05-28 20:10:03.424]  signal   Ctrl+C received, exiting
`

## Spudz76 | 2021-05-28T18:15:54+00:00
yeah that's the wrong push, try a `git fetch --all` and `git pull --rebase`

Also just shoved a new attempt for array access fix, based on this clue I found in another algorithm

```
            /* explicit cast to `uint` is required because some OpenCL implementations (e.g. NVIDIA)
             * handle get_global_id and get_global_offset as signed long long int and add
             * 0xFFFFFFFF... to `get_global_id` if we set on host side a 32bit offset where the first bit is `1`
             * (even if it is correct casted to unsigned on the host)
             */
            ((__local uint *)State)[10] |= (((uint)get_global_id(0) >> 8));
```

## Spudz76 | 2021-05-28T18:18:08+00:00
possibly you may need a `git reset --hard dev-fixAppleOpenCL` depending if you merged an earlier force-push

I pretty much always use `git pull --rebase` and always do force-pushes to keep micro edits rolled up into atomic commits (habit)

## ganzocrypt | 2021-05-28T18:22:12+00:00
got this:

 * POOL #1      lthn.ss.dxpool.com:6622 algo cn/2
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       #0 Apple/OpenCL 1.2 (Jun  8 2020 17:36:15)
 * OPENCL GPU   #0 n/a AMD Radeon RX 580 Compute Engine 1366 MHz cu:36 mem:2048/8192 MB
 * CUDA         disabled
[2021-05-28 20:21:45.162]  net      use pool lthn.ss.dxpool.com:6622  39.106.233.58
[2021-05-28 20:21:45.163]  net      new job from lthn.ss.dxpool.com:6622 diff 20000 algo cn/r height 967466
[2021-05-28 20:21:45.163]  opencl   use profile  cn/2  (1 thread) scratchpad 2048 KB
|  # | GPU |  BUS ID | INTENSITY | WSIZE | MEMORY | NAME
|  0 |   0 |     n/a |       384 |     8 |    768 | AMD Radeon RX 580 Compute Engine
[2021-05-28 20:21:45.165]  opencl   GPU #0 compiling...
[2021-05-28 20:21:45.168]  opencl   error CL_BUILD_PROGRAM_FAILURE when calling clBuildProgram
BUILD LOG:
<program source>:141:7: warning: no previous prototype for function 'AES_Round'
uint4 AES_Round(const __local uint *AES0,const __local uint *AES1,const __local uint *AES2,const __local uint *AES3,const uint4 X,uint4 key)
      ^
<program source>:149:7: warning: no previous prototype for function 'AES_Round_Two_Tables'
uint4 AES_Round_Two_Tables(const __local uint *AES0,const __local uint *AES1,const uint4 X,uint4 key)
      ^
<program source>:178:6: warning: no previous prototype for function 'AESExpandKey256'
void AESExpandKey256(uint *keybuf)
     ^
<program source>:221:7: warning: no previous prototype for function 'SKEIN_ROT'
ulong SKEIN_ROT(const uint2 x,const uint y)
      ^
<program source>:230:6: warning: no previous prototype for function 'SkeinMix8'
void SkeinMix8(ulong4 *pv0,ulong4 *pv1,const uint rc0,const uint rc1,const uint rc2,const uint rc3)
     ^
<program source>:239:8: warning: no previous prototype for function 'SkeinEvenRound'
ulong8 SkeinEvenRound(ulong8 p,const ulong8 h,const ulong *t,const uint s)
[2021-05-28 20:21:45.168]  opencl   thread #0 failed with error CL_INVALID_PROGRAM
[2021-05-28 20:21:45.170]  opencl   thread #0 self-test failed
[2021-05-28 20:21:45.170]  opencl   disabled (failed to start threads)
[2021-05-28 20:21:48.660]  signal   Ctrl+C received, exiting
[2021-05-28 20:21:48.660]  opencl   stopped (0 ms)


## Spudz76 | 2021-05-28T18:22:23+00:00
In fact, I just did it again.  (forgot to generate_cl before push)

## brianmcfadden | 2021-05-28T18:43:04+00:00
This time, I'm getting a bunch of warnings, but it doesn't show me the error.

[2021-05-28 14:31:25.900]  opencl   GPU #1 compiling...
[2021-05-28 14:31:25.900]  opencl   thread #1 failed with error CL_INVALID_PROGRAM
[2021-05-28 14:31:25.901]  opencl   thread #1 self-test failed
[2021-05-28 14:31:25.901]  opencl   error CL_BUILD_PROGRAM_FAILURE when calling clBuildProgram
BUILD LOG:
<program source>:141:7: warning: no previous prototype for function 'AES_Round'
uint4 AES_Round(const __local uint *AES0,const __local uint *AES1,const __local uint *AES2,const __local uint *AES3,const uint4 X,uint4 key)
      ^
<program source>:149:7: warning: no previous prototype for function 'AES_Round_Two_Tables'
uint4 AES_Round_Two_Tables(const __local uint *AES0,const __local uint *AES1,const uint4 X,uint4 key)
      ^
<program source>:178:6: warning: no previous prototype for function 'AESExpandKey256'
void AESExpandKey256(uint *keybuf)
     ^
<program source>:221:7: warning: no previous prototype for function 'SKEIN_ROT'
ulong SKEIN_ROT(const uint2 x,const uint y)
      ^
<program source>:230:6: warning: no previous prototype for function 'SkeinMix8'
void SkeinMix8(ulong4 *pv0,ulong4 *pv1,const uint rc0,const uint rc1,const uint rc2,const uint rc3)
     ^
<program source>:239:8: warning: no previous prototype for function 'SkeinEvenRound'
ulong8 SkeinEvenRound(ulong8 p,const ulong8 h,const ulong *t,const uint s)
       ^
<program source>:255:8: warning: no previous prototype for function 'SkeinOddRound'
ulong8 SkeinOddRound(ulong8 p,const ulong8 h,const ulong *t,const uint s)
       ^
<program source>:271:8: warning: no previous prototype for function 'Skein512Block'
ulong8 Skein512Block(ulong8 p,ulong8 h,ulong h8,const ulong *t)
       ^
<program source>:876:6: warning: no previous prototype for function 'keccakf1600_1'
void keccakf1600_1(ulong *st)
     ^
<program source>:918:6: warning: no previous prototype for function 'keccakf1600_2'
void keccakf1600_2(__local ulong *st)
     ^
<program source>:1330:16: warning: comparison of integers of different signs: 'int' and 'unsigned int'
for (int i=0; i<ITERATIONS; ++i) {
              ~^~~~~~~~~~~
SC failed. No reason given.

Just to let you know, those last 2 sentences "SC failed. No reason given." were part of the build log, and not my own commentary.

## Spudz76 | 2021-05-28T19:00:49+00:00
Strange / I just force-pushed another array fix attempt

## ganzocrypt | 2021-05-28T19:06:34+00:00
still errors:
![Screen Shot 2021-05-28 at 9 05 26 PM](https://user-images.githubusercontent.com/42419950/120031055-88a15080-bff8-11eb-9e15-58b4ac0fb1fe.png)


## brianmcfadden | 2021-05-28T19:08:25+00:00
Double-checking this is for commit b1dbaba84417cf7390b96cf9720990856d8ae96b

Same 'SC failed' errors.


## Spudz76 | 2021-05-28T19:17:38+00:00
Strange, nvidiaCL still compiles it, maybe we're close but slightly syntactically bad still

## Spudz76 | 2021-05-28T19:33:37+00:00
Re-tested current pile of hacks on M1, still works great.  hmmm

## ganzocrypt | 2021-05-29T08:32:18+00:00
A consideration for OpenCL configuration, there should be only 1 thread for all algos?
"cn/2": [
            {
                "index": 0,
                "intensity": 864,
                "worksize": 8,
                "strided_index": [2],
                "threads": [-1],
                "unroll": 8
            }
        ],
So all other algos in the OpenCL configuration should be similar to this one, is that correct?

## Spudz76 | 2021-05-29T19:50:49+00:00
Yes the 1 thread is the one that sends jobs to and results from the GPU.  While the GPU has a whole lot of threads.

Some fast cards like Vega benefit from having two "shoveler" threads.

I figured out cn/r works a bit better when I turn down the worksize and turn off strided index.

```
        "cn/r": [
            {
                "index": 0,
                "intensity": 176,
                "worksize": 2,
                "strided_index": false,
                "threads": [-1],
                "unroll": 8
            }   
        ],  
```



## ganzocrypt | 2021-05-29T20:13:07+00:00
Will test it tomorrow, which changes do I need to get? Let me know.

## Spudz76 | 2021-05-29T20:43:28+00:00
Pushed to the branch, commit `7d69aee34`

## brianmcfadden | 2021-05-30T00:41:25+00:00
So close.

program source:212:26: error: invalid conversion between vector type '__uint2' and integer type 'long' of different size
if(y<32) return(as_ulong(amd_bitalign(x,x.s10,32-y)));

At least it shows the error.


## brianmcfadden | 2021-05-30T00:45:24+00:00
Actually, ran generate and got a little more of the build log, don't know why:
BUILD LOG:
<program source>:142:7: warning: no previous prototype for function 'AES_Round'
uint4 AES_Round(const __local uint *AES0,const __local uint *AES1,const __local uint *AES2,const __local uint *AES3,const uint4 X,uint4 key)
      ^
<program source>:150:7: warning: no previous prototype for function 'AES_Round_Two_Tables'
uint4 AES_Round_Two_Tables(const __local uint *AES0,const __local uint *AES1,const uint4 X,uint4 key)
      ^
<program source>:179:6: warning: no previous prototype for function 'AESExpandKey256'
void AESExpandKey256(uint *keybuf)
     ^
<program source>:210:7: warning: no previous prototype for function 'SKEIN_ROT'
ulong SKEIN_ROT(const uint2 x,const uint y)
      ^
<program source>:212:26: error: invalid conversion between vector type '__uint2' and integer type 'long' of different size
if(y<32) return(as_ulong(amd_bitalign(x,x.s10,32-y)));
                         ^
<program source>:5:45: note: expanded from macro 'amd_bitalign'
#define amd_bitalign(src0, src1, src2) ((((((long)src0) << 32) | (long)src1) >> (src2 & 31)))
                                            ^
/System/Library/PrivateFrameworks/GPUCompiler.framework/Versions/A/lib/clang/3.5/include/cl_kernel.h:4278:43: note: expanded from macro 'as_ulong'
#define as_ulong( _x )  __builtin_astype( _x, ulong )
                                          ^
<program source>:212:26: error: invalid conversion between vector type '__uint2' and integer type 'long' of different size
if(y<32) return(as_ulong(amd_bitalign(x,x.s10,32-y)));
                         ^
<program source>:5:66: note: expanded from macro 'amd_bitalign'
#define amd_bitalign(src0, src1, src2) ((((((long)src0) << 32) | (long)src1) >> (src2 & 31)))
                                                                 ^
/System/Library/PrivateFrameworks/GPUCompiler.framework/Versions/A/lib/clang/3.5/include/cl_kernel.h:4278:43: note: expanded from macro 'as_ulong'


## Spudz76 | 2021-05-30T00:53:06+00:00
Something is really broken with your generate

## brianmcfadden | 2021-05-30T01:00:09+00:00
Using node v14.10.1, and it's the same code as in your latest commit.  Don't know what could be up, but I think we can ignore it unless it's important.

## Spudz76 | 2021-05-30T02:12:06+00:00
It just seems to be aborting before it includes `AES_Round_Two_Tables`, otherwise there is certainly a definition for it.

`2ec0faf5f` pushed; should fix that other problem (cross fingers)

It actually worked now on the test nvidia (previously still crashed, but only cn/r crashed out of all cn)

## brianmcfadden | 2021-05-30T02:21:39+00:00
There we go.. Build is OK, and it's even sending acceptable shares. 

[2021-05-29 22:14:59.870]  opencl   GPU #0 compiling...
[2021-05-29 22:15:19.381]  opencl   GPU #0 compilation completed (19512 ms)
[2021-05-29 22:15:19.382]  opencl   GPU #0 compiling...
[2021-05-29 22:15:19.383]  opencl   GPU #0 compilation completed (1 ms)
[2021-05-29 22:15:19.384]  opencl   READY threads 2/2 (19517 ms)
| OPENCL # | AFFINITY | 10s  H/s | 60s  H/s | 15m  H/s |
|        0 |       -1 |    18.34 |      n/a |      n/a | #0 n/a Intel(R) HD Graphics 530
|        1 |       -1 |    18.34 |      n/a |      n/a | #0 n/a Intel(R) HD Graphics 530
|        - |        - |    31.53 |      n/a |      n/a |
[2021-05-29 22:15:35.294]  miner    speed 10s/60s/15m 31.53 n/a n/a H/s max 35.90 H/s


## Spudz76 | 2021-05-30T03:14:00+00:00
Weird/Cool lol

The final patch was based on some [stuff in wolf-xmr-miner](https://github.com/hyc/wolf-xmr-miner/commit/6e30f9bfd634b8d0031c4ca8d4326f7e3e3b35ed) that made oddball Android OpenCL implementations work.

Note that's operating on the Intel iGPU not even an AMD...

## ganzocrypt | 2021-05-30T13:02:23+00:00
So I rebuild your branch from scratch with all the latest changes but I still getting errors.
I am attaching the log and the config
[log-config.zip](https://github.com/xmrig/xmrig/files/6566233/log-config.zip)

Maybe my build has some libs miss match with yours?
Not sure since the other KawPow algo works fine for days.



## Spudz76 | 2021-05-30T17:33:32+00:00
Strange I would expect more trouble making it work with Intel iGPU lol.

## ganzocrypt | 2021-05-30T18:25:49+00:00
would your xmrig binary work on my system? I can give it a try.

## brianmcfadden | 2021-05-30T19:09:09+00:00
It's worth a try.  I uploaded it here: https://drive.google.com/file/d/1hbO34GB5GoymkMVqGsMi_YA7LAzZxkZH/view


## ganzocrypt | 2021-05-30T19:13:02+00:00
cannot run it:
./xmrig 
dyld: Library not loaded: /usr/local/opt/hwloc/lib/libhwloc.15.dylib

## brianmcfadden | 2021-05-30T19:38:10+00:00
So, you could try the hwloc lib here: https://drive.google.com/file/d/19humuGQm2N3G0tJyijZ2yB1es2YdkYrN/view?usp=sharing

Or, optionally, I'm building one without hwloc, aaaaand, still waiting ... still waiting ... it's here: https://drive.google.com/file/d/17K2zlEnanPeIIVS3vofGHMd20pciwxTN/view?usp=sharing

## brianmcfadden | 2021-05-30T19:44:07+00:00
> Note that's operating on the Intel iGPU not even an AMD...

Crap, I glanced over this blindly both when I was reading my own logs and your note, and I remember that I changed the index in the config and forgot to change it back. Me is stupid. So, yeah, bad news now.

[2021-05-30 15:38:53.216]  opencl   GPU #1 compiling...
[2021-05-30 15:38:56.109]  opencl   error CL_BUILD_PROGRAM_FAILURE when calling clBuildProgram
BUILD LOG:
Error returned by cvms_element_build_from_source


## ganzocrypt | 2021-05-30T19:47:01+00:00
with lib:
![Screen Shot 2021-05-30 at 9 46 27 PM](https://user-images.githubusercontent.com/42419950/120118005-8d990800-c190-11eb-855a-3e126b3a28c0.png)

no lib:
![Screen Shot 2021-05-30 at 9 41 28 PM](https://user-images.githubusercontent.com/42419950/120117903-e1efb800-c18f-11eb-83d5-6672fd02dbeb.png)


## brianmcfadden | 2021-05-30T19:47:16+00:00
@Spudz76 This would be a bunch easier if you had access to my build machine, right?  I can open up ssh on my router and make a temporary account on it for you, if you're up for that. You'd be limited to command line and vi.

## Spudz76 | 2021-05-31T06:52:24+00:00
@brianmcfadden I suppose that would help me throw hacks at the wall until something sticks much faster than throwing patches at everyone in this thread on a much slower feedback basis.  I'll respond to your email, which I got, but just was busy with other things.

Still amazed the Intel worked (sort of well too).

## dg-Nacho | 2021-07-28T20:31:41+00:00
> @Sammed98 @empiresun1 @ef651100 @brianmcfadden could you please test the [release](https://github.com/ganzocrypt/xmrig-macos/releases/tag/v6.13.0-dev-macos) to see if everything is working? thx

Just wanted to chime in. I've been using this release for the past couple days on my iMac 2020 with a AMD Radeon Pro 5700 XT and I get around 8.6 MH/s up to 9.2 MH/s on the machine. And it swings from 2.5 Mh up to 21.5 Mh/s on the unmineable pool/site. Pretty happy with it so far. Under bootcamp using the unmineable app, it can hit an 28 Mh and swing from 15mh to  45mh on the site.

# Action History
- Created by: Sammed98 | 2021-05-05T03:43:19+00:00
- Closed at: 2025-06-20T11:12:00+00:00
