---
title: cli/rpc can't connect to daemon
source_url: https://github.com/monero-project/monero/issues/3834
author: CamilleScholtz
assignees: []
labels: []
created_at: '2018-05-19T19:27:46+00:00'
updated_at: '2018-05-20T14:38:09+00:00'
type: issue
status: closed
closed_at: '2018-05-20T14:37:46+00:00'
---

# Original Description
log, I can't figure out what's going on here...

```
2018-05-19 19:09:38.747	    7fd13cbd0780	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: boost::exception_detail::clone_impl<boost::exception_detail::error_info_injector<boost::system::system_error> >
2018-05-19 19:09:38.747	    7fd13cbd0780	INFO 	stacktrace	src/common/stack_trace.cpp:125	Unwound call stack:
2018-05-19 19:09:38.749	    7fd13cbd0780	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [1] monero-wallet-rpc:__cxa_throw+0x10a [0x55cdbaf1f5da]
2018-05-19 19:09:38.749	    7fd13cbd0780	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [2] monero-wallet-rpc:void boost::throw_exception<boost::system::system_error>(boost::system::system_error const&)+0x14e [0x55cdbac8075e]
2018-05-19 19:09:38.749	    7fd13cbd0780	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [3] monero-wallet-rpc:boost::asio::detail::do_throw_error(boost::system::error_code const&, char const*)+0x62 [0x55cdbac80812]
2018-05-19 19:09:38.749	    7fd13cbd0780	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [4] monero-wallet-rpc:boost::asio::ip::basic_resolver<boost::asio::ip::tcp>::resolve(boost::asio::ip::basic_resolver_query<boost::asio::ip::tcp> const&)+0x8c1 [0x55cdbaca1451]
2018-05-19 19:09:38.749	    7fd13cbd0780	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [5] monero-wallet-rpc:epee::net_utils::blocked_mode_client::connect(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::chrono::duration<long, std::ratio<1l, 1000l> >, bool, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&)+0x32b [0x55cdbaca1a0b]
2018-05-19 19:09:38.749	    7fd13cbd0780	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [6] monero-wallet-rpc:epee::net_utils::http::http_simple_client_template<epee::net_utils::blocked_mode_client>::invoke(boost::basic_string_ref<char, std::char_traits<char> >, boost::basic_string_ref<char, std::char_traits<char> >, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::chrono::duration<long, std::ratio<1l, 1000l> >, epee::net_utils::http::http_response_info const**, std::__cxx11::list<std::pair<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, std::allocator<std::pair<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > > const&)+0x7b7 [0x55cdbad277a7]
2018-05-19 19:09:38.749	    7fd13cbd0780	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [7] monero-wallet-rpc:bool epee::net_utils::invoke_http_json<epee::json_rpc::request<cryptonote::COMMAND_RPC_GET_VERSION::request>, epee::json_rpc::response<cryptonote::COMMAND_RPC_GET_VERSION::response, epee::json_rpc::error>, epee::net_utils::http::http_simple_client_template<epee::net_utils::blocked_mode_client> >(boost::basic_string_ref<char, std::char_traits<char> >, epee::json_rpc::request<cryptonote::COMMAND_RPC_GET_VERSION::request> const&, epee::json_rpc::response<cryptonote::COMMAND_RPC_GET_VERSION::response, epee::json_rpc::error>&, epee::net_utils::http::http_simple_client_template<epee::net_utils::blocked_mode_client>&, std::chrono::duration<long, std::ratio<1l, 1000l> >, boost::basic_string_ref<char, std::char_traits<char> >)+0x269 [0x55cdbae7e779]
2018-05-19 19:09:38.749	    7fd13cbd0780	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [8] monero-wallet-rpc:bool epee::net_utils::invoke_http_json_rpc<cryptonote::COMMAND_RPC_GET_VERSION::request, cryptonote::COMMAND_RPC_GET_VERSION::response, epee::net_utils::http::http_simple_client_template<epee::net_utils::blocked_mode_client> >(boost::basic_string_ref<char, std::char_traits<char> >, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, cryptonote::COMMAND_RPC_GET_VERSION::request const&, cryptonote::COMMAND_RPC_GET_VERSION::response&, epee::net_utils::http::http_simple_client_template<epee::net_utils::blocked_mode_client>&, std::chrono::duration<long, std::ratio<1l, 1000l> >, boost::basic_string_ref<char, std::char_traits<char> >, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&)+0x32e [0x55cdbae7f1ee]
2018-05-19 19:09:38.749	    7fd13cbd0780	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [9] monero-wallet-rpc:tools::NodeRPCProxy::get_rpc_version[abi:cxx11](unsigned int&) const+0x15f [0x55cdbaeb3cef]
2018-05-19 19:09:38.749	    7fd13cbd0780	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [10] monero-wallet-rpc:tools::wallet2::pull_blocks(unsigned long, unsigned long&, std::__cxx11::list<crypto::hash, std::allocator<crypto::hash> > const&, std::__cxx11::list<cryptonote::block_complete_entry, std::allocator<cryptonote::block_complete_entry> >&, std::vector<cryptonote::COMMAND_RPC_GET_BLOCKS_FAST::block_output_indices, std::allocator<cryptonote::COMMAND_RPC_GET_BLOCKS_FAST::block_output_indices> >&)+0x358 [0x55cdbada6838]
2018-05-19 19:09:38.749	    7fd13cbd0780	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [11] monero-wallet-rpc:tools::wallet2::refresh(unsigned long, unsigned long&, bool&)+0x268 [0x55cdbadb11a8]
2018-05-19 19:09:38.749	    7fd13cbd0780	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [12] monero-wallet-rpc:tools::wallet2::refresh(unsigned long, unsigned long&)+0x23 [0x55cdbadb24b3]
2018-05-19 19:09:38.749	    7fd13cbd0780	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [13] monero-wallet-rpc:tools::wallet2::refresh()+0x26 [0x55cdbadb24f6]
2018-05-19 19:09:38.749	    7fd13cbd0780	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [14] monero-wallet-rpc:main+0x787 [0x55cdbac3bee7]
2018-05-19 19:09:38.749	    7fd13cbd0780	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [15] /lib/libc.so.6:__libc_start_main+0xe7 [0x7fd139d1ca57]
2018-05-19 19:09:38.749	    7fd13cbd0780	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [16] monero-wallet-rpc:_start+0x2a [0x55cdbac4bbda]
2018-05-19 19:09:38.749	    7fd13cbd0780	INFO 	stacktrace	src/common/stack_trace.cpp:163	
2018-05-19 19:09:38.749	    7fd13cbd0780	ERROR	net.http	src/wallet/node_rpc_proxy.cpp:78	Failed to connect to daemon
2018-05-19 19:09:38.749	    7fd13cbd0780	ERROR	wallet.wallet2	src/wallet/wallet2.cpp:1633	result->empty(). THROW EXCEPTION: tools::error::no_connection_to_daemon
2018-05-19 19:09:38.750	    7fd13cbd0780	WARN 	net.http	src/wallet/wallet_errors.h:794	/usr/src/pkg/wrk/monero/src/monero-0.12.0.0/src/wallet/wallet2.cpp:1633:N5tools5error23no_connection_to_daemonE: no connection to daemon, request = getversion
2018-05-19 19:09:38.750	    7fd13cbd0780	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: tools::error::no_connection_to_daemon
2018-05-19 19:09:38.750	    7fd13cbd0780	INFO 	stacktrace	src/common/stack_trace.cpp:125	Unwound call stack:
2018-05-19 19:09:38.750	    7fd13cbd0780	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [1] monero-wallet-rpc:__cxa_throw+0x10a [0x55cdbaf1f5da]
2018-05-19 19:09:38.750	    7fd13cbd0780	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [2] monero-wallet-rpc:void tools::error::throw_wallet_ex<tools::error::no_connection_to_daemon, char [11]>(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >&&, char const (&) [11])+0x179 [0x55cdbae03e59]
2018-05-19 19:09:38.750	    7fd13cbd0780	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [3] monero-wallet-rpc:tools::wallet2::pull_blocks(unsigned long, unsigned long&, std::__cxx11::list<crypto::hash, std::allocator<crypto::hash> > const&, std::__cxx11::list<cryptonote::block_complete_entry, std::allocator<cryptonote::block_complete_entry> >&, std::vector<cryptonote::COMMAND_RPC_GET_BLOCKS_FAST::block_output_indices, std::allocator<cryptonote::COMMAND_RPC_GET_BLOCKS_FAST::block_output_indices> >&)+0x493 [0x55cdbada6973]
2018-05-19 19:09:38.750	    7fd13cbd0780	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [4] monero-wallet-rpc:tools::wallet2::refresh(unsigned long, unsigned long&, bool&)+0x268 [0x55cdbadb11a8]
2018-05-19 19:09:38.750	    7fd13cbd0780	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [5] monero-wallet-rpc:tools::wallet2::refresh(unsigned long, unsigned long&)+0x23 [0x55cdbadb24b3]
2018-05-19 19:09:38.750	    7fd13cbd0780	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [6] monero-wallet-rpc:tools::wallet2::refresh()+0x26 [0x55cdbadb24f6]
2018-05-19 19:09:38.750	    7fd13cbd0780	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [7] monero-wallet-rpc:main+0x787 [0x55cdbac3bee7]
2018-05-19 19:09:38.750	    7fd13cbd0780	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [8] /lib/libc.so.6:__libc_start_main+0xe7 [0x7fd139d1ca57]
2018-05-19 19:09:38.750	    7fd13cbd0780	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [9] monero-wallet-rpc:_start+0x2a [0x55cdbac4bbda]
2018-05-19 19:09:38.750	    7fd13cbd0780	INFO 	stacktrace	src/common/stack_trace.cpp:163	
2018-05-19 19:09:38.751	    7fd13cbd0780	ERROR	wallet.rpc	src/wallet/wallet_rpc_server.cpp:2990	Wallet initialization failed: no connection to daemon
```

