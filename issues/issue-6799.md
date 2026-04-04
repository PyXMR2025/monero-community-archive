---
title: Conflicting libraries
source_url: https://github.com/monero-project/monero/issues/6799
author: leopoldoorsini
assignees: []
labels: []
created_at: '2020-09-04T15:34:19+00:00'
updated_at: '2020-10-15T22:36:59+00:00'
type: issue
status: closed
closed_at: '2020-10-15T22:36:59+00:00'
---

# Original Description
```
duplicate symbol '_randombytes' in:
    /usr/local/lib/libzmq.a(src_libzmq_la-tweetnacl.o)
    /usr/local/lib/libsodium.a(libsodium_la-randombytes.o)
duplicate symbol '_randombytes_close' in:
    /usr/local/lib/libzmq.a(src_libzmq_la-tweetnacl.o)
    /usr/local/lib/libsodium.a(libsodium_la-randombytes.o)
duplicate symbol '_sodium_init' in:
    /usr/local/lib/libzmq.a(src_libzmq_la-tweetnacl.o)
    /usr/local/lib/libsodium.a(libsodium_la-core.o)
duplicate symbol '_crypto_stream_salsa20_xor' in:
    /usr/local/lib/libzmq.a(src_libzmq_la-tweetnacl.o)
    /usr/local/lib/libsodium.a(libsodium_la-stream_salsa20.o)
duplicate symbol '_crypto_stream_salsa20' in:
    /usr/local/lib/libzmq.a(src_libzmq_la-tweetnacl.o)
    /usr/local/lib/libsodium.a(libsodium_la-stream_salsa20.o)
duplicate symbol '_randombytes' in:
    /usr/local/lib/libzmq.a(src_libzmq_la-tweetnacl.o)
    /usr/local/lib/libsodium.a(libsodium_la-randombytes.o)
duplicate symbol '_randombytes_close' in:
    /usr/local/lib/libzmq.a(src_libzmq_la-tweetnacl.o)
    /usr/local/lib/libsodium.a(libsodium_la-randombytes.o)
```

# Discussion History
## ndorf | 2020-09-04T16:13:19+00:00
Which platform are you using? Did you install the sodium and zmq libraries using your platform's package manager, build them yourself, or some other method?

## leopoldoorsini | 2020-09-04T16:48:32+00:00
Mac OS, previously installed with brew

## vtnerd | 2020-09-04T18:04:26+00:00
The ZeroMQ static build includes a good chunk of libsodium, causing the conflicts. You will need to either:
  * Rebuild ZeroMQ with the libsodium symbols marked as private (not exported)
  * Rebuild ZeroMQ without libsodium support. The daemon is not using CurveZMQ currently anyway
  * Use shared libraried for ZeroMQ and libsodium

## leopoldoorsini | 2020-09-06T10:58:33+00:00
It still gives me several errors like
```
(.text+0x21c): undefined reference to `gss_release_cred'
/usr/bin/ld: (.text+0x230): undefined reference to `gss_release_name'
/usr/bin/ld: /usr/lib/gcc/x86_64-linux-gnu/9/../../../x86_64-linux-gnu/libzmq.a(libzmq_la-gssapi_server.o): in function `zmq::gssapi_server_t::~gssapi_server_t()':
```

## moneromooo-monero | 2020-10-05T22:46:27+00:00
https://github.com/monero-project/monero/pull/6845 should fix this one (it's in 0.17.0.1).

## xmrdog | 2020-10-11T19:08:34+00:00
> #6845 should fix this one (it's in 0.17.0.1).

On my macOS Mojave today, I get exactly these same "duplicate symbol" issues between libzqm and libsodium. I was checked out on the 0.17.0.1 tag and did "make release-static" there. Can this be investigated further?

## xmrdog | 2020-10-11T19:35:27+00:00
(It's worth mentioning that only "make" works fine (on macOS Mojave, tag 0.17.0.1 as before). It would be cool if "make release-static" would also work.)

## moneromooo-monero | 2020-10-12T16:00:18+00:00
You need to build your libzmq with libsodium support. Ohterwise it uses a separate tweetnacl lib which uses the same routine names, so they conflict.

## selsta | 2020-10-12T16:04:10+00:00
I used this to build libzmq on Mac:

```
sodium_CFLAGS=-I/usr/local/opt/libsodium/include sodium_LIBS=-L/usr/local/opt/libsodium/lib ./configure --enable-static --disable-libunwind --disable-perf --with-pic --without-docs --with-libsodium --prefix=/path/to/prefix
```

## xmrdog | 2020-10-13T19:14:15+00:00
@moneromooo-monero Thanks - that is working. Using @selsta comment as base, I solved it with "brew edit zeromq", adding these at the obvious places in the file:

    ENV["sodium_CFLAGS"] = "-I/usr/local/opt/libsodium/include"
    ENV["sodium_LIBS"] = "-L/usr/local/opt/libsodium/lib"
    "--enable-static", "--with-libsodium"

Finally "brew reinstall --build-from-source zeromq".

After this "make release-static" works.

# Action History
- Created by: leopoldoorsini | 2020-09-04T15:34:19+00:00
- Closed at: 2020-10-15T22:36:59+00:00
