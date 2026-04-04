---
title: '[aarch64/Manjaro] --stagenet and --testnet syncs fail. "Block with id <...>
  does not have enough proof of work"'
source_url: https://github.com/monero-project/monero/issues/7982
author: Dendrocalamus64
assignees: []
labels: []
created_at: '2021-09-30T00:05:04+00:00'
updated_at: '2022-02-18T23:49:01+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Monero 'Oxygen Orion' (v0.17.2.3-release) built & running on rockpro64 with current Manjaro linux, kernel 5.14.8-1-MANJARO-ARM.  It's working on mainnet.  I'm now trying to run monerod with --stagenet or --testnet, syncing from scratch, and I get the same error as #847 did 5 years ago.  It starts at height 3 and can't go any higher.  GCC version 10.2.0.

Loglevel 0:
```
2021-09-29 18:34:32.337 [P2P0]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:410     SYNCHRONIZATION started
2021-09-29 18:34:36.235 [P2P1]  WARNING global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:2910    monerod is now disconnected from the network
```
continually repeated.
Loglevel 1:
```
2021-09-29 18:53:32.713 [P2P4]  ERROR   verify  src/cryptonote_core/blockchain.cpp:4120 Block with id: <24f91aec948869d9453d37baea317f1a9b9f40f91577160997fff630147e159b>
2021-09-29 18:53:32.713 [P2P4]  ERROR   verify  src/cryptonote_core/blockchain.cpp:4120 does not have enough proof of work: <ef81a6d6a1feca1139b88aa77cacde5b4bb1e188eb249c6f86a0cdbb7fd25d0a> at height 3, unexpected difficulty: 60
```
Looks like it bans peers for that and eventually runs out of peers to try until p2pstate.bin is deleted.

Currently running the tests & waiting for core_tests to finish.

# Discussion History
## Dendrocalamus64 | 2021-09-30T10:37:14+00:00
```
Running tests...
      Start  1: hash-target
 1/22 Test  #1: hash-target ......................   Passed    1.07 sec
      Start  2: wallet-crypto-bench
 2/22 Test  #2: wallet-crypto-bench ..............   Passed    1.79 sec
      Start  3: core_tests
 3/22 Test  #3: core_tests .......................   Passed  16276.52 sec
      Start  4: cncrypto
 4/22 Test  #4: cncrypto .........................   Passed   16.35 sec
      Start  5: cnv4-jit
 5/22 Test  #5: cnv4-jit .........................   Passed  624.95 sec
      Start  6: functional_tests_rpc
 6/22 Test  #6: functional_tests_rpc .............   Passed  2348.59 sec
      Start  7: check_missing_rpc_methods
 7/22 Test  #7: check_missing_rpc_methods ........   Passed    0.53 sec
      Start  8: unit_tests
 8/22 Test  #8: unit_tests .......................***Failed  324.67 sec
      Start  9: difficulty
 9/22 Test  #9: difficulty .......................   Passed    0.11 sec
      Start 10: wide_difficulty
10/22 Test #10: wide_difficulty ..................   Passed   14.22 sec
      Start 11: block_weight
11/22 Test #11: block_weight .....................   Passed   49.76 sec
      Start 12: hash-fast
12/22 Test #12: hash-fast ........................   Passed    0.08 sec
      Start 13: hash-slow
13/22 Test #13: hash-slow ........................***Failed    0.57 sec
      Start 14: hash-slow-1
14/22 Test #14: hash-slow-1 ......................***Failed    0.69 sec
      Start 15: hash-slow-2
15/22 Test #15: hash-slow-2 ......................***Failed    1.62 sec
      Start 16: hash-slow-4
16/22 Test #16: hash-slow-4 ......................***Failed    3.11 sec
      Start 17: hash-tree
17/22 Test #17: hash-tree ........................   Passed    0.04 sec
      Start 18: hash-extra-blake
18/22 Test #18: hash-extra-blake .................   Passed    0.05 sec
      Start 19: hash-extra-groestl
19/22 Test #19: hash-extra-groestl ...............   Passed    0.07 sec
      Start 20: hash-extra-jh
20/22 Test #20: hash-extra-jh ....................   Passed    0.06 sec
      Start 21: hash-extra-skein
21/22 Test #21: hash-extra-skein .................   Passed    0.05 sec
      Start 22: hash-variant2-int-sqrt
22/22 Test #22: hash-variant2-int-sqrt ...........   Passed  565.52 sec

77% tests passed, 5 tests failed out of 22

Total Test time (real) = 20230.75 sec

The following tests FAILED:
          8 - unit_tests (Failed)
         13 - hash-slow (Failed)
         14 - hash-slow-1 (Failed)
         15 - hash-slow-2 (Failed)
         16 - hash-slow-4 (Failed)
Errors while running CTest
```

