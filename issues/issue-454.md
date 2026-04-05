---
title: '(LINUX CPU mining)  /data/xmrig/src/api/Httpd.cpp: In member function ‘bool
  Httpd::start()’: /data/xmrig/src/api/Httpd.cpp:49:34: error: ‘MHD_FEATURE_EPOLL’
  was not declared in this scope'
source_url: https://github.com/xmrig/xmrig/issues/454
author: asdj07
assignees:
- xmrig
labels:
- bug
created_at: '2018-03-16T01:23:07+00:00'
updated_at: '2018-03-18T01:34:34+00:00'
type: issue
status: closed
closed_at: '2018-03-18T01:33:57+00:00'
---

# Original Description
No description

# Discussion History
## xmrig | 2018-03-16T01:34:40+00:00
Too old libmicrohttpd version, what Linux distro you use?
Thank you.

## asdj07 | 2018-03-16T01:43:13+00:00
/usr/lib64/libmicrohttpd.so.10.22.0
It's a   centos7  virtual machine，I need to update the libmicrohttpd ?

## xmrig | 2018-03-16T01:48:28+00:00
You have 3 options:

1. Update libmicrohttpd
2. Build without libmicrohttpd `-DWITH_HTTPD=OFF` for `cmake`
3. Make some quick fix to change this part of code, I will add version checks later.

## asdj07 | 2018-03-16T01:50:06+00:00
OK, Thank you 

## gadingpideksa | 2018-03-17T06:51:21+00:00
![er](https://user-images.githubusercontent.com/37467346/37552535-f7fdda32-29e9-11e8-9050-201cd163d0b6.PNG)
 how about this?

## xmrig | 2018-03-18T01:33:57+00:00
Fixed. Epoll, IPv6 and feature checking was added in libmicrohttpd 0.9.35, CentOS7 shipped with 0.9.33.
Thank you.

# Action History
- Created by: asdj07 | 2018-03-16T01:23:07+00:00
- Closed at: 2018-03-18T01:33:57+00:00
