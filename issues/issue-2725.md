---
title: Android docker build failed
source_url: https://github.com/monero-project/monero/issues/2725
author: Senecarus
assignees: []
labels: []
created_at: '2017-10-24T17:35:08+00:00'
updated_at: '2017-12-13T21:40:32+00:00'
type: issue
status: closed
closed_at: '2017-12-13T21:40:32+00:00'
---

# Original Description
When i try to build android32 library with docker i get a some errors. Errors related to BOOST version is possible to fix by changing Cmake version to new in script code.

But I can't fix last error, "Could not find required header zmq.hpp"




Last login: Tue Oct 24 20:25:10 on ttys000
MacBook-Pro-2:monero XXXX$ cd utils/build_scripts/ && docker build -f android32.Dockerfile -t monero-android .
Sending build context to Docker daemon   16.9kB
Step 1/24 : FROM debian:jessie
 ---> 40aa6d4339d4
Step 2/24 : RUN apt-get update && apt-get install -y unzip automake build-essential curl file pkg-config git python
 ---> Using cache
 ---> a47f4e51fb4c
Step 3/24 : WORKDIR /opt/android
 ---> Using cache
 ---> 9aafc8bfaba1
Step 4/24 : RUN curl -s -O http://dl.google.com/android/android-sdk_r24.4.1-linux.tgz     && tar --no-same-owner -xzf android-sdk_r24.4.1-linux.tgz     && rm -f android-sdk_r24.4.1-linux.tgz
 ---> Using cache
 ---> a2b3ba49f949
Step 5/24 : ENV ANDROID_NDK_REVISION 14
 ---> Using cache
 ---> 34c7821a2cab
Step 6/24 : RUN curl -s -O https://dl.google.com/android/repository/android-ndk-r${ANDROID_NDK_REVISION}-linux-x86_64.zip     && unzip android-ndk-r${ANDROID_NDK_REVISION}-linux-x86_64.zip     && rm -f android-ndk-r${ANDROID_NDK_REVISION}-linux-x86_64.zip
 ---> Using cache
 ---> a0ac92ae827d
Step 7/24 : ENV WORKDIR /opt/android
 ---> Using cache
 ---> 36bbda2347df
Step 8/24 : ENV ANDROID_SDK_ROOT ${WORKDIR}/android-sdk-linux
 ---> Using cache
 ---> f47a5b9f074c
Step 9/24 : ENV ANDROID_NDK_ROOT ${WORKDIR}/android-ndk-r${ANDROID_NDK_REVISION}
 ---> Using cache
 ---> 33faabd39a2e
Step 10/24 : ENV BOOST_VERSION 1_62_0
 ---> Using cache
 ---> 212525916a39
Step 11/24 : ENV BOOST_VERSION_DOT 1.62.0
 ---> Using cache
 ---> be1a36b73bfe
Step 12/24 : RUN curl -s -L -o  boost_${BOOST_VERSION}.tar.bz2 https://sourceforge.net/projects/boost/files/boost/${BOOST_VERSION_DOT}/boost_${BOOST_VERSION}.tar.bz2/download     && tar -xvf boost_${BOOST_VERSION}.tar.bz2     && rm -f /usr/boost_${BOOST_VERSION}.tar.bz2     && cd boost_${BOOST_VERSION}     && ./bootstrap.sh
 ---> Using cache
 ---> 403ee9708f1e
Step 13/24 : ENV TOOLCHAIN_DIR ${WORKDIR}/toolchain-arm
 ---> Using cache
 ---> e6837ba86e49
Step 14/24 : RUN ${ANDROID_NDK_ROOT}/build/tools/make_standalone_toolchain.py          --arch arm          --api 21          --install-dir $TOOLCHAIN_DIR          --stl=libc++
 ---> Using cache
 ---> 2fe6ac1ea07d
Step 15/24 : ENV PATH $TOOLCHAIN_DIR/arm-linux-androideabi/bin:$TOOLCHAIN_DIR/bin:$PATH
 ---> Using cache
 ---> 3b0c169dee30
