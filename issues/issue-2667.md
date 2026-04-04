---
title: Not building on Ubuntu 14.04 LTS.
source_url: https://github.com/monero-project/monero/issues/2667
author: ViperRu
assignees: []
labels: []
created_at: '2017-10-16T10:00:57+00:00'
updated_at: '2017-11-08T20:31:43+00:00'
type: issue
status: closed
closed_at: '2017-11-08T20:31:43+00:00'
---

# Original Description
dpkg -l | grep libboost1
```
ii  libboost1.58-dev:amd64                      1.58.0+dfsg-4.1ubuntu3                            amd64        Boost C++ Libraries development files
ii  libboost1.58-tools-dev                      1.58.0+dfsg-4.1ubuntu3                            amd64        Boost C++ Libraries development tools
```
dpkg -l | grep openssl
```
ii  libevent-openssl-2.0-5:amd64                2.0.21-stable-1ubuntu1.14.04.2                    amd64        Asynchronous event notification library (openssl)
ii  libgnutls-openssl27:amd64                   3.2.16-1ubuntu3                                   amd64        GNU TLS library - OpenSSL wrapper
ii  openssl                                     1.1.0f-2~ubuntu14.04.1+deb.sury.org+1             amd64        Secure Sockets Layer toolkit - cryptographic utility
```
The process "make" has been end with:
```
[ 20%] Building CXX object src/common/CMakeFiles/obj_common.dir/download.cpp.o
In file included from /usr/include/openssl/bio.h:20:0,
                 from /usr/include/openssl/conf.h:13,
                 from /usr/include/boost/asio/ssl/detail/openssl_types.hpp:19,
                 from /usr/include/boost/asio/ssl/context_base.hpp:19,
                 from /usr/include/boost/asio/ssl/context.hpp:27,
                 from /usr/include/boost/asio/ssl.hpp:19,
                 from /home/my/bitmonero/contrib/epee/include/net/net_helper.h:40,
                 from /home/my/bitmonero/contrib/epee/include/net/http_client.h:40,
                 from /home/my/bitmonero/src/common/download.cpp:36:
/usr/include/boost/asio/ssl/detail/impl/openssl_init.ipp: In constructor ‘boost::asio::ssl::detail::openssl_init_base::do_init::do_init()’:
/usr/include/boost/asio/ssl/detail/impl/openssl_init.ipp:43:23: error: expected id-expression before ‘(’ token
     mutexes_.resize(::CRYPTO_num_locks());
                       ^
In file included from /usr/include/boost/asio/ssl/detail/openssl_init.hpp:100:0,
                 from /usr/include/boost/asio/ssl/context.hpp:29,
                 from /usr/include/boost/asio/ssl.hpp:19,
                 from /home/my/bitmonero/contrib/epee/include/net/net_helper.h:40,
                 from /home/my/bitmonero/contrib/epee/include/net/http_client.h:40,
                 from /home/my/bitmonero/src/common/download.cpp:36:
/usr/include/boost/asio/ssl/detail/impl/openssl_init.ipp:46:66: error: expected id-expression before ‘;’ token
     ::CRYPTO_set_locking_callback(&do_init::openssl_locking_func);
                                                                  ^
/usr/include/boost/asio/ssl/detail/impl/openssl_init.ipp:47:56: error: expected id-expression before ‘;’ token
     ::CRYPTO_set_id_callback(&do_init::openssl_id_func);
                                                        ^
/usr/include/boost/asio/ssl/detail/impl/openssl_init.ipp: In destructor ‘boost::asio::ssl::detail::openssl_init_base::do_init::~do_init()’:
/usr/include/boost/asio/ssl/detail/impl/openssl_init.ipp:64:32: error: expected id-expression before ‘;’ token
     ::CRYPTO_set_id_callback(0);
                                ^
/usr/include/boost/asio/ssl/detail/impl/openssl_init.ipp:65:37: error: expected id-expression before ‘;’ token
     ::CRYPTO_set_locking_callback(0);
                                     ^
In file included from /usr/include/openssl/engine.h:30:0,
                 from /usr/include/boost/asio/ssl/detail/openssl_types.hpp:22,
                 from /usr/include/boost/asio/ssl/context_base.hpp:19,
                 from /usr/include/boost/asio/ssl/context.hpp:27,
                 from /usr/include/boost/asio/ssl.hpp:19,
                 from /home/my/bitmonero/contrib/epee/include/net/net_helper.h:40,
                 from /home/my/bitmonero/contrib/epee/include/net/http_client.h:40,
                 from /home/my/bitmonero/src/common/download.cpp:36:
/usr/include/boost/asio/ssl/detail/impl/openssl_init.ipp:66:7: error: expected id-expression before ‘while’
     ::ERR_free_strings();
       ^
In file included from /usr/include/openssl/x509.h:23:0,
                 from /usr/include/openssl/ssl.h:50,
                 from /usr/include/boost/asio/ssl/detail/openssl_types.hpp:20,
                 from /usr/include/boost/asio/ssl/context_base.hpp:19,
                 from /usr/include/boost/asio/ssl/context.hpp:27,
                 from /usr/include/boost/asio/ssl.hpp:19,
                 from /home/my/bitmonero/contrib/epee/include/net/net_helper.h:40,
                 from /home/my/bitmonero/contrib/epee/include/net/http_client.h:40,
                 from /home/my/bitmonero/src/common/download.cpp:36:
/usr/include/boost/asio/ssl/detail/impl/openssl_init.ipp:72:7: error: expected id-expression before ‘while’
     ::EVP_cleanup();
       ^
In file included from /usr/include/openssl/bio.h:20:0,
                 from /usr/include/openssl/conf.h:13,
                 from /usr/include/boost/asio/ssl/detail/openssl_types.hpp:19,
                 from /usr/include/boost/asio/ssl/context_base.hpp:19,
                 from /usr/include/boost/asio/ssl/context.hpp:27,
                 from /usr/include/boost/asio/ssl.hpp:19,
                 from /home/my/bitmonero/contrib/epee/include/net/net_helper.h:40,
                 from /home/my/bitmonero/contrib/epee/include/net/http_client.h:40,
                 from /home/my/bitmonero/src/common/download.cpp:36:
/usr/include/boost/asio/ssl/detail/impl/openssl_init.ipp:73:7: error: expected id-expression before ‘while’
     ::CRYPTO_cleanup_all_ex_data();
       ^
In file included from /usr/include/boost/asio/ssl/detail/openssl_types.hpp:22:0,
                 from /usr/include/boost/asio/ssl/context_base.hpp:19,
                 from /usr/include/boost/asio/ssl/context.hpp:27,
                 from /usr/include/boost/asio/ssl.hpp:19,
                 from /home/my/bitmonero/contrib/epee/include/net/net_helper.h:40,
                 from /home/my/bitmonero/contrib/epee/include/net/http_client.h:40,
                 from /home/my/bitmonero/src/common/download.cpp:36:
/usr/include/boost/asio/ssl/detail/impl/openssl_init.ipp:76:7: error: expected id-expression before ‘while’
     ::ENGINE_cleanup();
       ^
In file included from /usr/include/boost/asio/ssl/context.hpp:786:0,
                 from /usr/include/boost/asio/ssl.hpp:19,
                 from /home/my/bitmonero/contrib/epee/include/net/net_helper.h:40,
                 from /home/my/bitmonero/contrib/epee/include/net/http_client.h:40,
                 from /home/my/bitmonero/src/common/download.cpp:36:
/usr/include/boost/asio/ssl/impl/context.ipp: In constructor ‘boost::asio::ssl::context::context(boost::asio::ssl::context_base::method)’:
/usr/include/boost/asio/ssl/impl/context.ipp:83:29: error: ‘::SSLv2_method’ has not been declared
     handle_ = ::SSL_CTX_new(::SSLv2_method());
                             ^
/usr/include/boost/asio/ssl/impl/context.ipp:86:29: error: ‘::SSLv2_client_method’ has not been declared
     handle_ = ::SSL_CTX_new(::SSLv2_client_method());
                             ^
/usr/include/boost/asio/ssl/impl/context.ipp:89:29: error: ‘::SSLv2_server_method’ has not been declared
     handle_ = ::SSL_CTX_new(::SSLv2_server_method());
                             ^
/usr/include/boost/asio/ssl/impl/context.ipp: In destructor ‘boost::asio::ssl::context::~context()’:
/usr/include/boost/asio/ssl/impl/context.ipp:208:16: error: invalid use of incomplete type ‘SSL_CTX {aka struct ssl_ctx_st}’
     if (handle_->default_passwd_callback_userdata)
                ^
In file included from /usr/include/openssl/crypto.h:31:0,
                 from /usr/include/openssl/bio.h:20,
                 from /usr/include/openssl/conf.h:13,
                 from /usr/include/boost/asio/ssl/detail/openssl_types.hpp:19,
                 from /usr/include/boost/asio/ssl/context_base.hpp:19,
                 from /usr/include/boost/asio/ssl/context.hpp:27,
                 from /usr/include/boost/asio/ssl.hpp:19,
                 from /home/my/bitmonero/contrib/epee/include/net/net_helper.h:40,
                 from /home/my/bitmonero/contrib/epee/include/net/http_client.h:40,
                 from /home/my/bitmonero/src/common/download.cpp:36:
/usr/include/openssl/ossl_typ.h:145:16: note: forward declaration of ‘SSL_CTX {aka struct ssl_ctx_st}’
 typedef struct ssl_ctx_st SSL_CTX;
                ^
In file included from /usr/include/boost/asio/ssl/context.hpp:786:0,
                 from /usr/include/boost/asio/ssl.hpp:19,
                 from /home/my/bitmonero/contrib/epee/include/net/net_helper.h:40,
                 from /home/my/bitmonero/contrib/epee/include/net/http_client.h:40,
                 from /home/my/bitmonero/src/common/download.cpp:36:
/usr/include/boost/asio/ssl/impl/context.ipp:212:20: error: invalid use of incomplete type ‘SSL_CTX {aka struct ssl_ctx_st}’
             handle_->default_passwd_callback_userdata);
                    ^
In file included from /usr/include/openssl/crypto.h:31:0,
                 from /usr/include/openssl/bio.h:20,
                 from /usr/include/openssl/conf.h:13,
                 from /usr/include/boost/asio/ssl/detail/openssl_types.hpp:19,
                 from /usr/include/boost/asio/ssl/context_base.hpp:19,
                 from /usr/include/boost/asio/ssl/context.hpp:27,
                 from /usr/include/boost/asio/ssl.hpp:19,
                 from /home/my/bitmonero/contrib/epee/include/net/net_helper.h:40,
                 from /home/my/bitmonero/contrib/epee/include/net/http_client.h:40,
                 from /home/my/bitmonero/src/common/download.cpp:36:
/usr/include/openssl/ossl_typ.h:145:16: note: forward declaration of ‘SSL_CTX {aka struct ssl_ctx_st}’
 typedef struct ssl_ctx_st SSL_CTX;
                ^
In file included from /usr/include/boost/asio/ssl/context.hpp:786:0,
                 from /usr/include/boost/asio/ssl.hpp:19,
                 from /home/my/bitmonero/contrib/epee/include/net/net_helper.h:40,
                 from /home/my/bitmonero/contrib/epee/include/net/http_client.h:40,
                 from /home/my/bitmonero/src/common/download.cpp:36:
/usr/include/boost/asio/ssl/impl/context.ipp:214:14: error: invalid use of incomplete type ‘SSL_CTX {aka struct ssl_ctx_st}’
       handle_->default_passwd_callback_userdata = 0;
              ^
In file included from /usr/include/openssl/crypto.h:31:0,
                 from /usr/include/openssl/bio.h:20,
                 from /usr/include/openssl/conf.h:13,
                 from /usr/include/boost/asio/ssl/detail/openssl_types.hpp:19,
                 from /usr/include/boost/asio/ssl/context_base.hpp:19,
                 from /usr/include/boost/asio/ssl/context.hpp:27,
                 from /usr/include/boost/asio/ssl.hpp:19,
                 from /home/my/bitmonero/contrib/epee/include/net/net_helper.h:40,
                 from /home/my/bitmonero/contrib/epee/include/net/http_client.h:40,
                 from /home/my/bitmonero/src/common/download.cpp:36:
/usr/include/openssl/ossl_typ.h:145:16: note: forward declaration of ‘SSL_CTX {aka struct ssl_ctx_st}’
 typedef struct ssl_ctx_st SSL_CTX;
                ^
In file included from /usr/include/boost/asio/ssl/context.hpp:786:0,
                 from /usr/include/boost/asio/ssl.hpp:19,
                 from /home/my/bitmonero/contrib/epee/include/net/net_helper.h:40,
                 from /home/my/bitmonero/contrib/epee/include/net/http_client.h:40,
                 from /home/my/bitmonero/src/common/download.cpp:36:
/usr/include/boost/asio/ssl/impl/context.ipp: In member function ‘boost::system::error_code boost::asio::ssl::context::use_certificate_chain(const boost::asio::const_buffer&, boost::system::error_code&)’:
/usr/include/boost/asio/ssl/impl/context.ipp:551:18: error: invalid use of incomplete type ‘SSL_CTX {aka struct ssl_ctx_st}’
           handle_->default_passwd_callback,
                  ^
In file included from /usr/include/openssl/crypto.h:31:0,
                 from /usr/include/openssl/bio.h:20,
                 from /usr/include/openssl/conf.h:13,
                 from /usr/include/boost/asio/ssl/detail/openssl_types.hpp:19,
                 from /usr/include/boost/asio/ssl/context_base.hpp:19,
                 from /usr/include/boost/asio/ssl/context.hpp:27,
                 from /usr/include/boost/asio/ssl.hpp:19,
                 from /home/my/bitmonero/contrib/epee/include/net/net_helper.h:40,
                 from /home/my/bitmonero/contrib/epee/include/net/http_client.h:40,
                 from /home/my/bitmonero/src/common/download.cpp:36:
/usr/include/openssl/ossl_typ.h:145:16: note: forward declaration of ‘SSL_CTX {aka struct ssl_ctx_st}’
 typedef struct ssl_ctx_st SSL_CTX;
                ^
In file included from /usr/include/boost/asio/ssl/context.hpp:786:0,
                 from /usr/include/boost/asio/ssl.hpp:19,
                 from /home/my/bitmonero/contrib/epee/include/net/net_helper.h:40,
                 from /home/my/bitmonero/contrib/epee/include/net/http_client.h:40,
                 from /home/my/bitmonero/src/common/download.cpp:36:
/usr/include/boost/asio/ssl/impl/context.ipp:552:18: error: invalid use of incomplete type ‘SSL_CTX {aka struct ssl_ctx_st}’
           handle_->default_passwd_callback_userdata) };
                  ^
In file included from /usr/include/openssl/crypto.h:31:0,
                 from /usr/include/openssl/bio.h:20,
                 from /usr/include/openssl/conf.h:13,
                 from /usr/include/boost/asio/ssl/detail/openssl_types.hpp:19,
                 from /usr/include/boost/asio/ssl/context_base.hpp:19,
                 from /usr/include/boost/asio/ssl/context.hpp:27,
                 from /usr/include/boost/asio/ssl.hpp:19,
                 from /home/my/bitmonero/contrib/epee/include/net/net_helper.h:40,
                 from /home/my/bitmonero/contrib/epee/include/net/http_client.h:40,
                 from /home/my/bitmonero/src/common/download.cpp:36:
/usr/include/openssl/ossl_typ.h:145:16: note: forward declaration of ‘SSL_CTX {aka struct ssl_ctx_st}’
 typedef struct ssl_ctx_st SSL_CTX;
                ^
In file included from /usr/include/boost/asio/ssl/context.hpp:786:0,
                 from /usr/include/boost/asio/ssl.hpp:19,
                 from /home/my/bitmonero/contrib/epee/include/net/net_helper.h:40,
                 from /home/my/bitmonero/contrib/epee/include/net/http_client.h:40,
                 from /home/my/bitmonero/src/common/download.cpp:36:
/usr/include/boost/asio/ssl/impl/context.ipp:569:16: error: invalid use of incomplete type ‘SSL_CTX {aka struct ssl_ctx_st}’
     if (handle_->extra_certs)
                ^
In file included from /usr/include/openssl/crypto.h:31:0,
                 from /usr/include/openssl/bio.h:20,
                 from /usr/include/openssl/conf.h:13,
                 from /usr/include/boost/asio/ssl/detail/openssl_types.hpp:19,
                 from /usr/include/boost/asio/ssl/context_base.hpp:19,
                 from /usr/include/boost/asio/ssl/context.hpp:27,
                 from /usr/include/boost/asio/ssl.hpp:19,
                 from /home/my/bitmonero/contrib/epee/include/net/net_helper.h:40,
                 from /home/my/bitmonero/contrib/epee/include/net/http_client.h:40,
                 from /home/my/bitmonero/src/common/download.cpp:36:
/usr/include/openssl/ossl_typ.h:145:16: note: forward declaration of ‘SSL_CTX {aka struct ssl_ctx_st}’
 typedef struct ssl_ctx_st SSL_CTX;
                ^
In file included from /usr/include/boost/asio/ssl/context.hpp:786:0,
                 from /usr/include/boost/asio/ssl.hpp:19,
                 from /home/my/bitmonero/contrib/epee/include/net/net_helper.h:40,
                 from /home/my/bitmonero/contrib/epee/include/net/http_client.h:40,
                 from /home/my/bitmonero/src/common/download.cpp:36:
/usr/include/boost/asio/ssl/impl/context.ipp:571:33: error: invalid use of incomplete type ‘SSL_CTX {aka struct ssl_ctx_st}’
       ::sk_X509_pop_free(handle_->extra_certs, X509_free);
                                 ^
In file included from /usr/include/openssl/crypto.h:31:0,
                 from /usr/include/openssl/bio.h:20,
                 from /usr/include/openssl/conf.h:13,
                 from /usr/include/boost/asio/ssl/detail/openssl_types.hpp:19,
                 from /usr/include/boost/asio/ssl/context_base.hpp:19,
                 from /usr/include/boost/asio/ssl/context.hpp:27,
                 from /usr/include/boost/asio/ssl.hpp:19,
                 from /home/my/bitmonero/contrib/epee/include/net/net_helper.h:40,
                 from /home/my/bitmonero/contrib/epee/include/net/http_client.h:40,
                 from /home/my/bitmonero/src/common/download.cpp:36:
/usr/include/openssl/ossl_typ.h:145:16: note: forward declaration of ‘SSL_CTX {aka struct ssl_ctx_st}’
 typedef struct ssl_ctx_st SSL_CTX;
                ^
In file included from /usr/include/boost/asio/ssl/context.hpp:786:0,
                 from /usr/include/boost/asio/ssl.hpp:19,
                 from /home/my/bitmonero/contrib/epee/include/net/net_helper.h:40,
                 from /home/my/bitmonero/contrib/epee/include/net/http_client.h:40,
                 from /home/my/bitmonero/src/common/download.cpp:36:
/usr/include/boost/asio/ssl/impl/context.ipp:572:14: error: invalid use of incomplete type ‘SSL_CTX {aka struct ssl_ctx_st}’
       handle_->extra_certs = 0;
              ^
In file included from /usr/include/openssl/crypto.h:31:0,
                 from /usr/include/openssl/bio.h:20,
                 from /usr/include/openssl/conf.h:13,
                 from /usr/include/boost/asio/ssl/detail/openssl_types.hpp:19,
                 from /usr/include/boost/asio/ssl/context_base.hpp:19,
                 from /usr/include/boost/asio/ssl/context.hpp:27,
                 from /usr/include/boost/asio/ssl.hpp:19,
                 from /home/my/bitmonero/contrib/epee/include/net/net_helper.h:40,
                 from /home/my/bitmonero/contrib/epee/include/net/http_client.h:40,
                 from /home/my/bitmonero/src/common/download.cpp:36:
/usr/include/openssl/ossl_typ.h:145:16: note: forward declaration of ‘SSL_CTX {aka struct ssl_ctx_st}’
 typedef struct ssl_ctx_st SSL_CTX;
                ^
In file included from /usr/include/boost/asio/ssl/context.hpp:786:0,
                 from /usr/include/boost/asio/ssl.hpp:19,
                 from /home/my/bitmonero/contrib/epee/include/net/net_helper.h:40,
                 from /home/my/bitmonero/contrib/epee/include/net/http_client.h:40,
                 from /home/my/bitmonero/src/common/download.cpp:36:
/usr/include/boost/asio/ssl/impl/context.ipp:576:18: error: invalid use of incomplete type ‘SSL_CTX {aka struct ssl_ctx_st}’
           handle_->default_passwd_callback,
                  ^
In file included from /usr/include/openssl/crypto.h:31:0,
                 from /usr/include/openssl/bio.h:20,
                 from /usr/include/openssl/conf.h:13,
                 from /usr/include/boost/asio/ssl/detail/openssl_types.hpp:19,
                 from /usr/include/boost/asio/ssl/context_base.hpp:19,
                 from /usr/include/boost/asio/ssl/context.hpp:27,
                 from /usr/include/boost/asio/ssl.hpp:19,
                 from /home/my/bitmonero/contrib/epee/include/net/net_helper.h:40,
                 from /home/my/bitmonero/contrib/epee/include/net/http_client.h:40,
                 from /home/my/bitmonero/src/common/download.cpp:36:
/usr/include/openssl/ossl_typ.h:145:16: note: forward declaration of ‘SSL_CTX {aka struct ssl_ctx_st}’
 typedef struct ssl_ctx_st SSL_CTX;
                ^
In file included from /usr/include/boost/asio/ssl/context.hpp:786:0,
                 from /usr/include/boost/asio/ssl.hpp:19,
                 from /home/my/bitmonero/contrib/epee/include/net/net_helper.h:40,
                 from /home/my/bitmonero/contrib/epee/include/net/http_client.h:40,
                 from /home/my/bitmonero/src/common/download.cpp:36:
/usr/include/boost/asio/ssl/impl/context.ipp:577:18: error: invalid use of incomplete type ‘SSL_CTX {aka struct ssl_ctx_st}’
           handle_->default_passwd_callback_userdata))
                  ^
In file included from /usr/include/openssl/crypto.h:31:0,
                 from /usr/include/openssl/bio.h:20,
                 from /usr/include/openssl/conf.h:13,
                 from /usr/include/boost/asio/ssl/detail/openssl_types.hpp:19,
                 from /usr/include/boost/asio/ssl/context_base.hpp:19,
                 from /usr/include/boost/asio/ssl/context.hpp:27,
                 from /usr/include/boost/asio/ssl.hpp:19,
                 from /home/my/bitmonero/contrib/epee/include/net/net_helper.h:40,
                 from /home/my/bitmonero/contrib/epee/include/net/http_client.h:40,
                 from /home/my/bitmonero/src/common/download.cpp:36:
/usr/include/openssl/ossl_typ.h:145:16: note: forward declaration of ‘SSL_CTX {aka struct ssl_ctx_st}’
 typedef struct ssl_ctx_st SSL_CTX;
                ^
In file included from /usr/include/boost/asio/ssl/context.hpp:786:0,
                 from /usr/include/boost/asio/ssl.hpp:19,
                 from /home/my/bitmonero/contrib/epee/include/net/net_helper.h:40,
                 from /home/my/bitmonero/contrib/epee/include/net/http_client.h:40,
                 from /home/my/bitmonero/src/common/download.cpp:36:
/usr/include/boost/asio/ssl/impl/context.ipp: In member function ‘boost::system::error_code boost::asio::ssl::context::use_private_key(const boost::asio::const_buffer&, boost::asio::ssl::context_base::file_format, boost::system::error_code&)’:
/usr/include/boost/asio/ssl/impl/context.ipp:653:28: error: invalid use of incomplete type ‘SSL_CTX {aka struct ssl_ctx_st}’
           bio.p, 0, handle_->default_passwd_callback,
                            ^
In file included from /usr/include/openssl/crypto.h:31:0,
                 from /usr/include/openssl/bio.h:20,
                 from /usr/include/openssl/conf.h:13,
                 from /usr/include/boost/asio/ssl/detail/openssl_types.hpp:19,
                 from /usr/include/boost/asio/ssl/context_base.hpp:19,
                 from /usr/include/boost/asio/ssl/context.hpp:27,
                 from /usr/include/boost/asio/ssl.hpp:19,
                 from /home/my/bitmonero/contrib/epee/include/net/net_helper.h:40,
                 from /home/my/bitmonero/contrib/epee/include/net/http_client.h:40,
                 from /home/my/bitmonero/src/common/download.cpp:36:
/usr/include/openssl/ossl_typ.h:145:16: note: forward declaration of ‘SSL_CTX {aka struct ssl_ctx_st}’
 typedef struct ssl_ctx_st SSL_CTX;
                ^
In file included from /usr/include/boost/asio/ssl/context.hpp:786:0,
                 from /usr/include/boost/asio/ssl.hpp:19,
                 from /home/my/bitmonero/contrib/epee/include/net/net_helper.h:40,
                 from /home/my/bitmonero/contrib/epee/include/net/http_client.h:40,
                 from /home/my/bitmonero/src/common/download.cpp:36:
/usr/include/boost/asio/ssl/impl/context.ipp:654:18: error: invalid use of incomplete type ‘SSL_CTX {aka struct ssl_ctx_st}’
           handle_->default_passwd_callback_userdata);
                  ^
In file included from /usr/include/openssl/crypto.h:31:0,
                 from /usr/include/openssl/bio.h:20,
                 from /usr/include/openssl/conf.h:13,
                 from /usr/include/boost/asio/ssl/detail/openssl_types.hpp:19,
                 from /usr/include/boost/asio/ssl/context_base.hpp:19,
                 from /usr/include/boost/asio/ssl/context.hpp:27,
                 from /usr/include/boost/asio/ssl.hpp:19,
                 from /home/my/bitmonero/contrib/epee/include/net/net_helper.h:40,
                 from /home/my/bitmonero/contrib/epee/include/net/http_client.h:40,
                 from /home/my/bitmonero/src/common/download.cpp:36:
/usr/include/openssl/ossl_typ.h:145:16: note: forward declaration of ‘SSL_CTX {aka struct ssl_ctx_st}’
 typedef struct ssl_ctx_st SSL_CTX;
                ^
In file included from /usr/include/boost/asio/ssl/context.hpp:786:0,
                 from /usr/include/boost/asio/ssl.hpp:19,
                 from /home/my/bitmonero/contrib/epee/include/net/net_helper.h:40,
                 from /home/my/bitmonero/contrib/epee/include/net/http_client.h:40,
                 from /home/my/bitmonero/src/common/download.cpp:36:
/usr/include/boost/asio/ssl/impl/context.ipp: In member function ‘boost::system::error_code boost::asio::ssl::context::use_rsa_private_key(const boost::asio::const_buffer&, boost::asio::ssl::context_base::file_format, boost::system::error_code&)’:
/usr/include/boost/asio/ssl/impl/context.ipp:712:28: error: invalid use of incomplete type ‘SSL_CTX {aka struct ssl_ctx_st}’
           bio.p, 0, handle_->default_passwd_callback,
                            ^
In file included from /usr/include/openssl/crypto.h:31:0,
                 from /usr/include/openssl/bio.h:20,
                 from /usr/include/openssl/conf.h:13,
                 from /usr/include/boost/asio/ssl/detail/openssl_types.hpp:19,
                 from /usr/include/boost/asio/ssl/context_base.hpp:19,
                 from /usr/include/boost/asio/ssl/context.hpp:27,
                 from /usr/include/boost/asio/ssl.hpp:19,
                 from /home/my/bitmonero/contrib/epee/include/net/net_helper.h:40,
                 from /home/my/bitmonero/contrib/epee/include/net/http_client.h:40,
                 from /home/my/bitmonero/src/common/download.cpp:36:
/usr/include/openssl/ossl_typ.h:145:16: note: forward declaration of ‘SSL_CTX {aka struct ssl_ctx_st}’
 typedef struct ssl_ctx_st SSL_CTX;
                ^
In file included from /usr/include/boost/asio/ssl/context.hpp:786:0,
                 from /usr/include/boost/asio/ssl.hpp:19,
                 from /home/my/bitmonero/contrib/epee/include/net/net_helper.h:40,
                 from /home/my/bitmonero/contrib/epee/include/net/http_client.h:40,
                 from /home/my/bitmonero/src/common/download.cpp:36:
/usr/include/boost/asio/ssl/impl/context.ipp:713:18: error: invalid use of incomplete type ‘SSL_CTX {aka struct ssl_ctx_st}’
           handle_->default_passwd_callback_userdata);
                  ^
In file included from /usr/include/openssl/crypto.h:31:0,
                 from /usr/include/openssl/bio.h:20,
                 from /usr/include/openssl/conf.h:13,
                 from /usr/include/boost/asio/ssl/detail/openssl_types.hpp:19,
                 from /usr/include/boost/asio/ssl/context_base.hpp:19,
                 from /usr/include/boost/asio/ssl/context.hpp:27,
                 from /usr/include/boost/asio/ssl.hpp:19,
                 from /home/my/bitmonero/contrib/epee/include/net/net_helper.h:40,
                 from /home/my/bitmonero/contrib/epee/include/net/http_client.h:40,
                 from /home/my/bitmonero/src/common/download.cpp:36:
/usr/include/openssl/ossl_typ.h:145:16: note: forward declaration of ‘SSL_CTX {aka struct ssl_ctx_st}’
 typedef struct ssl_ctx_st SSL_CTX;
                ^
In file included from /usr/include/boost/asio/ssl/context.hpp:786:0,
                 from /usr/include/boost/asio/ssl.hpp:19,
                 from /home/my/bitmonero/contrib/epee/include/net/net_helper.h:40,
                 from /home/my/bitmonero/contrib/epee/include/net/http_client.h:40,
                 from /home/my/bitmonero/src/common/download.cpp:36:
/usr/include/boost/asio/ssl/impl/context.ipp: In member function ‘boost::system::error_code boost::asio::ssl::context::do_set_password_callback(boost::asio::ssl::detail::password_callback_base*, boost::system::error_code&)’:
/usr/include/boost/asio/ssl/impl/context.ipp:932:14: error: invalid use of incomplete type ‘SSL_CTX {aka struct ssl_ctx_st}’
   if (handle_->default_passwd_callback_userdata)
              ^
In file included from /usr/include/openssl/crypto.h:31:0,
                 from /usr/include/openssl/bio.h:20,
                 from /usr/include/openssl/conf.h:13,
                 from /usr/include/boost/asio/ssl/detail/openssl_types.hpp:19,
                 from /usr/include/boost/asio/ssl/context_base.hpp:19,
                 from /usr/include/boost/asio/ssl/context.hpp:27,
                 from /usr/include/boost/asio/ssl.hpp:19,
                 from /home/my/bitmonero/contrib/epee/include/net/net_helper.h:40,
                 from /home/my/bitmonero/contrib/epee/include/net/http_client.h:40,
                 from /home/my/bitmonero/src/common/download.cpp:36:
/usr/include/openssl/ossl_typ.h:145:16: note: forward declaration of ‘SSL_CTX {aka struct ssl_ctx_st}’
 typedef struct ssl_ctx_st SSL_CTX;
                ^
In file included from /usr/include/boost/asio/ssl/context.hpp:786:0,
                 from /usr/include/boost/asio/ssl.hpp:19,
                 from /home/my/bitmonero/contrib/epee/include/net/net_helper.h:40,
                 from /home/my/bitmonero/contrib/epee/include/net/http_client.h:40,
                 from /home/my/bitmonero/src/common/download.cpp:36:
/usr/include/boost/asio/ssl/impl/context.ipp:934:16: error: invalid use of incomplete type ‘SSL_CTX {aka struct ssl_ctx_st}’
         handle_->default_passwd_callback_userdata);
                ^
In file included from /usr/include/openssl/crypto.h:31:0,
                 from /usr/include/openssl/bio.h:20,
                 from /usr/include/openssl/conf.h:13,
                 from /usr/include/boost/asio/ssl/detail/openssl_types.hpp:19,
                 from /usr/include/boost/asio/ssl/context_base.hpp:19,
                 from /usr/include/boost/asio/ssl/context.hpp:27,
                 from /usr/include/boost/asio/ssl.hpp:19,
                 from /home/my/bitmonero/contrib/epee/include/net/net_helper.h:40,
                 from /home/my/bitmonero/contrib/epee/include/net/http_client.h:40,
                 from /home/my/bitmonero/src/common/download.cpp:36:
/usr/include/openssl/ossl_typ.h:145:16: note: forward declaration of ‘SSL_CTX {aka struct ssl_ctx_st}’
 typedef struct ssl_ctx_st SSL_CTX;
                ^
In file included from /usr/include/boost/asio/ssl/context.hpp:786:0,
                 from /usr/include/boost/asio/ssl.hpp:19,
                 from /home/my/bitmonero/contrib/epee/include/net/net_helper.h:40,
                 from /home/my/bitmonero/contrib/epee/include/net/http_client.h:40,
                 from /home/my/bitmonero/src/common/download.cpp:36:
/usr/include/boost/asio/ssl/impl/context.ipp:936:10: error: invalid use of incomplete type ‘SSL_CTX {aka struct ssl_ctx_st}’
   handle_->default_passwd_callback_userdata = callback;
          ^
In file included from /usr/include/openssl/crypto.h:31:0,
                 from /usr/include/openssl/bio.h:20,
                 from /usr/include/openssl/conf.h:13,
                 from /usr/include/boost/asio/ssl/detail/openssl_types.hpp:19,
                 from /usr/include/boost/asio/ssl/context_base.hpp:19,
                 from /usr/include/boost/asio/ssl/context.hpp:27,
                 from /usr/include/boost/asio/ssl.hpp:19,
                 from /home/my/bitmonero/contrib/epee/include/net/net_helper.h:40,
                 from /home/my/bitmonero/contrib/epee/include/net/http_client.h:40,
                 from /home/my/bitmonero/src/common/download.cpp:36:
/usr/include/openssl/ossl_typ.h:145:16: note: forward declaration of ‘SSL_CTX {aka struct ssl_ctx_st}’
 typedef struct ssl_ctx_st SSL_CTX;
                ^
In file included from /usr/include/openssl/engine.h:30:0,
                 from /usr/include/boost/asio/ssl/detail/openssl_types.hpp:22,
                 from /usr/include/boost/asio/ssl/context_base.hpp:19,
                 from /usr/include/boost/asio/ssl/context.hpp:27,
                 from /usr/include/boost/asio/ssl.hpp:19,
                 from /home/my/bitmonero/contrib/epee/include/net/net_helper.h:40,
                 from /home/my/bitmonero/contrib/epee/include/net/http_client.h:40,
                 from /home/my/bitmonero/src/common/download.cpp:36:
/usr/include/boost/asio/ssl/detail/impl/engine.ipp: In member function ‘const boost::system::error_code& boost::asio::ssl::detail::engine::map_error_code(boost::system::error_code&) const’:
/usr/include/boost/asio/ssl/detail/impl/engine.ipp:207:9: error: ‘SSL_R_SHORT_READ’ was not declared in this scope
         ERR_PACK(ERR_LIB_SSL, 0, SSL_R_SHORT_READ),
         ^
In file included from /usr/include/boost/asio/ssl/detail/engine.hpp:163:0,
                 from /usr/include/boost/asio/ssl/detail/buffered_handshake_op.hpp:21,
                 from /usr/include/boost/asio/ssl/stream.hpp:29,
                 from /usr/include/boost/asio/ssl.hpp:24,
                 from /home/my/bitmonero/contrib/epee/include/net/net_helper.h:40,
                 from /home/my/bitmonero/contrib/epee/include/net/http_client.h:40,
                 from /home/my/bitmonero/src/common/download.cpp:36:
/usr/include/boost/asio/ssl/detail/impl/engine.ipp:214:11: error: invalid use of incomplete type ‘SSL {aka struct ssl_st}’
   if (ssl_->version == SSL2_VERSION)
           ^
In file included from /usr/include/openssl/crypto.h:31:0,
                 from /usr/include/openssl/bio.h:20,
                 from /usr/include/openssl/conf.h:13,
                 from /usr/include/boost/asio/ssl/detail/openssl_types.hpp:19,
                 from /usr/include/boost/asio/ssl/context_base.hpp:19,
                 from /usr/include/boost/asio/ssl/context.hpp:27,
                 from /usr/include/boost/asio/ssl.hpp:19,
                 from /home/my/bitmonero/contrib/epee/include/net/net_helper.h:40,
                 from /home/my/bitmonero/contrib/epee/include/net/http_client.h:40,
                 from /home/my/bitmonero/src/common/download.cpp:36:
/usr/include/openssl/ossl_typ.h:144:16: note: forward declaration of ‘SSL {aka struct ssl_st}’
 typedef struct ssl_st SSL;
                ^
In file included from /usr/include/openssl/engine.h:30:0,
                 from /usr/include/boost/asio/ssl/detail/openssl_types.hpp:22,
                 from /usr/include/boost/asio/ssl/context_base.hpp:19,
                 from /usr/include/boost/asio/ssl/context.hpp:27,
                 from /usr/include/boost/asio/ssl.hpp:19,
                 from /home/my/bitmonero/contrib/epee/include/net/net_helper.h:40,
                 from /home/my/bitmonero/contrib/epee/include/net/http_client.h:40,
                 from /home/my/bitmonero/src/common/download.cpp:36:
/usr/include/boost/asio/ssl/detail/impl/engine.ipp:221:9: error: ‘SSL_R_SHORT_READ’ was not declared in this scope
         ERR_PACK(ERR_LIB_SSL, 0, SSL_R_SHORT_READ),
         ^
/home/my/bitmonero/contrib/epee/include/net/net_helper.h: In member function ‘void epee::net_utils::blocked_mode_client::shutdown_ssl()’:
/home/my/bitmonero/contrib/epee/include/net/net_helper.h:579:106: error: ‘SSL_R_SHORT_READ’ was not declared in this scope
    if (ec.category() == boost::asio::error::get_ssl_category() && ec.value() != ERR_PACK(ERR_LIB_SSL, 0, SSL_R_SHORT_READ))
                                                                                                          ^
make[3]: *** [src/common/CMakeFiles/obj_common.dir/download.cpp.o] Error 1
```

