---
title: monerod - Illegal instruction
source_url: https://github.com/monero-project/monero/issues/4296
author: trasherdk
assignees: []
labels: []
created_at: '2018-08-23T12:04:29+00:00'
updated_at: '2018-08-24T01:18:07+00:00'
type: issue
status: closed
closed_at: '2018-08-24T01:18:07+00:00'
---

# Original Description
After compiling on one computer, running monerod on another give an "Illegal instruction" error.

Both are running Slackware64 14.2, both are up to date on all installed packages.

Compiling on: `Linux ghost-m1 4.4.144 #1 SMP Mon Aug 13 18:16:20 CEST 2018 x86_64 Intel(R) Xeon(R) CPU E3-1230 v5 @ 3.40GHz GenuineIntel GNU/Linux`
Testing on: `Linux compaq-laptop 4.4.144 #2 SMP Thu Jul 26 12:45:38 CDT 2018 x86_64 Intel(R) Core(TM)2 Duo CPU     T8100  @ 2.10GHz GenuineIntel GNU/Linux`

I can't figure out what the problem is. Everything looks good.


	bin$ ldd monerod
	        linux-vdso.so.1 (0x00007ffdc5fae000)
	        librt.so.1 => /lib64/librt.so.1 (0x00007fb750823000)
	        libdl.so.2 => /lib64/libdl.so.2 (0x00007fb75061f000)
	        libboost_chrono.so.1.59.0 => /usr/lib64/libboost_chrono.so.1.59.0 (0x00007fb750419000)
	        libboost_filesystem.so.1.59.0 => /usr/lib64/libboost_filesystem.so.1.59.0 (0x00007fb750202000)
	        libboost_program_options.so.1.59.0 => /usr/lib64/libboost_program_options.so.1.59.0 (0x00007fb74ff89000)
	        libboost_regex.so.1.59.0 => /usr/lib64/libboost_regex.so.1.59.0 (0x00007fb74fc88000)
	        libboost_system.so.1.59.0 => /usr/lib64/libboost_system.so.1.59.0 (0x00007fb74fa85000)
	        libzmq.so.5 => /usr/lib64/libzmq.so.5 (0x00007fb74f804000)
	        libsodium.so.23 => /usr/lib64/libsodium.so.23 (0x00007fb74f5ae000)
	        libreadline.so.6 => /usr/lib64/libreadline.so.6 (0x00007fb74f365000)
	        libtermcap.so.2 => /lib64/libtermcap.so.2 (0x00007fb74f162000)
	        libpcsclite.so.1 => /usr/lib64/libpcsclite.so.1 (0x00007fb74ef57000)
	        libunbound.so.2 => /usr/lib64/libunbound.so.2 (0x00007fb74ecae000)
	        libssl.so.1 => /lib64/libssl.so.1 (0x00007fb74ea3b000)
	        libcrypto.so.1 => /lib64/libcrypto.so.1 (0x00007fb74e5e7000)
	        libboost_date_time.so.1.59.0 => /usr/lib64/libboost_date_time.so.1.59.0 (0x00007fb74e3d6000)
	        libboost_serialization.so.1.59.0 => /usr/lib64/libboost_serialization.so.1.59.0 (0x00007fb74e19b000)
	        libboost_thread.so.1.59.0 => /usr/lib64/libboost_thread.so.1.59.0 (0x00007fb74df75000)
	        libstdc++.so.6 => /usr/lib64/libstdc++.so.6 (0x00007fb74dbf9000)
	        libm.so.6 => /lib64/libm.so.6 (0x00007fb74d8f0000)
	        libgcc_s.so.1 => /usr/lib64/libgcc_s.so.1 (0x00007fb74d6d9000)
	        libpthread.so.0 => /lib64/libpthread.so.0 (0x00007fb74d4bc000)
	        libc.so.6 => /lib64/libc.so.6 (0x00007fb74d0f3000)
	        /lib64/ld-linux-x86-64.so.2 (0x00007fb75140d000)
	        libicudata.so.56 => /usr/lib64/libicudata.so.56 (0x00007fb74b710000)
	        libicui18n.so.56 => /usr/lib64/libicui18n.so.56 (0x00007fb74b27f000)
	        libicuuc.so.56 => /usr/lib64/libicuuc.so.56 (0x00007fb74aee7000)
	        libunwind.so.8 => /usr/lib64/libunwind.so.8 (0x00007fb74accd000)
	        libevent-2.0.so.5 => /usr/lib64/libevent-2.0.so.5 (0x00007fb74aa85000)
	        liblzma.so.5 => /lib64/liblzma.so.5 (0x00007fb74a860000)



# Discussion History
## moneromooo-monero | 2018-08-23T13:34:59+00:00
Did you build it on the same machine ?

Try with the MONERO_USE_SOFTWARE_AES=1 env var.

## trasherdk | 2018-08-23T15:25:56+00:00
I build on the Xeon which has AES. The other don't.

So, you are probably right. I'll give it a try.

## trasherdk | 2018-08-23T16:19:54+00:00
Well, that wasn't it.

I can only find one reference to MONERO_USE_SOFTWARE_AES in function force_software_aes(void)
`/src/crypto/slow-hash.c:247:  const char *env = getenv("MONERO_USE_SOFTWARE_AES");`

There's a check_aes_hw(void) function, same file, line 260, doing some check.

In the builddir's CMakeCache.txt, line 302, there's a on/off for AES
`//Explicitly disable AES support
NO_AES:BOOL=OFF`

To be honest, I think the problem is elsewhere.

## trasherdk | 2018-08-23T17:02:53+00:00
In CMakeCache.txt, setting `NO_AES:BOOL=ON`

During make, I see a line on screen:
`-- AES support explicitly disabled`

After make, copying binaries to the test computer, I still get the "Illegal instruction" error.

## iDunk5400 | 2018-08-23T17:28:10+00:00
Add `-D ARCH="core2"` to the target you are building in the Makefile for your Penryn processor.

If you are making release `make -jX release`, then, in the cmake-release section, change the line `cd build/release && cmake -D CMAKE_BUILD_TYPE=Release ../..` to `cd build/release && cmake -D CMAKE_BUILD_TYPE=Release -D ARCH="core2" ../..`. Don't forget to remove the definition if you are building for Your Skylake-S again. Or, instead, make a new section in the Makefile for your Penryn CPU, preferably in a new local branch.

## moneromooo-monero | 2018-08-23T17:28:25+00:00
You might need to add some -march option if you want to build on one computer and run on another. I also seem to remember something about boost and AVX. If boost is linked statically, it might be that too.

## trasherdk | 2018-08-24T01:18:07+00:00
Okay. That ARCH thingy seems to do the trick. As I've got other CPU's than Core2 and Xeon,
I went with `x86-64` that, as far as I can figure, is generic enough, for my use.

Setting `ARCH:STRING=x86-64` in `build/CMakeCache.txt` line 19
or
Setting `set(ARCH x86-64 CACHE STRING "CPU to build for: -march value or 'default' to not pass -march at all")` in `monero-v0.12.3.0/CMakeLists.txt` line 490


# Action History
- Created by: trasherdk | 2018-08-23T12:04:29+00:00
- Closed at: 2018-08-24T01:18:07+00:00