Step 16/24 : RUN cd boost_${BOOST_VERSION}     && ./b2 --build-type=minimal link=static runtime-link=static --with-chrono --with-date_time --with-filesystem --with-program_options --with-regex --with-serialization --with-system --with-thread --build-dir=android32 --stagedir=android32 toolset=clang threading=multi threadapi=pthread target-os=android stage
 ---> Using cache
 ---> ca4bb5983ba5
Step 17/24 : ENV CMAKE_VERSION 3.6.3
 ---> Using cache
 ---> 9ee10c7d2b9b
Step 18/24 : RUN cd /usr     && curl -s -O https://cmake.org/files/v3.6/cmake-${CMAKE_VERSION}-Linux-x86_64.tar.gz     && tar -xzf /usr/cmake-${CMAKE_VERSION}-Linux-x86_64.tar.gz     && rm -f /usr/cmake-${CMAKE_VERSION}-Linux-x86_64.tar.gz
 ---> Using cache
 ---> 3ac736192d45
Step 19/24 : ENV PATH /usr/cmake-${CMAKE_VERSION}-Linux-x86_64/bin:$PATH
 ---> Using cache
 ---> 015ea31f659a
Step 20/24 : ENV ZLIB_VERSION 1.2.11
 ---> Using cache
 ---> 58c2ff8bc042
Step 21/24 : RUN curl -s -O http://zlib.net/zlib-${ZLIB_VERSION}.tar.gz     && tar -xzf zlib-${ZLIB_VERSION}.tar.gz     && rm zlib-${ZLIB_VERSION}.tar.gz     && mv zlib-${ZLIB_VERSION} zlib     && cd zlib && CC=clang CXX=clang++ ./configure --static     && make
 ---> Using cache
 ---> ba245af50d8d
Step 22/24 : ENV OPENSSL_VERSION 1.0.2j
 ---> Using cache
 ---> e607fdbb546c
Step 23/24 : RUN curl -s -O https://www.openssl.org/source/openssl-${OPENSSL_VERSION}.tar.gz     && tar -xzf openssl-${OPENSSL_VERSION}.tar.gz     && rm openssl-${OPENSSL_VERSION}.tar.gz     && cd openssl-${OPENSSL_VERSION}     && sed -i -e "s/mandroid/target\ armv7\-none\-linux\-androideabi/" Configure     && CC=clang CXX=clang++            ./Configure android-armv7            no-asm            no-shared --static            --with-zlib-include=${WORKDIR}/zlib/include --with-zlib-lib=${WORKDIR}/zlib/lib     && make build_crypto build_ssl     && cd .. && mv openssl-${OPENSSL_VERSION}  openssl
 ---> Using cache
 ---> f428ea51410c
Step 24/24 : RUN git clone https://github.com/monero-project/monero.git     && cd monero     && mkdir -p build/release     && CC=clang CXX=clang++          BOOST_ROOT=${WORKDIR}/boost_${BOOST_VERSION} BOOST_LIBRARYDIR=${WORKDIR}/boost_${BOOST_VERSION}/android32/lib/          OPENSSL_ROOT_DIR=${WORKDIR}/openssl/          make release-static-android
 ---> Running in 93dd768a02b5
