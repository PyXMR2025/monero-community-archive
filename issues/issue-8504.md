---
title: Couldn't allocate RandomX cache
source_url: https://github.com/monero-project/monero/issues/8504
author: slurfius
assignees: []
labels:
- mac
created_at: '2022-08-15T14:56:06+00:00'
updated_at: '2024-01-03T05:05:35+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
macOS High Sierra v 10.13.6 
Monero 'Fluorine Fermi' (v0.18.1.0-release)
started to sync but after 5 minutes
Couldn't allocate RandomX cache
error then crashes

# Discussion History
## slurfius | 2022-08-15T14:57:59+00:00
./monerod
2022-08-15 14:28:09.138	I Monero 'Fluorine Fermi' (v0.18.1.0-release)
2022-08-15 14:28:09.139	I Initializing cryptonote protocol...
2022-08-15 14:28:09.139	I Cryptonote protocol initialized OK
2022-08-15 14:28:09.139	I Initializing core...
2022-08-15 14:28:09.140	I Loading blockchain from folder /Users/Jonathan/.bitmonero/lmdb ...
2022-08-15 14:28:11.382	I Loading checkpoints
2022-08-15 14:28:11.383	I Core initialized OK
2022-08-15 14:28:11.383	I Initializing p2p server...
2022-08-15 14:28:11.391	I p2p server initialized OK
2022-08-15 14:28:11.391	I Initializing core RPC server...
2022-08-15 14:28:11.391	I Binding on 127.0.0.1 (IPv4):18081
2022-08-15 14:28:11.414	I core RPC server initialized OK on port: 18081
2022-08-15 14:28:11.415	I Starting core RPC server...
2022-08-15 14:28:11.415	I core RPC server started ok
2022-08-15 14:28:11.416	I Starting p2p net loop...
2022-08-15 14:28:12.420	I 
2022-08-15 14:28:12.420	I **********************************************************************
2022-08-15 14:28:12.420	I The daemon will start synchronizing with the network. This may take a long time to complete.
2022-08-15 14:28:12.420	I 
2022-08-15 14:28:12.420	I You can set the level of process detailization through "set_log <level|categories>" command,
2022-08-15 14:28:12.420	I where <level> is between 0 (no details) and 4 (very verbose), or custom category based levels (eg, *:WARNING).
2022-08-15 14:28:12.420	I 
2022-08-15 14:28:12.420	I Use the "help" command to see the list of available commands.
2022-08-15 14:28:12.420	I Use "help <command>" to see a command's documentation.
2022-08-15 14:28:12.420	I **********************************************************************
2022-08-15 14:28:38.022	I [73.86.233.190:18080 OUT] Sync data returned a new top block candidate: 2688887 -> 2690154 [Your node is 1267 blocks (1.8 days) behind] 
2022-08-15 14:28:38.022	I SYNCHRONIZATION started
2022-08-15 14:28:54.124	I Validating txpool for v15
2022-08-15 14:29:44.833	I Synced 2688907/2690154 (99%, 1247 left)
2022-08-15 14:31:23.676	I Synced 2688927/2690155 (99%, 1228 left, 3% of total synced, estimated 1.4 hours left)
2022-08-15 14:32:24.836	I [67.11.24.221:18080 OUT] Sync data returned a new top block candidate: 2688927 -> 2690155 [Your node is 1228 blocks (1.7 days) behind] 
2022-08-15 14:32:24.836	I SYNCHRONIZATION started
2022-08-15 14:33:25.492	I Synced 2688947/2690155 (99%, 1208 left, 4% of total synced, estimated 1.6 hours left)
2022-08-15 14:34:57.204	I Synced 2688967/2690155 (99%, 1188 left)
2022-08-15 14:36:25.255	I Synced 2688987/2690155 (99%, 1168 left, 7% of total synced, estimated 1.5 hours left)
2022-08-15 14:38:11.576	I [67.11.24.221:18080 OUT] Sync data returned a new top block candidate: 2688987 -> 2690158 [Your node is 1171 blocks (1.6 days) behind] 
2022-08-15 14:38:11.576	I SYNCHRONIZATION started
2022-08-15 14:39:22.827	I Synced 2689007/2690158 (99%, 1151 left, 9% of total synced, estimated 1.7 hours left)
2022-08-15 14:40:08.970	I [78.60.219.169:18080 OUT] Sync data returned a new top block candidate: 2689007 -> 2690160 [Your node is 1153 blocks (1.6 days) behind] 
2022-08-15 14:40:08.970	I SYNCHRONIZATION started
2022-08-15 14:40:38.638	I Synced 2689027/2690161 (99%, 1134 left)
2022-08-15 14:42:02.532	I Synced 2689047/2690162 (99%, 1115 left, 12% of total synced, estimated 1.6 hours left)
2022-08-15 14:43:28.296	I Synced 2689067/2690163 (99%, 1096 left)
2022-08-15 14:44:18.944	I Synced 2689087/2690163 (99%, 1076 left, 15% of total synced, estimated 1.4 hours left)
Couldn't allocate RandomX cache
 

