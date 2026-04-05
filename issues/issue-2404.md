---
title: '"Building CXX object" failed on debian arm64. error: missing binary operator
  before token "(" on multiple cxx header files.'
source_url: https://github.com/xmrig/xmrig/issues/2404
author: HimDek
assignees: []
labels: []
created_at: '2021-05-23T02:45:31+00:00'
updated_at: '2021-05-29T10:09:38+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
**_Trying to build v6.12.1 on debian for arm64_**

Command `root@debian:~/xmrig/build# cmake..` completes successfully without any error or fail but,

Command `root@debian:~/xmrig/build# make` runs without error till `Scanning dependencies of target xmrig` but fails multiple times while  `Building CXX object`. Errors are found in multiple CXX header files saying `error: missing binary operator before token "("`

[Heres the full log](https://github.com/xmrig/xmrig/files/6527437/log.txt).

What do I do?

**REQUEST:**
**Could someone please share a precompiled arm64 build of xmrig?**

# Discussion History
## Spudz76 | 2021-05-23T03:25:13+00:00
Seems related to Android SDK problem as seen here: https://github.com/abseil/abseil-cpp/issues/121

~Working up a patch for you to test.~

Nevermind looks like it's in the system headers which seems broken upstream.  Maybe something wrong with the installation.

## HimDek | 2021-05-23T03:46:21+00:00
Should I reinstall something?

## Spudz76 | 2021-05-23T04:04:41+00:00
Investigating.

Does `dpkg-query -l | grep gcc` all say `aarch64`?

## HimDek | 2021-05-23T04:26:34+00:00
```
root@debian:~/xmrig/build# dpkg-query -l | grep gcc
ii  gcc                        4:10.2.1-1                     arm64        GNU C compiler
ii  gcc-10                     10.2.1-6                       arm64        GNU C compiler
ii  gcc-10-base:arm64          10.2.1-6                       arm64        GCC, the GNU Compiler Collection (base package)
ii  gcc-8-base:arm64           8.3.0-6                        arm64        GCC, the GNU Compiler Collection (base package)
ii  gcc-9-base:arm64           9.3.0-22                       arm64        GCC, the GNU Compiler Collection (base package)
ii  libgcc-10-dev:arm64        10.2.1-6                       arm64        GCC support library (development files)
ii  libgcc-s1:arm64            10.2.1-6                       arm64        GCC support library
ii  libgcc1:arm64              1:8.3.0-6                      arm64        GCC support library
```

Should i remove gcc-8-base and gcc-9-base?

## Spudz76 | 2021-05-23T09:48:47+00:00
Yes that might be something to do with it, but it does seem like the files it dislikes are properly the 10 version.

There are a lot of various similar problems on other software for arm64 there might be a workaround.

## HimDek | 2021-05-23T13:18:41+00:00
> maybe you can try my binaries
> https://github.com/cmxhost/xmrig/releases/tag/v6.12.1

**Will try that...**
@cmxhost I appreciate your arm64 binary release. Maybe the official @xmrig should also add one.

## HimDek | 2021-05-23T14:11:34+00:00
**_UPDATE_**

Compiling on Alpine for arm(aarch64):
Fails while executing `make` yeilds the following [logs](https://github.com/xmrig/xmrig/files/6528224/log.txt).


## ghost | 2021-05-23T14:15:47+00:00
> **_UPDATE_**
> 
> Compiling on Alpine for arm(aarch64):
> Fails while executing `make` yeilds the following [logs](https://github.com/xmrig/xmrig/files/6528224/log.txt).

I don't know how you done in cmake command,  for me works fine 

## HimDek | 2021-05-23T14:18:56+00:00
why does asm/hwcap.h not exist for me? How to add it?

## HimDek | 2021-05-23T14:42:26+00:00
> **_Trying to build v6.12.1 on debian for arm64_**
> 
> Command `root@debian:~/xmrig/build# cmake..` completes successfully without any error or fail but,
> 
> Command `root@debian:~/xmrig/build# make` runs without error till `Scanning dependencies of target xmrig` but fails multiple times while `Building CXX object`. Errors are found in multiple CXX header files saying `error: missing binary operator before token "("`
> 
> [Heres the full log](https://github.com/xmrig/xmrig/files/6527437/log.txt).
> 
> What do I do?
> 
> **REQUEST:**
> **Could someone please share a precompiled arm64 build of xmrig?**

Above was debian for arm64

Below is alpine for aarch64 on qemu vm

> **_UPDATE_**
> 
> Compiling on Alpine for arm(aarch64):
> Fails while executing `make` yeilds the following [logs](https://github.com/xmrig/xmrig/files/6528224/log.txt).





## HimDek | 2021-05-23T15:12:15+00:00
Does your binary run directly on termux?

## ghost | 2021-05-23T15:20:25+00:00




> Does your binary run directly on termux?

yes i just run on pi 4 and termux

## HimDek | 2021-05-23T15:23:27+00:00
when i try to run in termux, it says `no such file or directory found`, even when xmrig is present in working directory.

**EDIT:**
logs:
```
~/xmrig-clang $ ls
config.json  xmrig
~/xmrig-clang $ ./xmrig -o rx.unmineable.com:3333 -k -a rx -u DOGE:D6PU16VQbx7akx1XrKLDKsgYRCv9vfFBYi.unmineable_miner_termux --http-port=60070
bash: ./xmrig: No such file or directory
```

## ghost | 2021-05-23T15:28:28+00:00
> when i try to run in termux, it says `no such file or directory found`, even when xmrig is present in working directory.

Upload ready static build try and let me know :)

## thosoo | 2021-05-25T08:31:49+00:00
> **_UPDATE_**
> 
> Compiling on Alpine for arm(aarch64):
> Fails while executing `make` yeilds the following [logs](https://github.com/xmrig/xmrig/files/6528224/log.txt).

```
localhost:~/xmrig/build# cmake .. -DXMRIG_DEPS=scripts/deps
```

what do you have in scripts/deps

## Spudz76 | 2021-05-25T11:32:17+00:00
```
localhost:~/xmrig/build# cmake .. -DXMRIG_DEPS=scripts/deps
```
That should be `../scripts/deps`

# Action History
- Created by: HimDek | 2021-05-23T02:45:31+00:00
