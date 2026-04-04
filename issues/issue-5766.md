---
title: Statically linking ZMQ
source_url: https://github.com/monero-project/monero/issues/5766
author: ForgedTactics
assignees: []
labels: []
created_at: '2019-07-20T08:55:03+00:00'
updated_at: '2019-07-21T17:39:08+00:00'
type: issue
status: closed
closed_at: '2019-07-21T17:39:08+00:00'
---

# Original Description
Whilst trying to compile a semi-static/dynamic version of monerod, I am receiving some errors:

I have compiled ZMQ statically as per:
https://github.com/monero-project/monero/issues/3989#issuecomment-398272939
```# ZMQ
git clone https://github.com/zeromq/libzmq.git -b v4.2.5 \
    && cd libzmq \
    && ./autogen.sh \
    && CFLAGS="-fPIC" CXXFLAGS="-fPIC" ./configure --enable-static --disable-shared \
    && make \
    && make install \
    && ldconfig

# zmq.hpp
git clone https://github.com/zeromq/cppzmq.git -b v4.2.3 \
    && cd cppzmq \
    && mv *.hpp /usr/local/include
```

When compiling monerod, all of the other static libraries work. However, I end up receiving an error for ZMQ:
```[ 82%] Building CXX object src/rpc/CMakeFiles/obj_daemon_rpc_server.dir/zmq_server.cpp.o
/home/ubuntu/dev/monero/src/rpc/zmq_server.cpp: In member function ‘void cryptonote::rpc::ZmqServer::serve()’:
/home/ubuntu/dev/monero/src/rpc/zmq_server.cpp:63:39: error: no matching function for call to ‘zmq::socket_t::recv(zmq                                               ::message_t*)’
       while (rep_socket->recv(&message))
```

Is there something I am doing wrong that you may have a solution to?

# Discussion History
## moneromooo-monero | 2019-07-20T10:15:42+00:00
See https://github.com/monero-project/monero/pull/5725

## ForgedTactics | 2019-07-21T17:39:08+00:00
AH! Thank you

# Action History
- Created by: ForgedTactics | 2019-07-20T08:55:03+00:00
- Closed at: 2019-07-21T17:39:08+00:00
