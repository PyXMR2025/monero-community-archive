---
title: unit_tests test fails on i686 and x86_64 but not on ARM
source_url: https://github.com/monero-project/monero/issues/975
author: radfish
assignees: []
labels: []
created_at: '2016-08-21T07:30:07+00:00'
updated_at: '2016-08-21T15:55:45+00:00'
type: issue
status: closed
closed_at: '2016-08-21T15:55:45+00:00'
---

# Original Description
Commit: 63ba244
gcc (GCC) 6.1.1 20160802
Arch Linux i686

```
Running tests...
Test project /home/redfish/dev/bitmonero-git-PKGBUILD/src/bitmonero/build
      Start  1: hash-target
 1/11 Test  #1: hash-target ......................   Passed    0.29 sec
      Start  2: crypto
 2/11 Test  #2: crypto ...........................   Passed   66.71 sec
      Start  3: unit_tests
 3/11 Test  #3: unit_tests .......................***Failed    1.57 sec
      Start  4: difficulty
 4/11 Test  #4: difficulty .......................   Passed    0.03 sec
      Start  5: hash-fast
 5/11 Test  #5: hash-fast ........................   Passed    0.04 sec
      Start  6: hash-slow
 6/11 Test  #6: hash-slow ........................   Passed    0.71 sec
      Start  7: hash-tree
 7/11 Test  #7: hash-tree ........................   Passed    0.00 sec
      Start  8: hash-extra-blake
 8/11 Test  #8: hash-extra-blake .................   Passed    0.01 sec
      Start  9: hash-extra-groestl
 9/11 Test  #9: hash-extra-groestl ...............   Passed    0.02 sec
      Start 10: hash-extra-jh
10/11 Test #10: hash-extra-jh ....................   Passed    0.04 sec
      Start 11: hash-extra-skein
11/11 Test #11: hash-extra-skein .................   Passed    0.01 sec

91% tests passed, 1 tests failed out of 11

Total Test time (real) =  69.46 sec

The following tests FAILED:
          3 - unit_tests (Failed)
Errors while running CTest
```


# Discussion History
## moneromooo-monero | 2016-08-21T09:53:27+00:00
Wich tests fail ?
Running the unit_tests binary alone will print on stdout or stderr.
The output might also be in some log file in build.


## radfish | 2016-08-21T15:55:45+00:00
lol, it was the DNS resolver tests. My ISP's DNS server returned a spam landing page for non-existant domains. Changed to not use ISP DNS server and the tests pass.


# Action History
- Created by: radfish | 2016-08-21T07:30:07+00:00
- Closed at: 2016-08-21T15:55:45+00:00
