---
title: debug build links monerod with internal libraries which are not installed.
source_url: https://github.com/monero-project/monero/issues/8133
author: blacklion
assignees: []
labels: []
created_at: '2022-01-06T11:14:49+00:00'
updated_at: '2022-01-06T17:10:15+00:00'
type: issue
status: closed
closed_at: '2022-01-06T15:33:12+00:00'
---

# Original Description
I'm trying to build `monerod` with debug information on FreeBSD 12 (amd64/x86_64) with `cmake` and `ninja`.

When I build release build (`-DCMAKE_BUILD_TYPE:STRING="Release"`) I get `monerod` linked only with "system" shared libraries and everything works:

```
root@sysmirror-default:/wrkdirs/usr/ports/net-p2p/monero-cli/work/.build # ldd ./bin/monerod
./bin/monerod:
        libexecinfo.so.1 => /usr/lib/libexecinfo.so.1 (0x801c69000)
        libboost_chrono.so.1.72.0 => /usr/local/lib/libboost_chrono.so.1.72.0 (0x801c6f000)
        libboost_filesystem.so.1.72.0 => /usr/local/lib/libboost_filesystem.so.1.72.0 (0x801c7a000)
        libboost_program_options.so.1.72.0 => /usr/local/lib/libboost_program_options.so.1.72.0 (0x801c97000)
        libboost_regex.so.1.72.0 => /usr/local/lib/libboost_regex.so.1.72.0 (0x801cf7000)
        libboost_system.so.1.72.0 => /usr/local/lib/libboost_system.so.1.72.0 (0x801da8000)
        libzmq.so.5 => /usr/local/lib/libzmq.so.5 (0x801dac000)
        libpgm-5.2.so.0 => /usr/local/lib/libpgm-5.2.so.0 (0x801e54000)
        libnorm.so.1 => /usr/local/lib/libnorm.so.1 (0x801ea4000)
        libgssapi_krb5.so.10 => /usr/lib/libgssapi_krb5.so.10 (0x801fe0000)
        libsodium.so.23 => /usr/local/lib/libsodium.so.23 (0x802002000)
        libreadline.so.8 => /usr/local/lib/libreadline.so.8 (0x8020aa000)
        libminiupnpc.so.17 => /usr/local/lib/libminiupnpc.so.17 (0x802104000)
        libunbound.so.8 => /usr/local/lib/libunbound.so.8 (0x802114000)
        libunwind.so.8 => /usr/local/lib/libunwind.so.8 (0x802215000)
        liblzma.so.5 => /usr/lib/liblzma.so.5 (0x80222f000)
        libssl.so.111 => /usr/lib/libssl.so.111 (0x80225b000)
        libcrypto.so.111 => /lib/libcrypto.so.111 (0x8022ff000)
        libboost_date_time.so.1.72.0 => /usr/local/lib/libboost_date_time.so.1.72.0 (0x8025f1000)
        libboost_thread.so.1.72.0 => /usr/local/lib/libboost_thread.so.1.72.0 (0x8025fe000)
        libboost_serialization.so.1.72.0 => /usr/local/lib/libboost_serialization.so.1.72.0 (0x802619000)
        libc++.so.1 => /usr/lib/libc++.so.1 (0x80265b000)
        libcxxrt.so.1 => /lib/libcxxrt.so.1 (0x802728000)
        libm.so.5 => /lib/libm.so.5 (0x80274b000)
        libgcc_s.so.1 => /lib/libgcc_s.so.1 (0x802781000)
        libthr.so.3 => /lib/libthr.so.3 (0x80279b000)
        libc.so.7 => /lib/libc.so.7 (0x8027c8000)
        libelf.so.2 => /lib/libelf.so.2 (0x802bc0000)
        librt.so.1 => /usr/lib/librt.so.1 (0x802bdc000)
        libicudata.so.70 => /usr/local/lib/libicudata.so.70 (0x802be5000)
        libicui18n.so.70 => /usr/local/lib/libicui18n.so.70 (0x802be8000)
        libicuuc.so.70 => /usr/local/lib/libicuuc.so.70 (0x802f35000)
        libgssapi.so.10 => /usr/lib/libgssapi.so.10 (0x803148000)
        libkrb5.so.11 => /usr/lib/libkrb5.so.11 (0x803155000)
        libroken.so.11 => /usr/lib/libroken.so.11 (0x8031d7000)
        libasn1.so.11 => /usr/lib/libasn1.so.11 (0x8031ed000)
        libcom_err.so.5 => /usr/lib/libcom_err.so.5 (0x803293000)
        libncursesw.so.8 => /lib/libncursesw.so.8 (0x803298000)
        libutil.so.9 => /lib/libutil.so.9 (0x8032fa000)
        libevent-2.1.so.7 => /usr/local/lib/libevent-2.1.so.7 (0x803312000)
        libnghttp2.so.14 => /usr/local/lib/libnghttp2.so.14 (0x803368000)
        libz.so.6 => /lib/libz.so.6 (0x803396000)
        libmd.so.6 => /lib/libmd.so.6 (0x8033b2000)
        libcrypt.so.5 => /lib/libcrypt.so.5 (0x8033d0000)
        libhx509.so.11 => /usr/lib/libhx509.so.11 (0x8033f1000)
        libwind.so.11 => /usr/lib/libwind.so.11 (0x803442000)
        libheimbase.so.11 => /usr/lib/libheimbase.so.11 (0x80346d000)
        libprivateheimipcc.so.11 => /usr/lib/libprivateheimipcc.so.11 (0x803474000)
```

