---
title: 'Compile Error: Add pkg-config to dependencies #951'
source_url: https://github.com/monero-project/monero/issues/969
author: grummerd
assignees: []
labels: []
created_at: '2016-08-17T07:46:13+00:00'
updated_at: '2016-08-28T08:46:33+00:00'
type: issue
status: closed
closed_at: '2016-08-28T08:09:08+00:00'
---

# Original Description
i'm on ubuntu 16.04.02 LTS

> $ make -j 4

```
CMake Error at /usr/share/cmake-3.5/Modules/FindPackageHandleStandardArgs.cmake:148 (message):
  Could NOT find PkgConfig (missing: PKG_CONFIG_EXECUTABLE)
Call Stack (most recent call first):
  /usr/share/cmake-3.5/Modules/FindPackageHandleStandardArgs.cmake:388 (_FPHSA_FAILURE_MESSAGE)
  /usr/share/cmake-3.5/Modules/FindPkgConfig.cmake:52 (find_package_handle_standard_args)
  external/unbound/CMakeLists.txt:57 (find_package)
```

> dpkg -l | grep pkg-config

if returns nothing then

> sudo apt-get install pkg-config

Please add `pkg-config` as a dependency in readme.md docs


# Discussion History
## radfish | 2016-08-22T21:34:57+00:00
merged in #973 


## radfish | 2016-08-25T02:49:52+00:00
oh, this one is good to close, right?


## grummerd | 2016-08-28T08:09:08+00:00
This one has been closed for at least one week. pkg-config dependency is in bitmonero and [moneroexamples](https://github.com/moneroexamples/compile-monero-09-on-ubuntu-16-04) docs 

Is not in the kovri docs yet. But as far as bitmonero is concerned this issue is closed


## anonimal | 2016-08-28T08:46:33+00:00
Not required for kovri. Completely different project.


# Action History
- Created by: grummerd | 2016-08-17T07:46:13+00:00
- Closed at: 2016-08-28T08:09:08+00:00
