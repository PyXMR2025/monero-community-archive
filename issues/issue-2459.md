---
title: Two tests fail on macOS on v0.11.0.0 branch
source_url: https://github.com/monero-project/monero/issues/2459
author: xmrdog
assignees: []
labels:
- duplicate
created_at: '2017-09-17T12:36:16+00:00'
updated_at: '2017-09-18T21:12:24+00:00'
type: issue
status: closed
closed_at: '2017-09-18T21:12:24+00:00'
---

# Original Description
On my macOS 10.12.6:

    git checkout v0.11.0.0
    make release-test

I have two tests failing:

    Running tests...
    Test project /.../monero/build/release
          Start  1: hash-target
     1/13 Test  #1: hash-target ......................   Passed    0.05 sec
          Start  2: coretests
     2/13 Test  #2: coretests ........................   Passed  2099.55 sec
          Start  3: cncrypto
     3/13 Test  #3: cncrypto .........................   Passed    9.11 sec
          Start  4: unit_tests
     4/13 Test  #4: unit_tests .......................***Failed   11.18 sec
          Start  5: difficulty
     5/13 Test  #5: difficulty .......................   Passed    0.01 sec
          Start  6: hash-fast
     6/13 Test  #6: hash-fast ........................   Passed    0.01 sec
          Start  7: hash-slow
     7/13 Test  #7: hash-slow ........................   Passed    0.07 sec
          Start  8: hash-tree
     8/13 Test  #8: hash-tree ........................   Passed    0.00 sec
          Start  9: hash-extra-blake
     9/13 Test  #9: hash-extra-blake .................   Passed    0.01 sec
          Start 10: hash-extra-groestl
    10/13 Test #10: hash-extra-groestl ...............   Passed    0.01 sec
          Start 11: hash-extra-jh
    11/13 Test #11: hash-extra-jh ....................   Passed    0.01 sec
          Start 12: hash-extra-skein
    12/13 Test #12: hash-extra-skein .................   Passed    0.01 sec
          Start 13: libwallet_api_tests
    13/13 Test #13: libwallet_api_tests ..............***Failed  242.88 sec
    
    85% tests passed, 2 tests failed out of 13
    
    Total Test time (real) = 2362.97 sec
    
    The following tests FAILED:
    	  4 - unit_tests (Failed)
    	 13 - libwallet_api_tests (Failed)

**What could this be? Is this anything serious?**

# Discussion History
## moneromooo-monero | 2017-09-17T13:20:10+00:00
Nothing serious. See the comments in the dupe.

+duplicate 2447


## danrmiller | 2017-09-18T21:11:57+00:00
@moneromooo-monero The label to add or remove needs to be on a line by itself:
+duplicate
(see #2447 )

# Action History
- Created by: xmrdog | 2017-09-17T12:36:16+00:00
- Closed at: 2017-09-18T21:12:24+00:00
