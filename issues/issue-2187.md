---
title: Failed to build on Mac 10.14.2
source_url: https://github.com/monero-project/monero-gui/issues/2187
author: Jaxiea
assignees: []
labels:
- resolved
created_at: '2019-05-31T09:59:44+00:00'
updated_at: '2019-07-03T23:27:41+00:00'
type: issue
status: closed
closed_at: '2019-07-03T23:27:41+00:00'
---

# Original Description
"Scanning dependencies of target mnemonics
[ 51%] Linking CXX static library libmnemonics.a
[ 51%] Built target mnemonics
[ 51%] Building CXX object src/rpc/CMakeFiles/obj_daemon_rpc_server.dir/zmq_server.cpp.o
/Users/jx/monero/src/rpc/zmq_server.cpp:62:26: error: no matching member function for call to 'recv'
      while (rep_socket->recv(&message))
             ~~~~~~~~~~~~^~~~
/usr/local/include/zmq.hpp:1244:27: note: candidate function not viable: no known conversion from 'zmq::message_t *' to 'zmq::message_t &' for
      1st argument; remove &
    detail::recv_result_t recv(message_t &msg, recv_flags flags = recv_flags::none)
                          ^
/usr/local/include/zmq.hpp:1230:34: note: candidate function not viable: no known conversion from 'zmq::message_t *' to 'zmq::mutable_buffer'
      for 1st argument
    detail::recv_buffer_result_t recv(mutable_buffer buf,
                                 ^
/usr/local/include/zmq.hpp:1215:10: note: candidate function not viable: requires 2 arguments, but 1 was provided
    bool recv(message_t *msg_, int flags_
         ^
/usr/local/include/zmq.hpp:1202:12: note: candidate function not viable: requires at least 2 arguments, but 1 was provided
    size_t recv(void *buf_, size_t len_, int flags_ = 0)
           ^
/Users/jx/monero/src/rpc/zmq_server.cpp:73:21: warning: 'send' is deprecated: from 4.3.1, use send taking message_t and send_flags
      [-Wdeprecated-declarations]
        rep_socket->send(reply);
                    ^
/usr/local/include/zmq.hpp:1137:5: note: 'send' has been explicitly marked deprecated here
    ZMQ_DEPRECATED("from 4.3.1, use send taking message_t and send_flags")
    ^
/usr/local/include/zmq.hpp:45:44: note: expanded from macro 'ZMQ_DEPRECATED'
#define ZMQ_DEPRECATED(msg) __attribute__((deprecated(msg)))
                                           ^
1 warning and 1 error generated."

Is this related to dependencies?

# Discussion History
## xiphon | 2019-06-01T13:57:46+00:00
`cppzmq` master is somewhat *broken* at the moment.
Please apply the following patch https://github.com/zeromq/cppzmq/pull/328 or use previous `zmq.hpp` version https://github.com/zeromq/cppzmq/blob/v4.3.0/zmq.hpp

## sanderfoobar | 2019-07-03T23:23:17+00:00
+resolved

# Action History
- Created by: Jaxiea | 2019-05-31T09:59:44+00:00
- Closed at: 2019-07-03T23:27:41+00:00
