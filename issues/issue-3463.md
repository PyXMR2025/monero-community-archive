---
title: Can't compile v0.12.0 release branch
source_url: https://github.com/monero-project/monero/issues/3463
author: gituser
assignees: []
labels:
- invalid
created_at: '2018-03-21T15:34:35+00:00'
updated_at: '2018-04-09T22:06:08+00:00'
type: issue
status: closed
closed_at: '2018-03-27T23:56:45+00:00'
---

# Original Description
Trying to build new `v0.12.0 branch` but it's not working for me (before it worked fine).

```
export BOOST_ROOT=/home/build/monero/boost/boost.build DEVELOPER_LOCAL_TOOLS=1
make release-static
```

seems it's missing `build/release/version.cpp` file for some reason.. not sure why

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

# Discussion History
## moneromooo-monero | 2018-03-21T16:16:29+00:00
What cmake version are you using ?
Can you paste the contents of /home/build/monero/source/build/release/CMakeFiles/CMakeError.log please.

About BOOST_ROOT, that's a boost thing, monero does not do anything with it.

## hyc | 2018-03-21T16:21:57+00:00
The missing version.cpp has actually been a problem on master for the past several months. The rule to generate it has gotten moved too late in the set of CMake files. I was investigating it earlier but haven't PR'd a fix yet. You can temporarily workaround it by doing a `touch build/release/version.cpp` - it will get regenerated with the correct contents later during the build.

## gituser | 2018-03-21T16:26:40+00:00
@hyc, now it's compiling thank you.

@moneromooo-monero it's very big file, i can upload it somewhere and post a link to this issue in a moment.


## moneromooo-monero | 2018-03-21T16:33:48+00:00
No need, since hyc know the cause.

## gituser | 2018-03-21T16:35:24+00:00
I was too early to celebrate.

The boost is self-compiled `v1.62.0`.

Now it failed with:

```
Scanning dependencies of target obj_wallet
make[3]: Leaving directory '/home/build/monero/source/build/release'
make[3]: Entering directory '/home/build/monero/source/build/release'
[ 89%] Building CXX object src/wallet/CMakeFiles/obj_wallet.dir/wallet2.cpp.o
[ 89%] Building CXX object src/wallet/CMakeFiles/obj_wallet.dir/wallet_args.cpp.o
[ 90%] Building CXX object src/wallet/CMakeFiles/obj_wallet.dir/ringdb.cpp.o
[ 90%] Building CXX object src/wallet/CMakeFiles/obj_wallet.dir/node_rpc_proxy.cpp.o
make[3]: Leaving directory '/home/build/monero/source/build/release'
[ 90%] Built target obj_wallet
make[3]: Entering directory '/home/build/monero/source/build/release'
Scanning dependencies of target wallet
make[3]: Leaving directory '/home/build/monero/source/build/release'
make[3]: Entering directory '/home/build/monero/source/build/release'
Linking CXX static library ../../lib/libwallet.a
make[3]: Leaving directory '/home/build/monero/source/build/release'
[ 90%] Built target wallet
make[3]: Entering directory '/home/build/monero/source/build/release'
Scanning dependencies of target wallet_rpc_server
make[3]: Leaving directory '/home/build/monero/source/build/release'
make[3]: Entering directory '/home/build/monero/source/build/release'
[ 91%] Building CXX object src/wallet/CMakeFiles/wallet_rpc_server.dir/wallet_rpc_server.cpp.o
Linking CXX executable ../../bin/monero-wallet-rpc
/usr/bin/ld: /home/build/monero/boost/boost.build/lib/libboost_chrono.a(chrono.o): relocation R_X86_64_32 against `.rodata.str1.1' can not be used when making a shared object; recompile with -fPIC
/home/build/monero/boost/boost.build/lib/libboost_chrono.a: error adding symbols: Bad value
collect2: error: ld returned 1 exit status
src/wallet/CMakeFiles/wallet_rpc_server.dir/build.make:123: recipe for target 'bin/monero-wallet-rpc' failed
make[3]: *** [bin/monero-wallet-rpc] Error 1
make[3]: Leaving directory '/home/build/monero/source/build/release'
CMakeFiles/Makefile2:2209: recipe for target 'src/wallet/CMakeFiles/wallet_rpc_server.dir/all' failed
make[2]: *** [src/wallet/CMakeFiles/wallet_rpc_server.dir/all] Error 2
make[2]: Leaving directory '/home/build/monero/source/build/release'
Makefile:127: recipe for target 'all' failed
make[1]: *** [all] Error 2
make[1]: Leaving directory '/home/build/monero/source/build/release'
Makefile:68: recipe for target 'release-static' failed
make: *** [release-static] Error 2
Build Failed.
```

## hyc | 2018-03-21T16:37:07+00:00
@gituser - on your latest paste, this means you need to recompile your Boost libraries with -fPIC.

As for the original problem, can you please delete your build/release tree and try again with my patch in #3466 and tell me if the version.cpp problem is fixed for you. It works for me.

## gituser | 2018-03-21T16:40:13+00:00
@hyc, do I need to build boost like this:

```
# Start building boost
echo 'using clang : : c++ : <cxxflags>"-fvisibility=hidden -fPIC" <linkflags>"" <archiver>"ar" <striper>"strip"  <ranlib>"ranlib" <rc>"" : ;' > user-config.jam
./bootstrap.sh --without-icu --with-libraries=chrono,filesystem,program_options,system,thread,test,date_time,regex,serialization,locale --with-toolset=clang
./b2 toolset=clang cxxflags="-stdlib=libc++" linkflags="-stdlib=libc++" -sICONV_PATH=/usr/local
doas ./b2 -d0 runtime-link=shared threadapi=pthread threading=multi link=static variant=release --layout=tagged --build-type=complete --user-config=user-config.jam -sNO_BZIP2=1 -sICONV_PATH=/usr/local --prefix=/usr/local install
```
or just use `link=static` should be enough?

>As for the original problem, can you please delete your build/release tree and try again with my patch in #3466 and tell me if the version.cpp problem is fixed for you. It works for me.

Yes, this patch fixes the issue for me.

## moneromooo-monero | 2018-03-21T16:43:56+00:00
add " -fPIC -DPIC " in the cxxflags.

## gituser | 2018-03-22T02:26:39+00:00
>add " -fPIC -DPIC " in the cxxflags.

@moneromooo-monero I've tried, but still no luck :/

here is how I built boost:

```
./b2 cxxflags="-fPIC -DPIC" --prefix=/home/build/monero/boost/boost.build link=static install
```

Now it fails with `libssl` error:

```
[ 89%] Building CXX object src/wallet/CMakeFiles/wallet_rpc_server.dir/wallet_rpc_server.cpp.o
Linking CXX executable ../../bin/monero-wallet-rpc
/usr/bin/ld: /usr/lib/gcc/x86_64-linux-gnu/4.9/../../../x86_64-linux-gnu/libssl.a(s23_meth.o): relocation R_X86_64_32 against `.rodata' can not be used when making a shared object; recompile with -fPIC
/usr/lib/gcc/x86_64-linux-gnu/4.9/../../../x86_64-linux-gnu/libssl.a: error adding symbols: Bad value
collect2: error: ld returned 1 exit status
src/wallet/CMakeFiles/wallet_rpc_server.dir/build.make:123: recipe for target 'bin/monero-wallet-rpc' failed
make[3]: *** [bin/monero-wallet-rpc] Error 1
make[3]: Leaving directory '/home/build/monero/source/build/release'
CMakeFiles/Makefile2:2209: recipe for target 'src/wallet/CMakeFiles/wallet_rpc_server.dir/all' failed
make[2]: *** [src/wallet/CMakeFiles/wallet_rpc_server.dir/all] Error 2
make[2]: Leaving directory '/home/build/monero/source/build/release'
Makefile:127: recipe for target 'all' failed
make[1]: *** [all] Error 2
make[1]: Leaving directory '/home/build/monero/source/build/release'
Makefile:68: recipe for target 'release-static' failed
make: *** [release-static] Error 2
Build Failed.
```


