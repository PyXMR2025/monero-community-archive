---
title: Floating point exception on cold start on Chromebook in M99
source_url: https://github.com/xmrig/xmrig/issues/2956
author: textures2
assignees: []
labels: []
created_at: '2022-03-06T14:01:34+00:00'
updated_at: '2022-03-08T10:41:41+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
**Describe the bug**
using v6.16.4 (latest sync) - build from source in Crostini (chromebook linux) using instructions for [Ubuntu](https://xmrig.com/docs/miner/build/ubuntu), encountering `floating point exception` crash.

**To Reproduce**
Invoke the binary:
`./xmrig -o pool.supportxmr.com:3333 -u FOOWALLET -U8 -p crbook -t 2
`
**Expected behavior**
It runs

**Required data**
 - Miner log as text or screenshot _(cannot provide as I can't get that far)_
 - Config file or command line `./xmrig -o pool.supportxmr.com:3333 -u FOOWALLET -U8 -p crbook -t 2` as mentioned above
 - OS: linux/chromeos:
`Linux penguin 5.10.92-14532-g179c52887ab5 #1 SMP PREEMPT Tue Mar 1 18:42:32 PST 2022 x86_64 GNU/Linux`
- For GPU related issues: information about GPUs and driver version.

**Additional context**
This started immediately after upgrading to ChromeOS 99.  The previous version didn't have any issue.

I tried blowing away and creating my linux container anew but that didn't work.  I recompiled from source on a clean image and still encounter the same issue.


# Discussion History
## textures2 | 2022-03-06T14:02:32+00:00
Tried looking through chrome forums etc. but couldn't find anyone who had hit this there.

I have no idea about how to go about troubleshooting this but am glad to help in any way I can.

## textures2 | 2022-03-06T14:07:34+00:00
Also I tried using a prebuilt binary (https://github.com/xmrig/xmrig/releases/download/v6.16.4/xmrig-6.16.4-linux-static-x64.tar.gz) which also had the exact same issue.

## Spudz76 | 2022-03-06T15:55:31+00:00
What does `-U8` do?  I don't see any option that maps to `-U`...

## Spudz76 | 2022-03-06T15:57:19+00:00
Also when I ran on a Chromebook ("Parrot") I nuked ChromeOS and installed a custom coreboot that launches real Linux, and everything worked fine.  The Parrot is Intel based, some Celeron thing, not ARM or anything weird.

## textures2 | 2022-03-07T08:20:59+00:00
There's no way to launch "real linux" on this Chromebook (Acer C933), afaik.

I encountered the same issue without -U8, not sure why that was in my command history:

```
➜  build git:(master) sudo ./xmrig -o pool.supportxmr.com:3333 -u FOOWALLET -p crbook -t 2 --verbose    
[1]    796 floating point exception  sudo ./xmrig -o pool.supportxmr.com:3333 -u  -p crbook -t 2 --verbose
```

## Spudz76 | 2022-03-07T18:27:19+00:00
So the chromebook real-linux [site is here](https://mrchromebox.tech/#devices) and the Acer 314 is listed there as a CB50 protected device but doesn't seem to show a valid FullROM for it.  Note 4 says:
> GeminiLake devices do not have functional legacy boot mode currently; they cannot boot/run anything other than ChromeOS at this time

So I guess you're right that one can't boot real linux. :(

Unsure if xmrig would ever work right in crostini but also can't try it myself because my Parrot board won't turn on anymore after 3 years of 24/7 mining, lol.  Also it was crossflashed to normal PC SeaBIOS.

## textures2 | 2022-03-07T18:31:48+00:00
It was "working fine" until the update to Chrome 99 yesterday.

I tried to review their changelog but could not find anything notable.

## Spudz76 | 2022-03-07T18:35:33+00:00
Interesting.  Perhaps try a rebuild based on the new 99 maybe some libraries changed.

## textures2 | 2022-03-07T18:39:47+00:00
Already did that.  Even nuked the entire chrome-linux image and created a new one.  Installed fresh.  No dice.

## textures2 | 2022-03-07T20:16:23+00:00
I would add print statements or strace or something to debug this if I knew where to start.  If you have suggestions where to look, let me know.  The thing that is so puzzling is it doesn't seem to even get through reading any startup options or command-line parameters.. it just dies instantly.

## Spudz76 | 2022-03-08T03:37:15+00:00
General techniques for running an executable under gdb to get a traceback from a crashpoint work well.

If you compile with debug enabled it will give source file and line information in the traceback which helps a ton.

Relevant cmake options for full debug mode:
```
  -DCMAKE_BUILD_TYPE=Debug \
  -DHWLOC_DEBUG=ON \
  -DWITH_DEBUG_LOG=ON \
  -DWITH_INTERLEAVE_DEBUG_LOG=ON \
  -DCMAKE_EXPORT_COMPILE_COMMANDS=ON \
  -DCMAKE_VERBOSE_MAKEFILE=ON \
```

## Spudz76 | 2022-03-08T03:39:35+00:00
It may be having trouble with MSR, you could try with `-DWITH_MSR=OFF`

N4000 CPU probably does not support the MSRs anyway and maybe it doesn't enjoy being probed, especially via crostini layer which I don't fully understand.

EDIT: or maybe simply at runtime with
```
        "rdmsr": false,
        "wrmsr": false,
```

which on command line without config.json would be
```
 --randomx-no-rdmsr --randomx-wrmsr=-1
```

## textures2 | 2022-03-08T08:37:38+00:00
Using `--randomx-no-rdmsr --randomx-wrmsr=-1` does not help.

Compiling as you suggest fails because of some jacked up log statements:

```
In file included from /home/textures2/xmrig/src/backend/opencl/runners/tools/OclSharedData.cpp:21:
/home/textures2/xmrig/src/backend/opencl/runners/tools/OclSharedData.cpp: In member function ‘uint64_t xmrig::OclSharedData::adjustDelay(size_t)’:
/home/textures2/xmrig/src/backend/opencl/runners/tools/OclSharedData.cpp:92:82: error: ‘id’ was not declared in this scope
   92 |     LOG_WARN("Thread #%zu was paused for %" PRIu64 " ms to adjust interleaving", id, delay);
      |                                                                                  ^~
/home/textures2/xmrig/src/base/io/log/Log.h:143:73: note: in definition of macro ‘LOG_WARN’
  143 | #define LOG_WARN(x, ...)    xmrig::Log::print(xmrig::Log::WARNING, x, ##__VA_ARGS__)
      |                                                                         ^~~~~~~~~~~
/home/textures2/xmrig/src/backend/opencl/runners/tools/OclSharedData.cpp: In member function ‘uint64_t xmrig::OclSharedData::resumeDelay(size_t)’:
/home/textures2/xmrig/src/backend/opencl/runners/tools/OclSharedData.cpp:124:82: error: ‘id’ was not declared in this scope
  124 |     LOG_WARN("Thread #%zu will be paused for %" PRIu64 " ms to before resuming", id, delay);
      |                                                                                  ^~
/home/textures2/xmrig/src/base/io/log/Log.h:143:73: note: in definition of macro ‘LOG_WARN’
  143 | #define LOG_WARN(x, ...)    xmrig::Log::print(xmrig::Log::WARNING, x, ##__VA_ARGS__)
      |                                                                         ^~~~~~~~~~~
```

I've manually edited out the references to ID to get the compile to work and would send a PR for this small issue but not sure if ID should actually be there?

## textures2 | 2022-03-08T08:43:15+00:00
Invoked the executable with no arguments whatsoever with gdb and got the following:

```
➜  build git:(master) ✗ gdb ./xmrig
GNU gdb (Debian 10.1-1.7) 10.1.90.20210103-git
Copyright (C) 2021 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.
Type "show copying" and "show warranty" for details.
This GDB was configured as "x86_64-linux-gnu".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<https://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
    <http://www.gnu.org/software/gdb/documentation/>.

For help, type "help".
Type "apropos word" to search for commands related to "word"...
Reading symbols from ./xmrig...
(gdb) run
Starting program: /home/textures2/xmrig/build/xmrig 
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".

Program received signal SIGFPE, Arithmetic exception.
0x0000555555cc98ab in look_proc (infos=infos@entry=0x555556198220, flags=flags@entry=0, highest_cpuid=highest_cpuid@entry=13, highest_ext_cpuid=highest_ext_cpuid@entry=2147483656, 
    features=features@entry=0x7fffffffdb80, cpuid_type=intel, src_cpuiddump=0x0, backend=<optimized out>, backend=<optimized out>) at topology-x86.c:686
686           infos->ids[CORE] = legacy_log_proc_id / max_nbthreads;
(gdb) 
```

## textures2 | 2022-03-08T08:57:47+00:00
This looks like actually an issue with **lstopo**, I've [opened an issue](https://github.com/open-mpi/hwloc/issues/525) there.

## SChernykh | 2022-03-08T10:03:17+00:00
Try to compile without HWLOC then. `-DWITH_HWLOC=OFF`

## textures2 | 2022-03-08T10:41:41+00:00
`-DWITH_HWLOC=OFF` does work around the issue!

# Action History
- Created by: textures2 | 2022-03-06T14:01:34+00:00