## selsta | 2022-08-15T19:06:25+00:00
How much RAM does your system have and how much free RAM did you have during sync?

## slurfius | 2022-08-15T21:02:04+00:00
20GB of which no more than 3.9GB is used according to activity monitor

## selsta | 2022-08-15T21:02:52+00:00
Do you know how to compile monero manually from source?

## slurfius | 2022-08-15T23:59:28+00:00
i've never tried that before but with instruction probably could do it

## selsta | 2022-08-16T01:45:29+00:00
Do you have homebrew installed?

## bf215181b5140522 | 2022-08-16T02:16:17+00:00
Same issue occurs on macOS 10.12.6, with both the official binary as well as one compiled from source on the target system.

## selsta | 2022-08-16T02:18:37+00:00
So you built the binary on 10.12? And this did not happen before v0.18?

Can you run randomx tests?

```
git clone https://github.com/tevador/RandomX
cd randomx
mkdir build
cd build
cmake ..
make
./randomx-tests
```

## bf215181b5140522 | 2022-08-16T02:26:01+00:00
> 

```[ 1] Cache initialization                     ... PASSED
[ 2] SuperscalarHash generator                ... PASSED
[ 3] randomx_reciprocal                       ... PASSED
[ 4] randomx_reciprocal_fast                  ... PASSED
[ 5] Dataset initialization (interpreter)     ... PASSED
[ 6] Dataset initialization (compiler)        ... PASSED
[ 7] AesGenerator1R                           ... PASSED
[ 8] IADD_RS (decode)                         ... PASSED
[ 9] IADD_RS (execute)                        ... PASSED
[10] IADD_RS with immediate (decode)          ... PASSED
[11] IADD_RS with immediate (decode)          ... PASSED
[12] IADD_M (decode)                          ... PASSED
[13] ISUB_R (decode)                          ... PASSED
[14] ISUB_R (execute)                         ... PASSED
[15] ISUB_R with immediate (decode)           ... PASSED
[16] ISUB_R with immediate (decode)           ... PASSED
[17] ISUB_M (decode)                          ... PASSED
[18] IMUL_R (decode)                          ... PASSED
[19] IMUL_R (execute)                         ... PASSED
[20] IMUL_R with immediate (decode)           ... PASSED
[21] IMUL_R with immediate (execute)          ... PASSED
[22] IMUL_M (decode)                          ... PASSED
[23] IMULH_R (decode)                         ... PASSED
[24] IMULH_R (execute)                        ... PASSED
[25] IMULH_R squared (decode)                 ... PASSED
[26] IMULH_M (decode)                         ... PASSED
[27] ISMULH_R (decode)                        ... PASSED
[28] ISMULH_R (execute)                       ... PASSED
[29] ISMULH_R squared (decode)                ... PASSED
[30] ISMULH_M (decode)                        ... PASSED
[31] IMUL_RCP (decode)                        ... PASSED
[32] IMUL_RCP zero imm32 (decode)             ... PASSED
[33] INEG_R (decode)                          ... PASSED
[34] INEG_R (execute)                         ... PASSED
[35] IXOR_R (decode)                          ... PASSED
[36] IXOR_R (execute)                         ... PASSED
[37] IXOR_R with immediate (decode)           ... PASSED
[38] IXOR_R with immediate (execute)          ... PASSED
[39] IXOR_M (decode)                          ... PASSED
[40] IROR_R (decode)                          ... PASSED
[41] IROR_R (execute)                         ... PASSED
[42] IROL_R (decode)                          ... PASSED
[43] IROL_R (execute)                         ... PASSED
[44] ISWAP_R (decode)                         ... PASSED
[45] ISWAP_R (execute)                        ... PASSED
[46] FSWAP_R (decode)                         ... PASSED
[47] FSWAP_R (execute)                        ... PASSED
[48] FADD_R (decode)                          ... PASSED
[49] FADD_R RoundToNearest (execute)          ... PASSED
[50] FADD_R RoundDown (execute)               ... PASSED
[51] FADD_R RoundUp (execute)                 ... PASSED
[52] FADD_R RoundToZero (execute)             ... PASSED
[53] FADD_M (decode)                          ... PASSED
[54] FADD_M (execute)                         ... PASSED
[55] FSUB_R (decode)                          ... PASSED
[56] FSUB_M (decode)                          ... PASSED
[57] FSCAL_R (decode)                         ... PASSED
[58] FSCAL_R (execute)                        ... PASSED
[59] FMUL_R (decode)                          ... PASSED
[60] FMUL_R RoundToNearest (execute)          ... PASSED
[61] FMUL_R RoundDown/RoundToZero (execute)   ... PASSED
[62] FMUL_R RoundUp (execute)                 ... PASSED
[63] FDIV_M (decode)                          ... PASSED
[64] FDIV_M RoundToNearest (execute)          ... PASSED
[65] FDIV_M RoundDown/RoundToZero (execute)   ... PASSED
[66] FDIV_M RoundUp (execute)                 ... PASSED
[67] FSQRT_R (decode)                         ... PASSED
[68] FSQRT_R RoundToNearest (execute)         ... PASSED
[69] FSQRT_R RoundDown/RoundToZero (execute)  ... PASSED
[70] FSQRT_R RoundUp (execute)                ... PASSED
[71] CBRANCH (decode) 100                     ... PASSED
[72] CBRANCH (decode) 200                     ... PASSED
[73] CBRANCH not taken (execute)              ... PASSED
[74] CBRANCH taken (execute)                  ... PASSED
[75] CFROUND (decode)                         ... PASSED
[76] ISTORE L1 (decode)                       ... PASSED
[77] ISTORE L2 (decode)                       ... PASSED
[78] ISTORE L3 (decode)                       ... PASSED
[79] Hash test 1a (interpreter)               ... PASSED
[80] Hash test 1b (interpreter)               ... PASSED
[81] Hash test 1c (interpreter)               ... PASSED
[82] Hash test 1d (interpreter)               ... PASSED
[83] Hash test 1e (interpreter)               ... PASSED
Assertion failed: (cache != nullptr), function initCache, file /Users/user/Downloads/RandomX/src/tests/tests.cpp, line 24.
[1]    10267 abort      ./randomx-tests

## selsta | 2022-08-16T02:41:29+00:00
And this did not happen before v0.18? And what's the output of `ulimit -a` ?

## bf215181b5140522 | 2022-08-16T02:46:49+00:00
> And this did not happen before v0.18?

That's correct, v0.17 and earlier all seemed to work fine.
`ulimit -a` indicates:
```-t: cpu time (seconds)              unlimited
-f: file size (blocks)              unlimited
-d: data seg size (kbytes)          unlimited
-s: stack size (kbytes)             8192
-c: core file size (blocks)         0
-v: address space (kbytes)          unlimited
-l: locked-in-memory size (kbytes)  unlimited
-u: processes                       709
-n: file descriptors                256