monero 0.12.0.0
boost 1.66.0

# Discussion History
## moneromooo-monero | 2018-05-19T20:02:20+00:00
Do you have the crash stack trace ?

## moneromooo-monero | 2018-05-19T20:04:04+00:00
And about the failure to connect, what IP are you using for the daemon ?

## CamilleScholtz | 2018-05-19T20:17:54+00:00
I'm using the following options, I have also tried `--daemon-address node.moneroworld.com:18089`:

`monero-wallet-rpc --daemon-host node.xmrbackb.one --rpc-bind-port 18082 --disable-rpc-login --wallet-file $HOME/.monero/wallet --log-file $HOME/.monero/log --max-concurrency 4 --prompt-for-password`

## CamilleScholtz | 2018-05-19T20:18:16+00:00
>Do you have the crash stack trace ?

How would I go about obtaining this?

## moneromooo-monero | 2018-05-19T21:16:58+00:00
If the crash left a core dump:

gdb /path/to/monerod /path/to/that/core/dump
bt

About the connection problem, try:

dig node.xmrbackb.one

Is your system IPv6 only ? Did you connect succesfully to that node before ?


## CamilleScholtz | 2018-05-20T10:18:21+00:00
It did connect successfully before, the client stopped working since I updated my distro last week: https://crux.nu/Main/ReleaseNotes3-4

