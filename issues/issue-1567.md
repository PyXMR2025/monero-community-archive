---
title: Can't build xmrig on raspbian BUSTER
source_url: https://github.com/xmrig/xmrig/issues/1567
author: Alekuso
assignees: []
labels: []
created_at: '2020-02-25T01:12:49+00:00'
updated_at: '2021-04-12T15:00:54+00:00'
type: issue
status: closed
closed_at: '2021-04-12T15:00:54+00:00'
---

# Original Description
**Describe the bug**
On the `make` command, I got two errors that I just can't find what is it and how can I fix it

**To Reproduce**
Just build it on a raspberry pi, on raspbian.

**Required data**
```
make[2]: *** [CMakeFiles/xmrig.dir/build.make:2714: xmrig] Error 1
make[1]: *** [CMakeFiles/Makefile2:73: CMakeFiles/xmrig.dir/all] Error 2
make: *** [Makefile:84: all] Error 2
```

**Additional context**
I already did builds on most branches/versions of xmrig, and they all fails with the same version.

# Discussion History
## Alekuso | 2020-02-25T02:58:14+00:00
After using #1102, there's the same error,
So, It's an `atomic` error,
The CPU type of the raspberry pi I use (a 3b+) is armv7l 4.19.97-v7+

For me, it's an "arm version" problem,
On the logs, there's "_atomic_load_**8**", and 8 can define `arm8`, and using an arm7l may affect this.

**Here's the full log of the error**
```
/usr/bin/ld: CMakeFiles/xmrig.dir/src/backend/opencl/OclWorker.cpp.o: in function `xmrig::OclWorker::consumeJob()':
OclWorker.cpp:(.text+0x35c): undefined reference to `__atomic_load_8'
/usr/bin/ld: OclWorker.cpp:(.text+0x38c): undefined reference to `__atomic_load_8'
/usr/bin/ld: CMakeFiles/xmrig.dir/src/backend/opencl/OclWorker.cpp.o: in function `xmrig::OclWorker::start()':
OclWorker.cpp:(.text+0x594): undefined reference to `__atomic_load_8'
/usr/bin/ld: OclWorker.cpp:(.text+0x608): undefined reference to `__atomic_load_8'
/usr/bin/ld: OclWorker.cpp:(.text+0x61c): undefined reference to `__atomic_load_8'
/usr/bin/ld: CMakeFiles/xmrig.dir/src/backend/opencl/OclWorker.cpp.o:OclWorker.cpp:(.text+0x6bc): more undefined references to `__atomic_load_8' follow
/usr/bin/ld: CMakeFiles/xmrig.dir/src/crypto/common/Nonce.cpp.o: in function `xmrig::Nonce::Nonce()':
Nonce.cpp:(.text+0x3c): undefined reference to `__atomic_store_8'
/usr/bin/ld: CMakeFiles/xmrig.dir/src/crypto/common/Nonce.cpp.o: in function `xmrig::Nonce::stop()':
Nonce.cpp:(.text+0x1a0): undefined reference to `__atomic_store_8'
/usr/bin/ld: CMakeFiles/xmrig.dir/src/crypto/common/Nonce.cpp.o: in function `xmrig::Nonce::touch()':
Nonce.cpp:(.text+0x1e0): undefined reference to `__atomic_fetch_add_8'
/usr/bin/ld: CMakeFiles/xmrig.dir/src/backend/common/Worker.cpp.o: in function `xmrig::Worker::storeStats()':
Worker.cpp:(.text+0x90): undefined reference to `__atomic_store_8'
/usr/bin/ld: Worker.cpp:(.text+0xbc): undefined reference to `__atomic_store_8'
/usr/bin/ld: CMakeFiles/xmrig.dir/src/backend/common/Worker.cpp.o: in function `xmrig::Worker::timestamp() const':
Worker.cpp:(.text._ZNK5xmrig6Worker9timestampEv[_ZNK5xmrig6Worker9timestampEv]+0x8): undefined reference to `__atomic_load_8'
/usr/bin/ld: CMakeFiles/xmrig.dir/src/backend/common/Worker.cpp.o: in function `xmrig::Worker::hashCount() const':
Worker.cpp:(.text._ZNK5xmrig6Worker9hashCountEv[_ZNK5xmrig6Worker9hashCountEv]+0x8): undefined reference to `__atomic_load_8'
/usr/bin/ld: CMakeFiles/xmrig.dir/src/backend/common/Workers.cpp.o: in function `xmrig::Workers<xmrig::CpuLaunchData>::stop()':
Workers.cpp:(.text._ZN5xmrig7WorkersINS_13CpuLaunchDataEE4stopEv[_ZN5xmrig7WorkersINS_13CpuLaunchDataEE4stopEv]+0x20): undefined reference to `__atomic_store_8'
/usr/bin/ld: Workers.cpp:(.text._ZN5xmrig7WorkersINS_13CpuLaunchDataEE4stopEv[_ZN5xmrig7WorkersINS_13CpuLaunchDataEE4stopEv]+0x9c): undefined reference to `__atomic_fetch_add_8'
/usr/bin/ld: CMakeFiles/xmrig.dir/src/backend/common/Workers.cpp.o: in function `xmrig::Workers<xmrig::CpuLaunchData>::tick(unsigned long long)':
Workers.cpp:(.text._ZN5xmrig7WorkersINS_13CpuLaunchDataEE4tickEy[_ZN5xmrig7WorkersINS_13CpuLaunchDataEE4tickEy]+0x38): undefined reference to `__atomic_load_8'
/usr/bin/ld: Workers.cpp:(.text._ZN5xmrig7WorkersINS_13CpuLaunchDataEE4tickEy[_ZN5xmrig7WorkersINS_13CpuLaunchDataEE4tickEy]+0x5c): undefined reference to `__atomic_load_8'
/usr/bin/ld: CMakeFiles/xmrig.dir/src/backend/common/Workers.cpp.o: in function `xmrig::Workers<xmrig::OclLaunchData>::stop()':
Workers.cpp:(.text._ZN5xmrig7WorkersINS_13OclLaunchDataEE4stopEv[_ZN5xmrig7WorkersINS_13OclLaunchDataEE4stopEv]+0x20): undefined reference to `__atomic_store_8'
/usr/bin/ld: Workers.cpp:(.text._ZN5xmrig7WorkersINS_13OclLaunchDataEE4stopEv[_ZN5xmrig7WorkersINS_13OclLaunchDataEE4stopEv]+0xdc): undefined reference to `__atomic_fetch_add_8'
/usr/bin/ld: CMakeFiles/xmrig.dir/src/backend/common/Workers.cpp.o: in function `xmrig::Workers<xmrig::OclLaunchData>::tick(unsigned long long)':
Workers.cpp:(.text._ZN5xmrig7WorkersINS_13OclLaunchDataEE4tickEy[_ZN5xmrig7WorkersINS_13OclLaunchDataEE4tickEy]+0x38): undefined reference to `__atomic_load_8'
/usr/bin/ld: Workers.cpp:(.text._ZN5xmrig7WorkersINS_13OclLaunchDataEE4tickEy[_ZN5xmrig7WorkersINS_13OclLaunchDataEE4tickEy]+0x5c): undefined reference to `__atomic_load_8'
/usr/bin/ld: CMakeFiles/xmrig.dir/src/backend/common/Workers.cpp.o: in function `xmrig::Workers<xmrig::CudaLaunchData>::stop()':
Workers.cpp:(.text._ZN5xmrig7WorkersINS_14CudaLaunchDataEE4stopEv[_ZN5xmrig7WorkersINS_14CudaLaunchDataEE4stopEv]+0x20): undefined reference to `__atomic_store_8'
/usr/bin/ld: Workers.cpp:(.text._ZN5xmrig7WorkersINS_14CudaLaunchDataEE4stopEv[_ZN5xmrig7WorkersINS_14CudaLaunchDataEE4stopEv]+0x9c): undefined reference to `__atomic_fetch_add_8'
/usr/bin/ld: CMakeFiles/xmrig.dir/src/backend/common/Workers.cpp.o: in function `xmrig::Workers<xmrig::CudaLaunchData>::tick(unsigned long long)':
Workers.cpp:(.text._ZN5xmrig7WorkersINS_14CudaLaunchDataEE4tickEy[_ZN5xmrig7WorkersINS_14CudaLaunchDataEE4tickEy]+0x38): undefined reference to `__atomic_load_8'
/usr/bin/ld: Workers.cpp:(.text._ZN5xmrig7WorkersINS_14CudaLaunchDataEE4tickEy[_ZN5xmrig7WorkersINS_14CudaLaunchDataEE4tickEy]+0x5c): undefined reference to `__atomic_load_8'
/usr/bin/ld: CMakeFiles/xmrig.dir/src/backend/common/Workers.cpp.o: in function `xmrig::Workers<xmrig::CpuLaunchData>::start(std::vector<xmrig::CpuLaunchData, std::allocator<xmrig::CpuLaunchData> > const&)':
Workers.cpp:(.text._ZN5xmrig7WorkersINS_13CpuLaunchDataEE5startERKSt6vectorIS1_SaIS1_EE[_ZN5xmrig7WorkersINS_13CpuLaunchDataEE5startERKSt6vectorIS1_SaIS1_EE]+0xd4): undefined reference to `__atomic_fetch_add_8'
/usr/bin/ld: CMakeFiles/xmrig.dir/src/backend/common/Workers.cpp.o: in function `xmrig::Workers<xmrig::OclLaunchData>::start(std::vector<xmrig::OclLaunchData, std::allocator<xmrig::OclLaunchData> > const&)':
Workers.cpp:(.text._ZN5xmrig7WorkersINS_13OclLaunchDataEE5startERKSt6vectorIS1_SaIS1_EE[_ZN5xmrig7WorkersINS_13OclLaunchDataEE5startERKSt6vectorIS1_SaIS1_EE]+0x200): undefined reference to `__atomic_fetch_add_8'
/usr/bin/ld: CMakeFiles/xmrig.dir/src/backend/common/Workers.cpp.o: in function `xmrig::Workers<xmrig::CudaLaunchData>::start(std::vector<xmrig::CudaLaunchData, std::allocator<xmrig::CudaLaunchData> > const&)':
Workers.cpp:(.text._ZN5xmrig7WorkersINS_14CudaLaunchDataEE5startERKSt6vectorIS1_SaIS1_EE[_ZN5xmrig7WorkersINS_14CudaLaunchDataEE5startERKSt6vectorIS1_SaIS1_EE]+0xd8): undefined reference to `__atomic_fetch_add_8'
/usr/bin/ld: CMakeFiles/xmrig.dir/src/backend/cpu/CpuWorker.cpp.o: in function `xmrig::CpuWorker<1u>::allocateRandomX_VM()':
CpuWorker.cpp:(.text._ZN5xmrig9CpuWorkerILj1EE18allocateRandomX_VMEv[_ZN5xmrig9CpuWorkerILj1EE18allocateRandomX_VMEv]+0x70): undefined reference to `__atomic_load_8'
/usr/bin/ld: CMakeFiles/xmrig.dir/src/backend/cpu/CpuWorker.cpp.o: in function `xmrig::CpuWorker<2u>::allocateRandomX_VM()':
CpuWorker.cpp:(.text._ZN5xmrig9CpuWorkerILj2EE18allocateRandomX_VMEv[_ZN5xmrig9CpuWorkerILj2EE18allocateRandomX_VMEv]+0x70): undefined reference to `__atomic_load_8'
/usr/bin/ld: CMakeFiles/xmrig.dir/src/backend/cpu/CpuWorker.cpp.o: in function `xmrig::CpuWorker<3u>::allocateRandomX_VM()':
CpuWorker.cpp:(.text._ZN5xmrig9CpuWorkerILj3EE18allocateRandomX_VMEv[_ZN5xmrig9CpuWorkerILj3EE18allocateRandomX_VMEv]+0x70): undefined reference to `__atomic_load_8'
/usr/bin/ld: CMakeFiles/xmrig.dir/src/backend/cpu/CpuWorker.cpp.o: in function `xmrig::CpuWorker<4u>::allocateRandomX_VM()':
CpuWorker.cpp:(.text._ZN5xmrig9CpuWorkerILj4EE18allocateRandomX_VMEv[_ZN5xmrig9CpuWorkerILj4EE18allocateRandomX_VMEv]+0x70): undefined reference to `__atomic_load_8'
/usr/bin/ld: CMakeFiles/xmrig.dir/src/backend/cpu/CpuWorker.cpp.o: in function `xmrig::CpuWorker<5u>::allocateRandomX_VM()':
CpuWorker.cpp:(.text._ZN5xmrig9CpuWorkerILj5EE18allocateRandomX_VMEv[_ZN5xmrig9CpuWorkerILj5EE18allocateRandomX_VMEv]+0x70): undefined reference to `__atomic_load_8'
/usr/bin/ld: CMakeFiles/xmrig.dir/src/backend/cpu/CpuWorker.cpp.o:CpuWorker.cpp:(.text._ZN5xmrig9CpuWorkerILj1EE10consumeJobEv[_ZN5xmrig9CpuWorkerILj1EE10consumeJobEv]+0x14): more undefined references to `__atomic_load_8' follow
collect2: error: ld returned 1 exit status
make[2]: *** [CMakeFiles/xmrig.dir/build.make:2714: xmrig] Error 1
make[1]: *** [CMakeFiles/Makefile2:73: CMakeFiles/xmrig.dir/all] Error 2
make: *** [Makefile:84: all] Error 2
```

