---
title: About -DBUILD_STATIC=ON
source_url: https://github.com/xmrig/xmrig/issues/801
author: rocke
assignees: []
labels: []
created_at: '2018-10-15T10:44:47+00:00'
updated_at: '2018-11-05T14:28:42+00:00'
type: issue
status: closed
closed_at: '2018-11-05T14:28:42+00:00'
---

# Original Description
OS: Centos 7

I have the following error after using the -DBUILD_STATIC=ON parameter:

> cc1plus: 警告：无法识别的命令行选项“-Wno-class-memaccess” [默认启用]
> [ 94%] Building CXX object CMakeFiles/xmrig.dir/src/common/api/Httpd.cpp.o
> [ 96%] Building CXX object CMakeFiles/xmrig.dir/src/common/api/HttpRequest.cpp.o
> [ 98%] Building CXX object CMakeFiles/xmrig.dir/src/common/net/Tls.cpp.o
> [100%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/Asm.cpp.o
> Linking CXX executable xmrig
> /usr/bin/ld: 找不到 -lssl
> /usr/bin/ld: 找不到 -lcrypto
> collect2: 错误：ld 返回 1
> make[2]: *** [xmrig] 错误 1
> make[1]: *** [CMakeFiles/xmrig.dir/all] 错误 2
> make: *** [all] 错误 2
> 

# Discussion History
## srwx666 | 2018-10-16T07:12:44+00:00
You are missing static openssl library.

## ghost | 2018-11-02T18:16:51+00:00
> 
> 
> OS: Centos 7
> 
> I have the following error after using the -DBUILD_STATIC=ON parameter:
> 
> > cc1plus: 警告：无法识别的命令行选项“-Wno-class-memaccess” [默认启用]
> > [ 94%] Building CXX object CMakeFiles/xmrig.dir/src/common/api/Httpd.cpp.o
> > [ 96%] Building CXX object CMakeFiles/xmrig.dir/src/common/api/HttpRequest.cpp.o
> > [ 98%] Building CXX object CMakeFiles/xmrig.dir/src/common/net/Tls.cpp.o
> > [100%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/Asm.cpp.o
> > Linking CXX executable xmrig
> > /usr/bin/ld: 找不到 -lssl
> > /usr/bin/ld: 找不到 -lcrypto
> > collect2: 错误：ld 返回 1
> > make[2]: *** [xmrig] 错误 1
> > make[1]: *** [CMakeFiles/xmrig.dir/all] 错误 2
> > make: *** [all] 错误 2

https://github.com/lotus1313/xmrig

But without http server and SSL/TLS

# Action History
- Created by: rocke | 2018-10-15T10:44:47+00:00
- Closed at: 2018-11-05T14:28:42+00:00
