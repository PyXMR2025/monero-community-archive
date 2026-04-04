---
title: 17.2 Debian patch
source_url: https://github.com/monero-project/monero/issues/8305
author: sweeden-ttu
assignees: []
labels: []
created_at: '2022-04-30T21:10:34+00:00'
updated_at: '2022-05-01T03:03:51+00:00'
type: issue
status: closed
closed_at: '2022-05-01T03:03:51+00:00'
---

# Original Description
I'm removing the recommendation to update to 17.3 in the Debian 17.2 release.  It's clearly unstable the make files can't even run tests on Microsoft or OSX.   17.3 is an ANDROID only device branch so far.

# Discussion History
## sweeden-ttu | 2022-04-30T21:17:08+00:00
@selsta 

## sweeden-ttu | 2022-04-30T21:18:24+00:00
Mac OSX Results: After 4 hours it can't run on CORE BECAUSE YOU VIRTUALIZED IT

[ 98%] Built target net_load_tests_clt
[100%] Building CXX object tests/net_load_tests/CMakeFiles/net_load_tests_srv.dir/srv.cpp.o
[100%] Linking CXX executable net_load_tests_srv
clang: warning: argument unused during compilation: '-pie' [-Wunused-command-line-argument]
[100%] Built target net_load_tests_srv
Running tests...
Test project /Volumes/Ext4/.bitmonero/github/build/Darwin/_HEAD_detached_at_v0.17.3.2_/debug
      Start  1: hash-target
 1/21 Test  #1: hash-target ......................   Passed    3.58 sec
      Start  2: wallet-crypto-bench
 2/21 Test  #2: wallet-crypto-bench ..............   Passed    1.64 sec
      Start  3: core_tests
^Cmake[1]: *** [test] Interrupt: 2
make: *** [debug-test] Interrupt: 2


## hyc | 2022-05-01T03:03:51+00:00
I see no bug here. Core tests routinely takes over 6 hours on my old Intel laptop.

# Action History
- Created by: sweeden-ttu | 2022-04-30T21:10:34+00:00
- Closed at: 2022-05-01T03:03:51+00:00
