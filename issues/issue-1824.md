---
title: Daemon ERROR "attempting to add transaction already in blockchain"
source_url: https://github.com/monero-project/monero/issues/1824
author: assylias
assignees: []
labels: []
created_at: '2017-03-01T07:36:18+00:00'
updated_at: '2017-03-06T09:39:47+00:00'
type: issue
status: closed
closed_at: '2017-03-03T16:57:17+00:00'
---

# Original Description
I upgraded my daemon to `v0.10.2.1-release` and it doesn't seem to be able to pickup where the previous version (0.10.1.1) left the database.

I have run it using the same `--data-dir` folder as the previous version.

Log until the first block errors (sorry for the length - the most relevant bits are probably in the last 20 lines):

```
2017-02-28 20:03:53.659     7f8dbd6a4740        INFO    global  contrib/epee/src/mlog.cpp:145   New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,global:INFO,verify:FATAL,stacktrace:INFO
2017-02-28 20:03:53.659     7f8dbd6a4740        INFO    global  src/daemon/main.cpp:282 Monero 'Wolfram Warptangent' (v0.10.2.1-release)
2017-02-28 20:03:53.660     7f8dbd6a4740        WARN    daemon  src/daemon/executor.cpp:62      Monero 'Wolfram Warptangent' (v0.10.2.1-release) Daemonised
2017-02-28 20:03:53.681     7f8dbd6a4740        INFO    global  src/daemon/protocol.h:55        Initializing cryptonote protocol...
2017-02-28 20:03:53.681     7f8dbd6a4740        INFO    global  src/daemon/protocol.h:60        Cryptonote protocol initialized OK
2017-02-28 20:03:53.681     7f8dbd6a4740        INFO    global  src/daemon/p2p.h:63     Initializing p2p server...
2017-02-28 20:04:13.682     7f8dbd6a4740        INFO    stacktrace      src/common/stack_trace.cpp:119  Exception: boost::archive::portable_binary_iarchive_exception
2017-02-28 20:04:13.682     7f8dbd6a4740        INFO    stacktrace      src/common/stack_trace.cpp:120  Unwound call stack:
2017-02-28 20:04:13.706     7f8dbd6a4740        INFO    stacktrace      src/common/stack_trace.cpp:158      [1] ./monerod() [0x57c262]
2017-02-28 20:04:13.706     7f8dbd6a4740        INFO    stacktrace      src/common/stack_trace.cpp:158      [2] ./monerod() [0x764d43]
2017-02-28 20:04:13.706     7f8dbd6a4740        INFO    stacktrace      src/common/stack_trace.cpp:158      [3] ./monerod() [0x7a1bc2]
2017-02-28 20:04:13.706     7f8dbd6a4740        INFO    stacktrace      src/common/stack_trace.cpp:158      [4] ./monerod:daemonize::t_daemon::t_daemon(boost::program_options::variables_map const&)+0xe0f [0x5c043f]
2017-02-28 20:04:13.706     7f8dbd6a4740        INFO    stacktrace      src/common/stack_trace.cpp:158      [5] ./monerod:daemonize::t_executor::create_daemon(boost::program_options::variables_map const&)+0xc3 [0x64cf13]
2017-02-28 20:04:13.706     7f8dbd6a4740        INFO    stacktrace      src/common/stack_trace.cpp:158      [6] ./monerod:main+0x190e [0x58281e]
2017-02-28 20:04:13.706     7f8dbd6a4740        INFO    stacktrace      src/common/stack_trace.cpp:158      [7] /lib/x86_64-linux-gnu/libc.so.6:__libc_start_main+0xf5 [0x7f8dbc9fab45]
2017-02-28 20:04:13.707     7f8dbd6a4740        INFO    stacktrace      src/common/stack_trace.cpp:158      [8] ./monerod:_start+0x29 [0x590509]
2017-02-28 20:04:13.707     7f8dbd6a4740        INFO    stacktrace      src/common/stack_trace.cpp:158
2017-02-28 20:04:14.278     7f8dbd6a4740        INFO    global  src/daemon/p2p.h:68     P2p server initialized OK
2017-02-28 20:04:14.278     7f8dbd6a4740        INFO    global  src/daemon/rpc.h:58     Initializing core rpc server...
2017-02-28 20:04:14.278     7f8dbd6a4740        INFO    global  contrib/epee/include/net/http_server_impl_base.h:70     Binding on 127.0.0.1:18081
2017-02-28 20:04:14.279     7f8dbd6a4740        INFO    global  src/daemon/rpc.h:63     Core rpc server initialized OK on port: 18081
2017-02-28 20:04:14.279     7f8dbd6a4740        INFO    global  src/daemon/core.h:73    Initializing core...
2017-02-28 20:04:14.298     7f8dbd6a4740        INFO    stacktrace      src/common/stack_trace.cpp:119  Exception: boost::archive::portable_binary_iarchive_exception
2017-02-28 20:04:14.298     7f8dbd6a4740        INFO    stacktrace      src/common/stack_trace.cpp:120  Unwound call stack:
2017-02-28 20:04:14.300     7f8dbd6a4740        INFO    stacktrace      src/common/stack_trace.cpp:158      [1] ./monerod() [0x57c262]
2017-02-28 20:04:14.300     7f8dbd6a4740        INFO    stacktrace      src/common/stack_trace.cpp:158      [2] ./monerod() [0x764d43]
2017-02-28 20:04:14.300     7f8dbd6a4740        INFO    stacktrace      src/common/stack_trace.cpp:158      [3] ./monerod:cryptonote::tx_memory_pool::init(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&)+0x1e5 [0x670105]
2017-02-28 20:04:14.300     7f8dbd6a4740        INFO    stacktrace      src/common/stack_trace.cpp:158      [4] ./monerod:cryptonote::core::init(boost::program_options::variables_map const&, cryptonote::test_options const*)+0x1b7 [0x658d17]
2017-02-28 20:04:14.300     7f8dbd6a4740        INFO    stacktrace      src/common/stack_trace.cpp:158      [5] ./monerod:daemonize::t_daemon::run(bool)+0x1fe [0x5baa6e]
2017-02-28 20:04:14.300     7f8dbd6a4740        INFO    stacktrace      src/common/stack_trace.cpp:158      [6] ./monerod:main+0x191a [0x58282a]
2017-02-28 20:04:14.300     7f8dbd6a4740        INFO    stacktrace      src/common/stack_trace.cpp:158      [7] /lib/x86_64-linux-gnu/libc.so.6:__libc_start_main+0xf5 [0x7f8dbc9fab45]
2017-02-28 20:04:14.300     7f8dbd6a4740        INFO    stacktrace      src/common/stack_trace.cpp:158      [8] ./monerod:_start+0x29 [0x590509]
2017-02-28 20:04:14.300     7f8dbd6a4740        INFO    stacktrace      src/common/stack_trace.cpp:158
2017-02-28 20:04:14.306     7f8dbd6a4740        INFO    global  src/cryptonote_core/cryptonote_core.cpp:316     Loading blockchain from folder /home/yann/monero/bin/data/lmdb ...
2017-02-28 20:04:14.883     7f8dbc1d7700        INFO    stacktrace      src/common/stack_trace.cpp:119  Exception: boost::thread_interrupted
2017-02-28 20:04:14.883     7f8dbc1d7700        INFO    stacktrace      src/common/stack_trace.cpp:120  Unwound call stack:
2017-02-28 20:04:14.885     7f8dbc1d7700        INFO    stacktrace      src/common/stack_trace.cpp:158      [1] ./monerod:boost::this_thread::interruption_point()+0x74 [0x863424]
2017-02-28 20:04:14.885     7f8dbc1d7700        INFO    stacktrace      src/common/stack_trace.cpp:158      [2] ./monerod() [0x768904]
2017-02-28 20:04:14.885     7f8dbc1d7700        INFO    stacktrace      src/common/stack_trace.cpp:158      [3] ./monerod() [0x8635b5]
2017-02-28 20:04:14.885     7f8dbc1d7700        INFO    stacktrace      src/common/stack_trace.cpp:158      [4] /lib/x86_64-linux-gnu/libpthread.so.0+0x8064 [0x7f8dbcd8c064]
2017-02-28 20:04:14.885     7f8dbc1d7700        INFO    stacktrace      src/common/stack_trace.cpp:158      [5] /lib/x86_64-linux-gnu/libc.so.6:clone+0x6d [0x7f8dbcac162d]
2017-02-28 20:04:14.885     7f8dbc1d7700        INFO    stacktrace      src/common/stack_trace.cpp:158
2017-02-28 20:04:15.603     7f8dbb1d5700        INFO    stacktrace      src/common/stack_trace.cpp:119  Exception: boost::thread_interrupted
2017-02-28 20:04:15.603     7f8dbb1d5700        INFO    stacktrace      src/common/stack_trace.cpp:120  Unwound call stack:
2017-02-28 20:04:15.604     7f8dbb1d5700        INFO    stacktrace      src/common/stack_trace.cpp:158      [1] ./monerod:boost::this_thread::interruption_point()+0x74 [0x863424]
2017-02-28 20:04:15.604     7f8dbb1d5700        INFO    stacktrace      src/common/stack_trace.cpp:158      [2] ./monerod() [0x768904]
2017-02-28 20:04:15.604     7f8dbb1d5700        INFO    stacktrace      src/common/stack_trace.cpp:158      [3] ./monerod() [0x8635b5]
2017-02-28 20:04:15.604     7f8dbb1d5700        INFO    stacktrace      src/common/stack_trace.cpp:158      [4] /lib/x86_64-linux-gnu/libpthread.so.0+0x8064 [0x7f8dbcd8c064]
2017-02-28 20:04:15.605     7f8dbb1d5700        INFO    stacktrace      src/common/stack_trace.cpp:158      [5] /lib/x86_64-linux-gnu/libc.so.6:clone+0x6d [0x7f8dbcac162d]
2017-02-28 20:04:15.605     7f8dbb1d5700        INFO    stacktrace      src/common/stack_trace.cpp:158
2017-02-28 20:04:16.924     7f8dbc9d8700        INFO    stacktrace      src/common/stack_trace.cpp:119  Exception: boost::thread_interrupted
2017-02-28 20:04:16.924     7f8dbc9d8700        INFO    stacktrace      src/common/stack_trace.cpp:120  Unwound call stack:
2017-02-28 20:04:16.925     7f8dbc9d8700        INFO    stacktrace      src/common/stack_trace.cpp:158      [1] ./monerod:boost::this_thread::interruption_point()+0x74 [0x863424]
2017-02-28 20:04:16.925     7f8dbc9d8700        INFO    stacktrace      src/common/stack_trace.cpp:158      [2] ./monerod() [0x768904]
2017-02-28 20:04:16.925     7f8dbc9d8700        INFO    stacktrace      src/common/stack_trace.cpp:158      [3] ./monerod() [0x8635b5]
2017-02-28 20:04:16.925     7f8dbc9d8700        INFO    stacktrace      src/common/stack_trace.cpp:158      [4] /lib/x86_64-linux-gnu/libpthread.so.0+0x8064 [0x7f8dbcd8c064]
2017-02-28 20:04:16.925     7f8dbc9d8700        INFO    stacktrace      src/common/stack_trace.cpp:158      [5] /lib/x86_64-linux-gnu/libc.so.6:clone+0x6d [0x7f8dbcac162d]
2017-02-28 20:04:16.925     7f8dbc9d8700        INFO    stacktrace      src/common/stack_trace.cpp:158
2017-02-28 20:04:19.823     7f8dbd6a4740        WARN    net.dns src/common/dns_utils.cpp:529    WARNING: no two valid MoneroPulse DNS checkpoint records were received
2017-02-28 20:04:19.823     7f8dbd6a4740        INFO    global  src/daemon/core.h:78    Core initialized OK
2017-02-28 20:04:19.823     7f8dbd6a4740        INFO    global  src/daemon/rpc.h:68     Starting core rpc server...
2017-02-28 20:04:19.823 [SRV_MAIN]      INFO    global  src/daemon/rpc.h:73     Core rpc server started ok
2017-02-28 20:04:19.823 [SRV_MAIN]      INFO    global  src/daemon/p2p.h:78     Starting p2p net loop...
2017-02-28 20:04:20.824 [P2P1]  INFO    global  src/cryptonote_core/cryptonote_core.cpp:1065    ESC[1;33m
**********************************************************************
The daemon will start synchronizing with the network. It may take up to several hours.

You can set the level of process detailization* through "set_log <level|categories>" command*,
where <level> is between 0 (no details) and 4 (very verbose), or custom category based levels (eg, *:WARNING)

Use the "help" command to see the list of available commands.
**********************************************************************
ESC[0m
2017-02-28 20:04:20.826 [P2P1]  WARN    net.dns src/common/dns_utils.cpp:529    WARNING: no two valid MoneroPulse DNS checkpoint records were received
2017-02-28 20:04:20.907 [P2P2]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:293     [37.59.53.25:18080 OUT] Sync data returned a new top block candidate: 1256217 -> 1256226 [Your node is 9 blocks (0 days) behind]
SYNCHRONIZATION started
2017-02-28 20:04:22.163 [P2P3]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:995     ESC[1;33m[37.59.53.25:18080 OUT]  Synced 1256226/1256226ESC[0m
2017-02-28 20:04:22.163 [P2P3]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1090    ESC[1;32mSYNCHRONIZED OKESC[0m
2017-02-28 20:04:22.163 [P2P3]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1106    ESC[1;33m
**********************************************************************
You are now synchronized with the network. You may now start monero-wallet-cli.

Use the "help" command to see the list of available commands.
**********************************************************************ESC[0m
2017-02-28 20:04:35.639     7f8dbb9d6700        INFO    stacktrace      src/common/stack_trace.cpp:119  Exception: boost::thread_interrupted
2017-02-28 20:04:35.639     7f8dbb9d6700        INFO    stacktrace      src/common/stack_trace.cpp:120  Unwound call stack:
2017-02-28 20:04:35.640     7f8dbb9d6700        INFO    stacktrace      src/common/stack_trace.cpp:158      [1] ./monerod:boost::this_thread::interruption_point()+0x74 [0x863424]
2017-02-28 20:04:35.640     7f8dbb9d6700        INFO    stacktrace      src/common/stack_trace.cpp:158      [2] ./monerod() [0x768904]
2017-02-28 20:04:35.640     7f8dbb9d6700        INFO    stacktrace      src/common/stack_trace.cpp:158      [3] ./monerod() [0x8635b5]
2017-02-28 20:04:35.640     7f8dbb9d6700        INFO    stacktrace      src/common/stack_trace.cpp:158      [4] /lib/x86_64-linux-gnu/libpthread.so.0+0x8064 [0x7f8dbcd8c064]
2017-02-28 20:04:35.640     7f8dbb9d6700        INFO    stacktrace      src/common/stack_trace.cpp:158      [5] /lib/x86_64-linux-gnu/libc.so.6:clone+0x6d [0x7f8dbcac162d]
2017-02-28 20:04:35.640     7f8dbb9d6700        INFO    stacktrace      src/common/stack_trace.cpp:158
2017-02-28 20:28:00.912 [P2P9]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1090    ESC[1;32mSYNCHRONIZED OKESC[0m
2017-02-28 21:04:35.024 [P2P0]  WARN    net.cn  src/cryptonote_protocol/cryptonote_protocol_handler-base.cpp:125        RATE LIMIT NOT IMPLEMENTED HERE YET (download at unlimited speed?)
2017-02-28 21:04:35.610 [P2P1]  WARN    net.cn  src/cryptonote_protocol/cryptonote_protocol_handler-base.cpp:125        RATE LIMIT NOT IMPLEMENTED HERE YET (download at unlimited speed?)
2017-02-28 21:14:26.281 [P2P6]  WARN    net.dns src/common/dns_utils.cpp:529    WARNING: no two valid MoneroPulse DNS checkpoint records were received
2017-02-28 21:14:28.819 [P2P7]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:293     [141.84.69.94:57789 INC] Sync data returned a new top block candidate: 1256262 -> 1256264 [Your node is 2 blocks (0 days) behind]
SYNCHRONIZATION started
2017-02-28 21:14:31.905 [P2P8]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:995     ESC[1;33m[37.59.53.25:18080 OUT]  Synced 1256264/1256264ESC[0m
2017-02-28 21:14:31.905 [P2P8]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1090    ESC[1;32mSYNCHRONIZED OKESC[0m
2017-02-28 21:14:31.974 [P2P4]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1090    ESC[1;32mSYNCHRONIZED OKESC[0m
2017-02-28 21:14:32.043 [P2P5]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1090    ESC[1;32mSYNCHRONIZED OKESC[0m
2017-02-28 21:14:32.047 [P2P0]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1090    ESC[1;32mSYNCHRONIZED OKESC[0m
2017-02-28 21:14:32.051 [P2P1]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1090    ESC[1;32mSYNCHRONIZED OKESC[0m
2017-02-28 21:34:37.630 [P2P7]  WARN    net.cn  src/cryptonote_protocol/cryptonote_protocol_handler-base.cpp:125        RATE LIMIT NOT IMPLEMENTED HERE YET (download at unlimited speed?)
2017-02-28 21:34:38.336 [P2P0]  WARN    net.cn  src/cryptonote_protocol/cryptonote_protocol_handler-base.cpp:125        RATE LIMIT NOT IMPLEMENTED HERE YET (download at unlimited speed?)
2017-02-28 21:54:20.913 [P2P2]  WARN    net.cn  src/cryptonote_protocol/cryptonote_protocol_handler-base.cpp:125        RATE LIMIT NOT IMPLEMENTED HERE YET (download at unlimited speed?)
2017-02-28 21:54:21.190 [P2P8]  WARN    net.cn  src/cryptonote_protocol/cryptonote_protocol_handler-base.cpp:125        RATE LIMIT NOT IMPLEMENTED HERE YET (download at unlimited speed?)
2017-02-28 22:03:01.557 [P2P8]  WARN    net.cn  src/cryptonote_protocol/cryptonote_protocol_handler-base.cpp:125        RATE LIMIT NOT IMPLEMENTED HERE YET (download at unlimited speed?)
2017-02-28 22:03:02.070 [P2P7]  WARN    net.cn  src/cryptonote_protocol/cryptonote_protocol_handler-base.cpp:125        RATE LIMIT NOT IMPLEMENTED HERE YET (download at unlimited speed?)
2017-02-28 22:05:51.487 [P2P1]  WARN    net.cn  src/cryptonote_protocol/cryptonote_protocol_handler-base.cpp:125        RATE LIMIT NOT IMPLEMENTED HERE YET (download at unlimited speed?)
2017-02-28 22:05:51.998 [P2P6]  WARN    net.cn  src/cryptonote_protocol/cryptonote_protocol_handler-base.cpp:125        RATE LIMIT NOT IMPLEMENTED HERE YET (download at unlimited speed?)
2017-02-28 22:22:38.754 [P2P7]  WARN    net.dns src/common/dns_utils.cpp:529    WARNING: no two valid MoneroPulse DNS checkpoint records were received
2017-02-28 22:22:40.003 [P2P4]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:293     [176.9.47.243:54715 INC] Sync data returned a new top block candidate: 1256298 -> 1256304 [Your node is 6 blocks (0 days) behind]
SYNCHRONIZATION started
2017-02-28 22:22:46.481 [P2P2]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:293     [68.52.96.191:18080 OUT] Sync data returned a new top block candidate: 1256300 -> 1256308 [Your node is 8 blocks (0 days) behind]
SYNCHRONIZATION started
2017-02-28 22:22:47.695 [P2P2]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:995     ESC[1;33m[195.94.211.86:18080 OUT]  Synced 1256308/1256308ESC[0m
2017-02-28 22:22:47.695 [P2P2]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1090    ESC[1;32mSYNCHRONIZED OKESC[0m
2017-02-28 22:22:47.695 [P2P3]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1090    ESC[1;32mSYNCHRONIZED OKESC[0m
2017-02-28 23:32:23.736 [P2P7]  WARN    net.dns src/common/dns_utils.cpp:529    WARNING: no two valid MoneroPulse DNS checkpoint records were received
2017-02-28 23:32:24.520 [P2P1]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:293     [173.68.50.102:22402 INC] Sync data returned a new top block candidate: 1256342 -> 1256348 [Your node is 6 blocks (0 days) behind]
SYNCHRONIZATION started
2017-02-28 23:32:33.598 [P2P7]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:995     ESC[1;33m[107.150.61.138:18080 OUT]  Synced 1256348/1256348ESC[0m
2017-02-28 23:32:33.598 [P2P7]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1090    ESC[1;32mSYNCHRONIZED OKESC[0m
2017-02-28 23:32:33.735 [P2P3]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1090    ESC[1;32mSYNCHRONIZED OKESC[0m
2017-03-01 00:10:05.971 [P2P9]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:995     ESC[1;33m[178.254.34.122:18080 OUT]  Synced 1256362/1256362ESC[0m
2017-03-01 00:10:05.971 [P2P9]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1090    ESC[1;32mSYNCHRONIZED OKESC[0m
2017-03-01 00:10:05.971 [P2P0]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1090    ESC[1;32mSYNCHRONIZED OKESC[0m
2017-03-01 00:10:06.032 [P2P2]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1090    ESC[1;32mSYNCHRONIZED OKESC[0m
2017-03-01 00:10:06.405 [P2P8]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1090    ESC[1;32mSYNCHRONIZED OKESC[0m
2017-03-01 00:26:38.153 [P2P1]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1090    ESC[1;32mSYNCHRONIZED OKESC[0m
2017-03-01 00:26:38.154 [P2P9]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1090    ESC[1;32mSYNCHRONIZED OKESC[0m
2017-03-01 00:40:34.845 [P2P1]  WARN    net.dns src/common/dns_utils.cpp:529    WARNING: no two valid MoneroPulse DNS checkpoint records were received
2017-03-01 00:40:42.627 [P2P3]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:293     [124.160.224.29:18080 OUT] Sync data returned a new top block candidate: 1256378 -> 1256379 [Your node is 1 blocks (0 days) behind]
SYNCHRONIZATION started
2017-03-01 00:40:44.202 [P2P6]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:995     ESC[1;33m[73.92.194.234:18080 OUT]  Synced 1256379/1256379ESC[0m
2017-03-01 00:40:44.202 [P2P6]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1090    ESC[1;32mSYNCHRONIZED OKESC[0m
2017-03-01 00:40:45.486 [P2P6]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1090    ESC[1;32mSYNCHRONIZED OKESC[0m
2017-03-01 01:26:25.862 [P2P7]  INFO    global  src/cryptonote_core/blockchain.cpp:1420 ESC[1;34m----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT 1256398
id:     <19840d4a4d66c12078e5ea93d1cd6719c598a68bd6e4ac76b125aa08b7f8c638>
PoW:    <79f2d44b00655627fcbe185236f4860409eb6af1054ecf77970a775800000000>
difficulty:     7325908798ESC[0m
2017-03-01 01:49:55.031 [RPC0]  WARN    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:71   Failed to add tx blob to db transaction: MDB_KEYEXIST: Key/data pair already exists
2017-03-01 01:49:55.031 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:119  Exception: cryptonote::DB_ERROR
2017-03-01 01:49:55.031 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:120  Unwound call stack:
2017-03-01 01:49:55.036 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:158      [1] ./monerod() [0x74c46f]
2017-03-01 01:49:55.036 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:158      [2] ./monerod:cryptonote::BlockchainLMDB::add_transaction_data(crypto::hash const&, cryptonote::transaction const&, crypto::hash const&)+0x433 [0x721793]
2017-03-01 01:49:55.036 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:158      [3] ./monerod:cryptonote::BlockchainDB::add_transaction(crypto::hash const&, cryptonote::transaction const&, crypto::hash const*)+0x144 [0x6af1c4]
2017-03-01 01:49:55.036 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:158      [4] ./monerod:cryptonote::BlockchainDB::add_block(cryptonote::block const&, unsigned long const&, unsigned long const&, unsigned long const&, std::vector<cryptonote::transaction, std::allocator<cryptonote::transaction> > const&)+0x11e [0x6af89e]
2017-03-01 01:49:55.036 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:158      [5] ./monerod:cryptonote::BlockchainLMDB::add_block(cryptonote::block const&, unsigned long const&, unsigned long const&, unsigned long const&, std::vector<cryptonote::transaction, std::allocator<cryptonote::transaction> > const&)+0x12f [0x6fe18f]
2017-03-01 01:49:55.036 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:158      [6] ./monerod:cryptonote::Blockchain::handle_block_to_main_chain(cryptonote::block const&, crypto::hash const&, cryptonote::block_verification_context&)+0x1b43 [0x664a33]
2017-03-01 01:49:55.036 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:158      [7] ./monerod:cryptonote::Blockchain::add_new_block(cryptonote::block const&, cryptonote::block_verification_context&)+0x312 [0x6661c2]
2017-03-01 01:49:55.036 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:158      [8] ./monerod:cryptonote::core::handle_block_found(cryptonote::block&)+0x5a [0x67b3aa]
2017-03-01 01:49:55.036 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:158      [9] ./monerod:cryptonote::core_rpc_server::on_submitblock(std::vector<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::allocator<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > const&, cryptonote::COMMAND_RPC_SUBMITBLOCK::response&, epee::json_rpc::error&)+0x1c4 [0x696484]
2017-03-01 01:49:55.036 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:158      [10] ./monerod() [0x5f03b1]
2017-03-01 01:49:55.036 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:158      [11] ./monerod() [0x5b1c93]
2017-03-01 01:49:55.036 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:158      [12] ./monerod() [0x63d5f2]
2017-03-01 01:49:55.036 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:158      [13] ./monerod() [0x60d23a]
2017-03-01 01:49:55.036 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:158      [14] ./monerod() [0x60ecd3]
2017-03-01 01:49:55.036 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:158      [15] ./monerod() [0x610837]
2017-03-01 01:49:55.036 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:158      [16] ./monerod:epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::handle_read(boost::system::error_code const&, unsigned long)+0x1ae [0x610a2e]
2017-03-01 01:49:55.036 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:158      [17] ./monerod() [0x624135]
2017-03-01 01:49:55.036 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:158      [18] ./monerod:boost::asio::detail::completion_handler<boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>, boost::system::error_code, unsigned long>, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> > > >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long)+0x118 [0x625548]
2017-03-01 01:49:55.036 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:158      [19] ./monerod:boost::asio::detail::reactive_socket_recv_op<boost::asio::mutable_buffers_1, boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running> >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long)+0x4b4 [0x60c9b4]
2017-03-01 01:49:55.036 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:158      [20] ./monerod() [0x752194]
2017-03-01 01:49:55.036 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:158      [21] ./monerod:epee::net_utils::boosted_tcp_server<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::worker_thread()+0x14f [0x5d354f]
2017-03-01 01:49:55.036 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:158      [22] ./monerod() [0x8635b5]
2017-03-01 01:49:55.036 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:158      [23] /lib/x86_64-linux-gnu/libpthread.so.0+0x8064 [0x7f8dbcd8c064]
2017-03-01 01:49:55.036 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:158      [24] /lib/x86_64-linux-gnu/libc.so.6:clone+0x6d [0x7f8dbcac162d]
2017-03-01 01:49:55.036 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:158
2017-03-01 01:49:55.036 [RPC0]  ERROR   blockchain      src/cryptonote_core/blockchain.cpp:3360 Error adding block with hash: <250f6f7414b54801110d5afc36ce93444d3ddbc7052b0f35143b9a82250f76da> to blockchain, what = Failed to add tx blob to db transaction: MDB_KEYEXIST: Key/data pair already exists
2017-03-01 01:50:33.578 [P2P3]  WARN    net.dns src/common/dns_utils.cpp:529    WARNING: no two valid MoneroPulse DNS checkpoint records were received
2017-03-01 01:50:33.613 [P2P3]  ERROR   blockchain      src/cryptonote_core/blockchain.cpp:3224 Block with id: <917c69773fc9ebc5b1d323aa583d2169975bf4ad4d7ef908afdbd5bb2329821d> attempting to add transaction already in blockchain with id: <17dec213fb69542ff317bcd06d6a127a95232dd322eb284ebced0e8c331ce1da>
2017-03-01 01:50:33.613 [P2P3]  WARN    net.cn  src/cryptonote_protocol/cryptonote_protocol_handler.inl:352     [195.154.169.129:46604 INC] Block verification failed, dropping connection
2017-03-01 01:50:33.644 [P2P3]  ERROR   blockchain      src/cryptonote_core/blockchain.cpp:3224 Block with id: <917c69773fc9ebc5b1d323aa583d2169975bf4ad4d7ef908afdbd5bb2329821d> attempting to add transaction already in blockchain with id: <17dec213fb69542ff317bcd06d6a127a95232dd322eb284ebced0e8c331ce1da>
2017-03-01 01:50:33.644 [P2P3]  WARN    net.cn  src/cryptonote_protocol/cryptonote_protocol_handler.inl:352     [176.9.47.243:44933 INC] Block verification failed, dropping connection
2017-03-01 01:50:34.173 [P2P7]  ERROR   blockchain      src/cryptonote_core/blockchain.cpp:3224 Block with id: <917c69773fc9ebc5b1d323aa583d2169975bf4ad4d7ef908afdbd5bb2329821d> attempting to add transaction already in blockchain with id: <17dec213fb69542ff317bcd06d6a127a95232dd322eb284ebced0e8c331ce1da>
2017-03-01 01:50:34.173 [P2P7]  WARN    net.cn  src/cryptonote_protocol/cryptonote_protocol_handler.inl:352     [88.126.142.198:33482 INC] Block verification failed, dropping connection
2017-03-01 01:50:34.175 [P2P7]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:293     [31.10.150.55:10140 INC] Sync data returned a new top block candidate: 1256404 -> 1256406 [Your node is 2 blocks (0 days) behind]
SYNCHRONIZATION started
2017-03-01 01:50:34.209 [P2P7]  ERROR   blockchain      src/cryptonote_core/blockchain.cpp:3224 Block with id: <917c69773fc9ebc5b1d323aa583d2169975bf4ad4d7ef908afdbd5bb2329821d> attempting to add transaction already in blockchain with id: <17dec213fb69542ff317bcd06d6a127a95232dd322eb284ebced0e8c331ce1da>
2017-03-01 01:50:34.209 [P2P7]  WARN    net.cn  src/cryptonote_protocol/cryptonote_protocol_handler.inl:352     [76.76.69.154:18080 OUT] Block verification failed, dropping connection
2017-03-01 01:50:34.239 [P2P7]  ERROR   blockchain      src/cryptonote_core/blockchain.cpp:3224 Block with id: <917c69773fc9ebc5b1d323aa583d2169975bf4ad4d7ef908afdbd5bb2329821d> attempting to add transaction already in blockchain with id: <17dec213fb69542ff317bcd06d6a127a95232dd322eb284ebced0e8c331ce1da>
2017-03-01 01:50:34.239 [P2P7]  WARN    net.cn  src/cryptonote_protocol/cryptonote_protocol_handler.inl:352     [54.86.143.72:18080 OUT] Block verification failed, dropping connection
2017-03-01 01:50:35.178 [P2P6]  ERROR   blockchain      src/cryptonote_core/blockchain.cpp:3224 Block with id: <917c69773fc9ebc5b1d323aa583d2169975bf4ad4d7ef908afdbd5bb2329821d> attempting to add transaction already in blockchain with id: <17dec213fb69542ff317bcd06d6a127a95232dd322eb284ebced0e8c331ce1da>
2017-03-01 01:50:35.179 [P2P6]  WARN    net.cn  src/cryptonote_protocol/cryptonote_protocol_handler.inl:352     [81.141.129.187:63209 INC] Block verification failed, dropping connection
2017-03-01 01:50:36.182 [P2P4]  ERROR   blockchain      src/cryptonote_core/blockchain.cpp:3224 Block with id: <917c69773fc9ebc5b1d323aa583d2169975bf4ad4d7ef908afdbd5bb2329821d> attempting to add transaction already in blockchain with id: <17dec213fb69542ff317bcd06d6a127a95232dd322eb284ebced0e8c331ce1da>
2017-03-01 01:50:36.183 [P2P4]  WARN    net.cn  src/cryptonote_protocol/cryptonote_protocol_handler.inl:352     [73.92.194.234:18080 OUT] Block verification failed, dropping connection

```

