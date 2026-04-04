---
title: Cross compile for win64 broken
source_url: https://github.com/monero-project/monero/issues/8409
author: agowa
assignees: []
labels: []
created_at: '2022-06-28T07:17:10+00:00'
updated_at: '2022-09-23T15:24:10+00:00'
type: issue
status: closed
closed_at: '2022-09-23T15:24:10+00:00'
---

# Original Description
Two issues so far for cross-compiling via `make depends target=x86_64-w64-mingw32` on Ubuntu.

1. Zeromq after version 4.3.1 doesn't properly compile (needs to be downgraded to 4.3.1 to compile, tested with 4.3.4)
```
src/condition_variable.hpp:129:10: error: ‘condition_variable_any’ in namespace ‘std’ does not name a type
  129 |     std::condition_variable_any _cv;
      |          ^~~~~~~~~~~~~~~~~~~~~~
src/condition_variable.hpp:98:1: note: ‘std::condition_variable_any’ is defined in header ‘<condition_variable>’; did you forget to ‘#include <condition_variable>’?
   97 | #include <condition_variable>
  +++ |+#include <condition_variable>
   98 |
src/condition_variable.hpp: In member function ‘int zmq::condition_variable_t::wait(zmq::mutex_t*, int)’:
src/condition_variable.hpp:111:13: error: ‘_cv’ was not declared in this scope
  111 |             _cv.wait (
      |             ^~~
src/condition_variable.hpp:113:20: error: ‘_cv’ was not declared in this scope
  113 |         } else if (_cv.wait_for (*mutex_, std::chrono::milliseconds (timeout_))
      |                    ^~~
src/condition_variable.hpp:114:28: error: ‘std::cv_status’ has not been declared
  114 |                    == std::cv_status::timeout) {
      |                            ^~~~~~~~~
src/condition_variable.hpp: In member function ‘void zmq::condition_variable_t::broadcast()’:
src/condition_variable.hpp:125:9: error: ‘_cv’ was not declared in this scope
  125 |         _cv.notify_all ();
      |         ^~~
make[2]: *** [Makefile:5581: src/libzmq_la-mailbox_safe.lo] Error 1
make[2]: Leaving directory '/home/user/monero/contrib/depends/work/build/x86_64-w64-mingw32/zeromq/4.3.4-5989d77c9e2'
make[1]: *** [funcs.mk:266: /home/user/monero/contrib/depends/work/build/x86_64-w64-mingw32/zeromq/4.3.4-5989d77c9e2/./.stamp_built] Error 2
make[1]: Leaving directory '/home/user/monero/contrib/depends'
make: *** [Makefile:50: depends] Error 2
```
2. protobuf fails to compile with `./google/protobuf/stubs/mutex.h:58:8: error: ‘mutex’ in namespace ‘std’ does not name a type`
```
user@ubuntu:~/monero$ make depends target=x86_64-w64-mingw32
cd contrib/depends && make HOST=x86_64-w64-mingw32 && cd ../.. && mkdir -p build/x86_64-w64-mingw32/release
make[1]: Entering directory '/home/user/monero/contrib/depends'
Building protobuf...
make[2]: Entering directory '/home/user/monero/contrib/depends/work/build/x86_64-w64-mingw32/protobuf/3.6.1-8b61dce8fde/src'
/bin/bash ../libtool  --tag=CXX   --mode=compile x86_64-w64-mingw32-g++ -DHAVE_CONFIG_H -I. -I..   -I/home/user/monero/contrib/depends/x86_64-w64-mingw32/include -pthread -DHAVE_PTHREAD=1  -Wall -Wno-sign-compare  -std=c++11 -c -o google/protobuf/stubs/bytestream.lo google/protobuf/stubs/bytestream.cc
libtool: compile:  x86_64-w64-mingw32-g++ -DHAVE_CONFIG_H -I. -I.. -I/home/user/monero/contrib/depends/x86_64-w64-mingw32/include -pthread -DHAVE_PTHREAD=1 -Wall -Wno-sign-compare -std=c++11 -c google/protobuf/stubs/bytestream.cc -o google/protobuf/stubs/bytestream.o
In file included from ./google/protobuf/stubs/common.h:52,
                 from ./google/protobuf/stubs/bytestream.h:56,
                 from google/protobuf/stubs/bytestream.cc:31:
./google/protobuf/stubs/mutex.h:58:8: error: ‘mutex’ in namespace ‘std’ does not name a type
   58 |   std::mutex mu_;
      |        ^~~~~
./google/protobuf/stubs/mutex.h:34:1: note: ‘std::mutex’ is defined in header ‘<mutex>’; did you forget to ‘#include <mutex>’?
   33 | #include <mutex>
  +++ |+#include <mutex>
   34 |
./google/protobuf/stubs/mutex.h: In member function ‘void google::protobuf::internal::WrappedMutex::Lock()’:
./google/protobuf/stubs/mutex.h:51:17: error: ‘mu_’ was not declared in this scope
   51 |   void Lock() { mu_.lock(); }
      |                 ^~~
./google/protobuf/stubs/mutex.h: In member function ‘void google::protobuf::internal::WrappedMutex::Unlock()’:
./google/protobuf/stubs/mutex.h:52:19: error: ‘mu_’ was not declared in this scope
   52 |   void Unlock() { mu_.unlock(); }
      |                   ^~~
make[2]: *** [Makefile:3975: google/protobuf/stubs/bytestream.lo] Error 1
make[2]: Leaving directory '/home/user/monero/contrib/depends/work/build/x86_64-w64-mingw32/protobuf/3.6.1-8b61dce8fde/src'
make[1]: *** [funcs.mk:266: /home/user/monero/contrib/depends/work/build/x86_64-w64-mingw32/protobuf/3.6.1-8b61dce8fde/./.stamp_built] Error 2
make[1]: Leaving directory '/home/user/monero/contrib/depends'
make: *** [Makefile:50: depends] Error 2
```