## moneromooo-monero | 2018-03-22T08:36:08+00:00
That's the same error, isn't it ? Did you build libssl with fPIC ?

## gituser | 2018-03-22T12:51:56+00:00
@moneromooo-monero no it isn't. 

i'm using stock libssl from debian and before it worked just fine.

## lacksfish | 2018-03-24T02:31:29+00:00
So I am also building either `master` or `release-v0.12` and I end up with the following error message. I know it is a different error message but I figured as this is an issue about not being able to  build I might as well share my finding here. Was able to build in the past, so this is new..


From `release-v12.0`:
```
make[3]: Entering directory '/storage/github/monero/build/release'
[ 37%] Building CXX object tests/fuzz/CMakeFiles/http-client_fuzz_tests.dir/http-client.cpp.o
[ 38%] Building CXX object tests/fuzz/CMakeFiles/parse-url_fuzz_tests.dir/fuzzer.cpp.o
[ 38%] Linking CXX executable parse-url_fuzz_tests
CMakeFiles/parse-url_fuzz_tests.dir/parse_url.cpp.o: In function `boost::re_detail_106501::perl_matcher<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > >, boost::regex_traits<char, boost::cpp_regex_traits<char> > >::unwind_extra_block(bool)':
parse_url.cpp:(.text._ZN5boost16re_detail_10650112perl_matcherIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEESaINS_9sub_matchISC_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE18unwind_extra_blockEb[_ZN5boost16re_detail_10650112perl_matcherIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEESaINS_9sub_matchISC_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE18unwind_extra_blockEb]+0x2c): undefined reference to `boost::re_detail_106501::put_mem_block(void*)'
CMakeFiles/parse-url_fuzz_tests.dir/parse_url.cpp.o: In function `__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > boost::re_detail_106501::re_is_set_member<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, char, boost::regex_traits<char, boost::cpp_regex_traits<char> >, unsigned int>(__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, __gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, boost::re_detail_106501::re_set_long<unsigned int> const*, boost::re_detail_106501::regex_data<char, boost::regex_traits<char, boost::cpp_regex_traits<char> > > const&, bool)':
parse_url.cpp:(.text._ZN5boost16re_detail_10650116re_is_set_memberIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEEcNS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEjEET_SH_SH_PKNS0_11re_set_longIT2_EERKNS0_10regex_dataIT0_T1_EEb[_ZN5boost16re_detail_10650116re_is_set_memberIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEEcNS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEjEET_SH_SH_PKNS0_11re_set_longIT2_EERKNS0_10regex_dataIT0_T1_EEb]+0x15e): undefined reference to `boost::re_detail_106501::cpp_regex_traits_implementation<char>::transform_primary(char const*, char const*) const'
parse_url.cpp:(.text._ZN5boost16re_detail_10650116re_is_set_memberIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEEcNS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEjEET_SH_SH_PKNS0_11re_set_longIT2_EERKNS0_10regex_dataIT0_T1_EEb[_ZN5boost16re_detail_10650116re_is_set_memberIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEEcNS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEjEET_SH_SH_PKNS0_11re_set_longIT2_EERKNS0_10regex_dataIT0_T1_EEb]+0x34f): undefined reference to `boost::re_detail_106501::cpp_regex_traits_implementation<char>::transform(char const*, char const*) const'
CMakeFiles/parse-url_fuzz_tests.dir/parse_url.cpp.o: In function `boost::re_detail_106501::perl_matcher<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > >, boost::regex_traits<char, boost::cpp_regex_traits<char> > >::find_imp()':
parse_url.cpp:(.text._ZN5boost16re_detail_10650112perl_matcherIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEESaINS_9sub_matchISC_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE8find_impEv[_ZN5boost16re_detail_10650112perl_matcherIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEESaINS_9sub_matchISC_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE8find_impEv]+0x1c): undefined reference to `boost::re_detail_106501::get_mem_block()'
parse_url.cpp:(.text._ZN5boost16re_detail_10650112perl_matcherIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEESaINS_9sub_matchISC_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE8find_impEv[_ZN5boost16re_detail_10650112perl_matcherIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEESaINS_9sub_matchISC_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE8find_impEv]+0x279): undefined reference to `boost::re_detail_106501::verify_options(unsigned int, boost::regex_constants::_match_flags)'
parse_url.cpp:(.text._ZN5boost16re_detail_10650112perl_matcherIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEESaINS_9sub_matchISC_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE8find_impEv[_ZN5boost16re_detail_10650112perl_matcherIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEESaINS_9sub_matchISC_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE8find_impEv]+0x2c0): undefined reference to `boost::re_detail_106501::put_mem_block(void*)'
parse_url.cpp:(.text._ZN5boost16re_detail_10650112perl_matcherIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEESaINS_9sub_matchISC_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE8find_impEv[_ZN5boost16re_detail_10650112perl_matcherIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEESaINS_9sub_matchISC_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE8find_impEv]+0x6a4): undefined reference to `boost::re_detail_106501::put_mem_block(void*)'
CMakeFiles/parse-url_fuzz_tests.dir/parse_url.cpp.o: In function `bool boost::regex_search<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > >, char, boost::regex_traits<char, boost::cpp_regex_traits<char> > >(__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, __gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, boost::match_results<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > > >&, boost::basic_regex<char, boost::regex_traits<char, boost::cpp_regex_traits<char> > > const&, boost::regex_constants::_match_flags, __gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >)':
parse_url.cpp:(.text._ZN5boost12regex_searchIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEESaINS_9sub_matchISB_EEEcNS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEEEbT_SJ_RNS_13match_resultsISJ_T0_EERKNS_11basic_regexIT1_T2_EENS_15regex_constants12_match_flagsESJ_[_ZN5boost12regex_searchIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEESaINS_9sub_matchISB_EEEcNS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEEEbT_SJ_RNS_13match_resultsISJ_T0_EERKNS_11basic_regexIT1_T2_EENS_15regex_constants12_match_flagsESJ_]+0x126): undefined reference to `boost::re_detail_106501::perl_matcher<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > >, boost::regex_traits<char, boost::cpp_regex_traits<char> > >::construct_init(boost::basic_regex<char, boost::regex_traits<char, boost::cpp_regex_traits<char> > > const&, boost::regex_constants::_match_flags)'
CMakeFiles/parse-url_fuzz_tests.dir/parse_url.cpp.o: In function `void boost::re_detail_106501::raise_error<boost::regex_traits_wrapper<boost::regex_traits<char, boost::cpp_regex_traits<char> > > >(boost::regex_traits_wrapper<boost::regex_traits<char, boost::cpp_regex_traits<char> > > const&, boost::regex_constants::error_type)':
parse_url.cpp:(.text._ZN5boost16re_detail_10650111raise_errorINS_20regex_traits_wrapperINS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEEEEEvRKT_NS_15regex_constants10error_typeE[_ZN5boost16re_detail_10650111raise_errorINS_20regex_traits_wrapperINS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEEEEEvRKT_NS_15regex_constants10error_typeE]+0xb5): undefined reference to `boost::re_detail_106501::raise_runtime_error(std::runtime_error const&)'
parse_url.cpp:(.text._ZN5boost16re_detail_10650111raise_errorINS_20regex_traits_wrapperINS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEEEEEvRKT_NS_15regex_constants10error_typeE[_ZN5boost16re_detail_10650111raise_errorINS_20regex_traits_wrapperINS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEEEEEvRKT_NS_15regex_constants10error_typeE]+0xe8): undefined reference to `boost::re_detail_106501::get_default_error_string(boost::regex_constants::error_type)'
CMakeFiles/parse-url_fuzz_tests.dir/parse_url.cpp.o: In function `boost::re_detail_106501::perl_matcher<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > >, boost::regex_traits<char, boost::cpp_regex_traits<char> > >::extend_stack()':
parse_url.cpp:(.text._ZN5boost16re_detail_10650112perl_matcherIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEESaINS_9sub_matchISC_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE12extend_stackEv[_ZN5boost16re_detail_10650112perl_matcherIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEESaINS_9sub_matchISC_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE12extend_stackEv]+0x18): undefined reference to `boost::re_detail_106501::get_mem_block()'
CMakeFiles/parse-url_fuzz_tests.dir/parse_url.cpp.o: In function `boost::re_detail_106501::perl_matcher<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > >, boost::regex_traits<char, boost::cpp_regex_traits<char> > >::match_toggle_case()':
parse_url.cpp:(.text._ZN5boost16re_detail_10650112perl_matcherIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEESaINS_9sub_matchISC_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE17match_toggle_caseEv[_ZN5boost16re_detail_10650112perl_matcherIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEESaINS_9sub_matchISC_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE17match_toggle_caseEv]+0x74): undefined reference to `boost::re_detail_106501::get_mem_block()'
CMakeFiles/parse-url_fuzz_tests.dir/parse_url.cpp.o: In function `boost::re_detail_106501::perl_matcher<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > >, boost::regex_traits<char, boost::cpp_regex_traits<char> > >::match_then()':
parse_url.cpp:(.text._ZN5boost16re_detail_10650112perl_matcherIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEESaINS_9sub_matchISC_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE10match_thenEv[_ZN5boost16re_detail_10650112perl_matcherIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEESaINS_9sub_matchISC_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE10match_thenEv]+0x54): undefined reference to `boost::re_detail_106501::get_mem_block()'
collect2: error: ld returned 1 exit status
tests/fuzz/CMakeFiles/parse-url_fuzz_tests.dir/build.make:130: recipe for target 'tests/fuzz/parse-url_fuzz_tests' failed
make[3]: *** [tests/fuzz/parse-url_fuzz_tests] Error 1
make[3]: Leaving directory '/storage/github/monero/build/release'
CMakeFiles/Makefile2:3884: recipe for target 'tests/fuzz/CMakeFiles/parse-url_fuzz_tests.dir/all' failed
make[2]: *** [tests/fuzz/CMakeFiles/parse-url_fuzz_tests.dir/all] Error 2
make[2]: *** Waiting for unfinished jobs....
[ 38%] Building CXX object tests/fuzz/CMakeFiles/http-client_fuzz_tests.dir/fuzzer.cpp.o
[ 38%] Linking CXX executable http-client_fuzz_tests
CMakeFiles/http-client_fuzz_tests.dir/http-client.cpp.o: In function `boost::re_detail_106501::perl_matcher<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > >, boost::regex_traits<char, boost::cpp_regex_traits<char> > >::unwind_extra_block(bool)':
http-client.cpp:(.text._ZN5boost16re_detail_10650112perl_matcherIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEESaINS_9sub_matchISC_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE18unwind_extra_blockEb[_ZN5boost16re_detail_10650112perl_matcherIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEESaINS_9sub_matchISC_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE18unwind_extra_blockEb]+0x2c): undefined reference to `boost::re_detail_106501::put_mem_block(void*)'
CMakeFiles/http-client_fuzz_tests.dir/http-client.cpp.o: In function `void boost::this_thread::sleep_for<long, boost::ratio<1l, 1000l> >(boost::chrono::duration<long, boost::ratio<1l, 1000l> > const&)':
http-client.cpp:(.text._ZN5boost11this_thread9sleep_forIlNS_5ratioILl1ELl1000EEEEEvRKNS_6chrono8durationIT_T0_EE[_ZN5boost11this_thread9sleep_forIlNS_5ratioILl1ELl1000EEEEEvRKNS_6chrono8durationIT_T0_EE]+0x58): undefined reference to `boost::this_thread::hidden::sleep_for(timespec const&)'
CMakeFiles/http-client_fuzz_tests.dir/http-client.cpp.o: In function `__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > boost::re_detail_106501::re_is_set_member<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, char, boost::regex_traits<char, boost::cpp_regex_traits<char> >, unsigned int>(__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, __gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, boost::re_detail_106501::re_set_long<unsigned int> const*, boost::re_detail_106501::regex_data<char, boost::regex_traits<char, boost::cpp_regex_traits<char> > > const&, bool)':
http-client.cpp:(.text._ZN5boost16re_detail_10650116re_is_set_memberIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEEcNS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEjEET_SH_SH_PKNS0_11re_set_longIT2_EERKNS0_10regex_dataIT0_T1_EEb[_ZN5boost16re_detail_10650116re_is_set_memberIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEEcNS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEjEET_SH_SH_PKNS0_11re_set_longIT2_EERKNS0_10regex_dataIT0_T1_EEb]+0x15e): undefined reference to `boost::re_detail_106501::cpp_regex_traits_implementation<char>::transform_primary(char const*, char const*) const'
http-client.cpp:(.text._ZN5boost16re_detail_10650116re_is_set_memberIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEEcNS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEjEET_SH_SH_PKNS0_11re_set_longIT2_EERKNS0_10regex_dataIT0_T1_EEb[_ZN5boost16re_detail_10650116re_is_set_memberIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEEcNS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEjEET_SH_SH_PKNS0_11re_set_longIT2_EERKNS0_10regex_dataIT0_T1_EEb]+0x34f): undefined reference to `boost::re_detail_106501::cpp_regex_traits_implementation<char>::transform(char const*, char const*) const'
CMakeFiles/http-client_fuzz_tests.dir/http-client.cpp.o: In function `boost::re_detail_106501::perl_matcher<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > >, boost::regex_traits<char, boost::cpp_regex_traits<char> > >::find_imp()':
http-client.cpp:(.text._ZN5boost16re_detail_10650112perl_matcherIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEESaINS_9sub_matchISC_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE8find_impEv[_ZN5boost16re_detail_10650112perl_matcherIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEESaINS_9sub_matchISC_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE8find_impEv]+0xa): undefined reference to `boost::re_detail_106501::get_mem_block()'
http-client.cpp:(.text._ZN5boost16re_detail_10650112perl_matcherIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEESaINS_9sub_matchISC_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE8find_impEv[_ZN5boost16re_detail_10650112perl_matcherIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEESaINS_9sub_matchISC_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE8find_impEv]+0x138): undefined reference to `boost::re_detail_106501::verify_options(unsigned int, boost::regex_constants::_match_flags)'
http-client.cpp:(.text._ZN5boost16re_detail_10650112perl_matcherIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEESaINS_9sub_matchISC_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE8find_impEv[_ZN5boost16re_detail_10650112perl_matcherIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEESaINS_9sub_matchISC_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE8find_impEv]+0x17f): undefined reference to `boost::re_detail_106501::put_mem_block(void*)'
http-client.cpp:(.text._ZN5boost16re_detail_10650112perl_matcherIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEESaINS_9sub_matchISC_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE8find_impEv[_ZN5boost16re_detail_10650112perl_matcherIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEESaINS_9sub_matchISC_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE8find_impEv]+0x2d3): undefined reference to `boost::re_detail_106501::put_mem_block(void*)'
CMakeFiles/http-client_fuzz_tests.dir/http-client.cpp.o: In function `bool boost::regex_search<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > >, char, boost::regex_traits<char, boost::cpp_regex_traits<char> > >(__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, __gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, boost::match_results<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > > >&, boost::basic_regex<char, boost::regex_traits<char, boost::cpp_regex_traits<char> > > const&, boost::regex_constants::_match_flags, __gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >)':
http-client.cpp:(.text._ZN5boost12regex_searchIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEESaINS_9sub_matchISB_EEEcNS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEEEbT_SJ_RNS_13match_resultsISJ_T0_EERKNS_11basic_regexIT1_T2_EENS_15regex_constants12_match_flagsESJ_[_ZN5boost12regex_searchIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEESaINS_9sub_matchISB_EEEcNS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEEEbT_SJ_RNS_13match_resultsISJ_T0_EERKNS_11basic_regexIT1_T2_EENS_15regex_constants12_match_flagsESJ_]+0x126): undefined reference to `boost::re_detail_106501::perl_matcher<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > >, boost::regex_traits<char, boost::cpp_regex_traits<char> > >::construct_init(boost::basic_regex<char, boost::regex_traits<char, boost::cpp_regex_traits<char> > > const&, boost::regex_constants::_match_flags)'
CMakeFiles/http-client_fuzz_tests.dir/http-client.cpp.o: In function `void boost::re_detail_106501::raise_error<boost::regex_traits_wrapper<boost::regex_traits<char, boost::cpp_regex_traits<char> > > >(boost::regex_traits_wrapper<boost::regex_traits<char, boost::cpp_regex_traits<char> > > const&, boost::regex_constants::error_type)':
http-client.cpp:(.text._ZN5boost16re_detail_10650111raise_errorINS_20regex_traits_wrapperINS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEEEEEvRKT_NS_15regex_constants10error_typeE[_ZN5boost16re_detail_10650111raise_errorINS_20regex_traits_wrapperINS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEEEEEvRKT_NS_15regex_constants10error_typeE]+0xb5): undefined reference to `boost::re_detail_106501::raise_runtime_error(std::runtime_error const&)'
http-client.cpp:(.text._ZN5boost16re_detail_10650111raise_errorINS_20regex_traits_wrapperINS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEEEEEvRKT_NS_15regex_constants10error_typeE[_ZN5boost16re_detail_10650111raise_errorINS_20regex_traits_wrapperINS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEEEEEvRKT_NS_15regex_constants10error_typeE]+0xe8): undefined reference to `boost::re_detail_106501::get_default_error_string(boost::regex_constants::error_type)'
CMakeFiles/http-client_fuzz_tests.dir/http-client.cpp.o: In function `boost::re_detail_106501::perl_matcher<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > >, boost::regex_traits<char, boost::cpp_regex_traits<char> > >::extend_stack()':
http-client.cpp:(.text._ZN5boost16re_detail_10650112perl_matcherIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEESaINS_9sub_matchISC_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE12extend_stackEv[_ZN5boost16re_detail_10650112perl_matcherIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEESaINS_9sub_matchISC_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE12extend_stackEv]+0x18): undefined reference to `boost::re_detail_106501::get_mem_block()'
collect2: error: ld returned 1 exit status
tests/fuzz/CMakeFiles/http-client_fuzz_tests.dir/build.make:132: recipe for target 'tests/fuzz/http-client_fuzz_tests' failed
make[3]: *** [tests/fuzz/http-client_fuzz_tests] Error 1
make[3]: Leaving directory '/storage/github/monero/build/release'
CMakeFiles/Makefile2:4002: recipe for target 'tests/fuzz/CMakeFiles/http-client_fuzz_tests.dir/all' failed
make[2]: *** [tests/fuzz/CMakeFiles/http-client_fuzz_tests.dir/all] Error 2
make[2]: Leaving directory '/storage/github/monero/build/release'
Makefile:138: recipe for target 'all' failed
make[1]: *** [all] Error 2
make[1]: Leaving directory '/storage/github/monero/build/release'
Makefile:64: recipe for target 'release-all' failed
make: *** [release-all] Error 2
```

