---
title: Can't build new v0.14.1.0
source_url: https://github.com/monero-project/monero/issues/5648
author: gituser
assignees: []
labels: []
created_at: '2019-06-15T12:35:45+00:00'
updated_at: '2019-07-18T10:18:19+00:00'
type: issue
status: closed
closed_at: '2019-07-18T10:18:18+00:00'
---

# Original Description
Hi!

Seems I can't build anymore new version on the setup which was working just fine on previous `v0.14.0.2`:

```
[ 79%] Building CXX object src/rpc/CMakeFiles/obj_daemon_messages.dir/message.cpp.o
[ 80%] Building CXX object src/rpc/CMakeFiles/obj_daemon_messages.dir/daemon_messages.cpp.o
In file included from /home/build/monero/source/src/rpc/daemon_messages.cpp:29:0:
/home/build/monero/source/src/rpc/daemon_messages.h:71:53: error: converting to 'cryptonote::rpc::GetTransactions::Response::txes_map {aka std::unordered_map<crypto::hash, cryptonote::rpc::transaction_info>}' from initializer list would use explicit constructor 'std::unordered_map<_Key, _Tp, _Hash, _Pred, _Alloc>::unordered_map(std::unordered_map<_Key, _Tp, _Hash, _Pred, _Alloc>::size_type, const hasher&, const key_equal&, const allocator_type&) [with _Key = crypto::hash; _Tp = cryptonote::rpc::transaction_info; _Hash = std::hash<crypto::hash>; _Pred = std::equal_to<crypto::hash>; _Alloc = std::allocator<std::pair<const crypto::hash, cryptonote::rpc::transaction_info> >; std::unordered_map<_Key, _Tp, _Hash, _Pred, _Alloc>::size_type = long unsigned int; std::unordered_map<_Key, _Tp, _Hash, _Pred, _Alloc>::hasher = std::hash<crypto::hash>; std::unordered_map<_Key, _Tp, _Hash, _Pred, _Alloc>::key_equal = std::equal_to<crypto::hash>; std::unordered_map<_Key, _Tp, _Hash, _Pred, _Alloc>::allocator_type = std::allocator<std::pair<const crypto::hash, cryptonote::rpc::transaction_info> >]'
 #define RPC_MESSAGE_MEMBER(type, name) type name = {}
                                                     ^
/home/build/monero/source/src/rpc/daemon_messages.h:123:5: note: in expansion of macro 'RPC_MESSAGE_MEMBER'
     RPC_MESSAGE_MEMBER(txes_map, txs);
     ^
/home/build/monero/source/src/rpc/daemon_messages.h:71:53: error: converting to 'cryptonote::rpc::key_images_with_tx_hashes {aka std::unordered_map<crypto::key_image, std::vector<crypto::hash> >}' from initializer list would use explicit constructor 'std::unordered_map<_Key, _Tp, _Hash, _Pred, _Alloc>::unordered_map(std::unordered_map<_Key, _Tp, _Hash, _Pred, _Alloc>::size_type, const hasher&, const key_equal&, const allocator_type&) [with _Key = crypto::key_image; _Tp = std::vector<crypto::hash>; _Hash = std::hash<crypto::key_image>; _Pred = std::equal_to<crypto::key_image>; _Alloc = std::allocator<std::pair<const crypto::key_image, std::vector<crypto::hash> > >; std::unordered_map<_Key, _Tp, _Hash, _Pred, _Alloc>::size_type = long unsigned int; std::unordered_map<_Key, _Tp, _Hash, _Pred, _Alloc>::hasher = std::hash<crypto::key_image>; std::unordered_map<_Key, _Tp, _Hash, _Pred, _Alloc>::key_equal = std::equal_to<crypto::key_image>; std::unordered_map<_Key, _Tp, _Hash, _Pred, _Alloc>::allocator_type = std::allocator<std::pair<const crypto::key_image, std::vector<crypto::hash> > >]'
 #define RPC_MESSAGE_MEMBER(type, name) type name = {}
                                                     ^
/home/build/monero/source/src/rpc/daemon_messages.h:321:5: note: in expansion of macro 'RPC_MESSAGE_MEMBER'
     RPC_MESSAGE_MEMBER(key_images_with_tx_hashes, key_images);
     ^
src/rpc/CMakeFiles/obj_daemon_messages.dir/build.make:86: recipe for target 'src/rpc/CMakeFiles/obj_daemon_messages.dir/daemon_messages.cpp.o' failed
make[2]: *** [src/rpc/CMakeFiles/obj_daemon_messages.dir/daemon_messages.cpp.o] Error 1
CMakeFiles/Makefile2:2143: recipe for target 'src/rpc/CMakeFiles/obj_daemon_messages.dir/all' failed
make[1]: *** [src/rpc/CMakeFiles/obj_daemon_messages.dir/all] Error 2
Makefile:138: recipe for target 'all' failed
make: *** [all] Error 2
Build Failed.
```

