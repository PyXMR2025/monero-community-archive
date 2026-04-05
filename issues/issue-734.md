---
title: There is a version for linux I386?
source_url: https://github.com/xmrig/xmrig/issues/734
author: artemide601
assignees: []
labels:
- libuv
created_at: '2018-08-09T22:10:44+00:00'
updated_at: '2018-11-05T06:58:38+00:00'
type: issue
status: closed
closed_at: '2018-11-05T06:58:38+00:00'
---

# Original Description
I triyed to compile to a centos 7 i386 machine,
i got to fix all the issue untill the make command
the make command will retutn errors and the won' compile...

so, my question is, there ia an already compiled version for linux i386 ?

# Discussion History
## bananajamma | 2018-08-10T08:17:39+00:00
> the make command will retutn errors and the won' compile...

You should paste the errors in this issue, as well as the commands you used to build.

## artemide601 | 2018-08-10T12:53:01+00:00
as wrote in the wiki https://github.com/xmrig/xmrig/wiki/CentOS-Build
i did the following commands:

sudo yum install -y epel-release
sudo yum install -y git make cmake gcc gcc-c++ libstdc++-static libmicrohttpd-devel libuv-static
git clone https://github.com/xmrig/xmrig.git
cd xmrig
mkdir build
cd build

till now everithing fine (well, i had some trouble to install some pakage, but at the end all are installed and updated)

I changed the cmake parameters, here the command I gave

cmake .. -DCMAKE_BUILD_TYPE=Release -DWITH_LIBCPUID=OFF -DWITH_HTTPD=OFF
-- The C compiler identification is GNU 4.8.5
-- The CXX compiler identification is GNU 4.8.5
-- Check for working C compiler: /usr/bin/cc
-- Check for working C compiler: /usr/bin/cc -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working CXX compiler: /usr/bin/c++
-- Check for working CXX compiler: /usr/bin/c++ -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Found UV: /usr/lib/libuv.a
-- Looking for syslog.h
-- Looking for syslog.h - found
-- Configuring done
-- Generating done
-- Build files have been written to: /opt/xmrig/build

seem ok, now I give the make command and this is the error I have

[root@osboxes build]# make
Scanning dependencies of target xmrig
[  2%] Building CXX object CMakeFiles/xmrig.dir/src/api/NetworkState.cpp.o
[  4%] Building CXX object CMakeFiles/xmrig.dir/src/App.cpp.o
In file included from /opt/xmrig/src/workers/Workers.h:34:0,
                 from /opt/xmrig/src/App.cpp:42:
/opt/xmrig/src/net/JobResult.h: In member function ‘uint64_t JobResult::actualDiff() const’:
/opt/xmrig/src/net/JobResult.h:52:71: warning: dereferencing type-punned pointer will break strict-aliasing rules [-Wstrict-aliasing]
         return Job::toDiff(reinterpret_cast<const uint64_t*>(result)[3]);
                                                                       ^
/opt/xmrig/src/App.cpp: In member function ‘int App::exec()’:
/opt/xmrig/src/App.cpp:131:36: error: ‘uv_loop_close’ was not declared in this scope
     uv_loop_close(uv_default_loop());
                                    ^
make[2]: *** [CMakeFiles/xmrig.dir/src/App.cpp.o] Error 1
make[1]: *** [CMakeFiles/xmrig.dir/all] Error 2
make: *** [all] Error 2
[root@osboxes build]#

note that the ^ simbol does not show in the same place as in my machine, 
in the first occurrence is under 3]) , in the second one is under ));

if it can help, here the detail of my system, is a virtual machine take from osboxes
[root@osboxes build]# uname -a
Linux osboxes 3.10.0-862.9.1.el7.centos.plus.i686 #1 SMP Tue Jul 17 12:37:35 UTC 2018 i686 i686 i386 GNU/Linux


## bananajamma | 2018-08-10T15:40:54+00:00
See if the resolution here helps you:

> libuv 0.10 not supported, use libuv 1+.

https://github.com/xmrig/xmrig-proxy/issues/157

## artemide601 | 2018-08-10T19:33:24+00:00
hello,
i'm not able to find a libu version for i686 greather than libuv-0.10.34...


## trasherdk | 2018-08-11T05:29:38+00:00
Take a look at this one: https://github.com/libuv/libuv

## artemide601 | 2018-08-21T22:27:07+00:00
here an update...

i've been away for soe days, when i was back i tryed to compile the updated libuv, but it requires an updated cmake, updating the cmake it "loose" some packets... fixing up this there is a conflict with a library, trying to unistall it for instlling an update version but it fail because it is used by some system files.....
i gived up to compile it on the centos machine...

at the end i instlled a vm fedora 28 32 bit, compiled the xmring (everithing worked fine) and moved the executble to the centos machine, it works !!! :-) 



## bananajamma | 2018-08-21T22:28:29+00:00
good, glad you figured out a solution that works for you.

# Action History
- Created by: artemide601 | 2018-08-09T22:10:44+00:00
- Closed at: 2018-11-05T06:58:38+00:00