____________________________________________________________

From `master`:
```
[ 42%] Building CXX object src/wallet/CMakeFiles/wallet_rpc_server.dir/wallet_rpc_server.cpp.o
[ 43%] Linking CXX executable ../../bin/monero-wallet-rpc
/usr/bin/ld: warning: libssl.so.1.0.0, needed by /usr/lib/gcc/x86_64-linux-gnu/5/../../../x86_64-linux-gnu/libunbound.so, may conflict with libssl.so.1.1
/usr/bin/ld: warning: libcrypto.so.1.0.0, needed by /usr/lib/gcc/x86_64-linux-gnu/5/../../../x86_64-linux-gnu/libunbound.so, may conflict with libcrypto.so.1.1
CMakeFiles/wallet_rpc_server.dir/wallet_rpc_server.cpp.o: In function `boost::re_detail_106501::perl_matcher<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > >, boost::regex_traits<char, boost::cpp_regex_traits<char> > >::unwind_extra_block(bool)':
wallet_rpc_server.cpp:(.text._ZN5boost16re_detail_10650112perl_matcherIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEESaINS_9sub_matchISC_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE18unwind_extra_blockEb[_ZN5boost16re_detail_10650112perl_matcherIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEESaINS_9sub_matchISC_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE18unwind_extra_blockEb]+0x2c): undefined reference to `boost::re_detail_106501::put_mem_block(void*)'
CMakeFiles/wallet_rpc_server.dir/wallet_rpc_server.cpp.o: In function `void boost::serialization::throw_exception<boost::archive::portable_binary_iarchive_exception>(boost::archive::portable_binary_iarchive_exception const&)':
wallet_rpc_server.cpp:(.text._ZN5boost13serialization15throw_exceptionINS_7archive34portable_binary_iarchive_exceptionEEEvRKT_[_ZN5boost13serialization15throw_exceptionINS_7archive34portable_binary_iarchive_exceptionEEEvRKT_]+0x36): undefined reference to `boost::archive::archive_exception::archive_exception(boost::archive::archive_exception const&)'
CMakeFiles/wallet_rpc_server.dir/wallet_rpc_server.cpp.o: In function `void boost::serialization::throw_exception<boost::archive::archive_exception>(boost::archive::archive_exception const&)':
wallet_rpc_server.cpp:(.text._ZN5boost13serialization15throw_exceptionINS_7archive17archive_exceptionEEEvRKT_[_ZN5boost13serialization15throw_exceptionINS_7archive17archive_exceptionEEEvRKT_]+0x1d): undefined reference to `boost::archive::archive_exception::archive_exception(boost::archive::archive_exception const&)'
CMakeFiles/wallet_rpc_server.dir/wallet_rpc_server.cpp.o: In function `void boost::this_thread::sleep_for<long, boost::ratio<1l, 1000l> >(boost::chrono::duration<long, boost::ratio<1l, 1000l> > const&)':
wallet_rpc_server.cpp:(.text._ZN5boost11this_thread9sleep_forIlNS_5ratioILl1ELl1000EEEEEvRKNS_6chrono8durationIT_T0_EE[_ZN5boost11this_thread9sleep_forIlNS_5ratioILl1ELl1000EEEEEvRKNS_6chrono8durationIT_T0_EE]+0x58): undefined reference to `boost::this_thread::hidden::sleep_for(timespec const&)'
CMakeFiles/wallet_rpc_server.dir/wallet_rpc_server.cpp.o: In function `epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::call_run_once_service_io()':
wallet_rpc_server.cpp:(.text._ZN4epee9net_utils10connectionINS0_4http19http_custom_handlerINS0_23connection_context_baseEEEE24call_run_once_service_ioEv[_ZN4epee9net_utils10connectionINS0_4http19http_custom_handlerINS0_23connection_context_baseEEEE24call_run_once_service_ioEv]+0x64f): undefined reference to `boost::this_thread::hidden::sleep_until(timespec const&)'
CMakeFiles/wallet_rpc_server.dir/wallet_rpc_server.cpp.o: In function `void boost::re_detail_106501::raise_error<boost::regex_traits_wrapper<boost::regex_traits<char, boost::cpp_regex_traits<char> > > >(boost::regex_traits_wrapper<boost::regex_traits<char, boost::cpp_regex_traits<char> > > const&, boost::regex_constants::error_type)':
wallet_rpc_server.cpp:(.text._ZN5boost16re_detail_10650111raise_errorINS_20regex_traits_wrapperINS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEEEEEvRKT_NS_15regex_constants10error_typeE[_ZN5boost16re_detail_10650111raise_errorINS_20regex_traits_wrapperINS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEEEEEvRKT_NS_15regex_constants10error_typeE]+0xb5): undefined reference to `boost::re_detail_106501::raise_runtime_error(std::runtime_error const&)'
wallet_rpc_server.cpp:(.text._ZN5boost16re_detail_10650111raise_errorINS_20regex_traits_wrapperINS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEEEEEvRKT_NS_15regex_constants10error_typeE[_ZN5boost16re_detail_10650111raise_errorINS_20regex_traits_wrapperINS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEEEEEvRKT_NS_15regex_constants10error_typeE]+0xe8): undefined reference to `boost::re_detail_106501::get_default_error_string(boost::regex_constants::error_type)'
CMakeFiles/wallet_rpc_server.dir/wallet_rpc_server.cpp.o: In function `__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > boost::re_detail_106501::re_is_set_member<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, char, boost::regex_traits<char, boost::cpp_regex_traits<char> >, unsigned int>(__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, __gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, boost::re_detail_106501::re_set_long<unsigned int> const*, boost::re_detail_106501::regex_data<char, boost::regex_traits<char, boost::cpp_regex_traits<char> > > const&, bool)':
wallet_rpc_server.cpp:(.text._ZN5boost16re_detail_10650116re_is_set_memberIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEEcNS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEjEET_SH_SH_PKNS0_11re_set_longIT2_EERKNS0_10regex_dataIT0_T1_EEb[_ZN5boost16re_detail_10650116re_is_set_memberIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEEcNS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEjEET_SH_SH_PKNS0_11re_set_longIT2_EERKNS0_10regex_dataIT0_T1_EEb]+0x15e): undefined reference to `boost::re_detail_106501::cpp_regex_traits_implementation<char>::transform_primary(char const*, char const*) const'
wallet_rpc_server.cpp:(.text._ZN5boost16re_detail_10650116re_is_set_memberIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEEcNS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEjEET_SH_SH_PKNS0_11re_set_longIT2_EERKNS0_10regex_dataIT0_T1_EEb[_ZN5boost16re_detail_10650116re_is_set_memberIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEEcNS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEjEET_SH_SH_PKNS0_11re_set_longIT2_EERKNS0_10regex_dataIT0_T1_EEb]+0x34f): undefined reference to `boost::re_detail_106501::cpp_regex_traits_implementation<char>::transform(char const*, char const*) const'
CMakeFiles/wallet_rpc_server.dir/wallet_rpc_server.cpp.o: In function `boost::re_detail_106501::perl_matcher<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > >, boost::regex_traits<char, boost::cpp_regex_traits<char> > >::extend_stack()':
wallet_rpc_server.cpp:(.text._ZN5boost16re_detail_10650112perl_matcherIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEESaINS_9sub_matchISC_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE12extend_stackEv[_ZN5boost16re_detail_10650112perl_matcherIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEESaINS_9sub_matchISC_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE12extend_stackEv]+0x18): undefined reference to `boost::re_detail_106501::get_mem_block()'
CMakeFiles/wallet_rpc_server.dir/wallet_rpc_server.cpp.o: In function `epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::do_send_chunk(void const*, unsigned long)':
wallet_rpc_server.cpp:(.text._ZN4epee9net_utils10connectionINS0_4http19http_custom_handlerINS0_23connection_context_baseEEEE13do_send_chunkEPKvm[_ZN4epee9net_utils10connectionINS0_4http19http_custom_handlerINS0_23connection_context_baseEEEE13do_send_chunkEPKvm]+0x263): undefined reference to `boost::this_thread::hidden::sleep_until(timespec const&)'
CMakeFiles/wallet_rpc_server.dir/wallet_rpc_server.cpp.o: In function `boost::re_detail_106501::perl_matcher<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > >, boost::regex_traits<char, boost::cpp_regex_traits<char> > >::match_imp()':
wallet_rpc_server.cpp:(.text._ZN5boost16re_detail_10650112perl_matcherIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEESaINS_9sub_matchISC_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE9match_impEv[_ZN5boost16re_detail_10650112perl_matcherIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEESaINS_9sub_matchISC_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE9match_impEv]+0xa): undefined reference to `boost::re_detail_106501::get_mem_block()'
wallet_rpc_server.cpp:(.text._ZN5boost16re_detail_10650112perl_matcherIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEESaINS_9sub_matchISC_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE9match_impEv[_ZN5boost16re_detail_10650112perl_matcherIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEESaINS_9sub_matchISC_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE9match_impEv]+0xf9): undefined reference to `boost::re_detail_106501::verify_options(unsigned int, boost::regex_constants::_match_flags)'
wallet_rpc_server.cpp:(.text._ZN5boost16re_detail_10650112perl_matcherIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEESaINS_9sub_matchISC_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE9match_impEv[_ZN5boost16re_detail_10650112perl_matcherIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEESaINS_9sub_matchISC_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE9match_impEv]+0x12b): undefined reference to `boost::re_detail_106501::put_mem_block(void*)'
wallet_rpc_server.cpp:(.text._ZN5boost16re_detail_10650112perl_matcherIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEESaINS_9sub_matchISC_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE9match_impEv[_ZN5boost16re_detail_10650112perl_matcherIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEESaINS_9sub_matchISC_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE9match_impEv]+0x1ee): undefined reference to `boost::re_detail_106501::put_mem_block(void*)'
CMakeFiles/wallet_rpc_server.dir/wallet_rpc_server.cpp.o: In function `epee::serialization::convert_to_integral<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, unsigned long, false>::convert(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, unsigned long&)':
wallet_rpc_server.cpp:(.text._ZN4epee13serialization19convert_to_integralINSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEmLb0EE7convertERKS7_Rm[_ZN4epee13serialization19convert_to_integralINSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEmLb0EE7convertERKS7_Rm]+0x2b0): undefined reference to `boost::re_detail_106501::perl_matcher<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > >, boost::regex_traits<char, boost::cpp_regex_traits<char> > >::construct_init(boost::basic_regex<char, boost::regex_traits<char, boost::cpp_regex_traits<char> > > const&, boost::regex_constants::_match_flags)'
CMakeFiles/wallet_rpc_server.dir/wallet_rpc_server.cpp.o: In function `boost::re_detail_106501::perl_matcher<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > >, boost::regex_traits<char, boost::cpp_regex_traits<char> > >::find_imp()':
wallet_rpc_server.cpp:(.text._ZN5boost16re_detail_10650112perl_matcherIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEESaINS_9sub_matchISC_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE8find_impEv[_ZN5boost16re_detail_10650112perl_matcherIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEESaINS_9sub_matchISC_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE8find_impEv]+0xa): undefined reference to `boost::re_detail_106501::get_mem_block()'
wallet_rpc_server.cpp:(.text._ZN5boost16re_detail_10650112perl_matcherIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEESaINS_9sub_matchISC_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE8find_impEv[_ZN5boost16re_detail_10650112perl_matcherIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEESaINS_9sub_matchISC_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE8find_impEv]+0x138): undefined reference to `boost::re_detail_106501::verify_options(unsigned int, boost::regex_constants::_match_flags)'
wallet_rpc_server.cpp:(.text._ZN5boost16re_detail_10650112perl_matcherIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEESaINS_9sub_matchISC_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE8find_impEv[_ZN5boost16re_detail_10650112perl_matcherIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEESaINS_9sub_matchISC_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE8find_impEv]+0x17f): undefined reference to `boost::re_detail_106501::put_mem_block(void*)'
wallet_rpc_server.cpp:(.text._ZN5boost16re_detail_10650112perl_matcherIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEESaINS_9sub_matchISC_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE8find_impEv[_ZN5boost16re_detail_10650112perl_matcherIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEESaINS_9sub_matchISC_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE8find_impEv]+0x2d3): undefined reference to `boost::re_detail_106501::put_mem_block(void*)'
CMakeFiles/wallet_rpc_server.dir/wallet_rpc_server.cpp.o: In function `bool boost::regex_search<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > >, char, boost::regex_traits<char, boost::cpp_regex_traits<char> > >(__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, __gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, boost::match_results<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > > >&, boost::basic_regex<char, boost::regex_traits<char, boost::cpp_regex_traits<char> > > const&, boost::regex_constants::_match_flags, __gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >)':
wallet_rpc_server.cpp:(.text._ZN5boost12regex_searchIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEESaINS_9sub_matchISB_EEEcNS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEEEbT_SJ_RNS_13match_resultsISJ_T0_EERKNS_11basic_regexIT1_T2_EENS_15regex_constants12_match_flagsESJ_[_ZN5boost12regex_searchIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEESaINS_9sub_matchISB_EEEcNS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEEEbT_SJ_RNS_13match_resultsISJ_T0_EERKNS_11basic_regexIT1_T2_EENS_15regex_constants12_match_flagsESJ_]+0x126): undefined reference to `boost::re_detail_106501::perl_matcher<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > >, boost::regex_traits<char, boost::cpp_regex_traits<char> > >::construct_init(boost::basic_regex<char, boost::regex_traits<char, boost::cpp_regex_traits<char> > > const&, boost::regex_constants::_match_flags)'
CMakeFiles/wallet_rpc_server.dir/wallet_rpc_server.cpp.o: In function `epee::net_utils::http::simple_http_connection_handler<epee::net_utils::connection_context_base>::parse_cached_header(epee::net_utils::http::http_header_info&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, unsigned long)':
wallet_rpc_server.cpp:(.text._ZN4epee9net_utils4http30simple_http_connection_handlerINS0_23connection_context_baseEE19parse_cached_headerERNS1_16http_header_infoERKNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEm[_ZN4epee9net_utils4http30simple_http_connection_handlerINS0_23connection_context_baseEE19parse_cached_headerERNS1_16http_header_infoERKNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEm]+0x33e): undefined reference to `boost::re_detail_106501::perl_matcher<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > >, boost::regex_traits<char, boost::cpp_regex_traits<char> > >::construct_init(boost::basic_regex<char, boost::regex_traits<char, boost::cpp_regex_traits<char> > > const&, boost::regex_constants::_match_flags)'
../../lib/libwallet.a(wallet2.cpp.o): In function `boost::archive::detail::common_iarchive<boost::archive::binary_iarchive>::vload(boost::archive::class_name_type&)':
wallet2.cpp:(.text._ZN5boost7archive6detail15common_iarchiveINS0_15binary_iarchiveEE5vloadERNS0_15class_name_typeE[_ZN5boost7archive6detail15common_iarchiveINS0_15binary_iarchiveEE5vloadERNS0_15class_name_typeE]+0x1): undefined reference to `boost::archive::basic_binary_iarchive<boost::archive::binary_iarchive>::load_override(boost::archive::class_name_type&)'
../../lib/libwallet.a(wallet2.cpp.o): In function `boost::archive::portable_binary_oarchive::portable_binary_oarchive(std::ostream&, unsigned int)':
wallet2.cpp:(.text._ZN5boost7archive24portable_binary_oarchiveC2ERSoj[_ZN5boost7archive24portable_binary_oarchiveC5ERSoj]+0x233): undefined reference to `boost::archive::archive_exception::archive_exception(boost::archive::archive_exception const&)'
../../contrib/epee/src/libepee.a(connection_basic.cpp.o): In function `epee::net_utils::connection_basic::sleep_before_packet(unsigned long, int, int)':
connection_basic.cpp:(.text+0x27f2): undefined reference to `boost::this_thread::hidden::sleep_until(timespec const&)'
../cryptonote_basic/libcryptonote_basic.a(miner.cpp.o): In function `cryptonote::miner::worker_thread()':
miner.cpp:(.text+0x7390): undefined reference to `boost::this_thread::hidden::sleep_until(timespec const&)'
miner.cpp:(.text+0x761c): undefined reference to `boost::this_thread::hidden::sleep_until(timespec const&)'
miner.cpp:(.text+0x7e82): undefined reference to `boost::this_thread::hidden::sleep_until(timespec const&)'
../cryptonote_basic/libcryptonote_basic.a(miner.cpp.o): In function `void boost::this_thread::sleep_for<long, boost::ratio<1l, 1l> >(boost::chrono::duration<long, boost::ratio<1l, 1l> > const&)':
miner.cpp:(.text._ZN5boost11this_thread9sleep_forIlNS_5ratioILl1ELl1EEEEEvRKNS_6chrono8durationIT_T0_EE[_ZN5boost11this_thread9sleep_forIlNS_5ratioILl1ELl1EEEEEvRKNS_6chrono8durationIT_T0_EE]+0x50): undefined reference to `boost::this_thread::hidden::sleep_for(timespec const&)'
../cryptonote_basic/libcryptonote_basic.a(miner.cpp.o): In function `bool boost::regex_match<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > >, char, boost::regex_traits<char, boost::cpp_regex_traits<char> > >(__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, __gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, boost::match_results<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > > >&, boost::basic_regex<char, boost::regex_traits<char, boost::cpp_regex_traits<char> > > const&, boost::regex_constants::_match_flags)':
miner.cpp:(.text._ZN5boost11regex_matchIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEESaINS_9sub_matchISB_EEEcNS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEEEbT_SJ_RNS_13match_resultsISJ_T0_EERKNS_11basic_regexIT1_T2_EENS_15regex_constants12_match_flagsE[_ZN5boost11regex_matchIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEESaINS_9sub_matchISB_EEEcNS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEEEbT_SJ_RNS_13match_resultsISJ_T0_EERKNS_11basic_regexIT1_T2_EENS_15regex_constants12_match_flagsE]+0xe9): undefined reference to `boost::re_detail_106501::perl_matcher<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > >, boost::regex_traits<char, boost::cpp_regex_traits<char> > >::construct_init(boost::basic_regex<char, boost::regex_traits<char, boost::cpp_regex_traits<char> > > const&, boost::regex_constants::_match_flags)'
collect2: error: ld returned 1 exit status
src/wallet/CMakeFiles/wallet_rpc_server.dir/build.make:132: recipe for target 'bin/monero-wallet-rpc' failed
make[3]: *** [bin/monero-wallet-rpc] Error 1
make[3]: Leaving directory '/storage/github/monero/build/release'
CMakeFiles/Makefile2:2232: recipe for target 'src/wallet/CMakeFiles/wallet_rpc_server.dir/all' failed
make[2]: *** [src/wallet/CMakeFiles/wallet_rpc_server.dir/all] Error 2
make[2]: Leaving directory '/storage/github/monero/build/release'
Makefile:138: recipe for target 'all' failed
make[1]: *** [all] Error 2
make[1]: Leaving directory '/storage/github/monero/build/release'
Makefile:64: recipe for target 'release-all' failed
make: *** [release-all] Error 2
```