Cloning into 'monero'...
mkdir -p build/release
cd build/release && cmake -D BUILD_TESTS=OFF -D ARCH="armv7-a" -D STATIC=ON -D BUILD_64=OFF -D CMAKE_BUILD_TYPE=release -D ANDROID=true -D INSTALL_VENDORED_LIBUNBOUND=ON -D BUILD_TAG="android" ../.. && make
-- The C compiler identification is Clang 3.8.275480
-- The CXX compiler identification is Clang 3.8.275480
-- Check for working C compiler: /opt/android/toolchain-arm/bin/clang
-- Check for working C compiler: /opt/android/toolchain-arm/bin/clang -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Detecting C compile features
-- Detecting C compile features - done
-- Check for working CXX compiler: /opt/android/toolchain-arm/bin/clang++
-- Check for working CXX compiler: /opt/android/toolchain-arm/bin/clang++ -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Building build tag android
-- Could not find DEVELOPER_LOCAL_TOOLS in env (not required)
-- BOOST_IGNORE_SYSTEM_PATHS defaults to OFF
-- Could not find DEVELOPER_LIBUNBOUND_OLD in env (not required)
-- Building for a 32-bit system
-- Building internal libraries as static
-- Could not find DATABASE in env (not required unless you want to change database type from default: lmdb)
-- Using LMDB as default DB type
-- Stack trace on exception disabled
-- Looking for pthread.h
-- Looking for pthread.h - found
-- Looking for pthread_create
-- Looking for pthread_create - found
-- Found Threads: TRUE  
-- Found OpenSSL: /opt/android/openssl/libssl.a;/opt/android/openssl/libcrypto.a (found version "1.0.2j") 
-- Using OpenSSL include dir at /opt/android/openssl/include
-- Could NOT find MiniUPnPc (missing:  MINIUPNP_INCLUDE_DIR MINIUPNP_LIBRARY) 
-- Using miniupnpc from local source tree for static build
-- Looking for libunbound
-- Looking for arpa/inet.h
-- Looking for arpa/inet.h - found
-- Looking for endian.h
-- Looking for endian.h - found
-- Looking for dlfcn.h
-- Looking for dlfcn.h - found
-- Looking for event.h
-- Looking for event.h - not found
-- Looking for getopt.h
-- Looking for getopt.h - found
-- Looking for glob.h
-- Looking for glob.h - not found
-- Looking for grp.h
-- Looking for grp.h - found
-- Looking for inttypes.h
-- Looking for inttypes.h - found
-- Looking for iphlpapi.h
-- Looking for iphlpapi.h - not found
-- Looking for login_cap.h
-- Looking for login_cap.h - not found
-- Looking for memory.h
-- Looking for memory.h - found
-- Looking for netdb.h
-- Looking for netdb.h - found
-- Looking for netinet/in.h
-- Looking for netinet/in.h - found
-- Looking for pthread.h
-- Looking for pthread.h - found
-- Looking for pwd.h
-- Looking for pwd.h - found
-- Looking for stdarg.h
-- Looking for stdarg.h - found
-- Looking for stdbool.h
-- Looking for stdbool.h - found
-- Looking for stdint.h
-- Looking for stdint.h - found
-- Looking for stdlib.h
-- Looking for stdlib.h - found
-- Looking for strings.h
-- Looking for strings.h - found
-- Looking for string.h
-- Looking for string.h - found
-- Looking for sys/param.h
-- Looking for sys/param.h - found
-- Looking for sys/resource.h
-- Looking for sys/resource.h - found
-- Looking for sys/sha2.h
-- Looking for sys/sha2.h - not found
-- Looking for sys/socket.h
-- Looking for sys/socket.h - found
-- Looking for sys/stat.h
-- Looking for sys/stat.h - found
-- Looking for sys/sysctl.h
-- Looking for sys/sysctl.h - not found
-- Looking for sys/types.h
-- Looking for sys/types.h - found
-- Looking for sys/uio.h
-- Looking for sys/uio.h - found
-- Looking for sys/un.h
-- Looking for sys/un.h - found
-- Looking for sys/wait.h
-- Looking for sys/wait.h - found
-- Looking for syslog.h
-- Looking for syslog.h - found
-- Looking for time.h
-- Looking for time.h - found
-- Looking for unistd.h
-- Looking for unistd.h - found
-- Looking for vfork.h
-- Looking for vfork.h - not found
-- Looking for windows.h
-- Looking for windows.h - not found
-- Looking for winsock2.h
-- Looking for winsock2.h - not found
-- Looking for ws2tcpip.h
-- Looking for ws2tcpip.h - not found
-- Looking for _beginthreadex
-- Looking for _beginthreadex - not found
-- Looking for arc4random
-- Looking for arc4random - found
-- Looking for arc4random_uniform
-- Looking for arc4random_uniform - found
-- Looking for chown
-- Looking for chown - found
-- Looking for chroot
-- Looking for chroot - found
-- Looking for ctime_r
-- Looking for ctime_r - found
-- Looking for daemon
-- Looking for daemon - found
-- Looking for endprotoent
-- Looking for endprotoent - not found
-- Looking for endservent
-- Looking for endservent - found
-- Looking for fork
-- Looking for fork - found
-- Looking for fseeko
-- Looking for fseeko - found
-- Looking for fsync
-- Looking for fsync - found
-- Looking for getauxval
-- Looking for getauxval - found
-- Looking for getentropy
-- Looking for getentropy - not found
-- Looking for getpwnam
-- Looking for getpwnam - found
-- Looking for getrlimit
-- Looking for getrlimit - found
-- Looking for glob
-- Looking for glob - not found
-- Looking for gmtime_r
-- Looking for gmtime_r - found
-- Looking for fcntl
-- Looking for fcntl - found
-- Looking for inet_aton
-- Looking for inet_aton - found
-- Looking for inet_ntop
-- Looking for inet_ntop - found
-- Looking for inet_pton
-- Looking for inet_pton - found
-- Looking for initgroups
-- Looking for initgroups - found
-- Looking for ioctlsocket
-- Looking for ioctlsocket - not found
-- Looking for isblank
-- Looking for isblank - found
-- Looking for kill
-- Looking for kill - found
-- Looking for localtime_r
-- Looking for localtime_r - found
-- Looking for malloc
-- Looking for malloc - found
-- Looking for memmove
-- Looking for memmove - found
-- Looking for random
-- Looking for random - found
-- Looking for reallocarray
-- Looking for reallocarray - not found
-- Looking for recvmsg
-- Looking for recvmsg - found
-- Looking for sbrk
-- Looking for sbrk - found
-- Looking for sendmsg
-- Looking for sendmsg - found
-- Looking for setregid
-- Looking for setregid - found
-- Looking for setresgid
-- Looking for setresgid - found
-- Looking for setresuid
-- Looking for setresuid - found
-- Looking for setreuid
-- Looking for setreuid - found
-- Looking for setrlimit
-- Looking for setrlimit - found
-- Looking for setsid
-- Looking for setsid - found
-- Looking for setusercontent
-- Looking for setusercontent - not found
-- Looking for sigprocmask
-- Looking for sigprocmask - found
-- Looking for sleep
-- Looking for sleep - found
-- Looking for snprintf
-- Looking for snprintf - found
-- Looking for socketpair
-- Looking for socketpair - found
-- Looking for srandom
-- Looking for srandom - found
-- Looking for strsep
-- Looking for strsep - found
-- Looking for strftime
-- Looking for strftime - found
-- Looking for strlcat
-- Looking for strlcat - found
-- Looking for strlcpy
-- Looking for strlcpy - found
-- Looking for strptime
-- Looking for strptime - found
-- Looking for tzset
-- Looking for tzset - found
-- Looking for usleep
-- Looking for usleep - found
-- Looking for writev
-- Looking for writev - found
-- Looking for getaddrinfo
-- Looking for getaddrinfo - found
-- Looking for stddef.h
-- Looking for stddef.h - found
-- Check size of time_t
-- Check size of time_t - done
-- Check size of gid_t
-- Check size of gid_t - done
-- Check size of in_addr_t
-- Check size of in_addr_t - failed
-- Check size of in_port_t
-- Check size of in_port_t - failed
-- Check size of int16_t
-- Check size of int16_t - done
-- Check size of int32_t
-- Check size of int32_t - done
-- Check size of int64_t
-- Check size of int64_t - done
-- Check size of int8_t
-- Check size of int8_t - done
-- Check size of pid_t
-- Check size of pid_t - done
-- Check size of rlim_t
-- Check size of rlim_t - done
-- Check size of ssize_t
-- Check size of ssize_t - done
-- Check size of uid_t
-- Check size of uid_t - done
-- Check size of uint16_t
-- Check size of uint16_t - done
-- Check size of uint32_t
-- Check size of uint32_t - done
-- Check size of uint64_t
-- Check size of uint64_t - done
-- Check size of uint8_t
-- Check size of uint8_t - done
-- Looking for PTHREAD_PRIO_INHERIT
-- Looking for PTHREAD_PRIO_INHERIT - not found
-- Looking for pthread_rwlock_t
-- Looking for pthread_rwlock_t - not found
-- Looking for pthread_spinlock_t
-- Looking for pthread_spinlock_t - not found
-- Looking for openssl/conf.h
-- Looking for openssl/conf.h - found
-- Looking for openssl/engine.h
-- Looking for openssl/engine.h - found
-- Looking for openssl/err.h
-- Looking for openssl/err.h - found
-- Looking for openssl/rand.h
-- Looking for openssl/rand.h - found
-- Looking for openssl/ssl.h
-- Looking for openssl/ssl.h - found
-- Looking for NID_secp384r1
-- Looking for NID_secp384r1 - not found
-- Looking for NID_X9_62_prime256v1
-- Looking for NID_X9_62_prime256v1 - not found
-- Looking for sk_SSL_COMP_pop_free
-- Looking for sk_SSL_COMP_pop_free - not found
-- Looking for SSL_COMP_get_compression_methods
-- Looking for SSL_COMP_get_compression_methods - not found
-- Looking for EVP_MD_CTX_new
-- Looking for EVP_MD_CTX_new - not found
-- Looking for EVP_sha1
-- Looking for EVP_sha1 - found
-- Looking for EVP_sha256
-- Looking for EVP_sha256 - found
-- Looking for EVP_sha512
-- Looking for EVP_sha512 - found
-- Looking for FIPS_mode
-- Looking for FIPS_mode - found
-- Looking for HMAC_Update
-- Looking for HMAC_Update - found
-- Looking for OPENSSL_config
-- Looking for OPENSSL_config - not found
-- Looking for SHA512_Update
-- Looking for SHA512_Update - found
-- Found PkgConfig: /usr/bin/pkg-config (found version "0.28") 
-- Using 32-bit LMDB from source tree
-- Building on x86_64 for armv7-a
-- AES support not available on ARMv7
-- Setting FPU Flags for ARM Processors
-- Checking to see if CXX compiler accepts flag -mfpu=vfp3-d16
-- Checking to see if CXX compiler accepts flag -mfpu=vfp3-d16 - yes
-- Checking to see if CXX compiler accepts flag -mfpu=vfp4
-- Checking to see if CXX compiler accepts flag -mfpu=vfp4 - yes
-- Checking to see if CXX compiler accepts flag -mfloat-abi=hard
-- Checking to see if CXX compiler accepts flag -mfloat-abi=hard - no
-- Checking to see if CXX compiler accepts flag -mfloat-abi=softfp
-- Checking to see if CXX compiler accepts flag -mfloat-abi=softfp - yes
-- Selecting VFP4 for ARMv7
-- Setting Software ABI for Floating Point
-- Enabling PIE executable
CMake Warning at /usr/cmake-3.6.3-Linux-x86_64/share/cmake-3.6/Modules/FindBoost.cmake:743 (message):
  Imported targets not available for Boost version 106200
