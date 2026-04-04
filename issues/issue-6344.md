---
title: Docker Build failed
source_url: https://github.com/monero-project/monero/issues/6344
author: Bentivimon
assignees: []
labels: []
created_at: '2020-02-18T09:41:23+00:00'
updated_at: '2020-02-18T14:15:27+00:00'
type: issue
status: closed
closed_at: '2020-02-18T14:15:27+00:00'
---

# Original Description
Hi all.
I try to build a docker image from branch ` release-v0.15`
Flow: 

- `git submodule init`
- `git submodule update`
- `docker build .`

Part of stack trace:
> [ 68%] Building CXX object src/rpc/CMakeFiles/obj_rpc_base.dir/rpc_args.cpp.o
> [ 68%] Building CXX object src/rpc/CMakeFiles/obj_rpc_base.dir/rpc_payment_signature.cpp.o
> [ 68%] Building CXX object src/rpc/CMakeFiles/obj_rpc_base.dir/rpc_handler.cpp.o
> make[3]: Leaving directory '/src/build/release'
> [ 68%] Built target obj_rpc_base
> [ 68%] Building CXX object src/rpc/CMakeFiles/obj_rpc.dir/rpc_payment.cpp.o
> [ 69%] Building CXX object src/rpc/CMakeFiles/obj_rpc.dir/instanciations.cpp.o
> src/rpc/CMakeFiles/obj_rpc.dir/build.make:75: recipe for target 'src/rpc/CMakeFiles/obj_rpc.dir/core_rpc_server.cpp.o' failed
> c++: internal compiler error: Killed (program cc1plus)
> Please submit a full bug report,
> with preprocessed source if appropriate.
> See <file:///usr/share/doc/gcc-5/README.Bugs> for instructions.
> make[3]: *** [src/rpc/CMakeFiles/obj_rpc.dir/core_rpc_server.cpp.o] Error 4
> make[3]: *** Waiting for unfinished jobs....
> make[3]: Entering directory '/src/build/release'
> Scanning dependencies of target obj_p2p
> make[3]: Leaving directory '/src/build/release'
> make[3]: Entering directory '/src/build/release'
> [ 69%] Building CXX object src/p2p/CMakeFiles/obj_p2p.dir/net_node.cpp.o
> [ 70%] Building CXX object src/p2p/CMakeFiles/obj_p2p.dir/net_peerlist.cpp.o
> make[3]: Leaving directory '/src/build/release'
> [ 70%] Built target obj_p2p
> make[3]: Entering directory '/src/build/release'
> Scanning dependencies of target obj_cryptonote_protocol
> make[3]: Leaving directory '/src/build/release'
> make[3]: Entering directory '/src/build/release'
> [ 70%] Building CXX object src/cryptonote_protocol/CMakeFiles/obj_cryptonote_protocol.dir/block_queue.cpp.o
> [ 71%] Building CXX object src/cryptonote_protocol/CMakeFiles/obj_cryptonote_protocol.dir/cryptonote_protocol_handler-base.cpp.o
> [ 71%] Building CXX object src/cryptonote_protocol/CMakeFiles/obj_cryptonote_protocol.dir/levin_notify.cpp.o
> make[2]: *** [src/rpc/CMakeFiles/obj_rpc.dir/all] Error 2
> make[2]: *** Waiting for unfinished jobs....
> make[3]: Leaving directory '/src/build/release'
> CMakeFiles/Makefile2:2260: recipe for target 'src/rpc/CMakeFiles/obj_rpc.dir/all' failed
> make[3]: Leaving directory '/src/build/release'
> [ 71%] Built target obj_cryptonote_protocol
> make[2]: Leaving directory '/src/build/release'
> make[1]: *** [all] Error 2
> Makefile:140: recipe for target 'all' failed
> make[1]: Leaving directory '/src/build/release'
> Makefile:106: recipe for target 'release-static' failed
> make: *** [release-static] Error 2
> The command '/bin/sh -c set -ex &&     git submodule init && git submodule update &&     rm -rf build &&     if [ -z "$NPROC" ] ;     then make -j$(nproc) release-static ;     else make -j$NPROC release-static ;     fi' returned a non-zero code: 2

This error throw in step: 

> RUN set -ex && \
>     git submodule init && git submodule update && \
>     rm -rf build && \
>     if [ -z "$NPROC" ] ; \
>     then make -j$(nproc) release-static ; \
>     else make -j$NPROC release-static ; \
>     fi

Running on Docker Desktop Community:
![image](https://user-images.githubusercontent.com/31740384/74723533-6c363600-5243-11ea-9a95-4678228053f6.png)


Can someone help me with it?

# Discussion History
## selsta | 2020-02-18T12:56:36+00:00
Can you try https://hub.docker.com/r/xmrto/monero ?

I don’t know if the dockerfile inside this repo is maintained. From the logs it looks like the compiler gets killed due to lack of RAM / resources.

## Bentivimon | 2020-02-18T14:13:52+00:00
> Can you try https://hub.docker.com/r/xmrto/monero ?
> 
> I don’t know if the dockerfile inside this repo is maintained. From the logs it looks like the compiler gets killed due to lack of RAM / resources.

You were right. Thank you very much. I extend docker resources to 6GB of RAM it helped me.
Can you please describe how you understand that problem in docker resources?

## selsta | 2020-02-18T14:14:51+00:00
> c++: internal compiler error: Killed (program cc1plus)

is a hint at lack of RAM.

## Bentivimon | 2020-02-18T14:15:15+00:00
Thank you)

# Action History
- Created by: Bentivimon | 2020-02-18T09:41:23+00:00
- Closed at: 2020-02-18T14:15:27+00:00
