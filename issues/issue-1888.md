---
title: Xmrig Compilation Error
source_url: https://github.com/xmrig/xmrig/issues/1888
author: xday3
assignees: []
labels: []
created_at: '2020-10-10T16:13:29+00:00'
updated_at: '2021-04-12T14:47:01+00:00'
type: issue
status: closed
closed_at: '2021-04-12T14:47:01+00:00'
---

# Original Description
Hi dev, when I try to compile a static xmrig with OpenSSL enabled I get the following error:

[100%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/cn/r/CryptonightR_gen                                                                                        .cpp.o
Linking CXX executable xmrig

CMakeFiles/xmrig.dir/src/base/kernel/Platform.cpp.o: In function `xmrig::Platfor                                                                                        m::init(char const*)':
Platform.cpp:(.text+0x9): undefined reference to `OPENSSL_init_ssl'
Platform.cpp:(.text+0x15): undefined reference to `OPENSSL_init_ssl'
Platform.cpp:(.text+0x26): undefined reference to `OPENSSL_init_crypto'
Platform.cpp:(.text+0x32): undefined reference to `OPENSSL_init_ssl'
Platform.cpp:(.text+0x3e): undefined reference to `OPENSSL_init_crypto'
CMakeFiles/xmrig.dir/src/base/net/stratum/Tls.cpp.o: In function `xmrig::Client:                                                                                        :Tls::Tls(xmrig::Client*)':
Tls.cpp:(.text+0x80): undefined reference to `TLS_method'
CMakeFiles/xmrig.dir/src/base/net/stratum/Tls.cpp.o: In function `xmrig::Client:                                                                                        :Tls::read(char const*, unsigned long)':
Tls.cpp:(.text+0x376): undefined reference to `SSL_is_init_finished'
CMakeFiles/xmrig.dir/src/base/net/stratum/Tls.cpp.o: In function `xmrig::Client:                                                                                        :Tls::Tls(xmrig::Client*)':
Tls.cpp:(.text+0xc1): undefined reference to `SSL_CTX_set_options'
CMakeFiles/xmrig.dir/src/base/net/tls/ServerTls.cpp.o: In function `xmrig::Serve                                                                                        rTls::read(char const*, unsigned long)':
ServerTls.cpp:(.text+0xfc): undefined reference to `SSL_is_init_finished'
CMakeFiles/xmrig.dir/src/base/net/tls/TlsContext.cpp.o: In function `xmrig::TlsC                                                                                        ontext::setCipherSuites(char const*)':
TlsContext.cpp:(.text+0x5d): undefined reference to `SSL_CTX_set_ciphersuites'
CMakeFiles/xmrig.dir/src/base/net/tls/TlsContext.cpp.o: In function `xmrig::TlsC                                                                                        ontext::setDH(char const*)':
TlsContext.cpp:(.text+0x209): undefined reference to `DH_set0_pqg'
CMakeFiles/xmrig.dir/src/base/net/tls/TlsContext.cpp.o: In function `xmrig::TlsC                                                                                        ontext::load(xmrig::TlsConfig const&)':
TlsContext.cpp:(.text+0x24f): undefined reference to `TLS_server_method'
TlsContext.cpp:(.text+0x2b8): undefined reference to `SSL_CTX_set_options'
TlsContext.cpp:(.text+0x2c5): undefined reference to `SSL_CTX_set_options'
TlsContext.cpp:(.text+0x2cf): undefined reference to `SSL_CTX_set_max_early_data                                                                                        '
TlsContext.cpp:(.text+0x2ef): undefined reference to `SSL_CTX_clear_options'
TlsContext.cpp:(.text+0x306): undefined reference to `SSL_CTX_clear_options'
TlsContext.cpp:(.text+0x31d): undefined reference to `SSL_CTX_clear_options'
TlsContext.cpp:(.text+0x376): undefined reference to `SSL_CTX_set_ciphersuites'
TlsContext.cpp:(.text+0x439): undefined reference to `SSL_CTX_set_options'
TlsContext.cpp:(.text+0x471): undefined reference to `SSL_CTX_set_options'
TlsContext.cpp:(.text+0x489): undefined reference to `SSL_CTX_set_options'
TlsContext.cpp:(.text+0x4a1): undefined reference to `SSL_CTX_set_options'
CMakeFiles/xmrig.dir/src/base/net/tls/TlsContext.cpp.o: In function `xmrig::TlsC                                                                                        ontext::setProtocols(unsigned int)':
TlsContext.cpp:(.text+0x56f): undefined reference to `SSL_CTX_clear_options'
TlsContext.cpp:(.text+0x582): undefined reference to `SSL_CTX_clear_options'
TlsContext.cpp:(.text+0x595): undefined reference to `SSL_CTX_clear_options'
TlsContext.cpp:(.text+0x5ca): undefined reference to `SSL_CTX_set_options'
TlsContext.cpp:(.text+0x5d9): undefined reference to `SSL_CTX_set_options'
TlsContext.cpp:(.text+0x5ea): undefined reference to `SSL_CTX_set_options'
TlsContext.cpp:(.text+0x5b8): undefined reference to `SSL_CTX_set_options'
CMakeFiles/xmrig.dir/src/base/net/tls/TlsGen.cpp.o: In function `xmrig::TlsGen::                                                                                        generate_x509(char const*)':
TlsGen.cpp:(.text+0x2cb): undefined reference to `X509_getm_notBefore'
TlsGen.cpp:(.text+0x2de): undefined reference to `X509_getm_notAfter'
collect2: error: ld returned 1 exit status
make[2]: *** [xmrig] Error 1
make[1]: *** [CMakeFiles/xmrig.dir/all] Error 2
make: *** [all] Error 2
=========================

Compilation without: [100%] Built target xmrig-notls
:~/xmrig/build# ldd xmrig-notls
        not a dynamic executable

There is anything what I can do to compile  xmrig static version with OpenSSL enabled? let me know.

# Discussion History
# Action History
- Created by: xday3 | 2020-10-10T16:13:29+00:00
- Closed at: 2021-04-12T14:47:01+00:00
