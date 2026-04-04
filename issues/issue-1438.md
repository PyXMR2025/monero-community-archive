---
title: Error building on Windows 10
source_url: https://github.com/monero-project/monero-gui/issues/1438
author: barretts
assignees: []
labels:
- resolved
created_at: '2018-06-01T14:05:28+00:00'
updated_at: '2019-08-28T14:46:38+00:00'
type: issue
status: closed
closed_at: '2018-12-17T09:18:35+00:00'
---

# Original Description
Following the new instructions I get an error when trying to build on Windows 10 64 bit. Any idea why make can't find a target for QApplication as the last messages suggest is the problem?
```
$ ./build.sh
Building release
/c/code/monero-gui /c/code/monero-gui
/c/code/monero-gui /c/code/monero-gui
': not a valid identifierline 88: export: `dashless
': not a valid identifierline 88: export: `sha1
': not a valid identifierline 88: export: `displaypath
warning: unable to rmdir 'external/rapidjson': Directory not empty
Submodule path '': checked out '8a7b3ff13858c5d879530c99de5c723c88429342'
D       include/INode.h
D       include/IWallet.h
Previous HEAD position was 8a7b3ff1 Merge pull request #3866
Switched to branch 'release-v0.12'
Your branch is up to date with 'origin/release-v0.12'.
You are currently on commit cd46edb
The most recent tag was at b40363c
You are ahead of or behind a tagged release
D       include/INode.h
D       include/IWallet.h
Switched to and reset branch 'cd46edb'
': not a valid identifierline 88: export: `dashless
': not a valid identifierline 88: export: `dashless
/c/code/monero-gui/monero /c/code/monero-gui /c/code/monero-gui
You are currently on commit bd567719
The most recent tag was at aa6850c7
You are ahead of or behind a tagged release
/c/code/monero-gui /c/code/monero-gui
latest libwallet version: cd46edb
Installed libwallet version: bd567719
Building new libwallet version cd46edb
Building libwallet release
cleaning up existing monero build dir, libs and includes
/c/code/monero-gui/monero/build/release /c/code/monero-gui /c/code/monero-gui
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
-- Found OpenSSL: C:/OpenSSL-Win64/lib/libeay32.lib (found version "1.0.2o")
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
-- Found Boost Version: 106600
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
-- Build files have been written to: C:/code/monero-gui/monero/build/release
/c/code/monero-gui/monero/build/release/src/wallet /c/code/monero-gui/monero/build/release /c/code/monero-gui /c/code/monero-gui
make: Entering directory '/c/code/monero-gui/monero/build/release'
make[1]: Entering directory '/c/code/monero-gui/monero/build/release'
make[2]: Entering directory '/c/code/monero-gui/monero/build/release'
make[3]: Entering directory '/c/code/monero-gui/monero/build/release'
Scanning dependencies of target genversion
make[3]: Leaving directory '/c/code/monero-gui/monero/build/release'
make[3]: Entering directory '/c/code/monero-gui/monero/build/release'
[  0%] Generating ../version.cpp
-- You are currently on commit bd567719
-- The most recent tag was at aa6850c7
-- You are ahead of or behind a tagged release
make[3]: Leaving directory '/c/code/monero-gui/monero/build/release'
[  0%] Built target genversion
make[3]: Entering directory '/c/code/monero-gui/monero/build/release'
Scanning dependencies of target obj_version
make[3]: Leaving directory '/c/code/monero-gui/monero/build/release'
make[3]: Entering directory '/c/code/monero-gui/monero/build/release'
[  0%] Building CXX object src/CMakeFiles/obj_version.dir/__/version.cpp.obj
make[3]: Leaving directory '/c/code/monero-gui/monero/build/release'
[ 50%] Built target obj_version
make[3]: Entering directory '/c/code/monero-gui/monero/build/release'
Scanning dependencies of target version
make[3]: Leaving directory '/c/code/monero-gui/monero/build/release'
make[3]: Entering directory '/c/code/monero-gui/monero/build/release'
[100%] Linking CXX static library libversion.a
make[3]: Leaving directory '/c/code/monero-gui/monero/build/release'
[100%] Built target version
make[2]: Leaving directory '/c/code/monero-gui/monero/build/release'
make[1]: Leaving directory '/c/code/monero-gui/monero/build/release'
make: Leaving directory '/c/code/monero-gui/monero/build/release'
[  0%] Generating stagenet_blocks.o
Scanning dependencies of target lmdb
[  0%] Generating blocks.o
[  0%] Building C object external/db_drivers/liblmdb/CMakeFiles/lmdb.dir/mdb.c.obj
[  1%] Generating testnet_blocks.o
Scanning dependencies of target blocks
[  1%] Building C object src/blocks/CMakeFiles/blocks.dir/blockexports.c.obj
[  2%] Linking C static library libblocks.a
[  2%] Built target blocks
Scanning dependencies of target unbound
[  3%] Building C object external/unbound/CMakeFiles/unbound.dir/services/authzone.c.obj
Scanning dependencies of target easylogging
Scanning dependencies of target obj_wallet
[  3%] Building CXX object external/easylogging++/CMakeFiles/easylogging.dir/easylogging++.cc.obj
[  3%] Building CXX object src/wallet/CMakeFiles/obj_wallet.dir/wallet2.cpp.obj
C:/code/monero-gui/monero/external/db_drivers/liblmdb/mdb.c: In function 'mdb_strerror':
cc1.exe: warning: function may return address of local variable [-Wreturn-local-addr]
C:/code/monero-gui/monero/external/db_drivers/liblmdb/mdb.c:1584:7: note: declared here
  char buf[MSGSIZE+PADSIZE], *ptr = buf;
       ^~~
