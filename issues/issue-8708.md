---
title: 'Exception: boost::wrapexcept<boost::system::system_error> when using Tor +
  ipv6'
source_url: https://github.com/monero-project/monero/issues/8708
author: ovhpse
assignees: []
labels: []
created_at: '2023-01-14T16:23:27+00:00'
updated_at: '2023-01-21T09:50:53+00:00'
type: issue
status: closed
closed_at: '2023-01-21T09:50:53+00:00'
---

# Original Description
Hello,

This exception is happening when I build Monero myself and not with the binary release.

```
Exception: boost::wrapexcept<boost::system::system_error>
Unwound call stack:
     1                  0x555555d2c559 __wrap___cxa_throw + 0xbf
     2                  0x5555557647a0 void boost::throw_exception<boost::system::system_error>(boost::system::system_error const&) + 0x57
     3                  0x55555575322c boost::asio::detail::do_throw_error(boost::system::error_code const&, char const*) + 0x47
     4                  0x555555753185 boost::asio::detail::throw_error(boost::system::error_code const&, char const*) + 0x37
     5                  0x55555577d43f boost::asio::ip::basic_resolver<boost::asio::ip::tcp, boost::asio::any_io_executor>::resolve(boost::asio::ip::basic_resolver_query<boost::asio::ip::tcp> const&) + 0x93
     6                  0x555555b55922 epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::init_server(unsigned int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, unsigned int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, bool, bool, epee::net_utils::ssl_options_t) + 0x74a
     7                  0x555555b3f243 epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::init_server(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, bool, bool, epee::net_utils::ssl_options_t) + 0x2cb
     8                  0x555555b00918 nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::init(boost::program_options::variables_map const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, bool) + 0xeae
     9                  0x5555557605de daemonize::t_p2p::t_p2p(boost::program_options::variables_map const&, daemonize::t_protocol&) + 0x13c
     a                  0x5555557623b7 daemonize::t_internals::t_internals(boost::program_options::variables_map const&) + 0xbf
     b                  0x55555573be0e daemonize::t_daemon::t_daemon(boost::program_options::variables_map const&, unsigned short) + 0x44
     c                  0x5555557ffbe9 daemonize::t_executor::run_non_interactive(boost::program_options::variables_map const&) + 0x41
     d                  0x555555816748 bool daemonizer::daemonize<daemonize::t_executor>(int, char const**, daemonize::t_executor&&, boost::program_options::variables_map const&) + 0x1a7
     e                  0x555555802a57 main + 0x1547
     f                  0x7ffff716a510 __libc_start_call_main + 0x80
    10                  0x7ffff716a5c9 __libc_start_main + 0x89
    11                  0x5555556369e5 _start + 0x25
```

After using GDB I found that the exception happen when we make the following call to `resolver.resolve(query)`  :

```
(gdb) print query
$17 = {<boost::asio::ip::resolver_query_base> = {<boost::asio::ip::resolver_base> = {<No data fields>}, <No data fields>}, hints_ = {ai_flags = 2, ai_family = 0, ai_socktype = 1, ai_protocol = 6, ai_addrlen = 0, ai_addr = 0x0, 
    ai_canonname = 0x0, ai_next = 0x0}, host_name_ = "", service_name_ = "18083"}
```

What is suspicious is the absence of hostname, as the preceding calls are ok:

```
(gdb) print query
$16 = {<boost::asio::ip::resolver_query_base> = {<boost::asio::ip::resolver_base> = {<No data fields>}, <No data fields>}, hints_ = {ai_flags = 2, ai_family = 0, ai_socktype = 1, ai_protocol = 6, ai_addrlen = 0, ai_addr = 0x0, 
    ai_canonname = 0x0, ai_next = 0x0}, host_name_ = "127.0.0.1", service_name_ = "18083"}
```

```
(gdb) print query
$15 = {<boost::asio::ip::resolver_query_base> = {<boost::asio::ip::resolver_base> = {<No data fields>}, <No data fields>}, hints_ = {ai_flags = 2, ai_family = 0, ai_socktype = 1, ai_protocol = 6, ai_addrlen = 0, ai_addr = 0x0, 
    ai_canonname = 0x0, ai_next = 0x0}, host_name_ = "::", service_name_ = "18080"}
```

```
(gdb) print query
$12 = {<boost::asio::ip::resolver_query_base> = {<boost::asio::ip::resolver_base> = {<No data fields>}, <No data fields>}, hints_ = {ai_flags = 2, ai_family = 0, ai_socktype = 1, ai_protocol = 6, ai_addrlen = 0, ai_addr = 0x0, 
    ai_canonname = 0x0, ai_next = 0x0}, host_name_ = "0.0.0.0", service_name_ = "18080"}
```

# Discussion History
## ovhpse | 2023-01-21T09:50:53+00:00
See #8702

# Action History
- Created by: ovhpse | 2023-01-14T16:23:27+00:00
- Closed at: 2023-01-21T09:50:53+00:00
