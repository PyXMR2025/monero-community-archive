---
title: Random stack traces in log
source_url: https://github.com/monero-project/monero/issues/6447
author: moroznah
assignees: []
labels: []
created_at: '2020-04-13T12:07:04+00:00'
updated_at: '2020-04-13T15:30:02+00:00'
type: issue
status: closed
closed_at: '2020-04-13T15:30:01+00:00'
---

# Original Description
The daemon runs and relays transactions fine. 
Config contains just two lines:
out-peers=16
in-peers=16

However, it keeps generating stack traces. I was trying to find source of the issue, however there are no patterns with any external actions, looks random to me.
Daemon is compiled from source, latest release. I also removed all additional CFLAGS in hopes that it's graphite/lto related without any luck, same stack traces with stock flags.
My system is Gentoo hardened, with selinux not enforcing during testing.

>...
gcc -v
Using built-in specs.
COLLECT_GCC=gcc
COLLECT_LTO_WRAPPER=/usr/libexec/gcc/x86_64-pc-linux-gnu/9.2.0/lto-wrapper
Target: x86_64-pc-linux-gnu
Configured with: /var/tmp/portage/sys-devel/gcc-9.2.0-r2/work/gcc-9.2.0/configure --host=x86_64-pc-linux-gnu --build=x86_64-pc-linux-gnu --prefix=/usr --bindir=/usr/x86_64-pc-linux-gnu/gcc-bin/9.2.0 --includedir=/usr/lib/gcc/x86_64-pc-linux-gnu/9.2.0/include --datadir=/usr/share/gcc-data/x86_64-pc-linux-gnu/9.2.0 --mandir=/usr/share/gcc-data/x86_64-pc-linux-gnu/9.2.0/man --infodir=/usr/share/gcc-data/x86_64-pc-linux-gnu/9.2.0/info --with-gxx-include-dir=/usr/lib/gcc/x86_64-pc-linux-gnu/9.2.0/include/g++-v9 --with-python-dir=/share/gcc-data/x86_64-pc-linux-gnu/9.2.0/python --enable-languages=c,c++ --enable-obsolete --enable-secureplt --disable-werror --with-system-zlib --enable-nls --without-included-gettext --enable-checking=release --with-bugurl=https://bugs.gentoo.org/ --with-pkgversion='Gentoo Hardened 9.2.0-r2 p3' --enable-esp --enable-libstdcxx-time --with-build-config=bootstrap-lto --disable-libstdcxx-pch --enable-shared --enable-threads=posix --enable-__cxa_atexit --enable-clocale=gnu --disable-multilib --with-multilib-list=m64 --disable-altivec --disable-fixed-point --enable-targets=all --enable-libgomp --disable-libmudflap --disable-libssp --disable-libada --disable-systemtap --enable-vtable-verify --disable-libquadmath --enable-lto --with-isl --disable-isl-version-check --enable-default-pie --enable-default-ssp
Thread model: posix
gcc version 9.2.0 (Gentoo Hardened 9.2.0-r2 p3) 
monerod status
2020-04-13 11:51:28.157	I Monero 'Carbon Chamaeleon' (v0.15.0.5-17ec003c0)
2020-04-13 11:51:28.159	I Generating SSL certificate
Height: 2075802/2075802 (100.0%) on mainnet, not mining, net hash 1.29 GH/s, v12, up to date, 16(out)+0(in) connections, uptime 0d 0h 8m 28s
>

