---
title: 'trezor/protocol.hpp:140:65: error: ‘MoneroLiveRefreshStepAck’ is not a member
  of ‘hw::trezor::messages::monero’'
source_url: https://github.com/monero-project/monero/issues/5661
author: jarole
assignees: []
labels: []
created_at: '2019-06-17T08:31:29+00:00'
updated_at: '2019-06-17T09:37:54+00:00'
type: issue
status: closed
closed_at: '2019-06-17T09:37:54+00:00'
---

# Original Description
Hi all! 
I can't compile monero 0.14.1.0 from source on Ubuntu 18.04
```
.........
Scanning dependencies of target obj_wallet
[ 76%] Building CXX object src/wallet/CMakeFiles/obj_wallet.dir/wallet2.cpp.o
In file included from /home/user123/monero/src/device_trezor/trezor.hpp:41:0,
                 from /home/user123/monero/src/device_trezor/device_trezor.hpp:33,
                 from /home/user123/monero/src/wallet/wallet2.cpp:78:
/home/user123/monero/src/device_trezor/trezor/protocol.hpp:140:65: error: ‘MoneroLiveRefreshStepAck’ is not a member of ‘hw::trezor::messages::monero’
                         const std::shared_ptr<messages::monero::MoneroLiveRefreshStepAck> & ack,
                                                                 ^~~~~~~~~~~~~~~~~~~~~~~~
/home/user123/monero/src/device_trezor/trezor/protocol.hpp:140:65: note: suggested alternative: ‘MoneroKeyImageSyncStepAck’
                         const std::shared_ptr<messages::monero::MoneroLiveRefreshStepAck> & ack,
                                                                 ^~~~~~~~~~~~~~~~~~~~~~~~
                                                                 MoneroKeyImageSyncStepAck
/home/user123/monero/src/device_trezor/trezor/protocol.hpp:140:65: error: ‘MoneroLiveRefreshStepAck’ is not a member of ‘hw::trezor::messages::monero’
/home/user123/monero/src/device_trezor/trezor/protocol.hpp:140:65: note: suggested alternative: ‘MoneroKeyImageSyncStepAck’
                         const std::shared_ptr<messages::monero::MoneroLiveRefreshStepAck> & ack,
                                                                 ^~~~~~~~~~~~~~~~~~~~~~~~
                                                                 MoneroKeyImageSyncStepAck
/home/user123/monero/src/device_trezor/trezor/protocol.hpp:140:89: error: template argument 1 is invalid
                         const std::shared_ptr<messages::monero::MoneroLiveRefreshStepAck> & ack,
                                                                                         ^
/home/user123/monero/src/device_trezor/trezor/protocol.hpp:315:37: error: ‘MoneroGetTxKeyRequest’ is not a member of ‘hw::trezor::messages::monero’
   std::shared_ptr<messages::monero::MoneroGetTxKeyRequest> get_tx_key(
                                     ^~~~~~~~~~~~~~~~~~~~~
/home/user123/monero/src/device_trezor/trezor/protocol.hpp:315:37: note: suggested alternative: ‘MoneroGetAddress’
   std::shared_ptr<messages::monero::MoneroGetTxKeyRequest> get_tx_key(
                                     ^~~~~~~~~~~~~~~~~~~~~
                                     MoneroGetAddress
/home/user123/monero/src/device_trezor/trezor/protocol.hpp:315:37: error: ‘MoneroGetTxKeyRequest’ is not a member of ‘hw::trezor::messages::monero’
/home/user123/monero/src/device_trezor/trezor/protocol.hpp:315:37: note: suggested alternative: ‘MoneroGetAddress’
   std::shared_ptr<messages::monero::MoneroGetTxKeyRequest> get_tx_key(
                                     ^~~~~~~~~~~~~~~~~~~~~
                                     MoneroGetAddress
/home/user123/monero/src/device_trezor/trezor/protocol.hpp:315:58: error: template argument 1 is invalid
   std::shared_ptr<messages::monero::MoneroGetTxKeyRequest> get_tx_key(
                                                          ^
/home/user123/monero/src/device_trezor/trezor/protocol.hpp:322:29: error: ISO C++ forbids declaration of ‘type name’ with no type [-fpermissive]
       std::shared_ptr<const messages::monero::MoneroGetTxKeyAck> ack
                             ^~~~~~~~
/home/user123/monero/src/device_trezor/trezor/protocol.hpp:322:64: error: template argument 1 is invalid
       std::shared_ptr<const messages::monero::MoneroGetTxKeyAck> ack
                                                                ^
/home/user123/monero/src/device_trezor/trezor/protocol.hpp:322:29: error: ISO C++ forbids declaration of ‘type name’ with no type [-fpermissive]
       std::shared_ptr<const messages::monero::MoneroGetTxKeyAck> ack
                             ^~~~~~~~
/home/user123/monero/src/device_trezor/trezor/protocol.hpp:322:64: error: template argument 1 is invalid
       std::shared_ptr<const messages::monero::MoneroGetTxKeyAck> ack
                                                                ^
/home/user123/monero/src/device_trezor/trezor/protocol.hpp:322:29: error: ISO C++ forbids declaration of ‘type name’ with no type [-fpermissive]
       std::shared_ptr<const messages::monero::MoneroGetTxKeyAck> ack
                             ^~~~~~~~
/home/user123/monero/src/device_trezor/trezor/protocol.hpp:322:64: error: template argument 1 is invalid
       std::shared_ptr<const messages::monero::MoneroGetTxKeyAck> ack
                                                                ^
/home/user123/monero/src/device_trezor/trezor/protocol.hpp:322:12: error: ‘std::shared_ptr’ is not a type
       std::shared_ptr<const messages::monero::MoneroGetTxKeyAck> ack
            ^~~~~~~~~~
/home/user123/monero/src/device_trezor/trezor/protocol.hpp:322:22: error: expected ‘,’ or ‘...’ before ‘<’ token
       std::shared_ptr<const messages::monero::MoneroGetTxKeyAck> ack
```
Used steps:

`$ cmake -DMANUAL_SUBMODULES=1`
`$ USE_SINGLE_BUILDDIR=1 make`


# Discussion History
## jarole | 2019-06-17T08:35:30+00:00
I used `-DMANUAL_SUBMODULES=1` because I got this error during my first compilation attempt:
```
USE_SINGLE_BUILDDIR=1 make                                                  
mkdir -p build/release
cd build/release && cmake -D BUILD_TESTS=ON -D CMAKE_BUILD_TYPE=release ../.. && make
-- CMake version 3.10.2
-- Building without build tag
-- Checking submodules
CMake Error at CMakeLists.txt:190 (message):
  Submodule 'external/miniupnp' is not up-to-date.  Please update with

  git submodule update --init --force external/miniupnp

  or run cmake with -DMANUAL_SUBMODULES=1
Call Stack (most recent call first):
  CMakeLists.txt:195 (check_submodule)


-- Configuring incomplete, errors occurred!
See also "/home/user123/monero/build/release/CMakeFiles/CMakeOutput.log".
See also "/home/user123/monero/build/release/CMakeFiles/CMakeError.log".
Makefile:98: recipe for target 'release-all' failed
make: *** [release-all] Error 1
```

## ph4r05 | 2019-06-17T08:58:01+00:00
Try running in the project root:

```
git submodule update --init --recursive
```

Your submodules are probably outdated.

## jarole | 2019-06-17T09:37:54+00:00
Many thanks !
that was the issue

# Action History
- Created by: jarole | 2019-06-17T08:31:29+00:00
- Closed at: 2019-06-17T09:37:54+00:00
