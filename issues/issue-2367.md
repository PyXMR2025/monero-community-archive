---
title: Fail to compile on windows RPC-Wallet
source_url: https://github.com/monero-project/monero/issues/2367
author: mps01k
assignees: []
labels:
- invalid
created_at: '2017-08-28T14:27:19+00:00'
updated_at: '2017-09-12T15:48:26+00:00'
type: issue
status: closed
closed_at: '2017-09-12T15:48:26+00:00'
---

# Original Description
Since about 4 days ago I cant compile on Windows any more with "make" it compiles everything except the RPC-WALLET that shows google test cant compile anymore. I looked at googletest here on github and shows some files were deleted a few days ago. I think maybe this has something to do with it. Any body else seeing this issue? I can compile on Mac no problem.

[ 25%] Building CXX object CMakeFiles/gtest.dir/src/gtest-all.cc.obj
In file included from C:/msys64/home/nathan/monero-core/monero/tests/gtest/include/gtest/internal/gtest-internal.h:40:0,
                 from C:/msys64/home/nathan/monero-core/monero/tests/gtest/include/gtest/gtest.h:58,
                 from C:/msys64/home/nathan/monero-core/monero/tests/gtest/src/gtest-all.cc:39:
C:/msys64/home/nathan/monero-core/monero/tests/gtest/include/gtest/internal/gtest-port.h:1782:3: error: 'AutoHandle' does not name a type; did you mean 'LongToHandle'?
   AutoHandle thread_;
   ^~~~~~~~~~
   LongToHandle
In file included from C:/msys64/home/nathan/monero-core/monero/tests/gtest/src/gtest-all.cc:43:0:

Edit: I was trying to Build on 32 Bit Environment, not sure if that was the reason. Changed to 64Bit Environment and it built with no problem.

# Discussion History
## moneromooo-monero | 2017-09-01T22:40:11+00:00
Your log shows "C:/msys64" though, that's presumably the 64 bit environment ? But it it was mixed 32/64, then that most likely explains the error, especially as the build bot seems to compile win32 just fine (though it does fail to link).

## moneromooo-monero | 2017-09-12T15:43:55+00:00
Seems to have been a 32/64 mismatch.

+invalid

# Action History
- Created by: mps01k | 2017-08-28T14:27:19+00:00
- Closed at: 2017-09-12T15:48:26+00:00
