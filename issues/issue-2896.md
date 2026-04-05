---
title: Unclear public memory allocation
source_url: https://github.com/xmrig/xmrig/issues/2896
author: UnixCro
assignees: []
labels:
- question
created_at: '2022-01-25T07:46:51+00:00'
updated_at: '2022-06-04T09:08:03+00:00'
type: issue
status: closed
closed_at: '2022-04-03T08:11:19+00:00'
---

# Original Description
Hi,

I have a question. As far as I know, XMRig uses `2080 MB` per CPU by default, which is also considered NUMA in the manual.  In addition there is NUMA cache `256 MB` so we are already at `2336 MB`.  In some XMRig github problems I have seen that employees write `(+ threads * 2MB)`.  So we have a CPU with `4` threads.  So it would be `2080+256+8 = 2.344MB.`

Please correct me if I say wrong.

But now XMRig offers `huge sites` . `1168` by default, although the manual clearly states that `1280` is recommended.  I don't know why it's `1168` then?

But does it mean that when the huge pages are activated.  That my main memory, which we have occupied with `2.344 MB` anyway, is now `+ 2336 MB` again?  Or how should I understand that?

And at `1GB pages`.  There it says that the processor socket is increased to `1024 MB * 3`. Like right now?  So does XMRig occupy `3GB per NUMA node` or anything else in memory?

I think you can see that the explanation was really very complicated.  

Can someone explain to me how exactly XMRig and what XMRig stores in memory in `normal mode`. In `huge pages mode`.  And in `1GB pages mode`.  Thank you for reading

# Discussion History
## Spudz76 | 2022-01-25T10:42:49+00:00
When NUMA is enabled it will allocate one 2080MB dataset per NUMA-node.  Some CPUs have more than one node per physical CPU, but most don't.  Some Epyc have dual memory controllers thus show up as two nodes in one chip.  This ensures each node is using memory that is local to itself, and not having to ask the other CPU for the data, which clogs memory busses and hurts hashrate (if NUMA was disabled or unsupported).

The 256MB is just a shared working space for all threads.  Doesn't really have anything to do with NUMA, it is allocated on the primary node always.  It does not have a lot of traffic so going cross-CPU is fine, and it needs to be shared between all threads on all nodes anyway.

Then the 2MB scratchpad per mining thread, fairly straightforward and you understand it correctly.

Regular hugepages are 2MB each so you divide the memory needed by 2.  So `2344/2=1172` of the 2MB hugepages for your example `4` thread CPU.  1280 is just plenty of pages for up to 112 threads (almost any known CPU).  But, the 1168 is only enough for zero threads, the bare minimum to get hugepages for the dataset and shared space because `(2080+256)/2=1168`.  So then the proper number is 1168 plus your number of threads.  Also if algo-switching some algos need more pages and one of those uses the full 1280 if I remember correctly.  But for this thread we're only speaking of `rx/0`.

1GB hugepages are obviously 1GB, and yes then you need 3GB for each NUMA node because it must be in full units of the hugepage size.

If any size of hugepages are available then all allocations use as many as it can get, and there are no regular (4KB) pages allocated unless hugepage allocation fails or it is disabled or unsupported or partial.  So there is no duplicate usage but there could be a mixture.

But also when hugepages are reserved in Linux that memory becomes unusable by anything that uses 4KB pages so it will be "missing" even if xmrig isn't running or hasn't allocated them.  And if you forget to enable hugepages in xmrig then it will allocate 4KB pages in addition to the reserved hugepages and use double the memory, but that's a definite misconfiguration (do not reserve without enabling, that would be silly).

Hugepages must be aligned and empty so sometimes they have to be reserved at boot so that nothing destroys their usability by writing 4KB in the middle of a hugepage region, spoiling it.  If there are 4KB fragments all over the place there may not be any 1GB or even 2MB contiguous and aligned pages available.  Windows doesn't have reservation, so after long uptimes it may require reboot to "defrag" the RAM, usually there are no problems with 2MB allocations on a fresh boot, but then you should only pause the miner so it holds the allocations and Windows can't dirty them (as close as Windows can get to reserved -- keep them allocated but pause the work if needed).

## UnixCro | 2022-01-25T15:06:13+00:00
Thanks @Spudz76, you really put a lot of effort into your post.  I have just made a list and I ask you to correct the things that are wrong.  I would like to be able to learn them by heart to support my mining farm and not make bad purchases.
 I would prefer it if you could copy and paste it and correct things.  I will then note the improved in my manual.

Imagine I have a 4 thread processor & plenty of L3 cache and memory.

Would this be correct then?

<br>
<br>
<br>

# Light Mode 

<br>

