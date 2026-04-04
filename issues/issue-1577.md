---
title: 0.12.3build error
source_url: https://github.com/monero-project/monero-gui/issues/1577
author: lyfbuaa
assignees: []
labels:
- resolved
created_at: '2018-10-01T14:38:20+00:00'
updated_at: '2018-10-13T19:18:21+00:00'
type: issue
status: closed
closed_at: '2018-10-13T19:18:21+00:00'
---

# Original Description
linux:
command:./build.sh release-static
error info:
make[2]: *** [src/wallet/CMakeFiles/wallet_rpc_server.dir/build.make:123: bin/monero-wallet-rpc] Error 1
make[1]: *** [CMakeFiles/Makefile2:2316: src/wallet/CMakeFiles/wallet_rpc_server.dir/all] Error 2
make: *** [Makefile:141: all] Error 2
[  3%] Built target blocks
[  3%] Built target obj_device
[  8%] Built target obj_wallet
[  8%] Built target obj_ringct
[  8%] Built target easylogging
[  8%] Built target lmdb
[ 11%] Built target obj_ringct_basic
[ 11%] Built target genversion
[ 16%] Built target generate_translations_header
[ 24%] Built target obj_cncrypto
[ 25%] Built target obj_checkpoints
[ 64%] Built target unbound
[ 69%] Built target obj_cryptonote_core
[ 69%] Built target obj_cryptonote_basic
[ 70%] Built target obj_multisig
[ 70%] Built target obj_rpc_base
[ 70%] Built target obj_mnemonics
[ 72%] Built target obj_blockchain_db
[ 77%] Built target epee
[ 82%] Built target obj_wallet_api
[ 87%] Built target obj_common
[ 88%] Built target obj_version
[ 89%] Built target cncrypto
[ 89%] Built target mnemonics
[ 92%] Built target version
[ 92%] Built target wallet_merged
[ 92%] Built target common
[ 93%] Built target rpc_base
[ 94%] Built target checkpoints
[ 94%] Built target ringct_basic
[ 96%] Built target device
[ 96%] Built target cryptonote_basic
[ 96%] Built target ringct
[ 96%] Built target multisig
[ 97%] Built target blockchain_db
[ 98%] Built target cryptonote_core
[ 98%] Built target wallet
[100%] Linking CXX executable ../../bin/monero-wallet-rpc
/usr/lib/gcc/x86_64-redhat-linux/8/../../../../lib64/libcrypto.a(c_zlib.o): In function `c_zlib.c':
(.text+0x3b): undefined reference to `inflate'
/usr/lib/gcc/x86_64-redhat-linux/8/../../../../lib64/libcrypto.a(c_zlib.o): In function `zlib_stateful_compress_block':
(.text+0xac): undefined reference to `deflate'
/usr/lib/gcc/x86_64-redhat-linux/8/../../../../lib64/libcrypto.a(c_zlib.o): In function `zlib_stateful_finish':
(.text+0xdd): undefined reference to `inflateEnd'
(.text+0xe6): undefined reference to `deflateEnd'
/usr/lib/gcc/x86_64-redhat-linux/8/../../../../lib64/libcrypto.a(c_zlib.o): In function `zlib_stateful_init':
(.text+0x1ac): undefined reference to `inflateInit_'
(.text+0x21a): undefined reference to `deflateInit_'
/usr/lib/gcc/x86_64-redhat-linux/8/../../../../lib64/libcrypto.a(c_zlib.o): In function `bio_zlib_ctrl':
(.text+0x46c): undefined reference to `deflate'
(.text+0x5a4): undefined reference to `zError'
/usr/lib/gcc/x86_64-redhat-linux/8/../../../../lib64/libcrypto.a(c_zlib.o): In function `bio_zlib_write':
(.text+0x6aa): undefined reference to `deflate'
(.text+0x77c): undefined reference to `zError'
(.text+0x7eb): undefined reference to `deflateInit_'
/usr/lib/gcc/x86_64-redhat-linux/8/../../../../lib64/libcrypto.a(c_zlib.o): In function `bio_zlib_read':
(.text+0x8dc): undefined reference to `inflate'
(.text+0x97c): undefined reference to `zError'
(.text+0x9d4): undefined reference to `inflateInit_'
/usr/lib/gcc/x86_64-redhat-linux/8/../../../../lib64/libcrypto.a(c_zlib.o): In function `bio_zlib_free':
(.text+0xa49): undefined reference to `inflateEnd'
(.text+0xa74): undefined reference to `deflateEnd'
collect2: error: ld returned 1 exit status
make[2]: *** [src/wallet/CMakeFiles/wallet_rpc_server.dir/build.make:123: bin/monero-wallet-rpc] Error 1
make[1]: *** [CMakeFiles/Makefile2:2316: src/wallet/CMakeFiles/wallet_rpc_server.dir/all] Error 2
make: *** [Makefile:141: all] Error 2
~/monero-gui/monero/build/release-static ~/monero-gui ~/monero-gui
~/monero-gui/monero/build/release-static/src/daemon ~/monero-gui/monero/build/release-static ~/monero-gui ~/monero-gui
Scanning dependencies of target libminiupnpc-static
[  3%] Built target generate_translations_header
[  4%] Built target easylogging
[  6%] Built target blocks
[ 15%] Built target obj_cncrypto
[ 17%] Built target obj_ringct_basic
[ 18%] Built target lmdb
[ 18%] Built target obj_ringct
[ 19%] Built target obj_device
[ 19%] Built target genversion
[ 20%] Built target obj_checkpoints
[ 20%] Building C object external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-static.dir/miniupnpc.c.o
[ 22%] Building C object external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-static.dir/igd_desc_parse.c.o
[ 22%] Building C object external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-static.dir/minixml.c.o
[ 23%] Building C object external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-static.dir/minisoap.c.o
[ 59%] Built target unbound
[ 61%] Built target obj_cryptonote_core
[ 63%] Built target obj_blockchain_db
[ 65%] Built target obj_cryptonote_basic
[ 65%] Built target obj_rpc_base
[ 66%] Built target obj_multisig
Scanning dependencies of target obj_daemon_rpc_server
[ 66%] Building C object external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-static.dir/minissdpc.c.o
Scanning dependencies of target obj_rpc
Scanning dependencies of target obj_daemonizer
Scanning dependencies of target obj_daemon_messages
[ 66%] Building CXX object src/rpc/CMakeFiles/obj_daemon_rpc_server.dir/daemon_handler.cpp.o
[ 67%] Building CXX object src/daemonizer/CMakeFiles/obj_daemonizer.dir/posix_fork.cpp.o
[ 67%] Building CXX object src/rpc/CMakeFiles/obj_rpc.dir/core_rpc_server.cpp.o
Scanning dependencies of target obj_serialization
Scanning dependencies of target obj_p2p
Scanning dependencies of target obj_cryptonote_protocol
[ 67%] Building CXX object src/rpc/CMakeFiles/obj_daemon_messages.dir/message.cpp.o
[ 67%] Building CXX object src/serialization/CMakeFiles/obj_serialization.dir/json_object.cpp.o
[ 67%] Building CXX object src/cryptonote_protocol/CMakeFiles/obj_cryptonote_protocol.dir/block_queue.cpp.o
[ 67%] Building CXX object src/p2p/CMakeFiles/obj_p2p.dir/net_node.cpp.o
[ 68%] Building CXX object src/cryptonote_protocol/CMakeFiles/obj_cryptonote_protocol.dir/cryptonote_protocol_handler-base.cpp.o
[ 69%] Building CXX object src/rpc/CMakeFiles/obj_daemon_messages.dir/daemon_messages.cpp.o
[ 70%] Building CXX object src/rpc/CMakeFiles/obj_rpc.dir/instanciations.cpp.o
[ 70%] Building CXX object src/rpc/CMakeFiles/obj_daemon_rpc_server.dir/zmq_server.cpp.o
[ 70%] Building C object external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-static.dir/miniwget.c.o
[ 72%] Building C object external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-static.dir/upnpcommands.c.o
[ 72%] Building C object external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-static.dir/upnpdev.c.o
[ 73%] Building C object external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-static.dir/upnpreplyparse.c.o
[ 73%] Built target obj_daemonizer
[ 77%] Built target epee
[ 82%] Built target obj_common
[ 82%] Building C object external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-static.dir/upnperrors.c.o
Scanning dependencies of target epee_readline
[ 83%] Building CXX object contrib/epee/src/CMakeFiles/epee_readline.dir/readline_buffer.cpp.o
[ 83%] Building C object external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-static.dir/connecthostport.c.o
[ 84%] Building C object external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-static.dir/portlistingparse.c.o
[ 84%] Building C object external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-static.dir/receivedata.c.o
[ 86%] Linking C static library libminiupnpc.a
[ 86%] Built target libminiupnpc-static
[ 87%] Built target obj_version
[ 88%] Built target cncrypto
[ 89%] Built target version
[ 89%] Built target common
[ 90%] Built target ringct_basic
[ 90%] Built target checkpoints
[ 91%] Built target rpc_base
Scanning dependencies of target daemonizer
[ 91%] Linking CXX static library libdaemonizer.a
[ 91%] Built target daemonizer
[ 93%] Built target device
[ 93%] Built target cryptonote_basic
[ 93%] Built target ringct
[ 93%] Built target multisig
[ 94%] Built target blockchain_db
[ 95%] Built target cryptonote_core
[ 95%] Linking CXX static library libepee_readline.a
[ 95%] Built target epee_readline
[ 95%] Built target obj_serialization
[ 95%] Built target obj_daemon_messages
[ 95%] Built target obj_cryptonote_protocol
[ 95%] Built target obj_p2p
Scanning dependencies of target p2p
[ 95%] Linking CXX static library libp2p.a
[ 95%] Built target p2p
Scanning dependencies of target cryptonote_protocol
[ 95%] Linking CXX static library libcryptonote_protocol.a
[ 95%] Built target cryptonote_protocol
Scanning dependencies of target serialization
[ 95%] Linking CXX static library libserialization.a
[ 95%] Built target serialization
Scanning dependencies of target daemon_messages
[ 96%] Linking CXX static library libdaemon_messages.a
[ 96%] Built target daemon_messages
[ 96%] Built target obj_daemon_rpc_server
[ 96%] Built target obj_rpc
Scanning dependencies of target rpc
[ 96%] Linking CXX static library librpc.a
[ 96%] Built target rpc
Scanning dependencies of target daemon_rpc_server
[ 96%] Linking CXX static library libdaemon_rpc_server.a
[ 96%] Built target daemon_rpc_server
[ 97%] Generating blocksdat.o
Scanning dependencies of target daemon
[ 97%] Building CXX object src/daemon/CMakeFiles/daemon.dir/command_server.cpp.o
[ 97%] Building CXX object src/daemon/CMakeFiles/daemon.dir/command_parser_executor.cpp.o
[ 98%] Building CXX object src/daemon/CMakeFiles/daemon.dir/daemon.cpp.o
[ 98%] Building CXX object src/daemon/CMakeFiles/daemon.dir/main.cpp.o
[ 98%] Building CXX object src/daemon/CMakeFiles/daemon.dir/executor.cpp.o
[100%] Building CXX object src/daemon/CMakeFiles/daemon.dir/rpc_command_executor.cpp.o
[100%] Linking CXX executable ../../bin/monerod
/usr/bin/ld: /usr/lib/gcc/x86_64-redhat-linux/8/../../../../lib64/libcrypto.a(c_zlib.o): undefined reference to symbol 'inflateEnd'
//usr/lib64/libz.so.1: error adding symbols: DSO missing from command line
collect2: error: ld returned 1 exit status
make[2]: *** [src/daemon/CMakeFiles/daemon.dir/build.make:222: bin/monerod] Error 1
make[1]: *** [CMakeFiles/Makefile2:3069: src/daemon/CMakeFiles/daemon.dir/all] Error 2
make: *** [Makefile:141: all] Error 2
[  1%] Built target easylogging
[  6%] Built target blocks
[  6%] Built target obj_device
[ 12%] Built target obj_cncrypto
[ 16%] Built target generate_translations_header
[ 18%] Built target obj_ringct_basic
[ 25%] Built target libminiupnpc-static
[ 26%] Built target lmdb
[ 26%] Built target genversion
[ 26%] Built target obj_ringct
[ 27%] Built target obj_checkpoints
[ 63%] Built target unbound
[ 65%] Built target obj_blockchain_db
[ 68%] Built target obj_multisig
[ 68%] Built target obj_cryptonote_core
[ 68%] Built target obj_daemon_rpc_server
[ 70%] Built target obj_cryptonote_basic
[ 72%] Built target obj_rpc
[ 72%] Built target obj_p2p
[ 72%] Built target obj_rpc_base
[ 73%] Built target obj_cryptonote_protocol
[ 74%] Built target obj_daemon_messages
[ 74%] Built target obj_serialization
[ 79%] Built target epee
[ 83%] Built target obj_common
[ 84%] Built target epee_readline
[ 86%] Built target obj_daemonizer
[ 87%] Built target obj_version
[ 88%] Built target cncrypto
[ 89%] Built target version
[ 89%] Built target common
[ 90%] Built target rpc_base
[ 91%] Built target ringct_basic
[ 91%] Built target checkpoints
[ 91%] Built target daemonizer
[ 93%] Built target device
[ 93%] Built target cryptonote_basic
[ 93%] Built target ringct
[ 94%] Built target blockchain_db
[ 94%] Built target multisig
[ 95%] Built target cryptonote_core
[ 95%] Built target p2p
[ 95%] Built target cryptonote_protocol
[ 95%] Built target rpc
[ 95%] Built target serialization
[ 96%] Built target daemon_messages
[ 96%] Built target daemon_rpc_server
[ 96%] Linking CXX executable ../../bin/monerod
/usr/bin/ld: /usr/lib/gcc/x86_64-redhat-linux/8/../../../../lib64/libcrypto.a(c_zlib.o): undefined reference to symbol 'inflateEnd'
//usr/lib64/libz.so.1: error adding symbols: DSO missing from command line
collect2: error: ld returned 1 exit status
make[2]: *** [src/daemon/CMakeFiles/daemon.dir/build.make:222: bin/monerod] Error 1
make[1]: *** [CMakeFiles/Makefile2:3069: src/daemon/CMakeFiles/daemon.dir/all] Error 2
make: *** [Makefile:141: all] Error 2
~/monero-gui/monero/build/release-static ~/monero-gui ~/monero-gui
make: Entering directory '/home/liao/monero-gui/monero/build/release-static/contrib/epee'
make[1]: Entering directory '/home/liao/monero-gui/monero/build/release-static'
make[2]: Entering directory '/home/liao/monero-gui/monero/build/release-static'
make[2]: Leaving directory '/home/liao/monero-gui/monero/build/release-static'
[ 16%] Built target easylogging
make[2]: Entering directory '/home/liao/monero-gui/monero/build/release-static'
make[2]: Leaving directory '/home/liao/monero-gui/monero/build/release-static'
[ 83%] Built target epee
make[2]: Entering directory '/home/liao/monero-gui/monero/build/release-static'
make[2]: Leaving directory '/home/liao/monero-gui/monero/build/release-static'
[100%] Built target epee_readline
make[1]: Leaving directory '/home/liao/monero-gui/monero/build/release-static'
Install the project...
-- Install configuration: "Release"
-- Installing: /home/liao/monero-gui/monero/lib/libepee.a
-- Installing: /home/liao/monero-gui/monero/lib/libepee_readline.a
make: Leaving directory '/home/liao/monero-gui/monero/build/release-static/contrib/epee'
make: Entering directory '/home/liao/monero-gui/monero/build/release-static/external/easylogging++'
make[1]: Entering directory '/home/liao/monero-gui/monero/build/release-static'
make[2]: Entering directory '/home/liao/monero-gui/monero/build/release-static'
make[2]: Leaving directory '/home/liao/monero-gui/monero/build/release-static'
[100%] Built target easylogging
make[1]: Leaving directory '/home/liao/monero-gui/monero/build/release-static'
Install the project...
-- Install configuration: "Release"
-- Installing: /home/liao/monero-gui/monero/lib/libeasylogging.a
make: Leaving directory '/home/liao/monero-gui/monero/build/release-static/external/easylogging++'
make: Entering directory '/home/liao/monero-gui/monero/build/release-static/external/db_drivers/liblmdb'
make[1]: Entering directory '/home/liao/monero-gui/monero/build/release-static'
make[2]: Entering directory '/home/liao/monero-gui/monero/build/release-static'
make[2]: Leaving directory '/home/liao/monero-gui/monero/build/release-static'
[100%] Built target lmdb
make[1]: Leaving directory '/home/liao/monero-gui/monero/build/release-static'
Install the project...
-- Install configuration: "Release"
-- Installing: /home/liao/monero-gui/monero/lib/liblmdb.a
make: Leaving directory '/home/liao/monero-gui/monero/build/release-static/external/db_drivers/liblmdb'
Installing libunbound...
~/monero-gui/monero/build/release-static/external/unbound ~/monero-gui/monero/build/release-static ~/monero-gui ~/monero-gui
[100%] Built target unbound
Install the project...
-- Install configuration: "Release"
-- Installing: /home/liao/monero-gui/monero/lib/libunbound.a
~/monero-gui/monero/build/release-static ~/monero-gui ~/monero-gui
~/monero-gui ~/monero-gui
make: Entering directory '/home/liao/monero-gui/src/zxcvbn-c'
make: Nothing to be done for 'all'.
make: Leaving directory '/home/liao/monero-gui/src/zxcvbn-c'
You are currently on commit 3fd37b9
The most recent tag was at 6206e3d
You are ahead of or behind a tagged release
~/monero-gui/monero ~/monero-gui ~/monero-gui
You are currently on commit c6ce8235
The most recent tag was at 558da368
You are ahead of or behind a tagged release
~/monero-gui ~/monero-gui
Project MESSAGE: using static libraries
Project MESSAGE: Building without libunwind
Updating '/home/liao/monero-gui/build/translations/monero-core_ar.qm'...
Removing translations equal to source text in '/home/liao/monero-gui/build/translations/monero-core_ar.qm'...
    Generated 257 translation(s) (257 finished and 0 unfinished)
    Ignored 215 untranslated source text(s)
