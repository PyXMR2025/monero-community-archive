---
title: '6.12.1: cmake install targed does not install anything'
source_url: https://github.com/xmrig/xmrig/issues/2371
author: kloczek
assignees: []
labels:
- question
created_at: '2021-05-12T20:10:35+00:00'
updated_at: '2022-04-03T14:39:48+00:00'
type: issue
status: closed
closed_at: '2022-04-03T14:39:48+00:00'
---

# Original Description
Looks like `install` targed oes not install anything
```console
$ /usr/bin/cmake --install x86_64-redhat-linux-gnu
-- Install configuration: "RelWithDebInfo"
$
```


# Discussion History
## Spudz76 | 2021-05-13T13:11:05+00:00
Correct.

## kloczek | 2021-05-13T13:13:00+00:00
Why?

## Spudz76 | 2021-05-13T13:21:04+00:00
Because to install you copy the resulting useful bits out of the `build/Release/` folder to where you want them.  There is no cmake install stub because copying a few files to where you want them doesn't need a convenience wrapper.

## kloczek | 2021-05-13T13:34:03+00:00
Moment so you want to say that you can decide where you want to install something on configure source tree using cmake without touching single file in configure source tree?
Just look on %cmake rpm macro used to build rpm packages on Linux:
```console
[tkloczko@barrel SPECS]$ rpm -E %cmake

CFLAGS="-O2 -g -grecord-gcc-switches -pipe -Wall -Werror=format-security -Wp,-D_FORTIFY_SOURCE=2 -Wp,-D_GLIBCXX_ASSERTIONS -specs=/usr/lib/rpm/redhat/redhat-hardened-cc1 -fstack-protector-strong -specs=/usr/lib/rpm/redhat/redhat-annobin-cc1 -m64 -mtune=generic -fasynchronous-unwind-tables -fstack-clash-protection -fcf-protection -fdata-sections -ffunction-sections -flto=auto -flto-partition=none";
CXXFLAGS="-O2 -g -grecord-gcc-switches -pipe -Wall -Werror=format-security -Wp,-D_FORTIFY_SOURCE=2 -Wp,-D_GLIBCXX_ASSERTIONS -specs=/usr/lib/rpm/redhat/redhat-hardened-cc1 -fstack-protector-strong -specs=/usr/lib/rpm/redhat/redhat-annobin-cc1 -m64 -mtune=generic -fasynchronous-unwind-tables -fstack-clash-protection -fcf-protection -fdata-sections -ffunction-sections -flto=auto -flto-partition=none";
FFLAGS="-O2 -g -grecord-gcc-switches -pipe -Wall -Werror=format-security -Wp,-D_FORTIFY_SOURCE=2 -Wp,-D_GLIBCXX_ASSERTIONS -specs=/usr/lib/rpm/redhat/redhat-hardened-cc1 -fstack-protector-strong -specs=/usr/lib/rpm/redhat/redhat-annobin-cc1 -m64 -mtune=generic -fasynchronous-unwind-tables -fstack-clash-protection -fcf-protection -fdata-sections -ffunction-sections -flto=auto -flto-partition=none -I/usr/lib64/gfortran/modules";
FCFLAGS="-O2 -g -grecord-gcc-switches -pipe -Wall -Werror=format-security -Wp,-D_FORTIFY_SOURCE=2 -Wp,-D_GLIBCXX_ASSERTIONS -specs=/usr/lib/rpm/redhat/redhat-hardened-cc1 -fstack-protector-strong -specs=/usr/lib/rpm/redhat/redhat-annobin-cc1 -m64 -mtune=generic -fasynchronous-unwind-tables -fstack-clash-protection -fcf-protection -fdata-sections -ffunction-sections -flto=auto -flto-partition=none -I/usr/lib64/gfortran/modules";
LDFLAGS="-Wl,-z,relro -Wl,--as-needed -Wl,--gc-sections -Wl,-z,now -specs=/usr/lib/rpm/redhat/redhat-hardened-ld -flto=auto -flto-partition=none -fuse-linker-plugin";
CC="/usr/bin/gcc"; CXX="/usr/bin/g++"; FC="/usr/bin/gfortran";
AR="/usr/bin/gcc-ar"; NM="/usr/bin/gcc-nm"; RANLIB="/usr/bin/gcc-ranlib";
export CFLAGS CXXFLAGS FFLAGS FCFLAGS LDFLAGS CC CXX FC AR NM RANLIB;

        /usr/bin/cmake \
        -B x86_64-redhat-linux-gnu \
        -D BUILD_SHARED_LIBS=ON \
        -D CMAKE_AR="$AR" \
        -D CMAKE_BUILD_TYPE=RelWithDebInfo \
        -D CMAKE_C_FLAGS_RELEASE="-DNDEBUG" \
        -D CMAKE_CXX_FLAGS_RELEASE="-DNDEBUG" \
        -D CMAKE_Fortran_FLAGS_RELEASE="-DNDEBUG" \
        -D CMAKE_INSTALL_PREFIX=/usr \
        -D CMAKE_NM="$NM" \
        -D CMAKE_RANLIB="$RANLIB" \
        -D CMAKE_VERBOSE_MAKEFILE=ON \
        -D DBUILD_SHARED_LIBS=ON \
        -D INCLUDE_INSTALL_DIR=/usr/include \
        -D LIB_INSTALL_DIR=/usr/lib64 \
%if "lib64" == "lib64"
        -D LIB_SUFFIX=64 \
%endif
        -D SHARE_INSTALL_PREFIX=/usr/share \
        -D SYSCONF_INSTALL_DIR=/etc \
        -S .
```
In other words as long as you will be using such standard variables `$(*_DIR)` variables you still would be able to install any class of siles where never you want .. but in CMakeLists.txt must be few `install()` lines. For now there is no even single one.


## SChernykh | 2021-05-13T13:44:26+00:00
There is no install script because there is no need for install script. Binary compiled -> add your config or command line -> ready to run.

## kloczek | 2021-05-13T14:16:21+00:00
Build framework is not only for building ands installing but testing just produced resources as well.
All under one hood without not obvious scripts.
it provides possibility to use use coverage, fuzzling and other code scanners, different types of optimisations like LTO and PGO.
If you want I can try to create a PR to add install target support.


# Action History
- Created by: kloczek | 2021-05-12T20:10:35+00:00
- Closed at: 2022-04-03T14:39:48+00:00
