---
title: 'v0.18.4.0 FTBFS: Arch Linux'
source_url: https://github.com/monero-project/monero/issues/9932
author: Dormouse665
assignees: []
labels: []
created_at: '2025-05-22T02:29:36+00:00'
updated_at: '2025-09-08T17:24:09+00:00'
type: issue
status: closed
closed_at: '2025-09-08T17:23:57+00:00'
---

# Original Description
CMake 4.x.x doesn't like your project:

```
$ git clone <clone_url>
$ cd monero/build
$ git checkout v0.18.4.0
$ cmake ..
CMake Warning (dev) at CMakeLists.txt:40 (include):
  Policy CMP0148 is not set: The FindPythonInterp and FindPythonLibs modules
  are removed.  Run "cmake --help-policy CMP0148" for policy details.  Use
  the cmake_policy command to set the policy and suppress this warning.

This warning is for project developers.  Use -Wno-dev to suppress it.

-- Found PythonInterp: /usr/bin/python (found version "3.13.3")
CMake Deprecation Warning at CMakeLists.txt:46 (cmake_minimum_required):
  Compatibility with CMake < 3.10 will be removed from a future version of
  CMake.

  Update the VERSION argument <min> value.  Or, use the <min>...<max> syntax
  to tell CMake that the project requires at least <min> but has been updated
  to work with policies introduced by <max> or earlier.


-- CMake version 4.0.2-dirty
-- The C compiler identification is GNU 15.1.1
-- The CXX compiler identification is GNU 15.1.1
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working C compiler: /usr/bin/cc - skipped
-- Detecting C compile features
-- Detecting C compile features - done
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Check for working CXX compiler: /usr/bin/c++ - skipped
-- Detecting CXX compile features
-- Detecting CXX compile features - done
CMake Deprecation Warning at /home/dormouse/gits/monero/build/CMakeFiles/CMakeTmp/CMakeLists.txt:1 (cmake_minimum_required):
  Compatibility with CMake < 3.10 will be removed from a future version of
  CMake.

  Update the VERSION argument <min> value.  Or, use the <min>...<max> syntax
  to tell CMake that the project requires at least <min> but has been updated
  to work with policies introduced by <max> or earlier.


-- Found usable ccache: /usr/bin/ccache
-- The ASM compiler identification is GNU
-- Found assembler: /usr/bin/cc
-- Looking for -Wl,--no-undefined linker flag
-- Looking for -Wl,--no-undefined linker flag - found
-- Looking for -Wl,-undefined,error linker flag
-- Looking for -Wl,-undefined,error linker flag - found
CMake Error at /home/dormouse/gits/monero/build/CMakeFiles/CMakeTmp/test_project/CMakeLists.txt:1 (cmake_minimum_required):
  Compatibility with CMake < 3.5 has been removed from CMake.

  Update the VERSION argument <min> value.  Or, use the <min>...<max> syntax
  to tell CMake that the project requires at least <min> but has been updated
  to work with policies introduced by <max> or earlier.

  Or, add -DCMAKE_POLICY_VERSION_MINIMUM=3.5 to try configuring anyway.


CMake Error at CMakeLists.txt:235 (try_compile):
  Failed to configure test project build system.
Call Stack (most recent call first):
  CMakeLists.txt:248 (forbid_undefined_symbols)


-- Configuring incomplete, errors occurred!
```

# Discussion History
## SyntheticBird45 | 2025-05-26T22:35:19+00:00
Weird, Arch CI build it successfully tho: https://github.com/monero-project/monero/actions/runs/15240535234/job/42860042197?pr=9936

## Dormouse665 | 2025-05-26T22:52:27+00:00
From CI log:
```
-- Looking for -Wl,--no-undefined linker flag - found
-- Looking for -Wl,-undefined,error linker flag
-- Looking for -Wl,-undefined,error linker flag - found
CMake Deprecation Warning at /__w/monero/monero/build/CMakeFiles/CMakeTmp/test_project/CMakeLists.txt:1 (cmake_minimum_required):
  Compatibility with CMake < 3.10 will be removed from a future version of
  CMake.

  Update the VERSION argument <min> value.  Or, use the <min>...<max> syntax
  to tell CMake that the project requires at least <min> but has been updated
  to work with policies introduced by <max> or earlier.


CMake Deprecation Warning at /__w/monero/monero/build/CMakeFiles/CMakeTmp/test_project/CMakeLists.txt:1 (cmake_minimum_required):
  Compatibility with CMake < 3.10 will be removed from a future version of
  CMake.

  Update the VERSION argument <min> value.  Or, use the <min>...<max> syntax
  to tell CMake that the project requires at least <min> but has been updated
  to work with policies introduced by <max> or earlier.


-- Building without build tag
-- Found Git: /usr/sbin/git (found version "2.49.0")
-- Checking submodules
```
For some reason it seems that the CI is only getting
deprecation warning for supporting CMake < 3.10,
while I get an error for supporting CMake < 3.5.


```
$ git branch
* (HEAD detached at v0.18.4.0)
$ git submodule deinit --all
$ git clean -fxd
$ git submodule init
$ git submodule update --recursive
$ cd build
$ cmake ..
```
Is how I reproduce this.

## nahuhh | 2025-05-26T23:55:19+00:00
https://github.com/monero-project/monero/commit/0d0a656618e396de7ff60368dde708ad9d45f866

fixed on release branch already

## Dormouse665 | 2025-05-27T01:11:59+00:00
This fixes my error, but it doesn't fix the deprecation warning.

Should I make a PR with requirement bumped to 3.10?

## selsta | 2025-06-01T17:34:19+00:00
I'm not sure it's worth upgrading the min required version just to fix a warning.

## Dormouse665 | 2025-06-02T04:31:52+00:00
The warning is going to become an error one day and then I will be back reporting this again.

## Dormouse665 | 2025-06-06T19:07:13+00:00
I tried fixing this in CMakeLists.txt in the root.
It makes the build run, but there are still warnings present.

I edited both minimum versions, one for the file itself, one that is used
to generate some other.

I have tried 3.10 (modification of your current version to minimum required for
cmake to shuddup) and 3.31.0 (Which is probably the version present on Arch last time
I have decided to bump the version in my AI project.)

I am not able to solve this one on what limited time I currently have for open source development:
```
CMake Deprecation Warning at /home/dormouse/gits/monero/build/CMakeFiles/CMakeTmp/CMakeLists.txt:1 (cmake_minimum_required):
  Compatibility with CMake < 3.10 will be removed from a future version of
  CMake.

  Update the VERSION argument <min> value.  Or, use the <min>...<max> syntax
  to tell CMake that the project requires at least <min> but has been updated
  to work with policies introduced by <max> or earlier.
```

I am also ignoring ones from external projects, about which I encourage
you to reach out to developers of.

If any dev is willing to walk me through how you handle CMake stuff,
I could help maintaining it so that Monero can avoid such build
fails in the future.

## selsta | 2025-09-08T17:23:57+00:00
I'm closing this as the original issue itself was solved, the only issue remaining is the warning. I will consider updating min CMake to 3.10, as Ubuntu 18.04 is the lowest we support currently and it ships with 3.10.

# Action History
- Created by: Dormouse665 | 2025-05-22T02:29:36+00:00
- Closed at: 2025-09-08T17:23:57+00:00
