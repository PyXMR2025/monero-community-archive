---
title: Can't build v0.17.3.0
source_url: https://github.com/monero-project/monero/issues/8108
author: gituser
assignees: []
labels: []
created_at: '2021-12-07T22:44:29+00:00'
updated_at: '2021-12-07T22:47:12+00:00'
type: issue
status: closed
closed_at: '2021-12-07T22:47:11+00:00'
---

# Original Description
Getting an error regarding to `external/miniupnp`:

```
fatal: reference is not a tree: 544e6fcc73c5ad9af48a8985c94f0f1d742ef2e0
Unable to checkout '544e6fcc73c5ad9af48a8985c94f0f1d742ef2e0' in submodule path 'external/miniupnp'
fatal: reference is not a tree: 544e6fcc73c5ad9af48a8985c94f0f1d742ef2e0
Submodule path 'external/randomx': checked out '9efc398c196ef1c50d8e6f5e1f2c5ac02f1f6ceb'
Submodule path 'external/rapidjson': checked out '129d19ba7f496df5e33658527a7158c79b99c21c'
Submodule path 'external/supercop': checked out '633500ad8c8759995049ccd022107d1fa8a1bbc9'
Submodule path 'external/trezor-common': checked out 'bff7fdfe436c727982cc553bdfb29a9021b423b0'
Submodule path 'external/unbound': checked out '0f6c0579d66b65f86066e30e7876105ba2775ef4'
Unable to checkout '544e6fcc73c5ad9af48a8985c94f0f1d742ef2e0' in submodule path 'external/miniupnp'
```

and compilation fails:

```
-- Found PythonInterp: /usr/bin/python (found version "2.7.12") 
-- CMake version 3.19.3
-- The C compiler identification is GNU 5.4.0
-- The CXX compiler identification is GNU 5.4.0
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working C compiler: /usr/bin/gcc - skipped
-- Detecting C compile features
-- Detecting C compile features - done
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Check for working CXX compiler: /usr/bin/g++ - skipped
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Found usable ccache: /usr/bin/ccache
-- The ASM compiler identification is GNU
-- Found assembler: /usr/bin/gcc
-- Looking for -Wl,--no-undefined linker flag
-- Looking for -Wl,--no-undefined linker flag - found
-- Looking for -Wl,-undefined,error linker flag
-- Looking for -Wl,-undefined,error linker flag - found
-- Building build tag linux-x64
-- Found Git: /usr/bin/git (found version "2.7.4") 
-- Checking submodules
CMake Error at CMakeLists.txt:273 (message):
  Submodule 'external/miniupnp' is not up-to-date.  Please update all
  submodules with

  git submodule update --init --force

  or run cmake with -DMANUAL_SUBMODULES=1

Call Stack (most recent call first):
  CMakeLists.txt:278 (check_submodule)
```


```
$ git submodule status
+4c700e09526a7d546394e85628c57e9490feefa0 external/miniupnp (remotes/origin/monero)
 9efc398c196ef1c50d8e6f5e1f2c5ac02f1f6ceb external/randomx (v1.1.10-6-g9efc398)
 129d19ba7f496df5e33658527a7158c79b99c21c external/rapidjson (v1.1.0-401-g129d19b)
 633500ad8c8759995049ccd022107d1fa8a1bbc9 external/supercop (remotes/origin/monero)
 bff7fdfe436c727982cc553bdfb29a9021b423b0 external/trezor-common (heads/master-147-gbff7fdf)
 0f6c0579d66b65f86066e30e7876105ba2775ef4 external/unbound (heads/master-182-g0f6c057)
```

Any ideas how to fix this?

# Discussion History
## selsta | 2021-12-07T22:46:06+00:00
```
git submodule sync
git submodule update --init --force --recursive
```

## gituser | 2021-12-07T22:47:11+00:00
@selsta great thank you!

didn't know there is need to sync as well, now works fine.

# Action History
- Created by: gituser | 2021-12-07T22:44:29+00:00
- Closed at: 2021-12-07T22:47:11+00:00
