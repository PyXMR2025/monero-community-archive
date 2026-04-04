---
title: Zlib & armv8a
source_url: https://github.com/monero-project/monero/issues/4478
author: zpaxyrco
assignees: []
labels: []
created_at: '2018-09-30T20:45:21+00:00'
updated_at: '2018-10-10T15:41:05+00:00'
type: issue
status: closed
closed_at: '2018-10-10T15:41:05+00:00'
---

# Original Description
zlib wont compile on android armv8a
on armv7a everything ok

Sending build context to Docker daemon  471.8MB

Step 1/46 : FROM debian:stable
 ---> 86f2c18bd3d4
Step 2/46 : RUN apt-get update && apt-get install -y unzip automake build-essential curl file pkg-config git python libtool
 ---> Using cache
 ---> 2f9e40f1396e
Step 3/46 : WORKDIR /opt/android
 ---> Using cache
 ---> 21dc1a89e813
Step 4/46 : ENV ANDROID_SDK_REVISION 4333796
 ---> Using cache
 ---> d2f5640cb83e
Step 5/46 : ENV ANDROID_SDK_HASH 92ffee5a1d98d856634e8b71132e8a95d96c83a63fde1099be3d86df3106def9
 ---> Using cache
 ---> ee2d72af9e36
Step 6/46 : RUN curl -s -O https://dl.google.com/android/repository/sdk-tools-linux-${ANDROID_SDK_REVISION}.zip     && echo "${ANDROID_SDK_HASH}  sdk-tools-linux-${ANDROID_SDK_REVISION}.zip" | sha256sum -c     && unzip sdk-tools-linux-${ANDROID_SDK_REVISION}.zip     && rm -f sdk-tools-linux-${ANDROID_SDK_REVISION}.zip
 ---> Using cache
 ---> 6381f368138a
Step 7/46 : ENV ANDROID_NDK_REVISION 17b
 ---> Using cache
 ---> e5733ee0fbda
Step 8/46 : ENV ANDROID_NDK_HASH 5dfbbdc2d3ba859fed90d0e978af87c71a91a5be1f6e1c40ba697503d48ccecd
 ---> Using cache
 ---> 7be78f4a5e64
Step 9/46 : RUN curl -s -O https://dl.google.com/android/repository/android-ndk-r${ANDROID_NDK_REVISION}-linux-x86_64.zip     && echo "${ANDROID_NDK_HASH}  android-ndk-r${ANDROID_NDK_REVISION}-linux-x86_64.zip" | sha256sum -c     && unzip android-ndk-r${ANDROID_NDK_REVISION}-linux-x86_64.zip     && rm -f android-ndk-r${ANDROID_NDK_REVISION}-linux-x86_64.zip
 ---> Using cache
 ---> 5dfd51666674
Step 10/46 : ENV WORKDIR /opt/android
 ---> Using cache
 ---> b3b34963b7d7
Step 11/46 : ENV ANDROID_SDK_ROOT ${WORKDIR}/tools
 ---> Using cache
 ---> 3bf87010b7cc
Step 12/46 : ENV ANDROID_NDK_ROOT ${WORKDIR}/android-ndk-r${ANDROID_NDK_REVISION}
 ---> Using cache
 ---> d26d08ee0eeb
Step 13/46 : ENV PREFIX /opt/android/prefix
 ---> Using cache
 ---> 25f792ec0080
Step 14/46 : ENV TOOLCHAIN_DIR ${WORKDIR}/toolchain-arm
 ---> Using cache
 ---> f38ad74ba632
Step 15/46 : RUN ${ANDROID_NDK_ROOT}/build/tools/make_standalone_toolchain.py         --arch arm64          --api 21          --install-dir ${TOOLCHAIN_DIR}          --stl=libc++
 ---> Using cache
 ---> e656d66c0440
Step 16/46 : ENV CMAKE_VERSION 3.12.1
 ---> Using cache
 ---> c90893c37c8e
Step 17/46 : RUN cd /usr     && curl -s -O https://cmake.org/files/v3.12/cmake-${CMAKE_VERSION}-Linux-x86_64.tar.gz     && tar -xzf /usr/cmake-${CMAKE_VERSION}-Linux-x86_64.tar.gz     && rm -f /usr/cmake-${CMAKE_VERSION}-Linux-x86_64.tar.gz
 ---> Using cache
 ---> a180b81f94df
Step 18/46 : ENV PATH /usr/cmake-${CMAKE_VERSION}-Linux-x86_64/bin:$PATH
 ---> Using cache
 ---> 28d5fb8fa802
Step 19/46 : ARG BOOST_VERSION=1_68_0
 ---> Using cache
 ---> b893fa5e4f93
Step 20/46 : ARG BOOST_VERSION_DOT=1.68.0
 ---> Using cache
 ---> c81362330b96
Step 21/46 : ARG BOOST_HASH=7f6130bc3cf65f56a618888ce9d5ea704fa10b462be126ad053e80e553d6d8b7
 ---> Using cache
 ---> ede3ab0aa56f