# Discussion History
## ViperRu | 2017-10-16T10:11:19+00:00
Tag v0.11.0.0 builded fine.

## radfish | 2017-10-16T15:23:19+00:00
Your openssl version should be 1.0.1f-1ubuntu2.22 not openssl 1.1.0f-2~ubuntu14.04.1+deb.sury.org+1:
https://packages.ubuntu.com/trusty-updates/openssl
You might have some third-party repository where it came from.

Also, your boost seems to not be coming from 14.04 repos, either:
https://packages.ubuntu.com/trusty-updates/libboost1.54-all-dev

It looks like boost 1.58 does not support openssl 1.1. If you want to build with openssl v1.1, you need a newer boost and #2663.

I don't think there's anything that can be done about this ticket, because it's probably because of the bad combinations of versions on your system. Please consider closing.

## ViperRu | 2017-10-16T15:51:01+00:00
After remove three commits:
git revert 1cf940f2a
git revert e2a276cbb
git revert 79207743b
the current version was build.

## ViperRu | 2017-10-16T16:27:56+00:00
The above error disappears after git revert 1cf940f.
Before git revert e2a276c I had error:
```
[ 85%] Building CXX object src/wallet/CMakeFiles/obj_wallet.dir/wallet2.cpp.o
/home/my/bitmonero/src/wallet/wallet2.cpp: In member function ‘bool tools::wallet2::init(std::string, boost::optional<epee::net_utils::http::login>, uint64_t, bool)’:
/home/my/bitmonero/src/wallet/wallet2.cpp:540:80: error: no matching function for call to ‘epee::net_utils::http::http_simple_client::set_server(std::string, const boost::optional<epee::net_utils::http::login>&, bool&)’
   return m_http_client.set_server(get_daemon_address(), get_daemon_login(), ssl);
                                                                                ^
In file included from /home/my/bitmonero/src/wallet/wallet2.h:46:0,
                 from /home/my/bitmonero/src/wallet/wallet2.cpp:41:
/home/my/bitmonero/contrib/epee/include/net/http_client.h:299:9: note: candidate: bool epee::net_utils::http::http_simple_client::set_server(const string&, boost::optional<epee::net_utils::http::login>)
    bool set_server(const std::string& address, boost::optional<login> user)
         ^
/home/my/bitmonero/contrib/epee/include/net/http_client.h:299:9: note:   candidate expects 2 arguments, 3 provided
/home/my/bitmonero/contrib/epee/include/net/http_client.h:308:9: note: candidate: void epee::net_utils::http::http_simple_client::set_server(std::string, std::string, boost::optional<epee::net_utils::http::login>)
    void set_server(std::string host, std::string port, boost::optional<login> user)
         ^
/home/my/bitmonero/contrib/epee/include/net/http_client.h:308:9: note:   no known conversion for argument 2 from ‘const boost::optional<epee::net_utils::http::login>’ to ‘std::string {aka std::basic_string<char>}’
```
Before git revert 7920774 I had error:
```
[ 84%] Building CXX object src/wallet/CMakeFiles/obj_wallet.dir/api/wallet.cpp.o
/home/my/bitmonero/src/wallet/api/wallet.cpp: In member function ‘bool Monero::WalletImpl::doInit(const string&, uint64_t, bool)’:
/home/my/bitmonero/src/wallet/api/wallet.cpp:1556:90: error: no matching function for call to ‘tools::wallet2::init(const string&, boost::optional<epee::net_utils::http::login>&, uint64_t&, bool&)’
     if (!m_wallet->init(daemon_address, m_daemon_login, upper_transaction_size_limit, ssl))
                                                                                          ^
In file included from /home/my/bitmonero/src/wallet/api/wallet.h:35:0,
                 from /home/my/bitmonero/src/wallet/api/wallet.cpp:32:
/home/my/bitmonero/src/wallet/wallet2.h:427:10: note: candidate: bool tools::wallet2::init(std::string, boost::optional<epee::net_utils::http::login>, uint64_t)
     bool init(std::string daemon_address = "http://localhost:8080",
          ^
/home/my/bitmonero/src/wallet/wallet2.h:427:10: note:   candidate expects 3 arguments, 4 provided
```