Updating '/home/liao/monero-gui/build/translations/monero-core_cat.qm'...
Removing translations equal to source text in '/home/liao/monero-gui/build/translations/monero-core_cat.qm'...
    Generated 241 translation(s) (241 finished and 0 unfinished)
    Ignored 174 untranslated source text(s)
Updating '/home/liao/monero-gui/build/translations/monero-core_cs.qm'...
Removing translations equal to source text in '/home/liao/monero-gui/build/translations/monero-core_cs.qm'...
    Generated 468 translation(s) (468 finished and 0 unfinished)
    Ignored 11 untranslated source text(s)
Updating '/home/liao/monero-gui/build/translations/monero-core_da.qm'...
Removing translations equal to source text in '/home/liao/monero-gui/build/translations/monero-core_da.qm'...
    Generated 435 translation(s) (435 finished and 0 unfinished)
    Ignored 13 untranslated source text(s)
Updating '/home/liao/monero-gui/build/translations/monero-core_de.qm'...
Removing translations equal to source text in '/home/liao/monero-gui/build/translations/monero-core_de.qm'...
    Generated 473 translation(s) (473 finished and 0 unfinished)
Updating '/home/liao/monero-gui/build/translations/monero-core_eo.qm'...
Removing translations equal to source text in '/home/liao/monero-gui/build/translations/monero-core_eo.qm'...
    Generated 454 translation(s) (454 finished and 0 unfinished)
    Ignored 33 untranslated source text(s)
Updating '/home/liao/monero-gui/build/translations/monero-core_es.qm'...
Removing translations equal to source text in '/home/liao/monero-gui/build/translations/monero-core_es.qm'...
    Generated 474 translation(s) (474 finished and 0 unfinished)
Updating '/home/liao/monero-gui/build/translations/monero-core_fi.qm'...
Removing translations equal to source text in '/home/liao/monero-gui/build/translations/monero-core_fi.qm'...
    Generated 469 translation(s) (469 finished and 0 unfinished)
    Ignored 28 untranslated source text(s)
Updating '/home/liao/monero-gui/build/translations/monero-core_fr.qm'...
Removing translations equal to source text in '/home/liao/monero-gui/build/translations/monero-core_fr.qm'...
    Generated 448 translation(s) (448 finished and 0 unfinished)
    Ignored 11 untranslated source text(s)
Updating '/home/liao/monero-gui/build/translations/monero-core_he.qm'...
Removing translations equal to source text in '/home/liao/monero-gui/build/translations/monero-core_he.qm'...
    Generated 459 translation(s) (459 finished and 0 unfinished)
    Ignored 33 untranslated source text(s)
Updating '/home/liao/monero-gui/build/translations/monero-core_hi.qm'...
Removing translations equal to source text in '/home/liao/monero-gui/build/translations/monero-core_hi.qm'...
    Generated 49 translation(s) (49 finished and 0 unfinished)
    Ignored 432 untranslated source text(s)
Updating '/home/liao/monero-gui/build/translations/monero-core_hr.qm'...
Removing translations equal to source text in '/home/liao/monero-gui/build/translations/monero-core_hr.qm'...
    Generated 472 translation(s) (472 finished and 0 unfinished)
    Ignored 13 untranslated source text(s)
Updating '/home/liao/monero-gui/build/translations/monero-core_hu.qm'...
Removing translations equal to source text in '/home/liao/monero-gui/build/translations/monero-core_hu.qm'...
    Generated 476 translation(s) (476 finished and 0 unfinished)
    Ignored 2 untranslated source text(s)
Updating '/home/liao/monero-gui/build/translations/monero-core_id.qm'...
Removing translations equal to source text in '/home/liao/monero-gui/build/translations/monero-core_id.qm'...
    Generated 257 translation(s) (257 finished and 0 unfinished)
    Ignored 202 untranslated source text(s)
Updating '/home/liao/monero-gui/build/translations/monero-core_it.qm'...
Removing translations equal to source text in '/home/liao/monero-gui/build/translations/monero-core_it.qm'...
    Generated 460 translation(s) (460 finished and 0 unfinished)
    Ignored 11 untranslated source text(s)
Updating '/home/liao/monero-gui/build/translations/monero-core_ja.qm'...
Removing translations equal to source text in '/home/liao/monero-gui/build/translations/monero-core_ja.qm'...
    Generated 474 translation(s) (474 finished and 0 unfinished)
    Ignored 11 untranslated source text(s)
Updating '/home/liao/monero-gui/build/translations/monero-core_ko.qm'...
Removing translations equal to source text in '/home/liao/monero-gui/build/translations/monero-core_ko.qm'...
    Generated 275 translation(s) (275 finished and 0 unfinished)
    Ignored 178 untranslated source text(s)
Updating '/home/liao/monero-gui/build/translations/monero-core_lt.qm'...
Removing translations equal to source text in '/home/liao/monero-gui/build/translations/monero-core_lt.qm'...
    Generated 461 translation(s) (461 finished and 0 unfinished)
    Ignored 39 untranslated source text(s)
Updating '/home/liao/monero-gui/build/translations/monero-core_nl.qm'...
Removing translations equal to source text in '/home/liao/monero-gui/build/translations/monero-core_nl.qm'...
    Generated 472 translation(s) (472 finished and 0 unfinished)
    Ignored 11 untranslated source text(s)
Updating '/home/liao/monero-gui/build/translations/monero-core_pl.qm'...
Removing translations equal to source text in '/home/liao/monero-gui/build/translations/monero-core_pl.qm'...
    Generated 470 translation(s) (470 finished and 0 unfinished)
    Ignored 11 untranslated source text(s)
Updating '/home/liao/monero-gui/build/translations/monero-core_pt-br.qm'...
Removing translations equal to source text in '/home/liao/monero-gui/build/translations/monero-core_pt-br.qm'...
    Generated 466 translation(s) (466 finished and 0 unfinished)
    Ignored 11 untranslated source text(s)
Updating '/home/liao/monero-gui/build/translations/monero-core_pt-pt.qm'...
Removing translations equal to source text in '/home/liao/monero-gui/build/translations/monero-core_pt-pt.qm'...
    Generated 458 translation(s) (458 finished and 0 unfinished)
    Ignored 11 untranslated source text(s)
Updating '/home/liao/monero-gui/build/translations/monero-core_ro.qm'...
Removing translations equal to source text in '/home/liao/monero-gui/build/translations/monero-core_ro.qm'...
    Generated 460 translation(s) (460 finished and 0 unfinished)
    Ignored 13 untranslated source text(s)
Updating '/home/liao/monero-gui/build/translations/monero-core_ru.qm'...
Removing translations equal to source text in '/home/liao/monero-gui/build/translations/monero-core_ru.qm'...
    Generated 473 translation(s) (473 finished and 0 unfinished)
    Ignored 23 untranslated source text(s)
Updating '/home/liao/monero-gui/build/translations/monero-core_sk.qm'...
Removing translations equal to source text in '/home/liao/monero-gui/build/translations/monero-core_sk.qm'...
    Generated 434 translation(s) (434 finished and 0 unfinished)
    Ignored 41 untranslated source text(s)
Updating '/home/liao/monero-gui/build/translations/monero-core_sl.qm'...
Removing translations equal to source text in '/home/liao/monero-gui/build/translations/monero-core_sl.qm'...
    Generated 318 translation(s) (318 finished and 0 unfinished)
    Ignored 139 untranslated source text(s)
Updating '/home/liao/monero-gui/build/translations/monero-core_sr.qm'...
Removing translations equal to source text in '/home/liao/monero-gui/build/translations/monero-core_sr.qm'...
    Generated 456 translation(s) (456 finished and 0 unfinished)
    Ignored 11 untranslated source text(s)
