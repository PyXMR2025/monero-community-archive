---
title: Mac build error
source_url: https://github.com/xmrig/xmrig/issues/1650
author: a8underscore
assignees: []
labels: []
created_at: '2020-04-19T18:48:03+00:00'
updated_at: '2020-08-28T16:38:36+00:00'
type: issue
status: closed
closed_at: '2020-08-28T16:38:36+00:00'
---

# Original Description
**Describe the bug**
it does not build on Mac 

**To Reproduce**
follow this steps https://xmrig.com/docs/miner/macos-build

**Expected behavior**
it builds without error

**Required data**
error
[ 99%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/https/HttpsServer.cpp.o
[ 99%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/common/Assembly.cpp.o
[100%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/cn/r/CryptonightR_gen.cpp.o
[100%] Linking CXX executable xmrig
Undefined symbols for architecture x86_64:
  "_ERR_load_crypto_strings", referenced from:
      xmrig::Platform::init(char const*) in Platform.cpp.o
  "_OpenSSL_add_all_digests", referenced from:
      xmrig::Platform::init(char const*) in Platform.cpp.o
  "_SSL_library_init", referenced from:
      xmrig::Platform::init(char const*) in Platform.cpp.o
  "_SSL_load_error_strings", referenced from:
      xmrig::Platform::init(char const*) in Platform.cpp.o
  "_SSL_state", referenced from:
      xmrig::Client::Tls::read(char const*, unsigned long) in Tls.cpp.o
      xmrig::ServerTls::read(char const*, unsigned long) in ServerTls.cpp.o
      xmrig::HttpsClient::read(char const*, unsigned long) in HttpsClient.cpp.o
     (maybe you meant: _SSL_stateless)
  "_SSLv23_method", referenced from:
      xmrig::Client::Tls::Tls(xmrig::Client*) in Tls.cpp.o
      xmrig::HttpsClient::HttpsClient(xmrig::FetchRequest&&, std::__1::weak_ptr<xmrig::IHttpListener> const&) in HttpsClient.cpp.o
  "_SSLv23_server_method", referenced from:
      xmrig::TlsContext::load(xmrig::TlsConfig const&) in TlsContext.cpp.o
ld: symbol(s) not found for architecture x86_64
clang: error: linker command failed with exit code 1 (use -v to see invocation)
make[2]: *** [xmrig] Error 1
make[1]: *** [CMakeFiles/xmrig.dir/all] Error 2
make: *** [all] Error 2


**Additional context**



# Discussion History
## a8underscore | 2020-05-14T16:24:41+00:00
bump

## ghost | 2020-06-24T23:03:06+00:00
try compiling hwloc and then compile xmrig as mentioned in advanced tab, that worked for me on `19.4.0 Darwin Kernel Version 19.4.0: Wed Mar  4 22:28:40 PST 2020; root:xnu-6153.101.6~15/RELEASE_X86_64 x86_64`
I also upgraded cmake to 3.17.3

## rtau | 2020-06-25T13:00:39+00:00
Sounds like it tried to reference OpenSSL but cannot find the header file?

# Action History
- Created by: a8underscore | 2020-04-19T18:48:03+00:00
- Closed at: 2020-08-28T16:38:36+00:00
