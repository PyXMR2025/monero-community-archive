---
title: Can't build full statical executable for linux
source_url: https://github.com/xmrig/xmrig/issues/388
author: mctracker
assignees: []
labels: []
created_at: '2018-02-05T15:16:45+00:00'
updated_at: '2018-11-05T12:49:20+00:00'
type: issue
status: closed
closed_at: '2018-11-05T12:49:20+00:00'
---

# Original Description
I'am using this command:

 `root@debian:~/monero/xmrig/build# cmake .. -DBUILD_SHARED_LIBS=OFF -DWITH_HTTPD=OFF -DCMAKE_BUILD_TYPE=Release -DUV_INCLUDE_DIR=/usr/local/src/libuv-1.8.0/ -DUV_LIBRARY=/usr/local/lib/libuv.a`

But when trying to run on other maching I've got this message:

> ./xmrig: /lib/x86_64-linux-gnu/libc.so.6: version `GLIBC_2.14' not found (required by ./xmrig)

How can I build an independent executable for Linux? Thank you.


# Discussion History
## djdomi | 2018-02-06T13:59:50+00:00
I would join your question, since i try to let it run also on others, building onetimes for all...
MAybe this is also a Point why no static binary is avaible from this Project for linux?

## Mila432 | 2018-02-06T15:47:40+00:00
use a good compiler and there you have your static bin

## 2010phenix | 2018-02-08T14:53:47+00:00
confirm what to say @Mila432 all good with static build.

## mctracker | 2018-02-09T08:31:19+00:00
> use a good compiler and there you have your static bin

Whats wrong with linux default compilers like gcc? The question is - is what proper flags for Cmake should I use to make full static binary.

## Mila432 | 2018-02-09T12:43:45+00:00
@mctracker everything from libc until ..

## mctracker | 2018-02-12T17:28:07+00:00
@Mila432 I need correct flags for CMAKE

## bs3vcenk | 2018-03-06T11:41:11+00:00
Either spin up a VM with an older version of CentOS (<7 should work) and build it there, or compile an older version of glibc and link it with xmrig when compiling.

## djdomi | 2018-03-07T05:58:06+00:00
@btx3
ok, but whoxh commands do you THEN suggest to use to build the static binary? cant you give an example for it? 

# Action History
- Created by: mctracker | 2018-02-05T15:16:45+00:00
- Closed at: 2018-11-05T12:49:20+00:00
