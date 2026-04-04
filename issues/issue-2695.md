---
title: 'net_helper.h:579:106: error: ‘SSL_R_SHORT_READ’ was not declared in this scope'
source_url: https://github.com/monero-project/monero/issues/2695
author: moneroexamples
assignees: []
labels: []
created_at: '2017-10-21T07:43:41+00:00'
updated_at: '2017-10-21T08:09:41+00:00'
type: issue
status: closed
closed_at: '2017-10-21T08:09:41+00:00'
---

# Original Description
On arch/manjaro

```
home/mwo/monero/contrib/epee/include/net/net_helper.h: In member function ‘void epee::net_utils::blocked_mode_client::shutdown_ssl()’:
/home/mwo/monero/contrib/epee/include/net/net_helper.h:579:106: error: ‘SSL_R_SHORT_READ’ was not declared in this scope
    if (ec.category() == boost::asio::error::get_ssl_category() && ec.value() != ERR_PACK(ERR_LIB_SSL, 0, SSL_R_SHORT_READ))
                                                                                                          ^
/home/mwo/monero/contrib/epee/include/net/net_helper.h:579:106: note: suggested alternative: ‘SSL_F_SSL_READ’
[ 22%] Building CXX object src/cryptonote_core/CMakeFiles/obj_cryptonote_core.dir/tx_pool.cpp.o
make[3]: *** [src/cryptonote_core/CMakeFiles/obj_cryptonote_core.dir/build.make:87: src/cryptonote_core/CMakeFiles/obj_cryptonote_core.dir/cryptonote_core.cpp.o] Error 1
make[3]: *** Waiting for unfinished jobs....
make[3]: Leaving directory '/home/mwo/monero/build/release'
make[2]: *** [CMakeFiles/Makefile2:1081: src/cryptonote_core/CMakeFiles/obj_cryptonote_core.dir/all] Error 2
make[3]: Leaving directory '/home/mwo/monero/build/release'
[ 22%] Built target obj_cryptonote_basic
make[2]: Leaving directory '/home/mwo/monero/build/release'
make[1]: *** [Makefile:141: all] Error 2
make[1]: Leaving directory '/home/mwo/monero/build/release'
make: *** [Makefile:63: release-all] Error 2
```

Monero version:

```
git log -1
commit 8d511f3c2486d22400cdd69c8d3640ee2d20aeff (HEAD -> master, origin/master, origin/HEAD)
Merge: 48af25ed 4d35ad76
Author: Riccardo Spagni <ric@spagni.net>
Date:   Sun Oct 15 21:36:36 2017 +0200

    Merge pull request #2601
    
    4d35ad76 Fix compiler warnings with Clang 6.0.0. (Vasil Dimov)
```

# Discussion History
## moneromooo-monero | 2017-10-21T07:48:32+00:00
https://github.com/monero-project/monero/pull/2663

## moneroexamples | 2017-10-21T08:09:41+00:00
It compiles now. thx.

# Action History
- Created by: moneroexamples | 2017-10-21T07:43:41+00:00
- Closed at: 2017-10-21T08:09:41+00:00
