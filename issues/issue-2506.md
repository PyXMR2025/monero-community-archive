---
title: Official XMRIG iOS Build
source_url: https://github.com/xmrig/xmrig/issues/2506
author: quimodotcom
assignees: []
labels: []
created_at: '2021-08-01T14:44:13+00:00'
updated_at: '2026-01-25T16:20:38+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
No description

# Discussion History
## quimodotcom | 2021-08-01T15:25:04+00:00
I mean for jailbroken devices. Not for actual ios app store. Unless you want to

## quimodotcom | 2021-08-01T19:15:26+00:00
no one ever told people how to set it up/make a tutroial : https://github.com/xmrig/xmrig/issues/666

## Torrekie | 2021-12-03T08:02:49+00:00
it is possible but not quite as easy as just cross compiling, since they are using some Apple specific JIT API which was added since Darwin 20 (macOS 11 & iOS 14), that was something private on iOS
```
/* src/crypto/common/VirtualMemory_unix.cpp */

bool xmrig::VirtualMemory::protectRX(void *p, size_t size)
{
#   if defined(XMRIG_OS_APPLE) && defined(XMRIG_ARM)
    pthread_jit_write_protect_np(true);
    flushInstructionCache(p, size);
    return true;
#   else
    return mprotect(p, size, PROT_READ | PROT_EXEC) == 0;
#   endif
}
```
If you attempts to compile it directly to iOS, you will see this error:
```
undef: _pthread_jit_write_protect_np
Undefined symbols for architecture arm64:
  "_pthread_jit_write_protect_np", referenced from:
      xmrig::VirtualMemory::protectRW(void*, unsigned long) in VirtualMemory_unix.cpp.o
      xmrig::VirtualMemory::protectRX(void*, unsigned long) in VirtualMemory_unix.cpp.o
      xmrig::VirtualMemory::allocateExecutableMemory(unsigned long, bool) in VirtualMemory_unix.cpp.o
ld: symbol(s) not found for architecture arm64
clang: error: linker command failed with exit code 1 (use -v to see invocation)
...
```
We might be able to compile an older version of xmrig which not using this API but that was definitely not a good choice, for this shit to work on iOS, we should link to `libsystem_pthread.dylib` which were "umbrellaed" under `libSystem`. We can't do this with a standard iOS SDK which provided by Xcode, you also need some headers from macOS SDK, and a bunch of Device Support files under `~/Library/Developer/Xcode/iOS DeviceSupport` (or extract a dyld shared cache file from your iOS device), these are the runtime libraries containing all symbols you need.
Then add some linker flags probably like that
`LDFLAGS="-L/Users/torrekie/Library/Developer/Xcode/iOS\ DeviceSupport/14.2\ (18B92)\ arm64e/Symbols/usr/lib/system -lsystem_pthread -Wl,-umbrella,System" cmake ...`
But I can't do this now cuz I ruined my jailbreak few days ago. Maybe I'll try to build xmrig for iOS once I can jailbreak again someday

## romeno-moreno | 2021-12-04T23:22:13+00:00
For my project I ended up just generating macOS Xcode project, converting it to iOS and then fixing all errors one by one for a few weeks
As Torrekie stated, there's problems with JIT, so I could make RandomX work only in interpreted mode, which is very slow. But if you try to run moneroocean fork of xmrig, you'll see that mac processors (M1, M1 Pro) never use rx algorithms, as they are much more effective in astrobwt, cryptonight, argon, etc (pay hashrate is ~5-6 KH/s compared to 2-2.5 KH/s for rx), so I'd look at MO fork anyways
You can take a look at my project here: https://github.com/romeno-moreno/mxmrig


