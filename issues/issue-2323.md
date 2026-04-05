---
title: Problem building for macOS-arm64
source_url: https://github.com/xmrig/xmrig/issues/2323
author: RS102839
assignees: []
labels: []
created_at: '2021-04-28T16:31:06+00:00'
updated_at: '2021-05-04T20:04:14+00:00'
type: issue
status: closed
closed_at: '2021-05-04T18:00:50+00:00'
---

# Original Description
**Describe the bug**
Directions for building for macOS-arm64 do not allow for a successful build of a macOS-arm64 executable

**To Reproduce**
- Clone the repo on a macOS Mini with ARM64 
- Attempt to follow instructions for a successful build

**Expected behavior**
Should successfully build a macOS-arm64 executable

(update) **RESOLUTION** SEE COMMENT AT END -  I was using x86_64 CMAKE not ARM64 CMAKE  

**Required data**
% mkdir build
% cd scripts
% ./build_deps.sh       __[ Comment: Needed to build dependencies, not in instructions !!  ]__

    [SNIP]

% cd ../build
% cmake .. -DOPENSSL_ROOT_DIR=/usr/local/opt/openssl -DHWLOC_INCLUDE_DIR=../scripts/deps/include     -DHWLOC_LIBRARY=../scripts/deps/lib/libhwloc.a

    -- WITH_MSR=OFF
    -- argon2: detecting feature 'sse2'...
    -- argon2: feature 'sse2' detected!
    -- argon2: detecting feature 'ssse3'...
    -- argon2: feature 'ssse3' detected!
    -- argon2: detecting feature 'xop'...
    -- argon2: detecting feature 'avx2'...
    -- argon2: feature 'avx2' detected!
    -- argon2: detecting feature 'avx512f'...
    -- argon2: feature 'avx512f' detected!
    -- Found OpenSSL: /usr/local/opt/openssl/lib/libcrypto.a (found version "1.1.1k")  
    -- Configuring done
    -- Generating done
    -- Build files have been written to: [REDACTED]/xmrig-m1/build

