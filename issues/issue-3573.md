---
title: Mingw64 debug build error
source_url: https://github.com/monero-project/monero/issues/3573
author: Keksov
assignees: []
labels: []
created_at: '2018-04-06T18:26:33+00:00'
updated_at: '2018-06-25T22:32:59+00:00'
type: issue
status: closed
closed_at: '2018-06-25T22:32:59+00:00'
---

# Original Description
Still no luck with building debug version
```
debug-static-win64:
	mkdir -p build/debug
	cd build/debug && cmake -G "MSYS Makefiles" -D STATIC=ON -D ARCH="x86-64" -D BUILD_64=ON -D CMAKE_BUILD_TYPE=Debug -D BUILD_TAG="win-x64" -D CMAKE_TOOLCHAIN_FILE=../../cmake/64-bit-toolchain.cmake -D MSYS2_FOLDER=c:/msys64 ../.. && $(MAKE)
```
Make output (last lines)
```
[ 85%] Building CXX object src/wallet/CMakeFiles/obj_wallet.dir/wallet2.cpp.obj
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/7.3.0/../../../../x86_64-w64-mingw32/bin/as.exe: CMakeFiles/obj_wallet.dir/wallet2.cpp.obj: too many sections (42811)
C:\msys64\tmp\ccLcStfV.s: Assembler messages:
C:\msys64\tmp\ccLcStfV.s: Fatal error: can't write 55 bytes to section .text of CMakeFiles/obj_wallet.dir/wallet2.cpp.obj: 'File too big'
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/7.3.0/../../../../x86_64-w64-mingw32/bin/as.exe: CMakeFiles/obj_wallet.dir/wallet2.cpp.obj: too many sections (42811)
C:\msys64\tmp\ccLcStfV.s: Fatal error: can't close CMakeFiles/obj_wallet.dir/wallet2.cpp.obj: File too big
make[3]: *** [src/wallet/CMakeFiles/obj_wallet.dir/build.make:63: src/wallet/CMakeFiles/obj_wallet.dir/wallet2.cpp.obj] Error 1
make[3]: Leaving directory '/usr/src/monero/build/debug'
make[2]: *** [CMakeFiles/Makefile2:2230: src/wallet/CMakeFiles/obj_wallet.dir/all] Error 2
make[2]: Leaving directory '/usr/src/monero/build/debug'
make[1]: *** [Makefile:129: all] Error 2
make[1]: Leaving directory '/usr/src/monero/build/debug'
make: *** [Makefile:115: debug-static-win64] Error 2
```


# Discussion History
## moneromooo-monero | 2018-04-06T19:46:42+00:00
Try with PR #3490.

## Keksov | 2018-04-07T06:57:29+00:00
Fixed! Just building couple of hours on my i5 and now I have nice monerod.exe of 319Mb in size... ))

## moneromooo-monero | 2018-06-25T22:00:30+00:00
+resolved

# Action History
- Created by: Keksov | 2018-04-06T18:26:33+00:00
- Closed at: 2018-06-25T22:32:59+00:00
