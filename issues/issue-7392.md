---
title: Building For M1 Macs Natively
source_url: https://github.com/monero-project/monero/issues/7392
author: jbrot
assignees: []
labels: []
created_at: '2021-02-21T00:51:20+00:00'
updated_at: '2021-03-30T07:42:07+00:00'
type: issue
status: closed
closed_at: '2021-03-30T02:38:29+00:00'
---

# Original Description
HI! I just compiled the repo on the new Mac Mini with M1 processor, and I'd like to report on my experience.

## Compiling

The root `CMakeLists.txt` is incompatible with the ARM Macs, because of [lines 486 to 494 of CMakeLists.txt](https://github.com/monero-project/monero/blob/master/CMakeLists.txt#L486):
```cmake
if (APPLE AND NOT IOS)
  set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -march=x86-64 -fvisibility=default -std=c++11")
  if (NOT OPENSSL_ROOT_DIR)
      EXECUTE_PROCESS(COMMAND brew --prefix openssl
        OUTPUT_VARIABLE OPENSSL_ROOT_DIR
        OUTPUT_STRIP_TRAILING_WHITESPACE)
    message(STATUS "Using OpenSSL found at ${OPENSSL_ROOT_DIR}")
  endif()
endif()
``` 
The problem here is that this adds `-march=x86-64` to `CMAKE_CXX_FLAGS`, while the M1 is an ARM processor. I commented out this block and the repo compiled successfully. I suspect just commenting out [line 487](https://github.com/monero-project/monero/blob/master/CMakeLists.txt#L487) would be sufficient, but I don't know if this line is needed under other circumstances. Hopefully someone more familiar with the project will be able to weigh in.

Furthermore, `README.md` suggests ZeroMQ 3.0 should be installed, but this resulted in a cryptic templating error. The error was ultimately caused because the function `zmq_send_const` was not present in my header files. I then installed ZeroMQ 4.3.4 and the repo compiled successfully. This suggests that the information in `README.md` is outdated.

## Testing

I started running the unit tests, ~~but skipped `core_tests` initially in the interest of time~~. I saw two failures:
1. [check_missing_rpc_methods](https://github.com/monero-project/monero/blob/master/tests/functional_tests/CMakeLists.txt#L78) failed. Further investigation revealed this was because I did not have the python package `requests` installed system-wide. I noticed that `functional_tests_rpc` above was only enabled when `requests` was found. My experience suggests that `check_missing_rpc_methods` should probably be gated under this condition, as well. I think `requests` should also be listed as an optional dependency in `README.md`.
2. The test suite `unit_tests` segfaulted on `zmq.read_write`. I'm not sure what to make of this, since I installed a different version of ZeroMQ then listed in the README. Perhaps a version other than the two I tried is needed to make this succeed.

I am currently running `core_tests`, and it appears to be going well so far. I will report back if it does end up failing. **Edit:** `core_tests` completed successfully.

## Running `monerod`

I've been running `monerod` for 30 minutes or so now, and have synchronized 3% of the block chain. ~~Everything appears to be going smoothly so far~~---so perhaps the zmq failure above is inconsequential. I'm very new to monero, so I'll be playing around with additional commands and report back if I experience any relevant issues.

### Edit: Kernel Panic
I'm now further along through the synchronization process and have run into an interesting issue. Once my `data.mdb` file reached a size of 49567 MiB , database resizes result in a kernel panic _when `monerod` is running as a demon_ (i.e., the 49567MiB to 56273 MiB resize resulted in a kernel panic, and all subsequent resizes were observed to result in a panic). However, when I'm running `monerod` interactively in my terminal, the resize proceeds without issue. I'm not sure what to make of this.

# Discussion History
## moneromooo-monero | 2021-02-23T19:12:53+00:00
Tests should not crash with a recent libzmq (assuming it's not a bug in libzmq, but that's unlikely). If you can get a stack trace (ie, from a core file), it'd help.

A kernel panic is almost certainly a kernel bug.


## mj-xmr | 2021-03-05T09:30:07+00:00
I will try ro create a CI step for ARM Mac.

## mj-xmr | 2021-03-05T19:53:26+00:00
I failed in creating a CI step for ARM Mac. The reason is, that libiconv doesn't seem to want to cooperate when I want to cross compile it. This must be the reason, why neither `arm-apple-darwin11` nor `aarch64-apple-darwin11` are advertised on the `depends` cross compilation suite.

What I can offer to you is opening the above 2 PRs and making sure, that the CMake change, that you requested, doesn't crash the currently used Mac builds on Monero's CI (one is done on the real hardware and the other is being cross compiled via `depends` package)

## mj-xmr | 2021-03-06T06:29:37+00:00
@jbrot : Could you please try compiling [this branch](https://github.com/mj-xmr/monero/tree/enable-mac-on-arm) on your M1 and tell if it went fine?

## jbrot | 2021-03-06T19:23:54+00:00
> @jbrot : Could you please try compiling [this branch](https://github.com/mj-xmr/monero/tree/enable-mac-on-arm) on your M1 and tell if it went fine?

Just tested it out and it worked! Thanks for taking the initiative to make the PR! 😄 

## jbrot | 2021-03-06T20:38:02+00:00
> Tests should not crash with a recent libzmq (assuming it's not a bug in libzmq, but that's unlikely). If you can get a stack trace (ie, from a core file), it'd help.

When I was validating @mj-xmr 's branch above, I noticed that this test no longer crashed. Some further investigation revealed that adding the `-fvisibility=default` flag is what caused the issue to appear. Specifically, the issue was because I commented out the full line
```cmake
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -march=x86-64 -fvisibility=default -std=c++11")
```
instead of just removing `-march=x86-64` like in mj-xmr 's PR.

## mj-xmr | 2021-03-06T21:28:56+00:00
This is awesome news! Thanks for testing. 

Merging the branch might take some time and discussion though. Please be patient.

## mj-xmr | 2021-03-30T07:40:37+00:00
@jbrot : Merged to master.

# Action History
- Created by: jbrot | 2021-02-21T00:51:20+00:00
- Closed at: 2021-03-30T02:38:29+00:00
