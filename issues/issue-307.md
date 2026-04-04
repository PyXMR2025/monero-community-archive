---
title: Compile error under Debian Wheezy
source_url: https://github.com/monero-project/monero/issues/307
author: diesisbit
assignees: []
labels: []
created_at: '2015-06-03T19:34:04+00:00'
updated_at: '2015-08-18T20:29:04+00:00'
type: issue
status: closed
closed_at: '2015-08-18T20:29:04+00:00'
---

# Original Description
Hello, building fails under debian wheezy amd64 with libboost 1.55 compiled from tarball.
This is the log:

```
# make release-static-64

mkdir -p build/release
cd build/release && cmake -D STATIC=ON -D ARCH="x86-64" -D BUILD_64=ON -D CMAKE_BUILD_TYPE=release ../.. && make
-- The C compiler identification is GNU 4.7.2
-- The CXX compiler identification is GNU 4.7.2
-- Check for working C compiler: /usr/bin/gcc
-- Check for working C compiler: /usr/bin/gcc -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working CXX compiler: /usr/bin/c++
-- Check for working CXX compiler: /usr/bin/c++ -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Could not find DEVELOPER_LOCAL_TOOLS in env (not required)
-- BOOST_IGNORE_SYSTEM_PATHS defaults to OFF
-- Could not find DEVELOPER_LIBUNBOUND_OLD in env (not required)
-- Building for a 64-bit system
-- Could not find DATABASE in env (not required unless you want to change database type from default: lmdb)
-- Looking for include file pthread.h
-- Looking for include file pthread.h - found
-- Looking for pthread_create
-- Looking for pthread_create - not found.
-- Looking for pthread_create in pthreads
-- Looking for pthread_create in pthreads - not found
-- Looking for pthread_create in pthread
-- Looking for pthread_create in pthread - found
-- Found Threads: TRUE  
-- Could not find miniupnp
-- Using miniupnpc from local source tree for static build
-- Looking for libunbound
-- Found OpenSSL: /usr/lib/x86_64-linux-gnu/libssl.a;/usr/lib/x86_64-linux-gnu/libcrypto.a (found version "1.0.1e") 
-- Looking for arpa/inet.h
-- Looking for arpa/inet.h - found
-- Looking for endian.h
-- Looking for endian.h - found
-- Looking for dlfcn.h
-- Looking for dlfcn.h - found
-- Looking for event.h
-- Looking for event.h - found
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
-- Looking for fnctl
-- Looking for fnctl - not found
-- Looking for fork
-- Looking for fork - found
-- Looking for fseeko
-- Looking for fseeko - found
-- Looking for getauxval
-- Looking for getauxval - not found
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
-- Looking for _beginthreadex
-- Looking for _beginthreadex - not found
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
-- Looking for PTHREAD_PRIO_INHERIT - not found.
-- Looking for pthread_rwlock_t
-- Looking for pthread_rwlock_t - not found.
-- Looking for pthread_spinlock_t
-- Looking for pthread_spinlock_t - not found.
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
-- Looking for sk_SSL_COMP_pop_free - found
-- Looking for SSL_COMP_get_compression_methods
-- Looking for SSL_COMP_get_compression_methods - not found.
-- Looking for EVP_sha1
-- Looking for EVP_sha1 - not found
-- Looking for EVP_sha256
-- Looking for EVP_sha256 - not found
-- Looking for EVP_sha512
-- Looking for EVP_sha512 - not found
-- Looking for FIPS_mode
-- Looking for FIPS_mode - found
-- Looking for HMAC_CTX_init
-- Looking for HMAC_CTX_init - not found
-- Looking for OPENSSL_config
-- Looking for OPENSSL_config - not found
-- Looking for SHA512_Update
-- Looking for SHA512_Update - found
-- Found PkgConfig: /usr/bin/pkg-config (found version "0.26") 
-- checking for module 'libevent'
--   found libevent, version 2.0.19-stable
-- Using 64-bit LMDB from source tree
-- Enabling AES support
-- Found Git: /usr/bin/git
Doxygen: graphviz not found - graphs disabled
-- Could NOT find Doxygen (missing:  DOXYGEN_EXECUTABLE) 
-- Configuring done
-- Generating done
-- Build files have been written to: /files/daemon/source/build/release
make[1]: Entering directory `/files/daemon/source/build/release'
make[2]: Entering directory `/files/daemon/source/build/release'
make[3]: Entering directory `/files/daemon/source/build/release'
Scanning dependencies of target version
make[3]: Leaving directory `/files/daemon/source/build/release'
make[3]: Entering directory `/files/daemon/source/build/release'
[  0%] Generating version/version.h
-- You are currently on commit 431397a
-- The most recent tag was at efad735
-- You are ahead or behind of a tagged release
make[3]: Leaving directory `/files/daemon/source/build/release'
[  0%] Built target version
make[3]: Entering directory `/files/daemon/source/build/release'
Scanning dependencies of target upnpc-static
make[3]: Leaving directory `/files/daemon/source/build/release'
make[3]: Entering directory `/files/daemon/source/build/release'
[  1%] Building C object external/miniupnpc/CMakeFiles/upnpc-static.dir/igd_desc_parse.c.o
[  2%] Building C object external/miniupnpc/CMakeFiles/upnpc-static.dir/miniupnpc.c.o
[  2%] Building C object external/miniupnpc/CMakeFiles/upnpc-static.dir/minixml.c.o
[  3%] Building C object external/miniupnpc/CMakeFiles/upnpc-static.dir/minisoap.c.o
[  4%] Building C object external/miniupnpc/CMakeFiles/upnpc-static.dir/miniwget.c.o
[  4%] Building C object external/miniupnpc/CMakeFiles/upnpc-static.dir/upnpc.c.o
[  5%] Building C object external/miniupnpc/CMakeFiles/upnpc-static.dir/upnpcommands.c.o
[  5%] Building C object external/miniupnpc/CMakeFiles/upnpc-static.dir/upnpreplyparse.c.o
[  6%] Building C object external/miniupnpc/CMakeFiles/upnpc-static.dir/upnperrors.c.o
[  7%] Building C object external/miniupnpc/CMakeFiles/upnpc-static.dir/connecthostport.c.o
[  7%] Building C object external/miniupnpc/CMakeFiles/upnpc-static.dir/portlistingparse.c.o
[  8%] Building C object external/miniupnpc/CMakeFiles/upnpc-static.dir/receivedata.c.o
[  9%] Building C object external/miniupnpc/CMakeFiles/upnpc-static.dir/minissdpc.c.o
Linking C static library libminiupnpc.a
make[3]: Leaving directory `/files/daemon/source/build/release'
[  9%] Built target upnpc-static
make[3]: Entering directory `/files/daemon/source/build/release'
Scanning dependencies of target unbound
make[3]: Leaving directory `/files/daemon/source/build/release'
make[3]: Entering directory `/files/daemon/source/build/release'
[ 10%] Building C object external/unbound/CMakeFiles/unbound.dir/services/cache/dns.c.o
In file included from /files/daemon/source/external/unbound/services/cache/dns.c:41:0:
/files/daemon/source/build/release/external/unbound/config.h:754:0: warning: "NDEBUG" redefined [enabled by default]
<command-line>:0:0: note: this is the location of the previous definition
/files/daemon/source/external/unbound/services/cache/dns.c: In function ‘dns_cache_store_msg’:
/files/daemon/source/external/unbound/services/cache/dns.c:130:3: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/services/cache/dns.c: In function ‘dns_cache_store’:
/files/daemon/source/external/unbound/services/cache/dns.c:852:3: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/services/cache/dns.c:875:3: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
[ 11%] Building C object external/unbound/CMakeFiles/unbound.dir/services/cache/infra.c.o
In file included from /files/daemon/source/external/unbound/services/cache/infra.c:41:0:
/files/daemon/source/build/release/external/unbound/config.h:754:0: warning: "NDEBUG" redefined [enabled by default]
<command-line>:0:0: note: this is the location of the previous definition
/files/daemon/source/external/unbound/services/cache/infra.c: In function ‘infra_delkeyfunc’:
/files/daemon/source/external/unbound/services/cache/infra.c:95:2: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/services/cache/infra.c: In function ‘infra_deldatafunc’:
/files/daemon/source/external/unbound/services/cache/infra.c:103:2: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/services/cache/infra.c: In function ‘rate_delkeyfunc’:
/files/daemon/source/external/unbound/services/cache/infra.c:134:2: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/services/cache/infra.c: In function ‘rate_deldatafunc’:
/files/daemon/source/external/unbound/services/cache/infra.c:142:2: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/services/cache/infra.c: In function ‘domain_limit_findcreate’:
/files/daemon/source/external/unbound/services/cache/infra.c:166:3: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/services/cache/infra.c:173:3: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/services/cache/infra.c:186:3: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/services/cache/infra.c: In function ‘infra_create’:
/files/daemon/source/external/unbound/services/cache/infra.c:225:3: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/services/cache/infra.c: In function ‘domain_limit_free’:
/files/daemon/source/external/unbound/services/cache/infra.c:254:3: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/services/cache/infra.c: In function ‘infra_delete’:
/files/daemon/source/external/unbound/services/cache/infra.c:267:2: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/services/cache/infra.c: In function ‘new_entry’:
/files/daemon/source/external/unbound/services/cache/infra.c:370:3: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/services/cache/infra.c:375:3: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/services/cache/infra.c: In function ‘infra_create_ratedata’:
/files/daemon/source/external/unbound/services/cache/infra.c:750:3: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/services/cache/infra.c:757:3: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
[ 11%] Building C object external/unbound/CMakeFiles/unbound.dir/services/cache/rrset.c.o
In file included from /files/daemon/source/external/unbound/services/cache/rrset.c:41:0:
/files/daemon/source/build/release/external/unbound/config.h:754:0: warning: "NDEBUG" redefined [enabled by default]
<command-line>:0:0: note: this is the location of the previous definition
[ 12%] Building C object external/unbound/CMakeFiles/unbound.dir/util/data/dname.c.o
In file included from /files/daemon/source/external/unbound/util/data/dname.c:42:0:
/files/daemon/source/build/release/external/unbound/config.h:754:0: warning: "NDEBUG" redefined [enabled by default]
<command-line>:0:0: note: this is the location of the previous definition
[ 13%] Building C object external/unbound/CMakeFiles/unbound.dir/util/data/msgencode.c.o
In file included from /files/daemon/source/external/unbound/util/data/msgencode.c:42:0:
/files/daemon/source/build/release/external/unbound/config.h:754:0: warning: "NDEBUG" redefined [enabled by default]
<command-line>:0:0: note: this is the location of the previous definition
[ 13%] Building C object external/unbound/CMakeFiles/unbound.dir/util/data/msgparse.c.o
In file included from /files/daemon/source/external/unbound/util/data/msgparse.c:39:0:
/files/daemon/source/build/release/external/unbound/config.h:754:0: warning: "NDEBUG" redefined [enabled by default]
<command-line>:0:0: note: this is the location of the previous definition
[ 14%] Building C object external/unbound/CMakeFiles/unbound.dir/util/data/msgreply.c.o
In file included from /files/daemon/source/external/unbound/util/data/msgreply.c:42:0:
/files/daemon/source/build/release/external/unbound/config.h:754:0: warning: "NDEBUG" redefined [enabled by default]
<command-line>:0:0: note: this is the location of the previous definition
/files/daemon/source/external/unbound/util/data/msgreply.c: In function ‘parse_create_rrset’:
/files/daemon/source/external/unbound/util/data/msgreply.c:319:15: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/util/data/msgreply.c: In function ‘reply_info_parsedelete’:
/files/daemon/source/external/unbound/util/data/msgreply.c:524:2: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/util/data/msgreply.c: In function ‘query_info_clear’:
/files/daemon/source/external/unbound/util/data/msgreply.c:573:2: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/util/data/msgreply.c: In function ‘query_entry_delete’:
/files/daemon/source/external/unbound/util/data/msgreply.c:596:2: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/util/data/msgreply.c: In function ‘reply_info_delete’:
/files/daemon/source/external/unbound/util/data/msgreply.c:603:2: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/util/data/msgreply.c: In function ‘log_dns_msg’:
/files/daemon/source/external/unbound/util/data/msgreply.c:811:3: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
[ 14%] Building C object external/unbound/CMakeFiles/unbound.dir/util/data/packed_rrset.c.o
In file included from /files/daemon/source/external/unbound/util/data/packed_rrset.c:42:0:
/files/daemon/source/build/release/external/unbound/config.h:754:0: warning: "NDEBUG" redefined [enabled by default]
<command-line>:0:0: note: this is the location of the previous definition
/files/daemon/source/external/unbound/util/data/packed_rrset.c: In function ‘ub_packed_rrset_parsedelete’:
/files/daemon/source/external/unbound/util/data/packed_rrset.c:61:3: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/util/data/packed_rrset.c: In function ‘ub_rrset_key_delete’:
/files/daemon/source/external/unbound/util/data/packed_rrset.c:134:2: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/util/data/packed_rrset.c: In function ‘rrset_data_delete’:
/files/daemon/source/external/unbound/util/data/packed_rrset.c:143:2: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/util/data/packed_rrset.c: In function ‘packed_rrset_copy_alloc’:
/files/daemon/source/external/unbound/util/data/packed_rrset.c:381:3: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
[ 15%] Building C object external/unbound/CMakeFiles/unbound.dir/iterator/iterator.c.o
In file included from /files/daemon/source/external/unbound/iterator/iterator.c:43:0:
/files/daemon/source/build/release/external/unbound/config.h:754:0: warning: "NDEBUG" redefined [enabled by default]
<command-line>:0:0: note: this is the location of the previous definition
/files/daemon/source/external/unbound/iterator/iterator.c: In function ‘caps_free’:
/files/daemon/source/external/unbound/iterator/iterator.c:92:3: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/iterator/iterator.c: In function ‘iter_deinit’:
/files/daemon/source/external/unbound/iterator/iterator.c:104:2: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/iterator/iterator.c: In function ‘iter_clear’:
/files/daemon/source/external/unbound/iterator/iterator.c:3111:4: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
[ 16%] Building C object external/unbound/CMakeFiles/unbound.dir/iterator/iter_delegpt.c.o
In file included from /files/daemon/source/external/unbound/iterator/iter_delegpt.c:42:0:
/files/daemon/source/build/release/external/unbound/config.h:754:0: warning: "NDEBUG" redefined [enabled by default]
<command-line>:0:0: note: this is the location of the previous definition
/files/daemon/source/external/unbound/iterator/iter_delegpt.c: In function ‘delegpt_create_mlc’:
/files/daemon/source/external/unbound/iterator/iter_delegpt.c:518:4: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/iterator/iter_delegpt.c: In function ‘delegpt_free_mlc’:
/files/daemon/source/external/unbound/iterator/iter_delegpt.c:534:3: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/iterator/iter_delegpt.c:541:3: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/iterator/iter_delegpt.c:544:2: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/iterator/iter_delegpt.c: In function ‘delegpt_add_ns_mlc’:
/files/daemon/source/external/unbound/iterator/iter_delegpt.c:572:3: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
[ 16%] Building C object external/unbound/CMakeFiles/unbound.dir/iterator/iter_donotq.c.o
In file included from /files/daemon/source/external/unbound/iterator/iter_donotq.c:44:0:
/files/daemon/source/build/release/external/unbound/config.h:754:0: warning: "NDEBUG" redefined [enabled by default]
<command-line>:0:0: note: this is the location of the previous definition
/files/daemon/source/external/unbound/iterator/iter_donotq.c: In function ‘donotq_delete’:
/files/daemon/source/external/unbound/iterator/iter_donotq.c:72:2: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
[ 17%] Building C object external/unbound/CMakeFiles/unbound.dir/iterator/iter_fwd.c.o
In file included from /files/daemon/source/external/unbound/iterator/iter_fwd.c:42:0:
/files/daemon/source/build/release/external/unbound/config.h:754:0: warning: "NDEBUG" redefined [enabled by default]
<command-line>:0:0: note: this is the location of the previous definition
/files/daemon/source/external/unbound/iterator/iter_fwd.c: In function ‘fwd_zone_free’:
/files/daemon/source/external/unbound/iterator/iter_fwd.c:81:2: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/iterator/iter_fwd.c: In function ‘fwd_del_tree’:
/files/daemon/source/external/unbound/iterator/iter_fwd.c:95:2: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/iterator/iter_fwd.c: In function ‘forwards_delete’:
/files/daemon/source/external/unbound/iterator/iter_fwd.c:104:2: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/iterator/iter_fwd.c: In function ‘forwards_insert_data’:
/files/daemon/source/external/unbound/iterator/iter_fwd.c:123:3: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/iterator/iter_fwd.c:134:3: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/iterator/iter_fwd.c: In function ‘read_fwds_name’:
/files/daemon/source/external/unbound/iterator/iter_fwd.c:194:3: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/iterator/iter_fwd.c:198:2: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/iterator/iter_fwd.c: In function ‘read_fwds_host’:
/files/daemon/source/external/unbound/iterator/iter_fwd.c:218:4: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/iterator/iter_fwd.c:222:3: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/iterator/iter_fwd.c: In function ‘make_stub_holes’:
/files/daemon/source/external/unbound/iterator/iter_fwd.c:303:4: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/iterator/iter_fwd.c:307:3: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
[ 18%] Building C object external/unbound/CMakeFiles/unbound.dir/iterator/iter_hints.c.o
In file included from /files/daemon/source/external/unbound/iterator/iter_hints.c:42:0:
/files/daemon/source/build/release/external/unbound/config.h:754:0: warning: "NDEBUG" redefined [enabled by default]
<command-line>:0:0: note: this is the location of the previous definition
/files/daemon/source/external/unbound/iterator/iter_hints.c: In function ‘hints_stub_free’:
/files/daemon/source/external/unbound/iterator/iter_hints.c:67:2: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/iterator/iter_hints.c: In function ‘hints_delete’:
/files/daemon/source/external/unbound/iterator/iter_hints.c:87:2: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/iterator/iter_hints.c: In function ‘ah’:
/files/daemon/source/external/unbound/iterator/iter_hints.c:106:3: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/iterator/iter_hints.c:109:2: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/iterator/iter_hints.c: In function ‘hints_insert’:
/files/daemon/source/external/unbound/iterator/iter_hints.c:183:3: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/iterator/iter_hints.c: In function ‘read_stubs_name’:
/files/daemon/source/external/unbound/iterator/iter_hints.c:205:3: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/iterator/iter_hints.c:209:2: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/iterator/iter_hints.c: In function ‘read_stubs_host’:
/files/daemon/source/external/unbound/iterator/iter_hints.c:229:4: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/iterator/iter_hints.c:233:3: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
[ 18%] Building C object external/unbound/CMakeFiles/unbound.dir/iterator/iter_priv.c.o
In file included from /files/daemon/source/external/unbound/iterator/iter_priv.c:43:0:
/files/daemon/source/build/release/external/unbound/config.h:754:0: warning: "NDEBUG" redefined [enabled by default]
<command-line>:0:0: note: this is the location of the previous definition
/files/daemon/source/external/unbound/iterator/iter_priv.c: In function ‘priv_delete’:
/files/daemon/source/external/unbound/iterator/iter_priv.c:74:2: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/iterator/iter_priv.c: In function ‘read_names’:
/files/daemon/source/external/unbound/iterator/iter_priv.c:127:3: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
[ 19%] Building C object external/unbound/CMakeFiles/unbound.dir/iterator/iter_resptype.c.o
In file included from /files/daemon/source/external/unbound/iterator/iter_resptype.c:42:0:
/files/daemon/source/build/release/external/unbound/config.h:754:0: warning: "NDEBUG" redefined [enabled by default]
<command-line>:0:0: note: this is the location of the previous definition
[ 19%] Building C object external/unbound/CMakeFiles/unbound.dir/iterator/iter_scrub.c.o
In file included from /files/daemon/source/external/unbound/iterator/iter_scrub.c:42:0:
/files/daemon/source/build/release/external/unbound/config.h:754:0: warning: "NDEBUG" redefined [enabled by default]
<command-line>:0:0: note: this is the location of the previous definition
[ 20%] Building C object external/unbound/CMakeFiles/unbound.dir/iterator/iter_utils.c.o
In file included from /files/daemon/source/external/unbound/iterator/iter_utils.c:42:0:
/files/daemon/source/build/release/external/unbound/config.h:754:0: warning: "NDEBUG" redefined [enabled by default]
<command-line>:0:0: note: this is the location of the previous definition
/files/daemon/source/external/unbound/iterator/iter_utils.c: In function ‘caps_white_apply_cfg’:
/files/daemon/source/external/unbound/iterator/iter_utils.c:125:4: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/iterator/iter_utils.c:135:4: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
[ 21%] Building C object external/unbound/CMakeFiles/unbound.dir/services/listen_dnsport.c.o
In file included from /files/daemon/source/external/unbound/services/listen_dnsport.c:41:0:
/files/daemon/source/build/release/external/unbound/config.h:754:0: warning: "NDEBUG" redefined [enabled by default]
<command-line>:0:0: note: this is the location of the previous definition
/files/daemon/source/external/unbound/services/listen_dnsport.c: In function ‘listen_create’:
/files/daemon/source/external/unbound/services/listen_dnsport.c:963:3: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/services/listen_dnsport.c: In function ‘listen_list_delete’:
/files/daemon/source/external/unbound/services/listen_dnsport.c:1014:3: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/services/listen_dnsport.c: In function ‘listen_delete’:
/files/daemon/source/external/unbound/services/listen_dnsport.c:1026:2: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/services/listen_dnsport.c: In function ‘listening_ports_free’:
/files/daemon/source/external/unbound/services/listen_dnsport.c:1126:3: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
[ 21%] Building C object external/unbound/CMakeFiles/unbound.dir/services/localzone.c.o
In file included from /files/daemon/source/external/unbound/services/localzone.c:41:0:
/files/daemon/source/build/release/external/unbound/config.h:754:0: warning: "NDEBUG" redefined [enabled by default]
<command-line>:0:0: note: this is the location of the previous definition
/files/daemon/source/external/unbound/services/localzone.c: In function ‘local_zones_delete’:
/files/daemon/source/external/unbound/services/localzone.c:85:2: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/services/localzone.c: In function ‘local_zone_delete’:
/files/daemon/source/external/unbound/services/localzone.c:95:2: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/services/localzone.c: In function ‘local_zone_create’:
/files/daemon/source/external/unbound/services/localzone.c:157:3: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/services/localzone.c: In function ‘lz_enter_zone’:
/files/daemon/source/external/unbound/services/localzone.c:207:3: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/services/localzone.c: In function ‘lz_enter_rr_into_zone’:
/files/daemon/source/external/unbound/services/localzone.c:445:3: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/services/localzone.c:450:3: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/services/localzone.c:454:2: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/services/localzone.c: In function ‘lz_enter_rr_str’:
/files/daemon/source/external/unbound/services/localzone.c:502:2: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/services/localzone.c: In function ‘lz_exists’:
/files/daemon/source/external/unbound/services/localzone.c:537:3: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/services/localzone.c:541:2: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/services/localzone.c: In function ‘lz_setup_implicit’:
/files/daemon/source/external/unbound/services/localzone.c:839:6: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/services/localzone.c:847:5: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/services/localzone.c:851:10: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/services/localzone.c:861:3: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/services/localzone.c: In function ‘local_zones_add_RR’:
/files/daemon/source/external/unbound/services/localzone.c:1362:3: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
[ 22%] Building C object external/unbound/CMakeFiles/unbound.dir/services/mesh.c.o
In file included from /files/daemon/source/external/unbound/services/mesh.c:45:0:
/files/daemon/source/build/release/external/unbound/config.h:754:0: warning: "NDEBUG" redefined [enabled by default]
<command-line>:0:0: note: this is the location of the previous definition
/files/daemon/source/external/unbound/services/mesh.c: In function ‘mesh_create’:
/files/daemon/source/external/unbound/services/mesh.c:172:3: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/services/mesh.c: In function ‘mesh_delete’:
/files/daemon/source/external/unbound/services/mesh.c:219:2: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/services/mesh.c: In function ‘mesh_do_callback’:
/files/daemon/source/external/unbound/services/mesh.c:826:2: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
[ 23%] Building C object external/unbound/CMakeFiles/unbound.dir/services/modstack.c.o
In file included from /files/daemon/source/external/unbound/services/modstack.c:41:0:
/files/daemon/source/build/release/external/unbound/config.h:754:0: warning: "NDEBUG" redefined [enabled by default]
<command-line>:0:0: note: this is the location of the previous definition
/files/daemon/source/external/unbound/services/modstack.c: In function ‘modstack_desetup’:
/files/daemon/source/external/unbound/services/modstack.c:202:9: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
[ 23%] Building C object external/unbound/CMakeFiles/unbound.dir/services/outbound_list.c.o
In file included from /files/daemon/source/external/unbound/services/outbound_list.c:42:0:
/files/daemon/source/build/release/external/unbound/config.h:754:0: warning: "NDEBUG" redefined [enabled by default]
<command-line>:0:0: note: this is the location of the previous definition
[ 24%] Building C object external/unbound/CMakeFiles/unbound.dir/services/outside_network.c.o
In file included from /files/daemon/source/external/unbound/services/outside_network.c:42:0:
/files/daemon/source/build/release/external/unbound/config.h:754:0: warning: "NDEBUG" redefined [enabled by default]
<command-line>:0:0: note: this is the location of the previous definition
[ 24%] Building C object external/unbound/CMakeFiles/unbound.dir/util/alloc.c.o
In file included from /files/daemon/source/external/unbound/util/alloc.c:42:0:
/files/daemon/source/build/release/external/unbound/config.h:754:0: warning: "NDEBUG" redefined [enabled by default]
<command-line>:0:0: note: this is the location of the previous definition
/files/daemon/source/external/unbound/util/alloc.c: In function ‘alloc_clear’:
/files/daemon/source/external/unbound/util/alloc.c:155:4: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/util/alloc.c:164:3: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
[ 25%] Building C object external/unbound/CMakeFiles/unbound.dir/util/config_file.c.o
In file included from /files/daemon/source/external/unbound/util/config_file.c:42:0:
/files/daemon/source/build/release/external/unbound/config.h:754:0: warning: "NDEBUG" redefined [enabled by default]
<command-line>:0:0: note: this is the location of the previous definition
/files/daemon/source/external/unbound/util/config_file.c: In function ‘config_create_forlib’:
/files/daemon/source/external/unbound/util/config_file.c:251:2: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/util/config_file.c: In function ‘config_set_option’:
/files/daemon/source/external/unbound/util/config_file.c:352:3: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/util/config_file.c:368:7: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/util/config_file.c:369:7: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/util/config_file.c:405:7: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/util/config_file.c:406:7: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/util/config_file.c:407:7: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/util/config_file.c:408:7: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/util/config_file.c:411:7: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/util/config_file.c:412:7: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/util/config_file.c:414:7: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/util/config_file.c:433:7: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/util/config_file.c:443:7: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/util/config_file.c:457:7: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/util/config_file.c:458:7: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/util/config_file.c:459:7: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/util/config_file.c:460:7: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/util/config_file.c:461:7: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/util/config_file.c:462:7: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/util/config_file.c:480:19: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/util/config_file.c:483:4: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/util/config_file.c: In function ‘config_collate_cat’:
/files/daemon/source/external/unbound/util/config_file.c:573:4: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/util/config_file.c: In function ‘config_delstrlist’:
/files/daemon/source/external/unbound/util/config_file.c:863:3: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/util/config_file.c: In function ‘config_deldblstrlist’:
/files/daemon/source/external/unbound/util/config_file.c:875:3: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/util/config_file.c: In function ‘config_delstubs’:
/files/daemon/source/external/unbound/util/config_file.c:888:3: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/util/config_file.c: In function ‘config_delete’:
/files/daemon/source/external/unbound/util/config_file.c:900:2: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
[ 26%] Building C object external/unbound/CMakeFiles/unbound.dir/util/configlexer.c.o
In file included from /files/daemon/source/external/unbound/util/configlexer.c:1:0:
/files/daemon/source/build/release/external/unbound/config.h:754:0: warning: "NDEBUG" redefined [enabled by default]
<command-line>:0:0: note: this is the location of the previous definition
[ 26%] Building C object external/unbound/CMakeFiles/unbound.dir/util/configparser.c.o
In file included from ./util/configparser.y:39:0:
/files/daemon/source/build/release/external/unbound/config.h:754:0: warning: "NDEBUG" redefined [enabled by default]
<command-line>:0:0: note: this is the location of the previous definition
[ 27%] Building C object external/unbound/CMakeFiles/unbound.dir/util/fptr_wlist.c.o
In file included from /files/daemon/source/external/unbound/util/fptr_wlist.c:46:0:
/files/daemon/source/build/release/external/unbound/config.h:754:0: warning: "NDEBUG" redefined [enabled by default]
<command-line>:0:0: note: this is the location of the previous definition
[ 28%] Building C object external/unbound/CMakeFiles/unbound.dir/util/locks.c.o
In file included from /files/daemon/source/external/unbound/util/locks.c:42:0:
/files/daemon/source/build/release/external/unbound/config.h:754:0: warning: "NDEBUG" redefined [enabled by default]
<command-line>:0:0: note: this is the location of the previous definition
[ 28%] Building C object external/unbound/CMakeFiles/unbound.dir/util/log.c.o
In file included from /files/daemon/source/external/unbound/util/log.c:40:0:
/files/daemon/source/build/release/external/unbound/config.h:754:0: warning: "NDEBUG" redefined [enabled by default]
<command-line>:0:0: note: this is the location of the previous definition
/files/daemon/source/external/unbound/util/log.c: In function ‘fatal_exit’:
/files/daemon/source/external/unbound/util/log.c:320:2: warning: incompatible implicit declaration of built-in function ‘exit’ [enabled by default]
[ 29%] Building C object external/unbound/CMakeFiles/unbound.dir/util/mini_event.c.o
In file included from /files/daemon/source/external/unbound/util/mini_event.c:43:0:
/files/daemon/source/build/release/external/unbound/config.h:754:0: warning: "NDEBUG" redefined [enabled by default]
<command-line>:0:0: note: this is the location of the previous definition
[ 30%] Building C object external/unbound/CMakeFiles/unbound.dir/util/module.c.o
In file included from /files/daemon/source/external/unbound/util/module.c:40:0:
/files/daemon/source/build/release/external/unbound/config.h:754:0: warning: "NDEBUG" redefined [enabled by default]
<command-line>:0:0: note: this is the location of the previous definition
[ 30%] Building C object external/unbound/CMakeFiles/unbound.dir/util/netevent.c.o
In file included from /files/daemon/source/external/unbound/util/netevent.c:41:0:
/files/daemon/source/build/release/external/unbound/config.h:754:0: warning: "NDEBUG" redefined [enabled by default]
<command-line>:0:0: note: this is the location of the previous definition
[ 31%] Building C object external/unbound/CMakeFiles/unbound.dir/util/net_help.c.o
In file included from /files/daemon/source/external/unbound/util/net_help.c:40:0:
/files/daemon/source/build/release/external/unbound/config.h:754:0: warning: "NDEBUG" redefined [enabled by default]
<command-line>:0:0: note: this is the location of the previous definition
[ 31%] Building C object external/unbound/CMakeFiles/unbound.dir/util/random.c.o
In file included from /files/daemon/source/external/unbound/util/random.c:60:0:
/files/daemon/source/build/release/external/unbound/config.h:754:0: warning: "NDEBUG" redefined [enabled by default]
<command-line>:0:0: note: this is the location of the previous definition
/files/daemon/source/external/unbound/util/random.c: In function ‘ub_randfree’:
/files/daemon/source/external/unbound/util/random.c:164:3: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
[ 32%] Building C object external/unbound/CMakeFiles/unbound.dir/util/rbtree.c.o
In file included from /files/daemon/source/external/unbound/util/rbtree.c:42:0:
/files/daemon/source/build/release/external/unbound/config.h:754:0: warning: "NDEBUG" redefined [enabled by default]
<command-line>:0:0: note: this is the location of the previous definition
[ 33%] Building C object external/unbound/CMakeFiles/unbound.dir/util/regional.c.o
In file included from /files/daemon/source/external/unbound/util/regional.c:43:0:
/files/daemon/source/build/release/external/unbound/config.h:754:0: warning: "NDEBUG" redefined [enabled by default]
<command-line>:0:0: note: this is the location of the previous definition
/files/daemon/source/external/unbound/util/regional.c: In function ‘regional_free_all’:
/files/daemon/source/external/unbound/util/regional.c:100:3: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/util/regional.c:106:3: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/util/regional.c: In function ‘regional_destroy’:
/files/daemon/source/external/unbound/util/regional.c:117:2: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
[ 33%] Building C object external/unbound/CMakeFiles/unbound.dir/util/rtt.c.o
In file included from /files/daemon/source/external/unbound/util/rtt.c:42:0:
/files/daemon/source/build/release/external/unbound/config.h:754:0: warning: "NDEBUG" redefined [enabled by default]
<command-line>:0:0: note: this is the location of the previous definition
[ 34%] Building C object external/unbound/CMakeFiles/unbound.dir/util/storage/dnstree.c.o
In file included from /files/daemon/source/external/unbound/util/storage/dnstree.c:42:0:
/files/daemon/source/build/release/external/unbound/config.h:754:0: warning: "NDEBUG" redefined [enabled by default]
<command-line>:0:0: note: this is the location of the previous definition
[ 35%] Building C object external/unbound/CMakeFiles/unbound.dir/util/storage/lookup3.c.o
In file included from /files/daemon/source/external/unbound/util/storage/lookup3.c:47:0:
/files/daemon/source/build/release/external/unbound/config.h:754:0: warning: "NDEBUG" redefined [enabled by default]
<command-line>:0:0: note: this is the location of the previous definition
[ 35%] Building C object external/unbound/CMakeFiles/unbound.dir/util/storage/lruhash.c.o
In file included from /files/daemon/source/external/unbound/util/storage/lruhash.c:43:0:
/files/daemon/source/build/release/external/unbound/config.h:754:0: warning: "NDEBUG" redefined [enabled by default]
<command-line>:0:0: note: this is the location of the previous definition
/files/daemon/source/external/unbound/util/storage/lruhash.c: In function ‘lruhash_create’:
/files/daemon/source/external/unbound/util/storage/lruhash.c:86:3: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/util/storage/lruhash.c: In function ‘lruhash_delete’:
/files/daemon/source/external/unbound/util/storage/lruhash.c:161:2: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/util/storage/lruhash.c: In function ‘table_grow’:
/files/daemon/source/external/unbound/util/storage/lruhash.c:254:2: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
[ 36%] Building C object external/unbound/CMakeFiles/unbound.dir/util/storage/slabhash.c.o
In file included from /files/daemon/source/external/unbound/util/storage/slabhash.c:45:0:
/files/daemon/source/build/release/external/unbound/config.h:754:0: warning: "NDEBUG" redefined [enabled by default]
<command-line>:0:0: note: this is the location of the previous definition
/files/daemon/source/external/unbound/util/storage/slabhash.c: In function ‘slabhash_create’:
/files/daemon/source/external/unbound/util/storage/slabhash.c:61:3: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/util/storage/slabhash.c: In function ‘slabhash_delete’:
/files/daemon/source/external/unbound/util/storage/slabhash.c:95:3: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/util/storage/slabhash.c:97:2: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/util/storage/slabhash.c: In function ‘delkey’:
/files/daemon/source/external/unbound/util/storage/slabhash.c:174:35: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/util/storage/slabhash.c: In function ‘deldata’:
/files/daemon/source/external/unbound/util/storage/slabhash.c:176:51: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
[ 36%] Building C object external/unbound/CMakeFiles/unbound.dir/util/timehist.c.o
In file included from /files/daemon/source/external/unbound/util/timehist.c:41:0:
/files/daemon/source/build/release/external/unbound/config.h:754:0: warning: "NDEBUG" redefined [enabled by default]
<command-line>:0:0: note: this is the location of the previous definition
/files/daemon/source/external/unbound/util/timehist.c: In function ‘timehist_setup’:
/files/daemon/source/external/unbound/util/timehist.c:94:3: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/util/timehist.c: In function ‘timehist_delete’:
/files/daemon/source/external/unbound/util/timehist.c:106:2: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
[ 37%] Building C object external/unbound/CMakeFiles/unbound.dir/util/tube.c.o
In file included from /files/daemon/source/external/unbound/util/tube.c:41:0:
/files/daemon/source/build/release/external/unbound/config.h:754:0: warning: "NDEBUG" redefined [enabled by default]
<command-line>:0:0: note: this is the location of the previous definition
/files/daemon/source/external/unbound/util/tube.c: In function ‘tube_create’:
/files/daemon/source/external/unbound/util/tube.c:71:3: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/util/tube.c: In function ‘tube_delete’:
/files/daemon/source/external/unbound/util/tube.c:96:2: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/util/tube.c: In function ‘tube_remove_bg_listen’:
/files/daemon/source/external/unbound/util/tube.c:122:3: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/util/tube.c: In function ‘tube_remove_bg_write’:
/files/daemon/source/external/unbound/util/tube.c:139:4: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/util/tube.c: In function ‘tube_handle_write’:
/files/daemon/source/external/unbound/util/tube.c:274:2: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/util/tube.c: In function ‘tube_read_msg’:
/files/daemon/source/external/unbound/util/tube.c:375:4: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/util/tube.c:380:4: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/util/tube.c:386:3: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/util/tube.c: In function ‘tube_queue_item’:
/files/daemon/source/external/unbound/util/tube.c:457:3: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
[ 38%] Building C object external/unbound/CMakeFiles/unbound.dir/util/winsock_event.c.o
In file included from /files/daemon/source/external/unbound/util/winsock_event.c:41:0:
/files/daemon/source/build/release/external/unbound/config.h:754:0: warning: "NDEBUG" redefined [enabled by default]
<command-line>:0:0: note: this is the location of the previous definition
[ 38%] Building C object external/unbound/CMakeFiles/unbound.dir/validator/autotrust.c.o
In file included from /files/daemon/source/external/unbound/validator/autotrust.c:43:0:
/files/daemon/source/build/release/external/unbound/config.h:754:0: warning: "NDEBUG" redefined [enabled by default]
<command-line>:0:0: note: this is the location of the previous definition
[ 39%] Building C object external/unbound/CMakeFiles/unbound.dir/validator/val_anchor.c.o
In file included from /files/daemon/source/external/unbound/validator/val_anchor.c:41:0:
/files/daemon/source/build/release/external/unbound/config.h:754:0: warning: "NDEBUG" redefined [enabled by default]
<command-line>:0:0: note: this is the location of the previous definition
/files/daemon/source/external/unbound/validator/val_anchor.c: In function ‘assembled_rrset_delete’:
/files/daemon/source/external/unbound/validator/val_anchor.c:104:3: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/validator/val_anchor.c:109:2: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/validator/val_anchor.c: In function ‘anchors_delfunc’:
/files/daemon/source/external/unbound/validator/val_anchor.c:124:3: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/validator/val_anchor.c: In function ‘anchors_delete’:
/files/daemon/source/external/unbound/validator/val_anchor.c:148:2: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/validator/val_anchor.c: In function ‘anchor_new_ta’:
/files/daemon/source/external/unbound/validator/val_anchor.c:234:3: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/validator/val_anchor.c: In function ‘anchor_new_ta_key’:
/files/daemon/source/external/unbound/validator/val_anchor.c:281:3: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/validator/val_anchor.c: In function ‘anchor_insert_insecure’:
/files/daemon/source/external/unbound/validator/val_anchor.c:391:2: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/validator/val_anchor.c: In function ‘process_bind_contents’:
/files/daemon/source/external/unbound/validator/val_anchor.c:689:5: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/validator/val_anchor.c:692:4: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/validator/val_anchor.c: In function ‘assemble_it’:
/files/daemon/source/external/unbound/validator/val_anchor.c:867:3: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/validator/val_anchor.c:878:3: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/validator/val_anchor.c:887:3: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/validator/val_anchor.c:894:3: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/validator/val_anchor.c:902:3: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
[ 40%] Building C object external/unbound/CMakeFiles/unbound.dir/validator/validator.c.o
In file included from /files/daemon/source/external/unbound/validator/validator.c:42:0:
/files/daemon/source/build/release/external/unbound/config.h:754:0: warning: "NDEBUG" redefined [enabled by default]
<command-line>:0:0: note: this is the location of the previous definition
/files/daemon/source/external/unbound/validator/validator.c: In function ‘fill_nsec3_iter’:
/files/daemon/source/external/unbound/validator/validator.c:75:2: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/validator/validator.c: In function ‘val_deinit’:
/files/daemon/source/external/unbound/validator/validator.c:193:2: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/validator/validator.c: In function ‘processFinished’:
/files/daemon/source/external/unbound/validator/validator.c:2075:5: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
[ 40%] Building C object external/unbound/CMakeFiles/unbound.dir/validator/val_kcache.c.o
In file included from /files/daemon/source/external/unbound/validator/val_kcache.c:41:0:
/files/daemon/source/build/release/external/unbound/config.h:754:0: warning: "NDEBUG" redefined [enabled by default]
<command-line>:0:0: note: this is the location of the previous definition
/files/daemon/source/external/unbound/validator/val_kcache.c: In function ‘key_cache_create’:
/files/daemon/source/external/unbound/validator/val_kcache.c:67:3: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/validator/val_kcache.c: In function ‘key_cache_delete’:
/files/daemon/source/external/unbound/validator/val_kcache.c:79:2: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
[ 41%] Building C object external/unbound/CMakeFiles/unbound.dir/validator/val_kentry.c.o
In file included from /files/daemon/source/external/unbound/validator/val_kentry.c:41:0:
/files/daemon/source/build/release/external/unbound/config.h:754:0: warning: "NDEBUG" redefined [enabled by default]
<command-line>:0:0: note: this is the location of the previous definition
[ 41%] Building C object external/unbound/CMakeFiles/unbound.dir/validator/val_neg.c.o
In file included from /files/daemon/source/external/unbound/validator/val_neg.c:44:0:
/files/daemon/source/build/release/external/unbound/config.h:754:0: warning: "NDEBUG" redefined [enabled by default]
<command-line>:0:0: note: this is the location of the previous definition
[ 42%] Building C object external/unbound/CMakeFiles/unbound.dir/validator/val_nsec3.c.o
In file included from /files/daemon/source/external/unbound/validator/val_nsec3.c:43:0:
/files/daemon/source/build/release/external/unbound/config.h:754:0: warning: "NDEBUG" redefined [enabled by default]
<command-line>:0:0: note: this is the location of the previous definition
[ 43%] Building C object external/unbound/CMakeFiles/unbound.dir/validator/val_nsec.c.o
In file included from /files/daemon/source/external/unbound/validator/val_nsec.c:43:0:
/files/daemon/source/build/release/external/unbound/config.h:754:0: warning: "NDEBUG" redefined [enabled by default]
<command-line>:0:0: note: this is the location of the previous definition
[ 43%] Building C object external/unbound/CMakeFiles/unbound.dir/validator/val_secalgo.c.o
In file included from /files/daemon/source/external/unbound/validator/val_secalgo.c:43:0:
/files/daemon/source/build/release/external/unbound/config.h:754:0: warning: "NDEBUG" redefined [enabled by default]
<command-line>:0:0: note: this is the location of the previous definition
[ 44%] Building C object external/unbound/CMakeFiles/unbound.dir/validator/val_sigcrypt.c.o
In file included from /files/daemon/source/external/unbound/validator/val_sigcrypt.c:43:0:
/files/daemon/source/build/release/external/unbound/config.h:754:0: warning: "NDEBUG" redefined [enabled by default]
<command-line>:0:0: note: this is the location of the previous definition
[ 45%] Building C object external/unbound/CMakeFiles/unbound.dir/validator/val_utils.c.o
In file included from /files/daemon/source/external/unbound/validator/val_utils.c:41:0:
/files/daemon/source/build/release/external/unbound/config.h:754:0: warning: "NDEBUG" redefined [enabled by default]
<command-line>:0:0: note: this is the location of the previous definition
[ 45%] Building C object external/unbound/CMakeFiles/unbound.dir/dns64/dns64.c.o
In file included from /files/daemon/source/external/unbound/dns64/dns64.c:42:0:
/files/daemon/source/build/release/external/unbound/config.h:754:0: warning: "NDEBUG" redefined [enabled by default]
<command-line>:0:0: note: this is the location of the previous definition
/files/daemon/source/external/unbound/dns64/dns64.c: In function ‘dns64_deinit’:
/files/daemon/source/external/unbound/dns64/dns64.c:351:5: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
[ 46%] Building C object external/unbound/CMakeFiles/unbound.dir/testcode/checklocks.c.o
In file included from /files/daemon/source/external/unbound/testcode/checklocks.c:36:0:
/files/daemon/source/build/release/external/unbound/config.h:754:0: warning: "NDEBUG" redefined [enabled by default]
<command-line>:0:0: note: this is the location of the previous definition
[ 46%] Building C object external/unbound/CMakeFiles/unbound.dir/sldns/keyraw.c.o
In file included from /files/daemon/source/external/unbound/sldns/keyraw.c:13:0:
/files/daemon/source/build/release/external/unbound/config.h:754:0: warning: "NDEBUG" redefined [enabled by default]
<command-line>:0:0: note: this is the location of the previous definition
[ 47%] Building C object external/unbound/CMakeFiles/unbound.dir/sldns/sbuffer.c.o
In file included from /files/daemon/source/external/unbound/sldns/sbuffer.c:14:0:
/files/daemon/source/build/release/external/unbound/config.h:754:0: warning: "NDEBUG" redefined [enabled by default]
<command-line>:0:0: note: this is the location of the previous definition
/files/daemon/source/external/unbound/sldns/sbuffer.c: In function ‘sldns_buffer_new’:
/files/daemon/source/external/unbound/sldns/sbuffer.c:29:3: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/sldns/sbuffer.c: In function ‘sldns_buffer_set_capacity’:
/files/daemon/source/external/unbound/sldns/sbuffer.c:79:21: warning: incompatible implicit declaration of built-in function ‘realloc’ [enabled by default]
/files/daemon/source/external/unbound/sldns/sbuffer.c: In function ‘sldns_buffer_free’:
/files/daemon/source/external/unbound/sldns/sbuffer.c:156:3: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
[ 48%] Building C object external/unbound/CMakeFiles/unbound.dir/sldns/wire2str.c.o
In file included from /files/daemon/source/external/unbound/sldns/wire2str.c:17:0:
/files/daemon/source/build/release/external/unbound/config.h:754:0: warning: "NDEBUG" redefined [enabled by default]
<command-line>:0:0: note: this is the location of the previous definition
[ 48%] Building C object external/unbound/CMakeFiles/unbound.dir/sldns/parse.c.o
In file included from /files/daemon/source/external/unbound/sldns/parse.c:10:0:
/files/daemon/source/build/release/external/unbound/config.h:754:0: warning: "NDEBUG" redefined [enabled by default]
<command-line>:0:0: note: this is the location of the previous definition
/files/daemon/source/external/unbound/sldns/parse.c: In function ‘sldns_fget_keyword_data_l’:
/files/daemon/source/external/unbound/sldns/parse.c:203:16: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/sldns/parse.c:212:16: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/sldns/parse.c:216:16: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/sldns/parse.c: In function ‘sldns_bget_keyword_data’:
/files/daemon/source/external/unbound/sldns/parse.c:454:16: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/sldns/parse.c:460:16: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/sldns/parse.c:466:16: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
[ 49%] Building C object external/unbound/CMakeFiles/unbound.dir/sldns/parseutil.c.o
In file included from /files/daemon/source/external/unbound/sldns/parseutil.c:15:0:
/files/daemon/source/build/release/external/unbound/config.h:754:0: warning: "NDEBUG" redefined [enabled by default]
<command-line>:0:0: note: this is the location of the previous definition
[ 50%] Building C object external/unbound/CMakeFiles/unbound.dir/sldns/rrdef.c.o
In file included from /files/daemon/source/external/unbound/sldns/rrdef.c:15:0:
/files/daemon/source/build/release/external/unbound/config.h:754:0: warning: "NDEBUG" redefined [enabled by default]
<command-line>:0:0: note: this is the location of the previous definition
[ 50%] Building C object external/unbound/CMakeFiles/unbound.dir/sldns/str2wire.c.o
In file included from /files/daemon/source/external/unbound/sldns/str2wire.c:14:0:
/files/daemon/source/build/release/external/unbound/config.h:754:0: warning: "NDEBUG" redefined [enabled by default]
<command-line>:0:0: note: this is the location of the previous definition
[ 51%] Building C object external/unbound/CMakeFiles/unbound.dir/compat/memcmp.c.o
In file included from /files/daemon/source/external/unbound/compat/memcmp.c:9:0:
/files/daemon/source/build/release/external/unbound/config.h:754:0: warning: "NDEBUG" redefined [enabled by default]
<command-line>:0:0: note: this is the location of the previous definition
[ 52%] Building C object external/unbound/CMakeFiles/unbound.dir/compat/strlcat.c.o
In file included from /files/daemon/source/external/unbound/compat/strlcat.c:32:0:
/files/daemon/source/build/release/external/unbound/config.h:754:0: warning: "NDEBUG" redefined [enabled by default]
<command-line>:0:0: note: this is the location of the previous definition
[ 52%] Building C object external/unbound/CMakeFiles/unbound.dir/compat/strlcpy.c.o
In file included from /files/daemon/source/external/unbound/compat/strlcpy.c:20:0:
/files/daemon/source/build/release/external/unbound/config.h:754:0: warning: "NDEBUG" redefined [enabled by default]
<command-line>:0:0: note: this is the location of the previous definition
[ 53%] Building C object external/unbound/CMakeFiles/unbound.dir/compat/explicit_bzero.c.o
In file included from /files/daemon/source/external/unbound/compat/explicit_bzero.c:6:0:
/files/daemon/source/build/release/external/unbound/config.h:754:0: warning: "NDEBUG" redefined [enabled by default]
<command-line>:0:0: note: this is the location of the previous definition
[ 53%] Building C object external/unbound/CMakeFiles/unbound.dir/compat/arc4random.c.o
In file included from /files/daemon/source/external/unbound/compat/arc4random.c:20:0:
/files/daemon/source/build/release/external/unbound/config.h:754:0: warning: "NDEBUG" redefined [enabled by default]
<command-line>:0:0: note: this is the location of the previous definition
[ 54%] Building C object external/unbound/CMakeFiles/unbound.dir/compat/arc4random_uniform.c.o
In file included from /files/daemon/source/external/unbound/compat/arc4random_uniform.c:19:0:
/files/daemon/source/build/release/external/unbound/config.h:754:0: warning: "NDEBUG" redefined [enabled by default]
<command-line>:0:0: note: this is the location of the previous definition
[ 55%] Building C object external/unbound/CMakeFiles/unbound.dir/compat/sha512.c.o
In file included from /files/daemon/source/external/unbound/compat/sha512.c:43:0:
/files/daemon/source/build/release/external/unbound/config.h:754:0: warning: "NDEBUG" redefined [enabled by default]
<command-line>:0:0: note: this is the location of the previous definition
[ 55%] Building C object external/unbound/CMakeFiles/unbound.dir/compat/reallocarray.c.o
In file included from /files/daemon/source/external/unbound/compat/reallocarray.c:18:0:
/files/daemon/source/build/release/external/unbound/config.h:754:0: warning: "NDEBUG" redefined [enabled by default]
<command-line>:0:0: note: this is the location of the previous definition
[ 56%] Building C object external/unbound/CMakeFiles/unbound.dir/compat/arc4_lock.c.o
In file included from /files/daemon/source/external/unbound/compat/arc4_lock.c:34:0:
/files/daemon/source/build/release/external/unbound/config.h:754:0: warning: "NDEBUG" redefined [enabled by default]
<command-line>:0:0: note: this is the location of the previous definition
[ 57%] Building C object external/unbound/CMakeFiles/unbound.dir/compat/getentropy_linux.c.o
In file included from /files/daemon/source/external/unbound/compat/getentropy_linux.c:19:0:
/files/daemon/source/build/release/external/unbound/config.h:754:0: warning: "NDEBUG" redefined [enabled by default]
<command-line>:0:0: note: this is the location of the previous definition
[ 57%] Building C object external/unbound/CMakeFiles/unbound.dir/libunbound/context.c.o
In file included from /files/daemon/source/external/unbound/libunbound/context.c:41:0:
/files/daemon/source/build/release/external/unbound/config.h:754:0: warning: "NDEBUG" redefined [enabled by default]
<command-line>:0:0: note: this is the location of the previous definition
/files/daemon/source/external/unbound/libunbound/context.c: In function ‘context_query_delete’:
/files/daemon/source/external/unbound/libunbound/context.c:106:2: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/libunbound/context.c: In function ‘context_new’:
/files/daemon/source/external/unbound/libunbound/context.c:136:3: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/libunbound/context.c:146:3: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/libunbound/context.c:151:3: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/libunbound/context.c: In function ‘context_deserialize_new_query’:
/files/daemon/source/external/unbound/libunbound/context.c:238:3: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/libunbound/context.c:247:3: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/libunbound/context.c:254:3: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
[ 58%] Building C object external/unbound/CMakeFiles/unbound.dir/libunbound/libunbound.c.o
In file included from /files/daemon/source/external/unbound/libunbound/libunbound.c:47:0:
/files/daemon/source/build/release/external/unbound/config.h:754:0: warning: "NDEBUG" redefined [enabled by default]
<command-line>:0:0: note: this is the location of the previous definition
/files/daemon/source/external/unbound/libunbound/libunbound.c: In function ‘ub_ctx_create_nopipe’:
/files/daemon/source/external/unbound/libunbound/libunbound.c:105:3: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/libunbound/libunbound.c:116:3: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/libunbound/libunbound.c:122:3: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/libunbound/libunbound.c: In function ‘ub_ctx_create’:
/files/daemon/source/external/unbound/libunbound/libunbound.c:147:3: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/libunbound/libunbound.c:158:3: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/libunbound/libunbound.c: In function ‘ub_stop_bg’:
/files/daemon/source/external/unbound/libunbound/libunbound.c:206:5: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/libunbound/libunbound.c:209:4: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/libunbound/libunbound.c: In function ‘ub_ctx_delete’:
/files/daemon/source/external/unbound/libunbound/libunbound.c:256:3: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/libunbound/libunbound.c:270:3: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/libunbound/libunbound.c:275:2: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/libunbound/libunbound.c: In function ‘ub_ctx_add_ta’:
/files/daemon/source/external/unbound/libunbound/libunbound.c:334:3: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/libunbound/libunbound.c:339:3: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/libunbound/libunbound.c: In function ‘ub_ctx_add_ta_file’:
/files/daemon/source/external/unbound/libunbound/libunbound.c:354:3: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/libunbound/libunbound.c:359:3: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/libunbound/libunbound.c: In function ‘ub_ctx_add_ta_autr’:
/files/daemon/source/external/unbound/libunbound/libunbound.c:373:3: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/libunbound/libunbound.c:379:3: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/libunbound/libunbound.c: In function ‘ub_ctx_trustedkeys’:
/files/daemon/source/external/unbound/libunbound/libunbound.c:394:3: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/libunbound/libunbound.c:399:3: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/libunbound/libunbound.c: In function ‘ub_process’:
/files/daemon/source/external/unbound/libunbound/libunbound.c:557:4: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/libunbound/libunbound.c:560:3: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/libunbound/libunbound.c: In function ‘ub_wait’:
/files/daemon/source/external/unbound/libunbound/libunbound.c:607:4: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/libunbound/libunbound.c: In function ‘ub_resolve_async’:
/files/daemon/source/external/unbound/libunbound/libunbound.c:757:3: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/libunbound/libunbound.c:761:2: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/libunbound/libunbound.c: In function ‘ub_cancel’:
/files/daemon/source/external/unbound/libunbound/libunbound.c:795:4: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/libunbound/libunbound.c:799:3: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/libunbound/libunbound.c: In function ‘ub_resolve_free’:
/files/daemon/source/external/unbound/libunbound/libunbound.c:811:2: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/libunbound/libunbound.c: In function ‘ub_ctx_set_fwd’:
/files/daemon/source/external/unbound/libunbound/libunbound.c:888:4: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/libunbound/libunbound.c:906:3: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/libunbound/libunbound.c: In function ‘ub_ctx_hosts’:
/files/daemon/source/external/unbound/libunbound/libunbound.c:1096:5: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/libunbound/libunbound.c: In function ‘ub_ctx_zone_add’:
/files/daemon/source/external/unbound/libunbound/libunbound.c:1159:3: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/libunbound/libunbound.c: In function ‘ub_ctx_zone_remove’:
/files/daemon/source/external/unbound/libunbound/libunbound.c:1193:2: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
/files/daemon/source/external/unbound/libunbound/libunbound.c: In function ‘ub_ctx_data_remove’:
/files/daemon/source/external/unbound/libunbound/libunbound.c:1222:2: warning: incompatible implicit declaration of built-in function ‘free’ [enabled by default]
[ 58%] Building C object external/unbound/CMakeFiles/unbound.dir/libunbound/libworker.c.o
In file included from /files/daemon/source/external/unbound/libunbound/libworker.c:44:0:
/files/daemon/source/build/release/external/unbound/config.h:754:0: warning: "NDEBUG" redefined [enabled by default]
<command-line>:0:0: note: this is the location of the previous definition
Linking C static library libunbound.a
make[3]: Leaving directory `/files/daemon/source/build/release'
[ 58%] Built target unbound
make[3]: Entering directory `/files/daemon/source/build/release'
Scanning dependencies of target lmdb
make[3]: Leaving directory `/files/daemon/source/build/release'
make[3]: Entering directory `/files/daemon/source/build/release'
[ 59%] Building C object external/db_drivers/liblmdb64/CMakeFiles/lmdb.dir/mdb.c.o
[ 59%] Building C object external/db_drivers/liblmdb64/CMakeFiles/lmdb.dir/midl.c.o
Linking C static library liblmdb.a
make[3]: Leaving directory `/files/daemon/source/build/release'
[ 59%] Built target lmdb
make[3]: Entering directory `/files/daemon/source/build/release'
Scanning dependencies of target otshell_utils
make[3]: Leaving directory `/files/daemon/source/build/release'
make[3]: Entering directory `/files/daemon/source/build/release'
[ 59%] Building CXX object contrib/otshell_utils/CMakeFiles/otshell_utils.dir/windows_stream.cpp.o
[ 60%] Building CXX object contrib/otshell_utils/CMakeFiles/otshell_utils.dir/runoptions.cpp.o
[ 61%] Building CXX object contrib/otshell_utils/CMakeFiles/otshell_utils.dir/utils.cpp.o
[ 61%] Building CXX object contrib/otshell_utils/CMakeFiles/otshell_utils.dir/ccolor.cpp.o
Linking CXX static library libotshell_utils.a
make[3]: Leaving directory `/files/daemon/source/build/release'
[ 61%] Built target otshell_utils
make[3]: Entering directory `/files/daemon/source/build/release'
Scanning dependencies of target crypto
make[3]: Leaving directory `/files/daemon/source/build/release'
make[3]: Entering directory `/files/daemon/source/build/release'
[ 62%] Building C object src/crypto/CMakeFiles/crypto.dir/aesb.c.o
[ 62%] Building C object src/crypto/CMakeFiles/crypto.dir/blake256.c.o
[ 63%] Building C object src/crypto/CMakeFiles/crypto.dir/chacha8.c.o
[ 64%] Building C object src/crypto/CMakeFiles/crypto.dir/crypto-ops-data.c.o
[ 64%] Building C object src/crypto/CMakeFiles/crypto.dir/crypto-ops.c.o
[ 65%] Building CXX object src/crypto/CMakeFiles/crypto.dir/crypto.cpp.o
[ 65%] Building C object src/crypto/CMakeFiles/crypto.dir/groestl.c.o
/files/daemon/source/src/crypto/groestl.c: In function ‘Init’:
/files/daemon/source/src/crypto/groestl.c:210:9: warning: comparison between signed and unsigned integer expressions [-Wsign-compare]
[ 66%] Building C object src/crypto/CMakeFiles/crypto.dir/hash-extra-blake.c.o
[ 67%] Building C object src/crypto/CMakeFiles/crypto.dir/hash-extra-groestl.c.o
[ 67%] Building C object src/crypto/CMakeFiles/crypto.dir/hash-extra-jh.c.o
[ 68%] Building C object src/crypto/CMakeFiles/crypto.dir/hash-extra-skein.c.o
[ 69%] Building C object src/crypto/CMakeFiles/crypto.dir/hash.c.o
[ 69%] Building C object src/crypto/CMakeFiles/crypto.dir/jh.c.o
[ 70%] Building C object src/crypto/CMakeFiles/crypto.dir/keccak.c.o
[ 70%] Building C object src/crypto/CMakeFiles/crypto.dir/oaes_lib.c.o
[ 71%] Building C object src/crypto/CMakeFiles/crypto.dir/random.c.o
[ 72%] Building C object src/crypto/CMakeFiles/crypto.dir/skein.c.o
/files/daemon/source/src/crypto/skein.c:80:5: warning: "SKEIN_256_NIST_MAX_HASH_BITS" is not defined [-Wundef]
/files/daemon/source/src/crypto/skein.c: In function ‘Skein_256_Final’:
/files/daemon/source/src/crypto/skein.c:1360:9: warning: dereferencing type-punned pointer will break strict-aliasing rules [-Wstrict-aliasing]
/files/daemon/source/src/crypto/skein.c: In function ‘Skein_512_Final’:
/files/daemon/source/src/crypto/skein.c:1560:9: warning: dereferencing type-punned pointer will break strict-aliasing rules [-Wstrict-aliasing]
/files/daemon/source/src/crypto/skein.c: In function ‘Skein1024_Final’:
/files/daemon/source/src/crypto/skein.c:1758:9: warning: dereferencing type-punned pointer will break strict-aliasing rules [-Wstrict-aliasing]
/files/daemon/source/src/crypto/skein.c: In function ‘Init’:
/files/daemon/source/src/crypto/skein.c:1944:5: warning: "SKEIN_256_NIST_MAX_HASH_BITS" is not defined [-Wundef]
[ 72%] Building C object src/crypto/CMakeFiles/crypto.dir/slow-hash.c.o
/files/daemon/source/src/crypto/slow-hash.c: In function ‘cn_slow_hash’:
/files/daemon/source/src/crypto/slow-hash.c:555:5: warning: dereferencing type-punned pointer will break strict-aliasing rules [-Wstrict-aliasing]
/files/daemon/source/src/crypto/slow-hash.c:555:5: warning: dereferencing type-punned pointer will break strict-aliasing rules [-Wstrict-aliasing]
/files/daemon/source/src/crypto/slow-hash.c:556:5: warning: dereferencing type-punned pointer will break strict-aliasing rules [-Wstrict-aliasing]
/files/daemon/source/src/crypto/slow-hash.c:556:5: warning: dereferencing type-punned pointer will break strict-aliasing rules [-Wstrict-aliasing]
/files/daemon/source/src/crypto/slow-hash.c:557:5: warning: dereferencing type-punned pointer will break strict-aliasing rules [-Wstrict-aliasing]
/files/daemon/source/src/crypto/slow-hash.c:557:5: warning: dereferencing type-punned pointer will break strict-aliasing rules [-Wstrict-aliasing]
/files/daemon/source/src/crypto/slow-hash.c:558:5: warning: dereferencing type-punned pointer will break strict-aliasing rules [-Wstrict-aliasing]
/files/daemon/source/src/crypto/slow-hash.c:558:5: warning: dereferencing type-punned pointer will break strict-aliasing rules [-Wstrict-aliasing]
[ 73%] Building C object src/crypto/CMakeFiles/crypto.dir/tree-hash.c.o
Linking CXX static library libcrypto.a
make[3]: Leaving directory `/files/daemon/source/build/release'
[ 73%] Built target crypto
make[3]: Entering directory `/files/daemon/source/build/release'
Scanning dependencies of target common
make[3]: Leaving directory `/files/daemon/source/build/release'
make[3]: Entering directory `/files/daemon/source/build/release'
[ 74%] Building CXX object src/common/CMakeFiles/common.dir/base58.cpp.o
[ 74%] Building CXX object src/common/CMakeFiles/common.dir/command_line.cpp.o
[ 75%] Building CXX object src/common/CMakeFiles/common.dir/dns_utils.cpp.o
[ 75%] Building CXX object src/common/CMakeFiles/common.dir/util.cpp.o
Linking CXX static library libcommon.a
make[3]: Leaving directory `/files/daemon/source/build/release'
[ 75%] Built target common
make[3]: Entering directory `/files/daemon/source/build/release'
Scanning dependencies of target blockchain_db
make[3]: Leaving directory `/files/daemon/source/build/release'
make[3]: Entering directory `/files/daemon/source/build/release'
[ 76%] Building CXX object src/blockchain_db/CMakeFiles/blockchain_db.dir/blockchain_db.cpp.o
In file included from /files/daemon/source/src/blockchain_db/blockchain_db.cpp:29:0:
/files/daemon/source/src/blockchain_db/blockchain_db.h:153:13: error: looser throw specifier for ‘virtual cryptonote::DB_EXCEPTION::~DB_EXCEPTION()’
In file included from /usr/include/c++/4.7/new:42:0,
                 from /usr/include/c++/4.7/ext/new_allocator.h:34,
                 from /usr/include/c++/4.7/x86_64-linux-gnu/bits/c++allocator.h:34,
                 from /usr/include/c++/4.7/bits/allocator.h:48,
                 from /usr/include/c++/4.7/list:62,
                 from /files/daemon/source/src/blockchain_db/blockchain_db.h:31,
                 from /files/daemon/source/src/blockchain_db/blockchain_db.cpp:29:
