---
title: gcc 5 (experimental C++14 support) and boost-1.57
source_url: https://github.com/monero-project/monero/issues/231
author: otila
assignees: []
labels: []
created_at: '2015-02-21T11:03:00+00:00'
updated_at: '2015-05-26T08:45:06+00:00'
type: issue
status: closed
closed_at: '2015-05-26T08:45:06+00:00'
---

# Original Description
```
/c/bitmonero/contrib/epee/include/storages/portable_storage.h:430:16: warning: converting to ‘bool’ from ‘std::nullptr_t’ requires direct-initialization [-fpermissive]
         return nullptr;
                ^
```

```
/c/bitmonero/src/p2p/net_node.inl:1108:370: error: redeclaration of ‘const peerid_type pr’
In file included from /c/bitmonero/src/p2p/net_node.h:254:0,
                 from /c/bitmonero/src/daemon/daemon.cpp:44:
/c/bitmonero/src/p2p/net_node.inl:1106:37: note: ‘const peerid_type pr’ previously declared here
         if(rsp.status != PING_OK_RESPONSE_STATUS_TEXT || pr != rsp.peer_id)
                                     ^
```

```
/c/bitmonero/src/p2p/net_node.inl:1098:9: sorry, unimplemented: non-trivial designated initializers not supported
         [=](int code, const COMMAND_PING::response& rsp, p2p_connection_context& context)
         ^
```


# Discussion History
## otila | 2015-03-05T18:33:53+00:00
clang 3.6.0.RELEASE has no problems compiling it, though :)


# Action History
- Created by: otila | 2015-02-21T11:03:00+00:00
- Closed at: 2015-05-26T08:45:06+00:00
