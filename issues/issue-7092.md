---
title: 'MACOS Big sur update: no member named ''library_version_type'' in namespace
  ''boost::serialization'''
source_url: https://github.com/monero-project/monero/issues/7092
author: IvRRimum
assignees: []
labels: []
created_at: '2020-12-07T11:55:02+00:00'
updated_at: '2021-10-06T02:49:45+00:00'
type: issue
status: closed
closed_at: '2021-10-06T02:49:45+00:00'
---

# Original Description
After updating to MACOS Big Sur and trying to compile monero branch release-v0.16 i get this error:

` [ 36%] Built target ringct
Scanning dependencies of target obj_cryptonote_core
[ 37%] Building CXX object src/cryptonote_core/CMakeFiles/obj_cryptonote_core.dir/blockchain.cpp.o
In file included from /Users/myuser/Projects/myproject/monero-16/src/cryptonote_core/blockchain.cpp:39:
In file included from /Users/myuser/Projects/myproject/monero-16/src/cryptonote_core/blockchain.h:35:
/usr/local/include/boost/serialization/list.hpp:53:33: error: no type named 'library_version_type' in namespace 'boost::serialization'; did you mean 'item_version_type'?
    const boost::serialization::library_version_type library_version(
          ~~~~~~~~~~~~~~~~~~~~~~^
/usr/local/include/boost/serialization/item_version_type.hpp:25:7: note: 'item_version_type' declared here
class item_version_type {
      ^
In file included from /Users/myuser/Projects/myproject/monero-16/src/cryptonote_core/blockchain.cpp:39:
In file included from /Users/myuser/Projects/myproject/monero-16/src/cryptonote_core/blockchain.h:35:
/usr/local/include/boost/serialization/list.hpp:60:30: error: no member named 'library_version_type' in namespace 'boost::serialization'
    if(boost::serialization::library_version_type(3) < library_version){
       ~~~~~~~~~~~~~~~~~~~~~~^
/Users/myuser/Projects/myproject/monero-16/src/cryptonote_core/blockchain.cpp:1183:21: warning: loop variable 'bei' of type 'const cryptonote::Blockchain::block_extended_info'
      creates a copy from type 'const cryptonote::Blockchain::block_extended_info' [-Wrange-loop-analysis]
    for (const auto bei: boost::adaptors::reverse(alt_chain))
                    ^
/Users/myuser/Projects/myproject/monero-16/src/cryptonote_core/blockchain.cpp:1183:10: note: use reference type 'const cryptonote::Blockchain::block_extended_info &' to
      prevent copying
    for (const auto bei: boost::adaptors::reverse(alt_chain))
         ^~~~~~~~~~~~~~~
                    &
In file included from /Users/myuser/Projects/myproject/monero-16/src/cryptonote_core/blockchain.cpp:37:
In file included from /Users/myuser/Projects/myproject/monero-16/src/cryptonote_basic/cryptonote_basic_impl.h:33:
In file included from /Users/myuser/Projects/myproject/monero-16/src/cryptonote_basic/cryptonote_basic.h:41:
/Users/myuser/Projects/myproject/monero-16/src/serialization/binary_archive.h:195:28: warning: shift count >= width of type [-Wshift-count-overflow]
      if (1 < sizeof(T)) v >>= 8;
                           ^   ~
/Users/myuser/Projects/myproject/monero-16/src/serialization/binary_archive.h:188:5: note: in instantiation of function template specialization
      'binary_archive<true>::serialize_uint<unsigned char>' requested here
    serialize_uint(static_cast<typename boost::make_unsigned<T>::type>(v));
    ^
/Users/myuser/Projects/myproject/monero-16/src/serialization/binary_archive.h:228:5: note: in instantiation of function template specialization
      'binary_archive<true>::serialize_int<unsigned char>' requested here
    serialize_int(t);
    ^
2 warnings and 2 errors generated.
make[3]: *** [src/cryptonote_core/CMakeFiles/obj_cryptonote_core.dir/blockchain.cpp.o] Error 1
make[2]: *** [src/cryptonote_core/CMakeFiles/obj_cryptonote_core.dir/all] Error 2
make[1]: *** [all] Error 2
make: *** [release-all] Error 2`

My boost version: Boost version: 1_74

# Discussion History
## selsta | 2020-12-07T11:56:13+00:00
Why are you trying to compile release-v0.16 and not release-v0.17?

## IvRRimum | 2020-12-07T11:59:06+00:00
Just what i have setup localy.

## selsta | 2020-12-07T12:00:36+00:00
v0.16 is outdated and not supported anymore.

If you really need to compile v0.16 then try downgrading your boost version to 1.70

# Action History
- Created by: IvRRimum | 2020-12-07T11:55:02+00:00
- Closed at: 2021-10-06T02:49:45+00:00
