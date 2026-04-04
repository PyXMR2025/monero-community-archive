---
title: ' error: implicit declaration of function ‘strdup’; did you mean ‘strcmp’?'
source_url: https://github.com/monero-project/monero/issues/9619
author: moneroexamples
assignees: []
labels: []
created_at: '2024-12-16T10:15:44+00:00'
updated_at: '2024-12-22T22:25:25+00:00'
type: issue
status: closed
closed_at: '2024-12-22T22:25:25+00:00'
---

# Original Description
gcc version 14.2.1 20241116 (Gentoo 14.2.1_p20241116 p3)

Monero: v0.18.3.4, last commit: 58a1d54a4f90a235616ede3f8ebae2b8dca41589

compilation fails on gentoo:

```
[ 60%] Building C object external/miniupnp/miniupnpc/CMakeFiles/listdevices.dir/listdevices.c.o
/home/mwo/monero/external/miniupnp/miniupnpc/listdevices.c: In function ‘add_device’:
/home/mwo/monero/external/miniupnp/miniupnpc/listdevices.c:60:24: error: implicit declaration of function ‘strdup’; did you mean ‘strcmp’? [-Wimplicit-function-declaration]
   60 |         elt->descURL = strdup(dev->descURL);
      |                        ^~~~~~
      |                        strcmp
/home/mwo/monero/external/miniupnp/miniupnpc/listdevices.c:60:22: error: assignment to ‘char *’ from ‘int’ makes pointer from integer without a cast [-Wint-conversion]
   60 |         elt->descURL = strdup(dev->descURL);
      |                      ^
make[3]: *** [external/miniupnp/miniupnpc/CMakeFiles/listdevices.dir/build.make:76: external/miniupnp/miniupnpc/CMakeFiles/listdevices.dir/listdevices.c.o] Error 1
make[2]: *** [CMakeFiles/Makefile2:1307: external/miniupnp/miniupnpc/CMakeFiles/listdevices.dir/all] Error 2
make[2]: *** Waiting for unfinished jobs....
In file included from /usr/lib/gcc/x86_64-pc-linux-gnu/14/include/g++-v14/bits/exception_ptr.h:37,
                 from /usr/lib/gcc/x86_64-pc-linux-gnu/14/include/g++-v14/exception:166,
                 from /usr/lib/gcc/x86_64-pc-linux-gnu/14/include/g++-v14/stdexcept:38,
                 from /usr/lib/gcc/x86_64-pc-linux-gnu/14/include/g++-v14/system_error:43,
                 from /usr/lib/gcc/x86_64-pc-linux-gnu/14/include/g++-v14/bits/ios_base.h:46,
                 from /usr/lib/gcc/x86_64-pc-linux-gnu/14/include/g++-v14/bits/locale_facets.h:43,
                 from /usr/lib/gcc/x86_64-pc-linux-gnu/14/include/g++-v14/locale:42,
                 from /usr/include/boost/format.hpp:23,
                 from /home/mwo/monero/src/wallet/wallet2.cpp:35:
In member function ‘bool std::type_info::operator==(const std::type_info&) const’,
    inlined from ‘bool std::type_info::operator!=(const std::type_info&) const’ at /usr/lib/gcc/x86_64-pc-linux-gnu/14/include/g++-v14/typeinfo:114:25,
    inlined from ‘epee::serialization::array_entry* epee::serialization::portable_storage::insert_first_value(const std::string&, t_value&&, hsection) [with t_value = long unsigned int]’ at /home/mwo/monero/contrib/epee/include/storages/portable_storage.h:266:25:
/usr/lib/gcc/x86_64-pc-linux-gnu/14/include/g++-v14/typeinfo:205:49: warning: ‘int __builtin_strcmp(const char*, const char*)’ of a string of length 282 and an array of size 53 evaluates to nonzero [-Wstring-compare]
  205 |     return __name[0] != '*' && __builtin_strcmp (__name, __arg.name()) == 0;
      |                                ~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~~~
[ 60%] Built target obj_wallet
make[1]: *** [Makefile:146: all] Error 2
make[1]: Leaving directory '/home/mwo/monero/build/release'
make: *** [Makefile:103: release-all] Error 2
```


# Discussion History
## selsta | 2024-12-16T17:29:48+00:00
https://github.com/monero-project/monero/issues/9618#issuecomment-2543163149

## selsta | 2024-12-22T22:25:25+00:00
Closing as a duplicate.

# Action History
- Created by: moneroexamples | 2024-12-16T10:15:44+00:00
- Closed at: 2024-12-22T22:25:25+00:00
