---
title: Build Xmrig with Ubuntu?
source_url: https://github.com/xmrig/xmrig/issues/1269
author: ghost
assignees: []
labels: []
created_at: '2019-11-09T14:18:02+00:00'
updated_at: '2019-12-22T19:29:35+00:00'
type: issue
status: closed
closed_at: '2019-12-22T19:29:35+00:00'
---

# Original Description
You let me ask a bit, when i recompile xmrig successfully with ubuntu. but when you bring xmrig to another ubuntu computer to run it will not work. 
That ubuntu computer has to have the xmrig build libraries to work.
Is there any way to integrate it into the executable file?
I build following this tutorial. [https://github.com/xmrig/xmrig/wiki/Ubuntu-Build](url)

sudo apt-get install git build-essential cmake libuv1-dev libssl-dev libhwloc-dev
git clone https://github.com/xmrig/xmrig.git
cd xmrig && mkdir build && cd build
cmake ..
make


# Discussion History
## y0bagu1 | 2019-11-14T19:04:25+00:00
take a look here 
http://containertutorials.com/alpine/get_started.html
and inside container give the folowing commands:
-------------------------------------------------------
apk add build-base cmake clang clang-dev git
git clone https://github.com/libuv/libuv.git /usr/local/src/libuv --depth 1 --branch v1.x
mkdir /usr/local/src/libuv/build
cd $_
cmake .. -DCMAKE_BUILD_TYPE=Release -DCMAKE_C_COMPILER=clang -DCMAKE_CXX_COMPILER=clang++ -DBUILD_TESTING=OFF
make -j$(nproc)
git clone https://github.com/xmrig/xmrig /usr/local/src/xmrig --branch dev --depth 1
cd /usr/local/src/xmrig
mkdir build
cd $_
cmake .. -DCMAKE_BUILD_TYPE=Release -DWITH_HTTPD=OFF -DWITH_TLS=OFF -DCMAKE_C_COMPILER=clang -DCMAKE_CXX_COMPILER=clang++ -DCMAKE_EXE_LINKER_FLAGS="-static" -DUV_INCLUDE_DIR=/usr/local/src/libuv/include -DUV_LIBRARY=/usr/local/src/libuv/build/libuv_a.a
make -j$(nproc)
-----------------------------------------------------------------------------------
then docker cp your file to the host and use it wherever you need, i tested it on 
 cat /etc/issue
CentOS release 6.10 (Final)
Kernel \r on an \m
as the oldest i got and it's working without any problem.

# Action History
- Created by: ghost | 2019-11-09T14:18:02+00:00
- Closed at: 2019-12-22T19:29:35+00:00