% make -j$(sysctl -n hw.logicalcpu)

    Scanning dependencies of target xmrig-asm
    [  0%] Building C object src/3rdparty/argon2/CMakeFiles/argon2-avx2.dir/arch/x86_64/lib/argon2-avx2.c.o
    [  0%] Building C object src/3rdparty/argon2/CMakeFiles/argon2-ssse3.dir/arch/x86_64/lib/argon2-ssse3.c.o
    [  1%] Building C object src/3rdparty/argon2/CMakeFiles/argon2-sse2.dir/arch/x86_64/lib/argon2-sse2.c.o
    [  2%] Building C object src/3rdparty/argon2/CMakeFiles/argon2-avx512f.dir/arch/x86_64/lib/argon2-avx512f.c.o
    [  3%] Building ASM object CMakeFiles/xmrig-asm.dir/src/crypto/cn/asm/cn_main_loop.S.o
    [  3%] Building C object src/3rdparty/argon2/CMakeFiles/argon2-xop.dir/arch/x86_64/lib/argon2-xop.c.o
    [  3%] Building ASM object CMakeFiles/xmrig-asm.dir/src/crypto/cn/asm/CryptonightR_template.S.o
    [  3%] Building C object src/3rdparty/libethash/CMakeFiles/ethash.dir/ethash_internal.c.o
    [  3%] Building C object src/3rdparty/libethash/CMakeFiles/ethash.dir/keccakf800.c.o
    [  4%] Linking C static library libargon2-xop.a
    [  5%] Linking C static library libxmrig-asm.a
    [  5%] Built target xmrig-asm
    [  5%] Built target argon2-xop
    [  5%] Linking C static library libargon2-sse2.a
    [  5%] Linking C static library libargon2-avx512f.a
    [  6%] Linking C static library libargon2-ssse3.a
    [  6%] Linking C static library libargon2-avx2.a
    [  7%] Linking C static library libethash.a
    [  7%] Built target argon2-avx512f
    [  7%] Built target argon2-ssse3
    [  7%] Built target argon2-sse2
    [  7%] Built target argon2-avx2
    [  7%] Built target ethash
    [  7%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/core.c.o
    [  7%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/argon2.c.o
    [  8%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/encoding.c.o
    [  7%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/genkat.c.o
    [  8%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/impl-select.c.o
    [  8%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/arch/x86_64/lib/argon2-arch.c.o
    [  9%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/blake2/blake2.c.o
    [ 10%] Linking C static library libargon2.a
    [ 10%] Built target argon2
    Scanning dependencies of target xmrig

    [SNIP]

    [100%] Linking CXX executable xmrig
    ld: warning: ignoring file ../scripts/deps/lib/libhwloc.a, building for macOS-x86_64 but attempting to link with file built for macOS-arm64

    [SNIP]

**Additional context**
- Believe the cmake step is NOT properly detecting/setting MACOS_ARM 
- Since there is a pre-built version for macOS-arm64, it is obviously possible to build it
- The "build_deps.sh" script successfully detects and builds for macOS-arm64, which is why the link fails
- Note: Without running the "build_deps.sh" script, the cmake step fails because it doesn't successfully find OpenSSL
- Running the latest XCODE on a 16GB Mac Mini M1


# Discussion History
## NobelEvil | 2021-04-28T22:40:39+00:00
Hi,
I was trying to build on  macOS Big Sur M1 Chip 2020 by following the instructions of https://xmrig.com/docs/miner/build/macos I made the Build ---> However, there was a problem with it,I don't know why and how to fix this. 
Problem: After all the process is followed the CPU shows either Virtual Apple and assembly auto: Intel.  Below is the attached screenshot.

Please assist me in making the build work on Apple processor (1) 64 bit AES similar to that of pre-build.(https://xmrig.com/download macOS 11+, Apple M1)
<img width="1278" alt="Screenshot 2021-04-29 at 1 18 33 AM" src="https://user-images.githubusercontent.com/83372867/116481383-1cfe8300-a894-11eb-910f-c54864545bc7.png">




## RS102839 | 2021-04-29T13:59:52+00:00
@NobelEvil Sounds like you successfully built the macOS-x86_64 version and are then running it under Rosetta.

Problem was you wanted to build the macOS-arm64 version, which runs about 20% faster.

## NobelEvil | 2021-04-29T23:01:47+00:00
> @NobelEvil Sounds like you successfully built the macOS-x86_64 version and are then running it under Rosetta.
> 
> Problem was you wanted to build the macOS-arm64 version, which runs about 20% faster.

That's true however whatever commands I run even without rosetta it shows the same results. As rosetta isn't the problem, maybe it's some assembly issue which doesn't allow to make the build on ARM-64.
Also the codes mentioned on the website of XMRIG aren't for ARM-64.

The ARM 64 built gives 1800 to  2281 h/s and macOS-x86-64 gives max 600 to 800 h/s. That is the reason I'm looking for solution to make build for M1 chip MacBook Air 2020.  
Also by using your commands it show macOS-x86_64 version, that's why I shared the screenshot to get the solution, maybe you can help.

## RS102839 | 2021-04-30T15:57:39+00:00
@NobelEvil  Seems like you have the basically same problem I have, that the build instructions and the CMAKE scripts don't appear to directly target the M1 processor and build an ARM64 executable.

I've been dipping into them, and so far haven't found a smoking gun.

## Spudz76 | 2021-04-30T19:01:13+00:00
So then you're all using [these macos build instructions](https://xmrig.com/docs/miner/build/macos) and also observing that step 4 is different for the Apple processor?

## RS102839 | 2021-04-30T19:07:43+00:00
> So then you're all using [these macos build instructions](https://xmrig.com/docs/miner/build/macos) and also observing that step 4 is different for the Apple processor?

Yes, but it doesn't build for ARM64, it builds for x86-64.   
Note: NobelEvil appears to have successfully built on M1, but also for x86-64.

More: By using the "build_deps.sh" script, I was able to build the dependencies as ARM64, so the linker failed as the XMRIG modules were built as x86-64.
My plan was to try to figure out ways of improving the hash rate on M1, but so far I'm in CMAKE/MAKE purgatory  :-(

More, more:

  brew install cmake wget automake libtool autoconf
  git clone https://github.com/xmrig/xmrig.git
  cd xmrig/scripts
  ./build.deps.sh
  mkdir ../build && cd ../build
  cmake .. -DOPENSSL_ROOT_DIR=../scripts/deps -DHWLOC_INCLUDE_DIR=../scripts/deps/include -DHWLOC_LIBRARY=../scripts/deps/lib/libhwloc.a -DUV_INCLUDE_DIRS=../scripts/deps/include -DUV_LIBRARY=../scripts/deps/lib/libuv.a -DOPENSSL_CRYPTO_LIBRARY=../scripts/deps/lib/libcrypto.a -DOPENSSL_INCLUDE_DIR=../scripts/deps/include -DOPENSSL_SSL_LIBRARY=../scripts/deps/lib/libssl.a
  build % make -j$(sysctl -n hw.logicalcpu)

The compile is successfull, but then the link fails because of the x86-64 versus arm64 problem described above:


  Scanning dependencies of target xmrig-asm
  [  0%] Building C object src/3rdparty/argon2/CMakeFiles/argon2-sse2.dir/arch/x86_64/lib/argon2-sse2.c.o
  [  0%] Building C object src/3rdparty/argon2/CMakeFiles/argon2-avx2.dir/arch/x86_64/lib/argon2-avx2.c.o
  [  0%] Building C object src/3rdparty/argon2/CMakeFiles/argon2-avx512f.dir/arch/x86_64/lib/argon2-avx512f.c.o
  [  0%] Building C object src/3rdparty/argon2/CMakeFiles/argon2-ssse3.dir/arch/x86_64/lib/argon2-ssse3.c.o
  [  1%] Building C object src/3rdparty/libethash/CMakeFiles/ethash.dir/ethash_internal.c.o
  [  1%] Building C object src/3rdparty/argon2/CMakeFiles/argon2-xop.dir/arch/x86_64/lib/argon2-xop.c.o

  [ SNIP ]

  [100%] Linking CXX executable xmrig
  ld: warning: ignoring file ../scripts/deps/lib/libuv.a, building for macOS-x86_64 but attempting to link with file built for macOS-arm64
  ld: warning: ignoring file ../scripts/deps/lib/libhwloc.a, building for macOS-x86_64 but attempting to link with file built for macOS-arm64
  ld: warning: ignoring file ../scripts/deps/lib/libcrypto.a, building for macOS-x86_64 but attempting to link with file built for macOS-arm64
  ld: warning: ignoring file ../scripts/deps/lib/libssl.a, building for macOS-x86_64 but attempting to link with file built for macOS-arm64



## NobelEvil | 2021-05-01T06:03:37+00:00
@RS102839 In that case will say Good Luck for both of us. Let's help out each other in this mission. Do let me know as soon as you find results & I'll do the same.

@Spudz76  Brother, all of us have followed the steps reading properly about the Apple process in step 4.
I think you should try too, maybe you might get some other results than us. If you get any success with those steps than help us all out of it. It will be considered as your great contribution in this cause.
Thanks & Good Luck.

@xmrig: Please help & update us if we're missing out on something as it is unsolvable puzzle, even after following all the steps from updated(6.12.1) source code properly and trying all different possible options can't get any solution.
 

## Spudz76 | 2021-05-01T06:08:00+00:00
Can't because I don't have any Apples.

## xmrig | 2021-05-01T08:40:00+00:00
Likely you run x86_64 shell, check output of `uname -m` command it should return `arm64` if not run `arch -arm64 zsh`. I guess in your case it was changed somehow earlier.
Thank you.

## RS102839 | 2021-05-01T17:07:28+00:00
> @xmrig Likely you run x86_64 shell, check output of `uname -m` command it should return `arm64` if not run `arch -arm64 zsh`. I guess in your case it was changed somehow earlier.
> Thank you.

`% uname -m`
`arm64`

Note: `build_deps.sh` correctly builds arm64

However, I subsequently did  `arch -arm64 zsh` regardless.

Note: Facing problems in `src/3rdparty/argon2`, that the compiler is giving the error: `error: unknown target CPU 'armv8-a'`, followed by a long list of Intel CPUs.   My conclusion is I now have some kind of generated hybrid set of makefiles that are simultaneously `arm64` and `x86_64`.  For example: 
`/Users/[REDACTED]/build/src/3rdparty/argon2/CMakeFiles/argon2.dir/flags.make` contains:

`C_DEFINES = -DHAVE_SYSLOG_H -DNDEBUG -DUNICODE -DXMRIG_ALGO_ARGON2 -DXMRIG_ALGO_RANDOMX -DXMRIG_ARM -DXMRIG_ARMv8 -DXMRIG_FEATURE_API -DXMRIG_FEATURE_BENCHMARK -DXMRIG_FEATURE_ENV -DXMRIG_FEATURE_HTTP -DXMRIG_FEATURE_HWLOC -DXMRIG_JSON_SINGLE_LINE_ARRAY -DXMRIG_MINER_PROJECT -DXMRIG_OS_APPLE -DXMRIG_OS_MACOS -DXMRIG_SECURE_JIT -D_FILE_OFFSET_BITS=64 -D__STDC_FORMAT_MACROS`

`C_INCLUDES = -I/Users/[REDACTED]/scripts/deps/include -I/Users/[REDACTED]-m1/src/3rdparty/argon2/../.. -I/Users/[REDACTED]/src/3rdparty/argon2/lib`

`C_FLAGSx86_64 =  -Wall -march=armv8-a -O3 -DNDEBUG -Ofast -funroll-loops -fmerge-all-constants -arch x86_64 -isysroot /Library/Developer/CommandLineTools/SDKs/MacOSX11.3.sdk -std=gnu99`

`C_FLAGS =  -Wall -march=armv8-a -O3 -DNDEBUG -Ofast -funroll-loops -fmerge-all-constants -arch x86_64 -isysroot /Library/Developer/CommandLineTools/SDKs/MacOSX11.3.sdk -std=gnu99`

Where `C_DEFINES` looks to be correct for MacOS ARM64, but `C_FLAGS`  is both `x86_64` and `armv8-a`

Same situation in all the other `flags.make` files.

When I hand-modify all the generated `flags.make` files to replace the `-arch x86_64` with `-arch arm64` in `C_FLAGS` and `CXX_FLAGS`, everything compiles, but then I get a (new) link error: 

` [SNIP] `
`[100%] Linking CXX executable xmrig`
`ld: warning: ignoring file CMakeFiles/xmrig.dir/src/backend/cpu/CpuLaunchData.cpp.o, building for macOS-x86_64 but attempting to link with file built for unknown-arm64`
` [SNIP] `
`Undefined symbols for architecture x86_64:`
`  "_main", referenced from:`
`     implicit entry/start for main executable`
`ld: symbol(s) not found for architecture x86_64`
`clang: error: linker command failed with exit code 1 (use -v to see invocation)`


**Initial conclusion**

1. There's a problem in the CMAKE stage generating `C_FLAGS` and `CXX_FLAGS` in the `flags.make` files.
2. There's a closely related problem in the link parameters and build target

I have to take a break now, and will try to work on the linker issue this evening

## xmrig | 2021-05-01T17:21:06+00:00
You must delete all generated files and run cmake with the correct shell again.
`flags.cmake` should looks like:

C_INCLUDES = ...
C_FLAGS**arm64** =  -Wall -march=**armv8-a+crypto** -O3 -DNDEBUG -Ofast -funroll-loops -fmerge-all-constants -arch **arm64** ..
C_FLAGS =  -Wall -march=**armv8-a+crypto** -O3 -DNDEBUG -Ofast -funroll-loops -fmerge-all-constants -arch **arm64** ...


## RS102839 | 2021-05-01T21:31:31+00:00
@xmrig  I think the solution is a bit trickier than that, because XCode is happy to build either or both of a x86_64 and arm64 target, so you have to ensure you tell it whether you are building both or building just one, and if just one, which.

I blew away the build directory (yet again) and modified `CMakeLists.txt` to explicitly tell it to build arm64 when on an ARM Mac; at line 155, in the Apple section, added:

`    if (XMRIG_ARM)`
`        set(CMAKE_OSX_ARCHITECTURES "arm64")`
`    else()`
 `       set(CMAKE_OSX_ARCHITECTURES "x86_64")`
 `   endif()`

This does properly output the `flags.make' files.  (with a problem that it isn't detecting crypto, but I'll address that later)

However, this doesn't solve all the problems as `/Users/[REDACTED]/build/CMakeFiles/3.20.1/CMakeSystem.cmake` still is configured for x86_64, and contains these lines:
`set(CMAKE_HOST_SYSTEM_PROCESSOR "x86_64")`
`set(CMAKE_SYSTEM_PROCESSOR "x86_64")`
If I hand-modify these to be `arm64` everything compiles and links.

My other problem, noted above, is the CMAKE file is failing to detect crypto, so this line in file `cmake\cpu.cmake` fails:
`CHECK_CXX_COMPILER_FLAG(-march=armv8-a+crypto XMRIG_ARM_CRYPTO)`

But I'll worry about that when `CMakeSystem.cmake` is being generated properly, since this might be a subservient bug.



## RS102839 | 2021-05-01T22:39:39+00:00
@xmrig, @NobelEvil 

I can now build and run xmrig in arm64 mode on a MacOS M1, but have some modifications.

1. Add two lines near the top of `CMakeLists.txt` to force CMake to generate for MacOS arm64
2. After running CMake, fixup `/Users/[REDACTED]/build/CMakeFiles/3.20.1/CMakeSystem.cmake` by changing the two instances of x86_64 to arm64
3. My Cmake command line options are more complex, as discussed above

This also fixes the issue noted immediately above of detecting crypto.

These changes to `CMakeLists.txt` replace the ones in the prior comment, and at line 35 (after the options are listed), insert:
`set(CMAKE_OSX_ARCHITECTURES "arm64")`
`set(CMAKE_SYSTEM_PROCESSOR "arm64")`

This unconditional fix obviously isn't appropriate for uploading to this site.

Something like this might work:   _Note: Entirely untested!!!!_
`# Deployment target/architectures for macOS`
`if(APPLE)`
`# on macOS "uname -m" returns the architecture (x86_64 or arm64)`
 `   execute_process(`
  `      COMMAND uname -m`
  `      RESULT_VARIABLE result`
  `      OUTPUT_VARIABLE XMRIG_OSX_NATIVE_ARCHITECTURE`
  `      OUTPUT_STRIP_TRAILING_WHITESPACE`
 `   )`
`set(CMAKE_OSX_ARCHITECTURES {XMRIG_OSX_NATIVE_ARCHITECTURE})`
`set(CMAKE_SYSTEM_PROCESSOR {XMRIG_OSX_NATIVE_ARCHITECTURE})`

`endif()`


However, I still have the problem that `/Users/[REDACTED]/build/CMakeFiles/3.20.1/CMakeSystem.cmake` isn't being properly generated, and therefore requiring a hand-modification.

## NobelEvil | 2021-05-03T20:55:08+00:00
@RS102839 did you made a build For M1. above things are so tricky. I am still standing on same point... 
@xmrig I use this **uname -m** as you mention it give me output **arm64** and **arch -arm64 zsh** gives me **arch: posix_spawnp: zsh: Bad CPU type in executable** what else I have to do to make a clean build for AMR64 M1 the given source code 6.12.1 need a lots of fixes regarding M1

## RS102839 | 2021-05-03T21:02:23+00:00
@NobelEvil: Do remember the code I provided was "entirely untested".  Sorry.

You can do the two other changes I suggested, but I currently don't have a great solution, just a poor solution.

Note: The best thing would to get a Metal version of the OpenCL code, and then we could run a GPU-based executable and a CPU-based executable at the same time.   
Just checked on resource use and xmrig is only using 2.5GB of memory, even though I'm on a 16GB Mac Mini M1, so I definitely have enough memory to run a second instance, its just the current instance uses 98% of my CPU whenever it can.

## RS102839 | 2021-05-04T03:29:17+00:00
@xmrig, @NobelEvil 

After much agony I realized my problem was using an x86_64 CMAKE to try to build an arm64 executable.   I got to this point from moving from an Intel-based Mac Mini to a M1 (arm64) based Mac Mini, copying all the files, which were all x86_64.

As I said earlier, the Mac M1 is very happy to build and run both x86_64 and arm64, and you too can fall victim to this.

1. **Make sure you have the arm64 version of both homebrew and cmake, and then make sure you use them  !!**
2. `/opt/homebrew/bin/brew install cmake wget automake libtool autoconf`
3. I also built all the dependencies
4. Then I successfully built the xmrig executable using:
5. `/opt/homebrew/bin/cmake .. -DHWLOC_INCLUDE_DIR=../scripts/deps/include -DHWLOC_LIBRARY=../scripts/deps/lib/libhwloc.a -DUV_INCLUDE_DIRS=../scripts/deps/include -DUV_LIBRARY=../scripts/deps/lib/libuv.a -DOPENSSL_CRYPTO_LIBRARY=../scripts/deps/lib/libcrypto.a -DOPENSSL_INCLUDE_DIR=../scripts/deps/include -DOPENSSL_SSL_LIBRARY=../scripts/deps/lib/libssl.a `


## Spudz76 | 2021-05-04T15:53:21+00:00
step 5 should work as:
```
/opt/homebrew/bin/cmake ..   -DCMAKE_PREFIX_PATH=../scripts/deps -DCMAKE_BUILD_TYPE=Release -DCMAKE_VERBOSE_MAKEFILE=ON -DWITH_OPENCL=OFF -DWITH_ADL=OFF -DWITH_CUDA=OFF -DWITH_NVML=OFF
```
Because all the deps should be found automatically by only setting the prefix (base folder with `lib` and `include`)

## RS102839 | 2021-05-04T18:01:49+00:00
The problem was resolved as an issue between x86_64 and arm64 on Mac M1, and the solution was properly described

## NobelEvil | 2021-05-04T20:04:14+00:00
@xmrig and @RS102839 Thanks.  Problem Solved 


# Action History
- Created by: RS102839 | 2021-04-28T16:31:06+00:00
- Closed at: 2021-05-04T18:00:50+00:00
