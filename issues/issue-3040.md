---
title: Android docker file
source_url: https://github.com/monero-project/monero-gui/issues/3040
author: selsta
assignees: []
labels: []
created_at: '2020-08-10T10:55:21+00:00'
updated_at: '2021-01-15T12:09:53+00:00'
type: issue
status: closed
closed_at: '2021-01-15T12:09:53+00:00'
---

# Original Description
From IRC, needs some modifications to work with master

```
FROM debian:unstable
RUN apt-get update && apt-get install -y unzip automake build-essential curl file pkg-config git python3 libtool wget libtinfo5
RUN dpkg --add-architecture i386 \
    && apt-get update \
    && apt-get install -y libc6:i386 libncurses5:i386 libstdc++6:i386 libz1:i386 \
    && apt-get install -y ca-certificates-java openjdk-8-jdk-headless openjdk-8-jre-headless ant
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64
ENV PATH $JAVA_HOME/bin:$PATH
WORKDIR /opt/android
ARG NPROC=26
## INSTALL ANDROID SDK
ENV ANDROID_SDK_REVISION 4333796
ENV ANDROID_SDK_HASH 92ffee5a1d98d856634e8b71132e8a95d96c83a63fde1099be3d86df3106def9
RUN curl -s -O https://dl.google.com/android/repository/sdk-tools-linux-${ANDROID_SDK_REVISION}.zip \
    && echo "${ANDROID_SDK_HASH}  sdk-tools-linux-${ANDROID_SDK_REVISION}.zip" | sha256sum -c \
    && unzip sdk-tools-linux-${ANDROID_SDK_REVISION}.zip \
    && rm -f sdk-tools-linux-${ANDROID_SDK_REVISION}.zip

## INSTALL ANDROID NDK
ENV ANDROID_NDK_REVISION 21d
ENV ANDROID_NDK_HASH bcf4023eb8cb6976a4c7cff0a8a8f145f162bf4d
RUN curl -s -O https://dl.google.com/android/repository/android-ndk-r${ANDROID_NDK_REVISION}-linux-x86_64.zip \
    && echo "${ANDROID_NDK_HASH}  android-ndk-r${ANDROID_NDK_REVISION}-linux-x86_64.zip" | shasum -c \
    && unzip android-ndk-r${ANDROID_NDK_REVISION}-linux-x86_64.zip \
    && rm -f android-ndk-r${ANDROID_NDK_REVISION}-linux-x86_64.zip

ENV WORKDIR /opt/android
ENV ANDROID_SDK_ROOT ${WORKDIR}/tools
ENV ANDROID_NDK_ROOT ${WORKDIR}/android-ndk-r${ANDROID_NDK_REVISION}
ENV PREFIX /opt/android/prefix

ENV TOOLCHAIN_DIR ${ANDROID_NDK_ROOT}/toolchains/llvm/prebuilt/linux-x86_64

ENV CMAKE_VERSION 3.18.1
ARG CMAKE_HASH=537de8ad3a7fb4ec9b8517870db255802ad211aec00002c651e178848f7a769e
RUN  cd /usr \
     && wget https://github.com/Kitware/CMake/releases/download/v3.18.1/cmake-3.18.1-Linux-x86_64.tar.gz \
     && echo "${CMAKE_HASH}  /usr/cmake-${CMAKE_VERSION}-Linux-x86_64.tar.gz" | sha256sum -c \
     && tar -xzf /usr/cmake-3.18.1-Linux-x86_64.tar.gz \
     && rm -f /usr/cmake-3.18.1-Linux-x86_64.tar.gz

ENV PATH /usr/cmake-${CMAKE_VERSION}-Linux-x86_64/bin:$PATH

## Boost
ARG BOOST_VERSION=1_73_0
ARG BOOST_VERSION_DOT=1.73.0
ARG BOOST_HASH=4eb3b8d442b426dc35346235c8733b5ae35ba431690e38c6a8263dce9fcbb402
RUN set -ex \
    && curl -s -L -o  boost_${BOOST_VERSION}.tar.bz2 https://dl.bintray.com/boostorg/release/${BOOST_VERSION_DOT}/source/boost_${BOOST_VERSION}.tar.bz2 \
    && echo "${BOOST_HASH}  boost_${BOOST_VERSION}.tar.bz2" | sha256sum -c \
    && tar -xvf boost_${BOOST_VERSION}.tar.bz2 \
    && rm -f boost_${BOOST_VERSION}.tar.bz2 \
    && cd boost_${BOOST_VERSION} \
    && ./bootstrap.sh --prefix=${PREFIX}

ENV HOST_PATH $PATH
ENV PATH $TOOLCHAIN_DIR/aarch64-linux-android/bin:$TOOLCHAIN_DIR/bin:$PATH

ENV PATH ${ANDROID_NDK_ROOT}/toolchains/llvm/prebuilt/linux-x86_64/bin:$PATH
# Build iconv for lib boost locale
ENV ICONV_VERSION 1.16
ENV ICONV_HASH  ccf536620a45458d26ba83887a983b96827001e92a13847b45e4925cc8913178
RUN curl -s -O http://ftp.gnu.org/pub/gnu/libiconv/libiconv-${ICONV_VERSION}.tar.gz \
    #&& echo "${ICONV_HASH}  libiconv-${ICONV_VERSION}.tar.gz" | sha256sum -c \
    && tar -xzf libiconv-${ICONV_VERSION}.tar.gz \
    && rm -f libiconv-${ICONV_VERSION}.tar.gz \
    && cd libiconv-${ICONV_VERSION} \
    && CC=aarch64-linux-android28-clang CXX=aarch64-linux-android28-clang++ ./configure --build=x86_64-linux-gnu --host=aarch64 --prefix=${PREFIX} --disable-rpath \
    && make -j${NPROC} && make install

## Build BOOST
RUN cd boost_${BOOST_VERSION} \
    && ./b2 --build-type=minimal link=static runtime-link=static --with-chrono --with-date_time --with-filesystem --with-program_options --with-regex --with-serialization --with-system --with-thread --with-locale --build-dir=android --stagedir=android toolset=clang threading=multi threadapi=pthread target-os=android -sICONV_PATH=${PREFIX} install -j${NPROC}

# download, configure and make Zlib
ENV ZLIB_VERSION 1.2.11
ENV ZLIB_HASH c3e5e9fdd5004dcb542feda5ee4f0ff0744628baf8ed2dd5d66f8ca1197cb1a1
RUN curl -s -O https://zlib.net/zlib-${ZLIB_VERSION}.tar.gz \
    && echo "${ZLIB_HASH}  zlib-${ZLIB_VERSION}.tar.gz" | sha256sum -c \
    && tar -xzf zlib-${ZLIB_VERSION}.tar.gz \
    && rm zlib-${ZLIB_VERSION}.tar.gz \
    && mv zlib-${ZLIB_VERSION} zlib \
    && cd zlib && CC=aarch64-linux-android28-clang CXX=aarch64-linux-android28-clang++ ./configure --static \
    && make -j${NPROC}

ENV ANDROID_NDK_HOME ${WORKDIR}/android-ndk-r${ANDROID_NDK_REVISION}
# open ssl
ARG OPENSSL_VERSION=1.1.1g
ARG OPENSSL_HASH=ddb04774f1e32f0c49751e21b67216ac87852ceb056b75209af2443400636d46
RUN curl -s -O https://www.openssl.org/source/openssl-${OPENSSL_VERSION}.tar.gz \
    && echo "${OPENSSL_HASH}  openssl-${OPENSSL_VERSION}.tar.gz" | sha256sum -c \
    && tar -xzf openssl-${OPENSSL_VERSION}.tar.gz \
    && rm openssl-${OPENSSL_VERSION}.tar.gz \
    && cd openssl-${OPENSSL_VERSION} \
    && ./Configure CC=aarch64-linux-android28-clang CXX=aarch64-linux-android28-clang++ \
          android-arm64 \
          no-asm \
         no-shared --static \
         --with-zlib-include=${WORKDIR}/zlib/include --with-zlib-lib=${WORKDIR}/zlib/lib \
          --prefix=${PREFIX} --openssldir=${PREFIX} \
    && sed -i 's/CNF_EX_LIBS=-ldl -pthread//g;s/BIN_CFLAGS=-pie $(CNF_CFLAGS) $(CFLAGS)//g' Makefile \
    && make -j${NPROC} \
    && make -j${NPROC} install

# ZMQ
ARG ZMQ_VERSION=master
ARG ZMQ_HASH=501d0815bf2b0abb93be8214fc66519918ef6c40
RUN git clone https://github.com/zeromq/libzmq.git -b ${ZMQ_VERSION} \
    && cd libzmq \
    && git checkout ${ZMQ_HASH} \
    && ./autogen.sh \
    && CC=aarch64-linux-android28-clang CXX=aarch64-linux-android28-clang++ ./configure --prefix=${PREFIX} --host=aarch64-linux-android --enable-static --disable-shared \
    && make -j${NPROC} \
    && make -j${NPROC} install

# Sodium
ARG SODIUM_VERSION=1.0.18
ARG SODIUM_HASH=4f5e89fa84ce1d178a6765b8b46f2b6f91216677
RUN set -ex \
    && git clone https://github.com/jedisct1/libsodium.git -b ${SODIUM_VERSION} \
    && cd libsodium \
    && test `git rev-parse HEAD` = ${SODIUM_HASH} || exit 1 \
    && ./autogen.sh \
    && CC=aarch64-linux-android28-clang CXX=aarch64-linux-android28-clang++ ./configure --prefix=${PREFIX} --host=aarch64-linux-android --enable-static --disable-shared \
    && make  -j${NPROC} \
    && make install

#Get Qt
ENV QT_VERSION 5.15

RUN git clone git://code.qt.io/qt/qt5.git -b ${QT_VERSION} \
    && cd qt5 \
    && perl init-repository

ENV ANDROID_API android-28

#ANDROID SDK TOOLS
RUN rm -rf /opt/android/boost_1_73_0/libs/wave/test/testwave/testfiles/utf8-test-*
RUN cd ${ANDROID_SDK_ROOT} && echo y | ./bin/sdkmanager "platform-tools" "platforms;${ANDROID_API}" "tools"

RUN cp -r ${WORKDIR}/platforms ${WORKDIR}/platform-tools ${ANDROID_SDK_ROOT}

ENV HOST_PATH $JAVA_HOME/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${ANDROID_SDK_ROOT}/bin

ENV PKG_CONFIG /usr/bin/pkg-config
#build Qt
RUN cd qt5 \
    #&& sed -i '649{s/,//g};1426{s/,//g};650,660d;1427,1431d' qtbase/configure.json \
    && PATH=${HOST_PATH} ./configure -v -developer-build -release \
    -xplatform android-clang \
    -android-ndk-platform ${ANDROID_API} \
    -android-ndk $ANDROID_NDK_ROOT \
    -android-sdk $ANDROID_SDK_ROOT \
    -android-ndk-host linux-x86_64 \
    #-android-toolchain-version 4.9 \
    #--sysroot=/opt/android/android-ndk-r17b/sysroot \
    #--disable-rpath \
    #pkg-config \
    -no-dbus\
    #-no-pch \
    -no-qpa-platform-guard \
    -opengl es2 \
    -no-use-gold-linker \
    -no-sql-mysql \
    #-optimize-size \
    -opensource -confirm-license \
    -android-arch arm64-v8a \
    -prefix ${WORKDIR}/Qt-${QT_VERSION} \
    -nomake tools -nomake tests -nomake examples \
    -skip qtwebengine \
    -skip qtserialport \
    -skip qtconnectivity \
    -skip qttranslations \
    -skip qtpurchasing \
    -skip qtgamepad -skip qtscript -skip qtdoc \
    -no-warnings-are-errors \
    #&& sed -i '213,215d' qtbase/src/3rdparty/pcre2/src/sljit/sljitConfigInternal.h \
    && PATH=${HOST_PATH} make -j${NPROC} module-qtwebsockets module-qtvirtualkeyboard module-qtsvg \
    module-qtwayland module-qtwebglplugin module-qtquickcontrols module-qtquickcontrols2 \
    module-qtlocation module-qtdeclarative module-qtgraphicaleffects module-qtmultimedia \
    && PATH=${HOST_PATH} make install

# Get ZBar
RUN git clone https://github.com/ZBar/ZBar.git

ENV PATH ${ANDROID_SDK_ROOT}/bin:${WORKDIR}/Qt-${QT_VERSION}/bin:${WORKDIR}/tools:$PATH

#Build libzbarjni.a
RUN wget https://raw.githubusercontent.com/monero-project/monero-gui/master/android/docker/android.mk.patch && cp android.mk.patch ${WORKDIR}/ZBar
RUN cd ZBar \
    && git apply android.mk.patch \
    && sed -i '15d;80d' android/jni/Android.mk \
    && echo \
"APP_ABI := arm64-v8a \n\
APP_STL := c++_shared \n\
TARGET_PLATFORM := ${ANDROID_API} \n\
TARGET_ARCH_ABI := arm64-v8a \n\
APP_CFLAGS +=  -target aarch64-none-linux-android -fexceptions -fstack-protector-strong -fno-limit-debug-info -mfloat-abi=softfp -fno-builtin-memmove -fno-omit-frame-pointer -fno-stack-protector\n"\
        >> android/jni/Application.mk \
    && cd android \
    && CC=aarch64-linux-android28-clang CXX=aarch64-linux-android28-clang++ ${ANDROID_NDK_ROOT}/ndk-build ICONV_SRC=${WORKDIR}/libiconv-${ICONV_VERSION} -B V=1 NDK_APPLICATION_MK=jni/Application.mk

RUN cp ZBar/android/obj/local/arm64-v8a/lib* ${ANDROID_NDK_ROOT}/platforms/${ANDROID_API}/arch-arm64/usr/lib

RUN cp -r ${PREFIX}/lib/* ${ANDROID_NDK_ROOT}/platforms/${ANDROID_API}/arch-arm64/usr/lib

ENV PATH ${WORKDIR}/Qt-${QT_VERSION}/bin:${JAVA_HOME}/bin:/usr/cmake-${CMAKE_VERSION}-Linux-x86_64/bin:${ANDROID_SDK_ROOT}/bin:${WORKDIR}/tools:$TOOLCHAIN_DIR/aarch64-linux-android/bin:$TOOLCHAIN_DIR/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH

# Since r26.0.0, old binary `android` has been removed but is stil used by androiddeployqt
# So using older binary `android` as a workaround
RUN cd tools && curl -O http://dl-ssl.google.com/android/repository/tools_r25.2.5-linux.zip \
  && unzip tools_r25.2.5-linux.zip \
  && rm -f tools_r25.2.5-linux.zip \
  && echo y | $ANDROID_SDK_ROOT/tools/android update sdk --no-ui --all --filter build-tools-28.0.3

RUN git clone --recursive https://github.com/monero-project/monero-gui
#ADD . ${WORKDIR}/monero-gui
RUN  cd ${WORKDIR}/monero-gui \
  && CMAKE_INCLUDE_PATH="${PREFIX}/include" \
     CMAKE_LIBRARY_PATH="${PREFIX}/lib" \
CC=aarch64-linux-android28-clang CXX=aarch64-linux-android28-clang++ \
 #      ANDROID_STANDALONE_TOOLCHAIN_PATH=${TOOLCHAIN_DIR} \
           ./build.sh release-android -j26

RUN cd ${WORKDIR}/monero-gui/build && PATH=${HOST_PATH} make deploy
```

# Discussion History
## xiphon | 2021-01-15T12:09:53+00:00
Monero GUI Android docker file has been reworked in v0.17.1.4 release.

# Action History
- Created by: selsta | 2020-08-10T10:55:21+00:00
- Closed at: 2021-01-15T12:09:53+00:00
