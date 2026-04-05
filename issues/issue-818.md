---
title: Please look for libmicrohttpd.a instead of libmicrohttpd.so when STATIC option
  is used
source_url: https://github.com/xmrig/xmrig/issues/818
author: ehaupt
assignees: []
labels:
- question
created_at: '2018-10-19T08:42:33+00:00'
updated_at: '2018-10-23T09:01:11+00:00'
type: issue
status: closed
closed_at: '2018-10-23T09:01:10+00:00'
---

# Original Description
Currently when you're building the static version and want to build with microhttpd, cmake is looking for libmicrohttpd.so instead of libmicrohttpd.a.

# Discussion History
## xmrig | 2018-10-19T09:51:09+00:00
Bad idea, usually system libmicrohttpd build with GnuTLS, so static linking with GnuTLS required too. For static build should build own libmicrohttpd without additional unused dependencies.

For example next command give you libmicrohttpd.a usable for static linking.
`./configure --disable-shared --disable-doc --disable-examples --disable-curl --enable-https=no --disable-bauth --disable-dauth --disable-httpupgrade`

## ehaupt | 2018-10-23T09:01:10+00:00
Sure. Works for me.

# Action History
- Created by: ehaupt | 2018-10-19T08:42:33+00:00
- Closed at: 2018-10-23T09:01:10+00:00
