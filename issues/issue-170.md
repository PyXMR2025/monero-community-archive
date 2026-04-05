---
title: Error when running make in Centos7
source_url: https://github.com/xmrig/xmrig/issues/170
author: StealthBadger747
assignees: []
labels: []
created_at: '2017-10-24T18:37:51+00:00'
updated_at: '2018-03-14T23:21:48+00:00'
type: issue
status: closed
closed_at: '2018-03-14T23:21:48+00:00'
---

# Original Description
I got cmake3 to successfully run, but I have this error when running make.
```
[erikthered@xmpserver24 build]$ sudo make
[ 12%] Built target cpuid
[ 14%] Building CXX object CMakeFiles/xmrig.dir/src/api/Api.cpp.o
In file included from /home/erikthered/xmrig/src/api/Api.cpp:27:0:
/home/erikthered/xmrig/src/api/Api.h:28:16: fatal error: uv.h: No such file or directory
 #include <uv.h>
                ^
compilation terminated.
make[2]: *** [CMakeFiles/xmrig.dir/src/api/Api.cpp.o] Error 1
make[1]: *** [CMakeFiles/xmrig.dir/all] Error 2
make: *** [all] Error 2
```


# Discussion History
## xmrig | 2017-10-24T19:00:01+00:00
You need libuv 1.x.x to build. If you have libuv 0.10.x it also not supported.
Thank you. 

## StealthBadger747 | 2017-10-24T19:59:47+00:00
Package 1:libuv-1.10.2-1.el7.x86_64 already installed and latest version

Still throws the same error

## mnik247 | 2017-10-24T20:25:50+00:00
What about "libuv-devel-1.10.2-1.el7.x86_64"?

