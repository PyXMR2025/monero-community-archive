---
title: 'c++: internal compiler error: Killed (program cc1plus) - Ubuntu 18.04.2 LTS'
source_url: https://github.com/monero-project/monero/issues/5791
author: lh1008
assignees: []
labels:
- invalid
created_at: '2019-08-02T14:54:06+00:00'
updated_at: '2022-01-05T06:45:36+00:00'
type: issue
status: closed
closed_at: '2019-08-02T15:50:01+00:00'
---

# Original Description
Hi everyone, 

Building from source I get this error. Any help is really appreciated.


[ 78%] Built target daemon_rpc_server
[ 79%] Building CXX object src/wallet/CMakeFiles/obj_wallet.dir/wallet2.cpp.o
/home/raver/monero/src/wallet/wallet2.cpp: In member function ‘void tools::wallet2::get_outs(std::vector<std::vector<std::tuple<long unsigned int, crypto::public_key, rct::key> > >&, const std::vector<long unsigned int>&, size_t)’:
/home/raver/monero/src/wallet/wallet2.cpp:7729:12: warning: variable ‘existing_ring_found’ set but not used [-Wunused-but-set-variable]
       bool existing_ring_found = false;
            ^~~~~~~~~~~~~~~~~~~
c++: internal compiler error: Killed (program cc1plus)
Please submit a full bug report,
with preprocessed source if appropriate.
See <file:///usr/share/doc/gcc-7/README.Bugs> for instructions.
src/wallet/CMakeFiles/obj_wallet.dir/build.make:62: recipe for target 'src/wallet/CMakeFiles/obj_wallet.dir/wallet2.cpp.o' failed
make[2]: *** [src/wallet/CMakeFiles/obj_wallet.dir/wallet2.cpp.o] Error 4
CMakeFiles/Makefile2:2401: recipe for target 'src/wallet/CMakeFiles/obj_wallet.dir/all' failed
make[1]: *** [src/wallet/CMakeFiles/obj_wallet.dir/all] Error 2
Makefile:140: recipe for target 'all' failed
make: *** [all] Error 2

>:)


# Discussion History
## lh1008 | 2019-08-02T14:55:49+00:00
I read the other related issues but there is no clear answer on how to solve this issue. It says is a memory problem but I have 2,8GB of RAM.

With a clean just installed Ubuntu so there is no other programs using the memory.

## lh1008 | 2019-08-02T15:14:38+00:00
Tried again and got this message:

ring_found’ set but not used [-Wunused-but-set-variable]
       bool existing_ring_found = false;
            ^~~~~~~~~~~~~~~~~~~
virtual memory exhausted: Cannot allocate memory
src/wallet/CMakeFiles/obj_wallet.dir/build.make:62: recipe for target 'src/wallet/CMakeFiles/obj_wallet.dir/wallet2.cpp.o' failed
make[2]: *** [src/wallet/CMakeFiles/obj_wallet.dir/wallet2.cpp.o] Error 1
CMakeFiles/Makefile2:2401: recipe for target 'src/wallet/CMakeFiles/obj_wallet.dir/all' failed
make[1]: *** [src/wallet/CMakeFiles/obj_wallet.dir/all] Error 2
Makefile:140: recipe for target 'all' failed
make: *** [all] Error 2

## hyc | 2019-08-02T15:42:07+00:00
Like it says, you're out of memory.

If you want to proceed, either install more RAM, or add about 2GB of swap space.

## hyc | 2019-08-02T15:42:13+00:00
+invalid

## lh1008 | 2019-08-02T23:34:46+00:00
@hyc it worked. Learned something new today. Thank you very much :). 


## WonderSimiliar | 2022-01-05T06:45:21+00:00
there is a more convenient option you should try:
$ catkin_make -j1
this command use single-thread compilation to avoid memory insufficiency caused by multiple threads.

# Action History
- Created by: lh1008 | 2019-08-02T14:54:06+00:00
- Closed at: 2019-08-02T15:50:01+00:00
