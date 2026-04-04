---
title: Failed to build static binaries of 0.11.1.0 on Ubuntu 14.
source_url: https://github.com/monero-project/monero/issues/2777
author: ViperRu
assignees: []
labels: []
created_at: '2017-11-08T10:21:32+00:00'
updated_at: '2017-11-08T22:33:23+00:00'
type: issue
status: closed
closed_at: '2017-11-08T22:33:22+00:00'
---

# Original Description
> dpkg -l |grep zmq
```
ii  libzmq3:amd64                               4.0.4+dfsg-2                                      amd64        lightweight messaging kernel (shared library)
ii  libzmq3-dev:amd64                           4.0.4+dfsg-2                                      amd64        lightweight messaging kernel (development files)
```
> make release-static
```
Linking CXX executable ../../bin/monerod
/usr/lib/gcc/x86_64-linux-gnu/5/../../../x86_64-linux-gnu/libzmq.a(libzmq_la-ipc_listener.o): In function `zmq::ipc_listener_t::set_address(char const*)':
(.text+0x5ed): warning: the use of `tempnam' is dangerous, better use `mkstemp'
/usr/lib/gcc/x86_64-linux-gnu/5/../../../x86_64-linux-gnu/libzmq.a(libzmq_la-zmq.o): In function `zmq_ctx_new':
(.text+0xc5): undefined reference to `pgm_init'
/usr/lib/gcc/x86_64-linux-gnu/5/../../../x86_64-linux-gnu/libzmq.a(libzmq_la-zmq.o): In function `zmq_ctx_new':
(.text+0x191): undefined reference to `pgm_error_free'
/usr/lib/gcc/x86_64-linux-gnu/5/../../../x86_64-linux-gnu/libzmq.a(libzmq_la-zmq.o): In function `zmq_ctx_term':
(.text+0x261): undefined reference to `pgm_shutdown'
/usr/lib/gcc/x86_64-linux-gnu/5/../../../x86_64-linux-gnu/libzmq.a(libzmq_la-socket_base.o): In function `zmq::socket_base_t::connect(char const*)':
(.text+0x24e2): undefined reference to `pgm_freeaddrinfo'
/usr/lib/gcc/x86_64-linux-gnu/5/../../../x86_64-linux-gnu/libzmq.a(libzmq_la-pgm_socket.o): In function `zmq::pgm_socket_t::init_address(char const*, pgm_addrinfo_t**, unsigned short*)':
(.text+0xc3): undefined reference to `pgm_getaddrinfo'
/usr/lib/gcc/x86_64-linux-gnu/5/../../../x86_64-linux-gnu/libzmq.a(libzmq_la-pgm_socket.o): In function `zmq::pgm_socket_t::init_address(char const*, pgm_addrinfo_t**, unsigned short*)':
(.text+0x145): undefined reference to `pgm_error_free'
/usr/lib/gcc/x86_64-linux-gnu/5/../../../x86_64-linux-gnu/libzmq.a(libzmq_la-pgm_socket.o): In function `zmq::pgm_socket_t::~pgm_socket_t()':
(.text+0x1db): undefined reference to `pgm_close'
/usr/lib/gcc/x86_64-linux-gnu/5/../../../x86_64-linux-gnu/libzmq.a(libzmq_la-pgm_socket.o): In function `zmq::pgm_socket_t::get_receiver_fds(int*, int*)':
(.text+0x39d): undefined reference to `pgm_getsockopt'
/usr/lib/gcc/x86_64-linux-gnu/5/../../../x86_64-linux-gnu/libzmq.a(libzmq_la-pgm_socket.o): In function `zmq::pgm_socket_t::get_receiver_fds(int*, int*)':
(.text+0x3d2): undefined reference to `pgm_getsockopt'
/usr/lib/gcc/x86_64-linux-gnu/5/../../../x86_64-linux-gnu/libzmq.a(libzmq_la-pgm_socket.o): In function `zmq::pgm_socket_t::get_sender_fds(int*, int*, int*, int*)':
(.text+0x59d): undefined reference to `pgm_getsockopt'
/usr/lib/gcc/x86_64-linux-gnu/5/../../../x86_64-linux-gnu/libzmq.a(libzmq_la-pgm_socket.o): In function `zmq::pgm_socket_t::get_sender_fds(int*, int*, int*, int*)':
(.text+0x5d2): undefined reference to `pgm_getsockopt'
/usr/lib/gcc/x86_64-linux-gnu/5/../../../x86_64-linux-gnu/libzmq.a(libzmq_la-pgm_socket.o): In function `zmq::pgm_socket_t::get_sender_fds(int*, int*, int*, int*)':
(.text+0x607): undefined reference to `pgm_getsockopt'
/usr/lib/gcc/x86_64-linux-gnu/5/../../../x86_64-linux-gnu/libzmq.a(libzmq_la-pgm_socket.o):(.text+0x63c): more undefined references to `pgm_getsockopt' follow
/usr/lib/gcc/x86_64-linux-gnu/5/../../../x86_64-linux-gnu/libzmq.a(libzmq_la-pgm_socket.o): In function `zmq::pgm_socket_t::send(unsigned char*, unsigned long)':
(.text+0x922): undefined reference to `pgm_send'
/usr/lib/gcc/x86_64-linux-gnu/5/../../../x86_64-linux-gnu/libzmq.a(libzmq_la-pgm_socket.o): In function `zmq::pgm_socket_t::get_rx_timeout()':
(.text+0xa80): undefined reference to `pgm_getsockopt'
/usr/lib/gcc/x86_64-linux-gnu/5/../../../x86_64-linux-gnu/libzmq.a(libzmq_la-pgm_socket.o): In function `zmq::pgm_socket_t::get_tx_timeout()':
(.text+0xb31): undefined reference to `pgm_getsockopt'
/usr/lib/gcc/x86_64-linux-gnu/5/../../../x86_64-linux-gnu/libzmq.a(libzmq_la-pgm_socket.o): In function `zmq::pgm_socket_t::get_max_tsdu_size()':
(.text+0xbdc): undefined reference to `pgm_getsockopt'
/usr/lib/gcc/x86_64-linux-gnu/5/../../../x86_64-linux-gnu/libzmq.a(libzmq_la-pgm_socket.o): In function `zmq::pgm_socket_t::init(bool, char const*)':
(.text+0xd2a): undefined reference to `pgm_socket'
/usr/lib/gcc/x86_64-linux-gnu/5/../../../x86_64-linux-gnu/libzmq.a(libzmq_la-pgm_socket.o): In function `zmq::pgm_socket_t::init(bool, char const*)':
(.text+0xd9e): undefined reference to `pgm_setsockopt'
/usr/lib/gcc/x86_64-linux-gnu/5/../../../x86_64-linux-gnu/libzmq.a(libzmq_la-pgm_socket.o): In function `zmq::pgm_socket_t::init(bool, char const*)':
(.text+0xdc3): undefined reference to `pgm_setsockopt'
/usr/lib/gcc/x86_64-linux-gnu/5/../../../x86_64-linux-gnu/libzmq.a(libzmq_la-pgm_socket.o): In function `zmq::pgm_socket_t::init(bool, char const*)':
(.text+0xe08): undefined reference to `pgm_setsockopt'
/usr/lib/gcc/x86_64-linux-gnu/5/../../../x86_64-linux-gnu/libzmq.a(libzmq_la-pgm_socket.o): In function `zmq::pgm_socket_t::init(bool, char const*)':
(.text+0xe35): undefined reference to `pgm_setsockopt'
/usr/lib/gcc/x86_64-linux-gnu/5/../../../x86_64-linux-gnu/libzmq.a(libzmq_la-pgm_socket.o): In function `zmq::pgm_socket_t::init(bool, char const*)':
(.text+0xedd): undefined reference to `pgm_setsockopt'
/usr/lib/gcc/x86_64-linux-gnu/5/../../../x86_64-linux-gnu/libzmq.a(libzmq_la-pgm_socket.o): In function `zmq::pgm_socket_t::init(bool, char const*)':
(.text+0xefb): undefined reference to `pgm_close'
/usr/lib/gcc/x86_64-linux-gnu/5/../../../x86_64-linux-gnu/libzmq.a(libzmq_la-pgm_socket.o): In function `zmq::pgm_socket_t::init(bool, char const*)':
(.text+0xf11): undefined reference to `pgm_freeaddrinfo'
/usr/lib/gcc/x86_64-linux-gnu/5/../../../x86_64-linux-gnu/libzmq.a(libzmq_la-pgm_socket.o): In function `zmq::pgm_socket_t::init(bool, char const*)':
(.text+0xf29): undefined reference to `pgm_error_free'
/usr/lib/gcc/x86_64-linux-gnu/5/../../../x86_64-linux-gnu/libzmq.a(libzmq_la-pgm_socket.o): In function `zmq::pgm_socket_t::init(bool, char const*)':
(.text+0xf7e): undefined reference to `pgm_socket'
/usr/lib/gcc/x86_64-linux-gnu/5/../../../x86_64-linux-gnu/libzmq.a(libzmq_la-pgm_socket.o): In function `zmq::pgm_socket_t::init(bool, char const*)':
(.text+0xfff): undefined reference to `pgm_setsockopt'
/usr/lib/gcc/x86_64-linux-gnu/5/../../../x86_64-linux-gnu/libzmq.a(libzmq_la-pgm_socket.o): In function `zmq::pgm_socket_t::init(bool, char const*)':
(.text+0x10cb): undefined reference to `pgm_setsockopt'
/usr/lib/gcc/x86_64-linux-gnu/5/../../../x86_64-linux-gnu/libzmq.a(libzmq_la-pgm_socket.o): In function `zmq::pgm_socket_t::init(bool, char const*)':
(.text+0x10f3): undefined reference to `pgm_setsockopt'
/usr/lib/gcc/x86_64-linux-gnu/5/../../../x86_64-linux-gnu/libzmq.a(libzmq_la-pgm_socket.o): In function `zmq::pgm_socket_t::init(bool, char const*)':
(.text+0x1120): undefined reference to `pgm_setsockopt'
/usr/lib/gcc/x86_64-linux-gnu/5/../../../x86_64-linux-gnu/libzmq.a(libzmq_la-pgm_socket.o): In function `zmq::pgm_socket_t::init(bool, char const*)':
(.text+0x1148): undefined reference to `pgm_setsockopt'
/usr/lib/gcc/x86_64-linux-gnu/5/../../../x86_64-linux-gnu/libzmq.a(libzmq_la-pgm_socket.o):(.text+0x1189): more undefined references to `pgm_setsockopt' follow
/usr/lib/gcc/x86_64-linux-gnu/5/../../../x86_64-linux-gnu/libzmq.a(libzmq_la-pgm_socket.o): In function `zmq::pgm_socket_t::init(bool, char const*)':
(.text+0x12ef): undefined reference to `pgm_gsi_create_from_data'
/usr/lib/gcc/x86_64-linux-gnu/5/../../../x86_64-linux-gnu/libzmq.a(libzmq_la-pgm_socket.o): In function `zmq::pgm_socket_t::init(bool, char const*)':
(.text+0x1348): undefined reference to `pgm_bind3'
/usr/lib/gcc/x86_64-linux-gnu/5/../../../x86_64-linux-gnu/libzmq.a(libzmq_la-pgm_socket.o): In function `zmq::pgm_socket_t::init(bool, char const*)':
(.text+0x1409): undefined reference to `pgm_setsockopt'
/usr/lib/gcc/x86_64-linux-gnu/5/../../../x86_64-linux-gnu/libzmq.a(libzmq_la-pgm_socket.o): In function `zmq::pgm_socket_t::init(bool, char const*)':
(.text+0x1488): undefined reference to `pgm_setsockopt'
/usr/lib/gcc/x86_64-linux-gnu/5/../../../x86_64-linux-gnu/libzmq.a(libzmq_la-pgm_socket.o): In function `zmq::pgm_socket_t::init(bool, char const*)':
(.text+0x149a): undefined reference to `pgm_freeaddrinfo'
/usr/lib/gcc/x86_64-linux-gnu/5/../../../x86_64-linux-gnu/libzmq.a(libzmq_la-pgm_socket.o): In function `zmq::pgm_socket_t::init(bool, char const*)':
(.text+0x14c8): undefined reference to `pgm_setsockopt'
/usr/lib/gcc/x86_64-linux-gnu/5/../../../x86_64-linux-gnu/libzmq.a(libzmq_la-pgm_socket.o): In function `zmq::pgm_socket_t::init(bool, char const*)':
(.text+0x14f5): undefined reference to `pgm_setsockopt'
/usr/lib/gcc/x86_64-linux-gnu/5/../../../x86_64-linux-gnu/libzmq.a(libzmq_la-pgm_socket.o): In function `zmq::pgm_socket_t::init(bool, char const*)':
(.text+0x1526): undefined reference to `pgm_setsockopt'
/usr/lib/gcc/x86_64-linux-gnu/5/../../../x86_64-linux-gnu/libzmq.a(libzmq_la-pgm_socket.o): In function `zmq::pgm_socket_t::init(bool, char const*)':
(.text+0x154b): undefined reference to `pgm_setsockopt'
/usr/lib/gcc/x86_64-linux-gnu/5/../../../x86_64-linux-gnu/libzmq.a(libzmq_la-pgm_socket.o): In function `zmq::pgm_socket_t::init(bool, char const*)':
(.text+0x155e): undefined reference to `pgm_connect'
/usr/lib/gcc/x86_64-linux-gnu/5/../../../x86_64-linux-gnu/libzmq.a(libzmq_la-pgm_socket.o): In function `zmq::pgm_socket_t::receive(void**, pgm_tsi_t const**)':
(.text+0x1923): undefined reference to `pgm_recvmsgv'
/usr/lib/gcc/x86_64-linux-gnu/5/../../../x86_64-linux-gnu/libzmq.a(libzmq_la-pgm_socket.o): In function `zmq::pgm_socket_t::receive(void**, pgm_tsi_t const**)':
(.text+0x1a8f): undefined reference to `pgm_free'
/usr/lib/gcc/x86_64-linux-gnu/5/../../../x86_64-linux-gnu/libzmq.a(libzmq_la-pgm_socket.o): In function `zmq::pgm_socket_t::process_upstream()':
(.text+0x1d98): undefined reference to `pgm_recvmsgv'
collect2: error: ld returned 1 exit status
```

# Discussion History
## moneromooo-monero | 2017-11-08T10:58:14+00:00
Should be fixed by https://github.com/monero-project/monero/pull/2689

## ViperRu | 2017-11-08T12:25:12+00:00
> git checkout master

After changing the one string (without this change the project is not build using "make" without parameters):
```
diff --git a/src/rpc/zmq_server.cpp b/src/rpc/zmq_server.cpp
index afdff23..6f06f44 100644
--- a/src/rpc/zmq_server.cpp
+++ b/src/rpc/zmq_server.cpp
@@ -102,7 +102,7 @@ bool ZmqServer::addTCPSocket(std::string address, std::string port)
 
     rep_socket.reset(new zmq::socket_t(context, ZMQ_REP));
 
