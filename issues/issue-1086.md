---
title: Windows MINGW32 compile crash
source_url: https://github.com/monero-project/monero-gui/issues/1086
author: SpliffyMap
assignees: []
labels:
- resolved
created_at: '2018-01-20T14:51:10+00:00'
updated_at: '2019-04-23T18:54:40+00:00'
type: issue
status: closed
closed_at: '2019-04-23T18:54:40+00:00'
---

# Original Description
I'm getting this error message, what is wrong with readline?
![readline](https://user-images.githubusercontent.com/35120072/35184737-18414798-fe02-11e7-999e-7f74396f29be.png)

ALSO:
CMake Error at CMakeLists.txt:817 (message):
  Could not find required header zmq.hpp

# Discussion History
## SpliffyMap | 2018-01-20T16:09:50+00:00
![depen](https://user-images.githubusercontent.com/35120072/35185431-18cf111c-fe0d-11e7-9e31-1f3d8240fadb.png)


## danrmiller | 2018-01-20T18:26:38+00:00
For the zmq message you need this file: https://github.com/zeromq/cppzmq/blob/master/zmq.hpp
It may also be included in a msys package with a name like cppzmq.

## UsFantom | 2018-01-21T04:24:13+00:00
I can't build this project in msys2.
I have an error in compiling epee.
"not found <sys/select.h>" 
Could you please tell me where the this file is? And how to import this file in this project.

And link error occured.
![image](https://user-images.githubusercontent.com/35334661/35190815-866441da-fe9d-11e7-9c6f-3c51a097f665.png)
undefined reference is main error!
Please help me.

## SpliffyMap | 2018-01-21T09:45:07+00:00
Thank you @danrmiller , I added zmq.hpp and it's building almost till the end, but I got this message
![errormess](https://user-images.githubusercontent.com/35120072/35192750-81abda1a-fea0-11e7-9d5d-feca341881e7.png)

## SpliffyMap | 2018-01-21T10:14:27+00:00
Looks  like as @KiPa-SuJi  mention before, something wrong with sys/select.h
![epeee](https://user-images.githubusercontent.com/35120072/35192988-8ea7068c-fea4-11e7-8542-f94fbfbbc03f.png)


## dEBRUYNE-1 | 2018-01-21T10:26:25+00:00
@SpliffyMap - Try to apply this PR:

https://github.com/monero-project/monero/pull/3155/files

As it's only one line, you can easily apply it locally. 

## SpliffyMap | 2018-01-21T10:52:29+00:00
Thanks @dEBRUYNE-1, by removing this line, error gone. Only left this one

`/i686-w64-mingw32/bin/ld.exe: cannot find -lwallet_merged
collect2.exe: error: ld returned 1 exit status`


## SpliffyMap | 2018-01-21T14:26:08+00:00
I think thats because of this error:
`CMakeFiles/wallet_rpc_server.dir/objects.a(wallet_rpc_server.cpp.obj):wallet_rpc_server.cpp:(.text$_ZN5boost16re_detail_10620012perl_matcherIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEESaINS_9sub_matchISC_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE8find_impEv[__ZN5boost16re_detail_10620012perl_matcherIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEESaINS_9sub_matchISC_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE8find_impEv]+0x293): undefined reference to `boost::re_detail_106200::put_mem_block(void*)'
collect2.exe: error: ld returned 1 exit status
src/wallet/CMakeFiles/wallet_rpc_server.dir/build.make:126: recipe for target 'bin/monero-wallet-rpc.exe' failed
mingw32-make[2]: *** [bin/monero-wallet-rpc.exe] Error 1`

I tried Boost boost_1_64_0 ( https://github.com/monero-project/monero-gui/pull/828 ) 
Same error :-1: 

## SpliffyMap | 2018-01-21T16:19:37+00:00
But before, even when I updated library to boost 1.64, compiler says:
`-- Found Boost Version: 106200`

So I removed mingw-w64-i686-boost, and now this error is gone, and compiler says:
`-- Found Boost Version: 106400`

And compiled this time even more code, but at the end still get some strange errors.
![strange](https://user-images.githubusercontent.com/35120072/35196192-888cf24c-fed7-11e7-9ac1-4cae85c38355.png)

`C:/msys64/home/Dredas/monero-gui/monero/lib/libepee.a(wipeable_string.cpp.obj):wipeable_string.cpp:(.text+0x1556): undefined reference to `__stack_chk_guard'
C:/msys64/home/Dredas/monero-gui/monero/lib/libepee.a(wipeable_string.cpp.obj):wipeable_string.cpp:(.text+0x15af): undefined reference to `__stack_chk_guard'
C:/msys64/home/Dredas/monero-gui/monero/lib/libepee.a(wipeable_string.cpp.obj):wipeable_string.cpp:(.text+0x1c4f): undefined reference to `__stack_chk_fail'
collect2.exe: error: ld returned 1 exit status
make[1]: *** [Makefile.Release:188: release/bin/monero-wallet-gui.exe] Error 1
`

## SpliffyMap | 2018-01-21T20:13:52+00:00
Also tried "pacman -Syuu" with no success, only different errors. Can anyone explain me why it is impossible to build gui wallet for Windows using these steps https://github.com/monero-project/monero-gui/blob/master/README.md#on-windows ? 

At this point I changed 2 things. Added zmq.hpp and removed "sys/select.h" line. Still cannot find -lwallet_merged collect2.exe, and that's I think so because of boost error. If changing version, I got other error (last image).

Are we need to change something in instruction or nobody can build it for windows (32 or 64 bit) at this point of development?

## iDunk5400 | 2018-01-21T21:42:05+00:00
It's because monero-gui is not compatible yet with hardening changes from monero-project/monero#2993

## SpliffyMap | 2018-01-22T07:11:35+00:00
So it's a new bug ☺ I need to find somehow how to fix it ☺ 

## UsFantom | 2018-01-22T08:06:59+00:00
thank you!
Please help me!

On Mon, Jan 22, 2018 at 2:11 PM, SpliffyMap <notifications@github.com>
wrote:

> So it's a new bug ☺ I need to find somehow how to fix it ☺
>
> —
> You are receiving this because you were mentioned.
> Reply to this email directly, view it on GitHub
> <https://github.com/monero-project/monero-gui/issues/1086#issuecomment-359341997>,
> or mute the thread
> <https://github.com/notifications/unsubscribe-auth/AhsqBcb3w5gPN7VJFwh1z7VQAsTmhgA_ks5tNDSpgaJpZM4RldnM>
> .
>


## SpliffyMap | 2018-01-22T13:42:33+00:00
In my opinion that's because of fstack-protector. But I'm not a architecture of this code, so don't know how we must fix it. It depends on why and how are we using it. Maybe we can add exception for windows 34 bit, or maybe we need to deal with it differently. 

## rbrunner7 | 2018-02-06T19:50:46+00:00
I have a similar problem right now that might also be caused by that "hardening", the linker exits with two symbols not found when trying to link `monero-wallet-gui.exe`:

``F:/msys64/home/br/monero-gui/monero/lib/libwallet_merged.a(wallet_manager.cpp.obj):wallet_manager.cpp:(.text+0x29c): undefined reference to `__stack_chk_fail'
``
and

``F:/msys64/home/br/monero-gui/monero/lib/libwallet_merged.a(wallet.cpp.obj):wallet.cpp:(.rdata$.refptr.__stack_chk_guard[.refptr.__stack_chk_guard]+0x0): undefined reference to `__stack_chk_guard'``

Any idea how to solve that?

## UsFantom | 2018-02-07T02:26:43+00:00
Sorry, I have no solution, if you have solved it, please tell me the result.
thanks.

On Wed, Feb 7, 2018 at 2:50 AM, René Brunner <notifications@github.com>
wrote:

> I have a similar problem right now that might also be caused by that
> "hardening", the linker exits with two symbols not found when trying to
> link monero-wallet-gui.exe:
>
> F:/msys64/home/br/monero-gui/monero/lib/libwallet_merged.a(
> wallet_manager.cpp.obj):wallet_manager.cpp:(.text+0x29c): undefined
> reference to `__stack_chk_fail'
> and
>
> F:/msys64/home/br/monero-gui/monero/lib/libwallet_merged.a(
> wallet.cpp.obj):wallet.cpp:(.rdata$.refptr.__stack_chk_
> guard[.refptr.__stack_chk_guard]+0x0): undefined reference to
> `__stack_chk_guard'
>
> Any idea how to solve that?
>
> —
> You are receiving this because you were mentioned.
> Reply to this email directly, view it on GitHub
> <https://github.com/monero-project/monero-gui/issues/1086#issuecomment-363543877>,
> or mute the thread
> <https://github.com/notifications/unsubscribe-auth/AhsqBU8-U7il83sZg-xDl9qNS9nNeGPnks5tSK0ZgaJpZM4RldnM>
> .
>


## glv2 | 2018-02-07T14:45:17+00:00
@rbrunner7, @KiPa-SuJi, Could you check if the following patch solves the ```undefined reference to `__stack_chk_guard'``` problem? (I don't have a Windows machine to test it right now).

```
diff --git a/monero-wallet-gui.pro b/monero-wallet-gui.pro
index 578ad0e..48318a6 100644
--- a/monero-wallet-gui.pro
+++ b/monero-wallet-gui.pro
@@ -5,6 +5,8 @@ QT += qml quick widgets
 WALLET_ROOT=$$PWD/monero
 
 CONFIG += c++11
+QMAKE_CXXFLAGS += -fPIC -fstack-protector
+QMAKE_LFLAGS += -fstack-protector
 
 # cleaning "auto-generated" bitmonero directory on "make distclean"
 QMAKE_DISTCLEAN += -r $$WALLET_ROOT
```

## rbrunner7 | 2018-02-07T21:04:54+00:00
@glv2: Perfect, works. Many thanks!

Will you make this into a PR?

## UsFantom | 2018-02-08T06:01:50+00:00
Tell me about it in detail, thank you.

On Thu, Feb 8, 2018 at 4:04 AM, René Brunner <notifications@github.com>
wrote:

> @glv2 <https://github.com/glv2>: Perfect, works. Many thanks!
>
> Will you make this into a PR?
>
> —
> You are receiving this because you were mentioned.
> Reply to this email directly, view it on GitHub
> <https://github.com/monero-project/monero-gui/issues/1086#issuecomment-363910139>,
> or mute the thread
> <https://github.com/notifications/unsubscribe-auth/AhsqBcHzJ3GSfq3teTKe0JVnU_Atu2B4ks5tSg_5gaJpZM4RldnM>
> .
>


## rbrunner7 | 2018-02-08T07:20:43+00:00
There is a textual file `monero-wallet-gui.pro` that guides the compilation process and that needs some correction until the whole thing works again. You can add two lines to that file:

Locate the following line, it's nearly at the top of the file

` CONFIG += c++11`

And then add the following two lines below it:

```
QMAKE_CXXFLAGS += -fPIC -fstack-protector
QMAKE_LFLAGS += -fstack-protector
```

Those lines instruct the C++ compiler and the linker to care about "stack protection".

If your MSYS2 installation is ready in every other aspect, i.e. you have the right packages installed, have compiled Boost to get static libraries, etc., with that change you will be able to successfully build.

## UsFantom | 2018-02-08T19:43:54+00:00
Thank you very much.


On Thu, Feb 8, 2018 at 2:20 PM, René Brunner <notifications@github.com>
wrote:

> There is a textual file monero-wallet-gui.pro that guides the compilation
> process and that needs some correction until the whole thing works again.
> You can add two lines to that file:
>
> Locate the following line, it's nearly at the top of the file
>
> CONFIG += c++11
>
> And then add the following two lines below it:
>
> QMAKE_CXXFLAGS += -fPIC -fstack-protector
> QMAKE_LFLAGS += -fstack-protector
>
> Those lines instruct the C++ compiler and the linker to care about "stack
> protection".
>
> If your MSYS2 installation is ready in every other aspect, i.e. you have
> the right packages installed, have compiled Boost to get static libraries,
> etc., with that change you will be able to successfully build.
>
> —
> You are receiving this because you were mentioned.
> Reply to this email directly, view it on GitHub
> <https://github.com/monero-project/monero-gui/issues/1086#issuecomment-364023889>,
> or mute the thread
> <https://github.com/notifications/unsubscribe-auth/AhsqBZ0zuIzENAk9nFZ9bX1mJfzVozl2ks5tSqBOgaJpZM4RldnM>
> .
>


## mesouug | 2018-03-11T09:04:42+00:00
@rbrunner7 Can you please share more details on dependencies that you've installed in order to build GUI.
I've followed README and installed all dependencies. I've tried various boost versions: 1.63, 1.64, 1.66. I've tried to install them to both MINGW32 and MINGW64 or each one is separate. I've tried to put boost to /mingw32/boost compiled in MINGW64 and to put it to /mingw64/boost compiled in MINGW32 and backwards. I think I've tried all possible combinations. I've tried to use boost provided from PACMAN. I've tried Windows 10 x64 and Windows 10 x32 and I was able just to build monero but not GUI. I've tried to compile previous release and master branch. Each time new error.
So my question is following:
1. In which env I should build monero-gui: (mingw64 or mingw32)?
2. In which env I should compile boost?
3. Do I need to have boost for both env's?
4. What else is missing in README as dependency?

## rbrunner7 | 2018-03-11T09:57:47+00:00
@mesouug: I was successful by only using 64bit: MinGW64 on Windows 7, X64, although the ReadMe of course still describes the way to do a 32bit build - should probably be updated, IMO.

I found that it did not work for me with the MSYS2 Boost package that pacman would install, I really needed to compile Boost myself. I went for 1.63 as per ReadMe and it worked.

I installed Qt5 with pacman, 64bit of course i.e. `mingw-w64-x86_64-qt5` and dependent stuff that comes along automatically.

For the Windows non-ASCII filenames stuff that I was working on I also have ICU installed: `mingw-w64-x86_64-icu`



## mesouug | 2018-03-11T10:16:48+00:00
@rbrunner7 Are you able to build latest commit or specific one?
Thank you for the hint. I've used QT5 from qt.io. I will try to build using pacman's.

## rbrunner7 | 2018-03-11T10:33:44+00:00
@mesouug: I am on the latest, i.e.  #1113. 

## mesouug | 2018-03-11T15:46:28+00:00
@rbrunner7 
Can you please add `set -x` at beginning of `get_libwallet_api.sh` script so it will show where it's looking for boost:
```
+ echo 'Configuring build for MINGW64..'
Configuring build for MINGW64..
+ BOOST_ROOT=/mingw64/boost
+ cmake -D CMAKE_BUILD_TYPE=Release -D STATIC=ON -D BOOST_ROOT=/mingw64/boost -D ARCH=x86-64 -D BUILD_GUI_DEPS=ON -D INSTALL_VENDORED_LIBUNBOUND=ON -D CMAKE_INSTALL_PREFIX=/home/redhat/monero-gui/monero -G 'MSYS Makefiles' ../..
```
I'm always getting this error:
<details>
<summary>Click to expand</summary>
CMake Warning at C:/msys64/mingw64/share/cmake-3.10/Modules/FindBoost.cmake:567 (message):
  Imported targets and dependency information not available for Boost version
  (all versions older than 1.33)
Call Stack (most recent call first):
  C:/msys64/mingw64/share/cmake-3.10/Modules/FindBoost.cmake:907 (_Boost_COMPONENT_DEPENDENCIES)
  C:/msys64/mingw64/share/cmake-3.10/Modules/FindBoost.cmake:1542 (_Boost_MISSING_DEPENDENCIES)
  CMakeLists.txt:786 (find_package)


CMake Warning at C:/msys64/mingw64/share/cmake-3.10/Modules/FindBoost.cmake:567 (message):
  Imported targets and dependency information not available for Boost version
  (all versions older than 1.33)
Call Stack (most recent call first):
  C:/msys64/mingw64/share/cmake-3.10/Modules/FindBoost.cmake:907 (_Boost_COMPONENT_DEPENDENCIES)
  C:/msys64/mingw64/share/cmake-3.10/Modules/FindBoost.cmake:1542 (_Boost_MISSING_DEPENDENCIES)
  CMakeLists.txt:786 (find_package)


CMake Warning at C:/msys64/mingw64/share/cmake-3.10/Modules/FindBoost.cmake:567 (message):
  Imported targets and dependency information not available for Boost version
  (all versions older than 1.33)
Call Stack (most recent call first):
  C:/msys64/mingw64/share/cmake-3.10/Modules/FindBoost.cmake:907 (_Boost_COMPONENT_DEPENDENCIES)
  C:/msys64/mingw64/share/cmake-3.10/Modules/FindBoost.cmake:1542 (_Boost_MISSING_DEPENDENCIES)
  CMakeLists.txt:786 (find_package)


CMake Warning at C:/msys64/mingw64/share/cmake-3.10/Modules/FindBoost.cmake:567 (message):
  Imported targets and dependency information not available for Boost version
  (all versions older than 1.33)
Call Stack (most recent call first):
  C:/msys64/mingw64/share/cmake-3.10/Modules/FindBoost.cmake:907 (_Boost_COMPONENT_DEPENDENCIES)
  C:/msys64/mingw64/share/cmake-3.10/Modules/FindBoost.cmake:1542 (_Boost_MISSING_DEPENDENCIES)
  CMakeLists.txt:786 (find_package)


CMake Warning at C:/msys64/mingw64/share/cmake-3.10/Modules/FindBoost.cmake:567 (message):
  Imported targets and dependency information not available for Boost version
  (all versions older than 1.33)
Call Stack (most recent call first):
  C:/msys64/mingw64/share/cmake-3.10/Modules/FindBoost.cmake:907 (_Boost_COMPONENT_DEPENDENCIES)
  C:/msys64/mingw64/share/cmake-3.10/Modules/FindBoost.cmake:1542 (_Boost_MISSING_DEPENDENCIES)
  CMakeLists.txt:786 (find_package)


CMake Warning at C:/msys64/mingw64/share/cmake-3.10/Modules/FindBoost.cmake:567 (message):
  Imported targets and dependency information not available for Boost version
  (all versions older than 1.33)
Call Stack (most recent call first):
  C:/msys64/mingw64/share/cmake-3.10/Modules/FindBoost.cmake:907 (_Boost_COMPONENT_DEPENDENCIES)
  C:/msys64/mingw64/share/cmake-3.10/Modules/FindBoost.cmake:1542 (_Boost_MISSING_DEPENDENCIES)
  CMakeLists.txt:786 (find_package)


CMake Warning at C:/msys64/mingw64/share/cmake-3.10/Modules/FindBoost.cmake:567 (message):
  Imported targets and dependency information not available for Boost version
  (all versions older than 1.33)
Call Stack (most recent call first):
  C:/msys64/mingw64/share/cmake-3.10/Modules/FindBoost.cmake:907 (_Boost_COMPONENT_DEPENDENCIES)
  C:/msys64/mingw64/share/cmake-3.10/Modules/FindBoost.cmake:1542 (_Boost_MISSING_DEPENDENCIES)
  CMakeLists.txt:786 (find_package)


CMake Warning at C:/msys64/mingw64/share/cmake-3.10/Modules/FindBoost.cmake:567 (message):
  Imported targets and dependency information not available for Boost version
  (all versions older than 1.33)
Call Stack (most recent call first):
  C:/msys64/mingw64/share/cmake-3.10/Modules/FindBoost.cmake:907 (_Boost_COMPONENT_DEPENDENCIES)
  C:/msys64/mingw64/share/cmake-3.10/Modules/FindBoost.cmake:1542 (_Boost_MISSING_DEPENDENCIES)
  CMakeLists.txt:786 (find_package)


CMake Warning at C:/msys64/mingw64/share/cmake-3.10/Modules/FindBoost.cmake:567 (message):
  Imported targets and dependency information not available for Boost version
  (all versions older than 1.33)
Call Stack (most recent call first):
  C:/msys64/mingw64/share/cmake-3.10/Modules/FindBoost.cmake:907 (_Boost_COMPONENT_DEPENDENCIES)
  C:/msys64/mingw64/share/cmake-3.10/Modules/FindBoost.cmake:1542 (_Boost_MISSING_DEPENDENCIES)
  CMakeLists.txt:786 (find_package)


CMake Error at C:/msys64/mingw64/share/cmake-3.10/Modules/FindBoost.cmake:1928 (message):
  Unable to find the requested Boost libraries.

  Unable to find the Boost header files.  Please set BOOST_ROOT to the root
  directory containing Boost or BOOST_INCLUDEDIR to the directory containing
  Boost's headers.
Call Stack (most recent call first):
  CMakeLists.txt:786 (find_package)


CMake Error at CMakeLists.txt:56 (message):
  Could not find Boost libraries, please make sure you have installed Boost
  or libboost-all-dev (1.58) or the equivalent
Call Stack (most recent call first):
  CMakeLists.txt:790 (die)
</details>

## mesouug | 2018-03-12T14:17:03+00:00
If I compile boost 1.63 from manual with prefix `/mingw64/boost` it starts to complain that boost is incompatible.
```
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/7.3.0/../../../../x86_64-w64-mingw32/bin/ld.exe: cannot find -lwallet_merged
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/7.3.0/../../../../x86_64-w64-mingw32/bin/ld.exe: skipping incompatible c:/msys64/mingw64/boost/lib\libboost_serialization-mt-s.a when searching for -lboost_serialization-mt-s
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/7.3.0/../../../../x86_64-w64-mingw32/bin/ld.exe: skipping incompatible C:/msys64/mingw64/boost/lib\libboost_serialization-mt-s.a when searching for -lboost_serialization-mt-s
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/7.3.0/../../../../x86_64-w64-mingw32/bin/ld.exe: cannot find -lboost_serialization-mt-s
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/7.3.0/../../../../x86_64-w64-mingw32/bin/ld.exe: skipping incompatible c:/msys64/mingw64/boost/lib\libboost_thread-mt-s.a when searching for -lboost_thread-mt-s
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/7.3.0/../../../../x86_64-w64-mingw32/bin/ld.exe: skipping incompatible C:/msys64/mingw64/boost/lib\libboost_thread-mt-s.a when searching for -lboost_thread-mt-s
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/7.3.0/../../../../x86_64-w64-mingw32/bin/ld.exe: cannot find -lboost_thread-mt-s
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/7.3.0/../../../../x86_64-w64-mingw32/bin/ld.exe: skipping incompatible c:/msys64/mingw64/boost/lib\libboost_system-mt-s.a when searching for -lboost_system-mt-s
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/7.3.0/../../../../x86_64-w64-mingw32/bin/ld.exe: skipping incompatible C:/msys64/mingw64/boost/lib\libboost_system-mt-s.a when searching for -lboost_system-mt-s
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/7.3.0/../../../../x86_64-w64-mingw32/bin/ld.exe: cannot find -lboost_system-mt-s
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/7.3.0/../../../../x86_64-w64-mingw32/bin/ld.exe: skipping incompatible c:/msys64/mingw64/boost/lib\libboost_date_time-mt-s.a when searching for -lboost_date_time-mt-s
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/7.3.0/../../../../x86_64-w64-mingw32/bin/ld.exe: skipping incompatible C:/msys64/mingw64/boost/lib\libboost_date_time-mt-s.a when searching for -lboost_date_time-mt-s
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/7.3.0/../../../../x86_64-w64-mingw32/bin/ld.exe: cannot find -lboost_date_time-mt-s
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/7.3.0/../../../../x86_64-w64-mingw32/bin/ld.exe: skipping incompatible c:/msys64/mingw64/boost/lib\libboost_filesystem-mt-s.a when searching for -lboost_filesystem-mt-s
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/7.3.0/../../../../x86_64-w64-mingw32/bin/ld.exe: skipping incompatible C:/msys64/mingw64/boost/lib\libboost_filesystem-mt-s.a when searching for -lboost_filesystem-mt-s
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/7.3.0/../../../../x86_64-w64-mingw32/bin/ld.exe: cannot find -lboost_filesystem-mt-s
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/7.3.0/../../../../x86_64-w64-mingw32/bin/ld.exe: skipping incompatible c:/msys64/mingw64/boost/lib\libboost_regex-mt-s.a when searching for -lboost_regex-mt-s
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/7.3.0/../../../../x86_64-w64-mingw32/bin/ld.exe: skipping incompatible C:/msys64/mingw64/boost/lib\libboost_regex-mt-s.a when searching for -lboost_regex-mt-s
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/7.3.0/../../../../x86_64-w64-mingw32/bin/ld.exe: cannot find -lboost_regex-mt-s
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/7.3.0/../../../../x86_64-w64-mingw32/bin/ld.exe: skipping incompatible c:/msys64/mingw64/boost/lib\libboost_chrono-mt-s.a when searching for -lboost_chrono-mt-s
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/7.3.0/../../../../x86_64-w64-mingw32/bin/ld.exe: skipping incompatible C:/msys64/mingw64/boost/lib\libboost_chrono-mt-s.a when searching for -lboost_chrono-mt-s
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/7.3.0/../../../../x86_64-w64-mingw32/bin/ld.exe: cannot find -lboost_chrono-mt-s
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/7.3.0/../../../../x86_64-w64-mingw32/bin/ld.exe: skipping incompatible c:/msys64/mingw64/boost/lib\libboost_program_options-mt-s.a when searching for -lboost_program_options-mt-s
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/7.3.0/../../../../x86_64-w64-mingw32/bin/ld.exe: skipping incompatible C:/msys64/mingw64/boost/lib\libboost_program_options-mt-s.a when searching for -lboost_program_options-mt-s
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/7.3.0/../../../../x86_64-w64-mingw32/bin/ld.exe: cannot find -lboost_program_options-mt-s
collect2.exe: error: ld returned 1 exit status
make[1]: *** [Makefile.Release:203: release/bin/monero-wallet-gui.exe] Error 1
make[1]: Leaving directory '/home/redhat/monero-gui/build'
make: *** [Makefile:36: release] Error 2
+ exit
```

Did anyone faced similar issues?

## pazos | 2018-03-14T21:03:04+00:00
@mesouug: It seems that you're mixing 32 & 64 bits libraries. Did you use `address-model=64` when you built boost for 64 bits? 

The instructions on the README are for 32 bits. I wonder if we can replace those instructions and build 32 and 64 bits libraries at the same time with `address-model=32,64`. This would require to install both 32 and 64 bits toolchains

## mesouug | 2018-03-22T09:26:24+00:00
@pazos Thank you for this hint. MoneroD now builds but I'm getting following error:
```
g++ -fstack-protector -Wl,--stack,4194304 -Wl,--dynamicbase -Wl,--nxcompat -Wl,-s,--relax,--gc-sections -static -Wl,-subsystem,windows -mthreads -o release/bin/monero-wallet-gui.exe object_script.monero-wallet-gui.Release  -lglu32 -lopengl32 -luser32 -lmingw32 -LC:/msys64/mingw64/lib C:/msys64/mingw64/lib/libqtmain.a -lshell32 -LC:/msys64/home/redhat/monero-gui/monero/lib -lwallet_merged -lepee -lunbound -leasylogging -Lc:/msys64/mingw64/lib -L/mingw64/lib -Lc:/msys64/mingw64/boost/lib -L/mingw64/boost/lib -Wl,-Bstatic -lboost_serialization-mt-s -lboost_thread-mt-s -lboost_system-mt-s -lboost_date_time-mt-s -lboost_filesystem-mt-s -lboost_regex-mt-s -lboost_chrono-mt-s -lboost_program_options-mt-s -lboost_locale-mt-s -licuio -licuin -licuuc -licudt -licutu -liconv -lssl -lcrypto -Wl,-Bdynamic -lws2_32 -lwsock32 -lIphlpapi -lgdi32 C:/msys64/mingw64/lib/libQt5Quick.dll.a C:/msys64/mingw64/lib/libQt5Widgets.dll.a C:/msys64/mingw64/lib/libQt5Gui.dll.a C:/msys64/mingw64/lib/libQt5Qml.dll.a C:/msys64/mingw64/lib/libQt5Network.dll.a C:/msys64/mingw64/lib/libQt5Core.dll.a
C:/msys64/home/redhat/monero-gui/monero/lib\libwallet_merged.a(ringdb.cpp.obj):ringdb.cpp:(.text+0x3a3): undefined reference to `mdb_txn_abort'
C:/msys64/home/redhat/monero-gui/monero/lib\libwallet_merged.a(ringdb.cpp.obj):ringdb.cpp:(.text+0x3e3): undefined reference to `mdb_txn_abort'
C:/msys64/home/redhat/monero-gui/monero/lib\libwallet_merged.a(ringdb.cpp.obj):ringdb.cpp:(.text+0x423): undefined reference to `mdb_txn_abort'
C:/msys64/home/redhat/monero-gui/monero/lib\libwallet_merged.a(ringdb.cpp.obj):ringdb.cpp:(.text+0x463): undefined reference to `mdb_txn_abort'
C:/msys64/home/redhat/monero-gui/monero/lib\libwallet_merged.a(ringdb.cpp.obj):ringdb.cpp:(.text+0x4a3): undefined reference to `mdb_txn_abort'
C:/msys64/home/redhat/monero-gui/monero/lib\libwallet_merged.a(ringdb.cpp.obj):ringdb.cpp:(.text+0x4e3): more undefined references to `mdb_txn_abort' follow
C:/msys64/home/redhat/monero-gui/monero/lib\libwallet_merged.a(ringdb.cpp.obj):ringdb.cpp:(.text+0xbe4): undefined reference to `mdb_dbi_close'
C:/msys64/home/redhat/monero-gui/monero/lib\libwallet_merged.a(ringdb.cpp.obj):ringdb.cpp:(.text+0xbf0): undefined reference to `mdb_dbi_close'
C:/msys64/home/redhat/monero-gui/monero/lib\libwallet_merged.a(ringdb.cpp.obj):ringdb.cpp:(.text+0xbf9): undefined reference to `mdb_env_close'
C:/msys64/home/redhat/monero-gui/monero/lib\libwallet_merged.a(ringdb.cpp.obj):ringdb.cpp:(.text+0xc56): undefined reference to `mdb_env_info'
C:/msys64/home/redhat/monero-gui/monero/lib\libwallet_merged.a(ringdb.cpp.obj):ringdb.cpp:(.text+0xc8f): undefined reference to `mdb_env_stat'
C:/msys64/home/redhat/monero-gui/monero/lib\libwallet_merged.a(ringdb.cpp.obj):ringdb.cpp:(.text+0xd3d): undefined reference to `mdb_env_set_mapsize'
C:/msys64/home/redhat/monero-gui/monero/lib\libwallet_merged.a(ringdb.cpp.obj):ringdb.cpp:(.text+0x1159): undefined reference to `mdb_env_create'
C:/msys64/home/redhat/monero-gui/monero/lib\libwallet_merged.a(ringdb.cpp.obj):ringdb.cpp:(.text+0x1283): undefined reference to `mdb_strerror'
C:/msys64/home/redhat/monero-gui/monero/lib\libwallet_merged.a(ringdb.cpp.obj):ringdb.cpp:(.text+0x131a): undefined reference to `mdb_env_set_maxdbs'
C:/msys64/home/redhat/monero-gui/monero/lib\libwallet_merged.a(ringdb.cpp.obj):ringdb.cpp:(.text+0x1402): undefined reference to `mdb_strerror'
```

## rbrunner7 | 2018-03-22T17:54:59+00:00
@mesouug: I think you need to cherry-pick either PR #1187 or PR #1172 into the branch that you try to compile to solve this problem.

## alexws54tk | 2019-04-19T17:44:32+00:00
For Gentoo need `net-libs/cppzmq`.

## dEBRUYNE-1 | 2019-04-23T18:15:35+00:00
I am doing some housekeeping and closing all old build relates issues, as they are probably not relevant anymore.

## dEBRUYNE-1 | 2019-04-23T18:15:41+00:00
+resolved

# Action History
- Created by: SpliffyMap | 2018-01-20T14:51:10+00:00
- Closed at: 2019-04-23T18:54:40+00:00