## ns1000 | 2018-03-24T23:54:57+00:00
I am getting this error:

[ 95%] Building CXX object tests/unit_tests/CMakeFiles/unit_tests.dir/varint.cpp.o
[ 95%] Building CXX object tests/unit_tests/CMakeFiles/unit_tests.dir/ringct.cpp.o
[ 96%] Building CXX object tests/unit_tests/CMakeFiles/unit_tests.dir/output_selection.cpp.o
[ 96%] Building CXX object tests/unit_tests/CMakeFiles/unit_tests.dir/vercmp.cpp.o
[ 96%] Linking CXX executable unit_tests
/usr/bin/ld: /usr/local/lib/libminiupnpc.a(miniupnpc.c.o): relocation R_X86_64_32 against `.rodata.str1.1' can not be used when making a shared object; recompile with -fPIC
/usr/local/lib/libminiupnpc.a: error adding symbols: Bad value
collect2: error: ld returned 1 exit status
tests/unit_tests/CMakeFiles/unit_tests.dir/build.make:1206: recipe for target 'tests/unit_tests/unit_tests' failed
make[3]: *** [tests/unit_tests/unit_tests] Error 1
make[3]: Leaving directory '/build/monerod/build/release'
CMakeFiles/Makefile2:4457: recipe for target 'tests/unit_tests/CMakeFiles/unit_tests.dir/all' failed
make[2]: *** [tests/unit_tests/CMakeFiles/unit_tests.dir/all] Error 2
make[2]: Leaving directory '/build/monerod/build/release'
Makefile:138: recipe for target 'all' failed
make[1]: *** [all] Error 2
make[1]: Leaving directory '/build/monerod/build/release'
Makefile:64: recipe for target 'release-all' failed
make: *** [release-all] Error 2


## hyc | 2018-03-25T02:06:06+00:00
@gituser 
> /usr/bin/ld: /home/build/monero/boost/boost.build/lib/libboost_chrono.a(chrono.o): relocation R_X86_64_32 against `.rodata.str1.1' can not be used when making a shared object; recompile with -fPIC

