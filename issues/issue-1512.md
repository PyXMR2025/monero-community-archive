---
title: Compile with intel compiler?
source_url: https://github.com/xmrig/xmrig/issues/1512
author: agentpatience
assignees: []
labels: []
created_at: '2020-01-23T20:29:53+00:00'
updated_at: '2021-11-16T10:57:04+00:00'
type: issue
status: closed
closed_at: '2021-04-12T15:02:10+00:00'
---

# Original Description
has anyone tried to compile xmrig with intel compiler, will it work, is there any gains on intel hardware by using it? Any info would be appreciated.



# Discussion History
## ValoWaking | 2020-01-23T21:15:50+00:00
Where i can download compiler to try!?

## agentpatience | 2020-01-23T21:38:24+00:00
> 
> 
> Where i can download compiler to try!?

Here you go.

https://dynamicinstaller.intel.com/system-studio/download

## agentpatience | 2020-01-23T21:40:58+00:00
Just in case the above link doesn't work right here is the doorway page: https://software.intel.com/en-us/system-studio/choose-download

## ValoWaking | 2020-01-23T21:52:56+00:00
u meen Intel® C++ Compiler? Right?

## agentpatience | 2020-01-23T22:55:22+00:00
Yes of course. 

Sent from my iPhone

> On Jan 23, 2020, at 4:52 PM, ValoWaking <notifications@github.com> wrote:
> 
> ﻿
> u meen Intel® C++ Compiler? Right?
> 
> —
> You are receiving this because you authored the thread.
> Reply to this email directly, view it on GitHub, or unsubscribe.


## agentpatience | 2020-01-23T23:22:41+00:00
I'm told for HPC applications that it is best to use the compiler included in Parallel Studio https://software.intel.com/en-us/parallel-studio-xe/choose-download but I am not sure exactly what the differences are. It seems you can get both for free trial and full software.

## Spudz76 | 2020-01-23T23:45:58+00:00
I spent a lot of time bothering with this and it never provided any visible gains.  Also the free license for open source developers (closest applicable thing to what I do) expired after a year and I didn't feel like figuring out the hoops to get a new key.

Currently I build miners with Clang-10 it seems in general fastest.  Though I haven't done a benchmark of compiler vs hashrate lately.

I believe their strengths are with things other than what miner code does, and given some of the core loops are ASM anyway the compiler doesn't have anything to do there other than maybe slightly improved optimization (it won't toss in cool instructions the ASM coder didn't use).  Clang knows CPUs pretty well and support thing almost release day, even the embedded ones.  I maybe should be using Clang-11 now that it is out... but haven't tried it yet.

## Spudz76 | 2020-01-23T23:48:49+00:00
I still have the patches that make it work correctly, could prep them for PR, there have been various attempts at adding it before though (search closed PR/Issues)

Out of the box it usually doesn't work.  I would have to obtain a licence for icc again to make sure the patches still work to submit PR.

## agentpatience | 2020-01-23T23:52:45+00:00
> 
> 
> I spent a lot of time bothering with this and it never provided any visible gains. Also the free license for open source developers (closest applicable thing to what I do) expired after a year and I didn't feel like figuring out the hoops to get a new key.
> 
> Currently I build miners with Clang-10 it seems in general fastest. Though I haven't done a benchmark of compiler vs hashrate lately.
> 
> I believe their strengths are with things other than what miner code does, and given some of the core loops are ASM anyway the compiler doesn't have anything to do there other than maybe slightly improved optimization (it won't toss in cool instructions the ASM coder didn't use). Clang knows CPUs pretty well and support thing almost release day, even the embedded ones. I maybe should be using Clang-11 now that it is out... but haven't tried it yet.

Thanks for the information Spudz. It appears from Intel Docs that they have made several revisions and upgrades to their software. Do you remember which version you tried? The trials allow you to use the brand new version for a year.


fwiw - I read that you can just recycle the license file installer and you get a renewal. It is stated in the System Studio download page.

## 2010phenix | 2020-01-23T23:54:40+00:00
Yes, just try to write to @agentpatience that you are @Spudz76 us remember used Intel compiler... ))
Clang... long time ago used.. but what  about static build and what size much big thn MinGW ?
thanks

