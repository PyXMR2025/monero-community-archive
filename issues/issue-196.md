---
title: Ubuntu 14.04 LTS
source_url: https://github.com/xmrig/xmrig/issues/196
author: chughta1
assignees: []
labels:
- bug
created_at: '2017-11-12T18:12:05+00:00'
updated_at: '2017-11-27T00:20:00+00:00'
type: issue
status: closed
closed_at: '2017-11-27T00:20:00+00:00'
---

# Original Description
Hi

The build instructions don't seem to work for 14.04 as the essential packages: 
`sudo apt-get install git build-essential cmake libuv1-dev libmicrohttpd-dev`

Are not available for 14.04 or LTS versions. Is there any alternative build instructions for lower versions of ubuntu?

# Discussion History
## luca-nardelli | 2017-11-13T15:35:06+00:00
I've managed to make it work by compiling libuv from sources https://github.com/libuv/libuv

## Algeroth123 | 2017-11-16T19:19:29+00:00
got the same problem, 
libuv is not a problem

xmrig/src/Summary.cpp: In function ‘void print_versions()’:
xmrig/src/Summary.cpp:45:85: error: ‘snprintf’ was not declared in this scope
     snprintf(buf, 16, " gcc/%d.%d.%d", __GNUC__, __GNUC_MINOR__, __GNUC_PATCHLEVEL__);
                                                                                     ^
xmrig/src/Summary.cpp: In function ‘void print_threads()’:
xmrig/src/Summary.cpp:95:76: error: ‘snprintf’ was not declared in this scope
         snprintf(buf, 32, ", affinity=0x%" PRIX64, Options::i()->affinity());
                                                                            ^
make[2]: *** [CMakeFiles/xmrig.dir/src/Summary.cpp.o] Error 1

gcc5, 6 ,7 the same error

## xmrig | 2017-11-17T10:03:10+00:00
Issue with `snprintf` should be fixed in https://github.com/xmrig/xmrig/commit/4b00eb4a9fbb68392a316d8ac6c36a0931567d74
Thank you.

# Action History
- Created by: chughta1 | 2017-11-12T18:12:05+00:00
- Closed at: 2017-11-27T00:20:00+00:00
