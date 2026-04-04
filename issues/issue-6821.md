---
title: how to solve building errors
source_url: https://github.com/monero-project/monero/issues/6821
author: ghost
assignees: []
labels: []
created_at: '2020-09-16T11:03:51+00:00'
updated_at: '2020-09-20T03:24:46+00:00'
type: issue
status: closed
closed_at: '2020-09-20T03:24:46+00:00'
---

# Original Description
Debin10 building errors:  make -j14 release-static
 
[ 98%] Linking CXX executable ../../bin/monerod
/usr/bin/ld: /usr/lib/gcc/x86_64-linux-gnu/8/../../../x86_64-linux-gnu/libzmq.a(libzmq_la-gssapi_client.o): in function `zmq::gssapi_client_t::~gssapi_client_t()':
(.text+0x59): undefined reference to `gss_release_cred'
/usr/bin/ld: /usr/lib/gcc/x86_64-linux-gnu/8/../../../x86_64-linux-gnu/libzmq.a(libzmq_la-gssapi_client.o): in function `zmq::gssapi_client_t::process_next_token(zmq::msg_t*) [clone .part.9]':
(.text+0x246): undefined reference to `gss_release_name'
/usr/bin/ld: /usr/lib/gcc/x86_64-linux-gnu/8/../../../x86_64-linux-gnu/libzmq.a(libzmq_la-gssapi_client.o): in function `zmq::gssapi_client_t::~gssapi_client_t()':
(.text+0x84c): undefined reference to `gss_release_cred'
/usr/bin/ld: /usr/lib/gcc/x86_64-linux-gnu/8/../../../x86_64-linux-gnu/libzmq.a(libzmq_la-gssapi_client.o): in function `zmq::gssapi_client_t::initialize_context()':
(.text+0x8ca): undefined reference to `gss_init_sec_context'
/usr/bin/ld: (.text+0x91d): undefined reference to `gss_import_name'
/usr/bin/ld: /usr/lib/gcc/x86_64-linux-gnu/8/../../../x86_64-linux-gnu/libzmq.a(libzmq_la-gssapi_client.o): in function `zmq::gssapi_client_t::produce_next_token(zmq::msg_t*)':
(.text+0x96c): undefined reference to `gss_release_buffer'
/usr/bin/ld: (.text+0x98e): undefined reference to `gss_release_buffer'
/usr/bin/ld: (.text+0x99a): undefined reference to `gss_release_name'
/usr/bin/ld: (.text+0x9ae): undefined reference to `gss_release_name'
/usr/bin/ld: (.text+0x9c3): undefined reference to `gss_delete_sec_context'
/usr/bin/ld: /usr/lib/gcc/x86_64-linux-gnu/8/../../../x86_64-linux-gnu/libzmq.a(libzmq_la-gssapi_server.o): in function `zmq::gssapi_server_t::~gssapi_server_t()':
(.text+0x208): undefined reference to `gss_release_cred'
/usr/bin/ld: (.text+0x21c): undefined reference to `gss_release_name'
/usr/bin/ld: /usr/lib/gcc/x86_64-linux-gnu/8/../../../x86_64-linux-gnu/libzmq.a(libzmq_la-gssapi_server.o): in function `zmq::gssapi_server_t::~gssapi_server_t()':
(.text+0x346): undefined reference to `gss_release_cred'
/usr/bin/ld: (.text+0x35a): undefined reference to `gss_release_name'
/usr/bin/ld: /usr/lib/gcc/x86_64-linux-gnu/8/../../../x86_64-linux-gnu/libzmq.a(libzmq_la-gssapi_server.o): in function `zmq::gssapi_server_t::send_zap_request()':
(.text+0x3ff): undefined reference to `gss_display_name'
/usr/bin/ld: (.text+0x428): undefined reference to `gss_release_buffer'
/usr/bin/ld: /usr/lib/gcc/x86_64-linux-gnu/8/../../../x86_64-linux-gnu/libzmq.a(libzmq_la-gssapi_server.o): in function `zmq::gssapi_server_t::produce_next_token(zmq::msg_t*)':
(.text+0x48e): undefined reference to `gss_release_buffer'
/usr/bin/ld: (.text+0x4a0): undefined reference to `gss_release_name'
/usr/bin/ld: (.text+0x4b5): undefined reference to `gss_delete_sec_context'
/usr/bin/ld: /usr/lib/gcc/x86_64-linux-gnu/8/../../../x86_64-linux-gnu/libzmq.a(libzmq_la-gssapi_server.o): in function `zmq::gssapi_server_t::process_next_token(zmq::msg_t*)':
(.text+0x599): undefined reference to `gss_release_name'
/usr/bin/ld: /usr/lib/gcc/x86_64-linux-gnu/8/../../../x86_64-linux-gnu/libzmq.a(libzmq_la-gssapi_server.o): in function `zmq::gssapi_server_t::accept_context()':
(.text+0x5d6): undefined reference to `gss_accept_sec_context'
/usr/bin/ld: /usr/lib/gcc/x86_64-linux-gnu/8/../../../x86_64-linux-gnu/libzmq.a(libzmq_la-gssapi_mechanism_base.o): in function `zmq::gssapi_mechanism_base_t::~gssapi_mechanism_base_t()':
(.text+0x126): undefined reference to `gss_release_name'
/usr/bin/ld: /usr/lib/gcc/x86_64-linux-gnu/8/../../../x86_64-linux-gnu/libzmq.a(libzmq_la-gssapi_mechanism_base.o): in function `zmq::gssapi_mechanism_base_t::~gssapi_mechanism_base_t()':
(.text+0x176): undefined reference to `gss_release_name'
/usr/bin/ld: /usr/lib/gcc/x86_64-linux-gnu/8/../../../x86_64-linux-gnu/libzmq.a(libzmq_la-gssapi_mechanism_base.o): in function `zmq::gssapi_mechanism_base_t::encode_message(zmq::msg_t*)':
(.text+0x281): undefined reference to `gss_wrap'
/usr/bin/ld: (.text+0x300): undefined reference to `gss_release_buffer'
/usr/bin/ld: /usr/lib/gcc/x86_64-linux-gnu/8/../../../x86_64-linux-gnu/libzmq.a(libzmq_la-gssapi_mechanism_base.o): in function `zmq::gssapi_mechanism_base_t::decode_message(zmq::msg_t*)':
(.text+0x590): undefined reference to `gss_unwrap'
/usr/bin/ld: (.text+0x626): undefined reference to `gss_release_buffer'
/usr/bin/ld: (.text+0xa3e): undefined reference to `gss_release_buffer'
/usr/bin/ld: /usr/lib/gcc/x86_64-linux-gnu/8/../../../x86_64-linux-gnu/libzmq.a(libzmq_la-gssapi_mechanism_base.o): in function `zmq::gssapi_mechanism_base_t::convert_nametype(int)':
(.text+0x1742): undefined reference to `GSS_C_NT_USER_NAME'
/usr/bin/ld: (.text+0x1753): undefined reference to `GSS_C_NT_HOSTBASED_SERVICE'
/usr/bin/ld: /usr/lib/gcc/x86_64-linux-gnu/8/../../../x86_64-linux-gnu/libzmq.a(libzmq_la-gssapi_mechanism_base.o): in function `zmq::gssapi_mechanism_base_t::acquire_credentials(char*, gss_cred_id_struct**, gss_OID_desc_struct*)':
(.text+0x17bc): undefined reference to `gss_import_name'
/usr/bin/ld: (.text+0x17db): undefined reference to `gss_acquire_cred'
/usr/bin/ld: (.text+0x17ec): undefined reference to `gss_release_name'
/usr/bin/ld: /usr/lib/gcc/x86_64-linux-gnu/8/../../../x86_64-linux-gnu/libzmq.a(libzmq_la-gssapi_mechanism_base.o): in function `zmq::gssapi_mechanism_base_t::~gssapi_mechanism_base_t()':
(.text+0x13d): undefined reference to `gss_delete_sec_context'
/usr/bin/ld: /usr/lib/gcc/x86_64-linux-gnu/8/../../../x86_64-linux-gnu/libzmq.a(libzmq_la-gssapi_mechanism_base.o): in function `zmq::gssapi_mechanism_base_t::~gssapi_mechanism_base_t()':
(.text+0x18d): undefined reference to `gss_delete_sec_context'
collect2: error: ld returned 1 exit status