Call Stack (most recent call first):
  /usr/cmake-3.6.3-Linux-x86_64/share/cmake-3.6/Modules/FindBoost.cmake:842 (_Boost_COMPONENT_DEPENDENCIES)
  /usr/cmake-3.6.3-Linux-x86_64/share/cmake-3.6/Modules/FindBoost.cmake:1395 (_Boost_MISSING_DEPENDENCIES)
  CMakeLists.txt:654 (find_package)


CMake Warning at /usr/cmake-3.6.3-Linux-x86_64/share/cmake-3.6/Modules/FindBoost.cmake:743 (message):
  Imported targets not available for Boost version 106200
Call Stack (most recent call first):
  /usr/cmake-3.6.3-Linux-x86_64/share/cmake-3.6/Modules/FindBoost.cmake:842 (_Boost_COMPONENT_DEPENDENCIES)
  /usr/cmake-3.6.3-Linux-x86_64/share/cmake-3.6/Modules/FindBoost.cmake:1395 (_Boost_MISSING_DEPENDENCIES)
  CMakeLists.txt:654 (find_package)


CMake Warning at /usr/cmake-3.6.3-Linux-x86_64/share/cmake-3.6/Modules/FindBoost.cmake:743 (message):
  Imported targets not available for Boost version 106200
