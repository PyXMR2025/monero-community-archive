---
title: v0.13.0.2 Docker image does not build
source_url: https://github.com/monero-project/monero/issues/4582
author: EmbeddedAndroid
assignees: []
labels: []
created_at: '2018-10-13T16:34:35+00:00'
updated_at: '2018-10-24T12:15:05+00:00'
type: issue
status: closed
closed_at: '2018-10-15T11:33:12+00:00'
---

# Original Description
I tried to build the v0.13.0.2 tag with Docker yesterday and found an issue with submodules:

```
+ rm -rf build
+ [ -z  ]
+ nproc
+ make -j1 release-static

mkdir -p build/release

cd build/release && cmake -D STATIC=ON -D ARCH="x86-64" -D BUILD_64=ON -D CMAKE_BUILD_TYPE=release ../.. && make

-- The C compiler identification is GNU 5.4.0

-- The CXX compiler identification is GNU 5.4.0

-- Check for working C compiler: /usr/bin/cc

-- Check for working C compiler: /usr/bin/cc -- works

-- Detecting C compiler ABI info

-- Detecting C compiler ABI info - done

-- Detecting C compile features

-- Detecting C compile features - done

-- Check for working CXX compiler: /usr/bin/c++

-- Check for working CXX compiler: /usr/bin/c++ -- works

-- Detecting CXX compiler ABI info

-- Detecting CXX compiler ABI info - done

-- Detecting CXX compile features

-- Detecting CXX compile features - done

-- Building without build tag

-- Found Git: /usr/bin/git (found version "2.7.4") 

-- Checking submodules

fatal: Not a git repository: /src/bh25sshk9wzob5xrpxpjb6t/.git/modules/external/miniupnp

fatal: Not a git repository: /src/bh25sshk9wzob5xrpxpjb6t/.git/modules/external/unbound

fatal: Not a git repository: /src/bh25sshk9wzob5xrpxpjb6t/.git/modules/external/rapidjson

CMake Error at CMakeLists.txt:189 (message):
  Submodules not up to date.  Please update with git submodule init && git
  submodule update, or run cmake with -DMANUAL_SUBMODULES=1

-- Configuring incomplete, errors occurred!
See also "/src/build/release/CMakeFiles/CMakeOutput.log".

Makefile:89: recipe for target 'release-static' failed
```

I will dig into the Dockerfile today, but figured I would open an issue in case others are having the same problem, or already working on a fix.

# Discussion History
# Action History
- Created by: EmbeddedAndroid | 2018-10-13T16:34:35+00:00
- Closed at: 2018-10-15T11:33:12+00:00
