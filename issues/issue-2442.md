---
title: Error in compiling (Windows 10 MSVC Visual Studio 2017)
source_url: https://github.com/xmrig/xmrig/issues/2442
author: XfedeX
assignees: []
labels: []
created_at: '2021-06-13T13:00:55+00:00'
updated_at: '2021-06-16T16:11:06+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
**Describe the bug**
Compilation fails because of:
```
Fatal Error C1083
Unable to open inclusion file 'uv.h': No such file or directory.
```
(Translated from Italian, in English the exact error text may be different...)
**To Reproduce**
Download and compile Xmrig on windows.

**NOTE:**
I used `-DWITH_TLS=OFF` because i am not able to make it work, any value i put in OPENSSL_ROOT_DIR doesn't work.

# Discussion History
## peme14k | 2021-06-13T21:08:46+00:00
#2442

## XfedeX | 2021-06-14T16:47:53+00:00
> 
> 
> #2442

Why you linked this same issue?

## Spudz76 | 2021-06-14T16:57:38+00:00
You need [xmrig-deps](https://github.com/xmrig/xmrig-deps) which includes everything you're missing...

Set `-DXMRIG_DEPS=X:/where/ever/is/xmrig-deps/msvc2017`

## XfedeX | 2021-06-15T20:57:41+00:00
> 
> 
> You need [xmrig-deps](https://github.com/xmrig/xmrig-deps) which includes everything you're missing...
> 
> Set `-DXMRIG_DEPS=X:/where/ever/is/xmrig-deps/msvc2017`

Sorry if I am noob, but where? If I try setting it in PROJECT>PROPERTIES>DEBUG>COMMAND LINE ARGS it still doesn't work . . . It gives the same error.

## ghost | 2021-06-16T01:59:23+00:00
> > You need [xmrig-deps](https://github.com/xmrig/xmrig-deps) which includes everything you're missing...
> > Set `-DXMRIG_DEPS=X:/where/ever/is/xmrig-deps/msvc2017`
> 
> Sorry if I am noob, but where? If I try setting it in PROJECT>PROPERTIES>DEBUG>COMMAND LINE ARGS it still doesn't work . . . It gives the same error.

Read this documentation clearly and move on

https://xmrig.com/docs/miner/build/windows

## Spudz76 | 2021-06-16T16:11:06+00:00
Seems like you're actually in Visual Studio for no reason (I only have the build-tools version installed).

CMake and msbuild are all that are needed do not open the resulting "project" that does no good.

# Action History
- Created by: XfedeX | 2021-06-13T13:00:55+00:00