## ViperRu | 2017-10-18T03:20:32+00:00
After
>git pull
>git fetch origin pull/2663/head:my_test
>git checkout my_test
>make

the problem is kept.
```
[ 20%] Building CXX object src/common/CMakeFiles/obj_common.dir/download.cpp.o
In file included from /usr/include/openssl/bio.h:20:0,
                 from /usr/include/openssl/conf.h:13,
                 from /usr/include/boost/asio/ssl/detail/openssl_types.hpp:19,
                 from /usr/include/boost/asio/ssl/context_base.hpp:19,
                 from /usr/include/boost/asio/ssl/context.hpp:27,
                 from /usr/include/boost/asio/ssl.hpp:19,
                 from /home/my/bitmonero/contrib/epee/include/net/net_helper.h:41,
                 from /home/my/bitmonero/contrib/epee/include/net/http_client.h:40,
                 from /home/my/bitmonero/src/common/download.cpp:36:
/usr/include/boost/asio/ssl/detail/impl/openssl_init.ipp: In constructor ‘boost::asio::ssl::detail::openssl_init_base::do_init::do_init()’:
/usr/include/boost/asio/ssl/detail/impl/openssl_init.ipp:43:23: error: expected id-expression before ‘(’ token
     mutexes_.resize(::CRYPTO_num_locks());
                       ^
In file included from /usr/include/boost/asio/ssl/detail/openssl_init.hpp:100:0,
                 from /usr/include/boost/asio/ssl/context.hpp:29,
                 from /usr/include/boost/asio/ssl.hpp:19,
                 from /home/my/bitmonero/contrib/epee/include/net/net_helper.h:41,
                 from /home/my/bitmonero/contrib/epee/include/net/http_client.h:40,
                 from /home/my/bitmonero/src/common/download.cpp:36:
/usr/include/boost/asio/ssl/detail/impl/openssl_init.ipp:46:66: error: expected id-expression before ‘;’ token
     ::CRYPTO_set_locking_callback(&do_init::openssl_locking_func);
                                                                  ^
...
```

