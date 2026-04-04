---
title: OpenBSD/amd64 fails ringct unit tests
source_url: https://github.com/monero-project/monero/issues/5568
author: mrme0w
assignees: []
labels: []
created_at: '2019-05-23T02:30:38+00:00'
updated_at: '2019-06-20T16:25:46+00:00'
type: issue
status: closed
closed_at: '2019-06-20T16:25:46+00:00'
---

# Original Description
Anyone well-versed with ringct who can point me in the right direction to get this fixed on OpenBSD/amd64?

Preview below.. full file compressed and attached as well.
[unit_tests.log.gz](https://github.com/monero-project/monero/files/3210043/unit_tests.log.gz)

2019-05-22 21:19:14.138    0xfc8bd4facc0        ERROR   ringct  src/ringct/rctSigs.cpp:698      genRct is not suitable for 2+ rings
2019-05-22 21:19:14.798    0xfc8bd4facc0        ERROR   ringct  src/ringct/rctSigs.cpp:476      Empty pubs
2019-05-22 21:19:14.798    0xfc8bd4facc0        ERROR   ringct  src/ringct/rctSigs.cpp:754      Empty inamounts
2019-05-22 21:19:14.799    0xfc8bd4facc0        ERROR   ringct  src/ringct/rctSigs.cpp:476      Empty pubs
2019-05-22 21:19:14.799    0xfc8bd4facc0        ERROR   ringct  src/ringct/rctSigs.cpp:754      Empty inamounts
2019-05-22 21:19:14.859    0xfc8bd4facc0        ERROR   ringct  src/ringct/rctSigs.cpp:476      Empty pubs
2019-05-22 21:19:14.860    0xfc8bd4facc0        ERROR   ringct  src/ringct/rctSigs.cpp:754      Empty inamounts
2019-05-22 21:19:17.627    0xfc8bd4facc0        ERROR   ringct  src/ringct/rctSigs.cpp:698      genRct is not suitable for 2+ rings
2019-05-22 21:19:17.681    0xfc8bd4facc0        ERROR   ringct  src/ringct/rctSigs.cpp:698      genRct is not suitable for 2+ rings
2019-05-22 21:19:17.735    0xfc8bd4facc0        ERROR   ringct  src/ringct/rctSigs.cpp:698      genRct is not suitable for 2+ rings
2019-05-22 21:19:20.730    0xfc8bd4facc0        ERROR   ringct  src/ringct/rctSigs.cpp:698      genRct is not suitable for 2+ rings
2019-05-22 21:19:20.784    0xfc8bd4facc0        ERROR   ringct  src/ringct/rctSigs.cpp:698      genRct is not suitable for 2+ rings
2019-05-22 21:19:21.140    0xfc8bd4facc0        ERROR   ringct  src/ringct/rctSigs.cpp:918      Mismatched sizes of outPk and rv.p.rangeSigs
2019-05-22 21:19:21.186    0xfc8bd4facc0        ERROR   ringct  src/ringct/rctSigs.cpp:918      Mismatched sizes of outPk and rv.p.rangeSigs
2019-05-22 21:19:21.231    0xfc8bd4facc0        ERROR   ringct  src/ringct/rctSigs.cpp:918      Mismatched sizes of outPk and rv.p.rangeSigs
2019-05-22 21:19:21.276    0xfc8bd4facc0        ERROR   ringct  src/ringct/rctSigs.cpp:920      full rctSig has not one MG
2019-05-22 21:19:21.362    0xfc8bd4facc0        ERROR   ringct  src/ringct/rctSigs.cpp:281      Bad rv.ss size
2019-05-22 21:19:21.451    0xfc8bd4facc0        ERROR   ringct  src/ringct/rctSigs.cpp:281      Bad rv.ss size
2019-05-22 21:19:21.538    0xfc8bd4facc0        ERROR   ringct  src/ringct/rctSigs.cpp:281      Bad rv.ss size
2019-05-22 21:19:21.624    0xfc8bd4facc0        ERROR   ringct  src/ringct/rctSigs.cpp:283      rv.ss is not rectangular
2019-05-22 21:19:21.711    0xfc8bd4facc0        ERROR   ringct  src/ringct/rctSigs.cpp:283      rv.ss is not rectangular
2019-05-22 21:19:21.797    0xfc8bd4facc0        ERROR   ringct  src/ringct/rctSigs.cpp:283      rv.ss is not rectangular
2019-05-22 21:19:21.883    0xfc8bd4facc0        ERROR   ringct  src/ringct/rctSigs.cpp:280      Bad II size
2019-05-22 21:19:21.970    0xfc8bd4facc0        ERROR   ringct  src/ringct/rctSigs.cpp:280      Bad II size
2019-05-22 21:19:22.056    0xfc8bd4facc0        ERROR   ringct  src/ringct/rctSigs.cpp:280      Bad II size

[SNIP]

# Discussion History
## moneromooo-monero | 2019-05-23T07:34:10+00:00
Your log seems to be missing the interesting parts (the test failure(s)).

## mrme0w | 2019-05-23T19:32:21+00:00
It's my first day! :P

Tell me exactly what you need from me. Is it another log file? Do I re-run the tests and paste the output? Thanks.

## moneromooo-monero | 2019-05-23T19:44:06+00:00
build/wherever/tests/unit_tests/unit_tests.log. You can delete it first, so you only get one run logged.


## mrme0w | 2019-05-23T21:44:16+00:00
Running tests...
Test project /home/mrme0w/monero/build/OpenBSD/master/release
      Start  1: hash-target
 1/20 Test  #1: hash-target ......................   Passed    1.87 sec
      Start  2: core_tests
 2/20 Test  #2: core_tests .......................   Passed  2523.23 sec
      Start  3: cncrypto
 3/20 Test  #3: cncrypto .........................   Passed   21.98 sec
      Start  4: cnv4-jit
 4/20 Test  #4: cnv4-jit .........................   Passed  127.01 sec
      Start  5: functional_tests_rpc
 5/20 Test  #5: functional_tests_rpc .............***Failed    0.05 sec
      Start  6: unit_tests
 6/20 Test  #6: unit_tests .......................***Failed  181.70 sec
      Start  7: difficulty
 7/20 Test  #7: difficulty .......................   Passed    0.04 sec
      Start  8: wide_difficulty
 8/20 Test  #8: wide_difficulty ..................   Passed   19.98 sec
      Start  9: block_weight
 9/20 Test  #9: block_weight .....................   Passed   79.73 sec
      Start 10: hash-fast
10/20 Test #10: hash-fast ........................   Passed    0.03 sec
      Start 11: hash-slow
11/20 Test #11: hash-slow ........................   Passed    0.09 sec
      Start 12: hash-slow-1
12/20 Test #12: hash-slow-1 ......................   Passed    0.11 sec
      Start 13: hash-slow-2
13/20 Test #13: hash-slow-2 ......................   Passed    0.28 sec
      Start 14: hash-slow-4
14/20 Test #14: hash-slow-4 ......................   Passed    0.45 sec
      Start 15: hash-tree
15/20 Test #15: hash-tree ........................   Passed    0.01 sec
      Start 16: hash-extra-blake
16/20 Test #16: hash-extra-blake .................   Passed    0.02 sec
      Start 17: hash-extra-groestl
17/20 Test #17: hash-extra-groestl ...............   Passed    0.03 sec
      Start 18: hash-extra-jh
18/20 Test #18: hash-extra-jh ....................   Passed    0.02 sec
      Start 19: hash-extra-skein
19/20 Test #19: hash-extra-skein .................   Passed    0.02 sec
      Start 20: hash-variant2-int-sqrt
20/20 Test #20: hash-variant2-int-sqrt ...........   Passed  683.13 sec

90% tests passed, 2 tests failed out of 20

Total Test time (real) = 3641.10 sec

The following tests FAILED:
          5 - functional_tests_rpc (Failed)
          6 - unit_tests (Failed)
Errors while running CTest
gmake[1]: *** [Makefile:130: test] Error 8
gmake[1]: Leaving directory '/home/mrme0w/monero/build/OpenBSD/master/release'
gmake: *** [Makefile:95: release-test] Error 2


## mrme0w | 2019-05-23T21:45:41+00:00
[unit_tests.log.gz](https://github.com/monero-project/monero/files/3214276/unit_tests.log.gz)


## mrme0w | 2019-05-23T21:48:07+00:00
$ ./functional_tests
2019-05-23 21:47:15.317     W libunbound was not built with threads enabled - crashes may occur

... interesting.. this might have something to do with monerod becoming unstable after syncing all the blocks.

## moneromooo-monero | 2019-05-23T22:01:35+00:00
Hmm, the interesting output doesn't get saved to that file :/ 
Run "unit_tests" manually, and post the output of that.

If by unstable you mean crash, get a stack trace (gdb /path/to/monerod /path/to/core, bt).


## moneromooo-monero | 2019-05-23T22:02:28+00:00
Same for functional_tests:

build/release/tests/functional_tests_rpc.py /usr/bin/python tests/functional_tests build/release all

Adapt for python path and build path. Then post stdout/stderr.

## mrme0w | 2019-05-23T22:08:59+00:00
Okay, I'm running the tests again.

By unstable I mean it appears to leak memory and consume the entire CPU. This seems to happen after the block syncing is done.

I'm also looking into why the libunbound package on OpenBSD isn't built thread-safe.

## mrme0w | 2019-05-23T23:31:05+00:00
Okay, core_tests are passing now.. my loopback was firewalled.. my bad... :0


## mrme0w | 2019-05-23T23:45:30+00:00
$ pwd
/home/mrme0w/monero/tests/functional_tests
$ python2.7 functional_tests_rpc.py /usr/local/bin/python2.7 /home/mrme0w/monero/tests/functional_tests /home/mrme0w/monero/build/OpenBSD/master/release all
Starting servers...
[TEST STARTED] daemon_info
Traceback (most recent call last):
  File "/home/mrme0w/monero/tests/functional_tests/daemon_info.py", line 39, in <module>
    from framework.daemon import Daemon
  File "/home/mrme0w/monero/utils/python-rpc/framework/daemon.py", line 31, in <module>
    from .rpc import JSONRPC
  File "/home/mrme0w/monero/utils/python-rpc/framework/rpc.py", line 29, in <module>
    import requests
ImportError: No module named requests
[TEST FAILED] daemon_info
[TEST STARTED] blockchain
Traceback (most recent call last):
  File "/home/mrme0w/monero/tests/functional_tests/blockchain.py", line 44, in <module>
    from framework.daemon import Daemon
  File "/home/mrme0w/monero/utils/python-rpc/framework/daemon.py", line 31, in <module>
    from .rpc import JSONRPC
  File "/home/mrme0w/monero/utils/python-rpc/framework/rpc.py", line 29, in <module>
    import requests
ImportError: No module named requests
[TEST FAILED] blockchain
[TEST STARTED] wallet_address
Traceback (most recent call last):
  File "/home/mrme0w/monero/tests/functional_tests/wallet_address.py", line 41, in <module>
    from framework.wallet import Wallet
  File "/home/mrme0w/monero/utils/python-rpc/framework/wallet.py", line 31, in <module>
    from .rpc import JSONRPC
  File "/home/mrme0w/monero/utils/python-rpc/framework/rpc.py", line 29, in <module>
    import requests
ImportError: No module named requests

... and so on and so on...  suggestions?

## moneromooo-monero | 2019-05-24T07:39:14+00:00
Install the python requests module.

## mrme0w | 2019-05-25T23:12:14+00:00
ok.. new run...

$ pwd
/home/mrme0w/monero/tests/functional_tests
$ python2.7 functional_tests_rpc.py /usr/local/bin/python2.7 /home/mrme0w/monero/tests/functional_tests /home/mrme0w/monero/build/OpenBSD/master/release all
Starting servers...
[TEST STARTED] daemon_info
Test hard_fork_info
Test get_info
[TEST PASSED] daemon_info
[TEST STARTED] blockchain
Resetting blockchain
Test generating 5 blocks
Testing alt chains
mined tip block 5, nonce 0
mined alt block 5, nonce 1
mined alt block 5, nonce 2
mined alt block 5, nonce 3
mined alt block 5, nonce 4
mining 3 on 1
Checking alt blocks match
mining 4 on 3
Checking alt blocks match
[TEST PASSED] blockchain
[TEST STARTED] wallet_address
Resetting blockchain
Creating wallet
Getting address
Checking keys
Creating subaddresses
Testing open/close
Testing languages
Creating German wallet
Creating English wallet
Creating Spanish wallet
Creating French wallet
Creating Italian wallet
Creating Dutch wallet
Creating Portuguese wallet
Creating Russian wallet
Creating Japanese wallet
Creating Chinese (simplified) wallet
Creating Esperanto wallet
Creating Lojban wallet
[TEST PASSED] wallet_address
[TEST STARTED] integrated_address
Creating wallet
Checking local address
Checking different address
Checking bad payment id
Checking bad standard address
[TEST PASSED] integrated_address
[TEST STARTED] mining
Resetting blockchain
Creating wallet
Test mining
[TEST PASSED] mining
[TEST STARTED] transfer
Resetting blockchain
Creating wallets
Mining some blocks
Creating transfer to self
Checking short payment IDs cannot be used when not in an integrated address
Checking empty destination is rejected
Creating transfer to another, manual relay
Creating multi out transfer
Sending to integrated address
Checking get_bulk_payments
Checking double spend detection
Sending single output
[TEST PASSED] transfer
[TEST STARTED] txpool
Resetting blockchain
Creating wallet
Mining some blocks
Creating 5 transactions
Flushing 2 transactions
Flushing unknown transactions
Mining transactions
Popping block
[TEST PASSED] txpool
[TEST STARTED] multisig
Resetting blockchain
Mining some blocks
Mining some blocks
Mining some blocks
Mining some blocks
Mining some blocks
Creating 2/2 multisig wallet
Importing multisig info from [1, 0]
Creating multisig transaction from wallet 1
Signing multisig transaction with wallet 0
Submitting multisig transaction with wallet 0
Importing multisig info from [0, 1]
Creating 2/3 multisig wallet
Importing multisig info from [0, 2]
Creating multisig transaction from wallet 0
Signing multisig transaction with wallet 2
Submitting multisig transaction with wallet 2
Importing multisig info from [0, 1, 2]
Creating 3/4 multisig wallet
Importing multisig info from [0, 2, 3]
Creating multisig transaction from wallet 0
Signing multisig transaction with wallet 2
Submitting multisig transaction prematurely with wallet 3
Signing multisig transaction with wallet 3
Submitting multisig transaction with wallet 3
Importing multisig info from [0, 1, 2, 3]
Creating 2/4 multisig wallet
Importing multisig info from [1, 2]
Creating multisig transaction from wallet 1
Signing multisig transaction with wallet 2
Submitting multisig transaction with wallet 2
Importing multisig info from [0, 1, 2, 3]
[TEST PASSED] multisig
[TEST STARTED] cold_signing
Resetting blockchain
Creating hot and cold wallet
Mining some blocks
Creating transaction in hot wallet
Signing transaction with cold wallet
Submitting transaction with hot wallet
[TEST PASSED] cold_signing
[TEST STARTED] sign_message
Creating wallets
Signing/verifing messages
[TEST PASSED] sign_message
[TEST STARTED] proofs
Resetting blockchain
Mining some blocks
Creating wallets
Creating transaction
Checking tx key
Checking tx proof
Checking reserve proof
[TEST PASSED] proofs
[TEST STARTED] get_output_distribution
Resetting blockchain
Test get_output_distribution
[TEST PASSED] get_output_distribution
Stopping servers...
monerod(18148) in free(): chunk is already free 0x420afc66740
Done, 12/12 tests passed


A nice double-free in there somewhere.. hmm

## moneromooo-monero | 2019-05-26T11:07:06+00:00
Run with -DSANITIZE=ON in cmake. I don't get that here.

## moneromooo-monero | 2019-05-29T17:46:18+00:00
Any luck ?

## ston1th | 2019-06-09T08:56:55+00:00
Unfortunately `-fsanitize=address` is not supported on OpenBSD.

After some manual debugging I found the double free cause.

Here the `attrs` object is copied: https://github.com/monero-project/monero/blob/51766d026bb0337d7bff17f1e3c0c403b21eaefd/src/cryptonote_basic/miner.cpp#L374

The destructor of `attrs` and `m_attrs` is called and causes the double free:
https://github.com/boostorg/thread/blob/5c6180fa4fcdf4378a8b6bb8fa6b13832ab5227f/include/boost/thread/pthread/thread_data.hpp#L49

## moneromooo-monero | 2019-06-15T11:00:40+00:00
I think it's all good now, is it ?

## ston1th | 2019-06-20T14:57:55+00:00
Yes. All 20 tests pass for me.

PR #5679 fixes a tests generation issue.

## moneromooo-monero | 2019-06-20T16:18:02+00:00
Thanks.

+resolved

# Action History
- Created by: mrme0w | 2019-05-23T02:30:38+00:00
- Closed at: 2019-06-20T16:25:46+00:00
