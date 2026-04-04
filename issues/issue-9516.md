---
title: Synchronization errors  monero-0.18.3.4-2
source_url: https://github.com/monero-project/monero/issues/9516
author: divinitus
assignees: []
labels:
- duplicate
created_at: '2024-10-12T15:36:12+00:00'
updated_at: '2024-10-17T23:30:00+00:00'
type: issue
status: closed
closed_at: '2024-10-17T23:29:49+00:00'
---

# Original Description
While performing initial synchronization process around 90% of full node (unpruned) the syn process slows down significantly and starts to produce more and more messages like those:

```
2024-10-12 15:25:02.036 [P2P0]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1696    Synced 3142356/3257498 (96%, 115142 left)
2024-10-12 15:25:20.527 [P2P0]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1696    Synced 3142376/3257498 (96%, 115122 left)
2024-10-12 15:25:53.672 [P2P0]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1696    Synced 3142396/3257498 (96%, 115102 left)
2024-10-12 15:26:43.508 [P2P0]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1696    Synced 3142416/3257498 (96%, 115082 left, 3% of total synced, estimated 3.1 days left)
2024-10-12 15:27:33.596 [P2P0]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1696    Synced 3142436/3257499 (96%, 115063 left)
2024-10-12 15:27:43.553 [P2P6]  INFO    stacktrace      src/common/stack_trace.cpp:133  Exception: boost::wrapexcept<boost::bad_weak_ptr>
2024-10-12 15:27:43.553 [P2P6]  INFO    stacktrace      src/common/stack_trace.cpp:134  Unwound call stack:
2024-10-12 15:27:43.554 [P2P6]  INFO    stacktrace      src/common/stack_trace.cpp:172      [1] /usr/bin/monerod(+0x10d348) [0x58cf1a2b2348]
2024-10-12 15:27:43.554 [P2P6]  INFO    stacktrace      src/common/stack_trace.cpp:172      [2] /usr/bin/monerod(+0x7f2a9) [0x58cf1a2242a9]
2024-10-12 15:27:43.554 [P2P6]  INFO    stacktrace      src/common/stack_trace.cpp:172      [3] /usr/bin/monerod(+0x2f59d2) [0x58cf1a49a9d2]
2024-10-12 15:27:43.554 [P2P6]  INFO    stacktrace      src/common/stack_trace.cpp:172      [4] /usr/bin/monerod(+0x31f198) [0x58cf1a4c4198]
2024-10-12 15:27:43.554 [P2P6]  INFO    stacktrace      src/common/stack_trace.cpp:172      [5] /usr/bin/monerod(+0x308d4a) [0x58cf1a4add4a]
2024-10-12 15:27:43.554 [P2P6]  INFO    stacktrace      src/common/stack_trace.cpp:172      [6] /usr/bin/monerod(+0x32e491) [0x58cf1a4d3491]
2024-10-12 15:27:43.554 [P2P6]  INFO    stacktrace      src/common/stack_trace.cpp:172      [7] /usr/bin/monerod(+0x34f02b) [0x58cf1a4f402b]
2024-10-12 15:27:43.554 [P2P6]  INFO    stacktrace      src/common/stack_trace.cpp:172      [8] /usr/bin/monerod(+0x5c6a15) [0x58cf1a76ba15]
2024-10-12 15:27:43.554 [P2P6]  INFO    stacktrace      src/common/stack_trace.cpp:172      [9] /usr/bin/monerod(+0x33239a) [0x58cf1a4d739a]
2024-10-12 15:27:43.554 [P2P6]  INFO    stacktrace      src/common/stack_trace.cpp:172      [10]  0x10f63) [0x7ee915fcbf63]:_thread.so.1.86.0(+0x10f63) [0x7ee915fcbf63]
2024-10-12 15:27:43.554 [P2P6]  INFO    stacktrace      src/common/stack_trace.cpp:172      [11] /usr/lib/libc.so.6(+0x9439d) [0x7ee9154a339d]
2024-10-12 15:27:43.554 [P2P6]  INFO    stacktrace      src/common/stack_trace.cpp:172      [12] /usr/lib/libc.so.6(+0x11949c) [0x7ee91552849c]
2024-10-12 15:27:43.554 [P2P6]  INFO    stacktrace      src/common/stack_trace.cpp:172
2024-10-12 15:28:12.563 [P2P0]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1696    Synced 3142456/3257499 (96%, 115043 left)
2024-10-12 15:28:55.495 [P2P0]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1696    Synced 3142476/3257499 (96%, 115023 left, 3% of total synced, estimated 3.1 days left)
```

