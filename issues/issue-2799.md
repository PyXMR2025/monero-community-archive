---
title: invalid use of incomplete type 'SSL_CTX {aka struct ssl_ctx_st}'
source_url: https://github.com/monero-project/monero/issues/2799
author: serhack
assignees: []
labels: []
created_at: '2017-11-13T20:30:21+00:00'
updated_at: '2018-01-19T00:00:32+00:00'
type: issue
status: closed
closed_at: '2018-01-19T00:00:32+00:00'
---

# Original Description
Hello,

I'm trying to build Monero in my server. I created a partitioned disk only for building Monero.

OS: Debian 8.9
Platform: 64bit System, 50gb hard disk, 1gb RAM 

I have cloned the repo 'monero' and
`cd monero && make`

GCC Version is the latest, cmake version 3.10


# Discussion History
## moneromooo-monero | 2017-11-13T20:59:38+00:00
Latest GCC version is currently 7.2, is that right ?

I had also asked for OpenSSL version and boost version (we use openssl via boost).


## serhack | 2017-11-14T12:23:15+00:00
GCC is 7.2

## serhack | 2017-11-14T19:48:59+00:00
BOOST Version: 1.62
OpenSSL version: OpenSSL 1.1.0g  


## moneromooo-monero | 2017-11-14T19:51:42+00:00
Do you have commit 29497f7920e8c171bdce076718513c2b062961c0 ? If not, update. If yes, make clean and try again.

## serhack | 2017-11-26T12:34:02+00:00
I have cleaned my vps and I added more swap. Now compilation works well. Can we close @moneromooo-monero ?

## moneromooo-monero | 2017-11-26T22:36:01+00:00
That's got nothing to do with the SSL type error, which has got to do with particular versions of software.

## lacksfish | 2017-11-27T20:44:36+00:00
I just had the same issue on a different computer (Ubuntu 16.04 LTS), might it have to do with libssl1.1.0g? Looks as if boost1.58 does not like openssl1.1.0.

```
$ make
mkdir -p build/release
cd build/release && cmake -D BUILD_TESTS=ON -D CMAKE_BUILD_TYPE=release ../.. && make
-- The C compiler identification is GNU 5.4.0
-- The CXX compiler identification is GNU 5.4.0
-- Check for working C compiler: /usr/bin/cc
-- Check for working C compiler: /usr/bin/cc -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Detecting C compile features
-- Detecting C compile features - done
-- Check for working CXX compiler: /usr/bin/c++
-- Check for working CXX compiler: /usr/bin/c++ -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Building without build tag
-- Could not find DEVELOPER_LOCAL_TOOLS in env (not required)
-- BOOST_IGNORE_SYSTEM_PATHS defaults to OFF
-- Could not find DEVELOPER_LIBUNBOUND_OLD in env (not required)
-- Building for a 64-bit system
-- Building internal libraries as static
-- Could not find DATABASE in env (not required unless you want to change database type from default: lmdb)
-- Using LMDB as default DB type
-- Stack trace on exception enabled (using easylogging++)
-- Looking for pthread.h
-- Looking for pthread.h - found
-- Looking for pthread_create
-- Looking for pthread_create - not found
-- Check if compiler accepts -pthread
-- Check if compiler accepts -pthread - yes
-- Found Threads: TRUE  
-- Found OpenSSL: /usr/lib/x86_64-linux-gnu/libssl.so;/usr/lib/x86_64-linux-gnu/libcrypto.so (found version "1.1.0g") 
-- Using OpenSSL include dir at /usr/include
-- Found MiniUPnPc: /usr/include/miniupnpc  
-- Found miniupnpc API version 10
-- Using shared miniupnpc found at /usr/include/miniupnpc
-- Looking for libunbound
-- Found libunbound include (unbound.h) in /usr/include
-- Found libunbound shared library
-- Using 64-bit LMDB from source tree
-- Building on x86_64 for native
-- AES support enabled
-- Found Boost Version: 105800
-- Found Readline: /usr/include  
-- Performing Test GNU_READLINE_FOUND
-- Performing Test GNU_READLINE_FOUND - Success
-- Found readline library at: /usr
-- Found Git: /usr/bin/git
-- Found GTest: /usr/lib/libgtest.a  
-- Found Doxygen: /usr/bin/doxygen (found version "1.8.11") 
-- Configuring done
-- Generating done
-- Build files have been written to: [path]/monero/build/release
```

and then later down the line

