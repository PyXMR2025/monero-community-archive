---
title: Static Build fails on 12.2 on Docker
source_url: https://github.com/monero-project/monero/issues/3989
author: protradingclub
assignees: []
labels: []
created_at: '2018-06-11T21:35:09+00:00'
updated_at: '2018-09-09T12:48:52+00:00'
type: issue
status: closed
closed_at: '2018-09-09T12:48:52+00:00'
---

# Original Description
Im sure some of you already know this but here is the issue  
```

/usr/bin/ld: /usr/lib/gcc/x86_64-linux-gnu/5/../../../x86_64-linux-gnu/libboost_chrono.a(chrono.o): relocation R_X86_64_32 against `.rodata.str1.1' can not be used when making a shared object; recompile with -fPIC
/usr/lib/gcc/x86_64-linux-gnu/5/../../../x86_64-linux-gnu/libboost_chrono.a: error adding symbols: Bad value
collect2: error: ld returned 1 exit status
src/wallet/CMakeFiles/wallet_rpc_server.dir/build.make:133: recipe for target 'bin/monero-wallet-rpc' failed
make[3]: *** [bin/monero-wallet-rpc] Error 1
make[3]: Leaving directory '/root/monero/build/release'
CMakeFiles/Makefile2:2367: recipe for target 'src/wallet/CMakeFiles/wallet_rpc_server.dir/all' failed
make[2]: *** [src/wallet/CMakeFiles/wallet_rpc_server.dir/all] Error 2
make[2]: Leaving directory '/root/monero/build/release'
Makefile:138: recipe for target 'all' failed
make[1]: *** [all] Error 2
make[1]: Leaving directory '/root/monero/build/release'
Makefile:68: recipe for target 'release-static' failed
make: *** [release-static] Error 2
```

# Discussion History
## homdx | 2018-06-11T21:42:43+00:00
With my commit fix?
https://github.com/monero-project/monero/pull/3879

## protradingclub | 2018-06-11T22:14:59+00:00
I am using Ubuntu 

My steps are

```
git clone 
git submodule init && git submodule update
make release-static

```
Am I missing something? 


## arnuschky | 2018-06-12T09:03:29+00:00
Fails for me too on Ubuntu 16.04. Built with `make release-static-linux-x86_64`.

So I suspect that this error is unrelated to Docker, and thus your commit won't fix it @homdx 

## homdx | 2018-06-12T10:44:12+00:00
I use my Docker file (from my pull request) and latest git version from monero (master) and:
``
 ---> Running in b56c8db6fbbb
Removing intermediate container b56c8db6fbbb
 ---> 220d15a28cdb
Step 38/40 : EXPOSE 18080
 ---> Running in d30574635cb6
Removing intermediate container d30574635cb6
 ---> 746333544875
Step 39/40 : EXPOSE 18081
 ---> Running in 95d2ed793435
Removing intermediate container 95d2ed793435
 ---> 975a2d136e18
Step 40/40 : ENTRYPOINT ["monerod", "--p2p-bind-ip=0.0.0.0", "--p2p-bind-port=18080", "--rpc-bind-ip=0.0.0.0", "--rpc-bind-port=18081", "--non-interactive", "--confirm-external-bind"]
 ---> Running in 55a571b03593
Removing intermediate container 55a571b03593
 ---> 35d72891a326
Successfully built 35d72891a326
Successfully tagged monero:latest
``
$ docker --version
Docker version 18.03.0-ce, build 0520e24

## dEBRUYNE-1 | 2018-06-12T10:57:11+00:00
@protradingclub - The error is fairly explanatory:

>/usr/bin/ld: /usr/lib/gcc/x86_64-linux-gnu/5/../../../x86_64-linux-gnu/libboost_chrono.a(chrono.o): relocation R_X86_64_32 against `.rodata.str1.1' can not be used when making a shared object; **recompile with -fPIC**

Emphasis mine. 

## arnuschky | 2018-06-12T16:31:26+00:00
`CXXFLAGS="$CXXFLAGS -fPIC" make release-static` results in the same.

Also, I am not sure if the -fPIC argument wouldn't result in broken static builds.

## stoffu | 2018-06-13T04:00:33+00:00
@arnuschky The flag must be given to the build of Boost, which is outside Monero's build. Some platforms (e.g. Ubuntu 17 or later? Not 100% sure) offer packaged Boost libraries built with -fPIC, but other platforms don't, in which case you need to build it yourself.

