---
title: Android gui
source_url: https://github.com/monero-project/monero-gui/issues/1555
author: takelberry41
assignees: []
labels:
- resolved
created_at: '2018-09-04T13:27:01+00:00'
updated_at: '2018-09-27T13:45:23+00:00'
type: issue
status: closed
closed_at: '2018-09-27T13:45:23+00:00'
---

# Original Description
i'm trying to compile latest gui for android.
For some reason patch cant happen on main.cpp
If will be released official gui for android(70% of smartphones)
monero will go in the sky.
Is very easy for core devs to do that!
Why not until now?

Sending build context to Docker daemon  791.3MB^M
ESC[91m[WARNING]: Empty continuation line found in:
    RUN git clone https://github.com/ZBar/ZBar.git ENV PATH /opt/android/tools:/opt/android/tools/platform-tools:${WORKDIR}/Qt-${QT_VERSION}/bin:$PATH
[WARNING]: Empty continuation lines will become errors in a future release.
ESC[0mStep 1/25 : FROM monero-android64
 ---> 775e8baa08eb
Step 2/25 : RUN echo "deb http://ftp.fr.debian.org/debian/ stable-backports main contrib non-free" >> /etc/apt/sources.list
 ---> Using cache
 ---> 39e61ef003f9
Step 3/25 : RUN dpkg --add-architecture i386     && apt-get update     && apt-get install -y libc6:i386 libncurses5:i386 libstdc++6:i386 libz1:i386     && apt-get install -y -t stretch-backports ca-certificates-
java openjdk-8-jdk-headless openjdk-8-jre-headless ant
 ---> Using cache
 ---> a969dec24efe
Step 4/25 : ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64
 ---> Using cache
 ---> cba9234be9bf
Step 5/25 : ENV PATH $JAVA_HOME/bin:$PATH
 ---> Using cache
 ---> 7c2a5bae52cc
Step 6/25 : ENV QT_VERSION 5.12
 ---> Using cache
 ---> 1ba5931c6204
Step 7/25 : RUN git clone git://code.qt.io/qt/qt5.git -b ${QT_VERSION}     && cd qt5     && perl init-repository
 ---> Using cache
 ---> 09c5a4db9f76
Step 8/25 : RUN cp -r qt5/qtbase/mkspecs/android-clang qt5/qtbase/mkspecs/android-clang-libc     && cd qt5/qtbase/mkspecs/android-clang-libc     && sed -i '16i ANDROID_SOURCES_CXX_STL_LIBDIR = $$NDK_ROOT/sources/cxx-stl/llvm-libc++/libs/$$ANDROID_TARGET_ARCH' qmake.conf     && sed -i '17i ANDROID_SOURCES_CXX_STL_INCDIR = $$NDK_ROOT/sources/cxx-stl/llvm-libc++/include' qmake.conf     && echo "QMAKE_LIBS_PRIVATE      = -lc++_shared -llog -lz -lm -ldl -lc -lgcc " >> qmake.conf     && echo "QMAKE_CFLAGS -= -mfpu=vfp " >> qmake.conf     && echo "QMAKE_CXXFLAGS -= -mfpu=vfp " >> qmake.conf     && echo "QMAKE_CFLAGS += -mfpu=vfp4 " >> qmake.conf     && echo "QMAKE_CXXFLAGS += -mfpu=vfp4 " >> qmake.conf
 ---> Using cache
 ---> 902432b26701
Step 9/25 : ENV ANDROID_API android-21
 ---> Using cache
 ---> 631b0d4f6566
Step 10/25 : RUN echo y | /opt/android/tools/android update sdk --no-ui --all --filter platform-tools
 ---> Using cache
 ---> c4df9699650e
Step 11/25 : RUN echo y | /opt/android/tools/android update sdk --no-ui --all --filter ${ANDROID_API}
 ---> Using cache
 ---> 47f60e323a8c
Step 12/25 : RUN echo y | /opt/android/tools/android update sdk --no-ui --all --filter build-tools-25.0.1
 ---> Using cache
 ---> d536a6c9bce2
Step 13/25 : ENV CLEAN_PATH $JAVA_HOME/bin:/usr/cmake-3.12.1-Linux-x86_64/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
 ---> Using cache
 ---> ea372d6780b8
Step 14/25 : RUN cd qt5 && PATH=${CLEAN_PATH} ./configure -developer-build -release     -xplatform android-clang-libc     -android-ndk-platform ${ANDROID_API}     -android-ndk $ANDROID_NDK_ROOT     -android-sdk $ANDROID_SDK_ROOT     -opensource -confirm-license     -prefix ${WORKDIR}/Qt-${QT_VERSION}     -nomake tests -nomake examples     -skip qtserialport     -skip qtconnectivity     -skip qttranslations     -skip qtgamepad -skip qtscript -skip qtdoc
 ---> Using cache
 ---> a8809ea542e0
Step 15/25 : COPY android/docker/androiddeployqt.patch qt5/qttools/androiddeployqt.patch
 ---> Using cache
 ---> b9a15fe421fa
Step 16/25 : COPY android/docker/main.cpp qt5/qttools
 ---> Using cache
 ---> 1d104c16e46c
Step 17/25 : RUN cd qt5/qttools     && git apply androiddeployqt.patch     && cd ..     && PATH=${CLEAN_PATH} make -j10     && PATH=${CLEAN_PATH} make install
 ---> Running in 6017b9ddcde5
ESC[91mwarning: main.cpp has type 100755, expected 100644
ESC[0mESC[91merror: patch failed: main.cpp:1122
error: main.cpp: patch does not apply
ESC[0mThe command '/bin/sh -c cd qt5/qttools     && git apply androiddeployqt.patch     && cd ..     && PATH=${CLEAN_PATH} make -j10     && PATH=${CLEAN_PATH} make install' returned a non-zero code: 1
(END)


# Discussion History
## MoroccanMalinois | 2018-09-04T19:15:58+00:00
> For some reason patch cant happen on main.cpp

You changed `QT_VERSION` from `5.8` to `5.12` and changes in that patch have been integrated in Qt.

Btw, even if you succeed to build it (i have a patch that i'll submit soon-ish), it's currently not usable (can't switch tabs ...).

> If will be released official gui for android(70% of smartphones)
> monero will go in the sky.

This is a bug tracker, please use other platforms (like IRC/reddit/...) for non technical discussions.

## takelberry41 | 2018-09-04T19:49:53+00:00
Not usable even if i compile?
so for what reason dockerfile,android details etc

## takelberry41 | 2018-09-04T20:50:49+00:00
now i have smth else

Dockerfile start with "from monero..."
succesful build for command line armv8.

for some reason is trying to compile for amrv7 and not armv8.

how to choose right arch?

/opt/android/android-ndk-r17b/toolchains/llvm/prebuilt/linux-x86_64/bin/clang -c -D__ANDROID_API__=21 -target armv7-none-linux-androideabi -gcc-toolchain /opt/android/android-ndk-r17b/toolchains/arm-linux-androideabi-4.9/prebuilt/linux-x86_64 -DANDROID_HAS_WSTRING --sysroot=/opt/android/android-ndk-r17b/sysroot -isystem /opt/android/android-ndk-r17b/sysroot/usr/include/arm-linux-androideabi -isystem /opt/android/android-ndk-r17b/sources/cxx-stl/llvm-libc++/include -isystem /opt/android/android-ndk-r17b/sources/android/support/include -isystem /opt/android/android-ndk-r17b/sources/cxx-stl/llvm-libc++abi/include -fstack-protector-strong -DANDROID -march=armv7-a -mfloat-abi=softfp -fno-builtin-memmove -mfpu=vfp4 -mthumb -Oz -fPIC -std=gnu11 -fvisibility=hidden -fno-exceptions -DQT_NO_NARROWING_CONVERSIONS_IN_CONNECT -DPNG_ARM_NEON_OPT=0 -DQT_NO_EXCEPTIONS -I. -I. -I../../../mkspecs/android-clang-libc -o .obj/png.o png.c

make[3]: Leaving directory '/opt/android/qt5/qtbase/src/tools/bootstrap'
make[2]: Leaving directory '/opt/android/qt5/qtbase/src'
make[1]: *** [sub-src-make_first] Error 2
Makefile:48: recipe for target 'sub-src-make_first' failed
make[1]: Leaving directory '/opt/android/qt5/qtbase'
make: *** [module-qtbase-make_first] Error 2
Makefile:77: recipe for target 'module-qtbase-make_first' failed
The command '/bin/sh -c cd qt5     && PATH=${CLEAN_PATH} make -j10     && PATH=${CLEAN_PATH} make install' returned a non-zero code: 2


## takelberry41 | 2018-09-04T20:53:50+00:00
Dockerfile
https://pastebin.com/v26iGMc6

## ayoubmtd | 2018-09-07T19:45:35+00:00
I am always getting this error when running `docker build -t monero-gui-android .`
```
Step 1/23 : FROM monero-android64
pull access denied for monero-android64, repository does not exist or may require 'docker login'
```
even with @takelberry41 dockerfiles gives the same error, I mean with changing to `FROM monero-android64`

Any idea why this error is happening ?


## MoroccanMalinois | 2018-09-24T23:17:55+00:00
#1571 

## dEBRUYNE-1 | 2018-09-27T13:36:57+00:00
+resolved

# Action History
- Created by: takelberry41 | 2018-09-04T13:27:01+00:00
- Closed at: 2018-09-27T13:45:23+00:00
