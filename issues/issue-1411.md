---
title: Compilation error with openssl 1.1
source_url: https://github.com/monero-project/monero/issues/1411
author: diederikdehaas
assignees: []
labels: []
created_at: '2016-12-06T14:57:43+00:00'
updated_at: '2017-08-07T18:30:20+00:00'
type: issue
status: closed
closed_at: '2017-08-07T18:30:20+00:00'
---

# Original Description
Debian Sid has openssl 1.1 as default openssl version, but current master (https://github.com/monero-project/monero/commit/45bb39357716b58b9d71a95de900b7446950a396) fails to compile with it (`libssl-dev` version 1.1.0c-2). If you install `libssl1.0-dev`, which removes `libssl-dev`, the compilation does succeed.
It is (very?) likely that Debian Stretch will ship with both openssl 1.0 and 1.1 with the latter being the default.

Full build log of failure (on my Debian Sid amd64 system):
```
diederik@bagend:~/dev/crypto/monero-project/monero$ make
mkdir -p build/release
cd build/release && cmake -D BUILD_TESTS=ON -D CMAKE_BUILD_TYPE=release ../.. && make
-- The C compiler identification is GNU 6.2.1
-- The CXX compiler identification is GNU 6.2.1
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
-- Could not find DEVELOPER_LOCAL_TOOLS in env (not required)
-- BOOST_IGNORE_SYSTEM_PATHS defaults to OFF
-- Could not find DEVELOPER_LIBUNBOUND_OLD in env (not required)
-- Building for a 64-bit system
-- Building internal libraries as static
-- Could not find DATABASE in env (not required unless you want to change database type from default: lmdb)
-- Using LMDB as default DB type
-- Could not find libunwind (missing:  LIBUNWIND_INCLUDE_DIR LIBUNWIND_LIBRARIES) 
-- Stack trace on exception disabled
-- Looking for pthread.h
-- Looking for pthread.h - found
-- Looking for pthread_create
-- Looking for pthread_create - not found
-- Check if compiler accepts -pthread
-- Check if compiler accepts -pthread - yes
-- Found Threads: TRUE  
-- Could not find miniupnp
-- Using miniupnpc from local source tree (/external/miniupnpc)
-- Looking for libunbound
-- Found OpenSSL: /usr/lib/x86_64-linux-gnu/libssl.so;/usr/lib/x86_64-linux-gnu/libcrypto.so (found version "1.1.0c") 
-- Looking for arpa/inet.h
-- Looking for arpa/inet.h - found
-- Looking for endian.h
-- Looking for endian.h - found
-- Looking for dlfcn.h
-- Looking for dlfcn.h - found
-- Looking for event.h
-- Looking for event.h - not found
-- Looking for getopt.h
-- Looking for getopt.h - found
-- Looking for glob.h
-- Looking for glob.h - found
-- Looking for grp.h
-- Looking for grp.h - found
-- Looking for inttypes.h
-- Looking for inttypes.h - found
-- Looking for iphlpapi.h
-- Looking for iphlpapi.h - not found
-- Looking for login_cap.h
-- Looking for login_cap.h - not found
-- Looking for memory.h
-- Looking for memory.h - found
-- Looking for netdb.h
-- Looking for netdb.h - found
-- Looking for netinet/in.h
-- Looking for netinet/in.h - found
-- Looking for pwd.h
-- Looking for pwd.h - found
-- Looking for stdarg.h
-- Looking for stdarg.h - found
-- Looking for stdbool.h
-- Looking for stdbool.h - found
-- Looking for stdint.h
-- Looking for stdint.h - found
-- Looking for stdlib.h
-- Looking for stdlib.h - found
-- Looking for strings.h
-- Looking for strings.h - found
-- Looking for string.h
-- Looking for string.h - found
-- Looking for sys/param.h
-- Looking for sys/param.h - found
-- Looking for sys/resource.h
-- Looking for sys/resource.h - found
-- Looking for sys/sha2.h
-- Looking for sys/sha2.h - not found
-- Looking for sys/socket.h
-- Looking for sys/socket.h - found
-- Looking for sys/stat.h
-- Looking for sys/stat.h - found
-- Looking for sys/sysctl.h
-- Looking for sys/sysctl.h - found
-- Looking for sys/types.h
-- Looking for sys/types.h - found
-- Looking for sys/uio.h
-- Looking for sys/uio.h - found
-- Looking for sys/un.h
-- Looking for sys/un.h - found
-- Looking for sys/wait.h
-- Looking for sys/wait.h - found
-- Looking for syslog.h
-- Looking for syslog.h - found
-- Looking for time.h
-- Looking for time.h - found
-- Looking for unistd.h
-- Looking for unistd.h - found
-- Looking for vfork.h
-- Looking for vfork.h - not found
-- Looking for windows.h
-- Looking for windows.h - not found
-- Looking for winsock2.h
-- Looking for winsock2.h - not found
-- Looking for ws2tcpip.h
-- Looking for ws2tcpip.h - not found
-- Looking for _beginthreadex
-- Looking for _beginthreadex - not found
-- Looking for arc4random
-- Looking for arc4random - not found
-- Looking for arc4random_uniform
-- Looking for arc4random_uniform - not found
-- Looking for chown
-- Looking for chown - found
-- Looking for chroot
-- Looking for chroot - found
-- Looking for ctime_r
-- Looking for ctime_r - found
-- Looking for daemon
-- Looking for daemon - found
-- Looking for endprotoent
-- Looking for endprotoent - found
-- Looking for endservent
-- Looking for endservent - found
-- Looking for fork
-- Looking for fork - found
-- Looking for fseeko
-- Looking for fseeko - found
-- Looking for fsync
-- Looking for fsync - found
-- Looking for getauxval
-- Looking for getauxval - found
-- Looking for getentropy
-- Looking for getentropy - not found
-- Looking for getpwnam
-- Looking for getpwnam - found
-- Looking for getrlimit
-- Looking for getrlimit - found
-- Looking for glob
-- Looking for glob - found
-- Looking for gmtime_r
-- Looking for gmtime_r - found
-- Looking for fcntl
-- Looking for fcntl - found
-- Looking for inet_aton
-- Looking for inet_aton - found
-- Looking for inet_ntop
-- Looking for inet_ntop - found
-- Looking for inet_pton
-- Looking for inet_pton - found
-- Looking for initgroups
-- Looking for initgroups - found
-- Looking for ioctlsocket
-- Looking for ioctlsocket - not found
-- Looking for isblank
-- Looking for isblank - found
-- Looking for kill
-- Looking for kill - found
-- Looking for localtime_r
-- Looking for localtime_r - found
-- Looking for malloc
-- Looking for malloc - found
-- Looking for memmove
-- Looking for memmove - found
-- Looking for random
-- Looking for random - found
-- Looking for reallocarray
-- Looking for reallocarray - not found
-- Looking for recvmsg
-- Looking for recvmsg - found
-- Looking for sbrk
-- Looking for sbrk - found
-- Looking for sendmsg
-- Looking for sendmsg - found
-- Looking for setregid
-- Looking for setregid - found
-- Looking for setresgid
-- Looking for setresgid - found
-- Looking for setresuid
-- Looking for setresuid - found
-- Looking for setreuid
-- Looking for setreuid - found
-- Looking for setrlimit
-- Looking for setrlimit - found
-- Looking for setsid
-- Looking for setsid - found
-- Looking for setusercontent
-- Looking for setusercontent - not found
-- Looking for sigprocmask
-- Looking for sigprocmask - found
-- Looking for sleep
-- Looking for sleep - found
-- Looking for snprintf
-- Looking for snprintf - found
-- Looking for socketpair
-- Looking for socketpair - found
-- Looking for srandom
-- Looking for srandom - found
-- Looking for strftime
-- Looking for strftime - found
-- Looking for strlcat
-- Looking for strlcat - not found
-- Looking for strlcpy
-- Looking for strlcpy - not found
-- Looking for strptime
-- Looking for strptime - found
-- Looking for tzset
-- Looking for tzset - found
-- Looking for usleep
-- Looking for usleep - found
-- Looking for writev
-- Looking for writev - found
-- Looking for getaddrinfo
-- Looking for getaddrinfo - found
-- Looking for stddef.h
-- Looking for stddef.h - found
-- Check size of time_t
-- Check size of time_t - done
-- Check size of gid_t
-- Check size of gid_t - done
-- Check size of in_addr_t
-- Check size of in_addr_t - done
-- Check size of in_port_t
-- Check size of in_port_t - done
-- Check size of int16_t
-- Check size of int16_t - done
-- Check size of int32_t
-- Check size of int32_t - done
-- Check size of int64_t
-- Check size of int64_t - done
-- Check size of int8_t
-- Check size of int8_t - done
-- Check size of pid_t
-- Check size of pid_t - done
-- Check size of rlim_t
-- Check size of rlim_t - done
-- Check size of ssize_t
-- Check size of ssize_t - done
-- Check size of uid_t
-- Check size of uid_t - done
-- Check size of uint16_t
-- Check size of uint16_t - done
-- Check size of uint32_t
-- Check size of uint32_t - done
-- Check size of uint64_t
-- Check size of uint64_t - done
-- Check size of uint8_t
-- Check size of uint8_t - done
-- Looking for PTHREAD_PRIO_INHERIT
-- Looking for PTHREAD_PRIO_INHERIT - not found
-- Looking for pthread_rwlock_t
-- Looking for pthread_rwlock_t - not found
-- Looking for pthread_spinlock_t
-- Looking for pthread_spinlock_t - not found
-- Looking for openssl/conf.h
-- Looking for openssl/conf.h - found
-- Looking for openssl/engine.h
-- Looking for openssl/engine.h - found
-- Looking for openssl/err.h
-- Looking for openssl/err.h - found
-- Looking for openssl/rand.h
-- Looking for openssl/rand.h - found
-- Looking for openssl/ssl.h
-- Looking for openssl/ssl.h - found
-- Looking for NID_secp384r1
-- Looking for NID_secp384r1 - found
-- Looking for NID_X9_62_prime256v1
-- Looking for NID_X9_62_prime256v1 - found
-- Looking for sk_SSL_COMP_pop_free
-- Looking for sk_SSL_COMP_pop_free - not found
-- Looking for SSL_COMP_get_compression_methods
-- Looking for SSL_COMP_get_compression_methods - not found
-- Looking for EVP_sha1
-- Looking for EVP_sha1 - found
-- Looking for EVP_sha256
-- Looking for EVP_sha256 - found
-- Looking for EVP_sha512
-- Looking for EVP_sha512 - found
-- Looking for FIPS_mode
-- Looking for FIPS_mode - found
-- Looking for HMAC_CTX_init
-- Looking for HMAC_CTX_init - not found
-- Looking for OPENSSL_config
-- Looking for OPENSSL_config - found
-- Looking for SHA512_Update
-- Looking for SHA512_Update - found
-- Found PkgConfig: /usr/bin/pkg-config (found version "0.29") 
-- Using 64-bit LMDB from source tree
-- Building on x86_64 for native
-- AES support enabled
-- Found Boost Version: 106200
-- Found Git: /usr/bin/git
-- Could NOT find GTest (missing:  GTEST_LIBRARY GTEST_INCLUDE_DIR GTEST_MAIN_LIBRARY) 
-- GTest not found on the system: will use GTest bundled with this source
-- Found PythonInterp: /usr/bin/python (found version "2.7.13") 
Doxygen: graphviz not found - graphs disabled
-- Could NOT find Doxygen (missing:  DOXYGEN_EXECUTABLE) 
-- Configuring done
-- Generating done
-- Build files have been written to: /home/diederik/dev/crypto/monero-project/monero/build/release
make[1]: Entering directory '/home/diederik/dev/crypto/monero-project/monero/build/release'
make[2]: Entering directory '/home/diederik/dev/crypto/monero-project/monero/build/release'
make[3]: Entering directory '/home/diederik/dev/crypto/monero-project/monero/build/release'
Scanning dependencies of target version
make[3]: Leaving directory '/home/diederik/dev/crypto/monero-project/monero/build/release'
make[3]: Entering directory '/home/diederik/dev/crypto/monero-project/monero/build/release'
[  0%] Generating version/version.h
-- You are currently on commit 45bb3935
-- The most recent tag was at 53e18caf
-- You are ahead of or behind a tagged release
make[3]: Leaving directory '/home/diederik/dev/crypto/monero-project/monero/build/release'
[  0%] Built target version
make[3]: Entering directory '/home/diederik/dev/crypto/monero-project/monero/build/release'
Scanning dependencies of target libminiupnpc-static
make[3]: Leaving directory '/home/diederik/dev/crypto/monero-project/monero/build/release'
make[3]: Entering directory '/home/diederik/dev/crypto/monero-project/monero/build/release'
[  1%] Building C object external/miniupnpc/CMakeFiles/libminiupnpc-static.dir/igd_desc_parse.c.o
[  1%] Building C object external/miniupnpc/CMakeFiles/libminiupnpc-static.dir/miniupnpc.c.o
[  2%] Building C object external/miniupnpc/CMakeFiles/libminiupnpc-static.dir/minixml.c.o
[  2%] Building C object external/miniupnpc/CMakeFiles/libminiupnpc-static.dir/minisoap.c.o
[  2%] Building C object external/miniupnpc/CMakeFiles/libminiupnpc-static.dir/minissdpc.c.o
[  3%] Building C object external/miniupnpc/CMakeFiles/libminiupnpc-static.dir/miniwget.c.o
[  3%] Building C object external/miniupnpc/CMakeFiles/libminiupnpc-static.dir/upnpcommands.c.o
[  3%] Building C object external/miniupnpc/CMakeFiles/libminiupnpc-static.dir/upnpdev.c.o
[  4%] Building C object external/miniupnpc/CMakeFiles/libminiupnpc-static.dir/upnpreplyparse.c.o
[  4%] Building C object external/miniupnpc/CMakeFiles/libminiupnpc-static.dir/upnperrors.c.o
[  4%] Building C object external/miniupnpc/CMakeFiles/libminiupnpc-static.dir/connecthostport.c.o
[  5%] Building C object external/miniupnpc/CMakeFiles/libminiupnpc-static.dir/portlistingparse.c.o
[  5%] Building C object external/miniupnpc/CMakeFiles/libminiupnpc-static.dir/receivedata.c.o
[  5%] Linking C static library libminiupnpc.a
make[3]: Leaving directory '/home/diederik/dev/crypto/monero-project/monero/build/release'
[  5%] Built target libminiupnpc-static
make[3]: Entering directory '/home/diederik/dev/crypto/monero-project/monero/build/release'
Scanning dependencies of target unbound
make[3]: Leaving directory '/home/diederik/dev/crypto/monero-project/monero/build/release'
make[3]: Entering directory '/home/diederik/dev/crypto/monero-project/monero/build/release'
[  5%] Building C object external/unbound/CMakeFiles/unbound.dir/services/cache/dns.c.o
[  5%] Building C object external/unbound/CMakeFiles/unbound.dir/services/cache/infra.c.o
[  6%] Building C object external/unbound/CMakeFiles/unbound.dir/services/cache/rrset.c.o
[  6%] Building C object external/unbound/CMakeFiles/unbound.dir/util/data/dname.c.o
[  6%] Building C object external/unbound/CMakeFiles/unbound.dir/util/data/msgencode.c.o
[  7%] Building C object external/unbound/CMakeFiles/unbound.dir/util/data/msgparse.c.o
[  7%] Building C object external/unbound/CMakeFiles/unbound.dir/util/data/msgreply.c.o
[  7%] Building C object external/unbound/CMakeFiles/unbound.dir/util/data/packed_rrset.c.o
[  8%] Building C object external/unbound/CMakeFiles/unbound.dir/iterator/iterator.c.o
[  8%] Building C object external/unbound/CMakeFiles/unbound.dir/iterator/iter_delegpt.c.o
[  9%] Building C object external/unbound/CMakeFiles/unbound.dir/iterator/iter_donotq.c.o
[  9%] Building C object external/unbound/CMakeFiles/unbound.dir/iterator/iter_fwd.c.o
[  9%] Building C object external/unbound/CMakeFiles/unbound.dir/iterator/iter_hints.c.o
[ 10%] Building C object external/unbound/CMakeFiles/unbound.dir/iterator/iter_priv.c.o
[ 10%] Building C object external/unbound/CMakeFiles/unbound.dir/iterator/iter_resptype.c.o
[ 10%] Building C object external/unbound/CMakeFiles/unbound.dir/iterator/iter_scrub.c.o
[ 11%] Building C object external/unbound/CMakeFiles/unbound.dir/iterator/iter_utils.c.o
[ 11%] Building C object external/unbound/CMakeFiles/unbound.dir/services/listen_dnsport.c.o
[ 11%] Building C object external/unbound/CMakeFiles/unbound.dir/services/localzone.c.o
[ 12%] Building C object external/unbound/CMakeFiles/unbound.dir/services/mesh.c.o
[ 12%] Building C object external/unbound/CMakeFiles/unbound.dir/services/modstack.c.o
[ 13%] Building C object external/unbound/CMakeFiles/unbound.dir/services/outbound_list.c.o
[ 13%] Building C object external/unbound/CMakeFiles/unbound.dir/services/outside_network.c.o
[ 13%] Building C object external/unbound/CMakeFiles/unbound.dir/util/alloc.c.o
[ 14%] Building C object external/unbound/CMakeFiles/unbound.dir/util/config_file.c.o
[ 14%] Building C object external/unbound/CMakeFiles/unbound.dir/util/configlexer.c.o
[ 14%] Building C object external/unbound/CMakeFiles/unbound.dir/util/configparser.c.o
[ 15%] Building C object external/unbound/CMakeFiles/unbound.dir/util/fptr_wlist.c.o
[ 15%] Building C object external/unbound/CMakeFiles/unbound.dir/util/locks.c.o
[ 15%] Building C object external/unbound/CMakeFiles/unbound.dir/util/log.c.o
[ 16%] Building C object external/unbound/CMakeFiles/unbound.dir/util/mini_event.c.o
[ 16%] Building C object external/unbound/CMakeFiles/unbound.dir/util/module.c.o
[ 17%] Building C object external/unbound/CMakeFiles/unbound.dir/util/netevent.c.o
[ 17%] Building C object external/unbound/CMakeFiles/unbound.dir/util/net_help.c.o
[ 17%] Building C object external/unbound/CMakeFiles/unbound.dir/util/random.c.o
[ 18%] Building C object external/unbound/CMakeFiles/unbound.dir/util/rbtree.c.o
[ 18%] Building C object external/unbound/CMakeFiles/unbound.dir/util/regional.c.o
[ 18%] Building C object external/unbound/CMakeFiles/unbound.dir/util/rtt.c.o
[ 19%] Building C object external/unbound/CMakeFiles/unbound.dir/util/storage/dnstree.c.o
[ 19%] Building C object external/unbound/CMakeFiles/unbound.dir/util/storage/lookup3.c.o
[ 19%] Building C object external/unbound/CMakeFiles/unbound.dir/util/storage/lruhash.c.o
[ 20%] Building C object external/unbound/CMakeFiles/unbound.dir/util/storage/slabhash.c.o
[ 20%] Building C object external/unbound/CMakeFiles/unbound.dir/util/timehist.c.o
[ 21%] Building C object external/unbound/CMakeFiles/unbound.dir/util/tube.c.o
[ 21%] Building C object external/unbound/CMakeFiles/unbound.dir/util/winsock_event.c.o
[ 21%] Building C object external/unbound/CMakeFiles/unbound.dir/validator/autotrust.c.o
[ 22%] Building C object external/unbound/CMakeFiles/unbound.dir/validator/val_anchor.c.o
[ 22%] Building C object external/unbound/CMakeFiles/unbound.dir/validator/validator.c.o
[ 22%] Building C object external/unbound/CMakeFiles/unbound.dir/validator/val_kcache.c.o
[ 23%] Building C object external/unbound/CMakeFiles/unbound.dir/validator/val_kentry.c.o
[ 23%] Building C object external/unbound/CMakeFiles/unbound.dir/validator/val_neg.c.o
[ 23%] Building C object external/unbound/CMakeFiles/unbound.dir/validator/val_nsec3.c.o
[ 24%] Building C object external/unbound/CMakeFiles/unbound.dir/validator/val_nsec.c.o
[ 24%] Building C object external/unbound/CMakeFiles/unbound.dir/validator/val_secalgo.c.o
/home/diederik/dev/crypto/monero-project/monero/external/unbound/validator/val_secalgo.c: In function ‘setup_dsa_sig’:
/home/diederik/dev/crypto/monero-project/monero/external/unbound/validator/val_secalgo.c:256:8: error: dereferencing pointer to incomplete type ‘DSA_SIG {aka struct DSA_SIG_st}’
  dsasig->r = R;
        ^~
/home/diederik/dev/crypto/monero-project/monero/external/unbound/validator/val_secalgo.c: In function ‘setup_ecdsa_sig’:
/home/diederik/dev/crypto/monero-project/monero/external/unbound/validator/val_secalgo.c:291:11: error: dereferencing pointer to incomplete type ‘ECDSA_SIG {aka struct ECDSA_SIG_st}’
  ecdsa_sig->r = BN_bin2bn(*sig, bnsize, ecdsa_sig->r);
           ^~
/home/diederik/dev/crypto/monero-project/monero/external/unbound/validator/val_secalgo.c: In function ‘setup_key_digest’:
/home/diederik/dev/crypto/monero-project/monero/external/unbound/validator/val_secalgo.c:348:19: warning: implicit declaration of function ‘EVP_dss1’ [-Wimplicit-function-declaration]
    *digest_type = EVP_dss1();
                   ^~~~~~~~
/home/diederik/dev/crypto/monero-project/monero/external/unbound/validator/val_secalgo.c:348:17: warning: assignment makes pointer from integer without a cast [-Wint-conversion]
    *digest_type = EVP_dss1();
                 ^
/home/diederik/dev/crypto/monero-project/monero/external/unbound/validator/val_secalgo.c: In function ‘verify_canonrrset’:
/home/diederik/dev/crypto/monero-project/monero/external/unbound/validator/val_secalgo.c:509:13: error: storage size of ‘ctx’ isn’t known
  EVP_MD_CTX ctx;
             ^~~
/home/diederik/dev/crypto/monero-project/monero/external/unbound/validator/val_secalgo.c:560:5: warning: implicit declaration of function ‘EVP_MD_CTX_cleanup’ [-Wimplicit-function-declaration]
  if(EVP_MD_CTX_cleanup(&ctx) == 0) {
     ^~~~~~~~~~~~~~~~~~
external/unbound/CMakeFiles/unbound.dir/build.make:1334: recipe for target 'external/unbound/CMakeFiles/unbound.dir/validator/val_secalgo.c.o' failed
make[3]: *** [external/unbound/CMakeFiles/unbound.dir/validator/val_secalgo.c.o] Error 1
make[3]: Leaving directory '/home/diederik/dev/crypto/monero-project/monero/build/release'
CMakeFiles/Makefile2:201: recipe for target 'external/unbound/CMakeFiles/unbound.dir/all' failed
make[2]: *** [external/unbound/CMakeFiles/unbound.dir/all] Error 2
make[2]: Leaving directory '/home/diederik/dev/crypto/monero-project/monero/build/release'
Makefile:138: recipe for target 'all' failed
make[1]: *** [all] Error 2
make[1]: Leaving directory '/home/diederik/dev/crypto/monero-project/monero/build/release'
Makefile:58: recipe for target 'release-all' failed
make: *** [release-all] Error 2
diederik@bagend:~/dev/crypto/monero-project/monero$
```

I figured the successful build with `openssl1.0-dev` isn't very interesting, but made a gist just in case: https://gist.github.com/diederikdehaas/d1131815e203d2f7c5fc1353230d1d8a

# Discussion History
## dotnwat | 2017-02-02T01:56:41+00:00
I'm having this issue too on Debian testing.

## anonimal | 2017-02-02T02:10:18+00:00
Monero uses libunbound 1.5.8 but the current release is 1.6.0. Monero doesn't use a git submodule so there's no easy way swapout versions. If you try installing unbound locally (with apt-get (debian testing shows 1.6.0)), I think monero will use that instead. Maybe 1.6.0 will bring better results?

## diederikdehaas | 2017-02-02T17:51:28+00:00
> If you try installing unbound locally (with apt-get (debian testing shows 1.6.0)), I think monero will use that instead.

It does indeed.

> Maybe 1.6.0 will bring better results?

It does, build against 15eb2bcf6f2132c5410e937186b6a3121147d628, first with libssl1.0-dev (version 1.0.2k-1) and then with libssl-dev (version 1.1.0d-2) and they succeeded both.
See https://gist.github.com/diederikdehaas/2db9c2c0f977a1736dc77658143a7a13 for the full build log of both.

## dotnwat | 2017-02-02T18:33:21+00:00
Thanks for the help I got things building now.

## potyt | 2017-02-20T22:49:39+00:00
Fresh install of Debian stretch, install libunbound 1.6 from deb repo as mentioned, now try and build and still doesn't work for me, still get issue around ctx size not known. Do I need to do anything else, or better still, what's the fix to the code that needs to be made?

## erikd | 2017-07-06T10:03:24+00:00
This has been fixed in commit a85b5759f34c0c4 .


## moneromooo-monero | 2017-08-07T17:20:45+00:00
+resolved

# Action History
- Created by: diederikdehaas | 2016-12-06T14:57:43+00:00
- Closed at: 2017-08-07T18:30:20+00:00