What could be the reason?

Thanks.

# Discussion History
## moneromooo-monero | 2019-06-15T12:46:50+00:00
What platform, and what compiler (including version) ?

## gituser | 2019-06-15T12:58:49+00:00
@moneromooo-monero 

Debian Jessie 8
Cmake 3.6.2-2~bpo8+1
-- The C compiler identification is GNU 4.9.2
-- The CXX compiler identification is GNU 4.9.2


## moneromooo-monero | 2019-06-15T13:17:11+00:00
That's quite an old GCC. I suspect this is the reason. The README says 4.7.3, might have to be changed.

## gituser | 2019-06-15T13:26:46+00:00
Yes, but what about `v0.14.0.2` ? It worked just fine with the previous version.

## moneromooo-monero | 2019-06-15T14:34:17+00:00
If you're asking "was the min version for 0.14.0.2 4.7.3 or earlier", then yes, since it worked for you. But since this is an obvious answer, maybe I'm misinterpreting your question :)

## gituser | 2019-06-16T12:10:26+00:00
@moneromooo-monero so I've tried on Ubuntu 16.04 by using `contrib/depends` and didn't work either:

```
BASEPREFIX=`pwd`/contrib/depends
cd build/release 
cmake -DCMAKE_TOOLCHAIN_FILE=${BASEPREFIX}/x86_64-pc-linux-gnu/share/toolchain.cmake -DBACKCOMPAT=ON ../..
```

```
[ 86%] Built target obj_device_trezor
Scanning dependencies of target device_trezor
[ 86%] Linking CXX static library libdevice_trezor.a
[ 86%] Built target device_trezor
Scanning dependencies of target wallet
[ 87%] Linking CXX static library ../../lib/libwallet.a
[ 87%] Built target wallet
Scanning dependencies of target obj_daemonizer
[ 87%] Building CXX object src/daemonizer/CMakeFiles/obj_daemonizer.dir/posix_fork.cpp.o
[ 87%] Built target obj_daemonizer
Scanning dependencies of target daemonizer
[ 87%] Linking CXX static library libdaemonizer.a
[ 87%] Built target daemonizer
Scanning dependencies of target wallet_rpc_server
[ 87%] Building CXX object src/wallet/CMakeFiles/wallet_rpc_server.dir/wallet_rpc_server.cpp.o
/home/build/monero/source/src/wallet/wallet_rpc_server.cpp: In member function 'bool tools::wallet_rpc_server::on_incoming_transfers(const request&, tools::wallet_rpc::COMMAND_RPC_INCOMING_TRANSFERS::response&, epee::json_rpc::error&, const connection_context*)':
/home/build/monero/source/src/wallet/wallet_rpc_server.cpp:1809:10: warning: variable 'transfers_found' set but not used [-Wunused-but-set-variable]
     bool transfers_found = false;
          ^
[ 88%] Linking CXX executable ../../bin/monero-wallet-rpc
/usr/bin/ld: /usr/lib/gcc/x86_64-linux-gnu/5/../../../x86_64-linux-gnu/libtinfo.a(lib_termcap.o): relocation R_X86_64_32 against `_nc_globals' can not be used when making a shared object; recompile with -fPIC
/usr/lib/gcc/x86_64-linux-gnu/5/../../../x86_64-linux-gnu/libtinfo.a: error adding symbols: Bad value
collect2: error: ld returned 1 exit status
src/wallet/CMakeFiles/wallet_rpc_server.dir/build.make:131: recipe for target 'bin/monero-wallet-rpc' failed
make[2]: *** [bin/monero-wallet-rpc] Error 1
CMakeFiles/Makefile2:2594: recipe for target 'src/wallet/CMakeFiles/wallet_rpc_server.dir/all' failed
make[1]: *** [src/wallet/CMakeFiles/wallet_rpc_server.dir/all] Error 2
Makefile:140: recipe for target 'all' failed
make: *** [all] Error 2
Build Failed.
```

## gituser | 2019-06-16T12:57:51+00:00
I've also checked there is no `ncurses` package in `contrib/depends` for some reason?
Is there any specific reason why it's not there?
That's why it errors with `libtinfo.a` being wrong.

## gituser | 2019-06-16T13:33:46+00:00
Very intersting if I delete `libtinfo5` and `libtinfo5-dev` from Ubuntu 16.04 monero `v0.14.1.0` successfully builds. So I guess it's a bug. There should be ncurses in the packages to avoid the linking to the system library (if it's there).

## gituser | 2019-06-17T11:29:15+00:00
@moneromooo-monero can you add `ncurses` library into `contrib/depends` packages to avoid a situation like I've described in https://github.com/monero-project/monero/issues/5648#issuecomment-502446592 (it happens only if you have locally installed `libtinfo5` and `libtinfo5-dev` locally) ?

Thanks.

## moneromooo-monero | 2019-06-17T12:22:02+00:00
AFAIK TheCharlatan is fixing readline/curses already.

## sedited | 2019-06-25T07:41:36+00:00
I've opened #5690 to address the missing libtinfo.

## gituser | 2019-07-17T22:31:48+00:00
Just tried on the fresh `v0.14.1.1` tag and still get this error when building on Ubuntu 16.04:

```
[ 87%] Building CXX object src/wallet/CMakeFiles/wallet_rpc_server.dir/wallet_rpc_server.cpp.o
/home/build/monero/source/src/wallet/wallet_rpc_server.cpp: In member function 'bool tools::wallet_rpc_server::on_incoming_transfers(const request&, tools::wallet_rpc::COMMAND_RPC_INCOMING_TRANSFERS::response&, epee::json_rpc::error&, const connection_context*)':
/home/build/monero/source/src/wallet/wallet_rpc_server.cpp:1814:10: warning: variable 'transfers_found' set but not used [-Wunused-but-set-variable]
     bool transfers_found = false;
          ^
