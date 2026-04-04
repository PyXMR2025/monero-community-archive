---
title: macOS Monterey (aarch64) Illegal Instruction
source_url: https://github.com/monero-project/monero-gui/issues/3782
author: sbehnke
assignees: []
labels: []
created_at: '2021-12-07T21:40:37+00:00'
updated_at: '2022-01-01T17:54:32+00:00'
type: issue
status: closed
closed_at: '2022-01-01T17:54:32+00:00'
---

# Original Description
If I download the macOS build in the Releases for v0.17.3.0 it crashes immediately upon launch with an illegal instruction exception. If I build the master branch with commit bddb9b0050ee086da5c7ee7fdb3627e0dff9f179 (HEAD -> master, tag: v0.17.3.0, origin/master, origin/HEAD) locally using Xcode 13.1 on macOS Monterey 12.0.1, everything works as expected. This is on a MacBook Pro 16 inch M1 Max. I've attached the crash log I get with the bundled version.

[CrashReport.txt](https://github.com/monero-project/monero-gui/files/7671748/CrashReport.txt)



# Discussion History
## selsta | 2021-12-07T21:52:07+00:00
Thanks for the report. I can reproduce but no idea yet what the issue is.

If someone else has this issue they can use v0.17.2.3 for now or compile manually: https://github.com/monero-project/monero-gui/releases/tag/v0.17.2.3

## surfaceflinger | 2021-12-09T17:59:10+00:00
Same thing is now happening on x86-64 builds from Arch Linux repos https://bugs.archlinux.org/task/72963

## selsta | 2021-12-09T18:03:32+00:00
@Morelcia does the binary from getmonero.org work on your system?

## selsta | 2021-12-09T18:11:05+00:00
I will check your linked commits @Morelcia, it seems that removing the generic x86-64 arch now makes it default to native arch.

I wanted to make it work for ARM but guess some extra work is required.

In the meantime it should work by adding `-D ARCH="default"` to CMake.

## surfaceflinger | 2021-12-09T18:11:06+00:00
Yeah, AppImage from getmonero.org works fine.
![Screenshot_2021-12-09_19-10-01](https://user-images.githubusercontent.com/44725111/145452132-60955aab-90dc-4bc0-9c98-a7f46f2208ac.png)


## kpcyrd | 2021-12-10T23:03:35+00:00
hi!

are there any official build instructions for  monero-gui? Arch Linux builds the project with:

```
  ARCH=default make release
```

back then `ARCH=default` was necessary to get binaries compatible with older cpus (see also the [PKGBUILD](https://github.com/archlinux/svntogit-community/blob/7e3f0a89d608b405815d9a98c9128374f8e242f1/trunk/PKGBUILD#L54) for the non-gui monero package)

## selsta | 2021-12-11T02:32:44+00:00
> are there any official build instructions for monero-gui?

We create the binaries for getmonero.org with the Dockerfile, but that's not relevant for Arch Linux.

Can you just add `ARCH=default` to GUI PKGBUILD too?

## kpcyrd | 2021-12-13T17:04:01+00:00
It's already there, the line is quoted is from the monero-gui PKGBUILD:

https://github.com/archlinux/svntogit-community/blob/85e74587018cd01d4486f019f2c9217334b56691/trunk/PKGBUILD#L56

## selsta | 2021-12-14T02:33:00+00:00
@kpcyrd Sorry, I'm confused now.

Someone reported that the Arch package requires AVX2 (https://bugs.archlinux.org/task/72963) since v0.17.3.0, but you said the PKGBUILD  already uses ARCH=default?

Can you try `ARCH="x86-64"` instead of `"default"`?

## kpcyrd | 2021-12-14T09:56:12+00:00
Yes, the way we build monero-gui didn't change between 0.17.2.3 -> 0.17.3.0 \[[diff](https://github.com/archlinux/svntogit-community/commit/a743119da12c2b463d68096db6b848412c4aaafc)\].

### monero-gui (with `ARCH=default`)

```
ARCH=default make release
```

```
% objdump -d usr/bin/monero-wallet-gui | rg -i VPBROADCASTQ
  2327d6:	c4 e2 7d 59 1d 41 93 	vpbroadcastq 0x11b9341(%rip),%ymm3        # 13ebb20 <_ZN6google8protobuf8internal26fixed_address_empty_stringB5cxx11E>
  38f766:	c4 e2 7d 59 c1       	vpbroadcastq %xmm1,%ymm0
  6cfd6d:	c4 e2 7d 59 c8       	vpbroadcastq %xmm0,%ymm1
  6f82df:	c4 e2 7d 59 05 38 38 	vpbroadcastq 0xcf3838(%rip),%ymm0        # 13ebb20 <_ZN6google8protobuf8internal26fixed_address_empty_stringB5cxx11E>
  6fa14f:	c4 e2 7d 59 05 c8 19 	vpbroadcastq 0xcf19c8(%rip),%ymm0        # 13ebb20 <_ZN6google8protobuf8internal26fixed_address_empty_stringB5cxx11E>
  6fa66f:	c4 e2 7d 59 05 a8 14 	vpbroadcastq 0xcf14a8(%rip),%ymm0        # 13ebb20 <_ZN6google8protobuf8internal26fixed_address_empty_stringB5cxx11E>
  6faeff:	c4 e2 7d 59 05 18 0c 	vpbroadcastq 0xcf0c18(%rip),%ymm0        # 13ebb20 <_ZN6google8protobuf8internal26fixed_address_empty_stringB5cxx11E>
  6fb92f:	c4 e2 7d 59 05 e8 01 	vpbroadcastq 0xcf01e8(%rip),%ymm0        # 13ebb20 <_ZN6google8protobuf8internal26fixed_address_empty_stringB5cxx11E>
  6fbb3f:	c4 e2 7d 59 05 d8 ff 	vpbroadcastq 0xceffd8(%rip),%ymm0        # 13ebb20 <_ZN6google8protobuf8internal26fixed_address_empty_stringB5cxx11E>
  7c54b0:	c4 e2 7d 59 c8       	vpbroadcastq %xmm0,%ymm1
  7c5555:	c4 e2 7d 59 c8       	vpbroadcastq %xmm0,%ymm1
  7c55fe:	c4 e2 7d 59 c8       	vpbroadcastq %xmm0,%ymm1
  7c56e0:	c4 e2 7d 59 c3       	vpbroadcastq %xmm3,%ymm0
```
### monero-gui (with `ARCH="x86-64"`)

```
ARCH="x86-64" make release
```

```
% objdump -d usr/bin/monero-wallet-gui | rg -i VPBROADCASTQ
  2327d6:	c4 e2 7d 59 1d 41 93 	vpbroadcastq 0x11b9341(%rip),%ymm3        # 13ebb20 <_ZN6google8protobuf8internal26fixed_address_empty_stringB5cxx11E>
  38f766:	c4 e2 7d 59 c1       	vpbroadcastq %xmm1,%ymm0
  6cfd6d:	c4 e2 7d 59 c8       	vpbroadcastq %xmm0,%ymm1
  6f82df:	c4 e2 7d 59 05 38 38 	vpbroadcastq 0xcf3838(%rip),%ymm0        # 13ebb20 <_ZN6google8protobuf8internal26fixed_address_empty_stringB5cxx11E>
  6fa14f:	c4 e2 7d 59 05 c8 19 	vpbroadcastq 0xcf19c8(%rip),%ymm0        # 13ebb20 <_ZN6google8protobuf8internal26fixed_address_empty_stringB5cxx11E>
  6fa66f:	c4 e2 7d 59 05 a8 14 	vpbroadcastq 0xcf14a8(%rip),%ymm0        # 13ebb20 <_ZN6google8protobuf8internal26fixed_address_empty_stringB5cxx11E>
  6faeff:	c4 e2 7d 59 05 18 0c 	vpbroadcastq 0xcf0c18(%rip),%ymm0        # 13ebb20 <_ZN6google8protobuf8internal26fixed_address_empty_stringB5cxx11E>
  6fb92f:	c4 e2 7d 59 05 e8 01 	vpbroadcastq 0xcf01e8(%rip),%ymm0        # 13ebb20 <_ZN6google8protobuf8internal26fixed_address_empty_stringB5cxx11E>
  6fbb3f:	c4 e2 7d 59 05 d8 ff 	vpbroadcastq 0xceffd8(%rip),%ymm0        # 13ebb20 <_ZN6google8protobuf8internal26fixed_address_empty_stringB5cxx11E>
  7c54b0:	c4 e2 7d 59 c8       	vpbroadcastq %xmm0,%ymm1
  7c5555:	c4 e2 7d 59 c8       	vpbroadcastq %xmm0,%ymm1
  7c55fe:	c4 e2 7d 59 c8       	vpbroadcastq %xmm0,%ymm1
  7c56e0:	c4 e2 7d 59 c3       	vpbroadcastq %xmm3,%ymm0
```

It seems this variables doesn't make any difference since the addresses are all the same too.

### monerod (as shipped by Arch Linux at the moment)
```
cmake -D BUILD_TESTS=ON -D CMAKE_BUILD_TYPE=release -D ARCH=default ../
make
```

```
% objdump -d usr/bin/monerod | rg -i VPBROADCASTQ
<nothing>
```
### monerod (without `-D ARCH=default`)
```
cmake -D BUILD_TESTS=ON -D CMAKE_BUILD_TYPE=release ../
make
```

```
% objdump -d usr/bin/monerod | rg -i VPBROADCASTQ
  608530:	c4 e2 7d 59 c8       	vpbroadcastq %xmm0,%ymm1
  6085d5:	c4 e2 7d 59 c8       	vpbroadcastq %xmm0,%ymm1
  60867e:	c4 e2 7d 59 c8       	vpbroadcastq %xmm0,%ymm1
  608760:	c4 e2 7d 59 c3       	vpbroadcastq %xmm3,%ymm0
  615430:	c4 e2 7d 59 e3       	vpbroadcastq %xmm3,%ymm4
```

## selsta | 2021-12-14T23:40:31+00:00
It just means that `ARCH` can't be set as an environment var but has to be set directly as a CMake arg, as you currently do it for `monerod`.

If setup correctly CMake should print something like

```
-- Building on x86_64 for default
```

You can use this for the monero-gui PKGBUILD

```
build() {
  cd "${pkgname}"
  mkdir -p build && cd build
  cmake -D CMAKE_BUILD_TYPE=Release -D ARCH=default ..
  make
}
```

## selsta | 2021-12-15T00:05:13+00:00
I updated the macOS build instructions in #3804, this issue will be resolved in v0.17.3.1 

## kpcyrd | 2021-12-15T09:21:08+00:00
@selsta thanks, I've used this to update the PKGBUILD and it's working:

```
% svn diff
Index: PKGBUILD
===================================================================
--- PKGBUILD	(revision 1065840)
+++ PKGBUILD	(working copy)
@@ -3,7 +3,7 @@
 pkgname=monero-gui
 pkgver=0.17.3.0
 _commit=bddb9b0050ee086da5c7ee7fdb3627e0dff9f179
-pkgrel=1
+pkgrel=2
 pkgdesc="QT GUI wallet for Monero: the secure, private, untraceable peer-to-peer currency"
 license=('BSD')
 arch=('x86_64')
@@ -53,12 +53,14 @@
 
 build() {
   cd "${pkgname}"
-  ARCH=default make release
+  mkdir -p build && cd build
+  cmake -D CMAKE_BUILD_TYPE=Release -D ARCH=default ../
+  make
 }
 
 package() {
   cd "${pkgname}"
-  install -Dm755 build/release/bin/monero-wallet-gui -t "${pkgdir}/usr/bin"
+  install -Dm755 build/bin/monero-wallet-gui -t "${pkgdir}/usr/bin"
   install -Dm644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
 
   install -Dm644 ../monero-gui.desktop -t "${pkgdir}/usr/share/applications"
```

testing the binary:

```
% objdump -d usr/bin/monero-wallet-gui | rg -i VPBROADCASTQ
<nothing>
```

# Action History
- Created by: sbehnke | 2021-12-07T21:40:37+00:00
- Closed at: 2022-01-01T17:54:32+00:00
