---
title: 'Hope to see more optimization for M1 Mac mini '
source_url: https://github.com/xmrig/xmrig/issues/2288
author: xq0404
assignees: []
labels: []
created_at: '2021-04-19T15:32:50+00:00'
updated_at: '2025-06-16T20:33:59+00:00'
type: issue
status: closed
closed_at: '2025-06-16T20:33:59+00:00'
---

# Original Description
This is among the rarest miners with a version for ARM chip-based M1 Mac mini .  That said, I would much appreciate it if more optimization is done for the new M1 lineup.  After all, the new M1 Macs has much faster CPUs than their counterparts have.  

M1 Mac mini's hash rate of around  2400 H/s is a little too slow.  Although it does not support hyperthreading, M1 has  achieved super fast singe core performance.  




# Discussion History
## xq0404 | 2021-04-23T03:53:54+00:00
Also I can't get  huge pages or 1GB pages enabled.

## Lonnegan | 2021-04-23T06:33:30+00:00
https://github.com/xmrig/xmrig/issues/1991

Huge pages not supported by Apple
RandomX JIT compiler can work only in slow secure mode on M1
Only 4 performance cores
The 4 slow cores have only 4 MB LL cache together, so only 2 cores can be fed

Sum all this up and you get a quite decent performance. 2300 H/s is still good for an ARM design thanks to the high single thread performance, but compared to the Zen 2/3 CPUs, the M1 lack cache and cores to compete

## RS102839 | 2021-04-24T02:20:52+00:00
It appears that JIT can be made to work for M1 processors

https://developer.apple.com/documentation/apple-silicon/porting-just-in-time-compilers-to-apple-silicon

## AndyRPH | 2021-04-25T19:22:35+00:00
It looks like those recommendations are already in the xmrig code.  In another issue it was stated that you can build from source with some flags that'll import into Xcode, add the entitlement, and then compile, but it didn't materially change the hash rate when tried.   Still probably looking at other bottlenecks in the M1 cache system or how MacOS exposes various pieces of the hardware impacting the efficiency of the code.  

Just because they're awesome new chips doesn't mean they're going to blow away the competition in every field, like CPU mining.  Look at the GPU side of things, it's supposed to have some awesome GPU, but nobody to my knowledge has been able to write a decent GPU miner for it since the GPU is largely custom hardware and not well documented at a low level.  Apple expects developers to use existing GPU tools they provide, which don't really lend themselves to GPU processing crypto mining. 

## xq0404 | 2021-04-26T14:53:55+00:00
> 
> 
> #1991
> 
> Huge pages not supported by Apple
> RandomX JIT compiler can work only in slow secure mode on M1
> Only 4 performance cores
> The 4 slow cores have only 4 MB LL cache together, so only 2 cores can be fed
> 
> Sum all this up and you get a quite decent performance. 2300 H/s is still good for an ARM design thanks to the high single thread performance, but compared to the Zen 2/3 CPUs, the M1 lack cache and cores to compete

Yes, M1's performance is at the same level as that of AMD Ryzen™ 9 5900HS, its latest laptop CPU (TDP 35W).
But AMD Ryzen™ 9 5900HX performs much faster (about 6000 H/s, TDP 45+W).  Both AMD laptop CPUs are 8-core ones.

## Lonnegan | 2021-04-26T15:24:51+00:00
> Yes, M1's performance is at the same level as that of AMD Ryzen™ 9 5900HS, its latest laptop CPU (TDP 35W).

Not even near!

## risner | 2021-04-29T03:18:05+00:00
https://patchwork.kernel.org/project/linux-arm-kernel/patch/20140628104057.3684.93274.stgit@localhost6.localdomain6/
Is it currently using the Neon sha512 special instructions?

I also couldn’t get OpenCL working. When enabled it tried to compile and failed then disabled it.

## risner | 2021-04-30T01:48:30+00:00
I also found these:
https://www.google.com/amp/s/blog.min.io/accelerating-sha256-by-100x-in-golang-on-arm/amp/

It shows a 100 times improvement (6 MB/s to 615MB/s) going from unaccelerated code to 64 bit arm SHA commands (sha256h, sha256h2, sha256su0 and sha256su1).

Here is the 64 bit code they implemented:
https://github.com/minio/sha256-simd/blob/6de4475307716de15b286880ff321c9547086fdd/sha256block_arm64.s

## RS102839 | 2021-04-30T16:13:59+00:00
@risner: Doesn't appear relevant to CPU-based mining using RandomX.

> I also found these:
> https://www.google.com/amp/s/blog.min.io/accelerating-sha256-by-100x-in-golang-on-arm/amp/
> 
> It shows a 100 times improvement (6 MB/s to 615MB/s) going from unaccelerated code to 64 bit arm SHA commands (sha256h, sha256h2, sha256su0 and sha256su1).
> 
> Here is the 64 bit code they implemented:
> https://github.com/minio/sha256-simd/blob/6de4475307716de15b286880ff321c9547086fdd/sha256block_arm64.s

Doesn't appear relevant to CPU-based mining using RandomX.

## xq0404 | 2021-05-02T00:36:31+00:00
> 
> 
> @risner: Doesn't appear relevant to CPU-based mining using RandomX.
> 
> > I also found these:
> > https://www.google.com/amp/s/blog.min.io/accelerating-sha256-by-100x-in-golang-on-arm/amp/
> > It shows a 100 times improvement (6 MB/s to 615MB/s) going from unaccelerated code to 64 bit arm SHA commands (sha256h, sha256h2, sha256su0 and sha256su1).
> > Here is the 64 bit code they implemented:
> > https://github.com/minio/sha256-simd/blob/6de4475307716de15b286880ff321c9547086fdd/sha256block_arm64.s
> 
> Doesn't appear relevant to CPU-based mining using RandomX.

I'm afraid not.  

## RS102839 | 2021-05-03T21:06:31+00:00
BTW:  @xq0404 Not at all rare

The best thing would to get a Metal version of the OpenCL code, and then we could run a GPU-based executable and a CPU-based executable at the same time.
Just checked on resource use and xmrig is only using 2.5GB of memory, even though I'm on a 16GB Mac Mini M1, so I definitely have enough memory to run a second GPU-based instance, its just the current instance uses 98% of my CPU whenever it can.

## RS102839 | 2021-05-03T21:12:45+00:00
> https://patchwork.kernel.org/project/linux-arm-kernel/patch/20140628104057.3684.93274.stgit@localhost6.localdomain6/
> Is it currently using the Neon sha512 special instructions?
> 
> I also couldn’t get OpenCL working. When enabled it tried to compile and failed then disabled it.

Some people are commenting on the internet about successfully building other miners OpenCL (not RandomX) code working on MacOS M1, so maybe that's an alternative?

## risner | 2021-05-10T03:43:19+00:00
I think super pages work on M1 Mac's.

https://raw.githubusercontent.com/brinlyau/xnu-source/e73593944b2bcca2fe76b7cd2d939fda0afc4449/tools/tests/superpages/measure_tlbs.c

This file is all over the internet, as part of macos source.

I've compiled it on an M1 Mac.
The TRUE on testt is whether or not to use super pages.
                        time1 = testt(TRUE, mode, 0, kb);       // read super
                        time4 = testt(FALSE, mode, 1, kb);      // write base
Running it, we see times for super and not super:
4; 0; 595; 0; 541; 0; 374; 0; 371; 0; 352; 0; 331

Is it possible they changed how to request super pages on macos big sur for M1?

## xq0404 | 2021-05-10T05:01:30+00:00
> I think super pages work on M1 Mac's.
> 
> https://raw.githubusercontent.com/brinlyau/xnu-source/e73593944b2bcca2fe76b7cd2d939fda0afc4449/tools/tests/superpages/measure_tlbs.c
> 
> This file is all over the internet, as part of macos source.
> 
> I've compiled it on an M1 Mac.
> The TRUE on testt is whether or not to use super pages.
> time1 = testt(TRUE, mode, 0, kb); // read super
> time4 = testt(FALSE, mode, 1, kb); // write base
> Running it, we see times for super and not super:
> 4; 0; 595; 0; 541; 0; 374; 0; 371; 0; 352; 0; 331
> 
> Is it possible they changed how to request super pages on macos big sur for M1?

Have you experimented with inserting the content of https://raw.githubusercontent.com/brinlyau/xnu-source/e73593944b2bcca2fe76b7cd2d939fda0afc4449/tools/tests/superpages/measure_tlbs.c into xmrig's  config.json to enable super pages?

## risner | 2021-05-10T12:33:13+00:00
I haven't had time to figure out where the malloc() is located.

In the measure_tlbs.c code, it doesn't use malloc(), it uses:
char *data;
mach_vm_address_t addr = 0;
int kr;
mach_vm_size_t  size = SUPERPAGE_ROUND_UP(pages*PAGE_SIZE); /* allocate full superpages */
kr = mach_vm_allocate(mach_task_self(), &addr, size,
     VM_FLAGS_ANYWHERE | (superpages? VM_FLAGS_SUPERPAGE_SIZE_2MB : VM_FLAGS_SUPERPAGE_NONE));
if (!addr)
     return 0;
data = (char*)(long)addr;

So you need to avoid using malloc() I guess.

If anyone can point me to the location in code it tries to malloc() a page with the if or inline for getting a hugepage or not I can try to test.

## Spudz76 | 2021-05-10T17:44:45+00:00
`mach_vm_allocate` sure sounds like it happens inside some sort of VM (sandbox) which isn't going to really be fast like true raw hardware access.  Not as terrible as trying to mine through Rosetta with x64 miner code, but almost.

Probably same sort of problem as their implementation of JIT which adds a bunch of slow extra handshaking for "security".

## RS102839 | 2021-05-10T18:51:45+00:00
> `mach_vm_allocate` sure sounds like it happens inside some sort of VM (sandbox) which isn't going to really be fast like true raw hardware access. Not as terrible as trying to mine through Rosetta with x64 miner code, but almost.
> 
> Probably same sort of problem as their implementation of JIT which adds a bunch of slow extra handshaking for "security".

Doesn't `mach` contain the freeBSD alternative to `mmap`, which is itself a virtual system?

