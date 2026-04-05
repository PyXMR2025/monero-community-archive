---
title: how to use xmrig 2.0 on ubuntu ?
source_url: https://github.com/xmrig/xmrig/issues/30
author: local139
assignees: []
labels: []
created_at: '2017-07-05T09:03:32+00:00'
updated_at: '2017-07-11T16:10:10+00:00'
type: issue
status: closed
closed_at: '2017-07-11T16:10:10+00:00'
---

# Original Description
hello, friend, i need your help
i use the old 0.8.2 , but today i find you update, so i have a try, but not work.
simple out, i do not know how to use the new verision (2.0) on ubuntu. 
apt-get install git build-essential cmake libcurl4-openssl-dev
git clone https://github.com/xmrig/xmrig
cd xmrig
then ??????

# Discussion History
## local139 | 2017-07-05T09:05:12+00:00
or the 2.0 verision is for windows only, it's not for linux?

## xmrig | 2017-07-05T11:14:08+00:00
There updated instructions https://github.com/xmrig/xmrig/wiki/Build only one difference libcurl4-openssl-dev no more required, instead libuv1-dev required.

Also on download page prebuild version for Ubuntu 16.04 available too.
Thank you. 

## local139 | 2017-07-05T11:39:45+00:00
thanks
1、does C++ better C ?  OR it(C++) is faster than C ?

## local139 | 2017-07-05T11:43:25+00:00
2、am i  must install gcc 7.1 ? dude
3、it is will be faster ? if i install gcc 7.1


## local139 | 2017-07-05T11:45:02+00:00
i do not want install gcc-7 g++-7 , does it will be work well ?

## xmrig | 2017-07-05T11:47:04+00:00
gcc 7.1 little bit faster, but optional, gcc 5.4 fine too.
C++ more easy for development and libuv nice lib for async io.

## local139 | 2017-07-05T11:53:34+00:00
thanks

# Action History
- Created by: local139 | 2017-07-05T09:03:32+00:00
- Closed at: 2017-07-11T16:10:10+00:00
