---
title: Fails to build with Boost 1.70 (Beta1)
source_url: https://github.com/monero-project/monero/issues/5304
author: jbeich
assignees: []
labels: []
created_at: '2019-03-17T13:46:27+00:00'
updated_at: '2019-03-21T13:25:51+00:00'
type: issue
status: closed
closed_at: '2019-03-21T13:25:51+00:00'
---

# Original Description
Regressed by boostorg/asio@a72fbb0b867f. Also reported in hyle-team/epee#1.
```c++
In file included from src/rpc/daemon_handler.cpp:29:
In file included from src/rpc/daemon_handler.h:36:
In file included from src/p2p/net_node.h:47:
In file included from contrib/epee/include/net/abstract_tcp_server2.h:393:
contrib/epee/include/net/abstract_tcp_server2.inl:102:19: error: no member named 'get_io_service' in
      'boost::asio::ssl::stream<boost::asio::basic_stream_socket<boost::asio::ip::tcp, boost::asio::executor> >'
                m_timer(socket_.get_io_service()),
                        ~~~~~~~ ^
contrib/epee/include/net/abstract_tcp_server2.inl:1210:64: error: no member named 'get_io_service' in
      'boost::asio::basic_stream_socket<boost::asio::ip::tcp, boost::asio::executor>'
    if(std::addressof(get_io_service()) == std::addressof(sock.get_io_service()))
                                                          ~~~~ ^
2 errors generated.
```


# Discussion History
## moneromooo-monero | 2019-03-21T11:02:53+00:00
Thanks for the report, fixed in https://github.com/monero-project/monero/pull/5328

## moneromooo-monero | 2019-03-21T13:22:06+00:00
+resolved

# Action History
- Created by: jbeich | 2019-03-17T13:46:27+00:00
- Closed at: 2019-03-21T13:25:51+00:00
