---
title: Build on Windows 11 run in cmake Minimum error
source_url: https://github.com/xmrig/xmrig/issues/3341
author: fohnbit
assignees: []
labels: []
created_at: '2023-09-29T09:45:46+00:00'
updated_at: '2025-06-18T22:20:10+00:00'
type: issue
status: closed
closed_at: '2025-06-18T22:20:10+00:00'
---

# Original Description
Hello!

I try to build xmrig on my Windows 11 PC. I faced in an error, which I don´t know how to fix:
I use MSYS2

```
pacman -S mingw-w64-x86_64-gcc git make
git clone https://github.com/xmrig/xmrig.git
mkdir xmrig/build && cd xmrig/build
```
but the next command:
`"c:\Program Files\CMake\bin\cmake.exe" .. -G "Unix Makefiles" -DXMRIG_DEPS=c:/xmrig-deps/gcc/x64`

throw the error:
```
CMake Deprecation Warning at CMakeLists.txt:1 (cmake_minimum_required):
  Compatibility with CMake < 3.5 will be removed from a future version of
  CMake.

  Update the VERSION argument <min> value or use a ...<max> suffix to tell
  CMake that the project does not need compatibility with older versions.


-- The C compiler identification is unknown
-- The CXX compiler identification is unknown
CMake Error at CMakeLists.txt:2 (project):
  No CMAKE_C_COMPILER could be found.

  Tell CMake where to find the compiler by setting either the environment
  variable "CC" or the CMake cache entry CMAKE_C_COMPILER to the full path to
  the compiler, or to the compiler name if it is in the PATH.


CMake Error at CMakeLists.txt:2 (project):
  No CMAKE_CXX_COMPILER could be found.

  Tell CMake where to find the compiler by setting either the environment
  variable "CXX" or the CMake cache entry CMAKE_CXX_COMPILER to the full path
  to the compiler, or to the compiler name if it is in the PATH.


-- Configuring incomplete, errors occurred!
```

Seems a problem with cmake version? I downloaded the last version 3.27.6. There is no newer version at:
https://cmake.org/download/

# Discussion History
## SChernykh | 2023-09-29T09:57:58+00:00
You have to install cmake inside MSYS2: `pacman -S cmake`, and then just run `cmake .. -G "Unix Makefiles" -DXMRIG_DEPS=c:/xmrig-deps/gcc/x64`

## fohnbit | 2023-09-29T10:03:50+00:00
Thanks!

This is now working, but on the next steps I get also some errors:
 **make -j$(nproc)**
