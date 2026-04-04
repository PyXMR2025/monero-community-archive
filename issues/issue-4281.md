---
title: unable to build with 16.04
source_url: https://github.com/monero-project/monero/issues/4281
author: calidion
assignees: []
labels: []
created_at: '2018-08-19T09:15:12+00:00'
updated_at: '2018-08-19T10:53:54+00:00'
type: issue
status: closed
closed_at: '2018-08-19T10:53:54+00:00'
---

# Original Description
/usr/bin/ld: /usr/lib/gcc/x86_64-linux-gnu/5/../../../../lib/libgtest.a(gtest-all.cc.o): relocation R_X86_64_32 against `.rodata' can not be used when making a shared object; recompile with -fPIC
/usr/lib/gcc/x86_64-linux-gnu/5/../../../../lib/libgtest.a: 无法添加符号: 错误的值
collect2: error: ld returned 1 exit status
tests/unit_tests/CMakeFiles/unit_tests.dir/build.make:1206: recipe for target 'tests/unit_tests/unit_tests' failed
make[3]: *** [tests/unit_tests/unit_tests] Error 1
make[3]: Leaving directory '/home/eric/monero/build/release'
CMakeFiles/Makefile2:4425: recipe for target 'tests/unit_tests/CMakeFiles/unit_tests.dir/all' failed
make[2]: *** [tests/unit_tests/CMakeFiles/unit_tests.dir/all] Error 2
make[2]: Leaving directory '/home/eric/monero/build/release'
Makefile:138: recipe for target 'all' failed
make[1]: *** [all] Error 2
make[1]: Leaving directory '/home/eric/monero/build/release'
Makefile:64: recipe for target 'release-all' failed
make: *** [release-all] Error 2


# Discussion History
## iDunk5400 | 2018-08-19T09:25:33+00:00
Seeing that you have tried to search for the answer, the way to compile tests is
```
sudo apt remove libgtest-dev
make clean
make
```


# Action History
- Created by: calidion | 2018-08-19T09:15:12+00:00
- Closed at: 2018-08-19T10:53:54+00:00
