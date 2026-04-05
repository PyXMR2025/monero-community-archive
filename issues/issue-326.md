---
title: Wiki missing Fedora dependencies
source_url: https://github.com/xmrig/xmrig/issues/326
author: Maxim-Mazurok
assignees: []
labels: []
created_at: '2018-01-07T06:40:46+00:00'
updated_at: '2020-04-10T19:47:55+00:00'
type: issue
status: closed
closed_at: '2018-01-08T05:26:55+00:00'
---

# Original Description
On fresh install of CentOS 7, you will need to install `make` and `libuv-static`. But before installing `libuv-static` you should install `epel-release` package to enable Epel repo.
So, the instructions should look like this for CentOS:
```
sudo yum install -y epel-release
sudo yum install -y git make cmake gcc gcc-c++ libuv-static libstdc++-static libmicrohttpd-devel libuv-static
git clone https://github.com/xmrig/xmrig.git
cd xmrig
mkdir build
cd build
cmake .. -DCMAKE_BUILD_TYPE=Release -DUV_LIBRARY=/usr/lib64/libuv.a
make
```
Add to Wiki, please, it seems like I don't have access to editing Wiki.
Thanks!

# Discussion History
## xmrig | 2018-01-08T05:26:55+00:00
I added wiki page https://github.com/xmrig/xmrig/wiki/CentOS-Build
Thank you.

## zhaoyongtao | 2018-01-11T06:37:17+00:00
How to `Install` and `Use`  `xmrig` on `CentOS6` ?

## Maxim-Mazurok | 2018-01-11T10:49:50+00:00
@zhaoyongtao I think that instructions will be the same as for CentOS 7. Can you try it?

## zhaoyongtao | 2018-01-11T11:40:55+00:00
@Maxim-Mazurok   It works! Thanks!

## 330377782 | 2019-02-07T03:44:02+00:00
你好，安装完毕以后，如何配置他呢？

## Maxim-Mazurok | 2019-02-07T09:23:15+00:00
@330377782, https://github.com/xmrig/xmrig/blob/master/README.md#options

https://github.com/xmrig/xmrig/blob/master/doc/api/1/config.json

https://github.com/xmrig/xmrig/blob/master/README.md#contacts

## 330377782 | 2019-02-17T09:58:16+00:00
> @330377782, https://github.com/xmrig/xmrig/blob/master/README.md#options
> 
> https://github.com/xmrig/xmrig/blob/master/doc/api/1/config.json
> 
> https://github.com/xmrig/xmrig/blob/master/README.md#contacts

在centos里面咋启动哈？

## Maxim-Mazurok | 2019-02-17T11:41:36+00:00
> > @330377782, https://github.com/xmrig/xmrig/blob/master/README.md#options
> > https://github.com/xmrig/xmrig/blob/master/doc/api/1/config.json
> > https://github.com/xmrig/xmrig/blob/master/README.md#contacts
> 
> 在centos里面咋启动哈？

你什么意思？(What do you mean?)

## exition | 2019-12-29T14:14:47+00:00
> @330377782, https://github.com/xmrig/xmrig/blob/master/README.md#options
> 
> https://github.com/xmrig/xmrig/blob/master/doc/api/1/config.json
> 
> https://github.com/xmrig/xmrig/blob/master/README.md#contacts

centos8里面 libstdc++-static  hwloc-devel openssl-devel 这三个yum里面找不到

missing libstdc++-static  hwloc-devel openssl-devel  packages in centos8 yum repository

## zungtm | 2020-04-09T10:15:35+00:00
hi, help me
CMake Error: your ASM_MASM compiler: "ml" was not found.   Please set CMAKE_ASM_MASM_COMPILER to a valid compiler path or name.
thank you!

## nfcg | 2020-04-10T19:47:55+00:00
> hi, help me
> CMake Error: your ASM_MASM compiler: "ml" was not found. Please set CMAKE_ASM_MASM_COMPILER to a valid compiler path or name.
> thank you!

Same error here on CentOs 7.

```
sudo yum install -y cmake3
cmake3 .. 
make
```
Build finishes  no errors.


# Action History
- Created by: Maxim-Mazurok | 2018-01-07T06:40:46+00:00
- Closed at: 2018-01-08T05:26:55+00:00
