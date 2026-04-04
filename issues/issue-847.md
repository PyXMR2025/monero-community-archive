---
title: 'bitmonerod with GCC 6.1.1 not syncing on armv7h: block does not have enough
  proof of work .... unexpected difficulty'
source_url: https://github.com/monero-project/monero/issues/847
author: radfish
assignees: []
labels:
- arm
created_at: '2016-05-19T22:17:29+00:00'
updated_at: '2017-09-20T21:36:25+00:00'
type: issue
status: closed
closed_at: '2017-09-20T21:36:25+00:00'
---

# Original Description
v0.9.4.0-a837c9c built natively with GCC v6

Synced on an x86_64 VPS (compiled from master) up to block 1050787, transferred lmdb to armv7h, launched daemon. It is stuck at block 1050788, with this error repeating:

```
Attempting to get output pubkey by global index, but key does not exist
EXCEPTION: Attempting to get output pubkey by global index, but key does not exist

[P2P9]Block with id: <74724176de696cfa20ccbaa5f7c203084e1ff963d19f6cf7f2a32d277dff5cd2>
does not have enough proof of work: <34f45fad9dfa1e314088b5c58342aa59be05e5972bd9c2a0cd200c8ecd2d7d0b>
unexpected difficulty: 1656389584
```


# Discussion History
## moneroexamples | 2016-05-21T07:16:40+00:00
Newest changes to monero code require resyncing blockchain, at least for me. Your issue  might be because of that.


## radfish | 2016-05-21T18:15:52+00:00
@moneroexamples I synced on x86_64 VPS from scratch.


## radfish | 2016-05-21T18:17:50+00:00
@hyc suggested that crypto code on ARM might be broken (due to latest GCC 6 or some other reason). The tests fail on my armv7h board (and another ARM server), which corroborates that hypothesis:

```
Running tests...
Test project bitmonero-git/src/bitmonero
      Start  1: hash-target
 1/13 Test  #1: hash-target ......................   Passed    0.38 sec
      Start  2: coretests
 2/13 Test  #2: coretests ........................***Failed  25731.55 sec
      Start  3: crypto
 3/13 Test  #3: crypto ...........................   Passed   97.99 sec
      Start  4: unit_tests
 4/13 Test  #4: unit_tests .......................***Failed    2.78 sec
      Start  5: difficulty
 5/13 Test  #5: difficulty .......................   Passed    0.05 sec
      Start  6: hash-fast
 6/13 Test  #6: hash-fast ........................   Passed    0.08 sec
      Start  7: hash-slow
 7/13 Test  #7: hash-slow ........................***Failed    1.31 sec
      Start  8: hash-tree
 8/13 Test  #8: hash-tree ........................   Passed    0.01 sec
      Start  9: hash-extra-blake
 9/13 Test  #9: hash-extra-blake .................   Passed    0.03 sec
      Start 10: hash-extra-groestl
10/13 Test #10: hash-extra-groestl ...............   Passed    0.04 sec
      Start 11: hash-extra-jh
11/13 Test #11: hash-extra-jh ....................   Passed    0.11 sec
      Start 12: hash-extra-skein
12/13 Test #12: hash-extra-skein .................   Passed    0.03 sec
      Start 13: libwallet_api_tests
13/13 Test #13: libwallet_api_tests ..............   Passed   21.08 sec

77% tests passed, 3 tests failed out of 13

Total Test time (real) = 25855.53 sec

The following tests FAILED:
          2 - coretests (Failed)
          4 - unit_tests (Failed)
          7 - hash-slow (Failed)
Errors while running CTest
Makefile:104: recipe for target 'test' failed
make: *** [test] Error 8
```


## iamsmooth | 2016-05-24T07:48:51+00:00
comment out the ARM asm code for mul128 in slow-hash.c and try again. I have seen it fail on other gcc versions as well.


## radfish | 2016-05-25T20:03:58+00:00
@iamsmooth Thanks, that worked. Documented the exact patch in #850.
Some tests still fail, but the above-described problem is gone, node does seem to be syncing:

