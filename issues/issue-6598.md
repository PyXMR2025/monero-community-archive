---
title: monero compilation failed on ubuntu 16.04
source_url: https://github.com/monero-project/monero/issues/6598
author: goodthebest
assignees: []
labels: []
created_at: '2020-05-28T08:14:25+00:00'
updated_at: '2020-05-28T09:05:46+00:00'
type: issue
status: closed
closed_at: '2020-05-28T09:05:46+00:00'
---

# Original Description
I'm having error in building monero on Ubuntu 16.04, any idea how to fix it?

/usr/bin/ld: /usr/lib/gcc/x86_64-linux-gnu/5/../../../../lib/libgtest.a(gtest-all.cc.o): relocation R_X86_64_32 against `.rodata' can not be used when making a shared object; recompile with -fPIC
/usr/lib/gcc/x86_64-linux-gnu/5/../../../../lib/libgtest.a: error adding symbols: Bad value
collect2: error: ld returned 1 exit status
tests/unit_tests/CMakeFiles/unit_tests.dir/build.make:1870: recipe for target 'tests/unit_tests/unit_tests' failed
make[3]: *** [tests/unit_tests/unit_tests] Error 1
make[3]: Leaving directory '/root/monero/build/Linux/release-v0.15/release'
CMakeFiles/Makefile2:5599: recipe for target 'tests/unit_tests/CMakeFiles/unit_tests.dir/all' failed
make[2]: *** [tests/unit_tests/CMakeFiles/unit_tests.dir/all] Error 2
make[2]: Leaving directory '/root/monero/build/Linux/release-v0.15/release'
Makefile:138: recipe for target 'all' failed
make[1]: *** [all] Error 2
make[1]: Leaving directory '/root/monero/build/Linux/release-v0.15/release'
Makefile:102: recipe for target 'release-all' failed
make: *** [release-all] Error 2

# Discussion History
# Action History
- Created by: goodthebest | 2020-05-28T08:14:25+00:00
- Closed at: 2020-05-28T09:05:46+00:00
