---
title: Monero refuses to compile
source_url: https://github.com/monero-project/monero/issues/8184
author: kvthweatt
assignees: []
labels: []
created_at: '2022-02-18T02:53:21+00:00'
updated_at: '2022-02-18T03:58:39+00:00'
type: issue
status: closed
closed_at: '2022-02-18T02:55:46+00:00'
---

# Original Description
[ 54%] Building CXX object src/rpc/CMakeFiles/obj_rpc.dir/core_rpc_server.cpp.o
/home/kvt/monero/src/rpc/core_rpc_server.cpp: In member function ‘bool cryptonote::core_rpc_server::on_rpc_access_data(const request&, cryptonote::COMMAND_RPC_ACCESS_DATA::response&, epee::json_rpc::error&, const connection_context)’:
/home/kvt/monero/src/rpc/core_rpc_server.cpp:3375:14: warning: ‘r’ may be used uninitialized in this function [-Wmaybe-uninitialized]
3375 | return r;
| ^
/home/kvt/monero/src/rpc/core_rpc_server.cpp: In member function ‘bool cryptonote::core_rpc_server::on_get_limit(const request&, cryptonote::COMMAND_RPC_GET_LIMIT::response&, const connection_context)’:
/home/kvt/monero/src/rpc/core_rpc_server.cpp:2772:14: warning: ‘r’ may be used uninitialized in this function [-Wmaybe-uninitialized]
2772 | return r;
| ^
/home/kvt/monero/src/rpc/core_rpc_server.cpp: In member function ‘bool cryptonote::core_rpc_server::on_get_version(const request&, cryptonote::COMMAND_RPC_GET_VERSION::response&, epee::json_rpc::error&, const connection_context)’:
/home/kvt/monero/src/rpc/core_rpc_server.cpp:2695:14: warning: ‘r’ may be used uninitialized in this function [-Wmaybe-uninitialized]
2695 | return r;
| ^
/home/kvt/monero/src/rpc/core_rpc_server.cpp: In member function ‘bool cryptonote::core_rpc_server::on_get_height(const request&, cryptonote::COMMAND_RPC_GET_HEIGHT::response&, const connection_context)’:
/home/kvt/monero/src/rpc/core_rpc_server.cpp:428:14: warning: ‘r’ may be used uninitialized in this function [-Wmaybe-uninitialized]
428 | return r;
| ^
c++: fatal error: Killed signal terminated program cc1plus
compilation terminated.
make[3]: *** [src/rpc/CMakeFiles/obj_rpc.dir/build.make:108: src/rpc/CMakeFiles/obj_rpc.dir/core_rpc_server.cpp.o] Error 1
make[3]: Leaving directory '/home/kvt/monero/build/Linux/release-v0.17/release'
make[2]: *** [CMakeFiles/Makefile2:3074: src/rpc/CMakeFiles/obj_rpc.dir/all] Error 2
make[2]: Leaving directory '/home/kvt/monero/build/Linux/release-v0.17/release'
make[1]: *** [Makefile:160: all] Error 2
make[1]: Leaving directory '/home/kvt/monero/build/Linux/release-v0.17/release'
make: *** [Makefile:103: release-all] Error 2

I'm on a Chromebook running the linux development environment.

This type of error has nothing to do with my cpu architecture, as you can see there's 4 instances of an uninitialized bool being used.

I followed the README.md instructions completely, I have all dependencies and I can't get past this point.
Any fix?

# Discussion History
## selsta | 2022-02-18T02:55:46+00:00
Your compiler ran out of RAM. Try to use `-j1`.

## kvthweatt | 2022-02-18T03:38:27+00:00
I closed everything running and compiled again with make -j1 and still no success.

## selsta | 2022-02-18T03:40:44+00:00
How much free RAM do you have? If it says

> c++: fatal error: Killed signal terminated

it means that you don't have enough memory.

## kvthweatt | 2022-02-18T03:45:57+00:00
~/monero$ grep MemTotal /proc/meminfo
MemTotal:        2844604 kB

## selsta | 2022-02-18T03:48:21+00:00
And free memory?

## kvthweatt | 2022-02-18T03:51:02+00:00
free -m
               total        used        free      shared  buff/cache   available
Mem:            2777           4        2773           0           0        2773
Swap:              0           0           0

2.7GB free

## selsta | 2022-02-18T03:58:24+00:00
Your operating system is killing the compiler, likely due to missing memory.

Try to add some swap or increase the memory of your VM, assuming it's a VM.

# Action History
- Created by: kvthweatt | 2022-02-18T02:53:21+00:00
- Closed at: 2022-02-18T02:55:46+00:00
