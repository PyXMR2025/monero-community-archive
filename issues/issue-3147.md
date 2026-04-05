---
title: Failed to build with the latest updates.
source_url: https://github.com/xmrig/xmrig/issues/3147
author: ghost
assignees: []
labels:
- question
created_at: '2022-10-28T15:04:36+00:00'
updated_at: '2022-12-13T14:32:14+00:00'
type: issue
status: closed
closed_at: '2022-12-13T14:32:14+00:00'
---

# Original Description
I'm on Fedora Linux 36.
I managed to build the latest version of xmrig (v6.18.1) on another machine running the same operating system, which it succeed.
I wanted to update my main machine's xmrig as well, when running `make -j2` it showed this error

```
/usr/bin/ld: CMakeFiles/xmrig.dir/src/base/net/tls/TlsContext.cpp.o: in function `xmrig::TlsContext::load(xmrig::TlsConfig const&)':
TlsContext.cpp:(.text+0x643): undefined reference to `SSLv23_server_method'
/usr/bin/ld: CMakeFiles/xmrig.dir/src/base/net/https/HttpsClient.cpp.o: in function `xmrig::HttpsClient::read(char const*, unsigned long)':
HttpsClient.cpp:(.text+0x9fd): undefined reference to `SSL_state'
/usr/bin/ld: HttpsClient.cpp:(.text+0xa65): undefined reference to `SSL_get_peer_certificate'
/usr/bin/ld: CMakeFiles/xmrig.dir/src/base/net/https/HttpsClient.cpp.o: in function `xmrig::HttpsClient::HttpsClient(char const*, xmrig::FetchRequest&&, std::weak_ptr<xmrig::IHttpListener> const&)':
HttpsClient.cpp:(.text+0xb72): undefined reference to `SSLv23_method'
/usr/bin/ld: CMakeFiles/xmrig.dir/src/base/kernel/Platform.cpp.o: in function `xmrig::Platform::init(char const*)':
Platform.cpp:(.text+0x5): undefined reference to `SSL_library_init'
/usr/bin/ld: Platform.cpp:(.text+0xa): undefined reference to `SSL_load_error_strings'
/usr/bin/ld: Platform.cpp:(.text+0x14): undefined reference to `ERR_load_crypto_strings'
/usr/bin/ld: Platform.cpp:(.text+0x19): undefined reference to `SSL_load_error_strings'
/usr/bin/ld: Platform.cpp:(.text+0x1e): undefined reference to `OpenSSL_add_all_digests'
/usr/bin/ld: CMakeFiles/xmrig.dir/src/base/net/stratum/Tls.cpp.o: in function `xmrig::Client::Tls::Tls(xmrig::Client*)':
Tls.cpp:(.text+0x38): undefined reference to `SSLv23_method'
/usr/bin/ld: CMakeFiles/xmrig.dir/src/base/net/stratum/Tls.cpp.o: in function `xmrig::Client::Tls::read(char const*, unsigned long)':
Tls.cpp:(.text+0x2b6): undefined reference to `SSL_state'
/usr/bin/ld: Tls.cpp:(.text+0x317): undefined reference to `SSL_get_peer_certificate'
/usr/bin/ld: CMakeFiles/xmrig.dir/src/base/net/tls/ServerTls.cpp.o: in function `xmrig::ServerTls::read(char const*, unsigned long)':
ServerTls.cpp:(.text+0x15b): undefined reference to `SSL_state'
collect2: error: ld returned 1 exit status
make[2]: *** [CMakeFiles/xmrig.dir/build.make:3854: xmrig] Error 1
make[1]: *** [CMakeFiles/Makefile2:182: CMakeFiles/xmrig.dir/all] Error 2
make: *** [Makefile:91: all] Error 2
```

Here's, what I believe, updates that caused the error since I have not installed any additional package.
![Screenshot from 2022-10-28 22-53-02](https://user-images.githubusercontent.com/108665518/198666229-7acee3aa-1e12-4c15-b447-e4c0deb00bc2.png)

My solution to the error was simply disabling TLS (I don't have to use it anyway).

# Discussion History
## Spudz76 | 2022-10-28T23:56:03+00:00
Use advanced build where the script `./scripts/build_deps.sh` makes OpenSSL/hwloc/LibUV with versions we know work well.

When you use system `devel` packages who knows what can happen (especially in any RedHat based thing).

# Action History
- Created by: ghost | 2022-10-28T15:04:36+00:00
- Closed at: 2022-12-13T14:32:14+00:00