Call Stack (most recent call first):
  /usr/cmake-3.6.3-Linux-x86_64/share/cmake-3.6/Modules/FindBoost.cmake:842 (_Boost_COMPONENT_DEPENDENCIES)
  /usr/cmake-3.6.3-Linux-x86_64/share/cmake-3.6/Modules/FindBoost.cmake:1395 (_Boost_MISSING_DEPENDENCIES)
  CMakeLists.txt:654 (find_package)


CMake Warning at /usr/cmake-3.6.3-Linux-x86_64/share/cmake-3.6/Modules/FindBoost.cmake:743 (message):
  Imported targets not available for Boost version 106200
Call Stack (most recent call first):
  /usr/cmake-3.6.3-Linux-x86_64/share/cmake-3.6/Modules/FindBoost.cmake:842 (_Boost_COMPONENT_DEPENDENCIES)
  /usr/cmake-3.6.3-Linux-x86_64/share/cmake-3.6/Modules/FindBoost.cmake:1395 (_Boost_MISSING_DEPENDENCIES)
  CMakeLists.txt:654 (find_package)


CMake Warning at /usr/cmake-3.6.3-Linux-x86_64/share/cmake-3.6/Modules/FindBoost.cmake:743 (message):
  Imported targets not available for Boost version 106200