> /usr/bin/ld: /usr/lib/gcc/x86_64-linux-gnu/4.9/../../../x86_64-linux-gnu/libssl.a(s23_meth.o): relocation R_X86_64_32 against `.rodata' can not be used when making a shared object; recompile with -fPIC


@ns1000
> /usr/bin/ld: /usr/local/lib/libminiupnpc.a(miniupnpc.c.o): relocation R_X86_64_32 against `.rodata.str1.1' can not be used when making a shared object; recompile with -fPIC

This is still the same error as already addressed above - pay attention to the actual error message and recompile the offending library with `-fPIC` just like it says.

@lacksfish looks to me like your boost was compiled with a different version of compiler than your monero tree. This C++ shit only works if you use the exact same compiler for both.

## gituser | 2018-03-25T03:29:56+00:00
@hyc, I did recompile the boost with `-fPIC`, now the problem is in openssl, before it worked just fine with stock libssl, guess now I need to compile libssl with `-fPIC` somewhere..

`v0.11.1.0` compiled just fine with stock libssl from debian 8.

## gituser | 2018-03-25T14:28:05+00:00
@hyc @moneromooo-monero  how do I specify where make will search for statically built libssl?

from README.md it seems there is only `BOOST_ROOT`  environment variable, but for other libs ? libssl or libminiupnpc ?

