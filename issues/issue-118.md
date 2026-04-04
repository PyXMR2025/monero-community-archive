---
title: 'Build: OpenBSD dynamic build failing for Kovri '
source_url: https://github.com/monero-project/meta/issues/118
author: anonimal
assignees: []
labels:
- resolved
created_at: '2017-09-23T20:53:27+00:00'
updated_at: '2017-10-12T21:03:11+00:00'
type: issue
status: closed
closed_at: '2017-10-12T15:21:04+00:00'
---

# Original Description
```
CMake Error at /usr/local/share/cmake/Modules/CMakeDetermineCCompiler.cmake:57 (message):
  Could not find compiler set in environment variable CC:

  clang38.
Call Stack (most recent call first):
  CMakeLists.txt:8 (project)


CMake Error: CMAKE_C_COMPILER not set, after EnableLanguage
CMake Error: CMAKE_CXX_COMPILER not set, after EnableLanguage
-- Configuring incomplete, errors occurred!
```

https://build.getmonero.org/builders/kovri-all-openbsd-amd64/builds/247/steps/compile/logs/stdio

# Discussion History
## anonimal | 2017-10-06T18:44:01+00:00
@danrmiller I also still can't login to the machine. pings sent through IRC, not sure if you've ever received them.

## danrmiller | 2017-10-12T14:40:28+00:00
Previously this used a separate build job that set the speficic options the openbsd job needed, but eventually the BSD builds didn't need anything individual from each other so I set them all to use the same job. 

What I missed was on this machine clang 3.8.0 is at ```/usr/local/bin/clang-3.8``` while on the other BSDs we build for its at ```/usr/local/bin/clang38``` so I just symlinked it here.

There is a new address for you to connect to the openbsd testing machine, catch me on IRC.

## danrmiller | 2017-10-12T14:41:27+00:00
+resolved

https://build.getmonero.org/builders/kovri-all-openbsd-amd64/builds/288

## danrmiller | 2017-10-12T15:18:53+00:00
+resolved

## anonimal | 2017-10-12T21:03:11+00:00
Thanks @danrmiller 

# Action History
- Created by: anonimal | 2017-09-23T20:53:27+00:00
- Closed at: 2017-10-12T15:21:04+00:00
