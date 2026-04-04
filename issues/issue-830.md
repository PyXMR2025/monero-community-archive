---
title: 'pine64 compile error, using "Ubuntu Linux Image base on Longsleep 20160421
  image, Pine64" and standard '
source_url: https://github.com/monero-project/monero/issues/830
author: Gingeropolous
assignees: []
labels: []
created_at: '2016-05-01T14:54:13+00:00'
updated_at: '2016-05-02T12:03:49+00:00'
type: issue
status: closed
closed_at: '2016-05-01T15:23:23+00:00'
---

# Original Description
Using standard dependency packages from ubuntu (as described in moneroexamples documentation).

Note - pine is both 64 bit and has aes (according to the internets).

using v0.9.4

using make release-arm7

[ 17%] Building CXX object contrib/otshell_utils/CMakeFiles/otshell_utils.dir/ccolor.cpp.o
c++: error: unrecognized command line option '-mfloat-abi=hard'

using make

[  9%] Building CXX object contrib/otshell_utils/CMakeFiles/otshell_utils.dir/ccolor.cpp.o
c++: error: unrecognized command line option '-maes'

Get same results with head. 


# Discussion History
## Gingeropolous | 2016-05-01T15:23:23+00:00
hyc> edit the CMakeCache.txt
<hyc> and set NO_AES to ON
<hyc> should be build/release/CMakeCache.txt
<hyc> and then in build/release do a "make rebuild_cache"

then go back and to make release .... made it to 

"[ 60%] Building CXX object src/mnemonics/CMakeFiles/mnemonics.dir/electrum-words.cpp.o"

and still going strong when I closed. 


## Gingeropolous | 2016-05-02T01:22:44+00:00
Can confirm the binaries compiled (even tests!) and I am currently syncing on the pine64


## osensei | 2016-05-02T12:03:49+00:00
Cool! 

So.... how many hashes/sec??? :)

I'm tempted to pre-order one.


# Action History
- Created by: Gingeropolous | 2016-05-01T14:54:13+00:00
- Closed at: 2016-05-01T15:23:23+00:00