# Discussion History
## moneromooo-monero | 2020-09-16T23:11:34+00:00
Your libzmq seems to need libgssapi.
Try this:

```
diff --git a/CMakeLists.txt b/CMakeLists.txt
index 2a16e0081..e688f7c1a 100644
--- a/CMakeLists.txt
+++ b/CMakeLists.txt
@@ -969,6 +969,7 @@ find_path(ZMQ_INCLUDE_PATH zmq.h)
 find_library(ZMQ_LIB zmq)
 find_library(PGM_LIBRARY pgm)
 find_library(NORM_LIBRARY norm)
+find_library(GSSAPI_LIBRARY libgssapi_krb5)
 find_library(PROTOLIB_LIBRARY protolib)
 find_library(SODIUM_LIBRARY sodium)
 
@@ -984,6 +985,9 @@ endif()
 if(NORM_LIBRARY)
   set(ZMQ_LIB "${ZMQ_LIB};${NORM_LIBRARY}")
 endif()
+if(GSSAPI_LIBRARY)
+  set(ZMQ_LIB "${ZMQ_LIB};${GSSAPI_LIBRARY}")
+endif()
 if(PROTOLIB_LIBRARY)
   set(ZMQ_LIB "${ZMQ_LIB};${PROTOLIB_LIBRARY}")
 endif()
```


