---
title: master branch, Ubuntu 16.04 amd64 build, make release-test fails
source_url: https://github.com/monero-project/monero/issues/3759
author: noahc66260
assignees: []
labels:
- invalid
created_at: '2018-05-06T03:47:27+00:00'
updated_at: '2018-05-16T23:48:52+00:00'
type: issue
status: closed
closed_at: '2018-05-16T23:48:52+00:00'
---

# Original Description
When compiling master, make fails with the following message

[ 98%] Linking CXX executable unit_tests
/usr/bin/ld: /usr/lib/gcc/x86_64-linux-gnu/5/../../../../lib/libgtest.a(gtest-all.cc.o): relocation R_X86_64_32 against `.rodata' can not be used when making a shared object; recompile with -fPIC
/usr/lib/gcc/x86_64-linux-gnu/5/../../../../lib/libgtest.a: error adding symbols: Bad value
collect2: error: ld returned 1 exit status
tests/unit_tests/CMakeFiles/unit_tests.dir/build.make:1205: recipe for target 'tests/unit_tests/unit_tests' failed
make[2]: *** [tests/unit_tests/unit_tests] Error 1
CMakeFiles/Makefile2:4425: recipe for target 'tests/unit_tests/CMakeFiles/unit_tests.dir/all' failed
make[1]: *** [tests/unit_tests/CMakeFiles/unit_tests.dir/all] Error 2
Makefile:138: recipe for target 'all' failed
make: *** [all] Error 2

This is a little confusing because the build is supposed to succeed: https://build.getmonero.org/builders/monero-static-ubuntu-amd64/builds/4193/steps/test/logs/stdio

It looks like the issue is a library (libgtest). My version of the library is above the required version:
$ apt-cache policy libgtest-dev
libgtest-dev:
  Installed: 1.7.0-4ubuntu1
  Candidate: 1.7.0-4ubuntu1
  Version table:
 *** 1.7.0-4ubuntu1 500
        500 http://us.archive.ubuntu.com/ubuntu xenial/universe amd64 Packages
        100 /var/lib/dpkg/status

Recompiling the libraries is not the issue. There are *.so versions of the libraries in /usr/libs/ and I get the same error when recompiling.


# Discussion History
## iDunk5400 | 2018-05-06T09:01:41+00:00
`sudo apt remove libgtest-dev`
`rm build/release/CMakeCache.txt`
`make`
This will make the build use the provided gtest in tests/

or upgrade to Ubuntu 16.10+ (Ubuntu 18.04 LTS is out).
[https://wiki.ubuntu.com/SecurityTeam/PIE](https://wiki.ubuntu.com/SecurityTeam/PIE)


## moneromooo-monero | 2018-05-16T23:33:55+00:00
+invalid

# Action History
- Created by: noahc66260 | 2018-05-06T03:47:27+00:00
- Closed at: 2018-05-16T23:48:52+00:00