## radfish | 2017-10-18T03:42:59+00:00
#2663 alone will not fix it. You need #2663 AND newer boost (>= 1.62)  IF you insist on using OpenSSL v1.1. Alternatively, install openssl 1.0. Install boost and openssl packages of versions that match official Ubuntu 14.04 repositories, and it should build. The versions you have are different.

## ViperRu | 2017-10-18T04:07:23+00:00
I have several libs for ssl:
>dpkg -l | grep libssl
```
ii  libssl-dev:amd64                            1.1.0f-2~ubuntu14.04.1+deb.sury.org+1             amd64        Secure Sockets Layer toolkit - development files
ii  libssl0.9.8:i386                            0.9.8o-7ubuntu3.2.14.04.1                         i386         SSL shared libraries
ii  libssl1.0.0:amd64                           1.0.2k-1+deb.sury.org~trusty+1                    amd64        Secure Sockets Layer toolkit - shared libraries
ii  libssl1.0.0:i386                            1.0.2k-1+deb.sury.org~trusty+1                    i386         Secure Sockets Layer toolkit - shared libraries
ii  libssl1.1:amd64                             1.1.0f-2~ubuntu14.04.1+deb.sury.org+1             amd64        Secure Sockets Layer toolkit - shared libraries
```
And I have the problem only with three commits: 1cf940f2a, e2a276cbb, 79207743b. As I wrote above after remove these commits the project builds and works.


