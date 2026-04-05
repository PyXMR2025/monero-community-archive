---
title: XMRig 6.20.0 / Compiling for Win 11 ARM / Error when building openssl
source_url: https://github.com/xmrig/xmrig/issues/3326
author: FSOL-XDAG
assignees: []
labels: []
created_at: '2023-09-03T22:27:28+00:00'
updated_at: '2025-06-18T22:22:58+00:00'
type: issue
status: closed
closed_at: '2025-06-18T22:22:58+00:00'
---

# Original Description
Hi XMRig Team 💕

I've got some issue when trying to build XMRig inside Win 11 ARM (through M2 Mac / Parallels Desktop).

I follow theses recommandations : https://www.msys2.org/wiki/arm64/

This is what I've done inside clangarm64.exe : 

```
pacman -S mingw-w64-clang-aarch64-gcc-compat mingw-w64-clang-aarch64-cmake automake libtool autoconf git make
git clone https://github.com/xmrig/xmrig.git
mkdir xmrig/build && cd xmrig/scripts
./build_deps.sh
```

I get this : 
![Capture d’écran 2023-09-04 à 00 10 39](https://github.com/xmrig/xmrig/assets/128682335/d460a2ca-2300-47b9-a420-26f4f9512cde)

Here is the complete log : 

[build_deps log.txt](https://github.com/xmrig/xmrig/files/12507945/build_deps.log.txt)

Don't know what to do.


# Discussion History
## SChernykh | 2023-09-04T06:39:29+00:00
build_deps uses the default compiler which is gcc (for x64), and you should use `mingw-w64-clang-aarch64-clang`. This script wasn't designed for cross-compilation, I don't see any way to select the compiler there.

## FSOL-XDAG | 2023-09-04T07:23:38+00:00
Thanks for your reply.

I hope finding help [here](https://github.com/openssl/openssl/issues/21943).

## FSOL-XDAG | 2023-09-04T12:24:14+00:00
@SChernykh Please check [openssl dev reply](https://github.com/openssl/openssl/issues/21943#issuecomment-1705051355). 

He said "Cross-compilation is supported by openssl via the https://github.com/openssl/openssl/blob/master/INSTALL.md#cross-compile-prefix Configure option."

What is possible to do with this ?

## xmrig | 2025-06-18T22:22:58+00:00
#3668

# Action History
- Created by: FSOL-XDAG | 2023-09-03T22:27:28+00:00
- Closed at: 2025-06-18T22:22:58+00:00
