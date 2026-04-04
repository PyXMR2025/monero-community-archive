---
title: GUI build breaking on Windows 8.1 with mingw64
source_url: https://github.com/monero-project/monero-gui/issues/1559
author: cryptobarbossa
assignees: []
labels:
- resolved
created_at: '2018-09-14T16:10:33+00:00'
updated_at: '2018-12-17T08:36:29+00:00'
type: issue
status: closed
closed_at: '2018-12-17T08:36:29+00:00'
---

# Original Description
**Setup:**

- Windows 8.1 x64

- 8GB RAM 

- 100GB+ storage

- Boost 1.68.0-1

- QT 5.11.1-3


**Instructions followed:**

- Install MSYS2 64-bit and open mingw64

- run 'pacman -Syuu' then exit mingw64

- open mingw64 and run 'pacman -Syuu' again

- 'pacman -S mingw-w64-x86_64-toolchain make mingw-w64-x86_64-cmake mingw-w64-x86_64-boost mingw-w64-x86_64-openssl mingw-w64-x86_64-zeromq mingw-w64-x86_64-libsodium'

- 'pacman -S mingw-w64-x86_64-qt5'

- 'pacman -S git'

- git clone --recursive https://github.com/monero-project/monero-gui.git

- cd monero-gui

- ./build.sh

**_Following errors occurred whilst building:_**

