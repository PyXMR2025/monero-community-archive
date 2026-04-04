---
title: Issue compiling w/ make debug on OSX - release-v0.15 + Master - v0.14 compiles
  fine
source_url: https://github.com/monero-project/monero/issues/6046
author: rotavele
assignees: []
labels: []
created_at: '2019-10-27T19:51:44+00:00'
updated_at: '2019-11-04T19:57:35+00:00'
type: issue
status: closed
closed_at: '2019-11-04T19:57:35+00:00'
---

# Original Description
I can't seem to build debug on OSx. this only happens w/v0.15 and master. 
```
[ 87%] Linking CXX shared library libcryptonote_basic.dylib
Undefined symbols for architecture x86_64:
  "cryptonote::get_block_longhash(cryptonote::Blockchain const*, cryptonote::block const&, crypto::hash&, unsigned long long, int)", referenced from:
      cryptonote::miner::worker_thread() in miner.cpp.o
      cryptonote::miner::find_nonce_for_given_block(cryptonote::Blockchain const*, cryptonote::block&, boost::multiprecision::number<boost::multiprecision::backends::cpp_int_backend<128u, 128u, (boost::multiprecision::cpp_integer_type)0, (boost::multiprecision::cpp_int_check_type)0, void>, (boost::multiprecision::expression_template_option)0> const&, unsigned long long) in miner.cpp.o
ld: symbol(s) not found for architecture x86_64
clang: error: linker command failed with exit code 1 (use -v to see invocation)
make[3]: *** [src/cryptonote_basic/libcryptonote_basic.dylib] Error 1
make[2]: *** [src/cryptonote_basic/CMakeFiles/cryptonote_basic.dir/all] Error 2
make[2]: *** Waiting for unfinished jobs....
```

# Discussion History
## moneromooo-monero | 2019-10-27T20:04:17+00:00
cryptonote_basic should not use anything from cryptonote_core. get_block_longhash seems to be defined in cryptonote_core. It should be moved (or accessed via function pointer if that's impossible, which I think it is since it now requires the blockchain)

## rotavele | 2019-10-27T20:25:11+00:00
It appears to be defined only in cryptonote_tx_utils.cpp/.h which is in cryptonote_core/ and it also seems to be accessing the Blockchain class(namespace?) as you mentioned:

in cryptonote_tx_utils.h
```
class Blockchain;
  bool get_block_longhash(const Blockchain *pb, const block& b, crypto::hash& res, const uint64_t height, const int miners);
  void get_altblock_longhash(const block& b, crypto::hash& res, const uint64_t main_height, const uint64_t height,
    const uint64_t seed_height, const crypto::hash& seed_hash);
  crypto::hash get_block_longhash(const Blockchain *pb, const block& b, const uint64_t height, const int miners);
  void get_block_longhash_reorg(const uint64_t split_height);
```
If you have a quick suggestion on how to refactor it I can experiment and try to get it to build on OSX.

## moneromooo-monero | 2019-10-27T21:15:40+00:00
I'll do that tomorrow, assuming someone else hasn't done it by then. My current idea is to pass the function as a function pointer, rather than call it by name.

## moneromooo-monero | 2019-10-27T21:19:06+00:00
That said, I can't test whatever changes I'll do, so feel free to try it now :) Failing that, I'll post a patch and you can try it then.

## moneromooo-monero | 2019-10-28T12:57:30+00:00
Does https://github.com/monero-project/monero/pull/6047 help ?

## moneromooo-monero | 2019-10-29T13:55:22+00:00
ping :) It'd be nice to have this in the imminent relase if it's confirmed to work.

## moneromooo-monero | 2019-10-31T01:18:25+00:00
I replaced the patch, as someone reported it did not move enough code. Same PR, different code.

## moneromooo-monero | 2019-11-04T19:52:28+00:00
+resolved

# Action History
- Created by: rotavele | 2019-10-27T19:51:44+00:00
- Closed at: 2019-11-04T19:57:35+00:00
