---
title: FreeBSD build errors
source_url: https://github.com/monero-project/monero/issues/9519
author: syleishere
assignees: []
labels:
- bsd
- reproduction needed
- more info needed
created_at: '2024-10-15T00:14:31+00:00'
updated_at: '2024-10-29T05:12:22+00:00'
type: issue
status: closed
closed_at: '2024-10-29T05:12:22+00:00'
---

# Original Description
FreeBSD 14.1-RELEASE-p5 FreeBSD 14.1-RELEASE-p5 GENERIC amd64
unbound packages installed from standard pkg command:
        lua54-luaunbound: 1.0.0_5
        unbound: 1.21.1

```
[ 92%] Built target daemonizer
[ 93%] Linking CXX executable ../../bin/monero-wallet-rpc
ld: warning: unknown -z value: noexecheap
ld: error: undefined symbol: el::base::debug::StackTrace::generateNew()
>>> referenced by stack_trace.cpp
>>>               stack_trace.cpp.o:(tools::log_stack_trace(char const*)) in archive ../common/libcommon.a

ld: error: undefined symbol: el::base::debug::operator<<(std::__1::basic_ostream<char, std::__1::char_traits<char>>&, el::base::debug::StackTrace const&)
>>> referenced by stack_trace.cpp
>>>               stack_trace.cpp.o:(tools::log_stack_trace(char const*)) in archive ../common/libcommon.a

ld: error: undefined symbol: nghttp2_session_server_new
>>> referenced by netevent.c
>>>               netevent.o:(comm_point_tcp_accept_callback) in archive /usr/local/lib/libunbound.a

ld: error: undefined symbol: nghttp2_submit_settings
>>> referenced by netevent.c
>>>               netevent.o:(comm_point_tcp_accept_callback) in archive /usr/local/lib/libunbound.a

ld: error: undefined symbol: nghttp2_strerror
>>> referenced by netevent.c
>>>               netevent.o:(comm_point_tcp_accept_callback) in archive /usr/local/lib/libunbound.a
>>> referenced by netevent.c
>>>               netevent.o:(comm_point_http_handle_callback) in archive /usr/local/lib/libunbound.a
>>> referenced by netevent.c
>>>               netevent.o:(comm_point_http_handle_callback) in archive /usr/local/lib/libunbound.a
>>> referenced 6 more times

ld: error: undefined symbol: nghttp2_session_recv
>>> referenced by netevent.c
>>>               netevent.o:(comm_point_http_handle_callback) in archive /usr/local/lib/libunbound.a

ld: error: undefined symbol: nghttp2_session_want_write
>>> referenced by netevent.c
>>>               netevent.o:(comm_point_http_handle_callback) in archive /usr/local/lib/libunbound.a
>>> referenced by netevent.c
>>>               netevent.o:(comm_point_http_handle_callback) in archive /usr/local/lib/libunbound.a

ld: error: undefined symbol: nghttp2_session_send
>>> referenced by netevent.c
>>>               netevent.o:(comm_point_http_handle_callback) in archive /usr/local/lib/libunbound.a

ld: error: undefined symbol: nghttp2_session_want_read
>>> referenced by netevent.c
>>>               netevent.o:(comm_point_http_handle_callback) in archive /usr/local/lib/libunbound.a
>>> referenced by netevent.c
>>>               netevent.o:(comm_point_http_handle_callback) in archive /usr/local/lib/libunbound.a

ld: error: undefined symbol: nghttp2_submit_rst_stream
>>> referenced by listen_dnsport.c
>>>               listen_dnsport.o:(http2_submit_dns_response) in archive /usr/local/lib/libunbound.a
>>> referenced by listen_dnsport.c
>>>               listen_dnsport.o:(http2_req_data_chunk_recv_cb) in archive /usr/local/lib/libunbound.a
>>> referenced by listen_dnsport.c
>>>               listen_dnsport.o:(http2_buffer_uri_query) in archive /usr/local/lib/libunbound.a

ld: error: undefined symbol: nghttp2_submit_response
>>> referenced by listen_dnsport.c
>>>               listen_dnsport.o:(http2_submit_dns_response) in archive /usr/local/lib/libunbound.a
>>> referenced by listen_dnsport.c
>>>               listen_dnsport.o:(http2_req_frame_recv_cb) in archive /usr/local/lib/libunbound.a

ld: error: undefined symbol: nghttp2_session_get_stream_user_data
>>> referenced by listen_dnsport.c
>>>               listen_dnsport.o:(http2_submit_response_read_callback) in archive /usr/local/lib/libunbound.a
>>> referenced by listen_dnsport.c
>>>               listen_dnsport.o:(http2_req_frame_recv_cb) in archive /usr/local/lib/libunbound.a
>>> referenced by listen_dnsport.c
>>>               listen_dnsport.o:(http2_req_header_cb) in archive /usr/local/lib/libunbound.a
>>> referenced 3 more times

ld: error: undefined symbol: nghttp2_session_callbacks_new
>>> referenced by listen_dnsport.c
>>>               listen_dnsport.o:(http2_req_callbacks_create) in archive /usr/local/lib/libunbound.a

ld: error: undefined symbol: nghttp2_session_callbacks_set_on_begin_headers_callback
>>> referenced by listen_dnsport.c
>>>               listen_dnsport.o:(http2_req_callbacks_create) in archive /usr/local/lib/libunbound.a

ld: error: undefined symbol: nghttp2_session_callbacks_set_on_frame_recv_callback
>>> referenced by listen_dnsport.c
>>>               listen_dnsport.o:(http2_req_callbacks_create) in archive /usr/local/lib/libunbound.a

ld: error: undefined symbol: nghttp2_session_callbacks_set_on_header_callback
>>> referenced by listen_dnsport.c
>>>               listen_dnsport.o:(http2_req_callbacks_create) in archive /usr/local/lib/libunbound.a

ld: error: undefined symbol: nghttp2_session_callbacks_set_on_data_chunk_recv_callback
>>> referenced by listen_dnsport.c
>>>               listen_dnsport.o:(http2_req_callbacks_create) in archive /usr/local/lib/libunbound.a

ld: error: undefined symbol: nghttp2_session_callbacks_set_recv_callback
>>> referenced by listen_dnsport.c
>>>               listen_dnsport.o:(http2_req_callbacks_create) in archive /usr/local/lib/libunbound.a

ld: error: undefined symbol: nghttp2_session_callbacks_set_send_callback
>>> referenced by listen_dnsport.c
>>>               listen_dnsport.o:(http2_req_callbacks_create) in archive /usr/local/lib/libunbound.a

ld: error: undefined symbol: nghttp2_session_del
>>> referenced by netevent.c
>>>               netevent.o:(comm_point_close) in archive /usr/local/lib/libunbound.a

ld: error: too many errors emitted, stopping now (use --error-limit=0 to see all errors)
c++: error: linker command failed with exit code 1 (use -v to see invocation)
gmake[3]: *** [src/wallet/CMakeFiles/wallet_rpc_server.dir/build.make:153: bin/monero-wallet-rpc] Error 1
gmake[2]: *** [CMakeFiles/Makefile2:3056: src/wallet/CMakeFiles/wallet_rpc_server.dir/all] Error 2
gmake[1]: *** [Makefile:146: all] Error 2
gmake[1]: Leaving directory '/root/monero/build/FreeBSD/release-v0.18/release'
gmake: *** [Makefile:107: release-static] Error 2
```