Call Stack (most recent call first):
  /usr/cmake-3.6.3-Linux-x86_64/share/cmake-3.6/Modules/FindBoost.cmake:842 (_Boost_COMPONENT_DEPENDENCIES)
  /usr/cmake-3.6.3-Linux-x86_64/share/cmake-3.6/Modules/FindBoost.cmake:1395 (_Boost_MISSING_DEPENDENCIES)
  CMakeLists.txt:654 (find_package)


CMake Warning at /usr/cmake-3.6.3-Linux-x86_64/share/cmake-3.6/Modules/FindBoost.cmake:743 (message):
  Imported targets not available for Boost version 106200
Call Stack (most recent call first):
  /usr/cmake-3.6.3-Linux-x86_64/share/cmake-3.6/Modules/FindBoost.cmake:842 (_Boost_COMPONENT_DEPENDENCIES)
  /usr/cmake-3.6.3-Linux-x86_64/share/cmake-3.6/Modules/FindBoost.cmake:1395 (_Boost_MISSING_DEPENDENCIES)
  CMakeLists.txt:654 (find_package)


CMake Warning at /usr/cmake-3.6.3-Linux-x86_64/share/cmake-3.6/Modules/FindBoost.cmake:743 (message):
  Imported targets not available for Boost version 106200
Call Stack (most recent call first):
  /usr/cmake-3.6.3-Linux-x86_64/share/cmake-3.6/Modules/FindBoost.cmake:842 (_Boost_COMPONENT_DEPENDENCIES)
  /usr/cmake-3.6.3-Linux-x86_64/share/cmake-3.6/Modules/FindBoost.cmake:1395 (_Boost_MISSING_DEPENDENCIES)
  CMakeLists.txt:654 (find_package)


CMake Warning at /usr/cmake-3.6.3-Linux-x86_64/share/cmake-3.6/Modules/FindBoost.cmake:743 (message):
  Imported targets not available for Boost version 106200
Call Stack (most recent call first):
  /usr/cmake-3.6.3-Linux-x86_64/share/cmake-3.6/Modules/FindBoost.cmake:842 (_Boost_COMPONENT_DEPENDENCIES)
  /usr/cmake-3.6.3-Linux-x86_64/share/cmake-3.6/Modules/FindBoost.cmake:1395 (_Boost_MISSING_DEPENDENCIES)
  CMakeLists.txt:654 (find_package)


