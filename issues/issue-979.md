---
title: 'failed to build in Ubuntu 16.04 x64 ( fatal error: wallet/wallet2_api.h: No
  such file or directory compilation terminated.)'
source_url: https://github.com/monero-project/monero-gui/issues/979
author: charleshsu168
assignees: []
labels: []
created_at: '2017-11-29T18:18:50+00:00'
updated_at: '2017-12-10T22:07:00+00:00'
type: issue
status: closed
closed_at: '2017-12-10T22:07:00+00:00'
---

# Original Description
following the guide on how to compile from source, I got this fatal error, even after installed all the necessary dependencies:
~/monero-core$ sudo ./build.sh 
Building release
~/monero-core ~/monero-core
~/monero-core ~/monero-core
You are currently on commit bbf9b4b
The most recent tag was at 6f14fde
You are ahead of or behind a tagged release
D	include/INode.h
D	include/IWallet.h
libwallet_merged.a not found - Building libwallet
Building libwallet release
cleaning up existing monero build dir, libs and includes
~/monero-core/monero/build/release ~/monero-core ~/monero-core
Configuring build for Linux x64
-- The C compiler identification is GNU 5.4.0
-- The CXX compiler identification is GNU 5.4.0
-- Check for working C compiler: /usr/bin/cc
-- Check for working C compiler: /usr/bin/cc -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Detecting C compile features
-- Detecting C compile features - done
-- Check for working CXX compiler: /usr/bin/c++
-- Check for working CXX compiler: /usr/bin/c++ -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Building without build tag
-- Could not find DEVELOPER_LOCAL_TOOLS in env (not required)
-- BOOST_IGNORE_SYSTEM_PATHS defaults to OFF
-- Could not find DEVELOPER_LIBUNBOUND_OLD in env (not required)
-- Building for a 64-bit system
-- Building internal libraries as static
-- Could not find DATABASE in env (not required unless you want to change database type from default: lmdb)
-- Using LMDB as default DB type
-- Stack trace on exception enabled (using easylogging++)
-- Looking for pthread.h
-- Looking for pthread.h - found
-- Looking for pthread_create
-- Looking for pthread_create - not found
-- Check if compiler accepts -pthread
-- Check if compiler accepts -pthread - yes
-- Found Threads: TRUE  
-- Found OpenSSL: /usr/lib/x86_64-linux-gnu/libssl.so;/usr/lib/x86_64-linux-gnu/libcrypto.so (found version "1.0.2g") 
-- Using OpenSSL include dir at /usr/include
-- Could NOT find MiniUPnPc (missing:  MINIUPNP_INCLUDE_DIR MINIUPNP_LIBRARY) 
-- Using miniupnpc from local source tree (/external/miniupnpc)
-- Looking for libunbound
-- Found libunbound include (unbound.h) in /usr/include
-- Found libunbound shared library
-- Using 64-bit LMDB from source tree
-- Building on x86_64 for native
-- AES support enabled
-- Found Boost Version: 105800
-- Could NOT find Readline (missing:  Readline_INCLUDE_DIR Readline_LIBRARY) 
-- Performing Test GNU_READLINE_FOUND
-- Performing Test GNU_READLINE_FOUND - Failed
-- Could not find GNU readline library so building without readline support
-- Configuring incomplete, errors occurred!
See also "/home/chuck/monero-core/monero/build/release/CMakeFiles/CMakeOutput.log".
See also "/home/chuck/monero-core/monero/build/release/CMakeFiles/CMakeError.log".
make: Entering directory '/home/chuck/monero-core/monero'
cat version.sh >version 
chmod a+x version
make: Leaving directory '/home/chuck/monero-core/monero'
~/monero-core ~/monero-core
~/monero-core
make: Entering directory '/home/chuck/monero-core/monero/build/release/external/easylogging++'
make: Leaving directory '/home/chuck/monero-core/monero/build/release/external/easylogging++'
Installing libunbound...
make: Entering directory '/home/chuck/monero-core/src/zxcvbn-c'
make: Nothing to be done for 'all'.
make: Leaving directory '/home/chuck/monero-core/src/zxcvbn-c'
You are currently on commit bbf9b4b
The most recent tag was at 6f14fde
You are ahead of or behind a tagged release
~/monero-core/monero ~/monero-core ~/monero-core
You are currently on commit 9fad400
The most recent tag was at 793bc97
You are ahead of or behind a tagged release
~/monero-core ~/monero-core
/usr/lib/x86_64-linux-gnu/qt5/bin/lrelease -compress -nounfinished -removeidentical ../translations/monero-core.ts -qm /home/chuck/monero-core/build/release/bin/translations/monero-core.qm
Updating '/home/chuck/monero-core/build/release/bin/translations/monero-core.qm'...
Removing translations equal to source text in '/home/chuck/monero-core/build/release/bin/translations/monero-core.qm'...
    Generated 0 translation(s) (0 finished and 0 unfinished)
    Ignored 390 untranslated source text(s)