Step 22/46 : RUN set -ex     && curl -s -L -o  boost_${BOOST_VERSION}.tar.bz2 https://dl.bintray.com/boostorg/release/${BOOST_VERSION_DOT}/source/boost_${BOOST_VERSION}.tar.bz2     && echo "${BOOST_HASH}  boost_${BOOST_VERSION}.tar.bz2" | sha256sum -c     && tar -xvf boost_${BOOST_VERSION}.tar.bz2     && rm -f boost_${BOOST_VERSION}.tar.bz2     && cd boost_${BOOST_VERSION}     && ./bootstrap.sh --prefix=${PREFIX}
 ---> Using cache
 ---> 4b9bb7c0c4fc
Step 23/46 : ENV HOST_PATH $PATH
 ---> Using cache
 ---> bd46a25bc987
Step 24/46 : ENV PATH $TOOLCHAIN_DIR/aarch64-linux-android/bin:$TOOLCHAIN_DIR/bin:$PATH
 ---> Using cache
 ---> 8a46d6c1008c
Step 25/46 : ARG NPROC=1
 ---> Using cache
 ---> 815d7a42eca0
Step 26/46 : ENV ICONV_VERSION 1.15
 ---> Using cache
 ---> 6200b10e06d0
Step 27/46 : ENV ICONV_HASH  ccf536620a45458d26ba83887a983b96827001e92a13847b45e4925cc8913178
 ---> Using cache
 ---> 11c6395d64d6
Step 28/46 : RUN curl -s -O http://ftp.gnu.org/pub/gnu/libiconv/libiconv-${ICONV_VERSION}.tar.gz     && echo "${ICONV_HASH}  libiconv-${ICONV_VERSION}.tar.gz" | sha256sum -c     && tar -xzf libiconv-${ICONV_VERSION}.tar.gz     && rm -f libiconv-${ICONV_VERSION}.tar.gz     && cd libiconv-${ICONV_VERSION}     && CC=aarch64-linux-android-clang CXX=aarch64-linux-android-clang++ ./configure --build=x86_64-linux-gnu --host=aarch64 --prefix=${PREFIX} --disable-rpath     && make -j${NPROC} && make install
 ---> Using cache
 ---> 964d08fc81d4
Step 29/46 : RUN cd boost_${BOOST_VERSION}     && ./b2 --build-type=minimal link=static runtime-link=static --with-chrono --with-date_time --with-filesystem --with-program_options --with-regex --with-serialization --with-system --with-thread --with-locale --build-dir=android --stagedir=android toolset=clang threading=multi threadapi=pthread target-os=android -sICONV_PATH=${PREFIX} install -j${NPROC}
 ---> Using cache
 ---> cf1f9e19eb39
Step 30/46 : ENV ZLIB_VERSION 1.2.11
 ---> Using cache
 ---> fdbefdff6f9d
Step 31/46 : ENV ZLIB_HASH c3e5e9fdd5004dcb542feda5ee4f0ff0744628baf8ed2dd5d66f8ca1197cb1a1
 ---> Using cache
 ---> 10d04d5be795
Step 32/46 : RUN curl -s -O https://zlib.net/zlib-${ZLIB_VERSION}.tar.gz     && echo "${ZLIB_HASH}  zlib-${ZLIB_VERSION}.tar.gz" | sha256sum -c     && tar -xzf zlib-${ZLIB_VERSION}.tar.gz     && rm zlib-${ZLIB_VERSION}.tar.gz     && mv zlib-${ZLIB_VERSION} zlib     && cd zlib && CC=clang CXX=clang ./configure --static     && make -j${NPROC}
 ---> Running in 61fa5d7ba22b
The command '/bin/sh -c curl -s -O https://zlib.net/zlib-${ZLIB_VERSION}.tar.gz     && echo "${ZLIB_HASH}  zlib-${ZLIB_VERSION}.tar.gz" | sha256sum -c     && tar -xzf zlib-${ZLIB_VERSION}.tar.gz     && rm zlib-${ZLIB_VERSION}.tar.gz     && mv zlib-${ZLIB_VERSION} zlib     && cd zlib && CC=clang CXX=clang ./configure --static     && make -j${NPROC}' returned a non-zero code: 7

# Discussion History
## moneromooo-monero | 2018-10-01T15:01:28+00:00
Find the logs. I have no idea where this build system puts them.


## moneromooo-monero | 2018-10-01T15:02:46+00:00
Or do those steps one at a time to see which one breaks.

## glemercier | 2018-10-07T17:13:17+00:00
I was able to build monero for Android armv8 using a special Dockerfile I wrote based on the armv7 version: https://github.com/glemercier/monero/commit/33a03054ba465a51ddd1072ae3c7498541683aaa

The only build issue I found was in libzmq, I fixed it and submitted a PR to libzmq (https://github.com/zeromq/libzmq/pull/3267), in the meantime the Dockerfile points to my forked repo of libzmq. I may submit this as a PR to monero whenever we can rely on an officially fixed version of libzmq. 

## moneromooo-monero | 2018-10-10T15:34:01+00:00
+resolved

# Action History
- Created by: zpaxyrco | 2018-09-30T20:45:21+00:00
- Closed at: 2018-10-10T15:41:05+00:00
