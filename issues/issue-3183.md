---
title: Segmentation Fault on M1 MacOS
source_url: https://github.com/xmrig/xmrig/issues/3183
author: TimJSwan89
assignees: []
labels:
- bug
- arm
- randomx
created_at: '2022-12-23T03:10:08+00:00'
updated_at: '2023-11-23T15:26:18+00:00'
type: issue
status: closed
closed_at: '2023-11-23T15:26:18+00:00'
---

# Original Description
Built using the recommended commands at https://xmrig.com/docs/miner/build/macos
```
brew install cmake libuv openssl hwloc
git clone https://github.com/xmrig/xmrig.git
mkdir xmrig/build && cd xmrig/build
cmake .. -DUV_INCLUDE_DIR=/opt/homebrew/include -DUV_LIBRARY=/opt/homebrew/lib/libuv.a -DOPENSSL_ROOT_DIR=/opt/homebrew/opt/openssl -DHWLOC_INCLUDE_DIR=/opt/homebrew/include -DHWLOC_LIBRARY=/opt/homebrew/lib/libhwloc.dylib
make -j$(sysctl -n hw.logicalcpu)
```
```
./xmrig --donate-level 10 --opencl -o stratum+tcp://stratum.cudopool.com:30010 -u o:744943:n:MBA-Tim -p x -k --nicehash --coin monero -a rx/0
 * ABOUT        XMRig/6.18.1 clang/14.0.0
 * LIBS         libuv/1.44.2 OpenSSL/3.0.7 hwloc/2.8.0
 * HUGE PAGES   unavailable
 * 1GB PAGES    unavailable
 * CPU          Apple M1 (1) 64-bit AES
                L2:16.0 MB L3:0.0 MB 8C/8T NUMA:1
 * MEMORY       7.7/8.0 GB (96%)
 * DONATE       10%
 * POOL #1      stratum+tcp://stratum.cudopool.com:30010 coin Monero
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       #0 Apple/OpenCL 1.2 (Sep 30 2022 01:38:14)
 * OPENCL GPU   #0 n/a Apple M1 1000 MHz cu:8 mem:1024/5461 MB
 * CUDA         disabled
[2022-12-22 21:56:33.151]  net      use pool stratum.cudopool.com:30010  147.135.37.197
[2022-12-22 21:56:33.152]  net      new job from stratum.cudopool.com:30010 diff 45000 algo rx/0 height 2783311 (13 tx)
[2022-12-22 21:56:33.153]  cpu      use argon2 implementation default
[2022-12-22 21:56:33.153]  randomx  init dataset algo rx/0 (8 threads) seed fd64b331392849ec...
[2022-12-22 21:56:33.154]  randomx  allocated 2336 MB (2080+256) huge pages 0% 0/1168 +JIT (1 ms)
[2022-12-22 21:56:39.590]  randomx  dataset ready (6436 ms)
[2022-12-22 21:56:39.590]  cpu      use profile  rx  (8 threads) scratchpad 2048 KB
[2022-12-22 21:56:39.591]  cpu      READY threads 8/8 (8) huge pages 0% 0/8 memory 16384 KB (1 ms)
zsh: segmentation fault  ./xmrig --donate-level 10 --opencl -o stratum+tcp://stratum.cudopool.com:3001
```
```
otool -L xmrig                   
xmrig:
	/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit (compatibility version 1.0.0, current version 275.0.0)
	/System/Library/Frameworks/CoreServices.framework/Versions/A/CoreServices (compatibility version 1.0.0, current version 1228.0.0)
	/opt/homebrew/opt/hwloc/lib/libhwloc.15.dylib (compatibility version 22.0.0, current version 22.0.0)
	/usr/lib/libc++.1.dylib (compatibility version 1.0.0, current version 1300.36.0)
	/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1319.0.0)
	/System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation (compatibility version 150.0.0, current version 1953.255.0)
```
If you need the commit hash, in the build folder:
```
git rev-parse HEAD
28e81bd7c09c88f8dfe5ab5fb1fbd62f3bca1f8b
```

