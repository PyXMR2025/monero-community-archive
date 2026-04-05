---
title: Failed to compile static file with MHD
source_url: https://github.com/xmrig/xmrig/issues/697
author: c0mm4nd
assignees: []
labels: []
created_at: '2018-06-18T07:24:23+00:00'
updated_at: '2018-06-18T07:59:57+00:00'
type: issue
status: closed
closed_at: '2018-06-18T07:59:57+00:00'
---

# Original Description
`cmake .. -DUV_LIBRARY=/usr/lib/x86_64-linux-gnu/libuv.a -DMHD_LIBRARY=/usr/lib/x86_64-linux-gnu/libmicrohttpd.a`

Error message as following:
```
                                                                       ^
[ 96%] Building CXX object CMakeFiles/xmrig.dir/src/common/api/Httpd.cpp.o
[ 98%] Building CXX object CMakeFiles/xmrig.dir/src/common/api/HttpRequest.cpp.o
[100%] Linking CXX executable xmrig
/usr/lib/gcc/x86_64-linux-gnu/4.8/../../../x86_64-linux-gnu/libmicrohttpd.a(daemon.o): In function `parse_options_va':
(.text+0x966): undefined reference to `gnutls_priority_deinit'
/usr/lib/gcc/x86_64-linux-gnu/4.8/../../../x86_64-linux-gnu/libmicrohttpd.a(daemon.o): In function `parse_options_va':
(.text+0x98c): undefined reference to `gnutls_priority_init'
/usr/lib/gcc/x86_64-linux-gnu/4.8/../../../x86_64-linux-gnu/libmicrohttpd.a(daemon.o): In function `parse_options_va':
(.text+0x99b): undefined reference to `gnutls_strerror'
/usr/lib/gcc/x86_64-linux-gnu/4.8/../../../x86_64-linux-gnu/libmicrohttpd.a(daemon.o): In function `send_tls_adapter':
(.text+0x180c): undefined reference to `gnutls_record_send'
/usr/lib/gcc/x86_64-linux-gnu/4.8/../../../x86_64-linux-gnu/libmicrohttpd.a(daemon.o): In function `recv_tls_adapter':
(.text+0x186e): undefined reference to `gnutls_record_recv'
/usr/lib/gcc/x86_64-linux-gnu/4.8/../../../x86_64-linux-gnu/libmicrohttpd.a(daemon.o): In function `internal_add_connection':
(.text+0x2026): undefined reference to `gnutls_init'
/usr/lib/gcc/x86_64-linux-gnu/4.8/../../../x86_64-linux-gnu/libmicrohttpd.a(daemon.o): In function `internal_add_connection':
(.text+0x2039): undefined reference to `gnutls_priority_set'
/usr/lib/gcc/x86_64-linux-gnu/4.8/../../../x86_64-linux-gnu/libmicrohttpd.a(daemon.o): In function `internal_add_connection':
(.text+0x2061): undefined reference to `gnutls_credentials_set'
/usr/lib/gcc/x86_64-linux-gnu/4.8/../../../x86_64-linux-gnu/libmicrohttpd.a(daemon.o): In function `internal_add_connection':
(.text+0x2070): undefined reference to `gnutls_transport_set_ptr'
/usr/lib/gcc/x86_64-linux-gnu/4.8/../../../x86_64-linux-gnu/libmicrohttpd.a(daemon.o): In function `internal_add_connection':
(.text+0x2081): undefined reference to `gnutls_transport_set_pull_function'
/usr/lib/gcc/x86_64-linux-gnu/4.8/../../../x86_64-linux-gnu/libmicrohttpd.a(daemon.o): In function `internal_add_connection':
(.text+0x2092): undefined reference to `gnutls_transport_set_push_function'
/usr/lib/gcc/x86_64-linux-gnu/4.8/../../../x86_64-linux-gnu/libmicrohttpd.a(daemon.o): In function `internal_add_connection':
(.text+0x20b9): undefined reference to `gnutls_certificate_server_set_request'
/usr/lib/gcc/x86_64-linux-gnu/4.8/../../../x86_64-linux-gnu/libmicrohttpd.a(daemon.o): In function `MHD_cleanup_connections':
(.text+0x26da): undefined reference to `gnutls_deinit'
/usr/lib/gcc/x86_64-linux-gnu/4.8/../../../x86_64-linux-gnu/libmicrohttpd.a(daemon.o): In function `MHD_get_timeout':
(.text+0x3246): undefined reference to `gnutls_record_check_pending'
/usr/lib/gcc/x86_64-linux-gnu/4.8/../../../x86_64-linux-gnu/libmicrohttpd.a(daemon.o): In function `MHD_get_timeout':
(.text+0x3328): undefined reference to `gnutls_record_check_pending'
/usr/lib/gcc/x86_64-linux-gnu/4.8/../../../x86_64-linux-gnu/libmicrohttpd.a(daemon.o): In function `MHD_stop_daemon':
(.text+0x4978): undefined reference to `gnutls_priority_deinit'
/usr/lib/gcc/x86_64-linux-gnu/4.8/../../../x86_64-linux-gnu/libmicrohttpd.a(daemon.o): In function `MHD_stop_daemon':
(.text+0x4989): undefined reference to `gnutls_certificate_free_credentials'
/usr/lib/gcc/x86_64-linux-gnu/4.8/../../../x86_64-linux-gnu/libmicrohttpd.a(daemon.o): In function `MHD_start_daemon_va':
(.text+0x5087): undefined reference to `gnutls_priority_init'
/usr/lib/gcc/x86_64-linux-gnu/4.8/../../../x86_64-linux-gnu/libmicrohttpd.a(daemon.o): In function `MHD_start_daemon_va':
(.text+0x50f9): undefined reference to `gnutls_priority_deinit'
/usr/lib/gcc/x86_64-linux-gnu/4.8/../../../x86_64-linux-gnu/libmicrohttpd.a(daemon.o): In function `MHD_start_daemon_va':
(.text+0x537f): undefined reference to `gnutls_certificate_allocate_credentials'
/usr/lib/gcc/x86_64-linux-gnu/4.8/../../../x86_64-linux-gnu/libmicrohttpd.a(daemon.o): In function `MHD_start_daemon_va':
(.text+0x53b7): undefined reference to `gnutls_certificate_set_x509_trust_mem'
/usr/lib/gcc/x86_64-linux-gnu/4.8/../../../x86_64-linux-gnu/libmicrohttpd.a(daemon.o): In function `MHD_start_daemon_va':
(.text+0x5419): undefined reference to `gnutls_certificate_set_x509_key_mem'
/usr/lib/gcc/x86_64-linux-gnu/4.8/../../../x86_64-linux-gnu/libmicrohttpd.a(daemon.o): In function `MHD_start_daemon_va':
(.text+0x55b1): undefined reference to `gnutls_priority_deinit'
/usr/lib/gcc/x86_64-linux-gnu/4.8/../../../x86_64-linux-gnu/libmicrohttpd.a(daemon.o): In function `MHD_init':
(.text.startup+0x27): undefined reference to `gcry_control'
/usr/lib/gcc/x86_64-linux-gnu/4.8/../../../x86_64-linux-gnu/libmicrohttpd.a(daemon.o): In function `MHD_init':
(.text.startup+0x2e): undefined reference to `gcry_check_version'
/usr/lib/gcc/x86_64-linux-gnu/4.8/../../../x86_64-linux-gnu/libmicrohttpd.a(daemon.o): In function `MHD_init':
(.text.startup+0x37): undefined reference to `gnutls_global_init'
/usr/lib/gcc/x86_64-linux-gnu/4.8/../../../x86_64-linux-gnu/libmicrohttpd.a(daemon.o): In function `MHD_fini':
(.text.exit+0x1): undefined reference to `gnutls_global_deinit'
/usr/lib/gcc/x86_64-linux-gnu/4.8/../../../x86_64-linux-gnu/libmicrohttpd.a(connection.o): In function `MHD_connection_handle_read':
(.text+0x1123): undefined reference to `gnutls_strerror'
/usr/lib/gcc/x86_64-linux-gnu/4.8/../../../x86_64-linux-gnu/libmicrohttpd.a(connection.o): In function `do_write':
(.text+0x11a2): undefined reference to `gnutls_strerror'
/usr/lib/gcc/x86_64-linux-gnu/4.8/../../../x86_64-linux-gnu/libmicrohttpd.a(connection.o): In function `MHD_get_connection_info':
(.text+0x156d): undefined reference to `gnutls_cipher_get'
/usr/lib/gcc/x86_64-linux-gnu/4.8/../../../x86_64-linux-gnu/libmicrohttpd.a(connection.o): In function `MHD_get_connection_info':
(.text+0x158d): undefined reference to `gnutls_protocol_get_version'
/usr/lib/gcc/x86_64-linux-gnu/4.8/../../../x86_64-linux-gnu/libmicrohttpd.a(connection.o): In function `MHD_connection_handle_idle':
(.text+0x1d5b): undefined reference to `gnutls_record_get_direction'
/usr/lib/gcc/x86_64-linux-gnu/4.8/../../../x86_64-linux-gnu/libmicrohttpd.a(connection_https.o): In function `run_tls_handshake':
(.text+0x28): undefined reference to `gnutls_handshake'
/usr/lib/gcc/x86_64-linux-gnu/4.8/../../../x86_64-linux-gnu/libmicrohttpd.a(connection_https.o): In function `MHD_tls_connection_handle_idle':
(.text+0x10b): undefined reference to `gnutls_record_check_pending'
/usr/lib/gcc/x86_64-linux-gnu/4.8/../../../x86_64-linux-gnu/libmicrohttpd.a(connection_https.o): In function `MHD_tls_connection_handle_idle':
(.text+0x14a): undefined reference to `gnutls_bye'
collect2: error: ld returned 1 exit status
make[2]: *** [xmrig] Error 1
make[1]: *** [CMakeFiles/xmrig.dir/all] Error 2
make: *** [all] Error 2

```

Under docker ubuntu:trusty, using the libmicrohttpd.a in apt. xmrig source is latest in github.

So how to make a static file with MHD, have to build MHD by myself?


# Discussion History
## xmrig | 2018-06-18T07:53:58+00:00
Yes you should build libmicrohttpd by yourself.
```
./configure --disable-shared --disable-doc --disable-examples --disable-curl --enable-https=no --disable-bauth --disable-dauth --disable-httpupgrade
```
Use options above to build static library without additional dependencies.
Thank you.

# Action History
- Created by: c0mm4nd | 2018-06-18T07:24:23+00:00
- Closed at: 2018-06-18T07:59:57+00:00