Stack traces:
>...
2020-04-13 11:43:01.463	    7a8617952a00	INFO	global	src/daemon/main.cpp:271	Monero 'Carbon Chamaeleon' (v0.15.0.5-17ec003c0)
2020-04-13 11:43:01.463	    7a8617952a00	INFO	msgwriter	src/common/scoped_message_writer.h:102	Forking to background...
2020-04-13 11:43:01.471	    7a8617952a00	WARNING	daemon	src/daemon/executor.cpp:61	Monero 'Carbon Chamaeleon' (v0.15.0.5-17ec003c0) Daemonised
2020-04-13 11:43:01.472	    7a8617952a00	INFO	global	src/daemon/protocol.h:53	Initializing cryptonote protocol...
2020-04-13 11:43:01.472	    7a8617952a00	INFO	global	src/daemon/protocol.h:58	Cryptonote protocol initialized OK
2020-04-13 11:43:01.476	    7a8617952a00	INFO	global	src/daemon/core.h:63	Initializing core...
2020-04-13 11:43:01.478	    7a8617952a00	INFO	global	src/cryptonote_core/cryptonote_core.cpp:506	Loading blockchain from folder /home/monerod/lmdb ...
2020-04-13 11:43:02.948	    7a8617952a00	INFO	global	src/cryptonote_core/cryptonote_core.cpp:668	Loading checkpoints
2020-04-13 11:43:03.970	    7a8617952a00	INFO	global	src/daemon/core.h:73	Core initialized OK
2020-04-13 11:43:03.970	    7a8617952a00	INFO	global	src/daemon/p2p.h:63	Initializing p2p server...
2020-04-13 11:43:04.819	    7a8617952a00	INFO	global	src/daemon/p2p.h:68	p2p server initialized OK
2020-04-13 11:43:04.820	    7a8617952a00	INFO	global	src/daemon/rpc.h:62	Initializing core RPC server...
2020-04-13 11:43:04.821	    7a8617952a00	INFO	global	contrib/epee/include/net/http_server_impl_base.h:79	Binding on 127.0.0.1 (IPv4):18081
2020-04-13 11:43:04.823	    7a8617952a00	INFO	global	contrib/epee/src/net_ssl.cpp:127	Generating SSL certificate
2020-04-13 11:43:05.780	    7a8617952a00	INFO	global	src/daemon/rpc.h:68	core RPC server initialized OK on port: 18081
2020-04-13 11:43:05.780	    7a8617952a00	INFO	global	src/daemon/rpc.h:73	Starting core RPC server...
2020-04-13 11:43:05.780	[SRV_MAIN]	INFO	global	src/daemon/rpc.h:78	core RPC server started ok
2020-04-13 11:43:05.784	[SRV_MAIN]	INFO	global	src/daemon/p2p.h:78	Starting p2p net loop...
2020-04-13 11:43:06.784	[P2P2]	INFO	global	src/cryptonote_core/cryptonote_core.cpp:1636	
2020-04-13 11:43:06.785	[P2P2]	INFO	global	src/cryptonote_core/cryptonote_core.cpp:1636	**********************************************************************
2020-04-13 11:43:06.785	[P2P2]	INFO	global	src/cryptonote_core/cryptonote_core.cpp:1636	The daemon will start synchronizing with the network. This may take a long time to complete.
2020-04-13 11:43:06.785	[P2P2]	INFO	global	src/cryptonote_core/cryptonote_core.cpp:1636	
2020-04-13 11:43:06.785	[P2P2]	INFO	global	src/cryptonote_core/cryptonote_core.cpp:1636	You can set the level of process detailization through "set_log <level|categories>" command,
2020-04-13 11:43:06.785	[P2P2]	INFO	global	src/cryptonote_core/cryptonote_core.cpp:1636	where <level> is between 0 (no details) and 4 (very verbose), or custom category based levels (eg, *:WARNING).
2020-04-13 11:43:06.785	[P2P2]	INFO	global	src/cryptonote_core/cryptonote_core.cpp:1636	
2020-04-13 11:43:06.785	[P2P2]	INFO	global	src/cryptonote_core/cryptonote_core.cpp:1636	Use the "help" command to see the list of available commands.
2020-04-13 11:43:06.785	[P2P2]	INFO	global	src/cryptonote_core/cryptonote_core.cpp:1636	Use "help <command>" to see a command's documentation.
2020-04-13 11:43:06.785	[P2P2]	INFO	global	src/cryptonote_core/cryptonote_core.cpp:1636	**********************************************************************
2020-04-13 11:43:07.681	[P2P3]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:371	[70.183.53.16:18080 OUT] Sync data returned a new top block candidate: 2075797 -> 2075799 [Your node is 2 blocks (0 days) behind] 
2020-04-13 11:43:07.681	[P2P3]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:371	SYNCHRONIZATION started
2020-04-13 11:43:08.216	    7a6fab0a9700	INFO	stacktrace	src/common/stack_trace.cpp:133	Exception: std::runtime_error
2020-04-13 11:43:08.216	    7a6fab0a9700	INFO	stacktrace	src/common/stack_trace.cpp:134	Unwound call stack:
2020-04-13 11:43:08.224	    7a6fab0a9700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [1]  0x126) [0x619aa86a638d]:__cxa_throw+0x126) [0x619aa86a638d]
2020-04-13 11:43:08.224	    7a6fab0a9700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [2] /usr/bin/monerod(+0x35b786) [0x619aa86ec786] 
2020-04-13 11:43:08.224	    7a6fab0a9700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [3]  0x203) [0x619aa8d621e3]:_alloc_cache+0x203) [0x619aa8d621e3]
2020-04-13 11:43:08.224	    7a6fab0a9700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [4]  0x351) [0x619aa8bb5811]:_slow_hash+0x351) [0x619aa8bb5811]
2020-04-13 11:43:08.224	    7a6fab0a9700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [5]  0xe9) [0x619aa8b9c7e9]:_ZN10cryptonote18get_block_longhashEPKNS_10BlockchainERKNS_5blockERN6crypto4hashEmi+0xe9) [0x619aa8b9c7e9]
2020-04-13 11:43:08.224	    7a6fab0a9700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [6]  0x24) [0x619aa8b9c9c4]:_ZN10cryptonote18get_block_longhashEPKNS_10BlockchainERKNS_5blockEmi+0x24) [0x619aa8b9c9c4]
2020-04-13 11:43:08.224	    7a6fab0a9700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [7]  0xc7) [0x619aa8b3d467]:_ZNK10cryptonote10Blockchain21block_longhash_workerEmRKN4epee4spanIKNS_5blockEEERSt13unordered_mapIN6crypto4hashESA_St4hashISA_ESt8equal_toISA_ESaISt4pairIKSA_SA_EEE+0xc7) [0x619aa8b3d467]
2020-04-13 11:43:08.224	    7a6fab0a9700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [8]  0x492) [0x619aa8bfc372]:_ZN5tools10threadpool3runEb+0x492) [0x619aa8bfc372]
2020-04-13 11:43:08.224	    7a6fab0a9700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [9]  0x1eda3) [0x7a8618054da3]:_thread.so.1.72.0(+0x1eda3) [0x7a8618054da3]
2020-04-13 11:43:08.225	    7a6fab0a9700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [10] /lib64/libpthread.so.0(+0x8497) [0x7a8617c11497] 
2020-04-13 11:43:08.225	    7a6fab0a9700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [11] /lib64/libc.so.6(clone+0x3f) [0x7a8617b3e0df] 
2020-04-13 11:43:08.225	    7a6fab0a9700	INFO	stacktrace	src/common/stack_trace.cpp:172	
2020-04-13 11:43:08.806	    7a6fab0a9700	INFO	stacktrace	src/common/stack_trace.cpp:133	Exception: std::runtime_error
2020-04-13 11:43:08.806	    7a6fab0a9700	INFO	stacktrace	src/common/stack_trace.cpp:134	Unwound call stack:
2020-04-13 11:43:08.810	    7a6fab0a9700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [1]  0x126) [0x619aa86a638d]:__cxa_throw+0x126) [0x619aa86a638d]
2020-04-13 11:43:08.810	    7a6fab0a9700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [2] /usr/bin/monerod(+0x35b786) [0x619aa86ec786] 
2020-04-13 11:43:08.810	    7a6fab0a9700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [3]  0x4d) [0x619aa8d67c0d]:_ZN7randomx6VmBaseINS_18LargePageAllocatorELb0EE8allocateEv+0x4d) [0x619aa8d67c0d]
2020-04-13 11:43:08.810	    7a6fab0a9700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [4]  0x43f) [0x619aa8d628ff]:_create_vm+0x43f) [0x619aa8d628ff]
2020-04-13 11:43:08.810	    7a6fab0a9700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [5]  0x49f) [0x619aa8bb595f]:_slow_hash+0x49f) [0x619aa8bb595f]
2020-04-13 11:43:08.810	    7a6fab0a9700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [6]  0xe9) [0x619aa8b9c7e9]:_ZN10cryptonote18get_block_longhashEPKNS_10BlockchainERKNS_5blockERN6crypto4hashEmi+0xe9) [0x619aa8b9c7e9]
2020-04-13 11:43:08.810	    7a6fab0a9700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [7]  0x24) [0x619aa8b9c9c4]:_ZN10cryptonote18get_block_longhashEPKNS_10BlockchainERKNS_5blockEmi+0x24) [0x619aa8b9c9c4]
2020-04-13 11:43:08.810	    7a6fab0a9700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [8]  0xc7) [0x619aa8b3d467]:_ZNK10cryptonote10Blockchain21block_longhash_workerEmRKN4epee4spanIKNS_5blockEEERSt13unordered_mapIN6crypto4hashESA_St4hashISA_ESt8equal_toISA_ESaISt4pairIKSA_SA_EEE+0xc7) [0x619aa8b3d467]
2020-04-13 11:43:08.810	    7a6fab0a9700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [9]  0x492) [0x619aa8bfc372]:_ZN5tools10threadpool3runEb+0x492) [0x619aa8bfc372]
2020-04-13 11:43:08.810	    7a6fab0a9700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [10]  0x1eda3) [0x7a8618054da3]:_thread.so.1.72.0(+0x1eda3) [0x7a8618054da3]
2020-04-13 11:43:08.810	    7a6fab0a9700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [11] /lib64/libpthread.so.0(+0x8497) [0x7a8617c11497] 
2020-04-13 11:43:08.810	    7a6fab0a9700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [12] /lib64/libc.so.6(clone+0x3f) [0x7a8617b3e0df] 
2020-04-13 11:43:08.810	    7a6fab0a9700	INFO	stacktrace	src/common/stack_trace.cpp:172	
2020-04-13 11:43:08.811	    7a6fa9ca5700	INFO	stacktrace	src/common/stack_trace.cpp:133	Exception: std::runtime_error
2020-04-13 11:43:08.811	    7a6fa9ca5700	INFO	stacktrace	src/common/stack_trace.cpp:134	Unwound call stack:
2020-04-13 11:43:08.817	    7a6fa9ca5700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [1]  0x126) [0x619aa86a638d]:__cxa_throw+0x126) [0x619aa86a638d]
2020-04-13 11:43:08.817	    7a6fa9ca5700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [2] /usr/bin/monerod(+0x35b786) [0x619aa86ec786] 
2020-04-13 11:43:08.817	    7a6fa9ca5700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [3]  0x4d) [0x619aa8d67c0d]:_ZN7randomx6VmBaseINS_18LargePageAllocatorELb0EE8allocateEv+0x4d) [0x619aa8d67c0d]
2020-04-13 11:43:08.817	    7a6fa9ca5700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [4]  0x43f) [0x619aa8d628ff]:_create_vm+0x43f) [0x619aa8d628ff]
2020-04-13 11:43:08.817	    7a6fa9ca5700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [5]  0x49f) [0x619aa8bb595f]:_slow_hash+0x49f) [0x619aa8bb595f]
2020-04-13 11:43:08.817	    7a6fa9ca5700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [6]  0xe9) [0x619aa8b9c7e9]:_ZN10cryptonote18get_block_longhashEPKNS_10BlockchainERKNS_5blockERN6crypto4hashEmi+0xe9) [0x619aa8b9c7e9]
2020-04-13 11:43:08.817	    7a6fa9ca5700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [7]  0x24) [0x619aa8b9c9c4]:_ZN10cryptonote18get_block_longhashEPKNS_10BlockchainERKNS_5blockEmi+0x24) [0x619aa8b9c9c4]
2020-04-13 11:43:08.817	    7a6fa9ca5700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [8]  0xc7) [0x619aa8b3d467]:_ZNK10cryptonote10Blockchain21block_longhash_workerEmRKN4epee4spanIKNS_5blockEEERSt13unordered_mapIN6crypto4hashESA_St4hashISA_ESt8equal_toISA_ESaISt4pairIKSA_SA_EEE+0xc7) [0x619aa8b3d467]
2020-04-13 11:43:08.817	    7a6fa9ca5700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [9]  0x492) [0x619aa8bfc372]:_ZN5tools10threadpool3runEb+0x492) [0x619aa8bfc372]
2020-04-13 11:43:08.817	    7a6fa9ca5700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [10]  0x1eda3) [0x7a8618054da3]:_thread.so.1.72.0(+0x1eda3) [0x7a8618054da3]
2020-04-13 11:43:08.817	    7a6fa9ca5700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [11] /lib64/libpthread.so.0(+0x8497) [0x7a8617c11497] 
2020-04-13 11:43:08.817	    7a6fa9ca5700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [12] /lib64/libc.so.6(clone+0x3f) [0x7a8617b3e0df] 
2020-04-13 11:43:08.818	    7a6fa9ca5700	INFO	stacktrace	src/common/stack_trace.cpp:172	
2020-04-13 11:43:09.295	[P2P3]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1454	Synced 2075799/2075799
2020-04-13 11:43:09.295	[P2P3]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:2163	SYNCHRONIZED OK
2020-04-13 11:43:09.295	[P2P3]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:2181	
2020-04-13 11:43:09.295	[P2P3]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:2181	**********************************************************************
2020-04-13 11:43:09.295	[P2P3]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:2181	You are now synchronized with the network. You may now start monero-wallet-cli.
2020-04-13 11:43:09.295	[P2P3]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:2181	
2020-04-13 11:43:09.295	[P2P3]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:2181	Use the "help" command to see the list of available commands.
2020-04-13 11:43:09.295	[P2P3]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:2181	**********************************************************************
2020-04-13 11:43:09.303	[P2P1]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:2163	SYNCHRONIZED OK
2020-04-13 11:49:08.086	    7a6faaba8700	INFO	stacktrace	src/common/stack_trace.cpp:133	Exception: std::runtime_error
2020-04-13 11:49:08.086	    7a6faaba8700	INFO	stacktrace	src/common/stack_trace.cpp:134	Unwound call stack:
2020-04-13 11:49:08.092	    7a6faaba8700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [1]  0x126) [0x619aa86a638d]:__cxa_throw+0x126) [0x619aa86a638d]
2020-04-13 11:49:08.092	    7a6faaba8700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [2] /usr/bin/monerod(+0x35b786) [0x619aa86ec786] 
2020-04-13 11:49:08.092	    7a6faaba8700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [3]  0x4d) [0x619aa8d67c0d]:_ZN7randomx6VmBaseINS_18LargePageAllocatorELb0EE8allocateEv+0x4d) [0x619aa8d67c0d]
2020-04-13 11:49:08.092	    7a6faaba8700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [4]  0x43f) [0x619aa8d628ff]:_create_vm+0x43f) [0x619aa8d628ff]
2020-04-13 11:49:08.092	    7a6faaba8700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [5]  0x49f) [0x619aa8bb595f]:_slow_hash+0x49f) [0x619aa8bb595f]
2020-04-13 11:49:08.092	    7a6faaba8700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [6]  0xe9) [0x619aa8b9c7e9]:_ZN10cryptonote18get_block_longhashEPKNS_10BlockchainERKNS_5blockERN6crypto4hashEmi+0xe9) [0x619aa8b9c7e9]
2020-04-13 11:49:08.092	    7a6faaba8700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [7]  0x24) [0x619aa8b9c9c4]:_ZN10cryptonote18get_block_longhashEPKNS_10BlockchainERKNS_5blockEmi+0x24) [0x619aa8b9c9c4]
2020-04-13 11:49:08.092	    7a6faaba8700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [8]  0xc7) [0x619aa8b3d467]:_ZNK10cryptonote10Blockchain21block_longhash_workerEmRKN4epee4spanIKNS_5blockEEERSt13unordered_mapIN6crypto4hashESA_St4hashISA_ESt8equal_toISA_ESaISt4pairIKSA_SA_EEE+0xc7) [0x619aa8b3d467]
2020-04-13 11:49:08.092	    7a6faaba8700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [9]  0x492) [0x619aa8bfc372]:_ZN5tools10threadpool3runEb+0x492) [0x619aa8bfc372]
2020-04-13 11:49:08.092	    7a6faaba8700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [10]  0x1eda3) [0x7a8618054da3]:_thread.so.1.72.0(+0x1eda3) [0x7a8618054da3]
2020-04-13 11:49:08.093	    7a6faaba8700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [11] /lib64/libpthread.so.0(+0x8497) [0x7a8617c11497] 
2020-04-13 11:49:08.093	    7a6faaba8700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [12] /lib64/libc.so.6(clone+0x3f) [0x7a8617b3e0df] 
2020-04-13 11:49:08.093	    7a6faaba8700	INFO	stacktrace	src/common/stack_trace.cpp:172	
>




