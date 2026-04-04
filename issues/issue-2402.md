---
title: CMake is not generating unbound/config.h correctly with openssl 1.1
source_url: https://github.com/monero-project/monero/issues/2402
author: danrmiller
assignees: []
labels: []
created_at: '2017-09-05T16:53:34+00:00'
updated_at: '2017-09-25T18:25:39+00:00'
type: issue
status: closed
closed_at: '2017-09-25T18:25:39+00:00'
---

# Original Description
This example uses debian stretch, aarch64, openssl 1.1.0f:

https://build.getmonero.org/builders/monero-static-debian-armv8/builds/1737/steps/compile/logs/stdio

/home/buildbot/slave/monero-static-debian-armv8/build/external/unbound/validator/val_secalgo.c:637:34: error: invalid application of 'sizeof' to an incomplete type 
                 'EVP_MD_CTX' (aka 'struct evp_md_ctx_st') ctx = (EVP_MD_CTX*)malloc(sizeof(*ctx));

On IRC hyc confirms the same issue for him with openssl 1.1

Manually editing unbound/config.h to #define HAVE_EVP_MD_CTX_NEW works.

This issue is to solicit help figuring out why configure_checks.cmake doesn't find EVP_MD_CTX_new


# Discussion History
## danrmiller | 2017-09-05T16:53:56+00:00
+help wanted

