---
title: Windows build gui.exe error
source_url: https://github.com/monero-project/monero-gui/issues/1455
author: ghost
assignees: []
labels: []
created_at: '2018-06-10T10:19:58+00:00'
updated_at: '2019-12-27T13:59:00+00:00'
type: issue
status: closed
closed_at: '2018-06-11T10:34:37+00:00'
---

# Original Description
Trying to compile the wallet gui, followed the simple guide correctly but I keep getting this build error.
Could anyone shed some light in resolving this compile error. I would imagine it has to do with missing .dll's possibly?

![image](https://user-images.githubusercontent.com/32077247/41200623-94539894-6ca8-11e8-9f60-8486779f5119.png)



# Discussion History
## stoffu | 2018-06-10T11:05:16+00:00
> ld.exe: cannot find -lwallet_merged

This message means there was something wrong when building the monero core library which is built with get_libwallet_api.sh which is internally called from build.sh. Run get_libwallet_api.sh separately and check the error message.


## ghost | 2018-06-10T12:27:25+00:00
After running get_libwallet_api.sh, im unable to source the error that is causing the root issue for the GUI.


```
$ ./get_libwallet_api.sh
~/monero-gui ~/monero-gui
Submodule path 'monero': checked out '25e7a7d96f2e46821d6613e6d2012b367dd70f38'
D       include/INode.h
D       include/IWallet.h
Previous HEAD position was 25e7a7d9 Merge pull request #3340
HEAD is now at e2c39f6b Merge pull request #3914
You are currently on commit d85f3ea
The most recent tag was at d85f3ea
You are building a tagged release
D       include/INode.h
D       include/IWallet.h
Switched to and reset branch 'release'
libwallet_merged.a not found - Building libwallet
Building libwallet release
cleaning up existing monero build dir, libs and includes
~/monero-gui/monero/build/release ~/monero-gui ~/monero-gui
Configuring build for MINGW64..
-- The C compiler identification is GNU 7.3.0
-- The CXX compiler identification is GNU 7.3.0
-- Check for working C compiler: C:/msys64/mingw64/bin/gcc.exe
-- Check for working C compiler: C:/msys64/mingw64/bin/gcc.exe -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Detecting C compile features
-- Detecting C compile features - done
-- Check for working CXX compiler: C:/msys64/mingw64/bin/g++.exe
-- Check for working CXX compiler: C:/msys64/mingw64/bin/g++.exe -- works
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
-- MSYS location: C:/msys64
-- Could not find DATABASE in env (not required unless you want to change database type from default: lmdb)
-- Using LMDB as default DB type
-- looking for liblzma
-- liblzma found
-- Could not find libunwind (missing: LIBUNWIND_INCLUDE_DIR)
-- Stack trace on exception disabled
-- Found OpenSSL: C:/msys64/mingw64/lib/libcrypto.a (found version "1.0.2o")
-- Using OpenSSL include dir at C:/msys64/mingw64/include
-- Found PCSC: /mingw64/x86_64-w64-mingw32/lib/libwinscard.a
-- Looking for memset_s in c
-- Looking for memset_s in c - not found
-- Looking for explicit_bzero in c
-- Looking for explicit_bzero in c - not found
-- Looking for strptime
-- Looking for strptime - not found
-- Could NOT find MiniUPnPc (missing: MINIUPNP_INCLUDE_DIR MINIUPNP_LIBRARY)
-- Using in-tree miniupnpc
-- Looking for libunbound
-- Looking for pthread.h
-- Looking for pthread.h - found
-- Looking for pthread_create
-- Looking for pthread_create - found
-- Found Threads: TRUE
-- Looking for arpa/inet.h
-- Looking for arpa/inet.h - not found
-- Looking for endian.h
-- Looking for endian.h - not found
-- Looking for dlfcn.h
-- Looking for dlfcn.h - not found
-- Looking for event.h
-- Looking for event.h - not found
-- Looking for getopt.h
-- Looking for getopt.h - found
-- Looking for glob.h
-- Looking for glob.h - not found
-- Looking for grp.h
-- Looking for grp.h - not found
-- Looking for inttypes.h
-- Looking for inttypes.h - found
-- Looking for iphlpapi.h
-- Looking for iphlpapi.h - found
-- Looking for login_cap.h
-- Looking for login_cap.h - not found
-- Looking for memory.h
-- Looking for memory.h - found
-- Looking for netdb.h
-- Looking for netdb.h - not found
-- Looking for netinet/in.h
-- Looking for netinet/in.h - not found
-- Looking for pthread.h
-- Looking for pthread.h - found
-- Looking for pwd.h
-- Looking for pwd.h - not found
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
-- Looking for sys/resource.h - not found
-- Looking for sys/sha2.h
-- Looking for sys/sha2.h - not found
-- Looking for sys/socket.h
-- Looking for sys/socket.h - not found
-- Looking for sys/stat.h
-- Looking for sys/stat.h - found
-- Looking for sys/sysctl.h
-- Looking for sys/sysctl.h - not found
-- Looking for sys/types.h
-- Looking for sys/types.h - found
-- Looking for sys/uio.h
-- Looking for sys/uio.h - not found
-- Looking for sys/un.h
-- Looking for sys/un.h - not found
-- Looking for sys/wait.h
-- Looking for sys/wait.h - not found
-- Looking for syslog.h
-- Looking for syslog.h - not found
-- Looking for time.h
-- Looking for time.h - found
-- Looking for unistd.h
-- Looking for unistd.h - found
-- Looking for vfork.h
-- Looking for vfork.h - not found
-- Looking for windows.h
-- Looking for windows.h - found
-- Looking for winsock2.h
-- Looking for winsock2.h - found
-- Looking for ws2tcpip.h
-- Looking for ws2tcpip.h - found
-- Looking for _beginthreadex
-- Looking for _beginthreadex - found
-- Looking for arc4random
-- Looking for arc4random - not found
-- Looking for arc4random_uniform
-- Looking for arc4random_uniform - not found
-- Looking for chown
-- Looking for chown - not found
-- Looking for chroot
-- Looking for chroot - not found
-- Looking for ctime_r
-- Looking for ctime_r - not found
-- Looking for daemon
-- Looking for daemon - not found
-- Looking for endprotoent
-- Looking for endprotoent - not found
-- Looking for endservent
-- Looking for endservent - not found
-- Looking for fork
-- Looking for fork - not found
-- Looking for fseeko
-- Looking for fseeko - found
-- Looking for fsync
-- Looking for fsync - not found
-- Looking for getauxval
-- Looking for getauxval - not found
-- Looking for getentropy
-- Looking for getentropy - not found
-- Looking for getpwnam
-- Looking for getpwnam - not found
-- Looking for getrlimit
-- Looking for getrlimit - not found
-- Looking for glob
-- Looking for glob - not found
-- Looking for gmtime_r
-- Looking for gmtime_r - not found
-- Looking for fcntl
-- Looking for fcntl - not found
-- Looking for inet_aton
-- Looking for inet_aton - not found
-- Looking for inet_ntop
-- Looking for inet_ntop - found
-- Looking for inet_pton
-- Looking for inet_pton - found
-- Looking for initgroups
-- Looking for initgroups - not found
-- Looking for ioctlsocket
-- Looking for ioctlsocket - found
-- Looking for isblank
-- Looking for isblank - found
-- Looking for kill
-- Looking for kill - not found
-- Looking for localtime_r
-- Looking for localtime_r - not found
-- Looking for malloc
-- Looking for malloc - found
-- Looking for memmove
-- Looking for memmove - found
-- Looking for random
-- Looking for random - not found
-- Looking for reallocarray
-- Looking for reallocarray - not found
-- Looking for recvmsg
-- Looking for recvmsg - not found
-- Looking for sbrk
-- Looking for sbrk - not found
-- Looking for sendmsg
-- Looking for sendmsg - not found
-- Looking for setregid
-- Looking for setregid - not found
-- Looking for setresgid
-- Looking for setresgid - not found
-- Looking for setresuid
-- Looking for setresuid - not found
-- Looking for setreuid
-- Looking for setreuid - not found
-- Looking for setrlimit
-- Looking for setrlimit - not found
-- Looking for setsid
-- Looking for setsid - not found
-- Looking for setusercontent
-- Looking for setusercontent - not found
-- Looking for sigprocmask
-- Looking for sigprocmask - not found
-- Looking for sleep
-- Looking for sleep - found
-- Looking for snprintf
-- Looking for snprintf - found
-- Looking for socketpair
-- Looking for socketpair - not found
-- Looking for srandom
-- Looking for srandom - not found
-- Looking for strsep
-- Looking for strsep - not found
-- Looking for strftime
-- Looking for strftime - found
-- Looking for strlcat
-- Looking for strlcat - not found
-- Looking for strlcpy
-- Looking for strlcpy - not found
-- Looking for strptime
-- Looking for strptime - not found
-- Looking for tzset
-- Looking for tzset - found
-- Looking for usleep
-- Looking for usleep - found
-- Looking for writev
-- Looking for writev - not found
-- Looking for getaddrinfo
-- Looking for getaddrinfo - found
-- Looking for stddef.h
-- Looking for stddef.h - found
-- Check size of time_t
-- Check size of time_t - done
-- Check size of gid_t
-- Check size of gid_t - failed
-- Check size of in_addr_t
-- Check size of in_addr_t - failed
-- Check size of in_port_t
-- Check size of in_port_t - failed
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
-- Check size of rlim_t - failed
-- Check size of ssize_t
-- Check size of ssize_t - done
-- Check size of uid_t
-- Check size of uid_t - failed
-- Check size of uint16_t
-- Check size of uint16_t - done
-- Check size of uint32_t
-- Check size of uint32_t - done
-- Check size of uint64_t
-- Check size of uint64_t - done
-- Check size of uint8_t
-- Check size of uint8_t - done
-- Looking for PTHREAD_PRIO_INHERIT
-- Looking for PTHREAD_PRIO_INHERIT - found
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
-- Using PCSC include dir at /mingw64/x86_64-w64-mingw32/include
-- Building on AMD64 for x86-64
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
-- Looking for -Wl,-z,relro linker flag
-- Looking for -Wl,-z,relro linker flag - not found
-- Looking for -Wl,-z,now linker flag
-- Looking for -Wl,-z,now linker flag - not found
-- Looking for -Wl,-z,noexecstack linker flag
-- Looking for -Wl,-z,noexecstack linker flag - not found
-- Looking for -Wl,-z,noexecheap linker flag
-- Looking for -Wl,-z,noexecheap linker flag - not found
-- Looking for -Wl,--dynamicbase linker flag
-- Looking for -Wl,--dynamicbase linker flag - found
-- Looking for -Wl,--nxcompat linker flag
-- Looking for -Wl,--nxcompat linker flag - found
-- Using C security hardening flags:  -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=1 -Wformat -Wformat-security -fstack-protector -fstack-protector-strong
-- Using C++ security hardening flags:  -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=1 -Wformat -Wformat-security -fstack-protector -fstack-protector-strong
-- Using linker security hardening flags:  -Wl,--dynamicbase -Wl,--nxcompat
-- AES support enabled
-- Found Boost Version: 106700
-- Could NOT find Readline (missing: Readline_INCLUDE_DIR)
-- Looking for rl_copy_text
-- Looking for rl_copy_text - not found
-- Looking for rl_filename_completion_function
-- Looking for rl_filename_completion_function - not found
-- Looking for rl_copy_text
-- Looking for rl_copy_text - found
-- Looking for rl_filename_completion_function
-- Looking for rl_filename_completion_function - found
-- Could not find GNU readline library so building without readline support
-- Found Git: C:/msys64/usr/bin/git.exe
Doxygen: graphviz not found - graphs disabled
-- Could NOT find Doxygen (missing: DOXYGEN_EXECUTABLE)
-- Performing Test HAVE_C11
-- Performing Test HAVE_C11 - Success
-- Configuring done
-- Generating done
-- Build files have been written to: C:/msys64/home/noobless_/monero-gui/monero/build/release
~/monero-gui/monero/build/release/src/wallet ~/monero-gui/monero/build/release ~/monero-gui ~/monero-gui
make: Entering directory '/home/noobless_/monero-gui/monero/build/release'
make[1]: Entering directory '/home/noobless_/monero-gui/monero/build/release'
make[2]: Entering directory '/home/noobless_/monero-gui/monero/build/release'
make[3]: Entering directory '/home/noobless_/monero-gui/monero/build/release'
Scanning dependencies of target genversion
make[3]: Leaving directory '/home/noobless_/monero-gui/monero/build/release'
make[3]: Entering directory '/home/noobless_/monero-gui/monero/build/release'
[  0%] Generating ../version.cpp
-- You are currently on commit e2c39f6b
-- The most recent tag was at e2c39f6b
-- You are building a tagged release
make[3]: Leaving directory '/home/noobless_/monero-gui/monero/build/release'
[  0%] Built target genversion
make[3]: Entering directory '/home/noobless_/monero-gui/monero/build/release'
Scanning dependencies of target obj_version
make[3]: Leaving directory '/home/noobless_/monero-gui/monero/build/release'
make[3]: Entering directory '/home/noobless_/monero-gui/monero/build/release'
[  0%] Building CXX object src/CMakeFiles/obj_version.dir/__/version.cpp.obj
make[3]: Leaving directory '/home/noobless_/monero-gui/monero/build/release'
[ 50%] Built target obj_version
make[3]: Entering directory '/home/noobless_/monero-gui/monero/build/release'
Scanning dependencies of target version
make[3]: Leaving directory '/home/noobless_/monero-gui/monero/build/release'
make[3]: Entering directory '/home/noobless_/monero-gui/monero/build/release'
[100%] Linking CXX static library libversion.a
make[3]: Leaving directory '/home/noobless_/monero-gui/monero/build/release'
[100%] Built target version
make[2]: Leaving directory '/home/noobless_/monero-gui/monero/build/release'
make[1]: Leaving directory '/home/noobless_/monero-gui/monero/build/release'
make: Leaving directory '/home/noobless_/monero-gui/monero/build/release'
Scanning dependencies of target easylogging
[  0%] Building CXX object external/easylogging++/CMakeFiles/easylogging.dir/easylogging++.cc.obj
Scanning dependencies of target obj_device
Scanning dependencies of target unbound
[  1%] Building C object external/unbound/CMakeFiles/unbound.dir/services/authzone.c.obj
[  2%] Building CXX object src/device/CMakeFiles/obj_device.dir/device.cpp.obj
Scanning dependencies of target obj_wallet
[  2%] Building CXX object src/wallet/CMakeFiles/obj_wallet.dir/wallet2.cpp.obj
[  2%] Building C object external/unbound/CMakeFiles/unbound.dir/services/cache/dns.c.obj
[  2%] Building C object external/unbound/CMakeFiles/unbound.dir/services/cache/infra.c.obj
[  2%] Building CXX object src/device/CMakeFiles/obj_device.dir/device_default.cpp.obj
[  3%] Building C object external/unbound/CMakeFiles/unbound.dir/services/cache/rrset.c.obj
[  3%] Building C object external/unbound/CMakeFiles/unbound.dir/util/data/dname.c.obj
[  3%] Linking CXX static library libeasylogging.a
[  3%] Built target easylogging
Scanning dependencies of target obj_cncrypto
[  5%] Building C object external/unbound/CMakeFiles/unbound.dir/util/data/msgencode.c.obj
[  5%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/aesb.c.obj
[  5%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/blake256.c.obj
[  6%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/chacha.c.obj
[  6%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/crypto-ops-data.c.obj
[  7%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/crypto-ops.c.obj
[  7%] Building C object external/unbound/CMakeFiles/unbound.dir/util/data/msgparse.c.obj
[  7%] Building C object external/unbound/CMakeFiles/unbound.dir/util/data/msgreply.c.obj
[  7%] Building CXX object src/crypto/CMakeFiles/obj_cncrypto.dir/crypto.cpp.obj
[  7%] Building CXX object src/device/CMakeFiles/obj_device.dir/log.cpp.obj
[  9%] Building C object external/unbound/CMakeFiles/unbound.dir/util/data/packed_rrset.c.obj
[  9%] Building C object external/unbound/CMakeFiles/unbound.dir/iterator/iterator.c.obj
[  9%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/groestl.c.obj
[ 10%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/hash-extra-blake.c.obj
[ 10%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/hash-extra-groestl.c.obj
[ 10%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/hash-extra-jh.c.obj
[ 10%] Building C object external/unbound/CMakeFiles/unbound.dir/iterator/iter_delegpt.c.obj
[ 11%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/hash-extra-skein.c.obj
[ 11%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/hash.c.obj
[ 12%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/jh.c.obj
[ 12%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/keccak.c.obj
[ 14%] Building C object external/unbound/CMakeFiles/unbound.dir/iterator/iter_donotq.c.obj
[ 14%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/oaes_lib.c.obj
[ 15%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/random.c.obj
[ 15%] Building C object external/unbound/CMakeFiles/unbound.dir/iterator/iter_fwd.c.obj
[ 15%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/skein.c.obj
[ 16%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/slow-hash.c.obj
[ 18%] Building CXX object src/device/CMakeFiles/obj_device.dir/device_ledger.cpp.obj
[ 19%] Building C object external/unbound/CMakeFiles/unbound.dir/iterator/iter_hints.c.obj
[ 19%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/tree-hash.c.obj
[ 19%] Built target obj_cncrypto
Scanning dependencies of target generate_translations_header
[ 19%] Creating directories for 'generate_translations_header'
[ 19%] Building C object external/unbound/CMakeFiles/unbound.dir/iterator/iter_priv.c.obj
[ 19%] No download step for 'generate_translations_header'
[ 19%] No patch step for 'generate_translations_header'
[ 20%] No update step for 'generate_translations_header'
[ 22%] Building C object external/unbound/CMakeFiles/unbound.dir/iterator/iter_resptype.c.obj
[ 22%] Performing configure step for 'generate_translations_header'
-- The C compiler identification is GNU 7.3.0
-- The CXX compiler identification is GNU 7.3.0
-- Check for working C compiler: C:/msys64/mingw64/bin/gcc.exe
[ 23%] Building C object external/unbound/CMakeFiles/unbound.dir/iterator/iter_scrub.c.obj
-- Check for working C compiler: C:/msys64/mingw64/bin/gcc.exe -- works
-- Detecting C compiler ABI info
[ 23%] Building C object external/unbound/CMakeFiles/unbound.dir/iterator/iter_utils.c.obj
-- Detecting C compiler ABI info - done
-- Detecting C compile features
[ 23%] Building C object external/unbound/CMakeFiles/unbound.dir/respip/respip.c.obj
[ 24%] Building C object external/unbound/CMakeFiles/unbound.dir/services/listen_dnsport.c.obj
C:/msys64/home/noobless_/monero-gui/monero/external/unbound/services/listen_dnsport.c: In function 'verbose_print_addr':
C:/msys64/home/noobless_/monero-gui/monero/external/unbound/services/listen_dnsport.c:88:6: warning: implicit declaration of function 'inet_ntop'; did you mean 'inet_ntoa'? [-Wimplicit-function-declaration]
   if(inet_ntop(addr->ai_family, sinaddr, buf,
      ^~~~~~~~~
      inet_ntoa
[ 24%] Building C object external/unbound/CMakeFiles/unbound.dir/services/localzone.c.obj
[ 24%] Built target obj_device
Scanning dependencies of target obj_ringct_basic
-- Detecting C compile features - done
-- Check for working CXX compiler: C:/msys64/mingw64/bin/g++.exe
[ 25%] Building CXX object src/ringct/CMakeFiles/obj_ringct_basic.dir/rctOps.cpp.obj
[ 27%] Building C object external/unbound/CMakeFiles/unbound.dir/services/mesh.c.obj
-- Check for working CXX compiler: C:/msys64/mingw64/bin/g++.exe -- works
-- Detecting CXX compiler ABI info
[ 27%] Building C object external/unbound/CMakeFiles/unbound.dir/services/modstack.c.obj
-- Detecting CXX compiler ABI info - done
-- Detecting CXX compile features
[ 27%] Building C object external/unbound/CMakeFiles/unbound.dir/services/outbound_list.c.obj
[ 28%] Building C object external/unbound/CMakeFiles/unbound.dir/services/outside_network.c.obj
[ 28%] Building CXX object src/ringct/CMakeFiles/obj_ringct_basic.dir/rctTypes.cpp.obj
[ 28%] Building C object external/unbound/CMakeFiles/unbound.dir/services/view.c.obj
[ 29%] Building C object external/unbound/CMakeFiles/unbound.dir/util/alloc.c.obj
[ 29%] Building C object external/unbound/CMakeFiles/unbound.dir/util/as112.c.obj
[ 29%] Building C object external/unbound/CMakeFiles/unbound.dir/util/config_file.c.obj
[ 29%] Building C object src/ringct/CMakeFiles/obj_ringct_basic.dir/rctCryptoOps.c.obj
[ 31%] Building CXX object src/ringct/CMakeFiles/obj_ringct_basic.dir/bulletproofs.cc.obj
-- Detecting CXX compile features - done
lrelease version 5.10.1
-- Configuring done
-- Generating done
-- Build files have been written to: C:/msys64/home/noobless_/monero-gui/monero/build/release/translations
In file included from C:/msys64/home/noobless_/monero-gui/monero/external/easylogging++/easylogging++.h:375:0,
                 from C:/msys64/home/noobless_/monero-gui/monero/contrib/epee/include/misc_log_ex.h:33,
                 from C:/msys64/home/noobless_/monero-gui/monero/src/ringct/bulletproofs.cc:34:
C:/msys64/mingw64/x86_64-w64-mingw32/include/winsock2.h:15:2: warning: #warning Please include winsock2.h before windows.h [-Wcpp]
 #warning Please include winsock2.h before windows.h
  ^~~~~~~
[ 31%] Performing build step for 'generate_translations_header'
[ 32%] Building C object external/unbound/CMakeFiles/unbound.dir/util/configlexer.c.obj
Scanning dependencies of target generate_translations_header
[ 50%] Building C object CMakeFiles/generate_translations_header.dir/generate_translations_header.c.obj
[100%] Linking C executable generate_translations_header.exe
Updating 'monero.qm'...
    Generated 0 translation(s) (0 finished and 0 unfinished)
    Ignored 737 untranslated source text(s)
Updating 'monero_fr.qm'...
    Generated 737 translation(s) (737 finished and 0 unfinished)
Updating 'monero_it.qm'...
    Generated 380 translation(s) (376 finished and 4 unfinished)
    Ignored 357 untranslated source text(s)
Updating 'monero_sv.qm'...
    Generated 737 translation(s) (737 finished and 0 unfinished)
[ 32%] Building C object external/unbound/CMakeFiles/unbound.dir/util/configparser.c.obj
Generating embedded translations header
[ 32%] Building C object external/unbound/CMakeFiles/unbound.dir/util/fptr_wlist.c.obj
[100%] Built target generate_translations_header
[ 33%] Performing install step for 'generate_translations_header'

[ 33%] Completed 'generate_translations_header'
[ 33%] Built target generate_translations_header
[ 33%] Generating stagenet_blocks.o
[ 33%] Built target obj_ringct_basic
[ 35%] Building C object external/unbound/CMakeFiles/unbound.dir/util/locks.c.obj
[ 35%] Generating blocks.o
Scanning dependencies of target lmdb
[ 36%] Generating testnet_blocks.o
[ 36%] Building C object external/db_drivers/liblmdb/CMakeFiles/lmdb.dir/mdb.c.obj
Scanning dependencies of target blocks
[ 36%] Building C object src/blocks/CMakeFiles/blocks.dir/blockexports.c.obj
[ 37%] Linking C static library libblocks.a
[ 37%] Building C object external/unbound/CMakeFiles/unbound.dir/util/log.c.obj
[ 37%] Built target blocks
[ 37%] Built target genversion
C:/msys64/home/noobless_/monero-gui/monero/external/db_drivers/liblmdb/mdb.c: In function 'mdb_strerror':
cc1.exe: warning: function may return address of local variable [-Wreturn-local-addr]
C:/msys64/home/noobless_/monero-gui/monero/external/db_drivers/liblmdb/mdb.c:1584:7: note: declared here
  char buf[MSGSIZE+PADSIZE], *ptr = buf;
       ^~~
[ 38%] Building C object external/unbound/CMakeFiles/unbound.dir/util/mini_event.c.obj
Scanning dependencies of target obj_ringct
[ 38%] Building CXX object src/ringct/CMakeFiles/obj_ringct.dir/rctSigs.cpp.obj
[ 38%] Building C object external/db_drivers/liblmdb/CMakeFiles/lmdb.dir/midl.c.obj
[ 38%] Building C object external/unbound/CMakeFiles/unbound.dir/util/module.c.obj
[ 40%] Linking C static library liblmdb.a
[ 40%] Built target lmdb
[ 40%] Building C object external/unbound/CMakeFiles/unbound.dir/util/netevent.c.obj
Scanning dependencies of target obj_checkpoints
[ 41%] Building CXX object src/checkpoints/CMakeFiles/obj_checkpoints.dir/checkpoints.cpp.obj
[ 42%] Building C object external/unbound/CMakeFiles/unbound.dir/util/net_help.c.obj
C:/msys64/home/noobless_/monero-gui/monero/external/unbound/util/net_help.c: In function 'log_addr':
C:/msys64/home/noobless_/monero-gui/monero/external/unbound/util/net_help.c:162:10: warning: implicit declaration of function 'inet_ntop'; did you mean 'inet_ntoa'? [-Wimplicit-function-declaration]
    (void)inet_ntop(af, sinaddr, dest,
          ^~~~~~~~~
          inet_ntoa
C:/msys64/home/noobless_/monero-gui/monero/external/unbound/util/net_help.c: In function 'ipstrtoaddr':
C:/msys64/home/noobless_/monero-gui/monero/external/unbound/util/net_help.c:225:6: warning: implicit declaration of function 'inet_pton'; did you mean 'inet_aton'? [-Wimplicit-function-declaration]
   if(inet_pton((int)sa->sin6_family, ip, &sa->sin6_addr) <= 0) {
      ^~~~~~~~~
      inet_aton
[ 42%] Building C object external/unbound/CMakeFiles/unbound.dir/util/random.c.obj
[ 42%] Building C object external/unbound/CMakeFiles/unbound.dir/util/rbtree.c.obj
[ 44%] Building C object external/unbound/CMakeFiles/unbound.dir/util/regional.c.obj
[ 44%] Building C object external/unbound/CMakeFiles/unbound.dir/util/rtt.c.obj
[ 44%] Built target obj_ringct
[ 45%] Building C object external/unbound/CMakeFiles/unbound.dir/util/storage/dnstree.c.obj
[ 45%] Building C object external/unbound/CMakeFiles/unbound.dir/util/storage/lookup3.c.obj
Scanning dependencies of target obj_cryptonote_basic
[ 45%] Building CXX object src/cryptonote_basic/CMakeFiles/obj_cryptonote_basic.dir/account.cpp.obj
[ 45%] Building C object external/unbound/CMakeFiles/unbound.dir/util/storage/lruhash.c.obj
[ 46%] Building C object external/unbound/CMakeFiles/unbound.dir/util/storage/slabhash.c.obj
[ 46%] Building C object external/unbound/CMakeFiles/unbound.dir/util/timehist.c.obj
[ 46%] Building C object external/unbound/CMakeFiles/unbound.dir/util/tube.c.obj
[ 48%] Building C object external/unbound/CMakeFiles/unbound.dir/util/ub_event.c.obj
[ 48%] Building C object external/unbound/CMakeFiles/unbound.dir/util/winsock_event.c.obj
[ 48%] Building CXX object src/cryptonote_basic/CMakeFiles/obj_cryptonote_basic.dir/cryptonote_basic_impl.cpp.obj
[ 49%] Building C object external/unbound/CMakeFiles/unbound.dir/validator/autotrust.c.obj
[ 49%] Building C object external/unbound/CMakeFiles/unbound.dir/validator/val_anchor.c.obj
[ 49%] Building C object external/unbound/CMakeFiles/unbound.dir/validator/validator.c.obj
[ 50%] Building C object external/unbound/CMakeFiles/unbound.dir/validator/val_kcache.c.obj
[ 50%] Built target obj_checkpoints
[ 50%] Building C object external/unbound/CMakeFiles/unbound.dir/validator/val_kentry.c.obj
[ 51%] Building CXX object src/cryptonote_basic/CMakeFiles/obj_cryptonote_basic.dir/cryptonote_format_utils.cpp.obj
Scanning dependencies of target obj_cryptonote_core
[ 51%] Building C object external/unbound/CMakeFiles/unbound.dir/validator/val_neg.c.obj
[ 51%] Building CXX object src/cryptonote_core/CMakeFiles/obj_cryptonote_core.dir/blockchain.cpp.obj
[ 53%] Building C object external/unbound/CMakeFiles/unbound.dir/validator/val_nsec3.c.obj
[ 53%] Building C object external/unbound/CMakeFiles/unbound.dir/validator/val_nsec.c.obj
[ 54%] Building C object external/unbound/CMakeFiles/unbound.dir/validator/val_secalgo.c.obj
[ 54%] Building C object external/unbound/CMakeFiles/unbound.dir/validator/val_sigcrypt.c.obj
[ 54%] Building C object external/unbound/CMakeFiles/unbound.dir/validator/val_utils.c.obj
[ 55%] Building C object external/unbound/CMakeFiles/unbound.dir/dns64/dns64.c.obj
[ 55%] Building C object external/unbound/CMakeFiles/unbound.dir/testcode/checklocks.c.obj
[ 57%] Building C object external/unbound/CMakeFiles/unbound.dir/sldns/keyraw.c.obj
[ 57%] Building C object external/unbound/CMakeFiles/unbound.dir/sldns/sbuffer.c.obj
[ 57%] Building CXX object src/cryptonote_basic/CMakeFiles/obj_cryptonote_basic.dir/difficulty.cpp.obj
[ 58%] Building CXX object src/cryptonote_basic/CMakeFiles/obj_cryptonote_basic.dir/hardfork.cpp.obj
[ 58%] Building C object external/unbound/CMakeFiles/unbound.dir/sldns/wire2str.c.obj
C:/msys64/home/noobless_/monero-gui/monero/external/unbound/sldns/wire2str.c: In function 'sldns_wire2str_a_scan':
C:/msys64/home/noobless_/monero-gui/monero/external/unbound/sldns/wire2str.c:1083:6: warning: implicit declaration of function 'inet_ntop'; did you mean 'inet_ntoa'? [-Wimplicit-function-declaration]
  if(!inet_ntop(AF_INET, *d, buf, (socklen_t)sizeof(buf)))
      ^~~~~~~~~
      inet_ntoa
[ 59%] Building C object external/unbound/CMakeFiles/unbound.dir/sldns/parse.c.obj
[ 59%] Building C object external/unbound/CMakeFiles/unbound.dir/sldns/parseutil.c.obj
[ 59%] Building C object external/unbound/CMakeFiles/unbound.dir/sldns/rrdef.c.obj
[ 61%] Building C object external/unbound/CMakeFiles/unbound.dir/sldns/str2wire.c.obj
C:/msys64/home/noobless_/monero-gui/monero/external/unbound/sldns/str2wire.c: In function 'sldns_str2wire_a_buf':
C:/msys64/home/noobless_/monero-gui/monero/external/unbound/sldns/str2wire.c:1059:5: warning: implicit declaration of function 'inet_pton'; did you mean 'inet_aton'? [-Wimplicit-function-declaration]
  if(inet_pton(AF_INET, (char*)str, &address) != 1)
     ^~~~~~~~~
     inet_aton
[ 61%] Building C object external/unbound/CMakeFiles/unbound.dir/compat/ctime_r.c.obj
[ 61%] Building CXX object src/cryptonote_basic/CMakeFiles/obj_cryptonote_basic.dir/miner.cpp.obj
[ 62%] Building C object external/unbound/CMakeFiles/unbound.dir/compat/gmtime_r.c.obj
[ 62%] Building C object external/unbound/CMakeFiles/unbound.dir/compat/inet_aton.c.obj
[ 62%] Building C object external/unbound/CMakeFiles/unbound.dir/compat/strsep.c.obj
[ 63%] Building C object external/unbound/CMakeFiles/unbound.dir/compat/strlcat.c.obj
[ 63%] Building C object external/unbound/CMakeFiles/unbound.dir/compat/strlcpy.c.obj
[ 63%] Building C object external/unbound/CMakeFiles/unbound.dir/compat/strptime.c.obj
[ 64%] Building C object external/unbound/CMakeFiles/unbound.dir/compat/explicit_bzero.c.obj
[ 66%] Building CXX object src/cryptonote_core/CMakeFiles/obj_cryptonote_core.dir/cryptonote_core.cpp.obj
[ 66%] Building C object external/unbound/CMakeFiles/unbound.dir/compat/arc4random.c.obj
[ 67%] Building C object external/unbound/CMakeFiles/unbound.dir/compat/arc4random_uniform.c.obj
[ 67%] Building C object external/unbound/CMakeFiles/unbound.dir/compat/reallocarray.c.obj
[ 67%] Building C object external/unbound/CMakeFiles/unbound.dir/compat/arc4_lock.c.obj
[ 68%] Building C object external/unbound/CMakeFiles/unbound.dir/compat/getentropy_win.c.obj
[ 68%] Building C object external/unbound/CMakeFiles/unbound.dir/libunbound/context.c.obj
[ 68%] Building C object external/unbound/CMakeFiles/unbound.dir/libunbound/libunbound.c.obj
[ 70%] Building C object external/unbound/CMakeFiles/unbound.dir/libunbound/libworker.c.obj
[ 70%] Linking C static library libunbound.a
[ 70%] Built target unbound
Scanning dependencies of target obj_multisig
[ 70%] Building CXX object src/multisig/CMakeFiles/obj_multisig.dir/multisig.cpp.obj
[ 70%] Built target obj_multisig
Scanning dependencies of target obj_blockchain_db
[ 70%] Building CXX object src/blockchain_db/CMakeFiles/obj_blockchain_db.dir/blockchain_db.cpp.obj
[ 70%] Built target obj_cryptonote_basic
Scanning dependencies of target obj_mnemonics
[ 70%] Building CXX object src/mnemonics/CMakeFiles/obj_mnemonics.dir/electrum-words.cpp.obj
[ 70%] Building CXX object src/cryptonote_core/CMakeFiles/obj_cryptonote_core.dir/tx_pool.cpp.obj
[ 70%] Building CXX object src/blockchain_db/CMakeFiles/obj_blockchain_db.dir/lmdb/db_lmdb.cpp.obj
[ 70%] Building CXX object src/cryptonote_core/CMakeFiles/obj_cryptonote_core.dir/cryptonote_tx_utils.cpp.obj
[ 70%] Built target obj_blockchain_db
[ 71%] Building CXX object src/wallet/CMakeFiles/obj_wallet.dir/wallet_args.cpp.obj
[ 71%] Building CXX object src/wallet/CMakeFiles/obj_wallet.dir/ringdb.cpp.obj
[ 71%] Built target obj_mnemonics
Scanning dependencies of target obj_rpc_base
[ 72%] Building CXX object src/rpc/CMakeFiles/obj_rpc_base.dir/rpc_args.cpp.obj
[ 72%] Built target obj_cryptonote_core
Scanning dependencies of target obj_wallet_api
[ 74%] Building CXX object src/wallet/api/CMakeFiles/obj_wallet_api.dir/wallet.cpp.obj
[ 74%] Building CXX object src/wallet/CMakeFiles/obj_wallet.dir/node_rpc_proxy.cpp.obj
[ 74%] Built target obj_rpc_base
Scanning dependencies of target epee
[ 75%] Building CXX object contrib/epee/src/CMakeFiles/epee.dir/hex.cpp.obj
Scanning dependencies of target obj_common
[ 75%] Building CXX object contrib/epee/src/CMakeFiles/epee.dir/http_auth.cpp.obj
[ 75%] Building CXX object src/common/CMakeFiles/obj_common.dir/base58.cpp.obj
[ 76%] Building CXX object src/common/CMakeFiles/obj_common.dir/command_line.cpp.obj
C:/msys64/home/noobless_/monero-gui/monero/src/wallet/api/wallet.cpp: In member function 'void Monero::WalletImpl::refreshThreadFunc()':
C:/msys64/home/noobless_/monero-gui/monero/src/wallet/api/wallet.cpp:1755:80: error: no matching function for call to 'boost::date_time::subsecond_duration<boost::posix_time::time_duration, 1000>::subsecond_duration(std::atomic<int>&)'
             boost::posix_time::milliseconds wait_for_ms(m_refreshIntervalMillis);
                                                                                ^
In file included from C:/msys64/mingw64/include/boost/date_time/posix_time/posix_time_config.hpp:16:0,
                 from C:/msys64/mingw64/include/boost/date_time/posix_time/posix_time_system.hpp:13,
                 from C:/msys64/mingw64/include/boost/date_time/posix_time/ptime.hpp:12,
                 from C:/msys64/mingw64/include/boost/date_time/posix_time/posix_time_types.hpp:12,
                 from C:/msys64/mingw64/include/boost/thread/thread_time.hpp:11,
                 from C:/msys64/mingw64/include/boost/thread/win32/basic_timed_mutex.hpp:16,
                 from C:/msys64/mingw64/include/boost/thread/win32/mutex.hpp:9,
                 from C:/msys64/mingw64/include/boost/thread/mutex.hpp:14,
                 from C:/msys64/home/noobless_/monero-gui/monero/src/crypto/crypto.h:35,
                 from C:/msys64/home/noobless_/monero-gui/monero/src/serialization/crypto.h:38,
                 from C:/msys64/home/noobless_/monero-gui/monero/src/cryptonote_basic/cryptonote_basic.h:44,
                 from C:/msys64/home/noobless_/monero-gui/monero/src/cryptonote_basic/account.h:33,
                 from C:/msys64/home/noobless_/monero-gui/monero/src/wallet/wallet2.h:43,
                 from C:/msys64/home/noobless_/monero-gui/monero/src/wallet/api/wallet.h:35,
                 from C:/msys64/home/noobless_/monero-gui/monero/src/wallet/api/wallet.cpp:32:
C:/msys64/mingw64/include/boost/date_time/time_duration.hpp:285:14: note: candidate: template<class T> boost::date_time::subsecond_duration<base_duration, frac_of_second>::subsecond_duration(const T&, typename boost::enable_if<boost::is_integral<Functor>, void>::type*)
     explicit subsecond_duration(T const& ss,
              ^~~~~~~~~~~~~~~~~~
C:/msys64/mingw64/include/boost/date_time/time_duration.hpp:285:14: note:   template argument deduction/substitution failed:
C:/msys64/mingw64/include/boost/date_time/time_duration.hpp: In substitution of 'template<class T> boost::date_time::subsecond_duration<boost::posix_time::time_duration, 1000>::subsecond_duration(const T&, typename boost::enable_if<boost::is_integral<T> >::type*) [with T = std::atomic<int>]':
C:/msys64/home/noobless_/monero-gui/monero/src/wallet/api/wallet.cpp:1755:80:   required from here
C:/msys64/mingw64/include/boost/date_time/time_duration.hpp:285:14: error: no type named 'type' in 'struct boost::enable_if<boost::is_integral<std::atomic<int> >, void>'
In file included from C:/msys64/mingw64/include/boost/date_time/posix_time/posix_time_config.hpp:16:0,
                 from C:/msys64/mingw64/include/boost/date_time/posix_time/posix_time_system.hpp:13,
                 from C:/msys64/mingw64/include/boost/date_time/posix_time/ptime.hpp:12,
                 from C:/msys64/mingw64/include/boost/date_time/posix_time/posix_time_types.hpp:12,
                 from C:/msys64/mingw64/include/boost/thread/thread_time.hpp:11,
                 from C:/msys64/mingw64/include/boost/thread/win32/basic_timed_mutex.hpp:16,
                 from C:/msys64/mingw64/include/boost/thread/win32/mutex.hpp:9,
                 from C:/msys64/mingw64/include/boost/thread/mutex.hpp:14,
                 from C:/msys64/home/noobless_/monero-gui/monero/src/crypto/crypto.h:35,
                 from C:/msys64/home/noobless_/monero-gui/monero/src/serialization/crypto.h:38,
                 from C:/msys64/home/noobless_/monero-gui/monero/src/cryptonote_basic/cryptonote_basic.h:44,
                 from C:/msys64/home/noobless_/monero-gui/monero/src/cryptonote_basic/account.h:33,
                 from C:/msys64/home/noobless_/monero-gui/monero/src/wallet/wallet2.h:43,
                 from C:/msys64/home/noobless_/monero-gui/monero/src/wallet/api/wallet.h:35,
                 from C:/msys64/home/noobless_/monero-gui/monero/src/wallet/api/wallet.cpp:32:
C:/msys64/mingw64/include/boost/date_time/time_duration.hpp:270:30: note: candidate: boost::date_time::subsecond_duration<boost::posix_time::time_duration, 1000>::subsecond_duration(const boost::date_time::subsecond_duration<boost::posix_time::time_duration, 1000>&)
   class BOOST_SYMBOL_VISIBLE subsecond_duration : public base_duration
                              ^~~~~~~~~~~~~~~~~~
C:/msys64/mingw64/include/boost/date_time/time_duration.hpp:270:30: note:   no known conversion for argument 1 from 'std::atomic<int>' to 'const boost::date_time::subsecond_duration<boost::posix_time::time_duration, 1000>&'
C:/msys64/mingw64/include/boost/date_time/time_duration.hpp:270:30: note: candidate: boost::date_time::subsecond_duration<boost::posix_time::time_duration, 1000>::subsecond_duration(boost::date_time::subsecond_duration<boost::posix_time::time_duration, 1000>&&)
C:/msys64/mingw64/include/boost/date_time/time_duration.hpp:270:30: note:   no known conversion for argument 1 from 'std::atomic<int>' to 'boost::date_time::subsecond_duration<boost::posix_time::time_duration, 1000>&&'
[ 76%] Building CXX object src/common/CMakeFiles/obj_common.dir/dns_utils.cpp.obj
make[2]: *** [src/wallet/api/CMakeFiles/obj_wallet_api.dir/build.make:63: src/wallet/api/CMakeFiles/obj_wallet_api.dir/wallet.cpp.obj] Error 1
make[1]: *** [CMakeFiles/Makefile2:2493: src/wallet/api/CMakeFiles/obj_wallet_api.dir/all] Error 2
make[1]: *** Waiting for unfinished jobs....
[ 76%] Building CXX object contrib/epee/src/CMakeFiles/epee.dir/mlog.cpp.obj
[ 76%] Building CXX object src/common/CMakeFiles/obj_common.dir/download.cpp.obj
[ 77%] Building CXX object contrib/epee/src/CMakeFiles/epee.dir/net_utils_base.cpp.obj
[ 77%] Building CXX object contrib/epee/src/CMakeFiles/epee.dir/string_tools.cpp.obj
[ 79%] Building CXX object contrib/epee/src/CMakeFiles/epee.dir/wipeable_string.cpp.obj
[ 79%] Building C object contrib/epee/src/CMakeFiles/epee.dir/memwipe.c.obj
[ 79%] Building CXX object contrib/epee/src/CMakeFiles/epee.dir/connection_basic.cpp.obj
[ 80%] Building CXX object contrib/epee/src/CMakeFiles/epee.dir/network_throttle.cpp.obj
[ 80%] Built target obj_wallet
[ 81%] Building CXX object src/common/CMakeFiles/obj_common.dir/util.cpp.obj
[ 81%] Building CXX object contrib/epee/src/CMakeFiles/epee.dir/network_throttle-detail.cpp.obj
[ 81%] Building CXX object src/common/CMakeFiles/obj_common.dir/i18n.cpp.obj
[ 83%] Building CXX object src/common/CMakeFiles/obj_common.dir/password.cpp.obj
[ 83%] Building CXX object src/common/CMakeFiles/obj_common.dir/perf_timer.cpp.obj
[ 83%] Building CXX object src/common/CMakeFiles/obj_common.dir/threadpool.cpp.obj
[ 84%] Building CXX object src/common/CMakeFiles/obj_common.dir/updates.cpp.obj
[ 84%] Built target obj_common
[ 84%] Linking CXX static library libepee.a
[ 84%] Built target epee
make: *** [Makefile:141: all] Error 2
[  0%] Built target easylogging
[ 16%] Built target obj_device
[ 42%] Built target obj_cncrypto
[ 57%] Built target generate_translations_header
[ 58%] Built target obj_wallet
[ 59%] Built target unbound
[ 59%] Built target genversion
[ 62%] Built target blocks
[ 63%] Built target lmdb
[ 66%] Built target obj_ringct_basic
[ 66%] Built target obj_ringct
[ 67%] Built target obj_checkpoints
[ 70%] Built target obj_cryptonote_basic
[ 70%] Built target obj_multisig
[ 70%] Built target obj_blockchain_db
[ 71%] Built target obj_cryptonote_core
[ 71%] Built target obj_mnemonics
[ 72%] Built target obj_rpc_base
[ 74%] Built target obj_version
[ 75%] Built target version
[ 80%] Built target obj_common
[ 81%] Building CXX object src/wallet/api/CMakeFiles/obj_wallet_api.dir/wallet_manager.cpp.obj
[ 81%] Building CXX object src/wallet/api/CMakeFiles/obj_wallet_api.dir/wallet.cpp.obj
[ 83%] Building CXX object src/wallet/api/CMakeFiles/obj_wallet_api.dir/transaction_info.cpp.obj
[ 88%] Built target epee
Scanning dependencies of target cncrypto
[ 88%] Linking CXX static library libcncrypto.a
[ 88%] Building CXX object src/wallet/api/CMakeFiles/obj_wallet_api.dir/transaction_history.cpp.obj
[ 88%] Built target cncrypto
Scanning dependencies of target mnemonics
[ 88%] Linking CXX static library libmnemonics.a
[ 88%] Built target mnemonics
Scanning dependencies of target common
[ 89%] Linking CXX static library libcommon.a
[ 89%] Built target common
Scanning dependencies of target ringct_basic
[ 89%] Linking CXX static library libringct_basic.a
[ 89%] Built target ringct_basic
Scanning dependencies of target checkpoints
[ 89%] Linking CXX static library libcheckpoints.a
[ 89%] Built target checkpoints
Scanning dependencies of target rpc_base
[ 89%] Linking CXX static library librpc_base.a
[ 89%] Built target rpc_base
Scanning dependencies of target device
[ 90%] Linking CXX static library libdevice.a
[ 90%] Built target device
Scanning dependencies of target cryptonote_basic
[ 90%] Linking CXX static library libcryptonote_basic.a
[ 90%] Built target cryptonote_basic
Scanning dependencies of target ringct
[ 90%] Linking CXX static library libringct.a
[ 90%] Built target ringct
Scanning dependencies of target multisig
[ 92%] Linking CXX static library libmultisig.a
[ 92%] Built target multisig
Scanning dependencies of target blockchain_db
[ 93%] Linking CXX static library libblockchain_db.a
[ 93%] Built target blockchain_db
Scanning dependencies of target cryptonote_core
[ 94%] Linking CXX static library libcryptonote_core.a
C:/msys64/home/noobless_/monero-gui/monero/src/wallet/api/wallet.cpp: In member function 'void Monero::WalletImpl::refreshThreadFunc()':
C:/msys64/home/noobless_/monero-gui/monero/src/wallet/api/wallet.cpp:1755:80: error: no matching function for call to 'boost::date_time::subsecond_duration<boost::posix_time::time_duration, 1000>::subsecond_duration(std::atomic<int>&)'
             boost::posix_time::milliseconds wait_for_ms(m_refreshIntervalMillis);
                                                                                ^
In file included from C:/msys64/mingw64/include/boost/date_time/posix_time/posix_time_config.hpp:16:0,
                 from C:/msys64/mingw64/include/boost/date_time/posix_time/posix_time_system.hpp:13,
                 from C:/msys64/mingw64/include/boost/date_time/posix_time/ptime.hpp:12,
                 from C:/msys64/mingw64/include/boost/date_time/posix_time/posix_time_types.hpp:12,
                 from C:/msys64/mingw64/include/boost/thread/thread_time.hpp:11,
                 from C:/msys64/mingw64/include/boost/thread/win32/basic_timed_mutex.hpp:16,
                 from C:/msys64/mingw64/include/boost/thread/win32/mutex.hpp:9,
                 from C:/msys64/mingw64/include/boost/thread/mutex.hpp:14,
                 from C:/msys64/home/noobless_/monero-gui/monero/src/crypto/crypto.h:35,
                 from C:/msys64/home/noobless_/monero-gui/monero/src/serialization/crypto.h:38,
                 from C:/msys64/home/noobless_/monero-gui/monero/src/cryptonote_basic/cryptonote_basic.h:44,
                 from C:/msys64/home/noobless_/monero-gui/monero/src/cryptonote_basic/account.h:33,
                 from C:/msys64/home/noobless_/monero-gui/monero/src/wallet/wallet2.h:43,
                 from C:/msys64/home/noobless_/monero-gui/monero/src/wallet/api/wallet.h:35,
                 from C:/msys64/home/noobless_/monero-gui/monero/src/wallet/api/wallet.cpp:32:
C:/msys64/mingw64/include/boost/date_time/time_duration.hpp:285:14: note: candidate: template<class T> boost::date_time::subsecond_duration<base_duration, frac_of_second>::subsecond_duration(const T&, typename boost::enable_if<boost::is_integral<Functor>, void>::type*)
     explicit subsecond_duration(T const& ss,
              ^~~~~~~~~~~~~~~~~~
C:/msys64/mingw64/include/boost/date_time/time_duration.hpp:285:14: note:   template argument deduction/substitution failed:
C:/msys64/mingw64/include/boost/date_time/time_duration.hpp: In substitution of 'template<class T> boost::date_time::subsecond_duration<boost::posix_time::time_duration, 1000>::subsecond_duration(const T&, typename boost::enable_if<boost::is_integral<T> >::type*) [with T = std::atomic<int>]':
C:/msys64/home/noobless_/monero-gui/monero/src/wallet/api/wallet.cpp:1755:80:   required from here
C:/msys64/mingw64/include/boost/date_time/time_duration.hpp:285:14: error: no type named 'type' in 'struct boost::enable_if<boost::is_integral<std::atomic<int> >, void>'
In file included from C:/msys64/mingw64/include/boost/date_time/posix_time/posix_time_config.hpp:16:0,
                 from C:/msys64/mingw64/include/boost/date_time/posix_time/posix_time_system.hpp:13,
                 from C:/msys64/mingw64/include/boost/date_time/posix_time/ptime.hpp:12,
                 from C:/msys64/mingw64/include/boost/date_time/posix_time/posix_time_types.hpp:12,
                 from C:/msys64/mingw64/include/boost/thread/thread_time.hpp:11,
                 from C:/msys64/mingw64/include/boost/thread/win32/basic_timed_mutex.hpp:16,
                 from C:/msys64/mingw64/include/boost/thread/win32/mutex.hpp:9,
                 from C:/msys64/mingw64/include/boost/thread/mutex.hpp:14,
                 from C:/msys64/home/noobless_/monero-gui/monero/src/crypto/crypto.h:35,
                 from C:/msys64/home/noobless_/monero-gui/monero/src/serialization/crypto.h:38,
                 from C:/msys64/home/noobless_/monero-gui/monero/src/cryptonote_basic/cryptonote_basic.h:44,
                 from C:/msys64/home/noobless_/monero-gui/monero/src/cryptonote_basic/account.h:33,
                 from C:/msys64/home/noobless_/monero-gui/monero/src/wallet/wallet2.h:43,
                 from C:/msys64/home/noobless_/monero-gui/monero/src/wallet/api/wallet.h:35,
                 from C:/msys64/home/noobless_/monero-gui/monero/src/wallet/api/wallet.cpp:32:
C:/msys64/mingw64/include/boost/date_time/time_duration.hpp:270:30: note: candidate: boost::date_time::subsecond_duration<boost::posix_time::time_duration, 1000>::subsecond_duration(const boost::date_time::subsecond_duration<boost::posix_time::time_duration, 1000>&)
   class BOOST_SYMBOL_VISIBLE subsecond_duration : public base_duration
                              ^~~~~~~~~~~~~~~~~~
C:/msys64/mingw64/include/boost/date_time/time_duration.hpp:270:30: note:   no known conversion for argument 1 from 'std::atomic<int>' to 'const boost::date_time::subsecond_duration<boost::posix_time::time_duration, 1000>&'
C:/msys64/mingw64/include/boost/date_time/time_duration.hpp:270:30: note: candidate: boost::date_time::subsecond_duration<boost::posix_time::time_duration, 1000>::subsecond_duration(boost::date_time::subsecond_duration<boost::posix_time::time_duration, 1000>&&)
C:/msys64/mingw64/include/boost/date_time/time_duration.hpp:270:30: note:   no known conversion for argument 1 from 'std::atomic<int>' to 'boost::date_time::subsecond_duration<boost::posix_time::time_duration, 1000>&&'
[ 94%] Built target cryptonote_core
Scanning dependencies of target wallet
[ 94%] Linking CXX static library ../../lib/libwallet.a
make[2]: *** [src/wallet/api/CMakeFiles/obj_wallet_api.dir/build.make:63: src/wallet/api/CMakeFiles/obj_wallet_api.dir/wallet.cpp.obj] Error 1
make[2]: *** Waiting for unfinished jobs....
make[1]: *** [CMakeFiles/Makefile2:2493: src/wallet/api/CMakeFiles/obj_wallet_api.dir/all] Error 2
make[1]: *** Waiting for unfinished jobs....
[ 94%] Built target wallet
make: *** [Makefile:141: all] Error 2
~/monero-gui/monero/build/release ~/monero-gui ~/monero-gui
~/monero-gui/monero/build/release/src/daemon ~/monero-gui/monero/build/release ~/monero-gui ~/monero-gui
[  0%] Built target easylogging
[  8%] Built target obj_cncrypto
[ 16%] Built target generate_translations_header
[ 28%] Built target obj_device
[ 47%] Built target blocks
Scanning dependencies of target libminiupnpc-static
[ 54%] Built target unbound
[ 55%] Building C object external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-static.dir/igd_desc_parse.c.obj
[ 56%] Built target lmdb
[ 56%] Built target genversion
[ 58%] Built target obj_ringct_basic
[ 58%] Building C object external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-static.dir/miniupnpc.c.obj
[ 58%] Built target obj_ringct
[ 59%] Built target obj_checkpoints
[ 62%] Built target obj_cryptonote_basic
[ 62%] Built target obj_multisig
[ 63%] Building C object external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-static.dir/minixml.c.obj
[ 64%] Built target obj_cryptonote_core
[ 65%] Built target obj_rpc_base
[ 65%] Built target obj_blockchain_db
[ 65%] Building C object external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-static.dir/minisoap.c.obj
Scanning dependencies of target obj_daemon_messages
Scanning dependencies of target obj_serialization
[ 66%] Building CXX object src/serialization/CMakeFiles/obj_serialization.dir/json_object.cpp.obj
[ 66%] Building CXX object src/rpc/CMakeFiles/obj_daemon_messages.dir/message.cpp.obj
[ 66%] Building C object external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-static.dir/minissdpc.c.obj
Scanning dependencies of target obj_p2p
[ 67%] Building CXX object src/p2p/CMakeFiles/obj_p2p.dir/net_node.cpp.obj
[ 68%] Building C object external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-static.dir/miniwget.c.obj
[ 68%] Building C object external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-static.dir/upnpcommands.c.obj
[ 68%] Building C object external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-static.dir/upnpdev.c.obj
[ 70%] Building C object external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-static.dir/upnpreplyparse.c.obj
[ 70%] Building C object external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-static.dir/upnperrors.c.obj
[ 71%] Building C object external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-static.dir/connecthostport.c.obj
[ 71%] Building C object external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-static.dir/portlistingparse.c.obj
[ 71%] Building C object external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-static.dir/receivedata.c.obj
[ 72%] Linking C static library libminiupnpc.a
[ 72%] Built target libminiupnpc-static
Scanning dependencies of target obj_cryptonote_protocol
[ 73%] Building CXX object src/cryptonote_protocol/CMakeFiles/obj_cryptonote_protocol.dir/block_queue.cpp.obj
[ 73%] Building CXX object src/rpc/CMakeFiles/obj_daemon_messages.dir/daemon_messages.cpp.obj
[ 73%] Built target obj_serialization
Scanning dependencies of target obj_rpc
[ 73%] Building CXX object src/rpc/CMakeFiles/obj_rpc.dir/core_rpc_server.cpp.obj
[ 73%] Building CXX object src/cryptonote_protocol/CMakeFiles/obj_cryptonote_protocol.dir/cryptonote_protocol_handler-base.cpp.obj
[ 73%] Built target obj_p2p
Scanning dependencies of target obj_daemon_rpc_server
[ 73%] Building CXX object src/rpc/CMakeFiles/obj_daemon_rpc_server.dir/daemon_handler.cpp.obj
[ 73%] Built target obj_daemon_messages
Scanning dependencies of target obj_daemonizer
[ 73%] Building CXX object src/daemonizer/CMakeFiles/obj_daemonizer.dir/windows_service.cpp.obj
[ 73%] Built target obj_daemonizer
[ 78%] Built target epee
[ 82%] Built target obj_common
[ 83%] Built target obj_version
[ 83%] Built target cncrypto
[ 85%] Built target version
[ 86%] Built target common
[ 86%] Built target ringct_basic
[ 86%] Built target checkpoints
[ 86%] Built target rpc_base
Scanning dependencies of target daemonizer
[ 86%] Linking CXX static library libdaemonizer.a
[ 86%] Built target daemonizer
[ 87%] Built target device
[ 87%] Built target cryptonote_basic
[ 87%] Built target ringct
[ 88%] Built target multisig
[ 89%] Built target blockchain_db
[ 89%] Built target obj_cryptonote_protocol
[ 90%] Built target cryptonote_core
[ 90%] Building CXX object src/rpc/CMakeFiles/obj_rpc.dir/instanciations.cpp.obj
Scanning dependencies of target p2p
[ 91%] Linking CXX static library libp2p.a
[ 91%] Built target p2p
Scanning dependencies of target cryptonote_protocol
[ 91%] Linking CXX static library libcryptonote_protocol.a
[ 91%] Built target cryptonote_protocol
Scanning dependencies of target serialization
[ 93%] Linking CXX static library libserialization.a
[ 93%] Built target serialization
Scanning dependencies of target daemon_messages
[ 93%] Linking CXX static library libdaemon_messages.a
[ 93%] Built target daemon_messages
[ 94%] Building CXX object src/rpc/CMakeFiles/obj_daemon_rpc_server.dir/zmq_server.cpp.obj
[ 94%] Built target obj_daemon_rpc_server
[ 94%] Built target obj_rpc
Scanning dependencies of target rpc
[ 95%] Linking CXX static library librpc.a
[ 95%] Built target rpc
Scanning dependencies of target daemon_rpc_server
[ 96%] Linking CXX static library libdaemon_rpc_server.a
[ 96%] Built target daemon_rpc_server
[ 96%] Generating blocksdat.o
Scanning dependencies of target daemon
[ 97%] Building CXX object src/daemon/CMakeFiles/daemon.dir/command_parser_executor.cpp.obj
[ 97%] Building CXX object src/daemon/CMakeFiles/daemon.dir/command_server.cpp.obj
[ 97%] Building CXX object src/daemon/CMakeFiles/daemon.dir/daemon.cpp.obj
[ 98%] Building CXX object src/daemon/CMakeFiles/daemon.dir/executor.cpp.obj
[ 98%] Building CXX object src/daemon/CMakeFiles/daemon.dir/main.cpp.obj
In file included from C:/msys64/home/noobless_/monero-gui/monero/src/daemonizer/daemonizer.h:63:0,
                 from C:/msys64/home/noobless_/monero-gui/monero/src/daemon/command_line_args.h:34,
                 from C:/msys64/home/noobless_/monero-gui/monero/src/daemon/daemon.cpp:47:
C:/msys64/home/noobless_/monero-gui/monero/src/daemonizer/windows_daemonizer.inl: In function 'bool daemonizer::daemonize(int, const char**, T_executor&&, const boost::program_options::variables_map&)':
C:/msys64/home/noobless_/monero-gui/monero/src/daemonizer/windows_daemonizer.inl:182:0: note: -Wmisleading-indentation is disabled from this point onwards, since column-tracking was disabled due to the size of the code/headers
     return false;

In file included from C:/msys64/home/noobless_/monero-gui/monero/src/daemonizer/daemonizer.h:63:0,
                 from C:/msys64/home/noobless_/monero-gui/monero/src/daemon/main.cpp:40:
C:/msys64/home/noobless_/monero-gui/monero/src/daemonizer/windows_daemonizer.inl: In function 'bool daemonizer::daemonize(int, const char**, T_executor&&, const boost::program_options::variables_map&)':
C:/msys64/home/noobless_/monero-gui/monero/src/daemonizer/windows_daemonizer.inl:182:0: note: -Wmisleading-indentation is disabled from this point onwards, since column-tracking was disabled due to the size of the code/headers
     return false;

[100%] Building CXX object src/daemon/CMakeFiles/daemon.dir/rpc_command_executor.cpp.obj
C:/msys64/home/noobless_/monero-gui/monero/src/daemonizer/windows_daemonizer.inl: At global scope:
C:/msys64/home/noobless_/monero-gui/monero/src/daemonizer/windows_daemonizer.inl:64:0: warning: 'std::__cxx11::string daemonizer::{anonymous}::get_argument_string(int, const char**)' defined but not used [-Wunused-function]
     std::string get_argument_string(int argc, char const * argv[])

In file included from C:/msys64/home/noobless_/monero-gui/monero/src/daemonizer/windows_daemonizer.inl:33:0,
                 from C:/msys64/home/noobless_/monero-gui/monero/src/daemonizer/daemonizer.h:63,
                 from C:/msys64/home/noobless_/monero-gui/monero/src/daemon/command_line_args.h:34,
                 from C:/msys64/home/noobless_/monero-gui/monero/src/daemon/daemon.cpp:47:
C:/msys64/home/noobless_/monero-gui/monero/src/daemonizer/windows_service_runner.h:45:23: warning: 'std::vector<char> windows::{anonymous}::vecstring(const string&)' defined but not used [-Wunused-function]
     std::vector<char> vecstring(std::string const & str)
                       ^~~~~~~~~
[100%] Linking CXX executable ../../bin/monerod.exe
[100%] Built target daemon
[  0%] Built target easylogging
[  8%] Built target obj_cncrypto
[ 12%] Built target generate_translations_header
[ 22%] Built target obj_device
[ 35%] Built target blocks
[ 58%] Built target libminiupnpc-static
[ 60%] Built target lmdb
[ 63%] Built target unbound
[ 64%] Built target obj_ringct_basic
[ 64%] Built target genversion
[ 64%] Built target obj_ringct
[ 65%] Built target obj_checkpoints
[ 67%] Built target obj_cryptonote_basic
[ 67%] Built target obj_multisig
[ 67%] Built target obj_blockchain_db
[ 68%] Built target obj_cryptonote_core
[ 70%] Built target obj_rpc_base
[ 71%] Built target obj_daemon_messages
[ 71%] Built target obj_serialization
[ 72%] Built target obj_p2p
[ 73%] Built target obj_cryptonote_protocol
[ 73%] Built target obj_daemonizer
[ 74%] Built target obj_daemon_rpc_server
[ 74%] Built target obj_rpc
[ 75%] Built target obj_version
[ 77%] Built target version
[ 81%] Built target obj_common
[ 86%] Built target epee
[ 86%] Built target cncrypto
[ 87%] Built target common
[ 87%] Built target ringct_basic
[ 87%] Built target checkpoints
[ 87%] Built target daemonizer
[ 87%] Built target rpc_base
[ 88%] Built target device
[ 88%] Built target cryptonote_basic
[ 88%] Built target ringct
[ 89%] Built target multisig
[ 90%] Built target blockchain_db
[ 91%] Built target cryptonote_core
[ 93%] Built target p2p
[ 93%] Built target cryptonote_protocol
[ 94%] Built target serialization
[ 95%] Built target rpc
[ 95%] Built target daemon_messages
[ 96%] Built target daemon_rpc_server
[100%] Built target daemon
Install the project...
-- Install configuration: "Release"
-- Installing: C:/msys64/home/noobless_/monero-gui/monero/bin/monerod.exe
~/monero-gui/monero/build/release ~/monero-gui ~/monero-gui
make: Entering directory '/home/noobless_/monero-gui/monero/build/release/contrib/epee'
make[1]: Entering directory '/C/msys64/home/noobless_/monero-gui/monero/build/release'
make[2]: Entering directory '/C/msys64/home/noobless_/monero-gui/monero/build/release'
make[2]: Leaving directory '/C/msys64/home/noobless_/monero-gui/monero/build/release'
[  0%] Built target easylogging
make[2]: Entering directory '/C/msys64/home/noobless_/monero-gui/monero/build/release'
make[2]: Leaving directory '/C/msys64/home/noobless_/monero-gui/monero/build/release'
[ 80%] Built target epee
make[2]: Entering directory '/C/msys64/home/noobless_/monero-gui/monero/build/release'
Scanning dependencies of target epee_readline
make[2]: Leaving directory '/C/msys64/home/noobless_/monero-gui/monero/build/release'
make[2]: Entering directory '/C/msys64/home/noobless_/monero-gui/monero/build/release'
[100%] Building CXX object contrib/epee/src/CMakeFiles/epee_readline.dir/readline_buffer.cpp.obj
[100%] Linking CXX static library libepee_readline.a
make[2]: Leaving directory '/C/msys64/home/noobless_/monero-gui/monero/build/release'
[100%] Built target epee_readline
make[1]: Leaving directory '/C/msys64/home/noobless_/monero-gui/monero/build/release'
Install the project...
-- Install configuration: "Release"
-- Installing: C:/msys64/home/noobless_/monero-gui/monero/lib/libepee.a
-- Installing: C:/msys64/home/noobless_/monero-gui/monero/lib/libepee_readline.a
make: Leaving directory '/home/noobless_/monero-gui/monero/build/release/contrib/epee'
make: Entering directory '/home/noobless_/monero-gui/monero/build/release/external/easylogging++'
make[1]: Entering directory '/C/msys64/home/noobless_/monero-gui/monero/build/release'
make[2]: Entering directory '/C/msys64/home/noobless_/monero-gui/monero/build/release'
make[2]: Leaving directory '/C/msys64/home/noobless_/monero-gui/monero/build/release'
Built target easylogging
make[1]: Leaving directory '/C/msys64/home/noobless_/monero-gui/monero/build/release'
Install the project...
-- Install configuration: "Release"
-- Installing: C:/msys64/home/noobless_/monero-gui/monero/lib/libeasylogging.a
make: Leaving directory '/home/noobless_/monero-gui/monero/build/release/external/easylogging++'
make: Entering directory '/home/noobless_/monero-gui/monero/build/release/external/db_drivers/liblmdb'
make[1]: Entering directory '/C/msys64/home/noobless_/monero-gui/monero/build/release'
make[2]: Entering directory '/C/msys64/home/noobless_/monero-gui/monero/build/release'
make[2]: Leaving directory '/C/msys64/home/noobless_/monero-gui/monero/build/release'
[100%] Built target lmdb
make[1]: Leaving directory '/C/msys64/home/noobless_/monero-gui/monero/build/release'
Install the project...
-- Install configuration: "Release"
-- Installing: C:/msys64/home/noobless_/monero-gui/monero/lib/liblmdb.a
make: Leaving directory '/home/noobless_/monero-gui/monero/build/release/external/db_drivers/liblmdb'
Installing libunbound...
~/monero-gui/monero/build/release/external/unbound ~/monero-gui/monero/build/release ~/monero-gui ~/monero-gui
[100%] Built target unbound
Install the project...
-- Install configuration: "Release"
-- Installing: C:/msys64/home/noobless_/monero-gui/monero/lib/libunbound.a
~/monero-gui/monero/build/release ~/monero-gui ~/monero-gui
~/monero-gui ~/monero-gui

noobless_@noobless MINGW64 ~/monero-gui

```

## stoffu | 2018-06-10T14:04:45+00:00
Hmm, I'm puzzled by that error, because the line src/wallet/api/wallet.cpp:1755 does indeed seem problematic in the sense that `boost::enable_if<boost::is_integral<std::atomic<int> >, void>::type` should fail to instantiate, but strangely the code has been compiling fine for me with Windows/OSX/Ubuntu.

Adding `.load()` will make it compile:

    boost::posix_time::milliseconds wait_for_ms(m_refreshIntervalMillis.load());


## stoffu | 2018-06-10T14:12:35+00:00
https://github.com/monero-project/monero/pull/3735

## stoffu | 2018-06-10T14:34:32+00:00
The error is due to the Boost upgrade to 1.67.

## ghost | 2018-06-10T22:00:28+00:00
just want to say thanks for the help you've provided @stoffu. This has seemed to have fixed the error above but now ive ran into this. - not sure if you've come across this before

```
/C/msys64/mingw64/bin/rcc.exe -name translations translations/translations.qrc -o release/qrc_translations.cpp
g++ -c -fno-keep-inline-dllexport -march=nocona -mtune=core2 -Wa,-mbig-obj -fPIC -fstack-protector -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=1 -Wformat -Wformat-security -fstack-protector -fstack-protector-strong -O2 -std=gnu++11 -Wall -W -Wextra -fexceptions -mthreads -DUNICODE -D_UNICODE -DWIN32 -DQT_NO_DEBUG -DQT_QUICK_LIB -DQT_WIDGETS_LIB -DQT_GUI_LIB -DQT_QML_LIB -DQT_NETWORK_LIB -DQT_CORE_LIB -DQT_NEEDS_QMAIN -I../../monero-gui -I. -I../monero/include -I../src/libwalletqt -I../src/QR-Code-generator -I../src -I../monero/src -I../../../../mingw64/include/QtQuick -I../../../../mingw64/include/QtWidgets -I../../../../mingw64/include/QtGui -I../../../../mingw64/include/QtQml -I../../../../mingw64/include/QtNetwork -I../../../../mingw64/include/QtCore -Irelease -I../../../../mingw64/include -I../../../../mingw64/share/qt5/mkspecs/win32-g++  -o release/qrc_translations.o release/qrc_translations.cpp
/C/msys64/mingw64/bin/rcc.exe -name qml ../qml.qrc -o release/qrc_qml.cpp
g++ -c -fno-keep-inline-dllexport -march=nocona -mtune=core2 -Wa,-mbig-obj -fPIC -fstack-protector -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=1 -Wformat -Wformat-security -fstack-protector -fstack-protector-strong -O2 -std=gnu++11 -Wall -W -Wextra -fexceptions -mthreads -DUNICODE -D_UNICODE -DWIN32 -DQT_NO_DEBUG -DQT_QUICK_LIB -DQT_WIDGETS_LIB -DQT_GUI_LIB -DQT_QML_LIB -DQT_NETWORK_LIB -DQT_CORE_LIB -DQT_NEEDS_QMAIN -I../../monero-gui -I. -I../monero/include -I../src/libwalletqt -I../src/QR-Code-generator -I../src -I../monero/src -I../../../../mingw64/include/QtQuick -I../../../../mingw64/include/QtWidgets -I../../../../mingw64/include/QtGui -I../../../../mingw64/include/QtQml -I../../../../mingw64/include/QtNetwork -I../../../../mingw64/include/QtCore -Irelease -I../../../../mingw64/include -I../../../../mingw64/share/qt5/mkspecs/win32-g++  -o release/qrc_qml.o release/qrc_qml.cpp
g++ -fstack-protector -Wl,--stack,4194304 -Wl,--dynamicbase -Wl,--nxcompat -Wl,-s,--relax,--gc-sections -Wl,-subsystem,windows -mthreads -o release/bin/monero-wallet-gui.exe object_script.monero-wallet-gui.Release  -lglu32 -lopengl32 -luser32 -lmingw32 -LC:/msys64/mingw64/lib C:/msys64/mingw64/lib/libqtmain.a -lshell32 -LC:/msys64/home/noobless_/monero-gui/monero/lib -lwallet_merged -llmdb -lepee -lunbound -leasylogging -Lc:/msys64/mingw64/lib -L/mingw64/lib -Lc:/msys64/mingw64/boost/lib -L/mingw64/boost/lib -Wl,-Bstatic -lboost_serialization-mt -lboost_thread-mt -lboost_system-mt -lboost_date_time-mt -lboost_filesystem-mt -lboost_regex-mt -lboost_chrono-mt -lboost_program_options-mt -lboost_locale-mt -licuio -licuin -licuuc -licudt -licutu -liconv -lssl -lcrypto -Wl,-Bdynamic -lws2_32 -lwsock32 -lIphlpapi -lgdi32 C:/msys64/mingw64/lib/libQt5Quick.dll.a C:/msys64/mingw64/lib/libQt5Widgets.dll.a C:/msys64/mingw64/lib/libQt5Gui.dll.a C:/msys64/mingw64/lib/libQt5Qml.dll.a C:/msys64/mingw64/lib/libQt5Network.dll.a C:/msys64/mingw64/lib/libQt5Core.dll.a
C:/msys64/home/noobless_/monero-gui/monero/lib/libwallet_merged.a(device_ledger.cpp.obj):device_ledger.cpp:(.text+0x10e1): undefined reference to `SCardReleaseContext'
C:/msys64/home/noobless_/monero-gui/monero/lib/libwallet_merged.a(device_ledger.cpp.obj):device_ledger.cpp:(.text+0x12a7): undefined reference to `SCardDisconnect'
C:/msys64/home/noobless_/monero-gui/monero/lib/libwallet_merged.a(device_ledger.cpp.obj):device_ledger.cpp:(.text+0x1a3d): undefined reference to `__imp_g_rgSCardT0Pci'
C:/msys64/home/noobless_/monero-gui/monero/lib/libwallet_merged.a(device_ledger.cpp.obj):device_ledger.cpp:(.text+0x1a6a): undefined reference to `SCardTransmit'
C:/msys64/home/noobless_/monero-gui/monero/lib/libwallet_merged.a(device_ledger.cpp.obj):device_ledger.cpp:(.text+0x2516): undefined reference to `SCardEstablishContext'
C:/msys64/home/noobless_/monero-gui/monero/lib/libwallet_merged.a(device_ledger.cpp.obj):device_ledger.cpp:(.text+0x2af9): undefined reference to `SCardListReadersA'
C:/msys64/home/noobless_/monero-gui/monero/lib/libwallet_merged.a(device_ledger.cpp.obj):device_ledger.cpp:(.text+0x3036): undefined reference to `SCardDisconnect'
C:/msys64/home/noobless_/monero-gui/monero/lib/libwallet_merged.a(device_ledger.cpp.obj):device_ledger.cpp:(.text+0x3363): undefined reference to `SCardConnectA'
C:/msys64/home/noobless_/monero-gui/monero/lib/libwallet_merged.a(device_ledger.cpp.obj):device_ledger.cpp:(.text+0x34d0): undefined reference to `SCardStatusA'
C:/msys64/home/noobless_/monero-gui/monero/lib/libwallet_merged.a(device_ledger.cpp.obj):device_ledger.cpp:(.text+0x35ef): undefined reference to `SCardFreeMemory'
C:/msys64/home/noobless_/monero-gui/monero/lib/libwallet_merged.a(device_ledger.cpp.obj):device_ledger.cpp:(.text+0x3735): undefined reference to `SCardFreeMemory'
collect2.exe: error: ld returned 1 exit status
make[1]: *** [Makefile.Release:212: release/bin/monero-wallet-gui.exe] Error 1
make[1]: Leaving directory '/home/noobless_/monero-gui/build'
make: *** [Makefile:36: release] Error 2
```

Which is weird because I thought it would of been related to this:
![image](https://user-images.githubusercontent.com/32077247/41206869-b9552fc8-6d0b-11e8-9a7c-170fd0db056a.png)

#1228 

## dEBRUYNE-1 | 2018-06-11T08:34:17+00:00
@noobieless - Apply #1444. 

## ghost | 2018-06-11T09:24:46+00:00
@dEBRUYNE-1 Thanks! monero.wallet-gui.exe compiled, absolutely brilliant.. unfortunately launching the exe gives System Errors, is this due to the compile missing dependencies? or maybe the version of boost perhaps. 

![image](https://user-images.githubusercontent.com/32077247/41223276-a10dc7aa-6d69-11e8-9fae-8fd302072c31.png)
![image](https://user-images.githubusercontent.com/32077247/41223299-b128ab0a-6d69-11e8-82fe-963cb8cb2369.png)
![image](https://user-images.githubusercontent.com/32077247/41223313-bc79c89a-6d69-11e8-913a-ed4eeaa58ea9.png)
![image](https://user-images.githubusercontent.com/32077247/41223326-c52f6e90-6d69-11e8-9255-d40e20505920.png)


## stoffu | 2018-06-11T09:26:54+00:00
Are you sure you run `make deploy` (in the `build` directory, or `make -C build deploy` in the top directory)? This step is needed to copy all needed files to one place.

## ghost | 2018-06-11T09:33:54+00:00
You are 100% correct, my mistake, i missed this step. 
I ran make deploy and it throws missing dll file. Is msys missing dll's
![image](https://user-images.githubusercontent.com/32077247/41223843-36e1564c-6d6b-11e8-97f9-69a39b707b75.png)

lastly, you guys have been so much help, how does one donate monero for the assistance?


## stoffu | 2018-06-11T09:44:51+00:00
https://github.com/monero-project/monero#supporting-the-project

Your love is appreciated :)

## ghost | 2018-06-11T10:34:36+00:00
@stoffu Brillaint, donated!

I edited windeploy_helper.sh and replaced `ICU_FILES=(libicudt58.dll libicuin58.dll libicuio58.dll libicutu58.dll libicuuc58.dll)`

with `ICU_FILES=(libicudt61.dll libicuin61.dll libicuio61.dll libicutu61.dll libicuuc61.dll)`

obviously calling for out dated dll's

## stoffu | 2018-06-11T11:00:24+00:00
@noobieless Maybe then could you make a pull request for that change?

## PidgeyBE | 2018-06-30T22:09:39+00:00
@wesleykadou Thanks! This worked for me too!

## PidgeyBE | 2018-07-01T22:03:14+00:00
Since I couldn't find a pull request for this change, I've created one myself...
https://github.com/monero-project/monero-gui/pull/1482

## manni07 | 2019-12-27T13:59:00+00:00
sorry, but your remarks are referencing to other issues which reference to other issues which reference to other issues and so on... it is like a puzzle

# Action History
- Created by: ghost | 2018-06-10T10:19:58+00:00
- Closed at: 2018-06-11T10:34:37+00:00