## Torrekie | 2021-12-05T09:32:24+00:00
I tried to remove Secure JIT APIs from XMRig and successfully compiled to iOS, a simple patch is available [here](https://github.com/Torrekie/Procursus/blob/xmrig/build_patch/xmrig/avoid-secure-jit-on-ios.patch), and I have submitted this to my [personal repo](https://apt.torrekie.com)

If you want to cross compile this to iOS by your self, follow these steps
### On macOS
1. Install [Homebrew](https://brew.sh)
2. Open your Terminal and install `cmake` by executing `brew install cmake`
3. Download the latest release source tarballs from [here](https://github.com/xmrig/xmrig/releases)
4. Extract the archive, then change your terminal work path to the extracted directory
5. You would also need `libuv`, `openssl` and `hwloc` compiled, or download prebuilt binaries from [My Repo](https://apt.torrekie.com/pre-release/debs)
6. Run `LDFLAGS="-framework CoreFoundation" xcrun --sdk iphoneos cmake -DWITH_OPENCL=OFF -DWITH_SECURE_JIT=OFF`, you might also need to add `-DUV_LIBRARY=` `-DOPENSSL_CRYPTO_LIBRARY=` `-DOPENSSL_SSL_LIBRARY=` and fill in the path of the corresponding library after the equal sign
7. After you see "Configuration done", run `make` to start building
8. If everything as expected, you will see a generated executable file which named `xmrig` under your build path

## UnixCro | 2022-02-07T14:45:51+00:00
I "simply" managed to compile it by using the open source ISH Shell and using XMRig's instructions for self-compilation under Alpine.  Compiling took 1 hour and 30 minutes under my A13 Bionic chip.  It is most likely not XMRig or something similar, but the terminal itself. I will point this out to the ISH developers in the forum.  But now it comes.  XMRig as soon as it is executed, I immediately only get the message "Illegal Instructions" .  This case is known in some other XMRig issues, but only on Raspberrys.  XMRig itself recommended setting "av" to False in the config.json file.  Unfortunately, I can't find an "av" in the file, so I don't know what to do next.  

```

HostName:~/xmrig-6.16.4/build# uname -a
Linux HostName 4.20.69-ish iSH 1.2.3 (298) Dec 17 2021 06:08:24 i686 Linux

HostName:~/xmrig-6.16.4/build# make
7%] Built target ghostrider
10%] Built target argon2
11%] Built target ethash
[100%] Built target xmrig

HostName:~/xmrig-6.16.4/build#./xmrig --stress
Illegal instruction
```
Thank you for reading.


## quimodotcom | 2022-02-16T16:48:51+00:00
> I tried to remove Secure JIT APIs from XMRig and successfully compiled to iOS, a simple patch is available [here](https://github.com/Torrekie/Procursus/blob/xmrig/build_patch/xmrig/avoid-secure-jit-on-ios.patch), and I have submitted this to my [personal repo](https://apt.torrekie.com)
> 
> If you want to cross compile this to iOS by your self, follow these steps
> 
> ### On macOS
> 1. Install [Homebrew](https://brew.sh)
> 2. Open your Terminal and install `cmake` by executing `brew install cmake`
> 3. Download the latest release source tarballs from [here](https://github.com/xmrig/xmrig/releases)
> 4. Extract the archive, then change your terminal work path to the extracted directory
> 5. You would also need `libuv`, `openssl` and `hwloc` compiled, or download prebuilt binaries from [My Repo](https://apt.torrekie.com/pre-release/debs)
> 6. Run `LDFLAGS="-framework CoreFoundation" xcrun --sdk iphoneos cmake -DWITH_OPENCL=OFF -DWITH_SECURE_JIT=OFF`, you might also need to add `-DUV_LIBRARY=` `-DOPENSSL_CRYPTO_LIBRARY=` `-DOPENSSL_SSL_LIBRARY=` and fill in the path of the corresponding library after the equal sign
> 7. After you see "Configuration done", run `make` to start building
> 8. If everything as expected, you will see a generated executable file which named `xmrig` under your build path

Installing the xmrig package from your repo gives me a “half-install” error or “half-configured” due to a non working sh script in the package. Please fix ASAP!

## Torrekie | 2022-02-16T16:59:39+00:00
> 

You should stop using my repo since there's still many unresolved problems, you might want to just install XMRig from deb package instead of installing from APT.
btw, if you have crashlogs in Cr4shed or somewhere else (e.g. Filza), I could give you some help

## quimodotcom | 2022-02-16T18:27:34+00:00
> You should stop using my repo since there's still many unresolved problems, you might want to just install XMRig from deb package instead of installing from APT.
> btw, if you have crashlogs in Cr4shed or somewhere else (e.g. Filza), I could give you some help

Where do I get the xmrig deb package

## UnixCro | 2022-09-20T13:54:08+00:00
Even if we manage to get xmrig working on iSH, we will see an embarrassingly low hash rate because iSH is constantly translating command line code to the Arm64 processor.  Those trying to compile it know how quickly their battery life has decreased and how many hours it has taken with such a powerful processor.  Don't use iSH Shell.  Use A Shell.  A-Shell would be able to run xmrig right out of the box I believe and we would only be making a profit for such a simple wattage.  The terminal is so well adapted to the processor that even an ffmpeg benchmark could beat my S22, which creates over 1K hashes with xmrig.  The iPhone is 3x more efficient than an Android phone and would generate more hashes.  I'm talking 2W at 1000+ H/s with no Huge Pages and MSR.  The only problem is that cmake doesn't work and that's why I finally decided to write this comment about it.  Is there any way to compile xmrig without cmake?  Using make is doable, cmake isn't currently, the developer of this shell told me it would be way too hard to get cmake to work.  Any idea?

## Torrekie | 2022-09-21T09:47:24+00:00
we are running on iOS natively but not using any 3rd party tools like iSH or A-Shell, the problem of it is described as above: `pthread_jit` API was not fully implemented on iOS, in another word, xmrig is using a macOS specific configuration that cannot use on iOS.
As the code described in [libpthread](https://github.com/apple-oss-distributions/libpthread/blob/cf9e1c7e611440e511af230905be2cfefc5c6121/src/pthread.c#L1165), corresponding features was only present in macOS, the symbol we are seeing in iOS was just a stub. So I've write a [patch](https://github.com/Torrekie/Procursus/blob/xmrig/build_patch/xmrig/avoid-secure-jit-on-ios.patch) to use a general JIT method instead of Secure JIT. This makes xmrig working under jailbroken iOS environment

## Vyeche | 2026-01-25T16:01:10+00:00
> For my project I ended up just generating macOS Xcode project, converting it to iOS and then fixing all errors one by one for a few weeks As Torrekie stated, there's problems with JIT, so I could make RandomX work only in interpreted mode, which is very slow. But if you try to run moneroocean fork of xmrig, you'll see that mac processors (M1, M1 Pro) never use rx algorithms, as they are much more effective in astrobwt, cryptonight, argon, etc (pay hashrate is ~5-6 KH/s compared to 2-2.5 KH/s for rx), so I'd look at MO fork anyways You can take a look at my project here: https://github.com/romeno-moreno/mxmrig

Hmm, the project works great. I would like to modify the pool url to my XMRig-Proxy is that possible? (I tried adding a config.json via sideloadly but it wouldnt take it for some reason and continue to override.)

**Update**
- I just had to let it sit there and then it picked up my files.

# Action History
- Created by: quimodotcom | 2021-08-01T14:44:13+00:00
