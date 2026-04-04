---
title: Monero is not building
source_url: https://github.com/monero-project/monero/issues/3596
author: skinderis
assignees: []
labels: []
created_at: '2018-04-10T11:23:34+00:00'
updated_at: '2018-04-10T15:41:00+00:00'
type: issue
status: closed
closed_at: '2018-04-10T15:36:22+00:00'
---

# Original Description
Try to build monero, but getting this error:
```
[ 95%] Linking CXX executable unit_tests
/usr/bin/ld: /usr/lib/gcc/x86_64-linux-gnu/5/../../../../lib/libgtest.a(gtest-all.cc.o): relocation R_X86_64_32 against `.rodata' can not be used when making a shared object; recompile with -fPIC
/usr/lib/gcc/x86_64-linux-gnu/5/../../../../lib/libgtest.a: error adding symbols: Bad value
collect2: error: ld returned 1 exit status
tests/unit_tests/CMakeFiles/unit_tests.dir/build.make:1205: recipe for target 'tests/unit_tests/unit_tests' failed
make[3]: *** [tests/unit_tests/unit_tests] Error 1
make[3]: Leaving directory '/home/igoris/Desktop/monero/build/release'
CMakeFiles/Makefile2:4348: recipe for target 'tests/unit_tests/CMakeFiles/unit_tests.dir/all' failed
make[2]: *** [tests/unit_tests/CMakeFiles/unit_tests.dir/all] Error 2
make[2]: Leaving directory '/home/igoris/Desktop/monero/build/release'
Makefile:138: recipe for target 'all' failed
make[1]: *** [all] Error 2
make[1]: Leaving directory '/home/igoris/Desktop/monero/build/release'
Makefile:64: recipe for target 'release-all' failed
make: *** [release-all] Error 2

```

# Discussion History
## moneromooo-monero | 2018-04-10T11:38:53+00:00
/usr/bin/ld: /usr/lib/gcc/x86_64-linux-gnu/5/../../../../lib/libgtest.a(gtest-all.cc.o): relocation R_X86_64_32 against `.rodata' can not be used when making a shared object; recompile with -fPIC

You can also uninstall libgtest from your machine, monero has an internal copy which it can use.

## skinderis | 2018-04-10T15:24:36+00:00
@monero-project , thanks solved

## dEBRUYNE-1 | 2018-04-10T15:36:19+00:00
+resolved

# Action History
- Created by: skinderis | 2018-04-10T11:23:34+00:00
- Closed at: 2018-04-10T15:36:22+00:00
