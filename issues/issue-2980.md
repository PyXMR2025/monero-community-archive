---
title: Build failing on Ubuntu 14.04 - zmq arguments
source_url: https://github.com/monero-project/monero/issues/2980
author: Divided-Pi
assignees: []
labels: []
created_at: '2017-12-21T01:31:56+00:00'
updated_at: '2017-12-28T04:16:38+00:00'
type: issue
status: closed
closed_at: '2017-12-21T06:14:57+00:00'
---

# Original Description
Hi All, 

I'm building on ubuntu 14.04, I know most of the dependencies are dependent on versions primarily released for 16.04, but I've been compiling packages from source as I go and today I made some good progress. 

but I also hit this issue
[ 46%] Building CXX object src/rpc/CMakeFiles/obj_daemon_rpc_server.dir/zmq_server.cpp.o
/home/[user]/repos/monero/src/rpc/zmq_server.cpp: In member function ‘bool cryptonote::rpc::ZmqServer::addTCPSocket(std::string, std::string)’:
/home/[user]/repos/monero/src/rpc/zmq_server.cpp:105:69: error: no matching function for call to ‘zmq::socket_t::setsockopt(int, const int&)’
     rep_socket->setsockopt(ZMQ_RCVTIMEO, DEFAULT_RPC_RECV_TIMEOUT_MS);
                                                                     ^
In file included from /home/[user]/repos/monero/src/rpc/zmq_server.h:32:0,
                 from /home/[user]/repos/monero/src/rpc/zmq_server.cpp:29:
/usr/include/zmq.hpp:354:21: note: candidate: void zmq::socket_t::setsockopt(int, const void*, size_t)
         inline void setsockopt (int option_, const void *optval_,
                     ^
/usr/include/zmq.hpp:354:21: note:   candidate expects 3 arguments, 2 provided
make[3]: *** [src/rpc/CMakeFiles/obj_daemon_rpc_server.dir/zmq_server.cpp.o] Error 1
make[3]: Leaving directory `/home/[user]/repos/monero/build/release'
make[2]: *** [src/rpc/CMakeFiles/obj_daemon_rpc_server.dir/all] Error 2
make[2]: Leaving directory `/home/[user]/repos/monero/build/release'
make[1]: *** [all] Error 2
make[1]: Leaving directory `/home/[user]/repos/monero/build/release'
make: *** [release-all] Error 2

I have libzmq3-dev installed, but I wouldn't be surprised if it is the wrong version. don't want to bog you guys down with rabbit holes, but even a couple pointers of how to troubleshoot this myself would be a great help

# Discussion History
## stoffu | 2017-12-21T01:44:09+00:00
The error message says there's no function overload of `setsockopt` that takes 2 arguments in your `/usr/include/zmq.hpp`. But I see such a function overload in the latest repository:

https://github.com/zeromq/cppzmq/blob/master/zmq.hpp#L542

Try
```
sudo wget -O /usr/include/zmq.hpp https://raw.githubusercontent.com/zeromq/cppzmq/master/zmq.hpp
```
and build again.


## Divided-Pi | 2017-12-21T03:20:36+00:00
Thank you! that was it - also ran into an issue with the libboost libraries being in the wrong place but got that sorted
To anyone who is building monero ubuntu 14.04 - if you installed libboost 1.58 on your own, make sure your boost_*.so files are in the correct directory (for me it was /usr/lib/x86_64-linux-gnu/ ) otherwise monero will fail to find them)

## Divided-Pi | 2017-12-21T03:34:51+00:00
Build just succeed, got a weird Waring. any reason to be concerned? Thanks Again!
[ 85%] Building CXX object tests/unit_tests/CMakeFiles/unit_tests.dir/crypto.cpp.o
/home/[user]/repos/monero/tests/unit_tests/crypto.cpp:73:8: warning: ‘bool {anonymous}::keccak_harness()’ defined but not used [-Wunused-function]
   bool keccak_harness()
        ^

## stoffu | 2017-12-21T03:50:00+00:00
No, that warning can be safely ignored.

## Divided-Pi | 2017-12-21T06:14:57+00:00
Successfully Built Monerod & xmr-stak on Ubuntu 14.04 for the fglrx miner.

## hyc | 2017-12-28T01:37:51+00:00
Rather than munging system-provided header files, we should instead fix zmq_server.cpp to pass the expected 3rd argument.

## stoffu | 2017-12-28T04:16:38+00:00
@hyc 
Good point. #3020 

# Action History
- Created by: Divided-Pi | 2017-12-21T01:31:56+00:00
- Closed at: 2017-12-21T06:14:57+00:00