## moneromooo-monero | 2020-09-16T23:12:12+00:00
patch -p1
Then paste the above patch
Then ^D
Then make again

## ghost | 2020-09-17T01:50:22+00:00
```
cd monero 
git diff CMakeLists.txt
diff --git a/CMakeLists.txt b/CMakeLists.txt
index 2a16e0081..e688f7c1a 100644
--- a/CMakeLists.txt
+++ b/CMakeLists.txt
@@ -969,6 +969,7 @@ find_path(ZMQ_INCLUDE_PATH zmq.h)
 find_library(ZMQ_LIB zmq)
 find_library(PGM_LIBRARY pgm)
 find_library(NORM_LIBRARY norm)
+find_library(GSSAPI_LIBRARY libgssapi_krb5)
 find_library(PROTOLIB_LIBRARY protolib)
 find_library(SODIUM_LIBRARY sodium)
 
@@ -984,6 +985,9 @@ endif()
 if(NORM_LIBRARY)
   set(ZMQ_LIB "${ZMQ_LIB};${NORM_LIBRARY}")
 endif()
+if(GSSAPI_LIBRARY)
+  set(ZMQ_LIB "${ZMQ_LIB};${GSSAPI_LIBRARY}")
+endif()
 if(PROTOLIB_LIBRARY)
  set(ZMQ_LIB "${ZMQ_LIB};${PROTOLIB_LIBRARY}")
 endif()
```
done, but still get the same error?



## moneromooo-monero | 2020-09-17T12:37:39+00:00
Do you have files named libgssapi\* in /usr somewhere ?

## ghost | 2020-09-17T13:05:09+00:00
> Do you have files named libgssapi* in /usr somewhere ?

No that file or folder in /usr/

## moneromooo-monero | 2020-09-17T13:22:58+00:00
Including in subdirectories ? I'd expect /usr/lib or /usr/lib64 or somesuch.

## ghost | 2020-09-17T13:26:59+00:00
> Including in subdirectories ? I'd expect /usr/lib or /usr/lib64 or somesuch.

i use "find libgssapi"  command，No results.


## moneromooo-monero | 2020-09-17T13:35:11+00:00
That will only find a file by that name. Try:

> find /usr -name libgssapi\\\*

## ghost | 2020-09-17T13:37:01+00:00
> That will only find a file by that name. Try:
> 
> > find /usr -name libgssapi\*

/usr/lib/x86_64-linux-gnu/samba/libgssapi-samba4.so.2.0.0
/usr/lib/x86_64-linux-gnu/samba/libgssapi-samba4.so.2
/usr/lib/x86_64-linux-gnu/libgssapi_krb5.so
/usr/lib/x86_64-linux-gnu/mit-krb5/libgssapi_krb5.so
/usr/lib/x86_64-linux-gnu/libgssapi_krb5.so.2
/usr/lib/x86_64-linux-gnu/libgssapi_krb5.so.2.2
/usr/share/doc/libgssapi-krb5-2
/usr/share/lintian/overrides/libgssapi-krb5-2


## moneromooo-monero | 2020-09-17T13:38:40+00:00
grep GSSAPI build/...../release/CMakeCache.txt

(replacing the .... with what matches your system, probably Linux/master)


## ghost | 2020-09-17T13:58:55+00:00
```
~/monero/build/Linux/master/release$
 grep GSSAPI CMakeCache.txt
GSSAPI_LIBRARY:FILEPATH=GSSAPI_LIBRARY-NOTFOUND
```


## moneromooo-monero | 2020-09-17T14:16:53+00:00
Oh, my bad. Replace
> find_library(GSSAPI_LIBRARY libgssapi_krb5)
with:
> find_library(GSSAPI_LIBRARY gssapi_krb5)


## ghost | 2020-09-17T14:25:40+00:00
Success !  really thank you! 

## moneromooo-monero | 2020-09-17T14:53:00+00:00
np, now in https://github.com/monero-project/monero/pull/6824

# Action History
- Created by: ghost | 2020-09-16T11:03:51+00:00
- Closed at: 2020-09-20T03:24:46+00:00
