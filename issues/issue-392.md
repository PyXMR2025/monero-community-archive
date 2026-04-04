---
title: development doesn't build on freebsd 10.2
source_url: https://github.com/monero-project/monero/issues/392
author: crypto750
assignees: []
labels: []
created_at: '2015-08-29T08:11:38+00:00'
updated_at: '2017-08-08T12:12:16+00:00'
type: issue
status: closed
closed_at: '2017-08-08T12:12:16+00:00'
---

# Original Description
I'm posting here as a followup to keep track of the issue.

pkg install git pkgconf gcc49 cmake libevent2 unbound googletest icu ldns expat bison
make release-static

http://pastebin.com/7mSLNm6A


# Discussion History
## crypto750 | 2015-08-29T10:20:01+00:00
I've managed to compile release-static on Freebsd 10.1...
Broken library: http://pkg.freebsd.org/freebsd:10:x86:64/release_2/All/boost-libs-1.55.0_5.txz
Use the previous one when compiling on 10.2: http://pkg.freebsd.org/freebsd:10:x86:64/release_1/All/boost-libs-1.55.0_4.txz

There is only one problem when I move this static binary to a box with no libevent2 installed:

$ ./bitmonerod 
Shared object "libevent-2.0.so.5" not found, required by "bitmonerod"

I see the same issue on linux - static binary complains about libevent missing when moved to another box. Is this normal?


## crypto750 | 2015-08-29T12:59:25+00:00
When I run bitmonerod on FreeBSD with a --detach option,
it can't connect to peers, the log is full of these:

2015-Aug-29 12:52:06.310125 [P2P0]Failed to connect to any of seed peers, continuing without seeds
2015-Aug-29 12:52:09.175140 [P2P0]Failed to connect to any of seed peers, continuing without seeds
2015-Aug-29 12:52:11.210792 [P2P0]Failed to connect to any of seed peers, continuing without seeds
2015-Aug-29 12:52:13.227779 [P2P0]Failed to connect to any of seed peers, continuing without seeds
2015-Aug-29 12:52:15.246961 [P2P0]Failed to connect to any of seed peers, continuing without seeds
2015-Aug-29 12:52:19.010519 [P2P0]Failed to connect to any of seed peers, continuing without seeds
2015-Aug-29 12:52:26.187094 [P2P9]Failed to connect to any of seed peers, continuing without seeds
2015-Aug-29 12:52:28.234203 [P2P9]Failed to connect to any of seed peers, continuing without seeds
2015-Aug-29 12:52:30.272402 [P2P9]Failed to connect to any of seed peers, continuing without seeds
2015-Aug-29 12:52:32.312657 [P2P9]Failed to connect to any of seed peers, continuing without seeds
2015-Aug-29 12:52:34.329002 [P2P9]Failed to connect to any of seed peers, continuing without seeds


## crypto750 | 2015-08-30T05:37:50+00:00
After syncing about 80% of the chain it stops, I exit, restart and get a segmentation fault.

2015-Aug-30 04:50:09.586410 Initializing cryptonote protocol...
2015-Aug-30 04:50:09.586664 Cryptonote protocol initialized OK
2015-Aug-30 04:50:09.587237 Initializing p2p server...
[New Thread 802c07c00 (LWP 100427/bitmonerod)]
2015-Aug-30 04:50:09.615206 Set limit-up to 2048 kB/s
2015-Aug-30 04:50:09.615606 Set limit-down to 8192 kB/s
2015-Aug-30 04:50:09.615802 Set limit-up to 2048 kB/s
2015-Aug-30 04:50:09.615991 Set limit-down to 8192 kB/s
2015-Aug-30 04:50:09.616333 ERROR /root/bitmonero/src/p2p/net_node.inl:151 Exception at [node_server::init_config], what=invalid signature
2015-Aug-30 04:50:09.616537 ERROR /root/bitmonero/src/p2p/net_node.inl:413 Failed to init config.
2015-Aug-30 04:50:09.616944 Deinitializing core...
2015-Aug-30 04:50:09.617130 Mining has been stopped, 0 finished
2015-Aug-30 04:50:09.617308 Closing IO Service.
2015-Aug-30 04:50:09.617527 Failed to deinitialize core...
2015-Aug-30 04:50:09.617750 Mining has been stopped, 0 finished
2015-Aug-30 04:50:09.617918 Deinitializing cryptonote_protocol...
2015-Aug-30 04:50:09.618152 ERROR /root/bitmonero/src/daemon/main.cpp:279 Exception in main! Failed to initialize p2p server.
[New Thread 802c06400 (LWP 100404/bitmonerod)]