# Discussion History
## TimJSwan89 | 2022-12-23T03:19:50+00:00
Scratch the OpenCL. The Seg fault happens without it.
```
./xmrig --donate-level 10 -o stratum+tcp://stratum.cudopool.com:30010 -u o:744943:n:MBA-Tim -p x -k --nicehash --coin monero -a rx/0
```
The only reason why I thought it depended on it was because earlier I had it running CPU only with another build, which I think I had simply downloaded from the website, which failed with an OpenCL metal dependency.

## Spudz76 | 2022-12-23T15:04:59+00:00
Use `./scripts/build_deps.sh` for the openssl/hwloc/libuv dependencies, the homebrew ones almost never work.

## Unnameless | 2022-12-24T13:41:01+00:00
> Use `./scripts/build_deps.sh` for the openssl/hwloc/libuv dependencies, the homebrew ones almost never work.

Actually most of the type brew installed dependencies always worked for me, in the last couple of years, ever since xmrig was on CN. This time something went sideways.

## Spudz76 | 2022-12-24T15:39:35+00:00
> the homebrew ones almost never work

in other words, bundled versions are the tested ones so if you like support, you use the bundled ones.

## Unnameless | 2023-02-06T09:06:39+00:00
> Use `./scripts/build_deps.sh` for the openssl/hwloc/libuv dependencies, the homebrew ones almost never work.

actually seg fault happens when compiling using the script also! The only way to avoid it, is to use the already compiled binaries

## furic | 2023-03-22T06:48:23+00:00
Ran `./scripts/build_deps.sh` and still having `zsh: segmentation fault` on the build.
I'm building 6.19.0, in macOS 13.2.1, M2 Pro.

## giffeler | 2023-04-03T19:36:12+00:00
xmrig 6.19.2, macOS 13.3. Independent of the chosen compiler (gcc or current xcode), independent of homebrew: segfault.

## ghost | 2023-04-18T12:55:18+00:00
Still crashes on Apple M2, installed from homebrew:
XMRig 6.19.2
 built on Apr  3 2023 with clang 14.0.0 (clang-1400.0.29.202)
 features:

libuv/1.44.2
OpenSSL/3.1.0
hwloc/2.9.0

By disableing the CPU miner, the opencl crashes:
```
UNSUPPORTED (log once): buildComputeProgram: cl2Metal failed
[2023-04-18 14:47:54.183]  opencl   error CL_BUILD_PROGRAM_FAILURE when calling clBuildProgram
BUILD LOG:
program_source:1786:1: warning: comparison of integers of different signs: 'uint32_t' (aka 'unsigned int') and 'int'
update_max(latency,(last_memory_op_slot+WORKERS_PER_HASH)/WORKERS_PER_HASH);
^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
program_source:1397:56: note: expanded from macro 'update_max'
#define update_max(value, next_value) do { if ((value) < (next_value)) (value) = (next_value); } while (0)
                                                ~~~~~  ^  ~~~~~~~~~~
program_source:1809:1: warning: comparison of integers of different signs: 'int32_t' (aka 'int') and 'unsigned int'
update_max(first_allowed_slot,latency*WORKERS_PER_HASH);
^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
program_source:1397:56: note: expanded from macro 'update_max'
#define update_max(value, next_value) do { if ((value) < (next_value)) (value) = (next_value); } while (0)
                                                ~~~~~  ^  ~~~~~~~~~~
program_source:1813:1: warning: comparison of integers of different signs: 'int32_t' (aka 'int') and 'unsigned int'
[2023-04-18 14:47:54.184]  opencl   thread #0 failed with error CL_INVALID_PROGRAM
```