## ViperRu | 2017-10-18T04:12:11+00:00
> Alternatively, install openssl 1.0. Install boost and openssl packages of versions that match official Ubuntu 14.04 repositories, and it should build. The versions you have are different.

The oficial repositories Ubuntu 14.04 LTS don't contain boost 1.58 which project need.

## radfish | 2017-10-18T04:32:22+00:00
Based on your boost version (1.58 iirc), you have to build against one of these:

On Tue, Oct 17, 2017 at 09:07:28PM -0700, Andrey wrote:
> ii  libssl1.0.0:amd64                           1.0.2k-1+deb.sury.org~trusty+1                    amd64        Secure Sockets Layer toolkit - shared libraries
> ii  libssl1.0.0:i386                            1.0.2k-1+deb.sury.org~trusty+1                    i386         Secure Sockets Layer toolkit - shared libraries

Check `dpkg -L libssl1.0.0` to see where the include and the lib dir are
and then add the paths to your cmake command, similar to this:
`cmake -DOPENSSL_ROOT_DIR='/usr/include/openssl-1.0;/usr/lib/openssl-1.0' .......`
With #2663.


## ViperRu | 2017-10-18T09:52:54+00:00
I replaced some packets (sury repo) to ubuntu repositaries and the problem with 1cf940f2a (epee http_client SSL support) solved without #2663. But other problem was appear:
> dpkg -l |grep libzmq
```
ii  libzmq3:amd64                               4.0.4+dfsg-2                                      amd64        lightweight messaging kernel (shared library)
ii  libzmq3-dev:amd64                           4.0.4+dfsg-2                                      amd64        lightweight messaging kernel (development files)
```
The build is broken with
```
[ 82%] Building CXX object src/rpc/CMakeFiles/obj_daemon_rpc_server.dir/zmq_server.cpp.o
/home/my/bitmonero/src/rpc/zmq_server.cpp: In member function ‘bool cryptonote::rpc::ZmqServer::addTCPSocket(std::string, std::string)’:
/home/my/bitmonero/src/rpc/zmq_server.cpp:105:69: error: no matching function for call to ‘zmq::socket_t::setsockopt(int, const int&)’
     rep_socket->setsockopt(ZMQ_RCVTIMEO, DEFAULT_RPC_RECV_TIMEOUT_MS);
                                                                     ^
In file included from /home/my/bitmonero/src/rpc/zmq_server.h:32:0,
                 from /home/my/bitmonero/src/rpc/zmq_server.cpp:29:
/usr/include/zmq.hpp:354:21: note: candidate: void zmq::socket_t::setsockopt(int, const void*, size_t)
         inline void setsockopt (int option_, const void *optval_,
                     ^
/usr/include/zmq.hpp:354:21: note:   candidate expects 3 arguments, 2 provided
```