Program received signal SIGSEGV, Segmentation fault.
[Switching to Thread 802c06400 (LWP 100404/bitmonerod)]
0x0000000000430932 in std::__1::__tree_balance_after_insertstd::__1::__tree_node_base<void*_> ()
(gdb) bt
#0  0x0000000000430932 in std::__1::__tree_balance_after_insert<std::__1::__tree_node_base<void_>*> ()
#1  0x0000000000727424 in nOT::nUtils::cLogger::Thread2Number ()
#2  0x00000000007261b3 in nOT::nUtils::cLogger::write_stream ()
#3  0x0000000000752141 in epee::net_utils::data_logger::~data_logger ()
#4  0x00000000007633cd in std::__1::unique_ptr<epee::net_utils::data_logger, std::__1::default_delete<epee::net_utils::data_logger> >::~unique_ptr ()
#5  0x0000000802349050 in __cxa_finalize () from /lib/libc.so.7
#6  0x00000008022ea57c in exit () from /lib/libc.so.7
#7  0x0000000000419026 in _start ()
#8  0x0000000800c54000 in ?? ()
#9  0x0000000000000000 in ?? ()


## crypto750 | 2015-08-30T15:53:36+00:00
0MQ compilation on FreeBSD is not successful.
libzmq and czmq were installed from github sources.

[ 79%] Building CXX object src/ipc/CMakeFiles/client_ipc.dir/wap_proto.c.o
CC: warning: treating 'c' input as 'c++' when in C++ mode, this behavior is deprecated
/root/bitmonero/src/ipc/wap_proto.c:2547:5: error: no matching function for call to 'zlist_append'
    zlist_append (blocks_block_ids, "Name: Brutus");
    ^~~~~~~~~~~~
/usr/local/include/zlist.h:72:5: note: candidate function not viable: no known conversion from 'const char [13]' to 'void _' for 2nd argument
    zlist_append (zlist_t *self, void *item);
    ^
/root/bitmonero/src/ipc/wap_proto.c:2548:5: error: no matching function for call to 'zlist_append'
    zlist_append (blocks_block_ids, "Age: 43");
    ^~~~~~~~~~~~
/usr/local/include/zlist.h:72:5: note: candidate function not viable: no known conversion from 'const char [8]' to 'void *' for 2nd argument
    zlist_append (zlist_t *self, void *item);
    ^
2 errors generated.
*_\* Error code 1

Quote:
your compiler flags (the defaults of which in this case are determined by FreeBSD and Debian). Debian's default compiler flags were allowing you to pass char \* arguments to a void \* parameter, but FreeBSD's default flags are not allowing this.

You should use an explicit casts to void \* here:

zlist_append (blocks_block_ids, (void *) "Name: Brutus");
zlist_append (blocks_block_ids, (void *) "Age: 43");

more of this:

[ 80%] Building CXX object src/ipc/CMakeFiles/server_ipc.dir/wap_server/wap_server.c.o
CC: warning: treating 'c' input as 'c++' when in C++ mode, this behavior is deprecated
In file included from /root/bitmonero/src/ipc/wap_server/wap_server.c:56:
/root/bitmonero/src/ipc/include/wap_server_engine.inc:1551:22: error: assigning to 'char *' from incompatible type 'const char *'
    self->log_prefix = args? (char *) args: "";
                     ^ ~~~~~~~~~~~~~~~~~~~~~~~
/root/bitmonero/src/ipc/wap_server/wap_server.c:114:24: error: no matching function for call to 'zactor_new'
    zactor_t *server = zactor_new (wap_server, "server");
                       ^~~~~~~~~~


## crypto750 | 2015-09-25T19:17:59+00:00
Master branch doesn't compile with the new hardfork commits on Freebsd 10.2.

[ 70%] Building CXX object 
src/cryptonote_core/CMakeFiles/cryptonote_core.dir/hardfork.cpp.o
/usr/home/test/bitmonero/src/cryptonote_core/hardfork.cpp:63:22: error: use of GNU old-style field
      designator extension [-Werror,-Wgnu-designator]
  heights.push_back({version: version, height: height, time: time});
                     ^~~~~~~~
                     .version = 
/usr/home/test/bitmonero/src/cryptonote_core/hardfork.cpp:63:40: error: use of GNU old-style field
      designator extension [-Werror,-Wgnu-designator]
  heights.push_back({version: version, height: height, time: time});
                                       ^~~~~~~
                                       .height = 