dig:

```
dig node.xmrbackb.one

; <<>> DiG 9.11.3 <<>> node.xmrbackb.one
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NXDOMAIN, id: 61593
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 1, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 4096
;; QUESTION SECTION:
;node.xmrbackb.one.             IN      A

;; ANSWER SECTION:
node.xmrbackb.one.      1783    IN      CNAME   frankfurt-1.xmrpool.net.xmrbackb.one.

;; AUTHORITY SECTION:
xmrbackb.one.           163     IN      SOA     ns11.constellix.com. dns.constellix.com. 2015010117 43200 3600 1209600 180

;; Query time: 0 msec
;; SERVER: 192.168.178.1#53(192.168.178.1)
;; WHEN: Sun May 20 11:54:39 CEST 2018
;; MSG SIZE  rcvd: 143
```

gdb (no core dumped):

```
2018-05-20 10:14:50.889     7ffff7fd9780        WARN    wallet.rpc      src/wallet/wallet_rpc_server.cpp:2948   Loading wallet...
Wallet password:
2018-05-20 10:15:16.078     7ffff7fd9780        WARN    wallet.wallet2  src/wallet/wallet2.cpp:3718     Loaded wallet keys file, with public address: [MY_ADDRESS]
[New Thread 0x7ffff2b00700 (LWP 11647)]
[New Thread 0x7ffff25ff700 (LWP 11648)]
[New Thread 0x7ffff20fe700 (LWP 11649)]
[New Thread 0x7ffff1bfd700 (LWP 11650)]
2018-05-20 10:15:16.169     7ffff7fd9780        ERROR   net.http        src/wallet/node_rpc_proxy.cpp:78        Failed to connect to daemon
2018-05-20 10:15:16.169     7ffff7fd9780        ERROR   wallet.wallet2  src/wallet/wallet2.cpp:1633     result->empty(). THROW EXCEPTION: tools::error::no_connection_to_daemon
2018-05-20 10:15:16.169     7ffff7fd9780        WARN    net.http        src/wallet/wallet_errors.h:794  /usr/src/pkg/wrk/monero/src/monero-0.12.0.0/src/wallet/wallet2.cpp:1633:N5tools5error23no_connection_to_daemonE: no connection to
daemon, request = getversion
2018-05-20 10:15:16.170     7ffff7fd9780        ERROR   wallet.rpc      src/wallet/wallet_rpc_server.cpp:2990   Wallet initialization failed: no connection to daemon
[Thread 0x7ffff1bfd700 (LWP 11650) exited]
[Thread 0x7ffff20fe700 (LWP 11649) exited]
[Thread 0x7ffff25ff700 (LWP 11648) exited]
[Thread 0x7ffff2b00700 (LWP 11647) exited]
[Inferior 1 (process 11578) exited with code 01]
```