## MarcusNewman | 2023-06-18T04:53:09+00:00
Still seeing this issue, M2 XMRig 6.19.3
Using build_deps.sh shows: * LIBS         libuv/1.45.0 OpenSSL/3.1.1 hwloc/2.9.0
precompiled binary shows: * LIBS         libuv/1.44.2 OpenSSL/3.0.7 hwloc/2.9.0
Another thought, if the build steps at https://xmrig.com/docs/miner/build/macos are incorrect, how can we the users update them?

## hut8 | 2023-06-20T19:41:47+00:00
I'm getting a segfault on the M2 as well. Thanks very much Marcus for pointing out the differences! I followed the instructions exact and was surprised there was such a segfault...

```
[2023-06-20 15:37:17.944]  randomx  dataset ready (3481 ms)
[2023-06-20 15:37:17.944]  cpu      use profile  rx  (12 threads) scratchpad 2048 KB
[2023-06-20 15:37:17.944]  cpu      READY threads 12/12 (12) huge pages 0% 0/12 memory 24576 KB (0 ms)
Process 35194 stopped
* thread #18, stop reason = EXC_BAD_ACCESS (code=1, address=0x0)
    frame #0: 0x0000000101c68404
->  0x101c68404: ldpsw  x18, x19, [x18]
    0x101c68408: mov.d  v28[0], x18
    0x101c6840c: mov.d  v28[1], x19
    0x101c68410: scvtf.2d v28, v28
Target 0: (xmrig) stopped.
(lldb) bt
* thread #18, stop reason = EXC_BAD_ACCESS (code=1, address=0x0)
  * frame #0: 0x0000000101c68404
(lldb) thread list
Process 35194 stopped
  thread #1: tid = 0x8c4c2b, 0x000000019da9e060 libsystem_kernel.dylib`kevent + 8, queue = 'com.apple.main-thread'
  thread #2: tid = 0x8c688e, 0x000000019da9b710 libsystem_kernel.dylib`__psynch_cvwait + 8
  thread #3: tid = 0x8c688f, 0x000000019da9b710 libsystem_kernel.dylib`__psynch_cvwait + 8
  thread #4: tid = 0x8c6890, 0x000000019da9b710 libsystem_kernel.dylib`__psynch_cvwait + 8
  thread #5: tid = 0x8c6891, 0x000000019da9b710 libsystem_kernel.dylib`__psynch_cvwait + 8
  thread #6: tid = 0x8c6892, 0x000000019da9b710 libsystem_kernel.dylib`__psynch_cvwait + 8
  thread #7: tid = 0x8c68c0, 0x000000019da9b50c libsystem_kernel.dylib`__semwait_signal + 8
  thread #8: tid = 0x8c68c1, 0x000000019da9b50c libsystem_kernel.dylib`__semwait_signal + 8
  thread #9: tid = 0x8c68c2, 0x000000019da9b50c libsystem_kernel.dylib`__semwait_signal + 8
  thread #10: tid = 0x8c68c3, 0x000000019da9b50c libsystem_kernel.dylib`__semwait_signal + 8
  thread #11: tid = 0x8c68c4, 0x000000019da9b50c libsystem_kernel.dylib`__semwait_signal + 8
  thread #12: tid = 0x8c68c5, 0x000000019da9b50c libsystem_kernel.dylib`__semwait_signal + 8
  thread #13: tid = 0x8c68c6, 0x000000019da9b50c libsystem_kernel.dylib`__semwait_signal + 8
  thread #14: tid = 0x8c68c7, 0x000000019da9b50c libsystem_kernel.dylib`__semwait_signal + 8
  thread #15: tid = 0x8c68c8, 0x000000019da9b50c libsystem_kernel.dylib`__semwait_signal + 8
  thread #16: tid = 0x8c68c9, 0x000000019da9b50c libsystem_kernel.dylib`__semwait_signal + 8
  thread #17: tid = 0x8c68ca, 0x000000019da9b50c libsystem_kernel.dylib`__semwait_signal + 8
