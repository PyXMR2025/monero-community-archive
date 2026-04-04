---
title: monero full node - runtime_error
source_url: https://github.com/monero-project/monero/issues/8164
author: hajes
assignees: []
labels: []
created_at: '2022-01-30T16:37:40+00:00'
updated_at: '2022-02-01T18:16:21+00:00'
type: issue
status: closed
closed_at: '2022-02-01T18:16:21+00:00'
---

# Original Description
running full monero node on latest Debian server. Log is full of following errors:

2022-01-30 16:32:49.219 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:133  Exception: std::runtime_error
2022-01-30 16:32:49.219 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:134  Unwound call stack:
2022-01-30 16:32:49.219 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:172      [1]  0x116) [0x559bf3740477]:__cxa_throw+0x116) [0x559bf3740477]
2022-01-30 16:32:49.219 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:172      [2] /usr/local/bin/monerod(+0x1277b1) [0x559bf379c7b1]
2022-01-30 16:32:49.219 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:172      [3] /usr/local/bin/monerod(+0x88612f) [0x559bf3efb12f]
2022-01-30 16:32:49.219 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:172      [4] /usr/local/bin/monerod(+0x8836c6) [0x559bf3ef86c6]
2022-01-30 16:32:49.219 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:172      [5] /usr/local/bin/monerod(+0x63a16a) [0x559bf3caf16a]
2022-01-30 16:32:49.219 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:172      [6] /usr/local/bin/monerod(+0x621c3e) [0x559bf3c96c3e]
2022-01-30 16:32:49.219 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:172      [7] /usr/local/bin/monerod(+0x621de5) [0x559bf3c96de5]
2022-01-30 16:32:49.219 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:172      [8] /usr/local/bin/monerod(+0x621e98) [0x559bf3c96e98]
2022-01-30 16:32:49.219 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:172      [9] /usr/local/bin/monerod(+0x5bacf5) [0x559bf3c2fcf5]
2022-01-30 16:32:49.219 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:172      [10] /usr/local/bin/monerod(+0x67ef18) [0x559bf3cf3f18]
2022-01-30 16:32:49.219 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:172      [11] /usr/local/bin/monerod(+0x67f60c) [0x559bf3cf460c]
2022-01-30 16:32:49.220 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:172      [12] /usr/local/bin/monerod(+0x5bf135) [0x559bf3c34135]
2022-01-30 16:32:49.220 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:172      [13] /usr/local/bin/monerod(+0x5e7f3f) [0x559bf3c5cf3f]
2022-01-30 16:32:49.220 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:172      [14] /usr/local/bin/monerod(+0x554e72) [0x559bf3bc9e72]
2022-01-30 16:32:49.220 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:172      [15] /usr/local/bin/monerod(+0x203dca) [0x559bf3878dca]
2022-01-30 16:32:49.220 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:172      [16] /usr/local/bin/monerod(+0x208e68) [0x559bf387de68]
2022-01-30 16:32:49.220 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:172      [17] /usr/local/bin/monerod(+0x20b76c) [0x559bf388076c]
2022-01-30 16:32:49.220 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:172      [18] /usr/local/bin/monerod(+0x52e0b4) [0x559bf3ba30b4]
2022-01-30 16:32:49.220 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:172      [19] /usr/local/bin/monerod(+0x54e622) [0x559bf3bc3622]
2022-01-30 16:32:49.220 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:172      [20] /usr/local/bin/monerod(+0x527dea) [0x559bf3b9cdea]
2022-01-30 16:32:49.220 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:172      [21] /usr/local/bin/monerod(+0x529a16) [0x559bf3b9ea16]
2022-01-30 16:32:49.220 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:172      [22] /usr/local/bin/monerod(+0x529f35) [0x559bf3b9ef35]
2022-01-30 16:32:49.220 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:172      [23] /usr/local/bin/monerod(+0x183ca3) [0x559bf37f8ca3]
2022-01-30 16:32:49.220 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:172      [24] /usr/local/bin/monerod(+0x4e8090) [0x559bf3b5d090]
2022-01-30 16:32:49.220 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:172      [25]  0xb787) [0x7f8d01a5e787]:_64-linux-gnu/libboost_thread.so.1.74.0(+0xb787) [0x7f8d01a5e787]
2022-01-30 16:32:49.220 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:172      [26]  0x8ea7) [0x7f8d016c8ea7]:_64-linux-gnu/libpthread.so.0(+0x8ea7) [0x7f8d016c8ea7]
2022-01-30 16:32:49.220 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:172      [27]  0x3f) [0x7f8d015f6def]:_64-linux-gnu/libc.so.6(clone+0x3f) [0x7f8d015f6def]
2022-01-30 16:32:49.220 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:172

# Discussion History
## selsta | 2022-02-01T02:59:20+00:00
Do you have any issues apart from the error in the log?

## hajes | 2022-02-01T04:36:57+00:00
there seems to be no issues. I just wonder whether is something wrong or is it normal

## selsta | 2022-02-01T18:16:21+00:00
It's just an uncaught exception. You can ignore it if you don't have any other issues.

# Action History
- Created by: hajes | 2022-01-30T16:37:40+00:00
- Closed at: 2022-02-01T18:16:21+00:00