Updating '/home/liao/monero-gui/build/translations/monero-core_sv.qm'...
Removing translations equal to source text in '/home/liao/monero-gui/build/translations/monero-core_sv.qm'...
    Generated 462 translation(s) (462 finished and 0 unfinished)
    Ignored 11 untranslated source text(s)
Updating '/home/liao/monero-gui/build/translations/monero-core_tr.qm'...
Removing translations equal to source text in '/home/liao/monero-gui/build/translations/monero-core_tr.qm'...
    Generated 466 translation(s) (466 finished and 0 unfinished)
    Ignored 11 untranslated source text(s)
Updating '/home/liao/monero-gui/build/translations/monero-core_uk.qm'...
Removing translations equal to source text in '/home/liao/monero-gui/build/translations/monero-core_uk.qm'...
    Generated 474 translation(s) (474 finished and 0 unfinished)
    Ignored 24 untranslated source text(s)
Updating '/home/liao/monero-gui/build/translations/monero-core_zh-cn.qm'...
Removing translations equal to source text in '/home/liao/monero-gui/build/translations/monero-core_zh-cn.qm'...
    Generated 468 translation(s) (468 finished and 0 unfinished)
    Ignored 14 untranslated source text(s)
Updating '/home/liao/monero-gui/build/translations/monero-core_zh-tw.qm'...
Removing translations equal to source text in '/home/liao/monero-gui/build/translations/monero-core_zh-tw.qm'...
    Generated 490 translation(s) (490 finished and 0 unfinished)
/usr/lib64/qt5/bin/lrelease -compress -nounfinished -removeidentical ../translations/monero-core_ar.ts -qm /home/liao/monero-gui/build/translations/monero-core_ar.qm
Updating '/home/liao/monero-gui/build/translations/monero-core_ar.qm'...
Removing translations equal to source text in '/home/liao/monero-gui/build/translations/monero-core_ar.qm'...
    Generated 257 translation(s) (257 finished and 0 unfinished)
    Ignored 215 untranslated source text(s)
/usr/lib64/qt5/bin/lrelease -compress -nounfinished -removeidentical ../translations/monero-core_cat.ts -qm /home/liao/monero-gui/build/translations/monero-core_cat.qm
Updating '/home/liao/monero-gui/build/translations/monero-core_cat.qm'...
Removing translations equal to source text in '/home/liao/monero-gui/build/translations/monero-core_cat.qm'...
    Generated 241 translation(s) (241 finished and 0 unfinished)
    Ignored 174 untranslated source text(s)
/usr/lib64/qt5/bin/lrelease -compress -nounfinished -removeidentical ../translations/monero-core_cs.ts -qm /home/liao/monero-gui/build/translations/monero-core_cs.qm
Updating '/home/liao/monero-gui/build/translations/monero-core_cs.qm'...
Removing translations equal to source text in '/home/liao/monero-gui/build/translations/monero-core_cs.qm'...
    Generated 468 translation(s) (468 finished and 0 unfinished)
    Ignored 11 untranslated source text(s)
/usr/lib64/qt5/bin/lrelease -compress -nounfinished -removeidentical ../translations/monero-core_da.ts -qm /home/liao/monero-gui/build/translations/monero-core_da.qm
Updating '/home/liao/monero-gui/build/translations/monero-core_da.qm'...
Removing translations equal to source text in '/home/liao/monero-gui/build/translations/monero-core_da.qm'...
    Generated 435 translation(s) (435 finished and 0 unfinished)
    Ignored 13 untranslated source text(s)
/usr/lib64/qt5/bin/lrelease -compress -nounfinished -removeidentical ../translations/monero-core_de.ts -qm /home/liao/monero-gui/build/translations/monero-core_de.qm
Updating '/home/liao/monero-gui/build/translations/monero-core_de.qm'...
Removing translations equal to source text in '/home/liao/monero-gui/build/translations/monero-core_de.qm'...
    Generated 473 translation(s) (473 finished and 0 unfinished)
/usr/lib64/qt5/bin/lrelease -compress -nounfinished -removeidentical ../translations/monero-core_eo.ts -qm /home/liao/monero-gui/build/translations/monero-core_eo.qm
Updating '/home/liao/monero-gui/build/translations/monero-core_eo.qm'...
Removing translations equal to source text in '/home/liao/monero-gui/build/translations/monero-core_eo.qm'...
    Generated 454 translation(s) (454 finished and 0 unfinished)
    Ignored 33 untranslated source text(s)
/usr/lib64/qt5/bin/lrelease -compress -nounfinished -removeidentical ../translations/monero-core_es.ts -qm /home/liao/monero-gui/build/translations/monero-core_es.qm
Updating '/home/liao/monero-gui/build/translations/monero-core_es.qm'...
Removing translations equal to source text in '/home/liao/monero-gui/build/translations/monero-core_es.qm'...
    Generated 474 translation(s) (474 finished and 0 unfinished)
/usr/lib64/qt5/bin/lrelease -compress -nounfinished -removeidentical ../translations/monero-core_fi.ts -qm /home/liao/monero-gui/build/translations/monero-core_fi.qm
Updating '/home/liao/monero-gui/build/translations/monero-core_fi.qm'...
Removing translations equal to source text in '/home/liao/monero-gui/build/translations/monero-core_fi.qm'...
    Generated 469 translation(s) (469 finished and 0 unfinished)
    Ignored 28 untranslated source text(s)
/usr/lib64/qt5/bin/lrelease -compress -nounfinished -removeidentical ../translations/monero-core_fr.ts -qm /home/liao/monero-gui/build/translations/monero-core_fr.qm
Updating '/home/liao/monero-gui/build/translations/monero-core_fr.qm'...
Removing translations equal to source text in '/home/liao/monero-gui/build/translations/monero-core_fr.qm'...
    Generated 448 translation(s) (448 finished and 0 unfinished)
    Ignored 11 untranslated source text(s)
/usr/lib64/qt5/bin/lrelease -compress -nounfinished -removeidentical ../translations/monero-core_he.ts -qm /home/liao/monero-gui/build/translations/monero-core_he.qm
Updating '/home/liao/monero-gui/build/translations/monero-core_he.qm'...
Removing translations equal to source text in '/home/liao/monero-gui/build/translations/monero-core_he.qm'...
    Generated 459 translation(s) (459 finished and 0 unfinished)
    Ignored 33 untranslated source text(s)
/usr/lib64/qt5/bin/lrelease -compress -nounfinished -removeidentical ../translations/monero-core_hi.ts -qm /home/liao/monero-gui/build/translations/monero-core_hi.qm
Updating '/home/liao/monero-gui/build/translations/monero-core_hi.qm'...
Removing translations equal to source text in '/home/liao/monero-gui/build/translations/monero-core_hi.qm'...
    Generated 49 translation(s) (49 finished and 0 unfinished)
    Ignored 432 untranslated source text(s)
/usr/lib64/qt5/bin/lrelease -compress -nounfinished -removeidentical ../translations/monero-core_hr.ts -qm /home/liao/monero-gui/build/translations/monero-core_hr.qm
Updating '/home/liao/monero-gui/build/translations/monero-core_hr.qm'...
Removing translations equal to source text in '/home/liao/monero-gui/build/translations/monero-core_hr.qm'...
    Generated 472 translation(s) (472 finished and 0 unfinished)
    Ignored 13 untranslated source text(s)
/usr/lib64/qt5/bin/lrelease -compress -nounfinished -removeidentical ../translations/monero-core_hu.ts -qm /home/liao/monero-gui/build/translations/monero-core_hu.qm
Updating '/home/liao/monero-gui/build/translations/monero-core_hu.qm'...
Removing translations equal to source text in '/home/liao/monero-gui/build/translations/monero-core_hu.qm'...
    Generated 476 translation(s) (476 finished and 0 unfinished)
    Ignored 2 untranslated source text(s)
/usr/lib64/qt5/bin/lrelease -compress -nounfinished -removeidentical ../translations/monero-core_id.ts -qm /home/liao/monero-gui/build/translations/monero-core_id.qm
Updating '/home/liao/monero-gui/build/translations/monero-core_id.qm'...
Removing translations equal to source text in '/home/liao/monero-gui/build/translations/monero-core_id.qm'...
    Generated 257 translation(s) (257 finished and 0 unfinished)
    Ignored 202 untranslated source text(s)
/usr/lib64/qt5/bin/lrelease -compress -nounfinished -removeidentical ../translations/monero-core_it.ts -qm /home/liao/monero-gui/build/translations/monero-core_it.qm
Updating '/home/liao/monero-gui/build/translations/monero-core_it.qm'...
Removing translations equal to source text in '/home/liao/monero-gui/build/translations/monero-core_it.qm'...
    Generated 460 translation(s) (460 finished and 0 unfinished)
    Ignored 11 untranslated source text(s)
/usr/lib64/qt5/bin/lrelease -compress -nounfinished -removeidentical ../translations/monero-core_ja.ts -qm /home/liao/monero-gui/build/translations/monero-core_ja.qm
Updating '/home/liao/monero-gui/build/translations/monero-core_ja.qm'...
Removing translations equal to source text in '/home/liao/monero-gui/build/translations/monero-core_ja.qm'...
    Generated 474 translation(s) (474 finished and 0 unfinished)
    Ignored 11 untranslated source text(s)
/usr/lib64/qt5/bin/lrelease -compress -nounfinished -removeidentical ../translations/monero-core_ko.ts -qm /home/liao/monero-gui/build/translations/monero-core_ko.qm
Updating '/home/liao/monero-gui/build/translations/monero-core_ko.qm'...
Removing translations equal to source text in '/home/liao/monero-gui/build/translations/monero-core_ko.qm'...
    Generated 275 translation(s) (275 finished and 0 unfinished)
    Ignored 178 untranslated source text(s)
/usr/lib64/qt5/bin/lrelease -compress -nounfinished -removeidentical ../translations/monero-core_lt.ts -qm /home/liao/monero-gui/build/translations/monero-core_lt.qm
Updating '/home/liao/monero-gui/build/translations/monero-core_lt.qm'...
Removing translations equal to source text in '/home/liao/monero-gui/build/translations/monero-core_lt.qm'...
    Generated 461 translation(s) (461 finished and 0 unfinished)
    Ignored 39 untranslated source text(s)
/usr/lib64/qt5/bin/lrelease -compress -nounfinished -removeidentical ../translations/monero-core_nl.ts -qm /home/liao/monero-gui/build/translations/monero-core_nl.qm
Updating '/home/liao/monero-gui/build/translations/monero-core_nl.qm'...
Removing translations equal to source text in '/home/liao/monero-gui/build/translations/monero-core_nl.qm'...
    Generated 472 translation(s) (472 finished and 0 unfinished)
    Ignored 11 untranslated source text(s)
/usr/lib64/qt5/bin/lrelease -compress -nounfinished -removeidentical ../translations/monero-core_pl.ts -qm /home/liao/monero-gui/build/translations/monero-core_pl.qm
Updating '/home/liao/monero-gui/build/translations/monero-core_pl.qm'...
Removing translations equal to source text in '/home/liao/monero-gui/build/translations/monero-core_pl.qm'...
    Generated 470 translation(s) (470 finished and 0 unfinished)
    Ignored 11 untranslated source text(s)
/usr/lib64/qt5/bin/lrelease -compress -nounfinished -removeidentical ../translations/monero-core_pt-br.ts -qm /home/liao/monero-gui/build/translations/monero-core_pt-br.qm
Updating '/home/liao/monero-gui/build/translations/monero-core_pt-br.qm'...
Removing translations equal to source text in '/home/liao/monero-gui/build/translations/monero-core_pt-br.qm'...
    Generated 466 translation(s) (466 finished and 0 unfinished)
    Ignored 11 untranslated source text(s)
/usr/lib64/qt5/bin/lrelease -compress -nounfinished -removeidentical ../translations/monero-core_pt-pt.ts -qm /home/liao/monero-gui/build/translations/monero-core_pt-pt.qm
Updating '/home/liao/monero-gui/build/translations/monero-core_pt-pt.qm'...
Removing translations equal to source text in '/home/liao/monero-gui/build/translations/monero-core_pt-pt.qm'...
    Generated 458 translation(s) (458 finished and 0 unfinished)
    Ignored 11 untranslated source text(s)
/usr/lib64/qt5/bin/lrelease -compress -nounfinished -removeidentical ../translations/monero-core_ro.ts -qm /home/liao/monero-gui/build/translations/monero-core_ro.qm
Updating '/home/liao/monero-gui/build/translations/monero-core_ro.qm'...
Removing translations equal to source text in '/home/liao/monero-gui/build/translations/monero-core_ro.qm'...
    Generated 460 translation(s) (460 finished and 0 unfinished)
    Ignored 13 untranslated source text(s)
/usr/lib64/qt5/bin/lrelease -compress -nounfinished -removeidentical ../translations/monero-core_ru.ts -qm /home/liao/monero-gui/build/translations/monero-core_ru.qm
Updating '/home/liao/monero-gui/build/translations/monero-core_ru.qm'...
Removing translations equal to source text in '/home/liao/monero-gui/build/translations/monero-core_ru.qm'...
    Generated 473 translation(s) (473 finished and 0 unfinished)
    Ignored 23 untranslated source text(s)