* thread #18: tid = 0x8c68cb, 0x0000000101c68404, stop reason = EXC_BAD_ACCESS (code=1, address=0x0)
```

What's interesting about those versions is that [build_deps.sh](
https://github.com/xmrig/xmrig/blob/0bc87345c4a0c796557a90885c9a17d3cd9d4c08/scripts/build_deps.sh) calls [build_openssl.sh](https://github.com/xmrig/xmrig/blob/0bc87345c4a0c796557a90885c9a17d3cd9d4c08/scripts/build.openssl.sh) which contains this line:

Apparently it builds the right version (`OPENSSL_VERSION="1.1.1s"`) and then links the wrong one? I'm not entirely sure...

## hut8 | 2023-06-20T20:09:24+00:00
Scratch that. The official instructions don't even mention build_deps.sh. When I run build_deps.sh (from `./scripts`), then compile using:

```
cmake .. -DOPENSSL_CRYPTO_LIBRARY=../scripts/deps/lib/libcrypto.a -DOPENSSL_SSL_LIBRARY=../scripts/deps/lib/libssl.a -DOPENSSL_INCLUDE_DIR=../scripts/deps/include -DHWLOC_INCLUDE_DIR=../scripts/deps/include -DHWLOC_LIBRARY=../scripts/deps/lib/libhwloc.a
make
```

I do get the expected version, but unfortunately it still segfaults in the same place :(

## SChernykh | 2023-06-21T05:34:47+00:00
This is a known problem, and the only solution so far is to use older MacOS SDK for the build: https://github.com/tevador/RandomX/issues/262#issuecomment-1509895418
So try to add `-DCMAKE_OSX_SYSROOT=/path/to/MacOSX12.3.sdk` (download the SDK first of course) to cmake command line and do a fresh build.

## katletkis | 2023-08-12T19:43:29+00:00
Thank you @SChernykh, building with OSX12.3.sdk worked for me

## alicedb2 | 2023-08-24T19:10:10+00:00
I'm compiling on a M2 Macbook Air running Ventura 13.4.2. Using `-DCMAKE_OSX_SYSROOT=/path/to/MacOSX12.3.sdk` when running cmake fixed the segfault for me as well, but the annoying thing is that during linking I did get a bunch of warnings
```
ld: warning: object file (/Users/alice/src/xmrig-6.20.0/scripts/deps/lib/libhwloc.a(topology.o)) was built for newer macOS version (13.0) than being linked (12.3)
ld: warning: object file (/Users/alice/src/xmrig-6.20.0/scripts/deps/lib/libuv.a(libuv_la-fs-poll.o)) was built for newer macOS version (13.0) than being linked (12.3)
ld: warning: object file (/Users/alice/src/xmrig-6.20.0/scripts/deps/lib/libssl.a(bio_ssl.o)) was built for newer macOS version (13.0) than being linked (12.3)
[...]
```
Obviously the 13.3 SDK was picked up by libuv/libhwloc/libssl during `build_deps.sh`.

What ended up working cleanly was to set the `SDKROOT` environment variable prior to both `build_deps.sh` and `cmake`, so something like

```
export SDKROOT=/Library/Developer/CommandLineTools/SDKs/MacOSX12.3.sdk
./build_deps.sh
cd ../build
cmake .. -DOPENSSL_CRYPTO_LIBRARY=../scripts/deps/lib/libcrypto.a -DOPENSSL_SSL_LIBRARY=../scripts/deps/lib/libssl.a -DOPENSSL_INCLUDE_DIR=../scripts/deps/include -DHWLOC_INCLUDE_DIR=../scripts/deps/include -DHWLOC_LIBRARY=../scripts/deps/lib/libhwloc.a -DUV_INCLUDE_DIR=../scripts/deps/include -DUV_LIBRARY=../scripts/deps/lib/libuv.a
make
```
No more segfaults yes, but also no more warnings against mismatched versions during linking.

## SChernykh | 2023-10-19T15:54:50+00:00
Fixed in #3346

# Action History
- Created by: TimJSwan89 | 2022-12-23T03:10:08+00:00
- Closed at: 2023-11-23T15:26:18+00:00