# Discussion History
## moneromooo-monero | 2017-03-01T09:37:11+00:00
You can try:

monero-blockchain-import --pop-blocks 100

Then start daemon again. A bit of a long shot, so it it still doesn't work you'll have to resync the blockchain. It's a fair bit faster with current master though :)

It's possibly linked to an off by one that was in the code for a week or two. Were you running a version from beween 15 january and and 11 february ?

## moneromooo-monero | 2017-03-01T09:37:43+00:00
Actually, please wait before popping blocks, hyc might want to ask something about the current database. I will ask.

## assylias | 2017-03-01T10:35:04+00:00
I have only been using the release versions: 0.10.1.1 since December and 0.10.2.1 since last night.

## assylias | 2017-03-01T11:23:36+00:00
@moneromooo-monero FYI I've tried to use an older blockchain backup (after saving the corrupted db) and I'm getting lots of errors like below. Not sure if it's related or not. It looks like it may be safer to rebuild the chain from scratch.

```
2017-03-01 11:18:12.345 [RPC1]  ERROR   verify  src/cryptonote_core/blockchain.cpp:2933 One of outputs for one of inputs has wrong tx.unlock_time = 1248840
2017-03-01 11:18:12.345 [RPC1]  ERROR   verify  src/cryptonote_core/blockchain.cpp:232  Failed to handle_output for output no = 2, with absolute offset 210363
2017-03-01 11:18:12.345 [RPC1]  ERROR   verify  src/cryptonote_core/blockchain.cpp:2953 Failed to get output keys for tx with amount = 0.000000000000 and count indexes 3
2017-03-01 11:18:12.345 [RPC1]  ERROR   verify  src/cryptonote_core/blockchain.cpp:2576 Failed to check ring signature for tx <87a34151cf111fac07c28c101a8a0d5cfcf567f50a22a78da34663cf386de428>  vin key with k_image: <d1e0158f39493148ad2c5a3642135e42167192ed7e2195abe939907f31b13805>  sig_index: 1
2017-03-01 11:18:12.345 [RPC1]  ERROR   verify  src/cryptonote_core/blockchain.cpp:2579   *pmax_used_block_height: 1248327
2017-03-01 11:18:13.674 [P2P5]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:293     [184.57.118.204:54538 INC] Sync data returned a new top block candidate: 1248816 -> 1256658 [Your node is 7842 blocks (10 days) behind]
SYNCHRONIZATION started
2017-03-01 11:18:15.674 [P2P5]  WARN    net.p2p src/p2p/net_node.inl:1399       [0.0.0.0:0 OUT] back ping connect failed to 184.57.118.204:18080
2017-03-01 11:18:16.626 [P2P5]  ERROR   net.p2p src/p2p/net_node.inl:1461       [23.250.10.250:60380 INC] COMMAND_REQUEST_SUPPORT_FLAGS invoke failed. (-6, LEVIN_ERROR_CONNECTION_HANDLER_NOT_DEFINED)
2017-03-01 11:18:17.822 [P2P5]  WARN    net.cn  src/cryptonote_protocol/cryptonote_protocol_handler-base.cpp:125        RATE LIMIT NOT IMPLEMENTED HERE YET (download at unlimited speed?)
```