/usr/lib64/qt5/bin/lrelease -compress -nounfinished -removeidentical ../translations/monero-core_sk.ts -qm /home/liao/monero-gui/build/translations/monero-core_sk.qm
Updating '/home/liao/monero-gui/build/translations/monero-core_sk.qm'...
Removing translations equal to source text in '/home/liao/monero-gui/build/translations/monero-core_sk.qm'...
    Generated 434 translation(s) (434 finished and 0 unfinished)
    Ignored 41 untranslated source text(s)
/usr/lib64/qt5/bin/lrelease -compress -nounfinished -removeidentical ../translations/monero-core_sl.ts -qm /home/liao/monero-gui/build/translations/monero-core_sl.qm
Updating '/home/liao/monero-gui/build/translations/monero-core_sl.qm'...
Removing translations equal to source text in '/home/liao/monero-gui/build/translations/monero-core_sl.qm'...
    Generated 318 translation(s) (318 finished and 0 unfinished)
    Ignored 139 untranslated source text(s)
/usr/lib64/qt5/bin/lrelease -compress -nounfinished -removeidentical ../translations/monero-core_sr.ts -qm /home/liao/monero-gui/build/translations/monero-core_sr.qm
Updating '/home/liao/monero-gui/build/translations/monero-core_sr.qm'...
Removing translations equal to source text in '/home/liao/monero-gui/build/translations/monero-core_sr.qm'...
    Generated 456 translation(s) (456 finished and 0 unfinished)
    Ignored 11 untranslated source text(s)
/usr/lib64/qt5/bin/lrelease -compress -nounfinished -removeidentical ../translations/monero-core_sv.ts -qm /home/liao/monero-gui/build/translations/monero-core_sv.qm
Updating '/home/liao/monero-gui/build/translations/monero-core_sv.qm'...
Removing translations equal to source text in '/home/liao/monero-gui/build/translations/monero-core_sv.qm'...
    Generated 462 translation(s) (462 finished and 0 unfinished)
    Ignored 11 untranslated source text(s)
/usr/lib64/qt5/bin/lrelease -compress -nounfinished -removeidentical ../translations/monero-core_tr.ts -qm /home/liao/monero-gui/build/translations/monero-core_tr.qm
Updating '/home/liao/monero-gui/build/translations/monero-core_tr.qm'...
Removing translations equal to source text in '/home/liao/monero-gui/build/translations/monero-core_tr.qm'...
    Generated 466 translation(s) (466 finished and 0 unfinished)
    Ignored 11 untranslated source text(s)
/usr/lib64/qt5/bin/lrelease -compress -nounfinished -removeidentical ../translations/monero-core_uk.ts -qm /home/liao/monero-gui/build/translations/monero-core_uk.qm
Updating '/home/liao/monero-gui/build/translations/monero-core_uk.qm'...
Removing translations equal to source text in '/home/liao/monero-gui/build/translations/monero-core_uk.qm'...
    Generated 474 translation(s) (474 finished and 0 unfinished)
    Ignored 24 untranslated source text(s)
/usr/lib64/qt5/bin/lrelease -compress -nounfinished -removeidentical ../translations/monero-core_zh-cn.ts -qm /home/liao/monero-gui/build/translations/monero-core_zh-cn.qm
Updating '/home/liao/monero-gui/build/translations/monero-core_zh-cn.qm'...
Removing translations equal to source text in '/home/liao/monero-gui/build/translations/monero-core_zh-cn.qm'...
    Generated 468 translation(s) (468 finished and 0 unfinished)
    Ignored 14 untranslated source text(s)
/usr/lib64/qt5/bin/lrelease -compress -nounfinished -removeidentical ../translations/monero-core_zh-tw.ts -qm /home/liao/monero-gui/build/translations/monero-core_zh-tw.qm
Updating '/home/liao/monero-gui/build/translations/monero-core_zh-tw.qm'...
Removing translations equal to source text in '/home/liao/monero-gui/build/translations/monero-core_zh-tw.qm'...
    Generated 490 translation(s) (490 finished and 0 unfinished)
g++ -c -pipe -fPIC -fstack-protector -fstack-protector-strong -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=1 -Wformat -Wformat-security -O2 -std=gnu++11 -Wall -W -D_REENTRANT -fPIC -DQT_NO_DEBUG -DQT_QUICK_LIB -DQT_WIDGETS_LIB -DQT_GUI_LIB -DQT_QML_LIB -DQT_NETWORK_LIB -DQT_CORE_LIB -I../../monero-gui -I. -I/home/liao/monero-gui/monero/include -I../src/libwalletqt -I../src/QR-Code-generator -I../src -I../monero/src -isystem /usr/include/qt5 -isystem /usr/include/qt5/QtQuick -isystem /usr/include/qt5/QtWidgets -isystem /usr/include/qt5/QtGui -isystem /usr/include/qt5/QtQml -isystem /usr/include/qt5/QtNetwork -isystem /usr/include/qt5/QtCore -I. -isystem /usr/include/libdrm -I/usr/lib64/qt5/mkspecs/linux-g++ -o main.o ../main.cpp
g++ -c -pipe -fPIC -fstack-protector -fstack-protector-strong -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=1 -Wformat -Wformat-security -O2 -std=gnu++11 -Wall -W -D_REENTRANT -fPIC -DQT_NO_DEBUG -DQT_QUICK_LIB -DQT_WIDGETS_LIB -DQT_GUI_LIB -DQT_QML_LIB -DQT_NETWORK_LIB -DQT_CORE_LIB -I../../monero-gui -I. -I/home/liao/monero-gui/monero/include -I../src/libwalletqt -I../src/QR-Code-generator -I../src -I../monero/src -isystem /usr/include/qt5 -isystem /usr/include/qt5/QtQuick -isystem /usr/include/qt5/QtWidgets -isystem /usr/include/qt5/QtGui -isystem /usr/include/qt5/QtQml -isystem /usr/include/qt5/QtNetwork -isystem /usr/include/qt5/QtCore -I. -isystem /usr/include/libdrm -I/usr/lib64/qt5/mkspecs/linux-g++ -o WalletManager.o ../src/libwalletqt/WalletManager.cpp
../src/libwalletqt/WalletManager.cpp: In member function 'bool WalletManager::moveWallet(const QString&, const QString&)':
../src/libwalletqt/WalletManager.cpp:170:47: warning: unused parameter 'src' [-Wunused-parameter]
 bool WalletManager::moveWallet(const QString &src, const QString &dst)
                                ~~~~~~~~~~~~~~~^~~
../src/libwalletqt/WalletManager.cpp:170:67: warning: unused parameter 'dst' [-Wunused-parameter]
 bool WalletManager::moveWallet(const QString &src, const QString &dst)
                                                    ~~~~~~~~~~~~~~~^~~
../src/libwalletqt/WalletManager.cpp: In member function 'QString WalletManager::walletLanguage(const QString&)':
../src/libwalletqt/WalletManager.cpp:176:54: warning: unused parameter 'locale' [-Wunused-parameter]
 QString WalletManager::walletLanguage(const QString &locale)
                                       ~~~~~~~~~~~~~~~^~~~~~
g++ -c -pipe -fPIC -fstack-protector -fstack-protector-strong -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=1 -Wformat -Wformat-security -O2 -std=gnu++11 -Wall -W -D_REENTRANT -fPIC -DQT_NO_DEBUG -DQT_QUICK_LIB -DQT_WIDGETS_LIB -DQT_GUI_LIB -DQT_QML_LIB -DQT_NETWORK_LIB -DQT_CORE_LIB -I../../monero-gui -I. -I/home/liao/monero-gui/monero/include -I../src/libwalletqt -I../src/QR-Code-generator -I../src -I../monero/src -isystem /usr/include/qt5 -isystem /usr/include/qt5/QtQuick -isystem /usr/include/qt5/QtWidgets -isystem /usr/include/qt5/QtGui -isystem /usr/include/qt5/QtQml -isystem /usr/include/qt5/QtNetwork -isystem /usr/include/qt5/QtCore -I. -isystem /usr/include/libdrm -I/usr/lib64/qt5/mkspecs/linux-g++ -o Wallet.o ../src/libwalletqt/Wallet.cpp
In file included from ../src/libwalletqt/Wallet.cpp:1:
../src/libwalletqt/Wallet.h: In constructor 'Wallet::Wallet(Monero::Wallet*, QObject*)':
../src/libwalletqt/Wallet.h:350:31: warning: 'Wallet::m_subaddressModel' will be initialized after [-Wreorder]
     mutable SubaddressModel * m_subaddressModel;
                               ^~~~~~~~~~~~~~~~~
../src/libwalletqt/Wallet.h:337:21: warning:   'quint64 Wallet::m_daemonBlockChainHeight' [-Wreorder]
     mutable quint64 m_daemonBlockChainHeight;
                     ^~~~~~~~~~~~~~~~~~~~~~~~
../src/libwalletqt/Wallet.cpp:852:1: warning:   when initialized here [-Wreorder]
 Wallet::Wallet(Monero::Wallet *w, QObject *parent)
 ^~~~~~
g++ -c -pipe -fPIC -fstack-protector -fstack-protector-strong -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=1 -Wformat -Wformat-security -O2 -std=gnu++11 -Wall -W -D_REENTRANT -fPIC -DQT_NO_DEBUG -DQT_QUICK_LIB -DQT_WIDGETS_LIB -DQT_GUI_LIB -DQT_QML_LIB -DQT_NETWORK_LIB -DQT_CORE_LIB -I../../monero-gui -I. -I/home/liao/monero-gui/monero/include -I../src/libwalletqt -I../src/QR-Code-generator -I../src -I../monero/src -isystem /usr/include/qt5 -isystem /usr/include/qt5/QtQuick -isystem /usr/include/qt5/QtWidgets -isystem /usr/include/qt5/QtGui -isystem /usr/include/qt5/QtQml -isystem /usr/include/qt5/QtNetwork -isystem /usr/include/qt5/QtCore -I. -isystem /usr/include/libdrm -I/usr/lib64/qt5/mkspecs/linux-g++ -o TransactionInfo.o ../src/libwalletqt/TransactionInfo.cpp
g++ -c -pipe -fPIC -fstack-protector -fstack-protector-strong -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=1 -Wformat -Wformat-security -O2 -std=gnu++11 -Wall -W -D_REENTRANT -fPIC -DQT_NO_DEBUG -DQT_QUICK_LIB -DQT_WIDGETS_LIB -DQT_GUI_LIB -DQT_QML_LIB -DQT_NETWORK_LIB -DQT_CORE_LIB -I../../monero-gui -I. -I/home/liao/monero-gui/monero/include -I../src/libwalletqt -I../src/QR-Code-generator -I../src -I../monero/src -isystem /usr/include/qt5 -isystem /usr/include/qt5/QtQuick -isystem /usr/include/qt5/QtWidgets -isystem /usr/include/qt5/QtGui -isystem /usr/include/qt5/QtQml -isystem /usr/include/qt5/QtNetwork -isystem /usr/include/qt5/QtCore -I. -isystem /usr/include/libdrm -I/usr/lib64/qt5/mkspecs/linux-g++ -o AddressBookModel.o ../src/model/AddressBookModel.cpp
../src/model/AddressBookModel.cpp: In member function 'virtual int AddressBookModel::rowCount(const QModelIndex&) const':
../src/model/AddressBookModel.cpp:25:51: warning: unused parameter 'parent' [-Wunused-parameter]
 int AddressBookModel::rowCount(const QModelIndex &parent) const
                                ~~~~~~~~~~~~~~~~~~~^~~~~~
