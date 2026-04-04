---
title: make debug fail
source_url: https://github.com/monero-project/monero/issues/2609
author: calvintam236
assignees: []
labels: []
created_at: '2017-10-08T22:30:39+00:00'
updated_at: '2017-10-08T23:23:09+00:00'
type: issue
status: closed
closed_at: '2017-10-08T23:08:04+00:00'
---

# Original Description
I tried to compile branch `release-v0.11.0.0` from source, and I encounter a make error.

Host: docker image - debian:latest

```console
$ make -j 4 debug
mkdir -p build/debug
cd build/debug && cmake -D CMAKE_BUILD_TYPE=Debug ../..
-- The C compiler identification is GNU 6.3.0
-- The CXX compiler identification is GNU 6.3.0
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
-- Building internal libraries with position independent code
-- Could not find DATABASE in env (not required unless you want to change database type from default: lmdb)
-- Using LMDB as default DB type
-- Stack trace on exception enabled
-- Found OpenSSL: /usr/lib/x86_64-linux-gnu/libssl.so;/usr/lib/x86_64-linux-gnu/libcrypto.so (found version "1.1.0f") 
-- Looking for pthread.h
-- Looking for pthread.h - found
-- Looking for pthread_create
-- Looking for pthread_create - not found
-- Check if compiler accepts -pthread
-- Check if compiler accepts -pthread - yes
-- Found Threads: TRUE  
-- Could NOT find MiniUPnPc (missing:  MINIUPNP_INCLUDE_DIR MINIUPNP_LIBRARY) 
-- Using miniupnpc from local source tree (/external/miniupnpc)
-- Looking for libunbound
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
-- Looking for pthread.h
-- Looking for pthread.h - found
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
-- Looking for strsep
-- Looking for strsep - found
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
-- Looking for EVP_MD_CTX_new
-- Looking for EVP_MD_CTX_new - found
-- Looking for EVP_sha1
-- Looking for EVP_sha1 - found
-- Looking for EVP_sha256
-- Looking for EVP_sha256 - found
-- Looking for EVP_sha512
-- Looking for EVP_sha512 - found
-- Looking for FIPS_mode
-- Looking for FIPS_mode - found
-- Looking for HMAC_Update
-- Looking for HMAC_Update - found
-- Looking for OPENSSL_config
-- Looking for OPENSSL_config - found
-- Looking for SHA512_Update
-- Looking for SHA512_Update - found
-- Found PkgConfig: /usr/bin/pkg-config (found version "0.29") 
-- Using 64-bit LMDB from source tree
-- Building on x86_64 for native
-- AES support enabled
-- Found Boost Version: 106200
-- Could NOT find Readline (missing:  Readline_INCLUDE_DIR Readline_LIBRARY) 
-- Performing Test GNU_READLINE_FOUND
-- Performing Test GNU_READLINE_FOUND - Failed
-- Could not find GNU readline library so building without readline support
-- Found Git: /usr/bin/git
Doxygen: graphviz not found - graphs disabled
-- Could NOT find Doxygen (missing:  DOXYGEN_EXECUTABLE) 
-- Configuring done
-- Generating done
-- Build files have been written to: /root/monero/build/debug
cd build/debug && make
make[1]: Entering directory '/root/monero/build/debug'
make[2]: Entering directory '/root/monero/build/debug'
make[3]: Entering directory '/root/monero/build/debug'
make[3]: Entering directory '/root/monero/build/debug'
make[3]: Entering directory '/root/monero/build/debug'
Scanning dependencies of target version
make[3]: Leaving directory '/root/monero/build/debug'
Scanning dependencies of target libminiupnpc-static
make[3]: Entering directory '/root/monero/build/debug'
Scanning dependencies of target lmdb
make[3]: Entering directory '/root/monero/build/debug'
make[3]: Leaving directory '/root/monero/build/debug'
make[3]: Leaving directory '/root/monero/build/debug'
make[3]: Entering directory '/root/monero/build/debug'
make[3]: Entering directory '/root/monero/build/debug'
Scanning dependencies of target unbound
[  1%] Generating version/version.h
[  1%] Building C object external/db_drivers/liblmdb/CMakeFiles/lmdb.dir/mdb.c.o
[  1%] Building C object external/miniupnpc/CMakeFiles/libminiupnpc-static.dir/igd_desc_parse.c.o
-- You are currently on commit 15b0ff2c
-- The most recent tag was at fda88c8d
-- You are ahead of or behind a tagged release
make[3]: Leaving directory '/root/monero/build/debug'
[  2%] Building C object external/miniupnpc/CMakeFiles/libminiupnpc-static.dir/miniupnpc.c.o
[  2%] Built target version
make[3]: Entering directory '/root/monero/build/debug'
make[3]: Leaving directory '/root/monero/build/debug'
Scanning dependencies of target easylogging
make[3]: Leaving directory '/root/monero/build/debug'
make[3]: Entering directory '/root/monero/build/debug'
make[3]: Entering directory '/root/monero/build/debug'
[  2%] Building C object external/unbound/CMakeFiles/unbound.dir/services/cache/dns.c.o
[  3%] Building CXX object external/easylogging++/CMakeFiles/easylogging.dir/easylogging++.cc.o
[  3%] Building C object external/miniupnpc/CMakeFiles/libminiupnpc-static.dir/minixml.c.o
[  4%] Building C object external/unbound/CMakeFiles/unbound.dir/services/cache/infra.c.o
[  5%] Building C object external/miniupnpc/CMakeFiles/libminiupnpc-static.dir/minisoap.c.o
[  5%] Building C object external/miniupnpc/CMakeFiles/libminiupnpc-static.dir/minissdpc.c.o
[  5%] Building C object external/unbound/CMakeFiles/unbound.dir/services/cache/rrset.c.o
[  6%] Building C object external/miniupnpc/CMakeFiles/libminiupnpc-static.dir/miniwget.c.o
[  7%] Building C object external/unbound/CMakeFiles/unbound.dir/util/data/dname.c.o
[  7%] Building C object external/miniupnpc/CMakeFiles/libminiupnpc-static.dir/upnpcommands.c.o
[  7%] Building C object external/db_drivers/liblmdb/CMakeFiles/lmdb.dir/midl.c.o
[  7%] Building C object external/unbound/CMakeFiles/unbound.dir/util/data/msgencode.c.o
[  7%] Building C object external/miniupnpc/CMakeFiles/libminiupnpc-static.dir/upnpdev.c.o
[  8%] Linking C shared library liblmdb.so
[  9%] Building C object external/miniupnpc/CMakeFiles/libminiupnpc-static.dir/upnpreplyparse.c.o
make[3]: Leaving directory '/root/monero/build/debug'
[  9%] Built target lmdb
make[3]: Entering directory '/root/monero/build/debug'
Scanning dependencies of target obj_cncrypto
[  9%] Building C object external/miniupnpc/CMakeFiles/libminiupnpc-static.dir/upnperrors.c.o
make[3]: Leaving directory '/root/monero/build/debug'
make[3]: Entering directory '/root/monero/build/debug'
[  9%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/aesb.c.o
[ 10%] Building C object external/miniupnpc/CMakeFiles/libminiupnpc-static.dir/connecthostport.c.o
[ 11%] Building C object external/unbound/CMakeFiles/unbound.dir/util/data/msgparse.c.o
[ 11%] Building C object external/miniupnpc/CMakeFiles/libminiupnpc-static.dir/portlistingparse.c.o
[ 12%] Building C object external/miniupnpc/CMakeFiles/libminiupnpc-static.dir/receivedata.c.o
[ 13%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/blake256.c.o
[ 13%] Building C object external/unbound/CMakeFiles/unbound.dir/util/data/msgreply.c.o
[ 13%] Linking C static library libminiupnpc.a
make[3]: Leaving directory '/root/monero/build/debug'
[ 13%] Built target libminiupnpc-static
make[3]: Entering directory '/root/monero/build/debug'
[ 13%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/chacha8.c.o
Scanning dependencies of target obj_common
make[3]: Leaving directory '/root/monero/build/debug'
make[3]: Entering directory '/root/monero/build/debug'
[ 14%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/crypto-ops-data.c.o
[ 14%] Building CXX object src/common/CMakeFiles/obj_common.dir/base58.cpp.o
[ 15%] Building C object external/unbound/CMakeFiles/unbound.dir/util/data/packed_rrset.c.o
[ 15%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/crypto-ops.c.o
[ 15%] Building C object external/unbound/CMakeFiles/unbound.dir/iterator/iterator.c.o
[ 16%] Building C object external/unbound/CMakeFiles/unbound.dir/iterator/iter_delegpt.c.o
[ 16%] Building C object external/unbound/CMakeFiles/unbound.dir/iterator/iter_donotq.c.o
[ 17%] Building C object external/unbound/CMakeFiles/unbound.dir/iterator/iter_fwd.c.o
[ 18%] Building CXX object src/crypto/CMakeFiles/obj_cncrypto.dir/crypto.cpp.o
[ 18%] Building C object external/unbound/CMakeFiles/unbound.dir/iterator/iter_hints.c.o
[ 18%] Building C object external/unbound/CMakeFiles/unbound.dir/iterator/iter_priv.c.o
[ 19%] Building C object external/unbound/CMakeFiles/unbound.dir/iterator/iter_resptype.c.o
[ 19%] Building C object external/unbound/CMakeFiles/unbound.dir/iterator/iter_scrub.c.o
[ 20%] Building C object external/unbound/CMakeFiles/unbound.dir/iterator/iter_utils.c.o
[ 20%] Building C object external/unbound/CMakeFiles/unbound.dir/respip/respip.c.o
[ 21%] Building CXX object src/common/CMakeFiles/obj_common.dir/command_line.cpp.o
[ 22%] Building C object external/unbound/CMakeFiles/unbound.dir/services/listen_dnsport.c.o
[ 22%] Building C object external/unbound/CMakeFiles/unbound.dir/services/localzone.c.o
[ 23%] Building C object external/unbound/CMakeFiles/unbound.dir/services/mesh.c.o
[ 23%] Building C object external/unbound/CMakeFiles/unbound.dir/services/modstack.c.o
[ 23%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/groestl.c.o
[ 24%] Building C object external/unbound/CMakeFiles/unbound.dir/services/outbound_list.c.o
[ 24%] Building C object external/unbound/CMakeFiles/unbound.dir/services/outside_network.c.o
[ 25%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/hash-extra-blake.c.o
[ 25%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/hash-extra-groestl.c.o
[ 26%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/hash-extra-jh.c.o
[ 26%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/hash-extra-skein.c.o
[ 27%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/hash.c.o
[ 27%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/jh.c.o
[ 28%] Building C object external/unbound/CMakeFiles/unbound.dir/services/view.c.o
[ 28%] Building C object external/unbound/CMakeFiles/unbound.dir/util/alloc.c.o
[ 29%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/keccak.c.o
[ 30%] Building C object external/unbound/CMakeFiles/unbound.dir/util/as112.c.o
[ 30%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/oaes_lib.c.o
[ 30%] Building C object external/unbound/CMakeFiles/unbound.dir/util/config_file.c.o
[ 30%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/random.c.o
[ 31%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/skein.c.o
[ 31%] Building C object external/unbound/CMakeFiles/unbound.dir/util/configlexer.c.o
[ 32%] Building C object external/unbound/CMakeFiles/unbound.dir/util/configparser.c.o
[ 32%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/slow-hash.c.o
[ 32%] Linking CXX shared library libeasylogging.so
[ 32%] Building C object external/unbound/CMakeFiles/unbound.dir/util/fptr_wlist.c.o
[ 33%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/tree-hash.c.o
make[3]: Leaving directory '/root/monero/build/debug'
[ 33%] Built target easylogging
make[3]: Leaving directory '/root/monero/build/debug'
[ 34%] Building C object external/unbound/CMakeFiles/unbound.dir/util/locks.c.o
[ 34%] Building CXX object src/common/CMakeFiles/obj_common.dir/dns_utils.cpp.o
[ 34%] Built target obj_cncrypto
make[3]: Entering directory '/root/monero/build/debug'
Scanning dependencies of target obj_ringct
make[3]: Leaving directory '/root/monero/build/debug'
make[3]: Entering directory '/root/monero/build/debug'
[ 34%] Building CXX object src/ringct/CMakeFiles/obj_ringct.dir/rctOps.cpp.o
[ 34%] Building C object external/unbound/CMakeFiles/unbound.dir/util/log.c.o
[ 35%] Building C object external/unbound/CMakeFiles/unbound.dir/util/mini_event.c.o
[ 35%] Building C object external/unbound/CMakeFiles/unbound.dir/util/module.c.o
[ 36%] Building C object external/unbound/CMakeFiles/unbound.dir/util/netevent.c.o
[ 36%] Building C object external/unbound/CMakeFiles/unbound.dir/util/net_help.c.o
[ 37%] Building C object external/unbound/CMakeFiles/unbound.dir/util/random.c.o
[ 37%] Building C object external/unbound/CMakeFiles/unbound.dir/util/rbtree.c.o
[ 38%] Building C object external/unbound/CMakeFiles/unbound.dir/util/regional.c.o
[ 38%] Building C object external/unbound/CMakeFiles/unbound.dir/util/rtt.c.o
[ 39%] Building C object external/unbound/CMakeFiles/unbound.dir/util/storage/dnstree.c.o
[ 39%] Building C object external/unbound/CMakeFiles/unbound.dir/util/storage/lookup3.c.o
[ 39%] Building C object external/unbound/CMakeFiles/unbound.dir/util/storage/lruhash.c.o
[ 40%] Building C object external/unbound/CMakeFiles/unbound.dir/util/storage/slabhash.c.o
[ 40%] Building C object external/unbound/CMakeFiles/unbound.dir/util/timehist.c.o
[ 41%] Building C object external/unbound/CMakeFiles/unbound.dir/util/tube.c.o
[ 41%] Building C object external/unbound/CMakeFiles/unbound.dir/util/ub_event.c.o
[ 42%] Building C object external/unbound/CMakeFiles/unbound.dir/util/winsock_event.c.o
[ 42%] Building C object external/unbound/CMakeFiles/unbound.dir/validator/autotrust.c.o
[ 43%] Building C object external/unbound/CMakeFiles/unbound.dir/validator/val_anchor.c.o
[ 43%] Building C object external/unbound/CMakeFiles/unbound.dir/validator/validator.c.o
[ 44%] Building C object external/unbound/CMakeFiles/unbound.dir/validator/val_kcache.c.o
[ 44%] Building C object external/unbound/CMakeFiles/unbound.dir/validator/val_kentry.c.o
[ 45%] Building C object external/unbound/CMakeFiles/unbound.dir/validator/val_neg.c.o
[ 45%] Building C object external/unbound/CMakeFiles/unbound.dir/validator/val_nsec3.c.o
[ 45%] Building C object external/unbound/CMakeFiles/unbound.dir/validator/val_nsec.c.o
[ 46%] Building C object external/unbound/CMakeFiles/unbound.dir/validator/val_secalgo.c.o
[ 47%] Building CXX object src/common/CMakeFiles/obj_common.dir/download.cpp.o
[ 47%] Building C object external/unbound/CMakeFiles/unbound.dir/validator/val_sigcrypt.c.o
[ 48%] Building C object external/unbound/CMakeFiles/unbound.dir/validator/val_utils.c.o
[ 48%] Building C object external/unbound/CMakeFiles/unbound.dir/dns64/dns64.c.o
[ 49%] Building C object external/unbound/CMakeFiles/unbound.dir/testcode/checklocks.c.o
[ 49%] Building C object external/unbound/CMakeFiles/unbound.dir/sldns/keyraw.c.o
[ 50%] Building C object external/unbound/CMakeFiles/unbound.dir/sldns/sbuffer.c.o
[ 50%] Building C object external/unbound/CMakeFiles/unbound.dir/sldns/wire2str.c.o
[ 51%] Building C object external/unbound/CMakeFiles/unbound.dir/sldns/parse.c.o
[ 51%] Building C object external/unbound/CMakeFiles/unbound.dir/sldns/parseutil.c.o
[ 52%] Building C object external/unbound/CMakeFiles/unbound.dir/sldns/rrdef.c.o
[ 52%] Building C object external/unbound/CMakeFiles/unbound.dir/sldns/str2wire.c.o
[ 53%] Building C object external/unbound/CMakeFiles/unbound.dir/compat/strlcat.c.o
[ 53%] Building C object external/unbound/CMakeFiles/unbound.dir/compat/strlcpy.c.o
[ 53%] Building C object external/unbound/CMakeFiles/unbound.dir/compat/explicit_bzero.c.o
[ 54%] Building C object external/unbound/CMakeFiles/unbound.dir/compat/arc4random.c.o
[ 54%] Building C object external/unbound/CMakeFiles/unbound.dir/compat/arc4random_uniform.c.o
[ 55%] Building C object external/unbound/CMakeFiles/unbound.dir/compat/reallocarray.c.o
[ 55%] Building C object external/unbound/CMakeFiles/unbound.dir/compat/arc4_lock.c.o
[ 56%] Building C object external/unbound/CMakeFiles/unbound.dir/compat/getentropy_linux.c.o
[ 56%] Building C object external/unbound/CMakeFiles/unbound.dir/libunbound/context.c.o
[ 57%] Building C object external/unbound/CMakeFiles/unbound.dir/libunbound/libunbound.c.o
[ 57%] Building C object external/unbound/CMakeFiles/unbound.dir/libunbound/libworker.c.o
[ 58%] Linking C shared library libunbound.so
make[3]: Leaving directory '/root/monero/build/debug'
[ 58%] Built target unbound
[ 58%] Building CXX object src/common/CMakeFiles/obj_common.dir/util.cpp.o
[ 59%] Building CXX object src/ringct/CMakeFiles/obj_ringct.dir/rctSigs.cpp.o
[ 59%] Building CXX object src/ringct/CMakeFiles/obj_ringct.dir/rctTypes.cpp.o
[ 60%] Building C object src/ringct/CMakeFiles/obj_ringct.dir/rctCryptoOps.c.o
[ 61%] Building CXX object src/common/CMakeFiles/obj_common.dir/i18n.cpp.o
/root/monero/src/common/download.cpp: In member function 'virtual bool tools::download_thread(tools::download_async_handle)::download_client::on_header(const epee::net_utils::http::http_response_info&)':
/root/monero/src/common/download.cpp:97:28: warning: 'length' may be used uninitialized in this function [-Wmaybe-uninitialized]
             content_length = length;
             ~~~~~~~~~~~~~~~^~~~~~~~
[ 61%] Building CXX object src/common/CMakeFiles/obj_common.dir/password.cpp.o
[ 62%] Building CXX object src/common/CMakeFiles/obj_common.dir/perf_timer.cpp.o
[ 62%] Building CXX object src/common/CMakeFiles/obj_common.dir/task_region.cpp.o
make[3]: Leaving directory '/root/monero/build/debug'
[ 62%] Built target obj_ringct
make[3]: Entering directory '/root/monero/build/debug'
Scanning dependencies of target obj_cryptonote_basic
make[3]: Leaving directory '/root/monero/build/debug'
make[3]: Entering directory '/root/monero/build/debug'
[ 63%] Building CXX object src/cryptonote_basic/CMakeFiles/obj_cryptonote_basic.dir/account.cpp.o
[ 64%] Building CXX object src/common/CMakeFiles/obj_common.dir/thread_group.cpp.o
make[3]: Entering directory '/root/monero/build/debug'
[ 64%] Generating testnet_blocks.o
[ 65%] Generating blocks.o
Scanning dependencies of target blocks
make[3]: Leaving directory '/root/monero/build/debug'
make[3]: Entering directory '/root/monero/build/debug'
[ 66%] Building C object src/blocks/CMakeFiles/blocks.dir/blockexports.c.o
[ 66%] Linking C static library libblocks.a
make[3]: Leaving directory '/root/monero/build/debug'
[ 66%] Built target blocks
make[3]: Entering directory '/root/monero/build/debug'
Scanning dependencies of target obj_cryptonote_core
make[3]: Leaving directory '/root/monero/build/debug'
make[3]: Entering directory '/root/monero/build/debug'
[ 66%] Building CXX object src/cryptonote_core/CMakeFiles/obj_cryptonote_core.dir/blockchain.cpp.o
[ 66%] Building CXX object src/common/CMakeFiles/obj_common.dir/updates.cpp.o
[ 67%] Building CXX object src/cryptonote_core/CMakeFiles/obj_cryptonote_core.dir/cryptonote_core.cpp.o
[ 67%] Building CXX object src/cryptonote_basic/CMakeFiles/obj_cryptonote_basic.dir/checkpoints.cpp.o
[ 67%] Building CXX object src/common/CMakeFiles/obj_common.dir/stack_trace.cpp.o
make[3]: Leaving directory '/root/monero/build/debug'
[ 67%] Built target obj_common
[ 68%] Building CXX object src/cryptonote_basic/CMakeFiles/obj_cryptonote_basic.dir/cryptonote_basic_impl.cpp.o
make[3]: Entering directory '/root/monero/build/debug'
Scanning dependencies of target obj_blockchain_db
make[3]: Leaving directory '/root/monero/build/debug'
make[3]: Entering directory '/root/monero/build/debug'
[ 69%] Building CXX object src/blockchain_db/CMakeFiles/obj_blockchain_db.dir/blockchain_db.cpp.o
[ 69%] Building CXX object src/cryptonote_basic/CMakeFiles/obj_cryptonote_basic.dir/cryptonote_format_utils.cpp.o
[ 69%] Building CXX object src/blockchain_db/CMakeFiles/obj_blockchain_db.dir/lmdb/db_lmdb.cpp.o
[ 70%] Building CXX object src/cryptonote_basic/CMakeFiles/obj_cryptonote_basic.dir/difficulty.cpp.o
[ 70%] Building CXX object src/cryptonote_basic/CMakeFiles/obj_cryptonote_basic.dir/hardfork.cpp.o
[ 71%] Building CXX object src/cryptonote_basic/CMakeFiles/obj_cryptonote_basic.dir/miner.cpp.o
[ 71%] Building CXX object src/cryptonote_core/CMakeFiles/obj_cryptonote_core.dir/tx_pool.cpp.o
[ 72%] Building CXX object src/cryptonote_core/CMakeFiles/obj_cryptonote_core.dir/cryptonote_tx_utils.cpp.o
make[3]: Leaving directory '/root/monero/build/debug'
[ 72%] Built target obj_blockchain_db
make[3]: Entering directory '/root/monero/build/debug'
Scanning dependencies of target obj_mnemonics
make[3]: Leaving directory '/root/monero/build/debug'
make[3]: Entering directory '/root/monero/build/debug'
[ 72%] Building CXX object src/mnemonics/CMakeFiles/obj_mnemonics.dir/electrum-words.cpp.o
make[3]: Entering directory '/root/monero/build/debug'
Scanning dependencies of target obj_rpc
make[3]: Leaving directory '/root/monero/build/debug'
make[3]: Entering directory '/root/monero/build/debug'
[ 72%] Building CXX object src/rpc/CMakeFiles/obj_rpc.dir/core_rpc_server.cpp.o
make[3]: Leaving directory '/root/monero/build/debug'
[ 72%] Built target obj_cryptonote_core
make[3]: Entering directory '/root/monero/build/debug'
Scanning dependencies of target obj_cryptonote_protocol
make[3]: Leaving directory '/root/monero/build/debug'
make[3]: Entering directory '/root/monero/build/debug'
[ 72%] Building CXX object src/cryptonote_protocol/CMakeFiles/obj_cryptonote_protocol.dir/block_queue.cpp.o
make[3]: Leaving directory '/root/monero/build/debug'
[ 72%] Built target obj_cryptonote_basic
make[3]: Entering directory '/root/monero/build/debug'
Scanning dependencies of target obj_p2p
make[3]: Leaving directory '/root/monero/build/debug'
make[3]: Entering directory '/root/monero/build/debug'
[ 73%] Building CXX object src/p2p/CMakeFiles/obj_p2p.dir/connection_basic.cpp.o
[ 73%] Building CXX object src/cryptonote_protocol/CMakeFiles/obj_cryptonote_protocol.dir/cryptonote_protocol_handler-base.cpp.o
make[3]: Leaving directory '/root/monero/build/debug'
[ 73%] Built target obj_mnemonics
make[3]: Entering directory '/root/monero/build/debug'
Scanning dependencies of target obj_wallet
make[3]: Leaving directory '/root/monero/build/debug'
make[3]: Entering directory '/root/monero/build/debug'
[ 73%] Building CXX object src/wallet/CMakeFiles/obj_wallet.dir/wallet2.cpp.o
[ 73%] Building CXX object src/p2p/CMakeFiles/obj_p2p.dir/network_throttle-detail.cpp.o
make[3]: Leaving directory '/root/monero/build/debug'
[ 73%] Built target obj_cryptonote_protocol
[ 74%] Building CXX object src/wallet/CMakeFiles/obj_wallet.dir/wallet_args.cpp.o
[ 74%] Building CXX object src/wallet/CMakeFiles/obj_wallet.dir/node_rpc_proxy.cpp.o
c++: internal compiler error: Killed (program cc1plus)
Please submit a full bug report,
with preprocessed source if appropriate.
See <file:///usr/share/doc/gcc-6/README.Bugs> for instructions.
src/rpc/CMakeFiles/obj_rpc.dir/build.make:62: recipe for target 'src/rpc/CMakeFiles/obj_rpc.dir/core_rpc_server.cpp.o' failed
make[3]: *** [src/rpc/CMakeFiles/obj_rpc.dir/core_rpc_server.cpp.o] Error 4
make[3]: Leaving directory '/root/monero/build/debug'
CMakeFiles/Makefile2:1239: recipe for target 'src/rpc/CMakeFiles/obj_rpc.dir/all' failed
make[2]: *** [src/rpc/CMakeFiles/obj_rpc.dir/all] Error 2
make[2]: *** Waiting for unfinished jobs....
[ 75%] Building CXX object src/p2p/CMakeFiles/obj_p2p.dir/network_throttle.cpp.o
[ 75%] Building CXX object src/wallet/CMakeFiles/obj_wallet.dir/api/wallet.cpp.o
make[3]: Leaving directory '/root/monero/build/debug'
[ 75%] Built target obj_p2p
[ 76%] Building CXX object src/wallet/CMakeFiles/obj_wallet.dir/api/wallet_manager.cpp.o
c++: internal compiler error: Killed (program cc1plus)
Please submit a full bug report,
with preprocessed source if appropriate.
See <file:///usr/share/doc/gcc-6/README.Bugs> for instructions.
src/wallet/CMakeFiles/obj_wallet.dir/build.make:62: recipe for target 'src/wallet/CMakeFiles/obj_wallet.dir/wallet2.cpp.o' failed
make[3]: *** [src/wallet/CMakeFiles/obj_wallet.dir/wallet2.cpp.o] Error 4
make[3]: *** Waiting for unfinished jobs....
make[3]: Leaving directory '/root/monero/build/debug'
CMakeFiles/Makefile2:1349: recipe for target 'src/wallet/CMakeFiles/obj_wallet.dir/all' failed
make[2]: *** [src/wallet/CMakeFiles/obj_wallet.dir/all] Error 2
make[2]: Leaving directory '/root/monero/build/debug'
Makefile:138: recipe for target 'all' failed
make[1]: *** [all] Error 2
make[1]: Leaving directory '/root/monero/build/debug'
Makefile:36: recipe for target 'debug' failed
make: *** [debug] Error 2
```

# Discussion History
## radfish | 2017-10-08T23:23:09+00:00
For future reference: probably ran out of RAM. Try with make -j2 or -j1 and/or add swap. Build may need up to ~2GB per thread in my experience.

# Action History
- Created by: calvintam236 | 2017-10-08T22:30:39+00:00
- Closed at: 2017-10-08T23:08:04+00:00