```
[ 18%] Building CXX object src/common/CMakeFiles/obj_common.dir/base58.cpp.o
[ 18%] Building CXX object src/common/CMakeFiles/obj_common.dir/command_line.cpp.o
[ 19%] Building CXX object src/common/CMakeFiles/obj_common.dir/dns_utils.cpp.o
[ 19%] Building CXX object src/common/CMakeFiles/obj_common.dir/download.cpp.o
In file included from /usr/include/openssl/bio.h:20:0,
                 from /usr/include/openssl/conf.h:13,
                 from /usr/include/boost/asio/ssl/detail/openssl_types.hpp:19,
                 from /usr/include/boost/asio/ssl/context_base.hpp:19,
                 from /usr/include/boost/asio/ssl/context.hpp:27,
                 from /usr/include/boost/asio/ssl.hpp:19,
                 from [path]/contrib/epee/include/net/net_helper.h:41,
                 from [path]/contrib/epee/include/net/http_client.h:40,
                 from [path]/src/common/download.cpp:36:
/usr/include/boost/asio/ssl/detail/impl/openssl_init.ipp: In constructor ‘boost::asio::ssl::detail::openssl_init_base::do_init::do_init()’:
/usr/include/boost/asio/ssl/detail/impl/openssl_init.ipp:43:23: error: expected id-expression before ‘(’ token
     mutexes_.resize(::CRYPTO_num_locks());
                       ^
In file included from /usr/include/boost/asio/ssl/detail/openssl_init.hpp:100:0,
                 from /usr/include/boost/asio/ssl/context.hpp:29,
                 from /usr/include/boost/asio/ssl.hpp:19,
                 from [path]/contrib/epee/include/net/net_helper.h:41,
                 from [path]/contrib/epee/include/net/http_client.h:40,
                 from [path]/src/common/download.cpp:36:
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
                 from [path]/contrib/epee/include/net/net_helper.h:41,
                 from [path]/contrib/epee/include/net/http_client.h:40,
                 from [path]/src/common/download.cpp:36:
/usr/include/boost/asio/ssl/detail/impl/openssl_init.ipp:66:7: error: expected id-expression before ‘while’
     ::ERR_free_strings();
       ^
In file included from /usr/include/openssl/x509.h:23:0,
                 from /usr/include/openssl/ssl.h:50,
                 from /usr/include/boost/asio/ssl/detail/openssl_types.hpp:20,
                 from /usr/include/boost/asio/ssl/context_base.hpp:19,
                 from /usr/include/boost/asio/ssl/context.hpp:27,
                 from /usr/include/boost/asio/ssl.hpp:19,
                 from [path]/contrib/epee/include/net/net_helper.h:41,
                 from [path]/contrib/epee/include/net/http_client.h:40,
                 from [path]/src/common/download.cpp:36:
/usr/include/boost/asio/ssl/detail/impl/openssl_init.ipp:72:7: error: expected id-expression before ‘while’
     ::EVP_cleanup();
       ^
In file included from /usr/include/openssl/bio.h:20:0,
                 from /usr/include/openssl/conf.h:13,
                 from /usr/include/boost/asio/ssl/detail/openssl_types.hpp:19,
                 from /usr/include/boost/asio/ssl/context_base.hpp:19,
                 from /usr/include/boost/asio/ssl/context.hpp:27,
                 from /usr/include/boost/asio/ssl.hpp:19,
                 from [path]/contrib/epee/include/net/net_helper.h:41,
                 from [path]/contrib/epee/include/net/http_client.h:40,
                 from [path]/src/common/download.cpp:36:
/usr/include/boost/asio/ssl/detail/impl/openssl_init.ipp:73:7: error: expected id-expression before ‘while’
     ::CRYPTO_cleanup_all_ex_data();
       ^
In file included from /usr/include/boost/asio/ssl/detail/openssl_types.hpp:22:0,
                 from /usr/include/boost/asio/ssl/context_base.hpp:19,
                 from /usr/include/boost/asio/ssl/context.hpp:27,
                 from /usr/include/boost/asio/ssl.hpp:19,
                 from [path]/contrib/epee/include/net/net_helper.h:41,
                 from [path]/contrib/epee/include/net/http_client.h:40,
                 from [path]/src/common/download.cpp:36:
/usr/include/boost/asio/ssl/detail/impl/openssl_init.ipp:76:7: error: expected id-expression before ‘while’
     ::ENGINE_cleanup();
       ^
In file included from /usr/include/boost/asio/ssl/context.hpp:786:0,
                 from /usr/include/boost/asio/ssl.hpp:19,
                 from [path]/contrib/epee/include/net/net_helper.h:41,
                 from [path]/contrib/epee/include/net/http_client.h:40,
                 from [path]/src/common/download.cpp:36:
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
                 from [path]/contrib/epee/include/net/net_helper.h:41,
                 from [path]/contrib/epee/include/net/http_client.h:40,
                 from [path]/src/common/download.cpp:36:
/usr/include/openssl/ossl_typ.h:145:16: note: forward declaration of ‘SSL_CTX {aka struct ssl_ctx_st}’
 typedef struct ssl_ctx_st SSL_CTX;
                ^
In file included from /usr/include/boost/asio/ssl/context.hpp:786:0,
                 from /usr/include/boost/asio/ssl.hpp:19,
                 from [path]/contrib/epee/include/net/net_helper.h:41,
                 from [path]/contrib/epee/include/net/http_client.h:40,
                 from [path]/src/common/download.cpp:36:
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
                 from [path]/contrib/epee/include/net/net_helper.h:41,
                 from [path]/contrib/epee/include/net/http_client.h:40,
                 from [path]/src/common/download.cpp:36:
/usr/include/openssl/ossl_typ.h:145:16: note: forward declaration of ‘SSL_CTX {aka struct ssl_ctx_st}’
 typedef struct ssl_ctx_st SSL_CTX;
                ^
In file included from /usr/include/boost/asio/ssl/context.hpp:786:0,
                 from /usr/include/boost/asio/ssl.hpp:19,
                 from [path]/contrib/epee/include/net/net_helper.h:41,
                 from [path]/contrib/epee/include/net/http_client.h:40,
                 from [path]/src/common/download.cpp:36:
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
                 from [path]/contrib/epee/include/net/net_helper.h:41,
                 from [path]/contrib/epee/include/net/http_client.h:40,
                 from [path]/src/common/download.cpp:36:
/usr/include/openssl/ossl_typ.h:145:16: note: forward declaration of ‘SSL_CTX {aka struct ssl_ctx_st}’
 typedef struct ssl_ctx_st SSL_CTX;
                ^
In file included from /usr/include/boost/asio/ssl/context.hpp:786:0,
                 from /usr/include/boost/asio/ssl.hpp:19,
                 from [path]/contrib/epee/include/net/net_helper.h:41,
                 from [path]/contrib/epee/include/net/http_client.h:40,
                 from [path]/src/common/download.cpp:36:
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
                 from [path]/contrib/epee/include/net/net_helper.h:41,
                 from [path]/contrib/epee/include/net/http_client.h:40,
                 from [path]/src/common/download.cpp:36:
/usr/include/openssl/ossl_typ.h:145:16: note: forward declaration of ‘SSL_CTX {aka struct ssl_ctx_st}’
 typedef struct ssl_ctx_st SSL_CTX;
                ^
In file included from /usr/include/boost/asio/ssl/context.hpp:786:0,
                 from /usr/include/boost/asio/ssl.hpp:19,
                 from [path]/contrib/epee/include/net/net_helper.h:41,
                 from [path]/contrib/epee/include/net/http_client.h:40,
                 from [path]/src/common/download.cpp:36:
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
                 from [path]/contrib/epee/include/net/net_helper.h:41,
                 from [path]/contrib/epee/include/net/http_client.h:40,
                 from [path]/src/common/download.cpp:36:
/usr/include/openssl/ossl_typ.h:145:16: note: forward declaration of ‘SSL_CTX {aka struct ssl_ctx_st}’
 typedef struct ssl_ctx_st SSL_CTX;
                ^
In file included from /usr/include/boost/asio/ssl/context.hpp:786:0,
                 from /usr/include/boost/asio/ssl.hpp:19,
                 from [path]/contrib/epee/include/net/net_helper.h:41,
                 from [path]/contrib/epee/include/net/http_client.h:40,
                 from [path]/src/common/download.cpp:36:
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
                 from [path]/contrib/epee/include/net/net_helper.h:41,
                 from [path]/contrib/epee/include/net/http_client.h:40,
                 from [path]/src/common/download.cpp:36:
/usr/include/openssl/ossl_typ.h:145:16: note: forward declaration of ‘SSL_CTX {aka struct ssl_ctx_st}’
 typedef struct ssl_ctx_st SSL_CTX;
                ^
In file included from /usr/include/boost/asio/ssl/context.hpp:786:0,
                 from /usr/include/boost/asio/ssl.hpp:19,
                 from [path]/contrib/epee/include/net/net_helper.h:41,
                 from [path]/contrib/epee/include/net/http_client.h:40,
                 from [path]/src/common/download.cpp:36:
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
                 from [path]/contrib/epee/include/net/net_helper.h:41,
                 from [path]/contrib/epee/include/net/http_client.h:40,
                 from [path]/src/common/download.cpp:36:
/usr/include/openssl/ossl_typ.h:145:16: note: forward declaration of ‘SSL_CTX {aka struct ssl_ctx_st}’
 typedef struct ssl_ctx_st SSL_CTX;
                ^
In file included from /usr/include/boost/asio/ssl/context.hpp:786:0,
                 from /usr/include/boost/asio/ssl.hpp:19,
                 from [path]/contrib/epee/include/net/net_helper.h:41,
                 from [path]/contrib/epee/include/net/http_client.h:40,
                 from [path]/src/common/download.cpp:36:
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
                 from [path]/contrib/epee/include/net/net_helper.h:41,
                 from [path]/contrib/epee/include/net/http_client.h:40,
                 from [path]/src/common/download.cpp:36:
/usr/include/openssl/ossl_typ.h:145:16: note: forward declaration of ‘SSL_CTX {aka struct ssl_ctx_st}’
 typedef struct ssl_ctx_st SSL_CTX;
                ^
In file included from /usr/include/boost/asio/ssl/context.hpp:786:0,
                 from /usr/include/boost/asio/ssl.hpp:19,
                 from [path]/contrib/epee/include/net/net_helper.h:41,
                 from [path]/contrib/epee/include/net/http_client.h:40,
                 from [path]/src/common/download.cpp:36:
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
                 from [path]/contrib/epee/include/net/net_helper.h:41,
                 from [path]/contrib/epee/include/net/http_client.h:40,
                 from [path]/src/common/download.cpp:36:
/usr/include/openssl/ossl_typ.h:145:16: note: forward declaration of ‘SSL_CTX {aka struct ssl_ctx_st}’
 typedef struct ssl_ctx_st SSL_CTX;
                ^
In file included from /usr/include/boost/asio/ssl/context.hpp:786:0,
                 from /usr/include/boost/asio/ssl.hpp:19,
                 from [path]/contrib/epee/include/net/net_helper.h:41,
                 from [path]/contrib/epee/include/net/http_client.h:40,
                 from [path]/src/common/download.cpp:36:
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
                 from [path]/contrib/epee/include/net/net_helper.h:41,
                 from [path]/contrib/epee/include/net/http_client.h:40,
                 from [path]/src/common/download.cpp:36:
/usr/include/openssl/ossl_typ.h:145:16: note: forward declaration of ‘SSL_CTX {aka struct ssl_ctx_st}’
 typedef struct ssl_ctx_st SSL_CTX;
                ^
In file included from /usr/include/boost/asio/ssl/context.hpp:786:0,
                 from /usr/include/boost/asio/ssl.hpp:19,
                 from [path]/contrib/epee/include/net/net_helper.h:41,
                 from [path]/contrib/epee/include/net/http_client.h:40,
                 from [path]/src/common/download.cpp:36:
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
                 from [path]/contrib/epee/include/net/net_helper.h:41,
                 from [path]/contrib/epee/include/net/http_client.h:40,
                 from [path]/src/common/download.cpp:36:
/usr/include/openssl/ossl_typ.h:145:16: note: forward declaration of ‘SSL_CTX {aka struct ssl_ctx_st}’
 typedef struct ssl_ctx_st SSL_CTX;
                ^
In file included from /usr/include/boost/asio/ssl/context.hpp:786:0,
                 from /usr/include/boost/asio/ssl.hpp:19,
                 from [path]/contrib/epee/include/net/net_helper.h:41,
                 from [path]/contrib/epee/include/net/http_client.h:40,
                 from [path]/src/common/download.cpp:36:
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
                 from [path]/contrib/epee/include/net/net_helper.h:41,
                 from [path]/contrib/epee/include/net/http_client.h:40,
                 from [path]/src/common/download.cpp:36:
/usr/include/openssl/ossl_typ.h:145:16: note: forward declaration of ‘SSL_CTX {aka struct ssl_ctx_st}’
 typedef struct ssl_ctx_st SSL_CTX;
                ^
In file included from /usr/include/boost/asio/ssl/context.hpp:786:0,
                 from /usr/include/boost/asio/ssl.hpp:19,
                 from [path]/contrib/epee/include/net/net_helper.h:41,
                 from [path]/contrib/epee/include/net/http_client.h:40,
                 from [path]/src/common/download.cpp:36:
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
                 from [path]/contrib/epee/include/net/net_helper.h:41,
                 from [path]/contrib/epee/include/net/http_client.h:40,
                 from [path]/src/common/download.cpp:36:
/usr/include/openssl/ossl_typ.h:145:16: note: forward declaration of ‘SSL_CTX {aka struct ssl_ctx_st}’
 typedef struct ssl_ctx_st SSL_CTX;
                ^
In file included from /usr/include/boost/asio/ssl/context.hpp:786:0,
                 from /usr/include/boost/asio/ssl.hpp:19,
                 from [path]/contrib/epee/include/net/net_helper.h:41,
                 from [path]/contrib/epee/include/net/http_client.h:40,
                 from [path]/src/common/download.cpp:36:
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
                 from [path]/contrib/epee/include/net/net_helper.h:41,
                 from [path]/contrib/epee/include/net/http_client.h:40,
                 from [path]/src/common/download.cpp:36:
/usr/include/openssl/ossl_typ.h:145:16: note: forward declaration of ‘SSL_CTX {aka struct ssl_ctx_st}’
 typedef struct ssl_ctx_st SSL_CTX;
                ^
In file included from /usr/include/boost/asio/ssl/context.hpp:786:0,
                 from /usr/include/boost/asio/ssl.hpp:19,
                 from [path]/contrib/epee/include/net/net_helper.h:41,
                 from [path]/contrib/epee/include/net/http_client.h:40,
                 from [path]/src/common/download.cpp:36:
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
                 from [path]/contrib/epee/include/net/net_helper.h:41,
                 from [path]/contrib/epee/include/net/http_client.h:40,
                 from [path]/src/common/download.cpp:36:
/usr/include/openssl/ossl_typ.h:145:16: note: forward declaration of ‘SSL_CTX {aka struct ssl_ctx_st}’
 typedef struct ssl_ctx_st SSL_CTX;
                ^
In file included from /usr/include/boost/asio/ssl/context.hpp:786:0,
                 from /usr/include/boost/asio/ssl.hpp:19,
                 from [path]/contrib/epee/include/net/net_helper.h:41,
                 from [path]/contrib/epee/include/net/http_client.h:40,
                 from [path]/src/common/download.cpp:36:
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
                 from [path]/contrib/epee/include/net/net_helper.h:41,
                 from [path]/contrib/epee/include/net/http_client.h:40,
                 from [path]/src/common/download.cpp:36:
/usr/include/openssl/ossl_typ.h:145:16: note: forward declaration of ‘SSL_CTX {aka struct ssl_ctx_st}’
 typedef struct ssl_ctx_st SSL_CTX;
                ^
In file included from /usr/include/boost/asio/ssl/context.hpp:786:0,
                 from /usr/include/boost/asio/ssl.hpp:19,
                 from [path]/contrib/epee/include/net/net_helper.h:41,
                 from [path]/contrib/epee/include/net/http_client.h:40,
                 from [path]/src/common/download.cpp:36:
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
                 from [path]/contrib/epee/include/net/net_helper.h:41,
                 from [path]/contrib/epee/include/net/http_client.h:40,
                 from [path]/src/common/download.cpp:36:
/usr/include/openssl/ossl_typ.h:145:16: note: forward declaration of ‘SSL_CTX {aka struct ssl_ctx_st}’
 typedef struct ssl_ctx_st SSL_CTX;
                ^
In file included from /usr/include/openssl/engine.h:30:0,
                 from /usr/include/boost/asio/ssl/detail/openssl_types.hpp:22,
                 from /usr/include/boost/asio/ssl/context_base.hpp:19,
                 from /usr/include/boost/asio/ssl/context.hpp:27,
                 from /usr/include/boost/asio/ssl.hpp:19,
                 from [path]/contrib/epee/include/net/net_helper.h:41,
                 from [path]/contrib/epee/include/net/http_client.h:40,
                 from [path]/src/common/download.cpp:36:
/usr/include/boost/asio/ssl/detail/impl/engine.ipp: In member function ‘const boost::system::error_code& boost::asio::ssl::detail::engine::map_error_code(boost::system::error_code&) const’:
/usr/include/boost/asio/ssl/detail/impl/engine.ipp:207:9: error: ‘SSL_R_SHORT_READ’ was not declared in this scope
         ERR_PACK(ERR_LIB_SSL, 0, SSL_R_SHORT_READ),
         ^
In file included from /usr/include/boost/asio/ssl/detail/engine.hpp:163:0,
                 from /usr/include/boost/asio/ssl/detail/buffered_handshake_op.hpp:21,
                 from /usr/include/boost/asio/ssl/stream.hpp:29,
                 from /usr/include/boost/asio/ssl.hpp:24,
                 from [path]/contrib/epee/include/net/net_helper.h:41,
                 from [path]/contrib/epee/include/net/http_client.h:40,
                 from [path]/src/common/download.cpp:36:
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
                 from [path]/contrib/epee/include/net/net_helper.h:41,
                 from [path]/contrib/epee/include/net/http_client.h:40,
                 from [path]/src/common/download.cpp:36:
/usr/include/openssl/ossl_typ.h:144:16: note: forward declaration of ‘SSL {aka struct ssl_st}’
 typedef struct ssl_st SSL;
                ^
In file included from /usr/include/openssl/engine.h:30:0,
                 from /usr/include/boost/asio/ssl/detail/openssl_types.hpp:22,
                 from /usr/include/boost/asio/ssl/context_base.hpp:19,
                 from /usr/include/boost/asio/ssl/context.hpp:27,
                 from /usr/include/boost/asio/ssl.hpp:19,
                 from [path]/contrib/epee/include/net/net_helper.h:41,
                 from [path]/contrib/epee/include/net/http_client.h:40,
                 from [path]/src/common/download.cpp:36:
/usr/include/boost/asio/ssl/detail/impl/engine.ipp:221:9: error: ‘SSL_R_SHORT_READ’ was not declared in this scope
         ERR_PACK(ERR_LIB_SSL, 0, SSL_R_SHORT_READ),
         ^
[path]/contrib/epee/include/net/net_helper.h: In member function ‘void epee::net_utils::blocked_mode_client::shutdown_ssl()’:
[path]/contrib/epee/include/net/net_helper.h:585:33: error: ‘SSL_R_SHORT_READ’ was not declared in this scope
        ERR_PACK(ERR_LIB_SSL, 0, SSL_R_SHORT_READ)
                                 ^
src/common/CMakeFiles/obj_common.dir/build.make:134: recipe for target 'src/common/CMakeFiles/obj_common.dir/download.cpp.o' failed
make[3]: *** [src/common/CMakeFiles/obj_common.dir/download.cpp.o] Error 1
make[3]: Leaving directory '[path]/build/release'
CMakeFiles/Makefile2:585: recipe for target 'src/common/CMakeFiles/obj_common.dir/all' failed
make[2]: *** [src/common/CMakeFiles/obj_common.dir/all] Error 2
make[2]: Leaving directory '[path]/build/release'
Makefile:138: recipe for target 'all' failed
make[1]: *** [all] Error 2
make[1]: Leaving directory '[path]/build/release'
Makefile:62: recipe for target 'release-all' failed
make: *** [release-all] Error 2

```


