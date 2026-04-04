---
title: cncrypto tests fail on aarch64 arm64
source_url: https://github.com/monero-project/monero/issues/4228
author: radfish
assignees: []
labels: []
created_at: '2018-08-05T21:03:33+00:00'
updated_at: '2018-09-11T09:24:53+00:00'
type: issue
status: closed
closed_at: '2018-09-11T09:24:53+00:00'
---

# Original Description
On aarch64 arm64 board, cncrypto test fails:

          Start  2: cncrypto
     2/11 Test  #2: cncrypto .........................***Failed   31.64 sec


    $ tests/crypto/cncrypto-tests  ../tests/crypto/tests.txt
    Wrong result on test 338
    Wrong result on test 339
    ...

Build flags:  `-march=armv8-a -O2 -pipe -fstack-protector-strong -fno-plt` (possibly others too)
Commit: 0dddfeacc982ad208808e3a828163837fc4aba38

This appears to be a regression, because I don't remember having this issue on this board some months ago, and I do usually build the package with tests, but can't be 100% sure.

Anything change recently with aarch64?

# Discussion History
## danrmiller | 2018-08-05T22:08:18+00:00
Check if #4159 does it

## radfish | 2018-08-07T03:27:19+00:00
Thanks. Yes, #4159  plus the patch to cmake to link with libsodium (given in comments on that same PR) fixes the issue. I'll leave this open for others to see until #4159 gets merged.

## moneromooo-monero | 2018-09-11T09:18:29+00:00
+resolved

# Action History
- Created by: radfish | 2018-08-05T21:03:33+00:00
- Closed at: 2018-09-11T09:24:53+00:00