## moneromooo-monero | 2017-03-01T14:23:38+00:00
hyc is away for the next few days, but asked to please keep the old blockchain db around so he can get to it when he's back.

## moneromooo-monero | 2017-03-02T11:44:02+00:00
If you kept the db, could you please run the following, and paste the results, please ?

mdb_stat -a /path/to.lmdb

Replace /path/to/lmdb with the actual path to where your saved up data.mdb is (without the data.mdb filename, just the directory).


## assylias | 2017-03-02T11:59:13+00:00
Database that got corrupted:

```
Status of Main DB
  Tree depth: 1
  Branch pages: 0
  Leaf pages: 1
  Overflow pages: 0
  Entries: 11
Status of block_heights
  Tree depth: 1
  Branch pages: 0
  Leaf pages: 1
  Overflow pages: 0
  Entries: 1256404
Status of block_info
  Tree depth: 1
  Branch pages: 0
  Leaf pages: 1
  Overflow pages: 0
  Entries: 1256404
Status of blocks
  Tree depth: 4
  Branch pages: 455
  Leaf pages: 101973
  Overflow pages: 34
  Entries: 1256404
Status of hf_versions
  Tree depth: 3
  Branch pages: 29
  Leaf pages: 6159
  Overflow pages: 0
  Entries: 1256404
Status of output_amounts
  Tree depth: 4
  Branch pages: 530
  Leaf pages: 80661
  Overflow pages: 0
  Entries: 22123813
Status of output_txs
  Tree depth: 1
  Branch pages: 0
  Leaf pages: 1
  Overflow pages: 0
  Entries: 22123813
Status of properties
  Tree depth: 1
  Branch pages: 0
  Leaf pages: 1
  Overflow pages: 0
  Entries: 1
Status of spent_keys
  Tree depth: 1
  Branch pages: 0
  Leaf pages: 1
  Overflow pages: 0
  Entries: 18597181
Status of tx_indices
  Tree depth: 1
  Branch pages: 0
  Leaf pages: 1
  Overflow pages: 0
  Entries: 2270751
Status of tx_outputs
  Tree depth: 4
  Branch pages: 243
  Leaf pages: 54182
  Overflow pages: 2383
  Entries: 2270750
Status of txs
  Tree depth: 4
  Branch pages: 1032
  Leaf pages: 231699
  Overflow pages: 1480625
  Entries: 2270750

```