```
Running tests...
Test project /mnt/flext/dev/bitmonero-git/src/bitmonero/build
      Start  1: hash-target
 1/12 Test  #1: hash-target ......................   Passed    1.13 sec
      Start  2: crypto
 2/12 Test  #2: crypto ...........................   Passed  353.81 sec
      Start  3: unit_tests
 3/12 Test  #3: unit_tests .......................***Failed    2.23 sec
      Start  4: difficulty
 4/12 Test  #4: difficulty .......................   Passed    0.36 sec
      Start  5: hash-fast
 5/12 Test  #5: hash-fast ........................   Passed    0.16 sec
      Start  6: hash-slow
 6/12 Test  #6: hash-slow ........................   Passed    3.30 sec
      Start  7: hash-tree
 7/12 Test  #7: hash-tree ........................   Passed    0.02 sec
      Start  8: hash-extra-blake
 8/12 Test  #8: hash-extra-blake .................   Passed    0.04 sec
      Start  9: hash-extra-groestl
 9/12 Test  #9: hash-extra-groestl ...............   Passed    0.13 sec
      Start 10: hash-extra-jh
10/12 Test #10: hash-extra-jh ....................   Passed    0.20 sec
      Start 11: hash-extra-skein
11/12 Test #11: hash-extra-skein .................   Passed    0.04 sec
      Start 12: libwallet_api_tests
12/12 Test #12: libwallet_api_tests ..............   Passed   43.54 sec

92% tests passed, 1 tests failed out of 12

Total Test time (real) = 405.02 sec

The following tests FAILED:
          3 - unit_tests (Failed)
Errors while running CTest

```


## radfish | 2016-05-28T03:34:56+00:00
For the sake of completeness:

I applied the patch. Then I synced on x86_64 from scratch (yes, again), cleanly exited bitmonerod, trasferred the bitmonerod folder to armv7h box, and launched bitmonerod. Shortly after startup, the log does contain the error `EXCEPTION: Attempting to get output pubkey by global index, but key does not exist`, but it does NOT contain the error about `block does not have enough proof of work`.

The node appears to be working fine: `status` shows the top block, and it gets new blocks from the network:

```
$ bitmonerod status
Height: 1056797/1056797 (100.0%) on mainnet, not mining, net hash 12.47 MH/s, v2, up to date, 6+4 connections
$ bitmonerod status
Height: 1056798/1056799 (100.0%) on mainnet, not mining, net hash 12.46 MH/s, v2, up to date, 7+4 connections
$ bitmonerod status
Height: 1056799/1056799 (100.0%) on mainnet, not mining, net hash 12.44 MH/s, v2, up to date, 7+5 connections
$ bitmonerod status
Height: 1056800/1056802 (100.0%) on mainnet, not mining, net hash 12.41 MH/s, v2, up to date, 3+13 connections
```


## radfish | 2016-06-01T15:41:43+00:00
So far it seems that the `EXCEPTION: ...` is not fatal (although not nice), because the node goes on to sync fine and work fine.  But the `block does not have enough proof of work` error is fatal, the node keeps fetching the same batch of blocks and keeps rejecting it with this error in an endless loop, while saturating disk I/O.

Likely the same root cause is at the bottom of the failure to `blockchain_import` ([verbose log](https://github.com/monero-project/bitmonero/files/293804/bitmonero.imported.verified.gcc6.txt)):

```
2016-Jun-01 02:24:49.438140 Failed to add block to blockchain, verification failed, height = 4
```

So far we (@hyc) found that from the same commit we can build a broken binary (with both the nonfatal and the fatal error) and a working binary (with the nonfatal error only). The prime suspect difference seems to be GCCv6 vs GCC 4.8/4.9. And, this problem happens with #850 applied.


## radfish | 2016-06-23T20:39:57+00:00
Tested with `-fno-strict-aliasing`: all tests pass (didn't try coretests, cause it's long), import proceeds past block #4 (see above), and syncing from network seems to proceed ok so far.

Will submit a PR with `-fno-strict-aliasing` as a temporary workaround, until aliasing is fixed in the code (leaving this ticket open for that).


## hyc | 2017-06-14T18:29:42+00:00
This was finally fixed as issue #1991 in PR #2078

## moneromooo-monero | 2017-09-20T21:17:25+00:00
+resolved

# Action History
- Created by: radfish | 2016-05-19T22:17:29+00:00
- Closed at: 2017-09-20T21:36:25+00:00
