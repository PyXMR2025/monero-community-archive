---
title: Dynamic automatic thread loading
source_url: https://github.com/xmrig/xmrig/issues/3025
author: NVMDSTEVil
assignees: []
labels:
- question
created_at: '2022-04-17T03:21:56+00:00'
updated_at: '2025-06-16T19:28:52+00:00'
type: issue
status: closed
closed_at: '2025-06-16T19:28:52+00:00'
---

# Original Description
**Describe the bug**
Is there a way to activate/deactivate threads automatically while mining?  Also there seems to be a thread affinity issue when SMT is enabled for Zen 1/1.5 Threadripper/EPYC.  Disabling SMT with memory interleave set to "channel" provides full performance while using stock thread affinity settings for XMRIG with SMT enabled and memory channel set to "auto" or other than "channel" (which should result in only 16 threads used) results in reduced hash rates.  Setting memory interleave to channel forces NUMA mode.

**To Reproduce**
Run XMRIG with thread balancing

**Expected behavior**
Run full threads during operations which use 1MB L3 per thread or less on CPU's which do not have 2MB of L3 per thread. (Ryzen 1/1.5), Intel.  Also upcoming algorithms may need dynamic loading as they may require more than 2MB of L3 per thread which would make thread dynamic loading on current CPU's good to have.

**Required data**
 - OS: ALL

**Additional context**
Some algorithms/coins such as GR/RTM would gain performance with the ability to load more threads dynamically.


# Discussion History
## SChernykh | 2022-04-17T08:50:01+00:00
XMRig already does this for GhostRider. Disabling SMT increases single thread performance in general (not just in XMRig) if you don't need to run 2 threads per core.

"Also upcoming algorithms may need dynamic loading as they may require more than 2MB of L3 per thread" - don't exist yet.

## NVMDSTEVil | 2022-04-17T09:10:10+00:00
Please read closer, XMRIG does not dynamically load the threads in real-time based on algorithm.

## SChernykh | 2022-04-17T09:16:47+00:00
XMRig starts as many threads as specified in config for each algorithm. If algorithm changes, XMRig stops old threads and starts new set of threads for the new algorithm. So it does load threads in real time.

## NVMDSTEVil | 2022-04-17T09:55:36+00:00
That is not what I am talking about.

For GR there are many different algorithms used.  Some would benefit from using full threads.  XMRIG does not recognize this and loads only half the threads on CPU's which have less than 2MB per thread of L3 for ALL of GR.

## SChernykh | 2022-04-17T10:02:50+00:00
XMRig runs full threads for these algorithms. It can run 2 threads per 1 thread specified in config when needed for GhostRider.

## SChernykh | 2022-04-17T10:05:59+00:00
https://github.com/xmrig/xmrig/pull/2712
> XMRig achieves higher hashrates by employing better auto-config and more fine-grained thread scheduling: it can calculate a single batch of hashes using 2 threads for parts that don't require much cache. For example, on a typical Intel CPU (2 MB cache per core) it will use 1 thread per core for cn/fast, and 2 threads per core for other Cryptonight variants while calculating the same batch of hashes, always achieving more than 50% CPU load.

## NVMDSTEVil | 2022-04-17T10:32:02+00:00
You obviously do not understand the question, please stop replying.

## SChernykh | 2022-04-17T10:37:06+00:00
You obviously can't properly formulate your own question.

## snipeTR | 2022-04-17T15:13:45+00:00
question? lol
Is there a way to activate/deactivate threads automatically while mining?


> XMRig already does this for GhostRider. Disabling SMT increases single thread performance in general (not just in XMRig) if you don't need to run 2 threads per core.
> 
> "Also upcoming algorithms may need dynamic loading as they may require more than 2MB of L3 per thread" - don't exist yet.



## SChernykh | 2022-04-17T15:25:44+00:00
Also, you obviously don't realize that if I don't understand your question, no one else will help you. Because I will be the one implementing changes to XMRig in the end. The way I see it, you just don't understand that if XMRig says "8 threads" in the console on 8-core Zen1 when mining GhostRider, it doesn't mean XMRig will not use 16 threads on algorithms that require <= 1 MB L3. It will switch to 16 threads dynamically, this is how it worked with GhostRider from the beginning.

Edit: this is assuming you don't use `-t` or `--threads` in XMRig command line. Explicitly setting number of threads in the command line turns off dynamic thread allocation.

## NVMDSTEVil | 2022-04-17T19:40:02+00:00
If  this is how it operates then it does not seem to work or is broken and losing performance as in GR my Threadripper 1950x system in linux gets 2.35Kh average with SMT manually disabled and NUMA mode forced on vs letting XMRIG choose its own threads with no modification whatsoever, which only manages on average 1.8-1.9Kh (24-48hrs minimum testing time for averages).

Watching core use levels does not seem to indicate any thread or load use changes during algorithm switches between high L3 and low L3 use algorithms.

Also there is a larger NUMA bug present with Gen 1/1.5 Threadripper/Epyc as this same change (disabling SMT) allows more performance for XMR as well - ~12Kh vs 9Kh.

Linux Mint Cinnamon 20.3 with latest Kernel is the current run environment.

This has also been the same with many other people I have been in contact with for Gen 1/1.5 Threadripper/Epyc cpu's on multiple OS's, this is not just a "my rig" problem.  It may even help Gen 1/1.5 Ryzen desktop parts, but I have yet to be able to test one on hand.

## NVMDSTEVil | 2022-04-17T20:45:53+00:00
For fun, here is the built-in benchmark for XMRIG.

Settings were as follows:
3.8Ghz, all c-states/power etc disabled to lock cores at 3.8Ghz with no changes.
IF power down disabled to lock IF to high performance mode
8x8GB 2933mhz memory 14-16-16-32-1T-Gear Down 0 with 4Gb chips (4 ranks per channel)
Memory interleave in Channel mode (forced NUMA)
opcache disabled in bios

![image](https://user-images.githubusercontent.com/95266968/163731470-7eb2c780-b224-4b60-b616-ace0bb657853.png)


## NVMDSTEVil | 2022-04-28T17:36:26+00:00
So, no ideas on why performance sucks for XMR and RTM with SMT enabled?  

I would love to give a an Epyc 7301/7351/7371 (Gen 1 ryzen, 2mb per thread even with SMT enabled) a try to see if the issue it literally due to thread-count (utilized or not) vs L2 size.. but I dont have one so I cant.  May be testing more algorithms in the future to add results but I havent had any time to do much due to busy season on the farm.

Have picked up a 2990wx to do some testing on when I get time but that's still a 1MB per thread cpu.  The 1.33MB/thread Ryzen 1's dont seem to suffer the issue quite as drastically.

Just for the record I think this may be related to the testing that Level1tech's did where there were performance issues due to thread control of the OS.  Supposedly its been fixed in Linux and Windows since then, but I dont think it ever really was as I have been able to cause the issues still in other programs (a good test I found is "Indigo Benchmark", the results can vary wildly between runs and reboots and different thread clamping methods).

 "cache_qos": true, has no effect, probably only works on Intel CPU's?

# Action History
- Created by: NVMDSTEVil | 2022-04-17T03:21:56+00:00
- Closed at: 2025-06-16T19:28:52+00:00