/usr/lib64/qt5/bin/rcc -name translations translations/translations.qrc -o qrc_translations.cpp
g++ -c -pipe -fPIC -fstack-protector -fstack-protector-strong -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=1 -Wformat -Wformat-security -O2 -std=gnu++11 -Wall -W -D_REENTRANT -fPIC -DQT_NO_DEBUG -DQT_QUICK_LIB -DQT_WIDGETS_LIB -DQT_GUI_LIB -DQT_QML_LIB -DQT_NETWORK_LIB -DQT_CORE_LIB -I../../monero-gui -I. -I/home/liao/monero-gui/monero/include -I../src/libwalletqt -I../src/QR-Code-generator -I../src -I../monero/src -isystem /usr/include/qt5 -isystem /usr/include/qt5/QtQuick -isystem /usr/include/qt5/QtWidgets -isystem /usr/include/qt5/QtGui -isystem /usr/include/qt5/QtQml -isystem /usr/include/qt5/QtNetwork -isystem /usr/include/qt5/QtCore -I. -isystem /usr/include/libdrm -I/usr/lib64/qt5/mkspecs/linux-g++ -o qrc_translations.o qrc_translations.cpp
/usr/lib64/qt5/bin/rcc -name qml_qmlcache qml_qmlcache.qrc -o qrc_qml_qmlcache.cpp
g++ -c -pipe -fPIC -fstack-protector -fstack-protector-strong -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=1 -Wformat -Wformat-security -O2 -std=gnu++11 -Wall -W -D_REENTRANT -fPIC -DQT_NO_DEBUG -DQT_QUICK_LIB -DQT_WIDGETS_LIB -DQT_GUI_LIB -DQT_QML_LIB -DQT_NETWORK_LIB -DQT_CORE_LIB -I../../monero-gui -I. -I/home/liao/monero-gui/monero/include -I../src/libwalletqt -I../src/QR-Code-generator -I../src -I../monero/src -isystem /usr/include/qt5 -isystem /usr/include/qt5/QtQuick -isystem /usr/include/qt5/QtWidgets -isystem /usr/include/qt5/QtGui -isystem /usr/include/qt5/QtQml -isystem /usr/include/qt5/QtNetwork -isystem /usr/include/qt5/QtCore -I. -isystem /usr/include/libdrm -I/usr/lib64/qt5/mkspecs/linux-g++ -o qrc_qml_qmlcache.o qrc_qml_qmlcache.cpp
/usr/lib64/qt5/bin/qmlcachegen --resource=/home/liao/monero-gui/qml.qrc -o LeftPanel_qml.cpp ../LeftPanel.qml
g++ -c -pipe -fPIC -fstack-protector -fstack-protector-strong -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=1 -Wformat -Wformat-security -O2 -std=gnu++11 -Wall -W -D_REENTRANT -fPIC -DQT_NO_DEBUG -DQT_QUICK_LIB -DQT_WIDGETS_LIB -DQT_GUI_LIB -DQT_QML_LIB -DQT_NETWORK_LIB -DQT_CORE_LIB -I../../monero-gui -I. -I/home/liao/monero-gui/monero/include -I../src/libwalletqt -I../src/QR-Code-generator -I../src -I../monero/src -isystem /usr/include/qt5 -isystem /usr/include/qt5/QtQuick -isystem /usr/include/qt5/QtWidgets -isystem /usr/include/qt5/QtGui -isystem /usr/include/qt5/QtQml -isystem /usr/include/qt5/QtNetwork -isystem /usr/include/qt5/QtCore -I. -isystem /usr/include/libdrm -I/usr/lib64/qt5/mkspecs/linux-g++ -o LeftPanel_qml.o LeftPanel_qml.cpp
/usr/lib64/qt5/bin/qmlcachegen --resource=/home/liao/monero-gui/qml.qrc -o version_js.cpp ../version.js
g++ -c -pipe -fPIC -fstack-protector -fstack-protector-strong -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=1 -Wformat -Wformat-security -O2 -std=gnu++11 -Wall -W -D_REENTRANT -fPIC -DQT_NO_DEBUG -DQT_QUICK_LIB -DQT_WIDGETS_LIB -DQT_GUI_LIB -DQT_QML_LIB -DQT_NETWORK_LIB -DQT_CORE_LIB -I../../monero-gui -I. -I/home/liao/monero-gui/monero/include -I../src/libwalletqt -I../src/QR-Code-generator -I../src -I../monero/src -isystem /usr/include/qt5 -isystem /usr/include/qt5/QtQuick -isystem /usr/include/qt5/QtWidgets -isystem /usr/include/qt5/QtGui -isystem /usr/include/qt5/QtQml -isystem /usr/include/qt5/QtNetwork -isystem /usr/include/qt5/QtCore -I. -isystem /usr/include/libdrm -I/usr/lib64/qt5/mkspecs/linux-g++ -o version_js.o version_js.cpp
/usr/lib64/qt5/bin/qmlcachegen --resource=/home/liao/monero-gui/qml.qrc -o MiddlePanel_qml.cpp ../MiddlePanel.qml
g++ -c -pipe -fPIC -fstack-protector -fstack-protector-strong -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=1 -Wformat -Wformat-security -O2 -std=gnu++11 -Wall -W -D_REENTRANT -fPIC -DQT_NO_DEBUG -DQT_QUICK_LIB -DQT_WIDGETS_LIB -DQT_GUI_LIB -DQT_QML_LIB -DQT_NETWORK_LIB -DQT_CORE_LIB -I../../monero-gui -I. -I/home/liao/monero-gui/monero/include -I../src/libwalletqt -I../src/QR-Code-generator -I../src -I../monero/src -isystem /usr/include/qt5 -isystem /usr/include/qt5/QtQuick -isystem /usr/include/qt5/QtWidgets -isystem /usr/include/qt5/QtGui -isystem /usr/include/qt5/QtQml -isystem /usr/include/qt5/QtNetwork -isystem /usr/include/qt5/QtCore -I. -isystem /usr/include/libdrm -I/usr/lib64/qt5/mkspecs/linux-g++ -o MiddlePanel_qml.o MiddlePanel_qml.cpp
/usr/lib64/qt5/bin/qmlcachegen --resource=/home/liao/monero-gui/qml.qrc -o main_qml.cpp ../main.qml
g++ -c -pipe -fPIC -fstack-protector -fstack-protector-strong -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=1 -Wformat -Wformat-security -O2 -std=gnu++11 -Wall -W -D_REENTRANT -fPIC -DQT_NO_DEBUG -DQT_QUICK_LIB -DQT_WIDGETS_LIB -DQT_GUI_LIB -DQT_QML_LIB -DQT_NETWORK_LIB -DQT_CORE_LIB -I../../monero-gui -I. -I/home/liao/monero-gui/monero/include -I../src/libwalletqt -I../src/QR-Code-generator -I../src -I../monero/src -isystem /usr/include/qt5 -isystem /usr/include/qt5/QtQuick -isystem /usr/include/qt5/QtWidgets -isystem /usr/include/qt5/QtGui -isystem /usr/include/qt5/QtQml -isystem /usr/include/qt5/QtNetwork -isystem /usr/include/qt5/QtCore -I. -isystem /usr/include/libdrm -I/usr/lib64/qt5/mkspecs/linux-g++ -o main_qml.o main_qml.cpp
/usr/lib64/qt5/bin/qmlcachegen --resource=/home/liao/monero-gui/qml.qrc -o wizard_WizardManageWalletUI_qml.cpp ../wizard/WizardManageWalletUI.qml
g++ -c -pipe -fPIC -fstack-protector -fstack-protector-strong -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=1 -Wformat -Wformat-security -O2 -std=gnu++11 -Wall -W -D_REENTRANT -fPIC -DQT_NO_DEBUG -DQT_QUICK_LIB -DQT_WIDGETS_LIB -DQT_GUI_LIB -DQT_QML_LIB -DQT_NETWORK_LIB -DQT_CORE_LIB -I../../monero-gui -I. -I/home/liao/monero-gui/monero/include -I../src/libwalletqt -I../src/QR-Code-generator -I../src -I../monero/src -isystem /usr/include/qt5 -isystem /usr/include/qt5/QtQuick -isystem /usr/include/qt5/QtWidgets -isystem /usr/include/qt5/QtGui -isystem /usr/include/qt5/QtQml -isystem /usr/include/qt5/QtNetwork -isystem /usr/include/qt5/QtCore -I. -isystem /usr/include/libdrm -I/usr/lib64/qt5/mkspecs/linux-g++ -o wizard_WizardManageWalletUI_qml.o wizard_WizardManageWalletUI_qml.cpp
/usr/lib64/qt5/bin/qmlcachegen --resource=/home/liao/monero-gui/qml.qrc -o components_TitleBar_qml.cpp ../components/TitleBar.qml
g++ -c -pipe -fPIC -fstack-protector -fstack-protector-strong -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=1 -Wformat -Wformat-security -O2 -std=gnu++11 -Wall -W -D_REENTRANT -fPIC -DQT_NO_DEBUG -DQT_QUICK_LIB -DQT_WIDGETS_LIB -DQT_GUI_LIB -DQT_QML_LIB -DQT_NETWORK_LIB -DQT_CORE_LIB -I../../monero-gui -I. -I/home/liao/monero-gui/monero/include -I../src/libwalletqt -I../src/QR-Code-generator -I../src -I../monero/src -isystem /usr/include/qt5 -isystem /usr/include/qt5/QtQuick -isystem /usr/include/qt5/QtWidgets -isystem /usr/include/qt5/QtGui -isystem /usr/include/qt5/QtQml -isystem /usr/include/qt5/QtNetwork -isystem /usr/include/qt5/QtCore -I. -isystem /usr/include/libdrm -I/usr/lib64/qt5/mkspecs/linux-g++ -o components_TitleBar_qml.o components_TitleBar_qml.cpp
/usr/lib64/qt5/bin/qmlcachegen --resource=/home/liao/monero-gui/qml.qrc -o components_PasswordDialog_qml.cpp ../components/PasswordDialog.qml
g++ -c -pipe -fPIC -fstack-protector -fstack-protector-strong -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=1 -Wformat -Wformat-security -O2 -std=gnu++11 -Wall -W -D_REENTRANT -fPIC -DQT_NO_DEBUG -DQT_QUICK_LIB -DQT_WIDGETS_LIB -DQT_GUI_LIB -DQT_QML_LIB -DQT_NETWORK_LIB -DQT_CORE_LIB -I../../monero-gui -I. -I/home/liao/monero-gui/monero/include -I../src/libwalletqt -I../src/QR-Code-generator -I../src -I../monero/src -isystem /usr/include/qt5 -isystem /usr/include/qt5/QtQuick -isystem /usr/include/qt5/QtWidgets -isystem /usr/include/qt5/QtGui -isystem /usr/include/qt5/QtQml -isystem /usr/include/qt5/QtNetwork -isystem /usr/include/qt5/QtCore -I. -isystem /usr/include/libdrm -I/usr/lib64/qt5/mkspecs/linux-g++ -o components_PasswordDialog_qml.o components_PasswordDialog_qml.cpp
/usr/lib64/qt5/bin/qmlcachegen --resource=/home/liao/monero-gui/qml.qrc -o components_Style_qml.cpp ../components/Style.qml
g++ -c -pipe -fPIC -fstack-protector -fstack-protector-strong -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=1 -Wformat -Wformat-security -O2 -std=gnu++11 -Wall -W -D_REENTRANT -fPIC -DQT_NO_DEBUG -DQT_QUICK_LIB -DQT_WIDGETS_LIB -DQT_GUI_LIB -DQT_QML_LIB -DQT_NETWORK_LIB -DQT_CORE_LIB -I../../monero-gui -I. -I/home/liao/monero-gui/monero/include -I../src/libwalletqt -I../src/QR-Code-generator -I../src -I../monero/src -isystem /usr/include/qt5 -isystem /usr/include/qt5/QtQuick -isystem /usr/include/qt5/QtWidgets -isystem /usr/include/qt5/QtGui -isystem /usr/include/qt5/QtQml -isystem /usr/include/qt5/QtNetwork -isystem /usr/include/qt5/QtCore -I. -isystem /usr/include/libdrm -I/usr/lib64/qt5/mkspecs/linux-g++ -o components_Style_qml.o components_Style_qml.cpp
/usr/lib64/qt5/bin/qmlcachegen --resource=/home/liao/monero-gui/qml.qrc -o components_WarningBox_qml.cpp ../components/WarningBox.qml
g++ -c -pipe -fPIC -fstack-protector -fstack-protector-strong -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=1 -Wformat -Wformat-security -O2 -std=gnu++11 -Wall -W -D_REENTRANT -fPIC -DQT_NO_DEBUG -DQT_QUICK_LIB -DQT_WIDGETS_LIB -DQT_GUI_LIB -DQT_QML_LIB -DQT_NETWORK_LIB -DQT_CORE_LIB -I../../monero-gui -I. -I/home/liao/monero-gui/monero/include -I../src/libwalletqt -I../src/QR-Code-generator -I../src -I../monero/src -isystem /usr/include/qt5 -isystem /usr/include/qt5/QtQuick -isystem /usr/include/qt5/QtWidgets -isystem /usr/include/qt5/QtGui -isystem /usr/include/qt5/QtQml -isystem /usr/include/qt5/QtNetwork -isystem /usr/include/qt5/QtCore -I. -isystem /usr/include/libdrm -I/usr/lib64/qt5/mkspecs/linux-g++ -o components_WarningBox_qml.o components_WarningBox_qml.cpp
/usr/lib64/qt5/bin/qmlcachegen --resource=/home/liao/monero-gui/qml.qrc -o components_InputDialog_qml.cpp ../components/InputDialog.qml
g++ -c -pipe -fPIC -fstack-protector -fstack-protector-strong -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=1 -Wformat -Wformat-security -O2 -std=gnu++11 -Wall -W -D_REENTRANT -fPIC -DQT_NO_DEBUG -DQT_QUICK_LIB -DQT_WIDGETS_LIB -DQT_GUI_LIB -DQT_QML_LIB -DQT_NETWORK_LIB -DQT_CORE_LIB -I../../monero-gui -I. -I/home/liao/monero-gui/monero/include -I../src/libwalletqt -I../src/QR-Code-generator -I../src -I../monero/src -isystem /usr/include/qt5 -isystem /usr/include/qt5/QtQuick -isystem /usr/include/qt5/QtWidgets -isystem /usr/include/qt5/QtGui -isystem /usr/include/qt5/QtQml -isystem /usr/include/qt5/QtNetwork -isystem /usr/include/qt5/QtCore -I. -isystem /usr/include/libdrm -I/usr/lib64/qt5/mkspecs/linux-g++ -o components_InputDialog_qml.o components_InputDialog_qml.cpp
/usr/lib64/qt5/bin/qmlcachegen --resource=/home/liao/monero-gui/qml.qrc -o components_LineEdit_qml.cpp ../components/LineEdit.qml
g++ -c -pipe -fPIC -fstack-protector -fstack-protector-strong -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=1 -Wformat -Wformat-security -O2 -std=gnu++11 -Wall -W -D_REENTRANT -fPIC -DQT_NO_DEBUG -DQT_QUICK_LIB -DQT_WIDGETS_LIB -DQT_GUI_LIB -DQT_QML_LIB -DQT_NETWORK_LIB -DQT_CORE_LIB -I../../monero-gui -I. -I/home/liao/monero-gui/monero/include -I../src/libwalletqt -I../src/QR-Code-generator -I../src -I../monero/src -isystem /usr/include/qt5 -isystem /usr/include/qt5/QtQuick -isystem /usr/include/qt5/QtWidgets -isystem /usr/include/qt5/QtGui -isystem /usr/include/qt5/QtQml -isystem /usr/include/qt5/QtNetwork -isystem /usr/include/qt5/QtCore -I. -isystem /usr/include/libdrm -I/usr/lib64/qt5/mkspecs/linux-g++ -o components_LineEdit_qml.o components_LineEdit_qml.cpp
/usr/lib64/qt5/bin/qmlcachegen --resource=/home/liao/monero-gui/qml.qrc -o components_HistoryTableInnerColumn_qml.cpp ../components/HistoryTableInnerColumn.qml
g++ -c -pipe -fPIC -fstack-protector -fstack-protector-strong -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=1 -Wformat -Wformat-security -O2 -std=gnu++11 -Wall -W -D_REENTRANT -fPIC -DQT_NO_DEBUG -DQT_QUICK_LIB -DQT_WIDGETS_LIB -DQT_GUI_LIB -DQT_QML_LIB -DQT_NETWORK_LIB -DQT_CORE_LIB -I../../monero-gui -I. -I/home/liao/monero-gui/monero/include -I../src/libwalletqt -I../src/QR-Code-generator -I../src -I../monero/src -isystem /usr/include/qt5 -isystem /usr/include/qt5/QtQuick -isystem /usr/include/qt5/QtWidgets -isystem /usr/include/qt5/QtGui -isystem /usr/include/qt5/QtQml -isystem /usr/include/qt5/QtNetwork -isystem /usr/include/qt5/QtCore -I. -isystem /usr/include/libdrm -I/usr/lib64/qt5/mkspecs/linux-g++ -o components_HistoryTableInnerColumn_qml.o components_HistoryTableInnerColumn_qml.cpp
/usr/lib64/qt5/bin/qmlcachegen --resource=/home/liao/monero-gui/qml.qrc -o components_StandardDropdown_qml.cpp ../components/StandardDropdown.qml
g++ -c -pipe -fPIC -fstack-protector -fstack-protector-strong -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=1 -Wformat -Wformat-security -O2 -std=gnu++11 -Wall -W -D_REENTRANT -fPIC -DQT_NO_DEBUG -DQT_QUICK_LIB -DQT_WIDGETS_LIB -DQT_GUI_LIB -DQT_QML_LIB -DQT_NETWORK_LIB -DQT_CORE_LIB -I../../monero-gui -I. -I/home/liao/monero-gui/monero/include -I../src/libwalletqt -I../src/QR-Code-generator -I../src -I../monero/src -isystem /usr/include/qt5 -isystem /usr/include/qt5/QtQuick -isystem /usr/include/qt5/QtWidgets -isystem /usr/include/qt5/QtGui -isystem /usr/include/qt5/QtQml -isystem /usr/include/qt5/QtNetwork -isystem /usr/include/qt5/QtCore -I. -isystem /usr/include/libdrm -I/usr/lib64/qt5/mkspecs/linux-g++ -o components_StandardDropdown_qml.o components_StandardDropdown_qml.cpp
/usr/lib64/qt5/bin/qmlcachegen --resource=/home/liao/monero-gui/qml.qrc -o components_InputMulti_qml.cpp ../components/InputMulti.qml
g++ -c -pipe -fPIC -fstack-protector -fstack-protector-strong -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=1 -Wformat -Wformat-security -O2 -std=gnu++11 -Wall -W -D_REENTRANT -fPIC -DQT_NO_DEBUG -DQT_QUICK_LIB -DQT_WIDGETS_LIB -DQT_GUI_LIB -DQT_QML_LIB -DQT_NETWORK_LIB -DQT_CORE_LIB -I../../monero-gui -I. -I/home/liao/monero-gui/monero/include -I../src/libwalletqt -I../src/QR-Code-generator -I../src -I../monero/src -isystem /usr/include/qt5 -isystem /usr/include/qt5/QtQuick -isystem /usr/include/qt5/QtWidgets -isystem /usr/include/qt5/QtGui -isystem /usr/include/qt5/QtQml -isystem /usr/include/qt5/QtNetwork -isystem /usr/include/qt5/QtCore -I. -isystem /usr/include/libdrm -I/usr/lib64/qt5/mkspecs/linux-g++ -o components_InputMulti_qml.o components_InputMulti_qml.cpp
/usr/lib64/qt5/bin/qmlcachegen --resource=/home/liao/monero-gui/qml.qrc -o components_RemoteNodeEdit_qml.cpp ../components/RemoteNodeEdit.qml
g++ -c -pipe -fPIC -fstack-protector -fstack-protector-strong -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=1 -Wformat -Wformat-security -O2 -std=gnu++11 -Wall -W -D_REENTRANT -fPIC -DQT_NO_DEBUG -DQT_QUICK_LIB -DQT_WIDGETS_LIB -DQT_GUI_LIB -DQT_QML_LIB -DQT_NETWORK_LIB -DQT_CORE_LIB -I../../monero-gui -I. -I/home/liao/monero-gui/monero/include -I../src/libwalletqt -I../src/QR-Code-generator -I../src -I../monero/src -isystem /usr/include/qt5 -isystem /usr/include/qt5/QtQuick -isystem /usr/include/qt5/QtWidgets -isystem /usr/include/qt5/QtGui -isystem /usr/include/qt5/QtQml -isystem /usr/include/qt5/QtNetwork -isystem /usr/include/qt5/QtCore -I. -isystem /usr/include/libdrm -I/usr/lib64/qt5/mkspecs/linux-g++ -o components_RemoteNodeEdit_qml.o components_RemoteNodeEdit_qml.cpp
/usr/lib64/qt5/bin/qmlcachegen --resource=/home/liao/monero-gui/qml.qrc -o components_ProgressBar_qml.cpp ../components/ProgressBar.qml
g++ -c -pipe -fPIC -fstack-protector -fstack-protector-strong -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=1 -Wformat -Wformat-security -O2 -std=gnu++11 -Wall -W -D_REENTRANT -fPIC -DQT_NO_DEBUG -DQT_QUICK_LIB -DQT_WIDGETS_LIB -DQT_GUI_LIB -DQT_QML_LIB -DQT_NETWORK_LIB -DQT_CORE_LIB -I../../monero-gui -I. -I/home/liao/monero-gui/monero/include -I../src/libwalletqt -I../src/QR-Code-generator -I../src -I../monero/src -isystem /usr/include/qt5 -isystem /usr/include/qt5/QtQuick -isystem /usr/include/qt5/QtWidgets -isystem /usr/include/qt5/QtGui -isystem /usr/include/qt5/QtQml -isystem /usr/include/qt5/QtNetwork -isystem /usr/include/qt5/QtCore -I. -isystem /usr/include/libdrm -I/usr/lib64/qt5/mkspecs/linux-g++ -o components_ProgressBar_qml.o components_ProgressBar_qml.cpp
/usr/lib64/qt5/bin/qmlcachegen --resource=/home/liao/monero-gui/qml.qrc -o components_LineEditMulti_qml.cpp ../components/LineEditMulti.qml
g++ -c -pipe -fPIC -fstack-protector -fstack-protector-strong -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=1 -Wformat -Wformat-security -O2 -std=gnu++11 -Wall -W -D_REENTRANT -fPIC -DQT_NO_DEBUG -DQT_QUICK_LIB -DQT_WIDGETS_LIB -DQT_GUI_LIB -DQT_QML_LIB -DQT_NETWORK_LIB -DQT_CORE_LIB -I../../monero-gui -I. -I/home/liao/monero-gui/monero/include -I../src/libwalletqt -I../src/QR-Code-generator -I../src -I../monero/src -isystem /usr/include/qt5 -isystem /usr/include/qt5/QtQuick -isystem /usr/include/qt5/QtWidgets -isystem /usr/include/qt5/QtGui -isystem /usr/include/qt5/QtQml -isystem /usr/include/qt5/QtNetwork -isystem /usr/include/qt5/QtCore -I. -isystem /usr/include/libdrm -I/usr/lib64/qt5/mkspecs/linux-g++ -o components_LineEditMulti_qml.o components_LineEditMulti_qml.cpp
/usr/lib64/qt5/bin/qmlcachegen --resource=/home/liao/monero-gui/qml.qrc -o js_Windows_js.cpp ../js/Windows.js
g++ -c -pipe -fPIC -fstack-protector -fstack-protector-strong -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=1 -Wformat -Wformat-security -O2 -std=gnu++11 -Wall -W -D_REENTRANT -fPIC -DQT_NO_DEBUG -DQT_QUICK_LIB -DQT_WIDGETS_LIB -DQT_GUI_LIB -DQT_QML_LIB -DQT_NETWORK_LIB -DQT_CORE_LIB -I../../monero-gui -I. -I/home/liao/monero-gui/monero/include -I../src/libwalletqt -I../src/QR-Code-generator -I../src -I../monero/src -isystem /usr/include/qt5 -isystem /usr/include/qt5/QtQuick -isystem /usr/include/qt5/QtWidgets -isystem /usr/include/qt5/QtGui -isystem /usr/include/qt5/QtQml -isystem /usr/include/qt5/QtNetwork -isystem /usr/include/qt5/QtCore -I. -isystem /usr/include/libdrm -I/usr/lib64/qt5/mkspecs/linux-g++ -o js_Windows_js.o js_Windows_js.cpp
/usr/lib64/qt5/bin/qmlcachegen --resource=/home/liao/monero-gui/qml.qrc -o js_Utils_js.cpp ../js/Utils.js
g++ -c -pipe -fPIC -fstack-protector -fstack-protector-strong -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=1 -Wformat -Wformat-security -O2 -std=gnu++11 -Wall -W -D_REENTRANT -fPIC -DQT_NO_DEBUG -DQT_QUICK_LIB -DQT_WIDGETS_LIB -DQT_GUI_LIB -DQT_QML_LIB -DQT_NETWORK_LIB -DQT_CORE_LIB -I../../monero-gui -I. -I/home/liao/monero-gui/monero/include -I../src/libwalletqt -I../src/QR-Code-generator -I../src -I../monero/src -isystem /usr/include/qt5 -isystem /usr/include/qt5/QtQuick -isystem /usr/include/qt5/QtWidgets -isystem /usr/include/qt5/QtGui -isystem /usr/include/qt5/QtQml -isystem /usr/include/qt5/QtNetwork -isystem /usr/include/qt5/QtCore -I. -isystem /usr/include/libdrm -I/usr/lib64/qt5/mkspecs/linux-g++ -o js_Utils_js.o js_Utils_js.cpp
/usr/lib64/qt5/bin/qmlcachegen --resource=/home/liao/monero-gui/qml.qrc -o pages_Transfer_qml.cpp ../pages/Transfer.qml
g++ -c -pipe -fPIC -fstack-protector -fstack-protector-strong -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=1 -Wformat -Wformat-security -O2 -std=gnu++11 -Wall -W -D_REENTRANT -fPIC -DQT_NO_DEBUG -DQT_QUICK_LIB -DQT_WIDGETS_LIB -DQT_GUI_LIB -DQT_QML_LIB -DQT_NETWORK_LIB -DQT_CORE_LIB -I../../monero-gui -I. -I/home/liao/monero-gui/monero/include -I../src/libwalletqt -I../src/QR-Code-generator -I../src -I../monero/src -isystem /usr/include/qt5 -isystem /usr/include/qt5/QtQuick -isystem /usr/include/qt5/QtWidgets -isystem /usr/include/qt5/QtGui -isystem /usr/include/qt5/QtQml -isystem /usr/include/qt5/QtNetwork -isystem /usr/include/qt5/QtCore -I. -isystem /usr/include/libdrm -I/usr/lib64/qt5/mkspecs/linux-g++ -o pages_Transfer_qml.o pages_Transfer_qml.cpp
/usr/lib64/qt5/bin/qmlcachegen --resource=/home/liao/monero-gui/qml.qrc -o pages_Mining_qml.cpp ../pages/Mining.qml
g++ -c -pipe -fPIC -fstack-protector -fstack-protector-strong -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=1 -Wformat -Wformat-security -O2 -std=gnu++11 -Wall -W -D_REENTRANT -fPIC -DQT_NO_DEBUG -DQT_QUICK_LIB -DQT_WIDGETS_LIB -DQT_GUI_LIB -DQT_QML_LIB -DQT_NETWORK_LIB -DQT_CORE_LIB -I../../monero-gui -I. -I/home/liao/monero-gui/monero/include -I../src/libwalletqt -I../src/QR-Code-generator -I../src -I../monero/src -isystem /usr/include/qt5 -isystem /usr/include/qt5/QtQuick -isystem /usr/include/qt5/QtWidgets -isystem /usr/include/qt5/QtGui -isystem /usr/include/qt5/QtQml -isystem /usr/include/qt5/QtNetwork -isystem /usr/include/qt5/QtCore -I. -isystem /usr/include/libdrm -I/usr/lib64/qt5/mkspecs/linux-g++ -o pages_Mining_qml.o pages_Mining_qml.cpp
/usr/lib64/qt5/bin/qmlcachegen --resource=/home/liao/monero-gui/qml.qrc -o pages_Sign_qml.cpp ../pages/Sign.qml
g++ -c -pipe -fPIC -fstack-protector -fstack-protector-strong -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=1 -Wformat -Wformat-security -O2 -std=gnu++11 -Wall -W -D_REENTRANT -fPIC -DQT_NO_DEBUG -DQT_QUICK_LIB -DQT_WIDGETS_LIB -DQT_GUI_LIB -DQT_QML_LIB -DQT_NETWORK_LIB -DQT_CORE_LIB -I../../monero-gui -I. -I/home/liao/monero-gui/monero/include -I../src/libwalletqt -I../src/QR-Code-generator -I../src -I../monero/src -isystem /usr/include/qt5 -isystem /usr/include/qt5/QtQuick -isystem /usr/include/qt5/QtWidgets -isystem /usr/include/qt5/QtGui -isystem /usr/include/qt5/QtQml -isystem /usr/include/qt5/QtNetwork -isystem /usr/include/qt5/QtCore -I. -isystem /usr/include/libdrm -I/usr/lib64/qt5/mkspecs/linux-g++ -o pages_Sign_qml.o pages_Sign_qml.cpp
/usr/lib64/qt5/bin/qmlcachegen --resource=/home/liao/monero-gui/qml.qrc -o pages_Keys_qml.cpp ../pages/Keys.qml
g++ -c -pipe -fPIC -fstack-protector -fstack-protector-strong -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=1 -Wformat -Wformat-security -O2 -std=gnu++11 -Wall -W -D_REENTRANT -fPIC -DQT_NO_DEBUG -DQT_QUICK_LIB -DQT_WIDGETS_LIB -DQT_GUI_LIB -DQT_QML_LIB -DQT_NETWORK_LIB -DQT_CORE_LIB -I../../monero-gui -I. -I/home/liao/monero-gui/monero/include -I../src/libwalletqt -I../src/QR-Code-generator -I../src -I../monero/src -isystem /usr/include/qt5 -isystem /usr/include/qt5/QtQuick -isystem /usr/include/qt5/QtWidgets -isystem /usr/include/qt5/QtGui -isystem /usr/include/qt5/QtQml -isystem /usr/include/qt5/QtNetwork -isystem /usr/include/qt5/QtCore -I. -isystem /usr/include/libdrm -I/usr/lib64/qt5/mkspecs/linux-g++ -o pages_Keys_qml.o pages_Keys_qml.cpp
/usr/lib64/qt5/bin/qmlcachegen --resource=/home/liao/monero-gui/qml.qrc -o pages_History_qml.cpp ../pages/History.qml
g++ -c -pipe -fPIC -fstack-protector -fstack-protector-strong -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=1 -Wformat -Wformat-security -O2 -std=gnu++11 -Wall -W -D_REENTRANT -fPIC -DQT_NO_DEBUG -DQT_QUICK_LIB -DQT_WIDGETS_LIB -DQT_GUI_LIB -DQT_QML_LIB -DQT_NETWORK_LIB -DQT_CORE_LIB -I../../monero-gui -I. -I/home/liao/monero-gui/monero/include -I../src/libwalletqt -I../src/QR-Code-generator -I../src -I../monero/src -isystem /usr/include/qt5 -isystem /usr/include/qt5/QtQuick -isystem /usr/include/qt5/QtWidgets -isystem /usr/include/qt5/QtGui -isystem /usr/include/qt5/QtQml -isystem /usr/include/qt5/QtNetwork -isystem /usr/include/qt5/QtCore -I. -isystem /usr/include/libdrm -I/usr/lib64/qt5/mkspecs/linux-g++ -o pages_History_qml.o pages_History_qml.cpp
/usr/lib64/qt5/bin/qmlcachegen --resource=/home/liao/monero-gui/qml.qrc -o pages_settings_SettingsInfo_qml.cpp ../pages/settings/SettingsInfo.qml
g++ -c -pipe -fPIC -fstack-protector -fstack-protector-strong -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=1 -Wformat -Wformat-security -O2 -std=gnu++11 -Wall -W -D_REENTRANT -fPIC -DQT_NO_DEBUG -DQT_QUICK_LIB -DQT_WIDGETS_LIB -DQT_GUI_LIB -DQT_QML_LIB -DQT_NETWORK_LIB -DQT_CORE_LIB -I../../monero-gui -I. -I/home/liao/monero-gui/monero/include -I../src/libwalletqt -I../src/QR-Code-generator -I../src -I../monero/src -isystem /usr/include/qt5 -isystem /usr/include/qt5/QtQuick -isystem /usr/include/qt5/QtWidgets -isystem /usr/include/qt5/QtGui -isystem /usr/include/qt5/QtQml -isystem /usr/include/qt5/QtNetwork -isystem /usr/include/qt5/QtCore -I. -isystem /usr/include/libdrm -I/usr/lib64/qt5/mkspecs/linux-g++ -o pages_settings_SettingsInfo_qml.o pages_settings_SettingsInfo_qml.cpp
/usr/lib64/qt5/bin/qmlcachegen --resource=/home/liao/monero-gui/qml.qrc -o pages_settings_Navbar_qml.cpp ../pages/settings/Navbar.qml
g++ -c -pipe -fPIC -fstack-protector -fstack-protector-strong -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=1 -Wformat -Wformat-security -O2 -std=gnu++11 -Wall -W -D_REENTRANT -fPIC -DQT_NO_DEBUG -DQT_QUICK_LIB -DQT_WIDGETS_LIB -DQT_GUI_LIB -DQT_QML_LIB -DQT_NETWORK_LIB -DQT_CORE_LIB -I../../monero-gui -I. -I/home/liao/monero-gui/monero/include -I../src/libwalletqt -I../src/QR-Code-generator -I../src -I../monero/src -isystem /usr/include/qt5 -isystem /usr/include/qt5/QtQuick -isystem /usr/include/qt5/QtWidgets -isystem /usr/include/qt5/QtGui -isystem /usr/include/qt5/QtQml -isystem /usr/include/qt5/QtNetwork -isystem /usr/include/qt5/QtCore -I. -isystem /usr/include/libdrm -I/usr/lib64/qt5/mkspecs/linux-g++ -o pages_settings_Navbar_qml.o pages_settings_Navbar_qml.cpp
/usr/lib64/qt5/bin/qmlcachegen --resource=/home/liao/monero-gui/qml.qrc -o pages_settings_Settings_qml.cpp ../pages/settings/Settings.qml
g++ -c -pipe -fPIC -fstack-protector -fstack-protector-strong -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=1 -Wformat -Wformat-security -O2 -std=gnu++11 -Wall -W -D_REENTRANT -fPIC -DQT_NO_DEBUG -DQT_QUICK_LIB -DQT_WIDGETS_LIB -DQT_GUI_LIB -DQT_QML_LIB -DQT_NETWORK_LIB -DQT_CORE_LIB -I../../monero-gui -I. -I/home/liao/monero-gui/monero/include -I../src/libwalletqt -I../src/QR-Code-generator -I../src -I../monero/src -isystem /usr/include/qt5 -isystem /usr/include/qt5/QtQuick -isystem /usr/include/qt5/QtWidgets -isystem /usr/include/qt5/QtGui -isystem /usr/include/qt5/QtQml -isystem /usr/include/qt5/QtNetwork -isystem /usr/include/qt5/QtCore -I. -isystem /usr/include/libdrm -I/usr/lib64/qt5/mkspecs/linux-g++ -o pages_settings_Settings_qml.o pages_settings_Settings_qml.cpp
/usr/lib64/qt5/bin/qmlcachegen --resource=/home/liao/monero-gui/qml.qrc -o pages_settings_SettingsLog_qml.cpp ../pages/settings/SettingsLog.qml
g++ -c -pipe -fPIC -fstack-protector -fstack-protector-strong -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=1 -Wformat -Wformat-security -O2 -std=gnu++11 -Wall -W -D_REENTRANT -fPIC -DQT_NO_DEBUG -DQT_QUICK_LIB -DQT_WIDGETS_LIB -DQT_GUI_LIB -DQT_QML_LIB -DQT_NETWORK_LIB -DQT_CORE_LIB -I../../monero-gui -I. -I/home/liao/monero-gui/monero/include -I../src/libwalletqt -I../src/QR-Code-generator -I../src -I../monero/src -isystem /usr/include/qt5 -isystem /usr/include/qt5/QtQuick -isystem /usr/include/qt5/QtWidgets -isystem /usr/include/qt5/QtGui -isystem /usr/include/qt5/QtQml -isystem /usr/include/qt5/QtNetwork -isystem /usr/include/qt5/QtCore -I. -isystem /usr/include/libdrm -I/usr/lib64/qt5/mkspecs/linux-g++ -o pages_settings_SettingsLog_qml.o pages_settings_SettingsLog_qml.cpp
/usr/lib64/qt5/bin/qmlcachegen --resource=/home/liao/monero-gui/qml.qrc -o pages_settings_SettingsLayout_qml.cpp ../pages/settings/SettingsLayout.qml
g++ -c -pipe -fPIC -fstack-protector -fstack-protector-strong -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=1 -Wformat -Wformat-security -O2 -std=gnu++11 -Wall -W -D_REENTRANT -fPIC -DQT_NO_DEBUG -DQT_QUICK_LIB -DQT_WIDGETS_LIB -DQT_GUI_LIB -DQT_QML_LIB -DQT_NETWORK_LIB -DQT_CORE_LIB -I../../monero-gui -I. -I/home/liao/monero-gui/monero/include -I../src/libwalletqt -I../src/QR-Code-generator -I../src -I../monero/src -isystem /usr/include/qt5 -isystem /usr/include/qt5/QtQuick -isystem /usr/include/qt5/QtWidgets -isystem /usr/include/qt5/QtGui -isystem /usr/include/qt5/QtQml -isystem /usr/include/qt5/QtNetwork -isystem /usr/include/qt5/QtCore -I. -isystem /usr/include/libdrm -I/usr/lib64/qt5/mkspecs/linux-g++ -o pages_settings_SettingsLayout_qml.o pages_settings_SettingsLayout_qml.cpp
/usr/lib64/qt5/bin/qmlcachegen --resource=/home/liao/monero-gui/qml.qrc -o pages_settings_SettingsWallet_qml.cpp ../pages/settings/SettingsWallet.qml
g++ -c -pipe -fPIC -fstack-protector -fstack-protector-strong -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=1 -Wformat -Wformat-security -O2 -std=gnu++11 -Wall -W -D_REENTRANT -fPIC -DQT_NO_DEBUG -DQT_QUICK_LIB -DQT_WIDGETS_LIB -DQT_GUI_LIB -DQT_QML_LIB -DQT_NETWORK_LIB -DQT_CORE_LIB -I../../monero-gui -I. -I/home/liao/monero-gui/monero/include -I../src/libwalletqt -I../src/QR-Code-generator -I../src -I../monero/src -isystem /usr/include/qt5 -isystem /usr/include/qt5/QtQuick -isystem /usr/include/qt5/QtWidgets -isystem /usr/include/qt5/QtGui -isystem /usr/include/qt5/QtQml -isystem /usr/include/qt5/QtNetwork -isystem /usr/include/qt5/QtCore -I. -isystem /usr/include/libdrm -I/usr/lib64/qt5/mkspecs/linux-g++ -o pages_settings_SettingsWallet_qml.o pages_settings_SettingsWallet_qml.cpp
/usr/lib64/qt5/bin/qmlcachegen --resource=/home/liao/monero-gui/qml.qrc -o pages_settings_SettingsNode_qml.cpp ../pages/settings/SettingsNode.qml
g++ -c -pipe -fPIC -fstack-protector -fstack-protector-strong -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=1 -Wformat -Wformat-security -O2 -std=gnu++11 -Wall -W -D_REENTRANT -fPIC -DQT_NO_DEBUG -DQT_QUICK_LIB -DQT_WIDGETS_LIB -DQT_GUI_LIB -DQT_QML_LIB -DQT_NETWORK_LIB -DQT_CORE_LIB -I../../monero-gui -I. -I/home/liao/monero-gui/monero/include -I../src/libwalletqt -I../src/QR-Code-generator -I../src -I../monero/src -isystem /usr/include/qt5 -isystem /usr/include/qt5/QtQuick -isystem /usr/include/qt5/QtWidgets -isystem /usr/include/qt5/QtGui -isystem /usr/include/qt5/QtQml -isystem /usr/include/qt5/QtNetwork -isystem /usr/include/qt5/QtCore -I. -isystem /usr/include/libdrm -I/usr/lib64/qt5/mkspecs/linux-g++ -o pages_settings_SettingsNode_qml.o pages_settings_SettingsNode_qml.cpp
/usr/lib64/qt5/bin/qmlcachegen --resource-file-mapping=/home/liao/monero-gui/qml.qrc=/home/liao/monero-gui/build/qml_qmlcache.qrc -o qmlcache_loader.cpp ../qml.qrc
g++ -c -pipe -fPIC -fstack-protector -fstack-protector-strong -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=1 -Wformat -Wformat-security -O2 -std=gnu++11 -Wall -W -D_REENTRANT -fPIC -DQT_NO_DEBUG -DQT_QUICK_LIB -DQT_WIDGETS_LIB -DQT_GUI_LIB -DQT_QML_LIB -DQT_NETWORK_LIB -DQT_CORE_LIB -I../../monero-gui -I. -I/home/liao/monero-gui/monero/include -I../src/libwalletqt -I../src/QR-Code-generator -I../src -I../monero/src -isystem /usr/include/qt5 -isystem /usr/include/qt5/QtQuick -isystem /usr/include/qt5/QtWidgets -isystem /usr/include/qt5/QtGui -isystem /usr/include/qt5/QtQml -isystem /usr/include/qt5/QtNetwork -isystem /usr/include/qt5/QtCore -I. -isystem /usr/include/libdrm -I/usr/lib64/qt5/mkspecs/linux-g++ -o qmlcache_loader.o qmlcache_loader.cpp
/usr/lib64/qt5/bin/moc -DQT_NO_DEBUG -DQT_QUICK_LIB -DQT_WIDGETS_LIB -DQT_GUI_LIB -DQT_QML_LIB -DQT_NETWORK_LIB -DQT_CORE_LIB --include ./moc_predefs.h -I/usr/lib64/qt5/mkspecs/linux-g++ -I/home/liao/monero-gui -I/home/liao/monero-gui/monero/include -I/home/liao/monero-gui/src/libwalletqt -I/home/liao/monero-gui/src/QR-Code-generator -I/home/liao/monero-gui/src -I/home/liao/monero-gui/monero/src -I/usr/include/qt5 -I/usr/include/qt5/QtQuick -I/usr/include/qt5/QtWidgets -I/usr/include/qt5/QtGui -I/usr/include/qt5/QtQml -I/usr/include/qt5/QtNetwork -I/usr/include/qt5/QtCore -I. -I/usr/include/c++/8 -I/usr/include/c++/8/x86_64-redhat-linux -I/usr/include/c++/8/backward -I/usr/lib/gcc/x86_64-redhat-linux/8/include -I/usr/local/include -I/usr/include ../src/libwalletqt/WalletManager.h -o moc_WalletManager.cpp
g++ -c -pipe -fPIC -fstack-protector -fstack-protector-strong -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=1 -Wformat -Wformat-security -O2 -std=gnu++11 -Wall -W -D_REENTRANT -fPIC -DQT_NO_DEBUG -DQT_QUICK_LIB -DQT_WIDGETS_LIB -DQT_GUI_LIB -DQT_QML_LIB -DQT_NETWORK_LIB -DQT_CORE_LIB -I../../monero-gui -I. -I/home/liao/monero-gui/monero/include -I../src/libwalletqt -I../src/QR-Code-generator -I../src -I../monero/src -isystem /usr/include/qt5 -isystem /usr/include/qt5/QtQuick -isystem /usr/include/qt5/QtWidgets -isystem /usr/include/qt5/QtGui -isystem /usr/include/qt5/QtQml -isystem /usr/include/qt5/QtNetwork -isystem /usr/include/qt5/QtCore -I. -isystem /usr/include/libdrm -I/usr/lib64/qt5/mkspecs/linux-g++ -o moc_WalletManager.o moc_WalletManager.cpp
/usr/lib64/qt5/bin/moc -DQT_NO_DEBUG -DQT_QUICK_LIB -DQT_WIDGETS_LIB -DQT_GUI_LIB -DQT_QML_LIB -DQT_NETWORK_LIB -DQT_CORE_LIB --include ./moc_predefs.h -I/usr/lib64/qt5/mkspecs/linux-g++ -I/home/liao/monero-gui -I/home/liao/monero-gui/monero/include -I/home/liao/monero-gui/src/libwalletqt -I/home/liao/monero-gui/src/QR-Code-generator -I/home/liao/monero-gui/src -I/home/liao/monero-gui/monero/src -I/usr/include/qt5 -I/usr/include/qt5/QtQuick -I/usr/include/qt5/QtWidgets -I/usr/include/qt5/QtGui -I/usr/include/qt5/QtQml -I/usr/include/qt5/QtNetwork -I/usr/include/qt5/QtCore -I. -I/usr/include/c++/8 -I/usr/include/c++/8/x86_64-redhat-linux -I/usr/include/c++/8/backward -I/usr/lib/gcc/x86_64-redhat-linux/8/include -I/usr/local/include -I/usr/include ../src/libwalletqt/Wallet.h -o moc_Wallet.cpp
g++ -c -pipe -fPIC -fstack-protector -fstack-protector-strong -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=1 -Wformat -Wformat-security -O2 -std=gnu++11 -Wall -W -D_REENTRANT -fPIC -DQT_NO_DEBUG -DQT_QUICK_LIB -DQT_WIDGETS_LIB -DQT_GUI_LIB -DQT_QML_LIB -DQT_NETWORK_LIB -DQT_CORE_LIB -I../../monero-gui -I. -I/home/liao/monero-gui/monero/include -I../src/libwalletqt -I../src/QR-Code-generator -I../src -I../monero/src -isystem /usr/include/qt5 -isystem /usr/include/qt5/QtQuick -isystem /usr/include/qt5/QtWidgets -isystem /usr/include/qt5/QtGui -isystem /usr/include/qt5/QtQml -isystem /usr/include/qt5/QtNetwork -isystem /usr/include/qt5/QtCore -I. -isystem /usr/include/libdrm -I/usr/lib64/qt5/mkspecs/linux-g++ -o moc_Wallet.o moc_Wallet.cpp
g++ -fstack-protector -fstack-protector-strong -static-libgcc -static-libstdc++ -pie -Wl,-z,relro -Wl,-z,now -Wl,-z,noexecstack -Wl,-O1 -o release/bin/monero-wallet-gui main.o filter.o clipboardAdapter.o oscursor.o WalletManager.o Wallet.o PendingTransaction.o TransactionHistory.o TransactionInfo.o QRCodeImageProvider.o oshelper.o TranslationManager.o TransactionHistoryModel.o TransactionHistorySortFilterModel.o BitBuffer.o QrCode.o QrSegment.o AddressBookModel.o AddressBook.o SubaddressModel.o Subaddress.o zxcvbn.o UnsignedTransaction.o Logger.o MainApp.o DaemonManager.o qrc_translations.o qrc_qml_qmlcache.o RightPanel_qml.o LeftPanel_qml.o version_js.o MiddlePanel_qml.o main_qml.o wizard_WizardConfigure_qml.o wizard_WizardDaemonSettings_qml.o wizard_WizardCreateViewOnlyWallet_qml.o wizard_WizardPassword_qml.o wizard_WizardPasswordInput_qml.o wizard_WizardMain_qml.o wizard_WizardRecoveryWallet_qml.o wizard_WizardOptions_qml.o wizard_WizardCreateWalletFromDevice_qml.o wizard_WizardManageWalletUI_qml.o wizard_WizardMemoTextInput_qml.o wizard_utils_js.o wizard_WizardWelcome_qml.o wizard_WizardCreateWallet_qml.o wizard_WizardFinish_qml.o wizard_WizardDonation_qml.o wizard_WizardPasswordUI_qml.o tabs_Twitter_qml.o tabs_tweetSearch_js.o tabs_TweetsModel_qml.o components_TipItem_qml.o components_PrivacyLevelSmall_qml.o components_DaemonConsole_qml.o components_RadioButton_qml.o components_InlineButton_qml.o components_DaemonManagerDialog_qml.o components_TickDelegate_qml.o components_TitleBar_qml.o components_NetworkStatusItem_qml.o components_LabelButton_qml.o components_MobileHeader_qml.o components_NewPasswordDialog_qml.o components_PasswordDialog_qml.o components_Scroll_qml.o components_TableDropdown_qml.o components_CheckBox_qml.o components_StandardDialog_qml.o components_PrivacyLevel_qml.o components_Style_qml.o components_LabelSubheader_qml.o components_WarningBox_qml.o components_TableHeader_qml.o components_InputDialog_qml.o components_IconButton_qml.o components_LineEdit_qml.o components_DashboardTable_qml.o components_HistoryTableInnerColumn_qml.o components_Label_qml.o components_DatePicker_qml.o components_StandardDropdown_qml.o components_HistoryTable_qml.o components_SearchInput_qml.o components_InputMulti_qml.o components_ProcessingSplash_qml.o components_RemoteNodeEdit_qml.o components_TextBlock_qml.o components_StandardButton_qml.o components_Notifier_qml.o components_AddressBookTable_qml.o components_HistoryTableMobile_qml.o components_ProgressBar_qml.o components_MenuButton_qml.o components_LineEditMulti_qml.o components_CheckBox2_qml.o components_QRCodeScanner_qml.o components_Input_qml.o js_Windows_js.o js_Utils_js.o js_TxUtils_js.o pages_Transfer_qml.o pages_Mining_qml.o pages_Sign_qml.o pages_AddressBook_qml.o pages_Dashboard_qml.o pages_Keys_qml.o pages_History_qml.o pages_SharedRingDB_qml.o pages_Receive_qml.o pages_TxKey_qml.o pages_settings_SettingsInfo_qml.o pages_settings_Navbar_qml.o pages_settings_Settings_qml.o pages_settings_SettingsLog_qml.o pages_settings_SettingsLayout_qml.o pages_settings_SettingsWallet_qml.o pages_settings_SettingsNode_qml.o qmlcache_loader.o moc_filter.o moc_clipboardAdapter.o moc_oscursor.o moc_WalletManager.o moc_Wallet.o moc_PendingTransaction.o moc_TransactionHistory.o moc_TransactionInfo.o moc_Transfer.o moc_NetworkType.o moc_oshelper.o moc_TranslationManager.o moc_TransactionHistoryModel.o moc_TransactionHistorySortFilterModel.o moc_AddressBookModel.o moc_AddressBook.o moc_SubaddressModel.o moc_Subaddress.o moc_UnsignedTransaction.o moc_MainApp.o moc_DaemonManager.o   -L/home/liao/monero-gui/monero/lib -lwallet_merged -lepee -leasylogging -Wl,-Bstatic -lunbound -lboost_serialization -lboost_thread -lboost_system -lboost_date_time -lboost_filesystem -lboost_regex -lboost_chrono -lboost_program_options -lssl -llmdb -lcrypto -Wl,-Bdynamic -lQt5Quick -lQt5Widgets -lQt5Gui -lQt5Qml -lQt5Network -lQt5Core -lGL -lpthread 
/usr/bin/ld: cannot find -lwallet_merged
collect2: error: ld returned 1 exit status
make: *** [Makefile:505: release/bin/monero-wallet-gui] Error 1

22:23:28 Build Failed. 48 errors, 87 warnings. (took 4m:16s.661ms)



# Discussion History
## Lafudoci | 2018-10-13T13:22:06+00:00
I have similar issue `cannot find -lwallet_merged` on MSYS2 win10 x64
```
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/8.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe: cannot find -lwallet_merged
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/8.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe: cannot find -lunbound
collect2.exe: error: ld returned 1 exit status
make[1]: *** [Makefile.Release:382: release/bin/monero-wallet-gui.exe] Error 1
make[1]: Leaving directory '/home/LeftC/monero-gui/build'
make: *** [Makefile:36: release] Error 2

```

## sanderfoobar | 2018-10-13T19:00:56+00:00
Multiple errors have been fixed in preparation of 0.13, which is now available as a tag: https://github.com/monero-project/monero-gui/tree/v0.13.0.2

+resolved

# Action History
- Created by: lyfbuaa | 2018-10-01T14:38:20+00:00
- Closed at: 2018-10-13T19:18:21+00:00