## StealthBadger747 | 2017-10-24T21:32:42+00:00
Thank you! We're making progress, but now I get this error.
```
[ 12%] Built target cpuid
make[2]: *** No rule to make target `/usr/lib64/libuv.a', needed by `xmrig'.  Stop.
make[1]: *** [CMakeFiles/xmrig.dir/all] Error 2
make: *** [all] Error 2
```
Sorry for being such a noob, I really need to learn how to properly troubleshoot these type if errors.

EDIT: Found that it is caused by duplicate libraries, I'm trying to find the duplicates right now.

EDIT2:  I tried to uninstall the other 'conflicting library, but there ended up not being any duplicate libraries
```
[root@xmpserver24 build]# repoquery -a --installed | grep libuv
libuv-1:1.10.2-1.el7.x86_64
libuv-devel-1:1.10.2-1.el7.x86_64
```
And I still get this error when I make 
```
[root@xmpserver24 build]# make
[ 12%] Built target cpuid
make[2]: *** No rule to make target `/usr/lib64/libuv.a', needed by `xmrig'.  Stop.
make[1]: *** [CMakeFiles/xmrig.dir/all] Error 2
make: *** [all] Error 2
```


## StealthBadger747 | 2017-10-24T23:08:21+00:00
I redid everything, including git clone, etc...
```
[erikthered@xmpserver24 build]$ sudo make
Scanning dependencies of target cpuid
[  2%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/cpuid_main.c.o
[  4%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/asm-bits.c.o
[  6%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/recog_amd.c.o
[  8%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/recog_intel.c.o
[ 10%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/libcpuid_util.c.o
[ 12%] Linking C static library libcpuid.a
[ 12%] Built target cpuid
Scanning dependencies of target xmrig
[ 14%] Building CXX object CMakeFiles/xmrig.dir/src/api/Api.cpp.o
[ 16%] Building CXX object CMakeFiles/xmrig.dir/src/api/ApiState.cpp.o
[ 18%] Building CXX object CMakeFiles/xmrig.dir/src/api/NetworkState.cpp.o
[ 20%] Building CXX object CMakeFiles/xmrig.dir/src/App.cpp.o
In file included from /home/erikthered/xmrig/src/workers/Workers.h:34:0,
                 from /home/erikthered/xmrig/src/App.cpp:43:
/home/erikthered/xmrig/src/net/JobResult.h: In member function ‘uint64_t JobResult::actualDiff() const’:
/home/erikthered/xmrig/src/net/JobResult.h:69:71: warning: dereferencing type-punned pointer will break strict-aliasing rules [-Wstrict-aliasing]
         return Job::toDiff(reinterpret_cast<const uint64_t*>(result)[3]);
                                                                       ^
[ 22%] Building CXX object CMakeFiles/xmrig.dir/src/Console.cpp.o
[ 25%] Building CXX object CMakeFiles/xmrig.dir/src/log/ConsoleLog.cpp.o
[ 27%] Building CXX object CMakeFiles/xmrig.dir/src/log/FileLog.cpp.o
[ 29%] Building CXX object CMakeFiles/xmrig.dir/src/log/Log.cpp.o
[ 31%] Building CXX object CMakeFiles/xmrig.dir/src/Mem.cpp.o
[ 33%] Building CXX object CMakeFiles/xmrig.dir/src/net/Client.cpp.o
In file included from /home/erikthered/xmrig/src/net/Client.cpp:44:0:
/home/erikthered/xmrig/src/net/JobResult.h: In member function ‘uint64_t JobResult::actualDiff() const’:
/home/erikthered/xmrig/src/net/JobResult.h:69:71: warning: dereferencing type-punned pointer will break strict-aliasing rules [-Wstrict-aliasing]
         return Job::toDiff(reinterpret_cast<const uint64_t*>(result)[3]);
                                                                       ^
[ 35%] Building CXX object CMakeFiles/xmrig.dir/src/net/Job.cpp.o
[ 37%] Building CXX object CMakeFiles/xmrig.dir/src/net/Network.cpp.o
In file included from /home/erikthered/xmrig/src/workers/Workers.h:34:0,
                 from /home/erikthered/xmrig/src/net/Network.cpp:44:
/home/erikthered/xmrig/src/net/JobResult.h: In member function ‘uint64_t JobResult::actualDiff() const’:
/home/erikthered/xmrig/src/net/JobResult.h:69:71: warning: dereferencing type-punned pointer will break strict-aliasing rules [-Wstrict-aliasing]
         return Job::toDiff(reinterpret_cast<const uint64_t*>(result)[3]);
                                                                       ^
[ 39%] Building CXX object CMakeFiles/xmrig.dir/src/net/strategies/DonateStrategy.cpp.o
[ 41%] Building CXX object CMakeFiles/xmrig.dir/src/net/strategies/FailoverStrategy.cpp.o
[ 43%] Building CXX object CMakeFiles/xmrig.dir/src/net/strategies/SinglePoolStrategy.cpp.o
[ 45%] Building CXX object CMakeFiles/xmrig.dir/src/net/SubmitResult.cpp.o
[ 47%] Building CXX object CMakeFiles/xmrig.dir/src/net/Url.cpp.o
[ 50%] Building CXX object CMakeFiles/xmrig.dir/src/Options.cpp.o
[ 52%] Building CXX object CMakeFiles/xmrig.dir/src/Platform.cpp.o
[ 54%] Building CXX object CMakeFiles/xmrig.dir/src/Summary.cpp.o
[ 56%] Building CXX object CMakeFiles/xmrig.dir/src/workers/DoubleWorker.cpp.o
In file included from /home/erikthered/xmrig/src/workers/DoubleWorker.h:30:0,
                 from /home/erikthered/xmrig/src/workers/DoubleWorker.cpp:29:
/home/erikthered/xmrig/src/net/JobResult.h: In member function ‘uint64_t JobResult::actualDiff() const’:
/home/erikthered/xmrig/src/net/JobResult.h:69:71: warning: dereferencing type-punned pointer will break strict-aliasing rules [-Wstrict-aliasing]
         return Job::toDiff(reinterpret_cast<const uint64_t*>(result)[3]);
                                                                       ^
/home/erikthered/xmrig/src/workers/DoubleWorker.cpp: In member function ‘virtual void DoubleWorker::start()’:
/home/erikthered/xmrig/src/workers/DoubleWorker.cpp:90:57: warning: dereferencing type-punned pointer will break strict-aliasing rules [-Wstrict-aliasing]
             if (*reinterpret_cast<uint64_t*>(m_hash + 24) < m_state->job.target()) {
                                                         ^
/home/erikthered/xmrig/src/workers/DoubleWorker.cpp:94:62: warning: dereferencing type-punned pointer will break strict-aliasing rules [-Wstrict-aliasing]
             if (*reinterpret_cast<uint64_t*>(m_hash + 32 + 24) < m_state->job.target()) {
                                                              ^
[ 58%] Building CXX object CMakeFiles/xmrig.dir/src/workers/Handle.cpp.o
[ 60%] Building CXX object CMakeFiles/xmrig.dir/src/workers/Hashrate.cpp.o
[ 62%] Building CXX object CMakeFiles/xmrig.dir/src/workers/SingleWorker.cpp.o
In file included from /home/erikthered/xmrig/src/workers/SingleWorker.h:29:0,
                 from /home/erikthered/xmrig/src/workers/SingleWorker.cpp:29:
/home/erikthered/xmrig/src/net/JobResult.h: In member function ‘uint64_t JobResult::actualDiff() const’:
/home/erikthered/xmrig/src/net/JobResult.h:69:71: warning: dereferencing type-punned pointer will break strict-aliasing rules [-Wstrict-aliasing]
         return Job::toDiff(reinterpret_cast<const uint64_t*>(result)[3]);
                                                                       ^
[ 64%] Building CXX object CMakeFiles/xmrig.dir/src/workers/Worker.cpp.o
[ 66%] Building CXX object CMakeFiles/xmrig.dir/src/workers/Workers.cpp.o
In file included from /home/erikthered/xmrig/src/workers/DoubleWorker.h:30:0,
                 from /home/erikthered/xmrig/src/workers/Workers.cpp:31:
/home/erikthered/xmrig/src/net/JobResult.h: In member function ‘uint64_t JobResult::actualDiff() const’:
/home/erikthered/xmrig/src/net/JobResult.h:69:71: warning: dereferencing type-punned pointer will break strict-aliasing rules [-Wstrict-aliasing]
         return Job::toDiff(reinterpret_cast<const uint64_t*>(result)[3]);
                                                                       ^
[ 68%] Building CXX object CMakeFiles/xmrig.dir/src/xmrig.cpp.o
[ 70%] Building CXX object CMakeFiles/xmrig.dir/src/App_unix.cpp.o
[ 72%] Building CXX object CMakeFiles/xmrig.dir/src/Cpu_unix.cpp.o
[ 75%] Building CXX object CMakeFiles/xmrig.dir/src/Mem_unix.cpp.o
[ 77%] Building CXX object CMakeFiles/xmrig.dir/src/Platform_unix.cpp.o
[ 79%] Building CXX object CMakeFiles/xmrig.dir/src/Cpu.cpp.o
[ 81%] Building C object CMakeFiles/xmrig.dir/src/crypto/c_keccak.c.o
[ 83%] Building C object CMakeFiles/xmrig.dir/src/crypto/c_groestl.c.o
[ 85%] Building C object CMakeFiles/xmrig.dir/src/crypto/c_blake256.c.o
[ 87%] Building C object CMakeFiles/xmrig.dir/src/crypto/c_jh.c.o
[ 89%] Building C object CMakeFiles/xmrig.dir/src/crypto/c_skein.c.o
[ 91%] Building C object CMakeFiles/xmrig.dir/src/crypto/soft_aes.c.o
[ 93%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/CryptoNight.cpp.o
In file included from /home/erikthered/xmrig/src/crypto/CryptoNight.cpp:29:0:
/home/erikthered/xmrig/src/net/JobResult.h: In member function ‘uint64_t JobResult::actualDiff() const’:
/home/erikthered/xmrig/src/net/JobResult.h:69:71: warning: dereferencing type-punned pointer will break strict-aliasing rules [-Wstrict-aliasing]
         return Job::toDiff(reinterpret_cast<const uint64_t*>(result)[3]);
                                                                       ^
/home/erikthered/xmrig/src/crypto/CryptoNight.cpp: In static member function ‘static bool CryptoNight::hash(const Job&, JobResult&, cryptonight_ctx*)’:
/home/erikthered/xmrig/src/crypto/CryptoNight.cpp:100:59: warning: dereferencing type-punned pointer will break strict-aliasing rules [-Wstrict-aliasing]
     return *reinterpret_cast<uint64_t*>(result.result + 24) < job.target();
                                                           ^
[ 95%] Building CXX object CMakeFiles/xmrig.dir/src/log/SysLog.cpp.o
[ 97%] Building CXX object CMakeFiles/xmrig.dir/src/api/Httpd.cpp.o
make[2]: *** No rule to make target `/usr/lib64/libuv.a', needed by `xmrig'.  Stop.
make[1]: *** [CMakeFiles/xmrig.dir/all] Error 2
make: *** [all] Error 2
```

## StealthBadger747 | 2017-10-25T00:15:04+00:00
I just installed Ubuntu 16.04 and got it over with...  Feel free to close this issue

## archenroot | 2017-12-11T17:14:23+00:00
@xmrig  Don't close this issue I have installed package libuv on Gentoo with following package files:
```
/usr
/usr/include
/usr/include/uv-errno.h
/usr/include/uv-linux.h
/usr/include/uv-threadpool.h
/usr/include/uv-unix.h
/usr/include/uv-version.h
/usr/include/uv.h
/usr/lib64
/usr/lib64/libuv.so -> libuv.so.1.0.0
/usr/lib64/libuv.so.1 -> libuv.so.1.0.0
/usr/lib64/libuv.so.1.0.0
/usr/lib64/pkgconfig
/usr/lib64/pkgconfig/libuv.pc
/usr/share
/usr/share/doc
/usr/share/doc/libuv-1.10.2
/usr/share/doc/libuv-1.10.2/AUTHORS.bz2
/usr/share/doc/libuv-1.10.2/ChangeLog.bz2
/usr/share/doc/libuv-1.10.2/README.md.bz2
```
Still having error:
zangetsu@mobile-server ~/devel/proj/crypto-currency/xmrig/build $ make
[ 12%] Built target cpuid
make[2]: *** No rule to make target '/usr/lib64/libuv.a', needed by 'xmrig'.  Stop.
make[1]: *** [CMakeFiles/Makefile2:68: CMakeFiles/xmrig.dir/all] Error 2
make: *** [Makefile:84: all] Error 2


## archenroot | 2017-12-11T17:20:17+00:00
Ok I fixed by installing package with static-libs option:
```
mobile-server ~ # equery f libuv
 * Searching for libuv ...
 * Contents of dev-libs/libuv-1.10.2:
/usr
/usr/include
/usr/include/uv-errno.h
/usr/include/uv-linux.h
/usr/include/uv-threadpool.h
/usr/include/uv-unix.h
/usr/include/uv-version.h
/usr/include/uv.h
/usr/lib32
/usr/lib32/libuv.a
/usr/lib32/libuv.so -> libuv.so.1.0.0
/usr/lib32/libuv.so.1 -> libuv.so.1.0.0
/usr/lib32/libuv.so.1.0.0
/usr/lib32/pkgconfig
/usr/lib32/pkgconfig/libuv.pc
/usr/lib64
/usr/lib64/libuv.a
/usr/lib64/libuv.so -> libuv.so.1.0.0
/usr/lib64/libuv.so.1 -> libuv.so.1.0.0
/usr/lib64/libuv.so.1.0.0
/usr/lib64/pkgconfig
/usr/lib64/pkgconfig/libuv.pc
/usr/share
/usr/share/doc
/usr/share/doc/libuv-1.10.2
/usr/share/doc/libuv-1.10.2/AUTHORS.bz2
/usr/share/doc/libuv-1.10.2/ChangeLog.bz2
/usr/share/doc/libuv-1.10.2/README.md.bz2
```


## biaxz | 2018-01-07T02:09:39+00:00
any ide to build it with Centos 7?
np : 

all libuv installed
libuv-1.10.2-1.el7.x86_64
libuv-static-1.10.2-1.el7.x86_64
libuv-devel-1.10.2-1.el7.x86_64


 I still get this :

```
[ 81%] Building CXX object CMakeFiles/xmrig.dir/src/Platform_unix.cpp.o
[ 84%] Building CXX object CMakeFiles/xmrig.dir/src/Cpu.cpp.o
[ 86%] Building C object CMakeFiles/xmrig.dir/src/crypto/c_keccak.c.o
[ 88%] Building C object CMakeFiles/xmrig.dir/src/crypto/c_groestl.c.o
[ 90%] Building C object CMakeFiles/xmrig.dir/src/crypto/c_blake256.c.o
[ 93%] Building C object CMakeFiles/xmrig.dir/src/crypto/c_jh.c.o
[ 95%] Building C object CMakeFiles/xmrig.dir/src/crypto/c_skein.c.o
[ 97%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/CryptoNight.cpp.o
[100%] Building CXX object CMakeFiles/xmrig.dir/src/log/SysLog.cpp.o
make[2]: *** No rule to make target `usr/lib64/libuv.a', needed by `xmrig'.  Stop.
make[1]: *** [CMakeFiles/xmrig.dir/all] Error 2
make: *** [all] Error 2
```


  

## biaxz | 2018-01-07T02:28:52+00:00
aha! done using build from source libuv 

https://github.com/libuv/libuv


with option cmake 
cmake .. -DUV_INCLUDE_DIR=usr/local/include -DUV_LIBRARY=/usr/local/lib/libuv.a

` cmake .. -DUV_INCLUDE_DIR=usr/local/include -DUV_LIBRARY                                                                                        =/usr/local/lib/libuv.a
-- The C compiler identification is GNU 5.3.1
-- The CXX compiler identification is GNU 5.3.1
-- Check for working C compiler: /opt/rh/devtoolset-4/root/usr/bin/cc
-- Check for working C compiler: /opt/rh/devtoolset-4/root/usr/bin/cc -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working CXX compiler: /opt/rh/devtoolset-4/root/usr/bin/c++
-- Check for working CXX compiler: /opt/rh/devtoolset-4/root/usr/bin/c++ -- work                                                                                        s
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Found UV: /usr/local/lib/libuv.a
-- Looking for syslog.h
-- Looking for syslog.h - found
-- Found mhd: /usr/include
-- Configuring done
-- Generating done
-- Build files have been written to: /root/xmrig/build
[root@localhost build]# make
Scanning dependencies of target cpuid
[  2%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/cpuid_main.c                                                                                        .o
[  4%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/asm-bits.c.o
[  6%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/recog_amd.c.                                                                                        o
[  8%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/recog_intel.                                                                                        c.o
[ 11%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/libcpuid_uti                                                                                        l.c.o
Linking C static library libcpuid.a
[ 11%] Built target cpuid
Scanning dependencies of target xmrig
[ 13%] Building CXX object CMakeFiles/xmrig.dir/src/api/Api.cpp.o
[ 15%] Building CXX object CMakeFiles/xmrig.dir/src/api/ApiState.cpp.o
[ 17%] Building CXX object CMakeFiles/xmrig.dir/src/api/NetworkState.cpp.o
[ 20%] Building CXX object CMakeFiles/xmrig.dir/src/App.cpp.o
[ 22%] Building CXX object CMakeFiles/xmrig.dir/src/Console.cpp.o
[ 24%] Building CXX object CMakeFiles/xmrig.dir/src/log/ConsoleLog.cpp.o
[ 26%] Building CXX object CMakeFiles/xmrig.dir/src/log/FileLog.cpp.o
[ 28%] Building CXX object CMakeFiles/xmrig.dir/src/log/Log.cpp.o
[ 31%] Building CXX object CMakeFiles/xmrig.dir/src/Mem.cpp.o
[ 33%] Building CXX object CMakeFiles/xmrig.dir/src/net/Client.cpp.o
[ 35%] Building CXX object CMakeFiles/xmrig.dir/src/net/Job.cpp.o
[ 37%] Building CXX object CMakeFiles/xmrig.dir/src/net/Network.cpp.o
[ 40%] Building CXX object CMakeFiles/xmrig.dir/src/net/strategies/DonateStrateg                                                                                        y.cpp.o
[ 42%] Building CXX object CMakeFiles/xmrig.dir/src/net/strategies/FailoverStrat                                                                                        egy.cpp.o
[ 44%] Building CXX object CMakeFiles/xmrig.dir/src/net/strategies/SinglePoolStr                                                                                        ategy.cpp.o
[ 46%] Building CXX object CMakeFiles/xmrig.dir/src/net/SubmitResult.cpp.o
[ 48%] Building CXX object CMakeFiles/xmrig.dir/src/net/Url.cpp.o
[ 51%] Building CXX object CMakeFiles/xmrig.dir/src/Options.cpp.o
[ 53%] Building CXX object CMakeFiles/xmrig.dir/src/Platform.cpp.o
[ 55%] Building CXX object CMakeFiles/xmrig.dir/src/Summary.cpp.o
[ 57%] Building CXX object CMakeFiles/xmrig.dir/src/workers/DoubleWorker.cpp.o
[ 60%] Building CXX object CMakeFiles/xmrig.dir/src/workers/Handle.cpp.o
[ 62%] Building CXX object CMakeFiles/xmrig.dir/src/workers/Hashrate.cpp.o
[ 64%] Building CXX object CMakeFiles/xmrig.dir/src/workers/SingleWorker.cpp.o
[ 66%] Building CXX object CMakeFiles/xmrig.dir/src/workers/Worker.cpp.o
[ 68%] Building CXX object CMakeFiles/xmrig.dir/src/workers/Workers.cpp.o
[ 71%] Building CXX object CMakeFiles/xmrig.dir/src/xmrig.cpp.o
[ 73%] Building CXX object CMakeFiles/xmrig.dir/src/App_unix.cpp.o
[ 75%] Building CXX object CMakeFiles/xmrig.dir/src/Cpu_unix.cpp.o
[ 77%] Building CXX object CMakeFiles/xmrig.dir/src/Mem_unix.cpp.o
[ 80%] Building CXX object CMakeFiles/xmrig.dir/src/Platform_unix.cpp.o
[ 82%] Building CXX object CMakeFiles/xmrig.dir/src/Cpu.cpp.o
[ 84%] Building C object CMakeFiles/xmrig.dir/src/crypto/c_keccak.c.o
[ 86%] Building C object CMakeFiles/xmrig.dir/src/crypto/c_groestl.c.o
[ 88%] Building C object CMakeFiles/xmrig.dir/src/crypto/c_blake256.c.o
[ 91%] Building C object CMakeFiles/xmrig.dir/src/crypto/c_jh.c.o
[ 93%] Building C object CMakeFiles/xmrig.dir/src/crypto/c_skein.c.o
[ 95%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/CryptoNight.cpp.o
[ 97%] Building CXX object CMakeFiles/xmrig.dir/src/log/SysLog.cpp.o
[100%] Building CXX object CMakeFiles/xmrig.dir/src/api/Httpd.cpp.o
Linking CXX executable xmrig
[100%] Built target xmrig
`

thanks!




## randallrodrigues | 2018-01-18T20:31:01+00:00
i was also getting this error 

[ 97%] Building CXX object CMakeFiles/xmrig.dir/src/log/SysLog.cpp.o
[100%] Building CXX object CMakeFiles/xmrig.dir/src/api/Httpd.cpp.o
make[2]: *** No rule to make target `/usr/lib64/libuv.a', needed by `xmrig'.  Stop.
make[1]: *** [CMakeFiles/xmrig.dir/all] Error 2
make: *** [all] Error 2


Got these packages installed and fixed the issue which was failing..


libuv-static-1.10.2-1.el7.x86_64.rpm
libuv-devel-1.10.2-1.el7.x86_64.rpm
libuv-1.10.2-1.el7.x86_64.rpm

Ran the make command again and ... viola 

[ 11%] Built target cpuid
Linking CXX executable xmrig
[100%] Built target xmrig



# Action History
- Created by: StealthBadger747 | 2017-10-24T18:37:51+00:00
- Closed at: 2018-03-14T23:21:48+00:00
