---
title: Cuprate Crash Starting RPC Server
source_url: https://github.com/Cuprate/cuprate/issues/522
author: ACK-J
assignees: []
labels:
- C-bug
created_at: '2025-07-30T00:38:48+00:00'
updated_at: '2025-07-30T00:38:48+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
## Bug
This isn't a significant bug but I found that when port 18081 is in use before starting cuprated the program aborts.

## Expected behavior
Exit gracefully with an error message

## Steps to reproduce
Example:

1. run monerod
2. start cuprated

# Source Code Location
https://github.com/Cuprate/cuprate/blob/97e539559a244609057c3593287e29d910941227/binaries/cuprated/src/rpc/server.rs#L84-L87

## Verbose Backtrace
```
thread 'cuprated-tokio' panicked at binaries/cuprated/src/rpc/server.rs:87:18:
called `Result::unwrap()` on an `Err` value: Address already in use (os error 98)
stack backtrace:
   0:     0x58d6980c1022 - std::backtrace_rs::backtrace::libunwind::trace::h74680e970b6e0712
                               at /rustc/6b00bc3880198600130e1cf62b8f8a93494488cc/library/std/src/../../backtrace/src/backtrace/libunwind.rs:117:9
   1:     0x58d6980c1022 - std::backtrace_rs::backtrace::trace_unsynchronized::ha3bf590e3565a312
                               at /rustc/6b00bc3880198600130e1cf62b8f8a93494488cc/library/std/src/../../backtrace/src/backtrace/mod.rs:66:14
   2:     0x58d6980c1022 - std::sys::backtrace::_print_fmt::hcf16024cbdd6c458
                               at /rustc/6b00bc3880198600130e1cf62b8f8a93494488cc/library/std/src/sys/backtrace.rs:66:9
   3:     0x58d6980c1022 - <std::sys::backtrace::BacktraceLock::print::DisplayBacktrace as core::fmt::Display>::fmt::h46a716bba2450163
                               at /rustc/6b00bc3880198600130e1cf62b8f8a93494488cc/library/std/src/sys/backtrace.rs:39:26
   4:     0x58d697f6da03 - core::fmt::rt::Argument::fmt::ha695e732309707b7
                               at /rustc/6b00bc3880198600130e1cf62b8f8a93494488cc/library/core/src/fmt/rt.rs:181:76
   5:     0x58d697f6da03 - core::fmt::write::h275e5980d7008551
                               at /rustc/6b00bc3880198600130e1cf62b8f8a93494488cc/library/core/src/fmt/mod.rs:1446:25
   6:     0x58d6980c0baf - std::io::default_write_fmt::hdc4119be3eb77042
                               at /rustc/6b00bc3880198600130e1cf62b8f8a93494488cc/library/std/src/io/mod.rs:639:11
   7:     0x58d6980c0baf - std::io::Write::write_fmt::h561a66a0340b6995
                               at /rustc/6b00bc3880198600130e1cf62b8f8a93494488cc/library/std/src/io/mod.rs:1914:13
   8:     0x58d6980c0e83 - std::sys::backtrace::BacktraceLock::print::hafb9d5969adc39a0
                               at /rustc/6b00bc3880198600130e1cf62b8f8a93494488cc/library/std/src/sys/backtrace.rs:42:9
   9:     0x58d6980c08a1 - std::panicking::default_hook::{{closure}}::hae2e97a5c4b2b777
  10:     0x58d6980c08a1 - std::panicking::default_hook::h3db1b505cfc4eb79
                               at /rustc/6b00bc3880198600130e1cf62b8f8a93494488cc/library/std/src/panicking.rs:327:9
  11:     0x58d6980c08a1 - std::panicking::rust_panic_with_hook::h409da73ddef13937
                               at /rustc/6b00bc3880198600130e1cf62b8f8a93494488cc/library/std/src/panicking.rs:833:13
  12:     0x58d6980f2b68 - std::panicking::begin_panic_handler::{{closure}}::h159b61b27f96a9c2
                               at /rustc/6b00bc3880198600130e1cf62b8f8a93494488cc/library/std/src/panicking.rs:706:13
  13:     0x58d6980f2ac9 - std::sys::backtrace::__rust_end_short_backtrace::h5b56844d75e766fc
                               at /rustc/6b00bc3880198600130e1cf62b8f8a93494488cc/library/std/src/sys/backtrace.rs:168:18
  14:     0x58d6980f31fc - __rustc[4794b31dd7191200]::rust_begin_unwind
                               at /rustc/6b00bc3880198600130e1cf62b8f8a93494488cc/library/std/src/panicking.rs:697:5
  15:     0x58d697c772ff - core::panicking::panic_fmt::hc8737e8cca20a7c8
                               at /rustc/6b00bc3880198600130e1cf62b8f8a93494488cc/library/core/src/panicking.rs:75:14
  16:     0x58d697c777c5 - core::result::unwrap_failed::h727108008d9f4c9b
                               at /rustc/6b00bc3880198600130e1cf62b8f8a93494488cc/library/core/src/result.rs:1732:5
  17:     0x58d697ed698a - cuprated::rpc::server::init_rpc_servers::{{closure}}::h6b3fdea8060dff84
  18:     0x58d697e0097b - tokio::runtime::task::raw::poll::h07a99a97b89a7241
  19:     0x58d69810ec19 - tokio::runtime::scheduler::multi_thread::worker::Context::run_task::he861baf18fbc4d61
  20:     0x58d698111640 - tokio::runtime::task::raw::poll::hccc0f3de358fea29
  21:     0x58d698102634 - std::sys::backtrace::__rust_begin_short_backtrace::hb524e0ab9b572891
  22:     0x58d698105dcb - core::ops::function::FnOnce::call_once{{vtable.shim}}::h593ae1e7ec2067f9
  23:     0x58d6980f34fb - <alloc::boxed::Box<F,A> as core::ops::function::FnOnce<Args>>::call_once::he4962534b56a5929
                               at /rustc/6b00bc3880198600130e1cf62b8f8a93494488cc/library/alloc/src/boxed.rs:1966:9
  24:     0x58d6980f34fb - <alloc::boxed::Box<F,A> as core::ops::function::FnOnce<Args>>::call_once::h95af12d5a868b9d0
                               at /rustc/6b00bc3880198600130e1cf62b8f8a93494488cc/library/alloc/src/boxed.rs:1966:9
  25:     0x58d6980f34fb - std::sys::pal::unix::thread::Thread::new::thread_start::h1822d22fde68314f
                               at /rustc/6b00bc3880198600130e1cf62b8f8a93494488cc/library/std/src/sys/pal/unix/thread.rs:97:17
  26:     0x74a1b6294ac3 - <unknown>
  27:     0x74a1b6326850 - <unknown>
  28:                0x0 - <unknown>
Aborted (core dumped)
```

# Discussion History
# Action History
- Created by: ACK-J | 2025-07-30T00:38:48+00:00
