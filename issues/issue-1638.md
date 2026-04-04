---
title: Build Error
source_url: https://github.com/monero-project/monero-gui/issues/1638
author: ghost
assignees: []
labels:
- invalid
created_at: '2018-10-12T04:56:45+00:00'
updated_at: '2018-10-12T15:09:27+00:00'
type: issue
status: closed
closed_at: '2018-10-12T15:09:27+00:00'
---

# Original Description
OS: Linux 18.04 LTS

I followed build instructions step by step and the final build step returned this error and no contents were in bin folder. I have managed to build and run Stellite GUI, but this I cannot get to work.

/usr/bin/ld: cannot find -lwallet_merged
collect2: error: ld returned 1 exit status
Makefile:295: recipe for target 'release/bin/monero-wallet-gui' failed
make: *** [release/bin/monero-wallet-gui] Error 1

Please help

# Discussion History
## sanderfoobar | 2018-10-12T10:10:44+00:00
Please post the full log.

## ghost | 2018-10-12T14:45:01+00:00
Hi @skftn I've attached the build method and error report as well as below:

[Compile & Reopen - XMC-GUI.pdf](https://github.com/monero-project/monero-gui/files/2473510/Compile.Reopen.-.XMC-GUI.pdf)

**BUILD:**

1. Install Monero dependencies
sudo apt install build-essential cmake libboost-all-dev miniupnpc libunbound-dev graphviz doxygen libunwind8-dev pkg-config libssl-dev libzmq3-dev

2. Install Qt:
sudo apt install qtbase5-dev qt5-default qtdeclarative5-dev qml-module-qtquick-controls qml-module-qtquick-controls2 qml-module-qtquick-dialogs qml-module-qtquick-xmllistmodel qml-module-qt-labs-settings qml-module-qt-labs-folderlistmodel qttools5-dev-tools

Optional : To build the flag WITH_SCANNER
sudo apt install qtmultimedia5-dev qml-module-qtmultimedia libzbar-dev

3.a
cd Programs

3.b. Clone repository
git clone https://github.com/monero-classic/monero-gui.git

4.a. Make directory for XMC-GUI
mkdir ~/Programs/XMC-GUI

4.b. Build
cd monero-gui
QT_SELECT=5 ./build.sh

The executable can be found in the build/release/bin folder.

================================================================================================================

**REOPEN:**

cd Programs/xmc-gui/monero-gui/build/release/bin

./ xxxxxxx

================================================================================================================

**ERROR**

blackparallax@JAG-Yoga:~$ cd Programs/xmc-gui
bash: cd: Programs/xmc-gui: No such file or directory
blackparallax@JAG-Yoga:~$ mkdir ~/Programs/xmc-gui
blackparallax@JAG-Yoga:~$ cd Programs/xmc-gui
blackparallax@JAG-Yoga:~/Programs/xmc-gui$ git clone https://github.com/monero-classic/monero-gui.git
Cloning into 'monero-gui'...
remote: Enumerating objects: 1, done.
remote: Counting objects: 100% (1/1), done.
remote: Total 9408 (delta 0), reused 0 (delta 0), pack-reused 9407
Receiving objects: 100% (9408/9408), 14.02 MiB | 594.00 KiB/s, done.
Resolving deltas: 100% (6702/6702), done.
blackparallax@JAG-Yoga:~/Programs/xmc-gui$ cd monero-gui
blackparallax@JAG-Yoga:~/Programs/xmc-gui/monero-gui$ QT_SELECT=5 ./build.sh
Building release
~/Programs/xmc-gui/monero-gui ~/Programs/xmc-gui/monero-gui
~/Programs/xmc-gui/monero-gui ~/Programs/xmc-gui/monero-gui
Submodule 'monero' (https://github.com/monero-classic/monero.git) registered for path 'monero'
Cloning into '/home/blackparallax/Programs/xmc-gui/monero-gui/monero'...
Submodule path 'monero': checked out '61a93019ccebba19d16b45498166b4fc3b566465'
HEAD is now at 61a93019 delayed update
You are currently on commit 840669b
The most recent tag was at 840669b
You are building a tagged release
Switched to a new branch 'release'
Submodule 'external/miniupnp' (https://github.com/monero-project/miniupnp) registered for path 'external/miniupnp'
Submodule 'external/rapidjson' (https://github.com/Tencent/rapidjson) registered for path 'external/rapidjson'
Submodule 'external/unbound' (https://github.com/monero-project/unbound) registered for path 'external/unbound'
Cloning into '/home/blackparallax/Programs/xmc-gui/monero-gui/monero/external/miniupnp'...
Cloning into '/home/blackparallax/Programs/xmc-gui/monero-gui/monero/external/rapidjson'...
Cloning into '/home/blackparallax/Programs/xmc-gui/monero-gui/monero/external/unbound'...
Submodule path 'external/miniupnp': checked out '6a63f9954959119568fbc4af57d7b491b9428d87'
Submodule path 'external/rapidjson': checked out 'af223d44f4e8d3772cb1ac0ce8bc2a132b51717f'
Submodule path 'external/unbound': checked out '193bdc4ee3fe2b0d17e547e86512528c2614483a'
libwallet_merged.a not found - Building libwallet
Building libwallet release
cleaning up existing monero build dir, libs and includes
~/Programs/xmc-gui/monero-gui/monero/build/release ~/Programs/xmc-gui/monero-gui ~/Programs/xmc-gui/monero-gui
Configuring build for Linux x64
./get_libwallet_api.sh: line 153: cmake: command not found
./get_libwallet_api.sh: line 214: pushd: /home/blackparallax/Programs/xmc-gui/monero-gui/monero/build/release/src/wallet: No such file or directory
make: Entering directory '/home/blackparallax/Programs/xmc-gui/monero-gui/monero'
g++     version.cpp   -o version
version.cpp:6:10: fatal error: version.h: No such file or directory
 #include "version.h"
          ^~~~~~~~~~~
compilation terminated.
<builtin>: recipe for target 'version' failed
make: *** [version] Error 1
make: Leaving directory '/home/blackparallax/Programs/xmc-gui/monero-gui/monero'
make: *** No targets specified and no makefile found. Stop.
make: *** No rule to make target 'install'. Stop.
~/Programs/xmc-gui/monero-gui ~/Programs/xmc-gui/monero-gui
./get_libwallet_api.sh: line 223: pushd: /home/blackparallax/Programs/xmc-gui/monero-gui/monero/build/release/src/daemon: No such file or directory
make: *** No targets specified and no makefile found. Stop.
make: *** No rule to make target 'install'. Stop.
~/Programs/xmc-gui/monero-gui
make: *** /home/blackparallax/Programs/xmc-gui/monero-gui/monero/build/release/contrib/epee: No such file or directory. Stop.
make: *** /home/blackparallax/Programs/xmc-gui/monero-gui/monero/build/release/external/easylogging++: No such file or directory. Stop.
make: *** /home/blackparallax/Programs/xmc-gui/monero-gui/monero/build/release/external/db_drivers/liblmdb: No such file or directory. Stop.
Installing libunbound...
./get_libwallet_api.sh: line 240: pushd: /home/blackparallax/Programs/xmc-gui/monero-gui/monero/build/release/external/unbound: No such file or directory
make: *** No rule to make target 'install'. Stop.
./get_libwallet_api.sh: line 244: popd: directory stack empty
./get_libwallet_api.sh: line 247: popd: directory stack empty
make: Entering directory '/home/blackparallax/Programs/xmc-gui/monero-gui/src/zxcvbn-c'
g++ -I. -std=c++11 -O2 -Wall -Wextra \
	-o dictgen dict-generate.cpp 
./dictgen -o dict-src.h words-eng_wiki.txt words-female.txt words-male.txt words-passwd.txt words-surname.txt words-tv_film.txt
cc -I. -O2 -Wall -Wextra -Wdeclaration-after-statement -c -o zxcvbn-inline.o zxcvbn.c
ar cvq libzxcvbn.a zxcvbn-inline.o
a - zxcvbn-inline.o
cc -I. -O2 -Wall -Wextra -Wdeclaration-after-statement -o test-statlib test.c libzxcvbn.a  -lm
make: Leaving directory '/home/blackparallax/Programs/xmc-gui/monero-gui/src/zxcvbn-c'
You are currently on commit 840669b
The most recent tag was at 840669b
You are building a tagged release
~/Programs/xmc-gui/monero-gui/monero ~/Programs/xmc-gui/monero-gui ~/Programs/xmc-gui/monero-gui
You are currently on commit 61a93019
The most recent tag was at 61a93019
You are building a tagged release
~/Programs/xmc-gui/monero-gui ~/Programs/xmc-gui/monero-gui
Info: creating stash file /home/blackparallax/Programs/xmc-gui/monero-gui/build/.qmake.stash
Project MESSAGE: Building without libunwind
Updating '/home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_ar.qm'...
Removing translations equal to source text in '/home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_ar.qm'...
    Generated 257 translation(s) (257 finished and 0 unfinished)
    Ignored 215 untranslated source text(s)
Updating '/home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_cat.qm'...
Removing translations equal to source text in '/home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_cat.qm'...
    Generated 241 translation(s) (241 finished and 0 unfinished)
    Ignored 174 untranslated source text(s)
Updating '/home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_cs.qm'...
Removing translations equal to source text in '/home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_cs.qm'...
    Generated 468 translation(s) (468 finished and 0 unfinished)
    Ignored 11 untranslated source text(s)
Updating '/home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_da.qm'...
Removing translations equal to source text in '/home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_da.qm'...
    Generated 435 translation(s) (435 finished and 0 unfinished)
    Ignored 13 untranslated source text(s)
Updating '/home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_de.qm'...
Removing translations equal to source text in '/home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_de.qm'...
    Generated 450 translation(s) (450 finished and 0 unfinished)
    Ignored 37 untranslated source text(s)
Updating '/home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_eo.qm'...
Removing translations equal to source text in '/home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_eo.qm'...
    Generated 454 translation(s) (454 finished and 0 unfinished)
    Ignored 33 untranslated source text(s)
Updating '/home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_es.qm'...
Removing translations equal to source text in '/home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_es.qm'...
    Generated 459 translation(s) (459 finished and 0 unfinished)
    Ignored 11 untranslated source text(s)
Updating '/home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_fi.qm'...
Removing translations equal to source text in '/home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_fi.qm'...
    Generated 126 translation(s) (126 finished and 0 unfinished)
    Ignored 322 untranslated source text(s)
Updating '/home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_fr.qm'...
Removing translations equal to source text in '/home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_fr.qm'...
    Generated 448 translation(s) (448 finished and 0 unfinished)
    Ignored 11 untranslated source text(s)
Updating '/home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_he.qm'...
Removing translations equal to source text in '/home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_he.qm'...
    Generated 459 translation(s) (459 finished and 0 unfinished)
    Ignored 33 untranslated source text(s)
Updating '/home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_hi.qm'...
Removing translations equal to source text in '/home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_hi.qm'...
    Generated 49 translation(s) (49 finished and 0 unfinished)
    Ignored 432 untranslated source text(s)
Updating '/home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_hr.qm'...
Removing translations equal to source text in '/home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_hr.qm'...
    Generated 472 translation(s) (472 finished and 0 unfinished)
    Ignored 13 untranslated source text(s)
Updating '/home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_hu.qm'...
Removing translations equal to source text in '/home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_hu.qm'...
    Generated 476 translation(s) (476 finished and 0 unfinished)
    Ignored 2 untranslated source text(s)
Updating '/home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_id.qm'...
Removing translations equal to source text in '/home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_id.qm'...
    Generated 257 translation(s) (257 finished and 0 unfinished)
    Ignored 202 untranslated source text(s)
Updating '/home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_it.qm'...
Removing translations equal to source text in '/home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_it.qm'...
    Generated 460 translation(s) (460 finished and 0 unfinished)
    Ignored 11 untranslated source text(s)
Updating '/home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_ja.qm'...
Removing translations equal to source text in '/home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_ja.qm'...
    Generated 474 translation(s) (474 finished and 0 unfinished)
    Ignored 11 untranslated source text(s)
Updating '/home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_ko.qm'...
Removing translations equal to source text in '/home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_ko.qm'...
    Generated 275 translation(s) (275 finished and 0 unfinished)
    Ignored 178 untranslated source text(s)
Updating '/home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_lt.qm'...
Removing translations equal to source text in '/home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_lt.qm'...
    Generated 461 translation(s) (461 finished and 0 unfinished)
    Ignored 39 untranslated source text(s)
Updating '/home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_nl.qm'...
Removing translations equal to source text in '/home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_nl.qm'...
    Generated 472 translation(s) (472 finished and 0 unfinished)
    Ignored 11 untranslated source text(s)
Updating '/home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_pl.qm'...
Removing translations equal to source text in '/home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_pl.qm'...
    Generated 470 translation(s) (470 finished and 0 unfinished)
    Ignored 11 untranslated source text(s)
Updating '/home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_pt-br.qm'...
Removing translations equal to source text in '/home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_pt-br.qm'...
    Generated 466 translation(s) (466 finished and 0 unfinished)
    Ignored 11 untranslated source text(s)
Updating '/home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_pt-pt.qm'...
Removing translations equal to source text in '/home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_pt-pt.qm'...
    Generated 458 translation(s) (458 finished and 0 unfinished)
    Ignored 11 untranslated source text(s)
Updating '/home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_ro.qm'...
Removing translations equal to source text in '/home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_ro.qm'...
    Generated 460 translation(s) (460 finished and 0 unfinished)
    Ignored 13 untranslated source text(s)
Updating '/home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_ru.qm'...
Removing translations equal to source text in '/home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_ru.qm'...
    Generated 473 translation(s) (473 finished and 0 unfinished)
    Ignored 23 untranslated source text(s)
Updating '/home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_sk.qm'...
Removing translations equal to source text in '/home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_sk.qm'...
    Generated 434 translation(s) (434 finished and 0 unfinished)
    Ignored 41 untranslated source text(s)
Updating '/home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_sl.qm'...
Removing translations equal to source text in '/home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_sl.qm'...
    Generated 318 translation(s) (318 finished and 0 unfinished)
    Ignored 139 untranslated source text(s)
Updating '/home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_sr.qm'...
Removing translations equal to source text in '/home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_sr.qm'...
    Generated 456 translation(s) (456 finished and 0 unfinished)
    Ignored 11 untranslated source text(s)
Updating '/home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_sv.qm'...
Removing translations equal to source text in '/home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_sv.qm'...
    Generated 462 translation(s) (462 finished and 0 unfinished)
    Ignored 11 untranslated source text(s)
Updating '/home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_tr.qm'...
Removing translations equal to source text in '/home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_tr.qm'...
    Generated 466 translation(s) (466 finished and 0 unfinished)
    Ignored 11 untranslated source text(s)
Updating '/home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_ua.qm'...
Removing translations equal to source text in '/home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_ua.qm'...
    Generated 474 translation(s) (474 finished and 0 unfinished)
    Ignored 24 untranslated source text(s)
Warning: dropping duplicate messages in '/home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_zh-cn.qm':

* Context: Transfer
* Source: Normal (x1 fee)

Updating '/home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_zh-cn.qm'...
Removing translations equal to source text in '/home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_zh-cn.qm'...
    Generated 475 translation(s) (475 finished and 0 unfinished)
    Ignored 14 untranslated source text(s)
Updating '/home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_zh-tw.qm'...
Removing translations equal to source text in '/home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_zh-tw.qm'...
    Generated 475 translation(s) (475 finished and 0 unfinished)
    Ignored 11 untranslated source text(s)
/usr/lib/qt5/bin/lrelease -compress -nounfinished -removeidentical ../translations/monero-core_ar.ts -qm /home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_ar.qm
Updating '/home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_ar.qm'...
Removing translations equal to source text in '/home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_ar.qm'...
    Generated 257 translation(s) (257 finished and 0 unfinished)
    Ignored 215 untranslated source text(s)
/usr/lib/qt5/bin/lrelease -compress -nounfinished -removeidentical ../translations/monero-core_cat.ts -qm /home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_cat.qm
Updating '/home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_cat.qm'...
Removing translations equal to source text in '/home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_cat.qm'...
    Generated 241 translation(s) (241 finished and 0 unfinished)
    Ignored 174 untranslated source text(s)
/usr/lib/qt5/bin/lrelease -compress -nounfinished -removeidentical ../translations/monero-core_cs.ts -qm /home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_cs.qm
Updating '/home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_cs.qm'...
Removing translations equal to source text in '/home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_cs.qm'...
    Generated 468 translation(s) (468 finished and 0 unfinished)
    Ignored 11 untranslated source text(s)
/usr/lib/qt5/bin/lrelease -compress -nounfinished -removeidentical ../translations/monero-core_da.ts -qm /home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_da.qm
Updating '/home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_da.qm'...
Removing translations equal to source text in '/home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_da.qm'...
    Generated 435 translation(s) (435 finished and 0 unfinished)
    Ignored 13 untranslated source text(s)
/usr/lib/qt5/bin/lrelease -compress -nounfinished -removeidentical ../translations/monero-core_de.ts -qm /home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_de.qm
Updating '/home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_de.qm'...
Removing translations equal to source text in '/home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_de.qm'...
    Generated 450 translation(s) (450 finished and 0 unfinished)
    Ignored 37 untranslated source text(s)
/usr/lib/qt5/bin/lrelease -compress -nounfinished -removeidentical ../translations/monero-core_eo.ts -qm /home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_eo.qm
Updating '/home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_eo.qm'...
Removing translations equal to source text in '/home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_eo.qm'...
    Generated 454 translation(s) (454 finished and 0 unfinished)
    Ignored 33 untranslated source text(s)
/usr/lib/qt5/bin/lrelease -compress -nounfinished -removeidentical ../translations/monero-core_es.ts -qm /home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_es.qm
Updating '/home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_es.qm'...
Removing translations equal to source text in '/home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_es.qm'...
    Generated 459 translation(s) (459 finished and 0 unfinished)
    Ignored 11 untranslated source text(s)
/usr/lib/qt5/bin/lrelease -compress -nounfinished -removeidentical ../translations/monero-core_fi.ts -qm /home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_fi.qm
Updating '/home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_fi.qm'...
Removing translations equal to source text in '/home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_fi.qm'...
    Generated 126 translation(s) (126 finished and 0 unfinished)
    Ignored 322 untranslated source text(s)
/usr/lib/qt5/bin/lrelease -compress -nounfinished -removeidentical ../translations/monero-core_fr.ts -qm /home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_fr.qm
Updating '/home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_fr.qm'...
Removing translations equal to source text in '/home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_fr.qm'...
    Generated 448 translation(s) (448 finished and 0 unfinished)
    Ignored 11 untranslated source text(s)
/usr/lib/qt5/bin/lrelease -compress -nounfinished -removeidentical ../translations/monero-core_he.ts -qm /home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_he.qm
Updating '/home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_he.qm'...
Removing translations equal to source text in '/home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_he.qm'...
    Generated 459 translation(s) (459 finished and 0 unfinished)
    Ignored 33 untranslated source text(s)
/usr/lib/qt5/bin/lrelease -compress -nounfinished -removeidentical ../translations/monero-core_hi.ts -qm /home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_hi.qm
Updating '/home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_hi.qm'...
Removing translations equal to source text in '/home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_hi.qm'...
    Generated 49 translation(s) (49 finished and 0 unfinished)
    Ignored 432 untranslated source text(s)
/usr/lib/qt5/bin/lrelease -compress -nounfinished -removeidentical ../translations/monero-core_hr.ts -qm /home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_hr.qm
Updating '/home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_hr.qm'...
Removing translations equal to source text in '/home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_hr.qm'...
    Generated 472 translation(s) (472 finished and 0 unfinished)
    Ignored 13 untranslated source text(s)
/usr/lib/qt5/bin/lrelease -compress -nounfinished -removeidentical ../translations/monero-core_hu.ts -qm /home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_hu.qm
Updating '/home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_hu.qm'...
Removing translations equal to source text in '/home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_hu.qm'...
    Generated 476 translation(s) (476 finished and 0 unfinished)
    Ignored 2 untranslated source text(s)
/usr/lib/qt5/bin/lrelease -compress -nounfinished -removeidentical ../translations/monero-core_id.ts -qm /home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_id.qm
Updating '/home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_id.qm'...
Removing translations equal to source text in '/home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_id.qm'...
    Generated 257 translation(s) (257 finished and 0 unfinished)
    Ignored 202 untranslated source text(s)
/usr/lib/qt5/bin/lrelease -compress -nounfinished -removeidentical ../translations/monero-core_it.ts -qm /home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_it.qm
Updating '/home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_it.qm'...
Removing translations equal to source text in '/home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_it.qm'...
    Generated 460 translation(s) (460 finished and 0 unfinished)
    Ignored 11 untranslated source text(s)
/usr/lib/qt5/bin/lrelease -compress -nounfinished -removeidentical ../translations/monero-core_ja.ts -qm /home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_ja.qm
Updating '/home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_ja.qm'...
Removing translations equal to source text in '/home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_ja.qm'...
    Generated 474 translation(s) (474 finished and 0 unfinished)
    Ignored 11 untranslated source text(s)
/usr/lib/qt5/bin/lrelease -compress -nounfinished -removeidentical ../translations/monero-core_ko.ts -qm /home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_ko.qm
Updating '/home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_ko.qm'...
Removing translations equal to source text in '/home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_ko.qm'...
    Generated 275 translation(s) (275 finished and 0 unfinished)
    Ignored 178 untranslated source text(s)
/usr/lib/qt5/bin/lrelease -compress -nounfinished -removeidentical ../translations/monero-core_lt.ts -qm /home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_lt.qm
Updating '/home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_lt.qm'...
Removing translations equal to source text in '/home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_lt.qm'...
    Generated 461 translation(s) (461 finished and 0 unfinished)
    Ignored 39 untranslated source text(s)
/usr/lib/qt5/bin/lrelease -compress -nounfinished -removeidentical ../translations/monero-core_nl.ts -qm /home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_nl.qm
Updating '/home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_nl.qm'...
Removing translations equal to source text in '/home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_nl.qm'...
    Generated 472 translation(s) (472 finished and 0 unfinished)
    Ignored 11 untranslated source text(s)
/usr/lib/qt5/bin/lrelease -compress -nounfinished -removeidentical ../translations/monero-core_pl.ts -qm /home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_pl.qm
Updating '/home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_pl.qm'...
Removing translations equal to source text in '/home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_pl.qm'...
    Generated 470 translation(s) (470 finished and 0 unfinished)
    Ignored 11 untranslated source text(s)
/usr/lib/qt5/bin/lrelease -compress -nounfinished -removeidentical ../translations/monero-core_pt-br.ts -qm /home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_pt-br.qm
Updating '/home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_pt-br.qm'...
Removing translations equal to source text in '/home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_pt-br.qm'...
    Generated 466 translation(s) (466 finished and 0 unfinished)
    Ignored 11 untranslated source text(s)
/usr/lib/qt5/bin/lrelease -compress -nounfinished -removeidentical ../translations/monero-core_pt-pt.ts -qm /home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_pt-pt.qm
Updating '/home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_pt-pt.qm'...
Removing translations equal to source text in '/home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_pt-pt.qm'...
    Generated 458 translation(s) (458 finished and 0 unfinished)
    Ignored 11 untranslated source text(s)
/usr/lib/qt5/bin/lrelease -compress -nounfinished -removeidentical ../translations/monero-core_ro.ts -qm /home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_ro.qm
Updating '/home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_ro.qm'...
Removing translations equal to source text in '/home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_ro.qm'...
    Generated 460 translation(s) (460 finished and 0 unfinished)
    Ignored 13 untranslated source text(s)
/usr/lib/qt5/bin/lrelease -compress -nounfinished -removeidentical ../translations/monero-core_ru.ts -qm /home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_ru.qm
Updating '/home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_ru.qm'...
Removing translations equal to source text in '/home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_ru.qm'...
    Generated 473 translation(s) (473 finished and 0 unfinished)
    Ignored 23 untranslated source text(s)
/usr/lib/qt5/bin/lrelease -compress -nounfinished -removeidentical ../translations/monero-core_sk.ts -qm /home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_sk.qm
Updating '/home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_sk.qm'...
Removing translations equal to source text in '/home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_sk.qm'...
    Generated 434 translation(s) (434 finished and 0 unfinished)
    Ignored 41 untranslated source text(s)
/usr/lib/qt5/bin/lrelease -compress -nounfinished -removeidentical ../translations/monero-core_sl.ts -qm /home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_sl.qm
Updating '/home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_sl.qm'...
Removing translations equal to source text in '/home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_sl.qm'...
    Generated 318 translation(s) (318 finished and 0 unfinished)
    Ignored 139 untranslated source text(s)
/usr/lib/qt5/bin/lrelease -compress -nounfinished -removeidentical ../translations/monero-core_sr.ts -qm /home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_sr.qm
Updating '/home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_sr.qm'...
Removing translations equal to source text in '/home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_sr.qm'...
    Generated 456 translation(s) (456 finished and 0 unfinished)
    Ignored 11 untranslated source text(s)
/usr/lib/qt5/bin/lrelease -compress -nounfinished -removeidentical ../translations/monero-core_sv.ts -qm /home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_sv.qm
Updating '/home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_sv.qm'...
Removing translations equal to source text in '/home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_sv.qm'...
    Generated 462 translation(s) (462 finished and 0 unfinished)
    Ignored 11 untranslated source text(s)
/usr/lib/qt5/bin/lrelease -compress -nounfinished -removeidentical ../translations/monero-core_tr.ts -qm /home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_tr.qm
Updating '/home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_tr.qm'...
Removing translations equal to source text in '/home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_tr.qm'...
    Generated 466 translation(s) (466 finished and 0 unfinished)
    Ignored 11 untranslated source text(s)
/usr/lib/qt5/bin/lrelease -compress -nounfinished -removeidentical ../translations/monero-core_ua.ts -qm /home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_ua.qm
Updating '/home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_ua.qm'...
Removing translations equal to source text in '/home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_ua.qm'...
    Generated 474 translation(s) (474 finished and 0 unfinished)
    Ignored 24 untranslated source text(s)
/usr/lib/qt5/bin/lrelease -compress -nounfinished -removeidentical ../translations/monero-core_zh-cn.ts -qm /home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_zh-cn.qm
Warning: dropping duplicate messages in '/home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_zh-cn.qm':

* Context: Transfer
* Source: Normal (x1 fee)

Updating '/home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_zh-cn.qm'...
Removing translations equal to source text in '/home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_zh-cn.qm'...
    Generated 475 translation(s) (475 finished and 0 unfinished)
    Ignored 14 untranslated source text(s)
/usr/lib/qt5/bin/lrelease -compress -nounfinished -removeidentical ../translations/monero-core_zh-tw.ts -qm /home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_zh-tw.qm
Updating '/home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_zh-tw.qm'...
Removing translations equal to source text in '/home/blackparallax/Programs/xmc-gui/monero-gui/build/translations/monero-core_zh-tw.qm'...
    Generated 475 translation(s) (475 finished and 0 unfinished)
    Ignored 11 untranslated source text(s)
g++ -c -pipe -fPIC -fstack-protector -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=1 -Wformat -Wformat-security -fstack-protector -fstack-protector-strong -O2 -std=gnu++11 -pthread -Wall -W -D_REENTRANT -fPIC -DQT_NO_DEBUG -DQT_QUICK_LIB -DQT_WIDGETS_LIB -DQT_GUI_LIB -DQT_QML_LIB -DQT_NETWORK_LIB -DQT_CORE_LIB -I../../monero-gui -I. -I/home/blackparallax/Programs/xmc-gui/monero-gui/monero/include -I../src/libwalletqt -I../src/QR-Code-generator -I../src -I../monero/src -isystem /usr/include/PCSC -isystem /usr/include/x86_64-linux-gnu/qt5 -isystem /usr/include/x86_64-linux-gnu/qt5/QtQuick -isystem /usr/include/x86_64-linux-gnu/qt5/QtWidgets -isystem /usr/include/x86_64-linux-gnu/qt5/QtGui -isystem /usr/include/x86_64-linux-gnu/qt5/QtQml -isystem /usr/include/x86_64-linux-gnu/qt5/QtNetwork -isystem /usr/include/x86_64-linux-gnu/qt5/QtCore -I. -isystem /usr/include/libdrm -I/usr/lib/x86_64-linux-gnu/qt5/mkspecs/linux-g++ -o main.o ../main.cpp
g++ -c -pipe -fPIC -fstack-protector -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=1 -Wformat -Wformat-security -fstack-protector -fstack-protector-strong -O2 -std=gnu++11 -pthread -Wall -W -D_REENTRANT -fPIC -DQT_NO_DEBUG -DQT_QUICK_LIB -DQT_WIDGETS_LIB -DQT_GUI_LIB -DQT_QML_LIB -DQT_NETWORK_LIB -DQT_CORE_LIB -I../../monero-gui -I. -I/home/blackparallax/Programs/xmc-gui/monero-gui/monero/include -I../src/libwalletqt -I../src/QR-Code-generator -I../src -I../monero/src -isystem /usr/include/PCSC -isystem /usr/include/x86_64-linux-gnu/qt5 -isystem /usr/include/x86_64-linux-gnu/qt5/QtQuick -isystem /usr/include/x86_64-linux-gnu/qt5/QtWidgets -isystem /usr/include/x86_64-linux-gnu/qt5/QtGui -isystem /usr/include/x86_64-linux-gnu/qt5/QtQml -isystem /usr/include/x86_64-linux-gnu/qt5/QtNetwork -isystem /usr/include/x86_64-linux-gnu/qt5/QtCore -I. -isystem /usr/include/libdrm -I/usr/lib/x86_64-linux-gnu/qt5/mkspecs/linux-g++ -o filter.o ../filter.cpp
g++ -c -pipe -fPIC -fstack-protector -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=1 -Wformat -Wformat-security -fstack-protector -fstack-protector-strong -O2 -std=gnu++11 -pthread -Wall -W -D_REENTRANT -fPIC -DQT_NO_DEBUG -DQT_QUICK_LIB -DQT_WIDGETS_LIB -DQT_GUI_LIB -DQT_QML_LIB -DQT_NETWORK_LIB -DQT_CORE_LIB -I../../monero-gui -I. -I/home/blackparallax/Programs/xmc-gui/monero-gui/monero/include -I../src/libwalletqt -I../src/QR-Code-generator -I../src -I../monero/src -isystem /usr/include/PCSC -isystem /usr/include/x86_64-linux-gnu/qt5 -isystem /usr/include/x86_64-linux-gnu/qt5/QtQuick -isystem /usr/include/x86_64-linux-gnu/qt5/QtWidgets -isystem /usr/include/x86_64-linux-gnu/qt5/QtGui -isystem /usr/include/x86_64-linux-gnu/qt5/QtQml -isystem /usr/include/x86_64-linux-gnu/qt5/QtNetwork -isystem /usr/include/x86_64-linux-gnu/qt5/QtCore -I. -isystem /usr/include/libdrm -I/usr/lib/x86_64-linux-gnu/qt5/mkspecs/linux-g++ -o clipboardAdapter.o ../clipboardAdapter.cpp
g++ -c -pipe -fPIC -fstack-protector -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=1 -Wformat -Wformat-security -fstack-protector -fstack-protector-strong -O2 -std=gnu++11 -pthread -Wall -W -D_REENTRANT -fPIC -DQT_NO_DEBUG -DQT_QUICK_LIB -DQT_WIDGETS_LIB -DQT_GUI_LIB -DQT_QML_LIB -DQT_NETWORK_LIB -DQT_CORE_LIB -I../../monero-gui -I. -I/home/blackparallax/Programs/xmc-gui/monero-gui/monero/include -I../src/libwalletqt -I../src/QR-Code-generator -I../src -I../monero/src -isystem /usr/include/PCSC -isystem /usr/include/x86_64-linux-gnu/qt5 -isystem /usr/include/x86_64-linux-gnu/qt5/QtQuick -isystem /usr/include/x86_64-linux-gnu/qt5/QtWidgets -isystem /usr/include/x86_64-linux-gnu/qt5/QtGui -isystem /usr/include/x86_64-linux-gnu/qt5/QtQml -isystem /usr/include/x86_64-linux-gnu/qt5/QtNetwork -isystem /usr/include/x86_64-linux-gnu/qt5/QtCore -I. -isystem /usr/include/libdrm -I/usr/lib/x86_64-linux-gnu/qt5/mkspecs/linux-g++ -o oscursor.o ../oscursor.cpp
g++ -c -pipe -fPIC -fstack-protector -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=1 -Wformat -Wformat-security -fstack-protector -fstack-protector-strong -O2 -std=gnu++11 -pthread -Wall -W -D_REENTRANT -fPIC -DQT_NO_DEBUG -DQT_QUICK_LIB -DQT_WIDGETS_LIB -DQT_GUI_LIB -DQT_QML_LIB -DQT_NETWORK_LIB -DQT_CORE_LIB -I../../monero-gui -I. -I/home/blackparallax/Programs/xmc-gui/monero-gui/monero/include -I../src/libwalletqt -I../src/QR-Code-generator -I../src -I../monero/src -isystem /usr/include/PCSC -isystem /usr/include/x86_64-linux-gnu/qt5 -isystem /usr/include/x86_64-linux-gnu/qt5/QtQuick -isystem /usr/include/x86_64-linux-gnu/qt5/QtWidgets -isystem /usr/include/x86_64-linux-gnu/qt5/QtGui -isystem /usr/include/x86_64-linux-gnu/qt5/QtQml -isystem /usr/include/x86_64-linux-gnu/qt5/QtNetwork -isystem /usr/include/x86_64-linux-gnu/qt5/QtCore -I. -isystem /usr/include/libdrm -I/usr/lib/x86_64-linux-gnu/qt5/mkspecs/linux-g++ -o WalletManager.o ../src/libwalletqt/WalletManager.cpp
../src/libwalletqt/WalletManager.cpp: In member function ‘bool WalletManager::moveWallet(const QString&, const QString&)’:
../src/libwalletqt/WalletManager.cpp:156:47: warning: unused parameter ‘src’ [-Wunused-parameter]
 bool WalletManager::moveWallet(const QString &src, const QString &dst)
                                               ^~~
../src/libwalletqt/WalletManager.cpp:156:67: warning: unused parameter ‘dst’ [-Wunused-parameter]
 bool WalletManager::moveWallet(const QString &src, const QString &dst)
                                                                   ^~~
../src/libwalletqt/WalletManager.cpp: In member function ‘QString WalletManager::walletLanguage(const QString&)’:
../src/libwalletqt/WalletManager.cpp:162:54: warning: unused parameter ‘locale’ [-Wunused-parameter]
 QString WalletManager::walletLanguage(const QString &locale)
                                                      ^~~~~~
g++ -c -pipe -fPIC -fstack-protector -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=1 -Wformat -Wformat-security -fstack-protector -fstack-protector-strong -O2 -std=gnu++11 -pthread -Wall -W -D_REENTRANT -fPIC -DQT_NO_DEBUG -DQT_QUICK_LIB -DQT_WIDGETS_LIB -DQT_GUI_LIB -DQT_QML_LIB -DQT_NETWORK_LIB -DQT_CORE_LIB -I../../monero-gui -I. -I/home/blackparallax/Programs/xmc-gui/monero-gui/monero/include -I../src/libwalletqt -I../src/QR-Code-generator -I../src -I../monero/src -isystem /usr/include/PCSC -isystem /usr/include/x86_64-linux-gnu/qt5 -isystem /usr/include/x86_64-linux-gnu/qt5/QtQuick -isystem /usr/include/x86_64-linux-gnu/qt5/QtWidgets -isystem /usr/include/x86_64-linux-gnu/qt5/QtGui -isystem /usr/include/x86_64-linux-gnu/qt5/QtQml -isystem /usr/include/x86_64-linux-gnu/qt5/QtNetwork -isystem /usr/include/x86_64-linux-gnu/qt5/QtCore -I. -isystem /usr/include/libdrm -I/usr/lib/x86_64-linux-gnu/qt5/mkspecs/linux-g++ -o Wallet.o ../src/libwalletqt/Wallet.cpp
In file included from ../src/libwalletqt/Wallet.cpp:1:0:
../src/libwalletqt/Wallet.h: In constructor ‘Wallet::Wallet(Monero::Wallet*, QObject*)’:
../src/libwalletqt/Wallet.h:350:31: warning: ‘Wallet::m_subaddressModel’ will be initialized after [-Wreorder]
     mutable SubaddressModel * m_subaddressModel;
                               ^~~~~~~~~~~~~~~~~
../src/libwalletqt/Wallet.h:337:21: warning:   ‘quint64 Wallet::m_daemonBlockChainHeight’ [-Wreorder]
     mutable quint64 m_daemonBlockChainHeight;
                     ^~~~~~~~~~~~~~~~~~~~~~~~
../src/libwalletqt/Wallet.cpp:846:1: warning:   when initialized here [-Wreorder]
 Wallet::Wallet(Monero::Wallet *w, QObject *parent)
 ^~~~~~
g++ -c -pipe -fPIC -fstack-protector -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=1 -Wformat -Wformat-security -fstack-protector -fstack-protector-strong -O2 -std=gnu++11 -pthread -Wall -W -D_REENTRANT -fPIC -DQT_NO_DEBUG -DQT_QUICK_LIB -DQT_WIDGETS_LIB -DQT_GUI_LIB -DQT_QML_LIB -DQT_NETWORK_LIB -DQT_CORE_LIB -I../../monero-gui -I. -I/home/blackparallax/Programs/xmc-gui/monero-gui/monero/include -I../src/libwalletqt -I../src/QR-Code-generator -I../src -I../monero/src -isystem /usr/include/PCSC -isystem /usr/include/x86_64-linux-gnu/qt5 -isystem /usr/include/x86_64-linux-gnu/qt5/QtQuick -isystem /usr/include/x86_64-linux-gnu/qt5/QtWidgets -isystem /usr/include/x86_64-linux-gnu/qt5/QtGui -isystem /usr/include/x86_64-linux-gnu/qt5/QtQml -isystem /usr/include/x86_64-linux-gnu/qt5/QtNetwork -isystem /usr/include/x86_64-linux-gnu/qt5/QtCore -I. -isystem /usr/include/libdrm -I/usr/lib/x86_64-linux-gnu/qt5/mkspecs/linux-g++ -o PendingTransaction.o ../src/libwalletqt/PendingTransaction.cpp
g++ -c -pipe -fPIC -fstack-protector -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=1 -Wformat -Wformat-security -fstack-protector -fstack-protector-strong -O2 -std=gnu++11 -pthread -Wall -W -D_REENTRANT -fPIC -DQT_NO_DEBUG -DQT_QUICK_LIB -DQT_WIDGETS_LIB -DQT_GUI_LIB -DQT_QML_LIB -DQT_NETWORK_LIB -DQT_CORE_LIB -I../../monero-gui -I. -I/home/blackparallax/Programs/xmc-gui/monero-gui/monero/include -I../src/libwalletqt -I../src/QR-Code-generator -I../src -I../monero/src -isystem /usr/include/PCSC -isystem /usr/include/x86_64-linux-gnu/qt5 -isystem /usr/include/x86_64-linux-gnu/qt5/QtQuick -isystem /usr/include/x86_64-linux-gnu/qt5/QtWidgets -isystem /usr/include/x86_64-linux-gnu/qt5/QtGui -isystem /usr/include/x86_64-linux-gnu/qt5/QtQml -isystem /usr/include/x86_64-linux-gnu/qt5/QtNetwork -isystem /usr/include/x86_64-linux-gnu/qt5/QtCore -I. -isystem /usr/include/libdrm -I/usr/lib/x86_64-linux-gnu/qt5/mkspecs/linux-g++ -o TransactionHistory.o ../src/libwalletqt/TransactionHistory.cpp
g++ -c -pipe -fPIC -fstack-protector -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=1 -Wformat -Wformat-security -fstack-protector -fstack-protector-strong -O2 -std=gnu++11 -pthread -Wall -W -D_REENTRANT -fPIC -DQT_NO_DEBUG -DQT_QUICK_LIB -DQT_WIDGETS_LIB -DQT_GUI_LIB -DQT_QML_LIB -DQT_NETWORK_LIB -DQT_CORE_LIB -I../../monero-gui -I. -I/home/blackparallax/Programs/xmc-gui/monero-gui/monero/include -I../src/libwalletqt -I../src/QR-Code-generator -I../src -I../monero/src -isystem /usr/include/PCSC -isystem /usr/include/x86_64-linux-gnu/qt5 -isystem /usr/include/x86_64-linux-gnu/qt5/QtQuick -isystem /usr/include/x86_64-linux-gnu/qt5/QtWidgets -isystem /usr/include/x86_64-linux-gnu/qt5/QtGui -isystem /usr/include/x86_64-linux-gnu/qt5/QtQml -isystem /usr/include/x86_64-linux-gnu/qt5/QtNetwork -isystem /usr/include/x86_64-linux-gnu/qt5/QtCore -I. -isystem /usr/include/libdrm -I/usr/lib/x86_64-linux-gnu/qt5/mkspecs/linux-g++ -o TransactionInfo.o ../src/libwalletqt/TransactionInfo.cpp
g++ -c -pipe -fPIC -fstack-protector -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=1 -Wformat -Wformat-security -fstack-protector -fstack-protector-strong -O2 -std=gnu++11 -pthread -Wall -W -D_REENTRANT -fPIC -DQT_NO_DEBUG -DQT_QUICK_LIB -DQT_WIDGETS_LIB -DQT_GUI_LIB -DQT_QML_LIB -DQT_NETWORK_LIB -DQT_CORE_LIB -I../../monero-gui -I. -I/home/blackparallax/Programs/xmc-gui/monero-gui/monero/include -I../src/libwalletqt -I../src/QR-Code-generator -I../src -I../monero/src -isystem /usr/include/PCSC -isystem /usr/include/x86_64-linux-gnu/qt5 -isystem /usr/include/x86_64-linux-gnu/qt5/QtQuick -isystem /usr/include/x86_64-linux-gnu/qt5/QtWidgets -isystem /usr/include/x86_64-linux-gnu/qt5/QtGui -isystem /usr/include/x86_64-linux-gnu/qt5/QtQml -isystem /usr/include/x86_64-linux-gnu/qt5/QtNetwork -isystem /usr/include/x86_64-linux-gnu/qt5/QtCore -I. -isystem /usr/include/libdrm -I/usr/lib/x86_64-linux-gnu/qt5/mkspecs/linux-g++ -o QRCodeImageProvider.o ../src/libwalletqt/QRCodeImageProvider.cpp
g++ -c -pipe -fPIC -fstack-protector -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=1 -Wformat -Wformat-security -fstack-protector -fstack-protector-strong -O2 -std=gnu++11 -pthread -Wall -W -D_REENTRANT -fPIC -DQT_NO_DEBUG -DQT_QUICK_LIB -DQT_WIDGETS_LIB -DQT_GUI_LIB -DQT_QML_LIB -DQT_NETWORK_LIB -DQT_CORE_LIB -I../../monero-gui -I. -I/home/blackparallax/Programs/xmc-gui/monero-gui/monero/include -I../src/libwalletqt -I../src/QR-Code-generator -I../src -I../monero/src -isystem /usr/include/PCSC -isystem /usr/include/x86_64-linux-gnu/qt5 -isystem /usr/include/x86_64-linux-gnu/qt5/QtQuick -isystem /usr/include/x86_64-linux-gnu/qt5/QtWidgets -isystem /usr/include/x86_64-linux-gnu/qt5/QtGui -isystem /usr/include/x86_64-linux-gnu/qt5/QtQml -isystem /usr/include/x86_64-linux-gnu/qt5/QtNetwork -isystem /usr/include/x86_64-linux-gnu/qt5/QtCore -I. -isystem /usr/include/libdrm -I/usr/lib/x86_64-linux-gnu/qt5/mkspecs/linux-g++ -o oshelper.o ../oshelper.cpp
g++ -c -pipe -fPIC -fstack-protector -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=1 -Wformat -Wformat-security -fstack-protector -fstack-protector-strong -O2 -std=gnu++11 -pthread -Wall -W -D_REENTRANT -fPIC -DQT_NO_DEBUG -DQT_QUICK_LIB -DQT_WIDGETS_LIB -DQT_GUI_LIB -DQT_QML_LIB -DQT_NETWORK_LIB -DQT_CORE_LIB -I../../monero-gui -I. -I/home/blackparallax/Programs/xmc-gui/monero-gui/monero/include -I../src/libwalletqt -I../src/QR-Code-generator -I../src -I../monero/src -isystem /usr/include/PCSC -isystem /usr/include/x86_64-linux-gnu/qt5 -isystem /usr/include/x86_64-linux-gnu/qt5/QtQuick -isystem /usr/include/x86_64-linux-gnu/qt5/QtWidgets -isystem /usr/include/x86_64-linux-gnu/qt5/QtGui -isystem /usr/include/x86_64-linux-gnu/qt5/QtQml -isystem /usr/include/x86_64-linux-gnu/qt5/QtNetwork -isystem /usr/include/x86_64-linux-gnu/qt5/QtCore -I. -isystem /usr/include/libdrm -I/usr/lib/x86_64-linux-gnu/qt5/mkspecs/linux-g++ -o TranslationManager.o ../TranslationManager.cpp
g++ -c -pipe -fPIC -fstack-protector -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=1 -Wformat -Wformat-security -fstack-protector -fstack-protector-strong -O2 -std=gnu++11 -pthread -Wall -W -D_REENTRANT -fPIC -DQT_NO_DEBUG -DQT_QUICK_LIB -DQT_WIDGETS_LIB -DQT_GUI_LIB -DQT_QML_LIB -DQT_NETWORK_LIB -DQT_CORE_LIB -I../../monero-gui -I. -I/home/blackparallax/Programs/xmc-gui/monero-gui/monero/include -I../src/libwalletqt -I../src/QR-Code-generator -I../src -I../monero/src -isystem /usr/include/PCSC -isystem /usr/include/x86_64-linux-gnu/qt5 -isystem /usr/include/x86_64-linux-gnu/qt5/QtQuick -isystem /usr/include/x86_64-linux-gnu/qt5/QtWidgets -isystem /usr/include/x86_64-linux-gnu/qt5/QtGui -isystem /usr/include/x86_64-linux-gnu/qt5/QtQml -isystem /usr/include/x86_64-linux-gnu/qt5/QtNetwork -isystem /usr/include/x86_64-linux-gnu/qt5/QtCore -I. -isystem /usr/include/libdrm -I/usr/lib/x86_64-linux-gnu/qt5/mkspecs/linux-g++ -o TransactionHistoryModel.o ../src/model/TransactionHistoryModel.cpp
g++ -c -pipe -fPIC -fstack-protector -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=1 -Wformat -Wformat-security -fstack-protector -fstack-protector-strong -O2 -std=gnu++11 -pthread -Wall -W -D_REENTRANT -fPIC -DQT_NO_DEBUG -DQT_QUICK_LIB -DQT_WIDGETS_LIB -DQT_GUI_LIB -DQT_QML_LIB -DQT_NETWORK_LIB -DQT_CORE_LIB -I../../monero-gui -I. -I/home/blackparallax/Programs/xmc-gui/monero-gui/monero/include -I../src/libwalletqt -I../src/QR-Code-generator -I../src -I../monero/src -isystem /usr/include/PCSC -isystem /usr/include/x86_64-linux-gnu/qt5 -isystem /usr/include/x86_64-linux-gnu/qt5/QtQuick -isystem /usr/include/x86_64-linux-gnu/qt5/QtWidgets -isystem /usr/include/x86_64-linux-gnu/qt5/QtGui -isystem /usr/include/x86_64-linux-gnu/qt5/QtQml -isystem /usr/include/x86_64-linux-gnu/qt5/QtNetwork -isystem /usr/include/x86_64-linux-gnu/qt5/QtCore -I. -isystem /usr/include/libdrm -I/usr/lib/x86_64-linux-gnu/qt5/mkspecs/linux-g++ -o TransactionHistorySortFilterModel.o ../src/model/TransactionHistorySortFilterModel.cpp
g++ -c -pipe -fPIC -fstack-protector -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=1 -Wformat -Wformat-security -fstack-protector -fstack-protector-strong -O2 -std=gnu++11 -pthread -Wall -W -D_REENTRANT -fPIC -DQT_NO_DEBUG -DQT_QUICK_LIB -DQT_WIDGETS_LIB -DQT_GUI_LIB -DQT_QML_LIB -DQT_NETWORK_LIB -DQT_CORE_LIB -I../../monero-gui -I. -I/home/blackparallax/Programs/xmc-gui/monero-gui/monero/include -I../src/libwalletqt -I../src/QR-Code-generator -I../src -I../monero/src -isystem /usr/include/PCSC -isystem /usr/include/x86_64-linux-gnu/qt5 -isystem /usr/include/x86_64-linux-gnu/qt5/QtQuick -isystem /usr/include/x86_64-linux-gnu/qt5/QtWidgets -isystem /usr/include/x86_64-linux-gnu/qt5/QtGui -isystem /usr/include/x86_64-linux-gnu/qt5/QtQml -isystem /usr/include/x86_64-linux-gnu/qt5/QtNetwork -isystem /usr/include/x86_64-linux-gnu/qt5/QtCore -I. -isystem /usr/include/libdrm -I/usr/lib/x86_64-linux-gnu/qt5/mkspecs/linux-g++ -o BitBuffer.o ../src/QR-Code-generator/BitBuffer.cpp
g++ -c -pipe -fPIC -fstack-protector -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=1 -Wformat -Wformat-security -fstack-protector -fstack-protector-strong -O2 -std=gnu++11 -pthread -Wall -W -D_REENTRANT -fPIC -DQT_NO_DEBUG -DQT_QUICK_LIB -DQT_WIDGETS_LIB -DQT_GUI_LIB -DQT_QML_LIB -DQT_NETWORK_LIB -DQT_CORE_LIB -I../../monero-gui -I. -I/home/blackparallax/Programs/xmc-gui/monero-gui/monero/include -I../src/libwalletqt -I../src/QR-Code-generator -I../src -I../monero/src -isystem /usr/include/PCSC -isystem /usr/include/x86_64-linux-gnu/qt5 -isystem /usr/include/x86_64-linux-gnu/qt5/QtQuick -isystem /usr/include/x86_64-linux-gnu/qt5/QtWidgets -isystem /usr/include/x86_64-linux-gnu/qt5/QtGui -isystem /usr/include/x86_64-linux-gnu/qt5/QtQml -isystem /usr/include/x86_64-linux-gnu/qt5/QtNetwork -isystem /usr/include/x86_64-linux-gnu/qt5/QtCore -I. -isystem /usr/include/libdrm -I/usr/lib/x86_64-linux-gnu/qt5/mkspecs/linux-g++ -o QrCode.o ../src/QR-Code-generator/QrCode.cpp
g++ -c -pipe -fPIC -fstack-protector -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=1 -Wformat -Wformat-security -fstack-protector -fstack-protector-strong -O2 -std=gnu++11 -pthread -Wall -W -D_REENTRANT -fPIC -DQT_NO_DEBUG -DQT_QUICK_LIB -DQT_WIDGETS_LIB -DQT_GUI_LIB -DQT_QML_LIB -DQT_NETWORK_LIB -DQT_CORE_LIB -I../../monero-gui -I. -I/home/blackparallax/Programs/xmc-gui/monero-gui/monero/include -I../src/libwalletqt -I../src/QR-Code-generator -I../src -I../monero/src -isystem /usr/include/PCSC -isystem /usr/include/x86_64-linux-gnu/qt5 -isystem /usr/include/x86_64-linux-gnu/qt5/QtQuick -isystem /usr/include/x86_64-linux-gnu/qt5/QtWidgets -isystem /usr/include/x86_64-linux-gnu/qt5/QtGui -isystem /usr/include/x86_64-linux-gnu/qt5/QtQml -isystem /usr/include/x86_64-linux-gnu/qt5/QtNetwork -isystem /usr/include/x86_64-linux-gnu/qt5/QtCore -I. -isystem /usr/include/libdrm -I/usr/lib/x86_64-linux-gnu/qt5/mkspecs/linux-g++ -o QrSegment.o ../src/QR-Code-generator/QrSegment.cpp
g++ -c -pipe -fPIC -fstack-protector -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=1 -Wformat -Wformat-security -fstack-protector -fstack-protector-strong -O2 -std=gnu++11 -pthread -Wall -W -D_REENTRANT -fPIC -DQT_NO_DEBUG -DQT_QUICK_LIB -DQT_WIDGETS_LIB -DQT_GUI_LIB -DQT_QML_LIB -DQT_NETWORK_LIB -DQT_CORE_LIB -I../../monero-gui -I. -I/home/blackparallax/Programs/xmc-gui/monero-gui/monero/include -I../src/libwalletqt -I../src/QR-Code-generator -I../src -I../monero/src -isystem /usr/include/PCSC -isystem /usr/include/x86_64-linux-gnu/qt5 -isystem /usr/include/x86_64-linux-gnu/qt5/QtQuick -isystem /usr/include/x86_64-linux-gnu/qt5/QtWidgets -isystem /usr/include/x86_64-linux-gnu/qt5/QtGui -isystem /usr/include/x86_64-linux-gnu/qt5/QtQml -isystem /usr/include/x86_64-linux-gnu/qt5/QtNetwork -isystem /usr/include/x86_64-linux-gnu/qt5/QtCore -I. -isystem /usr/include/libdrm -I/usr/lib/x86_64-linux-gnu/qt5/mkspecs/linux-g++ -o AddressBookModel.o ../src/model/AddressBookModel.cpp
../src/model/AddressBookModel.cpp: In member function ‘virtual int AddressBookModel::rowCount(const QModelIndex&) const’:
../src/model/AddressBookModel.cpp:25:51: warning: unused parameter ‘parent’ [-Wunused-parameter]
 int AddressBookModel::rowCount(const QModelIndex &parent) const
                                                   ^~~~~~
g++ -c -pipe -fPIC -fstack-protector -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=1 -Wformat -Wformat-security -fstack-protector -fstack-protector-strong -O2 -std=gnu++11 -pthread -Wall -W -D_REENTRANT -fPIC -DQT_NO_DEBUG -DQT_QUICK_LIB -DQT_WIDGETS_LIB -DQT_GUI_LIB -DQT_QML_LIB -DQT_NETWORK_LIB -DQT_CORE_LIB -I../../monero-gui -I. -I/home/blackparallax/Programs/xmc-gui/monero-gui/monero/include -I../src/libwalletqt -I../src/QR-Code-generator -I../src -I../monero/src -isystem /usr/include/PCSC -isystem /usr/include/x86_64-linux-gnu/qt5 -isystem /usr/include/x86_64-linux-gnu/qt5/QtQuick -isystem /usr/include/x86_64-linux-gnu/qt5/QtWidgets -isystem /usr/include/x86_64-linux-gnu/qt5/QtGui -isystem /usr/include/x86_64-linux-gnu/qt5/QtQml -isystem /usr/include/x86_64-linux-gnu/qt5/QtNetwork -isystem /usr/include/x86_64-linux-gnu/qt5/QtCore -I. -isystem /usr/include/libdrm -I/usr/lib/x86_64-linux-gnu/qt5/mkspecs/linux-g++ -o AddressBook.o ../src/libwalletqt/AddressBook.cpp
g++ -c -pipe -fPIC -fstack-protector -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=1 -Wformat -Wformat-security -fstack-protector -fstack-protector-strong -O2 -std=gnu++11 -pthread -Wall -W -D_REENTRANT -fPIC -DQT_NO_DEBUG -DQT_QUICK_LIB -DQT_WIDGETS_LIB -DQT_GUI_LIB -DQT_QML_LIB -DQT_NETWORK_LIB -DQT_CORE_LIB -I../../monero-gui -I. -I/home/blackparallax/Programs/xmc-gui/monero-gui/monero/include -I../src/libwalletqt -I../src/QR-Code-generator -I../src -I../monero/src -isystem /usr/include/PCSC -isystem /usr/include/x86_64-linux-gnu/qt5 -isystem /usr/include/x86_64-linux-gnu/qt5/QtQuick -isystem /usr/include/x86_64-linux-gnu/qt5/QtWidgets -isystem /usr/include/x86_64-linux-gnu/qt5/QtGui -isystem /usr/include/x86_64-linux-gnu/qt5/QtQml -isystem /usr/include/x86_64-linux-gnu/qt5/QtNetwork -isystem /usr/include/x86_64-linux-gnu/qt5/QtCore -I. -isystem /usr/include/libdrm -I/usr/lib/x86_64-linux-gnu/qt5/mkspecs/linux-g++ -o SubaddressModel.o ../src/model/SubaddressModel.cpp
../src/model/SubaddressModel.cpp: In member function ‘virtual int SubaddressModel::rowCount(const QModelIndex&) const’:
../src/model/SubaddressModel.cpp:53:50: warning: unused parameter ‘parent’ [-Wunused-parameter]
 int SubaddressModel::rowCount(const QModelIndex &parent) const
                                                  ^~~~~~
g++ -c -pipe -fPIC -fstack-protector -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=1 -Wformat -Wformat-security -fstack-protector -fstack-protector-strong -O2 -std=gnu++11 -pthread -Wall -W -D_REENTRANT -fPIC -DQT_NO_DEBUG -DQT_QUICK_LIB -DQT_WIDGETS_LIB -DQT_GUI_LIB -DQT_QML_LIB -DQT_NETWORK_LIB -DQT_CORE_LIB -I../../monero-gui -I. -I/home/blackparallax/Programs/xmc-gui/monero-gui/monero/include -I../src/libwalletqt -I../src/QR-Code-generator -I../src -I../monero/src -isystem /usr/include/PCSC -isystem /usr/include/x86_64-linux-gnu/qt5 -isystem /usr/include/x86_64-linux-gnu/qt5/QtQuick -isystem /usr/include/x86_64-linux-gnu/qt5/QtWidgets -isystem /usr/include/x86_64-linux-gnu/qt5/QtGui -isystem /usr/include/x86_64-linux-gnu/qt5/QtQml -isystem /usr/include/x86_64-linux-gnu/qt5/QtNetwork -isystem /usr/include/x86_64-linux-gnu/qt5/QtCore -I. -isystem /usr/include/libdrm -I/usr/lib/x86_64-linux-gnu/qt5/mkspecs/linux-g++ -o Subaddress.o ../src/libwalletqt/Subaddress.cpp
gcc -c -pipe -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=1 -Wformat -Wformat-security -fstack-protector -fstack-protector-strong -O2 -pthread -Wall -W -D_REENTRANT -fPIC -DQT_NO_DEBUG -DQT_QUICK_LIB -DQT_WIDGETS_LIB -DQT_GUI_LIB -DQT_QML_LIB -DQT_NETWORK_LIB -DQT_CORE_LIB -I../../monero-gui -I. -I/home/blackparallax/Programs/xmc-gui/monero-gui/monero/include -I../src/libwalletqt -I../src/QR-Code-generator -I../src -I../monero/src -isystem /usr/include/PCSC -isystem /usr/include/x86_64-linux-gnu/qt5 -isystem /usr/include/x86_64-linux-gnu/qt5/QtQuick -isystem /usr/include/x86_64-linux-gnu/qt5/QtWidgets -isystem /usr/include/x86_64-linux-gnu/qt5/QtGui -isystem /usr/include/x86_64-linux-gnu/qt5/QtQml -isystem /usr/include/x86_64-linux-gnu/qt5/QtNetwork -isystem /usr/include/x86_64-linux-gnu/qt5/QtCore -I. -isystem /usr/include/libdrm -I/usr/lib/x86_64-linux-gnu/qt5/mkspecs/linux-g++ -o zxcvbn.o ../src/zxcvbn-c/zxcvbn.c
g++ -c -pipe -fPIC -fstack-protector -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=1 -Wformat -Wformat-security -fstack-protector -fstack-protector-strong -O2 -std=gnu++11 -pthread -Wall -W -D_REENTRANT -fPIC -DQT_NO_DEBUG -DQT_QUICK_LIB -DQT_WIDGETS_LIB -DQT_GUI_LIB -DQT_QML_LIB -DQT_NETWORK_LIB -DQT_CORE_LIB -I../../monero-gui -I. -I/home/blackparallax/Programs/xmc-gui/monero-gui/monero/include -I../src/libwalletqt -I../src/QR-Code-generator -I../src -I../monero/src -isystem /usr/include/PCSC -isystem /usr/include/x86_64-linux-gnu/qt5 -isystem /usr/include/x86_64-linux-gnu/qt5/QtQuick -isystem /usr/include/x86_64-linux-gnu/qt5/QtWidgets -isystem /usr/include/x86_64-linux-gnu/qt5/QtGui -isystem /usr/include/x86_64-linux-gnu/qt5/QtQml -isystem /usr/include/x86_64-linux-gnu/qt5/QtNetwork -isystem /usr/include/x86_64-linux-gnu/qt5/QtCore -I. -isystem /usr/include/libdrm -I/usr/lib/x86_64-linux-gnu/qt5/mkspecs/linux-g++ -o UnsignedTransaction.o ../src/libwalletqt/UnsignedTransaction.cpp
../src/libwalletqt/UnsignedTransaction.cpp: In member function ‘quint64 UnsignedTransaction::amount(int) const’:
../src/libwalletqt/UnsignedTransaction.cpp:18:14: warning: comparison between signed and unsigned integer expressions [-Wsign-compare]
     if(index > arr.size() - 1)
        ~~~~~~^~~~~~~~~~~~~~~~
../src/libwalletqt/UnsignedTransaction.cpp: In member function ‘quint64 UnsignedTransaction::fee(int) const’:
../src/libwalletqt/UnsignedTransaction.cpp:26:14: warning: comparison between signed and unsigned integer expressions [-Wsign-compare]
     if(index > arr.size() - 1)
        ~~~~~~^~~~~~~~~~~~~~~~
../src/libwalletqt/UnsignedTransaction.cpp: In member function ‘quint64 UnsignedTransaction::mixin(int) const’:
../src/libwalletqt/UnsignedTransaction.cpp:34:14: warning: comparison between signed and unsigned integer expressions [-Wsign-compare]
     if(index > arr.size() - 1)
        ~~~~~~^~~~~~~~~~~~~~~~
g++ -c -pipe -fPIC -fstack-protector -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=1 -Wformat -Wformat-security -fstack-protector -fstack-protector-strong -O2 -std=gnu++11 -pthread -Wall -W -D_REENTRANT -fPIC -DQT_NO_DEBUG -DQT_QUICK_LIB -DQT_WIDGETS_LIB -DQT_GUI_LIB -DQT_QML_LIB -DQT_NETWORK_LIB -DQT_CORE_LIB -I../../monero-gui -I. -I/home/blackparallax/Programs/xmc-gui/monero-gui/monero/include -I../src/libwalletqt -I../src/QR-Code-generator -I../src -I../monero/src -isystem /usr/include/PCSC -isystem /usr/include/x86_64-linux-gnu/qt5 -isystem /usr/include/x86_64-linux-gnu/qt5/QtQuick -isystem /usr/include/x86_64-linux-gnu/qt5/QtWidgets -isystem /usr/include/x86_64-linux-gnu/qt5/QtGui -isystem /usr/include/x86_64-linux-gnu/qt5/QtQml -isystem /usr/include/x86_64-linux-gnu/qt5/QtNetwork -isystem /usr/include/x86_64-linux-gnu/qt5/QtCore -I. -isystem /usr/include/libdrm -I/usr/lib/x86_64-linux-gnu/qt5/mkspecs/linux-g++ -o Logger.o ../Logger.cpp
../Logger.cpp: In function ‘const QString getLogPath(QString)’:
../Logger.cpp:23:40: warning: unused parameter ‘logPath’ [-Wunused-parameter]
 const QString getLogPath(const QString logPath)
                                        ^~~~~~~
g++ -c -pipe -fPIC -fstack-protector -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=1 -Wformat -Wformat-security -fstack-protector -fstack-protector-strong -O2 -std=gnu++11 -pthread -Wall -W -D_REENTRANT -fPIC -DQT_NO_DEBUG -DQT_QUICK_LIB -DQT_WIDGETS_LIB -DQT_GUI_LIB -DQT_QML_LIB -DQT_NETWORK_LIB -DQT_CORE_LIB -I../../monero-gui -I. -I/home/blackparallax/Programs/xmc-gui/monero-gui/monero/include -I../src/libwalletqt -I../src/QR-Code-generator -I../src -I../monero/src -isystem /usr/include/PCSC -isystem /usr/include/x86_64-linux-gnu/qt5 -isystem /usr/include/x86_64-linux-gnu/qt5/QtQuick -isystem /usr/include/x86_64-linux-gnu/qt5/QtWidgets -isystem /usr/include/x86_64-linux-gnu/qt5/QtGui -isystem /usr/include/x86_64-linux-gnu/qt5/QtQml -isystem /usr/include/x86_64-linux-gnu/qt5/QtNetwork -isystem /usr/include/x86_64-linux-gnu/qt5/QtCore -I. -isystem /usr/include/libdrm -I/usr/lib/x86_64-linux-gnu/qt5/mkspecs/linux-g++ -o MainApp.o ../MainApp.cpp
g++ -c -pipe -fPIC -fstack-protector -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=1 -Wformat -Wformat-security -fstack-protector -fstack-protector-strong -O2 -std=gnu++11 -pthread -Wall -W -D_REENTRANT -fPIC -DQT_NO_DEBUG -DQT_QUICK_LIB -DQT_WIDGETS_LIB -DQT_GUI_LIB -DQT_QML_LIB -DQT_NETWORK_LIB -DQT_CORE_LIB -I../../monero-gui -I. -I/home/blackparallax/Programs/xmc-gui/monero-gui/monero/include -I../src/libwalletqt -I../src/QR-Code-generator -I../src -I../monero/src -isystem /usr/include/PCSC -isystem /usr/include/x86_64-linux-gnu/qt5 -isystem /usr/include/x86_64-linux-gnu/qt5/QtQuick -isystem /usr/include/x86_64-linux-gnu/qt5/QtWidgets -isystem /usr/include/x86_64-linux-gnu/qt5/QtGui -isystem /usr/include/x86_64-linux-gnu/qt5/QtQml -isystem /usr/include/x86_64-linux-gnu/qt5/QtNetwork -isystem /usr/include/x86_64-linux-gnu/qt5/QtCore -I. -isystem /usr/include/libdrm -I/usr/lib/x86_64-linux-gnu/qt5/mkspecs/linux-g++ -o DaemonManager.o ../src/daemon/DaemonManager.cpp
/usr/lib/qt5/bin/rcc -name translations translations/translations.qrc -o qrc_translations.cpp
g++ -c -pipe -fPIC -fstack-protector -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=1 -Wformat -Wformat-security -fstack-protector -fstack-protector-strong -O2 -std=gnu++11 -pthread -Wall -W -D_REENTRANT -fPIC -DQT_NO_DEBUG -DQT_QUICK_LIB -DQT_WIDGETS_LIB -DQT_GUI_LIB -DQT_QML_LIB -DQT_NETWORK_LIB -DQT_CORE_LIB -I../../monero-gui -I. -I/home/blackparallax/Programs/xmc-gui/monero-gui/monero/include -I../src/libwalletqt -I../src/QR-Code-generator -I../src -I../monero/src -isystem /usr/include/PCSC -isystem /usr/include/x86_64-linux-gnu/qt5 -isystem /usr/include/x86_64-linux-gnu/qt5/QtQuick -isystem /usr/include/x86_64-linux-gnu/qt5/QtWidgets -isystem /usr/include/x86_64-linux-gnu/qt5/QtGui -isystem /usr/include/x86_64-linux-gnu/qt5/QtQml -isystem /usr/include/x86_64-linux-gnu/qt5/QtNetwork -isystem /usr/include/x86_64-linux-gnu/qt5/QtCore -I. -isystem /usr/include/libdrm -I/usr/lib/x86_64-linux-gnu/qt5/mkspecs/linux-g++ -o qrc_translations.o qrc_translations.cpp
/usr/lib/qt5/bin/rcc -name qml ../qml.qrc -o qrc_qml.cpp
g++ -c -pipe -fPIC -fstack-protector -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=1 -Wformat -Wformat-security -fstack-protector -fstack-protector-strong -O2 -std=gnu++11 -pthread -Wall -W -D_REENTRANT -fPIC -DQT_NO_DEBUG -DQT_QUICK_LIB -DQT_WIDGETS_LIB -DQT_GUI_LIB -DQT_QML_LIB -DQT_NETWORK_LIB -DQT_CORE_LIB -I../../monero-gui -I. -I/home/blackparallax/Programs/xmc-gui/monero-gui/monero/include -I../src/libwalletqt -I../src/QR-Code-generator -I../src -I../monero/src -isystem /usr/include/PCSC -isystem /usr/include/x86_64-linux-gnu/qt5 -isystem /usr/include/x86_64-linux-gnu/qt5/QtQuick -isystem /usr/include/x86_64-linux-gnu/qt5/QtWidgets -isystem /usr/include/x86_64-linux-gnu/qt5/QtGui -isystem /usr/include/x86_64-linux-gnu/qt5/QtQml -isystem /usr/include/x86_64-linux-gnu/qt5/QtNetwork -isystem /usr/include/x86_64-linux-gnu/qt5/QtCore -I. -isystem /usr/include/libdrm -I/usr/lib/x86_64-linux-gnu/qt5/mkspecs/linux-g++ -o qrc_qml.o qrc_qml.cpp
g++ -pipe -fPIC -fstack-protector -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=1 -Wformat -Wformat-security -fstack-protector -fstack-protector-strong -O2 -std=gnu++11 -pthread -Wall -W -dM -E -o moc_predefs.h /usr/lib/x86_64-linux-gnu/qt5/mkspecs/features/data/dummy.cpp
/usr/lib/qt5/bin/moc -DQT_NO_DEBUG -DQT_QUICK_LIB -DQT_WIDGETS_LIB -DQT_GUI_LIB -DQT_QML_LIB -DQT_NETWORK_LIB -DQT_CORE_LIB --include ./moc_predefs.h -I/usr/lib/x86_64-linux-gnu/qt5/mkspecs/linux-g++ -I/home/blackparallax/Programs/xmc-gui/monero-gui -I/home/blackparallax/Programs/xmc-gui/monero-gui/monero/include -I/home/blackparallax/Programs/xmc-gui/monero-gui/src/libwalletqt -I/home/blackparallax/Programs/xmc-gui/monero-gui/src/QR-Code-generator -I/home/blackparallax/Programs/xmc-gui/monero-gui/src -I/home/blackparallax/Programs/xmc-gui/monero-gui/monero/src -I/usr/include/PCSC -I/usr/include/x86_64-linux-gnu/qt5 -I/usr/include/x86_64-linux-gnu/qt5/QtQuick -I/usr/include/x86_64-linux-gnu/qt5/QtWidgets -I/usr/include/x86_64-linux-gnu/qt5/QtGui -I/usr/include/x86_64-linux-gnu/qt5/QtQml -I/usr/include/x86_64-linux-gnu/qt5/QtNetwork -I/usr/include/x86_64-linux-gnu/qt5/QtCore -I. -I/usr/include/c++/7 -I/usr/include/x86_64-linux-gnu/c++/7 -I/usr/include/c++/7/backward -I/usr/lib/gcc/x86_64-linux-gnu/7/include -I/usr/local/include -I/usr/lib/gcc/x86_64-linux-gnu/7/include-fixed -I/usr/include/x86_64-linux-gnu -I/usr/include ../filter.h -o moc_filter.cpp
g++ -c -pipe -fPIC -fstack-protector -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=1 -Wformat -Wformat-security -fstack-protector -fstack-protector-strong -O2 -std=gnu++11 -pthread -Wall -W -D_REENTRANT -fPIC -DQT_NO_DEBUG -DQT_QUICK_LIB -DQT_WIDGETS_LIB -DQT_GUI_LIB -DQT_QML_LIB -DQT_NETWORK_LIB -DQT_CORE_LIB -I../../monero-gui -I. -I/home/blackparallax/Programs/xmc-gui/monero-gui/monero/include -I../src/libwalletqt -I../src/QR-Code-generator -I../src -I../monero/src -isystem /usr/include/PCSC -isystem /usr/include/x86_64-linux-gnu/qt5 -isystem /usr/include/x86_64-linux-gnu/qt5/QtQuick -isystem /usr/include/x86_64-linux-gnu/qt5/QtWidgets -isystem /usr/include/x86_64-linux-gnu/qt5/QtGui -isystem /usr/include/x86_64-linux-gnu/qt5/QtQml -isystem /usr/include/x86_64-linux-gnu/qt5/QtNetwork -isystem /usr/include/x86_64-linux-gnu/qt5/QtCore -I. -isystem /usr/include/libdrm -I/usr/lib/x86_64-linux-gnu/qt5/mkspecs/linux-g++ -o moc_filter.o moc_filter.cpp
/usr/lib/qt5/bin/moc -DQT_NO_DEBUG -DQT_QUICK_LIB -DQT_WIDGETS_LIB -DQT_GUI_LIB -DQT_QML_LIB -DQT_NETWORK_LIB -DQT_CORE_LIB --include ./moc_predefs.h -I/usr/lib/x86_64-linux-gnu/qt5/mkspecs/linux-g++ -I/home/blackparallax/Programs/xmc-gui/monero-gui -I/home/blackparallax/Programs/xmc-gui/monero-gui/monero/include -I/home/blackparallax/Programs/xmc-gui/monero-gui/src/libwalletqt -I/home/blackparallax/Programs/xmc-gui/monero-gui/src/QR-Code-generator -I/home/blackparallax/Programs/xmc-gui/monero-gui/src -I/home/blackparallax/Programs/xmc-gui/monero-gui/monero/src -I/usr/include/PCSC -I/usr/include/x86_64-linux-gnu/qt5 -I/usr/include/x86_64-linux-gnu/qt5/QtQuick -I/usr/include/x86_64-linux-gnu/qt5/QtWidgets -I/usr/include/x86_64-linux-gnu/qt5/QtGui -I/usr/include/x86_64-linux-gnu/qt5/QtQml -I/usr/include/x86_64-linux-gnu/qt5/QtNetwork -I/usr/include/x86_64-linux-gnu/qt5/QtCore -I. -I/usr/include/c++/7 -I/usr/include/x86_64-linux-gnu/c++/7 -I/usr/include/c++/7/backward -I/usr/lib/gcc/x86_64-linux-gnu/7/include -I/usr/local/include -I/usr/lib/gcc/x86_64-linux-gnu/7/include-fixed -I/usr/include/x86_64-linux-gnu -I/usr/include ../clipboardAdapter.h -o moc_clipboardAdapter.cpp
g++ -c -pipe -fPIC -fstack-protector -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=1 -Wformat -Wformat-security -fstack-protector -fstack-protector-strong -O2 -std=gnu++11 -pthread -Wall -W -D_REENTRANT -fPIC -DQT_NO_DEBUG -DQT_QUICK_LIB -DQT_WIDGETS_LIB -DQT_GUI_LIB -DQT_QML_LIB -DQT_NETWORK_LIB -DQT_CORE_LIB -I../../monero-gui -I. -I/home/blackparallax/Programs/xmc-gui/monero-gui/monero/include -I../src/libwalletqt -I../src/QR-Code-generator -I../src -I../monero/src -isystem /usr/include/PCSC -isystem /usr/include/x86_64-linux-gnu/qt5 -isystem /usr/include/x86_64-linux-gnu/qt5/QtQuick -isystem /usr/include/x86_64-linux-gnu/qt5/QtWidgets -isystem /usr/include/x86_64-linux-gnu/qt5/QtGui -isystem /usr/include/x86_64-linux-gnu/qt5/QtQml -isystem /usr/include/x86_64-linux-gnu/qt5/QtNetwork -isystem /usr/include/x86_64-linux-gnu/qt5/QtCore -I. -isystem /usr/include/libdrm -I/usr/lib/x86_64-linux-gnu/qt5/mkspecs/linux-g++ -o moc_clipboardAdapter.o moc_clipboardAdapter.cpp
/usr/lib/qt5/bin/moc -DQT_NO_DEBUG -DQT_QUICK_LIB -DQT_WIDGETS_LIB -DQT_GUI_LIB -DQT_QML_LIB -DQT_NETWORK_LIB -DQT_CORE_LIB --include ./moc_predefs.h -I/usr/lib/x86_64-linux-gnu/qt5/mkspecs/linux-g++ -I/home/blackparallax/Programs/xmc-gui/monero-gui -I/home/blackparallax/Programs/xmc-gui/monero-gui/monero/include -I/home/blackparallax/Programs/xmc-gui/monero-gui/src/libwalletqt -I/home/blackparallax/Programs/xmc-gui/monero-gui/src/QR-Code-generator -I/home/blackparallax/Programs/xmc-gui/monero-gui/src -I/home/blackparallax/Programs/xmc-gui/monero-gui/monero/src -I/usr/include/PCSC -I/usr/include/x86_64-linux-gnu/qt5 -I/usr/include/x86_64-linux-gnu/qt5/QtQuick -I/usr/include/x86_64-linux-gnu/qt5/QtWidgets -I/usr/include/x86_64-linux-gnu/qt5/QtGui -I/usr/include/x86_64-linux-gnu/qt5/QtQml -I/usr/include/x86_64-linux-gnu/qt5/QtNetwork -I/usr/include/x86_64-linux-gnu/qt5/QtCore -I. -I/usr/include/c++/7 -I/usr/include/x86_64-linux-gnu/c++/7 -I/usr/include/c++/7/backward -I/usr/lib/gcc/x86_64-linux-gnu/7/include -I/usr/local/include -I/usr/lib/gcc/x86_64-linux-gnu/7/include-fixed -I/usr/include/x86_64-linux-gnu -I/usr/include ../oscursor.h -o moc_oscursor.cpp
g++ -c -pipe -fPIC -fstack-protector -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=1 -Wformat -Wformat-security -fstack-protector -fstack-protector-strong -O2 -std=gnu++11 -pthread -Wall -W -D_REENTRANT -fPIC -DQT_NO_DEBUG -DQT_QUICK_LIB -DQT_WIDGETS_LIB -DQT_GUI_LIB -DQT_QML_LIB -DQT_NETWORK_LIB -DQT_CORE_LIB -I../../monero-gui -I. -I/home/blackparallax/Programs/xmc-gui/monero-gui/monero/include -I../src/libwalletqt -I../src/QR-Code-generator -I../src -I../monero/src -isystem /usr/include/PCSC -isystem /usr/include/x86_64-linux-gnu/qt5 -isystem /usr/include/x86_64-linux-gnu/qt5/QtQuick -isystem /usr/include/x86_64-linux-gnu/qt5/QtWidgets -isystem /usr/include/x86_64-linux-gnu/qt5/QtGui -isystem /usr/include/x86_64-linux-gnu/qt5/QtQml -isystem /usr/include/x86_64-linux-gnu/qt5/QtNetwork -isystem /usr/include/x86_64-linux-gnu/qt5/QtCore -I. -isystem /usr/include/libdrm -I/usr/lib/x86_64-linux-gnu/qt5/mkspecs/linux-g++ -o moc_oscursor.o moc_oscursor.cpp
/usr/lib/qt5/bin/moc -DQT_NO_DEBUG -DQT_QUICK_LIB -DQT_WIDGETS_LIB -DQT_GUI_LIB -DQT_QML_LIB -DQT_NETWORK_LIB -DQT_CORE_LIB --include ./moc_predefs.h -I/usr/lib/x86_64-linux-gnu/qt5/mkspecs/linux-g++ -I/home/blackparallax/Programs/xmc-gui/monero-gui -I/home/blackparallax/Programs/xmc-gui/monero-gui/monero/include -I/home/blackparallax/Programs/xmc-gui/monero-gui/src/libwalletqt -I/home/blackparallax/Programs/xmc-gui/monero-gui/src/QR-Code-generator -I/home/blackparallax/Programs/xmc-gui/monero-gui/src -I/home/blackparallax/Programs/xmc-gui/monero-gui/monero/src -I/usr/include/PCSC -I/usr/include/x86_64-linux-gnu/qt5 -I/usr/include/x86_64-linux-gnu/qt5/QtQuick -I/usr/include/x86_64-linux-gnu/qt5/QtWidgets -I/usr/include/x86_64-linux-gnu/qt5/QtGui -I/usr/include/x86_64-linux-gnu/qt5/QtQml -I/usr/include/x86_64-linux-gnu/qt5/QtNetwork -I/usr/include/x86_64-linux-gnu/qt5/QtCore -I. -I/usr/include/c++/7 -I/usr/include/x86_64-linux-gnu/c++/7 -I/usr/include/c++/7/backward -I/usr/lib/gcc/x86_64-linux-gnu/7/include -I/usr/local/include -I/usr/lib/gcc/x86_64-linux-gnu/7/include-fixed -I/usr/include/x86_64-linux-gnu -I/usr/include ../src/libwalletqt/WalletManager.h -o moc_WalletManager.cpp
g++ -c -pipe -fPIC -fstack-protector -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=1 -Wformat -Wformat-security -fstack-protector -fstack-protector-strong -O2 -std=gnu++11 -pthread -Wall -W -D_REENTRANT -fPIC -DQT_NO_DEBUG -DQT_QUICK_LIB -DQT_WIDGETS_LIB -DQT_GUI_LIB -DQT_QML_LIB -DQT_NETWORK_LIB -DQT_CORE_LIB -I../../monero-gui -I. -I/home/blackparallax/Programs/xmc-gui/monero-gui/monero/include -I../src/libwalletqt -I../src/QR-Code-generator -I../src -I../monero/src -isystem /usr/include/PCSC -isystem /usr/include/x86_64-linux-gnu/qt5 -isystem /usr/include/x86_64-linux-gnu/qt5/QtQuick -isystem /usr/include/x86_64-linux-gnu/qt5/QtWidgets -isystem /usr/include/x86_64-linux-gnu/qt5/QtGui -isystem /usr/include/x86_64-linux-gnu/qt5/QtQml -isystem /usr/include/x86_64-linux-gnu/qt5/QtNetwork -isystem /usr/include/x86_64-linux-gnu/qt5/QtCore -I. -isystem /usr/include/libdrm -I/usr/lib/x86_64-linux-gnu/qt5/mkspecs/linux-g++ -o moc_WalletManager.o moc_WalletManager.cpp
/usr/lib/qt5/bin/moc -DQT_NO_DEBUG -DQT_QUICK_LIB -DQT_WIDGETS_LIB -DQT_GUI_LIB -DQT_QML_LIB -DQT_NETWORK_LIB -DQT_CORE_LIB --include ./moc_predefs.h -I/usr/lib/x86_64-linux-gnu/qt5/mkspecs/linux-g++ -I/home/blackparallax/Programs/xmc-gui/monero-gui -I/home/blackparallax/Programs/xmc-gui/monero-gui/monero/include -I/home/blackparallax/Programs/xmc-gui/monero-gui/src/libwalletqt -I/home/blackparallax/Programs/xmc-gui/monero-gui/src/QR-Code-generator -I/home/blackparallax/Programs/xmc-gui/monero-gui/src -I/home/blackparallax/Programs/xmc-gui/monero-gui/monero/src -I/usr/include/PCSC -I/usr/include/x86_64-linux-gnu/qt5 -I/usr/include/x86_64-linux-gnu/qt5/QtQuick -I/usr/include/x86_64-linux-gnu/qt5/QtWidgets -I/usr/include/x86_64-linux-gnu/qt5/QtGui -I/usr/include/x86_64-linux-gnu/qt5/QtQml -I/usr/include/x86_64-linux-gnu/qt5/QtNetwork -I/usr/include/x86_64-linux-gnu/qt5/QtCore -I. -I/usr/include/c++/7 -I/usr/include/x86_64-linux-gnu/c++/7 -I/usr/include/c++/7/backward -I/usr/lib/gcc/x86_64-linux-gnu/7/include -I/usr/local/include -I/usr/lib/gcc/x86_64-linux-gnu/7/include-fixed -I/usr/include/x86_64-linux-gnu -I/usr/include ../src/libwalletqt/Wallet.h -o moc_Wallet.cpp
g++ -c -pipe -fPIC -fstack-protector -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=1 -Wformat -Wformat-security -fstack-protector -fstack-protector-strong -O2 -std=gnu++11 -pthread -Wall -W -D_REENTRANT -fPIC -DQT_NO_DEBUG -DQT_QUICK_LIB -DQT_WIDGETS_LIB -DQT_GUI_LIB -DQT_QML_LIB -DQT_NETWORK_LIB -DQT_CORE_LIB -I../../monero-gui -I. -I/home/blackparallax/Programs/xmc-gui/monero-gui/monero/include -I../src/libwalletqt -I../src/QR-Code-generator -I../src -I../monero/src -isystem /usr/include/PCSC -isystem /usr/include/x86_64-linux-gnu/qt5 -isystem /usr/include/x86_64-linux-gnu/qt5/QtQuick -isystem /usr/include/x86_64-linux-gnu/qt5/QtWidgets -isystem /usr/include/x86_64-linux-gnu/qt5/QtGui -isystem /usr/include/x86_64-linux-gnu/qt5/QtQml -isystem /usr/include/x86_64-linux-gnu/qt5/QtNetwork -isystem /usr/include/x86_64-linux-gnu/qt5/QtCore -I. -isystem /usr/include/libdrm -I/usr/lib/x86_64-linux-gnu/qt5/mkspecs/linux-g++ -o moc_Wallet.o moc_Wallet.cpp
/usr/lib/qt5/bin/moc -DQT_NO_DEBUG -DQT_QUICK_LIB -DQT_WIDGETS_LIB -DQT_GUI_LIB -DQT_QML_LIB -DQT_NETWORK_LIB -DQT_CORE_LIB --include ./moc_predefs.h -I/usr/lib/x86_64-linux-gnu/qt5/mkspecs/linux-g++ -I/home/blackparallax/Programs/xmc-gui/monero-gui -I/home/blackparallax/Programs/xmc-gui/monero-gui/monero/include -I/home/blackparallax/Programs/xmc-gui/monero-gui/src/libwalletqt -I/home/blackparallax/Programs/xmc-gui/monero-gui/src/QR-Code-generator -I/home/blackparallax/Programs/xmc-gui/monero-gui/src -I/home/blackparallax/Programs/xmc-gui/monero-gui/monero/src -I/usr/include/PCSC -I/usr/include/x86_64-linux-gnu/qt5 -I/usr/include/x86_64-linux-gnu/qt5/QtQuick -I/usr/include/x86_64-linux-gnu/qt5/QtWidgets -I/usr/include/x86_64-linux-gnu/qt5/QtGui -I/usr/include/x86_64-linux-gnu/qt5/QtQml -I/usr/include/x86_64-linux-gnu/qt5/QtNetwork -I/usr/include/x86_64-linux-gnu/qt5/QtCore -I. -I/usr/include/c++/7 -I/usr/include/x86_64-linux-gnu/c++/7 -I/usr/include/c++/7/backward -I/usr/lib/gcc/x86_64-linux-gnu/7/include -I/usr/local/include -I/usr/lib/gcc/x86_64-linux-gnu/7/include-fixed -I/usr/include/x86_64-linux-gnu -I/usr/include ../src/libwalletqt/PendingTransaction.h -o moc_PendingTransaction.cpp
g++ -c -pipe -fPIC -fstack-protector -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=1 -Wformat -Wformat-security -fstack-protector -fstack-protector-strong -O2 -std=gnu++11 -pthread -Wall -W -D_REENTRANT -fPIC -DQT_NO_DEBUG -DQT_QUICK_LIB -DQT_WIDGETS_LIB -DQT_GUI_LIB -DQT_QML_LIB -DQT_NETWORK_LIB -DQT_CORE_LIB -I../../monero-gui -I. -I/home/blackparallax/Programs/xmc-gui/monero-gui/monero/include -I../src/libwalletqt -I../src/QR-Code-generator -I../src -I../monero/src -isystem /usr/include/PCSC -isystem /usr/include/x86_64-linux-gnu/qt5 -isystem /usr/include/x86_64-linux-gnu/qt5/QtQuick -isystem /usr/include/x86_64-linux-gnu/qt5/QtWidgets -isystem /usr/include/x86_64-linux-gnu/qt5/QtGui -isystem /usr/include/x86_64-linux-gnu/qt5/QtQml -isystem /usr/include/x86_64-linux-gnu/qt5/QtNetwork -isystem /usr/include/x86_64-linux-gnu/qt5/QtCore -I. -isystem /usr/include/libdrm -I/usr/lib/x86_64-linux-gnu/qt5/mkspecs/linux-g++ -o moc_PendingTransaction.o moc_PendingTransaction.cpp
/usr/lib/qt5/bin/moc -DQT_NO_DEBUG -DQT_QUICK_LIB -DQT_WIDGETS_LIB -DQT_GUI_LIB -DQT_QML_LIB -DQT_NETWORK_LIB -DQT_CORE_LIB --include ./moc_predefs.h -I/usr/lib/x86_64-linux-gnu/qt5/mkspecs/linux-g++ -I/home/blackparallax/Programs/xmc-gui/monero-gui -I/home/blackparallax/Programs/xmc-gui/monero-gui/monero/include -I/home/blackparallax/Programs/xmc-gui/monero-gui/src/libwalletqt -I/home/blackparallax/Programs/xmc-gui/monero-gui/src/QR-Code-generator -I/home/blackparallax/Programs/xmc-gui/monero-gui/src -I/home/blackparallax/Programs/xmc-gui/monero-gui/monero/src -I/usr/include/PCSC -I/usr/include/x86_64-linux-gnu/qt5 -I/usr/include/x86_64-linux-gnu/qt5/QtQuick -I/usr/include/x86_64-linux-gnu/qt5/QtWidgets -I/usr/include/x86_64-linux-gnu/qt5/QtGui -I/usr/include/x86_64-linux-gnu/qt5/QtQml -I/usr/include/x86_64-linux-gnu/qt5/QtNetwork -I/usr/include/x86_64-linux-gnu/qt5/QtCore -I. -I/usr/include/c++/7 -I/usr/include/x86_64-linux-gnu/c++/7 -I/usr/include/c++/7/backward -I/usr/lib/gcc/x86_64-linux-gnu/7/include -I/usr/local/include -I/usr/lib/gcc/x86_64-linux-gnu/7/include-fixed -I/usr/include/x86_64-linux-gnu -I/usr/include ../src/libwalletqt/TransactionHistory.h -o moc_TransactionHistory.cpp
g++ -c -pipe -fPIC -fstack-protector -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=1 -Wformat -Wformat-security -fstack-protector -fstack-protector-strong -O2 -std=gnu++11 -pthread -Wall -W -D_REENTRANT -fPIC -DQT_NO_DEBUG -DQT_QUICK_LIB -DQT_WIDGETS_LIB -DQT_GUI_LIB -DQT_QML_LIB -DQT_NETWORK_LIB -DQT_CORE_LIB -I../../monero-gui -I. -I/home/blackparallax/Programs/xmc-gui/monero-gui/monero/include -I../src/libwalletqt -I../src/QR-Code-generator -I../src -I../monero/src -isystem /usr/include/PCSC -isystem /usr/include/x86_64-linux-gnu/qt5 -isystem /usr/include/x86_64-linux-gnu/qt5/QtQuick -isystem /usr/include/x86_64-linux-gnu/qt5/QtWidgets -isystem /usr/include/x86_64-linux-gnu/qt5/QtGui -isystem /usr/include/x86_64-linux-gnu/qt5/QtQml -isystem /usr/include/x86_64-linux-gnu/qt5/QtNetwork -isystem /usr/include/x86_64-linux-gnu/qt5/QtCore -I. -isystem /usr/include/libdrm -I/usr/lib/x86_64-linux-gnu/qt5/mkspecs/linux-g++ -o moc_TransactionHistory.o moc_TransactionHistory.cpp
/usr/lib/qt5/bin/moc -DQT_NO_DEBUG -DQT_QUICK_LIB -DQT_WIDGETS_LIB -DQT_GUI_LIB -DQT_QML_LIB -DQT_NETWORK_LIB -DQT_CORE_LIB --include ./moc_predefs.h -I/usr/lib/x86_64-linux-gnu/qt5/mkspecs/linux-g++ -I/home/blackparallax/Programs/xmc-gui/monero-gui -I/home/blackparallax/Programs/xmc-gui/monero-gui/monero/include -I/home/blackparallax/Programs/xmc-gui/monero-gui/src/libwalletqt -I/home/blackparallax/Programs/xmc-gui/monero-gui/src/QR-Code-generator -I/home/blackparallax/Programs/xmc-gui/monero-gui/src -I/home/blackparallax/Programs/xmc-gui/monero-gui/monero/src -I/usr/include/PCSC -I/usr/include/x86_64-linux-gnu/qt5 -I/usr/include/x86_64-linux-gnu/qt5/QtQuick -I/usr/include/x86_64-linux-gnu/qt5/QtWidgets -I/usr/include/x86_64-linux-gnu/qt5/QtGui -I/usr/include/x86_64-linux-gnu/qt5/QtQml -I/usr/include/x86_64-linux-gnu/qt5/QtNetwork -I/usr/include/x86_64-linux-gnu/qt5/QtCore -I. -I/usr/include/c++/7 -I/usr/include/x86_64-linux-gnu/c++/7 -I/usr/include/c++/7/backward -I/usr/lib/gcc/x86_64-linux-gnu/7/include -I/usr/local/include -I/usr/lib/gcc/x86_64-linux-gnu/7/include-fixed -I/usr/include/x86_64-linux-gnu -I/usr/include ../src/libwalletqt/TransactionInfo.h -o moc_TransactionInfo.cpp
g++ -c -pipe -fPIC -fstack-protector -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=1 -Wformat -Wformat-security -fstack-protector -fstack-protector-strong -O2 -std=gnu++11 -pthread -Wall -W -D_REENTRANT -fPIC -DQT_NO_DEBUG -DQT_QUICK_LIB -DQT_WIDGETS_LIB -DQT_GUI_LIB -DQT_QML_LIB -DQT_NETWORK_LIB -DQT_CORE_LIB -I../../monero-gui -I. -I/home/blackparallax/Programs/xmc-gui/monero-gui/monero/include -I../src/libwalletqt -I../src/QR-Code-generator -I../src -I../monero/src -isystem /usr/include/PCSC -isystem /usr/include/x86_64-linux-gnu/qt5 -isystem /usr/include/x86_64-linux-gnu/qt5/QtQuick -isystem /usr/include/x86_64-linux-gnu/qt5/QtWidgets -isystem /usr/include/x86_64-linux-gnu/qt5/QtGui -isystem /usr/include/x86_64-linux-gnu/qt5/QtQml -isystem /usr/include/x86_64-linux-gnu/qt5/QtNetwork -isystem /usr/include/x86_64-linux-gnu/qt5/QtCore -I. -isystem /usr/include/libdrm -I/usr/lib/x86_64-linux-gnu/qt5/mkspecs/linux-g++ -o moc_TransactionInfo.o moc_TransactionInfo.cpp
/usr/lib/qt5/bin/moc -DQT_NO_DEBUG -DQT_QUICK_LIB -DQT_WIDGETS_LIB -DQT_GUI_LIB -DQT_QML_LIB -DQT_NETWORK_LIB -DQT_CORE_LIB --include ./moc_predefs.h -I/usr/lib/x86_64-linux-gnu/qt5/mkspecs/linux-g++ -I/home/blackparallax/Programs/xmc-gui/monero-gui -I/home/blackparallax/Programs/xmc-gui/monero-gui/monero/include -I/home/blackparallax/Programs/xmc-gui/monero-gui/src/libwalletqt -I/home/blackparallax/Programs/xmc-gui/monero-gui/src/QR-Code-generator -I/home/blackparallax/Programs/xmc-gui/monero-gui/src -I/home/blackparallax/Programs/xmc-gui/monero-gui/monero/src -I/usr/include/PCSC -I/usr/include/x86_64-linux-gnu/qt5 -I/usr/include/x86_64-linux-gnu/qt5/QtQuick -I/usr/include/x86_64-linux-gnu/qt5/QtWidgets -I/usr/include/x86_64-linux-gnu/qt5/QtGui -I/usr/include/x86_64-linux-gnu/qt5/QtQml -I/usr/include/x86_64-linux-gnu/qt5/QtNetwork -I/usr/include/x86_64-linux-gnu/qt5/QtCore -I. -I/usr/include/c++/7 -I/usr/include/x86_64-linux-gnu/c++/7 -I/usr/include/c++/7/backward -I/usr/lib/gcc/x86_64-linux-gnu/7/include -I/usr/local/include -I/usr/lib/gcc/x86_64-linux-gnu/7/include-fixed -I/usr/include/x86_64-linux-gnu -I/usr/include ../src/libwalletqt/Transfer.h -o moc_Transfer.cpp
g++ -c -pipe -fPIC -fstack-protector -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=1 -Wformat -Wformat-security -fstack-protector -fstack-protector-strong -O2 -std=gnu++11 -pthread -Wall -W -D_REENTRANT -fPIC -DQT_NO_DEBUG -DQT_QUICK_LIB -DQT_WIDGETS_LIB -DQT_GUI_LIB -DQT_QML_LIB -DQT_NETWORK_LIB -DQT_CORE_LIB -I../../monero-gui -I. -I/home/blackparallax/Programs/xmc-gui/monero-gui/monero/include -I../src/libwalletqt -I../src/QR-Code-generator -I../src -I../monero/src -isystem /usr/include/PCSC -isystem /usr/include/x86_64-linux-gnu/qt5 -isystem /usr/include/x86_64-linux-gnu/qt5/QtQuick -isystem /usr/include/x86_64-linux-gnu/qt5/QtWidgets -isystem /usr/include/x86_64-linux-gnu/qt5/QtGui -isystem /usr/include/x86_64-linux-gnu/qt5/QtQml -isystem /usr/include/x86_64-linux-gnu/qt5/QtNetwork -isystem /usr/include/x86_64-linux-gnu/qt5/QtCore -I. -isystem /usr/include/libdrm -I/usr/lib/x86_64-linux-gnu/qt5/mkspecs/linux-g++ -o moc_Transfer.o moc_Transfer.cpp
/usr/lib/qt5/bin/moc -DQT_NO_DEBUG -DQT_QUICK_LIB -DQT_WIDGETS_LIB -DQT_GUI_LIB -DQT_QML_LIB -DQT_NETWORK_LIB -DQT_CORE_LIB --include ./moc_predefs.h -I/usr/lib/x86_64-linux-gnu/qt5/mkspecs/linux-g++ -I/home/blackparallax/Programs/xmc-gui/monero-gui -I/home/blackparallax/Programs/xmc-gui/monero-gui/monero/include -I/home/blackparallax/Programs/xmc-gui/monero-gui/src/libwalletqt -I/home/blackparallax/Programs/xmc-gui/monero-gui/src/QR-Code-generator -I/home/blackparallax/Programs/xmc-gui/monero-gui/src -I/home/blackparallax/Programs/xmc-gui/monero-gui/monero/src -I/usr/include/PCSC -I/usr/include/x86_64-linux-gnu/qt5 -I/usr/include/x86_64-linux-gnu/qt5/QtQuick -I/usr/include/x86_64-linux-gnu/qt5/QtWidgets -I/usr/include/x86_64-linux-gnu/qt5/QtGui -I/usr/include/x86_64-linux-gnu/qt5/QtQml -I/usr/include/x86_64-linux-gnu/qt5/QtNetwork -I/usr/include/x86_64-linux-gnu/qt5/QtCore -I. -I/usr/include/c++/7 -I/usr/include/x86_64-linux-gnu/c++/7 -I/usr/include/c++/7/backward -I/usr/lib/gcc/x86_64-linux-gnu/7/include -I/usr/local/include -I/usr/lib/gcc/x86_64-linux-gnu/7/include-fixed -I/usr/include/x86_64-linux-gnu -I/usr/include ../src/NetworkType.h -o moc_NetworkType.cpp
g++ -c -pipe -fPIC -fstack-protector -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=1 -Wformat -Wformat-security -fstack-protector -fstack-protector-strong -O2 -std=gnu++11 -pthread -Wall -W -D_REENTRANT -fPIC -DQT_NO_DEBUG -DQT_QUICK_LIB -DQT_WIDGETS_LIB -DQT_GUI_LIB -DQT_QML_LIB -DQT_NETWORK_LIB -DQT_CORE_LIB -I../../monero-gui -I. -I/home/blackparallax/Programs/xmc-gui/monero-gui/monero/include -I../src/libwalletqt -I../src/QR-Code-generator -I../src -I../monero/src -isystem /usr/include/PCSC -isystem /usr/include/x86_64-linux-gnu/qt5 -isystem /usr/include/x86_64-linux-gnu/qt5/QtQuick -isystem /usr/include/x86_64-linux-gnu/qt5/QtWidgets -isystem /usr/include/x86_64-linux-gnu/qt5/QtGui -isystem /usr/include/x86_64-linux-gnu/qt5/QtQml -isystem /usr/include/x86_64-linux-gnu/qt5/QtNetwork -isystem /usr/include/x86_64-linux-gnu/qt5/QtCore -I. -isystem /usr/include/libdrm -I/usr/lib/x86_64-linux-gnu/qt5/mkspecs/linux-g++ -o moc_NetworkType.o moc_NetworkType.cpp
/usr/lib/qt5/bin/moc -DQT_NO_DEBUG -DQT_QUICK_LIB -DQT_WIDGETS_LIB -DQT_GUI_LIB -DQT_QML_LIB -DQT_NETWORK_LIB -DQT_CORE_LIB --include ./moc_predefs.h -I/usr/lib/x86_64-linux-gnu/qt5/mkspecs/linux-g++ -I/home/blackparallax/Programs/xmc-gui/monero-gui -I/home/blackparallax/Programs/xmc-gui/monero-gui/monero/include -I/home/blackparallax/Programs/xmc-gui/monero-gui/src/libwalletqt -I/home/blackparallax/Programs/xmc-gui/monero-gui/src/QR-Code-generator -I/home/blackparallax/Programs/xmc-gui/monero-gui/src -I/home/blackparallax/Programs/xmc-gui/monero-gui/monero/src -I/usr/include/PCSC -I/usr/include/x86_64-linux-gnu/qt5 -I/usr/include/x86_64-linux-gnu/qt5/QtQuick -I/usr/include/x86_64-linux-gnu/qt5/QtWidgets -I/usr/include/x86_64-linux-gnu/qt5/QtGui -I/usr/include/x86_64-linux-gnu/qt5/QtQml -I/usr/include/x86_64-linux-gnu/qt5/QtNetwork -I/usr/include/x86_64-linux-gnu/qt5/QtCore -I. -I/usr/include/c++/7 -I/usr/include/x86_64-linux-gnu/c++/7 -I/usr/include/c++/7/backward -I/usr/lib/gcc/x86_64-linux-gnu/7/include -I/usr/local/include -I/usr/lib/gcc/x86_64-linux-gnu/7/include-fixed -I/usr/include/x86_64-linux-gnu -I/usr/include ../oshelper.h -o moc_oshelper.cpp
g++ -c -pipe -fPIC -fstack-protector -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=1 -Wformat -Wformat-security -fstack-protector -fstack-protector-strong -O2 -std=gnu++11 -pthread -Wall -W -D_REENTRANT -fPIC -DQT_NO_DEBUG -DQT_QUICK_LIB -DQT_WIDGETS_LIB -DQT_GUI_LIB -DQT_QML_LIB -DQT_NETWORK_LIB -DQT_CORE_LIB -I../../monero-gui -I. -I/home/blackparallax/Programs/xmc-gui/monero-gui/monero/include -I../src/libwalletqt -I../src/QR-Code-generator -I../src -I../monero/src -isystem /usr/include/PCSC -isystem /usr/include/x86_64-linux-gnu/qt5 -isystem /usr/include/x86_64-linux-gnu/qt5/QtQuick -isystem /usr/include/x86_64-linux-gnu/qt5/QtWidgets -isystem /usr/include/x86_64-linux-gnu/qt5/QtGui -isystem /usr/include/x86_64-linux-gnu/qt5/QtQml -isystem /usr/include/x86_64-linux-gnu/qt5/QtNetwork -isystem /usr/include/x86_64-linux-gnu/qt5/QtCore -I. -isystem /usr/include/libdrm -I/usr/lib/x86_64-linux-gnu/qt5/mkspecs/linux-g++ -o moc_oshelper.o moc_oshelper.cpp
/usr/lib/qt5/bin/moc -DQT_NO_DEBUG -DQT_QUICK_LIB -DQT_WIDGETS_LIB -DQT_GUI_LIB -DQT_QML_LIB -DQT_NETWORK_LIB -DQT_CORE_LIB --include ./moc_predefs.h -I/usr/lib/x86_64-linux-gnu/qt5/mkspecs/linux-g++ -I/home/blackparallax/Programs/xmc-gui/monero-gui -I/home/blackparallax/Programs/xmc-gui/monero-gui/monero/include -I/home/blackparallax/Programs/xmc-gui/monero-gui/src/libwalletqt -I/home/blackparallax/Programs/xmc-gui/monero-gui/src/QR-Code-generator -I/home/blackparallax/Programs/xmc-gui/monero-gui/src -I/home/blackparallax/Programs/xmc-gui/monero-gui/monero/src -I/usr/include/PCSC -I/usr/include/x86_64-linux-gnu/qt5 -I/usr/include/x86_64-linux-gnu/qt5/QtQuick -I/usr/include/x86_64-linux-gnu/qt5/QtWidgets -I/usr/include/x86_64-linux-gnu/qt5/QtGui -I/usr/include/x86_64-linux-gnu/qt5/QtQml -I/usr/include/x86_64-linux-gnu/qt5/QtNetwork -I/usr/include/x86_64-linux-gnu/qt5/QtCore -I. -I/usr/include/c++/7 -I/usr/include/x86_64-linux-gnu/c++/7 -I/usr/include/c++/7/backward -I/usr/lib/gcc/x86_64-linux-gnu/7/include -I/usr/local/include -I/usr/lib/gcc/x86_64-linux-gnu/7/include-fixed -I/usr/include/x86_64-linux-gnu -I/usr/include ../TranslationManager.h -o moc_TranslationManager.cpp
g++ -c -pipe -fPIC -fstack-protector -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=1 -Wformat -Wformat-security -fstack-protector -fstack-protector-strong -O2 -std=gnu++11 -pthread -Wall -W -D_REENTRANT -fPIC -DQT_NO_DEBUG -DQT_QUICK_LIB -DQT_WIDGETS_LIB -DQT_GUI_LIB -DQT_QML_LIB -DQT_NETWORK_LIB -DQT_CORE_LIB -I../../monero-gui -I. -I/home/blackparallax/Programs/xmc-gui/monero-gui/monero/include -I../src/libwalletqt -I../src/QR-Code-generator -I../src -I../monero/src -isystem /usr/include/PCSC -isystem /usr/include/x86_64-linux-gnu/qt5 -isystem /usr/include/x86_64-linux-gnu/qt5/QtQuick -isystem /usr/include/x86_64-linux-gnu/qt5/QtWidgets -isystem /usr/include/x86_64-linux-gnu/qt5/QtGui -isystem /usr/include/x86_64-linux-gnu/qt5/QtQml -isystem /usr/include/x86_64-linux-gnu/qt5/QtNetwork -isystem /usr/include/x86_64-linux-gnu/qt5/QtCore -I. -isystem /usr/include/libdrm -I/usr/lib/x86_64-linux-gnu/qt5/mkspecs/linux-g++ -o moc_TranslationManager.o moc_TranslationManager.cpp
/usr/lib/qt5/bin/moc -DQT_NO_DEBUG -DQT_QUICK_LIB -DQT_WIDGETS_LIB -DQT_GUI_LIB -DQT_QML_LIB -DQT_NETWORK_LIB -DQT_CORE_LIB --include ./moc_predefs.h -I/usr/lib/x86_64-linux-gnu/qt5/mkspecs/linux-g++ -I/home/blackparallax/Programs/xmc-gui/monero-gui -I/home/blackparallax/Programs/xmc-gui/monero-gui/monero/include -I/home/blackparallax/Programs/xmc-gui/monero-gui/src/libwalletqt -I/home/blackparallax/Programs/xmc-gui/monero-gui/src/QR-Code-generator -I/home/blackparallax/Programs/xmc-gui/monero-gui/src -I/home/blackparallax/Programs/xmc-gui/monero-gui/monero/src -I/usr/include/PCSC -I/usr/include/x86_64-linux-gnu/qt5 -I/usr/include/x86_64-linux-gnu/qt5/QtQuick -I/usr/include/x86_64-linux-gnu/qt5/QtWidgets -I/usr/include/x86_64-linux-gnu/qt5/QtGui -I/usr/include/x86_64-linux-gnu/qt5/QtQml -I/usr/include/x86_64-linux-gnu/qt5/QtNetwork -I/usr/include/x86_64-linux-gnu/qt5/QtCore -I. -I/usr/include/c++/7 -I/usr/include/x86_64-linux-gnu/c++/7 -I/usr/include/c++/7/backward -I/usr/lib/gcc/x86_64-linux-gnu/7/include -I/usr/local/include -I/usr/lib/gcc/x86_64-linux-gnu/7/include-fixed -I/usr/include/x86_64-linux-gnu -I/usr/include ../src/model/TransactionHistoryModel.h -o moc_TransactionHistoryModel.cpp
g++ -c -pipe -fPIC -fstack-protector -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=1 -Wformat -Wformat-security -fstack-protector -fstack-protector-strong -O2 -std=gnu++11 -pthread -Wall -W -D_REENTRANT -fPIC -DQT_NO_DEBUG -DQT_QUICK_LIB -DQT_WIDGETS_LIB -DQT_GUI_LIB -DQT_QML_LIB -DQT_NETWORK_LIB -DQT_CORE_LIB -I../../monero-gui -I. -I/home/blackparallax/Programs/xmc-gui/monero-gui/monero/include -I../src/libwalletqt -I../src/QR-Code-generator -I../src -I../monero/src -isystem /usr/include/PCSC -isystem /usr/include/x86_64-linux-gnu/qt5 -isystem /usr/include/x86_64-linux-gnu/qt5/QtQuick -isystem /usr/include/x86_64-linux-gnu/qt5/QtWidgets -isystem /usr/include/x86_64-linux-gnu/qt5/QtGui -isystem /usr/include/x86_64-linux-gnu/qt5/QtQml -isystem /usr/include/x86_64-linux-gnu/qt5/QtNetwork -isystem /usr/include/x86_64-linux-gnu/qt5/QtCore -I. -isystem /usr/include/libdrm -I/usr/lib/x86_64-linux-gnu/qt5/mkspecs/linux-g++ -o moc_TransactionHistoryModel.o moc_TransactionHistoryModel.cpp
/usr/lib/qt5/bin/moc -DQT_NO_DEBUG -DQT_QUICK_LIB -DQT_WIDGETS_LIB -DQT_GUI_LIB -DQT_QML_LIB -DQT_NETWORK_LIB -DQT_CORE_LIB --include ./moc_predefs.h -I/usr/lib/x86_64-linux-gnu/qt5/mkspecs/linux-g++ -I/home/blackparallax/Programs/xmc-gui/monero-gui -I/home/blackparallax/Programs/xmc-gui/monero-gui/monero/include -I/home/blackparallax/Programs/xmc-gui/monero-gui/src/libwalletqt -I/home/blackparallax/Programs/xmc-gui/monero-gui/src/QR-Code-generator -I/home/blackparallax/Programs/xmc-gui/monero-gui/src -I/home/blackparallax/Programs/xmc-gui/monero-gui/monero/src -I/usr/include/PCSC -I/usr/include/x86_64-linux-gnu/qt5 -I/usr/include/x86_64-linux-gnu/qt5/QtQuick -I/usr/include/x86_64-linux-gnu/qt5/QtWidgets -I/usr/include/x86_64-linux-gnu/qt5/QtGui -I/usr/include/x86_64-linux-gnu/qt5/QtQml -I/usr/include/x86_64-linux-gnu/qt5/QtNetwork -I/usr/include/x86_64-linux-gnu/qt5/QtCore -I. -I/usr/include/c++/7 -I/usr/include/x86_64-linux-gnu/c++/7 -I/usr/include/c++/7/backward -I/usr/lib/gcc/x86_64-linux-gnu/7/include -I/usr/local/include -I/usr/lib/gcc/x86_64-linux-gnu/7/include-fixed -I/usr/include/x86_64-linux-gnu -I/usr/include ../src/model/TransactionHistorySortFilterModel.h -o moc_TransactionHistorySortFilterModel.cpp
g++ -c -pipe -fPIC -fstack-protector -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=1 -Wformat -Wformat-security -fstack-protector -fstack-protector-strong -O2 -std=gnu++11 -pthread -Wall -W -D_REENTRANT -fPIC -DQT_NO_DEBUG -DQT_QUICK_LIB -DQT_WIDGETS_LIB -DQT_GUI_LIB -DQT_QML_LIB -DQT_NETWORK_LIB -DQT_CORE_LIB -I../../monero-gui -I. -I/home/blackparallax/Programs/xmc-gui/monero-gui/monero/include -I../src/libwalletqt -I../src/QR-Code-generator -I../src -I../monero/src -isystem /usr/include/PCSC -isystem /usr/include/x86_64-linux-gnu/qt5 -isystem /usr/include/x86_64-linux-gnu/qt5/QtQuick -isystem /usr/include/x86_64-linux-gnu/qt5/QtWidgets -isystem /usr/include/x86_64-linux-gnu/qt5/QtGui -isystem /usr/include/x86_64-linux-gnu/qt5/QtQml -isystem /usr/include/x86_64-linux-gnu/qt5/QtNetwork -isystem /usr/include/x86_64-linux-gnu/qt5/QtCore -I. -isystem /usr/include/libdrm -I/usr/lib/x86_64-linux-gnu/qt5/mkspecs/linux-g++ -o moc_TransactionHistorySortFilterModel.o moc_TransactionHistorySortFilterModel.cpp
/usr/lib/qt5/bin/moc -DQT_NO_DEBUG -DQT_QUICK_LIB -DQT_WIDGETS_LIB -DQT_GUI_LIB -DQT_QML_LIB -DQT_NETWORK_LIB -DQT_CORE_LIB --include ./moc_predefs.h -I/usr/lib/x86_64-linux-gnu/qt5/mkspecs/linux-g++ -I/home/blackparallax/Programs/xmc-gui/monero-gui -I/home/blackparallax/Programs/xmc-gui/monero-gui/monero/include -I/home/blackparallax/Programs/xmc-gui/monero-gui/src/libwalletqt -I/home/blackparallax/Programs/xmc-gui/monero-gui/src/QR-Code-generator -I/home/blackparallax/Programs/xmc-gui/monero-gui/src -I/home/blackparallax/Programs/xmc-gui/monero-gui/monero/src -I/usr/include/PCSC -I/usr/include/x86_64-linux-gnu/qt5 -I/usr/include/x86_64-linux-gnu/qt5/QtQuick -I/usr/include/x86_64-linux-gnu/qt5/QtWidgets -I/usr/include/x86_64-linux-gnu/qt5/QtGui -I/usr/include/x86_64-linux-gnu/qt5/QtQml -I/usr/include/x86_64-linux-gnu/qt5/QtNetwork -I/usr/include/x86_64-linux-gnu/qt5/QtCore -I. -I/usr/include/c++/7 -I/usr/include/x86_64-linux-gnu/c++/7 -I/usr/include/c++/7/backward -I/usr/lib/gcc/x86_64-linux-gnu/7/include -I/usr/local/include -I/usr/lib/gcc/x86_64-linux-gnu/7/include-fixed -I/usr/include/x86_64-linux-gnu -I/usr/include ../src/model/AddressBookModel.h -o moc_AddressBookModel.cpp
g++ -c -pipe -fPIC -fstack-protector -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=1 -Wformat -Wformat-security -fstack-protector -fstack-protector-strong -O2 -std=gnu++11 -pthread -Wall -W -D_REENTRANT -fPIC -DQT_NO_DEBUG -DQT_QUICK_LIB -DQT_WIDGETS_LIB -DQT_GUI_LIB -DQT_QML_LIB -DQT_NETWORK_LIB -DQT_CORE_LIB -I../../monero-gui -I. -I/home/blackparallax/Programs/xmc-gui/monero-gui/monero/include -I../src/libwalletqt -I../src/QR-Code-generator -I../src -I../monero/src -isystem /usr/include/PCSC -isystem /usr/include/x86_64-linux-gnu/qt5 -isystem /usr/include/x86_64-linux-gnu/qt5/QtQuick -isystem /usr/include/x86_64-linux-gnu/qt5/QtWidgets -isystem /usr/include/x86_64-linux-gnu/qt5/QtGui -isystem /usr/include/x86_64-linux-gnu/qt5/QtQml -isystem /usr/include/x86_64-linux-gnu/qt5/QtNetwork -isystem /usr/include/x86_64-linux-gnu/qt5/QtCore -I. -isystem /usr/include/libdrm -I/usr/lib/x86_64-linux-gnu/qt5/mkspecs/linux-g++ -o moc_AddressBookModel.o moc_AddressBookModel.cpp
/usr/lib/qt5/bin/moc -DQT_NO_DEBUG -DQT_QUICK_LIB -DQT_WIDGETS_LIB -DQT_GUI_LIB -DQT_QML_LIB -DQT_NETWORK_LIB -DQT_CORE_LIB --include ./moc_predefs.h -I/usr/lib/x86_64-linux-gnu/qt5/mkspecs/linux-g++ -I/home/blackparallax/Programs/xmc-gui/monero-gui -I/home/blackparallax/Programs/xmc-gui/monero-gui/monero/include -I/home/blackparallax/Programs/xmc-gui/monero-gui/src/libwalletqt -I/home/blackparallax/Programs/xmc-gui/monero-gui/src/QR-Code-generator -I/home/blackparallax/Programs/xmc-gui/monero-gui/src -I/home/blackparallax/Programs/xmc-gui/monero-gui/monero/src -I/usr/include/PCSC -I/usr/include/x86_64-linux-gnu/qt5 -I/usr/include/x86_64-linux-gnu/qt5/QtQuick -I/usr/include/x86_64-linux-gnu/qt5/QtWidgets -I/usr/include/x86_64-linux-gnu/qt5/QtGui -I/usr/include/x86_64-linux-gnu/qt5/QtQml -I/usr/include/x86_64-linux-gnu/qt5/QtNetwork -I/usr/include/x86_64-linux-gnu/qt5/QtCore -I. -I/usr/include/c++/7 -I/usr/include/x86_64-linux-gnu/c++/7 -I/usr/include/c++/7/backward -I/usr/lib/gcc/x86_64-linux-gnu/7/include -I/usr/local/include -I/usr/lib/gcc/x86_64-linux-gnu/7/include-fixed -I/usr/include/x86_64-linux-gnu -I/usr/include ../src/libwalletqt/AddressBook.h -o moc_AddressBook.cpp
g++ -c -pipe -fPIC -fstack-protector -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=1 -Wformat -Wformat-security -fstack-protector -fstack-protector-strong -O2 -std=gnu++11 -pthread -Wall -W -D_REENTRANT -fPIC -DQT_NO_DEBUG -DQT_QUICK_LIB -DQT_WIDGETS_LIB -DQT_GUI_LIB -DQT_QML_LIB -DQT_NETWORK_LIB -DQT_CORE_LIB -I../../monero-gui -I. -I/home/blackparallax/Programs/xmc-gui/monero-gui/monero/include -I../src/libwalletqt -I../src/QR-Code-generator -I../src -I../monero/src -isystem /usr/include/PCSC -isystem /usr/include/x86_64-linux-gnu/qt5 -isystem /usr/include/x86_64-linux-gnu/qt5/QtQuick -isystem /usr/include/x86_64-linux-gnu/qt5/QtWidgets -isystem /usr/include/x86_64-linux-gnu/qt5/QtGui -isystem /usr/include/x86_64-linux-gnu/qt5/QtQml -isystem /usr/include/x86_64-linux-gnu/qt5/QtNetwork -isystem /usr/include/x86_64-linux-gnu/qt5/QtCore -I. -isystem /usr/include/libdrm -I/usr/lib/x86_64-linux-gnu/qt5/mkspecs/linux-g++ -o moc_AddressBook.o moc_AddressBook.cpp
/usr/lib/qt5/bin/moc -DQT_NO_DEBUG -DQT_QUICK_LIB -DQT_WIDGETS_LIB -DQT_GUI_LIB -DQT_QML_LIB -DQT_NETWORK_LIB -DQT_CORE_LIB --include ./moc_predefs.h -I/usr/lib/x86_64-linux-gnu/qt5/mkspecs/linux-g++ -I/home/blackparallax/Programs/xmc-gui/monero-gui -I/home/blackparallax/Programs/xmc-gui/monero-gui/monero/include -I/home/blackparallax/Programs/xmc-gui/monero-gui/src/libwalletqt -I/home/blackparallax/Programs/xmc-gui/monero-gui/src/QR-Code-generator -I/home/blackparallax/Programs/xmc-gui/monero-gui/src -I/home/blackparallax/Programs/xmc-gui/monero-gui/monero/src -I/usr/include/PCSC -I/usr/include/x86_64-linux-gnu/qt5 -I/usr/include/x86_64-linux-gnu/qt5/QtQuick -I/usr/include/x86_64-linux-gnu/qt5/QtWidgets -I/usr/include/x86_64-linux-gnu/qt5/QtGui -I/usr/include/x86_64-linux-gnu/qt5/QtQml -I/usr/include/x86_64-linux-gnu/qt5/QtNetwork -I/usr/include/x86_64-linux-gnu/qt5/QtCore -I. -I/usr/include/c++/7 -I/usr/include/x86_64-linux-gnu/c++/7 -I/usr/include/c++/7/backward -I/usr/lib/gcc/x86_64-linux-gnu/7/include -I/usr/local/include -I/usr/lib/gcc/x86_64-linux-gnu/7/include-fixed -I/usr/include/x86_64-linux-gnu -I/usr/include ../src/model/SubaddressModel.h -o moc_SubaddressModel.cpp
g++ -c -pipe -fPIC -fstack-protector -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=1 -Wformat -Wformat-security -fstack-protector -fstack-protector-strong -O2 -std=gnu++11 -pthread -Wall -W -D_REENTRANT -fPIC -DQT_NO_DEBUG -DQT_QUICK_LIB -DQT_WIDGETS_LIB -DQT_GUI_LIB -DQT_QML_LIB -DQT_NETWORK_LIB -DQT_CORE_LIB -I../../monero-gui -I. -I/home/blackparallax/Programs/xmc-gui/monero-gui/monero/include -I../src/libwalletqt -I../src/QR-Code-generator -I../src -I../monero/src -isystem /usr/include/PCSC -isystem /usr/include/x86_64-linux-gnu/qt5 -isystem /usr/include/x86_64-linux-gnu/qt5/QtQuick -isystem /usr/include/x86_64-linux-gnu/qt5/QtWidgets -isystem /usr/include/x86_64-linux-gnu/qt5/QtGui -isystem /usr/include/x86_64-linux-gnu/qt5/QtQml -isystem /usr/include/x86_64-linux-gnu/qt5/QtNetwork -isystem /usr/include/x86_64-linux-gnu/qt5/QtCore -I. -isystem /usr/include/libdrm -I/usr/lib/x86_64-linux-gnu/qt5/mkspecs/linux-g++ -o moc_SubaddressModel.o moc_SubaddressModel.cpp
/usr/lib/qt5/bin/moc -DQT_NO_DEBUG -DQT_QUICK_LIB -DQT_WIDGETS_LIB -DQT_GUI_LIB -DQT_QML_LIB -DQT_NETWORK_LIB -DQT_CORE_LIB --include ./moc_predefs.h -I/usr/lib/x86_64-linux-gnu/qt5/mkspecs/linux-g++ -I/home/blackparallax/Programs/xmc-gui/monero-gui -I/home/blackparallax/Programs/xmc-gui/monero-gui/monero/include -I/home/blackparallax/Programs/xmc-gui/monero-gui/src/libwalletqt -I/home/blackparallax/Programs/xmc-gui/monero-gui/src/QR-Code-generator -I/home/blackparallax/Programs/xmc-gui/monero-gui/src -I/home/blackparallax/Programs/xmc-gui/monero-gui/monero/src -I/usr/include/PCSC -I/usr/include/x86_64-linux-gnu/qt5 -I/usr/include/x86_64-linux-gnu/qt5/QtQuick -I/usr/include/x86_64-linux-gnu/qt5/QtWidgets -I/usr/include/x86_64-linux-gnu/qt5/QtGui -I/usr/include/x86_64-linux-gnu/qt5/QtQml -I/usr/include/x86_64-linux-gnu/qt5/QtNetwork -I/usr/include/x86_64-linux-gnu/qt5/QtCore -I. -I/usr/include/c++/7 -I/usr/include/x86_64-linux-gnu/c++/7 -I/usr/include/c++/7/backward -I/usr/lib/gcc/x86_64-linux-gnu/7/include -I/usr/local/include -I/usr/lib/gcc/x86_64-linux-gnu/7/include-fixed -I/usr/include/x86_64-linux-gnu -I/usr/include ../src/libwalletqt/Subaddress.h -o moc_Subaddress.cpp
g++ -c -pipe -fPIC -fstack-protector -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=1 -Wformat -Wformat-security -fstack-protector -fstack-protector-strong -O2 -std=gnu++11 -pthread -Wall -W -D_REENTRANT -fPIC -DQT_NO_DEBUG -DQT_QUICK_LIB -DQT_WIDGETS_LIB -DQT_GUI_LIB -DQT_QML_LIB -DQT_NETWORK_LIB -DQT_CORE_LIB -I../../monero-gui -I. -I/home/blackparallax/Programs/xmc-gui/monero-gui/monero/include -I../src/libwalletqt -I../src/QR-Code-generator -I../src -I../monero/src -isystem /usr/include/PCSC -isystem /usr/include/x86_64-linux-gnu/qt5 -isystem /usr/include/x86_64-linux-gnu/qt5/QtQuick -isystem /usr/include/x86_64-linux-gnu/qt5/QtWidgets -isystem /usr/include/x86_64-linux-gnu/qt5/QtGui -isystem /usr/include/x86_64-linux-gnu/qt5/QtQml -isystem /usr/include/x86_64-linux-gnu/qt5/QtNetwork -isystem /usr/include/x86_64-linux-gnu/qt5/QtCore -I. -isystem /usr/include/libdrm -I/usr/lib/x86_64-linux-gnu/qt5/mkspecs/linux-g++ -o moc_Subaddress.o moc_Subaddress.cpp
/usr/lib/qt5/bin/moc -DQT_NO_DEBUG -DQT_QUICK_LIB -DQT_WIDGETS_LIB -DQT_GUI_LIB -DQT_QML_LIB -DQT_NETWORK_LIB -DQT_CORE_LIB --include ./moc_predefs.h -I/usr/lib/x86_64-linux-gnu/qt5/mkspecs/linux-g++ -I/home/blackparallax/Programs/xmc-gui/monero-gui -I/home/blackparallax/Programs/xmc-gui/monero-gui/monero/include -I/home/blackparallax/Programs/xmc-gui/monero-gui/src/libwalletqt -I/home/blackparallax/Programs/xmc-gui/monero-gui/src/QR-Code-generator -I/home/blackparallax/Programs/xmc-gui/monero-gui/src -I/home/blackparallax/Programs/xmc-gui/monero-gui/monero/src -I/usr/include/PCSC -I/usr/include/x86_64-linux-gnu/qt5 -I/usr/include/x86_64-linux-gnu/qt5/QtQuick -I/usr/include/x86_64-linux-gnu/qt5/QtWidgets -I/usr/include/x86_64-linux-gnu/qt5/QtGui -I/usr/include/x86_64-linux-gnu/qt5/QtQml -I/usr/include/x86_64-linux-gnu/qt5/QtNetwork -I/usr/include/x86_64-linux-gnu/qt5/QtCore -I. -I/usr/include/c++/7 -I/usr/include/x86_64-linux-gnu/c++/7 -I/usr/include/c++/7/backward -I/usr/lib/gcc/x86_64-linux-gnu/7/include -I/usr/local/include -I/usr/lib/gcc/x86_64-linux-gnu/7/include-fixed -I/usr/include/x86_64-linux-gnu -I/usr/include ../src/libwalletqt/UnsignedTransaction.h -o moc_UnsignedTransaction.cpp
g++ -c -pipe -fPIC -fstack-protector -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=1 -Wformat -Wformat-security -fstack-protector -fstack-protector-strong -O2 -std=gnu++11 -pthread -Wall -W -D_REENTRANT -fPIC -DQT_NO_DEBUG -DQT_QUICK_LIB -DQT_WIDGETS_LIB -DQT_GUI_LIB -DQT_QML_LIB -DQT_NETWORK_LIB -DQT_CORE_LIB -I../../monero-gui -I. -I/home/blackparallax/Programs/xmc-gui/monero-gui/monero/include -I../src/libwalletqt -I../src/QR-Code-generator -I../src -I../monero/src -isystem /usr/include/PCSC -isystem /usr/include/x86_64-linux-gnu/qt5 -isystem /usr/include/x86_64-linux-gnu/qt5/QtQuick -isystem /usr/include/x86_64-linux-gnu/qt5/QtWidgets -isystem /usr/include/x86_64-linux-gnu/qt5/QtGui -isystem /usr/include/x86_64-linux-gnu/qt5/QtQml -isystem /usr/include/x86_64-linux-gnu/qt5/QtNetwork -isystem /usr/include/x86_64-linux-gnu/qt5/QtCore -I. -isystem /usr/include/libdrm -I/usr/lib/x86_64-linux-gnu/qt5/mkspecs/linux-g++ -o moc_UnsignedTransaction.o moc_UnsignedTransaction.cpp
/usr/lib/qt5/bin/moc -DQT_NO_DEBUG -DQT_QUICK_LIB -DQT_WIDGETS_LIB -DQT_GUI_LIB -DQT_QML_LIB -DQT_NETWORK_LIB -DQT_CORE_LIB --include ./moc_predefs.h -I/usr/lib/x86_64-linux-gnu/qt5/mkspecs/linux-g++ -I/home/blackparallax/Programs/xmc-gui/monero-gui -I/home/blackparallax/Programs/xmc-gui/monero-gui/monero/include -I/home/blackparallax/Programs/xmc-gui/monero-gui/src/libwalletqt -I/home/blackparallax/Programs/xmc-gui/monero-gui/src/QR-Code-generator -I/home/blackparallax/Programs/xmc-gui/monero-gui/src -I/home/blackparallax/Programs/xmc-gui/monero-gui/monero/src -I/usr/include/PCSC -I/usr/include/x86_64-linux-gnu/qt5 -I/usr/include/x86_64-linux-gnu/qt5/QtQuick -I/usr/include/x86_64-linux-gnu/qt5/QtWidgets -I/usr/include/x86_64-linux-gnu/qt5/QtGui -I/usr/include/x86_64-linux-gnu/qt5/QtQml -I/usr/include/x86_64-linux-gnu/qt5/QtNetwork -I/usr/include/x86_64-linux-gnu/qt5/QtCore -I. -I/usr/include/c++/7 -I/usr/include/x86_64-linux-gnu/c++/7 -I/usr/include/c++/7/backward -I/usr/lib/gcc/x86_64-linux-gnu/7/include -I/usr/local/include -I/usr/lib/gcc/x86_64-linux-gnu/7/include-fixed -I/usr/include/x86_64-linux-gnu -I/usr/include ../MainApp.h -o moc_MainApp.cpp
g++ -c -pipe -fPIC -fstack-protector -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=1 -Wformat -Wformat-security -fstack-protector -fstack-protector-strong -O2 -std=gnu++11 -pthread -Wall -W -D_REENTRANT -fPIC -DQT_NO_DEBUG -DQT_QUICK_LIB -DQT_WIDGETS_LIB -DQT_GUI_LIB -DQT_QML_LIB -DQT_NETWORK_LIB -DQT_CORE_LIB -I../../monero-gui -I. -I/home/blackparallax/Programs/xmc-gui/monero-gui/monero/include -I../src/libwalletqt -I../src/QR-Code-generator -I../src -I../monero/src -isystem /usr/include/PCSC -isystem /usr/include/x86_64-linux-gnu/qt5 -isystem /usr/include/x86_64-linux-gnu/qt5/QtQuick -isystem /usr/include/x86_64-linux-gnu/qt5/QtWidgets -isystem /usr/include/x86_64-linux-gnu/qt5/QtGui -isystem /usr/include/x86_64-linux-gnu/qt5/QtQml -isystem /usr/include/x86_64-linux-gnu/qt5/QtNetwork -isystem /usr/include/x86_64-linux-gnu/qt5/QtCore -I. -isystem /usr/include/libdrm -I/usr/lib/x86_64-linux-gnu/qt5/mkspecs/linux-g++ -o moc_MainApp.o moc_MainApp.cpp
/usr/lib/qt5/bin/moc -DQT_NO_DEBUG -DQT_QUICK_LIB -DQT_WIDGETS_LIB -DQT_GUI_LIB -DQT_QML_LIB -DQT_NETWORK_LIB -DQT_CORE_LIB --include ./moc_predefs.h -I/usr/lib/x86_64-linux-gnu/qt5/mkspecs/linux-g++ -I/home/blackparallax/Programs/xmc-gui/monero-gui -I/home/blackparallax/Programs/xmc-gui/monero-gui/monero/include -I/home/blackparallax/Programs/xmc-gui/monero-gui/src/libwalletqt -I/home/blackparallax/Programs/xmc-gui/monero-gui/src/QR-Code-generator -I/home/blackparallax/Programs/xmc-gui/monero-gui/src -I/home/blackparallax/Programs/xmc-gui/monero-gui/monero/src -I/usr/include/PCSC -I/usr/include/x86_64-linux-gnu/qt5 -I/usr/include/x86_64-linux-gnu/qt5/QtQuick -I/usr/include/x86_64-linux-gnu/qt5/QtWidgets -I/usr/include/x86_64-linux-gnu/qt5/QtGui -I/usr/include/x86_64-linux-gnu/qt5/QtQml -I/usr/include/x86_64-linux-gnu/qt5/QtNetwork -I/usr/include/x86_64-linux-gnu/qt5/QtCore -I. -I/usr/include/c++/7 -I/usr/include/x86_64-linux-gnu/c++/7 -I/usr/include/c++/7/backward -I/usr/lib/gcc/x86_64-linux-gnu/7/include -I/usr/local/include -I/usr/lib/gcc/x86_64-linux-gnu/7/include-fixed -I/usr/include/x86_64-linux-gnu -I/usr/include ../src/daemon/DaemonManager.h -o moc_DaemonManager.cpp
g++ -c -pipe -fPIC -fstack-protector -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=1 -Wformat -Wformat-security -fstack-protector -fstack-protector-strong -O2 -std=gnu++11 -pthread -Wall -W -D_REENTRANT -fPIC -DQT_NO_DEBUG -DQT_QUICK_LIB -DQT_WIDGETS_LIB -DQT_GUI_LIB -DQT_QML_LIB -DQT_NETWORK_LIB -DQT_CORE_LIB -I../../monero-gui -I. -I/home/blackparallax/Programs/xmc-gui/monero-gui/monero/include -I../src/libwalletqt -I../src/QR-Code-generator -I../src -I../monero/src -isystem /usr/include/PCSC -isystem /usr/include/x86_64-linux-gnu/qt5 -isystem /usr/include/x86_64-linux-gnu/qt5/QtQuick -isystem /usr/include/x86_64-linux-gnu/qt5/QtWidgets -isystem /usr/include/x86_64-linux-gnu/qt5/QtGui -isystem /usr/include/x86_64-linux-gnu/qt5/QtQml -isystem /usr/include/x86_64-linux-gnu/qt5/QtNetwork -isystem /usr/include/x86_64-linux-gnu/qt5/QtCore -I. -isystem /usr/include/libdrm -I/usr/lib/x86_64-linux-gnu/qt5/mkspecs/linux-g++ -o moc_DaemonManager.o moc_DaemonManager.cpp
g++ -fstack-protector -pie -Wl,-z,relro -Wl,-z,now -Wl,-z,noexecstack -Wl,-O1 -o release/bin/monero-wallet-gui main.o filter.o clipboardAdapter.o oscursor.o WalletManager.o Wallet.o PendingTransaction.o TransactionHistory.o TransactionInfo.o QRCodeImageProvider.o oshelper.o TranslationManager.o TransactionHistoryModel.o TransactionHistorySortFilterModel.o BitBuffer.o QrCode.o QrSegment.o AddressBookModel.o AddressBook.o SubaddressModel.o Subaddress.o zxcvbn.o UnsignedTransaction.o Logger.o MainApp.o DaemonManager.o qrc_translations.o qrc_qml.o moc_filter.o moc_clipboardAdapter.o moc_oscursor.o moc_WalletManager.o moc_Wallet.o moc_PendingTransaction.o moc_TransactionHistory.o moc_TransactionInfo.o moc_Transfer.o moc_NetworkType.o moc_oshelper.o moc_TranslationManager.o moc_TransactionHistoryModel.o moc_TransactionHistorySortFilterModel.o moc_AddressBookModel.o moc_AddressBook.o moc_SubaddressModel.o moc_Subaddress.o moc_UnsignedTransaction.o moc_MainApp.o moc_DaemonManager.o   -L/home/blackparallax/Programs/xmc-gui/monero-gui/monero/lib -lwallet_merged -lepee -lunbound -leasylogging -ldl -lboost_serialization -lboost_thread -lboost_system -lboost_date_time -lboost_filesystem -lboost_regex -lboost_chrono -lboost_program_options -lssl -llmdb -lcrypto -Wl,-Bdynamic -lpcsclite -lQt5Quick -lQt5Widgets -lQt5Gui -lQt5Qml -lQt5Network -lQt5Core -lGL -lpthread 
/usr/bin/ld: cannot find -lwallet_merged
/usr/bin/ld: cannot find -lepee
/usr/bin/ld: cannot find -leasylogging
/usr/bin/ld: cannot find -llmdb
collect2: error: ld returned 1 exit status
Makefile:294: recipe for target 'release/bin/monero-wallet-gui' failed
make: *** [release/bin/monero-wallet-gui] Error 1
blackparallax@JAG-Yoga:~/Programs/xmc-gui/monero-gui$ 


## sanderfoobar | 2018-10-12T15:06:46+00:00
You're using `https://github.com/monero-classic/monero-gui.git`, please open the issue there. This issue tracker is for xmr, not xmc.

+invalid

# Action History
- Created by: ghost | 2018-10-12T04:56:45+00:00
- Closed at: 2018-10-12T15:09:27+00:00
