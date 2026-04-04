---
title: ubuntu static-release target fails with undefined symbols
source_url: https://github.com/monero-project/monero/issues/8439
author: bladedoyle
assignees: []
labels: []
created_at: '2022-07-16T19:11:06+00:00'
updated_at: '2022-07-21T14:34:23+00:00'
type: issue
status: closed
closed_at: '2022-07-17T15:54:34+00:00'
---

# Original Description
Trying to build v0.18.0.0

Getting undefined symbols linking on ubuntu 20.04 using "static-release" target.

Additional libraries are needed for static linking executables - required by libunbound

/usr/lib/x86_64-linux-gnu/libhogweed.a 
/usr/lib/x86_64-linux-gnu/libgmp.a 
/usr/lib/x86_64-linux-gnu/libnettle.a  
/usr/lib/x86_64-linux-gnu/libevent.a

Reference:
https://packages.debian.org/sid/libs/libunbound8

```
[ 96%] Linking CXX executable ../../bin/monero-gen-ssl-cert
/usr/bin/ld: /usr/lib/x86_64-linux-gnu/libunbound.a(ub_event_pluggable.o): in function `my_signal_new':
(.text+0xb9): undefined reference to `event_set'
...
/usr/bin/ld: /usr/lib/x86_64-linux-gnu/libunbound.a(val_secalgo.o): in function `_verify_nettle_rsa':
...
/usr/bin/ld: (.text+0x695): undefined reference to `__gmpz_clear'
...
(.text+0xb9): undefined reference to `event_set'
...
```

# Discussion History
## selsta | 2022-07-16T19:14:42+00:00
Why not use `make depends target=x86_64-linux-gnu` instead? It will compile all the dependencies for you.

If you don't want to use `make depends` then try compile static unbound yourself: https://github.com/monero-project/monero/blob/master/contrib/depends/packages/unbound.mk#L11

## bladedoyle | 2022-07-17T14:03:25+00:00
Yes, building the depends rather than installing packages does work.
Though, it doesnt guess at the target architecture, and it also doesnt build/link static binaries.
Im able to call the arch guessing script as part of the command:
`make -j$(nproc) depends target=$(contrib/depends/config.guess)`

Should I close this issue, or leave it open to track the issue with static build/linking?

## selsta | 2022-07-17T14:08:20+00:00
What do you mean it doesn't build / link static binaries? We use depends to create release binaries which are static linked.

> Should I close this issue, or leave it open to track the issue with static build/linking?

I'm not aware of any issues, if you want to compile static binaries without depends you have to correctly compile unbound library. I've linked in my previous comment how you have to compile it.

## bladedoyle | 2022-07-17T14:46:42+00:00
The issue would be:  Previous to this release it was possible to build and link using package manager installed dependency libraries using the "static-release" target, and now that fails due to missing libraries in the cmake generated link.txt file.

I agree that its possible to build the unbound library from source to work around this.

Its also possible to support the (untuntu 20.04) package manager installed unbound library by adding the 4 mentioned libraries to the cmake (link.txt) process.

So the question is if this issue should remain open to track that?

## hyc | 2022-07-17T15:35:38+00:00
IMO it's the distro packager's responsibility to ensure that static libraries reference their dependencies.
The ability to reference a static library's dependencies within the library itself has been added to GNU binutils 2.36, which has been out for quite a while.

## bladedoyle | 2022-07-17T15:54:34+00:00
Ok.  I had never heard of static libraries referencing dependencies.  

Closing.

## sethforprivacy | 2022-07-21T14:34:23+00:00
I'm working on a working static build here, feel free to follow along or jump into the PR with comments, hopefully will be helpful:

https://github.com/sethforprivacy/simple-monerod-docker/pull/61

# Action History
- Created by: bladedoyle | 2022-07-16T19:11:06+00:00
- Closed at: 2022-07-17T15:54:34+00:00