## selsta | 2021-10-06T02:26:26+00:00
I assume this is self compiled. Can you test the Linux ARM binaries from getmonero.org (in case they are compatible) and check if you have the same issue?

## Dendrocalamus64 | 2021-10-06T03:02:02+00:00
Yes, it's self-compiled.

Now testing file from https://downloads.getmonero.org/cli/linuxarm8
monero-linux-armv8-v0.17.2.3.tar.bz2

That binary of monerod is compatible, and it does not have the problem.  It's syncing successfully so far on both stagenet and testnet.

## selsta | 2021-10-06T03:03:45+00:00
Compiler bug? Not sure.

## Dendrocalamus64 | 2021-10-06T13:45:29+00:00
I left the getmonero binary syncing on stagenet; it got to block 124451 and then stalled again with another problem.

Loglevel 0: Hours of
```
2021-10-06 06:16:41.254 I [176.9.0.187:38080 OUT] Sync data returned a new top block candidate: 124451 -> 936976 [Your node is 812525 blocks (1.5 years) behind]              
2021-10-06 06:16:41.255 I SYNCHRONIZATION started                                                                                                                             
2021-10-06 06:17:17.520 W monerod is now disconnected from the network                                                                                                        
2021-10-06 06:31:08.083 I [95.217.83.249:38080 OUT] Sync data returned a new top block candidate: 124451 -> 936987 [Your node is 812536 blocks (1.5 years) behind]            
2021-10-06 06:31:08.084 I SYNCHRONIZATION started                                                                                                                             
2021-10-06 06:31:33.938 W monerod is now disconnected from the network                                                                                       
```

Loglevel 1 example:
```
2021-10-06 13:15:37.221 I [185.110.89.141:38080 OUT] [0] state: requesting callback in state synchronizing                                                                    
2021-10-06 13:15:37.222 I [185.110.89.141:38080 OUT]  kicking idle peer, last update 27.513 seconds ago, expecting 2007                                                       
2021-10-06 13:15:37.222 I [185.110.89.141:38080 OUT] [0] state: adding blocks in state synchronizing                                                                          
2021-10-06 13:15:37.223 I [185.110.89.141:38080 OUT] [0] state: stopping adding blocks in state synchronizing                                                                 
2021-10-06 13:15:37.223 I [185.110.89.141:38080 OUT] [0] state: We can download nothing from this peer, dropping in state synchronizing                                       
2021-10-06 13:15:37.224 E [185.110.89.141:38080 OUT] Failed to request missing objects, dropping connection                                                                   
2021-10-06 13:15:37.224 I Target height decreasing from 937209 to 0                                                                                                           
2021-10-06 13:15:37.225 W monerod is now disconnected from the network                                                                                                        
2021-10-06 13:15:37.225 I [185.110.89.141:38080 OUT] [0] state: closed in state synchronizing                                                                                 
2021-10-06 13:15:37.226 I [185.110.89.141:38080 10bdf4c6-3e39-4a27-9cb2-3a75052d5656 OUT] CLOSE CONNECTION
```

It keeps giving `Failed to request missing objects, dropping connection`, sometimes `returned not all requested objects (context.m_requested_objects.size()=20), dropping connection`

testnet sync is stuck at 4701 with the same error.  I'm going to delete that one and try it without --prune-blockchain.
Result: Now it gets the same error from block 1.  Maybe it's network state.  I'll leave it running on stagenet and see if it eventually starts syncing again.

The net hash reported is very low (stagenet 648 H/s vs mainnet 2.86 GH/s) so maybe there just aren't any full nodes online to sync from.

## selsta | 2022-02-18T23:49:01+00:00
I run a testnet and a stagenet node. The network should be fine.

# Action History
- Created by: Dendrocalamus64 | 2021-09-30T00:05:04+00:00