## arnuschky | 2018-06-13T06:42:47+00:00
Ah ok, thanks, I misunderstood the warning. Urgh, it's always boost, isn't it? ;)

I am on Ubuntu 16.04 using the default boost 1.58, so that's definitely not an fPIC build.

## shopglobal | 2018-06-13T06:44:17+00:00
If it's not boost it's going to be readline, if it's not readline it will
be openssl, if not openssl then libzmq, then if you haven't jumped off a
bridge yet you have built monero

On Wed, Jun 13, 2018, 2:42 AM arnuschky <notifications@github.com> wrote:

> Ah ok, thanks, I misunderstood the warning. Urgh, it's always boost, isn't
> it? ;)
>
> I am on Ubuntu 16.04 using the default boost 1.58, so that's definitely
> not an fPIC build.
>
> —
> You are receiving this because you are subscribed to this thread.
> Reply to this email directly, view it on GitHub
> <https://github.com/monero-project/monero/issues/3989#issuecomment-396831074>,
> or mute the thread
> <https://github.com/notifications/unsubscribe-auth/AMMA5yGh_Bqp_-CQ3_UMk-ZGPK2ixaCYks5t8LRwgaJpZM4Ujb0y>
> .
>


## arnuschky | 2018-06-13T06:48:19+00:00
I realized now that this is already documented in the readme:

> Dependencies need to be built with -fPIC. Static libraries usually aren't, so you may have to build them yourself with -fPIC. Refer to their documentation for how to build them.

Sorry for the noise people.

## shopglobal | 2018-06-19T04:46:57+00:00
This worked for me 

