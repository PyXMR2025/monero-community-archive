---
title: build obj_wallet_api fails on macOS 10.13.4 with boost 1.67.0_1
source_url: https://github.com/monero-project/monero-gui/issues/1335
author: teutat3s
assignees: []
labels:
- resolved
created_at: '2018-04-21T01:00:11+00:00'
updated_at: '2018-07-04T09:27:33+00:00'
type: issue
status: closed
closed_at: '2018-07-04T09:27:33+00:00'
---

# Original Description
Dear Contributors, 

when building monero-gui on freshly setup macOS High Sierra 10.13.4 with all dependencies (boost 1.67.0_1) and already using patch from PR https://github.com/monero-project/monero/pull/3667 

build still breaks as follows:


`Scanning dependencies of target obj_wallet_api
[ 57%] Building CXX object src/wallet/api/CMakeFiles/obj_wallet_api.dir/wallet.cpp.o
Scanning dependencies of target obj_rpc_base
[ 57%] Building CXX object src/rpc/CMakeFiles/obj_rpc_base.dir/rpc_args.cpp.o
1 warning generated.
1 warning generated.
[ 59%] Building CXX object src/wallet/api/CMakeFiles/obj_wallet_api.dir/wallet_manager.cpp.o
[ 59%] Building CXX object src/wallet/api/CMakeFiles/obj_wallet_api.dir/transaction_info.cpp.o
[ 59%] Built target obj_rpc_base
[ 59%] Built target obj_cryptonote_core
[ 60%] Building CXX object src/wallet/api/CMakeFiles/obj_wallet_api.dir/transaction_history.cpp.o
[ 60%] Building CXX object src/wallet/api/CMakeFiles/obj_wallet_api.dir/pending_transaction.cpp.o
Scanning dependencies of target epee
/Users/admin/codeRoom/monero-gui/monero/src/wallet/api/wallet.cpp:1755:45: error:
      no matching constructor for initialization of
      'boost::posix_time::milliseconds' (aka
      'subsecond_duration<boost::posix_time::time_duration, 1000>')
  ...boost::posix_time::milliseconds wait_for_ms(m_refreshIntervalMillis);
                                     ^           ~~~~~~~~~~~~~~~~~~~~~~~
/usr/local/include/boost/date_time/time_duration.hpp:270:30: note: candidate
      constructor (the implicit copy constructor) not viable: no known
      conversion from 'std::atomic<int>' to 'const
      boost::date_time::subsecond_duration<boost::posix_time::time_duration,
      1000>' for 1st argument
  class BOOST_SYMBOL_VISIBLE subsecond_duration : public base_duration
                             ^
/usr/local/include/boost/date_time/time_duration.hpp:270:30: note: candidate
      constructor (the implicit move constructor) not viable: no known
      conversion from 'std::atomic<int>' to
      'boost::date_time::subsecond_duration<boost::posix_time::time_duration,
      1000>' for 1st argument
/usr/local/include/boost/date_time/time_duration.hpp:286:59: note: candidate
      template ignored: disabled by 'enable_if' [with T = std::__1::atomic<int>]
                                typename boost::enable_if<boost::is_inte...
                                                          ^
In file included from /Users/admin/codeRoom/monero-gui/monero/src/wallet/api/wallet.cpp:32:
In file included from /Users/admin/codeRoom/monero-gui/monero/src/wallet/api/wallet.h:35:
In file included from /Users/admin/codeRoom/monero-gui/monero/src/wallet/wallet2.h:43:
In file included from /Users/admin/codeRoom/monero-gui/monero/src/cryptonote_basic/account.h:33:
In file included from /Users/admin/codeRoom/monero-gui/monero/src/cryptonote_basic/cryptonote_basic.h:41:
/Users/admin/codeRoom/monero-gui/monero/src/serialization/binary_archive.h:194:28: warning:
      shift count >= width of type [-Wshift-count-overflow]
      if (1 < sizeof(T)) v >>= 8;
                           ^   ~
/Users/admin/codeRoom/monero-gui/monero/src/serialization/binary_archive.h:187:5: note:
      in instantiation of function template specialization
      'binary_archive<true>::serialize_uint<unsigned char>' requested here
    serialize_uint(static_cast<typename boost::make_unsigned<T>::type>(v));
    ^
/Users/admin/codeRoom/monero-gui/monero/src/serialization/binary_archive.h:227:5: note:
      in instantiation of function template specialization
      'binary_archive<true>::serialize_int<unsigned char>' requested here
    serialize_int(t);
    ^
[ 62%] Building CXX object contrib/epee/src/CMakeFiles/epee.dir/hex.cpp.o
[ 62%] Built target obj_cryptonote_basic
[ 64%] Building CXX object src/wallet/api/CMakeFiles/obj_wallet_api.dir/utils.cpp.o
[ 65%] Building CXX object contrib/epee/src/CMakeFiles/epee.dir/http_auth.cpp.o
Scanning dependencies of target obj_common
1 warning and 1 error generated.
make[2]: *** [src/wallet/api/CMakeFiles/obj_wallet_api.dir/wallet.cpp.o] Error 1
make[2]: *** Waiting for unfinished jobs....`

[Here's the complete build log until error](https://gist.github.com/Teutone/d8969d8b705b6ab16335661447e677cd)

Building just monero works fine applying the mentioned PR patch. Problems seems to be with the wallet_api code ...

Thank you for coding for monero, keep it up!

EDIT: I can confirm that building monero-gui with boost 1.60.0 and patch from PR #1247 works fine on the same machine. Just a lot of warnings ...

# Discussion History
## iedemam | 2018-04-30T10:37:11+00:00
I believe I've fixed this for Intense Coin in https://github.com/valiant1x/intensecoin/commit/e1fe653725f0517131befbb6655c571ced219f46

Still waiting on feedback internally but wanted the Monero team to have it as well.

## dEBRUYNE-1 | 2018-07-04T08:41:39+00:00
+resolved

# Action History
- Created by: teutat3s | 2018-04-21T01:00:11+00:00
- Closed at: 2018-07-04T09:27:33+00:00