```

256 MB NUMA-Knoten-Cache +
8,192 MB (2048 KB * 4 Threads)

= 264,192 MB occupied in memory
```

<br>

# Fast Mode 

<br>

```

2080 MB NUMA-Knoten +
256 MB NUMA-Knoten-Cache +
8,192 MB (2048 KB * 4 Threads)

= 2344,192 MB occupied in memory 
```

<br>

# Huge Pages

<br>

```

2080 MB NUMA-Knoten +
256 MB NUMA-Knoten-Cache  +
8,192 MB (2048 KB * 4 Threads) +
2336 MB (1168 Seiten) 

= 4680,192 MB occupied in memory
```

<br>

# 1-GB-Huge-Pages

```

3072 MB NUMA-Knoten +
256 MB NUMA-Knoten-Cache +
8,192 MB ( 2048 KB * 4 Threads ) +
4096 MB ( 1024 MB (1-GB-Pages)* 4 Threads )

= 7432,192 MB occupied in memory
```

<br>

And as a last question.  Why does Linux actually have `vm.nr_hugepages` in `sysctl`?  Does Linux, not XMRig, work even with huge pages or how does it work there?

 Could you give me your BTC address?  I would like to donate something to you.

## UnixCro | 2022-01-25T15:21:51+00:00
![2866CFCA-E340-427F-916A-8D3786AB86BF](https://user-images.githubusercontent.com/70098046/151004643-43e7cfb1-6342-45dd-b371-5664fcc10f0b.jpeg)

> But, the 1168 is only enough for zero threads, the bare minimum to get huge pages for the dataset and shared space because (2080+256)/2=1168.

My i7 11700 has 16 threads.  But still uses 1168 pages?

## Spudz76 | 2022-01-25T19:01:40+00:00
No it's using 1168 (for the dataset + shared) in the first line, and then another 8 for the threads (READY line) or 1176 total.

That CPU has 8 cores thus can mine 8 threads (not 16 because the HT's are "fake" for purposes of mining, on Intel but not Ryzen)

## Spudz76 | 2022-01-25T19:24:14+00:00
`nr_hugepages` is for reserving hugepages.  To allocate any hugepages they must first be reserved (two-step process).  If there are none reserved then xmrig attempts to reserve them itself but may fail (per the unclean/fragmented memory problem, or not running as root).  If you have 8GB or less total system memory, after boot there may not be any clean hugepage regions to reserve.  So then you set the reservations on the kernel command line (grub args) or in early boot via sysfsutils, before userspace fires up and starts allocating 4KB pages everywhere randomly.  If they are reserved early then no 4KB application can damage them.  This is especially true for the 1GB pages.  If you have 4GB total than you can't really use 1GB pages since 3GB would need to be early-reserved and then the entire rest of the system including the kernel must fit within the remaining 1GB which is essentially impossible.  8GB-3GB leaves 5GB behind which works fine so 8GB is essentially the minimum for 1GB hugepages to work.  There probably won't be any of those reservation/allocation problems with your 32GB.

The proper place for hugepages when NUMA is enabled are elsewhere in sysfs:
```
# grep . /sys/devices/system/node/node*/hugepages/hugepages-*/*
/sys/devices/system/node/node0/hugepages/hugepages-1048576kB/free_hugepages:0
/sys/devices/system/node/node0/hugepages/hugepages-1048576kB/nr_hugepages:3
/sys/devices/system/node/node0/hugepages/hugepages-1048576kB/surplus_hugepages:0
/sys/devices/system/node/node0/hugepages/hugepages-2048kB/free_hugepages:233
/sys/devices/system/node/node0/hugepages/hugepages-2048kB/nr_hugepages:240
/sys/devices/system/node/node0/hugepages/hugepages-2048kB/surplus_hugepages:0
/sys/devices/system/node/node1/hugepages/hugepages-1048576kB/free_hugepages:0
/sys/devices/system/node/node1/hugepages/hugepages-1048576kB/nr_hugepages:3
/sys/devices/system/node/node1/hugepages/hugepages-1048576kB/surplus_hugepages:0
/sys/devices/system/node/node1/hugepages/hugepages-2048kB/free_hugepages:233
/sys/devices/system/node/node1/hugepages/hugepages-2048kB/nr_hugepages:240
/sys/devices/system/node/node1/hugepages/hugepages-2048kB/surplus_hugepages:0
```

Here you see I have the 3 * `1048576kB` (1GB) hugepages on each node (0 and 1).  They are all in use (allocated) because the `free_hugepages` is `0`.  If xmrig was not running then `free_hugepages` would equal the `nr_hugepages`, and `surplus_hugepages` would be `3` because all of them are not allocated.

If you set the main (non-NUMA) `nr_hugepages` or via sysctl (the "old" way from before NUMA, left there for compatibility), then it attempts to split them evenly across nodes, and then it should be the total of all nodes reservations.

Even if there is just node0 from NUMA, setting the per-node sysfs locations is still more correct than using sysctl.

This example rig does algo-switching therefore the 2MB hugepages being allocated and partially used.  During algo-switching the RandomX dataset stays allocated even when it jumps to some other algorithm that doesn't use it, but does use 2MB hugepages).  So I have a bunch of extra reservations you wouldn't need for pure rx/0 mining only.

## Spudz76 | 2022-01-25T19:56:18+00:00
For the above system I have grub kernel args:
`hugepagesz=1GB hugepages=6 hugepagesz=2MB hugepages=480`

The way the kernel args work you set which size you are setting then set the reservation.  So you repeat the `hugepages=N` after setting which one is targeted with `hugepagesz` just before it.  I believe if you completely omit `hugepagesz` the default is 2MB (so if you only had a `hugepages` setting it would be for 2MB hugepages even if the system supports 1GB also).

And then the system automatically split them onto each node (3 and 3 for the 6 `1GB` ones and then 240 and 240 for the 480 `2MB` ones).

But also sysctl does not have any 1GB hugepages access, because back when sysctl was the way there weren't 1GB hugepages yet.  sysfs locations were added when NUMA and then 1GB hugepages were added, but 1GB was not "backported" into the deprecated sysctl interface.  So to reserve any 1GB hugepages you must use the sysfs locations, and the combined ones are in `/sys/kernel/mm/hugepages/hugepages-*/*` (which are what the kernel args would set, leading to the automatic NUMA node splitting).

I reserve the 1GB hugepages first because of the dirtying regions problem, if I did the 2MB ones first they might select regions which invalidate 1GB regions.  So always reserve them in inverse size order (largest first) so that nothing can steal regions within the larger regions before they are reserved.  If you are not algo-switching and are only using RandomX then you probably don't need any 2MB pages at all so this is not really a rule you'd need to know.

If you had an Apple M1 chip, those don't have 4KB pages at all and so far also can't use their 2MB hugepage support even though it's supposed to be there in the hardware.  So they always use 16KB pages which aren't "regular" 4KB but also aren't really "huge".

## UnixCro | 2022-01-26T16:29:17+00:00
Okay, I can tell what you've got is a masterpiece.  I had to read the text more than several times to understand it.

———————————————————————

<br>

> No it's using 1168 (for the dataset + shared) in the first line, and then another 8 for the threads (READY line) or 1176 total.

<br>

Actually. The huge pages are allocated there so as far as I understand from you we have: 1168 huge pages with 0 threads. + My 8 threads = 1176 x 2MB huge pages.

Alright then, 1176 huge pages...

So the huge pages ( 1176*2 MB ) occupy memory.  So we would have occupied 2352 MB by the huge pages in RAM.

 If necessary, read the above twice

———————————————————————

<br> 

Now it comes.  In older XMRig Github issues, @SChernykh or you write:

 > 1 GB pages is 3 pages (3072 MB);  2MB get 1168 pages (2336MB);  4 KB (not huge pages) gets 1196032 pages (2336 MB).

So wait a minute.  If we use huge pages.  Then we use 2-MB-Pages and no longer 4-KB-Pages.  So 1168 huge pages + Threads and not 1196032 4-KB-Pages.

Then I apologize for my incomprehension.  XMRig only uses 2336 MB + ( 2 MB * threads) of memory. And not NUMA + cache + huge pages.  Because the data set ( NUMA + Cache ) is only meant to be 4-KB-pages.

<br>

> When NUMA is enabled it will allocate one 2080MB dataset per NUMA-node

So now the (2080+256) is intended for the NUMA area?  If it were for 4 KB pages then yes this wouldn't make sense when we are using huge pages. Then the 2336 MB would simply split into 2 MB pages.

But saying that 2336 MB (data set) + 2336 MB (huge pages) doesn't make any sense.

Because the quote says "4 KB (not huge pages) get 1196032 pages (2336 MB)."

 I hope you can understand it to some extent.

<br>
<br>

> Windows doesn't have reservation, so after long uptimes it may require reboot to "defrag" the RAM, usually there are no problems with 2MB allocations on a fresh boot, but then you should only pause the miner so it holds the allocations and Windows can't dirty them (as close as Windows can get to reserved -- keep them allocated but pause the work if needed).


But that was the question.  Why does Linux even have the option of reserving "huge pages".  Imagine a Linux user who doesn't know XMRig.  But sees the possibility to activate "giant pages" in sysctl.  Then, of course, you ask yourself what Linux is used for.  I did some research on the internet and found this:

> When a process uses some memory, the CPU is marking the RAM as used by that process. For efficiency, the CPU allocate RAM by chunks of 4K bytes (it's the default value on many platforms). Those chunks are named pages. Those pages can be swapped to disk, etc.
Since the process address space are virtual, the CPU and the operating system have to remember which page belong to which process, and where it is stored. Obviously, the more pages you have, the more time it takes to find where the memory is mapped. When a process uses 1GB of memory, that's 262144 entries to look up (1GB / 4K). If one Page Table Entry consume 8bytes, that's 2MB (262144 * 8) to look-up.
Most current CPU architectures support bigger pages (so the CPU/OS have less entries to look-up), those are named Huge pages (on Linux), Super Pages (on BSD) or Large Pages (on Windows), but it all the same thing.

<br>

> If you have 4GB total than you can't really use 1GB pages since 3GB would need to be early-reserved

But why 3GB (3072MB)?  The XMRig manual states that 3GB alone is reserved for the entire NUMA.  So each thread would have to occupy 1 GB of pages in addition?  Otherwise, wouldn't the normal huge pages consume more than the 1GB pages?

<br> 

> The 256MB is just a shared working space for all threads. Doesn't really have anything to do with NUMA, it is allocated on the primary node always.

But then why do we give the threads a workspace by saying 2336MB + (2MB * threads)?

<br>

———————————————————————
> If you had an Apple M1 chip, those don't have 4KB pages at all and so far also can't use their 2MB hugepage support even though it's supposed to be there in the hardware. So they always use 16KB pages which aren't "regular" 4KB but also aren't really "huge"

<br>

```
# grep . /sys/devices/system/node/node*/hugepages/hugepages-*/*
/sys/devices/system/node/node0/hugepages/hugepages-1048576kB/free_hugepages:0
/sys/devices/system/node/node0/hugepages/hugepages-1048576kB/nr_hugepages:3
/sys/devices/system/node/node0/hugepages/hugepages-1048576kB/surplus_hugepages:0
/sys/devices/system/node/node0/hugepages/hugepages-2048kB/free_hugepages:233
/sys/devices/system/node/node0/hugepages/hugepages-2048kB/nr_hugepages:240
/sys/devices/system/node/node0/hugepages/hugepages-2048kB/surplus_hugepages:0
/sys/devices/system/node/node1/hugepages/hugepages-1048576kB/free_hugepages:0
/sys/devices/system/node/node1/hugepages/hugepages-1048576kB/nr_hugepages:3
/sys/devices/system/node/node1/hugepages/hugepages-1048576kB/surplus_hugepages:0
/sys/devices/system/node/node1/hugepages/hugepages-2048kB/free_hugepages:233
/sys/devices/system/node/node1/hugepages/hugepages-2048kB/nr_hugepages:240
/sys/devices/system/node/node1/hugepages/hugepages-2048kB/surplus_hugepages:0
```

<br>

Very very interesting.  I would have had to search a long time for this information.

 So I would like to say a big thank you to you.  All the knowledge you gave me would save me a lot of time and nerves.  I will reward you for it.  I have one more small request.  Above I have "Light Mode";  "Fast Mode";  "Huge Pages";  1-GB-Huge-Pages". If you could correct that so that I could enter it in my manual, I would be very grateful. I think that would solve many problems of understanding.

Thank you for your effort and your answers

## UnixCro | 2022-06-04T07:27:00+00:00
The problem hasn't been fixed, so it's closed, but oh well. 

## Spudz76 | 2022-06-04T09:08:03+00:00
> But why 3GB (3072MB)? The XMRig manual states that 3GB alone is reserved for the entire NUMA. So each thread would have to occupy 1 GB of pages in addition? Otherwise, wouldn't the normal huge pages consume more than the 1GB pages?

Because to use any page size the allocation must be in whole pages of that size.  So, with 1GB pages, you get to choose 1, 2, or 3GB sizes and so if you need ~2.5GB then you allocate 3 (round upward to next whole-1GB).  Threads always use 2048KB or failing that 4KB pages (which also answers why you still need some of those allocated, but you are correct it's not the full 2.5GB worth).  1GB pages are just for the dataset.

In algo-hopping configurations there are other algorithms which don't use 1GB pages either, so they may need excess 2MB pages.  If you just run rx/0 or otherwise specific/locked algorithm then you don't need agility slack (maximum combination of every algo needs).

# Action History
- Created by: UnixCro | 2022-01-25T07:46:51+00:00
- Closed at: 2022-04-03T08:11:19+00:00