/usr/lib/x86_64-linux-gnu/qt5/bin/lrelease -compress -nounfinished -removeidentical ../translations/monero-core_ar.ts -qm /home/chuck/monero-core/build/release/bin/translations/monero-core_ar.qm
Updating '/home/chuck/monero-core/build/release/bin/translations/monero-core_ar.qm'...
Removing translations equal to source text in '/home/chuck/monero-core/build/release/bin/translations/monero-core_ar.qm'...
    Generated 0 translation(s) (0 finished and 0 unfinished)
    Ignored 390 untranslated source text(s)
/usr/lib/x86_64-linux-gnu/qt5/bin/lrelease -compress -nounfinished -removeidentical ../translations/monero-core_pt-br.ts -qm /home/chuck/monero-core/build/release/bin/translations/monero-core_pt-br.qm
Updating '/home/chuck/monero-core/build/release/bin/translations/monero-core_pt-br.qm'...
Removing translations equal to source text in '/home/chuck/monero-core/build/release/bin/translations/monero-core_pt-br.qm'...
    Generated 364 translation(s) (364 finished and 0 unfinished)
/usr/lib/x86_64-linux-gnu/qt5/bin/lrelease -compress -nounfinished -removeidentical ../translations/monero-core_de.ts -qm /home/chuck/monero-core/build/release/bin/translations/monero-core_de.qm
Updating '/home/chuck/monero-core/build/release/bin/translations/monero-core_de.qm'...
Removing translations equal to source text in '/home/chuck/monero-core/build/release/bin/translations/monero-core_de.qm'...
    Generated 314 translation(s) (314 finished and 0 unfinished)
    Ignored 49 untranslated source text(s)
/usr/lib/x86_64-linux-gnu/qt5/bin/lrelease -compress -nounfinished -removeidentical ../translations/monero-core_eo.ts -qm /home/chuck/monero-core/build/release/bin/translations/monero-core_eo.qm
Updating '/home/chuck/monero-core/build/release/bin/translations/monero-core_eo.qm'...
Removing translations equal to source text in '/home/chuck/monero-core/build/release/bin/translations/monero-core_eo.qm'...
    Generated 369 translation(s) (369 finished and 0 unfinished)
    Ignored 5 untranslated source text(s)
/usr/lib/x86_64-linux-gnu/qt5/bin/lrelease -compress -nounfinished -removeidentical ../translations/monero-core_es.ts -qm /home/chuck/monero-core/build/release/bin/translations/monero-core_es.qm
Updating '/home/chuck/monero-core/build/release/bin/translations/monero-core_es.qm'...
Removing translations equal to source text in '/home/chuck/monero-core/build/release/bin/translations/monero-core_es.qm'...
    Generated 328 translation(s) (328 finished and 0 unfinished)
    Ignored 22 untranslated source text(s)
/usr/lib/x86_64-linux-gnu/qt5/bin/lrelease -compress -nounfinished -removeidentical ../translations/monero-core_fi.ts -qm /home/chuck/monero-core/build/release/bin/translations/monero-core_fi.qm
Updating '/home/chuck/monero-core/build/release/bin/translations/monero-core_fi.qm'...
Removing translations equal to source text in '/home/chuck/monero-core/build/release/bin/translations/monero-core_fi.qm'...
    Generated 173 translation(s) (173 finished and 0 unfinished)
    Ignored 183 untranslated source text(s)
/usr/lib/x86_64-linux-gnu/qt5/bin/lrelease -compress -nounfinished -removeidentical ../translations/monero-core_fr.ts -qm /home/chuck/monero-core/build/release/bin/translations/monero-core_fr.qm
Updating '/home/chuck/monero-core/build/release/bin/translations/monero-core_fr.qm'...
Removing translations equal to source text in '/home/chuck/monero-core/build/release/bin/translations/monero-core_fr.qm'...
    Generated 352 translation(s) (352 finished and 0 unfinished)
/usr/lib/x86_64-linux-gnu/qt5/bin/lrelease -compress -nounfinished -removeidentical ../translations/monero-core_hr.ts -qm /home/chuck/monero-core/build/release/bin/translations/monero-core_hr.qm
Updating '/home/chuck/monero-core/build/release/bin/translations/monero-core_hr.qm'...
Removing translations equal to source text in '/home/chuck/monero-core/build/release/bin/translations/monero-core_hr.qm'...
    Generated 0 translation(s) (0 finished and 0 unfinished)
    Ignored 390 untranslated source text(s)