## setuidroot | 2020-02-25T09:16:53+00:00
Okay there are a few things that may have caused this, but without a full build log (specifically the cflags/compile commands you used to build with) I can't say for sure what caused it.

But I can say with certainty: you have an ARMv7 CPU... this means you must build with the cflag (-DARM_TARGET=7) and/or modify CMakeLists.txt appropriately.

The rest I'll speculate: in your error log I see issues with Ocl (OpenCL) files.  Most likely you don't have any GPUs attached, so you should build it without the GPU code disabled using the two flags (-DWITH_OPENCL=OFF -DWITH_CUDA=OFF.)

Now you may or may not have libhwloc dependency installed (on an ARM box, i'd say it's probably not installed unless you compiled it yourself.)  So just disable hwloc, you don't need it anyways, it's just to help the automatic configuration of the CPU (build with -DWITH_HWLOC=OFF.)

Now you need libuv and OpenSSL installed... maybe try, as root: 

````
apt update -y && apt upgrade -y && apt install libuv openssl
````

If you can't find openssl package, just build without that (-DWITH_TLS=OFF.)  But you need libuv... try searching:

````
apt search libuv*
````

Install libuv package... if you don't have one in package manager, then you'll have to build it yourself (you can just use the ~/xmrig/scripts/build_deps.sh script to build it and then compile with the static libuv.a library.)  But I don't think you'll have a problem getting libuv from your package manager through so I'll stop typing :sweat: .

So to finalize my instructions here:

<br>

1. Make sure you have libuv and openssl installed as dependencies.  OpenSSL library might go by the package name "libssl" (try an "apt search ssl" to search for OpenSSL lib.)

2. Re-download xmrig's code is the cleanest way (but at a minimum, back out of your build directory and make a whole new different build folder.)

3. Re-download xmrig's code and change the CMakeLists.txt to this one I just modified for you: https://gist.githubusercontent.com/setuidroot/31e70ed0dbe98013b98c364b3c158309/raw/4d60fe57beea3465e7816c160f3c11e688e92266/CMakeLists.txt 

4. Forget this stupid numbered list... just do all of the commands listed below in your terminal (only apt install libuv openssl/libssl needs to run as root, so prefix with "sudo".)

Note: the first command below is only to change into the main non-root user directory.  Replace the * with your username (or use the output of "whoami" command.)  Or just build xmrig anywhere you'd like because it doesn't really matter (just for filesystem organization, which only matters on multi-user systems like company servers.)  If you want to get finicky, user builds of binaries not managed by the distro (xmrig would be an example) should go in /usr/local/src/; while user builds of packages that are managed by the distro (such as libuv and openssl) would go in /usr/src.  But I usually put user builds of non-distro packages in a build folder located in the user's home directory (/home/*your-username*.)

<br>