When I build debug build (`-DCMAKE_BUILD_TYPE:STRING="Debug"`) I get `monerod` linked with "system" and internal shared libraries, which are not installed, and `monerod` can not be started:

```
root@sysmirror-default:/wrkdirs/usr/ports/net-p2p/monero-cli/work/.build # ldd ./bin/monerod
./bin/monerod:
        libexecinfo.so.1 => /usr/lib/libexecinfo.so.1 (0x8019bd000)
        libdaemonizer.so => /wrkdirs/usr/ports/net-p2p/monero-cli/work/.build/src/daemonizer/libdaemonizer.so (0x8019c3000)
        libdaemon_rpc_server.so => /wrkdirs/usr/ports/net-p2p/monero-cli/work/.build/src/rpc/libdaemon_rpc_server.so (0x8019d5000)
        libboost_chrono.so.1.72.0 => /usr/local/lib/libboost_chrono.so.1.72.0 (0x801aff000)
        libboost_filesystem.so.1.72.0 => /usr/local/lib/libboost_filesystem.so.1.72.0 (0x801b0a000)
        libboost_program_options.so.1.72.0 => /usr/local/lib/libboost_program_options.so.1.72.0 (0x801b27000)
        libboost_regex.so.1.72.0 => /usr/local/lib/libboost_regex.so.1.72.0 (0x801b87000)
        libboost_system.so.1.72.0 => /usr/local/lib/libboost_system.so.1.72.0 (0x801c38000)
        libzmq.so.5 => /usr/local/lib/libzmq.so.5 (0x801c3c000)
        libpgm-5.2.so.0 => /usr/local/lib/libpgm-5.2.so.0 (0x801ce4000)
        libnorm.so.1 => /usr/local/lib/libnorm.so.1 (0x801d34000)
        libgssapi_krb5.so.10 => /usr/lib/libgssapi_krb5.so.10 (0x801e70000)
        libsodium.so.23 => /usr/local/lib/libsodium.so.23 (0x801e92000)
        libreadline.so.8 => /usr/local/lib/libreadline.so.8 (0x801f3a000)
        librpc.so => /wrkdirs/usr/ports/net-p2p/monero-cli/work/.build/src/rpc/librpc.so (0x802000000)
        librpc_base.so => /wrkdirs/usr/ports/net-p2p/monero-cli/work/.build/src/rpc/librpc_base.so (0x8033c3000)
        libserialization.so => /wrkdirs/usr/ports/net-p2p/monero-cli/work/.build/src/serialization/libserialization.so (0x80346d000)
        libcryptonote_protocol.so => /wrkdirs/usr/ports/net-p2p/monero-cli/work/.build/src/cryptonote_protocol/libcryptonote_protocol.so (0x803558000)
        libp2p.so => /wrkdirs/usr/ports/net-p2p/monero-cli/work/.build/src/p2p/libp2p.so (0x8037aa000)
        libcryptonote_core.so => /wrkdirs/usr/ports/net-p2p/monero-cli/work/.build/src/cryptonote_core/libcryptonote_core.so (0x803a00000)
        libblockchain_db.so => /wrkdirs/usr/ports/net-p2p/monero-cli/work/.build/src/blockchain_db/libblockchain_db.so (0x803e5e000)
        liblmdb.so => /wrkdirs/usr/ports/net-p2p/monero-cli/work/.build/external/db_drivers/liblmdb/liblmdb.so (0x801f94000)
        libmultisig.so => /wrkdirs/usr/ports/net-p2p/monero-cli/work/.build/src/multisig/libmultisig.so (0x80400c000)
        libringct.so => /wrkdirs/usr/ports/net-p2p/monero-cli/work/.build/src/ringct/libringct.so (0x804056000)
        libhardforks.so => /wrkdirs/usr/ports/net-p2p/monero-cli/work/.build/src/hardforks/libhardforks.so (0x801fb7000)
        libnet.so => /wrkdirs/usr/ports/net-p2p/monero-cli/work/.build/src/net/libnet.so (0x804200000)
        libminiupnpc.so.17 => /usr/local/lib/libminiupnpc.so.17 (0x801fbc000)
        libcryptonote_basic.so => /wrkdirs/usr/ports/net-p2p/monero-cli/work/.build/src/cryptonote_basic/libcryptonote_basic.so (0x804800000)
        libdevice.so => /wrkdirs/usr/ports/net-p2p/monero-cli/work/.build/src/device/libdevice.so (0x8040fe000)
        libringct_basic.so => /wrkdirs/usr/ports/net-p2p/monero-cli/work/.build/src/ringct/libringct_basic.so (0x804608000)
        libwallet-crypto.so => /wrkdirs/usr/ports/net-p2p/monero-cli/work/.build/src/crypto/wallet/libwallet-crypto.so (0x801fcc000)
        libcryptonote_format_utils_basic.so => /wrkdirs/usr/ports/net-p2p/monero-cli/work/.build/src/cryptonote_basic/libcryptonote_format_utils_basic.so (0x804156000)
        libcheckpoints.so => /wrkdirs/usr/ports/net-p2p/monero-cli/work/.build/src/checkpoints/libcheckpoints.so (0x804cab000)
        libcommon.so => /wrkdirs/usr/ports/net-p2p/monero-cli/work/.build/src/common/libcommon.so (0x804f34000)
        libcncrypto.so => /wrkdirs/usr/ports/net-p2p/monero-cli/work/.build/src/crypto/libcncrypto.so (0x8046fc000)
        libepee.so => /wrkdirs/usr/ports/net-p2p/monero-cli/work/.build/contrib/epee/src/libepee.so (0x805400000)
        libssl.so.111 => /usr/lib/libssl.so.111 (0x805241000)
        libcrypto.so.111 => /lib/libcrypto.so.111 (0x80579b000)
        librandomx.so => /wrkdirs/usr/ports/net-p2p/monero-cli/work/.build/external/randomx/librandomx.so (0x804786000)
        libunbound.so.8 => /usr/local/lib/libunbound.so.8 (0x8052e5000)
        libunwind.so.8 => /usr/local/lib/libunwind.so.8 (0x801fe6000)
        liblzma.so.5 => /usr/lib/liblzma.so.5 (0x8039c4000)
        libboost_date_time.so.1.72.0 => /usr/local/lib/libboost_date_time.so.1.72.0 (0x8039f0000)
        libboost_thread.so.1.72.0 => /usr/local/lib/libboost_thread.so.1.72.0 (0x804198000)
        libboost_serialization.so.1.72.0 => /usr/local/lib/libboost_serialization.so.1.72.0 (0x8041b3000)
        libversion.so => /wrkdirs/usr/ports/net-p2p/monero-cli/work/.build/src/libversion.so (0x8041f5000)
        libeasylogging.so => /wrkdirs/usr/ports/net-p2p/monero-cli/work/.build/external/easylogging++/libeasylogging.so (0x805a8d000)
        libc++.so.1 => /usr/lib/libc++.so.1 (0x805b82000)
        libcxxrt.so.1 => /lib/libcxxrt.so.1 (0x805c4f000)
        libm.so.5 => /lib/libm.so.5 (0x805c72000)
        libgcc_s.so.1 => /lib/libgcc_s.so.1 (0x8053e6000)
        libthr.so.3 => /lib/libthr.so.3 (0x805ca8000)
        libc.so.7 => /lib/libc.so.7 (0x805cd5000)
        libelf.so.2 => /lib/libelf.so.2 (0x8060cd000)
        librpc_pub.so => /wrkdirs/usr/ports/net-p2p/monero-cli/work/.build/src/rpc/librpc_pub.so (0x80610a000)
        libdaemon_messages.so => /wrkdirs/usr/ports/net-p2p/monero-cli/work/.build/src/rpc/libdaemon_messages.so (0x806189000)
        librt.so.1 => /usr/lib/librt.so.1 (0x806285000)
        libicudata.so.70 => /usr/local/lib/libicudata.so.70 (0x8039fd000)
        libicui18n.so.70 => /usr/local/lib/libicui18n.so.70 (0x80628e000)
        libicuuc.so.70 => /usr/local/lib/libicuuc.so.70 (0x8065db000)
        libgssapi.so.10 => /usr/lib/libgssapi.so.10 (0x8067ee000)
        libkrb5.so.11 => /usr/lib/libkrb5.so.11 (0x8067fb000)
        libroken.so.11 => /usr/lib/libroken.so.11 (0x80687d000)
        libasn1.so.11 => /usr/lib/libasn1.so.11 (0x806893000)
        libcom_err.so.5 => /usr/lib/libcom_err.so.5 (0x8041f9000)
        libncursesw.so.8 => /lib/libncursesw.so.8 (0x806939000)
        libutil.so.9 => /lib/libutil.so.9 (0x80699b000)
        libevent-2.1.so.7 => /usr/local/lib/libevent-2.1.so.7 (0x8069b3000)
        libnghttp2.so.14 => /usr/local/lib/libnghttp2.so.14 (0x806a09000)
        libz.so.6 => /lib/libz.so.6 (0x806a37000)
        libmd.so.6 => /lib/libmd.so.6 (0x806a53000)
        libcrypt.so.5 => /lib/libcrypt.so.5 (0x806a71000)
        libhx509.so.11 => /usr/lib/libhx509.so.11 (0x806a92000)
        libwind.so.11 => /usr/lib/libwind.so.11 (0x806ae3000)
        libheimbase.so.11 => /usr/lib/libheimbase.so.11 (0x806b0e000)
        libprivateheimipcc.so.11 => /usr/lib/libprivateheimipcc.so.11 (0x806b15000)
```