Database when I tried rebuilding the blockchain from a backup:

```
Status of Main DB
  Tree depth: 1
  Branch pages: 0
  Leaf pages: 1
  Overflow pages: 0
  Entries: 11
Status of block_heights
  Tree depth: 1
  Branch pages: 0
  Leaf pages: 1
  Overflow pages: 0
  Entries: 889752
Status of block_info
  Tree depth: 1
  Branch pages: 0
  Leaf pages: 1
  Overflow pages: 0
  Entries: 889752
Status of blocks
  Tree depth: 4
  Branch pages: 319
  Leaf pages: 71241
  Overflow pages: 5
  Entries: 889752
Status of hf_versions
  Tree depth: 3
  Branch pages: 21
  Leaf pages: 4362
  Overflow pages: 0
  Entries: 889752
Status of output_amounts
  Tree depth: 4
  Branch pages: 503
  Leaf pages: 75768
  Overflow pages: 0
  Entries: 15779452
Status of output_txs
  Tree depth: 1
  Branch pages: 0
  Leaf pages: 1
  Overflow pages: 0
  Entries: 15779452
Status of properties
  Tree depth: 1
  Branch pages: 0
  Leaf pages: 1
  Overflow pages: 0
  Entries: 1
Status of spent_keys
  Tree depth: 1
  Branch pages: 0
  Leaf pages: 1
  Overflow pages: 0
  Entries: 12962100
Status of tx_indices
  Tree depth: 1
  Branch pages: 0
  Leaf pages: 1
  Overflow pages: 0
  Entries: 1413381
Status of tx_outputs
  Tree depth: 3
  Branch pages: 168
  Leaf pages: 37663
  Overflow pages: 2382
  Entries: 1413381
Status of txs
  Tree depth: 4
  Branch pages: 574
  Leaf pages: 128662
  Overflow pages: 604270
  Entries: 1413381

```