[https://en.wikipedia.org/wiki/Mach_(kernel)](https://en.wikipedia.org/wiki/Mach_(kernel))

Presume it would be an unacceptable solution to rewriting all the `mmap` calls for MacOS.

It seems like the code to implement JIT had the effect of sidestepping the ability to have huge (2MB) pages.



## risner | 2021-05-10T19:57:48+00:00
macOS runs under mach.
Mach is a micro kernel.
Mmap is the macOS interface to mach_vm_allocate().

Sounds like they have a bug or something that prevents us from using the mmap interface.

Especially considering a benchmark show a slight speed up.

Huge pages were side stepped because mmap() isn’t working.

## Spudz76 | 2021-05-11T19:53:14+00:00
Yes but I noted the include file mach.h which is for the native kernel, while mach_vm.h alludes it is for virtual machine.

Perhaps they just call every process a virtual machine because everything is a sandbox.  They built their OS like it's Java, lol.

## risner | 2021-05-11T19:55:43+00:00
vm = virtual memory in that context, not virtual machine. Virtual machines were not even a concept at that time in history (80's and early 90's).

## risner | 2021-05-11T19:57:14+00:00
Put a little more clearly, there appears to be a bug in the wrapper function (mmap) on Arm Mac's accessing the underlying api function mach_vm_allocate().

I don't know this code base well enough to modify it to use mach_vm_allocate() instead of mmap() on Arm Macs.

## Spudz76 | 2021-05-11T20:08:12+00:00
AHA! thanks.  Forgot about virtual memory as another "VM".  And that makes a lot more sense.

What doesn't make sense is not using the standard functions and making their own.  Let's be UNIX based but then break everything, good idea.

## risner | 2021-05-11T20:30:52+00:00
Just so we are all on the same page, they didn't make their own.

The mach kernel has a limited number of traps (system calls). Last I recall a total of 34. I'm sure Apple has added some.
Linux has at last I recall over 300.

All of the normal BSD calls running in the BSD system under Mach on MacOS has to boil down to underlying mach calls for hardware stuff. So to get virtual memory, to read/write from/to a device, etc.

So they didn't make their own, they started with mach, added FreeBSD (yes not just straight BSD) as a mach subsystem, and extended.

## Spudz76 | 2021-05-12T04:43:26+00:00
I see, that must be why it also works for heck on FreeBSD, lol.

I guess maybe I could install FreeBSD somewhere and see if I can make it work, and it may cross-apply then.

## Spudz76 | 2021-05-12T06:30:08+00:00
Okay, Installed FreeBSD 13 and all the stuff needed and it built first try, and runs.  Claims to support hugepages.

## Spudz76 | 2021-05-12T06:58:34+00:00
Found where it does Apple specific things, fake-set XMRIG_OS_APPLE to see how bad FreeBSD crashes acting like it's OSX.  Looks like it does have `mach_vm_allocate` in a compat header maybe I can test the interface that way...

## RS102839 | 2021-05-12T14:22:47+00:00
> Put a little more clearly, there appears to be a bug in the wrapper function (mmap) on Arm Mac's accessing the underlying api function mach_vm_allocate().
> 
> I don't know this code base well enough to modify it to use mach_vm_allocate() instead of mmap() on Arm Macs.

I looked at this, but the (undocumented) code-base is a challenge.
You can pass mach_vm.... flags through the MacOS mmap() but they cause crashes (not a surprise), so that doesn't appear to be an option.
I suspect there's a core MacOS restriction on triggering JIT with huge pages, as other projects seem to be hitting the same situation (ex: nodejs).   So we might be dependent on Apple fixing this, and that's only going to happen if some project that they really care about is impacted by the restriction.

In other words, switching to the native mach_vm_..() functions probably isn't going to solve the apparent problem where JIT is incompatible with superpages.

## risner | 2021-05-12T14:43:56+00:00
> In other words, switching to the native mach_vm_..() functions probably isn't going to solve the apparent problem where JIT is incompatible with superpages.

Thank you. That post clarified a lot for me. Your mentioning of other projects experiencing similar issue seems to reconcile with the fact the test code works but using that ram in a certain way (e.g. JIT) fails.


## Spudz76 | 2021-05-12T20:00:30+00:00
I think I saw some sample code somewhere about how to use hugepages + JIT together.  Even if that isn't possible the blocker seems to be that you can't execute stuff out of hugepage allocations, but data hugepages with execute disabled should still be allowed... OR perhaps the hack was to step through your hugepage allocation by normal-page-sizes and set all those execute permissible (loop of 512 4096b chunks per 2MB hugepage? waste of time but so is everything with JIT on M1, at least it's just setup time not every JIT recompile (hopefully))... but even if not there could be a halfway compromise and most of the speedup as far as I can tell is from the dataset being hugepaged, more so than the execution/JIT code which could stay in normal pages without much performance hit.

Obviously trying to trick FreeBSD to compile like it was Apple doesn't work, it blew up earlier than the VirtualMemory file in some Threads stuff.  Briefly looked at how to make FreeBSD use XNU/IOKit/etc like a FreeMacOS, but that seemed even less possible and questionably useful even if I did figure it out.

Plowing ahead, I figured out how to get some MacOS access but it's High Sierra on x64.  Waiting for all the brew junk... everything is saying it's too old, lol.  But I also wanted to test CUDA and it doesn't work on anything newer.  The hardware it's running on doesn't have avx2 so I don't think newer works anyway.  But I only know what the Internet says, haven't touched MacOS since the single digit 2000's.  High Sierra is "new" to me lol.

## risner | 2021-05-12T20:33:49+00:00
I have a spare box on M1 Mac, that could be used to test. If I recall this all works correctly on Intel Mac's. If there is uncertainty I can test that and make sure there are JIT and huge pages on Intel MacOS.

If you like I can set it up and create an account on the M1 Mac for you. I don't know how to private message the password tho?

## Spudz76 | 2021-05-12T21:46:25+00:00
Yep, hugepages already work on 10.3/x64
![image](https://user-images.githubusercontent.com/2391234/118048160-1ca4c400-b339-11eb-9d6a-2da33e814634.png)

But, I think it can use the M1 methods anyway, going to try to force it.

## AndyRPH | 2021-05-12T22:08:40+00:00
For what it's worth, I had compiled it via Xcode and added the flags for it to have the entitlements to do JIT apple's way and whatnot.  Didn't have a meaningful impact on hashrate as the developer has stated, but also didn't seem to like superpages.  

If you get far enough that you think you've got better code in a branch I can certainly test it.  Can't offer up an account to test with like above, but that's a sweet offer! 

## Spudz76 | 2021-05-13T12:41:13+00:00
Got it allocating by calling `mach_vm_allocate` and it works same as mmap.  Suppose I do require M1 access to see if any of it helps there, just SSH is fine, I can send you a ssh public key to stuff into `authorized_keys`?  Since then the password is my 4096bit private key and the public string is literally useless to anyone, way better than some typed password.  I can also tell you my source IP and then you can pinhole the ssh port just for that IP, extra secure.

Or I will commit what I think might work, to a branch on my fork.  Or I can drop patch files here.

EDIT: here's one that might do something, or at least show how to come up with an allocation and act like mmap...

[m1-huge-test001.patch.txt](https://github.com/xmrig/xmrig/files/6472509/m1-huge-test001.patch.txt)

Essentially some dirty copy and paste and adjustment based on [this sample](https://opensource.apple.com/source/xnu/xnu-2050.7.9/tools/tests/superpages/testsp.c)

## RS102839 | 2021-05-13T14:09:03+00:00
@Spudz76

That code works, but I'm not seeing any improvement in hash rates

`./xmrig -k --tls --config=../config.json
 * ABOUT        XMRig/6.12.1 clang/12.0.5
 * LIBS         libuv/1.41.0 OpenSSL/1.1.1j hwloc/2.4.1
 * HUGE PAGES   supported
 * 1GB PAGES    unavailable
 * CPU          Apple M1 (1) 64-bit AES
                L2:16.0 MB L3:0.0 MB 8C/8T NUMA:1
 * MEMORY       15.7/16.0 GB (98%)
 * DONATE       1%
 * POOL #1      [REDACTED] algo rx/0
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       disabled
[2021-05-13 11:11:17.667]  net      use pool [REDACTED]
[2021-05-13 11:11:17.668]  net      fingerprint (SHA-256): [REDACTED]
[2021-05-13 11:11:17.668]  net      new job from [REDACTED] algo rx/0 height 356398
[2021-05-13 11:11:17.668]  cpu      use argon2 implementation default
[2021-05-13 11:11:17.668]  randomx  init dataset algo rx/0 (8 threads) seed [REDACTED]
allocating 1040 hugepages
kr:4 g_a:0
allocating 128 hugepages
kr:4 g_a:0
[2021-05-13 11:11:17.668]  randomx  allocated 2336 MB (2080+256) huge pages 0% 0/1168 +JIT (0 ms)
[2021-05-13 11:11:26.715]  net      new job from [REDACTED] algo rx/0 height 356399
[2021-05-13 11:11:27.039]  randomx  dataset ready (9370 ms)
[2021-05-13 11:11:27.039]  cpu      use profile  rx  (8 threads) scratchpad 2048 KB
allocating 1 hugepages
kr:4 g_a:0
allocating 1 hugepages
kr:4 g_a:0
allocating 1 hugepages
kr:4 g_a:0
allocating 1 hugepages
kr:4 g_a:0
allocating 1 hugepages
kr:4 g_a:0
allocating 1 hugepages
kr:4 g_a:0
allocating 1 hugepages
kr:4 g_a:0
allocating 1 hugepages
kr:4 g_a:0
allocating 1 hugepages
kr:4 g_a:0
allocating 1 hugepages
kr:4 g_a:0
allocating 1 hugepages
kr:4 g_a:0
allocating 1 hugepages
kr:4 g_a:0
allocating 1 hugepages
kr:4 g_a:0
allocating 1 hugepages
kr:4 g_a:0
allocating 1 hugepages
kr:4 g_a:0
allocating 1 hugepages
kr:4 g_a:0
allocating 1 hugepages
kr:4 g_a:0
[2021-05-13 11:11:27.048]  cpu      READY threads 8/8 (8) huge pages 0% 0/8 memory 16384 KB (10 ms)
[2021-05-13 11:11:39.012]  cpu      accepted (1/0) diff 100001 (1439 ms)
[2021-05-13 11:11:39.012]  cpu      accepted (1/0) diff 100001 (1439 ms)
[2021-05-13 11:11:59.189]  net      new job from [REDACTED] algo rx/0 height 356400
[2021-05-13 11:12:08.015]  net      new job from [REDACTED] algo rx/0 height 356400
[2021-05-13 11:12:27.439]  miner    speed 10s/60s/15m 924.0 n/a n/a H/s max 931.3 H/s
[2021-05-13 11:12:44.879]  cpu      accepted (2/0) diff 60000 (143 ms)
[2021-05-13 11:13:08.000]  net      new job from [REDACTED] algo rx/0 height 356400
[2021-05-13 11:13:08.350]  cpu      accepted (3/0) diff 43620 (152 ms)
[2021-05-13 11:13:27.897]  miner    speed 10s/60s/15m 2298.7 1252.7 n/a H/s max 2298.7 H/s
[2021-05-13 11:13:44.572]  cpu      accepted (4/0) diff 43620 (151 ms)
[2021-05-13 11:14:06.971]  cpu      accepted (5/0) diff 43620 (154 ms)
[2021-05-13 11:14:08.007]  net      new job from [REDACTED] algo rx/0 height 356400
[2021-05-13 11:14:28.350]  miner    speed 10s/60s/15m 2223.5 2279.1 n/a H/s max 2329.5 H/s
[2021-05-13 11:14:33.530]  cpu      accepted (6/0) diff 51300 (147 ms)
[2021-05-13 11:14:56.799]  cpu      accepted (7/0) diff 51300 (145 ms)
[2021-05-13 11:15:05.925]  cpu      accepted (8/0) diff 51300 (139 ms)
[2021-05-13 11:15:08.008]  net      new job from [REDACTED] algo rx/0 height 356400
[2021-05-13 11:15:28.822]  miner    speed 10s/60s/15m 2276.2 2206.0 n/a H/s max 2329.5 H/s
[2021-05-13 11:15:41.134]  cpu      accepted (9/0) diff 57990 (179 ms)
[2021-05-13 11:15:49.459]  net      new job from [REDACTED] algo rx/0 height 356401`

## RS102839 | 2021-05-13T16:07:49+00:00
@Spudz76
Maybe there's a missing change?

`[2021-05-13 11:47:29.761]  randomx  init dataset algo rx/0 (8 threads) seed [REDACTED]`
`allocating 1040 hugepages`
`kr:4 g_a:0`
`allocating 128 hugepages`
`kr:4 g_a:0`
`[2021-05-13 11:47:29.761]  randomx  allocated 2336 MB (2080+256) huge pages 0% 0/1168 +JIT (1 ms)`



## risner | 2021-05-13T20:26:28+00:00
Ok I've added an account to 204.152.115.253 as spudz76.
If you give me the ssh pub I'll add to authorized.

## Spudz76 | 2021-05-13T21:30:44+00:00
Thanks so much @risner
```
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDIJ3ue6CZbSivVG9vw6QyZkNkEnoYP7N03PAcUT447o7BNKj2KBjJ9vBJuSr+1AF6908/NprKYy/oQ/WQrNSbloUBdTaaHANitJh+qxzw/QAg86aJLGo3TqELkfPNPKUzfzt/bq7xsjKCKNaBGju3rf1DGcHvNrfL3xX6B6elt4d2hgyY8fZ7EqUo8XciNWZFIYZVSTsxvnIeyF9VDT9tPAxbxpYPP7b1WEZ3GxiSc9qcZ2bdUJItz5b/KmV8MPoS9aAP1weJa6m8HOEQuSIOt9/xH8nb9DOfiPW13Y+hi6z+D1jexrZtH9D8OPX+kah4wGinoHPpuysVUfzAHSJv7UDknl4d4icpixo+y6sMDZGAgVi66ic3SKa2bv+HqCdcNftugkFFkOLjHTcqUse6Cn1xMEWoBFkyX+kN0QfvMBsQ5jblC9zblQk6UCoSETDofjzV3aZmplvzanvzhUE7udNhpQHC1GlAj4064CjULkWRjYiCnp9IVnQZNDWoMl8yZB1rx3wpexGnz4sVUWyNjAbzWzODCB+HOdHOyhz+KCU6bcvYe4vRVSUoU6gYwXJjuC2EM0dtApX1/h9yE45yqgIdsjh2lIv/XaZP0+fSdJrnCe2vs2qAG9b2n39ZxS28EDRfE6WQfow49J2oGPdGba5XjW7cRoOiUv7yJFpLFyw== spudz76@github
```

## Spudz76 | 2021-05-13T21:39:08+00:00
@RS102839 the interesting bit is the call returns a kernel return value of 4 (`KERN_INVALID_ARGUMENT`) instead of 0 (`KERN_SUCCESS`), and doesn't give the allocation (global_address stays zero).  Good to know it fails properly (fallback to non-huge) rather than fully crashing. Now to try and figure out which argument it hates, and if it's the 2MB one then I guess all the rumors are true.  I still have a feeling it's just really non-intuitive as to what the rules are similar to M1 being the only platform that needs additional JIT security.

## Spudz76 | 2021-05-13T21:49:13+00:00
Today's hearty chuckle:

![image](https://user-images.githubusercontent.com/2391234/118191909-92c12d80-b402-11eb-9783-ee13c7694e9c.png)

Not possible it has never been mentioned somewhere on there.  Scrubbed?  Shadow banned?  hahaha

Using the "improper" name superpages there are some results but the search is pretty horrible as far as forcing both search terms to be in the results.  But found [this from a month ago](https://developer.apple.com/forums/thread/677402) with a whole lot of silence from Apple (seems about right).

OH MY HECK this developer.apple.com site is one of the slowest forums I've ever seen.  Next page takes 20 seconds to even respond.

## Spudz76 | 2021-05-13T22:21:28+00:00
Things I've found seem like a few problems:
* AppleSilicon M1 only supports 4K or 16K "huge" aka "super" pages (16K is not very "super"...)
* Allocations from mach_vm_allocate are not allowed to be accessed by the allocating tasks children (WTF! Big Sur on x64 still allows this...)

@RS102839  Swap the `VM_FLAGS_SUPERPAGE_SIZE_2MB` to `VM_FLAGS_SUPERPAGE_SIZE_ANY` and see if it allocates some 16KB ones maybe.  As far as I can tell ANY means best available... and of course there is no `VM_FLAGS_SUPERPAGE_SIZE_16KB` to be explicit about asking for the weird-M1-only-sized-super-pages.

## risner | 2021-05-13T23:13:28+00:00
Spudz76, try now.

## RS102839 | 2021-05-13T23:48:39+00:00
@Spudz76 

Sorry, but `VM_FLAGS_SUPERPAGE_SIZE_ANY` had same effect.

However this seemed to work:
`kr = mach_vm_allocate(mach_task_self(), &global_addr, size, VM_FLAGS_ANYWHERE /*VM_FLAGS_SUPERPAGE_SIZE_2MB*/ );`

`[2021-05-13 19:53:38.050]  randomx  init dataset algo rx/0 (8 threads) seed ffb9df6b3b1ad713...`
`allocating 1040 hugepages`
`kr:0 g_a:280000000`
`allocating 128 hugepages`
`kr:0 g_a:103474000`
`[2021-05-13 19:53:38.405]  randomx  allocated 2336 MB (2080+256) huge pages 100% 1168/1168 +JIT (355 ms)`
`[2021-05-13 19:53:46.836]  randomx  dataset ready (8431 ms)`
`[2021-05-13 19:53:46.837]  cpu      use profile  rx  (8 threads) scratchpad 2048 KB`
`allocating 1 hugepages`
`kr:0 g_a:113474000`
`allocating 1 hugepages`
`kr:0 g_a:114000000`
`allocating 1 hugepages`
`kr:0 g_a:114200000`
`allocating 1 hugepages`
`kr:0 g_a:114400000`
`allocating 1 hugepages`
`kr:0 g_a:114600000`
`allocating 1 hugepages`
`kr:0 g_a:114800000`
`allocating 1 hugepages`
`kr:0 g_a:114a00000`
`allocating 1 hugepages`
`kr:0 g_a:114c00000`
`allocating 1 hugepages`
`kr:0 g_a:114e00000`
`[2021-05-13 19:53:46.844]  cpu      READY threads 8/8 (8) huge pages 100% 8/8 memory 16384 KB (8 ms)`


However, not seeing any improvement in hashrates:
`[2021-05-13 19:59:49.554]  miner    speed 10s/60s/15m 2253.0 2235.1 n/a H/s max 2316.0 H/s`


More:
These also returned errors: `VM_FLAGS_RETURN_4K_DATA_ADDR` and `VM_FLAGS_USER_ALLOCATE` and `VM_FLAGS_SUPERPAGE_SIZE_2MB`


## risner | 2021-05-13T23:58:57+00:00
forgot this step chown spudz75 authorized_keys
try again

## Spudz76 | 2021-05-14T00:15:33+00:00
Also has to be `chmod 0600` or ssh won't read it

## Spudz76 | 2021-05-14T00:18:36+00:00
@RS102839 Yes that likely just did the same as a normal allocation non-hugepage (but the xmrig code thought it got hugepages) therefore the identical performance along with the all green allocations.  But good to know mach_vm_allocate works at all / child inheritance may not be broken...

## Spudz76 | 2021-05-14T00:22:40+00:00
Something I'm chasing now is rumors that you have to allocate 2MB pages tied to a task that is allowed to use them, like task(0) the kernel itself or something weird, and then set allowances for the task(s) you want to be able to access the "kernel region".  Somewhat more similar to how Linux requires root to reserve hugepages, after which any regular userspace app can use them.

Also wonder if it acts different in any of the above variations, running under sudo...

## risner | 2021-05-14T00:24:02+00:00
Ok try 3. Sheesh.
# ls -ld /Users/spudz76/.ssh /Users/spudz76/.ssh/authorized_keys
drwx------  3 spudz76  staff   96 May 13 19:07 /Users/spudz76/.ssh
-rw-------  1 spudz76  staff  740 May 13 19:07 /Users/spudz76/.ssh/authorized_keys

## Spudz76 | 2021-05-14T00:28:33+00:00
Nope, lol.  Make sure the pasted key is still all on one line and didn't get "wrapped" or that also doesn't work... hrm 740 is the correct size though it would be larger if it wrapped (extra few `\n`).  I will make sure I'm not doing anything wrong on my end...

OOPS it was my bad I had my .ssh/config wrong so it wasn't using the user or keyfile args.

```
tony@tpad:~$ ssh risner-m1
spudz76@M1 ~ %                                                                                                                                                                    
```

Big win!  And thanks so much.

## Spudz76 | 2021-05-14T00:38:18+00:00
Ok there is no brew/cmake/anything and thus I need to be in Administrators (for sudo access) and also have a password that I know.  If you could set group, and then set password to `bad_password` I'll change it to something unknown to anyone immediately.  It doesn't appear you have Password Auth enabled with sshd anyway (good) so it will not matter.

Alternatively, install all the stuff! :)

## RS102839 | 2021-05-14T00:51:46+00:00
@Spudz76
I also tried running under sudo, without any benefit

## Spudz76 | 2021-05-14T00:52:19+00:00
@RS102839 OK sort of what I expected, it was only a slight hope :)

## Spudz76 | 2021-05-14T06:26:01+00:00
Found brew, wasn't in path

## xq0404 | 2021-05-14T07:35:43+00:00
> 
> 
> @Spudz76
> I also tried running under sudo, without any benefit

It had better be run under "su root"

## Spudz76 | 2021-05-14T09:17:44+00:00
Not really a success however I did discover the pagesize is always 16KB so it's already been sort-of using "slightly superpages"

Adjusted output to at least show as such.

```
M1:macos spudz76$ ./xmrig
allocating 2048 pages of 16384
kr:0 g_a:10359c000
 * ABOUT        XMRig/6.12.2-dev clang/12.0.5
 * LIBS         libuv/1.41.0 OpenSSL/1.1.1j hwloc/2.4.1
 * HUGE PAGES   supported (16KB)
 * 1GB PAGES    unavailable
 * CPU          Apple M1 (1) 64-bit AES
                L2:16.0 MB L3:0.0 MB 8C/8T NUMA:1
 * MEMORY       5.6/8.0 GB (71%)
 * DONATE       1%
 * POOL #1      donate.v2.xmrig.com:3333 algo auto
 * COMMANDS     hashrate, pause, resume, results, connection
[2021-05-14 05:13:16.004]  net      use pool donate.v2.xmrig.com:3333  178.128.242.134
[2021-05-14 05:13:16.005]  net      new job from donate.v2.xmrig.com:3333 diff 1000K algo rx/0 height 2360620
[2021-05-14 05:13:16.005]  cpu      use argon2 implementation default
[2021-05-14 05:13:16.005]  randomx  init dataset algo rx/0 (8 threads) seed f28a3022758579c6...
allocating 133120 pages of 16384
kr:0 g_a:280000000
allocating 16384 pages of 16384
kr:0 g_a:130000000
[2021-05-14 05:13:16.473]  randomx  allocated 2336 MB (2080+256) huge pages 100% 149504/149504 +JIT (468 ms)
[2021-05-14 05:13:21.181]  randomx  dataset ready (4708 ms)
[2021-05-14 05:13:21.181]  cpu      use profile  rx  (8 threads) scratchpad 2048 KB
allocating 128 pages of 16384
kr:0 g_a:103250000
[2021-05-14 05:13:21.181]  cpu      READY threads 8/8 (8) huge pages 100% 1024/1024 memory 16384 KB (1 ms)
|    CPU # | AFFINITY | 10s H/s | 60s H/s | 15m H/s |
|        0 |        0 |   300.7 |     n/a |     n/a |
|        1 |        1 |   301.4 |     n/a |     n/a |
|        2 |        2 |   298.9 |     n/a |     n/a |
|        3 |        3 |   298.5 |     n/a |     n/a |
|        4 |        4 |   298.7 |     n/a |     n/a |
|        5 |        5 |   298.6 |     n/a |     n/a |
|        6 |        6 |   298.6 |     n/a |     n/a |
|        7 |        7 |   298.7 |     n/a |     n/a |
|        - |        - |  2393.9 |     n/a |     n/a |
[2021-05-14 05:13:44.656]  miner    speed 10s/60s/15m 2393.9 n/a n/a H/s max 2401.8 H/s
[2021-05-14 05:13:46.185]  signal   Ctrl+C received, exiting
[2021-05-14 05:13:46.192]  cpu      stopped (4 ms)
```

Code is at [my xmrig fork branch dev-m1-superpages](https://github.com/Spudz76/xmrig/tree/dev-m1-superpages).

## RS102839 | 2021-05-14T16:34:53+00:00
@Spudz76

**currently I don't see any improvement in hash rates :-(**
`[2021-05-14 12:26:33.995]  randomx  init dataset algo rx/0 (8 threads) seed ffb9df6b3b1ad713...`
`allocating 133120 of 16384KB pages`
`kr:0 g_a:280000000`
`allocating 16384 of 16384KB pages`
`kr:0 g_a:130000000`
`[2021-05-14 12:26:34.477]  randomx  allocated 2336 MB (2080+256) huge pages 100% 149504/149504 +JIT (481 ms)`
[SKIP]
`[2021-05-14 12:27:39.850]  miner    speed 10s/60s/15m 2281.6 n/a n/a H/s max 2328.0 H/s`

_Note: this may just mean that the hashing bottleneck is elsewhere, so its still a worthwhile improvement._



## Spudz76 | 2021-05-14T22:46:51+00:00
Yes it is operating exactly as it always did internally, it just treats 16KB as "huge" pages now since anything over 4KB is technically larger than normal.  And M1 doesn't even let you do actual 4KB pages so it sort-of doesn't have normal-pages (might remove hugepages:false and force always-16 for now).

Also oops I put a `K` on the debug message without dividing by `1024` lol it was late and I was tired

Seems like for any other page size we must await Apple actually supporting it, like the other projects who all seem to be waiting for same.

## Spudz76 | 2021-05-14T22:55:05+00:00
If any of you have access to an older x64 mac with nvidia GPU that might still be running High Sierra, I've also fixed xmrig-cuda and xmrig so that it might work.  10.13 was the last officially supported OSX for CUDA support, and the last CUDA to support OSX was 10.2, but that should cover GTX9xx and GTX10xx just fine.  Older GTX7xx may need 9.2

I don't have any way to test it beyond that it compiled and the dylib loads and doesn't find a GPU (because it's on a VM lol)

Note brew fails to setup libuv so instead install autoconf and libtool and then use the `scripts/build_deps.sh` to make working libuv, libhwloc, and openssl for High Sierra.  The resulting `scripts/deps` folder is ready for pointing to with `-DXMRIG_DEPS=/location/of/scripts/deps`

It is all in the dev branches of the two projects, xmrig and the xmrig-cuda backend plugin.

## RS102839 | 2021-05-15T15:43:26+00:00
@Spudz76 
I was trying to dig into why the OpenCL build is failing on Mac M1.   Other similar projects seem to have found a way to make it work, though I take seriously the concern that the OpenCL code in XMRIG may never work on MacOS M1.

The whole situation is complicated by OpenCL never being part of my software expertise, so its a double learning curve of understanding a complex code-base using an unfamiliar development tool. 

## Spudz76 | 2021-05-15T20:00:24+00:00
@RS102839 Seems Apple has abandoned OpenCL so I never expect it to work again, especially on new hardware.  It likely still works on whichever OSX was the one before Metal when they still sort of wanted OpenCL to work.  Now they seem to be sabotaging it or at least ignoring it while it breaks due to other OS changes.  Some error messages say cl2metal failed which of course it did you can't emulate everything (looking at you, Rosetta).

Although, it might work if the OpenCL backend were forced to act generic (no AMD extensions even if it's an AMD, etc) so that Generic CL2Metal maybe does work.  But obviously going to be slow without the AMD proprietary calls.  This is how it "works" on Intel iGPUs.  nVidia OpenCL sometimes works but usually not.

## RS102839 | 2021-05-15T21:14:42+00:00
@Spudz76 
These are the error messages, which on the surface, do not generally appear to be serious.

`[2021-05-15 17:11:50.157]  opencl   GPU #0 compiling...
UNSUPPORTED (log once): buildComputeProgram: cl2Metal failed
[CL_DEVICE_NOT_AVAILABLE] : OpenCL Error : Error: Build Program driver returned (10014)
Break on OpenCLErrorBreak to debug.
OpenCL Warning : clBuildProgram failed: could not build program for 0x1027f00 (Apple M1) (err:-2)
Break on OpenCLWarningBreak to debug.
[CL_BUILD_ERROR] : OpenCL Build Error : Compiler build log:
Compilation failed: 

program_source:1736:1: warning: comparison of integers of different signs: 'uint32_t' (aka 'unsigned int') and 'int'
update_max(latency,(last_memory_op_slot+WORKERS_PER_HASH)/WORKERS_PER_HASH);
^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
program_source:1347:56: note: expanded from macro 'update_max'
#define update_max(value, next_value) do { if ((value) < (next_value)) (value) = (next_value); } while (0)
                                                ~~~~~  ^  ~~~~~~~~~~
program_source:1759:1: warning: comparison of integers of different signs: 'int32_t' (aka 'int') and 'unsigned int'
update_max(first_allowed_slot,latency*WORKERS_PER_HASH);
^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
program_source:1347:56: note: expanded from macro 'update_max'
#define update_max(value, next_value) do { if ((value) < (next_value)) (value) = (next_value); } while (0)
                                                ~~~~~  ^  ~~~~~~~~~~
program_source:1763:1: warning: comparison of integers of different signs: 'int32_t' (aka 'int') and 'unsigned int'
update_max(first_allowed_slot,get_byte(is_fp?registerReadCycleFP:registerReadCycle,dst)*WORKERS_PER_HASH);
^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
program_source:1347:56: note: expanded from macro 'update_max'
#define update_max(value, next_value) do { if ((value) < (next_value)) (value) = (next_value); } while (0)
                                                ~~~~~  ^  ~~~~~~~~~~
program_source:1765:1: warning: comparison of integers of different signs: 'int32_t' (aka 'int') and 'unsigned int'
update_max(first_allowed_slot,get_byte(registerReadCycle,src)*WORKERS_PER_HASH);
^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
program_source:1347:56: note: expanded from macro 'update_max'
#define update_max(value, next_value) do { if ((value) < (next_value)) (value) = (next_value); } while (0)
                                                ~~~~~  ^  ~~~~~~~~~~
program_source:1945:22: warning: comparison of integers of different signs: 'unsigned int' and 'int32_t' (aka 'int')
while ((i+num_workers<=last_used_slot)&&((i+num_workers) % WORKERS_PER_HASH)&&(execution_plan[i+num_workers]||(i+num_workers==first_instruction_slot)||((i+num_workers==first_instruction_slot+1)&&first_instruction_fp)))
        ~~~~~~~~~~~~~^ ~~~~~~~~~~~~~~
program_source:1945:125: warning: comparison of integers of different signs: 'unsigned int' and 'int32_t' (aka 'int')
while ((i+num_workers<=last_used_slot)&&((i+num_workers) % WORKERS_PER_HASH)&&(execution_plan[i+num_workers]||(i+num_workers==first_instruction_slot)||((i+num_workers==first_instruction_slot+1)&&first_instruction_fp)))
                                                                                                               ~~~~~~~~~~~~~^ ~~~~~~~~~~~~~~~~~~~~~~
program_source:1945:167: warning: comparison of integers of different signs: 'unsigned int' and 'int'
while ((i+num_workers<=last_used_slot)&&((i+num_workers) % WORKERS_PER_HASH)&&(execution_plan[i+num_workers]||(i+num_workers==first_instruction_slot)||((i+num_workers==first_instruction_slot+1)&&first_instruction_fp)))
                                                                                                                                                         ~~~~~~~~~~~~~^ ~~~~~~~~~~~~~~~~~~~~~~~~
program_source:2515:4: error: call to 'fma' is ambiguous
[2021-05-15 17:11:50.424]  opencl   error CL_BUILD_PROGRAM_FAILURE when calling clBuildProgram
BUILD LOG:
Compilation failed: 

program_source:1736:1: warning: comparison of integers of different signs: 'uint32_t' (aka 'unsigned int') and 'int'
update_max(latency,(last_memory_op_slot+WORKERS_PER_HASH)/WORKERS_PER_HASH);
^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
program_source:1347:56: note: expanded from macro 'update_max'
#define update_max(value, next_value) do { if ((value) < (next_value)) (value) = (next_value); } while (0)
                                                ~~~~~  ^  ~~~~~~~~~~
program_source:1759:1: warning: comparison of integers of different signs: 'int32_t' (aka 'int') and 'unsigned int'
update_max(first_allowed_slot,latency*WORKERS_PER_HASH);
^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
program_source:1347:56: note: expanded from macro 'update_max'
[2021-05-15 17:11:50.425]  opencl   thread #0 failed with error CL_INVALID_PROGRAM
`

Mostly `unsigned` vs `signed` issues, which should cast'able  by looking at the code.

BTW:  How does the code assemble `program_source`, since when I try to change the CL source code, `program_source` doesn't change?

## Spudz76 | 2021-05-15T22:47:19+00:00
Run `node scripts/generate_cl.js` to rebuild the combined code after changing things in the human-readable source code.  It sort of minifies it into the singular files that then become the kernel sources sent to the realtime compiler.

Also the warnings about types would normally just be ignored and you wouldn't see them.  Hunting for actual errors, it looks like the real reason for the crash is:
`program_source:2515:4: error: call to 'fma' is ambiguous`

It may help to begin with all extra algos disabled and see if some old simple CryptoNights will compile, first.  RandomX does a lot more "weird stuff" - and is of questionable use on GPU anyway.  If KawPow can work, that would be quite useful though.

## Spudz76 | 2021-05-15T23:23:44+00:00
There are only a few [fma()](https://www.khronos.org/registry/OpenCL/sdk/1.0/docs/man/xhtml/fma.html) calls and the CN one looks okay (uses floats).

The fma() calls from RX use doubles which might be what is not working, that requires fp64 extensions which I'm guessing might not be supported via CL2Metal (yet/ever).  But as I said it might not be that big a deal since RX doesn't "have to work" other than a proof of concept.

May have to both disable randomx during build, and also comment out the `rx()` call near the bottom of `generate_cl.js` so it completely leaves it out there too / otherwise it may still confuse the CL-compilation even though it would ultimately be uncalled.

## Spudz76 | 2021-05-15T23:40:15+00:00
CN/1 works, testing on @risner M1 shell.  Memory seems weird (1024MB max alloc?) and usual AMD environment vars don't seem to expand it.  Maybe different as root.  Anyway it gave me one thread and around 117H/s for cn/1...

## Spudz76 | 2021-05-15T23:50:34+00:00
Other CN flavors work also, it finally crashed trying to KawPow due to "it's an AMD" but "doesn't support any AMD stuff" because of the CL2Metal "firewall"...  checking to see if I can force a compatible mode without AMD extensions.
```
[2021-05-15 19:46:03.738]  opencl   use profile  kawpow  (1 thread) scratchpad 32 KB
|  # | GPU |  BUS ID | INTENSITY | WSIZE | MEMORY | NAME
|  0 |   0 |     n/a |   2097152 |   256 |   2664 | Apple M1
[2021-05-15 19:46:03.739]  opencl   GPU #0 compiling...
UNSUPPORTED (log once): buildComputeProgram: cl2Metal failed
[2021-05-15 19:46:03.874]  opencl   error CL_BUILD_PROGRAM_FAILURE when calling clBuildProgram
BUILD LOG:
Compilation failed: 

program_source:76:26: warning: unsupported OpenCL extension 'cl_amd_media_ops' - ignoring
#pragma OPENCL EXTENSION cl_amd_media_ops : enable
                         ^
program_source:81:8: warning: implicit declaration of function 'amd_bitalign' is invalid in OpenCL
return amd_bitalign((vv).xy,(vv).yx,32-r);
       ^
program_source:85:8: warning: implicit declaration of function 'amd_bitalign' is invalid in OpenCL
return amd_bitalign((vv).yx,(vv).xy,64-r);
       ^
Undefined symbol(s) for architecture 'air64':
  'amd_bitalign', referenced from:
error: symbol(s) not found for target 'air64-apple-macosx11.3.0'

[2021-05-15 19:46:03.876]  opencl   thread #0 failed with error CL_INVALID_PROGRAM
[2021-05-15 19:46:03.877]  opencl   thread #0 self-test failed
[2021-05-15 19:46:03.877]  opencl   disabled (failed to start threads)
```

## Spudz76 | 2021-05-16T00:05:55+00:00
All of the successful algos without any mods (other than disabling randomx and kawpow).  They all don't attempt to use anything more than 1024MB of VRAM therefore low intensities.  I turned them up 4x and it had no trouble but at least for cn/r it was slower.  GPU just not that powerful (8 cu's), or because it shares LPDDR4x system memory (not GDDR5 or 6).

AstroBWT and CN/Heavy threw a lot of compute errors during the benchmark.
```
    "algo-perf": {
        "cn/1": 116.0066348745594,
        "cn/2": 116.0066348745594,
        "cn/r": 116.0066348745594,
        "cn/fast": 232.0132697491188,
        "cn/half": 232.0132697491188,
        "cn/xao": 116.0066348745594,
        "cn/rto": 116.0066348745594,
        "cn/rwz": 154.67551316607919,
        "cn/zls": 154.67551316607919,
        "cn/double": 58.0033174372797,
        "cn-lite/1": 233.20199087515554,
        "cn-heavy/xhv": 133.6244541484716,
        "cn-pico": 1051.5938218862964,
        "cn-pico/tlo": 1051.5938218862964,
        "cn/ccx": 225.5984260574926,
        "cn/upx2": 4862.50650026001,
        "astrobwt": 8.11711842295985,
        "kawpow": 0.000345
    }
```

EDIT: added performance coefficient for ~1.51MH/s of KawPow after I fixed it

## Spudz76 | 2021-05-16T01:39:52+00:00
KawPow simply defaults to platform AMD I changed that default to UNKNOWN and it works
```
 * OPENCL       #0 Apple/OpenCL 1.2 (Feb 28 2021 03:51:21)
 * OPENCL GPU   #0 n/a Apple M1 1000 MHz cu:8 mem:1024/5461 MB
[2021-05-15 21:35:58.907]  net      use pool gulf.moneroocean.stream:20128 TLSv1.2 18.210.126.40
[2021-05-15 21:35:58.908]  net      fingerprint (SHA-256): "239daadd5c7d0ac097376c7871f787738826eef1c024729eff870e473b970855"
[2021-05-15 21:35:58.944]  net      use pool gulf.moneroocean.stream:20128 TLSv1.2 18.210.126.40
[2021-05-15 21:35:58.944]  net      fingerprint (SHA-256): "239daadd5c7d0ac097376c7871f787738826eef1c024729eff870e473b970855"
[2021-05-15 21:35:58.944]  net      new job from gulf.moneroocean.stream:20128 diff 89575K algo kawpow height 1755823
[2021-05-15 21:35:58.945]  opencl   use profile  kawpow  (1 thread) scratchpad 32 KB
|  # | GPU |  BUS ID | INTENSITY | WSIZE | MEMORY | NAME
|  0 |   0 |     n/a |   2097152 |   256 |   2941 | Apple M1
[2021-05-15 21:35:58.946]  opencl   GPU #0 compiling...
[2021-05-15 21:35:58.949]  opencl   GPU #0 compilation completed (3 ms)
[2021-05-15 21:35:58.950]  opencl   READY threads 1/1 (6 ms)
[2021-05-15 21:35:58.956]  opencl   KawPow program for period 585274 compiled (5ms)
[2021-05-15 21:35:58.961]  opencl   KawPow program for period 585275 compiled (6ms)
[2021-05-15 21:36:00.521]  net      new job from gulf.moneroocean.stream:20128 diff 89575K algo kawpow height 1755824
[2021-05-15 21:36:02.884]  miner    KawPow light cache for epoch 234 calculated (3928ms)
[2021-05-15 21:36:48.955]  opencl   KawPow DAG for epoch 234 calculated (46065ms)
[2021-05-15 21:37:03.691]  net      new job from gulf.moneroocean.stream:20128 diff 89575K algo kawpow height 1755825
[2021-05-15 21:37:04.361]  miner    speed 10s/60s/15m n/a n/a n/a H/s max n/a H/s
[2021-05-15 21:37:05.453]  opencl   KawPow program for period 585276 compiled (1092ms)
| OPENCL # | AFFINITY | 10s MH/s | 60s MH/s | 15m MH/s |
|        0 |       -1 |     1.51 |      n/a |      n/a | #0 n/a Apple M1
|        - |        - |     1.51 |      n/a |      n/a |
[2021-05-15 21:37:19.181]  miner    speed 10s/60s/15m 1.51 n/a n/a MH/s max 1.51 MH/s
```

## Spudz76 | 2021-05-16T02:00:47+00:00
PR #2379 will make oddball OpenCL work with KawPow (while leaving actual AMD OpenCL working the same)

## RS102839 | 2021-05-16T02:06:14+00:00
Using cn/heavy and OpenCL, we get an error, but it is definitely running in the GPU:

`[2021-05-15 22:00:53.767]  config   "../config.xhv.json" was changed, reloading configuration`
`[CL_INVALID_OPERATION] : OpenCL Error : Failed to retrieve device information! Invalid enumerated value!`

`Break on OpenCLErrorBreak to debug.`
`[2021-05-15 22:00:53.863]  cpu      stopped (96 ms)`
`[2021-05-15 22:00:53.863]  opencl   use profile  cn-heavy  (1 thread) scratchpad 4096 KB`
`|  # | GPU |  BUS ID | INTENSITY | WSIZE | MEMORY | NAME`
`|  0 |   0 |     n/a |       192 |     8 |    768 | Apple M1`
`[2021-05-15 22:00:53.873]  opencl   READY threads 1/1 (9 ms)`
`[2021-05-15 22:01:02.700]  opencl   accepted (16/0) diff 4650 (136 ms)`
`[2021-05-15 22:01:11.215]  opencl   accepted (17/0) diff 4650 (135 ms)`
`[2021-05-15 22:01:19.792]  opencl   accepted (18/0) diff 4650 (182 ms)`
`[2021-05-15 22:01:28.200]  net      new job from [REDACTED] diff 4860 algo cn-heavy/xhv height 855811`
`[2021-05-15 22:01:42.834]  net      new job from [REDACTED] diff 4860 algo cn-heavy/xhv height 855812`
`[2021-05-15 22:01:43.058]  miner    speed 10s/60s/15m 135.1 n/a n/a H/s max 135.4 H/s`


More:  Raising Intensity to 384 seems to give optimum throughput, but still only 140.  Going higher doesn't help.
`[2021-05-15 22:26:25.111]  miner    speed 10s/60s/15m 139.4 139.2 n/a H/s max 140.0 H/s`

## Spudz76 | 2021-05-16T03:08:30+00:00
Have to remember the whole thing is super low watts, too.

That's worth ~1992.56H/s XMR-value on MO right now and for the watts I guess that's not nothing.

Based on my 107.5H/s GTX550Ti and what it is currently showing as scoring 1.53KH/s.  Likely more watts than the entire M1 Mac draws, lol.

## AndyRPH | 2021-05-16T03:10:04+00:00
So, running the MO fork once this makes it way in nearly doubles the M1's output in XMR? 

## Spudz76 | 2021-05-16T03:13:09+00:00
MO makes a lot more on anything, than mining actual rx/0 almost ever does.  The last few posts were about OpenCL on the M1's GPU and cn-heavy/xhv (Haven).

But if you mean 2400H/s for the CPU on rx/0 is double your current output (1200H/s??) then, sure.

Also the MO fork compiles fine there just isn't a binary release for it due to github actions don't support M1 (yet).  And CN-GPU seems angry for the moment until I figure out why, but it probably isn't very useful on the M1 CPU (no other CPU does well with it).

## Spudz76 | 2021-05-16T03:31:01+00:00
Here are the current M1 CPU performance ratings for all the MO algos (minus cn/gpu as mentioned already)
```
    "algo-perf": {
        "cn/1": 15.85288522511097,
        "cn/2": 15.85288522511097,
        "cn/r": 15.85288522511097,
        "cn/fast": 31.70577045022194,
        "cn/half": 31.70577045022194,
        "cn/xao": 15.85288522511097,
        "cn/rto": 15.85288522511097,
        "cn/rwz": 21.13718030014796,
        "cn/zls": 21.13718030014796,
        "cn/double": 7.926442612555485,
        "cn-lite/1": 145.3529000698812,
        "cn-heavy/xhv": 24.17606244579358,
        "cn-pico": 689.2092431630273,
        "cn-pico/tlo": 689.2092431630273,
        "cn/ccx": 98.75509990584789,
        "cn/upx2": 2066.4875087090674,
        "cn/gpu": 184.7,
        "rx/0": 254.92537313432838,
        "rx/wow": 375.3987240829346,
        "rx/arq": 1415.0268336314849,
        "rx/sfx": 254.92537313432838,
        "argon2/chukwav2": 432.4702589223233,
        "astrobwt": 121.8905472636816,
        "panthera": 443.6179708420113
    }
```

EDIT: Fixed cn/gpu, performance updated (184.7H/s)

## AndyRPH | 2021-05-16T03:34:52+00:00
> MO makes a lot more on anything, than mining actual rx/0 almost ever does. The last few posts were about OpenCL on the M1's GPU and cn-heavy/xhv (Haven).
> 
> But if you mean 2400H/s for the CPU on rx/0 is double your current output (1200H/s??) then, sure.
> 
> Also the MO fork compiles fine there just isn't a binary release for it due to github actions don't support M1 (yet). And CN-GPU seems angry for the moment until I figure out why, but it probably isn't very useful on the M1 CPU (no other CPU does well with it).

No I meant that this would mean GPU mining on the M1 on top of existing CPU mining via MO could almost double the xmr MO gives me on my M1 running CPU only coins, I think?

## Spudz76 | 2021-05-16T03:54:43+00:00
Well currently the CPU is offering rx/wow which at 380H/s is at ~380H/s equivalence.

And then the GPU currently selects KawPow as most valuable at 1.51MH/s, but none of my devices are running that so I don't know the current MO exchange rate to make an equivalence.  But if that ends up being around 380H/s equivalence then yeah it would double your rates.

EDIT: Just fixed cn/gpu and it does 184.7H/s and is then selected to mine by MO.  Again don't have anything running cn/gpu to find the current ratio to XMR equivalence.  But it must be even more valuable at then moment than KawPow.

## risner | 2021-05-16T13:10:05+00:00
Thanks so much Spudz76.

This raises a couple questions:
1) It sounds the M1 may be better suited to other algorithms than rx/0? How do I generate the algo-perf values and add them to config.json? There doesn't seem to be anything I could find in searches.

2) If I use the GPU code, do I need to run two instances? One for GPU and one for CPU? Or can xmrig manage both concurrently?

## risner | 2021-05-16T13:52:46+00:00
Tried the xmrig-dev version of your opencl code and got an error:
[2021-05-16 09:22:59.490]  opencl   GPU #0 compiling...
UNSUPPORTED (log once): buildComputeProgram: cl2Metal failed
[2021-05-16 09:22:59.758]  opencl   error CL_BUILD_PROGRAM_FAILURE when calling clBuildProgram
BUILD LOG:
Compilation failed:

program_source:1736:1: warning: comparison of integers of different signs: 'uint32_t' (aka 'unsigned int') and 'int'

So I attempted to fix by adding some cast's in the maco, but couldn't generate:
risner@M1 scripts % node generate_cl.js
node:internal/bootstrap/switches/does_own_process_state:112
  rawMethods.chdir(directory);
Error: ENOENT: no such file or directory, chdir '/Users/risner/src/xmrig/xmrig-dev-v6.12.2-May-16/scripts' -> '/Users/risner/src/xmrig/xmrig-dev-v6.12.2-May-16/scripts/src/backend/opencl/cl/cn'

There is no cl or cl/cn in my opencl backend directory?

## RS102839 | 2021-05-16T14:14:04+00:00
@risner

Note: I had to get a current version of nodejs, but it sounds like you already did that

Don't run it from the scripts directory, go up a level and it should work:  `node scripts/generate_cl.js`
**I also found I have to first manually delete the target file.**

However, I haven't fixed all the casts on my version (missed two) :-(
But I did fix the fma warning with a cast, so @Spudz76 concern about fma might be unfounded.
....in same file as the other casts, line 1410:  `return (double)fma((double)a, (double)b, (double)c);`

I switched to testing the CN-based mining, which does mainly run in the GPU.  I'm able to run two copies of XMRIG on the Mac Mini M1, one CPU mining with `rx/0` at about 1790 H/s and one (mainly) GPU mining with `cn/heavy` at 140 H/s.  Just for a test, since I haven't bothered to figure out if taking a 24% reduction in `rx/0` mining is worth being able to concurrently mine `cn/heavy`.

_Update:   None of this mining makes economic sense, so IMHO it is just a hobby
But taking current mining revenues on XMR vs Haven, it is worthwhile to run two XMRIG instances in this configuration_
- 2400 H/s just on XMR earns around US$1.75 per week
- 1800 H/s on XMR = $1.33, and 140 H/s on Haven = $1.77 for total of $3.10 per week

## risner | 2021-05-16T14:31:10+00:00
@RS102839 Well, I'm using node v16.1.0. Thanks, that got the node command to work. However it is still ignoring my cast's in src/backend/opencl/cl/rx/randomx_vm.cl source. I guess I don't know how to modify the macro src/backend/opencl/cl/rx/randomx_vm.cl to be "put" into the binary.

What file did you change to fix the fma warning?


## RS102839 | 2021-05-16T18:57:12+00:00
@Spudz76 

Having fixed all the cast issues, now get the following error with `rx\0` and OpenCL:

`[CL_INVALID_OPERATION] : OpenCL Error : Failed to retrieve device information! Invalid enumerated value!`

`Break on OpenCLErrorBreak to debug.`
`[2021-05-16 14:40:51.211]  opencl   stopped (0 ms)`
`[2021-05-16 14:40:51.211]  opencl   use profile  rx  (1 thread) scratchpad 2048 KB`
`|  # | GPU |  BUS ID | INTENSITY | WSIZE | MEMORY | NAME`
`|  0 |   0 |     n/a |      1984 |     8 |   3968 | Apple M1`
`[2021-05-16 14:40:51.212]  opencl   GPU #0 compiling...`
`[2021-05-16 14:40:51.215]  opencl   GPU #0 compilation completed (3 ms)`
`[CL_INVALID_KERNEL] : OpenCL Error : Failed to create kernel! Could not create kernel for one or more devices.`
`Break on OpenCLErrorBreak to debug.`
`[2021-05-16 14:40:51.223]  opencl   error CL_INVALID_KERNEL when calling clCreateKernel for kernel execute_vm`
`[2021-05-16 14:40:51.223]  opencl   thread #0 failed with error CL_INVALID_KERNEL`
`[2021-05-16 14:40:51.223]  opencl   thread #0 self-test failed`
`[2021-05-16 14:40:51.223]  opencl   disabled (failed to start threads)`

However, noting your advice that `rx/0` is not ideal for running in the GPU....



## RS102839 | 2021-05-16T19:03:28+00:00
@Spudz76  @risner This resolves the casting issues:

`diff --git a/src/backend/opencl/cl/rx/randomx_vm.cl b/src/backend/opencl/cl/rx/randomx_vm.cl`
`index 58aa265b..ef70dab8 100644`
`--- a/src/backend/opencl/cl/rx/randomx_vm.cl`
`+++ b/src/backend/opencl/cl/rx/randomx_vm.cl`
`@@ -626,7 +626,7 @@ __kernel void init_vm(__global const void* entropy_data, __global void* vm_state`
`                                if (opcode < RANDOMX_FREQ_ISTORE)`
 `                               {`
`                                        latency = reg_read_latency;`
`-                                       update_max(latency, (last_memory_op_slot + WORKERS_PER_HASH) / WORKERS_PER_HASH);`
`+                                       update_max(latency, (uint32_t)((last_memory_op_slot + WORKERS_PER_HASH) / WORKERS_PER_HASH));`
`                                        is_memory_op = true;`
`                                        is_memory_store = true;`
`                                        break;`
`@@ -654,14 +654,14 @@ __kernel void init_vm(__global const void* entropy_data, __global void* vm_state
                        }`
 
`                        int32_t first_allowed_slot = first_available_slot;`
`-                       update_max(first_allowed_slot, latency * WORKERS_PER_HASH);`
`+                       update_max(first_allowed_slot, (int32_t)(latency * WORKERS_PER_HASH));`
`                        if (is_cfround)`
`                                update_max(first_allowed_slot, first_allowed_slot_cfround);`
`                        else`
`-                               update_max(first_allowed_slot, get_byte(is_fp ? registerReadCycleFP : registerReadCycle, dst) * WORKERS_PER_HASH);`
`+                               update_max(first_allowed_slot, (int32_t)(get_byte(is_fp ? registerReadCycleFP : registerReadCycle, dst) * WORKERS_PER_HASH));`
 
`                        if (is_swap)`
`-                               update_max(first_allowed_slot, get_byte(registerReadCycle, src) * WORKERS_PER_HASH);`
`+                               update_max(first_allowed_slot, (int32_t)(get_byte(registerReadCycle, src) * WORKERS_PER_HASH));`
 
`                        int32_t slot_to_use = last_used_slot + 1;`
`                        update_max(slot_to_use, first_allowed_slot);`
`@@ -934,7 +934,7 @@ __kernel void init_vm(__global const void* entropy_data, __global void* vm_state`
 
`                        uint32_t num_workers = 1;`
`                        uint32_t num_fp_insts = 0;`
`-                       while ((i + num_workers <= last_used_slot) && ((i + num_workers) % WORKERS_PER_HASH) && (execution_plan[i + num_workers] || (i + num_workers == first_instruction_slot) || ((i + num_workers == first_instruction_slot + 1) && first_instruction_fp)))`
`+                       while ((i + num_workers <= last_used_slot) && ((i + num_workers) % WORKERS_PER_HASH) && (execution_plan[i + num_workers] || (i + (int32_t)num_workers == first_instruction_slot) || ((i + (int32_t)num_workers == first_instruction_slot + 1) && first_instruction_fp)))`
`                        {`
`                                if ((num_workers & 1) && ((src_program[execution_plan[i + num_workers]].x & (0x20 << 8)) != 0))`
`                                        ++num_fp_insts;`
`@@ -1407,7 +1407,7 @@ double load_F_E_groups(int value, uint64_t andMask, uint64_t orMask)`
` double fma_soft(double a, double b, double c, uint32_t rounding_mode)`
` {`
`        if (rounding_mode == 0)`
`-               return fma(a, b, c);`
`+               return (double)fma((double)a, (double)b, (double)c);`
 
`        if ((a == 0.0) || (b == 0.0))`
`                return c;`
`@@ -1629,8 +1629,8 @@ double sqrt_rnd(double x, uint32_t fprc)`
 
`        // First Newton-Raphson iteration`
`        double t0 = y0 * x;`
`-       double t1 = y0 * -0.5;`
`-       t1 = fma(t1, t0, 0.5);                                  // 0.5 * (1.0 - y0 * y0 * x)`
`+       double t1 = y0 * (double)-0.5;`
`+       t1 = fma(t1, t0, (double)0.5);                                  // 0.5 * (1.0 - y0 * y0 * x)`
`        const double y1_x = fma(t0, t1, t0);    // y1 * x = 0.5 * y0 * x * (3.0 - y0 * y0 * x)`
 
`        // Second Newton-Raphson iteration`

## Spudz76 | 2021-05-17T08:50:44+00:00
@risner algo-perf is a feature added by the MoneroOcean fork of this project, compiling this codebase does not have it.  I use it as a nice and easy way to test every algo and share results :)

But if you check out theirs the master matches the master here and patches should for the most part still apply clean.

Or you can base on top of [my branch dev-mo](https://github.com/Spudz76/xmrig/tree/dev-mo) which is the same as [MoneroOcean/xmrig@master](https://github.com/MoneroOcean/xmrig) but applied to the dev branch, and then any patches based on xmrig/xmrig@dev will apply cleanly if they didn't on master.

My [branch dev-moCleanup](https://github.com/Spudz76/xmrig/tree/dev-moCleanup) has dev-mo plus some proposed patches (or sloppy hacks) I use in my own builds.

---

For part 2 depends if you will run on a switching pool like MO or a regular single algo pool.  If switching then yes separate xmrig copies in different folders one set for cpu-only and the other for opencl-only.  Usually this works very well on completely separate GPUs, but M1 is sharing the LPDDR4x memory between CPU and GPU so I think that is why the CPU loses 600H/s while GPU is also mining.  It is still much better than any Intel iGPU performance (especially while both are mining) and the watts and heat are insanely low for the speed although numerically low the hash/watt ratio is really amazing.

## rovo79 | 2021-05-26T14:59:12+00:00
@Spudz76 it would be amazing if there was some way for the CPU and GPU to work together instead of competing for the same pool of memory. 

> there’s no need to carve out portions of memory for each part of the SoC and then shuttle data between the two spaces for different parts of the processor. Instead, the GPU, CPU, and other parts of the processor can access the same data at the same memory address.

src: https://www.howtogeek.com/701804/how-unified-memory-speeds-up-apples-m1-arm-macs/

## rovo79 | 2021-05-26T15:14:46+00:00
Recent release of RandomX might resolve some limitations of M1 handling of JIT?

in https://github.com/tevador/RandomX/releases/tag/v1.1.9

## Spudz76 | 2021-05-26T15:22:06+00:00
@rovo79 Very interesting!  Though, no, the Secure-JIT is not something that can be resolved, it's locked, and will always be slower than "insecure" JIT.  But all those other changes are probably quite helpful.

## risner | 2021-05-26T15:24:59+00:00
@Spudz76 If you wish to use the M1 shell to test those changes for xmrig, feel free.

## Spudz76 | 2021-05-26T15:25:11+00:00
@rovo79 On the other thing, the issue is there are only so many "lanes" on the highway from CPU+GPU to the memory.  So the traffic jams are more of an issue than having the positive aspects of shared memory as that snippet says, or even having the memory ultra-local on the chip like HBM.  Still only a certain width on the highway to get there.

## Spudz76 | 2021-05-26T15:27:26+00:00
@risner thanks again, I have dropped in now and then to test other minor changes.  I am not sure if I know the RandomX integration quite deeply enough but @SChernykh might appreciate a shell and would be more efficient at merging the updates properly

## risner | 2021-08-10T23:24:09+00:00
@SChernykh if you need Apple M1 access to look at some improvements @Spudz76 is referring feel free to ping me on discord. My discord is in my profile.

## risner | 2021-11-01T13:36:54+00:00
@Spudz76 Have most of these changes been mainlined to xmrig? The current version still says huge pages unavailable:
 * ABOUT        XMRig/6.15.2-mo3 clang/12.0.5
 * HUGE PAGES   unavailable
 
 But based on your comments, it didn't seem like that is anything that should effect performance (It always does 16k?)
 
 The M1 Max seems to do well.
 
CPU:
     "algo-perf": {
        "cn/0": 710.847900390625,
        "cn/1": 221.3616485595703,
        "cn/2": 221.3616485595703,
        "cn/r": 221.3616485595703,
        "cn/fast": 442.7232971191406,
        "cn/half": 442.7232971191406,
        "cn/xao": 221.3616485595703,
        "cn/rto": 221.3616485595703,
        "cn/rwz": 295.14886474609375,
        "cn/zls": 295.14886474609375,
        "cn/double": 110.68082427978516,
        "cn/ccx": 1421.69580078125,
        "cn-lite/0": 1629.2108154296875,
        "cn-lite/1": 1629.2108154296875,
        "cn-heavy/xhv": 415.5580749511719,
        "cn-pico": 5990.42724609375,
        "cn-pico/tlo": 5990.42724609375,
        "cn/gpu": 47.19093704223633,
        "panthera": 5274.5263671875,
        "rx/0": 3381.978759765625,
        "rx/arq": 15226.9091796875,
        "rx/graft": 3269.983154296875,
        "rx/sfx": 3381.978759765625,
        "argon2/chukwav2": 5516.86328125,
        "astrobwt": 1468.7960205078125
        }
GPU. I disable all the ones that gave compute errors. Should I leave them enabled?
    "algo-perf": {
        "cn/0": 255.54760200429493,
        "cn/1": 212.58134490238612,
        "cn/2": 212.58134490238612,
        "cn/r": 212.58134490238612,
        "cn/fast": 425.16268980477224,
        "cn/half": 425.16268980477224,
        "cn/xao": 212.58134490238612,
        "cn/rto": 212.58134490238612,
        "cn/rwz": 283.4417932031815,
        "cn/zls": 283.4417932031815,
        "cn/double": 106.29067245119306,
        "cn/ccx": 511.09520400858986,
        "cn-lite/0": 493.5897435897436,
        "cn-lite/1": 493.5897435897436,
        "cn-heavy/xhv": 283.0769230769231,
        "cn-pico": 2464.48087431694,
        "cn-pico/tlo": 2464.48087431694
        }

## xq0404 | 2021-11-02T00:53:59+00:00
Not much improvement for this latest chip upgrade 
https://xmrig.com/benchmark
                          HASHRATE   
Apple M1 Max    3491.27
Apple M1 Pro     3470.23
Apple M1           2390.73

## nissaba | 2021-11-02T18:21:19+00:00
has any one tough about porting the code to a real Xcode project and use the Metal API ? I am working on a app that does a lot of computation for calculating live air-drag coefficient and running the same calculation using the Metal API massively improved performance. 

## AndyRPH | 2021-11-02T18:37:23+00:00
That's probably the only way to leverage the substantial power of the rest of the chip, however it doesn't seem anyone has had the interest to make a crypto miner using Metal APIs.  It would probably lend itself more towards GPU mining coins than CPU mined coins that use RandomX. 

Someone's bound to do it someday. 

## Spudz76 | 2021-11-02T22:40:12+00:00
I looked at Metal and it could be possible, but from what I saw the mining workload may not be any faster than OpenCL.

Would be fun to find out, but a huge waste of time if it turns out to be slower.  Then again OpenCL will be removed completely from MacOS sometime (like CUDA was).

Also homebrew already uses Xcode so I'm not sure how a "native" project would be any different.

## AndyRPH | 2021-11-03T00:49:11+00:00
I didn't think OpenCL was optimized much at all on the M1 Macs, so a rewrite using Metal APIs would probably benefit. 

## risner | 2021-11-03T01:31:58+00:00
How hard would it be to rewrite the opencl for cn-heavy/xhv to metal? Is it something I could do if someone showed me where the opencl is and explained what it does?

## Spudz76 | 2021-11-03T02:48:37+00:00
I found some more generic OpenCL-to-Metal in [this thread](https://developer.apple.com/forums/thread/662809) which was also mostly where I came up with "it might not always be faster".  Depends on workload and how it can be subdivided... which might then require a rework of how the algorithm kernel is designed -- the idea of threads/blocks and how they interrelate in the compiler / GPU shader population for max throughput for that workload, how the loops are set up so the compiler can optimize them, whether or not there is an option to embed "assembly" or more specific tricks the compiler might never think of (how AMD-OpenCL gets its boosts, over vanilla Apple-OpenCL on an AMD card).

What I saw in some other places (which might be out-of-date?) is that Metal does not support double-precision floats which is probably a major problem for most algorithms.  There are also specific rounding-modes for floats that are required for some algorithms, which is why some don't work on older GPUs that didn't have the right float-handling formats and modes (CN-GPU).

## Spudz76 | 2021-11-03T02:51:41+00:00
Somewhat well summarized by a section of a post from that thread:
> I only do compute with Metal, coming from OpenCL. I have found precision on float is identical to OpenCL (and equivalent to CPU float code), but you have to watch how you compile/write if you need highly precise float code. If you need double, you are indeed out of luck.

## rovo79 | 2021-11-05T10:27:36+00:00
I have very limited understanding of any of this, but my mind gravitates towards figuring out how to utilize the Accelerate framework more so than the Metal for possibly optimizing an M1 for these kinds of tasks. 

Accelerate: Make large-scale mathematical computations and image calculations, optimized for high performance and low energy consumption.
https://developer.apple.com/documentation/accelerate

Some interesting reading

The Secret Apple M1 Coprocessor
(BTW, this is how you access articles behind paywalls):
http://webcache.googleusercontent.com/search?q=cache:uJQwCGrE5ksJ:https://medium.com/swlh/apples-m1-secret-coprocessor-6599492fc1e1&client=safari&hl=en&gl=us&strip=1&vwsrc=0

Apple’s M1 processor and the full 128-bit integer product
https://lemire.me/blog/2021/03/17/apples-m1-processor-and-the-full-128-bit-integer-product/

Accelerate Framework:
https://developer.apple.com/documentation/accelerate


Just random interest
Core ML featureValueWithDouble:
https://developer.apple.com/documentation/coreml/mlfeaturevalue/2879398-featurevaluewithdouble?changes=latest____9&language=objc

https://gist.github.com/dougallj/7a75a3be1ec69ca550e7c36dc75e0d6f

Comparing Apple’s M1 matmul performance – AMX2 vs NEON
https://nod.ai/comparing-apple-m1-with-amx2-m1-with-neon/

Any kind of miner that fully utilizes Apple M1 would have to be so completely re architected, not just code ported to make it function; that is just limping along. 

## AndyRPH | 2021-11-05T11:29:31+00:00
Exactly.  It could be a stellar crypto mining machine, but it would need miner software rewritten quite a bit, and I don't suspect the pool of people with the desire and talent to do that  overlaps much with the average owner of new apple computers. 

## rovo79 | 2021-11-05T14:55:51+00:00
I think we are chasing our tail if we hope to ever see a performant miner for Apple M series by just porting over existing projects. 

This may be misguided, but if interested, I think this effort would be better spent towards a new initiative. I've started a new project repo here: 
[**SiliconMiner**](https://github.com/rovo79/SiliconMiner)
https://github.com/rovo79/SiliconMiner

Please join in, contribute in anyway if interested!


## Spudz76 | 2021-11-05T15:21:37+00:00
The miner kernels in xmrig are fairly modular and the network/stratum/main-loop stuff is probably not worth reinventing.  Should be ways to compile a library of Apple Accelerate/CoreML kernels per algorithm and hook them from normal C++?

A little bit like how xmrig-cuda works as a backend plugin.

## risner | 2021-11-05T17:22:26+00:00
I’d concur, it should be able to add separate algorithms.

this sounds like we’d need assistance from someone more adept at apple code to assist someone adept at xmrig.

## risner | 2021-11-05T19:57:35+00:00
Found this shim:
https://github.com/kakashidinho/metalangle

## RS102839 | 2021-11-05T21:57:06+00:00
> Found this shim: https://github.com/kakashidinho/metalangle

This shim is interesting, but only provided a small increase in performance (based on their own stats).  However, that itself is interesting, since the opposite is often true.

On a quick skim through it, I can't determine whether you could use this to export OpenGLES code to Metal code, which could then be hand-optimized.  Presumably the 80-20 rule applies and therefore most of the exported code is "good enough", and only some would benefit from optimization and that's where most of the performance gains would come from.

## xq0404 | 2021-11-06T01:00:07+00:00
> 
> 
> I think we are chasing our tail if we hope to ever see a performant miner for Apple M series by just porting over existing projects.
> 
> This may be misguided, but if interested, I think this effort would be better spent towards a new initiative. I've started a new project repo here: [**SiliconMiner**](https://github.com/rovo79/SiliconMiner) https://github.com/rovo79/SiliconMiner
> 
> Please join in, contribute in anyway if interested!

A step in the right direction. Congrats!

## Spudz76 | 2021-11-06T03:33:55+00:00
Already in use is the [sse2neon shim](https://raw.githubusercontent.com/DLTcollab/sse2neon/master/sse2neon.h) which is also out of date in the tree.  Perhaps some of the new/added polyfills make it faster as-is.

But also a similar polyfill might work for other non-ARM-Apple-Extensions.  But I agree with the general skepticism of shims being fast enough compared to straight custom.  But the 80/20 probably applies.  That's how the x86-64 kernels got good, spot optimization where the most gains are.  The Accelerator.framework seems to want generic code it can recognize and upgrade, any obfuscation probably makes it take the wrong assumptions.  So then shims to Accelerator probably wouldn't work right the loops are already designed for x86-like intrinsics...

## CarlosOrozco88 | 2021-11-21T07:53:16+00:00
Hi! I just bought an M1 Pro with 16gb ram i tested it. I scores 3.5KHs (https://xmrig.com/benchmark/78JS4w). 
Is there a way to test it in a ubuntu arm vm to check with hugepages?

## xq0404 | 2021-11-21T08:55:24+00:00
> Hi! I just bought an M1 Pro with 16gb ram i tested it. I scores 3.5KHs (https://xmrig.com/benchmark/78JS4w). Is there a way to test it in a ubuntu arm vm to check with hugepages?

Perhaps you could try a Linux version.
https://github.com/xmrig/xmrig/releases

## CarlosOrozco88 | 2021-11-21T09:38:15+00:00
> > Hi! I just bought an M1 Pro with 16gb ram i tested it. I scores 3.5KHs (https://xmrig.com/benchmark/78JS4w). Is there a way to test it in a ubuntu arm vm to check with hugepages?
> 
> Perhaps you could try a Linux version.
> https://github.com/xmrig/xmrig/releases

I am testing with ubuntu arm (using a virtual machine in utm) and building xmrig (https://xmrig.com/docs/miner/build/ubuntu). Without hugepages scores 1.9KHs and with hugepages 2.5KHs. If i can i will do some tests using parallels or multipass...

## risner | 2021-11-21T10:16:27+00:00
> > > Hi! I just bought an M1 Pro with 16gb ram i tested it. I scores 3.5KHs (https://xmrig.com/benchmark/78JS4w). Is there a way to test it in a ubuntu arm vm to check with hugepages?
> > 
> > 
> > Perhaps you could try a Linux version.
> > https://github.com/xmrig/xmrig/releases
> 
> I am testing with ubuntu arm (using a virtual machine in utm) and building xmrig (https://xmrig.com/docs/miner/build/ubuntu). Without hugepages scores 1.9KHs and with hugepages 2.5KHs. If i can i will do some tests using parallels or multipass...

If memory serves the original M1 runs at 2,400 on MacOS and 2,000 on native (No vm) Ubuntu with huge pages.

## Spudz76 | 2021-11-21T10:50:54+00:00
I doubt the VM Ubuntu does anything but pretend to do hugepages while it still uses the 16KB pages.

There is a baremetal way to boot a Linux kernel and use a Raspbian64 rootfs but it is unclear if that supports anything but 16KB either and it hasn't been updated in ~9 months.

## AndyRPH | 2021-11-23T03:37:26+00:00
Do any of the various coins that xmrig can mine make use of AMX? Apparently apple's M1 chips have an undocumented feature for it:  https://gist.github.com/dougallj/7a75a3be1ec69ca550e7c36dc75e0d6f. (from reading performance notes posted https://tlkh.dev/benchmarking-the-apple-m1-max) 

## rovo79 | 2021-11-23T10:32:05+00:00
> Do any of the various coins that xmrig can mine make use of AMX? Apparently apple's M1 chips have an undocumented feature for it: https://gist.github.com/dougallj/7a75a3be1ec69ca550e7c36dc75e0d6f. (from reading performance notes posted https://tlkh.dev/benchmarking-the-apple-m1-max)

That is some great reverse engineering

## Spudz76 | 2021-11-23T10:34:12+00:00
Most relevant algos use FP64 so everything about how rippin' fast it is for machine-learning (with lesser floats, not doubles) are pretty pointless.  Also saw reference that it does not do speculative or out-of-order execution which might destroy its usage in RandomX in particular (it's sort of designed like a GPU, thus the anti-GPU features of RandomX are tickled, so you lose more than you'd have gained by the faster calculation, probably).

Might help for some other algos.  Might also be a whole lot of work to find out it's slower.

## ink-splatters | 2022-01-12T11:45:52+00:00
@AndyRPH 

almost average M1 owner here to spoil your perfect sample of average Mac owners a bit:)

The true problem I see for myself: quite a learning curve which is constrained by spare time.

E.g. I've close to zero experience with aarch64 yet, unfortunately, but pretty much enthusiastic about digging into it.
This awesome piece of hardware is a main thing keeping me with Apple, as macOS ~ 1 / privacy (unless ripping out most of the `launchd` default stuff)

for those uninitiated like me, I recommend reading [Daniel Lemire's blog](https://lemire.me/blog/), it has triggered my big interest to M1 platform :)

He is one of `simdjson` authors (the lib benchmarks are ranging many gigabytes per sec of json data processed, so average SSD storage / networking does not seem to be capable to load the parser properly to avoid its starvation :)

Above all, there are several Lemire's posts regarding Apple M1 architecture / differences with x86_64 (but the focus is still mostly on vector operations, as this A12-related [post](https://lemire.me/blog/2019/07/10/parsing-json-using-simd-instructions-on-the-apple-a12-processor).

Sorry for the certainly an off-topic but I witnessed this awesomeness :)
>
>

```
simdjson/build/benchmark on  master [?] took 39s 
❯ maccina
                                                                               
                  ,MMMM.           Host        -  r2d2@MacBook-Air.local       
                .MMMMMM            Machine     -  MacBookAir10,1               
                MMMMM,             Kernel      -  21.2.0                       
      .;MMMMM:' MMMMMMMMMM;.       OS          -  macOS 12.1.0 Monterey        
    MMMMMMMMMMMMNWMMMMMMMMMMM:     DE          -  Aqua                         
  .MMMMMMMMMMMMMMMMMMMMMMMMWM.     WM          -  Quartz Compositor            
  MMMMMMMMMMMMMMMMMMMMMMMMM.       Packages    -  249 (Homebrew), 23 (cargo)   
 ;MMMMMMMMMMMMMMMMMMMMMMMM:        Terminal    -  xterm-256color               
 :MMMMMMMMMMMMMMMMMMMMMMMM:        Shell       -  fish                         
 .MMMMMMMMMMMMMMMMMMMMMMMMM.       Uptime      -  1d 19h 39m                   
  MMMMMMMMMMMMMMMMMMMMMMMMMMM.     CPU         -  Apple M1 (8)                 
   .MMMMMMMMMMMMMMMMMMMMMMMMMM.    Resolution  -  2880x1800@60fps (as 1440x900)
     MMMMMMMMMMMMMMMMMMMMMMMM      CPU Load    -  18%                          
      ;MMMMMMMMMMMMMMMMMMMM.       Memory      -  6.9 GB/16.8 GB               
        .MMMM,.    .MMMM,.         Battery     -  29% & Discharging            

❯ ./bench_parse_call
Unable to determine clock rate from sysctl: hw.cpufrequency: No such file or directory
2022-01-12T11:56:21+01:00
Running ./bench_parse_call
Run on (8 X 24.1207 MHz CPU s)
CPU Caches:
  L1 Data 64 KiB (x8)
  L1 Instruction 128 KiB (x8)
  L2 Unified 4096 KiB (x2)
Load Average: 1.85, 3.43, 3.01
-----------------------------------------------------------------------------------------------------
Benchmark                                           Time             CPU   Iterations UserCounters...
-----------------------------------------------------------------------------------------------------
fast_minify_twitter/repeats:10_mean             69008 ns        69008 ns           10 Gigabytes=9.15183G/s docs=14.4919k/s
fast_minify_twitter/repeats:10_median           68943 ns        68943 ns           10 Gigabytes=9.15999G/s docs=14.5048k/s
fast_minify_twitter/repeats:10_stddev             503 ns          503 ns           10 Gigabytes=66.6593M/s docs=105.555/s
fast_minify_twitter/repeats:10_cv                0.73 %          0.73 %            10 Gigabytes=0.73% docs=0.73%
fast_minify_twitter/repeats:10_max              69767 ns        69767 ns           10 Gigabytes=9.23685G/s docs=14.6265k/s
fast_minify_gsoc/repeats:10_mean               373133 ns       373131 ns           10 Gigabytes=8.91898G/s docs=2.68012k/s
fast_minify_gsoc/repeats:10_median             373703 ns       373703 ns           10 Gigabytes=8.90502G/s docs=2.67592k/s
fast_minify_gsoc/repeats:10_stddev               2332 ns         2331 ns           10 Gigabytes=55.7496M/s docs=16.7525/s
fast_minify_gsoc/repeats:10_cv                   0.62 %          0.62 %            10 Gigabytes=0.63% docs=0.63%
fast_minify_gsoc/repeats:10_max                376046 ns       376046 ns           10 Gigabytes=8.98738G/s docs=2.70067k/s
unicode_validate_twitter/repeats:10_mean        18935 ns        18935 ns           10 Gigabytes=33.3556G/s docs=52.8183k/s
unicode_validate_twitter/repeats:10_median      18825 ns        18824 ns           10 Gigabytes=33.5481G/s docs=53.1232k/s
unicode_validate_twitter/repeats:10_stddev        216 ns          216 ns           10 Gigabytes=379.187M/s docs=600.44/s
unicode_validate_twitter/repeats:10_cv           1.14 %          1.14 %            10 Gigabytes=1.14% docs=1.14%
unicode_validate_twitter/repeats:10_max         19286 ns        19286 ns           10 Gigabytes=33.7221G/s docs=53.3988k/s
parse_twitter/repeats:10_mean                  194275 ns       194275 ns           10 Gigabytes=3.25063G/s docs=5.14735k/s
parse_twitter/repeats:10_median                194240 ns       194240 ns           10 Gigabytes=3.25121G/s docs=5.14827k/s
parse_twitter/repeats:10_stddev                   115 ns          115 ns           10 Gigabytes=1.91993M/s docs=3.0402/s
parse_twitter/repeats:10_cv                      0.06 %          0.06 %            10 Gigabytes=0.06% docs=0.06%
parse_twitter/repeats:10_max                   194459 ns       194459 ns           10 Gigabytes=3.25271G/s docs=5.15065k/s
parse_gsoc/repeats:10_mean                     836943 ns       836942 ns           10 Gigabytes=3.97618G/s docs=1.19483k/s
parse_gsoc/repeats:10_median                   836795 ns       836794 ns           10 Gigabytes=3.97688G/s docs=1.19504k/s
parse_gsoc/repeats:10_stddev                      951 ns          951 ns           10 Gigabytes=4.51083M/s docs=1.35549/s
parse_gsoc/repeats:10_cv                         0.11 %          0.11 %            10 Gigabytes=0.11% docs=0.11%
parse_gsoc/repeats:10_max                      839211 ns       839211 ns           10 Gigabytes=3.98131G/s docs=1.19637k/s
parser_parse_error_code                          26.4 ns         26.4 ns     26491069
parser_parse_exception                           26.4 ns         26.4 ns     26684355
document_parse_error_code                         301 ns          301 ns      2321294
document_parse_exception                          285 ns          285 ns      2518520

simdjson/build/benchmark on  master [?] took 39s 
❯ 
```

Average load seems a bit nonsense (? I'm not sure at least), as `top` outputs its 99%.

---

Another interesting post by [EclecticLight](https://eclecticlight.co/2021/09/01/m1-icestorm-cores-can-still-perform-very-well/) is about Icestorm cores and QoS. Can it be beneficial at all for the current case to dig into this area?

Thanks everyone involved for the awesome work, by the way!

# Action History
- Created by: xq0404 | 2021-04-19T15:32:50+00:00
- Closed at: 2025-06-16T20:33:59+00:00
