---
title: macOS - make release link error
source_url: https://github.com/monero-project/monero/issues/1207
author: RaskaRuby
assignees: []
labels: []
created_at: '2016-10-11T16:45:03+00:00'
updated_at: '2016-10-18T16:56:10+00:00'
type: issue
status: closed
closed_at: '2016-10-18T16:56:10+00:00'
---

# Original Description
[100%] Linking CXX executable ../../bin/monerod
Undefined symbols for architecture x86_64:
  "bool cryptonote::Blockchain::get_blocks<unsigned long long, unsigned long long const, std::__1::list<cryptonote::block, std::__1::allocator<cryptonote::block> > >(unsigned long long const&, unsigned long long const&, std::__1::list<cryptonote::block, std::__1::allocator<cryptonote::block> >&) const", referenced from:
      cryptonote::core::get_coinbase_tx_sum(unsigned long long, unsigned long long) in libcryptonote_core.a(cryptonote_core.cpp.o)
ld: symbol(s) not found for architecture x86_64
clang: error: linker command failed with exit code 1 (use -v to see invocation)


# Discussion History
## schnerchi | 2016-10-13T20:39:29+00:00
PR #1204 causes this...


## monerobby | 2016-10-15T14:00:59+00:00
Broken in Mac OS X El Capitan as well.


## RaskaRuby | 2016-10-18T16:56:10+00:00
Thanks for fixing!


# Action History
- Created by: RaskaRuby | 2016-10-11T16:45:03+00:00
- Closed at: 2016-10-18T16:56:10+00:00