## radfish | 2017-10-18T17:51:16+00:00
I have not seen that. My zmq version is 4.2.2. (Maybe min version of v3.0.0 in README is incorrect?)

## ViperRu | 2017-10-19T08:43:04+00:00
The project was build after:
> git diff
```
diff --git a/src/rpc/zmq_server.cpp b/src/rpc/zmq_server.cpp
index afdff23..6f06f44 100644
--- a/src/rpc/zmq_server.cpp
+++ b/src/rpc/zmq_server.cpp
@@ -102,7 +102,7 @@ bool ZmqServer::addTCPSocket(std::string address, std::string port)
 
     rep_socket.reset(new zmq::socket_t(context, ZMQ_REP));
 
-    rep_socket->setsockopt(ZMQ_RCVTIMEO, DEFAULT_RPC_RECV_TIMEOUT_MS);
+    rep_socket->setsockopt(ZMQ_RCVTIMEO, &DEFAULT_RPC_RECV_TIMEOUT_MS, sizeof(DEFAULT_RPC_RECV_TIMEOUT_MS));
 
     std::string bind_address = addr_prefix + address + std::string(":") + port;
     rep_socket->bind(bind_address.c_str());
```
I don't understand what I made. I founded the example of use this function on the Internet.

## Riiume | 2017-10-19T14:26:45+00:00
I encountered one of the build errors (dealing with SSL) that ViperRU had (Boost worked fine for me, as I have 1.62 installed).

