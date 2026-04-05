---
title: 'libssl.so.10: cannot open shared object file: No such file or directory'
source_url: https://github.com/xmrig/xmrig/issues/795
author: welj
assignees: []
labels:
- question
created_at: '2018-10-13T08:16:53+00:00'
updated_at: '2019-03-17T16:32:37+00:00'
type: issue
status: closed
closed_at: '2019-03-17T16:32:37+00:00'
---

# Original Description
After update to latest xmrig i nave an error:

`xmrig: error while loading shared libraries: libssl.so.10: cannot open shared object file: No such file or directory`

`openssl version
OpenSSL 1.1.0f  25 May 2017
`
Ubuntu 16.04

# Discussion History
## xmrig | 2018-10-13T08:28:12+00:00
Please provide all possible information, you compile miner from source (how?) or use prebuilt binary.
Thank you.

## welj | 2018-10-13T08:32:31+00:00
Like this:
git clone https://github.com/xmrig/xmrig.git
cd xmrig
mkdir build
cd build
cmake .. -DCMAKE_BUILD_TYPE=Release -DUV_LIBRARY=/usr/lib64/libuv.a -DWITH_HTTPD=OFF -DWITH_AEON=OFF
make

If i make like:

cmake .. -DCMAKE_BUILD_TYPE=Release -DUV_LIBRARY=/usr/lib64/libuv.a -DWITH_HTTPD=OFF -DWITH_AEON=OFF -DWITH_TLS=OFF  -- its okay 



## xmrig | 2018-10-13T08:53:25+00:00
Ubuntu 16.04 shipped with OpenSSL 1.0.2g and miner compiled and works fine with this version. So this issue related how OpenSSL 1.1.0f installed on your system and what version found cmake.
Thank you.

## AndreySerg | 2018-10-13T09:22:37+00:00
Same issue here

## welj | 2018-10-13T09:28:13+00:00
all time im compiled  miner at Centos 7 with
openssl version
OpenSSL 1.0.2k-fips  26 Jan 2017

and send miner on my server Ubunte 16.04 - and fine works, now not. Only with -DWITH_TLS=OFF works.


## xmrig | 2018-10-13T09:32:58+00:00
OpenSSL support added in v2.8, if you no need SSL/TLS support, you can compile with `-DWITH_TLS=OFF` it's ok. If need SSL/TLS support AND binary compatibility with CentOS and Ubuntu you should build own static OpenSSL.

## DeadManWalkingTO | 2019-03-17T14:26:56+00:00
I think this issue can be closed.
Thank you!

# Action History
- Created by: welj | 2018-10-13T08:16:53+00:00
- Closed at: 2019-03-17T16:32:37+00:00