/usr/include/c++/4.7/exception:66:13: error:   overriding ‘virtual std::exception::~exception() noexcept (true)’
make[3]: *** [src/blockchain_db/CMakeFiles/blockchain_db.dir/blockchain_db.cpp.o] Error 1
make[3]: Leaving directory `/files/daemon/source/build/release'
make[2]: *** [src/blockchain_db/CMakeFiles/blockchain_db.dir/all] Error 2
make[2]: Leaving directory `/files/daemon/source/build/release'
make[1]: *** [all] Error 2
make[1]: Leaving directory `/files/daemon/source/build/release'
make: *** [release-static-64] Error 2
```


# Discussion History
## swalecko | 2015-08-17T14:32:56+00:00
Hi, I got the same error, i took the last master branch


## fluffypony | 2015-08-17T18:36:53+00:00
@swalecko what version of gcc? Wheezy is a complete pain because there are so many really old dependencies in by default, so you might find yourself having to install a number of things from source.


## swalecko | 2015-08-17T20:47:18+00:00
@fluffypony gcc version is 4.7.2 (Debian 4.7.2-5)


## fluffypony | 2015-08-17T21:25:09+00:00
@swalecko the minimum required version, per the README, is 4.7.3 - just to make certain do you want to try with a more recent version like 4.8?


## swalecko | 2015-08-18T06:35:23+00:00
@fluffypony  thanks a lot, i will try with 4.8 ;-)


## swalecko | 2015-08-18T20:13:36+00:00
@fluffypony Yeah, now it works!! The changes are really amazing!! Great work!!


## fluffypony | 2015-08-18T20:29:04+00:00
Awesome - closing this issue, then, thanks for updating us!


# Action History
- Created by: diesisbit | 2015-06-03T19:34:04+00:00
- Closed at: 2015-08-18T20:29:04+00:00
