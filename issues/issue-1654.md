---
title: make error while trying to compile xmrig in alpine
source_url: https://github.com/xmrig/xmrig/issues/1654
author: divramod
assignees: []
labels:
- bug
created_at: '2020-04-22T05:56:09+00:00'
updated_at: '2020-08-28T16:23:29+00:00'
type: issue
status: closed
closed_at: '2020-08-28T16:23:29+00:00'
---

# Original Description
**Describe the bug**
I am getting a ssl error when building xmrig in a docker alpine image.
I used libressl-dev as ssl lib and think this is the problem.
I already tried to build with openssl installed, but now i am out of options.
It would be really nice to have the latest xmrig running in docker.

**To Reproduce**
Use this dockerfile and try to build it:

```
FROM  alpine:latest
RUN   adduser -S -D -H -h /xmrig miner
RUN   apk add --no-cache --repository http://dl-cdn.alpinelinux.org/alpine/edge/testing hwloc-dev
RUN   apk --no-cache upgrade && \
      apk --no-cache add \
        git \
        cmake \
        libuv-dev \
        build-base \
        libressl-dev
RUN   git clone https://github.com/xmrig/xmrig
WORKDIR    /xmrig
RUN   mkdir build
RUN   ls -lisa
# RUN cmake -DCMAKE_BUILD_TYPE=Release -DWITH_HWLOC=OFF -DWITH_TLS=OFF . && \
# RUN   cmake -DWITH_TLS=OFF -DCMAKE_BUILD_TYPE=Release .
RUN   cmake -DCMAKE_BUILD_TYPE=Release .
RUN   make
RUN   cp build/xmrig /usr/local/bin
RUN   ls -lisa build
RUN   apk del \
        build-base \
        cmake \
        git
USER miner
ENTRYPOINT  ["./xmrig"]
```

**Expected behavior**
A successful docker build.

**Required data**
```
[ 95%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/log/backends/SysLog.cpp.o
[ 96%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Tls.cpp.o
[ 96%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/tls/ServerTls.cpp.o
[ 97%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/tls/TlsConfig.cpp.o
[ 97%] Building CXX object CMakeFiles/xmrig.dir/src/`
/xmrig/src/base/net/tls/TlsContext.cpp: In member function 'bool xmrig::TlsContext::load(const xmrig::TlsConfig&)':
/xmrig/src/base/net/tls/TlsContext.cpp:160:33: error: too few arguments to function 'int SSL_CTX_set_ex_data(SSL_CTX*, int, void*)'
  160 |     SSL_CTX_set_ex_data(m_ctx, 0);
      |                                 ^
In file included from /xmrig/src/base/net/tls/TlsContext.cpp:33:
/usr/include/openssl/ssl.h:1553:5: note: declared here
 1553 | int SSL_CTX_set_ex_data(SSL_CTX *ssl, int idx, void *data);
      |     ^~~~~~~~~~~~~~~~~~~
/xmrig/src/base/net/tls/TlsContext.cpp: In member function 'bool xmrig::TlsContext::setCipherSuites(const char*)':
/xmrig/src/base/net/tls/TlsContext.cpp:188:9: error: 'SSL_CTX_set_ciphersuites' was not declared in this scope; did you mean 'SSL_CTX_set_cipher_list'?
  188 |     if (SSL_CTX_set_ciphersuites(m_ctx, ciphersuites) == 1) {
      |         ^~~~~~~~~~~~~~~~~~~~~~~~
      |         SSL_CTX_set_cipher_list
make[2]: *** [CMakeFiles/xmrig.dir/build.make:2642: CMakeFiles/xmrig.dir/src/base/net/tls/TlsContext.cpp.o] Error 1
make[1]: *** [CMakeFiles/Makefile2:116: CMakeFiles/xmrig.dir/all] Error 2
make: *** [Makefile:84: all] Error 2
The command '/bin/sh -c make' returned a non-zero code: 2
```

**Additional context**
I added ```libressl-dev``` as openssl lib and i think this is the problem.
Could this be solved in https://github.com/xmrig/xmrig/blob/master/src/base/net/tls/TlsContext.cpp#L160 and https://github.com/xmrig/xmrig/blob/master/src/base/net/tls/TlsContext.cpp#L188

thx for building this tool!

# Discussion History
## xmrig | 2020-04-22T07:50:12+00:00
Fixed in dev branch.
Thank you.

# Action History
- Created by: divramod | 2020-04-22T05:56:09+00:00
- Closed at: 2020-08-28T16:23:29+00:00