Exceptions may happen once per hour but sometimes it happens several times in a row resulting in sync restart:


```
2024-10-12 15:30:32.334 [P2P3]  INFO    stacktrace      src/common/stack_trace.cpp:133  Exception: boost::wrapexcept<boost::bad_weak_ptr>
2024-10-12 15:30:32.334 [P2P3]  INFO    stacktrace      src/common/stack_trace.cpp:134  Unwound call stack:
2024-10-12 15:30:32.334 [P2P3]  INFO    stacktrace      src/common/stack_trace.cpp:172      [1] /usr/bin/monerod(+0x10d348) [0x58cf1a2b2348]
2024-10-12 15:30:32.334 [P2P3]  INFO    stacktrace      src/common/stack_trace.cpp:172      [2] /usr/bin/monerod(+0x7f2a9) [0x58cf1a2242a9]
2024-10-12 15:30:32.334 [P2P3]  INFO    stacktrace      src/common/stack_trace.cpp:172      [3] /usr/bin/monerod(+0x2f59d2) [0x58cf1a49a9d2]
2024-10-12 15:30:32.334 [P2P3]  INFO    stacktrace      src/common/stack_trace.cpp:172      [4] /usr/bin/monerod(+0x30b2e3) [0x58cf1a4b02e3]
2024-10-12 15:30:32.334 [P2P3]  INFO    stacktrace      src/common/stack_trace.cpp:172      [5] /usr/bin/monerod(+0x3239e7) [0x58cf1a4c89e7]
2024-10-12 15:30:32.334 [P2P3]  INFO    stacktrace      src/common/stack_trace.cpp:172      [6] /usr/bin/monerod(+0x671000) [0x58cf1a816000]
2024-10-12 15:30:32.334 [P2P3]  INFO    stacktrace      src/common/stack_trace.cpp:172      [7] /usr/bin/monerod(+0x30ac5a) [0x58cf1a4afc5a]
2024-10-12 15:30:32.334 [P2P3]  INFO    stacktrace      src/common/stack_trace.cpp:172      [8] /usr/bin/monerod(+0x372448) [0x58cf1a517448]
2024-10-12 15:30:32.334 [P2P3]  INFO    stacktrace      src/common/stack_trace.cpp:172      [9] /usr/bin/monerod(+0x1610b5) [0x58cf1a3060b5]
2024-10-12 15:30:32.335 [P2P3]  INFO    stacktrace      src/common/stack_trace.cpp:172      [10] /usr/bin/monerod(+0x5c6a15) [0x58cf1a76ba15]
2024-10-12 15:30:32.335 [P2P3]  INFO    stacktrace      src/common/stack_trace.cpp:172      [11] /usr/bin/monerod(+0x33239a) [0x58cf1a4d739a]
2024-10-12 15:30:32.335 [P2P3]  INFO    stacktrace      src/common/stack_trace.cpp:172      [12]  0x10f63) [0x7ee915fcbf63]:_thread.so.1.86.0(+0x10f63) [0x7ee915fcbf63]
2024-10-12 15:30:32.335 [P2P3]  INFO    stacktrace      src/common/stack_trace.cpp:172      [13] /usr/lib/libc.so.6(+0x9439d) [0x7ee9154a339d]
2024-10-12 15:30:32.335 [P2P3]  INFO    stacktrace      src/common/stack_trace.cpp:172      [14] /usr/lib/libc.so.6(+0x11949c) [0x7ee91552849c]
2024-10-12 15:30:32.335 [P2P3]  INFO    stacktrace      src/common/stack_trace.cpp:172
2024-10-12 15:30:32.335 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:133  Exception: boost::wrapexcept<boost::bad_weak_ptr>
2024-10-12 15:30:32.335 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:134  Unwound call stack:
2024-10-12 15:30:32.335 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:172      [1] /usr/bin/monerod(+0x10d348) [0x58cf1a2b2348]
2024-10-12 15:30:32.335 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:172      [2] /usr/bin/monerod(+0x7f2a9) [0x58cf1a2242a9]
2024-10-12 15:30:32.335 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:172      [3] /usr/bin/monerod(+0x2f59d2) [0x58cf1a49a9d2]
2024-10-12 15:30:32.335 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:172      [4] /usr/bin/monerod(+0x3237f2) [0x58cf1a4c87f2]
2024-10-12 15:30:32.335 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:172      [5] /usr/bin/monerod(+0x671000) [0x58cf1a816000]
2024-10-12 15:30:32.335 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:172      [6] /usr/bin/monerod(+0x30ac5a) [0x58cf1a4afc5a]
2024-10-12 15:30:32.336 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:172      [7] /usr/bin/monerod(+0x372448) [0x58cf1a517448]
2024-10-12 15:30:32.336 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:172      [8] /usr/bin/monerod(+0x1610b5) [0x58cf1a3060b5]
2024-10-12 15:30:32.336 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:172      [9] /usr/bin/monerod(+0x5c6a15) [0x58cf1a76ba15]
2024-10-12 15:30:32.336 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:172      [10] /usr/bin/monerod(+0x33239a) [0x58cf1a4d739a]
2024-10-12 15:30:32.336 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:172      [11]  0x10f63) [0x7ee915fcbf63]:_thread.so.1.86.0(+0x10f63) [0x7ee915fcbf63]
2024-10-12 15:30:32.336 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:172      [12] /usr/lib/libc.so.6(+0x9439d) [0x7ee9154a339d]
2024-10-12 15:30:32.336 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:172      [13] /usr/lib/libc.so.6(+0x11949c) [0x7ee91552849c]
2024-10-12 15:30:32.336 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:172
2024-10-12 15:30:32.336 [P2P7]  INFO    stacktrace      src/common/stack_trace.cpp:133  Exception: boost::wrapexcept<boost::bad_weak_ptr>
2024-10-12 15:30:32.336 [P2P7]  INFO    stacktrace      src/common/stack_trace.cpp:134  Unwound call stack:
2024-10-12 15:30:32.336 [P2P7]  INFO    stacktrace      src/common/stack_trace.cpp:172      [1] /usr/bin/monerod(+0x10d348) [0x58cf1a2b2348]
2024-10-12 15:30:32.336 [P2P7]  INFO    stacktrace      src/common/stack_trace.cpp:172      [2] /usr/bin/monerod(+0x7f2a9) [0x58cf1a2242a9]
2024-10-12 15:30:32.336 [P2P7]  INFO    stacktrace      src/common/stack_trace.cpp:172      [3] /usr/bin/monerod(+0x2f59d2) [0x58cf1a49a9d2]
2024-10-12 15:30:32.336 [P2P7]  INFO    stacktrace      src/common/stack_trace.cpp:172      [4] /usr/bin/monerod(+0x30b2e3) [0x58cf1a4b02e3]
2024-10-12 15:30:32.336 [P2P7]  INFO    stacktrace      src/common/stack_trace.cpp:172      [5] /usr/bin/monerod(+0x3239e7) [0x58cf1a4c89e7]
2024-10-12 15:30:32.336 [P2P7]  INFO    stacktrace      src/common/stack_trace.cpp:172      [6] /usr/bin/monerod(+0x671000) [0x58cf1a816000]
2024-10-12 15:30:32.336 [P2P7]  INFO    stacktrace      src/common/stack_trace.cpp:172      [7] /usr/bin/monerod(+0x30ac5a) [0x58cf1a4afc5a]
2024-10-12 15:30:32.336 [P2P7]  INFO    stacktrace      src/common/stack_trace.cpp:172      [8] /usr/bin/monerod(+0x372448) [0x58cf1a517448]
2024-10-12 15:30:32.336 [P2P7]  INFO    stacktrace      src/common/stack_trace.cpp:172      [9] /usr/bin/monerod(+0x1610b5) [0x58cf1a3060b5]
2024-10-12 15:30:32.336 [P2P7]  INFO    stacktrace      src/common/stack_trace.cpp:172      [10] /usr/bin/monerod(+0x5c6a15) [0x58cf1a76ba15]
2024-10-12 15:30:32.336 [P2P7]  INFO    stacktrace      src/common/stack_trace.cpp:172      [11] /usr/bin/monerod(+0x33239a) [0x58cf1a4d739a]
2024-10-12 15:30:32.337 [P2P7]  INFO    stacktrace      src/common/stack_trace.cpp:172      [12]  0x10f63) [0x7ee915fcbf63]:_thread.so.1.86.0(+0x10f63) [0x7ee915fcbf63]
2024-10-12 15:30:32.337 [P2P7]  INFO    stacktrace      src/common/stack_trace.cpp:172      [13] /usr/lib/libc.so.6(+0x9439d) [0x7ee9154a339d]
2024-10-12 15:30:32.337 [P2P7]  INFO    stacktrace      src/common/stack_trace.cpp:172      [14] /usr/lib/libc.so.6(+0x11949c) [0x7ee91552849c]
2024-10-12 15:30:32.337 [P2P7]  INFO    stacktrace      src/common/stack_trace.cpp:172
2024-10-12 15:30:38.909 [P2P9]  INFO    stacktrace      src/common/stack_trace.cpp:133  Exception: boost::wrapexcept<boost::bad_weak_ptr>
2024-10-12 15:30:38.909 [P2P9]  INFO    stacktrace      src/common/stack_trace.cpp:134  Unwound call stack:
2024-10-12 15:30:38.909 [P2P9]  INFO    stacktrace      src/common/stack_trace.cpp:172      [1] /usr/bin/monerod(+0x10d348) [0x58cf1a2b2348]
2024-10-12 15:30:38.910 [P2P9]  INFO    stacktrace      src/common/stack_trace.cpp:172      [2] /usr/bin/monerod(+0x7f2a9) [0x58cf1a2242a9]
2024-10-12 15:30:38.910 [P2P9]  INFO    stacktrace      src/common/stack_trace.cpp:172      [3] /usr/bin/monerod(+0x2f59d2) [0x58cf1a49a9d2]
2024-10-12 15:30:38.910 [P2P9]  INFO    stacktrace      src/common/stack_trace.cpp:172      [4] /usr/bin/monerod(+0x30b2e3) [0x58cf1a4b02e3]
2024-10-12 15:30:38.910 [P2P9]  INFO    stacktrace      src/common/stack_trace.cpp:172      [5] /usr/bin/monerod(+0x3239e7) [0x58cf1a4c89e7]
2024-10-12 15:30:38.910 [P2P9]  INFO    stacktrace      src/common/stack_trace.cpp:172      [6] /usr/bin/monerod(+0x671000) [0x58cf1a816000]
2024-10-12 15:30:38.910 [P2P9]  INFO    stacktrace      src/common/stack_trace.cpp:172      [7] /usr/bin/monerod(+0x30ac5a) [0x58cf1a4afc5a]
2024-10-12 15:30:38.910 [P2P9]  INFO    stacktrace      src/common/stack_trace.cpp:172      [8] /usr/bin/monerod(+0x372448) [0x58cf1a517448]
2024-10-12 15:30:38.910 [P2P9]  INFO    stacktrace      src/common/stack_trace.cpp:172      [9] /usr/bin/monerod(+0x1610b5) [0x58cf1a3060b5]
2024-10-12 15:30:38.910 [P2P9]  INFO    stacktrace      src/common/stack_trace.cpp:172      [10] /usr/bin/monerod(+0x5c6a15) [0x58cf1a76ba15]
2024-10-12 15:30:38.910 [P2P9]  INFO    stacktrace      src/common/stack_trace.cpp:172      [11] /usr/bin/monerod(+0x33239a) [0x58cf1a4d739a]
2024-10-12 15:30:38.910 [P2P9]  INFO    stacktrace      src/common/stack_trace.cpp:172      [12]  0x10f63) [0x7ee915fcbf63]:_thread.so.1.86.0(+0x10f63) [0x7ee915fcbf63]
2024-10-12 15:30:38.910 [P2P9]  INFO    stacktrace      src/common/stack_trace.cpp:172      [13] /usr/lib/libc.so.6(+0x9439d) [0x7ee9154a339d]
2024-10-12 15:30:38.910 [P2P9]  INFO    stacktrace      src/common/stack_trace.cpp:172      [14] /usr/lib/libc.so.6(+0x11949c) [0x7ee91552849c]
2024-10-12 15:30:38.910 [P2P9]  INFO    stacktrace      src/common/stack_trace.cpp:172
2024-10-12 15:30:38.910 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:133  Exception: boost::wrapexcept<boost::bad_weak_ptr>
2024-10-12 15:30:38.910 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:134  Unwound call stack:
2024-10-12 15:30:38.910 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:172      [1] /usr/bin/monerod(+0x10d348) [0x58cf1a2b2348]
2024-10-12 15:30:38.910 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:172      [2] /usr/bin/monerod(+0x7f2a9) [0x58cf1a2242a9]
2024-10-12 15:30:38.910 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:172      [3] /usr/bin/monerod(+0x2f59d2) [0x58cf1a49a9d2]
2024-10-12 15:30:38.910 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:172      [4] /usr/bin/monerod(+0x3237f2) [0x58cf1a4c87f2]
2024-10-12 15:30:38.910 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:172      [5] /usr/bin/monerod(+0x671000) [0x58cf1a816000]
2024-10-12 15:30:38.910 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:172      [6] /usr/bin/monerod(+0x30ac5a) [0x58cf1a4afc5a]
2024-10-12 15:30:38.910 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:172      [7] /usr/bin/monerod(+0x372448) [0x58cf1a517448]
2024-10-12 15:30:38.910 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:172      [8] /usr/bin/monerod(+0x1610b5) [0x58cf1a3060b5]
2024-10-12 15:30:38.910 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:172      [9] /usr/bin/monerod(+0x5c6a15) [0x58cf1a76ba15]
2024-10-12 15:30:38.910 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:172      [10] /usr/bin/monerod(+0x33239a) [0x58cf1a4d739a]
2024-10-12 15:30:38.910 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:172      [11]  0x10f63) [0x7ee915fcbf63]:_thread.so.1.86.0(+0x10f63) [0x7ee915fcbf63]
2024-10-12 15:30:38.910 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:172      [12] /usr/lib/libc.so.6(+0x9439d) [0x7ee9154a339d]
2024-10-12 15:30:38.910 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:172      [13] /usr/lib/libc.so.6(+0x11949c) [0x7ee91552849c]
2024-10-12 15:30:38.910 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:172
2024-10-12 15:30:38.910 [P2P1]  INFO    stacktrace      src/common/stack_trace.cpp:133  Exception: boost::wrapexcept<boost::bad_weak_ptr>
2024-10-12 15:30:38.910 [P2P1]  INFO    stacktrace      src/common/stack_trace.cpp:134  Unwound call stack:
2024-10-12 15:30:38.910 [P2P1]  INFO    stacktrace      src/common/stack_trace.cpp:172      [1] /usr/bin/monerod(+0x10d348) [0x58cf1a2b2348]
2024-10-12 15:30:38.910 [P2P1]  INFO    stacktrace      src/common/stack_trace.cpp:172      [2] /usr/bin/monerod(+0x7f2a9) [0x58cf1a2242a9]
2024-10-12 15:30:38.910 [P2P1]  INFO    stacktrace      src/common/stack_trace.cpp:172      [3] /usr/bin/monerod(+0x2f59d2) [0x58cf1a49a9d2]
2024-10-12 15:30:38.910 [P2P1]  INFO    stacktrace      src/common/stack_trace.cpp:172      [4] /usr/bin/monerod(+0x3237f2) [0x58cf1a4c87f2]
2024-10-12 15:30:38.910 [P2P1]  INFO    stacktrace      src/common/stack_trace.cpp:172      [5] /usr/bin/monerod(+0x671000) [0x58cf1a816000]
2024-10-12 15:30:38.910 [P2P1]  INFO    stacktrace      src/common/stack_trace.cpp:172      [6] /usr/bin/monerod(+0x30ac5a) [0x58cf1a4afc5a]
2024-10-12 15:30:38.910 [P2P1]  INFO    stacktrace      src/common/stack_trace.cpp:172      [7] /usr/bin/monerod(+0x372448) [0x58cf1a517448]
2024-10-12 15:30:38.910 [P2P1]  INFO    stacktrace      src/common/stack_trace.cpp:172      [8] /usr/bin/monerod(+0x1610b5) [0x58cf1a3060b5]
2024-10-12 15:30:38.910 [P2P1]  INFO    stacktrace      src/common/stack_trace.cpp:172      [9] /usr/bin/monerod(+0x5c6a15) [0x58cf1a76ba15]
2024-10-12 15:30:38.910 [P2P1]  INFO    stacktrace      src/common/stack_trace.cpp:172      [10] /usr/bin/monerod(+0x33239a) [0x58cf1a4d739a]
2024-10-12 15:30:38.910 [P2P1]  INFO    stacktrace      src/common/stack_trace.cpp:172      [11]  0x10f63) [0x7ee915fcbf63]:_thread.so.1.86.0(+0x10f63) [0x7ee915fcbf63]
2024-10-12 15:30:38.910 [P2P1]  INFO    stacktrace      src/common/stack_trace.cpp:172      [12] /usr/lib/libc.so.6(+0x9439d) [0x7ee9154a339d]
2024-10-12 15:30:38.910 [P2P1]  INFO    stacktrace      src/common/stack_trace.cpp:172      [13] /usr/lib/libc.so.6(+0x11949c) [0x7ee91552849c]
2024-10-12 15:30:38.910 [P2P1]  INFO    stacktrace      src/common/stack_trace.cpp:172
2024-10-12 15:30:38.910 [P2P2]  INFO    stacktrace      src/common/stack_trace.cpp:133  Exception: boost::wrapexcept<boost::bad_weak_ptr>
2024-10-12 15:30:38.910 [P2P2]  INFO    stacktrace      src/common/stack_trace.cpp:134  Unwound call stack:
2024-10-12 15:30:38.910 [P2P2]  INFO    stacktrace      src/common/stack_trace.cpp:172      [1] /usr/bin/monerod(+0x10d348) [0x58cf1a2b2348]
2024-10-12 15:30:38.910 [P2P2]  INFO    stacktrace      src/common/stack_trace.cpp:172      [2] /usr/bin/monerod(+0x7f2a9) [0x58cf1a2242a9]
2024-10-12 15:30:38.910 [P2P2]  INFO    stacktrace      src/common/stack_trace.cpp:172      [3] /usr/bin/monerod(+0x2f59d2) [0x58cf1a49a9d2]
2024-10-12 15:30:38.910 [P2P2]  INFO    stacktrace      src/common/stack_trace.cpp:172      [4] /usr/bin/monerod(+0x3237f2) [0x58cf1a4c87f2]
2024-10-12 15:30:38.910 [P2P2]  INFO    stacktrace      src/common/stack_trace.cpp:172      [5] /usr/bin/monerod(+0x671000) [0x58cf1a816000]
2024-10-12 15:30:38.910 [P2P2]  INFO    stacktrace      src/common/stack_trace.cpp:172      [6] /usr/bin/monerod(+0x30ac5a) [0x58cf1a4afc5a]
2024-10-12 15:30:38.910 [P2P2]  INFO    stacktrace      src/common/stack_trace.cpp:172      [7] /usr/bin/monerod(+0x372448) [0x58cf1a517448]
2024-10-12 15:30:38.910 [P2P2]  INFO    stacktrace      src/common/stack_trace.cpp:172      [8] /usr/bin/monerod(+0x1610b5) [0x58cf1a3060b5]
2024-10-12 15:30:38.910 [P2P2]  INFO    stacktrace      src/common/stack_trace.cpp:172      [9] /usr/bin/monerod(+0x5c6a15) [0x58cf1a76ba15]
2024-10-12 15:30:38.910 [P2P2]  INFO    stacktrace      src/common/stack_trace.cpp:172      [10] /usr/bin/monerod(+0x33239a) [0x58cf1a4d739a]
2024-10-12 15:30:38.910 [P2P2]  INFO    stacktrace      src/common/stack_trace.cpp:172      [11]  0x10f63) [0x7ee915fcbf63]:_thread.so.1.86.0(+0x10f63) [0x7ee915fcbf63]
2024-10-12 15:30:38.910 [P2P2]  INFO    stacktrace      src/common/stack_trace.cpp:172      [12] /usr/lib/libc.so.6(+0x9439d) [0x7ee9154a339d]
2024-10-12 15:30:38.910 [P2P2]  INFO    stacktrace      src/common/stack_trace.cpp:172      [13] /usr/lib/libc.so.6(+0x11949c) [0x7ee91552849c]
2024-10-12 15:30:38.910 [P2P2]  INFO    stacktrace      src/common/stack_trace.cpp:172
2024-10-12 15:30:38.910 [P2P6]  INFO    stacktrace      src/common/stack_trace.cpp:133  Exception: boost::wrapexcept<boost::bad_weak_ptr>
2024-10-12 15:30:38.910 [P2P6]  INFO    stacktrace      src/common/stack_trace.cpp:134  Unwound call stack:
2024-10-12 15:30:38.910 [P2P6]  INFO    stacktrace      src/common/stack_trace.cpp:172      [1] /usr/bin/monerod(+0x10d348) [0x58cf1a2b2348]
2024-10-12 15:30:38.910 [P2P6]  INFO    stacktrace      src/common/stack_trace.cpp:172      [2] /usr/bin/monerod(+0x7f2a9) [0x58cf1a2242a9]
2024-10-12 15:30:38.910 [P2P6]  INFO    stacktrace      src/common/stack_trace.cpp:172      [3] /usr/bin/monerod(+0x2f59d2) [0x58cf1a49a9d2]
2024-10-12 15:30:38.910 [P2P6]  INFO    stacktrace      src/common/stack_trace.cpp:172      [4] /usr/bin/monerod(+0x30b2e3) [0x58cf1a4b02e3]
2024-10-12 15:30:38.910 [P2P6]  INFO    stacktrace      src/common/stack_trace.cpp:172      [5] /usr/bin/monerod(+0x3239e7) [0x58cf1a4c89e7]
2024-10-12 15:30:38.910 [P2P6]  INFO    stacktrace      src/common/stack_trace.cpp:172      [6] /usr/bin/monerod(+0x671000) [0x58cf1a816000]
2024-10-12 15:30:38.910 [P2P6]  INFO    stacktrace      src/common/stack_trace.cpp:172      [7] /usr/bin/monerod(+0x30ac5a) [0x58cf1a4afc5a]
2024-10-12 15:30:38.910 [P2P6]  INFO    stacktrace      src/common/stack_trace.cpp:172      [8] /usr/bin/monerod(+0x372448) [0x58cf1a517448]
2024-10-12 15:30:38.910 [P2P6]  INFO    stacktrace      src/common/stack_trace.cpp:172      [9] /usr/bin/monerod(+0x1610b5) [0x58cf1a3060b5]
2024-10-12 15:30:38.910 [P2P6]  INFO    stacktrace      src/common/stack_trace.cpp:172      [10] /usr/bin/monerod(+0x5c6a15) [0x58cf1a76ba15]
2024-10-12 15:30:38.910 [P2P6]  INFO    stacktrace      src/common/stack_trace.cpp:172      [11] /usr/bin/monerod(+0x33239a) [0x58cf1a4d739a]
2024-10-12 15:30:38.910 [P2P6]  INFO    stacktrace      src/common/stack_trace.cpp:172      [12]  0x10f63) [0x7ee915fcbf63]:_thread.so.1.86.0(+0x10f63) [0x7ee915fcbf63]
2024-10-12 15:30:38.910 [P2P6]  INFO    stacktrace      src/common/stack_trace.cpp:172      [13] /usr/lib/libc.so.6(+0x9439d) [0x7ee9154a339d]
2024-10-12 15:30:38.910 [P2P6]  INFO    stacktrace      src/common/stack_trace.cpp:172      [14] /usr/lib/libc.so.6(+0x11949c) [0x7ee91552849c]
2024-10-12 15:30:38.910 [P2P6]  INFO    stacktrace      src/common/stack_trace.cpp:172
2024-10-12 15:30:41.730 [P2P0]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1696    Synced 3142536/3257500 (96%, 114964 left)
2024-10-12 15:30:49.469 [P2P9]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:406     [141.255.166.195:39756 INC] Sync data returned a new top block candidate: 3142536 -> 3257501 [Your node is 114965 blocks (5.2 months) behind]
2024-10-12 15:30:49.469 [P2P9]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:406     SYNCHRONIZATION started
2024-10-12 15:31:06.209 [P2P0]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1696    Synced 3142556/3257501 (96%, 114945 left, 3% of total synced, estimated 3.0 days left)
```



# Discussion History
## selsta | 2024-10-13T13:51:37+00:00
This is a known issue but should not cause any troubles during sync apart from verbose stack traces.

Sync slowing down towards end is expected.

## selsta | 2024-10-13T13:54:38+00:00
https://github.com/monero-project/monero/issues/8341

## selsta | 2024-10-17T23:29:49+00:00
Closing as this is a duplicate.

# Action History
- Created by: divinitus | 2024-10-12T15:36:12+00:00
- Closed at: 2024-10-17T23:29:49+00:00
