---
title: Docker fails to build from Dockerfile
source_url: https://github.com/monero-project/monero/issues/6483
author: CurtisLeeBolin
assignees: []
labels: []
created_at: '2020-04-27T15:28:42+00:00'
updated_at: '2022-02-19T04:32:35+00:00'
type: issue
status: closed
closed_at: '2022-02-19T04:32:35+00:00'
---

# Original Description
```
Step 47/57 : RUN set -ex &&     git submodule init && git submodule update &&     rm -rf build &&     if [ -z "$NPROC" ] ;     then make -j$(nproc) release-static ;     else make -j$NPROC release-static ;     fi
 ---> Running in bcc15082eef8
+ git submodule init
fatal: Not a git repository (or any of the parent directories): .git
The command '/bin/sh -c set -ex &&     git submodule init && git submodule update &&     rm -rf build &&     if [ -z "$NPROC" ] ;     then make -j$(nproc) release-static ;     else make -j$NPROC release-static ;     fi' returned a non-zero code: 128
```

# Discussion History
## moneromooo-monero | 2020-04-27T15:40:23+00:00
Did you get the tree without git ?

## CurtisLeeBolin | 2020-04-27T16:44:45+00:00
yes

## CurtisLeeBolin | 2020-04-27T17:15:16+00:00
I was expecting it to clone whatever repositories it needed in a build stage.

@moneromooo-monero, since you asked, I tried cloning the repository before building from the Dockerfile.  It still failed to build.

```
make[3]: Leaving directory '/src/build/release'
[ 63%] Built target obj_lmdb_lib
[ 63%] Building CXX object src/cryptonote_core/CMakeFiles/obj_cryptonote_core.dir/tx_pool.cpp.o
[ 63%] Building CXX object src/net/CMakeFiles/obj_net.dir/error.cpp.o
[ 64%] Building CXX object src/net/CMakeFiles/obj_net.dir/i2p_address.cpp.o
/src/src/cryptonote_core/tx_pool.cpp: In lambda function:
/src/src/cryptonote_core/tx_pool.cpp:619:27: error: 'relay_method' is not a class, namespace, or enumeration
       if (relay_method != relay_method::block && relay_method != relay_method::fluff)
                           ^
/src/src/cryptonote_core/tx_pool.cpp:619:66: error: 'relay_method' is not a class, namespace, or enumeration
       if (relay_method != relay_method::block && relay_method != relay_method::fluff)
                                                                  ^
make[3]: Entering directory '/src/build/release'
Scanning dependencies of target obj_mnemonics
make[3]: Leaving directory '/src/build/release'
make[3]: Entering directory '/src/build/release'
[ 64%] Building CXX object src/mnemonics/CMakeFiles/obj_mnemonics.dir/electrum-words.cpp.o
make[3]: *** [src/cryptonote_core/CMakeFiles/obj_cryptonote_core.dir/tx_pool.cpp.o] Error 1
src/cryptonote_core/CMakeFiles/obj_cryptonote_core.dir/build.make:88: recipe for target 'src/cryptonote_core/CMakeFiles/obj_cryptonote_core.dir/tx_pool.cpp.o' failed
make[3]: Leaving directory '/src/build/release'
make[2]: *** [src/cryptonote_core/CMakeFiles/obj_cryptonote_core.dir/all] Error 2
CMakeFiles/Makefile2:1524: recipe for target 'src/cryptonote_core/CMakeFiles/obj_cryptonote_core.dir/all' failed
make[2]: *** Waiting for unfinished jobs....
[ 64%] Building CXX object src/net/CMakeFiles/obj_net.dir/parse.cpp.o
[ 64%] Building CXX object src/net/CMakeFiles/obj_net.dir/socks.cpp.o
make[3]: Leaving directory '/src/build/release'
[ 64%] Built target obj_mnemonics
[ 64%] Building CXX object src/net/CMakeFiles/obj_net.dir/socks_connect.cpp.o
[ 65%] Building CXX object src/net/CMakeFiles/obj_net.dir/tor_address.cpp.o
[ 65%] Building CXX object src/net/CMakeFiles/obj_net.dir/zmq.cpp.o
make[3]: Leaving directory '/src/build/release'
[ 65%] Built target obj_cryptonote_basic
make[3]: Leaving directory '/src/build/release'
[ 65%] Built target obj_net
make[2]: Leaving directory '/src/build/release'
make[1]: *** [all] Error 2
Makefile:140: recipe for target 'all' failed
make[1]: Leaving directory '/src/build/release'
make: *** [release-static] Error 2
Makefile:106: recipe for target 'release-static' failed
ERROR: Service 'monero' failed to build: The command '/bin/sh -c set -ex &&     git submodule init && git submodule update &&     rm -rf build &&     if [ -z "$NPROC" ] ;     then make -j$(nproc) release-static ;     else make -j$NPROC release-static ;     fi' returned a non-zero code: 2
```

## selsta | 2020-04-27T17:19:36+00:00
I think the docker image uses an outdated GCC compiler version. Updating from 16.04 to 18.04 should solve the issue.

Does this one work? https://hub.docker.com/r/xmrto/monero/

## moneromooo-monero | 2020-04-28T00:00:27+00:00
Yes, looks like it's confusing two symbols in two different contexts. Admittedly something that's confusing. Thanks for the note.

## CurtisLeeBolin | 2020-04-28T13:11:23+00:00
> I think the docker image uses an outdated GCC compiler version. Updating from 16.04 to 18.04 should solve the issue.
> 
> Does this one work? https://hub.docker.com/r/xmrto/monero/

I am using my own Alpine Linux docker container until this is fixed. 

## ArqTras | 2020-05-02T14:14:47+00:00
Think that may help
#6434

## selsta | 2022-02-19T04:32:35+00:00
Dockerfile has been updated a while ago.

# Action History
- Created by: CurtisLeeBolin | 2020-04-27T15:28:42+00:00
- Closed at: 2022-02-19T04:32:35+00:00
