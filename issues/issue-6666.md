---
title: Device and cryptonote_basic cyclic dependency, debug build fails
source_url: https://github.com/monero-project/monero/issues/6666
author: ph4r05
assignees: []
labels: []
created_at: '2020-06-19T10:54:40+00:00'
updated_at: '2021-07-27T20:52:17+00:00'
type: issue
status: closed
closed_at: '2021-07-27T20:52:17+00:00'
---

# Original Description
Debug compilation (with shared lib compilation) fails due to the: 

```
[ 95%] Linking CXX shared library libdevice.dylib
Undefined symbols for architecture x86_64:
  "cryptonote::get_transaction_prefix_hash(cryptonote::transaction_prefix const&, crypto::hash&)", referenced from:
      hw::core::device_default::get_transaction_prefix_hash(cryptonote::transaction_prefix const&, crypto::hash&) in device_default.cpp.o
ld: symbol(s) not found for architecture x86_64
```

The problem is that the `device` module contains `device_default` and `device_ledger` while those are using `cryptonote_basic` functions. `cryptonote_basic` depends on the `device` module (probably due to the interfaces defined in the module). So `device` cannot depend on the `cryptonote_basic` to fix the compilation error as the cyclic dependency would be created.

A similar problem happened to me several times. It would be maybe better to leave only basic interfaces in the `device` and separate implementations to a new module which could depend on the `cryptonote_basic` and other modules.

What do you think @moneromooo-monero @selsta ?
(I am aware that statical linking is a valid workaround)


# Discussion History
## moneromooo-monero | 2020-06-19T11:28:52+00:00
Is this a new change ?

## ph4r05 | 2020-06-19T12:15:43+00:00
I am getting this error on master b3d6382d406e660b1d4ad503d63bfae89056925c on `make debug`. Can you pls reproduce it?

## moneromooo-monero | 2020-06-19T12:34:55+00:00
Unlikely, it only showed up on Mac before.

## ph4r05 | 2020-06-24T10:37:53+00:00
Ah interesting. It is happening on Mac/clang (`Apple clang version 11.0.3 (clang-1103.0.32.62)`), true. I've just checked that GCC 8.3.0 passes without problems.

## sanderfoobar | 2020-07-21T00:17:09+00:00
can reproduce on master 5d850dde99ca282d2c6f9a1b1eb00a3812cb15be, `-DCMAKE_BUILD_TYPE=Debug`, `Apple LLVM version 10.0.1 (clang-1001.0.46.3)`

## KamiD | 2020-10-19T03:26:29+00:00
it reproduced on https://github.com/monero-project/monero/commit/76cc82c29234fc2805f936f0fc53d48acc9cedf7 under macos 10.15.3, gcc version is 4.2.1

## KamiD | 2020-10-22T09:09:54+00:00
it still reproduced even i upgrade gcc to 7.2.5

# Action History
- Created by: ph4r05 | 2020-06-19T10:54:40+00:00
- Closed at: 2021-07-27T20:52:17+00:00
