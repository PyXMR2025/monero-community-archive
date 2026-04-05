---
title: How can I set the exact number of threads to use for RandomX in JSON config?
source_url: https://github.com/xmrig/xmrig/issues/2107
author: crocket
assignees: []
labels: []
created_at: '2021-02-16T06:35:30+00:00'
updated_at: '2021-05-31T00:23:10+00:00'
type: issue
status: closed
closed_at: '2021-04-12T14:13:39+00:00'
---

# Original Description
On command line, I can specify `-t` or `--threads`.
In JSON config, there is https://github.com/xmrig/xmrig/blob/master/doc/CPU.md#threads-definition and https://github.com/xmrig/xmrig/blob/master/doc/CPU.md#max-threads-hint-since-v420

Because my CPU has 12 threads, max-threads-hint cannot exactly specify number of threads to use.
10/12 = 0.8333333.....

Short object format for "threads" is not well defined, either. What is `intensity`? What are real valid values for CPU affinity? What is CPU affinity? What does each value of CPU affinity do?

Why can I not just specify `threads: 8` in JSON config?

https://github.com/xmrig/xmrig/blob/master/src/config.json doesn't really tell me how threads are manipulated.

Where am I supposed to define `"threads"` in JSON config?

Thread configuration should be unambiguously documented.

# Discussion History
## Lonnegan | 2021-02-16T14:15:41+00:00
https://github.com/xmrig/xmrig/issues/2084#issuecomment-774500529

## crocket | 2021-02-16T22:53:42+00:00
The issue is ambiguity of documentation.

I finally understood https://github.com/xmrig/xmrig/blob/master/doc/CPU.md after watching xmrig automatically write configuration and watching xmrig output on terminal emulator for hours.

However, https://github.com/xmrig/xmrig/blob/master/doc/CPU.md doesn't explain profile clearly. CPU.md assumes that I already know what profile is conceptually. That's why I was confused. CPU.md can serve as a reference for people who already know profiles conceptually.

CPU.md doesn't explain that each profile is a thread configuration for any algorithm that matches the profile. That's why I was confused to hell.

CPU.md doesn't explain how exactly an algorithm matches a profile. There are examplers, but examples don't substitute for concepts and theories.

Lastly, english grammar is bad in CPU.md. Bad english grammar confused me even more.

CPU.md should rigorously define profiles with examples in properly written english. If it takes hours for a computer veteran to understand documentation, it should be improved.

## Spudz76 | 2021-02-17T04:06:45+00:00
I'm a computer veteran and didn't need the documentation to figure out how it works.  Having looked at it for the first time now, it could be improved.

I'm actually more confused about what you're confused about.

Hints are used during autoconfiguration and are completely ignored after that phase.  That's why they are hints.  If you have 80 threads hand-configured in a definition it's not going to stop that, because it's a hint not a limit.  Conversely if you supply a hint of 80 threads but your CPU only has enough cores or cache to do two threads of a particular algo, the autoconfiguration limit will still be two threads.  Again it's a hint not an enforcement, and has nothing to do with runtime once the definitions have been generated and saved.

Intensity is simply how many work subthreads to run under a single upper management thread.  Normally 1:1 but you can do 2 threads per core for some smaller algos (cn-pico) for some gains.  This is different than what intensity means for GPUs, which is more like work batch size.  Never needs to be used unless the autoconfigurator already did, thus the lack of docs on how to use it.

Affinity depends on your system.  In general it's the core number beginning with zero, except where `-1` means automatic.  So if you have 8 thread cpu then you can use affinity 0-7, but with hyperthreading half of them will be the fake-cores, but which ones depend on the OS (Linux generally interleaves them so that evens are real and odds are fake, Windows does whatever it wants but usually all reals and then all fakes not interleaved).  But this CPU affinity idea is universal and not special to this miner, so google "what is cpu affinity", the knowledge of that is outside the scope of documentation here (or we should also document how electricity works? at some level).

Everything else about how thread decisions are made depend on the algo, and you need to know each algo's requirements to predict what autconfiguration will do.  In general for cryptonights divide the cache size by scratchpad size for max threads, and then if that is somehow larger than actual physical cores (not "threads") then reduce to physical core count.  So normal cryptonight is 2MB therefore to fully utilize a four core cpu it would need 8MB cache minimum, otherwise threads will be cut (a CPU core is pointless without cache to back it, for mining).  Other algos have other limitations which is again outside the scope of the CPU.md docs.

## crocket | 2021-02-17T11:22:06+00:00
The documentation still doesn't explain what a CPU affinity number means.

Until I read https://github.com/xmrig/xmrig/issues/2084#issuecomment-774500529, I thought CPU affinity number was some black magic.

I thought `[-1, -1, -,1 -1]` instructed xmrig to use the first 4 CPU threads and numbers other than `-1` meant how strongly xmrig binds to the first 4 threads. Thus, with `[-1, 3, -1, -1]`, xmrig would try very hard to bind to the second CPU thread.

If you don't define meanings of values explicitly, people are going to guess the meanings. There can be multiple meanings for any number. If you don't explain, people are going to guess crazy things.

CPU affinity values can be defined very differently in different applications. Each application has to explain its own semantics.

If I wrote xmrig, CPU affinity values could have been structured very differently.

Assuming that other people have the same cultural assumptions can backfire later. I'm a newbie who's exploring the conventions of this specific software. Every software is its own culture and has its own convetions. Softwares are similar but don't share the same exact conventions.

## Spudz76 | 2021-02-18T07:48:30+00:00
Nah, cpu affinity is always core number from 0, that's an industry standard.  Equal to the cpu index from sysfs (`ls -d /sys/devices/system/cpu/cpu*`) which makes so much sense it seems obvious.  Only other option is raw affinity-mask bitfield but that doesn't make sense unless specifying multiple cores into groups (which is not useful for a miner app).  Stuff like MySQL uses the raw bitmask for (optional) affinities as that type of task can be "fenced" to a certain subset of multiple cores.

So then `-1` is the only mysterious setting but that's also fairly standard for "don't care" or "auto" wherever literal null or strings are invalid.

I can't even think of any other way it would be, care to explain how you'd do it since it's so different?

## crocket | 2021-02-18T08:13:03+00:00
If I had an 8-core CPU, `[-1, -1, -1, -1]` in my version of xmrig could actually mean `[0 but can bind any other core, 1 but can bind any other core, 2 but can bind any other core, 3 but can bind any other core, disabled, disabled, disabled, disabled]` in xmrig.

Anyway, I think things I mentioned are better documented because new miners haven't used any application that deals with CPU affinity.

People should be able to write json config without having read automatically generated config and experimenting with options.

I want formal easy-to-understand definitions for algorithm thread profiles and thread definitions so that new users aren't confused.

## SChernykh | 2021-02-18T08:29:34+00:00
-1 means thread affinity is not set by XMRig at all, so it's up to OS which core to use for this thread.

## SChernykh | 2021-05-30T09:12:04+00:00
https://xmrig.com/docs/miner/command-line-options
```
--randomx-init=N thread count to initialize RandomX dataset
--threads=N number of CPU threads. Proper CPU affinity required for some optimizations.
```

## Spudz76 | 2021-05-30T12:08:57+00:00
Note: you have to delete all algo-defs from the cpu section of the config.json for initial configuration mode hints like `--threads` to work... or it doesn't autoconfigure thus doesn't need your thread hints.  It isn't an override, it's a hint...

# Action History
- Created by: crocket | 2021-02-16T06:35:30+00:00
- Closed at: 2021-04-12T14:13:39+00:00
