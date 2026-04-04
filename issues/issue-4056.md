---
title: Make from Source Code on Ubunto 14.04 Failing at 45%
source_url: https://github.com/monero-project/monero/issues/4056
author: spencershaw
assignees: []
labels:
- invalid
created_at: '2018-06-26T10:53:34+00:00'
updated_at: '2018-07-12T22:57:00+00:00'
type: issue
status: closed
closed_at: '2018-07-12T22:57:00+00:00'
---

# Original Description
Make fails at 45%
```
[ 43%] Built target cryptonote_protocol
make[3]: Entering directory `/home/spencer/monero/build/release'
Scanning dependencies of target serialization
make[3]: Leaving directory `/home/spencer/monero/build/release'
make[3]: Entering directory `/home/spencer/monero/build/release'
Linking CXX static library libserialization.a
make[3]: Leaving directory `/home/spencer/monero/build/release'
[ 43%] Built target serialization
make[3]: Entering directory `/home/spencer/monero/build/release'
Scanning dependencies of target daemon_messages
make[3]: Leaving directory `/home/spencer/monero/build/release'
make[3]: Entering directory `/home/spencer/monero/build/release'
Linking CXX static library libdaemon_messages.a
make[3]: Leaving directory `/home/spencer/monero/build/release'
[ 43%] Built target daemon_messages
make[3]: Entering directory `/home/spencer/monero/build/release'
Scanning dependencies of target obj_rpc_base
make[3]: Leaving directory `/home/spencer/monero/build/release'
make[3]: Entering directory `/home/spencer/monero/build/release'
[ 44%] Building CXX object src/rpc/CMakeFiles/obj_rpc_base.dir/rpc_args.cpp.o
make[3]: Leaving directory `/home/spencer/monero/build/release'
[ 44%] Built target obj_rpc_base
make[3]: Entering directory `/home/spencer/monero/build/release'
Scanning dependencies of target rpc_base
make[3]: Leaving directory `/home/spencer/monero/build/release'
make[3]: Entering directory `/home/spencer/monero/build/release'
Linking CXX static library librpc_base.a
make[3]: Leaving directory `/home/spencer/monero/build/release'
[ 44%] Built target rpc_base
make[3]: Entering directory `/home/spencer/monero/build/release'
Scanning dependencies of target obj_rpc
make[3]: Leaving directory `/home/spencer/monero/build/release'
make[3]: Entering directory `/home/spencer/monero/build/release'
[ 45%] Building CXX object src/rpc/CMakeFiles/obj_rpc.dir/core_rpc_server.cpp.o
In file included from /home/spencer/monero/contrib/epee/include/net/http_protoco                                                                             l_handler.h:229:0,
                 from /home/spencer/monero/contrib/epee/include/net/http_server_                                                                             cp2.h:34,
                 from /home/spencer/monero/contrib/epee/include/net/http_server_                                                                             impl_base.h:36,
                 from /home/spencer/monero/src/rpc/core_rpc_server.h:36,
                 from /home/spencer/monero/src/rpc/core_rpc_server.cpp:35:
/home/spencer/monero/contrib/epee/include/net/http_protocol_handler.inl: In func                                                                             tion ‘bool epee::net_utils::http::analize_http_method(const smatch&, epee::net_u                                                                             tils::http::http_method&, int&, int&)’:
/home/spencer/monero/contrib/epee/include/net/http_protocol_handler.inl:331:56:                                                                              warning: ‘result’ may be used uninitialized in this function [-Wmaybe-uninitiali                                                                             zed]
   http_ver_minor = boost::lexical_cast<int>(result[12]);
                                                        ^
/home/spencer/monero/contrib/epee/include/net/http_protocol_handler.inl:330:56:                                                                              warning: ‘result’ may be used uninitialized in this function [-Wmaybe-uninitiali                                                                             zed]
   http_ver_major = boost::lexical_cast<int>(result[11]);
                                                        ^

```

# Discussion History
## moneromooo-monero | 2018-06-26T21:20:11+00:00
I see no errors. Paste those please.

## moneromooo-monero | 2018-07-12T22:09:52+00:00
Reopen if you can provide the log with the errors.

+invalid

# Action History
- Created by: spencershaw | 2018-06-26T10:53:34+00:00
- Closed at: 2018-07-12T22:57:00+00:00
