---
title: An inquiry on running xmrig on OpenBSD
source_url: https://github.com/xmrig/xmrig/issues/3065
author: AndreiSva
assignees: []
labels:
- wontfix
created_at: '2022-06-09T07:12:51+00:00'
updated_at: '2025-06-29T00:30:02+00:00'
type: issue
status: closed
closed_at: '2025-06-29T00:30:02+00:00'
---

# Original Description
OpenBSD shares a lot of ideals with cryptocurrencies and especially monero. And as an OpenBSD user interested in such currencies I was excited to use xmrig to mine. Unfortunately it appears that `hwloc`, one of xmrig's dependencies does not run on OpenBSD. 

How necessary is the dependency for the core function of xmrig? Could it potentially be made an optional dependency on OpenBSD? If not is there any other possible way to get xmrig to run? Or does OpenBSD just lack too many hashrate optimization features for it to not be feasible to mine on? 

# Discussion History
## SChernykh | 2022-06-09T07:15:17+00:00
You can use `-DWITH_HWLOC=OFF` in cmake parameters.

## AndreiSva | 2022-06-10T02:29:22+00:00
Still doesn't work. Apparently OpenBSD doesn't implement the `setcpu` syscall which xmrig uses.

## Spudz76 | 2022-06-12T22:40:44+00:00
```
x@y:/usr/src/xmrig$ grep -ir setcpu src
x@y:/usr/src/xmrig$ 
```

...it does?

## Spudz76 | 2022-06-12T22:50:45+00:00
My bad, looks like it uses a [CPU_SET define](https://github.com/xmrig/xmrig/blob/master/src/base/kernel/Platform_unix.cpp#L81) that all other UNIXes have (even other BSD like MacOS) so this almost seems more like OpenBSD's fault.

## Spudz76 | 2022-06-12T23:02:17+00:00
And confirmation from [hwloc team](https://github.com/open-mpi/hwloc/issues/224#issuecomment-278007109) that it's definitely OpenBSD's fault for not supporting what literally everyone else does (FreeBSD, NetBSD, OSX...) and it's required to even probe the CPU properly (individual threads/cores must be pinned to the thread/core being probed...)

So xmrig might mostly work but without any affinity anything, and it also might not be able to tell what sort of cache sizes (or other CPUID specs) so you'd have to manually configure the thread counts, with the equivalent of `[-1, -1, -1, -1]` where it doesn't set any affinity but brings up four threads wherever the OS decides to put them.  And maybe also manually set the asm mode or other things that usually auto-set based on CPUID probes.

I don't feel like firing up an OpenBSD VM to hack at it.  Feel free to hunt and deactivate anywhere affinity is set until it compiles, and then see if it does anything.

## xmrig | 2025-06-29T00:30:02+00:00
OpenBSD is kind of useless for mining.
1. No huge pages support.
2. No CPU topology; as a result, there is no hwloc support and no way to auto-config, even a simple one.
3. No any kind of CPU affinity.
4. Enforced secure JIT with itself hurts performance and requires additional effort to make it just work.

# Action History
- Created by: AndreiSva | 2022-06-09T07:12:51+00:00
- Closed at: 2025-06-29T00:30:02+00:00