## moneromooo-monero | 2017-03-02T12:01:32+00:00
Thank you, tx_indices has one more entry than it should, good lead :)

## moneromooo-monero | 2017-03-02T18:53:47+00:00
I can't find the bug so far. A good way to recover, if you haven't already resynced, is to export (using monero-blockchain-export) and reimport with verification off. Since the problem is a dangling record in the database, it will not be part of the export/import, and you'll end up with an equivalent db without that dangling record. It'd be helpful if you could run monerod with log level 1 in case you get it again :)

## siculars | 2017-03-04T21:49:23+00:00
I'm coming across this issue... what should I do?

Monero 'Wolfram Warptangent' (v0.10.2.0-release)

2017-03-04 11:49:18.939	[P2P2]	INFO 	global	src/cryptonote_core/blockchain.cpp:1420	----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT 1258981
id:	<1bdd5a1330c0157c9e66e8428075495dff30eb98105efcbe22ec4917ad8d6d9a>
PoW:	<6a33fd089379c403610e39cda6cbd2b70728e75914207f9f8992347900000000>
difficulty:	6590332010
2017-03-04 11:49:18.939	[P2P2]	WARN 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:2423	WARNING: batch transaction mode already enabled, but asked to enable batch mode
2017-03-04 11:49:18.977	[P2P2]	INFO 	global	src/cryptonote_core/blockchain.cpp:884	REORGANIZE SUCCESS! on height: 1258981, new blockchain size: 1258983
2017-03-04 11:49:18.993	[P2P2]	WARN 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:71	Failed to add tx blob to db transaction: MDB_KEYEXIST: Key/data pair already exists
2017-03-04 11:49:19.000	[P2P2]	ERROR	blockchain	src/cryptonote_core/blockchain.cpp:3360	Error adding block with hash: <95a731ac022629bbcec200ab41eef369de880ed165a61ecee5063ee152389302> to blockchain, what = Failed to add tx blob to db transaction: MDB_KEYEXIST: Key/data pair already exists
2017-03-04 11:49:19.016	[P2P5]	ERROR	blockchain	src/cryptonote_core/blockchain.cpp:3224	Block with id: <95a731ac022629bbcec200ab41eef369de880ed165a61ecee5063ee152389302> attempting to add transaction already in blockchain with id: <bf5046d75de2841ac6f85e4dc3f787abe25f9fd5cf149dc532c18759402dd74e>
2017-03-04 11:49:19.035	[P2P5]	WARN 	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:350	[185.31.136.69:18080 OUT] Block verification failed, dropping connection
2017-03-04 11:49:20.118	[P2P3]	ERROR	blockchain	src/cryptonote_core/blockchain.cpp:3224	Block with id: <95a731ac022629bbcec200ab41eef369de880ed165a61ecee5063ee152389302> attempting to add transaction already in blockchain with id: <bf5046d75de2841ac6f85e4dc3f787abe25f9fd5cf149dc532c18759402dd74e>

