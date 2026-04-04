---
title: cannot compile last version
source_url: https://github.com/monero-project/monero/issues/158
author: Atrides
assignees: []
labels: []
created_at: '2014-09-24T23:16:10+00:00'
updated_at: '2014-09-25T10:48:33+00:00'
type: issue
status: closed
closed_at: '2014-09-25T10:48:33+00:00'
---

# Original Description
Hi, I have compiled today already two times without problems, but cannot currently last version:

```
-- The C compiler identification is GNU 4.8.2
-- The CXX compiler identification is GNU 4.8.2
-- Check for working C compiler: /usr/bin/cc
-- Check for working C compiler: /usr/bin/cc -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working CXX compiler: /usr/bin/c++
-- Check for working CXX compiler: /usr/bin/c++ -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Could not find DEVELOPER_LOCAL_TOOLS in env
-- BOOST_IGNORE_SYSTEM_PATHS defaults to OFF
-- Looking for include file pthread.h
-- Looking for include file pthread.h - found
-- Looking for pthread_create
-- Looking for pthread_create - not found
-- Looking for pthread_create in pthreads
-- Looking for pthread_create in pthreads - not found
-- Looking for pthread_create in pthread
-- Looking for pthread_create in pthread - found
-- Found Threads: TRUE  
Looking for libunbound
CMake Error at cmake/FindUnbound.cmake:52 (MESSAGE):
  Could not find unbound library
Call Stack (most recent call first):
  CMakeLists.txt:89 (find_package)


-- Configuring incomplete, errors occurred!
See also "/tmp/bitmonero-master/build/release/CMakeFiles/CMakeOutput.log".
See also "/tmp/bitmonero-master/build/release/CMakeFiles/CMakeError.log".
make: *** [cmake-release] Fehler 1
```

Files:
http://dwarfpool.com/static/xmr/CMakeError.log
http://dwarfpool.com/static/xmr/CMakeOutput.log


# Discussion History
## fluffypony | 2014-09-24T23:18:02+00:00
The CMake output gives you some indication when it says `Looking for libunbound` and `Could not find unbound library` - we have a new dependency:)

Per the updated README -

Dependencies: GCC 4.7.3 or later, CMake 2.8.6 or later, Unbound 1.4.16 or later, and Boost 1.53 or later (except 1.54, more details here).

Depending on your build environment, you may find that you require Unbound 1.4.22


## greatwolf | 2014-09-25T08:28:13+00:00
Can you include unbound under extern so everything is self-contained so we don't have to hunt for another dependency? For example, if cmake cannot find libunbound on the host system it's building on, it should fallback on its own copy of libunbound provided in `bitmonero.git/external`.


## fluffypony | 2014-09-25T08:35:47+00:00
@greatwolf Dependencies really shouldn't live in the source tree (except in edge cases where we're modifying an underlying dependency, in which case we should be using git submodule and not leaving it loose in the source tree as it currently is with miniupnpc).

If, for instance, we switch to Qt's signals and slots, you don't want the whole of QtCore in the source tree;)

I'm open to arguments against this methodology, of course.


## Atrides | 2014-09-25T10:48:33+00:00
That solves problem

```
aptitude install libunbound-dev
```


# Action History
- Created by: Atrides | 2014-09-24T23:16:10+00:00
- Closed at: 2014-09-25T10:48:33+00:00