# Discussion History
## moneromooo-monero | 2020-04-13T12:21:10+00:00
They're all from the mining code. It tries to use the most efficient way to mine and falls back to something else if it can't. Is is breaking somehow ? If so, how ?

## moroznah | 2020-04-13T14:22:20+00:00
I don't see any problems (yet). It works just fine, syncs and sends tx's. I didn't try mining tho.
Just tried explicitly disabling mining in conf file, log is still flooded with these stack traces.

## moneromooo-monero | 2020-04-13T14:24:15+00:00
Your deamon hashes to verify incoming blocks whether you are mining or not.

## moroznah | 2020-04-13T14:26:55+00:00
I just enabled mining on some threads. It also works fine, stack trace frequency in log is the same.


## moroznah | 2020-04-13T14:32:13+00:00
Gave it more cores, mines ok, new traces
monerod mining_status
2020-04-13 14:30:00.510	I Monero 'Carbon Chamaeleon' (v0.15.0.5-17ec003c0)
2020-04-13 14:30:00.512	I Generating SSL certificate
Mining at 4.74 kH/s with 104 threads


> ...
2020-04-13 14:29:44.400	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:133	Exception: boost::wrapexcept<boost::bad_weak_ptr>
2020-04-13 14:29:44.400	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:134	Unwound call stack:
2020-04-13 14:29:44.407	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [1]  0x126) [0x577adeb9e38d]:__cxa_throw+0x126) [0x577adeb9e38d]
2020-04-13 14:29:44.407	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [2]  0x184) [0x577adef747c4]:_ZN4epee9net_utils10connectionINS_5levin22async_protocol_handlerIN8nodetool24p2p_connection_context_tIN10cryptonote29cryptonote_connection_contextEEEEEE21safe_shared_from_thisEv+0x184) [0x577adef747c4]
2020-04-13 14:29:44.407	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [3]  0x39) [0x577adef96fd9]:_ZN4epee9net_utils10connectionINS_5levin22async_protocol_handlerIN8nodetool24p2p_connection_context_tIN10cryptonote29cryptonote_connection_contextEEEEEE5closeEv+0x39) [0x577adef96fd9]
2020-04-13 14:29:44.407	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [4]  0x3d1) [0x577adef50191]:_ZN4epee5levin29async_protocol_handler_configIN8nodetool24p2p_connection_context_tIN10cryptonote29cryptonote_connection_contextEEEE5closeEN5boost5uuids4uuidE+0x3d1) [0x577adef50191]
2020-04-13 14:29:44.407	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [5]  0x361) [0x577adeff90a1]:_ZN8nodetool11node_serverIN10cryptonote29t_cryptonote_protocol_handlerINS1_4coreEEEE22do_handshake_with_peerERmRNS_24p2p_connection_context_tINS1_29cryptonote_connection_contextEEEb+0x361) [0x577adeff90a1]
2020-04-13 14:29:44.407	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [6]  0x294) [0x577adeff9794]:_ZN8nodetool11node_serverIN10cryptonote29t_cryptonote_protocol_handlerINS1_4coreEEEE42try_to_connect_and_handshake_with_new_peerERKN4epee9net_utils15network_addressEbmNS5_8PeerTypeEm+0x294) [0x577adeff9794]
2020-04-13 14:29:44.407	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [7]  0xe0f) [0x577adeffc72f]:_ZN8nodetool11node_serverIN10cryptonote29t_cryptonote_protocol_handlerINS1_4coreEEEE33make_new_connection_from_peerlistERNS5_12network_zoneEb+0xe0f) [0x577adeffc72f]
2020-04-13 14:29:44.407	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [8]  0x1d3) [0x577adeffe793]:_ZN8nodetool11node_serverIN10cryptonote29t_cryptonote_protocol_handlerINS1_4coreEEEE31make_expected_connections_countERNS5_12network_zoneENS5_8PeerTypeEm+0x1d3) [0x577adeffe793]
2020-04-13 14:29:44.407	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [9]  0x312) [0x577adefff892]:_ZN8nodetool11node_serverIN10cryptonote29t_cryptonote_protocol_handlerINS1_4coreEEEE17connections_makerEv+0x312) [0x577adefff892]
2020-04-13 14:29:44.407	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [10]  0xba) [0x577adef46f9a]:_ZN8nodetool11node_serverIN10cryptonote29t_cryptonote_protocol_handlerINS1_4coreEEEE11idle_workerEv+0xba) [0x577adef46f9a]
2020-04-13 14:29:44.407	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [11]  0x52) [0x577adef89d32]:_ZN4epee9net_utils18boosted_tcp_serverINS_5levin22async_protocol_handlerIN8nodetool24p2p_connection_context_tIN10cryptonote29cryptonote_connection_contextEEEEEE20global_timer_handlerIN5boost3_bi6bind_tIbNSC_4_mfi3mf0IbNS4_11node_serverINS6_29t_cryptonote_protocol_handlerINS6_4coreEEEEEEENSD_5list1INSD_5valueIPSL_EEEEEEEEbNSC_10shared_ptrINSA_20idle_callback_conextIT_EEEE+0x52) [0x577adef89d32]
2020-04-13 14:29:44.408	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [12]  0x320) [0x577adefcafc0]:_ZN5boost4asio6detail12wait_handlerINS_3_bi6bind_tIbNS_4_mfi3mf1IbN4epee9net_utils18boosted_tcp_serverINS7_5levin22async_protocol_handlerIN8nodetool24p2p_connection_context_tIN10cryptonote29cryptonote_connection_contextEEEEEEENS_10shared_ptrINSI_20idle_callback_conextINS4_IbNS5_3mf0IbNSC_11node_serverINSE_29t_cryptonote_protocol_handlerINSE_4coreEEEEEEENS3_5list1INS3_5valueIPSQ_EEEEEEEEEEEENS3_5list2INST_IPSI_EENST_ISZ_EEEEEENS1_18io_object_executorINS0_8executorEEEE11do_completeEPvPNS1_19scheduler_operationERKNS_6system10error_codeEm+0x320) [0x577adefcafc0]
2020-04-13 14:29:44.408	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [13]  0x55f) [0x577adec39b5f]:_ZN5boost4asio6detail9scheduler3runERNS_6system10error_codeE+0x55f) [0x577adec39b5f]
2020-04-13 14:29:44.408	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [14]  0x1e7) [0x577adef6c7e7]:_ZN4epee9net_utils18boosted_tcp_serverINS_5levin22async_protocol_handlerIN8nodetool24p2p_connection_context_tIN10cryptonote29cryptonote_connection_contextEEEEEE13worker_threadEv+0x1e7) [0x577adef6c7e7]
2020-04-13 14:29:44.408	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [15]  0x1eda3) [0x71fd0eeafda3]:_thread.so.1.72.0(+0x1eda3) [0x71fd0eeafda3]
2020-04-13 14:29:44.408	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [16] /lib64/libpthread.so.0(+0x8497) [0x71fd0ea6c497] 
2020-04-13 14:29:44.408	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [17] /lib64/libc.so.6(clone+0x3f) [0x71fd0e9990df] 
2020-04-13 14:29:44.408	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	


## moneromooo-monero | 2020-04-13T14:57:39+00:00
You can ignore this one too, it's innocuous (and fixed in git).

## moroznah | 2020-04-13T15:30:01+00:00
Alright, it works, screw the logs. :)
Thanks


# Action History
- Created by: moroznah | 2020-04-13T12:07:04+00:00
- Closed at: 2020-04-13T15:30:01+00:00