/usr/home/test/bitmonero/src/cryptonote_core/hardfork.cpp:63:56: error: use of GNU old-style field
      designator extension [-Werror,-Wgnu-designator]
  heights.push_back({version: version, height: height, time: time});
                                                       ^~~~~
                                                       .time = 
3 errors generated.
**\* Error code 1


## crypto750 | 2015-09-25T19:21:23+00:00
FreeBSD 9.3 didn't compile master branch before hardfork commits.
0MQ on FreeBSD 10.2 pre-hardfork commits also fails, see the comments above.


## crypto750 | 2015-09-29T10:14:59+00:00
FreeBSD 10.2, master branch builds with commits 409, 410.

FreeBSD 10.2, development branch doesn't build with commits 407, 408.

pkg install libtool autoconf automake; 
git clone https://github.com/jedisct1/libsodium; cd libsodium; ./autogen.sh; ./configure; make; make install; cp libsodium.pc /usr/local/libdata/pkgconfig/;
cd; git clone https://github.com/zeromq/libzmq; cd libzmq; ./autogen.sh; ./configure; make; make install; cp src/libzmq.pc /usr/local/libdata/pkgconfig/;
cd; git clone https://github.com/zeromq/czmq; cd czmq; ./autogen.sh; ./configure; make; make install; cp src/libczmq.pc /usr/local/libdata/pkgconfig/;

[ 81%] Building CXX object src/ipc/CMakeFiles/server_ipc.dir/wap_server/wap_server.c.o
CC: warning: treating 'c' input as 'c++' when in C++ mode, this behavior is deprecated
In file included from /root/bitmonero/src/ipc/wap_server/wap_server.c:56:
/root/bitmonero/src/ipc/include/wap_server_engine.inc:1551:22: error: assigning to 'char _' from incompatible type 'const char *'
    self->log_prefix = args? (char *) args: "";
                     ^ ~~~~~~~~~~~~~~~~~~~~~~~
/root/bitmonero/src/ipc/wap_server/wap_server.c:114:24: error: no matching function for call to 'zactor_new'
    zactor_t *server = zactor_new (wap_server, "server");
                       ^~~~~~~~~~
/usr/local/include/zactor.h:30:5: note: candidate function not viable: no known conversion from 'const char [7]' to 'void *' for 2nd argument
    zactor_new (zactor_fn task, void *args);
    ^
In file included from /root/bitmonero/src/ipc/wap_server/wap_server.c:22:
In file included from /root/bitmonero/src/ipc/include/daemon_ipc_handlers.h:42:
In file included from /root/bitmonero/src/cryptonote_core/cryptonote_core.h:39:
In file included from /root/bitmonero/src/cryptonote_protocol/cryptonote_protocol_handler_common.h:34:
In file included from /root/bitmonero/src/cryptonote_protocol/cryptonote_protocol_defs.h:35:
In file included from /root/bitmonero/src/cryptonote_core/cryptonote_basic.h:41:
/root/bitmonero/src/serialization/binary_archive.h:194:28: warning: shift count >= width of type [-Wshift-count-overflow]
      if (1 < sizeof(T)) v >>= 8;
                           ^   ~
/root/bitmonero/src/serialization/binary_archive.h:187:5: note: in instantiation of function template specialization 'binary_archive<true>::serialize_uint<unsigned char>' requested here
    serialize_uint(static_cast<typename boost::make_unsigned<T>::type>(v));
    ^
/root/bitmonero/src/serialization/binary_archive.h:227:5: note: in instantiation of function template specialization 'binary_archive<true>::serialize_int<unsigned char>' requested here
    serialize_int(t);
    ^
1 warning and 2 errors generated.
*_\* Error code 1


## ghost | 2016-09-15T19:59:42+00:00
Hi @crypto750 is this still an issue for you or can this be closed now?


## anonimal | 2016-09-15T20:33:10+00:00
@NanoAkron this is issue far from closed. Monero on FreeBSD requires (or should require) clang + boost 1.58. Build instructions need to be updated along with build fixes. Also see [this comment](https://github.com/monero-project/monero/pull/964#issuecomment-241198395).

This issue should be renamed though since branch `development` was removed a while ago.


## moneromooo-monero | 2017-08-08T11:12:30+00:00
FreeBSD now builds fine (https://build.getmonero.org/builders/monero-static-freebsd64 shows only the DNSSEC failure test fails, as with most other build machines).

+resolved

# Action History
- Created by: crypto750 | 2015-08-29T08:11:38+00:00
- Closed at: 2017-08-08T12:12:16+00:00
