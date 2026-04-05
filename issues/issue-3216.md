---
title: 'make fails with error "fatal error: uv.h: No such file or directory"'
source_url: https://github.com/xmrig/xmrig/issues/3216
author: bsquared938
assignees: []
labels: []
created_at: '2023-02-23T21:50:14+00:00'
updated_at: '2024-03-18T11:08:25+00:00'
type: issue
status: closed
closed_at: '2023-03-16T14:22:41+00:00'
---

# Original Description
Working on getting this on a Pi 4.  Following a tutorial on this.  

I'm attempting to install xmrig, got the cmake working with this command: 
`cmake .. -DUV_INCLUDE_DIR=path/to/libuv/include -DUV_LIBRARY=path/to/libuv.a`


And now I'm trying make, but I get this error: 
`
[  0%] Building CXX object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/ghostrider.cpp.o
/home/neo/mining/xmrig/src/crypto/ghostrider/ghostrider.cpp:48:10: fatal error: uv.h: No such file or directory
 #include <uv.h>
          ^~~~~~
compilation terminated.
make[2]: *** [src/crypto/ghostrider/CMakeFiles/ghostrider.dir/build.make:271: src/crypto/ghostrider/CMakeFiles/ghostrider.dir/ghostrider.cpp.o] Error 1
make[1]: *** [CMakeFiles/Makefile2:221: src/crypto/ghostrider/CMakeFiles/ghostrider.dir/all] Error 2
make: *** [Makefile:84: all] Error 2
`

# Discussion History
## Spudz76 | 2023-02-24T07:13:54+00:00
Your `path/to/libuv/include` must be wrong.  CMake locates the needed deps anyway why would you ever need to specify?

Could use the `./scripts/build_deps.sh` to build officially supported versions of the three deps.

## bsquared938 | 2023-03-01T04:19:15+00:00
> Your `path/to/libuv/include` must be wrong. CMake locates the needed deps anyway why would you ever need to specify?
> 
> Could use the `./scripts/build_deps.sh` to build officially supported versions of the three deps.

Hi there, I saw your message but just trying what you said now.  this is the new error I seemed to get this time. 


Scanning dependencies of target argon2
[  0%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/argon2.c.                                                o
[  0%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/core.c.o
[  1%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/encoding.                                                c.o
[  1%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/genkat.c.                                                o
[  1%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/impl-sele                                                ct.c.o
[  2%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/blake2/bl                                                ake2.c.o
[  2%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/arch/generic/                                                lib/argon2-arch.c.o
[  3%] Linking C static library libargon2.a
[  3%] Built target argon2
Scanning dependencies of target ethash
[  3%] Building C object src/3rdparty/libethash/CMakeFiles/ethash.dir/ethash_internal.c.o
[  3%] Building C object src/3rdparty/libethash/CMakeFiles/ethash.dir/keccakf800.c.o
[  4%] Linking C static library libethash.a
[  4%] Built target ethash
[  4%] Building CXX object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/ghostrider.cpp.o
/home/neo/mining/xmrig/src/crypto/ghostrider/ghostrider.cpp:48:10: fatal error: uv.h: No such file or                            directory
 #include <uv.h>
          ^~~~~~
compilation terminated.
make[2]: *** [src/crypto/ghostrider/CMakeFiles/ghostrider.dir/build.make:271: src/crypto/ghostrider/C                           MakeFiles/ghostrider.dir/ghostrider.cpp.o] Error 1
make[1]: *** [CMakeFiles/Makefile2:221: src/crypto/ghostrider/CMakeFiles/ghostrider.dir/all] Error 2
make: *** [Makefile:84: all] Error 2




Seems to be a path related thing as you said.  Is there a specific path I need to put xmrig into so that it sees the dependencies in the correct directories? 

## SChernykh | 2023-03-01T06:22:10+00:00
`build_deps.sh` is an advanced build, first try the instructions from https://xmrig.com/docs/miner/build for your OS. For Ubuntu it's, for example:
```
sudo apt-get install git build-essential cmake libuv1-dev libssl-dev libhwloc-dev
git clone https://github.com/xmrig/xmrig.git
mkdir xmrig/build && cd xmrig/build
cmake ..
make -j$(nproc)
```

## bsquared938 | 2023-03-02T15:55:13+00:00
I'm trying to get this working on a raspberry pi 4.   I actually got another miner working on the pi but it's not nearly as configurable as xmrig. 

I'm wondering if the raspbian OS being 32-bit has anything to do with this.  I only learned more recently that the default OS is 32-bit. 

Specifically, libssl-dev cannot be found in the package list.  I've been trying to find ways around that one too.  







## SChernykh | 2023-03-03T06:56:42+00:00
@bsquared938 Only 64-bit OS will give you any meaningful hashrate on rpi4. You should get around 100 h/s on 64-bit and only 1-2 h/s on 32-bit, so I recommend switching to 64-bit and then compiling XMRig using standard instructions.

## bsquared938 | 2023-03-06T02:38:04+00:00
> @bsquared938 Only 64-bit OS will give you any meaningful hashrate on rpi4. You should get around 100 h/s on 64-bit and only 1-2 h/s on 32-bit, so I recommend switching to 64-bit and then compiling XMRig using standard instructions.

Okay I've been holding off on installing a 64-bit OS on the pi 4...

 I'm finding there's more things that I want that require it, so I'll pause this topic for now and try with the official steps once I've got 64-bit OS installed on it. 

Thanks to all who helped thus far...

## bsquared938 | 2023-03-16T14:22:41+00:00
Hi all,

Installing the 64-bit OS on the Pi 4 solved all the issues.  I had no issues compiling the code and installing dependencies. 

For anyone who happens to run into this topic, the "old" way of using a raspbian-nspawn-64 (https://github.com/sakaki-/raspbian-nspawn-64) no longer works.  The package is deprecated and I would also say not recommended a someone who has tried using 64-bit software on a 32-bit machine (on Linux, before this mining experiment) 

All other things I had running on my Pi 4 on the 32-bit OS work flawlessly on the 64-bit OS.  This includes a handful of docker containers and some other services kept running 24/7.

Good luck to anyone trying this! 64-bit OS is the answer, assuming your Pi has the hardware to run it. 

Over and out....closing this topic...

## dhow | 2024-03-18T11:07:49+00:00
Not for this but in my case by running `apt install build-essential pkgconf zlib1g-dev liblz4-dev libuv1-dev` I was able to get rid of the `fatal error: uv.h: No such file or directory` error and build the software I wanted. 

# Action History
- Created by: bsquared938 | 2023-02-23T21:50:14+00:00
- Closed at: 2023-03-16T14:22:41+00:00
