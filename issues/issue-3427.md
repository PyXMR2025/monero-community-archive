---
title: About  tag of Monero V7 release
source_url: https://github.com/monero-project/monero/issues/3427
author: netmebtc
assignees: []
labels:
- invalid
created_at: '2018-03-18T01:59:28+00:00'
updated_at: '2018-03-28T00:08:46+00:00'
type: issue
status: closed
closed_at: '2018-03-28T00:08:46+00:00'
---

# Original Description
xmr-stak‘s  auther said that you should release a offcial tag of Monero V7 POW,  otherwise they will not release a cryptonightV7 version for cpu and gpu miner.

What a  tag is ?   You and xmr-stak's auther ignore all of the cpu and gpu miners ， each shirk wrangling with each other?

https://github.com/fireice-uk/xmr-stak/issues/1163#issuecomment-373930158
https://github.com/fireice-uk/xmr-stak/issues/1160#issuecomment-373966408

# Discussion History
## netmebtc | 2018-03-18T02:01:33+00:00
I beg you release that  tag as as soon as possible，please！

## moneromooo-monero | 2018-03-18T09:22:38+00:00
A tag will be made very soon. We're not ignoring miners, whether cpu or gpu. Patches were made for most of the miners (we knew of).

## fireice-uk | 2018-03-18T11:45:50+00:00
Thanks! As you can see having such a major change without finalising the release code is getting everyone nervous.

## moneromooo-monero | 2018-03-18T13:45:11+00:00
The fork was pushed to the 6th for that reason (1546000). The need to add mitigations for the key reusing fork pushed a lot of work needing doing for the release too. Ah well. Maybe next time will be on time.

## netmebtc | 2018-03-19T00:53:47+00:00
hi @moneromooo-monero  and  @fireice-uk . I am very glad to see that your  consideration of all cpu and gpu miners. hope a very perfect and offcial  release version soon before 28 march. Thank you very much!

## sx5486510 | 2018-03-19T02:31:35+00:00
Is that mean, xmring 2.5 is not a release version?

## moneromooo-monero | 2018-03-19T09:02:00+00:00
The release-v0.12 branch is now on github.

## gituser | 2018-03-21T08:56:29+00:00
hi! how to build new version?

it doesn't recognize anymore `BOOST_ROOT` for some reason and trying to use system libboost which is in my case is 1.55 (on debian 8).

and in `/home/build/monero/boost/boost.build` I have Boost 1.62, it worked before just fine with `v0.11.1.0`

```
export BOOST_ROOT=/home/build/monero/boost/boost.build DEVELOPER_LOCAL_TOOLS=1
make release-static
```

also there is no release on github's release page - you've created a branch instead of the release.

## gituser | 2018-03-21T09:11:25+00:00
the new error for me is:

```
WARNING: Back-up your wallet if it exists within ./build!
This will destroy the build directory, continue (y/N)?: y
rm -rf build
mkdir -p build/release
cd build/release && cmake -D STATIC=ON -D ARCH="x86-64" -D BUILD_64=ON -D CMAKE_BUILD_TYPE=release ../.. && make
-- The C compiler identification is GNU 4.9.2
-- The CXX compiler identification is GNU 4.9.2
-- Check for working C compiler: /usr/bin/cc
-- Check for working C compiler: /usr/bin/cc -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working CXX compiler: /usr/bin/c++
-- Check for working CXX compiler: /usr/bin/c++ -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Building without build tag
-- Found: env DEVELOPER_LOCAL_TOOLS = 1
-- BOOST_IGNORE_SYSTEM_PATHS defaults to ON
-- Could not find DEVELOPER_LIBUNBOUND_OLD in env (not required)
-- Building for a 64-bit system
-- Building internal libraries as static
-- Could not find DATABASE in env (not required unless you want to change database type from default: lmdb)
-- Using LMDB as default DB type
-- Stack trace on exception enabled (using easylogging++)
-- Looking for include file pthread.h
-- Looking for include file pthread.h - found
-- Looking for pthread_create
-- Looking for pthread_create - not found
-- Looking for pthread_create in pthreads
-- Looking for pthread_create in pthreads - not found
-- Looking for pthread_create in pthread
-- Looking for pthread_create in pthread - found
-- Found Threads: TRUE  
-- Found OpenSSL: /usr/lib/x86_64-linux-gnu/libssl.a;/usr/lib/x86_64-linux-gnu/libcrypto.a (found version "1.0.1t") 
-- Using OpenSSL include dir at /usr/include
-- Found PkgConfig: /usr/bin/pkg-config (found version "0.28") 
-- checking for module 'libpcsclite'
--   package 'libpcsclite' not found
-- Could NOT find PCSC (missing:  PCSC_LIBRARY PCSC_INCLUDE_DIR) 
-- Looking for memset_s in c
-- Looking for memset_s in c - not found
-- Looking for explicit_bzero in c
-- Looking for explicit_bzero in c - not found
-- Looking for strptime
-- Looking for strptime - found
-- Found MiniUPnPc: /usr/include/miniupnpc  
-- Found miniupnpc API version 10
-- Using miniupnpc from local source tree for static build
-- Looking for libunbound
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
-- Looking for sk_SSL_COMP_pop_free - found
-- Looking for SSL_COMP_get_compression_methods
-- Looking for SSL_COMP_get_compression_methods - not found
-- Looking for EVP_MD_CTX_new
-- Looking for EVP_MD_CTX_new - not found
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
-- Looking for LIBRESSL_VERSION_TEXT
-- Looking for LIBRESSL_VERSION_TEXT - not found
-- Using 64-bit LMDB from source tree
-- Building on x86_64 for x86-64
-- Performing Test _Wformat_c
-- Performing Test _Wformat_c - Success
-- Performing Test _Wformat_cxx
-- Performing Test _Wformat_cxx - Success
-- Performing Test _Wformat_security_c
-- Performing Test _Wformat_security_c - Success
-- Performing Test _Wformat_security_cxx
-- Performing Test _Wformat_security_cxx - Success
-- Performing Test _fstack_protector_c
-- Performing Test _fstack_protector_c - Success
-- Performing Test _fstack_protector_cxx
-- Performing Test _fstack_protector_cxx - Success
-- Performing Test _fstack_protector_strong_c
-- Performing Test _fstack_protector_strong_c - Success
-- Performing Test _fstack_protector_strong_cxx
-- Performing Test _fstack_protector_strong_cxx - Success
-- Looking for -pie linker flag
-- Looking for -pie linker flag - found
-- Looking for -Wl,-z,relro linker flag
-- Looking for -Wl,-z,relro linker flag - found
-- Looking for -Wl,-z,now linker flag
-- Looking for -Wl,-z,now linker flag - found
-- Looking for -Wl,-z,noexecstack linker flag
-- Looking for -Wl,-z,noexecstack linker flag - found
-- Looking for -Wl,-z,noexecheap linker flag
-- Looking for -Wl,-z,noexecheap linker flag - not found
-- Using C security hardening flags:  -Wformat -Wformat-security -fstack-protector -fstack-protector-strong
-- Using C++ security hardening flags:  -Wformat -Wformat-security -fstack-protector -fstack-protector-strong
-- Using linker security hardening flags:  -pie -Wl,-z,relro -Wl,-z,now -Wl,-z,noexecstack
-- AES support enabled
-- Found Boost Version: 106200
-- Found Readline: /usr/include  
-- Looking for rl_copy_text
-- Looking for rl_copy_text - not found
-- Looking for rl_filename_completion_function
-- Looking for rl_filename_completion_function - not found
-- Looking for rl_copy_text
-- Looking for rl_copy_text - found
-- Looking for rl_filename_completion_function
-- Looking for rl_filename_completion_function - found
-- Found readline library at: /usr
-- Found Git: /usr/bin/git
-- Found Doxygen: /usr/bin/doxygen (found version "1.8.8") 
-- Performing Test HAVE_C11
-- Performing Test HAVE_C11 - Success
-- Configuring done
CMake Error at src/CMakeLists.txt:98 (add_library):
  Cannot find source file:

    /home/build/monero/source/build/release/version.cpp

  Tried extensions .c .C .c++ .cc .cpp .cxx .m .M .mm .h .hh .h++ .hm .hpp
  .hxx .in .txx
Call Stack (most recent call first):
  src/CMakeLists.txt:86 (monero_add_library_with_deps)
  src/CMakeLists.txt:109 (monero_add_library)


-- Build files have been written to: /home/build/monero/source/build/release
Makefile:68: recipe for target 'release-static' failed
make: *** [release-static] Error 1
Build Failed.

```

## moneromooo-monero | 2018-03-21T11:23:57+00:00
Please file bugs in new issues, or it's going to be very confusing and hard to track.

## gituser | 2018-03-21T15:34:56+00:00
https://github.com/monero-project/monero/issues/3463

done, sorry for that!

## moneromooo-monero | 2018-03-25T11:38:59+00:00
For the record, a tag was made yesterday.

## moneromooo-monero | 2018-03-27T23:27:16+00:00
+invalid

# Action History
- Created by: netmebtc | 2018-03-18T01:59:28+00:00
- Closed at: 2018-03-28T00:08:46+00:00