## moneromooo-monero | 2018-03-25T21:49:30+00:00
From /usr/share/cmake/Modules/FindOpenSSL.cmake:
```
# Hints
# ^^^^^
#
# Set ``OPENSSL_ROOT_DIR`` to the root directory of an OpenSSL installation.
# Set ``OPENSSL_USE_STATIC_LIBS`` to ``TRUE`` to look for static libraries.
# Set ``OPENSSL_MSVC_STATIC_RT`` set ``TRUE`` to choose the MT version of the lib.
```

## moneromooo-monero | 2018-03-27T23:25:52+00:00
+invalid

## gituser | 2018-04-07T20:43:58+00:00
for those who are having similar issues when building static binary with new version you need to:

Build static versions of packages (before building use `export CFLAGS='-fPIC' CXXFLAGS='-fPIC'`

1. `cppzmq v4.2.3`
2. `ncurses 5.9+`, (with libtinfo and termcap support)
3. `openssl 1.0.1+`
4. `readline 6.3+`
5. `zeromq 4.0.5+`
6. `boost 1.62+`

Best is to install all packages in some directory, e.g. `~build/monero/deps/installed`, install boost into `~build/monero/boost/boost.build` or into same  `~build/monero/deps/installed` directory and then you can use my script to build it:

```
!/bin/bash
#VER=$(git describe --tags)
daemon=$(pname=$(pwd); echo ${pname##/*/})

export BOOST_ROOT=/home/build/monero/boost/boost.build DEVELOPER_LOCAL_TOOLS=1
export OPENSSL_ROOT_DIR=/home/build/monero/deps/installed
export Readline_ROOT_DIR=/home/build/monero/deps/installed
export Readline_INCLUDE=/home/build/monero/deps/installed/include
export Readline_LIBRARY=/home/build/monero/deps/installed/lib
export READLINE_ROOT_DIR=/home/build/monero/deps/installed
export OPENSSL_USE_STATIC_LIBS=TRUE
export ZMQ_INCLUDE_PATH=/home/build/monero/deps/installed/include
export ZMQ_LIBRARY=/home/build/monero/deps/installed/lib/libzmq.a
export Termcap_LIBRARY=/home/build/monero/deps/installed/lib/libtinfo.a

rm -rf build
mkdir -p build/release
cd build/release 
cmake -D ZMQ_LIB=$ZMQ_LIBRARY -D Termcap_LIBRARY=$Termcap_LIBRARY -D Readline_ROOT_DIR=$Readline_ROOT_DIR -D ZMQ_INCLUDE_PATH=$ZMQ_INCLUDE_PATH -D STATIC=ON -D ARCH="x86-64" -D BUILD_64=ON -D CMAKE_BUILD_TYPE=release ../.. 
make

if [ "$?" == 0 ]; then
        VER=$(./build/release/bin/monerod --version 2>/dev/null|sed -r 's/.*\((v.*)\).*/\1/')
        mkdir -p ../$VER
        cp -prv build/release/bin/* ../$VER/;
	rm -rf ../current
	ln -sf $VER ../current
else
	echo "Build Failed."
fi
```

## danrmiller | 2018-04-09T21:52:34+00:00
In addition to the list above, zeromq may need libsodium.

You do not need to build cppzmq, you only need the zmq.hpp file.

@gituser, why do you specify boost 1.62+? The monero README and my experience indicates the minimum is 1.58.

If you are using debian packages, for example a debian or ubuntu system, @mesouug gives this method to rebuild the packages with -fPIC. Some other people may find it helpful.
```
sudo apt-get build-dep <packagename>
apt-get source <packagename>
cd <package src dir>
DEB_CFLAGS_APPEND="-fPIC" DEP_CXXFLAGS_APPEND="-fPIC" DEB_CPPFLAGS_APPEND="-fPIC" dpkg-buildpackage -B -us -uc -j3 -rfakeroot
sudo dpkg -i ../<package.deb>
```


## gituser | 2018-04-09T22:04:42+00:00
@danrmiller yes I'm sorry, it's just what I've used personally Boost 1.62, sure you can try with 1.58 but it didn't work for me that's why I've marked `1.62+`.

regarding debian packages - I don't think it's a good idea to re-compile debian packages and mess up the system dependencies just to get static monerod. 

I'd just use unprivileged binaries in some folder compiled just for this task.

But, of course this is a good info for others - who would want to get static debian packages re-compiled, so big up for that! 

# Action History
- Created by: gituser | 2018-03-21T15:34:35+00:00
- Closed at: 2018-03-27T23:56:45+00:00
