---
title: relocation R_X86_64_32 against `.rodata' can not be used when making a shared
  object; recompile with -fPIC
source_url: https://github.com/monero-project/monero/issues/4019
author: kamuluprashanth
assignees: []
labels: []
created_at: '2018-06-18T11:55:23+00:00'
updated_at: '2019-04-21T19:30:44+00:00'
type: issue
status: closed
closed_at: '2018-06-19T09:41:08+00:00'
---

# Original Description
/usr/bin/ld: /usr/lib/gcc/x86_64-linux-gnu/5/../../../../lib/libgtest.a(gtest-all.cc.o): relocation R_X86_64_32 against `.rodata' can not be used when making a shared object; recompile with -fPIC
/usr/lib/gcc/x86_64-linux-gnu/5/../../../../lib/libgtest.a: error adding symbols: Bad value
collect2: error: ld returned 1 exit status
tests/unit_tests/CMakeFiles/unit_tests.dir/build.make:1206: recipe for target 'tests/unit_tests/unit_tests' failed
make[3]: *** [tests/unit_tests/unit_tests] Error 1
make[3]: Leaving directory '/home/ubuntu16/Desktop/masari/build/release'
CMakeFiles/Makefile2:4348: recipe for target 'tests/unit_tests/CMakeFiles/unit_tests.dir/all' failed
make[2]: *** [tests/unit_tests/CMakeFiles/unit_tests.dir/all] Error 2
make[2]: Leaving directory '/home/ubuntu16/Desktop/masari/build/release'
Makefile:138: recipe for target 'all' failed
make[1]: *** [all] Error 2
make[1]: Leaving directory '/home/ubuntu16/Desktop/masari/build/release'
Makefile:64: recipe for target 'release-all' failed
make: *** [release-all] Error 2

please give me solution

# Discussion History
## moneromooo-monero | 2018-06-18T12:23:55+00:00
It tells you the solution:

/usr/bin/ld: /usr/lib/gcc/x86_64-linux-gnu/5/../../../../lib/libgtest.a(gtest-all.cc.o): relocation R_X86_64_32 against `.rodata' can not be used when making a shared object; recompile with -fPIC

You can also  uninstall libgtest from your system if nothing else uses it, monero has its own copy, which it builds with -fPIC.




## dEBRUYNE-1 | 2018-06-19T09:34:12+00:00
+resolved

## blackrangersoftware | 2019-04-21T19:30:44+00:00
Why then, isn't the code set to always look for the built-in version of gtest with the suggested switch  -fPIC??

I have another coin daemon that runs on the same host for business reasons that requires the version installed on the system.

I built and successfully tested this  version of Monero on a fresh build of Ubuntu without a single error, and now this error crashes a build at 95% time after time on my production build.

/usr/bin/ld: /usr/lib/gcc/x86_64-linux-gnu/5/../../../../lib/libgtest.a(gtest-all.cc.o): relocation R_X86_64_32 against `.rodata' can not be used when making a shared object; recompile with -fPIC

You can also uninstall libgtest from your system if nothing else uses it, monero has its own copy, which it builds with -fPIC

# Action History
- Created by: kamuluprashanth | 2018-06-18T11:55:23+00:00
- Closed at: 2018-06-19T09:41:08+00:00
