---
title: windows rebuild
source_url: https://github.com/xmrig/xmrig/issues/4
author: PQFitz
assignees: []
labels: []
created_at: '2017-05-11T05:13:32+00:00'
updated_at: '2017-08-17T14:33:50+00:00'
type: issue
status: closed
closed_at: '2017-08-17T14:33:50+00:00'
---

# Original Description
Hi Bro,
I was in trouble when compiling

Configure options for libcurl:
$ ./configure --disable-shared --enable-optimize --enable-threaded-resolver --disable-libcurl-option --disable-ares --disable-rt --disable-ftp --disable-file --disable-ldap --disable-ldaps --disable-rtsp --disable-dict --disable-telnet --disable-tftp --disable-pop3 --disable-imap --disable-smb --disable-smtp --disable-gopher --disable-manual --disable-ipv6 --disable-sspi --disable-crypto-auth --disable-ntlm-wb --disable-tls-srp --disable-unix-sockets --without-zlib --without-winssl --without-ssl --without-libssh2 --without-nghttp2 --disable-cookies --without-ca-bundle --without-librtmp
bash: ./configure: No such file or directory


Windows compiler can be more detailed? thank you !

# Discussion History
## esfomeado | 2017-05-11T08:33:42+00:00
Have you installed MSYS2 with the required packages?
Then just download curl:
https://curl.haxx.se/download/curl-7.54.0.zip

And execute that command followed by
make
make install


## PQFitz | 2017-05-12T13:51:45+00:00
build xmrig
1120KB

why?
you upload release 400kb?
thank you


## xmrig | 2017-05-13T14:26:30+00:00
@PQFitz just run `strip xmrig.exe`. Thank you.

## Hector555 | 2017-07-24T17:35:27+00:00
Can someone please make a "total noob tutorial- how to build miner" , please ?

## androspotter | 2017-07-27T14:06:31+00:00
@Hector555 @xmrig I would love to ! I m on Windows7 , tried to build with Mingw and failed for missing libuv
I need just a quick start guide : "What to install" with a list of links please !

## JKLHJ | 2017-07-28T14:16:54+00:00
@androspotter me too. please

## JKLHJ | 2017-07-29T06:43:44+00:00
@Hector555 how to use VS2015 bulid？

# Action History
- Created by: PQFitz | 2017-05-11T05:13:32+00:00
- Closed at: 2017-08-17T14:33:50+00:00