/usr/lib/x86_64-linux-gnu/qt5/bin/lrelease -compress -nounfinished -removeidentical ../translations/monero-core_id.ts -qm /home/chuck/monero-core/build/release/bin/translations/monero-core_id.qm
Updating '/home/chuck/monero-core/build/release/bin/translations/monero-core_id.qm'...
Removing translations equal to source text in '/home/chuck/monero-core/build/release/bin/translations/monero-core_id.qm'...
    Generated 342 translation(s) (342 finished and 0 unfinished)
    Ignored 24 untranslated source text(s)
/usr/lib/x86_64-linux-gnu/qt5/bin/lrelease -compress -nounfinished -removeidentical ../translations/monero-core_hi.ts -qm /home/chuck/monero-core/build/release/bin/translations/monero-core_hi.qm
Updating '/home/chuck/monero-core/build/release/bin/translations/monero-core_hi.qm'...
Removing translations equal to source text in '/home/chuck/monero-core/build/release/bin/translations/monero-core_hi.qm'...
    Generated 66 translation(s) (66 finished and 0 unfinished)
    Ignored 307 untranslated source text(s)
/usr/lib/x86_64-linux-gnu/qt5/bin/lrelease -compress -nounfinished -removeidentical ../translations/monero-core_it.ts -qm /home/chuck/monero-core/build/release/bin/translations/monero-core_it.qm
Updating '/home/chuck/monero-core/build/release/bin/translations/monero-core_it.qm'...
Removing translations equal to source text in '/home/chuck/monero-core/build/release/bin/translations/monero-core_it.qm'...
    Generated 364 translation(s) (364 finished and 0 unfinished)
/usr/lib/x86_64-linux-gnu/qt5/bin/lrelease -compress -nounfinished -removeidentical ../translations/monero-core_ja.ts -qm /home/chuck/monero-core/build/release/bin/translations/monero-core_ja.qm
Updating '/home/chuck/monero-core/build/release/bin/translations/monero-core_ja.qm'...
Removing translations equal to source text in '/home/chuck/monero-core/build/release/bin/translations/monero-core_ja.qm'...
    Generated 376 translation(s) (376 finished and 0 unfinished)
/usr/lib/x86_64-linux-gnu/qt5/bin/lrelease -compress -nounfinished -removeidentical ../translations/monero-core_nl.ts -qm /home/chuck/monero-core/build/release/bin/translations/monero-core_nl.qm
Updating '/home/chuck/monero-core/build/release/bin/translations/monero-core_nl.qm'...
Removing translations equal to source text in '/home/chuck/monero-core/build/release/bin/translations/monero-core_nl.qm'...
    Generated 369 translation(s) (369 finished and 0 unfinished)
/usr/lib/x86_64-linux-gnu/qt5/bin/lrelease -compress -nounfinished -removeidentical ../translations/monero-core_pl.ts -qm /home/chuck/monero-core/build/release/bin/translations/monero-core_pl.qm
Updating '/home/chuck/monero-core/build/release/bin/translations/monero-core_pl.qm'...
Removing translations equal to source text in '/home/chuck/monero-core/build/release/bin/translations/monero-core_pl.qm'...
    Generated 175 translation(s) (175 finished and 0 unfinished)
    Ignored 150 untranslated source text(s)
/usr/lib/x86_64-linux-gnu/qt5/bin/lrelease -compress -nounfinished -removeidentical ../translations/monero-core_ru.ts -qm /home/chuck/monero-core/build/release/bin/translations/monero-core_ru.qm
Updating '/home/chuck/monero-core/build/release/bin/translations/monero-core_ru.qm'...
Removing translations equal to source text in '/home/chuck/monero-core/build/release/bin/translations/monero-core_ru.qm'...
    Generated 343 translation(s) (343 finished and 0 unfinished)
    Ignored 37 untranslated source text(s)
/usr/lib/x86_64-linux-gnu/qt5/bin/lrelease -compress -nounfinished -removeidentical ../translations/monero-core_sv.ts -qm /home/chuck/monero-core/build/release/bin/translations/monero-core_sv.qm
Updating '/home/chuck/monero-core/build/release/bin/translations/monero-core_sv.qm'...
Removing translations equal to source text in '/home/chuck/monero-core/build/release/bin/translations/monero-core_sv.qm'...
    Generated 365 translation(s) (365 finished and 0 unfinished)
/usr/lib/x86_64-linux-gnu/qt5/bin/lrelease -compress -nounfinished -removeidentical ../translations/monero-core_zh-cn.ts -qm /home/chuck/monero-core/build/release/bin/translations/monero-core_zh-cn.qm
Updating '/home/chuck/monero-core/build/release/bin/translations/monero-core_zh-cn.qm'...
Removing translations equal to source text in '/home/chuck/monero-core/build/release/bin/translations/monero-core_zh-cn.qm'...
    Generated 349 translation(s) (349 finished and 0 unfinished)
    Ignored 23 untranslated source text(s)