## selsta | 2022-08-16T02:52:29+00:00
```
cd randomx
git checkout master~20
cd build
cmake ..
make
./randomx-tests
```

Does this show the same output?

## bf215181b5140522 | 2022-08-16T02:54:24+00:00
It looks to fail at the same test yes

## selsta | 2022-08-16T02:56:52+00:00
We use a newer SDK to build v0.18 binaries so that we are compatible with Apple Silicon.

What does not make sense currently is that you get the same monerod issue with the self compiled binary as with the release binary.

## selsta | 2022-08-16T03:29:17+00:00
@bf215181b5140522 Can you download and unpack https://bitcoincore.org/depends-sources/sdks/MacOSX10.11.sdk.tar.gz

And then add `-D CMAKE_OSX_SYSROOT=~/Downloads/MacOSX10.11.sdk/` to Makefile on line 103? https://github.com/monero-project/monero/blob/master/Makefile#L103

It should look like this

```
cd $(builddir)/release && cmake -D CMAKE_OSX_SYSROOT=~/Downloads/MacOSX10.11.sdk/ -D BUILD_TESTS=ON -D CMAKE_BUILD_TYPE=Release $(topdir) && $(MAKE)
```

Just make sure to change the path to where the SDK is. Then try to do a clean build on see if you continue to have the same issues.