```
[  2%] Built target xmrig-asm
[  3%] Built target ethash
[  4%] Built target argon2-avx512f
[  5%] Built target argon2-avx2
[  5%] Built target argon2-ssse3
[  8%] Built target argon2-sse2
[ 13%] Built target ghostrider
[ 14%] Built target argon2-xop
[ 16%] Built target argon2
[ 17%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/config/BaseConfig.cpp.obj
[ 19%] [ 19%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/log/backends/ConsoleLog.cpp.obj
Building CXX object CMakeFiles/xmrig.dir/src/base/io/log/Log.cpp.obj
[ 19%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/config/BaseTransform.cpp.obj
[ 19%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/config/Title.cpp.obj
[ 20%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Entry.cpp.obj
[ 20%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Platform.cpp.obj
[ 20%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Process.cpp.obj
[ 21%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/dns/Dns.cpp.obj
[ 21%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/dns/DnsConfig.cpp.obj
[ 21%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/dns/DnsRecord.cpp.obj
[ 22%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/dns/DnsRecords.cpp.obj
[ 22%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/dns/DnsUvBackend.cpp.obj
[ 22%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/Http.cpp.obj
[ 23%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/BaseClient.cpp.obj
[ 23%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Client.cpp.obj
C:/msys64/home/userxy/xmrig/src/base/io/log/backends/ConsoleLog.cpp: In constructor ‘xmrig::ConsoleLog::ConsoleLog(const xmrig::Title&)’:
C:/msys64/home/userxy/xmrig/src/base/io/log/backends/ConsoleLog.cpp:48:5: error: ‘HANDLE’ was not declared in this scope; did you mean ‘UV_HANDLE’?
   48 |     HANDLE handle = GetStdHandle(STD_INPUT_HANDLE);
      |     ^~~~~~
      |     UV_HANDLE
C:/msys64/home/userxy/xmrig/src/base/io/log/backends/ConsoleLog.cpp:49:9: error: ‘handle’ was not declared in this scope
   49 |     if (handle != INVALID_HANDLE_VALUE) { // NOLINT(cppcoreguidelines-pro-type-cstyle-cast, performance-no-int-to-ptr)
      |         ^~~~~~
C:/msys64/home/userxy/xmrig/src/base/io/log/backends/ConsoleLog.cpp:49:19: error: ‘INVALID_HANDLE_VALUE’ was not declared in this scope
   49 |     if (handle != INVALID_HANDLE_VALUE) { // NOLINT(cppcoreguidelines-pro-type-cstyle-cast, performance-no-int-to-ptr)
      |                   ^~~~~~~~~~~~~~~~~~~~
C:/msys64/home/userxy/xmrig/src/base/io/log/backends/ConsoleLog.cpp:50:9: error: ‘DWORD’ was not declared in this scope
   50 |         DWORD mode = 0;
      |         ^~~~~
C:/msys64/home/userxy/xmrig/src/base/io/log/backends/ConsoleLog.cpp:51:37: error: ‘mode’ was not declared in this scope; did you mean ‘mode_t’?
   51 |         if (GetConsoleMode(handle, &mode)) {
      |                                     ^~~~
      |                                     mode_t
C:/msys64/home/userxy/xmrig/src/base/io/log/backends/ConsoleLog.cpp:51:13: error: ‘GetConsoleMode’ was not declared in this scope
   51 |         if (GetConsoleMode(handle, &mode)) {
      |             ^~~~~~~~~~~~~~
C:/msys64/home/userxy/xmrig/src/base/io/log/backends/ConsoleLog.cpp:52:21: error: ‘ENABLE_QUICK_EDIT_MODE’ was not declared in this scope
   52 |            mode &= ~ENABLE_QUICK_EDIT_MODE;
      |                     ^~~~~~~~~~~~~~~~~~~~~~
C:/msys64/home/userxy/xmrig/src/base/io/log/backends/ConsoleLog.cpp:53:42: error: ‘ENABLE_EXTENDED_FLAGS’ was not declared in this scope
   53 |            SetConsoleMode(handle, mode | ENABLE_EXTENDED_FLAGS);
      |                                          ^~~~~~~~~~~~~~~~~~~~~
C:/msys64/home/userxy/xmrig/src/base/io/log/backends/ConsoleLog.cpp:53:12: error: ‘SetConsoleMode’ was not declared in this scope
   53 |            SetConsoleMode(handle, mode | ENABLE_EXTENDED_FLAGS);
      |            ^~~~~~~~~~~~~~
C:/msys64/home/userxy/xmrig/src/base/io/log/backends/ConsoleLog.cpp:58:9: error: ‘SetConsoleTitleA’ was not declared in this scope
   58 |         SetConsoleTitleA(title.value());
      |         ^~~~~~~~~~~~~~~~
make[2]: *** [CMakeFiles/xmrig.dir/build.make:272: CMakeFiles/xmrig.dir/src/base/io/log/backends/ConsoleLog.cpp.obj] Error 1
make[2]: *** Waiting for unfinished jobs....
[ 24%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Job.cpp.obj
In file included from /usr/include/sys/socket.h:13,
                 from C:/xmrig-deps/gcc/x64/include/uv/unix.h:30,
                 from C:/xmrig-deps/gcc/x64/include/uv.h:68,
                 from C:/msys64/home/userxy/xmrig/src/base/io/log/Log.cpp:32:
/usr/include/cygwin/socket.h:27:8: error: redefinition of ‘struct sockaddr’
   27 | struct sockaddr {
      |        ^~~~~~~~
In file included from /usr/include/w32api/winsock2.h:57,
                 from C:/msys64/home/userxy/xmrig/src/base/io/log/Log.cpp:21:
/usr/include/w32api/psdk_inc/_ip_types.h:70:8: note: previous definition of ‘struct sockaddr’
   70 | struct sockaddr {
      |        ^~~~~~~~
/usr/include/cygwin/socket.h:39:8: error: redefinition of ‘struct sockaddr_storage’
   39 | struct sockaddr_storage {
      |        ^~~~~~~~~~~~~~~~
/usr/include/w32api/winsock2.h:269:10: note: previous definition of ‘struct sockaddr_storage’
  269 |   struct sockaddr_storage {
      |          ^~~~~~~~~~~~~~~~
/usr/include/cygwin/socket.h:52:8: error: redefinition of ‘struct linger’
   52 | struct linger {
      |        ^~~~~~
/usr/include/w32api/psdk_inc/_ip_types.h:63:8: note: previous definition of ‘struct linger’
   63 | struct linger {
      |        ^~~~~~
/usr/include/sys/socket.h:21:7: error: conflicting declaration of C function ‘int accept(int, sockaddr*, socklen_t*)’
   21 |   int accept (int, struct sockaddr *__peer, socklen_t *);
      |       ^~~~~~
/usr/include/w32api/winsock2.h:1003:37: note: previous declaration ‘SOCKET accept(SOCKET, sockaddr*, int*)’
 1003 |   WINSOCK_API_LINKAGE SOCKET WSAAPI accept(SOCKET s,struct sockaddr *addr,int *addrlen);
      |                                     ^~~~~~
/usr/include/sys/socket.h:23:7: error: conflicting declaration of C function ‘int bind(int, const sockaddr*, socklen_t)’
   23 |   int bind (int, const struct sockaddr *__my_addr, socklen_t __addrlen);
      |       ^~~~
/usr/include/w32api/winsock2.h:1004:34: note: previous declaration ‘int bind(SOCKET, const sockaddr*, int)’
 1004 |   WINSOCK_API_LINKAGE int WSAAPI bind(SOCKET s,const struct sockaddr *name,int namelen);
      |                                  ^~~~
/usr/include/sys/socket.h:24:7: error: conflicting declaration of C function ‘int connect(int, const sockaddr*, socklen_t)’
   24 |   int connect (int, const struct sockaddr *, socklen_t);
      |       ^~~~~~~
/usr/include/w32api/winsock2.h:1006:34: note: previous declaration ‘int connect(SOCKET, const sockaddr*, int)’
 1006 |   WINSOCK_API_LINKAGE int WSAAPI connect(SOCKET s,const struct sockaddr *name,int namelen);
      |                                  ^~~~~~~
/usr/include/sys/socket.h:25:7: error: conflicting declaration of C function ‘int getpeername(int, sockaddr*, socklen_t*)’
   25 |   int getpeername (int, struct sockaddr *__peer, socklen_t *);
      |       ^~~~~~~~~~~
/usr/include/w32api/winsock2.h:1008:34: note: previous declaration ‘int getpeername(SOCKET, sockaddr*, int*)’
 1008 |   WINSOCK_API_LINKAGE int WSAAPI getpeername(SOCKET s,struct sockaddr *name,int *namelen);
      |                                  ^~~~~~~~~~~
/usr/include/sys/socket.h:26:7: error: conflicting declaration of C function ‘int getsockname(int, sockaddr*, socklen_t*)’
   26 |   int getsockname (int, struct sockaddr *__addr, socklen_t *);
      |       ^~~~~~~~~~~
/usr/include/w32api/winsock2.h:1009:34: note: previous declaration ‘int getsockname(SOCKET, sockaddr*, int*)’
 1009 |   WINSOCK_API_LINKAGE int WSAAPI getsockname(SOCKET s,struct sockaddr *name,int *namelen);
      |                                  ^~~~~~~~~~~
/usr/include/sys/socket.h:27:7: error: conflicting declaration of C function ‘int listen(int, int)’
   27 |   int listen (int, int __n);
      |       ^~~~~~
/usr/include/w32api/winsock2.h:1020:34: note: previous declaration ‘int listen(SOCKET, int)’
 1020 |   WINSOCK_API_LINKAGE int WSAAPI listen(SOCKET s,int backlog);
      |                                  ^~~~~~
/usr/include/sys/socket.h:28:11: error: conflicting declaration of C function ‘ssize_t recv(int, void*, size_t, int)’
   28 |   ssize_t recv (int, void *__buff, size_t __len, int __flags);
      |           ^~~~
/usr/include/w32api/winsock2.h:1028:34: note: previous declaration ‘int recv(SOCKET, char*, int, int)’
 1028 |   WINSOCK_API_LINKAGE int WSAAPI recv(SOCKET s,char *buf,int len,int flags);
      |                                  ^~~~
/usr/include/sys/socket.h:29:11: error: conflicting declaration of C function ‘ssize_t recvfrom(int, void*, size_t, int, sockaddr*, socklen_t*)’
   29 |   ssize_t recvfrom (int, void *__buff, size_t __len, int __flags,
      |           ^~~~~~~~
/usr/include/w32api/winsock2.h:1029:34: note: previous declaration ‘int recvfrom(SOCKET, char*, int, int, sockaddr*, int*)’
 1029 |   WINSOCK_API_LINKAGE int WSAAPI recvfrom(SOCKET s,char *buf,int len,int flags,struct sockaddr *from,int *fromlen);
      |                                  ^~~~~~~~
/usr/include/sys/socket.h:32:11: error: conflicting declaration of C function ‘ssize_t send(int, const void*, size_t, int)’
   32 |   ssize_t send (int, const void *__buff, size_t __len, int __flags);
      |           ^~~~
/usr/include/w32api/winsock2.h:1033:34: note: previous declaration ‘int send(SOCKET, const char*, int, int)’
 1033 |   WINSOCK_API_LINKAGE int WSAAPI send(SOCKET s,const char *buf,int len,int flags);
      |                                  ^~~~
/usr/include/sys/socket.h:34:11: error: conflicting declaration of C function ‘ssize_t sendto(int, const void*, size_t, int, const sockaddr*, socklen_t)’
   34 |   ssize_t sendto (int, const void *, size_t __len, int __flags,
      |           ^~~~~~
/usr/include/w32api/winsock2.h:1034:34: note: previous declaration ‘int sendto(SOCKET, const char*, int, int, const sockaddr*, int)’
 1034 |   WINSOCK_API_LINKAGE int WSAAPI sendto(SOCKET s,const char *buf,int len,int flags,const struct sockaddr *to,int tolen);
      |                                  ^~~~~~
/usr/include/sys/socket.h:36:7: error: conflicting declaration of C function ‘int setsockopt(int, int, int, const void*, socklen_t)’
   36 |   int setsockopt (int __s, int __level, int __optname, const void *optval,
      |       ^~~~~~~~~~
/usr/include/w32api/winsock2.h:1035:34: note: previous declaration ‘int setsockopt(SOCKET, int, int, const char*, int)’
 1035 |   WINSOCK_API_LINKAGE int WSAAPI setsockopt(SOCKET s,int level,int optname,const char *optval,int optlen);
      |                                  ^~~~~~~~~~
/usr/include/sys/socket.h:38:7: error: conflicting declaration of C function ‘int getsockopt(int, int, int, void*, socklen_t*)’
   38 |   int getsockopt (int __s, int __level, int __optname, void *__optval,
      |       ^~~~~~~~~~
/usr/include/w32api/winsock2.h:1010:34: note: previous declaration ‘int getsockopt(SOCKET, int, int, char*, int*)’
 1010 |   WINSOCK_API_LINKAGE int WSAAPI getsockopt(SOCKET s,int level,int optname,char *optval,int *optlen);
      |                                  ^~~~~~~~~~
/usr/include/sys/socket.h:40:7: error: conflicting declaration of C function ‘int shutdown(int, int)’
   40 |   int shutdown (int, int);
      |       ^~~~~~~~
/usr/include/w32api/winsock2.h:1036:34: note: previous declaration ‘int shutdown(SOCKET, int)’
 1036 |   WINSOCK_API_LINKAGE int WSAAPI shutdown(SOCKET s,int how);
      |                                  ^~~~~~~~
/usr/include/sys/socket.h:41:7: error: conflicting declaration of C function ‘int socket(int, int, int)’
   41 |   int socket (int __family, int __type, int __protocol);
      |       ^~~~~~
/usr/include/w32api/winsock2.h:1037:37: note: previous declaration ‘SOCKET socket(int, int, int)’
 1037 |   WINSOCK_API_LINKAGE SOCKET WSAAPI socket(int af,int type,int protocol);
      |                                     ^~~~~~
/usr/include/cygwin/in.h:39:3: error: expected identifier before numeric constant
   39 |   IPPROTO_IP = 0,               /* Dummy protocol for TCP               */
      |   ^~~~~~~~~~
/usr/include/cygwin/in.h:39:3: error: expected ‘}’ before numeric constant
In file included from /usr/include/netinet/in.h:12,
                 from C:/xmrig-deps/gcc/x64/include/uv/unix.h:31:
/usr/include/cygwin/in.h:38:1: note: to match this ‘{’
   38 | {
      | ^
/usr/include/cygwin/in.h:39:3: error: expected unqualified-id before numeric constant
   39 |   IPPROTO_IP = 0,               /* Dummy protocol for TCP               */
      |   ^~~~~~~~~~
/usr/include/cygwin/in.h:85:3: error: expected identifier before numeric constant
   85 |   IPPORT_ECHO = 7,              /* Echo service.  */
      |   ^~~~~~~~~~~
/usr/include/cygwin/in.h:85:3: error: expected ‘}’ before numeric constant
/usr/include/cygwin/in.h:84:1: note: to match this ‘{’
   84 | {
      | ^
/usr/include/cygwin/in.h:85:3: error: expected unqualified-id before numeric constant
   85 |   IPPORT_ECHO = 7,              /* Echo service.  */
      |   ^~~~~~~~~~~
/usr/include/cygwin/in.h:120:1: error: expected declaration before ‘}’ token
  120 | };
      | ^
/usr/include/cygwin/in.h:196:8: error: redefinition of ‘struct sockaddr_in’
  196 | struct sockaddr_in
      |        ^~~~~~~~~~~
/usr/include/w32api/psdk_inc/_ip_types.h:75:8: note: previous definition of ‘struct sockaddr_in’
   75 | struct sockaddr_in {
      |        ^~~~~~~~~~~
In file included from C:/xmrig-deps/gcc/x64/include/uv/unix.h:34:
/usr/include/netdb.h:75:9: error: redefinition of ‘struct hostent’
   75 | struct  hostent {
      |         ^~~~~~~
/usr/include/w32api/psdk_inc/_ip_types.h:25:8: note: previous definition of ‘struct hostent’
   25 | struct hostent {
      |        ^~~~~~~
/usr/include/netdb.h:89:9: error: redefinition of ‘struct netent’
   89 | struct  netent {
      |         ^~~~~~
/usr/include/w32api/psdk_inc/_ip_types.h:33:8: note: previous definition of ‘struct netent’
   33 | struct netent {
      |        ^~~~~~
/usr/include/netdb.h:96:9: error: redefinition of ‘struct servent’
   96 | struct  servent {
      |         ^~~~~~~
/usr/include/w32api/psdk_inc/_ip_types.h:40:8: note: previous definition of ‘struct servent’
   40 | struct servent {
      |        ^~~~~~~
/usr/include/netdb.h:103:9: error: redefinition of ‘struct protoent’
  103 | struct  protoent
      |         ^~~~~~~~
/usr/include/w32api/psdk_inc/_ip_types.h:52:8: note: previous definition of ‘struct protoent’
   52 | struct protoent {
      |        ^~~~~~~~
/usr/include/netdb.h:227:18: error: conflicting declaration of C function ‘hostent* gethostbyaddr(const void*, socklen_t, int)’
  227 | struct hostent  *gethostbyaddr (const void *, socklen_t, int);
      |                  ^~~~~~~~~~~~~
/usr/include/w32api/winsock2.h:1038:46: note: previous declaration ‘hostent* gethostbyaddr(const char*, int, int)’
 1038 |   WINSOCK_API_LINKAGE struct hostent *WSAAPI gethostbyaddr(const char *addr,int len,int type);
      |                                              ^~~~~~~~~~~~~
C:/xmrig-deps/gcc/x64/include/uv.h:1848:1: error: expected declaration before ‘}’ token
 1848 | }
      | ^
make[2]: *** [CMakeFiles/xmrig.dir/build.make:317: CMakeFiles/xmrig.dir/src/base/io/log/Log.cpp.obj] Error 1
make[1]: *** [CMakeFiles/Makefile2:182: CMakeFiles/xmrig.dir/all] Error 2
make: *** [Makefile:91: all] Error 2
```