# Discussion History
## 0xFFFC0000 | 2024-10-20T14:39:19+00:00
Looks to me the dependencies of `libunbound` are not available and/or not installed correctly. 

## syleishere | 2024-10-25T20:55:08+00:00
```
# pkg version -v|grep unbound
lua54-luaunbound-1.0.0_5           >   succeeds index (index has 1.0.0_1)
unbound-1.21.1                     >   succeeds index (index has 1.19.0)
```


## 0xFFFC0000 | 2024-10-26T06:08:21+00:00
It is not able to find nghttp2 library [1]. For some reason maybe it is not installed correctly?

And can you try this [2] ? I believe this should fix it. 

1. https://nghttp2.org/
2. https://github.com/monero-project/monero/pull/9475

## syleishere | 2024-10-28T19:43:43+00:00
```
# pkg version -v|grep nghttp2
libnghttp2-1.63.0                  >   succeeds index (index has 1.58.0)
nghttp2-1.63.0                     >   succeeds index (index has 1.58.0)
```
Tried set USE_UNWIND without success as well. 

## syleishere | 2024-10-28T22:13:19+00:00
Did a gmake clean all after above modifications, it finally compiles. It is the gmake release-static that is producing those errors.

## 0xFFFC0000 | 2024-10-29T05:12:15+00:00
I am closing this issue. Feel free to reopen it if you have any questions. 

# Action History
- Created by: syleishere | 2024-10-15T00:14:31+00:00
- Closed at: 2024-10-29T05:12:22+00:00