-    rep_socket->setsockopt(ZMQ_RCVTIMEO, DEFAULT_RPC_RECV_TIMEOUT_MS);
+    rep_socket->setsockopt(ZMQ_RCVTIMEO, &DEFAULT_RPC_RECV_TIMEOUT_MS, sizeof(DEFAULT_RPC_RECV_TIMEOUT_MS));
 
     std::string bind_address = addr_prefix + address + std::string(":") + port;
     rep_socket->bind(bind_address.c_str());

```
I do:
> make clean
> make release-static

And I have the same error.


## moneromooo-monero | 2017-11-08T19:08:37+00:00
Do you have libpgm and/or libnorm installed ?

## ViperRu | 2017-11-08T20:26:56+00:00
@moneromooo-monero 
Wow thanks. The problem was solved by install libpgm-dev.
Sorry, but can you  add the change to mainstream from comment above? Without it there is the error on  Ubuntu 14.04:
```
[ 82%] Building CXX object src/rpc/CMakeFiles/obj_daemon_rpc_server.dir/zmq_server.cpp.o
/home/my/bitmonero/src/rpc/zmq_server.cpp: In member function ‘bool cryptonote::rpc::ZmqServer::addTCPSocket(std::string, std::string)’:
/home/my/bitmonero/src/rpc/zmq_server.cpp:105:69: error: no matching function for call to ‘zmq::socket_t::setsockopt(int, const int&)’
     rep_socket->setsockopt(ZMQ_RCVTIMEO, DEFAULT_RPC_RECV_TIMEOUT_MS);
                                                                     ^
In file included from /home/my/bitmonero/src/rpc/zmq_server.h:32:0,
                 from /home/my/bitmonero/src/rpc/zmq_server.cpp:29:
/usr/include/zmq.hpp:354:21: note: candidate: void zmq::socket_t::setsockopt(int, const void*, size_t)
         inline void setsockopt (int option_, const void *optval_,
                     ^
/usr/include/zmq.hpp:354:21: note:   candidate expects 3 arguments, 2 provided
make[3]: *** [src/rpc/CMakeFiles/obj_daemon_rpc_server.dir/zmq_server.cpp.o] Error 1
```

## moneromooo-monero | 2017-11-08T20:55:26+00:00
tewinget said he'd have look at this in another bug.

## ViperRu | 2017-11-08T22:33:22+00:00
Thank you.

# Action History
- Created by: ViperRu | 2017-11-08T10:21:32+00:00
- Closed at: 2017-11-08T22:33:22+00:00
