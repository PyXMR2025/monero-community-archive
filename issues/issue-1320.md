---
title: Static build with TLS support
source_url: https://github.com/xmrig/xmrig/issues/1320
author: miki-bgd-011
assignees: []
labels: []
created_at: '2019-11-27T12:50:19+00:00'
updated_at: '2020-08-28T16:24:13+00:00'
type: issue
status: closed
closed_at: '2020-08-28T16:24:13+00:00'
---

# Original Description
It's about time someone figures out how to compile a fully static build on Alpine linux with TLS support. I'm giving a 2 XMR bounty to whoever provides instructions here. 

Xmrig would you like to act as an escrow?

# Discussion History
## icodeface | 2020-02-01T11:29:03+00:00
add
```
# Compile and install the static OpenSSL library
ENV OPENSSL_VERSION=1.1.1
RUN wget -O /tmp/openssl-${OPENSSL_VERSION}.tar.gz https://www.openssl.org/source/openssl-${OPENSSL_VERSION}.tar.gz && \
    cd /tmp && \
    tar xzvf /tmp/openssl-${OPENSSL_VERSION}.tar.gz && \
    rm /tmp/openssl-${OPENSSL_VERSION}.tar.gz && \
    cd /tmp/openssl-${OPENSSL_VERSION} && \
    ./Configure -static --static no-shared no-async no-hw no-zlib no-pic no-dso \
                no-engine no-threads linux-x86_64 && \
    make ${MAKE_ARGS} && \
    make install && \
    cd /tmp && \
    rm -rf /tmp/openssl-${OPENSSL_VERSION}
```
to your dockerfile should works

## xmrig | 2020-08-28T16:24:13+00:00
https://xmrig.com/docs/miner/build/alpine

# Action History
- Created by: miki-bgd-011 | 2019-11-27T12:50:19+00:00
- Closed at: 2020-08-28T16:24:13+00:00