```# Multistage docker build, requires docker 17.05

# builder stage
FROM ubuntu:16.04 as builder

RUN apt-get update && \
    apt-get --no-install-recommends --yes install \
        ca-certificates \
        cmake \
        g++ \
        make \
        pkg-config \
        graphviz \
        doxygen \
        git \
        curl \
        libtool-bin \
        autoconf \
        automake \
        bzip2

WORKDIR /usr/local

#Cmake
ARG CMAKE_VERSION=3.11.2
ARG CMAKE_VERSION_DOT=v3.11
ARG CMAKE_HASH=5ebc22bbcf2b4c7a20c4190d42c084cf38680a85b1a7980a2f1d5b4a52bf5248
RUN curl -s -O https://cmake.org/files/${CMAKE_VERSION_DOT}/cmake-${CMAKE_VERSION}.tar.gz \
    && echo "${CMAKE_HASH} cmake-${CMAKE_VERSION}.tar.gz" | sha256sum -c \
    && tar -xzf cmake-${CMAKE_VERSION}.tar.gz \
    && cd cmake-${CMAKE_VERSION} \
    && ./configure \
    && make \
    && make install

## Boost
ARG BOOST_VERSION=1_67_0
ARG BOOST_VERSION_DOT=1.67.0
ARG BOOST_HASH=2684c972994ee57fc5632e03bf044746f6eb45d4920c343937a465fd67a5adba
RUN curl -s -L -o  boost_${BOOST_VERSION}.tar.bz2 https://dl.bintray.com/boostorg/release/${BOOST_VERSION_DOT}/source/boost_${BOOST_VERSION}.tar.bz2 \
    && echo "${BOOST_HASH} boost_${BOOST_VERSION}.tar.bz2" | sha256sum -c \
    && tar -xvf boost_${BOOST_VERSION}.tar.bz2 \
    && cd boost_${BOOST_VERSION} \
    && ./bootstrap.sh \
    && ./b2 --build-type=minimal link=static runtime-link=static --with-chrono --with-date_time --with-filesystem --with-program_options --with-regex --with-serialization --with-system --with-thread --with-locale threading=multi threadapi=pthread cflags="-fPIC" cxxflags="-fPIC" stage
ENV BOOST_ROOT /usr/local/boost_${BOOST_VERSION}

# OpenSSL
ARG OPENSSL_VERSION=1.1.0h
ARG OPENSSL_HASH=5835626cde9e99656585fc7aaa2302a73a7e1340bf8c14fd635a62c66802a517
RUN curl -s -O https://www.openssl.org/source/openssl-${OPENSSL_VERSION}.tar.gz \
    && echo "${OPENSSL_HASH} openssl-${OPENSSL_VERSION}.tar.gz" | sha256sum -c \
    && tar -xzf openssl-${OPENSSL_VERSION}.tar.gz \
    && cd openssl-${OPENSSL_VERSION} \
    && ./Configure linux-x86_64 no-shared --static -fPIC \
    && make build_generated \
    && make libcrypto.a \
    && make install
ENV OPENSSL_ROOT_DIR=/usr/local/openssl-${OPENSSL_VERSION}

# ZMQ
ARG ZMQ_VERSION=v4.2.5
ARG ZMQ_HASH=d062edd8c142384792955796329baf1e5a3377cd
RUN git clone https://github.com/zeromq/libzmq.git -b ${ZMQ_VERSION} \
    && cd libzmq \
    && test `git rev-parse HEAD` = ${ZMQ_HASH} || exit 1 \
    && ./autogen.sh \
    && CFLAGS="-fPIC" CXXFLAGS="-fPIC" ./configure --enable-static --disable-shared \
    && make \
    && make install \
    && ldconfig

# zmq.hpp
ARG CPPZMQ_VERSION=v4.2.3
ARG CPPZMQ_HASH=6aa3ab686e916cb0e62df7fa7d12e0b13ae9fae6
RUN git clone https://github.com/zeromq/cppzmq.git -b ${CPPZMQ_VERSION} \
    && cd cppzmq \
    && test `git rev-parse HEAD` = ${CPPZMQ_HASH} || exit 1 \
    && mv *.hpp /usr/local/include

# Readline
ARG READLINE_VERSION=7.0
ARG READLINE_HASH=750d437185286f40a369e1e4f4764eda932b9459b5ec9a731628393dd3d32334
RUN curl -s -O https://ftp.gnu.org/gnu/readline/readline-${READLINE_VERSION}.tar.gz \
    && echo "${READLINE_HASH} readline-${READLINE_VERSION}.tar.gz" | sha256sum -c \
    && tar -xzf readline-${READLINE_VERSION}.tar.gz \
    && cd readline-${READLINE_VERSION} \
    && CFLAGS="-fPIC" CXXFLAGS="-fPIC" ./configure \
    && make \
    && make install

# Sodium
ARG SODIUM_VERSION=1.0.16
ARG SODIUM_HASH=675149b9b8b66ff44152553fb3ebf9858128363d
RUN git clone https://github.com/jedisct1/libsodium.git -b ${SODIUM_VERSION} \
    && cd libsodium \
    && test `git rev-parse HEAD` = ${SODIUM_HASH} || exit 1 \
    && ./autogen.sh \
    && CFLAGS="-fPIC" CXXFLAGS="-fPIC" ./configure \
    && make \
    && make check \
    && make install



WORKDIR /src
COPY . .

ARG NPROC
RUN rm -rf build && \
    if [ -z "$NPROC" ];then make -j$(nproc) release-static;else make -j$NPROC release-static;fi

# runtime stage
FROM ubuntu:16.04

RUN apt-get update && \
    apt-get --no-install-recommends --yes install ca-certificates && \
    apt-get clean && \
    rm -rf /var/lib/apt

COPY --from=builder /src/build/release/bin/* /usr/local/bin/

# Contains the blockchain
VOLUME /root/.bitmonero

# Generate your wallet via accessing the container and run:
# cd /wallet
# monero-wallet-cli
VOLUME /wallet

EXPOSE 18080
EXPOSE 18081

ENTRYPOINT ["monerod", "--p2p-bind-ip=0.0.0.0", "--p2p-bind-port=18080", "--rpc-bind-ip=0.0.0.0", "--rpc-bind-port=18081", "--non-interactive", "--confirm-external-bind"]```

## moneromooo-monero | 2018-07-19T21:40:35+00:00
The docker build is now thought to be fixed in 9c211b50

## moneromooo-monero | 2018-09-04T23:48:54+00:00
Can you report whether this is now fixed for you on latest master ? If no reply for a few days, I'll close as fixed.

## moneromooo-monero | 2018-09-09T12:47:56+00:00
+resolved


# Action History
- Created by: protradingclub | 2018-06-11T21:35:09+00:00
- Closed at: 2018-09-09T12:48:52+00:00