## Spudz76 | 2020-01-23T23:55:07+00:00
I have also tested it on Atom and some others and it was no different than other compilers (clang usually faster, even).

Some compilers make hashrate max higher but overall average rates are lower so they can be misleading.  I think ICC looks faster at peaks but it also has a lower rate over time, somehow.  Clang was the flattest result.  GCC pretty close to flat.

I had tested with 17, 18, and 19.  earlier than 17 didn't do C++11 or something required.  18 mostly since 19 came out near when license expired.

Interesting I think I nuked the whole install and licence state already but I will see if the reinstall does a renew.

## agentpatience | 2020-01-23T23:55:14+00:00
On a side note, I am preparing to test Clear Linux (intel optimized linux distro) I am hoping xmrig will show some gains here compared to Manjaro, Fedora or Ubuntu on Intel based server systems.

## 2010phenix | 2020-01-23T23:59:54+00:00
be nice to see some test result @agentpatience for xmrig community....

## Spudz76 | 2020-01-24T00:00:40+00:00
I have no need to static so I am unsure about that at all.
I did play with the Intel linker and its optimization options to reduce size / remove unused code and it makes linking take much longer for some size savings.  But not with static.
I did not keep any records of sizes and probably cleaned up the build trees too.

Most of my testing was on semi-shared equipment not dedicated to CPU mining.  Such as most have GPUs grinding Ethereum, and the CPU grinding xmrig.  I have not tuned each task to particular cores, to fence off the work, which might improve the stability of hashrate (pre-empted by PCIe xfers? or Eth rechecks on CPU now and then... evicting caches... getting in the way)

