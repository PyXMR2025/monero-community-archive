---
title: 'macOS: release builds fine, release-static does not'
source_url: https://github.com/monero-project/monero/issues/935
author: RaskaRuby
assignees: []
labels: []
created_at: '2016-07-26T19:02:34+00:00'
updated_at: '2016-07-27T19:44:45+00:00'
type: issue
status: closed
closed_at: '2016-07-27T19:44:44+00:00'
---

# Original Description
Using OS X 11.6 (El Capitan) and Brew with these packages:
boost cmake libevent miniupnpc pkgconfig

`[ 86%] Building CXX object src/miner/CMakeFiles/simpleminer.dir/simpleminer.cpp.o
[ 87%] Linking CXX executable ../../bin/simpleminer
ld: unknown option: --wrap=__cxa_throw
clang: error: linker command failed with exit code 1 (use -v to see invocation)
make[3]: *** [bin/simpleminer] Error 1
make[2]: *** [src/miner/CMakeFiles/simpleminer.dir/all] Error 2
make[1]: *** [all] Error 2
make: *** [release-static-64] Error 2
`


# Discussion History
## radfish | 2016-07-27T06:44:10+00:00
Try #937 please


## RaskaRuby | 2016-07-27T19:44:44+00:00
Fixed by [#937](https://github.com/monero-project/bitmonero/pull/937), master release-static built fine for me on macOS.
Thanks radfish!


# Action History
- Created by: RaskaRuby | 2016-07-26T19:02:34+00:00
- Closed at: 2016-07-27T19:44:44+00:00
