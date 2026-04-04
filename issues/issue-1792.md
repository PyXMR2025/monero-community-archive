---
title: '"make debug" fails: undefined reference to `cryptonote::BlockchainDB::get_block_from_height(unsigned
  long const&) const'''
source_url: https://github.com/monero-project/monero/issues/1792
author: danrmiller
assignees: []
labels: []
created_at: '2017-02-24T07:21:57+00:00'
updated_at: '2017-03-19T16:58:10+00:00'
type: issue
status: closed
closed_at: '2017-03-19T16:58:10+00:00'
---

# Original Description
"Make debug" fails on several platforms.

`
[ 95%] Linking CXX executable ../../bin/monero-utils-deserialize
../cryptonote_basic/libcryptonote_basic.so: undefined reference to `cryptonote::BlockchainDB::get_block_from_height(unsigned long const&) const'
collect2: error: ld returned 1 exit status
src/blockchain_utilities/CMakeFiles/cn_deserialize.dir/build.make:116: recipe for target 'bin/monero-utils-deserialize' failed`

For example: 
https://build.getmonero.org/builders/monero-tests-ubuntu-16.04-i686/builds/2/steps/compile/logs/stdio

# Discussion History
## moneromooo-monero | 2017-02-24T09:02:36+00:00
https://github.com/monero-project/monero/pull/1794 should fix it

## Jaqueeee | 2017-02-24T15:10:54+00:00
@moneromooo-monero Still having similar issue with debug build on osx.
```
Scanning dependencies of target cryptonote_basic
[ 69%] Linking CXX shared library libcryptonote_basic.dylib
Undefined symbols for architecture x86_64:
  "cryptonote::BlockchainDB::get_block_from_height(unsigned long long const&) const", referenced from:
      cryptonote::HardFork::get_block_version(unsigned long long) const in hardfork.cpp.o
      cryptonote::HardFork::reorganize_from_block_height(unsigned long long) in hardfork.cpp.o
      cryptonote::HardFork::rescan_from_block_height(unsigned long long) in hardfork.cpp.o
ld: symbol(s) not found for architecture x86_64
clang: error: linker command failed with exit code 1 (use -v to see invocation)
make[3]: *** [src/cryptonote_basic/libcryptonote_basic.dylib] Error 1
make[2]: *** [src/cryptonote_basic/CMakeFiles/cryptonote_basic.dir/all] Error 2
```

## moneromooo-monero | 2017-02-24T18:30:56+00:00
Looks like blockchain_db and cryptonote_basic require each other.

## tdprime | 2017-02-25T16:18:30+00:00
Commit 49efd3add9f7b9bbcbd2526538846f6d8e58ac86 broke things

## moneromooo-monero | 2017-02-25T16:43:50+00:00
Does https://github.com/moneromooo-monero/bitmonero/tree/crossdep fix it ?

## tdprime | 2017-02-25T21:42:12+00:00
This build succeeded.

What is being lost by doing this?

> On Feb 25, 2017, at 11:43 AM, moneromooo-monero <notifications@github.com> wrote:
> 
> Does https://github.com/moneromooo-monero/bitmonero/tree/crossdep <https://github.com/moneromooo-monero/bitmonero/tree/crossdep> fix it ?
> 
> —
> You are receiving this because you commented.
> Reply to this email directly, view it on GitHub <https://github.com/monero-project/monero/issues/1792#issuecomment-282495699>, or mute the thread <https://github.com/notifications/unsubscribe-auth/AYMjtm08sqjgw2_63_Sk8NeeeQpoHdvDks5rgFpJgaJpZM4MK5tH>.
> 



## moneromooo-monero | 2017-02-25T23:58:12+00:00
Nothing. A file is moved from cryptonote_basic to cryptonote_core, and it is the one that was causing a cross dependency. cryptonote_core and cryptonote_basic were the same lib until recently.
Thanks for checking, I'll PR.

## kenshi84 | 2017-03-09T06:25:28+00:00
Given Issue #1851, it's surprising to me that PR #1804 solved this issue. @danrmiller @Jaqueeee @tdprime Can you confirm?

I created another [patch](https://github.com/monero-project/monero/files/829486/diff_virtual.txt) for this - could you please try this by doing
```
git apply diff_virtual.txt
```
from the project root on the latest master b67877af6f7192a302453e542c266a5cfc3182a7?

## danrmiller | 2017-03-09T18:41:32+00:00
@kenshi84 I have the same issue as #1804 with https://github.com/monero-project/monero/commit/b67877af6f7192a302453e542c266a5cfc3182a7. 

Your patch works for me where I tried (osx).

## kenshi84 | 2017-03-17T02:38:51+00:00
Could you please close this issue which was solved by #1853?

# Action History
- Created by: danrmiller | 2017-02-24T07:21:57+00:00
- Closed at: 2017-03-19T16:58:10+00:00
