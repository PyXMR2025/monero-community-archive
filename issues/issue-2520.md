---
title: Can't build the Dockerfile
source_url: https://github.com/monero-project/monero/issues/2520
author: unixfox
assignees: []
labels: []
created_at: '2017-09-24T10:20:19+00:00'
updated_at: '2017-10-15T18:00:21+00:00'
type: issue
status: closed
closed_at: '2017-10-15T18:00:21+00:00'
---

# Original Description
The Dockerfile can't be built due to a missing dependency:
```
-- Could not find GNU readline library so building without readline support
-- Found Git: /usr/bin/git
CMake Error at CMakeLists.txt:696 (message):
  Could not find required header zmq.hpp


-- Configuring incomplete, errors occurred!
See also "/usr/local/src/monero/build/release/CMakeFiles/CMakeOutput.log".
See also "/usr/local/src/monero/build/release/CMakeFiles/CMakeError.log".
Makefile:66: recipe for target 'release-static' failed
make: *** [release-static] Error 1
The command '/bin/sh -c make -j$(nproc) release-static' returned a non-zero code: 2
```

# Discussion History
## bitkevin | 2017-09-25T10:44:42+00:00
Add `libzmq3-dev` to solve the problem:

```
 RUN set -x \
   && buildDeps=' \
       ca-certificates \
       cmake \
       g++ \
       git \
       libboost1.58-all-dev \
       libssl-dev \
       libzmq3-dev \
       make \
       pkg-config \
   ' \
   && apt-get -qq update \
   && apt-get -qq --no-install-recommends install $buildDeps
```

## bitkevin | 2017-09-25T10:49:10+00:00
But I got another error, seems need `libsodium-dev`

```
[ 98%] Linking CXX executable ../../bin/monerod
/usr/lib/gcc/x86_64-linux-gnu/5/../../../x86_64-linux-gnu/libzmq.a(libzmq_la-ctx.o): In function `zmq::ctx_t::~ctx_t()':
(.text+0xfa6): undefined reference to `randombytes_close'
/usr/lib/gcc/x86_64-linux-gnu/5/../../../x86_64-linux-gnu/libzmq.a(libzmq_la-zmq_utils.o): In function `zmq_curve_keypair':
(.text+0x337): undefined reference to `crypto_box_keypair'
/usr/lib/gcc/x86_64-linux-gnu/5/../../../x86_64-linux-gnu/libzmq.a(libzmq_la-curve_client.o): In function `zmq::curve_client_t::encode(zmq::msg_t*)':
(.text+0x176): undefined reference to `crypto_box_afternm'
/usr/lib/gcc/x86_64-linux-gnu/5/../../../x86_64-linux-gnu/libzmq.a(libzmq_la-curve_client.o): In function `zmq::curve_client_t::decode(zmq::msg_t*)':
(.text+0x4ab): undefined reference to `crypto_box_open_afternm'
/usr/lib/gcc/x86_64-linux-gnu/5/../../../x86_64-linux-gnu/libzmq.a(libzmq_la-curve_client.o): In function `zmq::curve_client_t::curve_client_t(zmq::options_t const&)':
(.text+0x87e): undefined reference to `sodium_init'
/usr/lib/gcc/x86_64-linux-gnu/5/../../../x86_64-linux-gnu/libzmq.a(libzmq_la-curve_client.o): In function `zmq::curve_client_t::curve_client_t(zmq::options_t const&)':
(.text+0x89a): undefined reference to `crypto_box_keypair'
/usr/lib/gcc/x86_64-linux-gnu/5/../../../x86_64-linux-gnu/libzmq.a(libzmq_la-curve_client.o): In function `zmq::curve_client_t::produce_hello(zmq::msg_t*)':
(.text+0xb9a): undefined reference to `crypto_box'
/usr/lib/gcc/x86_64-linux-gnu/5/../../../x86_64-linux-gnu/libzmq.a(libzmq_la-curve_client.o): In function `zmq::curve_client_t::process_welcome(unsigned char const*, unsigne$ long)':
(.text+0xe25): undefined reference to `crypto_box_open'
...
```

## unixfox | 2017-09-25T16:13:06+00:00
Thank you for the help, do you want to push a pull request with these changes?

## moneromooo-monero | 2017-10-15T17:49:28+00:00
+resolved

# Action History
- Created by: unixfox | 2017-09-24T10:20:19+00:00
- Closed at: 2017-10-15T18:00:21+00:00