## 2010phenix | 2020-01-24T00:03:22+00:00
@Spudz76 am just remember that nice days when miner be 500Kb size.. and now ohh ((

## agentpatience | 2020-01-24T00:07:29+00:00
I'll let you know about trying Intel's clear linux on a variety of hardware that I have. It is going toi take a couple hours to download... I am seeing the best hashrates with Manjaro so far...using GCC 9.1. 


Spudz - when you did your compilation for xmrig on Intel platform but using what software suite? Intel parallel studio xe or system studio? did you use linux or windows  

## Spudz76 | 2020-01-24T00:17:22+00:00
Linux, PS-xe.  just swapped `CC` and `CXX` env vars with `/opt/intel/bin/icc` and a few mods to cmake rules so it does the right things for Intel compiler.  I believe in that mode it still uses normal system gcc linker.  With more hacks you can get it to use the Intel linker but like I said I never saw much gain from bothering - however if you are targeting size then it might help.  No use of any of the performance primitives or thread whatever libs.

Yeah it currently won't let me download anything newer than 2019-r4 and even then the key is expired and cannot be removed or renewed (through the web).  I think I applied again so maybe that will work when the request is handled.

## agentpatience | 2020-01-24T00:25:44+00:00
[intel-sw-tools-installation-bundle-linux-linux.zip](https://github.com/xmrig/xmrig/files/4106279/intel-sw-tools-installation-bundle-linux-linux.zip)

That's the linux system studio 2020 w/ intel complier installer with licence.

## Spudz76 | 2020-01-24T00:57:57+00:00
That seems to work but I have not tried ICC since RandomX went in.  There are some issues with compilation in there that need repaired.

EDIT: Seems it is pedantic about `-fno-exceptions` and having try or throw in the code.  Other compilers simply ignore it and maybe warn.  So far commenting out all throwing in the randomx code appears to make it compile...

EDIT2: segfaults, oh well

EDIT3: okay I copied/refreshed the flags from GCC which enable exceptions and then it seems to be compiling...

## ValoWaking | 2020-01-24T01:51:31+00:00
i think we need to update with intel compiler all libs that used by xmrig - libuv, openssl, hwloc, etc

## Spudz76 | 2020-01-24T02:04:48+00:00
Haven't tried that before but, most of those are accessed once at setup time so it doesn't matter much.

There is a build-deps script which would make it possibly easy to try out

## ValoWaking | 2020-01-24T03:36:37+00:00
Are u tested build with GCC?

## SChernykh | 2020-01-24T09:34:52+00:00
95% of RandomX hashing time is spent inside JIT-generated main loop, so compiler can only optimize the remaining 5%. Modern compilers are already very good, so difference between them is usually 1-2%, so 1-2% out of those 5% is 0.1% hashrate difference at best.

## Spudz76 | 2020-01-24T18:57:29+00:00
That math generally matches what I have found by testing.  No difference that matters.

Sizes of output of various compilers:
```
2365352 xmrig-clang8
2365600 xmrig-clang10
2367784 xmrig-clang7
2369496 xmrig-clang9
3773496 xmrig-gcc6
3785704 xmrig-gcc8
3810264 xmrig-gcc9
3838952 xmrig-gcc7
4391904 xmrig-icc
```

EDIT: the ICC was configured with gcc-9 as its backing compiler (versus default gcc-7)

Working on the patchset which makes ICC work (without my other hacks)

## Spudz76 | 2020-01-24T19:11:07+00:00
I built deps with icc also and tried static, it seems to just coredump / haven't debugged much more

## Spudz76 | 2020-01-24T19:23:18+00:00
Here are [the patches](https://github.com/xmrig/xmrig/commit/5d96b0f92346c1ad18f3ee40fb93b406976ced91) that make ICC work

There is an added cmake option: `ICC_GCCVER`
Normally it will use the system default gcc but to force a different one use `-DICC_GCCVER=9` or such in your cmake setup phase.  And of course install the alternate gcc version.

## ValoWaking | 2020-01-25T09:31:37+00:00
any results in hashrate!?

## 2010phenix | 2020-01-25T13:32:43+00:00
@xmrig, maybe this one(https://github.com/xmrig/xmrig/commit/5d96b0f92346c1ad18f3ee40fb93b406976ced91) move to repo? for ICC if @Spudz76 say that exist some problem... No need crying members in issue tracker ))

## ValoWaking | 2020-01-27T02:14:39+00:00
@Spudz76 please help me. I'm try build with:

"C:/Program Files/CMake/bin/cmake.exe" .. -G "NMake Makefiles" -D CMAKE_C_COMPILER="C:/Program Files (x86)/IntelSWTools/compilers_and_libraries_2020.0.166/windows/bin/intel64/icl.exe" -D CMAKE_CXX_COMPILER="C:/Program Files (x86)/IntelSWTools/compilers_and_libraries_2020.0.166/windows/bin/intel64/icl.exe" -DXMRIG_DEPS="C:/xmrig-deps/msvc2019/x64"

but have many errors:

```
-- The C compiler identification is Intel 19.1.0.20191121
-- The CXX compiler identification is Intel 19.1.0.20191121
-- Check for working C compiler: C:/Program Files (x86)/IntelSWTools/compilers_and_libraries_2020.0.166/windows/bin/intel64/icl.exe
-- Check for working C compiler: C:/Program Files (x86)/IntelSWTools/compilers_and_libraries_2020.0.166/windows/bin/intel64/icl.exe -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Detecting C compile features
-- Detecting C compile features - done
-- Check for working CXX compiler: C:/Program Files (x86)/IntelSWTools/compilers_and_libraries_2020.0.166/windows/bin/intel64/icl.exe
-- Check for working CXX compiler: C:/Program Files (x86)/IntelSWTools/compilers_and_libraries_2020.0.166/windows/bin/intel64/icl.exe -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Detecting CXX compile features
-- Detecting CXX compile features - done
CMake Error at C:/Program Files/CMake/share/cmake-3.16/Modules/FindPackageHandleStandardArgs.cmake:146 (message):
  Could NOT find HWLOC (missing: HWLOC_LIBRARY HWLOC_INCLUDE_DIR)
Call Stack (most recent call first):
  C:/Program Files/CMake/share/cmake-3.16/Modules/FindPackageHandleStandardArgs.cmake:393 (_FPHSA_FAILURE_MESSAGE)
  cmake/FindHWLOC.cmake:25 (find_package_handle_standard_args)
  src/backend/cpu/cpu.cmake:30 (find_package)
  src/backend/backend.cmake:1 (include)
  CMakeLists.txt:37 (include)


-- Configuring incomplete, errors occurred!
See also "C:/xmrig-5.5.2/build/CMakeFiles/CMakeOutput.log".
```



## ValoWaking | 2020-01-27T05:19:32+00:00
ok, now i goes with: 
`"C:/Program Files/CMake/bin/cmake.exe" .. -T "Intel C++ Compiler 19.1" -DXMRIG_DEPS="C:/xmrig-deps/msvc2019/x64" -DWITH_HWLOC=OFF -DWITH_ASM=OFF`
and can do release with next errors:
[result.txt](https://github.com/xmrig/xmrig/files/4115666/result.txt)
**Spudz76** can you help with this?



## Spudz76 | 2020-01-27T20:26:46+00:00
Normal code checkouts won't build with ICC.  Are you using the patchset I posted above (my dev-icc branch?)

I have never tried Windows with anything but VS2017 or 2019.

## ValoWaking | 2020-01-27T21:23:14+00:00
Name of Intel compiler for windows is icl.exe. I want build for windows... Im trying use u patch, but have same result.

## ValoWaking | 2020-01-27T21:53:49+00:00
and how i can buld with gcc for windows?

## 2010phenix | 2020-01-27T22:09:09+00:00
> and how i can buld with gcc for windows?

for gcc you build in Msys2 \ MinGW

## ValoWaking | 2020-01-28T00:01:28+00:00
gcc is slower than vs2019, so i'm waiting any solution for fix build release by intel compiler (icl.exe)

## ValoWaking | 2020-02-03T15:41:32+00:00
any news about build for windows?

## Spudz76 | 2020-02-09T02:28:07+00:00
I doubt anything but VS will be fastest on Windows.  I may still test.

Still basically useless speed, but ICC does go faster on oddball CPUs.  Same clang-11 and icc versions on both.

This is on a hacked-for-debian old Chromebook:
```
  * CPU          Intel(R) Celeron(R) CPU 847 @ 1.10GHz (1) x64 -AES
                 L2:0.5 MB L3:2.0 MB 2C/2T NUMA:1
```
algo `rx/wow`
182.7 peak rate Clang-11
222.4 peak rate ICC

This is on older shelf-size PC:
```
  * CPU          Intel(R) Atom(TM) CPU D2550 @ 1.86GHz (1) x64 -AES
                 L2:1.0 MB L3:0.0 MB 2C/4T NUMA:1
```
algo `rx/0`
41.7 peak rate Clang-11
45.1 peak rate ICC

## ValoWaking | 2020-02-09T15:43:16+00:00
> VS will be fastest on Windows

What version of intel parallel studio xe u use? Intel compiler that used by windows and integrate in VS called ICL.exe, not ICC.exe



## moroznah | 2020-02-10T17:38:08+00:00
Thank you for doing this, was thinking of trying icc for a long time.
Some testing results, on oddball CPU :)
Ubuntu 18.04
Intel(R) Xeon Phi(TM) CPU 7210 @ 1.30GHz
No RAM, only cache in quadrant mode
Intel parallel studio xe ver. 19.0.5.20190815

rx/0 benchmark
compiler	        bin size	        hashrate
clang-10 	        2396048 	        6408kh
gcc-8	 	4200200		6412kh
icc 		        4862592		6380kh


## agentpatience | 2020-02-10T18:22:02+00:00
Whoa is that really K/h sec? Have you tried others ram to use memory bus or are the phi faster without outboard ram?

Sent from my iPhone

> On Feb 10, 2020, at 12:38 PM, moroznah <notifications@github.com> wrote:
> 
> ﻿
> Thank you for doing this, was thinking of trying icc for a long time.
> Some testing results, on oddball CPU :)
> Ubuntu 18.04
> Intel(R) Xeon Phi(TM) CPU 7210 @ 1.30GHz
> No RAM, only cache in quadrant mode
> Intel parallel studio xe ver. 19.0.5.20190815
> 
> rx/0 benchmark
> compiler bin size hashrate
> clang-10 2396048 6408kh
> gcc-8 4200200 6412kh
> icc 4862592 6380kh
> 
> —
> You are receiving this because you were mentioned.
> Reply to this email directly, view it on GitHub, or unsubscribe.


## moroznah | 2020-02-10T18:38:24+00:00
Oh man, missed the dot obviously. It's 6.4kh.
These Phi's are essentially large number of wooden Atom cores, no surprises here in performance.
I have couple of nodes populated with 6 channels of DDR4, tried on them with 1GB hugepages and saw no performance increase. MCDRAM has more bandwidth.
Too bad no increase with icc, i was hoping for some as Spudz76 had some success on an Atom.

## agentpatience | 2020-02-10T19:08:39+00:00
64000 is that for 1 Phi? My dual Xeon 6148 can only do 55000 h/S.

Sent from my iPhone

> On Feb 10, 2020, at 12:38 PM, moroznah <notifications@github.com> wrote:
> 
> ﻿
> Thank you for doing this, was thinking of trying icc for a long time.
> Some testing results, on oddball CPU :)
> Ubuntu 18.04
> Intel(R) Xeon Phi(TM) CPU 7210 @ 1.30GHz
> No RAM, only cache in quadrant mode
> Intel parallel studio xe ver. 19.0.5.20190815
> 
> rx/0 benchmark
> compiler bin size hashrate
> clang-10 2396048 6408kh
> gcc-8 4200200 6412kh
> icc 4862592 6380kh
> 
> —
> You are receiving this because you were mentioned.
> Reply to this email directly, view it on GitHub, or unsubscribe.


## moroznah | 2020-02-10T20:41:36+00:00
Yeah, single CPU, 256 threads. They don't have support and interconnects for DP/MP, the chipset is not from Xeon Scalable platform even tho the sockets are physically same.

Any benefits from icc compiler on Xeon Scalable? I have some, but no parallel studio there to test.

> 64000 is that for 1 Phi? My dual Xeon 6148 can only do 55000 h/S.
> […](#)
> Sent from my iPhone
> On Feb 10, 2020, at 12:38 PM, moroznah ***@***.***> wrote: ﻿ Thank you for doing this, was thinking of trying icc for a long time. Some testing results, on oddball CPU :) Ubuntu 18.04 Intel(R) Xeon Phi(TM) CPU 7210 @ 1.30GHz No RAM, only cache in quadrant mode Intel parallel studio xe ver. 19.0.5.20190815 rx/0 benchmark compiler bin size hashrate clang-10 2396048 6408kh gcc-8 4200200 6412kh icc 4862592 6380kh — You are receiving this because you were mentioned. Reply to this email directly, view it on GitHub, or unsubscribe.



## agentpatience | 2020-02-10T21:20:52+00:00
I have not tried icc yet. I am interested getting a ES 72xx cpu series but I need to check into mobo compatibility awhile ago I sold a could pci card versions which now I am a little pissed 🔥 lol

Sent from my iPhone

> On Feb 10, 2020, at 3:41 PM, moroznah <notifications@github.com> wrote:
> 
> ﻿
> Yeah, single CPU, 256 threads. They don't have support and interconnects for DP/MP, the chipset is not from Xeon Scalable platform even tho the sockets are physically same.
> 
> Any benefits from icc compiler on Xeon Scalable? I have some, but no parallel studio there to test.
> 
> 64000 is that for 1 Phi? My dual Xeon 6148 can only do 55000 h/S.
> …
> Sent from my iPhone
> On Feb 10, 2020, at 12:38 PM, moroznah @.***> wrote: ﻿ Thank you for doing this, was thinking of trying icc for a long time. Some testing results, on oddball CPU :) Ubuntu 18.04 Intel(R) Xeon Phi(TM) CPU 7210 @ 1.30GHz No RAM, only cache in quadrant mode Intel parallel studio xe ver. 19.0.5.20190815 rx/0 benchmark compiler bin size hashrate clang-10 2396048 6408kh gcc-8 4200200 6412kh icc 4862592 6380kh — You are receiving this because you were mentioned. Reply to this email directly, view it on GitHub, or unsubscribe.
> 
> —
> You are receiving this because you were mentioned.
> Reply to this email directly, view it on GitHub, or unsubscribe.


## agentpatience | 2020-02-12T16:57:02+00:00
Hi! Which mobo/system do you have? Have you tried the ES Phi CPU, if they work? There only seems to be 3 boards that support these?

> 
> 
> Yeah, single CPU, 256 threads. They don't have support and interconnects for DP/MP, the chipset is not from Xeon Scalable platform even tho the sockets are physically same.
> 
> Any benefits from icc compiler on Xeon Scalable? I have some, but no parallel studio there to test.
> 
> > 64000 is that for 1 Phi? My dual Xeon 6148 can only do 55000 h/S.
> > […](#)
> > Sent from my iPhone
> > On Feb 10, 2020, at 12:38 PM, moroznah _**@**_.***> wrote: ﻿ Thank you for doing this, was thinking of trying icc for a long time. Some testing results, on oddball CPU :) Ubuntu 18.04 Intel(R) Xeon Phi(TM) CPU 7210 @ 1.30GHz No RAM, only cache in quadrant mode Intel parallel studio xe ver. 19.0.5.20190815 rx/0 benchmark compiler bin size hashrate clang-10 2396048 6408kh gcc-8 4200200 6412kh icc 4862592 6380kh — You are receiving this because you were mentioned. Reply to this email directly, view it on GitHub, or unsubscribe.



## moroznah | 2020-02-13T09:55:06+00:00
We're going completely offtopic here :)
First of all you'll have hard time getting blank mobo's as all OEMs usually sell Phi systems preassembled.
I'm running ASRock Rack 2U4N-F/X200 systems. I can tell you for sure that ASRock Rack won't run any ES revision CPUs, however they do run non standard OEM ones (for ex. Scalable - Platinum 8167M).
Your best bet would be Supermicro, they usually don't have problems with ES.

## agentpatience | 2020-02-13T15:40:27+00:00
I know but I wasn't sure how to PM you. It doesn't seem like a viable option for 6400h/S. You can get that performance out of the dual E5 V1/V2/V3 chips... actually they are higher. I appreciate your feedback. The PHI's have always interested me. 

## Spudz76 | 2020-02-24T22:47:35+00:00
No luck with ICC windows, can't seem to figure out how to make CMake work with it, or maybe it didn't integrate properly with VS to provide MSBuild compatible usage.

## ValoWaking | 2020-02-24T23:31:24+00:00
> 
> 
> No luck with ICC windows, can't seem to figure out how to make CMake work with it, or maybe it didn't integrate properly with VS to provide MSBuild compatible usage.

u needed to start "Intel C++ compiler" from "windows start"

## ValoWaking | 2020-02-24T23:33:43+00:00
for compile by intel compiler u needed some like this:

"C:\Program Files\CMake\bin\cmake.exe" .. -G "Visual Studio 16 2019" -A x64 -D CMAKE_C_COMPILER="C:\Program Files (x86)\IntelSWTools\compilers_and_libraries_2020.0.166\windows\bin\intel64\icl.exe" -D CMAKE_CXX_COMPILER="C:\Program Files (x86)\IntelSWTools\compilers_and_libraries_2020.0.166\windows\bin\intel64\icl.exe" -DXMRIG_DEPS=C:\xmrig-deps\msvc2019\x64



## ValoWaking | 2020-02-24T23:37:21+00:00
when u run "-G "Visual Studio 16 2019" -A x64" in "Intel C++ compiler" CMD - icl.exe automatic compile with intel compiler

## ValoWaking | 2020-02-24T23:44:42+00:00
just watch the screen. But this is an old version.

https://software.intel.com/sites/default/files/managed/88/34/use_command_prompt_for_icc.png

## YetAnotherRussian | 2020-03-05T12:30:51+00:00
To build with Intel compiler, follow these steps:
1) **OPTIONAL** If you have an AMD CPU as a build machine, follow the steps from here https://www.reddit.com/r/Rlanguage/comments/f477er/discussion_workaround_for_mkl_on_amd/ to set up the env variable. This will fix possible CPU dispatcher or code optimization issues.
2) **OPTIONAL** If you have an AMD CPU as a build machine, comment this line in CmakeLists.txt:
`#include(cmake/cn-gpu.cmake)`
or Intel compiler will crash (this seems to be due to SSSE3 specific on AMD, and may be never fixed in ICC as they are not interested in AMD support, this is proved in the installation wizard disclaimer as well). Please note that cn-gpu will not be supported in XMRig. Also, older versions of Intel compiler (<1900) do not require this step. You may also set up this (if used):

