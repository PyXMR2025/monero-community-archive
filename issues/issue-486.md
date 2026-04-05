---
title: getaddrinfo problem on linux static build
source_url: https://github.com/xmrig/xmrig/issues/486
author: developernew123
assignees: []
labels: []
created_at: '2018-03-30T11:07:40+00:00'
updated_at: '2018-11-05T13:03:12+00:00'
type: issue
status: closed
closed_at: '2018-11-05T13:03:12+00:00'
---

# Original Description
I got these errors while building static build on ubuntu 17.10 with gcc 7.2

`/home/user/Desktop/xmrig-cpu/libuv/lib/libuv.a(libuv_la-core.o): In function `uv__getpwuid_r':
/home/user/Desktop/libuv-v1.19.2/src/unix/core.c:1188: warning: Using 'getpwuid_r' in statically linked applications requires at runtime the shared libraries from the glibc version used for linking
/home/user/Desktop/xmrig-cpu/libuv/lib/libuv.a(libuv_la-getaddrinfo.o): In function `uv__getaddrinfo_work':
/home/user/Desktop/libuv-v1.19.2/src/unix/getaddrinfo.c:103: warning: Using 'getaddrinfo' in statically linked applications requires at runtime the shared libraries from the glibc version used for linking
`

# Discussion History
## xmrig | 2018-03-30T12:57:04+00:00
Please check this issue #238
Thank you.

## developernew123 | 2018-03-30T17:46:56+00:00
will the musl libc method work ?

## xmrig | 2018-03-30T17:49:47+00:00
I not checked it by myself, but it should work fine.
Thank you.

## kpcyrd | 2018-03-30T22:59:25+00:00
@developernew123 the musl instructions in #442 should work fine

## developernew123 | 2018-03-31T03:13:11+00:00
@kpcyrd

can you provide steps

## brandsalazar | 2018-05-30T02:54:02+00:00
@developernew123 I've built one if you still need it

# Action History
- Created by: developernew123 | 2018-03-30T11:07:40+00:00
- Closed at: 2018-11-05T13:03:12+00:00
