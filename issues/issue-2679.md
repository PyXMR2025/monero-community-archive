---
title: 'CheckFunctionExists.c:(.text+0x10): undefined reference to `EVP_MD_CTX_new'''
source_url: https://github.com/monero-project/monero/issues/2679
author: vasence
assignees: []
labels:
- invalid
created_at: '2017-10-18T21:42:29+00:00'
updated_at: '2017-11-24T17:48:24+00:00'
type: issue
status: closed
closed_at: '2017-11-24T17:48:24+00:00'
---

# Original Description
File /home/vaso/Downloads/monero-master/build/release/CMakeFiles/CMakeTmp/CheckSymbolExists.c:
/* */
#include <openssl/ssl.h>

int main(int argc, char** argv)
{
  (void)argv;
#ifndef SSL_COMP_get_compression_methods
  return ((int*)(&SSL_COMP_get_compression_methods))[argc];
#else
  (void)argc;
  return 0;
#endif
}

Determining if the function EVP_MD_CTX_new exists failed with the following output:
Change Dir: /home/vaso/Downloads/monero-master/build/release/CMakeFiles/CMakeTmp

Run Build Command:"/usr/bin/gmake" "cmTC_e918d/fast"
gmake[1]: Entering directory '/home/vaso/Downloads/monero-master/build/release/CMakeFiles/CMakeTmp'
/usr/bin/gmake -f CMakeFiles/cmTC_e918d.dir/build.make CMakeFiles/cmTC_e918d.dir/build
gmake[2]: Entering directory '/home/vaso/Downloads/monero-master/build/release/CMakeFiles/CMakeTmp'
Building C object CMakeFiles/cmTC_e918d.dir/CheckFunctionExists.c.o
/usr/bin/cc   -DCHECK_FUNCTION_EXISTS=EVP_MD_CTX_new   -o CMakeFiles/cmTC_e918d.dir/CheckFunctionExists.c.o   -c /usr/share/cmake-3.9/Modules/CheckFunctionExists.c
Linking C executable cmTC_e918d
/usr/bin/cmake -E cmake_link_script CMakeFiles/cmTC_e918d.dir/link.txt --verbose=1
/usr/bin/cc  -DCHECK_FUNCTION_EXISTS=EVP_MD_CTX_new    -rdynamic CMakeFiles/cmTC_e918d.dir/CheckFunctionExists.c.o  -o cmTC_e918d /usr/lib64/libssl.so /usr/lib64/libcrypto.so 
CMakeFiles/cmTC_e918d.dir/CheckFunctionExists.c.o: In function `main':
CheckFunctionExists.c:(.text+0x10): undefined reference to `EVP_MD_CTX_new'
collect2: error: ld returned 1 exit status
gmake[2]: *** [CMakeFiles/cmTC_e918d.dir/build.make:100: cmTC_e918d] Error 1
gmake[2]: Leaving directory '/home/vaso/Downloads/monero-master/build/release/CMakeFiles/CMakeTmp'
gmake[1]: *** [Makefile:126: cmTC_e918d/fast] Error 2
gmake[1]: Leaving directory '/home/vaso/Downloads/monero-master/build/release/CMakeFiles/CMakeTmp'


bash-4.4$ ld --version
GNU ld version 2.29.1-slack15
Copyright (C) 2017 Free Software Foundation, Inc.
This program is free software; you may redistribute it under the terms of
the GNU General Public License version 3 or (at your option) a later version.
This program has absolutely no warranty.
bash-4.4$ gcc --version
gcc (GCC) 7.2.0
Copyright (C) 2017 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

bash-4.4$ gc
gc-analyze        gcc-ar            gccbrig           gcj               gconf-merge-tree  gcov              gcr-viewer        
gcc               gcc-nm            gccgo             gcj-dbtool        gconftool-2       gcov-dump         
gcc-7.2.0         gcc-ranlib        gccmakedep        gcjh              gcore             gcov-tool         
bash-4.4$ g++ --version
g++ (GCC) 7.2.0
Copyright (C) 2017 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

bash-4.4$ cat /etc/slackware-version 
Slackware 14.2
bash-4.4$ 


# Discussion History
## moneromooo-monero | 2017-10-18T23:39:08+00:00
and is EVP_MD_CTX_new present (and public) in /usr/lib64/libssl.so or /usr/lib64/libcrypto.so ?

nm -a /usr/lib64/libssl.so | grep EVP_MD_CTX_new