## moneromooo-monero | 2018-05-20T11:09:48+00:00
The A record does not have an IP address. That's odd, but I don't know if that's OK or not.
Can you do: ping node.xmrbackb.one
Does this find it ?
If so, try:
telnet node.xmrbackb.one 18081
Does this connect ?

About the crash: are you sure it crashed ?
If so, there are instructions in README.md about how to enable core dumps.

## CamilleScholtz | 2018-05-20T11:34:16+00:00
```
ping node.xmrbackb.one
ping: unknown host node.xmrbackb.one
```

```
telnet node.xmrbackb.one 18081
Server lookup failure:  node.xmrbackb.one:18081, Name or service not known
```

>About the crash: are you sure it crashed ?

Maybe it didn't actually crash but simply exit because of the connection problem. I interpreted it as a crash.

## moneromooo-monero | 2018-05-20T12:54:31+00:00
The rpc one exits when it can't connect, because it's mostly useless without it (questionable). The cli one should not exit.

Anyway, if you can't resolve anything, then you need to fix that first.


## CamilleScholtz | 2018-05-20T14:37:46+00:00
I'm sorry for taking up your time. It seems that monerowold might be having problems that causes the client not to connect and raise these errors. I got `node.viaxmr.com` to work...

# Action History
- Created by: CamilleScholtz | 2018-05-19T19:27:46+00:00
- Closed at: 2018-05-20T14:37:46+00:00