...
2017-03-04 15:28:18.650	[P2P6]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:291	[174.61.169.23:18080 OUT] Sync data returned a new top block candidate: 1258983 -> 1259102 [Your node is 119 blocks (0 days) behind] 
SYNCHRONIZATION started
2017-03-04 15:28:33.431	[P2P3]	ERROR	blockchain	src/cryptonote_core/blockchain.cpp:3224	Block with id: <95a731ac022629bbcec200ab41eef369de880ed165a61ecee5063ee152389302> attempting to add transaction already in blockchain with id: <bf5046d75de2841ac6f85e4dc3f787abe25f9fd5cf149dc532c18759402dd74e>
2017-03-04 15:28:33.431	[P2P3]	INFO 	global	src/p2p/net_node.inl:249	IP 174.61.169.23 blocked.
2017-03-04 15:29:06.079	[P2P7]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:291	[72.234.154.162:18080 OUT] Sync data returned a new top block candidate: 1258983 -> 1259103 [Your node is 120 blocks (0 days) behind] 
SYNCHRONIZATION started

2017-03-04 15:47:33.104	[P2P9]	ERROR	blockchain	src/cryptonote_core/blockchain.cpp:3224	Block with id: <95a731ac022629bbcec200ab41eef369de880ed165a61ecee5063ee152389302> attempting to add transaction already in blockchain with id: <bf5046d75de2841ac6f85e4dc3f787abe25f9fd5cf149dc532c18759402dd74e>
2017-03-04 15:47:42.460	[P2P0]	ERROR	blockchain	src/cryptonote_core/blockchain.cpp:3224	Block with id: <95a731ac022629bbcec200ab41eef369de880ed165a61ecee5063ee152389302> attempting to add transaction already in blockchain with id: <bf5046d75de2841ac6f85e4dc3f787abe25f9fd5cf149dc532c18759402dd74e>

status
Height: 1258983/1259110 (99.9%) on mainnet, not mining, net hash 54.51 MH/s, v4, up to date, 6(out)+0(in) connections, uptime 5d 21h 43m 21s



## hyc | 2017-03-06T08:52:30+00:00
For the record, this is fixed in git master and the fix will be in the next point release which should be coming out today. In the meantime, you will need to dump and reload your blockchain DB.
use monero-blockchain-export then delete your ~/.bitmonero/lmdb/data.mdb file. Then reimport, using monero-blockchain-import --verify 0 --database lmdb#nosync


## ghost | 2017-03-06T09:19:51+00:00
@hyc Is it worth having 'dump and reload' functionality documented in the README? Or maybe as a small emergency recovery utility?

Perhaps even worth combining the blockchain-import and blockchain-export programs into a single utility and add this extra functionality?

## hyc | 2017-03-06T09:39:47+00:00
IMO import/export should have just been built into monerod. It would have made migration to the new DB layout a lot easier too. I would hope we don't need dump/reload often enough to warrant a dedicated utility though.


# Action History
- Created by: assylias | 2017-03-01T07:36:18+00:00
- Closed at: 2017-03-03T16:57:17+00:00
