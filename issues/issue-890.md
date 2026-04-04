---
title: monero make error
source_url: https://github.com/monero-project/monero/issues/890
author: shaoxianduiyuan007
assignees: []
labels: []
created_at: '2016-07-08T07:06:02+00:00'
updated_at: '2016-12-15T17:37:51+00:00'
type: issue
status: closed
closed_at: '2016-12-15T17:37:51+00:00'
---

# Original Description
`
/usr/include/boost/filesystem/path.hpp:300:5: note:   template argument deduction/substitution failed:
/usr/include/boost/filesystem/path.hpp: In substitution of ‘template<class Source> typename boost::enable_if<boost::filesystem::path_traits::is_pathable<typename boost::decay<F>::type>, boost::filesystem::path&>::type boost::filesystem::path::operator/=(const Source&) [with Source = boost::sub_match<__gnu_cxx::__normal_iterator<const char*, std::basic_string<char> > >]’:
/root/bitmonero/src/wallet/api/wallet_manager.cpp:104:66:   required from here
/usr/include/boost/filesystem/path.hpp:300:5: error: no type named ‘type’ in ‘struct boost::enable_if<boost::filesystem::path_traits::is_pathable<boost::sub_match<__gnu_cxx::__normal_iterator<const char*, std::basic_string<char> > > >, boost::filesystem::path&>’
make[3]: *** [src/wallet/CMakeFiles/wallet.dir/api/wallet_manager.cpp.o] Error 1
make[3]: Leaving directory '/root/bitmonero/build/release'
make[2]: *** [src/wallet/CMakeFiles/wallet.dir/all] Error 2
make[2]: Leaving directory '/root/bitmonero/build/release'
make[1]: *** [all] Error 2
make[1]: Leaving directory '/root/bitmonero/build/release'
make: *** [release-all] Error 2
`

> Use libboost 1.55
> Use libboost 1.55
> Use libboost 1.55


# Discussion History
## moneromooo-monero | 2016-07-08T19:10:21+00:00
More information would be helpful. In particular the call site from the monero tree (there may be like a dozen layers in the output). Also GCC version, and 32/64 bit of your arch.


## iDunk5400 | 2016-07-08T21:10:53+00:00
IIRC, that output comes after the /= operator error. Should be fixed in #889 and is already merged in master.


## shaoxianduiyuan007 | 2016-07-11T00:55:38+00:00
ubuntu 14 x64


## ghost | 2016-09-15T14:57:11+00:00
@shaoxianduiyuan007 is this issue still present or can it be closed?


## luigi1111 | 2016-12-15T17:37:51+00:00
Assume fixed in #889. If not please reopen with more information.

# Action History
- Created by: shaoxianduiyuan007 | 2016-07-08T07:06:02+00:00
- Closed at: 2016-12-15T17:37:51+00:00
