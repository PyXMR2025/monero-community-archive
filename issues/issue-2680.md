---
title: 'Latest master (11608) fails to build: error: ‘SSL_R_SHORT_READ’ was not declared
  in this scope'
source_url: https://github.com/monero-project/monero/issues/2680
author: emesik
assignees: []
labels: []
created_at: '2017-10-18T22:48:03+00:00'
updated_at: '2017-10-19T00:51:08+00:00'
type: issue
status: closed
closed_at: '2017-10-19T00:51:08+00:00'
---

# Original Description
I can't build latest master. I have `boost-1.65.1-1`  `boost-libs-1.65.1-1`  `openssl-1.1.0.f-2` installed, running Arch Linux.

```
[ 16%] Building CXX object src/common/CMakeFiles/obj_common.dir/download.cpp.o
In file included from /usr/include/openssl/engine.h:30:0,
                 from /usr/include/boost/asio/ssl/detail/openssl_types.hpp:23,
                 from /usr/include/boost/asio/ssl/context_base.hpp:19,
                 from /usr/include/boost/asio/ssl/context.hpp:27,
                 from /usr/include/boost/asio/ssl.hpp:19,
                 from /home/emes/devel/monero/contrib/epee/include/net/net_helper.h:40,
                 from /home/emes/devel/monero/contrib/epee/include/net/http_client.h:40,
                 from /home/emes/devel/monero/src/common/download.cpp:36:
/home/emes/devel/monero/contrib/epee/include/net/net_helper.h: In member function ‘void epee::net_utils::blocked_mode_client::shutdown_ssl()’:
/home/emes/devel/monero/contrib/epee/include/net/net_helper.h:579:106: error: ‘SSL_R_SHORT_READ’ was not declared in this scope
    if (ec.category() == boost::asio::error::get_ssl_category() && ec.value() != ERR_PACK(ERR_LIB_SSL, 0, SSL_R_SHORT_READ))
                                                                                                          ^
/home/emes/devel/monero/contrib/epee/include/net/net_helper.h:579:106: note: suggested alternative: ‘SSL_F_SSL_READ’
make[2]: *** [src/common/CMakeFiles/obj_common.dir/build.make:135: src/common/CMakeFiles/obj_common.dir/download.cpp.o] Error 1
make[1]: *** [CMakeFiles/Makefile2:553: src/common/CMakeFiles/obj_common.dir/all] Error 2
make[1]: *** Waiting for unfinished jobs....
```

# Discussion History
## moneromooo-monero | 2017-10-18T23:32:21+00:00
https://github.com/monero-project/monero/pull/2663

## emesik | 2017-10-19T00:51:08+00:00
Great, it works.

# Action History
- Created by: emesik | 2017-10-18T22:48:03+00:00
- Closed at: 2017-10-19T00:51:08+00:00
