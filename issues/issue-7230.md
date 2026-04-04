---
title: __AFL_LOOP macro used as a function name
source_url: https://github.com/monero-project/monero/issues/7230
author: unseddd
assignees: []
labels: []
created_at: '2020-12-30T02:26:45+00:00'
updated_at: '2020-12-30T02:53:34+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
The `__AFL_LOOP` macro is used as a function name in [tests/fuzz/fuzzer.cpp](https://github.com/monero-project/monero/blob/master/tests/fuzz/fuzzer.cpp#L39)

This causes fuzz tests to not compile when not using `OSS_FUZZ` builds, since __AFL_LOOP is defined in [aflplusplus](https://github.com/AFLplusplus/AFLplusplus/blob/stable/src/afl-cc.c#L834) and [afl](https://github.com/google/AFL/blob/fab1ca5ed7e3552833a18fc2116d33a9241699bc/llvm_mode/afl-clang-fast.c#L251).

# Discussion History
# Action History
- Created by: unseddd | 2020-12-30T02:26:45+00:00