diff with stripped addresses is:

```
--- monerod.rel.ldd	2022-01-06 14:09:54.158275900 +0300
+++ monerod.dbg.ldd	2022-01-06 14:09:47.302300200 +0300
@@ -1,6 +1,8 @@
 root@sysmirror-default:/wrkdirs/usr/ports/net-p2p/monero-cli/work/.build # ldd ./bin/monerod
 ./bin/monerod:
         libexecinfo.so.1 => /usr/lib/libexecinfo.so.1
+        libdaemonizer.so => /wrkdirs/usr/ports/net-p2p/monero-cli/work/.build/src/daemonizer/libdaemonizer.so
+        libdaemon_rpc_server.so => /wrkdirs/usr/ports/net-p2p/monero-cli/work/.build/src/rpc/libdaemon_rpc_server.so
         libboost_chrono.so.1.72.0 => /usr/local/lib/libboost_chrono.so.1.72.0
         libboost_filesystem.so.1.72.0 => /usr/local/lib/libboost_filesystem.so.1.72.0
         libboost_program_options.so.1.72.0 => /usr/local/lib/libboost_program_options.so.1.72.0
@@ -12,15 +14,39 @@
         libgssapi_krb5.so.10 => /usr/lib/libgssapi_krb5.so.10
         libsodium.so.23 => /usr/local/lib/libsodium.so.23
         libreadline.so.8 => /usr/local/lib/libreadline.so.8
+        librpc.so => /wrkdirs/usr/ports/net-p2p/monero-cli/work/.build/src/rpc/librpc.so
+        librpc_base.so => /wrkdirs/usr/ports/net-p2p/monero-cli/work/.build/src/rpc/librpc_base.so
+        libserialization.so => /wrkdirs/usr/ports/net-p2p/monero-cli/work/.build/src/serialization/libserialization.so
+        libcryptonote_protocol.so => /wrkdirs/usr/ports/net-p2p/monero-cli/work/.build/src/cryptonote_protocol/libcryptonote_protocol.so
+        libp2p.so => /wrkdirs/usr/ports/net-p2p/monero-cli/work/.build/src/p2p/libp2p.so
+        libcryptonote_core.so => /wrkdirs/usr/ports/net-p2p/monero-cli/work/.build/src/cryptonote_core/libcryptonote_core.so
+        libblockchain_db.so => /wrkdirs/usr/ports/net-p2p/monero-cli/work/.build/src/blockchain_db/libblockchain_db.so
+        liblmdb.so => /wrkdirs/usr/ports/net-p2p/monero-cli/work/.build/external/db_drivers/liblmdb/liblmdb.so
+        libmultisig.so => /wrkdirs/usr/ports/net-p2p/monero-cli/work/.build/src/multisig/libmultisig.so
+        libringct.so => /wrkdirs/usr/ports/net-p2p/monero-cli/work/.build/src/ringct/libringct.so
+        libhardforks.so => /wrkdirs/usr/ports/net-p2p/monero-cli/work/.build/src/hardforks/libhardforks.so
+        libnet.so => /wrkdirs/usr/ports/net-p2p/monero-cli/work/.build/src/net/libnet.so
         libminiupnpc.so.17 => /usr/local/lib/libminiupnpc.so.17
+        libcryptonote_basic.so => /wrkdirs/usr/ports/net-p2p/monero-cli/work/.build/src/cryptonote_basic/libcryptonote_basic.so
+        libdevice.so => /wrkdirs/usr/ports/net-p2p/monero-cli/work/.build/src/device/libdevice.so
+        libringct_basic.so => /wrkdirs/usr/ports/net-p2p/monero-cli/work/.build/src/ringct/libringct_basic.so
+        libwallet-crypto.so => /wrkdirs/usr/ports/net-p2p/monero-cli/work/.build/src/crypto/wallet/libwallet-crypto.so
+        libcryptonote_format_utils_basic.so => /wrkdirs/usr/ports/net-p2p/monero-cli/work/.build/src/cryptonote_basic/libcryptonote_format_utils_basic.so
+        libcheckpoints.so => /wrkdirs/usr/ports/net-p2p/monero-cli/work/.build/src/checkpoints/libcheckpoints.so
+        libcommon.so => /wrkdirs/usr/ports/net-p2p/monero-cli/work/.build/src/common/libcommon.so
+        libcncrypto.so => /wrkdirs/usr/ports/net-p2p/monero-cli/work/.build/src/crypto/libcncrypto.so
+        libepee.so => /wrkdirs/usr/ports/net-p2p/monero-cli/work/.build/contrib/epee/src/libepee.so
+        libssl.so.111 => /usr/lib/libssl.so.111
+        libcrypto.so.111 => /lib/libcrypto.so.111
+        librandomx.so => /wrkdirs/usr/ports/net-p2p/monero-cli/work/.build/external/randomx/librandomx.so
         libunbound.so.8 => /usr/local/lib/libunbound.so.8
         libunwind.so.8 => /usr/local/lib/libunwind.so.8
         liblzma.so.5 => /usr/lib/liblzma.so.5
-        libssl.so.111 => /usr/lib/libssl.so.111
-        libcrypto.so.111 => /lib/libcrypto.so.111
         libboost_date_time.so.1.72.0 => /usr/local/lib/libboost_date_time.so.1.72.0
         libboost_thread.so.1.72.0 => /usr/local/lib/libboost_thread.so.1.72.0
         libboost_serialization.so.1.72.0 => /usr/local/lib/libboost_serialization.so.1.72.0
+        libversion.so => /wrkdirs/usr/ports/net-p2p/monero-cli/work/.build/src/libversion.so
+        libeasylogging.so => /wrkdirs/usr/ports/net-p2p/monero-cli/work/.build/external/easylogging++/libeasylogging.so
         libc++.so.1 => /usr/lib/libc++.so.1
         libcxxrt.so.1 => /lib/libcxxrt.so.1
         libm.so.5 => /lib/libm.so.5
@@ -28,6 +54,8 @@
         libthr.so.3 => /lib/libthr.so.3
         libc.so.7 => /lib/libc.so.7
         libelf.so.2 => /lib/libelf.so.2
+        librpc_pub.so => /wrkdirs/usr/ports/net-p2p/monero-cli/work/.build/src/rpc/librpc_pub.so
+        libdaemon_messages.so => /wrkdirs/usr/ports/net-p2p/monero-cli/work/.build/src/rpc/libdaemon_messages.so
         librt.so.1 => /usr/lib/librt.so.1
         libicudata.so.70 => /usr/local/lib/libicudata.so.70
         libicui18n.so.70 => /usr/local/lib/libicui18n.so.70
```