Link to full [log](https://pastebin.com/xwxK0MVN)
`Bdynamic -lwinscard -lws2_32 -lwsock32 -lIphlpapi -lgdi32 C:/msys64/mingw64/lib/libQt5Quick.dll.a C:/msys64/mingw64/lib/libQt5Widgets.dll.a C:/msys64/mingw64/lib/libQt5Gui.dll.a C:/msys64/mingw64/lib/libQt5Qml.dll.a C:/msys64/mingw64/lib/libQt5Network.dll.a C:/msys64/mingw64/lib/libQt5Core.dll.a
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/8.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe: C:/msys64/home/lad/monero-gui/monero/lib/libwallet_merged.a(wallet.cpp.obj):wallet.cpp:(.text+0x4ee): undefined reference to `__stack_chk_fail'
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/8.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe: C:/msys64/home/lad/monero-gui/monero/lib/libwallet_merged.a(wallet.cpp.obj):wallet.cpp:(.text+0x55a): undefined reference to `__stack_chk_fail'
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/8.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe: C:/msys64/home/lad/monero-gui/monero/lib/libwallet_merged.a(wallet.cpp.obj):wallet.cpp:(.text+0x5be): undefined reference to `__stack_chk_fail'
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/8.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe: C:/msys64/home/lad/monero-gui/monero/lib/libwallet_merged.a(wallet.cpp.obj):wallet.cpp:(.text+0x62e): undefined reference to `__stack_chk_fail'
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/8.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe: C:/msys64/home/lad/monero-gui/monero/lib/libwallet_merged.a(wallet.cpp.obj):wallet.cpp:(.text+0x677): undefined reference to `__stack_chk_fail'
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/8.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe: C:/msys64/home/lad/monero-gui/monero/lib/libwallet_merged.a(wallet.cpp.obj):wallet.cpp:(.text+0x707): more undefined references to `__stack_chk_fail' follow
collect2.exe: error: ld returned 1 exit status
make[1]: *** [Makefile.Release:396: release/bin/monero-wallet-gui.exe] Error 1
make[1]: Leaving directory '/home/lad/monero-gui/build'
make: *** [Makefile:36: release] Error 2`


# Discussion History
## cryptobarbossa | 2018-09-14T21:38:05+00:00
Update....
Managed to compile the code. no errors. 

However,

When I try to run the monero daemon or GUI I get a `segmentation fault`

## BigslimVdub | 2018-09-15T02:47:13+00:00
how did you get this to compile? I have been unsuccessful 3 times now on 2 different systems on msys2 64 win10?
edit: literally identical fault:
https://paste.fedoraproject.org/paste/5y0DELxEPb~W7jJV6~a8CA

get_libwallet_api.sh runs and only compiles RPC and Daemon same as on aeon (https://github.com/aeonix/aeon-gui/issues/15) : 
https://paste.fedoraproject.org/paste/Wy1tCZHLYUWzKxJ4biGqyg




## rbrunner7 | 2018-09-19T16:20:31+00:00
@cryptobarbossa : I have the same problem, and I would be very interested how you managed to finally compile.

I wonder which recent code or make file change brought this problem with it.

## sanderfoobar | 2018-10-13T21:01:40+00:00
https://github.com/monero-project/monero-gui/tree/v0.13.0.2

The above (new) tag is known to compile correctly using `mingw-w64-x86_64-qt5-5.11.1-3-any.pkg.tar.xz`. Could you try this one and let us know?

## BigslimVdub | 2018-10-13T21:06:20+00:00
I will uninstall qt and reinstall that package when I am available. Probably tomorrow. I will let you know what happens 

## sanderfoobar | 2018-10-13T21:07:26+00:00
@Lafudoci was able to correctly build using specifically this mingw/qt version on Windows 10 64bit, using the [0.13.0.2 tag](https://github.com/monero-project/monero-gui/tree/v0.13.0.2).

## BigslimVdub | 2018-10-14T18:27:16+00:00
looks like Msys issue not finding the package anymore. 
I was building with 5.11.2-2 prior and uninstalled it. 

```

$ pacman -U mingw-w64-x86_64-qt5-5.11.1-3-any.pkg.tar.xz                     
   loading packages...
   error: 'mingw-w64-x86_64-qt5-5.11.1-3-any.pkg.tar.xz': could not find or read package
```

But I have downloaded the tar from their old repo -
 http://repo.msys2.org/mingw/x86_64/mingw-w64-x86_64-qt5-5.11.1-3-any.pkg.tar.xz 

## sanderfoobar | 2018-10-14T18:33:36+00:00
@BigslimVdub Let me know if that works. In addition, perhaps we (you) could also update the README, which contains `pacman -S mingw-w64-x86_64-qt5` - which does not work at this moment?

## BigslimVdub | 2018-10-14T18:36:39+00:00
ahh,, figured it out. SO I had to download the tar from their repo and then CD to that folder on Mingw64 and then run the install line `pacman -U mingw-w64-x86_64-qt5-5.11.1-3-any.pkg.tar.xz`

I will try to clone again and build after qt installs and see what happens. May have dependency issues though since all my other packages are up to date. 

edit: if this works for building I will pr the readme to include this. thanks

## rbrunner7 | 2018-10-14T19:17:09+00:00
@skftn, @BigslimVdub: That problem with the latest Qt version from MSYS2 package might be already over in only a few days when an update arrives from the MSYS2 people, so maybe it would be a little premature to change the ReadMe. And after all the latest-at-a-given-moment package worked for months now.

## BigslimVdub | 2018-10-14T20:10:22+00:00
Well tested with and without --recursive and both fail still at - 
```
make[1]: execvp: /C/msys64/mingw64/bin/qmlcachegen.exe: Bad address
make[1]: *** [Makefile.Release:1035: release/qmlcache_loader.cpp] Error 127
```
It seems it can't link anything together. I had the identical error on the latest QT package so I don't believe its QT package related. 

```
The only Cmake error I get is this : CMake Warning (dev) at C:/msys64/mingw64/share/cmake-3.12/Modules/CheckIncludeFile.cmake:70 (message):
  Policy CMP0075 is not set: Include file check macros honor
  CMAKE_REQUIRED_LIBRARIES.  Run "cmake --help-policy CMP0075" for policy
  details.  Use the cmake_policy command to set the policy and suppress this
  warning.

  CMAKE_REQUIRED_LIBRARIES is set to:

    iphlpapi;ws2_32

```
But I am unable to change policies in any way. Cmake_policy does not have an option in msys2 to edit the policy. 


## Lafudoci | 2018-10-15T01:46:33+00:00
>ahh,, figured it out. SO I had to download the tar from their repo and then CD to that folder on Mingw64 and then run the install line pacman -U mingw-w64-x86_64-qt5-5.11.1-3-any.pkg.tar.xz

@BigslimVdub this command will do the downgrade for you.
```
pacman -U http://repo.msys2.org/mingw/x86_64/mingw-w64-x86_64-qt5-5.11.1-3-any.pkg.tar.xz
```
or you'll like to remove current one before downgrade for avoiding some downgrade issue.
```
pacman -R mingw-w64-x86_64-qt5
```
Also make sure you qt is in default path, then the 5.11.2 issue should be good now.
```
$ qmake -v
QMake version 3.1
Using Qt version 5.11.1 in C:/msys64/mingw64/lib
```
But for the last qmlcachegen.exe issue, it's the same with my previous issue #1636, it's still unsolved on one of my machine.

## BigslimVdub | 2018-10-15T02:16:26+00:00
Ok I will wait for resolution on 1636 then

## stoffu | 2018-12-04T01:14:52+00:00
I've tested a few downgraded versions and found 5.10.0 to be the latest working one:

    pacman -U http://repo.msys2.org/mingw/x86_64/mingw-w64-x86_64-qt5-5.10.0-1-any.pkg.tar.xz

Edit: Looks like I have to manually copy libicu*58.dll due to the use of the old Qt version.


## mmbyday | 2018-12-07T19:30:06+00:00
fwiw, On windows, I've fixed

qmlcachegen.exe issues by deleting one file,

monero-gui/build/qml_qmlcache.qrc

then build.sh works as expected, again.


$ qmake -v                                                                       
QMake version 3.1                                                                
Using Qt version 5.11.1 in C:/msys64/mingw64/lib
--




## stoffu | 2018-12-10T04:52:58+00:00
I realized that the build with the latest version `mingw-w64-x86_64-qt5 5.11.2-3` succeeds by doing `make -C build` once the error was emitted. After further experimentation, I realized that the build succeeds also when I copied the entire contents of `build.sh` to the console manually. Even more simply, I found that

    source ./build.sh release-static

also succeeds. I find this workaround weird and ugly, but perhaps it's worth updating the build instruction in README?


## mmbyday | 2018-12-17T08:20:36+00:00
+resolved
by #1796

## dEBRUYNE-1 | 2018-12-17T08:32:23+00:00
+resolved

# Action History
- Created by: cryptobarbossa | 2018-09-14T16:10:33+00:00
- Closed at: 2018-12-17T08:36:29+00:00
