---
title: Current master fails to compile on Ubuntu 16.04
source_url: https://github.com/monero-project/monero/issues/4727
author: ndorf
assignees: []
labels: []
created_at: '2018-10-25T22:50:18+00:00'
updated_at: '2018-10-26T20:48:59+00:00'
type: issue
status: closed
closed_at: '2018-10-26T20:48:59+00:00'
---

# Original Description
The trouble seems to stem from commit f5f7c2ac245523b5a78a9aff57f05077ff352c1f -- reverting that resolves the failure.

This doesn't affect release-v0.13.

```
% git status && git rev-parse HEAD
HEAD detached at origin/master
nothing to commit, working directory clean
1e74586ee99e4bd89626d2eb4d23883cd91f0f81

% rm -r build && make
[...]
[ 30%] Building CXX object src/rpc/CMakeFiles/obj_daemon_rpc_server.dir/daemon_handler.cpp.o
In file included from /mnt/src/src/rpc/daemon_messages.cpp:29:0:
/mnt/src/src/rpc/daemon_messages.h:121:81: error: invalid use of ‘::’
     RPC_MESSAGE_MEMBER(std::unordered_map<crypto::hash COMMA() cryptonote::rpc::transaction_info>, txs);
                                                                                 ^
/mnt/src/src/rpc/daemon_messages.h:70:52: note: in definition of macro ‘RPC_MESSAGE_MEMBER’
 #define RPC_MESSAGE_MEMBER(type, name) type name = type{}
                                                    ^
/mnt/src/src/rpc/daemon_messages.h:121:81: error: expected ‘;’ at end of member declaration
     RPC_MESSAGE_MEMBER(std::unordered_map<crypto::hash COMMA() cryptonote::rpc::transaction_info>, txs);
                                                                                 ^
/mnt/src/src/rpc/daemon_messages.h:70:52: note: in definition of macro ‘RPC_MESSAGE_MEMBER’
 #define RPC_MESSAGE_MEMBER(type, name) type name = type{}
                                                    ^
/mnt/src/src/rpc/daemon_messages.h:121:97: error: expected unqualified-id before ‘>’ token
     RPC_MESSAGE_MEMBER(std::unordered_map<crypto::hash COMMA() cryptonote::rpc::transaction_info>, txs);
                                                                                                 ^
/mnt/src/src/rpc/daemon_messages.h:70:52: note: in definition of macro ‘RPC_MESSAGE_MEMBER’
 #define RPC_MESSAGE_MEMBER(type, name) type name = type{}
                                                    ^
/mnt/src/src/rpc/daemon_messages.h:121:51: error: wrong number of template arguments (1, should be at least 2)
     RPC_MESSAGE_MEMBER(std::unordered_map<crypto::hash COMMA() cryptonote::rpc::transaction_info>, txs);
                                                   ^
/mnt/src/src/rpc/daemon_messages.h:70:52: note: in definition of macro ‘RPC_MESSAGE_MEMBER’
 #define RPC_MESSAGE_MEMBER(type, name) type name = type{}
                                                    ^
In file included from /usr/include/c++/5/unordered_map:48:0,
                 from /mnt/src/src/rpc/message_data_structs.h:35,
                 from /mnt/src/src/rpc/message.h:32,
                 from /mnt/src/src/rpc/daemon_messages.h:31,
                 from /mnt/src/src/rpc/daemon_messages.cpp:29:
/usr/include/c++/5/bits/unordered_map.h:98:11: note: provided for ‘template<class _Key, class _Tp, class _Hash, class _Pred, class _Alloc> class std::unordered_map’
     class unordered_map
           ^
In file included from /mnt/src/src/rpc/daemon_handler.h:31:0,
                 from /mnt/src/src/rpc/daemon_handler.cpp:29:
/mnt/src/src/rpc/daemon_messages.h:121:81: error: invalid use of ‘::’
     RPC_MESSAGE_MEMBER(std::unordered_map<crypto::hash COMMA() cryptonote::rpc::transaction_info>, txs);
                                                                                 ^
/mnt/src/src/rpc/daemon_messages.h:70:52: note: in definition of macro ‘RPC_MESSAGE_MEMBER’
 #define RPC_MESSAGE_MEMBER(type, name) type name = type{}
                                                    ^
/mnt/src/src/rpc/daemon_messages.h:121:81: error: expected ‘;’ at end of member declaration
     RPC_MESSAGE_MEMBER(std::unordered_map<crypto::hash COMMA() cryptonote::rpc::transaction_info>, txs);
                                                                                 ^
/mnt/src/src/rpc/daemon_messages.h:70:52: note: in definition of macro ‘RPC_MESSAGE_MEMBER’
 #define RPC_MESSAGE_MEMBER(type, name) type name = type{}
                                                    ^
/mnt/src/src/rpc/daemon_messages.h:121:97: error: expected unqualified-id before ‘>’ token
     RPC_MESSAGE_MEMBER(std::unordered_map<crypto::hash COMMA() cryptonote::rpc::transaction_info>, txs);
                                                                                                 ^
/mnt/src/src/rpc/daemon_messages.h:70:52: note: in definition of macro ‘RPC_MESSAGE_MEMBER’
 #define RPC_MESSAGE_MEMBER(type, name) type name = type{}
                                                    ^
/mnt/src/src/rpc/daemon_messages.h:121:51: error: wrong number of template arguments (1, should be at least 2)
     RPC_MESSAGE_MEMBER(std::unordered_map<crypto::hash COMMA() cryptonote::rpc::transaction_info>, txs);
                                                   ^
/mnt/src/src/rpc/daemon_messages.h:70:52: note: in definition of macro ‘RPC_MESSAGE_MEMBER’
 #define RPC_MESSAGE_MEMBER(type, name) type name = type{}
                                                    ^
In file included from /usr/include/c++/5/unordered_map:48:0,
                 from /mnt/src/src/rpc/message_data_structs.h:35,
                 from /mnt/src/src/rpc/message.h:32,
                 from /mnt/src/src/rpc/daemon_messages.h:31,
                 from /mnt/src/src/rpc/daemon_handler.h:31,
                 from /mnt/src/src/rpc/daemon_handler.cpp:29:
/usr/include/c++/5/bits/unordered_map.h:98:11: note: provided for ‘template<class _Key, class _Tp, class _Hash, class _Pred, class _Alloc> class std::unordered_map’
     class unordered_map
           ^
src/rpc/CMakeFiles/obj_daemon_messages.dir/build.make:86: recipe for target 'src/rpc/CMakeFiles/obj_daemon_messages.dir/daemon_messages.cpp.o' failed
make[3]: *** [src/rpc/CMakeFiles/obj_daemon_messages.dir/daemon_messages.cpp.o] Error 1
make[3]: Leaving directory '/mnt/src/build/Linux/master/release'
CMakeFiles/Makefile2:1791: recipe for target 'src/rpc/CMakeFiles/obj_daemon_messages.dir/all' failed
make[2]: *** [src/rpc/CMakeFiles/obj_daemon_messages.dir/all] Error 2
make[2]: *** Waiting for unfinished jobs....
[ 30%] Building CXX object src/rpc/CMakeFiles/obj_daemon_rpc_server.dir/zmq_server.cpp.o
src/rpc/CMakeFiles/obj_daemon_rpc_server.dir/build.make:62: recipe for target 'src/rpc/CMakeFiles/obj_daemon_rpc_server.dir/daemon_handler.cpp.o' failed
make[3]: *** [src/rpc/CMakeFiles/obj_daemon_rpc_server.dir/daemon_handler.cpp.o] Error 1
make[3]: Leaving directory '/mnt/src/build/Linux/master/release'
CMakeFiles/Makefile2:1828: recipe for target 'src/rpc/CMakeFiles/obj_daemon_rpc_server.dir/all' failed
make[2]: *** [src/rpc/CMakeFiles/obj_daemon_rpc_server.dir/all] Error 2
make[3]: Leaving directory '/mnt/src/build/Linux/master/release'
[ 30%] Built target obj_rpc
make[2]: Leaving directory '/mnt/src/build/Linux/master/release'
Makefile:138: recipe for target 'all' failed
make[1]: *** [all] Error 2
make[1]: Leaving directory '/mnt/src/build/Linux/master/release'
Makefile:85: recipe for target 'release-all' failed
make: *** [release-all] Error 2

% git revert f5f7c2ac && make
[...]
[100%] Linking CXX executable unit_tests
[100%] Linking CXX executable ../../bin/monerod
make[3]: Leaving directory '/mnt/src/build/Linux/master/release'
[100%] Built target daemon
make[3]: Leaving directory '/mnt/src/build/Linux/master/release'
[100%] Built target unit_tests
make[2]: Leaving directory '/mnt/src/build/Linux/master/release'
make[1]: Leaving directory '/mnt/src/build/Linux/master/release'
%


# Discussion History
## moneromooo-monero | 2018-10-25T22:52:00+00:00
https://github.com/monero-project/monero/pull/4719

## moneromooo-monero | 2018-10-26T20:43:47+00:00
+resolved

# Action History
- Created by: ndorf | 2018-10-25T22:50:18+00:00
- Closed at: 2018-10-26T20:48:59+00:00