If found and the single letter is lowercase, it's private/unusable. I think the letter should normally T (text, public).

## radfish | 2017-10-19T02:26:32+00:00
And, what's your openssl version?

## vasence | 2017-10-19T06:46:14+00:00
root@vaso10:/home/vaso/Downloads# openssl
OpenSSL> version
OpenSSL 1.0.2l  25 May 2017
OpenSSL> 

bash-4.4$ ldd /lib/libssl.so.1
        linux-gate.so.1 (0xf779f000)
        libcrypto.so.1 => /lib/libcrypto.so.1 (0xf74ec000)
        libdl.so.2 => /lib/libdl.so.2 (0xf74e7000)
        libc.so.6 => /lib/libc.so.6 (0xf7330000)
        /lib/ld-linux.so.2 (0xf77a0000)
bash-4.4$ ldd /usr/lib/libssl.so
        linux-gate.so.1 (0xf774d000)
        libcrypto.so.1 => /lib/libcrypto.so.1 (0xf749a000)
        libdl.so.2 => /lib/libdl.so.2 (0xf7495000)
        libc.so.6 => /lib/libc.so.6 (0xf72de000)
        /lib/ld-linux.so.2 (0xf774e000)
bash-4.4$ ldd /usr/lib64/libssl.so
        linux-vdso.so.1 (0x00007ffd3bfdb000)
        libcrypto.so.1 => /lib64/libcrypto.so.1 (0x00007efcffd9b000)
        libdl.so.2 => /lib64/libdl.so.2 (0x00007efcffb97000)
        libc.so.6 => /lib64/libc.so.6 (0x00007efcff7b8000)
        /lib64/ld-linux-x86-64.so.2 (0x00007efd00463000)
bash-4.4$ 


## vasence | 2017-10-19T10:42:26+00:00
nm: /usr/lib64/libssl.so: no symbols


## radfish | 2017-10-19T14:52:47+00:00
Looking again at it. You're looking at some output from CMakeTmp, that's not relevant. It's checking whether or not compilation succeeds. The main build should just take a YES/NO result and continue. What is the main build output? Paste the whole log, including the command you are running.

## vasence | 2017-10-19T18:07:30+00:00
bash-4.4$ make
mkdir -p build/release
cd build/release && cmake -D BUILD_TESTS=ON -D CMAKE_BUILD_TYPE=release ../.. && make
-- The C compiler identification is GNU 7.2.0
-- The CXX compiler identification is GNU 7.2.0
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
-- Found OpenSSL: /usr/lib64/libcrypto.so (found version "1.0.2l") 
-- Using OpenSSL include dir at /usr/include
-- Could NOT find MiniUPnPc (missing: MINIUPNP_INCLUDE_DIR MINIUPNP_LIBRARY) 
-- Using miniupnpc from local source tree (/external/miniupnpc)
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
-- Looking for getentropy - found
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
-- Looking for reallocarray - found
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
-- Found PkgConfig: /usr/bin/pkg-config (found version "0.29.2") 
-- Using 64-bit LMDB from source tree
-- Building on x86_64 for native
-- AES support enabled
-- Found Boost Version: 106501
-- Found Readline: /usr/include  
-- Performing Test GNU_READLINE_FOUND
-- Performing Test GNU_READLINE_FOUND - Success
-- Found readline library at: /usr
CMake Error at CMakeLists.txt:708 (message):
  Could not find required header zmq.hpp


-- Configuring incomplete, errors occurred!
See also "/home/vaso/Downloads/monero-master/build/release/CMakeFiles/CMakeOutput.log".
See also "/home/vaso/Downloads/monero-master/build/release/CMakeFiles/CMakeError.log".
make: *** [Makefile:63: release-all] Error 1
bash-4.4$ 
[CMakeError.log](https://github.com/monero-project/monero/files/1399503/CMakeError.log)
[CMakeOutput.log](https://github.com/monero-project/monero/files/1399504/CMakeOutput.log)


## radfish | 2017-10-19T18:17:01+00:00
On Thu, Oct 19, 2017 at 11:07:41AM -0700, vasence wrote:
> CMake Error at CMakeLists.txt:708 (message):
>   Could not find required header zmq.hpp

zmq library is a dependency (see table in README.md). Install it and try again.


## moneromooo-monero | 2017-11-24T17:38:02+00:00
+invalid

# Action History
- Created by: vasence | 2017-10-18T21:42:29+00:00
- Closed at: 2017-11-24T17:48:24+00:00