## moneromooo-monero | 2017-11-27T22:30:43+00:00
Did you build from scratch ? The cmake stuff is supposed to warn if you're using incompatible boost and openssl versions (29497f7920e8c171bdce076718513c2b062961c0)

## lacksfish | 2017-11-28T11:15:42+00:00
I've ran `make clean` before, was thinking the same thing. I've seen no notification like I would expect to see from 29497f7920e8c171bdce076718513c2b062961c0

## moneromooo-monero | 2017-11-28T11:32:47+00:00
Maybe the version check should be against 106200, not 1.62. Not sure how that one works. Try it :)

## lacksfish | 2017-11-28T18:09:12+00:00
After building boost-1.65 I get a different error.

```
[ 54%] Building CXX object tests/core_tests/CMakeFiles/core_tests.dir/block_reward.cpp.o
[ 54%] Linking CXX executable ../../bin/monero-blockchain-export
[ 54%] Building CXX object src/blockchain_utilities/CMakeFiles/blockchain_import.dir/blocksdat_file.cpp.o
/usr/bin/ld: warning: libssl.so.1.0.0, needed by /usr/lib/gcc/x86_64-linux-gnu/5/../../../x86_64-linux-gnu/libunbound.so, may conflict with libssl.so.1.1
/usr/bin/ld: warning: libcrypto.so.1.0.0, needed by /usr/lib/gcc/x86_64-linux-gnu/5/../../../x86_64-linux-gnu/libunbound.so, may conflict with libcrypto.so.1.1
../cryptonote_core/libcryptonote_core.a(blockchain.cpp.o): In function `cryptonote::Blockchain::prepare_handle_incoming_blocks(std::__cxx11::list<cryptonote::block_complete_entry, std::allocator<cryptonote::block_complete_entry> > const&)':
blockchain.cpp:(.text+0x26bb5): undefined reference to `boost::this_thread::hidden::sleep_until(timespec const&)'
../cryptonote_core/libcryptonote_core.a(blockchain.cpp.o): In function `void boost::this_thread::sleep_for<long, boost::ratio<1l, 1000l> >(boost::chrono::duration<long, boost::ratio<1l, 1000l> > const&)':
blockchain.cpp:(.text._ZN5boost11this_thread9sleep_forIlNS_5ratioILl1ELl1000EEEEEvRKNS_6chrono8durationIT_T0_EE[_ZN5boost11this_thread9sleep_forIlNS_5ratioILl1ELl1000EEEEEvRKNS_6chrono8durationIT_T0_EE]+0x58): undefined reference to `boost::this_thread::hidden::sleep_for(timespec const&)'
../cryptonote_basic/libcryptonote_basic.a(hardfork.cpp.o): In function `cryptonote::HardFork::check(cryptonote::block const&) const':
hardfork.cpp:(.text+0xb9): undefined reference to `boost::this_thread::hidden::sleep_for(timespec const&)'
../cryptonote_basic/libcryptonote_basic.a(hardfork.cpp.o): In function `cryptonote::HardFork::get_state(long) const':
hardfork.cpp:(.text+0x4bb): undefined reference to `boost::this_thread::hidden::sleep_for(timespec const&)'
../cryptonote_basic/libcryptonote_basic.a(hardfork.cpp.o): In function `cryptonote::HardFork::get_state() const':
hardfork.cpp:(.text+0x5f2): undefined reference to `boost::this_thread::hidden::sleep_for(timespec const&)'
../cryptonote_basic/libcryptonote_basic.a(hardfork.cpp.o): In function `cryptonote::HardFork::get_current_version() const':
hardfork.cpp:(.text+0x720): undefined reference to `boost::this_thread::hidden::sleep_for(timespec const&)'
../cryptonote_basic/libcryptonote_basic.a(hardfork.cpp.o):hardfork.cpp:(.text+0x810): more undefined references to `boost::this_thread::hidden::sleep_for(timespec const&)' follow
../cryptonote_basic/libcryptonote_basic.a(miner.cpp.o): In function `cryptonote::miner::worker_thread()':
miner.cpp:(.text+0x706d): undefined reference to `boost::this_thread::hidden::sleep_until(timespec const&)'
miner.cpp:(.text+0x72e4): undefined reference to `boost::this_thread::hidden::sleep_until(timespec const&)'
miner.cpp:(.text+0x7af7): undefined reference to `boost::this_thread::hidden::sleep_until(timespec const&)'
../cryptonote_basic/libcryptonote_basic.a(miner.cpp.o): In function `void boost::this_thread::sleep_for<long, boost::ratio<1l, 1l> >(boost::chrono::duration<long, boost::ratio<1l, 1l> > const&)':
miner.cpp:(.text._ZN5boost11this_thread9sleep_forIlNS_5ratioILl1ELl1EEEEEvRKNS_6chrono8durationIT_T0_EE[_ZN5boost11this_thread9sleep_forIlNS_5ratioILl1ELl1EEEEEvRKNS_6chrono8durationIT_T0_EE]+0x50): undefined reference to `boost::this_thread::hidden::sleep_for(timespec const&)'
../common/libcommon.a(download.cpp.o): In function `boost::re_detail_106501::perl_matcher<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > >, boost::regex_traits<char, boost::cpp_regex_traits<char> > >::unwind_extra_block(bool)':
download.cpp:(.text._ZN5boost16re_detail_10650112perl_matcherIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEESaINS_9sub_matchISC_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE18unwind_extra_blockEb[_ZN5boost16re_detail_10650112perl_matcherIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEESaINS_9sub_matchISC_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE18unwind_extra_blockEb]+0x2c): undefined reference to `boost::re_detail_106501::put_mem_block(void*)'
../common/libcommon.a(download.cpp.o): In function `__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > boost::re_detail_106501::re_is_set_member<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, char, boost::regex_traits<char, boost::cpp_regex_traits<char> >, unsigned int>(__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, __gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, boost::re_detail_106501::re_set_long<unsigned int> const*, boost::re_detail_106501::regex_data<char, boost::regex_traits<char, boost::cpp_regex_traits<char> > > const&, bool)':
download.cpp:(.text._ZN5boost16re_detail_10650116re_is_set_memberIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEEcNS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEjEET_SH_SH_PKNS0_11re_set_longIT2_EERKNS0_10regex_dataIT0_T1_EEb[_ZN5boost16re_detail_10650116re_is_set_memberIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEEcNS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEjEET_SH_SH_PKNS0_11re_set_longIT2_EERKNS0_10regex_dataIT0_T1_EEb]+0x15e): undefined reference to `boost::re_detail_106501::cpp_regex_traits_implementation<char>::transform_primary(char const*, char const*) const'
download.cpp:(.text._ZN5boost16re_detail_10650116re_is_set_memberIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEEcNS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEjEET_SH_SH_PKNS0_11re_set_longIT2_EERKNS0_10regex_dataIT0_T1_EEb[_ZN5boost16re_detail_10650116re_is_set_memberIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEEcNS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEjEET_SH_SH_PKNS0_11re_set_longIT2_EERKNS0_10regex_dataIT0_T1_EEb]+0x349): undefined reference to `boost::re_detail_106501::cpp_regex_traits_implementation<char>::transform(char const*, char const*) const'
../common/libcommon.a(download.cpp.o): In function `void boost::re_detail_106501::raise_error<boost::regex_traits_wrapper<boost::regex_traits<char, boost::cpp_regex_traits<char> > > >(boost::regex_traits_wrapper<boost::regex_traits<char, boost::cpp_regex_traits<char> > > const&, boost::regex_constants::error_type)':
download.cpp:(.text._ZN5boost16re_detail_10650111raise_errorINS_20regex_traits_wrapperINS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEEEEEvRKT_NS_15regex_constants10error_typeE[_ZN5boost16re_detail_10650111raise_errorINS_20regex_traits_wrapperINS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEEEEEvRKT_NS_15regex_constants10error_typeE]+0xb2): undefined reference to `boost::re_detail_106501::raise_runtime_error(std::runtime_error const&)'
download.cpp:(.text._ZN5boost16re_detail_10650111raise_errorINS_20regex_traits_wrapperINS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEEEEEvRKT_NS_15regex_constants10error_typeE[_ZN5boost16re_detail_10650111raise_errorINS_20regex_traits_wrapperINS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEEEEEvRKT_NS_15regex_constants10error_typeE]+0xe0): undefined reference to `boost::re_detail_106501::get_default_error_string(boost::regex_constants::error_type)'
../common/libcommon.a(download.cpp.o): In function `boost::re_detail_106501::perl_matcher<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > >, boost::regex_traits<char, boost::cpp_regex_traits<char> > >::extend_stack()':
download.cpp:(.text._ZN5boost16re_detail_10650112perl_matcherIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEESaINS_9sub_matchISC_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE12extend_stackEv[_ZN5boost16re_detail_10650112perl_matcherIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEESaINS_9sub_matchISC_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE12extend_stackEv]+0x18): undefined reference to `boost::re_detail_106501::get_mem_block()'
../common/libcommon.a(download.cpp.o): In function `boost::re_detail_106501::perl_matcher<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > >, boost::regex_traits<char, boost::cpp_regex_traits<char> > >::find_imp()':
download.cpp:(.text._ZN5boost16re_detail_10650112perl_matcherIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEESaINS_9sub_matchISC_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE8find_impEv[_ZN5boost16re_detail_10650112perl_matcherIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEESaINS_9sub_matchISC_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE8find_impEv]+0xa): undefined reference to `boost::re_detail_106501::get_mem_block()'
download.cpp:(.text._ZN5boost16re_detail_10650112perl_matcherIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEESaINS_9sub_matchISC_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE8find_impEv[_ZN5boost16re_detail_10650112perl_matcherIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEESaINS_9sub_matchISC_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE8find_impEv]+0x138): undefined reference to `boost::re_detail_106501::verify_options(unsigned int, boost::regex_constants::_match_flags)'
download.cpp:(.text._ZN5boost16re_detail_10650112perl_matcherIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEESaINS_9sub_matchISC_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE8find_impEv[_ZN5boost16re_detail_10650112perl_matcherIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEESaINS_9sub_matchISC_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE8find_impEv]+0x17f): undefined reference to `boost::re_detail_106501::put_mem_block(void*)'
download.cpp:(.text._ZN5boost16re_detail_10650112perl_matcherIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEESaINS_9sub_matchISC_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE8find_impEv[_ZN5boost16re_detail_10650112perl_matcherIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEESaINS_9sub_matchISC_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE8find_impEv]+0x2d3): undefined reference to `boost::re_detail_106501::put_mem_block(void*)'
../common/libcommon.a(download.cpp.o): In function `bool boost::regex_search<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > >, char, boost::regex_traits<char, boost::cpp_regex_traits<char> > >(__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, __gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, boost::match_results<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > > >&, boost::basic_regex<char, boost::regex_traits<char, boost::cpp_regex_traits<char> > > const&, boost::regex_constants::_match_flags, __gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >)':
download.cpp:(.text._ZN5boost12regex_searchIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEESaINS_9sub_matchISB_EEEcNS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEEEbT_SJ_RNS_13match_resultsISJ_T0_EERKNS_11basic_regexIT1_T2_EENS_15regex_constants12_match_flagsESJ_[_ZN5boost12regex_searchIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEESaINS_9sub_matchISB_EEEcNS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEEEbT_SJ_RNS_13match_resultsISJ_T0_EERKNS_11basic_regexIT1_T2_EENS_15regex_constants12_match_flagsESJ_]+0x11b): undefined reference to `boost::re_detail_106501::perl_matcher<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > >, boost::regex_traits<char, boost::cpp_regex_traits<char> > >::construct_init(boost::basic_regex<char, boost::regex_traits<char, boost::cpp_regex_traits<char> > > const&, boost::regex_constants::_match_flags)'
../common/libcommon.a(download.cpp.o): In function `epee::net_utils::http::http_simple_client::parse_header(epee::net_utils::http::http_header_info&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&)':
download.cpp:(.text._ZN4epee9net_utils4http18http_simple_client12parse_headerERNS1_16http_header_infoERKNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEE[_ZN4epee9net_utils4http18http_simple_client12parse_headerERNS1_16http_header_infoERKNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEE]+0x323): undefined reference to `boost::re_detail_106501::perl_matcher<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > >, boost::regex_traits<char, boost::cpp_regex_traits<char> > >::construct_init(boost::basic_regex<char, boost::regex_traits<char, boost::cpp_regex_traits<char> > > const&, boost::regex_constants::_match_flags)'
collect2: error: ld returned 1 exit status
src/blockchain_utilities/CMakeFiles/blockchain_export.dir/build.make:178: recipe for target 'bin/monero-blockchain-export' failed
make[3]: *** [bin/monero-blockchain-export] Error 1
make[3]: Leaving directory '[path]/monero/build/release'
CMakeFiles/Makefile2:2442: recipe for target 'src/blockchain_utilities/CMakeFiles/blockchain_export.dir/all' failed
make[2]: *** [src/blockchain_utilities/CMakeFiles/blockchain_export.dir/all] Error 2
make[2]: *** Waiting for unfinished jobs....
```

## moneromooo-monero | 2017-12-15T13:08:07+00:00
monero builds fine here with boost 1.65 and openssl 1.1.0f, GCC 6.4.1 (though I doubt the GCC version would cause those type issues).

## moneromooo-monero | 2017-12-26T12:11:17+00:00
Does https://github.com/monero-project/monero/pull/3007 fix it ?

make clean first to  be sure.

## lacksfish | 2017-12-27T15:59:52+00:00
Builds just fine with #3007. Awesome! :)

## moneromooo-monero | 2017-12-27T16:22:24+00:00
Great, thanks :)

## serhack | 2017-12-27T17:04:08+00:00
Should I close? I can confirm building is okay with patch #3007.

## moneromooo-monero | 2017-12-27T18:35:21+00:00
When it's merged.

## moneromooo-monero | 2018-01-18T23:36:14+00:00
+resolved

# Action History
- Created by: serhack | 2017-11-13T20:30:21+00:00
- Closed at: 2018-01-19T00:00:32+00:00
