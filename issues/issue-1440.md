---
title: 'Compilation failure since #1436'
source_url: https://github.com/monero-project/monero/issues/1440
author: ghost
assignees: []
labels: []
created_at: '2016-12-13T00:49:13+00:00'
updated_at: '2016-12-13T01:11:10+00:00'
type: issue
status: closed
closed_at: '2016-12-13T01:11:10+00:00'
---

# Original Description
Ubuntu 16.04 on ARMv8, GCC 5.4.0, BOOST 1.58 

```
[ 61%] Building CXX object src/wallet/CMakeFiles/obj_wallet.dir/wallet2.cpp.o
/home/nodey/monero/src/wallet/wallet2.cpp: In member function ‘bool tools::wallet2::add_address_book_row(const cryptonote::account_public_address&, const crypto::hash&, const string&)’:
/home/nodey/monero/src/wallet/wallet2.cpp:1574:28: warning: comparison between signed and unsigned integer expressions [-Wsign-compare]
   if(m_address_book.size() == old_size+1)
                            ^
/home/nodey/monero/src/wallet/wallet2.cpp: In member function ‘bool tools::wallet2::delete_address_book_row(int)’:
/home/nodey/monero/src/wallet/wallet2.cpp:1580:28: warning: comparison between signed and unsigned integer expressions [-Wsign-compare]
   if(m_address_book.size() <= row_id)
                            ^
c++: internal compiler error: Killed (program cc1plus)
Please submit a full bug report,
with preprocessed source if appropriate.
See <file:///usr/share/doc/gcc-5/README.Bugs> for instructions.
src/wallet/CMakeFiles/obj_wallet.dir/build.make:86: recipe for target 'src/wallet/CMakeFiles/obj_wallet.dir/wallet2.cpp.o' failed
make[3]: *** [src/wallet/CMakeFiles/obj_wallet.dir/wallet2.cpp.o] Error 4
make[3]: Leaving directory '/home/nodey/monero/build/release'
CMakeFiles/Makefile2:1063: recipe for target 'src/wallet/CMakeFiles/obj_wallet.dir/all' failed
make[2]: *** [src/wallet/CMakeFiles/obj_wallet.dir/all] Error 2
make[2]: Leaving directory '/home/nodey/monero/build/release'
Makefile:138: recipe for target 'all' failed
make[1]: *** [all] Error 2
make[1]: Leaving directory '/home/nodey/monero/build/release'
Makefile:51: recipe for target 'release' failed
make: *** [release] Error 2
```

# Discussion History
## moneromooo-monero | 2016-12-13T00:58:04+00:00
The failure is unrelated to the warnings. You want more RAM (or TMPDIR to a non tmpfs directory).

## ghost | 2016-12-13T00:58:46+00:00
How can you tell this is an OOM issue? I've got 1.6GB of available ram at the start of compilation.

## ghost | 2016-12-13T01:11:09+00:00
Added `export TMPDIR=$HOME/gcctemp` to `~/.profile` 

Seems to work

# Action History
- Created by: ghost | 2016-12-13T00:49:13+00:00
- Closed at: 2016-12-13T01:11:10+00:00