# Discussion History
## selsta | 2022-01-06T15:23:37+00:00
https://github.com/monero-project/monero/blob/master/CMakeLists.txt#L465-L475

Could be these lines?

## hyc | 2022-01-06T15:33:12+00:00
This is intentional. Debug builds are for *debugging*. The internal libs are built as shared libs so that if any of them needs to be changed, no time is wasted relinking all the resulting executables. None of these are meant to be run anywhere besides the build tree.

## blacklion | 2022-01-06T16:48:52+00:00
> This is intentional. Debug builds are for _debugging_. The internal libs are built as shared libs so that if any of them needs to be changed, no time is wasted relinking all the resulting executables. None of these are meant to be run anywhere besides the build tree.

Stack traces in log file without debugging info is useless...

## hyc | 2022-01-06T17:00:13+00:00
Irrelevant. There is no need to install a debug binary, just run it from the build tree.

## blacklion | 2022-01-06T17:06:07+00:00
> Irrelevant. There is no need to install a debug binary, just run it from the build tree.

Then stack traces must be turned off in release build, as they take time (monerod consumes 100% of one core when stacktrace is being printed out to log) and, again, useless in release build. And CMake looks for libunwind unconditionally...

## selsta | 2022-01-06T17:07:37+00:00
Does your monerod work fine if you disable stack traces? I don't think your issues are related to the printing of stack traces.

## blacklion | 2022-01-06T17:10:15+00:00
> Does your monerod work fine if you disable stack traces? I don't think your issues are related to the printing of stack traces.

It is what I'm investigating right now, but I think, it is better to continue in #8132

I'll post updates with proper stacktraces and without stacktraces at all to #8132

# Action History
- Created by: blacklion | 2022-01-06T11:14:49+00:00
- Closed at: 2022-01-06T15:33:12+00:00
