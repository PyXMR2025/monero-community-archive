---
title: bitmonerod release-static fails to build on macOS, stack_trace.cpp undefined
  ___real___cxa_throw
source_url: https://github.com/monero-project/monero/issues/932
author: RaskaRuby
assignees: []
labels: []
created_at: '2016-07-26T00:01:33+00:00'
updated_at: '2016-07-26T06:53:46+00:00'
type: issue
status: closed
closed_at: '2016-07-26T06:53:46+00:00'
---

# Original Description
Using OS X 11.6 (El Capitan) and Brew with these packages: 
boost cmake libevent miniupnpc pkgconfig

`[ 95%] Linking CXX executable ../../bin/bitmonerod Undefined symbols for architecture x86_64: "___real___cxa_throw", referenced from: ___wrap___cxa_throw in libcommon.a(stack_trace.cpp.o) ld: symbol(s) not found for architecture x86_64`


# Discussion History
## radfish | 2016-07-26T02:39:05+00:00
Try #934.


# Action History
- Created by: RaskaRuby | 2016-07-26T00:01:33+00:00
- Closed at: 2016-07-26T06:53:46+00:00