/usr/lib/x86_64-linux-gnu/qt5/bin/lrelease -compress -nounfinished -removeidentical ../translations/monero-core_zh-tw.ts -qm /home/chuck/monero-core/build/release/bin/translations/monero-core_zh-tw.qm
Updating '/home/chuck/monero-core/build/release/bin/translations/monero-core_zh-tw.qm'...
Removing translations equal to source text in '/home/chuck/monero-core/build/release/bin/translations/monero-core_zh-tw.qm'...
    Generated 377 translation(s) (377 finished and 0 unfinished)
/usr/lib/x86_64-linux-gnu/qt5/bin/lrelease -compress -nounfinished -removeidentical ../translations/monero-core_he.ts -qm /home/chuck/monero-core/build/release/bin/translations/monero-core_he.qm
Updating '/home/chuck/monero-core/build/release/bin/translations/monero-core_he.qm'...
Removing translations equal to source text in '/home/chuck/monero-core/build/release/bin/translations/monero-core_he.qm'...
    Generated 369 translation(s) (369 finished and 0 unfinished)
    Ignored 21 untranslated source text(s)
/usr/lib/x86_64-linux-gnu/qt5/bin/lrelease -compress -nounfinished -removeidentical ../translations/monero-core_ko.ts -qm /home/chuck/monero-core/build/release/bin/translations/monero-core_ko.qm
Updating '/home/chuck/monero-core/build/release/bin/translations/monero-core_ko.qm'...
Removing translations equal to source text in '/home/chuck/monero-core/build/release/bin/translations/monero-core_ko.qm'...
    Generated 373 translation(s) (373 finished and 0 unfinished)
    Ignored 3 untranslated source text(s)
/usr/lib/x86_64-linux-gnu/qt5/bin/lrelease -compress -nounfinished -removeidentical ../translations/monero-core_ro.ts -qm /home/chuck/monero-core/build/release/bin/translations/monero-core_ro.qm
Updating '/home/chuck/monero-core/build/release/bin/translations/monero-core_ro.qm'...
Removing translations equal to source text in '/home/chuck/monero-core/build/release/bin/translations/monero-core_ro.qm'...
    Generated 357 translation(s) (357 finished and 0 unfinished)
g++ -c -m64 -pipe -O2 -std=c++0x -Wall -W -D_REENTRANT -fPIC -DQT_NO_DEBUG -DQT_QUICK_LIB -DQT_WIDGETS_LIB -DQT_GUI_LIB -DQT_QML_LIB -DQT_NETWORK_LIB -DQT_CORE_LIB -I../../monero-core -I. -I/home/chuck/monero-core/monero/include -I../src/libwalletqt -I../src/QR-Code-generator -I../src -I../monero/src -isystem /usr/include/x86_64-linux-gnu/qt5 -isystem /usr/include/x86_64-linux-gnu/qt5/QtQuick -isystem /usr/include/x86_64-linux-gnu/qt5/QtWidgets -isystem /usr/include/x86_64-linux-gnu/qt5/QtGui -isystem /usr/include/x86_64-linux-gnu/qt5/QtQml -isystem /usr/include/x86_64-linux-gnu/qt5/QtNetwork -isystem /usr/include/x86_64-linux-gnu/qt5/QtCore -I. -I/usr/lib/x86_64-linux-gnu/qt5/mkspecs/linux-g++-64 -o main.o ../main.cpp
Makefile:807: recipe for target 'main.o' failed

# Discussion History
## dEBRUYNE-1 | 2017-12-01T11:50:32+00:00
Could you install libreadline and try again?

## danrmiller | 2017-12-01T13:48:38+00:00
@dEBRUYNE-1 This shouldn't happen. You should be able to build without libreadline. It looks like he is hitting the issue that was fixed in https://github.com/monero-project/monero/pull/2841

Another user came on irc with a similar problem.


## charleshsu168 | 2017-12-01T21:59:29+00:00
@dEBRUYNE-1 I installed libreadline and tried again. still failed to build
@danrmiller the fix did not resolve this error.

## danrmiller | 2017-12-01T22:03:57+00:00
What is the commit your monero submodule is on? I'm not so sure its using the fix.

## charleshsu168 | 2017-12-01T22:16:38+00:00
 i git clone https://github.com/monero-project/monero-core.git  
and followed the guide https://github.com/monero-project/monero-gui to build and got this error.
to be sure, i  also checked the cmake/FindReadline.cmake file and it did include the additional 4 lines fix.



## danrmiller | 2017-12-07T01:09:22+00:00
@charleshsu168 can you upload a gist or pastebin of the CMakeError.log from the monero submodule, located somewhere like monero/build/release/CMakeFiles/CMakeError.log?

# Action History
- Created by: charleshsu168 | 2017-11-29T18:18:50+00:00
- Closed at: 2017-12-10T22:07:00+00:00
