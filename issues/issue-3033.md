---
title: 'Static builds for aarch64 please '
source_url: https://github.com/xmrig/xmrig/issues/3033
author: seisdr
assignees: []
labels: []
created_at: '2022-04-21T03:28:18+00:00'
updated_at: '2025-06-18T23:02:39+00:00'
type: issue
status: closed
closed_at: '2025-06-18T23:02:39+00:00'
---

# Original Description
No description

# Discussion History
## JacksonChen666 | 2022-06-16T20:12:17+00:00
aarch64 architecture is not enough information unless the plan is to support aarch64 on all platforms.

do you want support for aarch64 for linux, freebsd, or ubuntu (windows is out of the question because pretty much the lack of demand really)? or for macOS?

there's already a binary for macOS (available on the download page).
and you should be able to compile an aarch64 binary yourself, even if none is provided as of right now (i did it on linux running on M1 mac (thanks to [asahi linux](https://asahilinux.org/)).

## seisdr | 2022-06-16T20:27:01+00:00
A binary executable that run on any aarch64 with no extra libraries just fetch a binary and run it 
It's easy to compile but i prefer static 

## JacksonChen666 | 2022-06-16T20:52:14+00:00
> A binary executable that run on any aarch64

yeah uh just really, don't expect a macOS binary to work on linux.
linux binary on another linux system on aarch64? sure, if it works.

> with no extra libraries just fetch a binary and run it 

you can compile that type of binary yourself, but [apparently only works on alpine linux and freebsd](https://xmrig.com/docs/miner/cmake-options#:~:text=STATIC=ON)

> It's easy to compile but i prefer static

if it's easy to [compile it yourself](https://xmrig.com/docs/miner/build) then compile it yourself. but because you prefer static, [compile with the static flag](https://xmrig.com/docs/miner/cmake-options#:~:text=STATIC=ON).
but if you can't compile with static (even in like a VM of some sort), compile and copy to see if it works. if it doesn't, compile on the system you're trying to run it on. (if it's a lot then maybe a static binary may be worth it).

to save you some trouble of accidentally running a development version, link to the source code download [in zip format](https://github.com/xmrig/xmrig/archive/refs/tags/v6.17.0.zip) or [in tar.gz format](https://github.com/xmrig/xmrig/archive/refs/tags/v6.17.0.tar.gz) for v6.17.0

## Spudz76 | 2022-06-16T21:43:47+00:00
aarch64 systems are widely variable, unlike x86_64

they all use almost random libc's and even when static it has to be compatible with the OS libc version (usually glibc)

What you are asking is not actually possible.

## Kaned1as | 2024-01-28T01:47:39+00:00
I hacked a generic version, see [here](https://gitlab.com/Kanedias/xmrig-aarch64-static)

# Action History
- Created by: seisdr | 2022-04-21T03:28:18+00:00
- Closed at: 2025-06-18T23:02:39+00:00
