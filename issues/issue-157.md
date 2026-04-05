---
title: no compile in Linux
source_url: https://github.com/xmrig/xmrig/issues/157
author: ilikeafrica
assignees: []
labels:
- bug
created_at: '2017-10-17T14:58:29+00:00'
updated_at: '2019-02-07T08:23:49+00:00'
type: issue
status: closed
closed_at: '2017-11-27T00:40:34+00:00'
---

# Original Description
 **I have a problem.

I used CentOS release 5.8 (Final)
I know I'm using too old Linux.
But I want to try it.

I tried to install it with the following command.**
//---------------------
cd /home/suser && curl -sSL https://github.com/libuv/libuv/archive/v1.8.0.tar.gz | sudo tar zxfv - -C /usr/local/src

cd /usr/local/src/libuv-1.8.0 && sudo sh autogen.sh && ./configure && make -j && make -j install && rm -rf /usr/local/src/libuv-1.8.0 && cd ~/  && ldconfig

yum install -y  libuv-static libstdc++-static libmicrohttpd-devel

cd /home/suser/ && git clone https://github.com/xmrig/xmrig.git && cd xmrig 

vi CMakeLists.txt 

vi CMakeLists.txt Add
add_definitions(/D__STDC_FORMAT_MACROS)

mkdir build && cd build && cmake .. -DCMAKE_BUILD_TYPE=Release -DUV_LIBRARY=/usr/local/lib/libuv.a -DWITH_HTTPD=OFF &&  make


--------------------------------------//


However, the following error message is not installed.

//----------------------------
.
.
.

[ 70%] Building CXX object CMakeFiles/xmrig.dir/src/xmrig.cpp.o
[ 72%] Building CXX object CMakeFiles/xmrig.dir/src/App_unix.cpp.o
[ 74%] Building CXX object CMakeFiles/xmrig.dir/src/Cpu_unix.cpp.o
[ 76%] Building CXX object CMakeFiles/xmrig.dir/src/Mem_unix.cpp.o
/home/suser/xmrig/xmrig-2.4.1/src/Mem_unix.cpp: In static member function 'static bool Mem::allocate(int, int, bool, bool)':
/home/suser/xmrig/xmrig-2.4.1/src/Mem_unix.cpp:55:106: error: 'MAP_HUGETLB' was not declared in this scope
     m_memory = static_cast<uint8_t*>(mmap(0, size, PROT_READ | PROT_WRITE, MAP_PRIVATE | MAP_ANONYMOUS | MAP_HUGETLB |
                                                                                                          ^
make[2]: *** [CMakeFiles/xmrig.dir/src/Mem_unix.cpp.o] Error 1
make[1]: *** [CMakeFiles/xmrig.dir/all] Error 2
make: *** [all] Error 2
-----------------------------------//

Is there a solution? 

thank you.

# Discussion History
## rtau | 2017-10-17T23:10:51+00:00
Did you take a look on issue #52?

## ilikeafrica | 2017-10-17T23:37:16+00:00
@rtau I have already seen the article. But I did not succeed. Thank you..^^;;

## Likelym | 2017-10-29T21:19:59+00:00
![qq 20171030051501](https://user-images.githubusercontent.com/29804337/32148441-e84a81fa-bd31-11e7-8303-fdb2b302bf97.png)
In the build process encountered this error, I have tried updating the libuv version, but still get this error if i am not using libuv to build it side without this error please help me, thank  you.
os is:centos6.8
@xmrig 


## xmrig | 2017-10-29T21:50:01+00:00
@Likelym please check fix in https://github.com/xmrig/xmrig/commit/6479d6bb6f29bbace7ba0c3c22ecf0edb003030f

# Action History
- Created by: ilikeafrica | 2017-10-17T14:58:29+00:00
- Closed at: 2017-11-27T00:40:34+00:00
