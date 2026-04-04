---
title: make release error on macOS ElCap 10.11.6 in wallet2.cpp, "no member named
  'default_random_engine'"
source_url: https://github.com/monero-project/monero/issues/965
author: RaskaRuby
assignees: []
labels: []
created_at: '2016-08-16T19:39:53+00:00'
updated_at: '2016-08-23T02:04:01+00:00'
type: issue
status: closed
closed_at: '2016-08-23T02:04:01+00:00'
---

# Original Description
Both 'make release' and 'make release-static' are giving this error now.
I'm using an up-to-date brew with 'boost cmake libevent miniupnpc pkgconfig'

[ 73%] Building CXX object src/wallet/CMakeFiles/wallet.dir/wallet2.cpp.o
/Users/cgrice/src/bitmonero/src/wallet/wallet2.cpp:2487:53: error: no member named 'default_random_engine' in namespace 'std'
      std::shuffle(order.begin(), order.end(), std::default_random_engine(crypto::rand<unsigned>()));


# Discussion History
## moneromooo-monero | 2016-08-16T22:20:28+00:00
Is this fixed if you add this at the end of the include list in src/wallet/wallet2.cpp, near line 57 ?

#include <random>


## RaskaRuby | 2016-08-17T00:26:47+00:00
What should be included? (I think your comment got chopped off)


## iDunk5400 | 2016-08-17T01:54:28+00:00
Yep, `#include <random>` fixes it in MSYS2 on Windows.


## RaskaRuby | 2016-08-17T04:18:45+00:00
Me too. macOS builds fine  with release and release-static after adding `#include <random>` to wallet2.cpp


## moneroexamples | 2016-08-17T04:43:45+00:00
The same on arch linux with gcc 6.1


## moneromooo-monero | 2016-08-17T07:06:44+00:00
Sorry, something parses that as HTML I guess.
Thanks for reporting.


## RaskaRuby | 2016-08-23T02:04:01+00:00
Fixed by the changes in [https://github.com/monero-project/bitmonero/pull/968](url)
Thanks for fixing!


# Action History
- Created by: RaskaRuby | 2016-08-16T19:39:53+00:00
- Closed at: 2016-08-23T02:04:01+00:00
