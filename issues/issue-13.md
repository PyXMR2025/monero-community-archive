---
title: Can not build xmrig under windows xp
source_url: https://github.com/xmrig/xmrig/issues/13
author: tomay3000
assignees: []
labels: []
created_at: '2017-06-15T13:49:26+00:00'
updated_at: '2017-06-16T16:12:00+00:00'
type: issue
status: closed
closed_at: '2017-06-16T16:12:00+00:00'
---

# Original Description
I have successfully built libcurl v7.54.1 with the options described, but xmrig is compiling with the following errors:
`$ make
[ 11%] Built target cpuid
[ 37%] Built target jansson
Scanning dependencies of target xmrig32
[ 39%] Building C object CMakeFiles/xmrig32.dir/xmrig.c.obj
[ 41%] Building C object CMakeFiles/xmrig32.dir/stratum.c.obj
C:/xmrig/stratum.c: In function 'send_line':
C:/xmrig/stratum.c:442:23: error: storage size of 'pfd' isn't known
         struct pollfd pfd;
                       ^~~
C:/xmrig/stratum.c:444:22: error: 'POLLOUT' undeclared (first use in this function); did you mean 'PUAFOUT'?
         pfd.events = POLLOUT;
                      ^~~~~~~
                      PUAFOUT
C:/xmrig/stratum.c:444:22: note: each undeclared identifier is reported only once for each function it appears in
C:/xmrig/stratum.c:52:41: warning: implicit declaration of function 'WSAPoll'; did you mean 'WSANtohl'? [-Wimplicit-function-declaration]
 #   define poll(fdarray, nfds, timeout) WSAPoll(fdarray, nfds, timeout)
                                         ^
C:/xmrig/stratum.c:52:41: note: in definition of macro 'poll'
 #   define poll(fdarray, nfds, timeout) WSAPoll(fdarray, nfds, timeout)
                                         ^~~~~~~
C:/xmrig/stratum.c: In function 'socket_full':
C:/xmrig/stratum.c:475:19: error: storage size of 'pfd' isn't known
     struct pollfd pfd;
                   ^~~
C:/xmrig/stratum.c:477:18: error: 'POLLIN' undeclared (first use in this function); did you mean 'LPOLELINK'?
     pfd.events = POLLIN;
                  ^~~~~~
                  LPOLELINK
CMakeFiles/xmrig32.dir/build.make:238: recipe for target 'CMakeFiles/xmrig32.dir/stratum.c.obj' failed
make[2]: *** [CMakeFiles/xmrig32.dir/stratum.c.obj] Error 1
CMakeFiles/Makefile2:61: recipe for target 'CMakeFiles/xmrig32.dir/all' failed
make[1]: *** [CMakeFiles/xmrig32.dir/all] Error 2
Makefile:75: recipe for target 'all' failed
make: *** [all] Error 2
`
What is the problem here ?


# Discussion History
## xmrig | 2017-06-15T17:32:35+00:00
Windows XP not supported.

In dev branch miner rewritten on C++ with libuv, libcurl dependency removed. It can compile and run on Windows XP, but... not connect to pool at all. I have not looked why it. Maybe need downgrade of libuv version, etc.

## tomay3000 | 2017-06-16T02:00:13+00:00
Thank you for the reply.
I will try Windows 7 Pro x86.

**EDIT:** it compiles without problems under windows 7.

# Action History
- Created by: tomay3000 | 2017-06-15T13:49:26+00:00
- Closed at: 2017-06-16T16:12:00+00:00
