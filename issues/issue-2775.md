---
title: Command-line option --cpu-priority=0 is position-dependent
source_url: https://github.com/xmrig/xmrig/issues/2775
author: ghost
assignees: []
labels:
- bug
- algo
created_at: '2021-12-02T19:28:54+00:00'
updated_at: '2025-06-16T20:25:07+00:00'
type: issue
status: closed
closed_at: '2025-06-16T20:25:07+00:00'
---

# Original Description
````
$ xmrig -a gr --cpu-priority=0 --tls --url=eu.flockpool.com:5555 ...
 * ABOUT        XMRig/6.16.2 clang/13.0.0
 * LIBS         libuv/1.42.0 OpenSSL/1.1.1l hwloc/2.5.0
 * ....
````

# Discussion History
## Spudz76 | 2021-12-02T19:36:21+00:00
If you already have cpu->priority in config.json you must change it there.

config.json always wins over most commandline options (unless they don't exist in the config.json)

## SChernykh | 2021-12-02T19:37:52+00:00
How did you determine that it "has no effect"?

## SChernykh | 2021-12-02T19:40:13+00:00
If you're running Linux, xmrig sets priorities per thread, not for the whole process, so you won't see it in a regular `top` command with default display settings.

## ghost | 2021-12-02T19:44:17+00:00
The output of the following command-line is empty:

    $ strace -f xmrig -a gr --cpu-priority=0 --tls --url=eu.flockpool.com:5555 ... |& grep json

> How did you determine that it "has no effect"?

htop screenshot:

![Screenshot_20211202_204143](https://user-images.githubusercontent.com/22368256/144491919-f88f60e7-7974-4074-9f5a-38b6fd76f258.png)


## SChernykh | 2021-12-02T19:49:49+00:00
What OS are you using? XMRig official release or self compiled?

## ghost | 2021-12-02T19:52:01+00:00
Gentoo Linux. xmrig is compiled from sources.

````
$ cat build.sh 
#!/bin/bash
set -e
export CC=ccache-clang
export CXX=ccache-clang++
export CFLAGS="-flto -g1 -gz -march=native -O3 -Wall"
export CXXFLAGS="$CFLAGS"
rm -fr CMakeCache.txt CMakeFiles
cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo -DCMAKE_VERBOSE_MAKEFILE=TRUE .
make -j$(nproc)
````

## SChernykh | 2021-12-02T19:55:01+00:00
My only guess is that `SCHED_IDLE` is not defined on your system: https://github.com/xmrig/xmrig/blob/master/src/base/kernel/Platform_unix.cpp#L135

Can you try the official Linux static build? You can also try `--cpu-priority=1` to see if it works.

## ghost | 2021-12-02T20:22:42+00:00
It turns out that the bug to fix is to make the following two commands behave identically:

    $ xmrig -a gr --cpu-priority=0 --tls --url=eu.flockpool.com:5555 --user=foo

    $ xmrig -a gr --tls --url=eu.flockpool.com:5555 --user=foo --cpu-priority=0

That is: If `--cpu-priority=0` isn't the last argument then it has no effect.

# Action History
- Created by: ghost | 2021-12-02T19:28:54+00:00
- Closed at: 2025-06-16T20:25:07+00:00