`option(WITH_CN_GPU          "Enable CryptoNight-GPU algorithm" OFF)`

3) Generate solution, e.g.
`"%PROGRAMFILES%\CMake\bin\cmake.exe" .. -G "Visual Studio 16 2019" -A x64 -DXMRIG_DEPS=F:\xmrig-deps\msvc2019\x64`
4) Open solution, rmb click on xmrig project in solution tree, and select "Intel Compiler -> Use Intel C++". This step requires Intel VS integration to be installed.
5) Build

If you want the new compiler to be properly logged in xmrig CLI output, this will require code changes (compiler macros side), something like this (in BaseConfig.cpp):

```
#   elif defined(__INTEL_COMPILER)
    snprintf(buf, sizeof buf, "Intel Compiler %d", __INTEL_COMPILER);
#   elif defined(_MSC_VER)
    snprintf(buf, sizeof buf, "MSVC/%d", MSVC_VERSION);
```

That's it. 

@xmrig may add this macros as well (to suport the compiler natively). ICC is available for Linux as well.

Result:
![icc](https://user-images.githubusercontent.com/4670472/75981785-491fad80-5ef6-11ea-9819-7575247e50bb.png)

To make this build portable, additional dll's like libiomp5md.dll may be required to run on the target machine (depending on the build parameters which can be set in the project properties). These may be found on the build machine in ICC installation folder, e.g. \IntelSWTools\compilers_and_libraries_<YOUR_VERSION_HERE>\

## ValoWaking | 2020-03-05T13:40:36+00:00
**YetAnotherRussian**, any hashrate boost with Intel Compiler on Windows 10?

## YetAnotherRussian | 2020-03-05T14:51:09+00:00
@ValoWaking 
- 2-4% for cn-lite on Sandy Bridge (build tuned for Sandy Bridge)
- 10-12% for cn-lite on Goldmont Plus using low power mode aka double threads (2 hashes per thread, av=2) (build tuned for Goldmont Plus)
- RandomX, Argon2 and others untested

## ValoWaking | 2020-03-06T09:30:27+00:00
@YetAnotherRussian did u can upload build release? I want to check RandomX

## ValoWaking | 2020-05-01T09:03:33+00:00
> 
> 
> @ValoWaking
> 
>     * 2-4% for cn-lite on Sandy Bridge (build tuned for Sandy Bridge)
> 
>     * 10-12% for cn-lite on Goldmont Plus using low power mode aka double threads (2 hashes per thread, av=2) (build tuned for Goldmont Plus)
> 
>     * RandomX, Argon2 and others untested

I got a performance decrease on 20 hash with intel compiler on randomX. What tegs optimization you use?

## agentpatience | 2020-12-22T18:33:50+00:00
There seems to be a new version of the Intel Compiler out (Intel oneAPI DPC++ / C++ Compiler 2021): 

https://software.intel.com/content/www/us/en/develop/tools/oneapi/base-toolkit.html

The Intel® oneAPI HPC Toolkit
is a comprehensive suite of development tools that make it fast and easy to build modern code that gets maximum performance out of the newest Intel® processors. This toolkit enables high performance computing on clusters or individual nodes with flexible options including optimal performance on a CPU or GPU.
Creating code is simplified with the latest techniques in vectorization, multi-threading, multi-node, and memory optimization. Get powerful, consistent programming with 512-bit Intel® Advanced Vector Extensions (Intel® AVX-512) for Intel® Core™ and Intel® Xeon® processors, OpenMP support, plus support for the latest standards and integrated development environments (IDEs). New features include greater scalability and reduced latency with the next-generation Intel® MPI Library. Take advantage of industry leading Priority Support provided by Intel engineers who can help you quickly troubleshoot and accelerate your performance-critical applications for improved business value.
The goal of this Get Started guide is to get you acquainted with the HPC Kit by building a sample project and using this toolkit to optimize your code for the best performance possible.
Included in this toolkit are:

    Intel® oneAPI DPC++/C++ Compiler
    Intel® C++ Compiler
    Intel® Fortran Compiler (Beta)
    Intel® MPI Library
    Intel® Inspector
    Intel® Trace Analyzer and Collector
    Intel® Cluster Checker 

https://software.intel.com/content/www/us/en/develop/tools/oneapi/hpc-toolkit.html


## sigkill | 2021-11-16T10:57:04+00:00
Did anyone ever try building for KNC?

# Action History
- Created by: agentpatience | 2020-01-23T20:29:53+00:00
- Closed at: 2021-04-12T15:02:10+00:00
