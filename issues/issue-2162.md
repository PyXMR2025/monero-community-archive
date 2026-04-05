---
title: Building in Termux fails
source_url: https://github.com/xmrig/xmrig/issues/2162
author: NetherStar64
assignees: []
labels: []
created_at: '2021-03-07T16:22:38+00:00'
updated_at: '2021-04-12T14:05:25+00:00'
type: issue
status: closed
closed_at: '2021-04-12T14:05:25+00:00'
---

# Original Description
Building from Termux fails with ```[100%] Linking CXX executable xmrig                                              /data/data/com.termux/files/usr/bin/ld: ../scripts/deps/lib/libuv.a(libuv_la-process.o): in function `uv__process_child_init':                                    /data/data/com.termux/files/home/xmrig/scripts/build/libuv-1.40.0/src/unix/process.c:394: undefined reference to `uv__pthread_sigmask'                            /data/data/com.termux/files/usr/bin/ld: ../scripts/deps/lib/libuv.a(libuv_la-signal.o): in function `uv__signal_unlock_and_unblock':                              /data/data/com.termux/files/home/xmrig/scripts/build/libuv-1.40.0/src/unix/signal.c:160: undefined reference to `uv__pthread_sigmask'                             /data/data/com.termux/files/usr/bin/ld: /data/data/com.termux/files/home/xmrig/scripts/build/libuv-1.40.0/src/unix/signal.c:160: undefined reference to `uv__pthread_sigmask'                                                                      /data/data/com.termux/files/usr/bin/ld: /data/data/com.termux/files/home/xmrig/scripts/build/libuv-1.40.0/src/unix/signal.c:160: undefined reference to `uv__pthread_sigmask'                                                                      /data/data/com.termux/files/usr/bin/ld: ../scripts/deps/lib/libuv.a(libuv_la-signal.o): in function `uv__signal_block_and_lock':                                  /data/data/com.termux/files/home/xmrig/scripts/build/libuv-1.40.0/src/unix/signal.c:148: undefined reference to `uv__pthread_sigmask'                             /data/data/com.termux/files/usr/bin/ld: ../scripts/deps/lib/libuv.a(libuv_la-linux-core.o):/data/data/com.termux/files/home/xmrig/scripts/build/libuv-1.40.0/src/unix/linux-core.c:310: more undefined references to `uv__pthread_sigmask' follow  clang-11: error: linker command failed with exit code 1 (use -v to see invocation)                                                                                make[2]: *** [CMakeFiles/xmrig.dir/build.make:3379: xmrig] Error 1               make[1]: *** [CMakeFiles/Makefile2:137: CMakeFiles/xmrig.dir/all] Error 2        make: *** [Makefile:103: all] Error 2 ```


Compiled with scripts/build_deps.sh

# Discussion History
## xmrig | 2021-04-12T14:05:25+00:00
To build your own libuv for Termux you need to apply some patches https://github.com/termux/termux-packages/tree/master/packages/libuv.
Thank you.

# Action History
- Created by: NetherStar64 | 2021-03-07T16:22:38+00:00
- Closed at: 2021-04-12T14:05:25+00:00