## anonimal | 2017-09-06T00:11:53+00:00
(for housekeeping, referencing https://github.com/monero-project/monero/pull/2133)

## hyc | 2017-09-06T13:34:05+00:00
On my build machine, this appears to be the result of a stale CMakeCache.txt. I.e., it was generated far back in the past, when the machine had OpenSSL 1.0 installed. Later I upgraded the OS, which brought in OpenSSL 1.1. The old value for HAVE_EVP_MD_CTX_NEW (empty, false) was in the CMakeCache.txt file so cmake didn't bother to run the check again. Deleting the cache file, or just deleting the line with HAVE_EVP_MD_CTX_NEW and rerunning cmake to regenerate the CMakeFiles worked.

## danrmiller | 2017-09-06T14:23:46+00:00
I removed ~/.cmake and cloned to a fresh directory.

When I run cmake -D BUILD_TESTS=OFF -D ARCH="armv8-a" -D STATIC=ON -D BUILD_64=ON -D CMAKE_BUILD_TYPE=release -D BUILD_TAG="linux-armv8" ../.. as in the "release-static-linux-armv8" Makefile target, EVP_MD_CTX_new is not found:

-- Looking for EVP_MD_CTX_new
-- Looking for EVP_MD_CTX_new - not found

If I just run cmake -D CMAKE_BUILD_TYPE=release ../.. then it is found:

-- Looking for EVP_MD_CTX_new
-- Looking for EVP_MD_CTX_new - found

## hyc | 2017-09-06T14:35:33+00:00
Perhaps you have no static libcrypto library?

## danrmiller | 2017-09-06T14:44:58+00:00
-- Found OpenSSL: /usr/lib/aarch64-linux-gnu/libssl.a;/usr/lib/aarch64-linux-gnu/libcrypto.a (found version "1.1.0f") 

Package: libssl-dev                      
Version: 1.1.0f-3
Maintainer: Debian OpenSSL Team <pkg-openssl-devel@lists.alioth.debian.org>


## hyc | 2017-09-06T14:53:53+00:00
CMakeFiles/CMakeOutput.log should have some info about the check, can you find anything in there for EVP_MD_CTX_new ?

## danrmiller | 2017-09-06T15:08:48+00:00
Determining if the function EVP_MD_CTX_new exists failed with the following output:
Change Dir: /home/buildbot/slave/monero-static-debian-armv8/build/build/release/CMakeFiles/CMakeTmp

Run Build Command:"/usr/bin/make" "cmTC_34550/fast"
/usr/bin/make -f CMakeFiles/cmTC_34550.dir/build.make CMakeFiles/cmTC_34550.dir/build
make[1]: Entering directory '/home/buildbot/slave/monero-static-debian-armv8/build/build/release/CMakeFiles/CMakeTmp'
Building C object CMakeFiles/cmTC_34550.dir/CheckFunctionExists.c.o
/usr/bin/cc    -DCHECK_FUNCTION_EXISTS=EVP_MD_CTX_new   -o CMakeFiles/cmTC_34550.dir/CheckFunctionExists.c.o   -c /usr/share/cmake-3.7/Modules/CheckFunctionExists.c
Linking C executable cmTC_34550
/usr/bin/cmake -E cmake_link_script CMakeFiles/cmTC_34550.dir/link.txt --verbose=1
/usr/bin/cc   -DCHECK_FUNCTION_EXISTS=EVP_MD_CTX_new    CMakeFiles/cmTC_34550.dir/CheckFunctionExists.c.o  -o cmTC_34550 -rdynamic /usr/lib/aarch64-linux-gnu/libssl.a /usr/lib/aarch64-linux-gnu/libcrypto.a -ldl 
/usr/lib/aarch64-linux-gnu/libcrypto.a(threads_pthread.o): In function `CRYPTO_THREAD_lock_new':
(.text+0x30): undefined reference to `pthread_rwlock_init'
/usr/lib/aarch64-linux-gnu/libcrypto.a(threads_pthread.o): In function `CRYPTO_THREAD_read_lock':
(.text+0x68): undefined reference to `pthread_rwlock_rdlock'
/usr/lib/aarch64-linux-gnu/libcrypto.a(threads_pthread.o): In function `CRYPTO_THREAD_write_lock':
(.text+0x88): undefined reference to `pthread_rwlock_wrlock'
/usr/lib/aarch64-linux-gnu/libcrypto.a(threads_pthread.o): In function `CRYPTO_THREAD_unlock':
(.text+0xa8): undefined reference to `pthread_rwlock_unlock'
/usr/lib/aarch64-linux-gnu/libcrypto.a(threads_pthread.o): In function `CRYPTO_THREAD_lock_free':
(.text+0xd4): undefined reference to `pthread_rwlock_destroy'
/usr/lib/aarch64-linux-gnu/libcrypto.a(threads_pthread.o): In function `CRYPTO_THREAD_run_once':
(.text+0x108): undefined reference to `pthread_once'
/usr/lib/aarch64-linux-gnu/libcrypto.a(threads_pthread.o): In function `CRYPTO_THREAD_init_local':
(.text+0x128): undefined reference to `pthread_key_create'
/usr/lib/aarch64-linux-gnu/libcrypto.a(threads_pthread.o): In function `CRYPTO_THREAD_get_local':
(.text+0x144): undefined reference to `pthread_getspecific'
/usr/lib/aarch64-linux-gnu/libcrypto.a(threads_pthread.o): In function `CRYPTO_THREAD_set_local':
(.text+0x154): undefined reference to `pthread_setspecific'
/usr/lib/aarch64-linux-gnu/libcrypto.a(threads_pthread.o): In function `CRYPTO_THREAD_cleanup_local':
(.text+0x174): undefined reference to `pthread_key_delete'
collect2: error: ld returned 1 exit status
CMakeFiles/cmTC_34550.dir/build.make:99: recipe for target 'cmTC_34550' failed
make[1]: *** [cmTC_34550] Error 1
make[1]: Leaving directory '/home/buildbot/slave/monero-static-debian-armv8/build/build/release/CMakeFiles/CMakeTmp'
Makefile:126: recipe for target 'cmTC_34550/fast' failed
make: *** [cmTC_34550/fast] Error 2


## hyc | 2017-09-06T15:49:19+00:00
OK, that explains it. They now have a dependency on libpthread. Linking a shared library pulls in the dependency automatically, but using a static library doesn't. But in the meantime, all the other OpenSSL function checks should be failing this same way. Are they?

## danrmiller | 2017-09-06T16:57:09+00:00
Yes the other OpenSSL function checks like EVP_sha* fail with undefined references to pthread also.

https://pastebin.mozilla.org/9031624

## hyc | 2017-09-06T17:50:01+00:00
I would have expected pkg-config to have included -lpthread in the libssl/libcrypto dependencies. You may just have to edit the CMakeLists.txt file to add this. Not sure how to do this portably though.


## ViperRu | 2017-09-16T20:32:30+00:00
Hello,
after git clone, I have the same problem in is ubuntu-14.04 LTS AMD64.

## danrmiller | 2017-09-16T20:39:24+00:00
What version of openssl? I would have expected ubuntu-14.04 to use openssl 1.0. For now I have avoided the issue by using openssl 1.0 instead of 1.1

## ViperRu | 2017-09-16T20:55:59+00:00
`~ > dpkg -l | grep libssl

ii  libssl-dev:amd64                            1.1.0f-2~ubuntu14.04.1+deb.sury.org+1             amd64       Secure Sockets Layer toolkit - development files

ii  libssl0.9.8:i386                            0.9.8o-7ubuntu3.2.14.04.1                         i386         SSL shared libraries

ii  libssl1.0.0:amd64                           1.0.2k-1+deb.sury.org~trusty+1                    amd64        Secure Sockets Layer toolkit - shared libraries

ii  libssl1.0.0:i386                            1.0.2k-1+deb.sury.org~trusty+1                    i386         Secure Sockets Layer toolkit - shared libraries

rc  libssl1.0.2:amd64                           1.0.2l-0~ubuntu14.04.1+deb.sury.org+1             amd64        Secure Sockets Layer toolkit - shared libraries

ii  libssl1.1:amd64                             1.1.0f-2~ubuntu14.04.1+deb.sury.org+1             amd64        Secure Sockets Layer toolkit - shared libraries`

## hyc | 2017-09-16T21:10:02+00:00
What's in your `/usr/lib/x86_64-linux-gnu/pkgconfig/libcrypto.pc` ?

## hyc | 2017-09-16T21:11:59+00:00
On arch mine has
````
prefix=/usr
exec_prefix=${prefix}
libdir=${exec_prefix}/lib
includedir=${prefix}/include
enginesdir=${libdir}/engines-1.1

Name: OpenSSL-libcrypto
Description: OpenSSL cryptography library
Version: 1.1.0f
Libs: -L${libdir} -lcrypto
Libs.private: -ldl
Cflags: -I${includedir}
````
Which is an obvious packaging bug. They should have added -lpthread to Libs.private. If you add it there yourself, you should be able to get past this problem.

## ViperRu | 2017-09-16T21:12:39+00:00
~ > cat /usr/lib/x86_64-linux-gnu/pkgconfig/libcrypto.pc
prefix=/usr
exec_prefix=${prefix}
libdir=${exec_prefix}/lib/x86_64-linux-gnu
includedir=${prefix}/include
enginesdir=${libdir}/engines-1.1

Name: OpenSSL-libcrypto
Description: OpenSSL cryptography library
Version: 1.1.0f
Libs: -L${libdir} -lcrypto
Libs.private: -ldl 
Cflags: -I${includedir}


## hyc | 2017-09-16T21:13:18+00:00
Edit the file, add `-lpthread` to the end of the Libs.private: line - that should take care of this.

## ViperRu | 2017-09-16T21:20:51+00:00
Thank you, but I alreade builded src before posting about problem this way:
$ cd external/unbound/
$ cmake
add by manual #define HAVE_EVP_MD_CTX_NEW in unbound/config.h
$ make
$ cd ../..
$ make

# Action History
- Created by: danrmiller | 2017-09-05T16:53:34+00:00
- Closed at: 2017-09-25T18:25:39+00:00