## SChernykh | 2023-09-29T10:13:01+00:00
You probably need to download the latest dependencies from https://github.com/xmrig/xmrig-deps/ - just download the repository itself, and then take gcc/x64 folder.

## fohnbit | 2023-09-29T10:28:46+00:00
Unfortunately same error. I download from https://github.com/xmrig/xmrig-deps/ and extract alle files in c:/xmrig-deps.

**"c:\Program Files\CMake\bin\cmake.exe" .. -G "Unix Makefiles" -DXMRIG_DEPS=c:/xmrig-deps/gcc/x64**
Was running ok

**make -j$(nproc)**
produce the error


## fohnbit | 2023-09-29T10:38:15+00:00
Hi!

I was able to build with Visual Studio:

```
git clone https://github.com/xmrig/xmrig.git
mkdir xmrig\build && cd xmrig\build
cmake .. -G "Visual Studio 17 2022" -A x64 -DXMRIG_DEPS=c:\xmrig-deps\msvc2019\x64
cmake --build . --config Release
```

## SChernykh | 2023-09-29T11:23:56+00:00
Then it must be something with your MSYS2 installation, maybe it's not updated to the latest. The error you get is from missing Windows headers. I just checked and XMRig compiles fine on MSYS2 for me.

# Action History
- Created by: fohnbit | 2023-09-29T09:45:46+00:00
- Closed at: 2025-06-18T22:20:10+00:00