-- Found Boost Version: 106200
-- Could NOT find Readline (missing:  Readline_INCLUDE_DIR Readline_LIBRARY) 
-- Performing Test GNU_READLINE_FOUND
-- Performing Test GNU_READLINE_FOUND - Failed
-- Could not find GNU readline library so building without readline support
-- Found Git: /usr/bin/git
CMake Error at CMakeLists.txt:708 (message):
  Could not find required header zmq.hpp


-- Configuring incomplete, errors occurred!
See also "/opt/android/monero/build/release/CMakeFiles/CMakeOutput.log".
See also "/opt/android/monero/build/release/CMakeFiles/CMakeError.log".
make: *** [release-static-android] Error 1
The command '/bin/sh -c git clone https://github.com/monero-project/monero.git     && cd monero     && mkdir -p build/release     && CC=clang CXX=clang++          BOOST_ROOT=${WORKDIR}/boost_${BOOST_VERSION} BOOST_LIBRARYDIR=${WORKDIR}/boost_${BOOST_VERSION}/android32/lib/          OPENSSL_ROOT_DIR=${WORKDIR}/openssl/          make release-static-android' returned a non-zero code: 2

  

# Discussion History
## moneromooo-monero | 2017-10-24T17:47:42+00:00
Install it, then build again. The README.md has a link to it. And make clean at each attempt, since cmake tends to cache even when it should not.


## Senecarus | 2017-10-24T18:27:39+00:00
Sorry, but what i must install and build? 

## moneromooo-monero | 2017-10-24T18:41:44+00:00
zmq.hpp, from the error you mentioned.

## Senecarus | 2017-10-25T07:05:58+00:00
I added installation libzmq3-dev to docker script android32.Dockerfile and CMake Error is gone.
But later i have a clang compilation error that zmq.hpp can't be found.

## danrmiller | 2017-10-25T13:31:02+00:00
That libzmq3-dev package you installed is for the x86 host in the container that will build monero for the android target.
You need to build zmq for the arm target:
git clone https://github.com/zeromq/zeromq4-1.git
cd zeromq4-1 && ./autogen.sh && ./configure --host=arm-none-linux-gnueabi && make

Then you can get zmq.hpp from here: https://github.com/zeromq/cppzmq/

## Senecarus | 2017-10-25T14:13:16+00:00
So i need to change docker script and add two more steps?
1. pull zeromq4-1.git and build it
2. pull https://github.com/zeromq/cppzmq/ and add folder with zmq.hpp to include dirs? 

## danrmiller | 2017-10-25T14:18:09+00:00
Yes that's right. And when it builds monero it will need to know where the zeromq4-1/.libs/libzmq.a you built is, or else link it somewhere that it already looks like android/tool32/lib


## Senecarus | 2017-10-25T15:46:24+00:00
Trying to follow you recomendation and get error when make zeromq4-1

configure: error: in `/opt/android/zeromq4-1':
configure: error: C compiler cannot create executables
See `config.log' for more details
The command '/bin/sh -c cd zeromq4-1 && ./autogen.sh && ./configure --host=arm-none-linux-gnueabi && make' returned a non-zero code: 77

## danrmiller | 2017-10-25T16:12:26+00:00
Probably you need to make sure you are using the clang/clang++ CC/CXX compilers targeting ARM from android/tool32/bin.

You can also check config.log.

## Senecarus | 2017-10-25T16:38:54+00:00
I'm right that a can instead using a docker for android build, build Portable Statically Linked Binaries for arm and use it my android app (for arm)?

## danrmiller | 2017-10-25T16:46:16+00:00
Yes. But make sure you use the compilers and build tools from the android NDK.

## moneromooo-monero | 2017-12-13T21:16:58+00:00
+resolved

# Action History
- Created by: Senecarus | 2017-10-24T17:35:08+00:00
- Closed at: 2017-12-13T21:40:32+00:00
