---
title: Cannot be compiled on Centos 6
source_url: https://github.com/xmrig/xmrig/issues/387
author: tkalfaoglu
assignees: []
labels: []
created_at: '2018-02-05T08:16:13+00:00'
updated_at: '2018-02-05T08:42:49+00:00'
type: issue
status: closed
closed_at: '2018-02-05T08:42:49+00:00'
---

# Original Description
Unfortunately xmrig cannot be compiled under Centos 6.

There are multiple issues.. 
1. -Ofast,  -ftree-loop-if-convert-stores  , -std=c++11  are not accepted. 
2. Once these are edited out from the Makefiles, then it complains about
  "error: ‘nullptr’ was not declared in this scope"
  which apparently cannot be remedied by adding -std=c++0x   , or I have not been adding it to the correct place.. 

PS: I also had to update  libuv, and using the newer copy.

 cmake -DWITH_HTTPD=OFF -DUV_LIBRARY=/usr/local/lib/libuv.so .
-- Found UV: /usr/local/lib/libuv.so  
-- Configuring done
-- Generating done
-- Build files have been written to: /root/xmrig/build
[root@pluto build]# make
[  2%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/cpuid_main.c.o
cc1: error: invalid option argument ‘-Ofast’
cc1: error: unrecognized command line option "-ftree-loop-if-convert-stores"
make[2]: *** [src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/cpuid_main.c.o] Error 1
make[1]: *** [src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/all] Error 2
make: *** [all] Error 2
$ gcc --version
gcc (GCC) 4.7.2 20121015 (Red Hat 4.7.2-5)


# Discussion History
## tkalfaoglu | 2018-02-05T08:40:37+00:00
Followup.. I think this will solve the GCC issues in Centos 6:
https://www.softwarecollections.org/en/scls/rhscl/devtoolset-7/


## tkalfaoglu | 2018-02-05T08:42:49+00:00
O yeah.. All done and happy.
[ 88%] Building C object CMakeFiles/xmrig.dir/src/crypto/c_groestl.c.o
[ 90%] Building C object CMakeFiles/xmrig.dir/src/crypto/c_blake256.c.o
[ 93%] Building C object CMakeFiles/xmrig.dir/src/crypto/c_jh.c.o
[ 95%] Building C object CMakeFiles/xmrig.dir/src/crypto/c_skein.c.o
[ 97%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/CryptoNight.cpp.o
[100%] Building CXX object CMakeFiles/xmrig.dir/src/log/SysLog.cpp.o
Linking CXX executable xmrig
[100%] Built target xmrig


# Action History
- Created by: tkalfaoglu | 2018-02-05T08:16:13+00:00
- Closed at: 2018-02-05T08:42:49+00:00
