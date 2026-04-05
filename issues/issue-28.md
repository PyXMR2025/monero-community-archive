---
title: Unable to compile on Alpine linux
source_url: https://github.com/xmrig/xmrig/issues/28
author: b-i-t-n
assignees: []
labels: []
created_at: '2017-07-05T00:18:18+00:00'
updated_at: '2017-07-09T12:16:21+00:00'
type: issue
status: closed
closed_at: '2017-07-09T12:16:21+00:00'
---

# Original Description
I am building XMRig in a Alpine Docker container.
I have had a quick look around on how to fix this but I am not a c++ dev.

It could be because Alpine linux does not use glibc so in most cases it is treated like linux but should be treated like osx or freebsd.
```
[ 77%] Building CXX object CMakeFiles/xmrig.dir/src/Cpu_unix.cpp.o
In file included from /usr/include/pthread.h:30:0,
                 from /xmrig/src/Cpu_unix.cpp:25:
/xmrig/src/Cpu_unix.cpp: In static member function 'static void Cpu::setAffinity(int, uint64_t)':
/xmrig/src/Cpu_unix.cpp:46:5: error: 'memset' was not declared in this scope
     CPU_ZERO(&set);
     ^
make[2]: *** [CMakeFiles/xmrig.dir/build.make:591: CMakeFiles/xmrig.dir/src/Cpu_unix.cpp.o] Error 1
make[1]: *** [CMakeFiles/Makefile2:69: CMakeFiles/xmrig.dir/all] Error 2
make: *** [Makefile:84: all] Error 2
```

# Discussion History
## xmrig | 2017-07-05T01:18:35+00:00
Can you provide some instructions how setup developer environment, install compiler, cmake, libuv on Alpine Linux. It can speed up process because I was never work with that Linux.
Thank you.

## b-i-t-n | 2017-07-05T07:09:25+00:00
What I have done to install xmrig on Alpine linux manually
```bash
# apk add openssl-dev curl-dev git cmake libuv-dev build-base
# git clone https://github.com/xmrig/xmrig
# cd xmrig
# mkdir build
# cmake -DCMAKE_BUILD_TYPE=Release .
# make
```
To use the Dockerfile copy or download the following and run `docker build --rm .` in the same folder.
https://raw.githubusercontent.com/b-i-t-n/alpine-xmrig/master/Dockerfile
```Dockerfile
FROM  alpine:latest
RUN   adduser -S -D -H -h /xmrig miner
RUN   apk --no-cache upgrade && \
      apk --no-cache add \
        openssl-dev \
        curl-dev \
        git \
        cmake \
        libuv-dev \
        build-base && \
      git clone https://github.com/xmrig/xmrig && \
      cd xmrig && \
      mkdir build && \
      cmake -DCMAKE_BUILD_TYPE=Release . && \
      make && \
      apk del \
        build-base \
        cmake \
        git
USER miner
WORKDIR    /xmrig
ENTRYPOINT ["./xmrig"]
```

## b-i-t-n | 2017-07-05T07:14:49+00:00
I probably do not need some of the packages as you do not support TLS or HTTP.

## xmrig | 2017-07-05T07:50:44+00:00
Yes openssl-dev and curl-dev not required. Okay I will check it later.
Thank you.

## xmrig | 2017-07-07T04:18:02+00:00
I fixed it, just one include was missing.

# Action History
- Created by: b-i-t-n | 2017-07-05T00:18:18+00:00
- Closed at: 2017-07-09T12:16:21+00:00