I fixed the error by following ViperRU's suggestion, `git revert 1cf940f`

My platform: `Linux MoneroWorkshop1 4.13.0-1-amd64 #1 SMP Debian 4.13.4-2 (2017-10-15) x86_64 GNU/Linux`

Installed apt packages: 
[installedpackages.txt](https://github.com/monero-project/monero/files/1398757/installedpackages.txt)


## radfish | 2017-10-19T14:56:00+00:00
@Riiume can you post the full output from cmake or make including the command?

## Riiume | 2017-10-19T15:04:08+00:00
Attached the build output. I should mention that I merged these [11 commits](https://github.com/monero-project/monero/pull/2134/commits) from @moneromooo-monero .
[buildoutput1.txt](https://github.com/monero-project/monero/files/1398890/buildoutput1.txt)


## tewinget | 2017-10-20T22:25:46+00:00
@ViperRu that change to the setsockopt call should be fine.  There should be a 2-argument version of that call for basic types, but it's possible that convenience overload was added in a more recent version than your distro has packaged.

I have no build issues on Ubuntu with the following w.r.t. zmq:
```
$ dpkg -l | grep zmq
ii  libzmq3-dev:amd64                                           4.2.1-2ubuntu1                                amd64        lightweight messaging kernel (development files)
ii  libzmq5:amd64                                               4.2.1-2ubuntu1                                amd64        lightweight messaging kernel (shared library)
```

## ViperRu | 2017-10-21T05:54:50+00:00
@tewinget As I understand this change will be work and in the more later version of libzmq? May be to change call in the project?

## tewinget | 2017-10-21T06:11:51+00:00
I commented on another thread (this issue?) regarding this.  For relatively
recent versions of zmq this seems to be a non-issue.  I'll look into the
specifics and write cmake complaints if it seems relevant.

On Oct 19, 2017 4:43 AM, "Andrey" <notifications@github.com> wrote:

> The project was build after:
>
> git diff
>
> diff --git a/src/rpc/zmq_server.cpp b/src/rpc/zmq_server.cpp
> index afdff23..6f06f44 100644
> --- a/src/rpc/zmq_server.cpp
> +++ b/src/rpc/zmq_server.cpp
> @@ -102,7 +102,7 @@ bool ZmqServer::addTCPSocket(std::string address, std::string port)
>
>      rep_socket.reset(new zmq::socket_t(context, ZMQ_REP));
>
> -    rep_socket->setsockopt(ZMQ_RCVTIMEO, DEFAULT_RPC_RECV_TIMEOUT_MS);
> +    rep_socket->setsockopt(ZMQ_RCVTIMEO, &DEFAULT_RPC_RECV_TIMEOUT_MS, sizeof(DEFAULT_RPC_RECV_TIMEOUT_MS));
>
>      std::string bind_address = addr_prefix + address + std::string(":") + port;
>      rep_socket->bind(bind_address.c_str());
>
> I don't understand what I made. I founded the example of use this function
> on the Internet.
>
> —
> You are receiving this because you are subscribed to this thread.
> Reply to this email directly, view it on GitHub
> <https://github.com/monero-project/monero/issues/2667#issuecomment-337840590>,
> or mute the thread
> <https://github.com/notifications/unsubscribe-auth/AE3k5lL6SurUarIcb2qOP68F4mVBdkJlks5stwuagaJpZM4P6X6l>
> .
>


# Action History
- Created by: ViperRu | 2017-10-16T10:00:57+00:00
- Closed at: 2017-11-08T20:31:43+00:00
