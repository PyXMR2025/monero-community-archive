---
title: Docker build failed
source_url: https://github.com/monero-project/monero/issues/6697
author: PhilipChani
assignees: []
labels: []
created_at: '2020-06-29T05:41:11+00:00'
updated_at: '2020-08-13T14:01:46+00:00'
type: issue
status: closed
closed_at: '2020-08-13T14:01:45+00:00'
---

# Original Description
I try building an image but always meet a dead end here

[ 68%] Building CXX object src/p2p/CMakeFiles/obj_p2p.dir/net_node.cpp.o                                                            [ 69%] Building CXX object src/p2p/CMakeFiles/obj_p2p.dir/net_peerlist.cpp.o                                                        [ 70%] Building CXX object src/rpc/CMakeFiles/obj_rpc.dir/rpc_payment.cpp.o                                                         src/rpc/CMakeFiles/obj_rpc.dir/build.make:88: recipe for target 'src/rpc/CMakeFiles/obj_rpc.dir/core_rpc_server.cpp.o' failed       c++: internal compiler error: Killed (program cc1plus)            Please submit a full bug report,                                  with preprocessed source if appropriate.                          See <file:///usr/share/doc/gcc-5/README.Bugs> for instructions.   make[3]: *** [src/rpc/CMakeFiles/obj_rpc.dir/core_rpc_server.cpp.o] Error 4
make[3]: *** Waiting for unfinished jobs....                      make[3]: Entering directory '/src/build/release'                  Scanning dependencies of target obj_cryptonote_protocol           make[3]: Leaving directory '/src/build/release'                   make[3]: Entering directory '/src/build/release'                  [ 70%] Building CXX object src/cryptonote_protocol/CMakeFiles/obj_cryptonote_protocol.dir/block_queue.cpp.o                         make[3]: Leaving directory '/src/build/release'                   [ 70%] Built target obj_p2p                                       [ 71%] Building CXX object src/cryptonote_protocol/CMakeFiles/obj_cryptonote_protocol.dir/cryptonote_protocol_handler-base.cpp.o
make[3]: Leaving directory '/src/build/release'                   CMakeFiles/Makefile2:2260: recipe for target 'src/rpc/CMakeFiles/obj_rpc.dir/all' failed                                            make[2]: *** [src/rpc/CMakeFiles/obj_rpc.dir/all] Error 2         make[2]: *** Waiting for unfinished jobs....
[ 71%] Building CXX object src/cryptonote_protocol/CMakeFiles/obj_cryptonote_protocol.dir/levin_notify.cpp.o
^[[A^[[Amake[3]: Leaving directory '/src/build/release'
[ 71%] Built target obj_cryptonote_protocol
make[2]: Leaving directory '/src/build/release'
Makefile:140: recipe for target 'all' failed
make[1]: *** [all] Error 2
make[1]: Leaving directory '/src/build/release'
Makefile:106: recipe for target 'release-static' failed
make: *** [release-static] Error 2
The command '/bin/sh -c set -ex &&     git submodule init && git submodule update &&     rm -rf build &&     if [ -z "$NPROC" ] ;     then make -j$(nproc) release-static ;     else make -j$NPROC release-static ;     fi' returned a non-zero code: 2



# Discussion History
## sumogr | 2020-06-29T07:32:51+00:00
add a couple of GB of swap space

## PhilipChani | 2020-08-13T14:01:45+00:00
I was building from master which was failing, i checked out release 16 which built an image successfully

# Action History
- Created by: PhilipChani | 2020-06-29T05:41:11+00:00
- Closed at: 2020-08-13T14:01:45+00:00
