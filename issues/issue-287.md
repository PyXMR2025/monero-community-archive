---
title: compile for vmware 6?
source_url: https://github.com/xmrig/xmrig/issues/287
author: nstojanoski
assignees: []
labels: []
created_at: '2017-12-23T10:38:47+00:00'
updated_at: '2018-11-05T12:32:52+00:00'
type: issue
status: closed
closed_at: '2018-11-05T12:32:52+00:00'
---

# Original Description
Hi,

I have quite a few vmware boxes that are idling 99,9999% of the time

Is there a way to compile xmrig to work on the vmware host and not deploy vm's on each of them?

I've tried with some static build options but i can't get it to work.

Regards

# Discussion History
## ColtB45 | 2018-01-07T04:22:49+00:00
I was able to get a working static build with the following from ubuntu. However, it seg faults on ESXi.
```
sudo add-apt-repository ppa:jonathonf/gcc-7.2
sudo apt-get update
sudo apt-get install git build-essential cmake libuv1-dev libmicrohttpd-dev gcc-7 g++-7
cd ~
git clone https://github.com/xmrig/xmrig.git
mkdir xmrig/build
cd build
sed -i 's/include_directories(${UV_INCLUDE_DIR})/include_directories(${UV_INCLUDE_DIR})\nset(CMAKE_EXE_LINKER_FLAGS " -static")/g' ../CMakeLists.txt
sed -i 's/target_link_libraries(xmrig ${UV_LIBRARIES} ${MHD_LIBRARY} ${EXTRA_LIBS} ${CPUID_LIB})/target_link_libraries(xmrig ${UV_LIBRARIES} ${MHD_LIBRARY} ${EXTRA_LIBS} ${CPUID_LIB} -static-libgcc -static-libstdc++ -static)/g' ../CMakeLists.txt
cmake .. -DCMAKE_C_COMPILER=gcc-7 -DCMAKE_CXX_COMPILER=g++-7 -DWITH_HTTPD=OFF
make
```

[Here](https://www.virtuallyghetto.com/2011/02/how-to-compile-statically-linked-rsync.html) and [here](http://www.kioptrix.com/blog/a-few-nice-esxi-5-5-binaries/) they talk about how to build static executables for ESXi 5.5. I assume it would work for 6/6.5 but I haven't tried yet.

I hope it's of some help to you. Please let us know if it works for you.
  

## zelasge | 2018-05-07T17:23:35+00:00
same issue for me
I looks like a thief and steal the server's CPU and don't want anyone knows 

# Action History
- Created by: nstojanoski | 2017-12-23T10:38:47+00:00
- Closed at: 2018-11-05T12:32:52+00:00
