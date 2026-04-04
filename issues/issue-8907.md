---
title: Problem after building monero from source
source_url: https://github.com/monero-project/monero/issues/8907
author: SnAFKe
assignees: []
labels:
- arm
created_at: '2023-06-15T02:57:33+00:00'
updated_at: '2023-12-07T21:10:42+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
I'm running AMR64 on Debian 11 and trying to building monero from source.

I'm compile static binaries, building finish without issue.

When i'm try to run monerod without issue but flood me with this.

```
[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:133	Exception: std::bad_alloc
[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:134	Unwound call stack:
[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [1] /usr/local/bin/monerod(+0x4eb634) [0xaaaad8f6b634] 
[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [2] /usr/local/bin/monerod(+0x873af4) [0xaaaad92f3af4] 
[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [3] /usr/local/bin/monerod(+0x86d17c) [0xaaaad92ed17c] 
[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [4] /usr/local/bin/monerod(+0x86a32c) [0xaaaad92ea32c] 
[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [5] /usr/local/bin/monerod(+0x4b287c) [0xaaaad8f3287c] 
[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [6] /usr/local/bin/monerod(+0x4b37e0) [0xaaaad8f337e0] 
[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [7] /usr/local/bin/monerod(+0x49b54c) [0xaaaad8f1b54c] 
[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [8] /usr/local/bin/monerod(+0x49b734) [0xaaaad8f1b734] 
[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [9] /usr/local/bin/monerod(+0x49b7fc) [0xaaaad8f1b7fc] 
[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [10] /usr/local/bin/monerod(+0x442e44) [0xaaaad8ec2e44] 
[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [11] /usr/local/bin/monerod(+0x4e413c) [0xaaaad8f6413c] 
[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [12] /usr/local/bin/monerod(+0x4e49ac) [0xaaaad8f649ac] 
[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [13] /usr/local/bin/monerod(+0x449908) [0xaaaad8ec9908] 
[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [14] /usr/local/bin/monerod(+0x46ae88) [0xaaaad8eeae88] 
[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [15] /usr/local/bin/monerod(+0x3ff004) [0xaaaad8e7f004] 
[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [16] /usr/local/bin/monerod(+0x1715f4) [0xaaaad8bf15f4] 
[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [17] /usr/local/bin/monerod(+0x3e8288) [0xaaaad8e68288] 
[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [18] /usr/local/bin/monerod(+0x3e966c) [0xaaaad8e6966c] 
[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [19] /usr/local/bin/monerod(+0x25cd84) [0xaaaad8cdcd84] 
[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [20] /usr/local/bin/monerod(+0x13fc2c) [0xaaaad8bbfc2c] 
[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [21] /usr/local/bin/monerod(+0x37bd7c) [0xaaaad8dfbd7c] 
[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [22] /usr/local/bin/monerod(+0x3b1898) [0xaaaad8e31898] 
[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [23] /usr/local/bin/monerod(+0xa8377c) [0xaaaad950377c] 
[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [24] /lib/aarch64-linux-gnu/libpthread.so.0(+0x7648) [0xffffa19db648] 
[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [25] /lib/aarch64-linux-gnu/libc.so.6(+0xd1fdc) [0xffffa1931fdc] 
```
This only happen building monero from source and if i use official binary not have this issue.

I've enough memory and space too, also i not have any memory issue.

Not sure what i doing wrong from building from source.

# Discussion History
## 0xFFFC0000 | 2023-06-15T05:36:32+00:00
Can you build a debug build? 

This should not happen. It seems there is an issue/mismatch with one of the libraries you are using to build Monero. 

## SnAFKe | 2023-06-15T09:57:06+00:00
How i can build debug static armv8?

## 0xFFFC0000 | 2023-06-15T10:01:06+00:00
Are you cross-compiling?


I am not sure about your specific architecture. But generally, you can build debug binaries via 
``` 
make debug
```


## selsta | 2023-06-15T10:05:54+00:00
That's the libunwind library. The official binaries don't ship with libunwind, that's why you don't see these log messages.

## SnAFKe | 2023-06-15T10:12:08+00:00
> Are you cross-compiling?
> 
> I am not sure about your specific architecture. But generally, you can build debug binaries via
> 
> ```
> make debug
> ```

No.

> That's the libunwind library. The official binaries don't ship with libunwind, that's why you don't see these log messages.

I already see somewhere in here but i uninstall libunwind8-dev (debian) and still give me this error.

## selsta | 2023-06-15T10:13:16+00:00
You have to uninstall it and then do a clean recompile, just uninstalling isn't enough.

Also libunwind and libunbound are not the same thing, you have to uninstall the correct library.

## SnAFKe | 2023-06-15T10:14:44+00:00
I know, even i delete folder and clone again and still.

## selsta | 2023-06-15T10:26:25+00:00
Please share a build log on paste.debian.net so that I can see if libunwind is still used or not.

## SnAFKe | 2023-06-15T10:40:56+00:00
Sorry, where are the logs located?

## selsta | 2023-06-15T10:42:11+00:00
It prints it to the command line after entering `make`.

## SnAFKe | 2023-06-15T10:54:23+00:00
[https://paste.debian.net/plainh/1083bead](url)

## selsta | 2023-06-15T11:11:11+00:00
-- Stack trace on exception enabled (using easylogging++)


it uses a different library, will have to check how to disable it

## selsta | 2023-06-15T13:12:23+00:00
Try to delete all this code and build again: https://github.com/monero-project/monero/blob/master/CMakeLists.txt#L528-L561

## SnAFKe | 2023-06-16T07:05:01+00:00
Seems to work now, running about 12h and not issue.

But my curious why you can build without this error and not modify anything?

Hope now my other problem solve to apply patch for that issue.

## selsta | 2023-06-16T12:34:52+00:00
It's not an error, it's just logging. You just disabled the logging of this exception but the exception itself continues to happen.

## SnAFKe | 2023-06-16T17:10:03+00:00
But that is ignoring the error and not solving the problem, that does not generate a loss of performance.

Damn it, the other problem not fix issue, i'm sick with that error i going to create separate issue.

## selsta | 2023-06-16T21:40:39+00:00
Try to enable hugepages: https://xmrig.com/docs/miner/hugepages

See also https://github.com/monero-project/monero/issues/8790#issuecomment-1498778690

# Action History
- Created by: SnAFKe | 2023-06-15T02:57:33+00:00