````
cd /home/*/  //or use the command below instead

cd /home/$(whoami)  //this won't work if logged in as root

git clone https://github.com/xmrig/xmrig.git

cd xmrig

mv CMakeLists.txt CMakeLists.txt.original

wget 'https://gist.githubusercontent.com/setuidroot/31e70ed0dbe98013b98c364b3c158309/raw/4d60fe57beea3465e7816c160f3c11e688e92266/CMakeLists.txt'

mkdir build && cd build

cmake .. -DCMAKE_BUILD_TYPE=Release -DARM_TARGET=7 -DWITH_OPENCL=OFF -DWITH_CUDA=OFF -DWITH_HWLOC=OFF

make -j 4
````

These steps to compile xmrig should have already been preceded by the installation of libuv and openssl dependencies as mentioned.

If you still have problems, let me know and I'll help you because I have a lot of experience compiling xmrig (on many ARM based devices) and it has been working fine for me on ARMv7 and ARMv8 devices.


=================

If the above build steps still fail, try removing TLS (openssl) and also ASM (assembly; isn't used on ARM builds anyways.)

In other words, if the above fails: delete the build directory, make a new one and build inside the new build directory with this full cmake command:

````
cmake .. -DCMAKE_BUILD_TYPE=Release -DARM_TARGET=7 -DWITH_OPENCL=OFF -DWITH_CUDA=OFF -DWITH_HWLOC=OFF -DWITH_TLS=OFF -DWITH_ASM=OFF

make -j 4 --environment-overrides --keep-going
````

If all of the above fail, please reply back with an output of the commands:

````
lscpu  //or: cat /proc/cpuinfo

uname -a
````

As a sidenote... I've experienced that "atomic" build error once before.  It happened to me when building in Termux (Android TV box.)  I never fully worked the issue out because I just downloaded an ARM binary that should have run on the device, but it did not run (crashed with some error... this was over a year ago  :thinking: .  Since a known working ARMv7 (NEON ISA used for fpu in the build, no AES) xmrig binary that I built wouldn't run on the system, I just gave up.  I've since realized that this problem was most likely caused by the fact that the TV box hardware and software didn't match up, which threw xmrig's compiling off.  The TV box had an ARMv8 (64 bit with AES) CPU and xmrig recognized this (the output of "lscpu" showed an 8-core, 64 bit ARMv8 CPU with AES and SHA extensions) but the userspace operating system was running a 32 bit version of Android.  This conflicting info between ARMv8 hardware (and a 64 bit kernel to back that up) combined with the 32 bit Android Operating system must have messed with my entire Termux environment because I had problems with other builds as well.  It wasn't just xmrig because I set it to build ARMv7/32 bit without AES but it failed... it even failed it run the good 32 bit xmrig build.  So I'm thinking it must have been a conflict that messed up Termux for me.

This is a really long way of saying you need to build for ARMv7 as your target (-DARM_TARGET=7.) :relieved:  Oh and don't build OpenCL or CUDA code... all of this is done in the CMakeLists.txt file I made for you, you shouldn't even need to add the build flags to the cmdline.

## setuidroot | 2020-02-25T10:06:34+00:00
My bad... the rPi 3B+ has an ARMv8 (64 bit) quad core Broadcom CPU. I assumed it was 32 bit (ARMv7) because you stated "armv7l" ... that tells me that you are probably running a 32 bit Linux kernel on a 64 bit capable CPU. There's nothing inherently wrong with that... personally I hate when they restrict hardware with software limitations, but there are actually some advantages to running a 32 bit OS 🤔 I don't remember what they are though 😂 (I'm thinking something along the lines of using more memory for program pointers with the longer 64 bit mem addresses.) For normal people running with a 32 bit kernel on such a device would be best because the main benefit to a 64 bit kernel is it allows more than 4GB max RAM and you can use hard drives larger than 2TB 🤔 but these are related to hardware that isn't relevant to your use case because the rPi 3B+ has only 1GB of LPDDR2 RAM.

This means you wont be able to run RandomX algos on that rPi board (you need over 3GB of RAM to run RandomX's dataset and still have some RAM for the system.) You won't really get good hashrates with that CPU either way... but I do a lot of this for fun.

So if setting the build target to ARMv7 doesn't work for you, then you have the same issue I had with that TV box I mentioned. Which means you'd need to run a 64 bit OS (with a 64 bit kernel; but all 64 bit userspace will have a 64 bit kernel.) To switch to a 64 bit OS I would download Debian and dd it to a microSD card. Running with a 64 bit kernel would give you better hashrate with xmrig, but you cannot run RandomX either way (except in slow/verification mode, which is a waste of energy.) Other algos that xmrig supports may run better with a 64 bit OS (so xmrig can use full 64 bit memory addresses; you don't have AES instructions with that CPU, thus switching to a 64 bit OS probably won't give much of an improvement.)

Anyways, here's a link to debian for rPi if you want to look into testing that out: https://wiki.debian.org/RaspberryPi

## Alekuso | 2020-02-25T14:40:14+00:00
> Okay there are a few things that may have caused this, but without a full build log (specifically the cflags/compile commands you used to build with) I can't say for sure what caused it.
> 
> But I can say with certainty: you have an ARMv7 CPU... this means you must build with the cflag (-DARM_TARGET=7) and/or modify CMakeLists.txt appropriately.
> 
> The rest I'll speculate: in your error log I see issues with Ocl (OpenCL) files. Most likely you don't have any GPUs attached, so you should build it without the GPU code disabled using the two flags (-DWITH_OPENCL=OFF -DWITH_CUDA=OFF.)
> 
> Now you may or may not have libhwloc dependency installed (on an ARM box, i'd say it's probably not installed unless you compiled it yourself.) So just disable hwloc, you don't need it anyways, it's just to help the automatic configuration of the CPU (build with -DWITH_HWLOC=OFF.)
> 
> Now you need libuv and OpenSSL installed... maybe try, as root:
> 
> ```
> apt update -y && apt upgrade -y && apt install libuv openssl
> ```
> 
> If you can't find openssl package, just build without that (-DWITH_TLS=OFF.) But you need libuv... try searching:
> 
> ```
> apt search libuv*
> ```
> 
> Install libuv package... if you don't have one in package manager, then you'll have to build it yourself (you can just use the ~/xmrig/scripts/build_deps.sh script to build it and then compile with the static libuv.a library.) But I don't think you'll have a problem getting libuv from your package manager through so I'll stop typing 😓 .
> 
> So to finalize my instructions here:
> 
> 
> 1. Make sure you have libuv and openssl installed as dependencies.  OpenSSL library might go by the package name "libssl" (try an "apt search ssl" to search for OpenSSL lib.)
> 2. Re-download xmrig's code is the cleanest way (but at a minimum, back out of your build directory and make a whole new different build folder.)
> 3. Re-download xmrig's code and change the CMakeLists.txt to this one I just modified for you: https://gist.githubusercontent.com/setuidroot/31e70ed0dbe98013b98c364b3c158309/raw/4d60fe57beea3465e7816c160f3c11e688e92266/CMakeLists.txt
> 4. Forget this stupid numbered list... just do all of the commands listed below in your terminal (only apt install libuv openssl/libssl needs to run as root, so prefix with "sudo".)
> 
> Note: the first command below is only to change into the main non-root user directory. Replace the * with your username (or use the output of "whoami" command.) Or just build xmrig anywhere you'd like because it doesn't really matter (just for filesystem organization, which only matters on multi-user systems like company servers.) If you want to get finicky, user builds of binaries not managed by the distro (xmrig would be an example) should go in /usr/local/src/; while user builds of packages that are managed by the distro (such as libuv and openssl) would go in /usr/src. But I usually put user builds of non-distro packages in a build folder located in the user's home directory (/home/_your-username_.)
> 
> 
> ```
> cd /home/*/  //or use the command below instead
> 
> cd /home/$(whoami)  //this won't work if logged in as root
> 
> git clone https://github.com/xmrig/xmrig.git
> 
> cd xmrig
> 
> mv CMakeLists.txt CMakeLists.txt.original
> 
> wget 'https://gist.githubusercontent.com/setuidroot/31e70ed0dbe98013b98c364b3c158309/raw/4d60fe57beea3465e7816c160f3c11e688e92266/CMakeLists.txt'
> 
> mkdir build && cd build
> 
> cmake .. -DCMAKE_BUILD_TYPE=Release -DARM_TARGET=7 -DWITH_OPENCL=OFF -DWITH_CUDA=OFF -DWITH_HWLOC=OFF
> 
> make -j 4
> ```
> 
> These steps to compile xmrig should have already been preceded by the installation of libuv and openssl dependencies as mentioned.
> 
> If you still have problems, let me know and I'll help you because I have a lot of experience compiling xmrig (on many ARM based devices) and it has been working fine for me on ARMv7 and ARMv8 devices.
> 
> =================
> 
> If the above build steps still fail, try removing TLS (openssl) and also ASM (assembly; isn't used on ARM builds anyways.)
> 
> In other words, if the above fails: delete the build directory, make a new one and build inside the new build directory with this full cmake command:
> 
> ```
> cmake .. -DCMAKE_BUILD_TYPE=Release -DARM_TARGET=7 -DWITH_OPENCL=OFF -DWITH_CUDA=OFF -DWITH_HWLOC=OFF -DWITH_TLS=OFF -DWITH_ASM=OFF
> 
> make -j 4 --environment-overrides --keep-going
> ```
> 
> If all of the above fail, please reply back with an output of the commands:
> 
> ```
> lscpu  //or: cat /proc/cpuinfo
> 
> uname -a
> ```
> 
> As a sidenote... I've experienced that "atomic" build error once before. It happened to me when building in Termux (Android TV box.) I never fully worked the issue out because I just downloaded an ARM binary that should have run on the device, but it did not run (crashed with some error... this was over a year ago 🤔 . Since a known working ARMv7 (NEON ISA used for fpu in the build, no AES) xmrig binary that I built wouldn't run on the system, I just gave up. I've since realized that this problem was most likely caused by the fact that the TV box hardware and software didn't match up, which threw xmrig's compiling off. The TV box had an ARMv8 (64 bit with AES) CPU and xmrig recognized this (the output of "lscpu" showed an 8-core, 64 bit ARMv8 CPU with AES and SHA extensions) but the userspace operating system was running a 32 bit version of Android. This conflicting info between ARMv8 hardware (and a 64 bit kernel to back that up) combined with the 32 bit Android Operating system must have messed with my entire Termux environment because I had problems with other builds as well. It wasn't just xmrig because I set it to build ARMv7/32 bit without AES but it failed... it even failed it run the good 32 bit xmrig build. So I'm thinking it must have been a conflict that messed up Termux for me.
> 
> This is a really long way of saying you need to build for ARMv7 as your target (-DARM_TARGET=7.) 😌 Oh and don't build OpenCL or CUDA code... all of this is done in the CMakeLists.txt file I made for you, you shouldn't even need to add the build flags to the cmdline.

So, first, I can't locate libuv via the package installer (`E: Unable to locate package libuv`)
For the `lscpu` command, I've got:
```
Architecture:        armv7l
Byte Order:          Little Endian
CPU(s):              4
On-line CPU(s) list: 0-3
Thread(s) per core:  1
Core(s) per socket:  4
Socket(s):           1
Vendor ID:           ARM
Model:               4
Model name:          Cortex-A53
Stepping:            r0p4
CPU max MHz:         1450.0000
CPU min MHz:         600.0000
BogoMIPS:            38.40
Flags:               half thumb fastmult vfp edsp neon vfpv3 tls vfpv4 idiva idivt vfpd32 lpae evtstrm crc32
```
And for the `uname -a`, it shows:
```
Linux raspberry 4.19.97-v7+ #1294 SMP Thu Jan 30 13:15:58 GMT 2020 armv7l GNU/Linux
```



**Complete build logs**
```
[  6%] Built target argon2
Scanning dependencies of target xmrig-notls
[  7%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/io/Console.cpp.o
[  7%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/cpu/CpuLaunchData.cpp.o
[  9%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/io/json/JsonChain.cpp.o
[  9%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/io/json/Json.cpp.o
[ 10%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/io/json/JsonRequest.cpp.o
[ 11%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/io/log/backends/ConsoleLog.cpp.o
[ 11%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/io/log/backends/FileLog.cpp.o
[ 12%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/io/log/FileLogWriter.cpp.o
[ 13%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/io/log/Log.cpp.o
In file included from /usr/include/c++/8/vector:69,
                 from /home/pi/xmrig/src/base/io/json/JsonChain.h:29,
                 from /home/pi/xmrig/src/base/io/json/JsonChain.cpp:27:
/usr/include/c++/8/bits/vector.tcc: In member function ‘void std::vector<_Tp, _Alloc>::_M_realloc_insert(std::vector<_Tp, _Alloc>::iterator, _Args&& ...) [with _Args = {rapidjson::GenericDocument<rapidjson::UTF8<char>, rapidjson::MemoryPoolAllocator<rapidjson::CrtAllocator>, rapidjson::CrtAllocator>}; _Tp = rapidjson::GenericDocument<rapidjson::UTF8<char>, rapidjson::MemoryPoolAllocator<rapidjson::CrtAllocator>, rapidjson::CrtAllocator>; _Alloc = std::allocator<rapidjson::GenericDocument<rapidjson::UTF8<char>, rapidjson::MemoryPoolAllocator<rapidjson::CrtAllocator>, rapidjson::CrtAllocator> >]’:
/usr/include/c++/8/bits/vector.tcc:413:7: note: parameter passing for argument of type ‘std::vector<rapidjson::GenericDocument<rapidjson::UTF8<char>, rapidjson::MemoryPoolAllocator<rapidjson::CrtAllocator>, rapidjson::CrtAllocator> >::iterator’ {aka ‘__gnu_cxx::__normal_iterator<rapidjson::GenericDocument<rapidjson::UTF8<char>, rapidjson::MemoryPoolAllocator<rapidjson::CrtAllocator>, rapidjson::CrtAllocator>*, std::vector<rapidjson::GenericDocument<rapidjson::UTF8<char>, rapidjson::MemoryPoolAllocator<rapidjson::CrtAllocator>, rapidjson::CrtAllocator> > >’} changed in GCC 7.1
       vector<_Tp, _Alloc>::
       ^~~~~~~~~~~~~~~~~~~
/usr/include/c++/8/bits/vector.tcc: In member function ‘bool xmrig::JsonChain::addFile(const char*)’:
/usr/include/c++/8/bits/vector.tcc:109:4: note: parameter passing for argument of type ‘__gnu_cxx::__normal_iterator<rapidjson::GenericDocument<rapidjson::UTF8<char>, rapidjson::MemoryPoolAllocator<rapidjson::CrtAllocator>, rapidjson::CrtAllocator>*, std::vector<rapidjson::GenericDocument<rapidjson::UTF8<char>, rapidjson::MemoryPoolAllocator<rapidjson::CrtAllocator>, rapidjson::CrtAllocator> > >’ changed in GCC 7.1
    _M_realloc_insert(end(), std::forward<_Args>(__args)...);
    ^~~~~~~~~~~~~~~~~
/usr/include/c++/8/bits/vector.tcc: In member function ‘bool xmrig::JsonChain::add(rapidjson::Document&&)’:
/usr/include/c++/8/bits/vector.tcc:109:4: note: parameter passing for argument of type ‘__gnu_cxx::__normal_iterator<rapidjson::GenericDocument<rapidjson::UTF8<char>, rapidjson::MemoryPoolAllocator<rapidjson::CrtAllocator>, rapidjson::CrtAllocator>*, std::vector<rapidjson::GenericDocument<rapidjson::UTF8<char>, rapidjson::MemoryPoolAllocator<rapidjson::CrtAllocator>, rapidjson::CrtAllocator> > >’ changed in GCC 7.1
    _M_realloc_insert(end(), std::forward<_Args>(__args)...);
    ^~~~~~~~~~~~~~~~~
[ 15%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/kernel/Base.cpp.o
[ 15%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/io/Watcher.cpp.o
[ 15%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/kernel/config/BaseConfig.cpp.o
[ 16%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/kernel/config/BaseTransform.cpp.o
/usr/include/c++/8/bits/vector.tcc: In member function ‘bool xmrig::JsonChain::addRaw(const char*)’:
/usr/include/c++/8/bits/vector.tcc:109:4: note: parameter passing for argument of type ‘__gnu_cxx::__normal_iterator<rapidjson::GenericDocument<rapidjson::UTF8<char>, rapidjson::MemoryPoolAllocator<rapidjson::CrtAllocator>, rapidjson::CrtAllocator>*, std::vector<rapidjson::GenericDocument<rapidjson::UTF8<char>, rapidjson::MemoryPoolAllocator<rapidjson::CrtAllocator>, rapidjson::CrtAllocator> > >’ changed in GCC 7.1
    _M_realloc_insert(end(), std::forward<_Args>(__args)...);
    ^~~~~~~~~~~~~~~~~
[ 17%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/kernel/Entry.cpp.o
[ 18%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/kernel/Env.cpp.o
[ 19%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/kernel/Platform.cpp.o
[ 19%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/kernel/Process.cpp.o
[ 20%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/kernel/Signals.cpp.o
[ 21%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/dns/Dns.cpp.o
[ 22%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/dns/DnsRecord.cpp.o
[ 23%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/http/Http.cpp.o
[ 23%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/stratum/BaseClient.cpp.o
[ 24%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/stratum/Client.cpp.o
[ 25%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/stratum/Job.cpp.o
[ 26%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/stratum/NetworkState.cpp.o
[ 26%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/stratum/Pool.cpp.o
[ 27%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/stratum/Pools.cpp.o
[ 28%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/stratum/ProxyUrl.cpp.o
In file included from /usr/include/c++/8/vector:69,
                 from /home/pi/xmrig/src/base/net/stratum/Pools.h:29,
                 from /home/pi/xmrig/src/base/net/stratum/Pools.cpp:26:
/usr/include/c++/8/bits/vector.tcc: In member function ‘void std::vector<_Tp, _Alloc>::_M_realloc_insert(std::vector<_Tp, _Alloc>::iterator, _Args&& ...) [with _Args = {xmrig::Pool}; _Tp = xmrig::Pool; _Alloc = std::allocator<xmrig::Pool>]’:
/usr/include/c++/8/bits/vector.tcc:413:7: note: parameter passing for argument of type ‘std::vector<xmrig::Pool>::iterator’ {aka ‘__gnu_cxx::__normal_iterator<xmrig::Pool*, std::vector<xmrig::Pool> >’} changed in GCC 7.1
       vector<_Tp, _Alloc>::
       ^~~~~~~~~~~~~~~~~~~
[ 29%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/stratum/Socks5.cpp.o
/usr/include/c++/8/bits/vector.tcc: In member function ‘void xmrig::Pools::load(const xmrig::IJsonReader&)’:
/usr/include/c++/8/bits/vector.tcc:109:4: note: parameter passing for argument of type ‘__gnu_cxx::__normal_iterator<xmrig::Pool*, std::vector<xmrig::Pool> >’ changed in GCC 7.1
    _M_realloc_insert(end(), std::forward<_Args>(__args)...);
    ^~~~~~~~~~~~~~~~~
[ 30%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/stratum/strategies/FailoverStrategy.cpp.o
[ 30%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/stratum/strategies/SinglePoolStrategy.cpp.o
[ 31%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/stratum/Url.cpp.o
[ 32%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/tools/Arguments.cpp.o
[ 33%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/tools/Buffer.cpp.o
[ 34%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/tools/String.cpp.o
[ 34%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/tools/Timer.cpp.o
[ 35%] Building C object CMakeFiles/xmrig-notls.dir/src/3rdparty/http-parser/http_parser.c.o
[ 36%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/api/Api.cpp.o
[ 37%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/api/Httpd.cpp.o
[ 38%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/api/requests/ApiRequest.cpp.o
[ 38%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/api/requests/HttpApiRequest.cpp.o
[ 39%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/http/HttpApiResponse.cpp.o
[ 40%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/http/HttpClient.cpp.o
[ 41%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/http/HttpContext.cpp.o
[ 42%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/http/HttpResponse.cpp.o
[ 42%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/http/HttpServer.cpp.o
[ 43%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/stratum/DaemonClient.cpp.o
[ 44%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/stratum/SelfSelectClient.cpp.o
[ 45%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/tools/TcpServer.cpp.o
[ 46%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/common/Hashrate.cpp.o
[ 46%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/common/Threads.cpp.o
[ 47%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/common/Worker.cpp.o
[ 48%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/common/Workers.cpp.o
/home/pi/xmrig/src/backend/common/Workers.cpp: In static member function ‘static xmrig::IWorker* xmrig::Workers<T>::create(xmrig::Thread<T>*) [with T = xmrig::CpuLaunchData]’:
/home/pi/xmrig/src/backend/common/Workers.cpp:194:63: warning: ‘new’ of type ‘xmrig::CpuWorker<1>’ with extended alignment 16 [-Waligned-new=]
         return new CpuWorker<1>(handle->id(), handle->config());
                                                               ^
/home/pi/xmrig/src/backend/common/Workers.cpp:194:63: note: uses ‘void* operator new(std::size_t)’, which does not have an alignment parameter
/home/pi/xmrig/src/backend/common/Workers.cpp:194:63: note: use ‘-faligned-new’ to enable C++17 over-aligned new support
/home/pi/xmrig/src/backend/common/Workers.cpp:197:63: warning: ‘new’ of type ‘xmrig::CpuWorker<2>’ with extended alignment 16 [-Waligned-new=]
         return new CpuWorker<2>(handle->id(), handle->config());
                                                               ^
/home/pi/xmrig/src/backend/common/Workers.cpp:197:63: note: uses ‘void* operator new(std::size_t)’, which does not have an alignment parameter
/home/pi/xmrig/src/backend/common/Workers.cpp:197:63: note: use ‘-faligned-new’ to enable C++17 over-aligned new support
/home/pi/xmrig/src/backend/common/Workers.cpp:200:63: warning: ‘new’ of type ‘xmrig::CpuWorker<3>’ with extended alignment 16 [-Waligned-new=]
         return new CpuWorker<3>(handle->id(), handle->config());
                                                               ^
/home/pi/xmrig/src/backend/common/Workers.cpp:200:63: note: uses ‘void* operator new(std::size_t)’, which does not have an alignment parameter
/home/pi/xmrig/src/backend/common/Workers.cpp:200:63: note: use ‘-faligned-new’ to enable C++17 over-aligned new support
/home/pi/xmrig/src/backend/common/Workers.cpp:203:63: warning: ‘new’ of type ‘xmrig::CpuWorker<4>’ with extended alignment 16 [-Waligned-new=]
         return new CpuWorker<4>(handle->id(), handle->config());
                                                               ^
/home/pi/xmrig/src/backend/common/Workers.cpp:203:63: note: uses ‘void* operator new(std::size_t)’, which does not have an alignment parameter
/home/pi/xmrig/src/backend/common/Workers.cpp:203:63: note: use ‘-faligned-new’ to enable C++17 over-aligned new support
/home/pi/xmrig/src/backend/common/Workers.cpp:206:63: warning: ‘new’ of type ‘xmrig::CpuWorker<5>’ with extended alignment 16 [-Waligned-new=]
         return new CpuWorker<5>(handle->id(), handle->config());
                                                               ^
/home/pi/xmrig/src/backend/common/Workers.cpp:206:63: note: uses ‘void* operator new(std::size_t)’, which does not have an alignment parameter
/home/pi/xmrig/src/backend/common/Workers.cpp:206:63: note: use ‘-faligned-new’ to enable C++17 over-aligned new support
[ 49%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/cpu/Cpu.cpp.o
[ 50%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/cpu/CpuBackend.cpp.o
[ 50%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/cpu/CpuConfig.cpp.o
[ 51%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/cpu/CpuThread.cpp.o
[ 52%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/cpu/CpuThreads.cpp.o
[ 53%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/cpu/CpuWorker.cpp.o
[ 53%] Building CXX object CMakeFiles/xmrig-notls.dir/src/App.cpp.o
In file included from /usr/include/c++/8/vector:69,
                 from /home/pi/xmrig/src/backend/cpu/CpuThreads.h:29,
                 from /home/pi/xmrig/src/backend/cpu/CpuThreads.cpp:29:
/usr/include/c++/8/bits/vector.tcc: In member function ‘void std::vector<_Tp, _Alloc>::_M_realloc_insert(std::vector<_Tp, _Alloc>::iterator, _Args&& ...) [with _Args = {const xmrig::CpuThread&}; _Tp = xmrig::CpuThread; _Alloc = std::allocator<xmrig::CpuThread>]’:
/usr/include/c++/8/bits/vector.tcc:413:7: note: parameter passing for argument of type ‘std::vector<xmrig::CpuThread>::iterator’ {aka ‘__gnu_cxx::__normal_iterator<xmrig::CpuThread*, std::vector<xmrig::CpuThread> >’} changed in GCC 7.1
       vector<_Tp, _Alloc>::
       ^~~~~~~~~~~~~~~~~~~
In file included from /usr/include/c++/8/vector:64,
                 from /home/pi/xmrig/src/backend/cpu/CpuThreads.h:29,
                 from /home/pi/xmrig/src/backend/cpu/CpuThreads.cpp:29:
/usr/include/c++/8/bits/stl_vector.h: In constructor ‘xmrig::CpuThreads::CpuThreads(size_t, uint32_t)’:
/usr/include/c++/8/bits/stl_vector.h:1085:4: note: parameter passing for argument of type ‘__gnu_cxx::__normal_iterator<xmrig::CpuThread*, std::vector<xmrig::CpuThread> >’ changed in GCC 7.1
    _M_realloc_insert(end(), __x);
    ^~~~~~~~~~~~~~~~~
/usr/include/c++/8/bits/stl_vector.h: In constructor ‘xmrig::CpuThreads::CpuThreads(const Value&)’:
/usr/include/c++/8/bits/stl_vector.h:1085:4: note: parameter passing for argument of type ‘__gnu_cxx::__normal_iterator<xmrig::CpuThread*, std::vector<xmrig::CpuThread> >’ changed in GCC 7.1
    _M_realloc_insert(end(), __x);
    ^~~~~~~~~~~~~~~~~
/usr/include/c++/8/bits/stl_vector.h:1085:4: note: parameter passing for argument of type ‘__gnu_cxx::__normal_iterator<xmrig::CpuThread*, std::vector<xmrig::CpuThread> >’ changed in GCC 7.1
    _M_realloc_insert(end(), __x);
    ^~~~~~~~~~~~~~~~~
In file included from /usr/include/c++/8/vector:69,
                 from /home/pi/xmrig/src/base/tools/String.h:30,
                 from /home/pi/xmrig/src/backend/common/Threads.h:33,
                 from /home/pi/xmrig/src/backend/cpu/CpuConfig.h:29,
                 from /home/pi/xmrig/src/backend/cpu/CpuConfig.cpp:26:
/usr/include/c++/8/bits/vector.tcc: In member function ‘void std::vector<_Tp, _Alloc>::_M_realloc_insert(std::vector<_Tp, _Alloc>::iterator, _Args&& ...) [with _Args = {const xmrig::Miner*&, const xmrig::Algorithm&, const xmrig::CpuConfig&, const xmrig::CpuThread&}; _Tp = xmrig::CpuLaunchData; _Alloc = std::allocator<xmrig::CpuLaunchData>]’:
/usr/include/c++/8/bits/vector.tcc:413:7: note: parameter passing for argument of type ‘std::vector<xmrig::CpuLaunchData>::iterator’ {aka ‘__gnu_cxx::__normal_iterator<xmrig::CpuLaunchData*, std::vector<xmrig::CpuLaunchData> >’} changed in GCC 7.1
       vector<_Tp, _Alloc>::
       ^~~~~~~~~~~~~~~~~~~
/usr/include/c++/8/bits/vector.tcc: In member function ‘std::vector<xmrig::CpuLaunchData> xmrig::CpuConfig::get(const xmrig::Miner*, const xmrig::Algorithm&) const’:
/usr/include/c++/8/bits/vector.tcc:109:4: note: parameter passing for argument of type ‘__gnu_cxx::__normal_iterator<xmrig::CpuLaunchData*, std::vector<xmrig::CpuLaunchData> >’ changed in GCC 7.1
    _M_realloc_insert(end(), std::forward<_Args>(__args)...);
    ^~~~~~~~~~~~~~~~~
[ 54%] Building CXX object CMakeFiles/xmrig-notls.dir/src/core/config/Config.cpp.o
[ 55%] Building CXX object CMakeFiles/xmrig-notls.dir/src/core/config/ConfigTransform.cpp.o
[ 56%] Building CXX object CMakeFiles/xmrig-notls.dir/src/core/Controller.cpp.o
[ 57%] Building CXX object CMakeFiles/xmrig-notls.dir/src/core/Miner.cpp.o
[ 57%] Building CXX object CMakeFiles/xmrig-notls.dir/src/net/JobResults.cpp.o
In file included from /usr/include/c++/8/map:60,
                 from /home/pi/xmrig/src/backend/common/Threads.h:29,
                 from /home/pi/xmrig/src/backend/cpu/CpuConfig.h:29,
                 from /home/pi/xmrig/src/core/config/Config.h:32,
                 from /home/pi/xmrig/src/core/Miner.cpp:39:
/usr/include/c++/8/bits/stl_tree.h: In function ‘std::_Rb_tree<_Key, _Val, _KeyOfValue, _Compare, _Alloc>::iterator std::_Rb_tree<_Key, _Val, _KeyOfValue, _Compare, _Alloc>::_M_emplace_hint_unique(std::_Rb_tree<_Key, _Val, _KeyOfValue, _Compare, _Alloc>::const_iterator, _Args&& ...) [with _Args = {const std::piecewise_construct_t&, std::tuple<xmrig::Algorithm::Id&&>, std::tuple<>}; _Key = xmrig::Algorithm::Id; _Val = std::pair<const xmrig::Algorithm::Id, double>; _KeyOfValue = std::_Select1st<std::pair<const xmrig::Algorithm::Id, double> >; _Compare = std::less<xmrig::Algorithm::Id>; _Alloc = std::allocator<std::pair<const xmrig::Algorithm::Id, double> >]’:
/usr/include/c++/8/bits/stl_tree.h:2411:7: note: parameter passing for argument of type ‘std::_Rb_tree<xmrig::Algorithm::Id, std::pair<const xmrig::Algorithm::Id, double>, std::_Select1st<std::pair<const xmrig::Algorithm::Id, double> >, std::less<xmrig::Algorithm::Id>, std::allocator<std::pair<const xmrig::Algorithm::Id, double> > >::const_iterator’ {aka ‘std::_Rb_tree_const_iterator<std::pair<const xmrig::Algorithm::Id, double> >’} changed in GCC 7.1
       _Rb_tree<_Key, _Val, _KeyOfValue, _Compare, _Alloc>::
       ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In file included from /usr/include/c++/8/map:61,
                 from /home/pi/xmrig/src/backend/common/Threads.h:29,
                 from /home/pi/xmrig/src/backend/cpu/CpuConfig.h:29,
                 from /home/pi/xmrig/src/core/config/Config.h:32,
                 from /home/pi/xmrig/src/core/Miner.cpp:39:
/usr/include/c++/8/bits/stl_map.h: In member function ‘void xmrig::MinerPrivate::getHashrate(rapidjson::Value&, rapidjson::Document&, int) const’:
/usr/include/c++/8/bits/stl_map.h:518:8: note: parameter passing for argument of type ‘std::_Rb_tree<xmrig::Algorithm::Id, std::pair<const xmrig::Algorithm::Id, double>, std::_Select1st<std::pair<const xmrig::Algorithm::Id, double> >, std::less<xmrig::Algorithm::Id>, std::allocator<std::pair<const xmrig::Algorithm::Id, double> > >::const_iterator’ {aka ‘std::_Rb_tree_const_iterator<std::pair<const xmrig::Algorithm::Id, double> >’} changed in GCC 7.1
    __i = _M_t._M_emplace_hint_unique(__i, std::piecewise_construct,
[ 58%] Building CXX object CMakeFiles/xmrig-notls.dir/src/net/Network.cpp.o
[ 59%] Building CXX object CMakeFiles/xmrig-notls.dir/src/net/strategies/DonateStrategy.cpp.o
[ 60%] Building CXX object CMakeFiles/xmrig-notls.dir/src/Summary.cpp.o
/usr/include/c++/8/bits/stl_map.h: In member function ‘void xmrig::Miner::printHashrate(bool)’:
/usr/include/c++/8/bits/stl_map.h:518:8: note: parameter passing for argument of type ‘std::_Rb_tree<xmrig::Algorithm::Id, std::pair<const xmrig::Algorithm::Id, double>, std::_Select1st<std::pair<const xmrig::Algorithm::Id, double> >, std::less<xmrig::Algorithm::Id>, std::allocator<std::pair<const xmrig::Algorithm::Id, double> > >::const_iterator’ {aka ‘std::_Rb_tree_const_iterator<std::pair<const xmrig::Algorithm::Id, double> >’} changed in GCC 7.1
    __i = _M_t._M_emplace_hint_unique(__i, std::piecewise_construct,
/usr/include/c++/8/bits/stl_map.h: In member function ‘virtual void xmrig::Miner::onTimer(const xmrig::Timer*)’:
/usr/include/c++/8/bits/stl_map.h:518:8: note: parameter passing for argument of type ‘std::_Rb_tree<xmrig::Algorithm::Id, std::pair<const xmrig::Algorithm::Id, double>, std::_Select1st<std::pair<const xmrig::Algorithm::Id, double> >, std::less<xmrig::Algorithm::Id>, std::allocator<std::pair<const xmrig::Algorithm::Id, double> > >::const_iterator’ {aka ‘std::_Rb_tree_const_iterator<std::pair<const xmrig::Algorithm::Id, double> >’} changed in GCC 7.1
    __i = _M_t._M_emplace_hint_unique(__i, std::piecewise_construct,
/usr/include/c++/8/bits/stl_map.h:518:8: note: parameter passing for argument of type ‘std::_Rb_tree<xmrig::Algorithm::Id, std::pair<const xmrig::Algorithm::Id, double>, std::_Select1st<std::pair<const xmrig::Algorithm::Id, double> >, std::less<xmrig::Algorithm::Id>, std::allocator<std::pair<const xmrig::Algorithm::Id, double> > >::const_iterator’ {aka ‘std::_Rb_tree_const_iterator<std::pair<const xmrig::Algorithm::Id, double> >’} changed in GCC 7.1
    __i = _M_t._M_emplace_hint_unique(__i, std::piecewise_construct,
[ 61%] Building CXX object CMakeFiles/xmrig-notls.dir/src/xmrig.cpp.o
[ 61%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/io/json/Json_unix.cpp.o
[ 62%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/kernel/Platform_unix.cpp.o
[ 63%] Building CXX object CMakeFiles/xmrig-notls.dir/src/App_unix.cpp.o
[ 64%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/common/VirtualMemory_unix.cpp.o
[ 65%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/common/LinuxMemory.cpp.o
[ 65%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/cpu/platform/BasicCpuInfo_arm.cpp.o
[ 66%] Building C object CMakeFiles/xmrig-notls.dir/src/crypto/cn/c_blake256.c.o
[ 67%] Building C object CMakeFiles/xmrig-notls.dir/src/crypto/cn/c_groestl.c.o
[ 68%] Building C object CMakeFiles/xmrig-notls.dir/src/crypto/cn/c_jh.c.o
[ 69%] Building C object CMakeFiles/xmrig-notls.dir/src/crypto/cn/c_skein.c.o
[ 69%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/cn/CnCtx.cpp.o
[ 70%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/cn/CnHash.cpp.o
[ 71%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/common/Algorithm.cpp.o
In file included from /home/pi/xmrig/src/crypto/cn/CnHash.cpp:35:
/home/pi/xmrig/src/crypto/cn/CryptoNight_arm.h: In function ‘__m128i _mm_aesenc_si128(__m128i, __m128i)’:
/home/pi/xmrig/src/crypto/cn/CryptoNight_arm.h:86:31: warning: requested alignment 16 is larger than 8 [-Wattributes]
     alignas(16) const __m128i zero = { 0 };
                               ^~~~
/home/pi/xmrig/src/crypto/cn/CryptoNight_arm.h: In function ‘__m128i aes_round_tweak_div(const __m128i&, const __m128i&)’:
/home/pi/xmrig/src/crypto/cn/CryptoNight_arm.h:400:29: warning: requested alignment 16 is larger than 8 [-Wattributes]
     alignas(16) uint32_t k[4];
                             ^
/home/pi/xmrig/src/crypto/cn/CryptoNight_arm.h:401:29: warning: requested alignment 16 is larger than 8 [-Wattributes]
     alignas(16) uint32_t x[4];
                             ^
[ 72%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/common/Coin.cpp.o
[ 73%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/common/HugePagesInfo.cpp.o
[ 73%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/common/keccak.cpp.o
[ 74%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/common/MemoryPool.cpp.o
[ 75%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/common/Nonce.cpp.o
[ 76%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/common/VirtualMemory.cpp.o
[ 76%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/randomx/aes_hash.cpp.o
[ 77%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/randomx/allocator.cpp.o
[ 78%] Building C object CMakeFiles/xmrig-notls.dir/src/crypto/randomx/argon2_core.c.o
[ 79%] Building C object CMakeFiles/xmrig-notls.dir/src/crypto/randomx/argon2_ref.c.o
[ 80%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/randomx/blake2_generator.cpp.o
[ 80%] Building C object CMakeFiles/xmrig-notls.dir/src/crypto/randomx/blake2/blake2b.c.o
[ 81%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/randomx/bytecode_machine.cpp.o
[ 82%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/randomx/dataset.cpp.o
[ 83%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/randomx/instructions_portable.cpp.o
In file included from /usr/include/c++/8/vector:69,
                 from /home/pi/xmrig/src/crypto/randomx/dataset.hpp:32,
                 from /home/pi/xmrig/src/crypto/randomx/dataset.cpp:43:
/usr/include/c++/8/bits/vector.tcc: In member function ‘void std::vector<_Tp, _Alloc>::_M_realloc_insert(std::vector<_Tp, _Alloc>::iterator, _Args&& ...) [with _Args = {const long long unsigned int&}; _Tp = long long unsigned int; _Alloc = std::allocator<long long unsigned int>]’:
/usr/include/c++/8/bits/vector.tcc:413:7: note: parameter passing for argument of type ‘std::vector<long long unsigned int>::iterator’ {aka ‘__gnu_cxx::__normal_iterator<long long unsigned int*, std::vector<long long unsigned int> >’} changed in GCC 7.1
       vector<_Tp, _Alloc>::
       ^~~~~~~~~~~~~~~~~~~
In file included from /usr/include/c++/8/vector:64,
                 from /home/pi/xmrig/src/crypto/randomx/dataset.hpp:32,
                 from /home/pi/xmrig/src/crypto/randomx/dataset.cpp:43:
/usr/include/c++/8/bits/stl_vector.h: In function ‘void randomx::initCache(randomx_cache*, const void*, size_t)’:
/usr/include/c++/8/bits/stl_vector.h:1085:4: note: parameter passing for argument of type ‘__gnu_cxx::__normal_iterator<long long unsigned int*, std::vector<long long unsigned int> >’ changed in GCC 7.1
    _M_realloc_insert(end(), __x);
    ^~~~~~~~~~~~~~~~~
[ 84%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/randomx/randomx.cpp.o
[ 84%] Building C object CMakeFiles/xmrig-notls.dir/src/crypto/randomx/reciprocal.c.o
[ 85%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/randomx/soft_aes.cpp.o
[ 86%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/randomx/superscalar.cpp.o
/home/pi/xmrig/src/crypto/randomx/randomx.cpp: In function ‘void randomx_calculate_hash(randomx_vm*, const void*, size_t, void*)’:
/home/pi/xmrig/src/crypto/randomx/randomx.cpp:475:34: warning: requested alignment 16 is larger than 8 [-Wattributes]
   alignas(16) uint64_t tempHash[8];
                                  ^
[ 87%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/randomx/virtual_machine.cpp.o
[ 88%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/randomx/virtual_memory.cpp.o
[ 88%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/randomx/vm_compiled_light.cpp.o
[ 89%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/randomx/vm_compiled.cpp.o
[ 90%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/randomx/vm_interpreted_light.cpp.o
[ 91%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/randomx/vm_interpreted.cpp.o
[ 92%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/rx/Rx.cpp.o
[ 92%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/rx/RxAlgo.cpp.o
[ 93%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/rx/RxBasicStorage.cpp.o
[ 95%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/rx/RxCache.cpp.o
[ 95%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/rx/RxConfig.cpp.o
[ 96%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/rx/RxDataset.cpp.o
[ 96%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/rx/RxQueue.cpp.o
/home/pi/xmrig/src/crypto/rx/RxDataset.cpp: In member function ‘void xmrig::RxDataset::setRaw(const void*)’:
/home/pi/xmrig/src/crypto/rx/RxDataset.cpp:177:11: warning: ‘void* memcpy(void*, const void*, size_t)’ pointer overflow between offset 0 and size [2181038080, 2147483647] [-Warray-bounds]
     memcpy(randomx_get_dataset_memory(m_dataset), raw, maxSize());
     ~~~~~~^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
/home/pi/xmrig/src/crypto/rx/RxDataset.cpp:177:11: warning: ‘void* memcpy(void*, const void*, size_t)’ specified size 2181038080 exceeds maximum object size 2147483647 [-Wstringop-overflow=]
[ 97%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/rx/RxVm.cpp.o
[ 98%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/argon2/Impl.cpp.o
[ 99%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/io/log/backends/SysLog.cpp.o
[100%] Linking CXX executable xmrig-notls
/usr/bin/ld: CMakeFiles/xmrig-notls.dir/src/crypto/common/Nonce.cpp.o: in function `xmrig::Nonce::Nonce()':
Nonce.cpp:(.text+0x3c): undefined reference to `__atomic_store_8'
/usr/bin/ld: CMakeFiles/xmrig-notls.dir/src/crypto/common/Nonce.cpp.o: in function `xmrig::Nonce::stop()':
Nonce.cpp:(.text+0x1a0): undefined reference to `__atomic_store_8'
/usr/bin/ld: CMakeFiles/xmrig-notls.dir/src/crypto/common/Nonce.cpp.o: in function `xmrig::Nonce::touch()':
Nonce.cpp:(.text+0x1e0): undefined reference to `__atomic_fetch_add_8'
/usr/bin/ld: CMakeFiles/xmrig-notls.dir/src/backend/common/Worker.cpp.o: in function `xmrig::Worker::storeStats()':
Worker.cpp:(.text+0x90): undefined reference to `__atomic_store_8'
/usr/bin/ld: Worker.cpp:(.text+0xbc): undefined reference to `__atomic_store_8'
/usr/bin/ld: CMakeFiles/xmrig-notls.dir/src/backend/common/Worker.cpp.o: in function `xmrig::Worker::timestamp() const':
Worker.cpp:(.text._ZNK5xmrig6Worker9timestampEv[_ZNK5xmrig6Worker9timestampEv]+0x8): undefined reference to `__atomic_load_8'
/usr/bin/ld: CMakeFiles/xmrig-notls.dir/src/backend/common/Worker.cpp.o: in function `xmrig::Worker::hashCount() const':
Worker.cpp:(.text._ZNK5xmrig6Worker9hashCountEv[_ZNK5xmrig6Worker9hashCountEv]+0x8): undefined reference to `__atomic_load_8'
/usr/bin/ld: CMakeFiles/xmrig-notls.dir/src/backend/common/Workers.cpp.o: in function `xmrig::Workers<xmrig::CpuLaunchData>::stop()':
Workers.cpp:(.text._ZN5xmrig7WorkersINS_13CpuLaunchDataEE4stopEv[_ZN5xmrig7WorkersINS_13CpuLaunchDataEE4stopEv]+0x20): undefined reference to `__atomic_store_8'
/usr/bin/ld: Workers.cpp:(.text._ZN5xmrig7WorkersINS_13CpuLaunchDataEE4stopEv[_ZN5xmrig7WorkersINS_13CpuLaunchDataEE4stopEv]+0x9c): undefined reference to `__atomic_fetch_add_8'
/usr/bin/ld: CMakeFiles/xmrig-notls.dir/src/backend/common/Workers.cpp.o: in function `xmrig::Workers<xmrig::CpuLaunchData>::tick(unsigned long long)':
Workers.cpp:(.text._ZN5xmrig7WorkersINS_13CpuLaunchDataEE4tickEy[_ZN5xmrig7WorkersINS_13CpuLaunchDataEE4tickEy]+0x38): undefined reference to `__atomic_load_8'
/usr/bin/ld: Workers.cpp:(.text._ZN5xmrig7WorkersINS_13CpuLaunchDataEE4tickEy[_ZN5xmrig7WorkersINS_13CpuLaunchDataEE4tickEy]+0x5c): undefined reference to `__atomic_load_8'
/usr/bin/ld: CMakeFiles/xmrig-notls.dir/src/backend/common/Workers.cpp.o: in function `xmrig::Workers<xmrig::CpuLaunchData>::start(std::vector<xmrig::CpuLaunchData, std::allocator<xmrig::CpuLaunchData> > const&)':
Workers.cpp:(.text._ZN5xmrig7WorkersINS_13CpuLaunchDataEE5startERKSt6vectorIS1_SaIS1_EE[_ZN5xmrig7WorkersINS_13CpuLaunchDataEE5startERKSt6vectorIS1_SaIS1_EE]+0xd4): undefined reference to `__atomic_fetch_add_8'
/usr/bin/ld: CMakeFiles/xmrig-notls.dir/src/backend/cpu/CpuWorker.cpp.o: in function `xmrig::CpuWorker<1u>::allocateRandomX_VM()':
CpuWorker.cpp:(.text._ZN5xmrig9CpuWorkerILj1EE18allocateRandomX_VMEv[_ZN5xmrig9CpuWorkerILj1EE18allocateRandomX_VMEv]+0x70): undefined reference to `__atomic_load_8'
/usr/bin/ld: CMakeFiles/xmrig-notls.dir/src/backend/cpu/CpuWorker.cpp.o: in function `xmrig::CpuWorker<2u>::allocateRandomX_VM()':
CpuWorker.cpp:(.text._ZN5xmrig9CpuWorkerILj2EE18allocateRandomX_VMEv[_ZN5xmrig9CpuWorkerILj2EE18allocateRandomX_VMEv]+0x70): undefined reference to `__atomic_load_8'
/usr/bin/ld: CMakeFiles/xmrig-notls.dir/src/backend/cpu/CpuWorker.cpp.o: in function `xmrig::CpuWorker<3u>::allocateRandomX_VM()':
CpuWorker.cpp:(.text._ZN5xmrig9CpuWorkerILj3EE18allocateRandomX_VMEv[_ZN5xmrig9CpuWorkerILj3EE18allocateRandomX_VMEv]+0x70): undefined reference to `__atomic_load_8'
/usr/bin/ld: CMakeFiles/xmrig-notls.dir/src/backend/cpu/CpuWorker.cpp.o: in function `xmrig::CpuWorker<4u>::allocateRandomX_VM()':
CpuWorker.cpp:(.text._ZN5xmrig9CpuWorkerILj4EE18allocateRandomX_VMEv[_ZN5xmrig9CpuWorkerILj4EE18allocateRandomX_VMEv]+0x70): undefined reference to `__atomic_load_8'
/usr/bin/ld: CMakeFiles/xmrig-notls.dir/src/backend/cpu/CpuWorker.cpp.o: in function `xmrig::CpuWorker<5u>::allocateRandomX_VM()':
CpuWorker.cpp:(.text._ZN5xmrig9CpuWorkerILj5EE18allocateRandomX_VMEv[_ZN5xmrig9CpuWorkerILj5EE18allocateRandomX_VMEv]+0x70): undefined reference to `__atomic_load_8'
/usr/bin/ld: CMakeFiles/xmrig-notls.dir/src/backend/cpu/CpuWorker.cpp.o:CpuWorker.cpp:(.text._ZN5xmrig9CpuWorkerILj1EE10consumeJobEv[_ZN5xmrig9CpuWorkerILj1EE10consumeJobEv]+0x14): more undefined references to `__atomic_load_8' follow
collect2: error: ld returned 1 exit status
make[2]: *** [CMakeFiles/xmrig-notls.dir/build.make:1826: xmrig-notls] Error 1
make[2]: Target 'CMakeFiles/xmrig-notls.dir/build' not remade because of errors.
make[1]: *** [CMakeFiles/Makefile2:73: CMakeFiles/xmrig-notls.dir/all] Error 2
make[1]: Target 'all' not remade because of errors.
make: *** [Makefile:84: all] Error 2
make: Target 'default_target' not remade because of errors.
```

## DocDrydenn | 2020-03-03T19:14:46+00:00
I did some testing: 
- Raspbian (Stretch) - No failures 
- Raspbian (Buster) - Exact same failure as above.

## Alekuso | 2020-03-04T20:10:27+00:00
> I did some testing:
> 
> * Raspbian (Stretch) - No failures
> * Raspbian (Buster) - Exact same failure as above.

Here's a link where I can download Raspbian Stretch lite ?

## DocDrydenn | 2020-03-04T20:26:10+00:00
Full - https://downloads.raspberrypi.org/raspbian/images/raspbian-2019-04-09/2019-04-08-raspbian-stretch.zip

Lite - http://downloads.raspberrypi.org/raspbian_lite/images/raspbian_lite-2019-04-09/2019-04-08-raspbian-stretch-lite.zip

## Alekuso | 2020-03-04T20:29:04+00:00
Gotta test it now and sees what happens . . .

## Alekuso | 2020-03-04T21:28:38+00:00
It's working now, Thanks all for your help !

## DocDrydenn | 2020-03-04T23:18:56+00:00
Wait... what do you mean it's working now?  Do you mean it compiles/builds on Raspbian (Buster) or do you mean you installed Raspbian (Stretch) and it worked. If it's the latter, then this issue should probably be left open until we get it fixed and working right on Raspbian (Buster).

## Alekuso | 2020-03-06T20:16:59+00:00
The build works on raspbian stretch*
And yeah, good idea, I'll open the issue for buster

## BroHowAreYou | 2020-05-18T22:27:48+00:00
Having this issue as well.

## James-yaoshenglong | 2020-05-27T14:29:21+00:00
Having this issue as well

## grahamreeds | 2020-05-28T12:49:41+00:00
Just a note that Xmrig compiles and runs fine on the new Raspberry OS (64bit kernal and userland) on a RPi3b+.  Gets 9.9H/s at stock clock :-)

I have a 4b8 ordered.

## Moreno-Borsalino | 2021-01-10T16:12:37+00:00
I have a Raspberry Pi 4 with Rasbian Buster and I compiled xmrig source code without problem.
Here it the steps to configure raspberry pi 4 with raspbian buster to compile xmrig:
open terminal windows and execute following steps:

sudo apt update
sudo apt full-upgrade
sudo apt-get clean
sudo shutdown -r now
sudo apt-get install -y raspbian-nspawn-64

Select Yes to enable 64-bit kernel and you should be prompted to reboot afterwards.

open terminal windows and execute following steps:
sudo ds64-shell
sudo apt-get update
sudo apt-get install git build-essential cmake libuv1-dev libssl-dev libhwloc-dev
git clone https://github.com/xmrig/xmrig.git
cd xmrig
mkdir build
cd build
cmake .. -DCMAKE_BUILD_TYPE=Release -DWITH_OPENCL=OFF -DWITH_CUDA=OFF
make

create config.json file with your mining pool data and start mining with:
sudo ./xmrig

I can get 40.50 H/s
Note that AES is not enabled. ARM CPU support AES but Broadcom and the RPi foundation did not license the h/w crypto extensions so AES is not available.
But I have a raspberry pi 4 with only 2 GB RAM so when running xmrig I get "not enough memory for RandomX dataset" and "failed to allocate RandomX dataset, switching to slow mode"

some data while mining:

[2021-01-10 16:29:34.091]  miner    speed 10s/60s/15m 39.96 40.13 39.85 H/s max 40.61 H/s
[2021-01-10 16:29:58.694]  net      new job from pool.minexmr.com:5555 diff 25000 algo rx/0 height 2271519
[2021-01-10 16:30:34.145]  miner    speed 10s/60s/15m 40.28 40.27 39.85 H/s max 40.61 H/s
[2021-01-10 16:31:34.203]  miner    speed 10s/60s/15m 40.59 40.40 39.98 H/s max 40.70 H/s
[2021-01-10 16:32:34.301]  miner    speed 10s/60s/15m 40.17 40.34 40.07 H/s max 40.70 H/s
[2021-01-10 16:33:24.836]  net      new job from pool.minexmr.com:5555 diff 25000 algo rx/0 height 2271520
[2021-01-10 16:33:34.365]  miner    speed 10s/60s/15m 40.16 40.38 40.07 H/s max 40.70 H/s
[2021-01-10 16:34:34.437]  miner    speed 10s/60s/15m 40.49 40.46 40.08 H/s max 40.70 H/s

And here it is the data just after start:

 * ABOUT        XMRig/6.7.0 gcc/8.3.0
 * LIBS         libuv/1.24.1 OpenSSL/1.1.1d hwloc/1.11.12
 * HUGE PAGES   supported
 * 1GB PAGES    unavailable
 * CPU          ARM Cortex-A72 (1) 64-bit -AES
                L2:0.0 MB L3:0.0 MB 4C/4T NUMA:1
 * MEMORY       1.5/1.8 GB (81%)
 * DONATE       0%
 * POOL #1      pool.minexmr.com:5555 coin monero
 * COMMANDS     hashrate, pause, resume, results, connection
 * HTTP API     0.0.0.0:12345 
[2021-01-10 16:09:28.922]  config   configuration saved to: "/root/xmrig/build/config.json"
[2021-01-10 16:09:29.004]  net      use pool pool.minexmr.com:5555  37.59.55.60
[2021-01-10 16:09:29.004]  net      new job from pool.minexmr.com:5555 diff 75000 algo rx/0 height 2271509
[2021-01-10 16:09:29.004]  cpu      use argon2 implementation default
[2021-01-10 16:09:30.204]  randomx  init dataset algo rx/0 (4 threads) seed 670f0b991dc3fe80...
[2021-01-10 16:09:30.204]  randomx  not enough memory for RandomX dataset
[2021-01-10 16:09:30.204]  randomx  failed to allocate RandomX dataset, switching to slow mode (1 ms)
[2021-01-10 16:09:33.009]  randomx  dataset ready (2804 ms)
[2021-01-10 16:09:33.009]  cpu      use profile  rx  (4 threads) scratchpad 2048 KB
[2021-01-10 16:09:33.011]  cpu      READY threads 4/4 (4) huge pages 0% 0/4 memory 8192 KB (2 ms)
[2021-01-10 16:09:59.570]  net      new job from pool.minexmr.com:5555 diff 75000 algo rx/0 height 2271510


## grahamreeds | 2021-01-11T01:28:20+00:00
You do not need nspawn.  Just enable 64bit after install and it builds fine.

With the 4gb and 8gb units you get ~100H/s and with a small overclock
~110H/s.

GR

On Sun, 10 Jan 2021, 16:12 Moreno Borsalino, <notifications@github.com>
wrote:

> I have a Raspberry Pi 4 with Rasbian Buster and I compiled xmrig source
> code without problem.
> Here it the steps to configure raspberry pi 4 with raspbian buster to
> compile xmrig:
> open terminal windows and execute following steps:
>
> sudo apt update
> sudo apt full-upgrade
> sudo apt-get clean
> sudo shutdown -r now
> sudo apt-get install -y raspbian-nspawn-64
>
> Select Yes to enable 64-bit kernel and you should be prompted to reboot
> afterwards.
>
> open terminal windows and execute following steps:
> sudo ds64-shell
> sudo apt-get update
> sudo apt-get install git build-essential cmake libuv1-dev libssl-dev
> libhwloc-dev
> git clone https://github.com/xmrig/xmrig.git
> cd xmrig
> mkdir build
> cd build
> cmake .. -DCMAKE_BUILD_TYPE=Release -DWITH_OPENCL=OFF -DWITH_CUDA=OFF
> make
>
> create config.json file with your mining pool data and start mining with:
> sudo ./xmrig
>
> I can get 40.50 H/s
> Note that AES is not enabled. ARM CPU support AES but Broadcom and the RPi
> foundation did not license the h/w crypto extensions so AES is not
> available.
> But I have a raspberry pi 4 with only 2 GB RAM so when running xmrig I get
> "not enough memory for RandomX dataset" and "failed to allocate RandomX
> dataset, switching to slow mode"
>
> some data while mining:
>
> [2021-01-10 16:29:34.091] miner speed 10s/60s/15m 39.96 40.13 39.85 H/s
> max 40.61 H/s
> [2021-01-10 16:29:58.694] net new job from pool.minexmr.com:5555 diff
> 25000 algo rx/0 height 2271519
> [2021-01-10 16:30:34.145] miner speed 10s/60s/15m 40.28 40.27 39.85 H/s
> max 40.61 H/s
> [2021-01-10 16:31:34.203] miner speed 10s/60s/15m 40.59 40.40 39.98 H/s
> max 40.70 H/s
> [2021-01-10 16:32:34.301] miner speed 10s/60s/15m 40.17 40.34 40.07 H/s
> max 40.70 H/s
> [2021-01-10 16:33:24.836] net new job from pool.minexmr.com:5555 diff
> 25000 algo rx/0 height 2271520
> [2021-01-10 16:33:34.365] miner speed 10s/60s/15m 40.16 40.38 40.07 H/s
> max 40.70 H/s
> [2021-01-10 16:34:34.437] miner speed 10s/60s/15m 40.49 40.46 40.08 H/s
> max 40.70 H/s
>
> And here it is the data just after start:
>
>    - ABOUT XMRig/6.7.0 gcc/8.3.0
>    - LIBS libuv/1.24.1 OpenSSL/1.1.1d hwloc/1.11.12
>    - HUGE PAGES supported
>    - 1GB PAGES unavailable
>    - CPU ARM Cortex-A72 (1) 64-bit -AES
>    L2:0.0 MB L3:0.0 MB 4C/4T NUMA:1
>    - MEMORY 1.5/1.8 GB (81%)
>    - DONATE 0%
>    - POOL #1 <https://github.com/xmrig/xmrig/issues/1>
>    pool.minexmr.com:5555 coin monero
>    - COMMANDS hashrate, pause, resume, results, connection
>    - HTTP API 0.0.0.0:12345
>    [2021-01-10 16:09:28.922] config configuration saved to:
>    "/root/xmrig/build/config.json"
>    [2021-01-10 16:09:29.004] net use pool pool.minexmr.com:5555
>    37.59.55.60
>    [2021-01-10 16:09:29.004] net new job from pool.minexmr.com:5555 diff
>    75000 algo rx/0 height 2271509
>    [2021-01-10 16:09:29.004] cpu use argon2 implementation default
>    [2021-01-10 16:09:30.204] randomx init dataset algo rx/0 (4 threads)
>    seed 670f0b991dc3fe80...
>    [2021-01-10 16:09:30.204] randomx not enough memory for RandomX dataset
>    [2021-01-10 16:09:30.204] randomx failed to allocate RandomX dataset,
>    switching to slow mode (1 ms)
>    [2021-01-10 16:09:33.009] randomx dataset ready (2804 ms)
>    [2021-01-10 16:09:33.009] cpu use profile rx (4 threads) scratchpad
>    2048 KB
>    [2021-01-10 16:09:33.011] cpu READY threads 4/4 (4) huge pages 0% 0/4
>    memory 8192 KB (2 ms)
>    [2021-01-10 16:09:59.570] net new job from pool.minexmr.com:5555 diff
>    75000 algo rx/0 height 2271510
>
> —
> You are receiving this because you commented.
> Reply to this email directly, view it on GitHub
> <https://github.com/xmrig/xmrig/issues/1567#issuecomment-757501022>, or
> unsubscribe
> <https://github.com/notifications/unsubscribe-auth/ABGL3HDR7ONQ7QDXQIJ4MB3SZHGYHANCNFSM4K2X7M5Q>
> .
>


## joebnb | 2021-02-21T13:50:07+00:00
same issue and not find solution,now i'm doloading old version of raspberry os,could xmrig contributor write a build example raspberryPi,or test it

## grahamreeds | 2021-02-22T10:01:23+00:00
What is your exact issue?

With a fresh install of Raspberry OS on a Pi4/4 I can install xmrig and
have it up and running in 30 minutes.

GR

Sent from my Nexus 10

On Sun, 21 Feb 2021, 13:50 chenbo, <notifications@github.com> wrote:

> same issue and not find solution,now i'm doloading old version of
> raspberry os,could xmrig contributor write a build example raspberryPi,or
> test it
>
> —
> You are receiving this because you commented.
> Reply to this email directly, view it on GitHub
> <https://github.com/xmrig/xmrig/issues/1567#issuecomment-782861298>, or
> unsubscribe
> <https://github.com/notifications/unsubscribe-auth/ABGL3HH3JCZRADXMFEILD2TTAEFSFANCNFSM4K2X7M5Q>
> .
>


## joebnb | 2021-02-22T10:09:07+00:00
release source code can't compile to executetable and out put 

```shell
make[2]: *** [CMakeFiles/xmrig.dir/src/crypto/cn/cnhash.cpp.o] error 1
make[1]: *** [CMakeFiles/Makefile2:73: CMakeFiles/xmrig.dir/all] Error 2
make: *** [Makefile:84: all] Error 2
```

and i was try all raspbian issue to make it work，but didn't. a lot of folks were discuss about raspbian compile.if there have a guide maybe better and efficient

## grahamreeds | 2021-02-22T11:45:42+00:00
Just grabbed v6.9.0 and see chenbo issue.

This is not the issue which the OP had.

GR

Sent from my Nexus 10

On Mon, 22 Feb 2021, 10:09 chenbo, <notifications@github.com> wrote:

> release source code can't compile to executetable and out put
>
> make[2]: *** [CMakeFiles/xmrig.dir/src/crypto/cn/cnhash.cpp.o] error 1
>
> make[1]: *** [CMakeFiles/Makefile2:73: CMakeFiles/xmrig.dir/all] Error 2
>
> make: *** [Makefile:84: all] Error 2
>
> and i was try all raspbian issue to make it work，but didn't. a lot of
> folks were discuss about raspbian compile.if there have a guide maybe
> better and efficient
>
> —
> You are receiving this because you commented.
> Reply to this email directly, view it on GitHub
> <https://github.com/xmrig/xmrig/issues/1567#issuecomment-783257855>, or
> unsubscribe
> <https://github.com/notifications/unsubscribe-auth/ABGL3HCMY4IAIWFOVVPP663TAIUNHANCNFSM4K2X7M5Q>
> .
>


## joebnb | 2021-02-23T10:59:14+00:00
> Just grabbed v6.9.0 and see chenbo issue. This is not the issue which the OP had. GR
> […](#)
> Sent from my Nexus 10
> On Mon, 22 Feb 2021, 10:09 chenbo, ***@***.***> wrote: release source code can't compile to executetable and out put make[2]: *** [CMakeFiles/xmrig.dir/src/crypto/cn/cnhash.cpp.o] error 1 make[1]: *** [CMakeFiles/Makefile2:73: CMakeFiles/xmrig.dir/all] Error 2 make: *** [Makefile:84: all] Error 2 and i was try all raspbian issue to make it work，but didn't. a lot of folks were discuss about raspbian compile.if there have a guide maybe better and efficient — You are receiving this because you commented. Reply to this email directly, view it on GitHub <[#1567 (comment)](https://github.com/xmrig/xmrig/issues/1567#issuecomment-783257855)>, or unsubscribe <https://github.com/notifications/unsubscribe-auth/ABGL3HCMY4IAIWFOVVPP663TAIUNHANCNFSM4K2X7M5Q> .


apologize for my words,i have  done after  a  refresh  setup, newest  os  and 64bit  kernel, above solution works  for  my case ,and  i  think it could resolve many cases 

# Action History
- Created by: Alekuso | 2020-02-25T01:12:49+00:00
- Closed at: 2021-04-12T15:00:54+00:00