# Discussion History
## selsta | 2022-06-28T13:41:53+00:00
Which Ubuntu version are you using?

We cross compile every single commit to Windows for testing purposes and there are no issues that I'm aware of, see https://github.com/monero-project/monero/runs/7081500633 from 16h ago.

## agowa | 2022-06-28T16:53:48+00:00
```
PRETTY_NAME="Ubuntu 21.10"
NAME="Ubuntu"
VERSION_ID="21.10"
VERSION="21.10 (Impish Indri)"
VERSION_CODENAME=impish
ID=ubuntu
ID_LIKE=debian
HOME_URL="https://www.ubuntu.com/"
SUPPORT_URL="https://help.ubuntu.com/"
BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"
PRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy"
UBUNTU_CODENAME=impish
```

## selsta | 2022-06-28T17:10:46+00:00
I'll run the cross compile CI job on Ubuntu 22.04 and report back if it works. We currently use ~~20.04~~ 18.04 for CI.

## hyc | 2022-06-28T18:14:54+00:00
and just for reference, the official binaries are built on a Ubuntu 18.04 base.

## selsta | 2022-06-28T23:27:20+00:00
@agowa338 Do you have a system with Ubuntu 18.04 or 20.04? Seems like for 22.04 at least some tweaks are necessary before cross compiling works.

## agowa | 2022-06-29T02:30:30+00:00
Currently? No, but I could just use a docker container or spin up a VM.

Could you please add a disclaimer to the cross-compile section within the readme? Just knowing that it is currently Ubuntu version dependent does already help.

## hyc | 2022-06-29T10:16:25+00:00
>No, but I could just use a docker container or spin up a VM.

Indeed. Just use `contrib/gitian/dockrun.sh`

## Basement-Science | 2022-07-31T20:41:20+00:00
Same problem on Debian 10 and monero v0.18.0.0
Regular compilation for linux works.

## duggavo | 2022-09-22T19:12:43+00:00
Same problem on Ubuntu 22

## selsta | 2022-09-22T19:14:26+00:00
Something doesn't make sense here since I got it to cross compile on a fresh 22.04 VM: https://github.com/selsta/monero/actions/runs/3091744278/jobs/5002197898

## selsta | 2022-09-23T15:24:10+00:00
https://github.com/monero-project/monero/pull/8590

# Action History
- Created by: agowa | 2022-06-28T07:17:10+00:00
- Closed at: 2022-09-23T15:24:10+00:00
