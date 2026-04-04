---
title: 'tests: "libwallet_api_t" received signal SIGSEGV, Segmentation fault'
source_url: https://github.com/monero-project/monero/issues/1240
author: anonimal
assignees: []
labels: []
created_at: '2016-10-21T06:29:30+00:00'
updated_at: '2018-01-08T13:02:57+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
As seen in the [waterfall](https://build.getmonero.org/waterfall):

`make release-test`

1st run:

``` bash
$ gdb ./libwallet_api_tests
```

```
Thread 42 "libwallet_api_t" received signal SIGSEGV, Segmentation fault.
[Switching to Thread 0x7fff9f7fe700 (LWP 7983)]
0x000000000050803b in Bitmonero::WalletImpl::errorString[abi:cxx11]() const ()
(gdb) bt
#0  0x000000000050803b in Bitmonero::WalletImpl::errorString[abi:cxx11]() const ()
#1  0x0000000000517335 in Bitmonero::WalletImpl::doRefresh() ()
#2  0x00000000005077dd in Bitmonero::WalletImpl::refreshThreadFunc() ()
#3  0x00007ffff63fa976 in ?? () from /usr/lib/libboost_thread.so.1.61.0
#4  0x00007ffff5617454 in start_thread () from /usr/lib/libpthread.so.0
#5  0x00007ffff535a7df in clone () from /usr/lib/libc.so.6
```

2nd run:

``` bash
$ gdb ./libwallet_api_tests
```

```
Thread 42 "libwallet_api_t" received signal SIGSEGV, Segmentation fault.
[Switching to Thread 0x7fff9f7fe700 (LWP 8195)]
0x000000000051729d in Bitmonero::WalletImpl::doRefresh() ()
(gdb) bt
#0  0x000000000051729d in Bitmonero::WalletImpl::doRefresh() ()
#1  0x00000000005077dd in Bitmonero::WalletImpl::refreshThreadFunc() ()
#2  0x00007ffff63fa976 in ?? () from /usr/lib/libboost_thread.so.1.61.0
#3  0x00007ffff5617454 in start_thread () from /usr/lib/libpthread.so.0
#4  0x00007ffff535a7df in clone () from /usr/lib/libc.so.6
```

Notes:
- ^ above is on Arch, gcc 6.2.1
- possibly related? 62b3708ea5b6a2ee45491f632d2c753eae8a00ee
- `make debug-test` won't produce segfault when ran _with_ gdb but will produce segfault otherwise


# Discussion History
## danrmiller | 2016-10-31T04:23:57+00:00
A new "Debug" step was added to the daily test builders to show the backtrace.
For example, see https://build.getmonero.org/builders/monero-tests-ubuntu-16.04-amd64/builds/10/steps/Debug/logs/stdio


## dEBRUYNE-1 | 2018-01-08T13:02:56+00:00
@anonimal Is this still valid?

# Action History
- Created by: anonimal | 2016-10-21T06:29:30+00:00