[  3%] Building C object external/db_drivers/liblmdb/CMakeFiles/lmdb.dir/midl.c.obj
[  5%] Linking C static library liblmdb.a
[  5%] Building C object external/unbound/CMakeFiles/unbound.dir/services/cache/dns.c.obj
[  5%] Built target lmdb
[  5%] Built target genversion
Scanning dependencies of target obj_cncrypto
[  5%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/aesb.c.obj
[  5%] Building C object external/unbound/CMakeFiles/unbound.dir/services/cache/infra.c.obj
[  5%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/blake256.c.obj
[  6%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/chacha.c.obj
[  6%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/crypto-ops-data.c.obj
[  7%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/crypto-ops.c.obj
[  9%] Building C object external/unbound/CMakeFiles/unbound.dir/services/cache/rrset.c.obj
[  9%] Building C object external/unbound/CMakeFiles/unbound.dir/util/data/dname.c.obj
[  9%] Building CXX object src/crypto/CMakeFiles/obj_cncrypto.dir/crypto.cpp.obj
[ 10%] Building C object external/unbound/CMakeFiles/unbound.dir/util/data/msgencode.c.obj
[ 10%] Linking CXX static library libeasylogging.a
[ 10%] Built target easylogging
Scanning dependencies of target generate_translations_header
[ 10%] Creating directories for 'generate_translations_header'
[ 10%] No download step for 'generate_translations_header'
[ 10%] No patch step for 'generate_translations_header'
[ 11%] No update step for 'generate_translations_header'
[ 11%] Building C object external/unbound/CMakeFiles/unbound.dir/util/data/msgparse.c.obj
[ 12%] Performing configure step for 'generate_translations_header'
-- The C compiler identification is GNU 7.3.0
-- The CXX compiler identification is GNU 7.3.0
-- Check for working C compiler: C:/msys64/mingw64/bin/gcc.exe
[ 12%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/groestl.c.obj
-- Check for working C compiler: C:/msys64/mingw64/bin/gcc.exe -- works
-- Detecting C compiler ABI info
[ 14%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/hash-extra-blake.c.obj
[ 14%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/hash-extra-groestl.c.obj
[ 14%] Building C object external/unbound/CMakeFiles/unbound.dir/util/data/msgreply.c.obj
[ 14%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/hash-extra-jh.c.obj
-- Detecting C compiler ABI info - done
-- Detecting C compile features
[ 15%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/hash-extra-skein.c.obj
[ 15%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/hash.c.obj
[ 16%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/jh.c.obj
[ 16%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/keccak.c.obj
[ 16%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/oaes_lib.c.obj
[ 18%] Building C object external/unbound/CMakeFiles/unbound.dir/util/data/packed_rrset.c.obj
-- Detecting C compile features - done
-- Check for working CXX compiler: C:/msys64/mingw64/bin/g++.exe
[ 19%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/random.c.obj
-- Check for working CXX compiler: C:/msys64/mingw64/bin/g++.exe -- works
-- Detecting CXX compiler ABI info
[ 19%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/skein.c.obj
[ 19%] Building C object external/unbound/CMakeFiles/unbound.dir/iterator/iterator.c.obj
-- Detecting CXX compiler ABI info - done
-- Detecting CXX compile features
[ 20%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/slow-hash.c.obj
[ 20%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/tree-hash.c.obj
[ 20%] Built target obj_cncrypto
[ 20%] Building C object external/unbound/CMakeFiles/unbound.dir/iterator/iter_delegpt.c.obj
Scanning dependencies of target obj_ringct
-- Detecting CXX compile features - done
lrelease version 5.10.1
-- Configuring done
-- Generating done
-- Build files have been written to: C:/code/monero-gui/monero/build/release/translations
[ 20%] Building CXX object src/ringct/CMakeFiles/obj_ringct.dir/rctSigs.cpp.obj
[ 20%] Performing build step for 'generate_translations_header'
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
[ 22%] Building C object external/unbound/CMakeFiles/unbound.dir/iterator/iter_donotq.c.obj
Generating embedded translations header
[100%] Built target generate_translations_header
[ 23%] Performing install step for 'generate_translations_header'

[ 23%] Completed 'generate_translations_header'
[ 23%] Built target generate_translations_header
[ 23%] Building C object external/unbound/CMakeFiles/unbound.dir/iterator/iter_fwd.c.obj
Scanning dependencies of target obj_ringct_basic
[ 24%] Building CXX object src/ringct/CMakeFiles/obj_ringct_basic.dir/rctOps.cpp.obj
[ 25%] Building C object external/unbound/CMakeFiles/unbound.dir/iterator/iter_hints.c.obj
[ 25%] Building C object external/unbound/CMakeFiles/unbound.dir/iterator/iter_priv.c.obj
[ 25%] Building C object external/unbound/CMakeFiles/unbound.dir/iterator/iter_resptype.c.obj
[ 27%] Building C object external/unbound/CMakeFiles/unbound.dir/iterator/iter_scrub.c.obj
[ 27%] Building C object external/unbound/CMakeFiles/unbound.dir/iterator/iter_utils.c.obj
[ 27%] Building CXX object src/ringct/CMakeFiles/obj_ringct_basic.dir/rctTypes.cpp.obj
[ 27%] Building C object external/unbound/CMakeFiles/unbound.dir/respip/respip.c.obj
[ 28%] Building C object external/unbound/CMakeFiles/unbound.dir/services/listen_dnsport.c.obj
[ 28%] Built target obj_ringct
Scanning dependencies of target obj_checkpoints
C:/code/monero-gui/monero/external/unbound/services/listen_dnsport.c: In function 'verbose_print_addr':
C:/code/monero-gui/monero/external/unbound/services/listen_dnsport.c:88:6: warning: implicit declaration of function 'inet_ntop'; did you mean 'inet_ntoa'? [-Wimplicit-function-declaration]
   if(inet_ntop(addr->ai_family, sinaddr, buf,
      ^~~~~~~~~
      inet_ntoa
[ 29%] Building CXX object src/checkpoints/CMakeFiles/obj_checkpoints.dir/checkpoints.cpp.obj
[ 29%] Building C object external/unbound/CMakeFiles/unbound.dir/services/localzone.c.obj
[ 29%] Building C object src/ringct/CMakeFiles/obj_ringct_basic.dir/rctCryptoOps.c.obj
[ 31%] Building CXX object src/ringct/CMakeFiles/obj_ringct_basic.dir/bulletproofs.cc.obj
In file included from C:/code/monero-gui/monero/external/easylogging++/easylogging++.h:375:0,
                 from C:/code/monero-gui/monero/contrib/epee/include/misc_log_ex.h:33,
                 from C:/code/monero-gui/monero/src/ringct/bulletproofs.cc:34:
C:/msys64/mingw64/x86_64-w64-mingw32/include/winsock2.h:15:2: warning: #warning Please include winsock2.h before windows.h [-Wcpp]
 #warning Please include winsock2.h before windows.h
  ^~~~~~~
[ 32%] Building C object external/unbound/CMakeFiles/unbound.dir/services/mesh.c.obj
[ 32%] Building C object external/unbound/CMakeFiles/unbound.dir/services/modstack.c.obj
[ 32%] Building C object external/unbound/CMakeFiles/unbound.dir/services/outbound_list.c.obj
[ 33%] Building C object external/unbound/CMakeFiles/unbound.dir/services/outside_network.c.obj
[ 33%] Built target obj_ringct_basic
[ 33%] Building C object external/unbound/CMakeFiles/unbound.dir/services/view.c.obj
Scanning dependencies of target obj_cryptonote_basic
[ 33%] Building CXX object src/cryptonote_basic/CMakeFiles/obj_cryptonote_basic.dir/account.cpp.obj
[ 35%] Building C object external/unbound/CMakeFiles/unbound.dir/util/alloc.c.obj
[ 35%] Building C object external/unbound/CMakeFiles/unbound.dir/util/as112.c.obj
[ 35%] Building C object external/unbound/CMakeFiles/unbound.dir/util/config_file.c.obj
[ 36%] Building C object external/unbound/CMakeFiles/unbound.dir/util/configlexer.c.obj
[ 36%] Building C object external/unbound/CMakeFiles/unbound.dir/util/configparser.c.obj
[ 36%] Building CXX object src/cryptonote_basic/CMakeFiles/obj_cryptonote_basic.dir/cryptonote_basic_impl.cpp.obj
[ 36%] Building C object external/unbound/CMakeFiles/unbound.dir/util/fptr_wlist.c.obj
[ 37%] Building C object external/unbound/CMakeFiles/unbound.dir/util/locks.c.obj
[ 37%] Building C object external/unbound/CMakeFiles/unbound.dir/util/log.c.obj
[ 38%] Building C object external/unbound/CMakeFiles/unbound.dir/util/mini_event.c.obj
[ 38%] Building C object external/unbound/CMakeFiles/unbound.dir/util/module.c.obj
[ 38%] Building C object external/unbound/CMakeFiles/unbound.dir/util/netevent.c.obj
[ 40%] Building C object external/unbound/CMakeFiles/unbound.dir/util/net_help.c.obj
[ 40%] Built target obj_checkpoints
[ 41%] Building CXX object src/cryptonote_basic/CMakeFiles/obj_cryptonote_basic.dir/cryptonote_format_utils.cpp.obj
C:/code/monero-gui/monero/external/unbound/util/net_help.c: In function 'log_addr':
C:/code/monero-gui/monero/external/unbound/util/net_help.c:162:10: warning: implicit declaration of function 'inet_ntop'; did you mean 'inet_ntoa'? [-Wimplicit-function-declaration]
    (void)inet_ntop(af, sinaddr, dest,
          ^~~~~~~~~
          inet_ntoa
C:/code/monero-gui/monero/external/unbound/util/net_help.c: In function 'ipstrtoaddr':
C:/code/monero-gui/monero/external/unbound/util/net_help.c:225:6: warning: implicit declaration of function 'inet_pton'; did you mean 'inet_aton'? [-Wimplicit-function-declaration]
   if(inet_pton((int)sa->sin6_family, ip, &sa->sin6_addr) <= 0) {
      ^~~~~~~~~
      inet_aton
[ 41%] Building C object external/unbound/CMakeFiles/unbound.dir/util/random.c.obj
Scanning dependencies of target obj_device
[ 42%] Building CXX object src/device/CMakeFiles/obj_device.dir/device.cpp.obj
[ 42%] Building C object external/unbound/CMakeFiles/unbound.dir/util/rbtree.c.obj
[ 44%] Building C object external/unbound/CMakeFiles/unbound.dir/util/regional.c.obj
[ 44%] Building C object external/unbound/CMakeFiles/unbound.dir/util/rtt.c.obj
[ 45%] Building C object external/unbound/CMakeFiles/unbound.dir/util/storage/dnstree.c.obj
[ 45%] Building CXX object src/device/CMakeFiles/obj_device.dir/device_default.cpp.obj
[ 45%] Building C object external/unbound/CMakeFiles/unbound.dir/util/storage/lookup3.c.obj
[ 45%] Building C object external/unbound/CMakeFiles/unbound.dir/util/storage/lruhash.c.obj
[ 46%] Building C object external/unbound/CMakeFiles/unbound.dir/util/storage/slabhash.c.obj
[ 46%] Building C object external/unbound/CMakeFiles/unbound.dir/util/timehist.c.obj
[ 46%] Building C object external/unbound/CMakeFiles/unbound.dir/util/tube.c.obj
[ 48%] Building C object external/unbound/CMakeFiles/unbound.dir/util/ub_event.c.obj
[ 48%] Building C object external/unbound/CMakeFiles/unbound.dir/util/winsock_event.c.obj
[ 48%] Building CXX object src/device/CMakeFiles/obj_device.dir/log.cpp.obj
[ 48%] Building CXX object src/cryptonote_basic/CMakeFiles/obj_cryptonote_basic.dir/difficulty.cpp.obj
[ 49%] Building C object external/unbound/CMakeFiles/unbound.dir/validator/autotrust.c.obj
[ 50%] Building CXX object src/cryptonote_basic/CMakeFiles/obj_cryptonote_basic.dir/hardfork.cpp.obj
[ 50%] Building C object external/unbound/CMakeFiles/unbound.dir/validator/val_anchor.c.obj
[ 50%] Building C object external/unbound/CMakeFiles/unbound.dir/validator/validator.c.obj
[ 51%] Building C object external/unbound/CMakeFiles/unbound.dir/validator/val_kcache.c.obj
[ 51%] Building C object external/unbound/CMakeFiles/unbound.dir/validator/val_kentry.c.obj
[ 53%] Building CXX object src/device/CMakeFiles/obj_device.dir/device_ledger.cpp.obj
[ 53%] Building C object external/unbound/CMakeFiles/unbound.dir/validator/val_neg.c.obj
[ 54%] Building C object external/unbound/CMakeFiles/unbound.dir/validator/val_nsec3.c.obj
[ 54%] Building CXX object src/cryptonote_basic/CMakeFiles/obj_cryptonote_basic.dir/miner.cpp.obj
[ 54%] Building C object external/unbound/CMakeFiles/unbound.dir/validator/val_nsec.c.obj
[ 55%] Building C object external/unbound/CMakeFiles/unbound.dir/validator/val_secalgo.c.obj
[ 55%] Building C object external/unbound/CMakeFiles/unbound.dir/validator/val_sigcrypt.c.obj
[ 55%] Building C object external/unbound/CMakeFiles/unbound.dir/validator/val_utils.c.obj
[ 57%] Building C object external/unbound/CMakeFiles/unbound.dir/dns64/dns64.c.obj
[ 57%] Built target obj_device
[ 57%] Building C object external/unbound/CMakeFiles/unbound.dir/testcode/checklocks.c.obj
Scanning dependencies of target obj_cryptonote_core
[ 57%] Building CXX object src/cryptonote_core/CMakeFiles/obj_cryptonote_core.dir/blockchain.cpp.obj
[ 58%] Building C object external/unbound/CMakeFiles/unbound.dir/sldns/keyraw.c.obj
[ 58%] Building C object external/unbound/CMakeFiles/unbound.dir/sldns/sbuffer.c.obj
[ 58%] Building C object external/unbound/CMakeFiles/unbound.dir/sldns/wire2str.c.obj
C:/code/monero-gui/monero/external/unbound/sldns/wire2str.c: In function 'sldns_wire2str_a_scan':
C:/code/monero-gui/monero/external/unbound/sldns/wire2str.c:1083:6: warning: implicit declaration of function 'inet_ntop'; did you mean 'inet_ntoa'? [-Wimplicit-function-declaration]
  if(!inet_ntop(AF_INET, *d, buf, (socklen_t)sizeof(buf)))
      ^~~~~~~~~
      inet_ntoa
[ 59%] Building C object external/unbound/CMakeFiles/unbound.dir/sldns/parse.c.obj
[ 59%] Building C object external/unbound/CMakeFiles/unbound.dir/sldns/parseutil.c.obj
[ 59%] Building C object external/unbound/CMakeFiles/unbound.dir/sldns/rrdef.c.obj
[ 61%] Building C object external/unbound/CMakeFiles/unbound.dir/sldns/str2wire.c.obj
C:/code/monero-gui/monero/external/unbound/sldns/str2wire.c: In function 'sldns_str2wire_a_buf':
C:/code/monero-gui/monero/external/unbound/sldns/str2wire.c:1059:5: warning: implicit declaration of function 'inet_pton'; did you mean 'inet_aton'? [-Wimplicit-function-declaration]
  if(inet_pton(AF_INET, (char*)str, &address) != 1)
     ^~~~~~~~~
     inet_aton
[ 61%] Building C object external/unbound/CMakeFiles/unbound.dir/compat/ctime_r.c.obj
[ 62%] Building C object external/unbound/CMakeFiles/unbound.dir/compat/gmtime_r.c.obj
[ 62%] Building C object external/unbound/CMakeFiles/unbound.dir/compat/inet_aton.c.obj
[ 62%] Building C object external/unbound/CMakeFiles/unbound.dir/compat/strsep.c.obj
[ 63%] Building C object external/unbound/CMakeFiles/unbound.dir/compat/strlcat.c.obj
[ 63%] Building C object external/unbound/CMakeFiles/unbound.dir/compat/strlcpy.c.obj
[ 63%] Building C object external/unbound/CMakeFiles/unbound.dir/compat/strptime.c.obj
[ 64%] Building C object external/unbound/CMakeFiles/unbound.dir/compat/explicit_bzero.c.obj
[ 64%] Building C object external/unbound/CMakeFiles/unbound.dir/compat/arc4random.c.obj
[ 66%] Building C object external/unbound/CMakeFiles/unbound.dir/compat/arc4random_uniform.c.obj
[ 66%] Building C object external/unbound/CMakeFiles/unbound.dir/compat/reallocarray.c.obj
[ 66%] Building C object external/unbound/CMakeFiles/unbound.dir/compat/arc4_lock.c.obj
[ 66%] Built target obj_cryptonote_basic
Scanning dependencies of target obj_blockchain_db
[ 66%] Building CXX object src/blockchain_db/CMakeFiles/obj_blockchain_db.dir/blockchain_db.cpp.obj
[ 67%] Building CXX object src/cryptonote_core/CMakeFiles/obj_cryptonote_core.dir/cryptonote_core.cpp.obj
[ 67%] Building CXX object src/blockchain_db/CMakeFiles/obj_blockchain_db.dir/lmdb/db_lmdb.cpp.obj
[ 68%] Building CXX object src/wallet/CMakeFiles/obj_wallet.dir/wallet_args.cpp.obj
[ 68%] Built target obj_blockchain_db
[ 70%] Building C object external/unbound/CMakeFiles/unbound.dir/compat/getentropy_win.c.obj
[ 70%] Building C object external/unbound/CMakeFiles/unbound.dir/libunbound/context.c.obj
[ 70%] Building CXX object src/cryptonote_core/CMakeFiles/obj_cryptonote_core.dir/tx_pool.cpp.obj
[ 70%] Building C object external/unbound/CMakeFiles/unbound.dir/libunbound/libunbound.c.obj
[ 71%] Building C object external/unbound/CMakeFiles/unbound.dir/libunbound/libworker.c.obj
[ 71%] Building CXX object src/cryptonote_core/CMakeFiles/obj_cryptonote_core.dir/cryptonote_tx_utils.cpp.obj
[ 71%] Linking C static library libunbound.a
[ 71%] Built target unbound
Scanning dependencies of target obj_multisig
[ 71%] Building CXX object src/multisig/CMakeFiles/obj_multisig.dir/multisig.cpp.obj
[ 71%] Building CXX object src/wallet/CMakeFiles/obj_wallet.dir/ringdb.cpp.obj
[ 71%] Built target obj_multisig
Scanning dependencies of target obj_mnemonics
[ 71%] Building CXX object src/mnemonics/CMakeFiles/obj_mnemonics.dir/electrum-words.cpp.obj
[ 71%] Building CXX object src/wallet/CMakeFiles/obj_wallet.dir/node_rpc_proxy.cpp.obj
[ 71%] Built target obj_cryptonote_core
Scanning dependencies of target obj_rpc_base
[ 72%] Building CXX object src/rpc/CMakeFiles/obj_rpc_base.dir/rpc_args.cpp.obj
Scanning dependencies of target obj_wallet_api
[ 74%] Building CXX object src/wallet/api/CMakeFiles/obj_wallet_api.dir/wallet.cpp.obj
[ 74%] Built target obj_rpc_base
Scanning dependencies of target epee
[ 75%] Building CXX object contrib/epee/src/CMakeFiles/epee.dir/hex.cpp.obj
[ 75%] Building CXX object contrib/epee/src/CMakeFiles/epee.dir/http_auth.cpp.obj
[ 75%] Building CXX object contrib/epee/src/CMakeFiles/epee.dir/mlog.cpp.obj
[ 75%] Built target obj_mnemonics
[ 76%] Built target obj_version
[ 76%] Building CXX object src/wallet/api/CMakeFiles/obj_wallet_api.dir/wallet_manager.cpp.obj
[ 77%] Building CXX object src/wallet/api/CMakeFiles/obj_wallet_api.dir/transaction_info.cpp.obj
[ 77%] Building CXX object src/wallet/api/CMakeFiles/obj_wallet_api.dir/transaction_history.cpp.obj
[ 79%] Building CXX object contrib/epee/src/CMakeFiles/epee.dir/net_utils_base.cpp.obj
[ 79%] Built target obj_wallet
[ 79%] Building CXX object contrib/epee/src/CMakeFiles/epee.dir/string_tools.cpp.obj
Scanning dependencies of target obj_common
[ 79%] Building CXX object src/common/CMakeFiles/obj_common.dir/base58.cpp.obj
[ 80%] Building CXX object contrib/epee/src/CMakeFiles/epee.dir/wipeable_string.cpp.obj
[ 81%] Building CXX object src/common/CMakeFiles/obj_common.dir/command_line.cpp.obj
[ 81%] Building C object contrib/epee/src/CMakeFiles/epee.dir/memwipe.c.obj
[ 81%] Building CXX object contrib/epee/src/CMakeFiles/epee.dir/connection_basic.cpp.obj
[ 81%] Building CXX object src/common/CMakeFiles/obj_common.dir/dns_utils.cpp.obj
[ 81%] Building CXX object src/wallet/api/CMakeFiles/obj_wallet_api.dir/pending_transaction.cpp.obj
[ 81%] Building CXX object src/common/CMakeFiles/obj_common.dir/download.cpp.obj
[ 83%] Building CXX object contrib/epee/src/CMakeFiles/epee.dir/network_throttle.cpp.obj
[ 84%] Building CXX object src/wallet/api/CMakeFiles/obj_wallet_api.dir/utils.cpp.obj
[ 85%] Building CXX object src/common/CMakeFiles/obj_common.dir/util.cpp.obj
[ 85%] Building CXX object src/wallet/api/CMakeFiles/obj_wallet_api.dir/address_book.cpp.obj
[ 85%] Building CXX object src/common/CMakeFiles/obj_common.dir/i18n.cpp.obj
[ 85%] Building CXX object contrib/epee/src/CMakeFiles/epee.dir/network_throttle-detail.cpp.obj
[ 87%] Building CXX object src/common/CMakeFiles/obj_common.dir/password.cpp.obj
[ 87%] Building CXX object src/common/CMakeFiles/obj_common.dir/perf_timer.cpp.obj
[ 87%] Building CXX object src/common/CMakeFiles/obj_common.dir/threadpool.cpp.obj
[ 88%] Building CXX object src/common/CMakeFiles/obj_common.dir/updates.cpp.obj
[ 88%] Building CXX object src/wallet/api/CMakeFiles/obj_wallet_api.dir/subaddress.cpp.obj
[ 88%] Built target obj_common
[ 89%] Built target version
[ 90%] Building CXX object src/wallet/api/CMakeFiles/obj_wallet_api.dir/subaddress_account.cpp.obj
[ 90%] Building CXX object src/wallet/api/CMakeFiles/obj_wallet_api.dir/unsigned_transaction.cpp.obj
[ 90%] Linking CXX static library libepee.a
[ 90%] Built target epee
Scanning dependencies of target cncrypto
[ 90%] Linking CXX static library libcncrypto.a
[ 90%] Built target cncrypto
Scanning dependencies of target mnemonics
[ 90%] Linking CXX static library libmnemonics.a
[ 90%] Built target mnemonics
Scanning dependencies of target common
[ 92%] Linking CXX static library libcommon.a
[ 92%] Built target common
Scanning dependencies of target ringct_basic
[ 92%] Linking CXX static library libringct_basic.a
[ 92%] Built target ringct_basic
Scanning dependencies of target checkpoints
[ 92%] Linking CXX static library libcheckpoints.a
[ 92%] Built target checkpoints
Scanning dependencies of target device
[ 93%] Linking CXX static library libdevice.a
[ 93%] Built target device
Scanning dependencies of target rpc_base
[ 93%] Linking CXX static library librpc_base.a
[ 93%] Built target rpc_base
Scanning dependencies of target cryptonote_basic
[ 93%] Linking CXX static library libcryptonote_basic.a
[ 93%] Built target cryptonote_basic
Scanning dependencies of target ringct
[ 93%] Linking CXX static library libringct.a
[ 93%] Built target ringct
Scanning dependencies of target blockchain_db
[ 94%] Linking CXX static library libblockchain_db.a
[ 94%] Built target blockchain_db
Scanning dependencies of target multisig
[ 96%] Linking CXX static library libmultisig.a
[ 96%] Built target multisig
Scanning dependencies of target cryptonote_core
[ 97%] Linking CXX static library libcryptonote_core.a
[ 97%] Built target cryptonote_core
Scanning dependencies of target wallet
[ 97%] Linking CXX static library ../../lib/libwallet.a
[ 97%] Built target obj_wallet_api
Scanning dependencies of target wallet_merged
[ 98%] Linking CXX static library ../../lib/libwallet_merged.a
[ 98%] Built target wallet
Scanning dependencies of target wallet_rpc_server
[ 98%] Building CXX object src/wallet/CMakeFiles/wallet_rpc_server.dir/wallet_rpc_server.cpp.obj
[ 98%] Built target wallet_merged
[100%] Linking CXX executable ../../bin/monero-wallet-rpc.exe
[100%] Built target wallet_rpc_server
[  2%] Built target blocks
[  3%] Built target lmdb
[  3%] Built target genversion
[  3%] Built target easylogging
[ 24%] Built target generate_translations_header
[ 50%] Built target unbound
[ 59%] Built target obj_cncrypto
[ 61%] Built target obj_wallet
[ 61%] Built target obj_ringct
[ 63%] Built target obj_ringct_basic
[ 64%] Built target obj_checkpoints
[ 67%] Built target obj_device
[ 70%] Built target obj_cryptonote_basic
[ 70%] Built target obj_blockchain_db
[ 71%] Built target obj_cryptonote_core
[ 71%] Built target obj_multisig
[ 71%] Built target obj_mnemonics
[ 72%] Built target obj_rpc_base
[ 74%] Built target obj_version
[ 75%] Built target version
[ 80%] Built target obj_common
[ 85%] Built target obj_wallet_api
[ 90%] Built target epee
[ 92%] Built target wallet_merged
[ 92%] Built target mnemonics
[ 92%] Built target cncrypto
[ 93%] Built target common
[ 93%] Built target checkpoints
[ 93%] Built target ringct_basic
[ 93%] Built target rpc_base
[ 94%] Built target device
[ 94%] Built target cryptonote_basic
[ 94%] Built target ringct
[ 96%] Built target blockchain_db
[ 97%] Built target multisig
[ 98%] Built target cryptonote_core
[ 98%] Built target wallet
[100%] Built target wallet_rpc_server
Install the project...
-- Install configuration: "Release"
-- Installing: C:/code/monero-gui/monero/bin/monero-wallet-rpc.exe
-- Installing: C:/code/monero-gui/monero/lib/libwallet_merged.a
-- Installing: C:/code/monero-gui/monero/include/wallet/api/wallet2_api.h
/c/code/monero-gui/monero/build/release /c/code/monero-gui /c/code/monero-gui
/c/code/monero-gui/monero/build/release/src/daemon /c/code/monero-gui/monero/build/release /c/code/monero-gui /c/code/monero-gui
Scanning dependencies of target libminiupnpc-static
[  2%] Built target blocks
[  3%] Built target lmdb
[  4%] Building C object external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-static.dir/igd_desc_parse.c.obj
[  4%] Built target genversion
[  4%] Built target easylogging
[  4%] Building C object external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-static.dir/miniupnpc.c.obj
[ 42%] Built target unbound
[ 43%] Building C object external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-static.dir/minixml.c.obj
[ 47%] Built target generate_translations_header
[ 55%] Built target obj_cncrypto
[ 55%] Building C object external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-static.dir/minisoap.c.obj
[ 55%] Built target obj_ringct
[ 57%] Built target obj_ringct_basic
[ 58%] Built target obj_checkpoints
[ 58%] Building C object external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-static.dir/minissdpc.c.obj
[ 59%] Building C object external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-static.dir/miniwget.c.obj
[ 62%] Built target obj_cryptonote_basic
[ 64%] Built target obj_device
[ 64%] Built target obj_blockchain_db
[ 65%] Built target obj_cryptonote_core
[ 65%] Built target obj_multisig
[ 65%] Building C object external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-static.dir/upnpcommands.c.obj
[ 66%] Built target obj_rpc_base
[ 66%] Building C object external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-static.dir/upnpdev.c.obj
[ 67%] Building C object external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-static.dir/upnpreplyparse.c.obj
[ 67%] Building C object external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-static.dir/upnperrors.c.obj
[ 68%] Building C object external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-static.dir/connecthostport.c.obj
Scanning dependencies of target obj_p2p
Scanning dependencies of target obj_rpc
Scanning dependencies of target obj_cryptonote_protocol
[ 70%] Building CXX object src/p2p/CMakeFiles/obj_p2p.dir/net_node.cpp.obj
[ 71%] Building CXX object src/cryptonote_protocol/CMakeFiles/obj_cryptonote_protocol.dir/block_queue.cpp.obj
[ 71%] Building CXX object src/rpc/CMakeFiles/obj_rpc.dir/core_rpc_server.cpp.obj
[ 71%] Building C object external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-static.dir/portlistingparse.c.obj
[ 71%] Building C object external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-static.dir/receivedata.c.obj
[ 72%] Linking C static library libminiupnpc.a
[ 72%] Built target libminiupnpc-static
Scanning dependencies of target obj_daemon_rpc_server
[ 72%] Building CXX object src/rpc/CMakeFiles/obj_daemon_rpc_server.dir/daemon_handler.cpp.obj
[ 72%] Building CXX object src/cryptonote_protocol/CMakeFiles/obj_cryptonote_protocol.dir/cryptonote_protocol_handler-base.cpp.obj
[ 72%] Built target obj_p2p
Scanning dependencies of target obj_daemon_messages
[ 73%] Building CXX object src/rpc/CMakeFiles/obj_daemon_messages.dir/message.cpp.obj
[ 74%] Building CXX object src/rpc/CMakeFiles/obj_daemon_rpc_server.dir/zmq_server.cpp.obj
[ 74%] Built target obj_cryptonote_protocol
Scanning dependencies of target obj_serialization
[ 74%] Building CXX object src/serialization/CMakeFiles/obj_serialization.dir/json_object.cpp.obj
[ 74%] Building CXX object src/rpc/CMakeFiles/obj_daemon_messages.dir/daemon_messages.cpp.obj
[ 74%] Built target obj_daemon_rpc_server
Scanning dependencies of target obj_daemonizer
[ 74%] Building CXX object src/daemonizer/CMakeFiles/obj_daemonizer.dir/windows_service.cpp.obj
[ 74%] Built target obj_daemonizer
[ 79%] Built target epee
[ 80%] Built target obj_version
[ 80%] Built target cncrypto
[ 85%] Built target obj_common
[ 86%] Built target version
[ 87%] Built target common
[ 87%] Built target ringct_basic
[ 87%] Built target checkpoints
[ 88%] Built target device
[ 88%] Built target obj_daemon_messages
[ 88%] Built target rpc_base
[ 88%] Building CXX object src/rpc/CMakeFiles/obj_rpc.dir/instanciations.cpp.obj
Scanning dependencies of target daemonizer
[ 88%] Linking CXX static library libdaemonizer.a
[ 88%] Built target daemonizer
[ 88%] Built target cryptonote_basic
[ 88%] Built target ringct
[ 89%] Built target blockchain_db
[ 89%] Built target obj_serialization
[ 90%] Built target multisig
[ 91%] Built target cryptonote_core
Scanning dependencies of target p2p
[ 93%] Linking CXX static library libp2p.a
[ 93%] Built target p2p
Scanning dependencies of target cryptonote_protocol
[ 93%] Linking CXX static library libcryptonote_protocol.a
[ 93%] Built target cryptonote_protocol
Scanning dependencies of target serialization
[ 94%] Linking CXX static library libserialization.a
[ 94%] Built target serialization
Scanning dependencies of target daemon_messages
[ 94%] Linking CXX static library libdaemon_messages.a
[ 94%] Built target daemon_messages
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
In file included from C:/code/monero-gui/monero/src/daemonizer/daemonizer.h:63:0,
                 from C:/code/monero-gui/monero/src/daemon/command_line_args.h:34,
                 from C:/code/monero-gui/monero/src/daemon/daemon.cpp:47:
C:/code/monero-gui/monero/src/daemonizer/windows_daemonizer.inl: In function 'bool daemonizer::daemonize(int, const char**, T_executor&&, const boost::program_options::variables_map&)':
C:/code/monero-gui/monero/src/daemonizer/windows_daemonizer.inl:182:0: note: -Wmisleading-indentation is disabled from this point onwards, since column-tracking was disabled due to the size of the code/headers
     return false;

In file included from C:/code/monero-gui/monero/src/daemonizer/daemonizer.h:63:0,
                 from C:/code/monero-gui/monero/src/daemon/main.cpp:40:
C:/code/monero-gui/monero/src/daemonizer/windows_daemonizer.inl: In function 'bool daemonizer::daemonize(int, const char**, T_executor&&, const boost::program_options::variables_map&)':
C:/code/monero-gui/monero/src/daemonizer/windows_daemonizer.inl:182:0: note: -Wmisleading-indentation is disabled from this point onwards, since column-tracking was disabled due to the size of the code/headers
     return false;

[100%] Building CXX object src/daemon/CMakeFiles/daemon.dir/rpc_command_executor.cpp.obj
C:/code/monero-gui/monero/src/daemonizer/windows_daemonizer.inl: At global scope:
C:/code/monero-gui/monero/src/daemonizer/windows_daemonizer.inl:64:0: warning: 'std::__cxx11::string daemonizer::{anonymous}::get_argument_string(int, const char**)' defined but not used [-Wunused-function]
     std::string get_argument_string(int argc, char const * argv[])

In file included from C:/code/monero-gui/monero/src/daemonizer/windows_daemonizer.inl:33:0,
                 from C:/code/monero-gui/monero/src/daemonizer/daemonizer.h:63,
                 from C:/code/monero-gui/monero/src/daemon/command_line_args.h:34,
                 from C:/code/monero-gui/monero/src/daemon/daemon.cpp:47:
C:/code/monero-gui/monero/src/daemonizer/windows_service_runner.h:45:23: warning: 'std::vector<char> windows::{anonymous}::vecstring(const string&)' defined but not used [-Wunused-function]
     std::vector<char> vecstring(std::string const & str)
                       ^~~~~~~~~
[100%] Linking CXX executable ../../bin/monerod.exe
[100%] Built target daemon
[  2%] Built target blocks
[  3%] Built target lmdb
[ 10%] Built target libminiupnpc-static
[ 10%] Built target genversion
[ 10%] Built target easylogging
[ 48%] Built target unbound
[ 51%] Built target generate_translations_header
[ 59%] Built target obj_cncrypto
[ 59%] Built target obj_ringct
[ 60%] Built target obj_checkpoints
[ 63%] Built target obj_ringct_basic
[ 65%] Built target obj_cryptonote_basic
[ 67%] Built target obj_device
[ 67%] Built target obj_blockchain_db
[ 67%] Built target obj_multisig
[ 68%] Built target obj_rpc_base
[ 70%] Built target obj_cryptonote_core
[ 70%] Built target obj_rpc
[ 71%] Built target obj_p2p
[ 72%] Built target obj_cryptonote_protocol
[ 73%] Built target obj_daemon_rpc_server
[ 74%] Built target obj_daemon_messages
[ 74%] Built target obj_daemonizer
[ 74%] Built target obj_serialization
[ 75%] Built target obj_version
[ 77%] Built target version
[ 81%] Built target epee
[ 86%] Built target obj_common
[ 86%] Built target cncrypto
[ 87%] Built target common
[ 87%] Built target rpc_base
[ 87%] Built target checkpoints
[ 87%] Built target daemonizer
[ 87%] Built target ringct_basic
[ 88%] Built target device
[ 88%] Built target cryptonote_basic
[ 88%] Built target ringct
[ 89%] Built target blockchain_db
[ 90%] Built target multisig
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
-- Installing: C:/code/monero-gui/monero/bin/monerod.exe
/c/code/monero-gui/monero/build/release /c/code/monero-gui /c/code/monero-gui
make: Entering directory '/c/code/monero-gui/monero/build/release/contrib/epee'
make[1]: Entering directory '/C/code/monero-gui/monero/build/release'
make[2]: Entering directory '/C/code/monero-gui/monero/build/release'
make[2]: Leaving directory '/C/code/monero-gui/monero/build/release'
[  0%] Built target easylogging
make[2]: Entering directory '/C/code/monero-gui/monero/build/release'
make[2]: Leaving directory '/C/code/monero-gui/monero/build/release'
[ 80%] Built target epee
make[2]: Entering directory '/C/code/monero-gui/monero/build/release'
Scanning dependencies of target epee_readline
make[2]: Leaving directory '/C/code/monero-gui/monero/build/release'
make[2]: Entering directory '/C/code/monero-gui/monero/build/release'
[100%] Building CXX object contrib/epee/src/CMakeFiles/epee_readline.dir/readline_buffer.cpp.obj
[100%] Linking CXX static library libepee_readline.a
make[2]: Leaving directory '/C/code/monero-gui/monero/build/release'
[100%] Built target epee_readline
make[1]: Leaving directory '/C/code/monero-gui/monero/build/release'
Install the project...
-- Install configuration: "Release"
-- Installing: C:/code/monero-gui/monero/lib/libepee.a
-- Installing: C:/code/monero-gui/monero/lib/libepee_readline.a
make: Leaving directory '/c/code/monero-gui/monero/build/release/contrib/epee'
make: Entering directory '/c/code/monero-gui/monero/build/release/external/easylogging++'
make[1]: Entering directory '/C/code/monero-gui/monero/build/release'
make[2]: Entering directory '/C/code/monero-gui/monero/build/release'
make[2]: Leaving directory '/C/code/monero-gui/monero/build/release'
Built target easylogging
make[1]: Leaving directory '/C/code/monero-gui/monero/build/release'
Install the project...
-- Install configuration: "Release"
-- Installing: C:/code/monero-gui/monero/lib/libeasylogging.a
make: Leaving directory '/c/code/monero-gui/monero/build/release/external/easylogging++'
make: Entering directory '/c/code/monero-gui/monero/build/release/external/db_drivers/liblmdb'
make[1]: Entering directory '/C/code/monero-gui/monero/build/release'
make[2]: Entering directory '/C/code/monero-gui/monero/build/release'
make[2]: Leaving directory '/C/code/monero-gui/monero/build/release'
[100%] Built target lmdb
make[1]: Leaving directory '/C/code/monero-gui/monero/build/release'
Install the project...
-- Install configuration: "Release"
-- Installing: C:/code/monero-gui/monero/lib/liblmdb.a
make: Leaving directory '/c/code/monero-gui/monero/build/release/external/db_drivers/liblmdb'
Installing libunbound...
/c/code/monero-gui/monero/build/release/external/unbound /c/code/monero-gui/monero/build/release /c/code/monero-gui /c/code/monero-gui
[100%] Built target unbound
Install the project...
-- Install configuration: "Release"
-- Installing: C:/code/monero-gui/monero/lib/libunbound.a
/c/code/monero-gui/monero/build/release /c/code/monero-gui /c/code/monero-gui
/c/code/monero-gui /c/code/monero-gui
make: Entering directory '/c/code/monero-gui/src/zxcvbn-c'
make: Nothing to be done for 'all'.
make: Leaving directory '/c/code/monero-gui/src/zxcvbn-c'
You are currently on commit cd46edb
The most recent tag was at b40363c
You are ahead of or behind a tagged release
/c/code/monero-gui/monero /c/code/monero-gui /c/code/monero-gui
You are currently on commit bd567719
The most recent tag was at aa6850c7
You are ahead of or behind a tagged release
/c/code/monero-gui /c/code/monero-gui
Updating 'C:/code/monero-gui/build/translations/monero-core_ar.qm'...
Removing translations equal to source text in 'C:/code/monero-gui/build/translations/monero-core_ar.qm'...
    Generated 257 translation(s) (257 finished and 0 unfinished)
    Ignored 207 untranslated source text(s)
Updating 'C:/code/monero-gui/build/translations/monero-core_cat.qm'...
Removing translations equal to source text in 'C:/code/monero-gui/build/translations/monero-core_cat.qm'...
    Generated 241 translation(s) (241 finished and 0 unfinished)
    Ignored 166 untranslated source text(s)
Updating 'C:/code/monero-gui/build/translations/monero-core_cs.qm'...
Removing translations equal to source text in 'C:/code/monero-gui/build/translations/monero-core_cs.qm'...
    Generated 475 translation(s) (475 finished and 0 unfinished)
Updating 'C:/code/monero-gui/build/translations/monero-core_da.qm'...
Removing translations equal to source text in 'C:/code/monero-gui/build/translations/monero-core_da.qm'...
    Generated 442 translation(s) (442 finished and 0 unfinished)
Updating 'C:/code/monero-gui/build/translations/monero-core_de.qm'...
Removing translations equal to source text in 'C:/code/monero-gui/build/translations/monero-core_de.qm'...
    Generated 461 translation(s) (461 finished and 0 unfinished)
    Ignored 22 untranslated source text(s)
Updating 'C:/code/monero-gui/build/translations/monero-core_eo.qm'...
Removing translations equal to source text in 'C:/code/monero-gui/build/translations/monero-core_eo.qm'...
    Generated 479 translation(s) (479 finished and 0 unfinished)
    Ignored 2 untranslated source text(s)
Updating 'C:/code/monero-gui/build/translations/monero-core_es.qm'...
Removing translations equal to source text in 'C:/code/monero-gui/build/translations/monero-core_es.qm'...
    Generated 465 translation(s) (465 finished and 0 unfinished)
Updating 'C:/code/monero-gui/build/translations/monero-core_fi.qm'...
Removing translations equal to source text in 'C:/code/monero-gui/build/translations/monero-core_fi.qm'...
    Generated 126 translation(s) (126 finished and 0 unfinished)
    Ignored 315 untranslated source text(s)
Updating 'C:/code/monero-gui/build/translations/monero-core_fr.qm'...
Removing translations equal to source text in 'C:/code/monero-gui/build/translations/monero-core_fr.qm'...
    Generated 453 translation(s) (453 finished and 0 unfinished)
Updating 'C:/code/monero-gui/build/translations/monero-core_he.qm'...
Removing translations equal to source text in 'C:/code/monero-gui/build/translations/monero-core_he.qm'...
    Generated 467 translation(s) (467 finished and 0 unfinished)
    Ignored 19 untranslated source text(s)
Updating 'C:/code/monero-gui/build/translations/monero-core_hi.qm'...
Removing translations equal to source text in 'C:/code/monero-gui/build/translations/monero-core_hi.qm'...
    Generated 49 translation(s) (49 finished and 0 unfinished)
    Ignored 424 untranslated source text(s)
Updating 'C:/code/monero-gui/build/translations/monero-core_hr.qm'...
Removing translations equal to source text in 'C:/code/monero-gui/build/translations/monero-core_hr.qm'...
    Generated 365 translation(s) (365 finished and 0 unfinished)
    Ignored 104 untranslated source text(s)
Updating 'C:/code/monero-gui/build/translations/monero-core_id.qm'...
Removing translations equal to source text in 'C:/code/monero-gui/build/translations/monero-core_id.qm'...
    Generated 257 translation(s) (257 finished and 0 unfinished)
    Ignored 194 untranslated source text(s)
Updating 'C:/code/monero-gui/build/translations/monero-core_it.qm'...
Removing translations equal to source text in 'C:/code/monero-gui/build/translations/monero-core_it.qm'...
    Generated 466 translation(s) (466 finished and 0 unfinished)
Updating 'C:/code/monero-gui/build/translations/monero-core_ja.qm'...
Removing translations equal to source text in 'C:/code/monero-gui/build/translations/monero-core_ja.qm'...
    Generated 480 translation(s) (480 finished and 0 unfinished)
Updating 'C:/code/monero-gui/build/translations/monero-core_ko.qm'...
Removing translations equal to source text in 'C:/code/monero-gui/build/translations/monero-core_ko.qm'...
    Generated 276 translation(s) (276 finished and 0 unfinished)
    Ignored 170 untranslated source text(s)
Updating 'C:/code/monero-gui/build/translations/monero-core_nl.qm'...
Removing translations equal to source text in 'C:/code/monero-gui/build/translations/monero-core_nl.qm'...
    Generated 478 translation(s) (478 finished and 0 unfinished)
Updating 'C:/code/monero-gui/build/translations/monero-core_pl.qm'...
Removing translations equal to source text in 'C:/code/monero-gui/build/translations/monero-core_pl.qm'...
    Generated 476 translation(s) (476 finished and 0 unfinished)
Updating 'C:/code/monero-gui/build/translations/monero-core_pt-br.qm'...
Removing translations equal to source text in 'C:/code/monero-gui/build/translations/monero-core_pt-br.qm'...
    Generated 472 translation(s) (472 finished and 0 unfinished)
Updating 'C:/code/monero-gui/build/translations/monero-core_pt-pt.qm'...
Removing translations equal to source text in 'C:/code/monero-gui/build/translations/monero-core_pt-pt.qm'...
    Generated 464 translation(s) (464 finished and 0 unfinished)
Updating 'C:/code/monero-gui/build/translations/monero-core_ro.qm'...
Removing translations equal to source text in 'C:/code/monero-gui/build/translations/monero-core_ro.qm'...
    Generated 466 translation(s) (466 finished and 0 unfinished)
Updating 'C:/code/monero-gui/build/translations/monero-core_ru.qm'...
Removing translations equal to source text in 'C:/code/monero-gui/build/translations/monero-core_ru.qm'...
    Generated 479 translation(s) (479 finished and 0 unfinished)
    Ignored 12 untranslated source text(s)
Updating 'C:/code/monero-gui/build/translations/monero-core_sk.qm'...
Removing translations equal to source text in 'C:/code/monero-gui/build/translations/monero-core_sk.qm'...
    Generated 439 translation(s) (439 finished and 0 unfinished)
    Ignored 33 untranslated source text(s)
Updating 'C:/code/monero-gui/build/translations/monero-core_sl.qm'...
Removing translations equal to source text in 'C:/code/monero-gui/build/translations/monero-core_sl.qm'...
    Generated 318 translation(s) (318 finished and 0 unfinished)
    Ignored 132 untranslated source text(s)
Updating 'C:/code/monero-gui/build/translations/monero-core_sr.qm'...
Removing translations equal to source text in 'C:/code/monero-gui/build/translations/monero-core_sr.qm'...
    Generated 461 translation(s) (461 finished and 0 unfinished)
Updating 'C:/code/monero-gui/build/translations/monero-core_sv.qm'...
Removing translations equal to source text in 'C:/code/monero-gui/build/translations/monero-core_sv.qm'...
    Generated 468 translation(s) (468 finished and 0 unfinished)
Updating 'C:/code/monero-gui/build/translations/monero-core_tr.qm'...
Removing translations equal to source text in 'C:/code/monero-gui/build/translations/monero-core_tr.qm'...
    Generated 472 translation(s) (472 finished and 0 unfinished)
Updating 'C:/code/monero-gui/build/translations/monero-core_ua.qm'...
Removing translations equal to source text in 'C:/code/monero-gui/build/translations/monero-core_ua.qm'...
    Generated 369 translation(s) (369 finished and 0 unfinished)
    Ignored 114 untranslated source text(s)
Updating 'C:/code/monero-gui/build/translations/monero-core_zh-cn.qm'...
Removing translations equal to source text in 'C:/code/monero-gui/build/translations/monero-core_zh-cn.qm'...
    Generated 478 translation(s) (478 finished and 0 unfinished)
Updating 'C:/code/monero-gui/build/translations/monero-core_zh-tw.qm'...
Removing translations equal to source text in 'C:/code/monero-gui/build/translations/monero-core_zh-tw.qm'...
    Generated 481 translation(s) (481 finished and 0 unfinished)
Updating 'C:/code/monero-gui/build/translations/monero-core_ar.qm'...
Removing translations equal to source text in 'C:/code/monero-gui/build/translations/monero-core_ar.qm'...
    Generated 257 translation(s) (257 finished and 0 unfinished)
    Ignored 207 untranslated source text(s)
Updating 'C:/code/monero-gui/build/translations/monero-core_cat.qm'...
Removing translations equal to source text in 'C:/code/monero-gui/build/translations/monero-core_cat.qm'...
    Generated 241 translation(s) (241 finished and 0 unfinished)
    Ignored 166 untranslated source text(s)
Updating 'C:/code/monero-gui/build/translations/monero-core_cs.qm'...
Removing translations equal to source text in 'C:/code/monero-gui/build/translations/monero-core_cs.qm'...
    Generated 475 translation(s) (475 finished and 0 unfinished)
Updating 'C:/code/monero-gui/build/translations/monero-core_da.qm'...
Removing translations equal to source text in 'C:/code/monero-gui/build/translations/monero-core_da.qm'...
    Generated 442 translation(s) (442 finished and 0 unfinished)
Updating 'C:/code/monero-gui/build/translations/monero-core_de.qm'...
Removing translations equal to source text in 'C:/code/monero-gui/build/translations/monero-core_de.qm'...
    Generated 461 translation(s) (461 finished and 0 unfinished)
    Ignored 22 untranslated source text(s)
Updating 'C:/code/monero-gui/build/translations/monero-core_eo.qm'...
Removing translations equal to source text in 'C:/code/monero-gui/build/translations/monero-core_eo.qm'...
    Generated 479 translation(s) (479 finished and 0 unfinished)
    Ignored 2 untranslated source text(s)
Updating 'C:/code/monero-gui/build/translations/monero-core_es.qm'...
Removing translations equal to source text in 'C:/code/monero-gui/build/translations/monero-core_es.qm'...
    Generated 465 translation(s) (465 finished and 0 unfinished)
Updating 'C:/code/monero-gui/build/translations/monero-core_fi.qm'...
Removing translations equal to source text in 'C:/code/monero-gui/build/translations/monero-core_fi.qm'...
    Generated 126 translation(s) (126 finished and 0 unfinished)
    Ignored 315 untranslated source text(s)
Updating 'C:/code/monero-gui/build/translations/monero-core_fr.qm'...
Removing translations equal to source text in 'C:/code/monero-gui/build/translations/monero-core_fr.qm'...
    Generated 453 translation(s) (453 finished and 0 unfinished)
Updating 'C:/code/monero-gui/build/translations/monero-core_he.qm'...
Removing translations equal to source text in 'C:/code/monero-gui/build/translations/monero-core_he.qm'...
    Generated 467 translation(s) (467 finished and 0 unfinished)
    Ignored 19 untranslated source text(s)
Updating 'C:/code/monero-gui/build/translations/monero-core_hi.qm'...
Removing translations equal to source text in 'C:/code/monero-gui/build/translations/monero-core_hi.qm'...
    Generated 49 translation(s) (49 finished and 0 unfinished)
    Ignored 424 untranslated source text(s)
Updating 'C:/code/monero-gui/build/translations/monero-core_hr.qm'...
Removing translations equal to source text in 'C:/code/monero-gui/build/translations/monero-core_hr.qm'...
    Generated 365 translation(s) (365 finished and 0 unfinished)
    Ignored 104 untranslated source text(s)
Updating 'C:/code/monero-gui/build/translations/monero-core_id.qm'...
Removing translations equal to source text in 'C:/code/monero-gui/build/translations/monero-core_id.qm'...
    Generated 257 translation(s) (257 finished and 0 unfinished)
    Ignored 194 untranslated source text(s)
Updating 'C:/code/monero-gui/build/translations/monero-core_it.qm'...
Removing translations equal to source text in 'C:/code/monero-gui/build/translations/monero-core_it.qm'...
    Generated 466 translation(s) (466 finished and 0 unfinished)
Updating 'C:/code/monero-gui/build/translations/monero-core_ja.qm'...
Removing translations equal to source text in 'C:/code/monero-gui/build/translations/monero-core_ja.qm'...
    Generated 480 translation(s) (480 finished and 0 unfinished)
Updating 'C:/code/monero-gui/build/translations/monero-core_ko.qm'...
Removing translations equal to source text in 'C:/code/monero-gui/build/translations/monero-core_ko.qm'...
    Generated 276 translation(s) (276 finished and 0 unfinished)
    Ignored 170 untranslated source text(s)
Updating 'C:/code/monero-gui/build/translations/monero-core_nl.qm'...
Removing translations equal to source text in 'C:/code/monero-gui/build/translations/monero-core_nl.qm'...
    Generated 478 translation(s) (478 finished and 0 unfinished)
Updating 'C:/code/monero-gui/build/translations/monero-core_pl.qm'...
Removing translations equal to source text in 'C:/code/monero-gui/build/translations/monero-core_pl.qm'...
    Generated 476 translation(s) (476 finished and 0 unfinished)
Updating 'C:/code/monero-gui/build/translations/monero-core_pt-br.qm'...
Removing translations equal to source text in 'C:/code/monero-gui/build/translations/monero-core_pt-br.qm'...
    Generated 472 translation(s) (472 finished and 0 unfinished)
Updating 'C:/code/monero-gui/build/translations/monero-core_pt-pt.qm'...
Removing translations equal to source text in 'C:/code/monero-gui/build/translations/monero-core_pt-pt.qm'...
    Generated 464 translation(s) (464 finished and 0 unfinished)
Updating 'C:/code/monero-gui/build/translations/monero-core_ro.qm'...
Removing translations equal to source text in 'C:/code/monero-gui/build/translations/monero-core_ro.qm'...
    Generated 466 translation(s) (466 finished and 0 unfinished)
Updating 'C:/code/monero-gui/build/translations/monero-core_ru.qm'...
Removing translations equal to source text in 'C:/code/monero-gui/build/translations/monero-core_ru.qm'...
    Generated 479 translation(s) (479 finished and 0 unfinished)
    Ignored 12 untranslated source text(s)
Updating 'C:/code/monero-gui/build/translations/monero-core_sk.qm'...
Removing translations equal to source text in 'C:/code/monero-gui/build/translations/monero-core_sk.qm'...
    Generated 439 translation(s) (439 finished and 0 unfinished)
    Ignored 33 untranslated source text(s)
Updating 'C:/code/monero-gui/build/translations/monero-core_sl.qm'...
Removing translations equal to source text in 'C:/code/monero-gui/build/translations/monero-core_sl.qm'...
    Generated 318 translation(s) (318 finished and 0 unfinished)
    Ignored 132 untranslated source text(s)
Updating 'C:/code/monero-gui/build/translations/monero-core_sr.qm'...
Removing translations equal to source text in 'C:/code/monero-gui/build/translations/monero-core_sr.qm'...
    Generated 461 translation(s) (461 finished and 0 unfinished)
Updating 'C:/code/monero-gui/build/translations/monero-core_sv.qm'...
Removing translations equal to source text in 'C:/code/monero-gui/build/translations/monero-core_sv.qm'...
    Generated 468 translation(s) (468 finished and 0 unfinished)
Updating 'C:/code/monero-gui/build/translations/monero-core_tr.qm'...
Removing translations equal to source text in 'C:/code/monero-gui/build/translations/monero-core_tr.qm'...
    Generated 472 translation(s) (472 finished and 0 unfinished)
Updating 'C:/code/monero-gui/build/translations/monero-core_ua.qm'...
Removing translations equal to source text in 'C:/code/monero-gui/build/translations/monero-core_ua.qm'...
    Generated 369 translation(s) (369 finished and 0 unfinished)
    Ignored 114 untranslated source text(s)
Updating 'C:/code/monero-gui/build/translations/monero-core_zh-cn.qm'...
Removing translations equal to source text in 'C:/code/monero-gui/build/translations/monero-core_zh-cn.qm'...
    Generated 478 translation(s) (478 finished and 0 unfinished)
Updating 'C:/code/monero-gui/build/translations/monero-core_zh-tw.qm'...
Removing translations equal to source text in 'C:/code/monero-gui/build/translations/monero-core_zh-tw.qm'...
    Generated 481 translation(s) (481 finished and 0 unfinished)
Updating 'C:/code/monero-gui/build/translations/monero-core_ar.qm'...
    Generated 288 translation(s) (258 finished and 30 unfinished)
    Ignored 207 untranslated source text(s)
Updating 'C:/code/monero-gui/build/translations/monero-core_cat.qm'...
    Generated 329 translation(s) (263 finished and 66 unfinished)
    Ignored 166 untranslated source text(s)
Updating 'C:/code/monero-gui/build/translations/monero-core_cs.qm'...
    Generated 498 translation(s) (498 finished and 0 unfinished)
Updating 'C:/code/monero-gui/build/translations/monero-core_da.qm'...
    Generated 495 translation(s) (495 finished and 0 unfinished)
Updating 'C:/code/monero-gui/build/translations/monero-core_de.qm'...
    Generated 473 translation(s) (473 finished and 0 unfinished)
    Ignored 22 untranslated source text(s)
Updating 'C:/code/monero-gui/build/translations/monero-core_eo.qm'...
    Generated 493 translation(s) (493 finished and 0 unfinished)
    Ignored 2 untranslated source text(s)
Updating 'C:/code/monero-gui/build/translations/monero-core_es.qm'...
    Generated 495 translation(s) (495 finished and 0 unfinished)
Updating 'C:/code/monero-gui/build/translations/monero-core_fi.qm'...
    Generated 180 translation(s) (137 finished and 43 unfinished)
    Ignored 315 untranslated source text(s)
Updating 'C:/code/monero-gui/build/translations/monero-core_fr.qm'...
    Generated 495 translation(s) (495 finished and 0 unfinished)
Updating 'C:/code/monero-gui/build/translations/monero-core_he.qm'...
    Generated 476 translation(s) (476 finished and 0 unfinished)
    Ignored 19 untranslated source text(s)
Updating 'C:/code/monero-gui/build/translations/monero-core_hi.qm'...
    Generated 71 translation(s) (50 finished and 21 unfinished)
    Ignored 424 untranslated source text(s)
Updating 'C:/code/monero-gui/build/translations/monero-core_hr.qm'...
    Generated 391 translation(s) (381 finished and 10 unfinished)
    Ignored 104 untranslated source text(s)
Updating 'C:/code/monero-gui/build/translations/monero-core_id.qm'...
    Generated 301 translation(s) (270 finished and 31 unfinished)
    Ignored 194 untranslated source text(s)
Updating 'C:/code/monero-gui/build/translations/monero-core_it.qm'...
    Generated 495 translation(s) (495 finished and 0 unfinished)
Updating 'C:/code/monero-gui/build/translations/monero-core_ja.qm'...
    Generated 495 translation(s) (495 finished and 0 unfinished)
Updating 'C:/code/monero-gui/build/translations/monero-core_ko.qm'...
    Generated 325 translation(s) (278 finished and 47 unfinished)
    Ignored 170 untranslated source text(s)
Updating 'C:/code/monero-gui/build/translations/monero-core_nl.qm'...
    Generated 495 translation(s) (495 finished and 0 unfinished)
Updating 'C:/code/monero-gui/build/translations/monero-core_pl.qm'...
    Generated 495 translation(s) (495 finished and 0 unfinished)
Updating 'C:/code/monero-gui/build/translations/monero-core_pt-br.qm'...
    Generated 495 translation(s) (495 finished and 0 unfinished)
Updating 'C:/code/monero-gui/build/translations/monero-core_pt-pt.qm'...
    Generated 495 translation(s) (493 finished and 2 unfinished)
Updating 'C:/code/monero-gui/build/translations/monero-core_ro.qm'...
    Generated 495 translation(s) (495 finished and 0 unfinished)
Updating 'C:/code/monero-gui/build/translations/monero-core_ru.qm'...
    Generated 483 translation(s) (481 finished and 2 unfinished)
    Ignored 12 untranslated source text(s)
Updating 'C:/code/monero-gui/build/translations/monero-core_sk.qm'...
    Generated 462 translation(s) (461 finished and 1 unfinished)
    Ignored 33 untranslated source text(s)
Updating 'C:/code/monero-gui/build/translations/monero-core_sl.qm'...
    Generated 363 translation(s) (320 finished and 43 unfinished)
    Ignored 132 untranslated source text(s)
Updating 'C:/code/monero-gui/build/translations/monero-core_sr.qm'...
    Generated 495 translation(s) (495 finished and 0 unfinished)
Updating 'C:/code/monero-gui/build/translations/monero-core_sv.qm'...
    Generated 495 translation(s) (495 finished and 0 unfinished)
Updating 'C:/code/monero-gui/build/translations/monero-core_tr.qm'...
    Generated 495 translation(s) (495 finished and 0 unfinished)
Updating 'C:/code/monero-gui/build/translations/monero-core_ua.qm'...
    Generated 381 translation(s) (371 finished and 10 unfinished)
    Ignored 114 untranslated source text(s)
Updating 'C:/code/monero-gui/build/translations/monero-core_zh-cn.qm'...
    Generated 495 translation(s) (495 finished and 0 unfinished)
Updating 'C:/code/monero-gui/build/translations/monero-core_zh-tw.qm'...
    Generated 495 translation(s) (495 finished and 0 unfinished)
Project MESSAGE: Host is 64bit
Project MESSAGE: Target is 32bit
Project MESSAGE: Host is 64bit
Project MESSAGE: Target is 32bit
Project MESSAGE: Host is 64bit
Project MESSAGE: Target is 32bit
WARNING: Failure to find: debug/monero-wallet-gui_resource_res.o
make -f Makefile.Release
make[1]: Entering directory '/c/code/monero-gui/build'
C:/msys64/mingw64/bin\lrelease.exe -compress -nounfinished -removeidentical ../translations/monero-core_ar.ts -qm C:/code/monero-gui/build/translations/monero-core_ar.qm
Updating 'C:/code/monero-gui/build/translations/monero-core_ar.qm'...
Removing translations equal to source text in 'C:/code/monero-gui/build/translations/monero-core_ar.qm'...
    Generated 257 translation(s) (257 finished and 0 unfinished)
    Ignored 207 untranslated source text(s)
C:/msys64/mingw64/bin\lrelease.exe -compress -nounfinished -removeidentical ../translations/monero-core_cat.ts -qm C:/code/monero-gui/build/translations/monero-core_cat.qm
Updating 'C:/code/monero-gui/build/translations/monero-core_cat.qm'...
Removing translations equal to source text in 'C:/code/monero-gui/build/translations/monero-core_cat.qm'...
    Generated 241 translation(s) (241 finished and 0 unfinished)
    Ignored 166 untranslated source text(s)
C:/msys64/mingw64/bin\lrelease.exe -compress -nounfinished -removeidentical ../translations/monero-core_cs.ts -qm C:/code/monero-gui/build/translations/monero-core_cs.qm
Updating 'C:/code/monero-gui/build/translations/monero-core_cs.qm'...
Removing translations equal to source text in 'C:/code/monero-gui/build/translations/monero-core_cs.qm'...
    Generated 475 translation(s) (475 finished and 0 unfinished)
C:/msys64/mingw64/bin\lrelease.exe -compress -nounfinished -removeidentical ../translations/monero-core_da.ts -qm C:/code/monero-gui/build/translations/monero-core_da.qm
Updating 'C:/code/monero-gui/build/translations/monero-core_da.qm'...
Removing translations equal to source text in 'C:/code/monero-gui/build/translations/monero-core_da.qm'...
    Generated 442 translation(s) (442 finished and 0 unfinished)
C:/msys64/mingw64/bin\lrelease.exe -compress -nounfinished -removeidentical ../translations/monero-core_de.ts -qm C:/code/monero-gui/build/translations/monero-core_de.qm
Updating 'C:/code/monero-gui/build/translations/monero-core_de.qm'...
Removing translations equal to source text in 'C:/code/monero-gui/build/translations/monero-core_de.qm'...
    Generated 461 translation(s) (461 finished and 0 unfinished)
    Ignored 22 untranslated source text(s)
C:/msys64/mingw64/bin\lrelease.exe -compress -nounfinished -removeidentical ../translations/monero-core_eo.ts -qm C:/code/monero-gui/build/translations/monero-core_eo.qm
Updating 'C:/code/monero-gui/build/translations/monero-core_eo.qm'...
Removing translations equal to source text in 'C:/code/monero-gui/build/translations/monero-core_eo.qm'...
    Generated 479 translation(s) (479 finished and 0 unfinished)
    Ignored 2 untranslated source text(s)
C:/msys64/mingw64/bin\lrelease.exe -compress -nounfinished -removeidentical ../translations/monero-core_es.ts -qm C:/code/monero-gui/build/translations/monero-core_es.qm
Updating 'C:/code/monero-gui/build/translations/monero-core_es.qm'...
Removing translations equal to source text in 'C:/code/monero-gui/build/translations/monero-core_es.qm'...
    Generated 465 translation(s) (465 finished and 0 unfinished)
C:/msys64/mingw64/bin\lrelease.exe -compress -nounfinished -removeidentical ../translations/monero-core_fi.ts -qm C:/code/monero-gui/build/translations/monero-core_fi.qm
Updating 'C:/code/monero-gui/build/translations/monero-core_fi.qm'...
Removing translations equal to source text in 'C:/code/monero-gui/build/translations/monero-core_fi.qm'...
    Generated 126 translation(s) (126 finished and 0 unfinished)
    Ignored 315 untranslated source text(s)
C:/msys64/mingw64/bin\lrelease.exe -compress -nounfinished -removeidentical ../translations/monero-core_fr.ts -qm C:/code/monero-gui/build/translations/monero-core_fr.qm
Updating 'C:/code/monero-gui/build/translations/monero-core_fr.qm'...
Removing translations equal to source text in 'C:/code/monero-gui/build/translations/monero-core_fr.qm'...
    Generated 453 translation(s) (453 finished and 0 unfinished)
C:/msys64/mingw64/bin\lrelease.exe -compress -nounfinished -removeidentical ../translations/monero-core_he.ts -qm C:/code/monero-gui/build/translations/monero-core_he.qm
Updating 'C:/code/monero-gui/build/translations/monero-core_he.qm'...
Removing translations equal to source text in 'C:/code/monero-gui/build/translations/monero-core_he.qm'...
    Generated 467 translation(s) (467 finished and 0 unfinished)
    Ignored 19 untranslated source text(s)
C:/msys64/mingw64/bin\lrelease.exe -compress -nounfinished -removeidentical ../translations/monero-core_hi.ts -qm C:/code/monero-gui/build/translations/monero-core_hi.qm
Updating 'C:/code/monero-gui/build/translations/monero-core_hi.qm'...
Removing translations equal to source text in 'C:/code/monero-gui/build/translations/monero-core_hi.qm'...
    Generated 49 translation(s) (49 finished and 0 unfinished)
    Ignored 424 untranslated source text(s)
C:/msys64/mingw64/bin\lrelease.exe -compress -nounfinished -removeidentical ../translations/monero-core_hr.ts -qm C:/code/monero-gui/build/translations/monero-core_hr.qm
Updating 'C:/code/monero-gui/build/translations/monero-core_hr.qm'...
Removing translations equal to source text in 'C:/code/monero-gui/build/translations/monero-core_hr.qm'...
    Generated 365 translation(s) (365 finished and 0 unfinished)
    Ignored 104 untranslated source text(s)
C:/msys64/mingw64/bin\lrelease.exe -compress -nounfinished -removeidentical ../translations/monero-core_id.ts -qm C:/code/monero-gui/build/translations/monero-core_id.qm
Updating 'C:/code/monero-gui/build/translations/monero-core_id.qm'...
Removing translations equal to source text in 'C:/code/monero-gui/build/translations/monero-core_id.qm'...
    Generated 257 translation(s) (257 finished and 0 unfinished)
    Ignored 194 untranslated source text(s)
C:/msys64/mingw64/bin\lrelease.exe -compress -nounfinished -removeidentical ../translations/monero-core_it.ts -qm C:/code/monero-gui/build/translations/monero-core_it.qm
Updating 'C:/code/monero-gui/build/translations/monero-core_it.qm'...
Removing translations equal to source text in 'C:/code/monero-gui/build/translations/monero-core_it.qm'...
    Generated 466 translation(s) (466 finished and 0 unfinished)
C:/msys64/mingw64/bin\lrelease.exe -compress -nounfinished -removeidentical ../translations/monero-core_ja.ts -qm C:/code/monero-gui/build/translations/monero-core_ja.qm
Updating 'C:/code/monero-gui/build/translations/monero-core_ja.qm'...
Removing translations equal to source text in 'C:/code/monero-gui/build/translations/monero-core_ja.qm'...
    Generated 480 translation(s) (480 finished and 0 unfinished)
C:/msys64/mingw64/bin\lrelease.exe -compress -nounfinished -removeidentical ../translations/monero-core_ko.ts -qm C:/code/monero-gui/build/translations/monero-core_ko.qm
Updating 'C:/code/monero-gui/build/translations/monero-core_ko.qm'...
Removing translations equal to source text in 'C:/code/monero-gui/build/translations/monero-core_ko.qm'...
    Generated 276 translation(s) (276 finished and 0 unfinished)
    Ignored 170 untranslated source text(s)
C:/msys64/mingw64/bin\lrelease.exe -compress -nounfinished -removeidentical ../translations/monero-core_nl.ts -qm C:/code/monero-gui/build/translations/monero-core_nl.qm
Updating 'C:/code/monero-gui/build/translations/monero-core_nl.qm'...
Removing translations equal to source text in 'C:/code/monero-gui/build/translations/monero-core_nl.qm'...
    Generated 478 translation(s) (478 finished and 0 unfinished)
C:/msys64/mingw64/bin\lrelease.exe -compress -nounfinished -removeidentical ../translations/monero-core_pl.ts -qm C:/code/monero-gui/build/translations/monero-core_pl.qm
Updating 'C:/code/monero-gui/build/translations/monero-core_pl.qm'...
Removing translations equal to source text in 'C:/code/monero-gui/build/translations/monero-core_pl.qm'...
    Generated 476 translation(s) (476 finished and 0 unfinished)
C:/msys64/mingw64/bin\lrelease.exe -compress -nounfinished -removeidentical ../translations/monero-core_pt-br.ts -qm C:/code/monero-gui/build/translations/monero-core_pt-br.qm
Updating 'C:/code/monero-gui/build/translations/monero-core_pt-br.qm'...
Removing translations equal to source text in 'C:/code/monero-gui/build/translations/monero-core_pt-br.qm'...
    Generated 472 translation(s) (472 finished and 0 unfinished)
C:/msys64/mingw64/bin\lrelease.exe -compress -nounfinished -removeidentical ../translations/monero-core_pt-pt.ts -qm C:/code/monero-gui/build/translations/monero-core_pt-pt.qm
Updating 'C:/code/monero-gui/build/translations/monero-core_pt-pt.qm'...
Removing translations equal to source text in 'C:/code/monero-gui/build/translations/monero-core_pt-pt.qm'...
    Generated 464 translation(s) (464 finished and 0 unfinished)
C:/msys64/mingw64/bin\lrelease.exe -compress -nounfinished -removeidentical ../translations/monero-core_ro.ts -qm C:/code/monero-gui/build/translations/monero-core_ro.qm
Updating 'C:/code/monero-gui/build/translations/monero-core_ro.qm'...
Removing translations equal to source text in 'C:/code/monero-gui/build/translations/monero-core_ro.qm'...
    Generated 466 translation(s) (466 finished and 0 unfinished)
C:/msys64/mingw64/bin\lrelease.exe -compress -nounfinished -removeidentical ../translations/monero-core_ru.ts -qm C:/code/monero-gui/build/translations/monero-core_ru.qm
Updating 'C:/code/monero-gui/build/translations/monero-core_ru.qm'...
Removing translations equal to source text in 'C:/code/monero-gui/build/translations/monero-core_ru.qm'...
    Generated 479 translation(s) (479 finished and 0 unfinished)
    Ignored 12 untranslated source text(s)
C:/msys64/mingw64/bin\lrelease.exe -compress -nounfinished -removeidentical ../translations/monero-core_sk.ts -qm C:/code/monero-gui/build/translations/monero-core_sk.qm
Updating 'C:/code/monero-gui/build/translations/monero-core_sk.qm'...
Removing translations equal to source text in 'C:/code/monero-gui/build/translations/monero-core_sk.qm'...
    Generated 439 translation(s) (439 finished and 0 unfinished)
    Ignored 33 untranslated source text(s)
C:/msys64/mingw64/bin\lrelease.exe -compress -nounfinished -removeidentical ../translations/monero-core_sl.ts -qm C:/code/monero-gui/build/translations/monero-core_sl.qm
Updating 'C:/code/monero-gui/build/translations/monero-core_sl.qm'...
Removing translations equal to source text in 'C:/code/monero-gui/build/translations/monero-core_sl.qm'...
    Generated 318 translation(s) (318 finished and 0 unfinished)
    Ignored 132 untranslated source text(s)
C:/msys64/mingw64/bin\lrelease.exe -compress -nounfinished -removeidentical ../translations/monero-core_sr.ts -qm C:/code/monero-gui/build/translations/monero-core_sr.qm
Updating 'C:/code/monero-gui/build/translations/monero-core_sr.qm'...
Removing translations equal to source text in 'C:/code/monero-gui/build/translations/monero-core_sr.qm'...
    Generated 461 translation(s) (461 finished and 0 unfinished)
C:/msys64/mingw64/bin\lrelease.exe -compress -nounfinished -removeidentical ../translations/monero-core_sv.ts -qm C:/code/monero-gui/build/translations/monero-core_sv.qm
Updating 'C:/code/monero-gui/build/translations/monero-core_sv.qm'...
Removing translations equal to source text in 'C:/code/monero-gui/build/translations/monero-core_sv.qm'...
    Generated 468 translation(s) (468 finished and 0 unfinished)
C:/msys64/mingw64/bin\lrelease.exe -compress -nounfinished -removeidentical ../translations/monero-core_tr.ts -qm C:/code/monero-gui/build/translations/monero-core_tr.qm
Updating 'C:/code/monero-gui/build/translations/monero-core_tr.qm'...
Removing translations equal to source text in 'C:/code/monero-gui/build/translations/monero-core_tr.qm'...
    Generated 472 translation(s) (472 finished and 0 unfinished)
C:/msys64/mingw64/bin\lrelease.exe -compress -nounfinished -removeidentical ../translations/monero-core_ua.ts -qm C:/code/monero-gui/build/translations/monero-core_ua.qm
Updating 'C:/code/monero-gui/build/translations/monero-core_ua.qm'...
Removing translations equal to source text in 'C:/code/monero-gui/build/translations/monero-core_ua.qm'...
    Generated 369 translation(s) (369 finished and 0 unfinished)
    Ignored 114 untranslated source text(s)
C:/msys64/mingw64/bin\lrelease.exe -compress -nounfinished -removeidentical ../translations/monero-core_zh-cn.ts -qm C:/code/monero-gui/build/translations/monero-core_zh-cn.qm
Updating 'C:/code/monero-gui/build/translations/monero-core_zh-cn.qm'...
Removing translations equal to source text in 'C:/code/monero-gui/build/translations/monero-core_zh-cn.qm'...
    Generated 478 translation(s) (478 finished and 0 unfinished)
C:/msys64/mingw64/bin\lrelease.exe -compress -nounfinished -removeidentical ../translations/monero-core_zh-tw.ts -qm C:/code/monero-gui/build/translations/monero-core_zh-tw.qm
Updating 'C:/code/monero-gui/build/translations/monero-core_zh-tw.qm'...
Removing translations equal to source text in 'C:/code/monero-gui/build/translations/monero-core_zh-tw.qm'...
    Generated 481 translation(s) (481 finished and 0 unfinished)
make[1]: *** No rule to make target '../../../../msys64/mingw64/include/QtWidgets/QApplication', needed by 'release/main.o'.  Stop.
make[1]: Leaving directory '/c/code/monero-gui/build'
make: *** [Makefile:36: release] Error 2
```

# Discussion History
## barretts | 2018-06-01T19:50:23+00:00
Tried the same steps on a fresh install of Windows 7 and get the same error.

## barretts | 2018-06-05T01:35:01+00:00
Trying to figure out what is wrong I changed some parameters on make to debug but I just don't understand what I'm looking at.

```
      Considering target file 'release/main.o'.
       File 'release/main.o' does not exist.
        Considering target file '../main.cpp'.
         Looking for an implicit rule for '../main.cpp'.
         No implicit rule found for '../main.cpp'.
         Finished prerequisites of target file '../main.cpp'.
        No need to remake target '../main.cpp'.
        Considering target file '../../../../msys64/mingw64/include/QtWidgets/QApplication'.
         File '../../../../msys64/mingw64/include/QtWidgets/QApplication' does not exist.
         Looking for an implicit rule for '../../../../msys64/mingw64/include/QtWidgets/QApplication'.
         No implicit rule found for '../../../../msys64/mingw64/include/QtWidgets/QApplication'.
         Finished prerequisites of target file '../../../../msys64/mingw64/include/QtWidgets/QApplication'.
        Must remake target '../../../../msys64/mingw64/include/QtWidgets/QApplication'.
make[1]: Entering directory '/c/code/monero-gui/build'
make[1]: *** No rule to make target '../../../../msys64/mingw64/include/QtWidgets/QApplication', needed by 'release/main.o'.  Stop.
make[1]: Leaving directory '/c/code/monero-gui/build'
Reaping losing child 0x600064b00 PID 18420
make: *** [Makefile:36: release] Error 2
Removing child 0x600064b00 PID 18420 from chain.
```

But I know that `/msys64/mingw64/include/QtWidgets/QApplication` does exist, at least it exists at `/c/msys64/mingw64/include/QtWidgets/QApplication`

From the build folder running `notepad ../../../../msys64/mingw64/include/QtWidgets/QApplication` works as well.

## barretts | 2018-06-05T04:58:01+00:00
I tried installing older builds of qt5 thinking that might change the outcome of the run but no luck going back to 5.10-1 or 5.9

## pazos | 2018-06-05T20:16:30+00:00
Did you install qt outside msys? What is the output of `qmake -v`

Are you able to compile other project or example, like [this](https://doc.qt.io/archives/3.3/tutorial1-01.html)?

## barretts | 2018-06-06T14:40:50+00:00
```
$ qmake -v
QMake version 3.1
Using Qt version 5.10.1 in C:/msys64/mingw64/lib
```

You had the right idea and I'm unable to compile that simple tutorial!
```
g++ -c -fno-keep-inline-dllexport -march=nocona -mtune=core2 -Wa,-mbig-obj -g -Wall -W -Wextra -fexceptions -mthreads -DUNICODE -D_UNICODE -DWIN32 -DQT_DEPRECATED_WARNINGS -DQT_GUI_LIB -DQT_CORE_LIB -DQT_NEEDS_QMAIN -I. -I. -I../../msys64/mingw64/include/QtGui -I../../msys64/mingw64/include/QtCore -Idebug -I../../msys64/mingw64/include -I../../msys64/mingw64/share/qt5/mkspecs/win32-g++  -o debug/main.o main.cpp
main.cpp:7:10: fatal error: qapplication.h: No such file or directory
```

I'm off to look into that now. Thanks for the lead.

## barretts | 2018-06-12T16:35:50+00:00
Unfortunately that tutorial is woefully out of date and took me on a pretty wild goose chase trying to make a Qt 3 project run in Qt 5.

I was able to follow and build this tutorial though http://zetcode.com/gui/qt5/menusandtoolbars/

## DNCloud-open | 2018-07-30T18:43:22+00:00
install the msys2 into C:\
 `cd C:`
`git clone https://github.com/monero-project/monero-gui.git`
`cd monero-gui`
`./bulid.sh`
Make sure that the msys2 and the monero-gui are in the C disk.

sorry，My English is poor
@barretts 




## kamuluprashanth | 2018-08-14T11:29:45+00:00
you must and should have the software msys64 in your system of local disk C

then open the MSYS2 MINGW 64 bit shell. if you are using 64 bit windows 10 version otherwise you choose MSYS2 MINGW 32 bit shell from windows 10  32 bit

then clone the repository
git clone https://github.com/monero-project/monero-gui.git
cd monero-gui
./bulid.sh

after running above process i fixed the above issue i think it is helpful.

## mmbyday | 2018-12-17T08:22:41+00:00
+resolved

## dEBRUYNE-1 | 2018-12-17T08:31:58+00:00
+resolved

## naughtyfox | 2019-08-28T14:00:14+00:00
Hi!

I have the same problem right now. I have `MSYS2` and `monero-gui` on the root of `C:\`. How did you solve your problem?

## xiphon | 2019-08-28T14:40:17+00:00
> I have the same problem right now. I have `MSYS2` and `monero-gui` on the root of `C:\`. How did you solve your problem?

There is a bug in the build process right now, `monero-gui` repo can't be a top level directory, move it into some subdirectory as a workaround.


## naughtyfox | 2019-08-28T14:42:51+00:00
I already did, I moved it to `/c/exa/monero-gui` and got the same result


## naughtyfox | 2019-08-28T14:46:03+00:00
I think the problem is in relative path `../../../../msys64/mingw64/include/QtWidgets/QApplication` which is generated by `qmake`. It's always one level more than it should be. I don't know how to fight this problem.

Instead of `../../../../msys64/mingw64/include/QtWidgets/QApplication` it should be `../../../msys64/mingw64/include/QtWidgets/QApplication`

# Action History
- Created by: barretts | 2018-06-01T14:05:28+00:00
- Closed at: 2018-12-17T09:18:35+00:00