Build monero like this:

```
make
```

without adding release or anything.

## slurfius | 2022-08-16T04:00:17+00:00
I think the homebrew question is irrelevant now but yes I do have it not very familiar with using it.

## bf215181b5140522 | 2022-08-16T04:39:02+00:00
@selsta So I had to reinstall my system for an unrelated reason between the time when I compiled v0.18 on 10.12.6, which was 3 or 4 days ago, and now, and now I'm having trouble setting up a working build environment on 10.12 again. There seem to be issues with the current versions of some of the dependencies on that old of a macOS version, and I'm not sure which old versions I was using previously when everything worked. In the meantime I'm installing 10.13.6 to test there, but I'm not currently able to test building with the 10.11 SDK.

## tevador | 2022-08-16T06:06:37+00:00
RAM is not an issue here. The mmap call to allocate an executable memory buffer fails [on this line](https://github.com/tevador/RandomX/blob/master/src/virtual_memory.c#L146).

As a temporary workaround, you can start monerod with the environment variable `MONERO_RANDOMX_UMASK=8`. This will disable JIT.

## hyc | 2022-08-16T16:14:25+00:00
Then I guess it's objecting to both PROT_WRITE and PROT_EXEC being requested. Seems that MAP_JIT isn't doing anything useful for us. The v0.17 release had the same mmap flags, so this must be solely due to the SDK version.

## umma08 | 2022-08-20T10:55:41+00:00
> RAM is not an issue here. The mmap call to allocate an executable memory buffer fails [on this line](https://github.com/tevador/RandomX/blob/master/src/virtual_memory.c#L146).
> 
> As a temporary workaround, you can start monerod with the environment variable `MONERO_RANDOMX_UMASK=8`. This will disable JIT.

This works for a period of time (approx syncing for 4000 blocks), until sync process exits with the following error:

```
dyld: lazy symbol binding failed: Symbol not found: _clock_gettime
  Referenced from: /Applications/monero-x86_64-apple-darwin11-v0.18.1.0/./monerod
  Expected in: /usr/lib/libSystem.B.dylib
 
dyld: Symbol not found: _clock_gettime
  Referenced from: /Applications/monero-x86_64-apple-darwin11-v0.18.1.0/./monerod
  Expected in: /usr/lib/libSystem.B.dylib
 
Trace/BPT trap: 5
```

## tevador | 2022-08-20T11:34:55+00:00
That looks like a different error unrelated to RandomX. You might want to open a separate issue.

## slurfius | 2022-08-20T14:30:54+00:00

> As a temporary workaround, you can start monerod with the environment variable `MONERO_RANDOMX_UMASK=8`. This will disable JIT.

How do I change the environment variable?

## tevador | 2022-08-20T15:25:36+00:00
> How do I change the environment variable?

Start monerod like this from the command line: `MONERO_RANDOMX_UMASK=8 ./monerod`

## bf215181b5140522 | 2022-09-18T17:30:07+00:00
> @bf215181b5140522 Can you download and unpack https://bitcoincore.org/depends-sources/sdks/MacOSX10.11.sdk.tar.gz
> 
> And then add `-D CMAKE_OSX_SYSROOT=~/Downloads/MacOSX10.11.sdk/` to Makefile on line 103? https://github.com/monero-project/monero/blob/master/Makefile#L103
> 
> It should look like this
> 
> ```
> cd $(builddir)/release && cmake -D CMAKE_OSX_SYSROOT=~/Downloads/MacOSX10.11.sdk/ -D BUILD_TESTS=ON -D CMAKE_BUILD_TYPE=Release $(topdir) && $(MAKE)
> ```
> 
> Just make sure to change the path to where the SDK is. Then try to do a clean build on see if you continue to have the same issues.
> 
> Build monero like this:
> 
> ```
> make
> ```
> 
> without adding release or anything.

I was able to set up a working build environment on 10.12.6 again, so I tried this. Using the 10.11 SDK, the resulting monerod v0.18.1.1 binary seems to be stable.

I also compiled again with the default system SDK that comes with 10.12, and that indeed causes a crash with the original error from this issue some time into syncing.

I guess it is a macOS bug?

## novice66 | 2022-12-02T23:12:11+00:00
Subject: Couldn't initialize RandomX cache...  This may be the wrong place to comment.  Please redirect me if appropriate.  I downloaded  monero-i686-w64-mingw32-v0.18.1.2 this week.  I'm running monerod.exe in a DOS command window.  Host operating system is Windows 10.  Processor is Xeon x5675.  Installed memory is 32 GBytes.  The daemon appears to start-up sync correctly, and then crashes.  Throws a 'RandomX cache' error message.  Therefore, I believe that the bug is not specific to the Apple/macOS operating system.  Is there a Windows command line switch to disable MAP_JIT?  

Command window trace follows... 
----- ----- --- 

E:\>.\monero-i686-w64-mingw32-v0.18.1.2\monerod.exe --data-dir .\files_blockchain --block-sync-size 20
2022-12-02 21:22:46.868 I Monero 'Fluorine Fermi' (v0.18.1.2-release)
2022-12-02 21:22:46.868 I Initializing cryptonote protocol...
2022-12-02 21:22:46.868 I Cryptonote protocol initialized OK
2022-12-02 21:22:46.870 I Initializing core...
2022-12-02 21:22:46.871 I Loading blockchain from folder .\files_blockchain\lmdb ...
2022-12-02 21:22:48.540 I Loading checkpoints
2022-12-02 21:22:48.541 I Core initialized OK
2022-12-02 21:22:48.541 I Initializing p2p server...
2022-12-02 21:22:48.568 I p2p server initialized OK
2022-12-02 21:22:48.569 I Initializing core RPC server...
2022-12-02 21:22:48.570 I Binding on 127.0.0.1 (IPv4):18081
2022-12-02 21:22:48.601 I core RPC server initialized OK on port: 18081
2022-12-02 21:22:48.619 I Starting core RPC server...
2022-12-02 21:22:48.620 I core RPC server started ok
2022-12-02 21:22:48.621 I Starting p2p net loop...
2022-12-02 21:22:49.621 I
2022-12-02 21:22:49.622 I **********************************************************************
2022-12-02 21:22:49.622 I The daemon will start synchronizing with the network. This may take a long time to complete.
2022-12-02 21:22:49.623 I
2022-12-02 21:22:49.623 I You can set the level of process detailization through "set_log <level|categories>" command,
2022-12-02 21:22:49.623 I where <level> is between 0 (no details) and 4 (very verbose), or custom category based levels (eg, *:WARNING).
2022-12-02 21:22:49.623 I
2022-12-02 21:22:49.624 I Use the "help" command to see the list of available commands.
2022-12-02 21:22:49.624 I Use "help <command>" to see a command's documentation.2022-12-02 21:22:49.624 I **********************************************************************
2022-12-02 21:22:50.343 I [46.28.204.223:18080 OUT] Sync data returned a new top block candidate: 2719741 -> 2768783 [Your node is 49042 blocks (2.2 months) behind]
2022-12-02 21:22:50.344 I SYNCHRONIZATION started
2022-12-02 21:24:06.469 I Synced 2719761/2768783 (98%, 49022 left)
2022-12-02 21:25:01.058 I Synced 2719781/2768783 (98%, 49002 left, 0% of total synced, estimated 1.8 days left)
2022-12-02 21:25:49.665 I Synced 2719801/2768783 (98%, 48982 left)
Couldn't allocate RandomX cache

E:\>pause
Press any key to continue . . .


![daemon_crash_(20221203)](https://user-images.githubusercontent.com/119708974/205404568-9edfec8e-fc55-4851-8973-f0ea5108000b.JPG)



## hyc | 2022-12-03T02:15:26+00:00
If you'r using a Xeon with 32GB of RAM you should be using the x86-64 binaries, not the i686 binaries.

## novice66 | 2022-12-03T02:40:59+00:00
OK.  I'll try it.  Thanks.  

## novice66 | 2022-12-03T11:06:28+00:00
Update:  I've been running the daemon for well over six hours without a crash.  It would seem that running the x86-64 binary version(s) either fixes the bug or else renders it very infrequent.  So, my thanks to hyc for the suggestion.   

# Action History
- Created by: slurfius | 2022-08-15T14:56:06+00:00