[ 88%] Linking CXX executable ../../bin/monero-wallet-rpc
/usr/bin/ld: /usr/lib/gcc/x86_64-linux-gnu/5/../../../x86_64-linux-gnu/libtinfo.a(lib_termcap.o): relocation R_X86_64_32 against `_nc_globals' can not be used when making a shared object; recompile with -fPIC
/usr/lib/gcc/x86_64-linux-gnu/5/../../../x86_64-linux-gnu/libtinfo.a: error adding symbols: Bad value
collect2: error: ld returned 1 exit status
src/wallet/CMakeFiles/wallet_rpc_server.dir/build.make:131: recipe for target 'bin/monero-wallet-rpc' failed
make[2]: *** [bin/monero-wallet-rpc] Error 1
CMakeFiles/Makefile2:2594: recipe for target 'src/wallet/CMakeFiles/wallet_rpc_server.dir/all' failed
make[1]: *** [src/wallet/CMakeFiles/wallet_rpc_server.dir/all] Error 2
Makefile:140: recipe for target 'all' failed
make: *** [all] Error 2
Build Failed.
```

## hyc | 2019-07-17T22:55:55+00:00
@gituser As the error message says

> recompile with -fPIC

You need to recompile libtinfo. Alternatively, comment out/remove all references to PIE/pie in the Monero CMakeLists.txt.

On a modern Ubuntu system everything is PIC already so it all Just Works but your Ubuntu 16.04 is too old.

## gituser | 2019-07-18T09:06:09+00:00
@hyx earlier I've described the bug - https://github.com/monero-project/monero/issues/5648#issuecomment-502452909

It seems it wasn't fixed with that pull request #5690 it still tries to link against system libraries instead of the ones in the dependencies folder.

The new monero build system should take care of this and it has nothing to do if it's Ubuntu 16.04 being too old as dependencies should be built within monero source tree and used.

UPDATE: it seems the issue was the outdated `contrib/depends` directory, after re-running make there, the build was successful.

## gituser | 2019-07-18T10:18:18+00:00
It seems the issue was the outdated contrib/depends directory, after re-running make there, the build was successful.

# Action History
- Created by: gituser | 2019-06-15T12:35:45+00:00
- Closed at: 2019-07-18T10:18:18+00:00
