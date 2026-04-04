---
title: 2 release-tests (unit_tests, libwallet_api_tests) fail, v0.11.0
source_url: https://github.com/monero-project/monero/issues/2447
author: ernsteiswuerfel
assignees: []
labels:
- duplicate
created_at: '2017-09-14T08:44:37+00:00'
updated_at: '2017-10-03T15:12:24+00:00'
type: issue
status: closed
closed_at: '2017-10-03T15:12:24+00:00'
---

# Original Description

[CMakeOutput.zip](https://github.com/monero-project/monero/files/1302352/CMakeOutput.zip)
Building v0.11.0 just worked fine on my Gentoo box, but make release-test failed:

Running tests...
Test project /root/build/monero/build/release
      Start  1: hash-target
 1/13 Test  #1: hash-target ......................   Passed    0.13 sec
      Start  2: coretests
 2/13 Test  #2: coretests ........................   Passed  8945.50 sec
      Start  3: cncrypto
 3/13 Test  #3: cncrypto .........................   Passed   35.66 sec
      Start  4: unit_tests
 4/13 Test  #4: unit_tests .......................***Failed   38.29 sec
      Start  5: difficulty
 5/13 Test  #5: difficulty .......................   Passed    0.03 sec
      Start  6: hash-fast
 6/13 Test  #6: hash-fast ........................   Passed    0.01 sec
      Start  7: hash-slow
 7/13 Test  #7: hash-slow ........................   Passed    0.25 sec
      Start  8: hash-tree
 8/13 Test  #8: hash-tree ........................   Passed    0.01 sec
      Start  9: hash-extra-blake
 9/13 Test  #9: hash-extra-blake .................   Passed    0.01 sec
      Start 10: hash-extra-groestl
10/13 Test #10: hash-extra-groestl ...............   Passed    0.02 sec
      Start 11: hash-extra-jh
11/13 Test #11: hash-extra-jh ....................   Passed    0.02 sec
      Start 12: hash-extra-skein
12/13 Test #12: hash-extra-skein .................   Passed    0.01 sec
      Start 13: libwallet_api_tests
13/13 Test #13: libwallet_api_tests ..............***Exception: SegFault280.84 sec

85% tests passed, 2 tests failed out of 13

Total Test time (real) = 9300.89 sec

The following tests FAILED:
	  4 - unit_tests (Failed)
	 13 - libwallet_api_tests (SEGFAULT)
Errors while running CTest
make[1]: *** [Makefile:117: test] Fehler 8
make[1]: Verzeichnis „/root/build/monero/build/release“ wird verlassen
make: *** [Makefile:59: release-test] Fehler 2



# Discussion History
## moneromooo-monero | 2017-09-14T09:21:50+00:00
Failing unit tests are likely the DNS ones. If you temporarily set DNS to 8.8.8.8 (or another "good" DNS server), they should pass. If anything else fails, please report. You can run the tests manually with: ./build/release/tests/unit_tests/unit_tests, which will then show which tests are failing.

The wallet tests are known to fail, they need special setup.

## ernsteiswuerfel | 2017-09-14T10:35:04+00:00
Just ran the test manually and it's just like you said, though I do not fancy setting Google DNS. ;) Thanks for clearing up! 

## moneromooo-monero | 2017-10-03T15:11:45+00:00
Those are already known and tracked elsewhere.

+duplicate


# Action History
- Created by: ernsteiswuerfel | 2017-09-14T08:44:37+00:00
- Closed at: 2017-10-03T15:12:24+00:00
