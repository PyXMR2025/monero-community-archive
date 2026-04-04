---
title: 'build monero for android failed  '
source_url: https://github.com/monero-project/monero/issues/3739
author: jianjunchu
assignees: []
labels: []
created_at: '2018-05-01T05:55:54+00:00'
updated_at: '2021-08-13T04:28:04+00:00'
type: issue
status: closed
closed_at: '2021-08-13T04:28:03+00:00'
---

# Original Description
build under Ubuntu 64 bit

followed the instructions:
https://forum.getmonero.org/5/support/87643/building-monero-v0-10-3-1-for-android
and
https://github.com/m2049r/xmrwallet/blob/master/doc/BUILDING-external-libs.md

found an error:   the specified comparator type does not provide a const call operator
Is there something wrong ?

====logs========
[ 72%] Building CXX object src/wallet/api/CMakeFiles/obj_wallet_api.dir/pending_transaction.cpp.o
[ 73%] Building CXX object src/wallet/api/CMakeFiles/obj_wallet_api.dir/utils.cpp.o
[ 73%] Building CXX object src/wallet/api/CMakeFiles/obj_wallet_api.dir/address_book.cpp.o
[ 75%] Building CXX object src/wallet/api/CMakeFiles/obj_wallet_api.dir/subaddress.cpp.o
[ 75%] Building CXX object src/wallet/api/CMakeFiles/obj_wallet_api.dir/subaddress_account.cpp.o
[ 75%] Building CXX object src/wallet/api/CMakeFiles/obj_wallet_api.dir/unsigned_transaction.cpp.o
[ 75%] Built target obj_wallet_api
[ 76%] Building CXX object src/cryptonote_core/CMakeFiles/obj_cryptonote_core.dir/cryptonote_core.cpp.o
In file included from /opt/android/monero/src/cryptonote_core/cryptonote_core.cpp:33:
In file included from /opt/android/monero/contrib/epee/include/include_base_utils.h:32:
In file included from /opt/android/monero/contrib/epee/include/misc_log_ex.h:33:
In file included from /opt/android/monero/external/easylogging++/easylogging++.h:383:
In file included from /opt/android/tool/x86_64/bin/../lib/gcc/x86_64-linux-android/4.9.x/../../../../include/c++/4.9.x/map:442:
/opt/android/tool/x86_64/bin/../lib/gcc/x86_64-linux-android/4.9.x/../../../../include/c++/4.9.x/__tree:1819:22: error: the specified comparator type does
      not provide a const call operator [-Werror,-Wuser-defined-warnings]
                     __trigger_diagnostics()), "");
                     ^
/opt/android/tool/x86_64/bin/../lib/gcc/x86_64-linux-android/4.9.x/../../../../include/c++/4.9.x/__tree:960:70: note: in instantiation of member function
      'std::__ndk1::__tree<std::__ndk1::pair<std::__ndk1::pair<double, long>, crypto::hash>, cryptonote::txCompare,
      std::__ndk1::allocator<std::__ndk1::pair<std::__ndk1::pair<double, long>, crypto::hash> > >::~__tree' requested here
    template <class, class, class> friend class _LIBCPP_TEMPLATE_VIS set;
                                                                     ^
/opt/android/tool/x86_64/bin/../lib/gcc/x86_64-linux-android/4.9.x/../../../../include/c++/4.9.x/__tree:970:7: note: from 'diagnose_if' attribute on
      '__trigger_diagnostics':
      _LIBCPP_DIAGNOSE_WARNING(!__invokable<_Compare const&, _Tp const&, _Tp const&>::value,
      ^                        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
/opt/android/tool/x86_64/bin/../lib/gcc/x86_64-linux-android/4.9.x/../../../../include/c++/4.9.x/__config:1095:20: note: expanded from macro
      '_LIBCPP_DIAGNOSE_WARNING'
    __attribute__((diagnose_if(__VA_ARGS__, "warning")))
                   ^           ~~~~~~~~~~~
1 error generated.
src/cryptonote_core/CMakeFiles/obj_cryptonote_core.dir/build.make:86: recipe for target 'src/cryptonote_core/CMakeFiles/obj_cryptonote_core.dir/cryptonote_core.cpp.o' failed
make[3]: *** [src/cryptonote_core/CMakeFiles/obj_cryptonote_core.dir/cryptonote_core.cpp.o] Error 1
make[3]: *** Waiting for unfinished jobs....
Scanning dependencies of target epee
[ 78%] Building CXX object contrib/epee/src/CMakeFiles/epee.dir/hex.cpp.o
[ 78%] Building CXX object contrib/epee/src/CMakeFiles/epee.dir/http_auth.cpp.o
[ 79%] Building CXX object contrib/epee/src/CMakeFiles/epee.dir/mlog.cpp.o


# Discussion History
## moneromooo-monero | 2018-09-04T23:05:46+00:00
Current master fixes Android build issues, probably fixes yours too, please try again and report.


## moneromooo-monero | 2018-10-27T12:13:53+00:00
ping

## selsta | 2021-08-13T04:28:03+00:00
No reply from issue creator and also no longer relevant.

# Action History
- Created by: jianjunchu | 2018-05-01T05:55:54+00:00
- Closed at: 2021-08-13T04:28:03+00:00
